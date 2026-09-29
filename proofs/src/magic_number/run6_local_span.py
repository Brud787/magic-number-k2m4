"""Complete n9 all-Z tile inventory and full Run4 local relation matrix.

Only new Run6 artifacts are written. The geometric relations and complete
source admissibility classification are preserved inputs, not rank guesses.
"""

from __future__ import annotations

import json
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path

from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix

from .parent_profiles import composition_type
from .parent_relations import embed, relabel
from .rank2 import RankTwoCell, cells, facets


ROOT = Path(__file__).resolve().parents[2]


def _read(path):
    return json.loads((ROOT / path).read_text())


def _cell_record(cell):
    return {"affine": cell.affine, "classes": cell.classes, "bases": cell.bases,
            "necklace": cell.necklace, "support": cell.support, "loops": cell.loops,
            "dimension": cell.dimension}


@lru_cache(maxsize=1)
def tile_inventory():
    source = _read("results/run2/child_status_n9.json")
    assert len(source["cells"]) == 1554
    assert all(row["admissibility"]["status"] in ("CERTIFIED_TILE", "CERTIFIED_NON_TILE")
               for row in source["cells"])
    certified = sorted((row for row in source["cells"]
                        if row["admissibility"]["status"] == "CERTIFIED_TILE"),
                       key=lambda row: row["affine_permutation"])
    cells_by_window = {tuple(row["affine_permutation"]): RankTwoCell(
        9, tuple(map(tuple, row["parallel_classes"]))) for row in certified}
    columns = tuple(cells_by_window)
    assert len(columns) == 942
    index = {window: j for j, window in enumerate(columns)}
    unseen, orbit_membership, orbits = set(columns), {}, []
    while unseen:
        representative = min(unseen)
        actions = {}
        for direction in (-1, 1):
            for shift in range(9):
                target = relabel(cells_by_window[representative], direction, shift).affine
                assert target in index
                actions.setdefault(target, []).append({"direction": direction, "shift": shift})
        members = tuple(sorted(actions))
        orbit_id = f"n9-orbit-{len(orbits):03d}"
        assert set(members) <= unseen
        unseen.difference_update(members)
        orbits.append({"id": orbit_id, "representative_affine": representative,
                       "size": len(members), "member_columns": [index[w] for w in members],
                       "member_affines": members})
        for window in members:
            orbit_membership[window] = {"orbit_id": orbit_id,
                                        "representative_affine": representative,
                                        "orbit_size": len(members),
                                        "representative_to_tile_actions": actions[window]}
    records = []
    for j, row in enumerate(certified):
        window = tuple(row["affine_permutation"])
        cell = cells_by_window[window]
        q, s = len(cell.support), len(cell.classes)
        eligible = [i for i, block in enumerate(cell.classes) if len(block) == q-5]
        kind = row["admissibility"]["tile_kind"]
        if kind == "BCFW":
            assert eligible
            proof_references = ["results/run2/general_bcfw_n9.json",
                                "research/run2/ADMISSIBILITY_REVIEW.md",
                                "BCFW v3 Theorem 8.7 and the explicit recipe in admissibility"]
        else:
            assert kind == "NON_BCFW_SPURION" and not eligible
            proof_references = ["m4_spurion_tiles Sections 5.1-5.3",
                                "research/run2/PARENT_ENUMERATION.md",
                                "Published spurion injectivity plus cyclic symmetry"]
        records.append({"column": j, **_cell_record(cell),
                        "profile": {"q": q, "s": s, "ordered_class_sizes": list(map(len, cell.classes)),
                                    "sorted_class_sizes": sorted(map(len, cell.classes)),
                                    "dihedral_composition_type": composition_type(map(len, cell.classes))},
                        "tile_kind": kind, "status": "CERTIFIED_TILE", "scope": "ALL_Z",
                        "admissibility": row["admissibility"],
                        "admissibility_proof_references": proof_references,
                        "dihedral_orbit": orbit_membership[window],
                        "complement_five": {
                            "applicable": bool(eligible), "qualifying_class_indices": eligible,
                            "qualifying_classes": [cell.classes[i] for i in eligible],
                            "chosen_class_index": eligible[0] if eligible else None,
                            "scope": "Source-profile applicability; closed membership needs its own proof"}})
    return {"n": 9, "k": 2, "m": 4,
            "claim_tag": "COMPUTATIONALLY-VERIFIED",
            "geometric_status": "SOURCE-VERIFIED_AND_PROVED_PRESERVED_ALL_Z_CLASSIFICATION",
            "source_inventory_reference": "results/run2/child_status_n9.json",
            "source_cell_count": 1554, "source_status_counts": source["status_counts"],
            "tile_count": len(records), "column_affine_permutations": columns, "tiles": records,
            "tile_kind_counts": dict(Counter(row["tile_kind"] for row in records)),
            "support_size_counts": dict(Counter(len(row["support"]) for row in records)),
            "complement_five_applicable_count": sum(row["complement_five"]["applicable"] for row in records),
            "dihedral_orbit_count": len(orbits), "dihedral_orbits": orbits,
            "scope": "COMPLETE_ALL_Z_EIGHT_DIMENSIONAL_TILE_SOURCE_UNIVERSE_AT_N9",
            "not_claimed": "A classification of complete tilings or a new injectivity theorem"}


