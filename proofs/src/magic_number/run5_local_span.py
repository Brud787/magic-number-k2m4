"""Full Run4 one-parent relation spans in the complete n7/n8 tile universes.

Inputs are preserved all-Z geometric relation and admissibility certificates.
No source boundary chain or sampled image membership is used as a relation.
"""

from __future__ import annotations

import json
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path

from sympy import Matrix

from .certified_relations import PROVENANCE, standard_dihedral_orbit
from .parent_profiles import composition_type
from .parent_relations import embed, relabel
from .rank2 import RankTwoCell, cells, facets


ROOT = Path(__file__).resolve().parents[2]


def _read(path):
    return json.loads((ROOT / path).read_text())


@lru_cache(maxsize=None)
def certified_tile_universe(n):
    if n not in (7, 8):
        raise ValueError("This bounded implementation handles only n=7,8")
    rows = _read(f"results/run2/child_status_n{n}.json")["cells"]
    if any(row["admissibility"]["status"] not in ("CERTIFIED_TILE", "CERTIFIED_NON_TILE")
           for row in rows):
        raise ValueError("The source admissibility inventory is incomplete")
    return tuple(sorted((row for row in rows
                         if row["admissibility"]["status"] == "CERTIFIED_TILE"),
                        key=lambda row: row["affine_permutation"]))


def _cell_record(cell):
    return {"affine": cell.affine, "classes": cell.classes, "bases": cell.bases,
            "necklace": cell.necklace, "support": cell.support, "dimension": cell.dimension}


@lru_cache(maxsize=None)
def build_local_matrix(n):
    """Return ordered full-U_n integer matrix plus every labeled parent."""
    tiles = certified_tile_universe(n)
    columns = tuple(tuple(tile["affine_permutation"]) for tile in tiles)
    index = {window: j for j, window in enumerate(columns)}
    core_data = _read("results/run4/core_status.json")["cores"]
    core_by_type = {tuple(row["dihedral_composition_type"]): row for row in core_data}
    prototypes = _read("results/run4/sign_relations.json")["relations"]
    generated = {}
    for prototype in prototypes:
        q = prototype["n"]
        if q > n:
            continue
        parent = RankTwoCell(q, tuple(map(tuple, prototype["parent_classes"])))
        source_walls = [(RankTwoCell(q, tuple(map(tuple, wall["classes"]))),
                         wall["coefficient"]) for wall in prototype["signed_admissible_facets"]]
        for direction in (-1, 1):
            for shift in range(q):
                for support in combinations(range(1, n + 1), q):
                    target_parent = embed(relabel(parent, direction, shift), n, support)
                    row = [0] * len(columns)
                    for child, coefficient in source_walls:
                        transformed = embed(relabel(child, direction, shift), n, support)
                        row[index[transformed.affine]] += coefficient
                    common_sign = 1 if next(value for value in row if value) > 0 else -1
                    row = tuple(common_sign * value for value in row)
                    assert sum(row) == 0
                    origin = {"source_relation": prototype["id"],
                              "core_type": prototype["core_type"], "core_n": q,
                              "dihedral_direction": direction, "dihedral_shift": shift,
                              "increasing_support": support, "common_sign": common_sign,
                              "parent_affine": target_parent.affine}
                    generated.setdefault(row, []).append(origin)
    row_vectors = tuple(sorted(generated))
    relation_records = []
    parent_to_rows = {}
    for row_index, vector in enumerate(row_vectors):
        origins = generated[vector]
        parents = sorted({tuple(origin["parent_affine"]) for origin in origins})
        for parent in parents:
            parent_to_rows.setdefault(parent, []).append(row_index)
        relation_records.append({"id": f"n{n}-P{row_index:03d}", "row_index": row_index,
                                 "terms": [{"column": j, "coefficient": c}
                                           for j, c in enumerate(vector) if c],
                                 "parent_affines": parents, "transport_origins": origins,
                                 "coefficient_sum": sum(vector),
                                 "scope": "ALL_Z_GEOMETRIC_INDICATOR_RELATION",
                                 "proof_reference": "research/run4/LOCAL_PARENT_THEOREM.md"})
    parent_records = []
    for parent in cells(n, 9):
        core_type = composition_type(map(len, parent.classes))
        core = core_by_type[core_type]
        source_walls = facets(parent)
        admissible = sorted(child.affine for child in source_walls if child.affine in index)
        row_indices = parent_to_rows.get(parent.affine, [])
        # Run4 classification: 0,6,8,10 admissible walls; only 6 and10 have relations.
        count = len(admissible)
        sector = ("BALANCED" if count in (6, 10)
                  else "HOSTILE_ZERO_KERNEL" if count == 8 else "COLLAPSED")
        assert count in (0, 6, 8, 10)
        assert len(row_indices) == (1 if sector == "BALANCED" else 0)
        if row_indices:
            participating = {columns[j] for j, c in enumerate(row_vectors[row_indices[0]]) if c}
            assert participating == set(admissible)
        parent_records.append({**_cell_record(parent), "core_type": core_type,
                               "core_id": core["id"], "sector": sector,
                               "source_facet_count": len(source_walls),
                               "admissible_facets": admissible, "relation_rows": row_indices})
    matrix = Matrix(row_vectors)
    _, column_pivots = matrix.rref()
    _, independent_rows = matrix.T.rref()
    assert len(column_pivots) == len(independent_rows)
    return {"n": n, "k": 2, "m": 4,
            "claim_tag": "COMPUTATIONALLY-VERIFIED",
            "scope": "FULL_RUN4_ONE_PARENT_RELATION_SPAN_IN_COMPLETE_ALL_Z_TILE_UNIVERSE",
            "tile_universe_reference": f"results/run2/child_status_n{n}.json",
            "local_relation_reference": "results/run4/sign_relations.json",
            "tile_count": len(columns), "column_affine_permutations": columns,
            "tiles": [{"column": j, **_cell_record(RankTwoCell(
                       n, tuple(map(tuple, tile["parallel_classes"])))),
                       "admissibility": tile["admissibility"]}
                      for j, tile in enumerate(tiles)],
            "relation_count": len(row_vectors), "rows": row_vectors,
            "relations": relation_records, "parents": sorted(parent_records,
                                                            key=lambda row: row["affine"]),
            "source_parent_count": len(parent_records),
            "parent_sector_counts": dict(Counter(row["sector"] for row in parent_records)),
            "rank_over_Q": len(column_pivots), "independent_row_indices": independent_rows,
            "pivot_columns": column_pivots,
            "quotient_dimension": len(columns) - len(column_pivots),
            "all_row_sums_zero": all(sum(row) == 0 for row in row_vectors),
            "not_claimed": "The full indicator kernel, arbitrary-tiling generation, or flip connectivity"}


