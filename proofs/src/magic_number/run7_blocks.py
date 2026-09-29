"""Exact finite support blocks and corrected adjacent amalgamation at n<=9.

All saved earlier files are read-only inputs. No n10 source universe or
geometric degeneration is assumed by these combinatorial matrix checks.
"""

from __future__ import annotations

import json
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path

from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix

from . import affine
from .bcfw import standard_k2
from .rank2 import cell_from_bases
from .parent_relations import embed, relabel


ROOT = Path(__file__).resolve().parents[2]


def _domain(rows, width):
    data = {i: {j: QQ(x) for j, x in enumerate(row) if QQ(x)} for i, row in enumerate(rows)}
    return DomainMatrix({i: row for i, row in data.items() if row}, (len(rows), width), QQ)


def _rank(rows, width):
    return len(_domain(rows, width).rref()[1]) if width and rows else 0


@lru_cache(maxsize=None)
def finite_data(n):
    if n not in (7, 8, 9):
        raise ValueError("The bounded task has complete matrices only at n=7,8,9")
    source = f"results/run{6 if n == 9 else 5}/local_relation_matrix_n{n}.json"
    data = json.loads((ROOT/source).read_text())
    windows = tuple(map(tuple, data["column_affine_permutations"]))
    cells = tuple(cell_from_bases(n, affine.bases(window)) for window in windows)
    reduced, pivots = _domain(data["rows"], len(windows)).rref()
    sparse = reduced.to_dod()
    basis = tuple(sparse[i] for i in range(len(pivots)))
    free = tuple(j for j in range(len(windows)) if j not in pivots)
    assert len(pivots) == data["rank_over_Q"]
    return {"n": n, "source_reference": source, "data": data, "columns": windows,
            "cells": cells, "index": {w: j for j, w in enumerate(windows)},
            "rref": basis, "pivots": pivots, "free_columns": free}


def normal_form(vector, data):
    row = {j: QQ(value) for j, value in enumerate(vector) if value}
    for pivot, basis in zip(data["pivots"], data["rref"]):
        factor = row.get(pivot, QQ.zero)
        if factor:
            for j, value in basis.items():
                updated = row.get(j, QQ.zero)-factor*value
                if updated:
                    row[j] = updated
                else:
                    row.pop(j, None)
    return row


def support_subspace_record(data, columns):
    """dim image(U_S -> U/L)=|S|-rank(L)+rank(L projected outside S)."""
    columns = sorted(columns)
    complement = [j for j in range(len(data["columns"])) if j not in set(columns)]
    projection = [[row[j] for j in complement] for row in data["data"]["rows"]]
    rank = _rank(projection, len(complement))
    return {"tile_columns": columns, "column_count": len(columns),
            "outside_projection_rank_over_Q": rank,
            "image_dimension_over_Q": len(columns)-len(data["pivots"])+rank}


