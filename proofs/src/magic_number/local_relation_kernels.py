"""Exact spanning-tree overlaps for five already proved ten-wall relations.

An edge certifies a nonempty open overlap of two opposite-side tiles by
exhibiting two exact positive source points with equal image row spaces.
The previously proved same-side partitions supply absence of other open
indicators on that overlap. No complete chamber or tiling enumeration occurs.
"""
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from random import Random
import json

from sympy import Matrix, Rational, zeros

from .linear_parent_fibers import source_matrix as linear_source
from .spurion_relation import source_matrix as spurion_source
from .smaller_parent_fibers import reflected_source
from .q10_parent_fibers import source_matrix as q10_source
from .rank2 import cell_from_bases
from .run4_hostile import serializable

FAMILIES = {
    'n8_alternating': (8,(0,1),'fixtures/run3/linear_n8_alternating.json','research/run3/LARGER_SUPPORT.md'),
    'n9_spurion': (9,(0,1),'fixtures/run2/spurion_repaired_candidate.json','research/run2/SPURION_ATTEMPT.md'),
    'n9_reflected_1323': (9,(8,9),'fixtures/run4/smaller_core_relations.json','research/run4/SMALLER_CORES.md'),
    'n10_433': (10,(5,6),'fixtures/run4/q10_433.json','research/run4/Q10_334.md'),
    'n10_424': (10,(4,5),'fixtures/run4/q10_424.json','research/run4/Q10_334.md'),
}


def source(name,x):
    if name == 'n8_alternating': return linear_source(x,'alternating')
    if name == 'n9_spurion': return spurion_source(x)
    if name == 'n9_reflected_1323': return reflected_source(x)
    return q10_source(x,(4,3,3) if name == 'n10_433' else (4,2,4))


def wall_cell(name,i):
    n = FAMILIES[name][0]
    x = [1]*10
    x[i] = 0
    c = source(name,x)
    values = {pair:c[:,[j-1 for j in pair]].det() for pair in combinations(range(1,n+1),2)}
    assert all(value >= 0 for value in values.values())
    return cell_from_bases(n,[pair for pair,value in values.items() if value > 0])


def relation_data(name):
    path = Path(FAMILIES[name][2])
    raw = path.read_bytes()
    data = json.loads(raw)
    if name == 'n9_reflected_1323': data = data['reflected_1323']
    coefficients = tuple(row['coefficient'] for row in data['walls'])
    assert len(coefficients) == 10 and sum(coefficients) == 0
    assert set(coefficients) == {-1,1}
    return coefficients,sha256(raw).hexdigest()


def ambient_kernel(name,y,z):
    """Independent ambient12x14 elimination, then normalize two source rows."""
    columns = []
    for i in range(10):
        e = [0]*10
        e[i] = 1
        columns.append(Matrix(list(source(name,e)*z)))
    for i in range(4):
        e = zeros(2,2)
        e[i//2,i%2] = 1
        columns.append(-Matrix(list(e*y)))
    matrix = Matrix.hstack(*columns)
    nullspace = Matrix.hstack(*matrix.nullspace())
    assert nullspace.cols == 2
    coeff = nullspace[:10,:]
    pivot = list(FAMILIES[name][1])
    return coeff*coeff[pivot,:].inv()


def endpoint_pair(name,seed,z):
    seed = Matrix(seed)
    y = source(name,seed)*z
    k = ambient_kernel(name,y,z)
    p,q = FAMILIES[name][1]
    h = k*Matrix([seed[q],-seed[p]])
    lower = max(-seed[i]/h[i] for i in range(10) if h[i] > 0)
    upper = min(-seed[i]/h[i] for i in range(10) if h[i] < 0)
    assert lower < 0 < upper
    records = []
    for parameter in (lower,upper):
        point = seed+parameter*h
        zero = [i for i,value in enumerate(point) if value == 0]
        if len(zero) != 1: return None
        assert all(value > 0 for i,value in enumerate(point) if i != zero[0])
        c = source(name,point)
        mapped = c*z
        change = mapped[:,:2]*y[:,:2].inv()
        assert change.det() != 0 and change*y == mapped
        records.append({'wall_index':zero[0],'source_coefficients':tuple(point),
                        'source_matrix':c.tolist(),'image_row_change':change.tolist(),
                        'fiber_parameter':parameter})
    return {'source_seed':tuple(seed),'target_representative':y.tolist(),
            'fiber_tangent':tuple(h),'endpoints':records}


@lru_cache(maxsize=None)
def spanning_tree_fixture(name,bound=99):
    if not 1 <= bound <= 99: raise ValueError('This bounded task allows at most99 source seeds')
    n,pivot,path,proof = FAMILIES[name]
    z = Matrix([[i**j for j in range(6)] for i in range(1,n+1)])
    coefficients,digest = relation_data(name)
    components = list(range(10))
    tree,all_edges = [],set()
    rng = Random(4400+list(FAMILIES).index(name))
    for trial in range(bound):
        seed = [Rational(rng.randint(1,9)) for _ in range(10)]
        if trial >= 30: seed[(trial-30)%10] = Rational(1,1000)
        pair = endpoint_pair(name,seed,z)
        if pair is None: continue
        i,j = (row['wall_index'] for row in pair['endpoints'])
        assert coefficients[i] == -coefficients[j]
        all_edges.add(tuple(sorted((i,j))))
        if components[i] != components[j]:
            old,new = components[j],components[i]
            components = [new if value == old else value for value in components]
            pair['trial_index'] = trial
            tree.append(pair)
        if len(tree) == 9: break
    incidence = zeros(len(tree),10)
    for row,edge in enumerate(tree):
        for endpoint in edge['endpoints']: incidence[row,endpoint['wall_index']] = 1
    assert incidence*Matrix(coefficients) == zeros(len(tree),1)
    walls = []
    for i in range(10):
        cell = wall_cell(name,i)
        walls.append({'wall_index':i,'affine':cell.affine,'classes':cell.classes,
                      'bases':cell.bases,'coefficient':coefficients[i]})
    connected = len(tree) == 9
    if connected:
        assert incidence.rank() == 9
        assert len(incidence.nullspace()) == 1
    return {'family':name,'n':n,'scope':'At this exact Z and for constant-coefficient all-Z relations; not every fixed Z',
            'source_relation_fixture':path,'source_relation_sha256':digest,'source_relation_proof':proof,
            'external_matrix':z.tolist(),'positive_external_certificate':'Strictly positive Vandermonde six-minors',
            'pivot_indices':pivot,'walls':walls,'canonical_relation_coefficients':coefficients,
            'seed_bound':bound,'seeds_used':trial+1,'distinct_edges_found':sorted(all_edges),
            'connected':connected,'spanning_tree':tree,'edge_incidence_matrix':incidence.tolist(),
            'incidence_rank':incidence.rank(),'certified_relation_space_dimension':1 if connected else None,
            'proof_reference':'research/run4/LOCAL_RELATION_KERNELS.md'}


def main():
    data = {name:spanning_tree_fixture(name) for name in FAMILIES}
    Path('fixtures/run4/local_relation_kernels.json').write_text(json.dumps(serializable(data),indent=2)+'\n')
    report = {name:{key:value for key,value in fixture.items() if key in (
        'scope','connected','seeds_used','seed_bound','incidence_rank','certified_relation_space_dimension')}
              for name,fixture in data.items()}
    Path('results/run4/local_relation_kernels.json').write_text(json.dumps(serializable(report),indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__': main()
