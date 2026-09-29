"""Literal finite witness validation; all constructions are replayed exactly."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import hashlib
import json
from pathlib import Path
from sympy import Matrix
from independent.combinatorics import (bases, classes, profile, affine, loopless,
    mechanism, admissible, facets, tiles, transform, transported_rows)
from independent.membership import (positive_external, source_minors, prepare,
    decide, spurion, generic, twistor_covectors, replay_n9)
from .exact import determinant, rank_certificate

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT/'certificates'/path).read_text())


def membership_catalogue():
    data = read('membership/catalogue.json')
    old = read('membership/historical_cores.json')
    assert len(data['cells']) == 221
    assert len({r['id'] for r in data['cells']}) == 221
    counts = []
    for q in range(6, 11):
        rows = [r for r in data['cells'] if r['q'] == q]
        assert {bases(r['classes']) for r in rows} == set(loopless(q, 8))
        for row in rows:
            key = bases(row['classes'])
            assert affine(q, key) == tuple(row['affine'])
            assert mechanism(key) == row['mechanism']
            assert (row['membership_status']=='CERTIFIED_TILE') == admissible(key)
            assert sum(map(len,row['classes']))+row['s'] == 12
            orbit = {}
            for direction in (-1,1):
                for shift in range(q):
                    mapping={i:1+(direction*(i-1)+shift)%q for i in range(1,q+1)}
                    orbit[(direction,shift)] = transform(key,mapping)
            assert row['orbit_size'] == len(set(orbit.values()))
            assert row['stabilizer'] == [list(a) for a,b in orbit.items() if b==key]
            assert tuple(row['orbit_representative']) in {affine(q,b) for b in orbit.values()}
        counts.append(sum(admissible(bases(r['classes'])) for r in rows))
    assert counts == [1,14,36,30,5]
    assert len({tuple(r['dihedral_type']) for r in data['cells']}) == 24
    for core in old['cores']:
        actual=[r for r in data['cells'] if tuple(r['dihedral_type'])==tuple(core['dihedral_composition_type'])]
        assert {tuple(r['affine']) for r in actual} == set(map(tuple,core['labeled_affine_permutations']))
    return data


def four_mass():
    d=read('membership/four_mass_historical.json')
    z=Matrix(d['external_matrix']); positive_external(z)
    a,b=map(Matrix,d['four_mass_positive_preimages'])
    g=Matrix(d['four_mass_image_row_operation'])
    assert g.det()!=0 and b*z==g*a*z
    expected=bases(d['four_mass_classes'])
    for c in (a,b):
        minors=source_minors(c.tolist())
        assert min(minors.values())>=0
        assert tuple(p for p,v in minors.items() if v>0)==expected
    assert Matrix.vstack(a,b).rank()>2
    public=read('membership/four_mass.json')
    assert Matrix(public['Z'])==z and public['classes']==d['four_mass_classes']
    assert Matrix(public['C1'])==a and Matrix(public['C2'])==b
    assert Matrix(public['G'])==g.inv() and a*z==Matrix(public['G'])*b*z


def spurion_fixture():
    d=read('membership/spurion_inverse.json')
    z=Matrix(d['external_matrix']); positive_external(z)
    chart=prepare([bases(d['source_classes'])],z)[0]
    for row in d['cases']:
        y=Matrix(row['target'])
        assert Matrix(row['source_matrix'])*z==y
        value,_=spurion(chart,y,strict=False)
        assert value==row['open_inverse']['indicator']
        if row.get('strict_inverse') is not None:
            strict,_=spurion(chart,y)
            assert strict==row['strict_inverse']['indicator']


def parents():
    data=read('local/parents.json')['parents']
    old=read('local/parents_historical.json')['cores']
    assert len(data)==29 and [p['id'] for p in data]==[f'P{i:03d}' for i in range(1,30)]
    all_types={profile(classes(key)) for q in range(7,12) for key in loopless(q,9)}
    assert all_types=={tuple(p['dihedral_type']) for p in data}
    assert sum(len(loopless(q,9)) for q in range(7,12))==364
    sectors=Counter()
    for p in data:
        key=bases(p['classes'])
        assert sum(map(len,p['classes']))+len(p['classes'])==13
        assert affine(p['q'],key)==tuple(p['affine'])
        fs=facets(key)
        assert set(fs)=={bases(f['classes']) for f in p['facets']}
        for f in p['facets']:
            b=bases(f['classes'])
            assert affine(p['q'],b)==tuple(f['affine'])
            assert f['admissible']==admissible(b) and f['mechanism']==mechanism(b)
        count=sum(f['admissible'] for f in p['facets'])
        sectors[count]+=1
        v=p['relation_vector']
        assert len(v)==len(fs) and sum(v)==0
        if count in (6,10):
            assert Counter(x for x in v if x)=={1:count//2,-1:count//2}
            assert all(bool(x)==f['admissible'] for f,x in zip(p['facets'],v))
            assert p['relation_dimension']==1
        else:
            assert not any(v) and p['relation_dimension']==0
        historical=next(r for r in old if r['id']==p['historical_id'])
        assert historical['certified_admissible_wall_count']==count
    assert sectors=={0:12,6:10,10:5,8:2}
    prototypes=read('local/relations_historical.json')['relations']
    assert len(prototypes)==15
    for r in prototypes:
        p=next(p for p in data if p['historical_relation_id']==r['id'])
        assert {tuple(f['affine']):x for f,x in zip(p['facets'],p['relation_vector']) if x}=={
            tuple(f['affine']):f['coefficient'] for f in r['signed_admissible_facets']}
    return prototypes


def overlaps():
    data=read('local/overlaps_historical.json')
    public=read('local/overlap_witnesses.json')['witnesses']
    assert len(data)==5 and len(public)==45 and len({w['id'] for w in public})==45
    for family,d in data.items():
        z=Matrix(d['external_matrix']);positive_external(z)
        keys=[tuple(map(tuple,w['bases'])) for w in d['walls']]
        charts=prepare(keys,z)
        sign=d['canonical_relation_coefficients']
        assert Counter(sign)=={1:5,-1:5}
        edges=[]
        for edge in d['spanning_tree']:
            y=Matrix(edge['target_representative'])
            row=[0]*10
            for ep in edge['endpoints']:
                k=ep['wall_index'];row[k]=1
                coords=list(map(Fraction,ep['source_coefficients']))
                assert coords[k]==0 and all(v>0 for i,v in enumerate(coords) if i!=k)
                c=Matrix(ep['source_matrix'])
                minors=source_minors(c.tolist())
                assert min(minors.values())>=0
                assert tuple(p for p,v in minors.items() if v>0)==keys[k]
                change=Matrix(ep['image_row_change'])
                assert change.det()!=0 and c*z==change*y
            assert sum(row)==2 and sum(a*b for a,b in zip(row,sign))==0
            # Exact inverse checks every other wall as well as the two endpoints.
            rebuilt=[decide(chart,y,{})[0] for chart in charts]
            assert rebuilt==row
            edges.append(row)
        assert edges==[list(map(int,r)) for r in d['edge_incidence_matrix']] and len(edges)==9
        # Any deleted vertex gives a unimodular tree minor.
        assert abs(determinant([row[1:] for row in edges]))==1
        saved=[w for w in public if w['family']==family]
        assert len(saved)==9
        for w in saved:
            e=d['spanning_tree'][w['historical_edge_index']]
            assert w['external_matrix']==d['external_matrix']
            assert all(w[k]==v for k,v in e.items())
            parent=next(p for p in read('local/parents.json')['parents'] if p['id']==w['parent_id'])
            mapping={int(i):v for i,v in w['prototype_to_parent_labels'].items()}
            index={tuple(f['affine']):f['id'] for f in parent['facets']}
            assert w['wall_facet_ids']==[index[affine(d['n'],transform(key,mapping))] for key in keys]
            assert w['equation_facet_ids']==[w['wall_facet_ids'][ep['wall_index']] for ep in e['endpoints']]


def hostile(n):
    d=read(f'local/hostile_q{n}.json')
    z=Matrix(d['external_matrix']);positive_external(z)
    keys=[bases(f['source_classes']) for f in d['ordered_admissible_facets']]
    assert len(keys)==8
    assert set(keys)=={k for k in facets(bases(d['parent_classes'])) if admissible(k)}
    charts,covectors=prepare(keys,z),twistor_covectors(z)
    rows=[]
    for record in d['target_records']:
        y=Matrix(record['target_representative'])
        generic(y,covectors)
        cache={}
        rows.append([decide(c,y,cache)[0] for c in charts])
    assert rows==[list(map(int,r)) for r in d['indicator_matrix']] and determinant(rows)==1
    public=next(p for p in read('local/hostile_index.json')['cores'] if p['id']==f'LOCAL-HOSTILE-{n}')
    assert public['matrix']==rows and public['determinant']=='1'
    assert public['witness_ids']==[f"{public['parent_id']}-H{i+1:02d}" for i in range(8)]
    parent=next(p for p in read('local/parents.json')['parents'] if p['id']==public['parent_id'])
    mapping={int(i):v for i,v in public['prototype_to_parent_labels'].items()}
    index={tuple(f['affine']):f['id'] for f in parent['facets']}
    assert public['column_facet_ids']==[index[affine(n,transform(key,mapping))] for key in keys]


def local_n9(prototypes):
    keys=tiles(9)
    assert len(keys)==942
    old=read('n9/local_historical.json')
    public=read('n9/R9.json')
    assert public['row_ids']==[f'N9-R{i+1:04d}' for i in range(693)]
    cols=read('n9/tiles.json')['tiles']
    assert [list(affine(9,k)) for k in keys]==old['column_affine_permutations']==[r['affine'] for r in cols]
    assert [r['id'] for r in cols]==public['column_ids']==[f'N9-T{i+1:04d}' for i in range(942)]
    rebuilt=transported_rows(9,keys,prototypes)
    rows=sorted(rebuilt)
    assert len(rows)==693 and [list(r) for r in rows]==old['rows']==public['rows']
    assert all(sum(r)==0 for r in rows)
    for r,record in zip(rows,old['relations']):
        assert rebuilt[r]==set(map(tuple,record['parent_affines']))
    rank=rank_certificate(rows,942,public['pivot_columns'],public['independent_rows'],public['rref'],'-1')
    assert rank==470
    return keys,rows


def indicator_n9(keys,relations,progress):
    old=read('n9/indicator_historical.json')
    public=read('n9/A9.json')
    assert public['row_ids']==[f'N9-W{i+1:04d}' for i in range(472)]
    assert public['column_ids']==[f'N9-T{i+1:04d}' for i in range(942)]
    witnesses=read('n9/witnesses.json')
    assert witnesses['external_matrix']==old['external_matrix']
    assert len(witnesses['witnesses'])==472
    for i,(w,r) in enumerate(zip(witnesses['witnesses'],old['target_records'])):
        assert w['id']==f'N9-W{i+1:04d}' and w['row']==i
        assert all(w[k]==v for k,v in r.items())
    rows,counts,digest=replay_n9(old,keys,progress)
    assert rows==public['rows']
    assert public['minor_columns']==old['minor_column_indices']
    assert len(set(public['minor_columns']))==472
    minor=[[r[j] for j in public['minor_columns']] for r in rows]
    assert determinant(minor)==4
    sparse=[[(j,v) for j,v in enumerate(r) if v] for r in relations]
    assert all(sum(v*r[j] for j,v in s)==0 for r in rows for s in sparse)
    return counts,digest


def normalized(prototypes):
    expected=[(1,0,0,1),(15,7,6,9),(50,47,31,19),(66,121,54,12),(35,141,35,0),(5,46,5,0)]
    result=[]
    historical=read('normalized/historical.json')['normalized_cores']
    for n,expect,old in zip(range(6,12),expected,historical):
        d=read(f'normalized/N{n}.json')
        assert d['column_ids']==[f'N{n}-T{i+1:03d}' for i in range(len(d['columns']))]
        assert d['row_ids']==[f'N{n}-R{i+1:03d}' for i in range(len(d['rows']))]
        assert all(d[k]==v for k,v in old.items())
        keys=tiles(n,normalized=True)
        assert [list(affine(n,k)) for k in keys]==[r['affine'] for r in d['columns']]
        mapping={}
        for row,parents in transported_rows(n,keys,prototypes,normalized=True).items():
            for parent in parents:
                assert parent not in mapping or mapping[parent]==row
                mapping[parent]=row
        rows=[list(mapping[k]) for k in sorted(mapping)]
        assert rows==d['rows']
        assert list(sorted(mapping))==[tuple(r['parent_affine']) for r in d['projected_parent_rows']]
        rank=rank_certificate(rows,len(keys),d['pivot_columns'],d['independent_row_indices'],d['rref_rows'],d['minor_determinant_exact'])
        assert (len(keys),len(rows),rank,len(keys)-rank)==expect
        if n==10:assert d['minor_determinant_exact']=='-1'
        if n==11:assert d['minor_determinant_exact']=='1'
        result.append(n)
    assert not tiles(12,normalized=True)
    return result


def hashes():
    path=ROOT/'SHA256SUMS.txt'
    lines=path.read_text().splitlines()
    assert lines
    for line in lines:
        digest,name=line.split('  ',1)
        p=ROOT/name
        assert p.is_file() and p.resolve().is_relative_to(ROOT)
        assert hashlib.sha256(p.read_bytes()).hexdigest()==digest, f'Hash mismatch: {name}'


def unit_functional(n, replay=True):
    data=read('auxiliary/indicator_n8.json' if n==8 else 'n9/indicator_historical.json')
    unit=read(f'auxiliary/unit_n{n}.json')
    weights=list(map(Fraction,unit['weights']))
    rows=data['indicator_rows']
    assert len(weights)==len(rows)==(103 if n==8 else 472)
    assert sum(weights)==(20 if n==8 else 50)
    assert all(sum(w*row[j] for w,row in zip(weights,rows))==1 for j in range(len(rows[0])))
    if n==8 and replay:
        z=Matrix(data['external_matrix']);positive_external(z)
        keys=tiles(8)
        assert [list(affine(8,k)) for k in keys]==data['column_affine_permutations']
        charts,covectors=prepare(keys,z),twistor_covectors(z)
        for i,record in enumerate(data['target_records']):
            y=Matrix(record['target_representative']);generic(y,covectors)
            cache={}
            assert [decide(c,y,cache)[0] for c in charts]==rows[i]
    return weights


def weight_probes():
    for record in read('auxiliary/weight_probes.json')['records']:
        n=record['n'];weights=unit_functional(n,replay=False)
        rows=record['witness_metadata']
        assert len(rows)==len(weights)
        data=read('auxiliary/indicator_n8.json' if n==8 else 'n9/indicator_historical.json')
        lookup={affine(n,k):k for k in tiles(n)}
        for i,(row,weight) in enumerate(zip(rows,weights)):
            assert row['row']==i and Fraction(row['weight'])==weight
            source=tuple(data['target_records'][i]['source_affine'])
            assert tuple(row['source_affine'])==source
            key=lookup[source]
            assert tuple(row['core_profile'])==profile(classes(key))
            assert tuple(row['support'])==tuple(sorted({x for b in key for x in b}))
        for field,test in record['metadata_fit_tests'].items():
            groups={}
            for r in rows:
                value=r[field];value=tuple(value) if isinstance(value,list) else value
                groups.setdefault(value,[]).append(r['row'])
            assert len(groups)==test['group_count']
            assert sum(len({weights[i] for i in g})>1 for g in groups.values())==test['groups_with_multiple_weights']
            pair=test['first_conflicting_row_pair']
            if pair is not None:
                a,b=pair
                assert rows[a][field]==rows[b][field] and weights[a]!=weights[b]