def rank_and_support_data():
    records, ranks = [], []
    quotient_dims = {6: 1, 7: 15, 8: 103, 9: 472}
    for n in (7, 8, 9):
        data = finite_data(n)
        support = [set(cell.support) for cell in data["cells"]]
        filtration, previous = [], 0
        for q in range(6, n+1):
            record = support_subspace_record(data, [j for j, labels in enumerate(support) if len(labels) <= q])
            record.update({"support_cutoff": q,
                           "graded_increment": record["image_dimension_over_Q"]-previous})
            previous = record["image_dimension_over_Q"]
            filtration.append(record)
        single = []
        for deleted in range(1, n+1):
            record = support_subspace_record(data, [j for j, labels in enumerate(support) if deleted not in labels])
            assert record["image_dimension_over_Q"] == quotient_dims[n-1]
            record["deleted_label"] = deleted
            single.append(record)
        pairs = []
        for a, b in combinations(range(1, n+1), 2):
            union = support_subspace_record(data, [j for j, labels in enumerate(support) if a not in labels or b not in labels])
            shared = support_subspace_record(data, [j for j, labels in enumerate(support) if a not in labels and b not in labels])
            intersection = 2*quotient_dims[n-1]-union["image_dimension_over_Q"]
            expected = quotient_dims[n-2] if n-2 >= 6 else 0
            assert intersection == shared["image_dimension_over_Q"] == expected
            pairs.append({"deleted_labels": [a, b], "union": union, "shared_support": shared,
                          "intersection_dimension_over_Q": intersection,
                          "intersection_equals_shared_support_image": True})
        records.append({"n": n, "filtration": filtration, "fixed_zero_insertions": single,
                        "all_pair_intersections": pairs,
                        "all_supports_sum_dimension": filtration[-2]["image_dimension_over_Q"],
                        "fixed_zero_insertion_dimension": quotient_dims[n-1],
                        "new_loopless_quotient_dimension": filtration[-1]["graded_increment"]})
        ranks.append({"n": n, "matrix_reference": data["source_reference"],
                      "tile_count": len(data["columns"]), "full_local_row_count": len(data["data"]["rows"]),
                      "local_rank_over_Q": len(data["pivots"]), "quotient_dimension": len(data["free_columns"]),
                      "column_affine_permutations": data["columns"], "quotient_basis_columns": data["free_columns"]})
    return {"claim_tag": "COMPUTATIONALLY-VERIFIED", "rank_data": ranks}, records


def amalgamate_cell(cell):
    """Exact generic source matroid under c[n-1] <- c[n-1]+c[n].

    All ordered minors are sums of nonnegative source minors, so support is
    exactly the label-merge image of the old bases, with duplicate labels removed.
    """
    n = cell.n
    merged = {tuple(sorted(n-1 if i == n else i for i in pair)) for pair in cell.bases}
    target = cell_from_bases(n-1, [pair for pair in merged if pair[0] != pair[1]])
    colors = {label: block for block in cell.classes for label in block}
    a, b = colors.get(n-1), colors.get(n)
    if a is None or b is None:
        case, drop = "AT_LEAST_ONE_LOOP", 0
    elif a == b:
        case, drop = "SAME_NONLOOP_CLASS", 1
    elif len(a) >= 2 and len(b) >= 2:
        case, drop = "DISTINCT_NONSINGLETON_CLASSES", 0
    elif len(a) == len(b) == 1:
        case, drop = "TWO_SINGLETON_CLASSES", 2
    else:
        case, drop = "ONE_SINGLETON_CLASS", 1
    assert target.dimension == cell.dimension-drop
    return target, case