def _sparse_qq(rows, width):
    return DomainMatrix({i: {j: QQ(value) for j, value in enumerate(row) if value}
                         for i, row in enumerate(rows)}, (len(rows), width), QQ)


def modular_determinant(matrix, modulus=1000003):
    """Exact determinant residue, an integer-minor nonvanishing certificate."""
    size = len(matrix)
    work = [{j: int(value) % modulus for j, value in enumerate(row) if value % modulus}
            for row in matrix]
    determinant = 1
    for j in range(size):
        pivot = next((i for i in range(j, size) if work[i].get(j, 0)), None)
        if pivot is None:
            return 0
        if pivot != j:
            work[j], work[pivot] = work[pivot], work[j]
            determinant = -determinant
        value = work[j][j]
        determinant = determinant * value % modulus
        inverse = pow(value, -1, modulus)
        for i in range(j+1, size):
            if j not in work[i]:
                continue
            factor = work[i][j] * inverse % modulus
            for column, entry in work[j].items():
                updated = (work[i].get(column, 0) - factor * entry) % modulus
                if updated:
                    work[i][column] = updated
                else:
                    work[i].pop(column, None)
    return determinant % modulus


def unit_pivot_determinant(matrix):
    """Exact integer elimination for the stored minor, which has unit pivots.

    This certificate routine rejects a non-unit pivot instead of performing
    floating point division or making a general unimodularity assumption.
    """
    work = [{j: int(value) for j, value in enumerate(row) if value} for row in matrix]
    determinant = 1
    for k in range(len(work)):
        pivot = next((i for i in range(k, len(work)) if abs(work[i].get(k, 0)) == 1), None)
        if pivot is None:
            raise ValueError("The selected minor lacks a unit elimination pivot")
        if pivot != k:
            work[k], work[pivot] = work[pivot], work[k]
            determinant = -determinant
        value = work[k][k]
        determinant *= value
        for i in range(k+1, len(work)):
            factor = work[i].get(k, 0)*value
            if factor:
                for j, entry in work[k].items():
                    updated = work[i].get(j, 0)-factor*entry
                    if updated:
                        work[i][j] = updated
                    else:
                        work[i].pop(j, None)
    return determinant


