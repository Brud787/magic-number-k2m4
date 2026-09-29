"""Exact ambient inverse replay; no production construction is imported.

The six-row complement inverse follows the Run6 secondary audit, with
standalone class decoding. The spurion is solved by 12 ambient equations
with four unknown row-frame coefficients, not the producer's 8x9 quotient.
Strict failures raise: an exceptional input is NEVER silently a zero.
"""
from itertools import combinations
from sympy import Matrix, Rational, zeros
from .combinatorics import classes, bases, affine


def source_minors(c):
    return {(i+1, j+1): c[0][i]*c[1][j]-c[0][j]*c[1][i]
            for i, j in combinations(range(len(c[0])), 2)}


def positive_external(z):
    assert z.cols == 6
    assert all(z[list(s), :].det() > 0 for s in combinations(range(z.rows), 6))


def prepare(keys, z):
    frames = {}
    charts = []
    for key in keys:
        blocks = classes(key)
        q = sum(map(len, blocks))
        d = next((j for j, b in enumerate(blocks) if len(b) == q-5), None)
        if d is not None:
            blocks = blocks[d+1:] + blocks[:d+1]
        else:
            assert tuple(map(len, blocks)) == (3, 3, 3)
        labels = tuple(i for b in blocks for i in b)
        signs = tuple(-1 if i < labels[0] else 1 for i in labels)
        external = Matrix([[sign*v for v in z[label-1, :]] for label, sign in zip(labels, signs)])
        chart = dict(key=key, blocks=blocks, labels=labels, signs=signs,
                     external=external, n=z.rows, family='SPURION' if d is None else 'COMPLEMENT_FIVE')
        if d is not None:
            assert sum(map(len, blocks[:-1])) == 5 and len(blocks)-1+len(blocks[-1]) == 6
            frame_key = tuple(zip(labels[:6], signs[:6]))
            if frame_key not in frames:
                frames[frame_key] = external[:6, :].inv(method='DM')
            chart.update(frame_key=frame_key, frame_inverse=frames[frame_key])
        charts.append(chart)
    return charts


def complement(chart, y, cache):
    key = chart['frame_key']
    if key not in cache:
        coordinates = y*chart['frame_inverse']
        h0, h1 = coordinates[0, 5], coordinates[1, 5]
        assert h0 or h1, 'Exceptional target contained in the complement hyperplane'
        raw = [h1*coordinates[0, i]-h0*coordinates[1, i] for i in range(5)]
        assert all(raw), 'Exceptional zero hyperplane coefficient'
        if min(raw) < 0 < max(raw):
            cache[key] = None
        else:
            a = [v/raw[0] for v in raw]
            image_index = 0 if h0 else 1
            multiplier = 1 if coordinates[image_index, 5] > 0 else -1
            second = [multiplier*v for v in y[image_index, :]]
            change = Matrix([[h1/raw[0], -h0/raw[0]],
                             [multiplier if image_index == 0 else 0,
                              multiplier if image_index == 1 else 0]])
            cache[key] = (a, second, change)
    if cache[key] is None:
        return 0, 'MIXED'
    a, second, change = cache[key]
    assert all(v > 0 for v in a) and change.det() != 0
    blocks, external = chart['blocks'], chart['external']
    ell = len(blocks)-1
    rows, position = [], 0
    for block in blocks[:-1]:
        rows.append([sum(a[i]*external[i, j] for i in range(position, position+len(block)))
                     for j in range(6)])
        position += len(block)
    rows.extend(list(external[i, :]) for i in range(5, external.rows))
    coefficients = Matrix(rows).T.inv(method='DM')*Matrix(second)
    first = list(a)+[0]*(external.rows-5)
    second_source, position = [], 0
    for j, block in enumerate(blocks[:-1]):
        second_source.extend(coefficients[j]*a[i] for i in range(position, position+len(block)))
        position += len(block)
    second_source.extend(coefficients[ell:])
    source = [[Rational(0)]*chart['n'] for _ in range(2)]
    for i, (label, sign) in enumerate(zip(chart['labels'], chart['signs'])):
        source[0][label-1], source[1][label-1] = sign*first[i], sign*second_source[i]
    assert Matrix([first, second_source])*external == change*y
    minors = source_minors(source)
    value = int(all(v >= 0 for v in minors.values()))
    assert all([coefficients[j+1]-coefficients[j] for j in range(ell-1)] + list(coefficients[ell:])), 'Exceptional boundary coefficient'
    if value:
        assert tuple(b for b, v in minors.items() if v > 0) == chart['key']
    else:
        assert any(v < 0 for v in minors.values())
    return value, 'SIX_ROW'