def amalgamation_certificate(n):
    if n not in (8, 9):
        raise ValueError("Only the two preserved finite transitions are tested")
    upstairs, downstairs = finite_data(n), finite_data(n-1)
    status = {tuple(row["affine_permutation"]): row["admissibility"] for row in json.loads(
        (ROOT/f"results/run2/child_status_n{n-1}.json").read_text())["cells"]}
    mapping, cells = [], []
    for j, cell in enumerate(upstairs["cells"]):
        target, case = amalgamate_cell(cell)
        target_column = downstairs["index"].get(target.affine) if target.dimension == 8 else None
        certificate = status[target.affine] if target.dimension == 8 else None
        assert target_column is not None or target.dimension < 8 or certificate["status"] == "CERTIFIED_NON_TILE"
        mapping.append(target_column)
        cells.append({"source_column": j, "source_affine": cell.affine, "case": case,
                      "output_affine": target.affine, "output_bases": target.bases,
                      "output_classes": target.classes, "output_dimension": target.dimension,
                      "output_admissibility": certificate, "target_tile_column": target_column,
                      "zero_reason": None if target_column is not None else "DIMENSION_DROP" if target.dimension < 8 else "CERTIFIED_NON_TILE"})
    def map_vector(row):
        result = [0]*len(downstairs["columns"])
        for j, coefficient in enumerate(row):
            if coefficient and mapping[j] is not None:
                result[mapping[j]] += coefficient
        return result
    relation_images = []
    for i, row in enumerate(upstairs["data"]["rows"]):
        image = map_vector(row)
        remainder = normal_form(image, downstairs)
        assert not remainder
        relation_images.append({"source_row_index": i, "image": image,
                                "downstairs_rref_coefficients": [image[p] for p in downstairs["pivots"]],
                                "normal_form_remainder": []})
    insertion = []
    for cell in downstairs["cells"]:
        injected = cell_from_bases(n, cell.bases)
        j = upstairs["index"][injected.affine]
        assert mapping[j] == downstairs["index"][cell.affine]
        insertion.append(j)
    for row in downstairs["data"]["rows"]:
        injected = [0]*len(upstairs["columns"])
        for j, value in enumerate(row):
            injected[insertion[j]] = value
        assert not normal_form(injected, upstairs)
    induced = []
    for column in upstairs["free_columns"]:
        source = [0]*len(upstairs["columns"])
        source[column] = 1
        image = normal_form(map_vector(source), downstairs)
        induced.append([str(image.get(j, QQ.zero)) for j in downstairs["free_columns"]])
    induced_rank = _rank(induced, len(downstairs["free_columns"]))
    assert induced_rank == len(downstairs["free_columns"])
    base_up = [0]*len(upstairs["columns"])
    for row in standard_k2(n):
        base_up[upstairs["index"][row["affine"]]] = 1
    base_down = [0]*len(downstairs["columns"])
    for row in standard_k2(n-1):
        base_down[downstairs["index"][row["affine"]]] = 1
    assert map_vector(base_up) == base_down
    return {"n": n, "downstairs_n": n-1, "claim_tag": "COMPUTATIONALLY-VERIFIED",
            "scope": "EXACT_FINITE_COMBINATORIAL_QUOTIENT_MAP; NOT A GEOMETRIC PUSHFORWARD CLAIM",
            "column_map": mapping, "source_cell_images": cells,
            "output_histogram": dict(Counter(f"dim{r['output_dimension']}:"+("TILE" if r["target_tile_column"] is not None else "ZERO") for r in cells)),
            "case_histogram": dict(Counter(r["case"] for r in cells)),
            "relation_images": relation_images,
            "downstairs_rref_basis": [[(j, str(x)) for j, x in sorted(row.items())] for row in downstairs["rref"]],
            "image_local_rank_over_Q": _rank([r["image"] for r in relation_images], len(downstairs["columns"])),
            "all_relations_map_into_downstairs_local_span": True,
            "last_loop_insertion_columns": insertion, "insertion_is_right_inverse_on_free_tile_spaces": True,
            "quotient_matrix": induced, "quotient_map_rank_over_Q": induced_rank,
            "quotient_kernel_dimension": len(upstairs["free_columns"])-induced_rank,
            "standard_upstairs_tiling": base_up, "standard_downstairs_tiling": base_down,
            "standard_tiling_maps_exactly_to_standard_tiling": True,
            "not_claimed": "An all-n amalgamation theorem, a geometric tile pushforward, or generation from a quotient map"}


@lru_cache(maxsize=None)
def loopless_tile_cores(q):
    if q == 6:
        return (cell_from_bases(6, combinations(range(1, 7), 2)),)
    if q in (7, 8, 9):
        return tuple(cell for cell in finite_data(q)["cells"] if not cell.loops)
    if q == 10:
        cores = {}
        for start in range(1, 6):
            a = {(start+j-1) % 10+1 for j in range(5)}
            b = set(range(1, 11))-a
            cell = cell_from_bases(10, [(i, j) for i in a for j in b])
            cores[cell.affine] = cell
        assert len(cores) == 5
        return tuple(cores[w] for w in sorted(cores))
    return ()


