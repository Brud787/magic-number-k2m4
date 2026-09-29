"""Independent literal-basis transport and Fraction audit of normalized zeros."""

from fractions import Fraction
import json
from pathlib import Path

from . import affine
from .run6_membership_cores import classify, loopless_eight_cells


ROOT=Path(__file__).resolve().parents[2]


def determinant(matrix):
    rows=[list(map(Fraction,row)) for row in matrix]
    result=Fraction(1)
    for i in range(len(rows)):
        pivot=next((j for j in range(i,len(rows)) if rows[j][i]),None)
        if pivot is None:
            return Fraction(0)
        if pivot!=i:
            rows[i],rows[pivot]=rows[pivot],rows[i]
            result=-result
        value=rows[i][i]
        result*=value
        for j in range(i+1,len(rows)):
            ratio=rows[j][i]/value
            if ratio:
                for k in range(i+1,len(rows)):
                    rows[j][k]-=ratio*rows[i][k]
                rows[j][i]=0
    return result


def audit_normalized_zeros():
    data=json.loads((ROOT/"results/run7/normalized_core_ranks.json").read_text())
    source=json.loads((ROOT/"results/run4/sign_relations.json").read_text())["relations"]
    prototypes={r["id"]:r for r in source}
    reports=[]
    for record in data["normalized_cores"]:
        n=record["n"]
        if n not in (10,11):
            continue
        expected=set()
        for q in (n-1,n):
            for cell in loopless_eight_cells(q):
                if classify(cell)["status"]=="CERTIFIED_TILE":
                    offset=n-q
                    expected.add(tuple(tuple(i+offset for i in b) for b in cell.bases))
        actual=[]
        for c in record["columns"]:
            bases=affine.bases(c["affine"])
            assert affine.dimension(c["affine"])==8
            assert set(c["loops"])<= {1}
            actual.append(bases)
        assert len(actual)==len(set(actual)) and set(actual)==expected
        index={b:i for i,b in enumerate(actual)}
        checked_origins=0
        for row,certificate in zip(record["rows"],record["projected_parent_rows"]):
            assert row==certificate["row"]
            assert affine.dimension(certificate["parent_affine"])==9
            for origin in certificate["transport_origins"]:
                prototype=prototypes[origin["prototype_id"]]
                q=prototype["n"]
                mapping={i:origin["support"][(origin["direction"]*(i-1)+origin["shift"])%q]
                         for i in range(1,q+1)}
                def transform(bases):
                    return tuple(sorted(tuple(sorted(mapping[i] for i in b)) for b in bases))
                assert transform(affine.bases(prototype["parent_affine"]))==affine.bases(certificate["parent_affine"])
                computed=[0]*len(actual)
                for wall in prototype["signed_admissible_facets"]:
                    b=transform(affine.bases(wall["affine"]))
                    column=index.get(b)
                    if column is not None:
                        computed[column]+=origin["common_sign"]*wall["coefficient"]
                    else:
                        support={i for pair in b for i in pair}
                        assert any(i not in support for i in range(2,n+1))
                assert computed==row
                checked_origins+=1
        pivots=record["pivot_columns"]
        independent=record["independent_row_indices"]
        assert pivots==list(range(len(actual))) and len(independent)==len(actual)
        minor=[[record["rows"][i][j] for j in pivots] for i in independent]
        det=determinant(minor)
        assert det and str(det)==record["minor_determinant_exact"]
        reports.append({"n":n,"complete_normalized_column_count":len(actual),
                        "certified_projected_rows":len(record["rows"]),
                        "literal_transports_checked":checked_origins,
                        "independent_Fraction_determinant":str(det),
                        "normalized_quotient_is_zero":True})
    assert len(reports)==2
    return {"claim_tag":"COMPUTATIONALLY-VERIFIED exact independent certificate",
            "scope":"All normalized generators eliminated at source sizes10 and11",
            "records":reports,"no_full_n10_matrix":True,
            "simplicial_and_amalgamation_scope":"REQUIRE SEPARATE GEOMETRIC PROOFS"}


if __name__=="__main__":
    output=audit_normalized_zeros()
    (ROOT/"results/run7/normalized_independent_review.json").write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps(output,indent=2))