@lru_cache(maxsize=None)
def known_tiling_span(n):
    """Exact coefficients or a separating covector for every orbit difference."""
    data = build_local_matrix(n)
    columns, rows = data["column_affine_permutations"], data["rows"]
    matrix = Matrix(rows)
    row_indices, pivots = data["independent_row_indices"], data["pivot_columns"]
    basis = matrix[list(row_indices), :]
    pivot_inverse = basis[:, list(pivots)].inv()
    tilings = standard_dihedral_orbit(n)
    base = tilings[0]
    base_set = set(base["cells"])
    differences = []
    for tiling in tilings[1:]:
        target = set(tiling["cells"])
        difference = Matrix([[int(window in target) - int(window in base_set)
                              for window in columns]])
        coefficients = difference[:, list(pivots)] * pivot_inverse
        reconstructed = coefficients * basis
        residual = difference - reconstructed
        record = {"positive_tiling": tiling["id"], "negative_tiling": base["id"],
                  "difference": list(map(int, difference)), "coefficient_sum": int(sum(difference)),
                  "in_full_local_span": not any(residual)}
        if not any(residual):
            record["local_decomposition"] = [
                {"row_index": row_indices[j], "coefficient": str(value)}
                for j, value in enumerate(coefficients) if value]
        else:
            witness = next(vector for vector in matrix.nullspace()
                           if (difference * vector)[0] != 0)
            record["separating_covector"] = list(map(str, witness))
            record["separator_value_on_difference"] = str((difference * witness)[0])
            record["local_annihilation_exact"] = not any(matrix * witness)
        differences.append(record)
    difference_matrix = Matrix([row["difference"] for row in differences])
    return {"n": n, "scope": "KNOWN_COMPLETE_STANDARD_DIHEDRAL_ALL_Z_TILINGS",
            "provenance": PROVENANCE, "base_tiling": base["id"], "tilings": tilings,
            "tiling_count": len(tilings), "tile_count_per_tiling": len(base["cells"]),
            "all_pair_difference_count": len(tilings) * (len(tilings) - 1) // 2,
            "relative_base_differences": differences,
            "all_pair_differences_in_full_local_span": all(row["in_full_local_span"]
                                                          for row in differences),
            "tiling_difference_rank_over_Q": difference_matrix.rank(),
            "local_plus_tiling_difference_rank_over_Q": matrix.col_join(difference_matrix).rank(),
            "logical_implication": "Every pair difference is the difference of two saved relative-base certificates.",
            "not_claimed": "All n8 tilings were enumerated or local moves connect these tilings"}


def main():
    destination = ROOT / "results/run5"
    destination.mkdir(parents=True, exist_ok=True)
    summary = {}
    for n in (7, 8):
        local, known = build_local_matrix(n), known_tiling_span(n)
        for filename, content in ((f"local_relation_matrix_n{n}.json", local),
                                  (f"known_tiling_span_n{n}.json", known)):
            (destination / filename).write_text(json.dumps(content, indent=2) + "\n")
        summary[n] = {"tiles": local["tile_count"], "parent_rows": local["relation_count"],
                      "rank": local["rank_over_Q"], "quotient": local["quotient_dimension"],
                      "all_known_orbit_differences_in_span": known["all_pair_differences_in_full_local_span"]}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
