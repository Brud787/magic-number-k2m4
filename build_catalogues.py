"""Normalize preserved data into release catalogues; never writes research paths.

This producer is NOT called by verify_all.py. Verification reconstructs data.
"""
import json
from pathlib import Path
from collections import Counter
from independent.combinatorics import bases, classes, profile, affine, loopless, mechanism, transform

ROOT = Path(__file__).resolve().parent
C = ROOT/'certificates'


def read(name):
    return json.loads((C/name).read_text())


def write(name, data):
    (C/name).write_text(json.dumps(data, indent=2)+'\n')


def main():
    members = []
    historical = read('membership/historical_cores.json')
    by_type = {tuple(c['dihedral_composition_type']): c for c in historical['cores']}
    for q in range(6, 11):
        for key in sorted(loopless(q, 8), key=lambda b: affine(q, b)):
            blocks = classes(key)
            orbit = {}
            for direction in (-1, 1):
                for shift in range(q):
                    mapping = {i: 1+(direction*(i-1)+shift) % q for i in range(1, q+1)}
                    orbit[(direction, shift)] = transform(key, mapping)
            old = by_type[profile(blocks)]
            assert affine(q, key) in list(map(tuple, old['labeled_affine_permutations']))
            members.append(dict(id=f'M{len(members)+1:03d}', q=q, s=len(blocks),
                classes=blocks, class_sizes=list(map(len, blocks)), bases=key, affine=affine(q, key),
                dihedral_type=profile(blocks), orbit_representative=old['representative_affine'],
                orbit_size=len(set(orbit.values())), stabilizer=[list(a) for a, b in orbit.items() if b == key],
                membership_status=old['status'], mechanism=mechanism(key), historical_id=old['id']))
    write('membership/catalogue.json', dict(schema_version=1, cells=members,
        counts={str(q):sum(c['q']==q and c['membership_status']=='CERTIFIED_TILE' for c in members) for q in range(6,11)}))
    core_data = read('local/parents_historical.json')['cores']
    relations = {tuple(r['core_type']):r for r in read('local/relations_historical.json')['relations']}
    parents = []
    for i, old in enumerate(sorted(core_data, key=lambda c:(c['q'],c['dihedral_composition_type'])), 1):
        pid = f'P{i:03d}'
        walls = sorted(old['source_walls'], key=lambda w:w['affine'])
        facets = [dict(id=f'{pid}-F{j:02d}', classes=w['classes'], affine=w['affine'],
                       mechanism=mechanism(bases(w['classes'])), admissible=w['status']=='CERTIFIED_TILE')
                  for j,w in enumerate(walls,1)]
        r = relations.get(tuple(old['dihedral_composition_type']))
        coeff = {tuple(w['affine']):w['coefficient'] for w in r['signed_admissible_facets']} if r else {}
        if r:
            assert tuple(r['parent_affine']) == tuple(old['representative_affine'])
        vector = [coeff.get(tuple(f['affine']),0) for f in facets]
        assert sum(vector) == 0
        count = old['certified_admissible_wall_count']
        sector = {0:'collapsed',6:'complement-five 3<->3',10:'reflection/spurion 5<->5',8:'hostile'}[count]
        parents.append(dict(id=pid, historical_id=old['id'], q=old['q'], s=old['s'],
            classes=old['parallel_classes'], class_sizes=list(map(len,old['parallel_classes'])),
            dihedral_type=old['dihedral_composition_type'], affine=old['representative_affine'],
            labeled_orbit_size=old['labeled_loopless_count'], facets=facets, sector=sector,
            relation_dimension=old['all_Z_relation_space_dimension'], relation_vector=vector,
            positive_facets=[f['id'] for f,v in zip(facets,vector) if v==1],
            negative_facets=[f['id'] for f,v in zip(facets,vector) if v==-1],
            mechanism=old.get('mechanism'), proof=old.get('proof_reference'),
            historical_relation_id=r['id'] if r else None))
    write('local/parents.json',dict(schema_version=1,parents=parents))
    lines=['# Complete parent catalogue','', 'Facet IDs and vectors use the order in `parents.json`; coefficients on excluded facets are zero.','',
        '| ID | q,s | Cyclic sizes | Sector | Kernel dimension | Positive facets | Negative facets |',
        '|---|---|---|---|---:|---|---|']
    for p in parents:
        lines.append(f"| {p['id']} | {p['q']},{p['s']} | {p['class_sizes']} | {p['sector']} | {p['relation_dimension']} | {', '.join(p['positive_facets'])} | {', '.join(p['negative_facets'])} |")
    (C/'local/PARENTS.md').write_text('\n'.join(lines)+'\n')
    raw = read('local/overlaps_historical.json')
    witnesses=[]
    def parent_mapping(key,p):
        q=p['q']; target=bases(p['classes'])
        for direction in (-1,1):
            for shift in range(q):
                mapping={i:1+(direction*(i-1)+shift)%q for i in range(1,q+1)}
                if transform(key,mapping)==target:
                    return mapping
        raise AssertionError('No dihedral identification of prototype parent')
    for family,data in raw.items():
        # The wall union recovers the prototype parent basis set.
        key=tuple(sorted({tuple(b) for w in data['walls'] for b in w['bases']}))
        p=next(p for p in parents if tuple(p['dihedral_type'])==profile(classes(key)))
        mapping=parent_mapping(key,p)
        facet_index={tuple(f['affine']):f['id'] for f in p['facets']}
        facet_ids=[facet_index[affine(p['q'],transform(tuple(map(tuple,w['bases'])),mapping))] for w in data['walls']]
        for j, edge in enumerate(data['spanning_tree'],1):
            witnesses.append(dict(id=f"{p['id']}-W{j:02d}",parent_id=p['id'],family=family,
                historical_edge_index=j-1,external_matrix=data['external_matrix'],
                prototype_to_parent_labels=mapping,wall_facet_ids=facet_ids,
                equation_facet_ids=[facet_ids[e['wall_index']] for e in edge['endpoints']],**edge))
    assert len(witnesses)==45
    write('local/overlap_witnesses.json',dict(witnesses=witnesses))
    hostiles=[]
    for q in (8,9):
        d=read(f'local/hostile_q{q}.json');key=bases(d['parent_classes'])
        p=next(p for p in parents if tuple(p['dihedral_type'])==profile(classes(key)))
        mapping=parent_mapping(key,p)
        index={tuple(f['affine']):f['id'] for f in p['facets']}
        hostiles.append(dict(id=f'LOCAL-HOSTILE-{q}',parent_id=p['id'],
            prototype_to_parent_labels=mapping,source_file=f'hostile_q{q}.json',
            column_facet_ids=[index[affine(q,transform(bases(f['source_classes']),mapping))] for f in d['ordered_admissible_facets']],
            witness_ids=[f"{p['id']}-H{i+1:02d}" for i in range(8)],
            matrix=[[int(v) for v in row] for row in d['indicator_matrix']],determinant='1'))
    write('local/hostile_index.json',dict(cores=hostiles))
    raw=read('n9/indicator_historical.json')
    keys_by_affine={affine(9,b):b for b in __import__('independent.combinatorics',fromlist=['tiles']).tiles(9)}
    write('n9/tiles.json',dict(tiles=[dict(id=f'N9-T{i+1:04d}',column=i,affine=w,classes=classes(keys_by_affine[tuple(w)])) for i,w in enumerate(raw['column_affine_permutations'])]))
    write('n9/witnesses.json',dict(external_matrix=raw['external_matrix'],witnesses=[dict(id=f'N9-W{i+1:04d}',row=i,**r) for i,r in enumerate(raw['target_records'])]))
    write('n9/A9.json',dict(row_ids=[f'N9-W{i+1:04d}' for i in range(472)],column_ids=[f'N9-T{i+1:04d}' for i in range(942)],rows=raw['indicator_rows'],minor_columns=raw['minor_column_indices'],minor_determinant='4'))
    local=read('n9/local_historical.json')
    write('n9/R9.json',dict(row_ids=[f'N9-R{i+1:04d}' for i in range(693)],column_ids=[f'N9-T{i+1:04d}' for i in range(942)],rows=local['rows'],pivot_columns=local['pivot_columns'],independent_rows=local['independent_row_indices'],rref=local['rref_nonzero_rows'],minor_determinant=local['rank_certificate']['minor_determinant_exact']))
    for r in read('normalized/historical.json')['normalized_cores']:
        n=r['n']
        write(f'normalized/N{n}.json',dict(**r,column_ids=[f'N{n}-T{i+1:03d}' for i in range(len(r['columns']))],row_ids=[f'N{n}-R{i+1:03d}' for i in range(len(r['rows']))]))
    print('Built membership, parent, relation, overlap, n9, and normalized catalogues.')


if __name__=='__main__':
    main()
