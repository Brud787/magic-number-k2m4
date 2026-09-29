"""Independent profile counts, source encodings, and deletion obstruction."""

from collections import Counter
from fractions import Fraction
from math import comb

from magic_number import affine
from magic_number.run6_membership_cores import build_inventory, deletion_obstruction


def _compositions(total, length):
    if length == 1:
        if total > 0:
            yield (total,)
        return
    for first in range(1, total-length+2):
        for tail in _compositions(total-first, length-1):
            yield (first,)+tail


def _dihedral(word):
    return min(tuple(word[(direction*j+shift) % len(word)] for j in range(len(word)))
               for direction in (1, -1) for shift in range(len(word)))


def test_all_core_counts_by_independent_ordered_compositions():
    data = build_inventory()
    assert data["loopless_source_count"] == 221
    assert data["dihedral_source_type_count"] == 24
    assert data["dihedral_kind_counts"] == {"COMPLEMENT_FIVE":10,"COLLAPSED":12,"FOUR_MASS":1,"SPURION":1}
    assert data["labeled_kind_counts"] == {"COMPLEMENT_FIVE":83,"COLLAPSED":133,"FOUR_MASS":2,"SPURION":3}
    for q in range(6, 11):
        s=12-q
        expected=Counter()
        for word in _compositions(q,s):
            expected[_dihedral(word)]+=Fraction(q,s)
        actual={tuple(row["dihedral_composition_type"]):row["labeled_loopless_count"]
                for row in data["cores"] if row["q"]==q}
        assert dict(expected)==actual
        assert sum(expected.values())==comb(q,s)


def test_every_recorded_cell_has_independent_affine_dimension_and_bases():
    data=build_inventory()
    for row in data["cores"]:
        window=row["representative_affine"]
        assert affine.dimension(window)==8
        assert affine.bases(window)==row["representative_bases"]
        assert affine.necklace(window)==row["representative_necklace"]
        for f in row["labeled_affine_permutations"]:
            assert affine.dimension(f)==8
            assert all(f[i-1]!=i for i in range(1,len(f)+1))


def test_nonzero_parent_row_counts_and_independent_parent_recovery():
    from magic_number.parent_profiles import loopless_parents
    from magic_number.rank2 import facets
    from magic_number.run6_membership_cores import classify
    data=build_inventory()
    assert [r["nonzero_parent_relation_count"] for r in data["loopless_parent_summaries"]]==[7,40,81,60,11]
    for q in range(7,12):
        for parent in loopless_parents(q):
            children=[f for f in facets(parent) if classify(f)["status"]=="CERTIFIED_TILE"]
            if len(children) in (6,10):
                assert set().union(*(set(affine.bases(f.affine)) for f in children))==set(affine.bases(parent.affine))


def test_deletion_projection_by_independent_basis_restriction():
    data=deletion_obstruction()
    j=data["deleted_label"]
    small={frozenset(affine.bases(f)):i for i,f in enumerate(data["target_columns"])}
    projected=[0]*len(small)
    for coefficient,f,target in zip(data["source_row"],data["source_columns"],data["column_projection"]):
        all_bases=affine.bases(f)
        if any(j in b for b in all_bases):
            assert target is None
            continue
        new_bases=frozenset(tuple(i-int(i>j) for i in b) for b in all_bases)
        assert target==small[new_bases]
        projected[target]+=coefficient
    assert projected==data["projected_row"]
    assert sum(projected)==data["projected_coefficient_sum"]!=0
    assert sum(c!=0 for c in projected)==1
    assert data["all_target_local_rows_have_sum_zero"]
