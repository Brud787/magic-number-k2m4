"""Independent source-basis and cyclic-color audits of all deletion defects."""

from collections import Counter
import json

from magic_number import affine
from magic_number.parent_profiles import composition_type
from magic_number.parent_relations import embed
from magic_number.rank2 import cell_from_bases
from magic_number.run7_deletion import ROOT, build_defects, catalogs, naive_delete_row


def saved():
    return json.loads((ROOT/"results/run7/deletion_defects.json").read_text())


def test_all_136_literal_prototype_deletions_from_affine_loops_and_bases():
    result=saved()
    literal=json.loads((ROOT/"results/run4/sign_relations.json").read_text())["relations"]
    by_id={row["id"]:row for row in literal}
    counts=Counter()
    for record in result["relations"]:
        original=by_id[record["relation_id"]]
        for decision in record["defects_by_label"]:
            j=decision["deleted_label"]
            surviving=[wall for wall in original["signed_admissible_facets"]
                       if wall["affine"][j-1]==j]
            assert len(surviving)<=1
            assert bool(surviving)==bool(decision["defect"])
            if surviving:
                wall=surviving[0]
                old_bases=affine.bases(wall["affine"])
                expected={tuple(i-int(i>j) for i in pair) for pair in old_bases}
                actual=decision["defect"][0]
                assert affine.dimension(actual["affine"])==8
                assert set(affine.bases(actual["affine"]))==expected
                assert actual["coefficient"]==wall["coefficient"]
            counts[decision["kind"]]+=1
    assert counts=={"SIGNED_SINGLETON":82,"ZERO":54}
    assert result["prototype_label_decision_count"]==136


def test_all_798_slots_independently_by_neighbor_colors_and_parent_bases():
    result=saved()
    relation_types=set(catalogs()[0])
    checked=0
    for entry in result["tile_insertion_slots"]:
        tile=entry["tile"]
        blocks=tile["classes"]
        n=tile["n"]
        color={label:index for index,block in enumerate(blocks) for label in block}
        old_bases=affine.bases(tile["affine"])
        for slot in entry["slots"]:
            j=slot["insertion_label"]
            # In a loopless cyclic word only the colors neighboring this gap
            # can receive its new label without breaking interval convexity.
            neighboring={color[(j-2)%n+1],color[(j-1)%n+1]}
            expected=set()
            for index in neighboring:
                sizes=[len(block) for block in blocks]
                sizes[index]+=1
                if composition_type(sizes) in relation_types:
                    expected.add(tuple(blocks[index]))
            found={tuple(w["enlarged_class"]) for w in slot["witnesses"]}
            assert expected==found and expected
            for witness in slot["witnesses"]:
                parent=witness["parent"]
                mapping={i:i+int(i>=j) for i in range(1,n+1)}
                pair_set={tuple(sorted(mapping[i] for i in pair)) for pair in old_bases}
                pair_set|={tuple(sorted((j,mapping[i]))) for i in range(1,n+1)
                           if i not in witness["enlarged_class"]}
                assert set(affine.bases(parent["affine"]))==pair_set
                assert affine.dimension(parent["affine"])==9
                assert abs(witness["coefficient"])==1
            checked+=1
    assert checked==798
    assert result["all_tiles_are_defects_for_every_slot"]


def test_all_loop_transport_slots_return_exact_original_relation():
    for original in catalogs()[0].values():
        n=original["n"]
        row={tuple(w["affine"]):w["coefficient"] for w in original["signed_admissible_facets"]}
        for j in range(1,n+2):
            support=tuple(i for i in range(1,n+2) if i!=j)
            inserted={embed(cell_from_bases(n,affine.bases(window)),n+1,support).affine:value
                      for window,value in row.items()}
            assert naive_delete_row(n+1,inserted,j)==row


def test_all_fourteen_zero_kernel_cores_explicitly_have_no_row():
    result=saved()
    assert Counter(r["category"] for r in result["no_row_cores"])=={
        "COLLAPSED":12,"NO_NONZERO_ALL_Z_FACET_RELATION":2}
    assert all(r["relation"] is None and r["defects"] is None
               and r["all_Z_relation_space_dimension"]==0 for r in result["no_row_cores"])
    assert len(result["relations"])+len(result["no_row_cores"])==29


def test_saved_certificate_reproduces_exactly():
    assert json.loads(json.dumps(build_defects()))==saved()