@lru_cache(maxsize=None)
def normalized_core_data(n):
    if n not in range(6, 12):
        raise ValueError("The finite normalized core diagnostic stops at n11")
    cells = list(loopless_tile_cores(n))
    cells += [embed(c, n, range(2, n+1)) for c in loopless_tile_cores(n-1)]
    cells.sort(key=lambda c: c.affine)
    index = {c.affine: j for j, c in enumerate(cells)}
    prototypes = json.loads((ROOT/"results/run4/sign_relations.json").read_text())["relations"]
    parent_rows = {}
    for prototype in prototypes:
        q = prototype["n"]
        if q not in (n-1, n):
            continue
        parent = cell_from_bases(q, affine.bases(tuple(prototype["parent_affine"])))
        support = tuple(range(1, n+1)) if q == n else tuple(range(2, n+1))
        for direction in (-1, 1):
            for shift in range(q):
                target_parent = embed(relabel(parent, direction, shift), n, support)
                row = [0]*len(cells)
                walls = []
                for wall in prototype["signed_admissible_facets"]:
                    source = cell_from_bases(q, wall["bases"])
                    target = embed(relabel(source, direction, shift), n, support)
                    coefficient = wall["coefficient"]
                    column = index.get(target.affine)
                    if column is not None:
                        row[column] += coefficient
                    walls.append({"affine": target.affine, "bases": target.bases,
                                  "normalized_column": column, "coefficient": coefficient})
                if any(row):
                    sign = 1 if next(x for x in row if x) > 0 else -1
                    row = tuple(sign*x for x in row)
                    key = target_parent.affine
                    origin = {"prototype_id": prototype["id"], "core_n": q,
                              "direction": direction, "shift": shift, "support": support,
                              "common_sign": sign}
                    if key in parent_rows:
                        assert parent_rows[key]["row"] == row
                        parent_rows[key]["transport_origins"].append(origin)
                    else:
                        parent_rows[key] = {"parent_affine": key, "parent_bases": target_parent.bases,
                                            "row": row, "unscaled_full_walls": walls,
                                            "transport_origins": [origin]}
    parents = [parent_rows[w] for w in sorted(parent_rows)]
    rows = [row["row"] for row in parents]
    reduced, pivots = _domain(rows, len(cells)).rref()
    _, independent = _domain(rows, len(cells)).transpose().rref()
    sparse = reduced.to_dod()
    basis = [sparse[i] for i in range(len(pivots))]
    minor = [[rows[i][j] for j in pivots] for i in independent]
    # These matrices have at most66 columns; exact determinant remains bounded.
    determinant = _domain(minor, len(pivots)).det() if pivots else QQ.one
    unit_decompositions = None
    if len(pivots) == len(cells):
        inverse = _domain(minor, len(cells)).inv().to_list()
        unit_decompositions = [[(independent[i], str(value)) for i, value in enumerate(row) if value]
                               for row in inverse]
    return {"n": n, "cells": cells, "index": index, "rows": rows, "pivots": pivots,
            "rref": basis, "free_columns": tuple(j for j in range(len(cells)) if j not in pivots),
            "artifact": {"n": n, "normalized_tile_count": len(cells), "projected_parent_count": len(rows),
                         "columns": [{"affine": c.affine, "bases": c.bases, "classes": c.classes,
                                      "support": c.support, "loops": c.loops} for c in cells],
                         "projected_parent_rows": parents, "rows": rows,
                         "rank_over_Q": len(pivots), "normalized_quotient_dimension": len(cells)-len(pivots),
                         "rref_rows": [[(j, str(x)) for j, x in sorted(row.items())] for row in basis],
                         "pivot_columns": pivots, "independent_row_indices": independent,
                         "minor_determinant_exact": str(determinant),
                         "unit_vector_local_decompositions": unit_decompositions}}


