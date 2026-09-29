"""Small characteristic-zero certificate checks using Python Fraction arithmetic."""
from fractions import Fraction


def determinant(matrix):
    a = [{j: Fraction(v) for j, v in enumerate(row) if v} for row in matrix]
    n = len(a)
    assert all(len(row) == n for row in matrix)
    value = Fraction(1)  # determinant of the empty 0 x 0 matrix
    for j in range(n):
        p = next((i for i in range(j, n) if a[i].get(j)), None)
        if p is None:
            return Fraction(0)
        if p != j:
            a[j], a[p] = a[p], a[j]
            value = -value
        pivot = a[j][j]
        value *= pivot
        for i in range(j+1, n):
            if a[i].get(j):
                ratio = a[i][j]/pivot
                for k, v in a[j].items():
                    updated = a[i].get(k, 0)-ratio*v
                    if updated:
                        a[i][k] = updated
                    else:
                        a[i].pop(k, None)
    return value


def upper_bound(rows, pivots, sparse_rref, width):
    """Every original row lies in the published r-dimensional rational span."""
    assert len(pivots) == len(sparse_rref) and len(set(pivots)) == len(pivots)
    basis = [dict((j, Fraction(v)) for j, v in row) for row in sparse_rref]
    assert all(all(row.get(p, 0) == (i == k) for k, p in enumerate(pivots))
               for i, row in enumerate(basis))
    for row in rows:
        assert len(row) == width
        reconstructed = {}
        for p, b in zip(pivots, basis):
            if row[p]:
                for j, value in b.items():
                    reconstructed[j] = reconstructed.get(j, 0) + row[p]*value
        assert all(reconstructed.get(j, 0) == value for j, value in enumerate(row))
    return len(basis)


def rank_certificate(rows, width, pivots, selected, rref, expected_det):
    r = upper_bound(rows, pivots, rref, width)
    assert len(selected) == r and len(set(selected)) == r
    minor = [[rows[i][j] for j in pivots] for i in selected]
    value = determinant(minor)
    assert value == Fraction(expected_det) and value != 0
    return r
