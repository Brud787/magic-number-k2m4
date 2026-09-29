"""Exact indicator-rank obstructions for the two hostile Run 4 parents.

Fixed-positive-Z countercertificates to homogeneous all-Z tile relations.
Completeness of each tile-membership decision is proved in the companion note.
"""
from functools import lru_cache
from itertools import combinations
from pathlib import Path
from random import Random
import json
from sympy import Matrix, Rational, factor, sign, solve, symbols
from .conic_fibers import kernel_plane as conic_kernel, proportionality_quadric
from .conic_fibers import source_matrix as conic_source
from .linear_parent_fibers import normalized_fiber_basis, source_matrix as linear_source
from .parent_relations import class_complement_obstruction, classify_cell
from .rank2 import RankTwoCell, cells, facets

PARENTS = {8: RankTwoCell(8, ((1,2),(3,4),(5,6),(7,),(8,))),
           9: RankTwoCell(9, ((1,2),(3,4),(5,6),(7,8,9)))}
ANCHORS = {8: ((1,2),(3,4),(5,6)), 9: ((1,2),(5,6),(7,8,9))}
WALLS = {8: ((0,),(1,),(2,),(3,),(4,),(5,),(6,),(9,)),
         9: ((0,),(1,),(2,3),(4,5),(6,),(7,),(3,5),(2,4))}
SEEDS = {
8: ((6,5,8,2,1,9,5,1,25,4), (5,3,2,2,1,4,4,7,Rational(26,7),3),
    (6,8,2,8,5,1,9,8,Rational(75,8),3), (4,3,9,4,1,1,1,9,Rational(79,9),7),
    (5,1,2,4,4,5,1,3,6,6), (5,1,1,9,8,6,6,7,Rational(87,7),4),
    (0,1,1,1,1,1,1,4,1,1), (1,1,1,1,1,1,1,4,1,0)),
9: ((6,1,12,2,24,4,6,2,8,5,1), (1,6,15,5,6,2,7,3,1,1,3),
    (5,3,12,2,36,6,7,4,1,7,6), (2,8,4,4,6,6,6,8,2,7,8),
    (3,4,6,2,18,6,7,8,7,2,3), (1,6,40,8,20,4,3,1,6,6,2),
    (0,1,1,1,1,1,1,2,1,1,1), (1,1,1,0,1,0,1,1,1,1,1))}


def source(n, x):
    return linear_source(x, 'adjacent') if n == 8 else conic_source(x)


def external(n, nodes=None):
    return Matrix([[i**j for j in range(6)] for i in (nodes or range(1,n+1))])


def wall_source(n, wall):
    from .rank2 import cell_from_bases
    x = [1]*(10 if n == 8 else 11)
    if n == 8: x[7] = 4
    for i in wall: x[i] = 0
    c = source(n, x)
    minors = {pair: c[:,[i-1 for i in pair]].det() for pair in combinations(range(1,n+1),2)}
    assert all(value >= 0 for value in minors.values())
    return cell_from_bases(n, [pair for pair,value in minors.items() if value > 0])


def wall_preimages(n, y, z):
    """Complete candidate in each open admissible facet at our exact targets.

    The normalized anchor chart is global on each open facet. Other source
    strata are handled by a separate closure/gauge certificate.
    """
    result = []
    if n == 8:
        k = normalized_fiber_basis(y,z,'adjacent')
        base, tangent = k*Matrix([0,1]), k*Matrix([1,-1])
        for (i,) in WALLS[n]:
            assert tangent[i] != 0
            point = base-base[i]/tangent[i]*tangent
            delta = factor(point[7]*point[8]-point[6]*point[9])
            assert delta != 0
            result.append((point,delta))
        return k,result
    k = conic_kernel(y,z)
    t,s = symbols('t s',real=True)
    for wall in WALLS[n]:
        if len(wall) == 2:
            ns = k[list(wall),:].nullspace()
            assert len(ns) == 1 and ns[0][0] != 0
            point = k*(ns[0]/ns[0][0])
        elif wall == (0,):
            xx = k*Matrix([0,1,s])
            roots = solve(proportionality_quadric(xx),s)
            assert len(roots) == 1 and roots[0].is_Rational
            point = xx.subs(s,roots[0])
        else:
            xx = k*Matrix([1,t,s])
            assert xx[wall[0]].coeff(s) == 0
            wall_roots = solve(xx[wall[0]],t)
            assert len(wall_roots) == 1
            xx = xx.subs(t,wall_roots[0])
            roots = solve(proportionality_quadric(xx),s)
            assert len(roots) == 1 and roots[0].is_Rational
            point = xx.subs(s,roots[0])
        assert proportionality_quadric(point) == 0
        result.append((point,None))
    return k,result