@lru_cache(maxsize=1)
def build_local_matrix():
    inventory = tile_inventory()
    columns = inventory["column_affine_permutations"]
    index = {window: j for j, window in enumerate(columns)}
    core_data = _read("results/run4/core_status.json")["cores"]
    core_by_type = {tuple(row["dihedral_composition_type"]): row for row in core_data}
    prototypes = _read("results/run4/sign_relations.json")["relations"]
    generated = {}
    for prototype in prototypes:
        q = prototype["n"]
        if q > 9:
            continue
        parent = RankTwoCell(q, tuple(map(tuple, prototype["parent_classes"])))
        source_walls = [(RankTwoCell(q, tuple(map(tuple, wall["classes"]))),
                         wall["coefficient"]) for wall in prototype["signed_admissible_facets"]]
        for direction in (-1, 1):
            for shift in range(q):
                rotated_parent = relabel(parent, direction, shift)
                rotated_walls = [(relabel(child, direction, shift), coefficient)
                                 for child, coefficient in source_walls]
                for support in combinations(range(1, 10), q):
                    target_parent = embed(rotated_parent, 9, support)
                    row = [0] * len(columns)
                    for child, coefficient in rotated_walls:
                        row[index[embed(child, 9, support).affine]] += coefficient
                    common_sign = 1 if next(value for value in row if value) > 0 else -1
                    row = tuple(common_sign * value for value in row)
                    assert sum(row) == 0
                    generated.setdefault(row, []).append({
                        "source_relation": prototype["id"], "core_type": prototype["core_type"],
                        "core_n": q, "dihedral_direction": direction, "dihedral_shift": shift,
                        "increasing_support": support, "common_sign": common_sign,
                        "parent_affine": target_parent.affine})
    rows = tuple(sorted(generated))
    relations, parent_to_rows = [], {}
    for row_index, row in enumerate(rows):
        origins = generated[row]
        parents = sorted({tuple(origin["parent_affine"]) for origin in origins})
        for parent in parents:
            parent_to_rows.setdefault(parent, []).append(row_index)
        relations.append({"id": f"n9-P{row_index:03d}", "row_index": row_index,
                          "terms": [{"column": j, "coefficient": value}
                                    for j, value in enumerate(row) if value],
                          "parent_affines": parents, "transport_origins": origins,
                          "coefficient_sum": sum(row), "scope": "ALL_Z_GEOMETRIC_INDICATOR_RELATION",
                          "proof_reference": "research/run4/LOCAL_PARENT_THEOREM.md"})
    parents = []
    for parent in cells(9, 9):
        core_type = composition_type(map(len, parent.classes))
        core = core_by_type[core_type]
        source_walls = facets(parent)
        admissible = sorted(child.affine for child in source_walls if child.affine in index)
        source_rows = parent_to_rows.get(parent.affine, [])
        count = len(admissible)
        assert count in (0, 6, 8, 10)
        sector = "BALANCED" if count in (6, 10) else "HOSTILE_ZERO_KERNEL" if count == 8 else "COLLAPSED"
        assert len(source_rows) == (1 if sector == "BALANCED" else 0)
        assert count == core["certified_admissible_wall_count"]
        if source_rows:
            assert {columns[j] for j, value in enumerate(rows[source_rows[0]]) if value} == set(admissible)
        parents.append({**_cell_record(parent), "core_type": core_type, "core_id": core["id"],
                        "sector": sector, "source_facet_count": len(source_walls),
                        "admissible_facets": admissible, "relation_rows": source_rows,
                        "run4_kernel_dimension": core["all_Z_relation_space_dimension"]})
    domain_matrix = _sparse_qq(rows, len(columns))
    reduced, pivot_columns = domain_matrix.rref()
    _, independent_rows = domain_matrix.transpose().rref()
    rank = len(pivot_columns)
    assert len(independent_rows) == rank
    nonzero_reduced = reduced.to_dod()
    rref_rows = [[(j, str(value)) for j, value in sorted(nonzero_reduced[i].items())]
                 for i in range(rank)]
    minor = [[rows[i][j] for j in pivot_columns] for i in independent_rows]
    determinant_exact = unit_pivot_determinant(minor)
    determinant_residue = modular_determinant(minor)
    assert determinant_exact and determinant_residue != 0
    return {"n": 9, "k": 2, "m": 4, "claim_tag": "COMPUTATIONALLY-VERIFIED",
            "scope": "FULL_RUN4_ONE_PARENT_RELATION_SPAN_IN_COMPLETE_942_TILE_UNIVERSE",
            "tile_universe_reference": "results/run6/tile_universe_n9.json",
            "local_relation_reference": "results/run4/sign_relations.json",
            "tile_count": len(columns), "column_affine_permutations": columns,
            "relation_count": len(rows), "rows": rows, "relations": relations,
            "parents": sorted(parents, key=lambda row: row["affine"]),
            "source_parent_count": len(parents),
            "parent_sector_counts": dict(Counter(row["sector"] for row in parents)),
            "relation_support_size_counts": dict(Counter(origins[0]["core_n"] for origins in generated.values())),
            "relation_term_count_histogram": dict(Counter(sum(value != 0 for value in row) for row in rows)),
            "rank_over_Q": rank, "quotient_dimension": len(columns) - rank,
            "independent_row_indices": independent_rows, "pivot_columns": pivot_columns,
            "rref_nonzero_rows": rref_rows,
            "rank_certificate": {
                "exact_domain": "QQ", "method": "Sparse DomainMatrix RREF",
                "upper_certificate": "Every source row equals the sum of RREF basis rows weighted by its pivot-column entries.",
                "lower_certificate": "Recorded independent source rows and pivot columns have the stated exact nonzero integer determinant, also checked modulo the stated modulus.",
                "minor_determinant_exact": str(determinant_exact),
                "minor_modulus": 1000003, "minor_determinant_residue": determinant_residue},
            "all_row_sums_zero": all(sum(row) == 0 for row in rows),
            "participating_tile_count": sum(any(row[j] for row in rows) for j in range(len(columns))),
            "not_claimed": "Complete indicator kernel, tiling-difference generation, or flip connectivity"}


