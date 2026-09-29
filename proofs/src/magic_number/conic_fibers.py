"""Exact conic fibers for the hostile parent (12)(34)(56)(789).

All fixture multiplicities below concern one explicit rational positive Z.
Global rank statements and scope are explained in research/run3/MULTIPLICITY.md.
No four-mass wall is promoted to an injective positroid tile.
"""
from __future__ import annotations

from pathlib import Path
import json
from itertools import combinations

from sympy import Matrix, Rational, diff, factor, simplify, solve, symbols, zeros
from sympy.solvers.inequalities import reduce_rational_inequalities

COORDINATES = ('a1', 'a2', 'u3', 'v3', 'u4', 'v4', 'c5', 'c6', 'd7', 'd8', 'd9')
SCENARIOS = {
    'zero_positive_fourmass_preimages': (1,) * 11,
    'one_positive_fourmass_preimage': (1,) * 10 + (0,),
    'two_positive_fourmass_preimages': (1, 3, 12, 3, 16, 4, 1, 1, 5, 1, 0),
}
EXPECTED_PARENT_INTERVALS = {
    'zero_positive_fourmass_preimages': (Rational(10, 37), Rational(61, 37)),
    'one_positive_fourmass_preimage': (Rational(1), Rational(125, 77)),
    'two_positive_fourmass_preimages': (Rational(1853, 897), Rational(3)),
}


def source_matrix(x):
    if len(x) != 11:
        raise ValueError('Eleven homogeneous coefficients are required')
    a1, a2, u3, v3, u4, v4, c5, c6, d7, d8, d9 = x
    return Matrix([[a1, a2, u3+v3, u4+v4, c5, c6, 0, 0, 0],
                   [0, 0, v3, v4, c5, c6, d7, d8, d9]])


def proportionality_quadric(x):
    return factor(x[2]*x[5] - x[4]*x[3])


def moment_z():
    return Matrix([[i**j for j in range(6)] for i in range(1, 10)])


def fiber_matrix(y, z):
    """Eight linear equations for row containment C(x)Z <= Y."""
    y, z = Matrix(y), Matrix(z)
    if y.shape != (2, 6) or z.shape != (9, 6) or y.rank() != 2:
        raise ValueError('Require rank-two2x6 Y and9x6 Z')
    quotient = Matrix.hstack(*y.nullspace())
    e = z * quotient
    zero = zeros(4, 1)
    return Matrix.hstack(
        e[0, :].T.col_join(zero), e[1, :].T.col_join(zero),
        e[2, :].T.col_join(zero), e[2, :].T.col_join(e[2, :].T),
        e[3, :].T.col_join(zero), e[3, :].T.col_join(e[3, :].T),
        e[4, :].T.col_join(e[4, :].T), e[5, :].T.col_join(e[5, :].T),
        zero.col_join(e[6, :].T), zero.col_join(e[7, :].T), zero.col_join(e[8, :].T),
    )


def kernel_plane(y, z):
    """Basis with rows(a1,a2,d9)=I3; the remaining8x8 pivot is inverted."""
    m = fiber_matrix(y, z)
    free, dependent = (0, 1, 10), tuple(range(2, 10))
    coefficients = -m[:, dependent].inv() * m[:, free]
    k = zeros(11, 3)
    for j, i in enumerate(free):
        k[i, j] = 1
    for j, i in enumerate(dependent):
        k[i, :] = coefficients[j, :]
    return k


def conic_chart(y, z):
    """Normalize a1=1; return exact x(t,s), quadric and rational graph s(t)."""
    t, s = symbols('t s', real=True)
    k = kernel_plane(y, z)
    x = k * Matrix([1, t, s])
    q = proportionality_quadric(x)
    solutions = solve(q, s)
    if len(solutions) != 1:
        raise ValueError('This bounded laboratory expects one rational graph chart')
    graph = factor(solutions[0])
    rational_coordinates = tuple(factor(v.subs(s, graph)) for v in x)
    return {'t': t, 's': s, 'kernel': k, 'coordinates': x, 'quadric': q,
            'graph': graph, 'rational_coordinates': rational_coordinates}


def positive_parent_region(chart):
    return reduce_rational_inequalities(
        [[coordinate > 0 for coordinate in chart['rational_coordinates']]], chart['t'])


def fourmass_preimages(chart):
    """All real positive preimages in the d9=0 four-mass source cell."""
    t, s = chart['t'], chart['s']
    roots = solve(chart['quadric'].subs(s, 0), t)
    records = []
    for root in roots:
        x = tuple(simplify(v.subs({t: root, s: 0})) for v in chart['coordinates'])
        signs = [v.is_positive for i, v in enumerate(x) if i != 10]
        if any(value is None for value in signs):
            raise ValueError('An algebraic coordinate sign was not decided exactly')
        positive = all(signs)
        # Orientation of the conic is(dt,ds)=(q_s,-q_t), so this is its
        # oriented normal at the wall s=0. It is not the complex degree.
        normal = simplify(-diff(chart['quadric'], t).subs({t: root, s: 0}))
        records.append({'parameter': root, 'coefficients': x,
                        'strictly_positive_on_fourmass_wall': positive,
                        'oriented_conic_wall_normal': normal})
    return records


