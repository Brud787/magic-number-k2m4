"""Complete positive three-direction inverse, with strict closed-image gates.

The (3,3,3) spurion is the principal case. All positive fibers are the
projectivized positive kernels of an 8x9 linear system. The closure gates
exclude all missing two-direction charts before certifying a strict zero.
See research/run6/SPURION_INVERSION.md for hypotheses and proof scope.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json


def _rows(matrix):
    return [[F(value) for value in row] for row in (
        matrix.tolist() if hasattr(matrix, 'tolist') else matrix)]


def _dot(left, right):
    return sum(a*b for a, b in zip(left, right))


def _multiply(left, right):
    return [[_dot(row, column) for column in zip(*right)] for row in left]


def _rref(matrix):
    """Exact rectangular reduction and a full-row-rank minor certificate.

    When the matrix has full row rank, pivot_minor is the determinant of
    its original submatrix on pivot_columns (all rows, their original order).
    """
    work = _rows(matrix)
    count, width = len(work), len(work[0])
    pivot_row = 0
    pivots = []
    determinant = F(1)
    for column in range(width):
        pivot = next((i for i in range(pivot_row, count) if work[i][column]), None)
        if pivot is None:
            continue
        if pivot != pivot_row:
            work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
            determinant = -determinant
        value = work[pivot_row][column]
        determinant *= value
        work[pivot_row] = [entry/value for entry in work[pivot_row]]
        for i in range(count):
            if i != pivot_row and work[i][column]:
                value = work[i][column]
                work[i] = [a-value*b for a, b in zip(work[i], work[pivot_row])]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == count:
            break
    return {'rref': work, 'rank': pivot_row, 'pivot_columns': tuple(pivots),
            'pivot_minor': determinant if pivot_row == count else None}


def prepare_three_class(cell, z):
    """Prepare any admissible 9-support three-class profile with sizes <=4.

    Positive external maximal minors are a mathematical input hypothesis,
    as in the Run5 producer. The caller's global Z certificate establishes
    it; this routine does not repeat all external determinant checks.
    """
    if len(cell.support) != 9 or len(cell.classes) != 3 or max(map(len, cell.classes)) > 4:
        raise ValueError('Expected a nine-support three-class admissible profile')
    external = _rows(z)
    if len(external) != cell.n or any(len(row) != 6 for row in external):
        raise ValueError('Expected an n by 6 external matrix')
    labels = tuple(label for block in cell.classes for label in block)
    signs = tuple(-1 if label < labels[0] else 1 for label in labels)
    cut_external = [[sign*value for value in external[label-1]]
                    for label, sign in zip(labels, signs)]
    sizes = tuple(map(len, cell.classes))
    return {'cell': cell, 'labels': labels, 'signs': signs,
            'external': cut_external, 'class_sizes': sizes,
            'class_positions': (tuple(range(sizes[0])),
                                tuple(range(sizes[0], sizes[0]+sizes[1])),
                                tuple(range(sizes[0]+sizes[1], 9))),
            'inverse_kind': 'THREE_DIRECTION_LINEAR_KERNEL'}


def prepare_spurion(cell, z):
    if tuple(map(len, cell.classes)) != (3, 3, 3):
        raise ValueError('Expected the (3,3,3) spurion source or a zero insertion')
    return prepare_three_class(cell, z)


def source_matrix(chart, coordinates):
    """Undo the signed cyclic chart, retaining loops as literal zero columns."""
    if len(coordinates) != 9:
        raise ValueError('Expected nine homogeneous coordinates')
    a, b, _ = chart['class_sizes']
    source = [[F(0)]*chart['cell'].n for _ in range(2)]
    for i, (label, sign, value) in enumerate(zip(chart['labels'], chart['signs'], coordinates)):
        if i < a+b:
            source[0][label-1] = sign*value
        if i >= a:
            source[1][label-1] = sign*value
    return source


def quotient_projection(y):
    """An exact rational basis of null(Y), with an adaptive 2-column pivot."""
    y = _rows(y)
    if len(y) != 2 or any(len(row) != 6 for row in y):
        raise ValueError('Expected a 2 by 6 target representative')
    pivot = next(((i, j) for i, j in combinations(range(6), 2)
                  if y[0][i]*y[1][j]-y[0][j]*y[1][i]), None)
    if pivot is None:
        raise ValueError('Target representative has rank below two')
    p, q = pivot
    determinant = y[0][p]*y[1][q]-y[0][q]*y[1][p]
    free = tuple(j for j in range(6) if j not in pivot)
    projection = [[F(0)]*4 for _ in range(6)]
    for h, j in enumerate(free):
        projection[p][h] = -(y[1][q]*y[0][j]-y[0][q]*y[1][j])/determinant
        projection[q][h] = -(-y[1][p]*y[0][j]+y[0][p]*y[1][j])/determinant
        projection[j][h] = F(1)
    return projection, pivot, determinant


def fiber_matrix(chart, y):
    projection, pivot, determinant = quotient_projection(y)
    projected = _multiply(chart['external'], projection)
    a, b, _ = chart['class_sizes']
    matrix = [[projected[i][j] if i < a+b else F(0) for i in range(9)] for j in range(4)]
    matrix += [[projected[i][j] if i >= a else F(0) for i in range(9)] for j in range(4)]
    return matrix, pivot, determinant


def open_inverse(chart, y):
    """Complete open-image decision for every rank-two Y and positive Z.

    The rank-deficient exclusion uses the independently known all-Z
    injectivity of this source tile. The strict API below additionally
    supplies closed nonmembership and open-neighborhood certificates.
    """
    matrix, y_pivot, y_minor = fiber_matrix(chart, y)
    reduction = _rref(matrix)
    result = {'indicator': 0, 'reason': 'RANK_DEFICIENT_FIBER_MATRIX',
              'fiber_rank': reduction['rank'],
              'target_pivot_columns': y_pivot, 'target_pivot_minor': y_minor,
              'fiber_pivot_columns': reduction['pivot_columns'],
              'fiber_pivot_minor': reduction['pivot_minor']}
    if reduction['rank'] != 8:
        result['scope'] = 'OPEN_NONMEMBERSHIP_BY_PUBLISHED_ALL_Z_INJECTIVITY; CLOSED_UNDECIDED'
        return result
    free = next(j for j in range(9) if j not in reduction['pivot_columns'])
    kernel = [F(0)]*9
    kernel[free] = F(1)
    for i, pivot in enumerate(reduction['pivot_columns']):
        kernel[pivot] = -reduction['rref'][i][free]
    assert all(_dot(row, kernel) == 0 for row in matrix)
    result.update({'free_coordinate': free, 'kernel_coefficients': kernel,
                   'reason': 'COMPLETE_THREE_DIRECTION_INVERSE',
                   'scope': 'COMPLETE_OPEN_MEMBERSHIP'})
    if any(value == 0 for value in kernel):
        result['reason'] = 'ZERO_KERNEL_COORDINATE'
        return result
    result['indicator'] = int(all(value > 0 for value in kernel) or all(value < 0 for value in kernel))
    if result['indicator']:
        positive = kernel if kernel[0] > 0 else [-value for value in kernel]
        result['positive_source_coordinates'] = positive
    else:
        result['reason'] = 'MIXED_STRICT_KERNEL_COORDINATES'
    return result


def inversion(chart, y):
    """Strict closed-indicator certificate, or None at an exceptional target.

    Each returned result is valid on an ambient open neighborhood. The
    three block-rank gates are checked here, so closed exclusion does not
    depend on an unstated global twistor-genericity promise by the caller.
    """
    result = open_inverse(chart, y)
    if result['fiber_rank'] != 8 or any(value == 0 for value in result['kernel_coefficients']):
        return None
    y = _rows(y)
    gate_records = []
    for positions in chart['class_positions']:
        matrix = y + [chart['external'][i] for i in positions]
        reduction = _rref(matrix)
        if reduction['rank'] != len(positions)+2:
            return None
        gate_records.append({'class_positions': positions,
                             'rank': reduction['rank'],
                             'pivot_columns': reduction['pivot_columns'],
                             'nonzero_pivot_minor': reduction['pivot_minor']})
    result['merger_exclusion_gates'] = gate_records
    result['scope'] = 'STRICT_OPEN_MEMBERSHIP_OR_CLOSED_NONMEMBERSHIP_ON_AN_OPEN_NEIGHBORHOOD'
    return result


def _serializable(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: _serializable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_serializable(item) for item in value]
    return value


def fixture_data():
    from .rank2 import RankTwoCell
    cell = RankTwoCell(9, ((1, 2, 3), (4, 5, 6), (7, 8, 9)))
    z = [[F(i**j) for j in range(6)] for i in range(1, 10)]
    chart = prepare_spurion(cell, z)
    coordinates = list(map(F, (2, 3, 5, 7, 11, 13, 17, 19, 23)))
    cases = []
    for kind, index in [('OPEN', None)] + [('NEGATIVE', i) for i in range(9)] + [('ZERO', i) for i in range(9)]:
        values = list(coordinates)
        if kind == 'NEGATIVE':
            values[index] = -values[index]
        elif kind == 'ZERO':
            values[index] = 0
        c = source_matrix(chart, values)
        y = _multiply(c, z)
        cases.append({'kind': kind, 'changed_coordinate': index,
                      'source_coordinates': values, 'source_matrix': c, 'target': y,
                      'open_inverse': open_inverse(chart, y), 'strict_inverse': inversion(chart, y)})
    return {'claim_tag': 'COMPUTATIONALLY-VERIFIED',
            'proof_reference': 'research/run6/SPURION_INVERSION.md',
            'scope': 'Exact regression of a separately proved all-Z inverse, not numerical tile certification',
            'source_affine': cell.affine, 'source_classes': cell.classes,
            'external_matrix': z, 'cases': cases}


if __name__ == '__main__':
    output = Path('fixtures/run6/spurion_inverse.json')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(_serializable(fixture_data()), indent=2)+'\n')
    print(output)
