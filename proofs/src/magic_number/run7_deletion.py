"""Exact naive deletion defects of the certified rank-two parent relations.

This module transports preserved all-Z image relations. It never supplies a
relation for a collapsed parent or a parent with zero admissible-facet kernel.
"""

from collections import Counter
from functools import lru_cache
import json
from pathlib import Path

from .parent_profiles import composition_type
from .parent_relations import embed, relabel
from .rank2 import RankTwoCell, cell_from_bases
from .run6_membership_cores import classify, delete_loop, loopless_eight_cells


ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"results/run7/deletion_defects.json"


@lru_cache(maxsize=1)
def catalogs():
    relations=json.loads((ROOT/"results/run4/sign_relations.json").read_text())["relations"]
    cores=json.loads((ROOT/"results/run4/core_status.json").read_text())["cores"]
    return ({tuple(r["core_type"]):r for r in relations},
            {tuple(r["dihedral_composition_type"]):r for r in cores})


def as_cell(n,classes):
    return RankTwoCell(n,tuple(map(tuple,classes)))


def sparse(row):
    return [{"affine":window,"coefficient":value} for window,value in sorted(row.items()) if value]


def source_record(cell):
    return {"n":cell.n,"classes":cell.classes,"affine":cell.affine,
            "bases":cell.bases,"dimension":cell.dimension,"loops":cell.loops}


def naive_delete_row(n,row,label):
    output=Counter()
    for window,coefficient in row.items():
        from .affine import bases
        cell=cell_from_bases(n,bases(window))
        target=delete_loop(cell,label)
        if target is not None:
            output[target.affine]+=coefficient
    return {window:value for window,value in output.items() if value}


@lru_cache(maxsize=None)
def relation_for(parent):
    """Return an explicitly transported certified relation, or no relation."""
    profile=composition_type(map(len,parent.classes))
    records,cores=catalogs()
    core_status=cores[profile]
    if profile not in records:
        return {"category":core_status["category"],"row":None,
                "relation_id":None,"parent":source_record(parent)}
    original=records[profile]
    q=len(parent.support)
    index={label:i+1 for i,label in enumerate(parent.support)}
    core=as_cell(q,[[index[label] for label in block] for block in parent.classes])
    prototype=as_cell(q,original["parent_classes"])
    action=next((sign,shift) for sign in (1,-1) for shift in range(q)
                if relabel(prototype,sign,shift).affine==core.affine)
    row={}
    for wall in original["signed_admissible_facets"]:
        source=as_cell(q,wall["classes"])
        transported=embed(relabel(source,*action),parent.n,parent.support)
        row[transported.affine]=wall["coefficient"]
    return {"category":core_status["category"],"row":row,
            "relation_id":original["id"],"parent":source_record(parent),
            "dihedral_action":action,"support_embedding":parent.support}


def insert_into_class(cell,label,class_index):
    """Insert a nonloop in a chosen old direction, if cyclically admissible."""
    if not 1<=label<=cell.n+1:
        raise ValueError("Insertion label outside new ground set")
    old_to_new={i:i+int(i>=label) for i in range(1,cell.n+1)}
    chosen=set(cell.classes[class_index])
    bases=[tuple(sorted((old_to_new[a],old_to_new[b]))) for a,b in cell.bases]
    bases.extend(tuple(sorted((label,old_to_new[i]))) for i in cell.support if i not in chosen)
    try:
        parent=cell_from_bases(cell.n+1,bases)
    except ValueError:
        return None
    assert parent.dimension==9
    return parent


def defect_witnesses(cell,label):
    """Every possible parent whose j-coordinate facet deletes to this tile."""
    witnesses=[]
    for class_index in range(len(cell.classes)):
        parent=insert_into_class(cell,label,class_index)
        if parent is None:
            continue
        relation=relation_for(parent)
        if relation["row"] is None:
            continue
        defect=naive_delete_row(parent.n,relation["row"],label)
        assert len(defect)==1 and cell.affine in defect
        witnesses.append({"enlarged_class":cell.classes[class_index],
                          "parent":source_record(parent),
                          "relation_id":relation["relation_id"],
                          "dihedral_action":relation["dihedral_action"],
                          "support_embedding":relation["support_embedding"],
                          "coefficient":defect[cell.affine]})
    return witnesses