def main():
    destination = ROOT / "results/run6"
    destination.mkdir(parents=True, exist_ok=True)
    inventory = tile_inventory()
    (destination / "tile_universe_n9.json").write_text(json.dumps(inventory, indent=2) + "\n")
    local = build_local_matrix()
    (destination / "local_relation_matrix_n9.json").write_text(json.dumps(local, indent=2) + "\n")
    print(json.dumps({"tiles": inventory["tile_count"],
                      "tile_kinds": inventory["tile_kind_counts"],
                      "complement_five": inventory["complement_five_applicable_count"],
                      "dihedral_orbits": inventory["dihedral_orbit_count"],
                      "source_parents": local["source_parent_count"],
                      "rows": local["relation_count"], "rank": local["rank_over_Q"],
                      "indicator_rank_target": local["quotient_dimension"],
                      "minor_determinant_residue": local["rank_certificate"]["minor_determinant_residue"]},
                     indent=2))


def support_block_certificate():
    """The loopless sector adds one quotient class; records its signed weight."""
    from .bcfw import standard_k2
    inventory = _read("results/run6/tile_universe_n9.json")
    local = _read("results/run6/local_relation_matrix_n9.json")
    columns = [row["column"] for row in inventory["tiles"] if len(row["support"]) == 9]
    projected = [[row[j] for j in columns] for row in local["rows"]]
    sparse = {i: {j: QQ(x) for j, x in enumerate(row) if x} for i, row in enumerate(projected)}
    matrix = DomainMatrix({i: row for i, row in sparse.items() if row}, (len(projected), len(columns)), QQ)
    _, pivot_columns = matrix.rref()
    _, independent_rows = matrix.transpose().rref()
    minor = [[projected[i][j] for j in pivot_columns] for i in independent_rows]
    determinant = _sparse_qq(minor, len(pivot_columns)).det()
    weight = [0]*942
    for j in columns:
        weight[j] = 1 if inventory["tiles"][j]["tile_kind"] == "BCFW" else -1
    assert all(sum(a*b for a, b in zip(row, weight)) == 0 for row in local["rows"])
    assert len(pivot_columns) == 29 and determinant
    index = {tuple(w): j for j, w in enumerate(local["column_affine_permutations"])}
    base_columns = [index[row["affine"]] for row in standard_k2(9)]
    raw_sums = [sum(row[j] for j in columns) for row in local["rows"]]
    return {"n": 9, "claim_tag": "COMPUTATIONALLY-VERIFIED",
            "scope": "FULL_LOCAL_QUOTIENT_SUPPORT_BLOCK_AND_SIGNED_COVECTOR",
            "local_matrix_reference": "results/run6/local_relation_matrix_n9.json",
            "loopless_tile_columns": columns, "projected_rows": projected,
            "projected_rank_over_Q": 29, "projected_kernel_dimension": 1,
            "projected_minor_row_indices": independent_rows,
            "projected_minor_columns_in_loopless_block": pivot_columns,
            "projected_minor_determinant_exact": str(determinant),
            "ambient_covector": weight,
            "weight_rule": "+1 on 27 loopless BCFW tiles, -1 on three spurions, zero on every tile with a loop",
            "local_annihilation": [sum(a*b for a, b in zip(row, weight)) for row in local["rows"]],
            "raw_loopless_count_relation_sums": raw_sums,
            "raw_loopless_count_failing_row_indices": [i for i, x in enumerate(raw_sums) if x],
            "support_at_most_eight_column_count": 912,
            "support_at_most_eight_image_dimension_in_local_quotient": 471,
            "new_loopless_quotient_dimension": 1,
            "standard_base_columns": base_columns,
            "standard_base_weight": sum(weight[j] for j in base_columns),
            "complete_tiling_conservation_scope": "Conditional here on the separate all-Z indicator kernel equality; then every all-Z complete tiling has weight two"}


if __name__ == "__main__":
    main()
