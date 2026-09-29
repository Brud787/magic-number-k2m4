"""Complete n=7 all-Z tilings via parity and one exact cyclic-polytope test.

The fixed moment-curve test is used only for exclusion. Existence for every Z
comes from matching each maximal compatible collection to a preserved BCFW
tiling. The proof and exact conventions are in research/run5/N7_PROOF.md.
"""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import prod
from pathlib import Path

from sympy import Matrix

from . import affine
from .certified_relations import standard_dihedral_orbit
from .exact_geometry import matrix_rank
from .rank2 import cells
from .run5_local_span import build_local_matrix


LABELS = tuple(range(1, 8))
SUPPORTS = tuple(combinations(LABELS, 5))
ROOT = Path(__file__).resolve().parents[2]


def parity_window(window, dual_rank):
    """GL's output shift: bounded b=k+f is sent to ell+f^{-1}."""
    window = tuple(window)
    n, k = len(window), affine.rank(window)
    f = tuple(value - k for value in window)
    inverse = []
    for target in range(1, n + 1):
        j = next(j for j in range(1, n + 1) if (f[j - 1] - target) % n == 0)
        inverse.append(j + target - f[j - 1] + dual_rank)
    result = tuple(inverse)
    affine.validate(result)
    if affine.rank(result) != dual_rank:
        raise ValueError("Parity window has the wrong rank")
    return result


def in_parity_bound(window, dual_rank):
    k = affine.rank(window)
    return all(i - k <= value - k <= i + dual_rank
               for i, value in enumerate(window, 1))


@lru_cache(maxsize=1)
def tile_dictionary():
    """Every possible n7 tile, by exact GL bound and inverse simplex support."""
    result = []
    known_cells = {window for tiling in standard_dihedral_orbit(7)
                   for window in tiling['cells']}
    for cell in sorted(cells(7, 8), key=lambda item: item.affine):
        if not in_parity_bound(cell.affine, 1):
            continue
        dual = parity_window(cell.affine, 1)
        support = tuple(basis[0] for basis in affine.bases(dual))
        assert affine.dimension(dual) == 4 and len(support) == 5
        assert parity_window(dual, 2) == cell.affine
        assert cell.affine in known_cells
        result.append({'affine': cell.affine, 'classes': cell.classes,
                       'dual_rank_one_affine': dual, 'simplex_support': support,
                       'admissibility': 'CERTIFIED_TILE',
                       'proof': 'GL Theorem 3.5(1), rank-one simplex injectivity; also BCFW'})
    assert len(result) == 21 and {r['simplex_support'] for r in result} == set(SUPPORTS)
    return tuple(result)


def moment_matrix():
    return Matrix([[i ** exponent for exponent in range(5)] for i in LABELS])


def gale_weights():
    return {i: Fraction(1, prod(i - j for j in LABELS if j != i)) for i in LABELS}


def _exclusive_signs(left, right):
    a, b = set(left), set(right)
    return {i: (1 if i in a else -1) for i in sorted(a ^ b)}


def gale_overlap_witness(left, right):
    """Exact Gale formula, returning (a,b) when lambda_i(a+b*i) works.

    None is an exact infeasibility conclusion, not a failed sample search.
    Supports must be distinct five-subsets of [7].
    """
    left, right = tuple(left), tuple(right)
    if left == right or left not in SUPPORTS or right not in SUPPORTS:
        raise ValueError('Expected distinct five-subsets of [7]')
    weights = gale_weights()
    signs = {i: sign * (1 if weights[i] > 0 else -1)
             for i, sign in _exclusive_signs(left, right).items()}
    outside = sorted(set(LABELS) - set(left) - set(right))
    if outside:
        assert len(outside) == 1
        root = outside[0]
        factors = [sign * (1 if i > root else -1) for i, sign in signs.items()]
        if len(set(factors)) != 1:
            return None
        slope = factors[0]
        return Fraction(-slope * root), Fraction(slope)
    items = list(signs.items())
    changes = [j for j in range(len(items) - 1) if items[j][1] != items[j + 1][1]]
    if len(changes) > 1:
        return None
    if not changes:
        return Fraction(items[0][1]), Fraction(0)
    j = changes[0]
    root = Fraction(items[j][0] + items[j + 1][0], 2)
    slope = items[j + 1][1]
    return -slope * root, Fraction(slope)


@lru_cache(maxsize=1)
def independent_gale_basis():
    """Gaussian elimination of the actual 5x7 matrix, without Gale formula."""
    vectors = moment_matrix().T.nullspace()
    assert len(vectors) == 2
    return Matrix.hstack(*vectors)


