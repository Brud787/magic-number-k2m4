"""Independent affine, basis-incidence, transport and exact-rank certificates."""

import json
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path

from magic_number import affine
from magic_number.run6_local_span import build_local_matrix, tile_inventory


@lru_cache(maxsize=None)
def read(relative):
    return json.loads(Path(relative).read_text())


def test_complete_942_tile_inventory_and_source_certificates():
    data = tile_inventory()
    source = read("results/run2/child_status_n9.json")
    independently_enumerated = set(affine.windows(9, 2, 8))
    assert independently_enumerated == {tuple(row["affine_permutation"]) for row in source["cells"]}
    assert len(independently_enumerated) == 1554
    certified = {tuple(row["affine_permutation"]): row for row in source["cells"]
                 if row["admissibility"]["status"] == "CERTIFIED_TILE"}
    assert set(data["column_affine_permutations"]) == set(certified)
    assert data["tile_kind_counts"] == {"BCFW": 939, "NON_BCFW_SPURION": 3}
    assert data["support_size_counts"] == {6: 84, 7: 504, 8: 324, 9: 30}
    assert Counter(row["admissibility"]["status"] for row in source["cells"]) == {
        "CERTIFIED_TILE": 942, "CERTIFIED_NON_TILE": 612}
    for row in data["tiles"]:
        window = row["affine"]
        assert row["admissibility"] == certified[window]["admissibility"]
        assert row["bases"] == affine.bases(window)
        assert row["necklace"] == affine.necklace(window)
        assert affine.dimension(window) == row["dimension"] == 8
        support = set().union(*map(set, row["bases"]))
        assert support == set(row["support"])
        assert set(row["loops"]) == set(range(1, 10)) - support
        eligible = [i for i, block in enumerate(row["classes"]) if len(support - set(block)) == 5]
        assert eligible == row["complement_five"]["qualifying_class_indices"]
        assert bool(eligible) == (row["tile_kind"] == "BCFW")
    assert json.loads(json.dumps(data)) == read("results/run6/tile_universe_n9.json")


def test_complete_dihedral_orbits_by_independent_basis_maps():
    data = tile_inventory()
    tiles = data["tiles"]
    by_bases = {frozenset(tile["bases"]): tile["column"] for tile in tiles}
    covered = []
    assert data["dihedral_orbit_count"] == 61
    assert Counter(orbit["size"] for orbit in data["dihedral_orbits"]) == {3: 2, 9: 14, 18: 45}
    for orbit in data["dihedral_orbits"]:
        representative_bases = affine.bases(orbit["representative_affine"])
        expected = set()
        for direction in (-1, 1):
            for shift in range(9):
                mapping = {i: (direction*(i-1)+shift) % 9 + 1 for i in range(1, 10)}
                image = frozenset(tuple(sorted((mapping[i], mapping[j]))) for i, j in representative_bases)
                column = by_bases[image]
                expected.add(column)
                assert {"direction": direction, "shift": shift} in tiles[column]["dihedral_orbit"]["representative_to_tile_actions"]
        assert expected == set(orbit["member_columns"])
        covered.extend(expected)
    assert sorted(covered) == list(range(942))


def test_all_882_parents_and_every_admissible_facet_by_full_basis_inclusion():
    data = build_local_matrix()
    assert {row["affine"] for row in data["parents"]} == set(affine.windows(9, 2, 9))
    assert data["source_parent_count"] == 882
    assert data["parent_sector_counts"] == {"BALANCED": 693, "COLLAPSED": 108, "HOSTILE_ZERO_KERNEL": 81}
    bits = {pair: 1 << i for i, pair in enumerate(combinations(range(1, 10), 2))}
    masks = {window: sum(bits[pair] for pair in affine.bases(window))
             for window in data["column_affine_permutations"]}
    for parent in data["parents"]:
        parent_mask = sum(bits[pair] for pair in affine.bases(parent["affine"]))
        expected = {window for window, mask in masks.items() if mask != parent_mask and mask & parent_mask == mask}
        assert expected == set(parent["admissible_facets"])
        assert affine.dimension(parent["affine"]) == 9
        assert len(parent["relation_rows"]) == (parent["sector"] == "BALANCED")
        if parent["relation_rows"]:
            row = data["rows"][parent["relation_rows"][0]]
            assert {window for window, value in zip(data["column_affine_permutations"], row) if value} == expected
    assert data["relation_support_size_counts"] == {7: 252, 8: 360, 9: 81}
    assert data["relation_term_count_histogram"] == {6: 594, 10: 99}
    assert data["participating_tile_count"] == 942