def spurion(chart, y, strict=True):
    external = chart['external']
    columns = []
    for i in range(9):
        row = list(external[i, :])
        columns.append(Matrix((row if i < 6 else [0]*6)+(row if i >= 3 else [0]*6)))
    columns.extend((Matrix(list(-y[0, :])+[0]*6), Matrix(list(-y[1, :])+[0]*6),
                    Matrix([0]*6+list(-y[0, :])), Matrix([0]*6+list(-y[1, :]))))
    ambient = Matrix.hstack(*columns)
    null = ambient.nullspace(simplify=False)
    if not strict and len(null) != 1:
        return 0, 'EXCEPTIONAL'
    assert len(null) == 1, 'Exceptional spurion fiber rank'
    vector = null[0]
    assert ambient*vector == zeros(12, 1)
    x = vector[:9]
    if strict:
        assert all(x), 'Exceptional zero spurion coefficient'
        for start in (0, 3, 6):
            assert Matrix.vstack(y, external[start:start+3, :]).rank() == 5, 'Exceptional merged-direction gauge'
    value = int(all(v > 0 for v in x) or all(v < 0 for v in x))
    if value:
        c = Matrix([list(x[:6])+[0]*3, [0]*3+list(x[3:])])
        assert Matrix.vstack(c*external, y).rank() == 2
    return value, 'SPURION'


def decide(chart, y, cache):
    return complement(chart, y, cache) if chart['family'] == 'COMPLEMENT_FIVE' else spurion(chart, y)


def twistor_covectors(z):
    pairs = tuple(combinations(range(6), 2))
    covectors = []
    for labels in combinations(range(z.rows), 4):
        external = z[list(labels), :]
        covectors.append([(-1)**(i+j+1)*external[:, [h for h in range(6) if h not in (i, j)]].det()
                          for i, j in pairs])
    return pairs, covectors


def generic(y, covectors):
    pairs, covectors = covectors
    pluckers = [y[0, i]*y[1, j]-y[0, j]*y[1, i] for i, j in pairs]
    values = [sum(a*b for a, b in zip(row, pluckers)) for row in covectors]
    assert all(values), 'Exceptional zero four-twistor'
    return values


def replay_n9(data, keys, progress):
    from collections import Counter
    import hashlib
    z = Matrix(data['external_matrix'])
    positive_external(z)
    charts, covectors = prepare(keys, z), twistor_covectors(z)
    assert len(charts) == 942 and len(data['target_records']) == 472
    counts, rebuilt = Counter(), []
    for i, target in enumerate(data['target_records']):
        y, c = Matrix(target['target_representative']), Matrix(target['source_matrix'])
        assert c*z == y
        minors = source_minors(c.tolist())
        assert all(v >= 0 for v in minors.values())
        key = tuple(b for b, v in minors.items() if v > 0)
        assert affine(9, key) == tuple(target['source_affine'])
        assert len(generic(y, covectors)) == 126
        cache, row = {}, []
        for chart in charts:
            value, kind = decide(chart, y, cache)
            counts[kind] += 1
            row.append(value)
        assert row == target['indicator_vector'] == data['indicator_rows'][i], f'N9-W{i+1:04d} membership mismatch'
        rebuilt.append(row)
        if (i+1) % 16 == 0:
            progress(f'[INFO] independent membership replay: {i+1}/472 witnesses')
    assert sum(counts.values()) == 444624
    digest = hashlib.sha256(bytes(v for row in rebuilt for v in row)).hexdigest()
    return rebuilt, dict(counts), digest