def target_record(n, seed):
    z = external(n)
    y = source(n,seed)*z
    k,candidates = wall_preimages(n,y,z)
    twistors = [{'indices': indices,'value': y.col_join(z[[i-1 for i in indices],:]).det()}
                for indices in combinations(range(1,n+1),4)]
    assert all(row['value'] != 0 for row in twistors)
    candidate_records,indicators = [],[]
    for wall,(point,delta) in zip(WALLS[n],candidates):
        assert all(point[i] == 0 for i in wall)
        other = [value for i,value in enumerate(point) if i not in wall]
        assert all(value != 0 for value in other)
        indicator = int(bool(all(value > 0 for value in other) and (delta is None or delta > 0)))
        indicators.append(indicator)
        candidate_records.append({'zero_coordinates': wall,'homogeneous_source_coordinates': tuple(point),
                                  'quadratic_order_minor': delta,'tile_indicator': indicator})
    return {'seed': seed,'target_representative': y.tolist(),'kernel_basis': k.tolist(),
            'all_nonzero_twistors': twistors,'wall_candidates': candidate_records,'indicator_vector': indicators}


@lru_cache(maxsize=None)
def gauge_audit(n):
    """Exhaustive source closure and every failed anchor-gauge obstruction."""
    parent = PARENTS[n]
    pb = set(parent.bases)
    closure = sorted((cell for cell in cells(n) if set(cell.bases) <= pb),key=lambda cell: cell.affine)
    bad = []
    for cell in closure:
        colors = {i:j for j,block in enumerate(cell.classes) for i in block}
        directions = [{colors[i] for i in block if i in colors} for block in ANCHORS[n]]
        good = all(len(d) == 1 for d in directions) and len(set.union(*directions)) == 3
        if good: continue
        obstruction = class_complement_obstruction(cell)
        assert obstruction is not None
        bad.append({'affine': cell.affine,'parallel_class': obstruction['parallel_class'],
                    'outside_support': obstruction['outside_support']})
    return {'n': n,'parent_classes': parent.classes,'anchor_blocks': ANCHORS[n],
            'closure_stratum_count': len(closure),'closure_affines': [cell.affine for cell in closure],
            'invalid_gauge_stratum_count': len(bad),'invalid_gauge_obstructions': bad}


@lru_cache(maxsize=None)
def indicator_rank_fixture(n):
    rows = [target_record(n,seed) for seed in SEEDS[n]]
    matrix = Matrix([row['indicator_vector'] for row in rows])
    assert matrix.shape == (8,8) and matrix.det() != 0
    wall_records = []
    for wall in WALLS[n]:
        cell = wall_source(n,wall)
        certificate = classify_cell(cell)
        assert certificate['status'] == 'CERTIFIED_TILE'
        wall_records.append({'zero_coordinates': wall,'source_classes': cell.classes,
                             'affine': cell.affine,'admissibility': certificate})
    certified_facets = {cell.affine for cell in facets(PARENTS[n])
                        if classify_cell(cell)['status'] == 'CERTIFIED_TILE'}
    assert certified_facets == {row['affine'] for row in wall_records}
    return {'scope': 'Fixed positive rational Z; excludes every nonzero constant-coefficient relation valid for all Z',
            'parent_classes': PARENTS[n].classes,'external_matrix': external(n).tolist(),
            'positivity_certificate': 'Ordered Vandermonde six-minors are strictly positive',
            'ordered_admissible_facets': wall_records,'target_records': rows,
            'indicator_matrix': matrix.tolist(),'determinant': matrix.det(),'rank': matrix.rank(),
            'local_constancy_certificate': 'All solved non-wall coordinates, q8 order minors, and all twistors are nonzero',
            'gauge_audit': gauge_audit(n),'proof_reference': 'research/run4/COUNTEREXAMPLE_SEARCH.md'}


