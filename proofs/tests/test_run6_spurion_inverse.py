"""Independent ambient equations, source signs, and closure-gauge regressions."""

from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json

from sympy import Matrix, zeros

from magic_number.parent_relations import embed, relabel
from magic_number.rank2 import RankTwoCell
from magic_number.run6_spurion_inverse import (
    fiber_matrix, fixture_data, inversion, open_inverse,
    prepare_spurion, prepare_three_class, source_matrix,
)
from magic_number.spurion import spurion_facet_functionaries


BASE = RankTwoCell(9, ((1, 2, 3), (4, 5, 6), (7, 8, 9)))


def external(n):
    return Matrix([[i**j for j in range(6)] for i in range(1, n+1)])


def ambient_kernel(chart, y):
    """No quotient matrix: solve C(x)E=H Y as twelve ambient equations."""
    e, y = Matrix(chart['external']), Matrix(y)
    a, b, _ = chart['class_sizes']
    columns = []
    for i in range(9):
        first = e[i, :].T if i < a+b else zeros(6, 1)
        second = e[i, :].T if i >= a else zeros(6, 1)
        columns.append(first.col_join(second))
    for row in range(2):
        for j in range(2):
            column = zeros(12, 1)
            column[6*row:6*(row+1), :] = -y[j, :].T
            columns.append(column)
    matrix = Matrix.hstack(*columns)
    return matrix, matrix.nullspace()


def test_every_exact_regression_inverse_by_independent_ambient_solve():
    data = fixture_data()
    z = Matrix(data['external_matrix'])
    chart = prepare_spurion(BASE, z)
    for case in data['cases']:
        y = Matrix(case['target'])
        matrix, kernel = ambient_kernel(chart, y)
        assert matrix.shape == (12, 13) and len(kernel) == 1
        independent = list(kernel[0][:9, :])
        certificate = case['open_inverse']
        saved = certificate['kernel_coefficients']
        factor = independent[certificate['free_coordinate']]
        assert factor != 0
        assert [value/factor for value in independent] == saved
        c = Matrix(source_matrix(chart, saved))
        values = [c[:, list(pair)].det() for pair in combinations(range(9), 2)]
        if case['kind'] == 'OPEN':
            assert certificate['indicator'] == 1
            assert all(value >= 0 for value in values)
            assert {pair for pair in combinations(range(1, 10), 2)
                    if c[:, [i-1 for i in pair]].det() > 0} == set(BASE.bases)
        elif case['kind'] == 'NEGATIVE':
            assert certificate['indicator'] == 0
            assert min(values) < 0 < max(values)
            assert case['strict_inverse']['indicator'] == 0
        else:
            assert certificate['indicator'] == 0 and case['strict_inverse'] is None


def test_pivot_and_merger_gate_minors_recomputed_by_independent_determinants():
    data = fixture_data()
    chart = prepare_spurion(BASE, data['external_matrix'])
    for case in data['cases']:
        certificate = case['strict_inverse']
        if certificate is None:
            continue
        y = Matrix(case['target'])
        m, _, _ = fiber_matrix(chart, y)
        assert Matrix(m)[:, list(certificate['fiber_pivot_columns'])].det() == certificate['fiber_pivot_minor']
        assert y[:, list(certificate['target_pivot_columns'])].det() == certificate['target_pivot_minor']
        for gate in certificate['merger_exclusion_gates']:
            block = Matrix([chart['external'][i] for i in gate['class_positions']])
            stacked = y.col_join(block)
            assert stacked[:, list(gate['pivot_columns'])].det() == gate['nonzero_pivot_minor']
            assert gate['nonzero_pivot_minor'] != 0


def test_three_merger_gauges_are_closed_preimages_not_false_strict_zeros():
    z = external(9)
    chart = prepare_spurion(BASE, z)
    values = list(range(1, 10))
    patterns = [
        Matrix([[values[i] if i < 6 else 0 for i in range(9)],
                [values[i] if i >= 6 else 0 for i in range(9)]]),
        Matrix([[values[i] if i < 3 else 0 for i in range(9)],
                [values[i] if i >= 3 else 0 for i in range(9)]]),
        Matrix([[values[i] if i < 3 else -values[i] if i >= 6 else 0 for i in range(9)],
                [values[i] if 3 <= i < 6 else 0 for i in range(9)]]),
    ]
    for c in patterns:
        assert c.rank() == 2
        nonzero = {pair for pair in combinations(range(1, 10), 2)
                   if c[:, [i-1 for i in pair]].det() > 0}
        assert nonzero < set(BASE.bases)
        assert all(c[:, list(pair)].det() >= 0 for pair in combinations(range(9), 2))
        y = c*z
        assert any(y.col_join(z[list(positions), :]).rank() < 5
                   for positions in ((0, 1, 2), (3, 4, 5), (6, 7, 8)))
        assert inversion(chart, y) is None
    # Deleting a whole group retains a rank-two closed source point.
    x = [0, 0, 0, 4, 5, 6, 7, 8, 9]
    c = Matrix(source_matrix(chart, x))
    assert c.rank() == 2 and inversion(chart, c*z) is None


