"""Independent exact audit of every n9 indicator decision.

No producer inverse is imported. Complement-five decisions use six-row
ambient frames, SymPy rational inversion and every source minor. Spurions
use a 12x13 ambient system retaining the four unknown image frame entries,
instead of the producer's 8x9 quotient system.
"""

from collections import Counter
from functools import lru_cache
import hashlib
from itertools import combinations
import json
from pathlib import Path
from time import monotonic

from sympy import Matrix, Rational, zeros

from . import affine
from .rank2 import cell_from_bases


ROOT=Path(__file__).resolve().parents[2]
INPUT=ROOT/"results/run6/indicator_kernel_n9.json"
OUTPUT=ROOT/"results/run6/indicator_membership_independent.json"


def _charts(data):
    z=Matrix(data["external_matrix"])
    assert z.shape==(9,6)
    assert all(z[list(labels),:].det()>0 for labels in combinations(range(9),6))
    assert len(set(map(tuple,data["column_affine_permutations"])))==942
    frames={}
    result=[]
    for window in data["column_affine_permutations"]:
        assert affine.dimension(window)==8
        cell=cell_from_bases(9,affine.bases(window))
        distinguished=next((i for i,b in enumerate(cell.classes)
                            if len(b)==len(cell.support)-5),None)
        if distinguished is None:
            assert tuple(map(len,cell.classes))==(3,3,3)
            blocks=cell.classes
        else:
            blocks=cell.classes[distinguished+1:]+cell.classes[:distinguished+1]
        labels=tuple(i for b in blocks for i in b)
        signs=tuple(-1 if i<labels[0] else 1 for i in labels)
        external=Matrix([[sign*v for v in z[label-1,:]] for label,sign in zip(labels,signs)])
        # Discrete parity verifies the external row transport for every Z.
        for subset in combinations(range(len(labels)),6):
            order=[labels[i] for i in subset]
            inversion_count=sum(order[i]>order[j] for i in range(6) for j in range(i+1,6))
            assert (-1)**inversion_count * __import__('math').prod(signs[i] for i in subset)==1
        chart={"cell":cell,"blocks":blocks,"labels":labels,"signs":signs,"external":external,
               "family":"SPURION" if distinguished is None else "COMPLEMENT_FIVE"}
        if distinguished is not None:
            assert sum(map(len,blocks[:-1]))==5 and len(blocks)-1+len(blocks[-1])==6
            frame_key=tuple(zip(labels[:6],signs[:6]))
            if frame_key not in frames:
                frames[frame_key]=external[:6,:].inv(method="DM")
            chart["frame_key"],chart["frame_inverse"]=frame_key,frames[frame_key]
        result.append(chart)
    return z,result


def _source_minors(source):
    return {(i+1,j+1):source[0][i]*source[1][j]-source[0][j]*source[1][i]
            for i,j in combinations(range(len(source[0])),2)}


def _complement(chart,y,cache):
    key=chart["frame_key"]
    if key not in cache:
        coordinates=y*chart["frame_inverse"]
        h0,h1=coordinates[0,5],coordinates[1,5]
        assert h0 or h1
        raw=[h1*coordinates[0,i]-h0*coordinates[1,i] for i in range(5)]
        assert all(raw)
        if min(raw)<0<max(raw):
            cache[key]=None
        else:
            a=[v/raw[0] for v in raw]
            image_index=0 if h0 else 1
            multiplier=1 if coordinates[image_index,5]>0 else -1
            second=[multiplier*v for v in y[image_index,:]]
            change=Matrix([[h1/raw[0],-h0/raw[0]],
                           [multiplier if image_index==0 else 0,
                            multiplier if image_index==1 else 0]])
            cache[key]=(a,second,change)
    recovered=cache[key]
    if recovered is None:
        return 0,"MIXED"
    a,second,change=recovered
    assert all(v>0 for v in a) and change.det()!=0
    blocks,external=chart["blocks"],chart["external"]
    ell=len(blocks)-1
    rows=[]
    position=0
    for block in blocks[:-1]:
        rows.append([sum(a[i]*external[i,j] for i in range(position,position+len(block)))
                     for j in range(6)])
        position+=len(block)
    rows.extend([list(external[i,:]) for i in range(5,external.rows)])
    # Independent backend and full ambient equation; no root cached solve.
    coefficients=Matrix(rows).T.inv(method="DM")*Matrix(second)
    first=list(a)+[0]*(external.rows-5)
    second_source=[]
    position=0
    for block_index,block in enumerate(blocks[:-1]):
        second_source.extend(coefficients[block_index]*a[i]
                             for i in range(position,position+len(block)))
        position+=len(block)
    second_source.extend(coefficients[ell:])
    source=[[Rational(0)]*9 for _ in range(2)]
    for i,(label,sign) in enumerate(zip(chart["labels"],chart["signs"])):
        source[0][label-1]=sign*first[i]
        source[1][label-1]=sign*second_source[i]
    # Check ambient row-space equality without invoking any producer helper.
    assert Matrix([first,second_source])*external==change*y
    minors=_source_minors(source)
    indicator=int(all(value>=0 for value in minors.values()))
    if indicator:
        assert {pair for pair,value in minors.items() if value>0}==set(chart["cell"].bases)
    else:
        assert any(value<0 for value in minors.values())
    assert all([coefficients[j+1]-coefficients[j] for j in range(ell-1)]+list(coefficients[ell:]))
    return indicator,"SIX_ROW"


