"""Source-chain kill-test, with geometric and formal chain objects separated.

At n=8 the geometric local rows do not lie in the ordinary source boundary
kernel. Removing all lower strata below nonadmissible eight-cells restores
a formal mod-2 complex, but leaves spurious unit cycles and H8 dimension 15.
"""

from __future__ import annotations

import json
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path

from sympy import Matrix

from .rank2 import cells, facets
from .run5_local_span import build_local_matrix
from .run5_n7 import tile_dictionary


ROOT = Path(__file__).resolve().parents[2]


def gf2_rank_bitsets(vectors):
    pivots = {}
    for vector in vectors:
        value = int(vector)
        while value:
            pivot = value.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = value
                break
            value ^= pivots[pivot]
    return len(pivots)


def gf2_rank_dense(vectors, width):
    """Independent ordinary row elimination, ascending columns, mod two."""
    rows = [[(int(value) >> j) & 1 for j in range(width)] for value in vectors]
    pivot_row = 0
    for column in range(width):
        pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        for i in range(pivot_row + 1, len(rows)):
            if rows[i][column]:
                rows[i] = [(a + b) % 2 for a, b in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def support_indices(mask):
    return tuple(i for i in range(mask.bit_length()) if (mask >> i) & 1)


def _cell_record(cell):
    return {'affine': cell.affine, 'classes': cell.classes, 'dimension': cell.dimension,
            'bases': cell.bases, 'necklace': cell.necklace}


def _xor_columns(columns, support):
    result = 0
    for index in support:
        result ^= columns[index]
    return result


@lru_cache(maxsize=1)
def n8_source_chain_test():
    local = build_local_matrix(8)
    lower = tuple(sorted(cells(8, 7), key=lambda cell: cell.affine))
    middle = tuple(sorted(cells(8, 8), key=lambda cell: cell.affine))
    upper = tuple(sorted(cells(8, 9), key=lambda cell: cell.affine))
    lower_index = {cell.affine: i for i, cell in enumerate(lower)}
    middle_index = {cell.affine: i for i, cell in enumerate(middle)}
    middle_by_affine = {cell.affine: cell for cell in middle}
    lower_bases = [frozenset(cell.bases) for cell in lower]
    full_boundary_columns = []
    for cell in middle:
        direct = tuple(sorted(lower_index[face.affine] for face in facets(cell)))
        # A genuinely separate incidence construction: enumerate every lower
        # cell and compare complete bases, with the dimensions fixed in advance.
        parent_bases = frozenset(cell.bases)
        independent = tuple(i for i, child_bases in enumerate(lower_bases)
                            if child_bases <= parent_bases)
        assert direct == independent
        full_boundary_columns.append(sum(1 << i for i in direct))
    full_parent_records = []
    middle_bases = [frozenset(cell.bases) for cell in middle]
    for parent in upper:
        direct = tuple(sorted(middle_index[face.affine] for face in facets(parent)))
        parent_bases = frozenset(parent.bases)
        independent = tuple(i for i, child_bases in enumerate(middle_bases)
                            if child_bases <= parent_bases)
        assert direct == independent
        boundary_squared = _xor_columns(full_boundary_columns, direct)
        assert boundary_squared == 0
        full_parent_records.append({'parent_affine': parent.affine,
                                    'source_facet_middle_indices': direct,
                                    'ordinary_source_boundary_squared_zero': True})
    columns = tuple(local['column_affine_permutations'])
    tile_set = set(columns)
    admissible_columns = tuple(full_boundary_columns[middle_index[window]] for window in columns)
    nonadmissible = tuple(i for i, cell in enumerate(middle) if cell.affine not in tile_set)
    killed_mask = 0
    kill_witnesses = {}
    for index in nonadmissible:
        killed_mask |= full_boundary_columns[index]
        for lower_id in support_indices(full_boundary_columns[index]):
            kill_witnesses.setdefault(lower_id, index)
    reduced_columns = tuple(column & ~killed_mask for column in admissible_columns)
    local_mod2 = tuple(sum(1 << j for j, value in enumerate(row) if value % 2)
                       for row in local['rows'])
    products = []
    for relation, row in zip(local['relations'], local_mod2):
        support = support_indices(row)
        raw = _xor_columns(admissible_columns, support)
        reduced = raw & ~killed_mask
        assert reduced == 0
        parents = relation['parent_affines']
        for parent_affine in parents:
            parent = next(cell for cell in upper if cell.affine == tuple(parent_affine))
            non_tile_facets = tuple(middle_index[face.affine] for face in facets(parent)
                                    if face.affine not in tile_set)
            assert _xor_columns(full_boundary_columns, non_tile_facets) == raw
        products.append({'local_relation_id': relation['id'],
                         'parent_affines': parents,
                         'admissible_tile_column_indices': support,
                         'ordinary_source_boundary_nonzero_indices': support_indices(raw),
                         'ordinary_source_boundary_weight': raw.bit_count(),
                         'quotient_boundary_nonzero_indices': support_indices(reduced),
                         'raw_product_equals_boundary_of_omitted_nonadmissible_source_facets': True})
    raw_rank = gf2_rank_bitsets(admissible_columns)
    reduced_rank = gf2_rank_bitsets(reduced_columns)
    local_rank = gf2_rank_bitsets(local_mod2)
    assert raw_rank == gf2_rank_dense(admissible_columns, len(lower))
    assert reduced_rank == gf2_rank_dense(reduced_columns, len(lower))
    assert local_rank == gf2_rank_dense(local_mod2, len(columns))
    zero_columns = []
    for j, column in enumerate(reduced_columns):
        if column:
            continue
        witnesses = [{'lower_index': i, 'nonadmissible_middle_index': kill_witnesses[i]}
                     for i in support_indices(admissible_columns[j])]
        assert gf2_rank_bitsets(local_mod2 + (1 << j,)) == local_rank + 1
        zero_columns.append({'tile_column': j,
                             **_cell_record(middle_by_affine[columns[j]]),
                             'ordinary_source_facet_lower_indices': support_indices(admissible_columns[j]),
                             'discarded_facet_closure_witnesses': witnesses,
                             'formal_quotient_cycle_augmentation_mod2': 1,
                             'not_in_geometric_local_row_span': True,
                             'geometric_indicator_is_nonzero': 'All-Z admissible tile has a nonempty open image; source-cycle status does not give an image relation'})
    return {'n': 8, 'claim_tag': 'COMPUTATIONALLY-VERIFIED',
            'proof_reference': 'research/run5/SOURCE_CHAIN_TEST.md',
            'coefficient_field': 'F2',
            'scope': 'FORMAL_SOURCE_CELL_CHAIN_TEST; NOT AN IMAGE_RELATION_CERTIFICATE',
            'source_seven_cells': [_cell_record(cell) for cell in lower],
            'source_eight_cells': [_cell_record(cell) for cell in middle],
            'source_nine_parent_records': full_parent_records,
            'source_dimensions': {'C7': len(lower), 'C8': len(middle), 'C9': len(upper)},
            'independent_base_inclusion_incidence_agrees': True,
            'full_ordinary_source_boundary_squared_zero_for_all_parents': True,
            'ordinary_d8_all_source_columns_lower_indices': [support_indices(column) for column in full_boundary_columns],
            'admissible_tile_affine_column_order': columns,
            'ordinary_d8_admissible_columns_lower_indices': [support_indices(column) for column in admissible_columns],
            'geometric_d9_mod2_columns_tile_indices': [support_indices(row) for row in local_mod2],
            'nonadmissible_eight_cell_middle_indices': nonadmissible,
            'quotient_discarded_lower_indices': support_indices(killed_mask),
            'quotient_retained_lower_indices': tuple(i for i in range(len(lower)) if not (killed_mask >> i) & 1),
            'quotient_d8_admissible_columns_lower_indices': [support_indices(column) for column in reduced_columns],
            'source_chain_product_columns': products,
            'raw_nonzero_product_columns': sum(bool(row['ordinary_source_boundary_nonzero_indices']) for row in products),
            'raw_product_total_nonzero_entries': sum(row['ordinary_source_boundary_weight'] for row in products),
            'raw_product_column_weight_histogram': dict(sorted(Counter(row['ordinary_source_boundary_weight'] for row in products).items())),
            'quotient_product_zero': all(not row['quotient_boundary_nonzero_indices'] for row in products),
            'ranks_mod2': {'ordinary_d8_on_admissible_tiles': raw_rank,
                           'quotient_d8_on_admissible_tiles': reduced_rank,
                           'geometric_local_d9': local_rank,
                           'formal_H8_after_quotient': len(columns) - reduced_rank - local_rank},
            'independent_mod2_rank_algorithms_agree': True,
            'zero_quotient_boundary_tile_columns': zero_columns,
            'conclusions': {'ordinary_source_boundary_cannot_be_used_directly': 'FAILED',
                            'quotient_is_a_formal_three_term_chain_complex': 'PROVED',
                            'quotient_complex_exactness_at_tile_space': 'FAILED',
                            'quotient_cycles_are_geometric_indicator_relations': 'FAILED'},
            'warning': 'F2 cycles, dimensions, and augmentations are formal source statements; none is an unbalanced geometric tile relation.'}


def simplicial_boundary(lower_subsets, upper_subsets):
    index = {subset: i for i, subset in enumerate(lower_subsets)}
    matrix = Matrix.zeros(len(lower_subsets), len(upper_subsets))
    for j, simplex in enumerate(upper_subsets):
        for i in range(len(simplex)):
            face = simplex[:i] + simplex[i + 1:]
            matrix[index[face], j] = (-1) ** i
    return matrix


@lru_cache(maxsize=1)
def n7_simplicial_chain_test():
    local = build_local_matrix(7)
    support_by_affine = {row['affine']: row['simplex_support'] for row in tile_dictionary()}
    four = tuple(combinations(range(1, 8), 4))
    five = tuple(support_by_affine[window] for window in local['column_affine_permutations'])
    six = tuple(combinations(range(1, 8), 6))
    d4 = simplicial_boundary(four, five)
    d5 = simplicial_boundary(five, six)
    assert d4 * d5 == Matrix.zeros(35, 7)
    matches = []
    for record, row in zip(local['relations'], local['rows']):
        vector = Matrix(row)
        j, sign = next((j, sign) for j in range(d5.cols) for sign in (1, -1)
                       if vector == sign * d5[:, j])
        matches.append({'local_relation_id': record['id'], 'six_subset': six[j],
                        'simplicial_column_index': j, 'orientation_factor': sign})
    assert len({row['simplicial_column_index'] for row in matches}) == 7
    assert d4.rank() == 15 and d5.rank() == 6
    return {'n': 7, 'claim_tag': 'PROVED', 'coefficient_field': 'Q (matrices integral)',
            'scope': 'ABSTRACT_FULL_SIMPLEX_CHAIN_AFTER_ALL_Z_PARITY_LABEL_IDENTIFICATION',
            'not_claimed': 'This is not a literal oriented cell boundary on Gr(2,7), nor an assertion that parity transports arbitrary indicator relations.',
            'C3_four_subsets': four, 'C4_five_subsets_in_tile_order': five, 'C5_six_subsets': six,
            'd4_matrix': d4.tolist(), 'd5_matrix': d5.tolist(),
            'd4_d5_zero': True, 'd4_rank': 15, 'd5_rank': 6,
            'H4_dimension': 21 - d4.rank() - d5.rank(),
            'every_full_local_parent_row_matches_simplicial_boundary': matches,
            'proof': 'The full abstract 6-simplex is contractible; its integral simplicial chain complex is exact in positive degrees. Direct matrices also verify the ranks and product.',
            'all_d5_column_coefficient_sums_zero': all(sum(d5[:, j]) == 0 for j in range(d5.cols))}


def main():
    data = {'n8_source_chain': n8_source_chain_test(),
            'n7_parity_simplicial_chain': n7_simplicial_chain_test()}
    path = ROOT / 'results/run5/source_chain_test.json'
    path.write_text(json.dumps(data, indent=2, default=int) + '\n')
    print(json.dumps({'n8_ranks_mod2': data['n8_source_chain']['ranks_mod2'],
                      'n8_spurious_unit_cycles': len(data['n8_source_chain']['zero_quotient_boundary_tile_columns']),
                      'n7_H4_dimension': data['n7_parity_simplicial_chain']['H4_dimension']}))


if __name__ == '__main__':
    main()