def test_all_693_geometric_rows_by_independent_prototype_basis_transport():
    data = build_local_matrix()
    prototypes = {row["id"]: row for row in read("results/run4/sign_relations.json")["relations"]}
    column_by_bases = {frozenset(affine.bases(window)): j for j, window in enumerate(data["column_affine_permutations"])}
    assert len(data["relations"]) == len(data["rows"]) == 693
    assert len(set(data["rows"])) == 693
    assert sum(len(row["transport_origins"]) for row in data["relations"]) == 1044
    for relation in data["relations"]:
        assert len(relation["parent_affines"]) == 1
        expected = data["rows"][relation["row_index"]]
        assert sum(expected) == relation["coefficient_sum"] == 0
        assert set(expected) == {-1, 0, 1}
        assert next(value for value in expected if value) == 1
        for origin in relation["transport_origins"]:
            prototype = prototypes[origin["source_relation"]]
            q, direction, shift = origin["core_n"], origin["dihedral_direction"], origin["dihedral_shift"]
            mapping = {i: origin["increasing_support"][(direction*(i-1)+shift) % q]
                       for i in range(1, q+1)}
            actual = [0]*942
            for wall in prototype["signed_admissible_facets"]:
                image = frozenset(tuple(sorted((mapping[i], mapping[j]))) for i, j in wall["bases"])
                actual[column_by_bases[image]] += origin["common_sign"]*wall["coefficient"]
            assert tuple(actual) == expected
            parent_bases = frozenset(tuple(sorted((mapping[i], mapping[j])))
                                     for i, j in affine.bases(tuple(prototype["parent_affine"])))
            assert parent_bases == frozenset(affine.bases(origin["parent_affine"]))


def _fraction_determinant(matrix):
    """Independent sparse rational Gaussian elimination, without SymPy."""
    work = [{j: Fraction(value) for j, value in enumerate(row) if value} for row in matrix]
    answer = Fraction(1)
    for k in range(len(work)):
        pivot = next((i for i in range(k, len(work)) if work[i].get(k)), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            work[k], work[pivot] = work[pivot], work[k]
            answer = -answer
        coefficient = work[k][k]
        answer *= coefficient
        for i in range(k+1, len(work)):
            value = work[i].pop(k, Fraction(0))
            if value:
                for j, entry in work[k].items():
                    if j == k:
                        continue
                    reduced = work[i].get(j, Fraction(0)) - value*entry/coefficient
                    if reduced:
                        work[i][j] = reduced
                    else:
                        work[i].pop(j, None)
    return answer


def test_exact_rank_upper_factorization_and_independent_determinant_minus_one():
    data = build_local_matrix()
    assert data["rank_over_Q"] == 470 and data["quotient_dimension"] == 472
    pivots = data["pivot_columns"]
    basis = [{j: Fraction(value) for j, value in row} for row in data["rref_nonzero_rows"]]
    assert len(basis) == len(pivots) == len(data["independent_row_indices"]) == 470
    for i, row in enumerate(basis):
        assert all(row.get(p, Fraction(0)) == int(i == j) for j, p in enumerate(pivots))
    # Explicit M = M[:, pivots] * RREF_nonzero establishes the rank upper bound.
    for row in data["rows"]:
        reconstructed = {}
        for coefficient, reduced in zip((row[p] for p in pivots), basis):
            if coefficient:
                for j, value in reduced.items():
                    reconstructed[j] = reconstructed.get(j, Fraction(0)) + coefficient*value
        assert {j: value for j, value in reconstructed.items() if value} == {j: Fraction(value) for j, value in enumerate(row) if value}
    minor = [[data["rows"][i][j] for j in pivots] for i in data["independent_row_indices"]]
    determinant = _fraction_determinant(minor)
    assert determinant == -1 == Fraction(data["rank_certificate"]["minor_determinant_exact"])
    assert int(determinant) % data["rank_certificate"]["minor_modulus"] == data["rank_certificate"]["minor_determinant_residue"]
    assert json.loads(json.dumps(data)) == read("results/run6/local_relation_matrix_n9.json")


def test_loopless_support_block_has_one_signed_quotient_class():
    data = read("results/run6/support_blocks.json")
    local, inventory = build_local_matrix(), tile_inventory()
    columns = [tile["column"] for tile in inventory["tiles"] if len(tile["support"]) == 9]
    assert columns == data["loopless_tile_columns"] and len(columns) == 30
    projected = [[row[j] for j in columns] for row in local["rows"]]
    assert projected == data["projected_rows"]
    weight = [1 if tile["tile_kind"] == "BCFW" else -1 for tile in inventory["tiles"] if len(tile["support"]) == 9]
    assert Counter(weight) == {1: 27, -1: 3}
    assert all(sum(a*b for a, b in zip(row, weight)) == 0 for row in projected)
    minor = [[projected[i][j] for j in data["projected_minor_columns_in_loopless_block"]]
             for i in data["projected_minor_row_indices"]]
    assert len(minor) == 29 and _fraction_determinant(minor) == -1
    assert data["support_at_most_eight_image_dimension_in_local_quotient"] == 912-(470-29) == 471
    assert data["new_loopless_quotient_dimension"] == 30-29 == 1
    assert Counter(sum(row) for row in projected) == {0: 675, -2: 10, 2: 8}
    ambient = data["ambient_covector"]
    assert ambient == [weight[columns.index(j)] if j in columns else 0 for j in range(942)]
    assert sum(ambient[j] for j in data["standard_base_columns"]) == data["standard_base_weight"] == 2