def test_signed_cyclic_dihedral_and_zero_insertion_transport_exactly():
    cells = {relabel(BASE, direction, shift).affine: relabel(BASE, direction, shift)
             for direction in (-1, 1) for shift in range(9)}
    assert len(cells) == 3
    cells['inserted'] = embed(BASE, 11, (1, 2, 3, 5, 6, 7, 9, 10, 11))
    x = list(range(2, 11))
    for cell in cells.values():
        z = external(cell.n)
        chart = prepare_spurion(cell, z)
        for size in (2, 6):
            for positions in combinations(range(9), size):
                labels = [chart['labels'][i] for i in positions]
                parity = sum(labels[i] > labels[j] for i in range(size) for j in range(i+1, size))
                sign = (-1)**parity
                for i in positions:
                    sign *= chart['signs'][i]
                assert sign == 1
        c = Matrix(source_matrix(chart, x))
        result = inversion(chart, c*z)
        assert result['indicator'] == 1
        recovered = result['positive_source_coordinates']
        assert [value/recovered[0] for value in recovered] == [Fraction(value, x[0]) for value in x]
        assert {pair for pair in combinations(range(1, cell.n+1), 2)
                if c[:, [i-1 for i in pair]].det() > 0} == set(cell.bases)
    # A genuine reflection intertwines positive source and external data.
    z = external(9)
    chart = prepare_spurion(BASE, z)
    c = Matrix(source_matrix(chart, x))
    j = Matrix.eye(9)[:, list(reversed(range(9)))]
    g = Matrix.diag(-1, 1, 1, 1, 1, 1)
    h = Matrix([[0, 1], [1, 0]])
    reflected_z, reflected_c = j*z*g, h*c*j
    assert all(reflected_z[list(rows), :].det() > 0 for rows in combinations(range(9), 6))
    assert inversion(prepare_spurion(BASE, reflected_z), reflected_c*reflected_z)['indicator'] == 1
    assert reflected_c*reflected_z == h*c*z*g


def test_uniform_three_direction_profiles_and_arbitrary_target_frame():
    z = external(9)
    for sizes in ((1, 4, 4), (2, 3, 4), (3, 3, 3)):
        a, b, _ = sizes
        cell = RankTwoCell(9, (tuple(range(1, a+1)), tuple(range(a+1, a+b+1)), tuple(range(a+b+1, 10))))
        chart = prepare_three_class(cell, z)
        x = list(range(3, 12))
        c = Matrix(source_matrix(chart, x))
        y = c*z
        # This row change has negative determinant; no target-frame orientation
        # is silently assumed by the positive source inverse.
        y = Matrix([[2, 3], [5, 7]])*y
        result = inversion(chart, y)
        assert result['indicator'] == 1
        assert Matrix(source_matrix(chart, result['positive_source_coordinates'])).col_join(c).rank() == 2


def test_published_spurion_functionaries_agree_with_the_inverse_projectively():
    data = fixture_data()
    case = data['cases'][0]
    values = spurion_facet_functionaries(Matrix(case['target']), Matrix(data['external_matrix']))
    recovered = [-values[3], values[4], -values[5], -values[0], values[1], -values[2],
                 -values[6], values[7], -values[8]]
    x = case['source_coordinates']
    assert all(value > 0 for value in recovered)
    assert [value/recovered[0] for value in recovered] == [value/x[0] for value in x]


def test_spurion_saved_exact_fixture_reproduces():
    data = fixture_data()
    def encode(value):
        if isinstance(value, Fraction):
            return str(value)
        raise TypeError(type(value).__name__)
    saved = json.loads(Path('fixtures/run6/spurion_inverse.json').read_text())
    assert saved == json.loads(json.dumps(data, default=encode))