def fourmass_map_jacobian(x, z):
    """Exact oriented8x8 Jacobian on the positive four-mass source chart.

    Source coordinates are(a2,r,v3,v4,c5,c6,d7,d8), witha1=1,d9=0 and
    u3=r*v3,u4=r*v4. Target coordinates flatten[Y[:,0:2]^-1 Y[:,2:6]].
    This is an ordinary differential determinant, not a multiplicity count.
    """
    x = tuple(map(simplify, x))
    if x[0] != 1 or x[10] != 0 or proportionality_quadric(x) != 0:
        raise ValueError('Require normalized proportional d9=0 chart')
    r, v3, v4 = x[2]/x[3], x[3], x[5]
    derivatives = []
    for entries in (
        ((0, 1, 1),),
        ((0, 2, v3), (0, 3, v4)),
        ((0, 2, r+1), (1, 2, 1)),
        ((0, 3, r+1), (1, 3, 1)),
        ((0, 4, 1), (1, 4, 1)),
        ((0, 5, 1), (1, 5, 1)),
        ((1, 6, 1),), ((1, 7, 1),),
    ):
        dc = zeros(2, 9)
        for row, column, coefficient in entries:
            dc[row, column] = coefficient
        derivatives.append(dc * z)
    y = source_matrix(x) * z
    inverse = y[:, :2].inv()
    target = inverse * y[:, 2:]
    differential_columns = [Matrix(list(inverse * (dy[:, 2:] - dy[:, :2]*target)))
                            for dy in derivatives]
    return factor(Matrix.hstack(*differential_columns).det())


def fixture_data():
    z = moment_z()
    result = {'scope': 'Fixed positive rational moment-curve Z; no all-Z multiplicity claim',
              'source_parent': [[1, 2], [3, 4], [5, 6], [7, 8, 9]],
              'fourmass_wall': [[1, 2], [3, 4], [5, 6], [7, 8]],
              'coordinate_order': COORDINATES, 'Z': [[int(v) for v in row] for row in z.tolist()], 'scenarios': {}}
    for name, seed in SCENARIOS.items():
        y = source_matrix(seed) * z
        chart = conic_chart(y, z)
        preimages = fourmass_preimages(chart)
        record = {
            'seed_coefficients': seed, 'Y_representative': [[int(v) for v in row] for row in y.tolist()],
            'kernel_plane_basis': [[str(v) for v in row] for row in chart['kernel'].tolist()],
            'affine_conic_equation': str(chart['quadric']),
            's_of_t': str(chart['graph']),
            'positive_parent_parameter_region': str(positive_parent_region(chart)),
            'positive_parent_coordinates': [str(v) for v in chart['rational_coordinates']],
            'positive_fourmass_preimage_count': sum(p['strictly_positive_on_fourmass_wall'] for p in preimages),
            'fourmass_solutions': [],
            'positive_parent_interval_endpoints': [],
            'nonnegative_parent_parameter_region': str(reduce_rational_inequalities(
                [[v >= 0 for v in chart['rational_coordinates']]], chart['t'])),
        }
        for endpoint in EXPECTED_PARENT_INTERVALS[name]:
            vector = [simplify(v.subs(chart['t'], endpoint)) for v in chart['rational_coordinates']]
            record['positive_parent_interval_endpoints'].append({
                'parameter': str(endpoint), 'coefficients': [str(v) for v in vector],
                'zero_coordinates': [COORDINATES[i] for i,v in enumerate(vector) if v == 0],
            })
        for preimage in preimages:
            solution = {key: value if isinstance(value, bool) else
                        [str(v) for v in value] if isinstance(value, tuple) else str(value)
                        for key, value in preimage.items()}
            if preimage['strictly_positive_on_fourmass_wall']:
                solution['oriented_map_jacobian'] = str(fourmass_map_jacobian(preimage['coefficients'], z))
                mapped = source_matrix(preimage['coefficients']) * z
                change = mapped[:, :2] * y[:, :2].inv()
                if change * y != mapped:
                    raise AssertionError('Preimage row-space equality failed')
                solution['exact_image_row_change'] = [[str(v) for v in row] for row in change.tolist()]
            record['fourmass_solutions'].append(solution)
        result['scenarios'][name] = record
    return result