def independent_overlap_lp(left, right):
    """Independent rational feasibility by vertices of a two-variable LP.

    Required strict forms may be rescaled to >=1. With one outside label,
    the equality reduces to a line. Otherwise distinct Gale rows give a
    pointed two-dimensional polyhedron; a nonempty one has a vertex.
    """
    kernel = independent_gale_basis()
    exclusive = _exclusive_signs(left, right)
    outside = sorted(set(LABELS) - set(left) - set(right))
    if outside:
        directions = kernel[outside[0] - 1, :].nullspace()
        assert len(directions) == 1
        direction = directions[0]
        slopes = [sign * (kernel[i - 1, :] * direction)[0]
                  for i, sign in exclusive.items()]
        if any(value == 0 for value in slopes):
            return None
        parameter = 1 / slopes[0]
        candidate = parameter * direction
        if all(sign * (kernel[i - 1, :] * candidate)[0] > 0
               for i, sign in exclusive.items()):
            return tuple(candidate)
        return None
    constraints = [sign * kernel[i - 1, :] for i, sign in exclusive.items()]
    for first, second in combinations(constraints, 2):
        active = first.col_join(second)
        if not active.det():
            continue
        candidate = active.inv() * Matrix([1, 1])
        if all((row * candidate)[0] >= 1 for row in constraints):
            return tuple(candidate)
    return None


def positive_intersection_certificate(left, right, witness):
    """Positive normalized barycentric coordinates, independently checkable."""
    a, b = witness
    w = {i: value * (a + b * i) for i, value in gale_weights().items()}
    common = set(left) & set(right)
    first, second = {}, {}
    for i in LABELS:
        if i in common:
            first[i] = max(w[i], 0) + 1
            second[i] = max(-w[i], 0) + 1
        elif i in left:
            first[i] = w[i]
        elif i in right:
            second[i] = -w[i]
    scale = sum(first.values())
    assert scale == sum(second.values())
    assert all(value > 0 for value in list(first.values()) + list(second.values()))
    return {"left_coefficients": tuple(first[i] / scale for i in left),
            "right_coefficients": tuple(second[i] / scale for i in right)}


@lru_cache(maxsize=1)
def compatibility_data():
    adjacency = [set() for _ in SUPPORTS]
    pairs = []
    for i, j in combinations(range(len(SUPPORTS)), 2):
        left, right = SUPPORTS[i], SUPPORTS[j]
        witness = gale_overlap_witness(left, right)
        independent = independent_overlap_lp(left, right)
        assert (witness is None) == (independent is None)
        record = {'vertices': (i, j), 'simplex_supports': (left, right),
                  'open_interiors_disjoint': witness is None,
                  'independent_exact_LP_agrees': True}
        if witness is None:
            adjacency[i].add(j)
            adjacency[j].add(i)
        else:
            certificate = positive_intersection_certificate(left, right, witness)
            record.update({'gale_affine_coefficients': tuple(map(str, witness)),
                           'independent_kernel_parameters': tuple(map(str, independent)),
                           **{key: tuple(map(str, values)) for key, values in certificate.items()}})
        pairs.append(record)
    return tuple(frozenset(neighbors) for neighbors in adjacency), pairs


def maximal_cliques_bron_kerbosch(adjacency):
    result = []

    def visit(chosen, possible, excluded):
        if not possible and not excluded:
            result.append(tuple(sorted(chosen)))
            return
        pivot = max(possible | excluded, key=lambda vertex: len(possible & adjacency[vertex]))
        for vertex in sorted(possible - adjacency[pivot]):
            visit(chosen | {vertex}, possible & adjacency[vertex], excluded & adjacency[vertex])
            possible.remove(vertex)
            excluded.add(vertex)

    visit(set(), set(range(len(adjacency))), set())
    return tuple(sorted(result))


def maximal_cliques_independent(adjacency):
    """Enumerate every clique by increasing extension, then test maximality.

    Unlike Bron--Kerbosch, this does not prune nonmaximal clique branches.
    The saved size histogram certifies the complete finite search space.
    """
    all_cliques = [()]
    frontier = [()]
    while frontier:
        extended = []
        for clique in frontier:
            for vertex in range(clique[-1] + 1 if clique else 0, len(adjacency)):
                if all(vertex in adjacency[member] for member in clique):
                    extended.append(clique + (vertex,))
        all_cliques.extend(extended)
        frontier = extended
    maximal = []
    for clique in all_cliques:
        if not any(vertex not in clique and all(vertex in adjacency[member] for member in clique)
                   for vertex in range(len(adjacency))):
            maximal.append(clique)
    return tuple(sorted(maximal)), dict(sorted(Counter(map(len, all_cliques)).items()))