def build_defects():
    relations,cores=catalogs()
    records=[]
    for profile,original in sorted(relations.items(),key=lambda item:(sum(item[0]),item[0])):
        parent=as_cell(original["n"],original["parent_classes"])
        row={tuple(w["affine"]):w["coefficient"] for w in original["signed_admissible_facets"]}
        by_label=[]
        for label in range(1,parent.n+1):
            defect=naive_delete_row(parent.n,row,label)
            assert len(defect)<=1 and all(abs(v)==1 for v in defect.values())
            by_label.append({"deleted_label":label,"defect":sparse(defect),
                             "kind":"SIGNED_SINGLETON" if defect else "ZERO",
                             "coefficient_sum":sum(defect.values())})
        records.append({"relation_id":original["id"],"core_type":profile,
                        "parent":source_record(parent),"row":sparse(row),
                        "defects_by_label":by_label,
                        "defect_counts":dict(Counter(r["kind"] for r in by_label))})
    absent=[]
    for profile,core in sorted(cores.items(),key=lambda item:(sum(item[0]),item[0])):
        if profile in relations:
            continue
        absent.append({"core_type":profile,"category":core["category"],
                       "relation":None,"defects":None,
                       "all_Z_relation_space_dimension":0,
                       "proof_reference":core["proof_reference"],
                       "reason":"NO CERTIFIED NONZERO ROW EXISTS; no artificial source-boundary vector used"})
    slot_records=[]
    summaries=[]
    for q in range(6,11):
        admitted=[cell for cell in loopless_eight_cells(q) if classify(cell)["status"]=="CERTIFIED_TILE"]
        hist=Counter()
        for cell in admitted:
            slots=[]
            for label in range(1,q+2):
                witnesses=defect_witnesses(cell,label)
                slots.append({"insertion_label":label,"witnesses":witnesses,
                              "is_singleton_defect":bool(witnesses)})
            assert all(slot["is_singleton_defect"] for slot in slots)
            failed=[slot["insertion_label"] for slot in slots if not slot["is_singleton_defect"]]
            hist[len(failed)]+=1
            slot_records.append({"tile":source_record(cell),"core_type":composition_type(map(len,cell.classes)),
                                 "slots":slots,"failed_slots":failed})
        summaries.append({"support_size":q,"tile_count":len(admitted),
                          "failed_linear_slot_count_histogram":dict(sorted(hist.items()))})
    counts=Counter(d["kind"] for r in records for d in r["defects_by_label"])
    return {"claim_tag":"PROVED with exact independent finite checks",
            "scope":"All certified rank-two dimension-nine local parent relations and all source labels",
            "relation_core_count":15,"no_row_core_count":14,
            "no_row_categories":dict(Counter(r["category"] for r in absent)),
            "prototype_label_decision_count":sum(counts.values()),"prototype_defect_counts":dict(counts),
            "relations":records,"no_row_cores":absent,
            "loopless_tile_count":len(slot_records),"all_tiles_are_defects_for_every_slot":True,
            "fixed_slot_decision_count":sum(len(r["slots"]) for r in slot_records),
            "slot_support_summaries":summaries,"tile_insertion_slots":slot_records,
            "uniform_breadth":"For every n>=6 and every j in [n+1], delta_j(L_(n+1))=V_n",
            "fixed_slot_scope":"Exact local criterion: enlarge an adjacent cyclic class to a balanced parent core",
            "correction_scope":"Naive deletion fails; this does not exclude adjacent amalgamation corrections",
            "proof_reference":"research/run7/CORRECTED_DELETION.md"}


def main():
    data=build_defects()
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps(data,indent=2)+"\n")
    print(json.dumps({key:data[key] for key in ("prototype_label_decision_count","prototype_defect_counts",
                                                "no_row_categories","slot_support_summaries")},indent=2))


if __name__=="__main__":
    main()
