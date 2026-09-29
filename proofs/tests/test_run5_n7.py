"""Independent finite completeness and actual geometric-flip bookkeeping."""

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path

from sympy import Matrix

from magic_number import affine
from magic_number.rank2 import cells, necklace_from_bases, affine_from_necklace
from magic_number.run5_n7 import (
    LABELS, SUPPORTS, build_n7_artifact, compatibility_data,
    gale_overlap_witness, gale_weights, independent_overlap_lp,
    in_parity_bound, maximal_cliques_bron_kerbosch,
    maximal_cliques_independent, moment_matrix, parity_window,
    positive_intersection_certificate, tile_dictionary,
)
from magic_number.run5_local_span import build_local_matrix


def test_complete_source_and_dual_simplex_dictionary_independent_encodings():
    rank_two = {cell.affine for cell in cells(7, 8)}
    independent = set(affine.windows(7, 2, target_dimension=8))
    assert rank_two == independent and len(rank_two) == 28
    expected = {window for window in independent if in_parity_bound(window, 1)}
    assert len(expected) == 21
    dictionary = tile_dictionary()
    assert {row['affine'] for row in dictionary} == expected
    assert {row['simplex_support'] for row in dictionary} == set(SUPPORTS)
    for row in dictionary:
        bases = tuple((i,) for i in row['simplex_support'])
        # Construct the rank-one affine index from its bases independently of
        # affine inversion, then round-trip the actual GL shift convention.
        dual = affine_from_necklace(necklace_from_bases(7, bases))
        assert dual == row['dual_rank_one_affine']
        assert parity_window(dual, 2) == row['affine']


def test_gale_kernel_and_external_total_positivity_exact():
    z = moment_matrix()
    assert all(z[[i - 1 for i in support], :].det() > 0 for support in SUPPORTS)
    weights = gale_weights()
    g = Matrix([[weights[i], i * weights[i]] for i in LABELS])
    assert g.rank() == 2 and z.T * g == Matrix.zeros(5, 2)
    # General-position Gale rows are pairwise independent. This also verifies
    # the exact LP's pointed-polyhedron hypothesis for every union-seven pair.
    assert all(g[list(pair), :].det() != 0 for pair in combinations(range(7), 2))


def test_every_pair_overlap_decision_has_independent_exact_feasibility_check():
    for left, right in combinations(SUPPORTS, 2):
        assert (gale_overlap_witness(left, right) is None) == (
            independent_overlap_lp(left, right) is None)


def test_every_overlap_has_positive_normalized_equal_image_certificate():
    z = moment_matrix()
    overlap_count = 0
    for left, right in combinations(SUPPORTS, 2):
        witness = gale_overlap_witness(left, right)
        if witness is None:
            continue
        overlap_count += 1
        certificate = positive_intersection_certificate(left, right, witness)
        a, b = certificate['left_coefficients'], certificate['right_coefficients']
        assert all(value > 0 for value in a + b)
        assert sum(a) == sum(b) == 1
        assert Matrix([a]) * z[[i - 1 for i in left], :] == (
            Matrix([b]) * z[[i - 1 for i in right], :])
    assert overlap_count == 126


def test_two_independent_exhaustive_clique_algorithms_have_no_omitted_collections():
    adjacency, _ = compatibility_data()
    first = maximal_cliques_bron_kerbosch(adjacency)
    second, histogram = maximal_cliques_independent(adjacency)
    assert first == second and len(first) == 7
    assert histogram == {0: 1, 1: 21, 2: 84, 3: 133, 4: 105, 5: 42, 6: 7}
    assert all(len(clique) == 6 for clique in first)


def test_complete_cliques_match_all_z_bcfw_collections_and_actual_c7_flips():
    data = build_n7_artifact()
    tilings = {row['id']: frozenset(map(tuple, row['affine_cells']))
               for row in data['complete_tilings']}
    assert len(tilings) == 7 and {len(collection) for collection in tilings.values()} == {6}
    local = build_local_matrix(7)
    row_by_id = {record['id']: row for record, row in zip(local['relations'], local['rows'])}
    columns = local['column_affine_permutations']
    used_relations = set()
    for edge in data['genuine_local_flip_graph']['edges']:
        left, right = map(tilings.__getitem__, edge['tilings'])
        assert len(left - right) == len(right - left) == 3
        difference = tuple(int(window in left) - int(window in right) for window in columns)
        assert len(edge['local_relation_ids']) == 1
        rid = edge['local_relation_ids'][0]
        used_relations.add(rid)
        row = tuple(row_by_id[rid])
        assert difference in (row, tuple(-value for value in row))
    assert used_relations == set(row_by_id)
    graph = data['genuine_local_flip_graph']
    assert graph['connected'] and len(graph['edges']) == 7
    assert set(graph['degree_by_vertex'].values()) == {2}


def test_complete_tiling_difference_space_equals_full_local_parent_space():
    data = build_n7_artifact()
    linear = data['linear_algebra']
    local = Matrix(build_local_matrix(7)['rows'])
    complete = Matrix(linear['all_pair_tiling_differences'])
    assert complete.rows == 21
    assert complete.rank() == local.rank() == local.col_join(complete).rank() == 6
    assert all(sum(row) == 0 for row in linear['all_pair_tiling_differences'])
    assert linear['D7_equals_L7'] and linear['free_tile_space_mod_local_relations_dimension'] == 15


def test_saved_n7_certificate_reproduces_and_contains_all_pair_records():
    saved = json.loads(Path('results/run5/tilings_n7.json').read_text())
    rebuilt = json.loads(json.dumps(build_n7_artifact(), default=int))
    assert saved == rebuilt
    assert len(saved['pair_certificates']) == 210
    for row in saved['pair_certificates']:
        if not row['open_interiors_disjoint']:
            assert sum(map(Fraction, row['left_coefficients'])) == 1
            assert sum(map(Fraction, row['right_coefficients'])) == 1
