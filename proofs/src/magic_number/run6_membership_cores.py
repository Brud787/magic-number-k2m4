"""Complete finite rank-two dimension-eight source and membership core inventory.

The classifier encodes the proofs in research/run6/MEMBERSHIP_CORES.md.
It does not infer all-Z injectivity from a differential rank calculation.
"""

from collections import Counter, defaultdict
from itertools import combinations
import json
from math import comb
from pathlib import Path

from .rank2 import RankTwoCell
from .parent_profiles import composition_type


ROOT = Path(__file__).resolve().parents[2]


def loopless_eight_cells(q):
    s = 12 - q
    if not 2 <= s <= q:
        return
    for starts in combinations(range(q), s):
        blocks = tuple(tuple((a + t) % q + 1
                             for t in range((starts[(j + 1) % s] - a) % q))
                       for j, a in enumerate(starts))
        yield RankTwoCell(q, blocks)


def classify(cell):
    if cell.dimension != 8:
        raise ValueError("The theorem classifies source dimension eight only")
    q = len(cell.support)
    sizes = tuple(map(len, cell.classes))
    maximum = max(sizes)
    if maximum > q - 5:
        block = next(block for block in cell.classes if len(block) == maximum)
        return {"status": "CERTIFIED_NON_TILE", "kind": "COLLAPSED",
                "obstruction_class": block, "complement_size": q - maximum,
                "image_dimension_upper_bound": q - maximum + 3,
                "proof": "research/run6/MEMBERSHIP_CORES.md#2-the-two-exclusion-mechanisms"}
    if maximum == q - 5:
        return {"status": "CERTIFIED_TILE", "kind": "COMPLEMENT_FIVE",
                "distinguished_class": next(block for block in cell.classes if len(block) == maximum),
                "proof": "research/run6/MEMBERSHIP_CORES.md#3-uniform-inversion-for-the-ten-complement-five-types"}
    if q == 9 and sizes == (3, 3, 3):
        return {"status": "CERTIFIED_TILE", "kind": "SPURION",
                "proof": "literature/m4_spurion_tiles.pdf Section 5.1; research/run6/MEMBERSHIP_CORES.md"}
    if q == 8 and sizes == (2, 2, 2, 2):
        return {"status": "CERTIFIED_NON_TILE", "kind": "FOUR_MASS",
                "proof": "research/run3/MULTIPLICITY.md; research/run6/MEMBERSHIP_CORES.md"}
    raise AssertionError("A dimension-eight core escaped the exhaustive profile argument")


def build_inventory():
    records, summaries = [], []
    for q in range(6, 11):
        grouped = defaultdict(list)
        for cell in loopless_eight_cells(q):
            grouped[composition_type(map(len, cell.classes))].append(cell)
        for profile, members in sorted(grouped.items()):
            representative = min(members, key=lambda cell: cell.affine)
            decision = classify(representative)
            assert all(classify(cell)["kind"] == decision["kind"] for cell in members)
            records.append({"id": "membership-" + "-".join(map(str, profile)),
                            "q": q, "s": 12 - q, "dihedral_composition_type": profile,
                            "representative_classes": representative.classes,
                            "representative_affine": representative.affine,
                            "representative_necklace": representative.necklace,
                            "representative_bases": representative.bases,
                            "labeled_loopless_count": len(members),
                            "labeled_affine_permutations": sorted(cell.affine for cell in members),
                            **decision})
        counts = Counter(classify(cell)["kind"] for cell in loopless_eight_cells(q))
        summaries.append({"q": q, "s": 12 - q, "source_count": comb(q, 12-q),
                          "dihedral_type_count": len(grouped), "kind_counts": dict(counts),
                          "admissible_count": sum(counts[k] for k in ("COMPLEMENT_FIVE", "SPURION"))})
    counts = Counter(row["kind"] for row in records)
    labeled = Counter()
    for row in records:
        labeled[row["kind"]] += row["labeled_loopless_count"]
    from .parent_profiles import loopless_parents
    from .rank2 import facets
    parent_summaries = []
    for q in range(7,12):
        parent_counts = Counter()
        for parent in loopless_parents(q):
            admissible = [f for f in facets(parent) if classify(f)["status"] == "CERTIFIED_TILE"]
            parent_counts[len(admissible)] += 1
            if len(admissible) in (6,10):
                assert set().union(*(set(f.bases) for f in admissible)) == set(parent.bases)
        parent_summaries.append({"q":q,"admissible_facet_count_histogram":dict(parent_counts),
                                 "nonzero_parent_relation_count":parent_counts[6]+parent_counts[10]})
    return {"n_scope": "Every n>=6 via exact loop insertion and dihedral transport",
            "k": 2, "m": 4, "source_dimension": 8,
            "claim_tag": "PROVED with independently checked finite source accounting",
            "source_support_equation": "q+s=12; 6<=q<=10",
            "loopless_source_count": sum(row["source_count"] for row in summaries),
            "dihedral_source_type_count": len(records),
            "dihedral_kind_counts": dict(counts), "labeled_kind_counts": dict(labeled),
            "admissible_dihedral_type_count": counts["COMPLEMENT_FIVE"]+counts["SPURION"],
            "admissible_labeled_loopless_count": labeled["COMPLEMENT_FIVE"]+labeled["SPURION"],
            "support_summaries": summaries, "cores": records,
            "all_n_tile_universe_count": "binom(n,6)+14binom(n,7)+36binom(n,8)+30binom(n,9)+5binom(n,10)",
            "loopless_parent_summaries":parent_summaries,
            "admissible_facets_recover_each_balanced_parent_bases":True,
            "all_n_parent_row_count":"7binom(n,7)+40binom(n,8)+81binom(n,9)+60binom(n,10)+11binom(n,11)",
            "not_claimed": "Cardinality of complete tilings, full indicator generation, or novelty of source types",
            "proof_reference": "research/run6/MEMBERSHIP_CORES.md"}