def build_n7_artifact():
    dictionary = tile_dictionary()
    support_to_affine = {row['simplex_support']: row['affine'] for row in dictionary}
    adjacency, pair_records = compatibility_data()
    cliques = maximal_cliques_bron_kerbosch(adjacency)
    independent, histogram = maximal_cliques_independent(adjacency)
    assert cliques == independent and len(cliques) == 7
    known = {tiling['cells']: tiling for tiling in standard_dihedral_orbit(7)}
    tilings = []
    for i, clique in enumerate(cliques):
        collection = tuple(sorted(support_to_affine[SUPPORTS[j]] for j in clique))
        source = known[collection]
        tilings.append({'id': f'n7-C{i:02d}', 'simplex_vertex_indices': clique,
                        'simplex_supports': tuple(SUPPORTS[j] for j in clique),
                        'affine_cells': collection, 'tile_count': len(collection),
                        'known_BCFW_tiling_id': source['id'],
                        'BCFW_dihedral_actions': source['actions'],
                        'existence_scope': 'ALL_Z_SOURCE_VERIFIED_BCFW',
                        'completeness_scope': 'ALL_Z_BY_PARITY_AND_EXACT_FIXED_MATRIX_EXCLUSION'})
    assert {row['affine_cells'] for row in tilings} == set(known)
    local = build_local_matrix(7)
    columns = tuple(local['column_affine_permutations'])
    rows = local['rows']
    assert columns == tuple(row['affine'] for row in dictionary)
    collection_to_id = {frozenset(row['affine_cells']): row['id'] for row in tilings}
    edges = {}
    for tiling in tilings:
        collection = frozenset(tiling['affine_cells'])
        for relation, vector in zip(local['relations'], rows):
            positive = frozenset(columns[j] for j, c in enumerate(vector) if c == 1)
            negative = frozenset(columns[j] for j, c in enumerate(vector) if c == -1)
            assert len(positive) == len(negative) == 3
            for remove, insert in ((positive, negative), (negative, positive)):
                if remove <= collection and not insert & collection:
                    target = (collection - remove) | insert
                    assert target in collection_to_id
                    edge = tuple(sorted((tiling['id'], collection_to_id[target])))
                    edges.setdefault(edge, []).append(relation['id'])
    edge_records = [{'tilings': edge, 'local_relation_ids': sorted(set(relations)),
                     'replacement_size': (3, 3),
                     'geometric_certification': 'RUN4_ALL_Z_MULTIPLICITY_ONE_PARENT_FLIP'}
                    for edge, relations in sorted(edges.items())]
    degree = Counter(vertex for edge in edges for vertex in edge)
    reached = {tilings[0]['id']}
    while True:
        expanded = reached | {b for a, b in edges if a in reached} | {a for a, b in edges if b in reached}
        if expanded == reached:
            break
        reached = expanded
    differences = []
    for left, right in combinations(tilings, 2):
        a, b = set(left['affine_cells']), set(right['affine_cells'])
        differences.append([int(window in a) - int(window in b) for window in columns])
    d_rank, l_rank = matrix_rank(differences), matrix_rank(rows)
    stacked_rank = matrix_rank(list(rows) + differences)
    assert d_rank == Matrix(differences).rank() == l_rank == stacked_rank == 6
    assert len(edges) == 7 and set(degree.values()) == {2} and len(reached) == 7
    return {'n': 7, 'k': 2, 'm': 4,
            'claim_tag': 'PROVED',
            'certificate_type': 'EXACT_EXHAUSTIVE_FINITE_CERTIFICATE',
            'proof_reference': 'research/run5/N7_PROOF.md',
            'prior_art_scope': 'Finite explicit reconstruction of known parity/cyclic-polytope behavior; no novelty claim',
            'source_cell_count': len(list(cells(7, 8))), 'admissible_tile_count': len(dictionary),
            'excluded_source_affines': [cell.affine for cell in cells(7, 8)
                                         if not in_parity_bound(cell.affine, 1)],
            'tiles': dictionary, 'cyclic_polytope_simplex_order': SUPPORTS,
            'fixed_exclusion_matrix_rows': moment_matrix().tolist(),
            'pair_count': len(pair_records), 'compatibility_edge_count': sum(map(len, adjacency)) // 2,
            'pair_certificates': pair_records,
            'maximal_clique_algorithms_agree': True, 'all_clique_size_histogram': histogram,
            'all_Z_complete_tiling_count': len(tilings), 'complete_tilings': tilings,
            'genuine_local_flip_graph': {'vertices': [row['id'] for row in tilings],
                                         'edges': edge_records, 'degree_by_vertex': dict(sorted(degree.items())),
                                         'connected': len(reached) == len(tilings), 'graph_type': 'C7'},
            'linear_algebra': {'column_affine_permutations': columns,
                              'all_pair_tiling_differences': differences,
                              'D7_rank_over_Q': d_rank, 'L7_rank_over_Q': l_rank,
                              'stacked_rank_over_Q': stacked_rank, 'D7_equals_L7': True,
                              'free_tile_space_mod_local_relations_dimension': len(columns) - l_rank,
                              'local_matrix_reference': 'results/run5/local_relation_matrix_n7.json',
                              'scope': 'D7 is the complete all-Z tiling-difference space; L7 is the full Run4 single-parent span. No assertion about every abstract indicator relation.'}}


def _json_default(value):
    if getattr(value, 'is_Integer', False):
        return int(value)
    raise TypeError(f'Cannot encode {type(value).__name__}')


def main():
    data = build_n7_artifact()
    destination = ROOT / 'results/run5/tilings_n7.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(data, indent=2, default=_json_default) + '\n')
    print(json.dumps({key: data[key] for key in ('admissible_tile_count', 'compatibility_edge_count',
                                               'all_Z_complete_tiling_count', 'all_clique_size_histogram')}))


if __name__ == '__main__':
    main()