def normalized_anchor_gauge_exists(cell):
    """Whether the source stratum has three distinct nonzero A,C,D directions."""
    colors = {i: j for j, block in enumerate(cell.classes) for i in block}
    directions = [{colors[i] for i in block if i in colors}
                  for block in ((1, 2), (5, 6), (7, 8, 9))]
    return all(len(d) == 1 for d in directions) and len(set.union(*directions)) == 3


def closed_facet_exclusion_data():
    """Finite exact certificate excluding all other closed source-facet images.

    Completeness uses the classical rank-two source closure description.
    The two exhaustive source algorithms are compared in the tests. No
    sampled differential ranks enter this certificate.
    """
    from .rank2 import RankTwoCell, cell_from_bases, cells, facets
    from .parent_relations import class_complement_obstruction, classify_cell

    parent = RankTwoCell(9, ((1, 2), (3, 4), (5, 6), (7, 8, 9)))
    parent_bases = set(parent.bases)
    closure = sorted((c for c in cells(9) if set(c.bases) <= parent_bases),
                     key=lambda c: c.affine)
    z = moment_z()
    y = source_matrix(SCENARIOS['two_positive_fourmass_preimages']) * z
    twistors = {indices: y.col_join(z[[i-1 for i in indices], :]).det()
                for indices in combinations(range(1, 10), 4)}
    if any(value == 0 for value in twistors.values()):
        raise AssertionError('The general-position target certificate failed')
    chart = conic_chart(y, z)
    endpoint_strata = []
    for endpoint in EXPECTED_PARENT_INTERVALS['two_positive_fourmass_preimages']:
        point = tuple(v.subs(chart['t'], endpoint) for v in chart['rational_coordinates'])
        c = source_matrix(point)
        bases = []
        for i, j in combinations(range(1, 10), 2):
            minor = c[:, [i-1, j-1]].det()
            if minor < 0:
                raise AssertionError('A fiber endpoint has a negative source minor')
            if minor > 0:
                bases.append((i, j))
        endpoint_strata.append(cell_from_bases(9, bases))
    bad = []
    for cell in closure:
        if normalized_anchor_gauge_exists(cell):
            continue
        obstruction = class_complement_obstruction(cell)
        if obstruction is None:
            raise AssertionError('An unhandled source gauge degeneration remains')
        outside = set(obstruction['outside_support'])
        witness = next(indices for indices in twistors if outside <= set(indices))
        bad.append({'affine': cell.affine,
                    'parallel_class': obstruction['parallel_class'],
                    'outside_support': obstruction['outside_support'],
                    'forced_zero_twistor': witness})
    source_facets = []
    for cell in facets(parent):
        source_facets.append({'affine': cell.affine, 'classes': cell.classes,
                              'loops': cell.loops, 'admissibility': classify_cell(cell),
                              'closed_image_contains_target': any(
                                  set(endpoint.bases) <= set(cell.bases) for endpoint in endpoint_strata)})
    return {
        'scope': 'Exact fixed-Z closed-image exclusion; not a theorem about arbitrary tile covers',
        'parent_classes': parent.classes,
        'Y_representative': [[int(v) for v in row] for row in y.tolist()],
        'source_closure_stratum_count': len(closure),
        'source_closure_affines': [c.affine for c in closure],
        'non_normalizable_stratum_count': len(bad),
        'non_normalizable_stratum_obstructions': bad,
        'all_126_nonzero_twistors': [{'indices': i, 'value': int(v)} for i, v in twistors.items()],
        'source_facets': source_facets,
        'conic_evidence_fixture': 'fixtures/run3/hostile_conic_multiplicity.json',
        'conic_evidence_scenario': 'two_positive_fourmass_preimages',
        'endpoint_stratum_affines': [cell.affine for cell in endpoint_strata],
        'admissible_facet_count': sum(f['admissibility']['status'] == 'CERTIFIED_TILE'
                                    for f in source_facets),
        'only_closed_source_facet_image_containing_target': '(12)(34)(56)(78), loop9',
        'positive_parent_interior_parameter': '5/2',
        'positive_parent_interior_d9': '779/161882',
        'quadric_s_derivative_at_interior_point': '11563/56',
        'proof_reference': 'research/run3/MULTIPLICITY.md',
    }


if __name__ == '__main__':
    data = fixture_data()
    path = Path(__file__).resolve().parents[2] / 'fixtures' / 'run3' / 'hostile_conic_multiplicity.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + '\n')
    exclusion_path = path.with_name('hostile_closed_facet_exclusion.json')
    exclusion_path.write_text(json.dumps(closed_facet_exclusion_data(), indent=2) + '\n')
    print(json.dumps({name: {key: value for key,value in case.items() if key in (
        'affine_conic_equation', 'positive_parent_parameter_region', 'positive_fourmass_preimage_count')}
        for name,case in data['scenarios'].items()}, indent=2))