def delete_loop(cell, label):
    """The degree-eight part of source column deletion, zero on nonloops."""
    if not 1 <= label <= cell.n:
        raise ValueError("Label outside the ground set")
    if label in cell.support:
        return None
    return RankTwoCell(cell.n-1, tuple(tuple(i-int(i > label) for i in block)
                                      for block in cell.classes))


def deletion_obstruction():
    """Exact n8->n7 failure of the naive loop-deletion quotient map."""
    from .rank2 import cell_from_bases
    from .affine import bases
    large = json.loads((ROOT/"results/run5/local_relation_matrix_n8.json").read_text())
    small = json.loads((ROOT/"results/run5/local_relation_matrix_n7.json").read_text())
    small_index = {tuple(f): j for j, f in enumerate(small["column_affine_permutations"])}
    for label in range(1, 9):
        projection = []
        for window in large["column_affine_permutations"]:
            cell = cell_from_bases(8, bases(window))
            target = delete_loop(cell, label)
            projection.append(None if target is None else small_index[target.affine])
        for row_index, row in enumerate(large["rows"]):
            result = [0] * small["tile_count"]
            for coefficient, target in zip(row, projection):
                if target is not None:
                    result[target] += coefficient
            if sum(result):
                return {"claim_tag": "PROVED by exact coefficient-sum obstruction",
                        "source_n": 8, "target_n": 7, "deleted_label": label,
                        "source_relation_row": row_index,
                        "source_parent_affine": large["relations"][row_index]["parent_affines"][0],
                        "source_row": row, "source_columns": large["column_affine_permutations"],
                        "column_projection": projection,
                        "target_columns": small["column_affine_permutations"],
                        "projected_row": result, "projected_coefficient_sum": sum(result),
                        "target_annihilator": [1] * small["tile_count"],
                        "all_target_local_rows_have_sum_zero": all(sum(r)==0 for r in small["rows"]),
                        "conclusion": "Loop deletion does not send L8 into L7",
                        "proof_reference": "research/run6/DELETION.md"}
    raise AssertionError("The expected obstruction was not found")


def main():
    destination = ROOT/"results/run6"
    destination.mkdir(parents=True, exist_ok=True)
    inventory, deletion = build_inventory(), deletion_obstruction()
    for filename, data in (("membership_cores.json", inventory), ("deletion_obstruction.json", deletion)):
        (destination/filename).write_text(json.dumps(data, indent=2)+"\n")
    print(json.dumps({"source_cells": inventory["loopless_source_count"],
                      "source_types": inventory["dihedral_source_type_count"],
                      "admissible_types": inventory["admissible_dihedral_type_count"],
                      "admissible_loopless_cells": inventory["admissible_labeled_loopless_count"],
                      "deletion_projected_sum": deletion["projected_coefficient_sum"]}, indent=2))


if __name__ == "__main__":
    main()