def _spurion(chart,y,saved):
    external=chart["external"]
    columns=[]
    for i in range(9):
        row=list(external[i,:])
        columns.append(Matrix((row if i<6 else [0]*6)+(row if i>=3 else [0]*6)))
    columns.extend((Matrix(list(-y[0,:])+[0]*6),Matrix(list(-y[1,:])+[0]*6),
                    Matrix([0]*6+list(-y[0,:])),Matrix([0]*6+list(-y[1,:]))))
    ambient=Matrix.hstack(*columns)
    null=ambient.nullspace(simplify=False)
    assert len(null)==1
    vector=null[0]
    assert all(vector[:9]) and ambient*vector==zeros(12,1)
    for start in (0,3,6):
        assert Matrix.vstack(y,external[start:start+3,:]).rank()==5
    x=vector[:9]
    indicator=int(all(v>0 for v in x) or all(v<0 for v in x))
    normalized=[v/x[0] for v in x]
    published=[Rational(v) for v in saved["kernel_coefficients"]]
    assert normalized==[v/published[0] for v in published]
    assert saved["fiber_rank"]==8 and saved["indicator"]==indicator
    return indicator


@lru_cache(maxsize=1)
def audit_all(progress=False):
    start=monotonic()
    data=json.loads(INPUT.read_text())
    z,charts=_charts(data)
    assert len(charts)==942 and Counter(c["family"] for c in charts)=={"COMPLEMENT_FIVE":939,"SPURION":3}
    column_pairs=tuple(combinations(range(6),2))
    covectors=[]
    for labels in combinations(range(9),4):
        external=z[list(labels),:]
        covectors.append([(-1)**(i+j+1)*external[:,[h for h in range(6) if h not in (i,j)]].det()
                          for i,j in column_pairs])
    totals=Counter()
    for row_index,record in enumerate(data["target_records"]):
        y=Matrix(record["target_representative"])
        source=Matrix(record["source_matrix"])
        assert source*z==y
        source_minors=_source_minors(source.tolist())
        assert all(v>=0 for v in source_minors.values())
        assert {b for b,v in source_minors.items() if v>0}==set(affine.bases(record["source_affine"]))
        pluckers=[y[0,i]*y[1,j]-y[0,j]*y[1,i] for i,j in column_pairs]
        twistors=[sum(a*b for a,b in zip(covector,pluckers)) for covector in covectors]
        assert len(twistors)==126 and all(twistors)
        saved_spurions={v["column"]:v["certificate"] for v in record["spurion_certificates"]}
        vector=[];cache={}
        for column,chart in enumerate(charts):
            if chart["family"]=="COMPLEMENT_FIVE":
                value,kind=_complement(chart,y,cache)
            else:
                value,kind=_spurion(chart,y,saved_spurions[column]),"SPURION"
            totals[kind]+=1
            vector.append(value)
        assert vector==record["indicator_vector"]==data["indicator_rows"][row_index]
        if progress and (row_index+1)%16==0:
            print(f'Independent ambient audit {row_index+1}/472 targets; {monotonic()-start:.1f}s',flush=True)
    assert len(data["target_records"])==472 and sum(totals.values())==444624
    payload=json.dumps({k:data[k] for k in ("external_matrix","column_affine_permutations","indicator_rows","target_records")},sort_keys=True)
    return {"claim_tag":"COMPUTATIONALLY-VERIFIED exact independent membership certificate",
            "source_reference":"results/run6/indicator_kernel_n9.json",
            "audited_payload_sha256":hashlib.sha256(payload.encode()).hexdigest(),
            "target_count":472,"tile_count":942,"exact_membership_decisions":sum(totals.values()),
            "decision_counts":dict(totals),"twistors_independently_nonzero":472*126,
            "spurion_ambient_system_shape":[12,13],"independent_backend":"SymPy exact rational ambient equations",
            "all_source_minors_checked_when_inverse_exists":True,
            "all_indicator_rows_match":True,"elapsed_seconds":round(monotonic()-start,3),
            "scope":"Full fixed-Z open-neighborhood membership audit; no all-n generation assertion"}


def main():
    result=audit_all(progress=True)
    OUTPUT.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":
    main()
