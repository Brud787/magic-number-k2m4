"""Exact rejection of naive source-chain models and n7 parity regression."""

import json
from pathlib import Path

from sympy import Matrix

from magic_number.rank2 import RankTwoCell
from magic_number.run5_source_chain import (
    gf2_rank_bitsets, gf2_rank_dense, n7_simplicial_chain_test,
    n8_source_chain_test,
)


def test_all_ordinary_source_boundaries_square_to_zero_before_tile_filtering():
    data = n8_source_chain_test()
    columns = data['ordinary_d8_all_source_columns_lower_indices']
    assert data['source_dimensions'] == {'C7': 504, 'C8': 266, 'C9': 112}
    assert len(data['source_nine_parent_records']) == 112
    for parent in data['source_nine_parent_records']:
        result = set()
        for middle_index in parent['source_facet_middle_indices']:
            result.symmetric_difference_update(columns[middle_index])
        assert not result


def test_every_geometric_local_row_fails_the_unquotiented_source_chain_test():
    data = n8_source_chain_test()
    assert data['raw_nonzero_product_columns'] == 96
    assert data['raw_product_total_nonzero_entries'] == 1680
    assert data['raw_product_column_weight_histogram'] == {10: 8, 14: 56, 25: 16, 26: 16}
    assert data['ranks_mod2']['ordinary_d8_on_admissible_tiles'] == 176
    assert all(row['ordinary_source_boundary_nonzero_indices']
               for row in data['source_chain_product_columns'])


def test_nonadmissible_closure_quotient_restores_chain_identity_but_not_exactness():
    data = n8_source_chain_test()
    assert len(data['nonadmissible_eight_cell_middle_indices']) == 90
    assert len(data['quotient_discarded_lower_indices']) == 408
    assert len(data['quotient_retained_lower_indices']) == 96
    killed = set(data['quotient_discarded_lower_indices'])
    for row in data['source_chain_product_columns']:
        assert set(row['ordinary_source_boundary_nonzero_indices']) <= killed
        assert not row['quotient_boundary_nonzero_indices']
    assert data['ranks_mod2'] == {
        'ordinary_d8_on_admissible_tiles': 176,
        'quotient_d8_on_admissible_tiles': 88,
        'geometric_local_d9': 73,
        'formal_H8_after_quotient': 15,
    }


def test_each_spurious_unit_cycle_has_exact_nonadmissible_closure_witnesses():
    data = n8_source_chain_test()
    lower, middle = data['source_seven_cells'], data['source_eight_cells']
    nonadmissible = set(data['nonadmissible_eight_cell_middle_indices'])
    units = data['zero_quotient_boundary_tile_columns']
    assert len(units) == 8
    assert tuple(units[0]['affine']) == (1, 4, 6, 7, 5, 8, 10, 11)
    for unit in units:
        tile_bases = set(map(tuple, unit['bases']))
        assert unit['formal_quotient_cycle_augmentation_mod2'] == 1
        assert unit['not_in_geometric_local_row_span']
        for witness in unit['discarded_facet_closure_witnesses']:
            lower_cell = lower[witness['lower_index']]
            parent_index = witness['nonadmissible_middle_index']
            assert parent_index in nonadmissible
            parent = middle[parent_index]
            lower_bases = set(map(tuple, lower_cell['bases']))
            assert lower_bases <= tile_bases
            assert lower_bases <= set(map(tuple, parent['bases']))
            assert lower_cell['dimension'] == 7 and parent['dimension'] == 8


def test_mod2_ranks_recomputed_from_saved_sparse_columns():
    data = n8_source_chain_test()
    for key, width, expected in (
        ('ordinary_d8_admissible_columns_lower_indices', 504, 176),
        ('quotient_d8_admissible_columns_lower_indices', 504, 88),
        ('geometric_d9_mod2_columns_tile_indices', 176, 73),
    ):
        masks = [sum(1 << index for index in column) for column in data[key]]
        assert gf2_rank_bitsets(masks) == gf2_rank_dense(masks, width) == expected


def test_n7_simplicial_complex_and_exact_matches_to_all_local_rows():
    data = n7_simplicial_chain_test()
    d4, d5 = Matrix(data['d4_matrix']), Matrix(data['d5_matrix'])
    assert d4.shape == (35, 21) and d5.shape == (21, 7)
    assert d4 * d5 == Matrix.zeros(35, 7)
    assert d4.rank() == 15 and d5.rank() == 6
    assert data['H4_dimension'] == 0
    matches = data['every_full_local_parent_row_matches_simplicial_boundary']
    assert {record['simplicial_column_index'] for record in matches} == set(range(7))
    assert all(sum(d5[:, j]) == 0 for j in range(7))


def test_saved_source_chain_artifact_reproduces_exactly():
    saved = json.loads(Path('results/run5/source_chain_test.json').read_text())
    current = {'n8_source_chain': n8_source_chain_test(),
               'n7_parity_simplicial_chain': n7_simplicial_chain_test()}
    assert saved == json.loads(json.dumps(current, default=int))