def bounded_q8_endpoint_screen():
    records = []
    for count,seed,varying_nodes in ((80,20260906,False),(120,420260906,True)):
        rng = Random(seed)
        for index in range(count):
            nodes,last = [],0
            if varying_nodes:
                for _ in range(8):
                    last += rng.randint(1,9)
                    nodes.append(last)
            else: nodes = list(range(1,9))
            z = external(8,nodes)
            x = Matrix([rng.randint(1,9) for _ in range(10)])
            x[8] = x[6]*x[9]/x[7]+rng.randint(1,9)
            y = source(8,x)*z
            k = normalized_fiber_basis(y,z,'adjacent')
            base,h = x/(x[0]+x[1]),k*Matrix([1,-1])
            lower = max(-base[i]/h[i] for i in range(10) if h[i] > 0)
            upper = min(-base[i]/h[i] for i in range(10) if h[i] < 0)
            deltas = []
            for endpoint in (lower,upper):
                point = base+endpoint*h
                deltas.append(factor(point[7]*point[8]-point[6]*point[9]))
            records.append({'screen_seed': seed,'index': index,'nodes': nodes,'source_seed': tuple(x),
                            'compact_orthant_interval': (lower,upper),'endpoint_order_minors': deltas,
                            'endpoint_signs': [int(sign(value)) for value in deltas]})
    from collections import Counter
    histogram = Counter(tuple(row['endpoint_signs']) for row in records)
    return {'scope': 'A bounded exact screen only; no all-Z q8 cover or no-cover conclusion',
            'sample_count': len(records),'histogram': [{'signs': k,'count': v} for k,v in sorted(histogram.items())],
            'records': records}


def serializable(value):
    if isinstance(value,dict): return {key:serializable(v) for key,v in value.items()}
    if isinstance(value,(tuple,list)): return [serializable(v) for v in value]
    if value is None or isinstance(value,(str,bool,int)): return value
    return str(value)


def main():
    directory = Path('fixtures/run4')
    directory.mkdir(parents=True,exist_ok=True)
    overview = {'scope': 'Only the two hostile source-parent cores; no complete tiling search','cores': []}
    for n in (8,9):
        fixture = indicator_rank_fixture(n)
        path = directory/f'hostile_q{n}_indicator_rank.json'
        path.write_text(json.dumps(serializable(fixture),indent=2)+'\n')
        overview['cores'].append({'n': n,'rank': fixture['rank'],'determinant': fixture['determinant'],
                                  'admissible_facets': 8,'nonzero_all_Z_indicator_relation': 'EXCLUDED',
                                  'all_Z_admissible_facet_cover': 'UNRESOLVED' if n == 8 else 'EXCLUDED_BY_RUN3_OPEN_HOLE',
                                  'fixture': str(path)})
    screen = bounded_q8_endpoint_screen()
    (directory/'hostile_q8_bounded_endpoint_screen.json').write_text(json.dumps(serializable(screen),indent=2)+'\n')
    overview['bounded_endpoint_screen'] = {k:v for k,v in screen.items() if k != 'records'}
    destination = Path('results/run4/counterexample_search.json')
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(serializable(overview),indent=2)+'\n')
    print(json.dumps(serializable(overview),indent=2))


if __name__ == '__main__': main()
