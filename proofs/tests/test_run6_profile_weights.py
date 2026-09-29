"""Exact small profile compression, with no larger global relation search."""

from pathlib import Path
import json

from sympy import Matrix

from magic_number.run6_profile_weights import build_profile_weights, independent_type, profile_weights


def test_complete_fifteen_prototype_compression_and_six_parameter_solution():
    data = build_profile_weights()
    matrix = Matrix(data['compressed_matrix'])
    basis = Matrix(data['integer_nullspace_basis'])
    assert matrix.shape == (15, 11)
    assert matrix.rank() == 5 and basis.rank() == 6
    assert matrix*basis.T == Matrix.zeros(15, 6)
    assert Matrix(data['rank_minor']).det() == -1
    for record in data['prototype_records']:
        row = [0]*11
        for term in record['terms']:
            assert tuple(data['tile_profile_columns'][term['profile_column']]) == independent_type(term['class_sizes'])
            row[term['profile_column']] += term['coefficient']
        assert row == record['profile_row']


def test_high_support_extension_and_unit_covector():
    data = build_profile_weights()
    assert profile_weights(1, 1, 1, 1, 1, 1) == (1,)*11
    assert data['high_support_covector'] == [0]*7+[1, 1, -1, 1]
    assert data['standard_n9_high_support_weight_sum'] == 2
    assert sum(data['standard_n9_profile_counts']) == 50
    assert data['standard_n9_basis_weight_sums'] == [10, 30, 0, -12, 10, 12]


def test_saved_profile_weight_certificate_reproduces():
    saved = json.loads(Path('results/run6/profile_weights.json').read_text())
    assert saved == json.loads(json.dumps(build_profile_weights(), default=int))