def amalgamate_at(cell, face):
    """Cyclic-bar faces on source bases, including the signed wrap face."""
    n = cell.n
    if not 0 <= face < n:
        raise ValueError("There are n adjacent amalgamation faces")
    if face == n-1:
        mapping = {i: 1 if i == n else i for i in range(1, n+1)}
    else:
        left, right = face+1, face+2
        mapping = {i: left if i == right else i-int(i > right) for i in range(1, n+1)}
    bases = {tuple(sorted((mapping[i], mapping[j]))) for i, j in cell.bases if mapping[i] != mapping[j]}
    return cell_from_bases(n-1, bases)


def normalized_boundary_certificate(n):
    upstairs, downstairs = normalized_core_data(n), normalized_core_data(n-1)
    boundary, face_records = [], []
    for cell in upstairs["cells"]:
        row, faces = [0]*len(downstairs["cells"]), []
        for face in range(n):
            target = amalgamate_at(cell, face)
            column = downstairs["index"].get(target.affine) if target.dimension == 8 else None
            if column is not None:
                row[column] += (-1)**face
            faces.append({"face": face, "output_affine": target.affine,
                          "output_dimension": target.dimension, "normalized_column": column})
        boundary.append(row)
        face_records.append(faces)
    relation_checks = []
    for source in upstairs["rows"]:
        image = [sum(coefficient*boundary[i][j] for i, coefficient in enumerate(source))
                 for j in range(len(downstairs["cells"]))]
        assert not normal_form(image, downstairs)
        relation_checks.append(image)
    quotient_rows = []
    for column in upstairs["free_columns"]:
        reduced = normal_form(boundary[column], downstairs)
        quotient_rows.append([str(reduced.get(j, QQ.zero)) for j in downstairs["free_columns"]])
    rank = _rank(quotient_rows, len(downstairs["free_columns"]))
    return {"n": n, "boundary_matrix": boundary, "face_records": face_records,
            "projected_parent_boundary_images": relation_checks,
            "all_projected_relations_map_to_downstairs_relations": True,
            "source_quotient_basis_columns": upstairs["free_columns"],
            "target_quotient_basis_columns": downstairs["free_columns"],
            "induced_quotient_boundary": quotient_rows, "boundary_rank_over_Q": rank,
            "source_normalized_dimension": len(upstairs["free_columns"]),
            "target_normalized_dimension": len(downstairs["free_columns"])}


def write_normalized_diagnostic():
    records = [normalized_core_data(n)["artifact"] for n in range(6, 12)]
    boundaries = [normalized_boundary_certificate(n) for n in range(7, 12)]
    artifact = {"claim_tag": "COMPUTATIONALLY-VERIFIED", "scope": "PROJECTED_FINITE_CORES_ONLY; NO_FULL_N10_MATRIX",
                "pre_registration": "research/run7/N10_DIAGNOSTIC.md", "normalized_cores": records,
                "alternating_boundaries": boundaries}
    (ROOT/"results/run7/normalized_core_ranks.json").write_text(json.dumps(artifact, indent=2)+"\n")
    return artifact


def main():
    rank_data, blocks = rank_and_support_data()
    amalgamations = [amalgamation_certificate(n) for n in (8, 9)]
    result = {"claim_tag": "COMPUTATIONALLY-VERIFIED", "support_blocks": blocks,
              "amalgamations": amalgamations, "scope": "BOUNDED_N7_N8_N9_FINITE_MATRIX_CERTIFICATES"}
    (ROOT/"results/run7/rank_data.json").write_text(json.dumps(rank_data, indent=2)+"\n")
    (ROOT/"results/run7/block_ranks.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"ranks": [{k: r[k] for k in ("n", "tile_count", "full_local_row_count", "local_rank_over_Q", "quotient_dimension")} for r in rank_data["rank_data"]],
                      "amalgamation_quotient_ranks": [r["quotient_map_rank_over_Q"] for r in amalgamations],
                      "amalgamation_kernel_dimensions": [r["quotient_kernel_dimension"] for r in amalgamations]}, indent=2))


if __name__ == "__main__":
    main()
