"""Independent exact checks of support blocks, amalgamation and normalized cores."""

import json
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path

from magic_number import affine
from magic_number.exact_geometry import matrix_rank
from magic_number.rank2 import cell_from_bases
from magic_number.run7_blocks import finite_data, normal_form


@lru_cache(maxsize=None)
def read(path):
    return json.loads(Path(path).read_text())


def _fraction_rank(rows):
    echelon = {}
    for source in rows:
        row = {j: Fraction(str(x)) for j, x in enumerate(source) if Fraction(str(x))}
        for pivot in sorted(echelon):
            factor = row.get(pivot, Fraction(0))
            if factor:
                for j, value in echelon[pivot].items():
                    result = row.get(j, Fraction(0))-factor*value
                    if result:
                        row[j] = result
                    else:
                        row.pop(j, None)
        if row:
            pivot = min(row)
            factor = row[pivot]
            echelon[pivot] = {j: value/factor for j, value in row.items()}
    return len(echelon)


def _determinant(matrix):
    work = [list(map(Fraction, row)) for row in matrix]
    result = Fraction(1)
    for j in range(len(work)):
        pivot = next((i for i in range(j, len(work)) if work[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            work[j], work[pivot] = work[pivot], work[j]
            result = -result
        coefficient = work[j][j]
        result *= coefficient
        for i in range(j+1, len(work)):
            multiplier = work[i][j]/coefficient
            if multiplier:
                work[i] = [a-multiplier*b for a, b in zip(work[i], work[j])]
    return result


def _matrix_bases(matrix):
    minors = {(i+1, j+1): matrix[0][i]*matrix[1][j]-matrix[1][i]*matrix[0][j]
              for i, j in combinations(range(len(matrix[0])), 2)}
    assert all(value >= 0 for value in minors.values())
    return {pair for pair, value in minors.items() if value}


def test_preserved_ranks_and_support_filtration_by_quotient_representatives():
    data = read("results/run7/block_ranks.json")
    expected = {7: [7, 15], 8: [28, 92, 103], 9: [84, 372, 471, 472]}
    for record in data["support_blocks"]:
        n = record["n"]
        source = finite_data(n)
        normal_columns = []
        for j in range(len(source["columns"])):
            vector = [0]*len(source["columns"])
            vector[j] = 1
            reduced = normal_form(vector, source)
            normal_columns.append([reduced.get(k, 0) for k in source["free_columns"]])
        for block, rank in zip(record["filtration"], expected[n]):
            assert _fraction_rank([normal_columns[j] for j in block["tile_columns"]]) == block["image_dimension_over_Q"] == rank
        for pair in record["all_pair_intersections"]:
            a, b = pair["deleted_labels"]
            shared = {j for j, cell in enumerate(source["cells"]) if a in cell.loops and b in cell.loops}
            assert shared == set(pair["shared_support"]["tile_columns"])
            assert pair["intersection_dimension_over_Q"] == pair["shared_support"]["image_dimension_over_Q"] == (0 if n == 7 else 1 if n == 8 else 15)


def test_every_fixed_amalgamation_output_by_positive_source_matrix_minors():
    for data in read("results/run7/block_ranks.json")["amalgamations"]:
        n = data["n"]
        for record in data["source_cell_images"]:
            cell = cell_from_bases(n, affine.bases(tuple(record["source_affine"])))
            C = cell.realization()
            A = [row[:-2]+[row[-2]+row[-1]] for row in C]
            assert _matrix_bases(A) == set(map(tuple, record["output_bases"]))
            assert affine.dimension(tuple(record["output_affine"])) == record["output_dimension"]
            assert record["target_tile_column"] == data["column_map"][record["source_column"]]
            if record["output_dimension"] == 8 and record["target_tile_column"] is None:
                assert record["output_admissibility"]["certificate"]["kind"] == "CLASS_COMPLEMENT_SCHUBERT_OBSTRUCTION"


def test_all_local_row_images_and_split_quotient_maps_exactly():
    for data in read("results/run7/block_ranks.json")["amalgamations"]:
        up, down = finite_data(data["n"]), finite_data(data["downstairs_n"])
        basis = [{j: Fraction(x) for j, x in row} for row in data["downstairs_rref_basis"]]
        for source, certificate in zip(up["data"]["rows"], data["relation_images"]):
            image = [0]*len(down["columns"])
            for j, value in enumerate(source):
                target = data["column_map"][j]
                if target is not None:
                    image[target] += value
            assert image == certificate["image"]
            reconstructed = [Fraction(0)]*len(image)
            for coefficient, row in zip(certificate["downstairs_rref_coefficients"], basis):
                for j, value in row.items():
                    reconstructed[j] += coefficient*value
            assert reconstructed == image
        assert _fraction_rank([r["image"] for r in data["relation_images"]]) == data["image_local_rank_over_Q"] == len(down["pivots"])
        assert _fraction_rank(data["quotient_matrix"]) == data["quotient_map_rank_over_Q"] == len(down["free_columns"])
        assert data["quotient_kernel_dimension"] == len(up["free_columns"])-len(down["free_columns"])
        for j, inserted in enumerate(data["last_loop_insertion_columns"]):
            assert data["column_map"][inserted] == j
            assert set(up["cells"][inserted].bases) == set(down["cells"][j].bases)
        output = [0]*len(down["columns"])
        for j, value in enumerate(data["standard_upstairs_tiling"]):
            if data["column_map"][j] is not None:
                output[data["column_map"][j]] += value
        assert output == data["standard_downstairs_tiling"]


def test_normalized_core_rows_match_preserved_full_matrices_at_n7_n8_n9():
    data = read("results/run7/normalized_core_ranks.json")
    for record in data["normalized_cores"]:
        n = record["n"]
        if n not in (7, 8, 9):
            continue
        full = finite_data(n)
        columns = [j for j, cell in enumerate(full["cells"]) if set(cell.loops) <= {1}]
        assert [full["columns"][j] for j in columns] == [tuple(r["affine"]) for r in record["columns"]]
        projected = set()
        for row in full["data"]["rows"]:
            vector = tuple(row[j] for j in columns)
            if any(vector):
                sign = 1 if next(x for x in vector if x) > 0 else -1
                projected.add(tuple(sign*x for x in vector))
        assert projected == set(map(tuple, record["rows"]))


def test_every_new_normalized_parent_transport_by_independent_basis_maps():
    data = read("results/run7/normalized_core_ranks.json")
    prototypes = {r["id"]: r for r in read("results/run4/sign_relations.json")["relations"]}
    for record in data["normalized_cores"]:
        by_bases = {frozenset(map(tuple, row["bases"])): j for j, row in enumerate(record["columns"])}
        for parent in record["projected_parent_rows"]:
            assert affine.dimension(tuple(parent["parent_affine"])) == 9
            for origin in parent["transport_origins"]:
                source = prototypes[origin["prototype_id"]]
                q, direction, shift = origin["core_n"], origin["direction"], origin["shift"]
                mapping = {i: origin["support"][(direction*(i-1)+shift) % q] for i in range(1, q+1)}
                image = [0]*record["normalized_tile_count"]
                for wall in source["signed_admissible_facets"]:
                    bases = frozenset(tuple(sorted((mapping[i], mapping[j]))) for i, j in wall["bases"])
                    if bases in by_bases:
                        image[by_bases[bases]] += origin["common_sign"]*wall["coefficient"]
                assert image == parent["row"]
                source_bases = affine.bases(tuple(source["parent_affine"]))
                transformed = {tuple(sorted((mapping[i], mapping[j]))) for i, j in source_bases}
                assert transformed == set(map(tuple, parent["parent_bases"]))


def test_normalized_rank_certificates_independently_kill_predicted_n10_class():
    data = read("results/run7/normalized_core_ranks.json")
    assert [r["normalized_tile_count"] for r in data["normalized_cores"]] == [1, 15, 50, 66, 35, 5]
    assert [r["normalized_quotient_dimension"] for r in data["normalized_cores"]] == [1, 9, 19, 12, 0, 0]
    for record in data["normalized_cores"]:
        pivots = record["pivot_columns"]
        reduced = [{j: Fraction(x) for j, x in row} for row in record["rref_rows"]]
        for row in record["rows"]:
            reconstructed = [Fraction(0)]*len(row)
            for pivot, basis in zip(pivots, reduced):
                for j, value in basis.items():
                    reconstructed[j] += row[pivot]*value
            assert reconstructed == row
        minor = [[record["rows"][i][j] for j in pivots] for i in record["independent_row_indices"]]
        assert _determinant(minor) == Fraction(record["minor_determinant_exact"]) != 0
        if record["unit_vector_local_decompositions"] is not None:
            for column, expression in enumerate(record["unit_vector_local_decompositions"]):
                vector = [sum(Fraction(c)*record["rows"][i][j] for i, c in expression)
                          for j in range(record["normalized_tile_count"])]
                assert vector == [int(j == column) for j in range(record["normalized_tile_count"])]
                assert all(Fraction(c).denominator == 1 for _, c in expression)
    ten = data["normalized_cores"][4]
    assert ten["rank_over_Q"] == 35 and ten["minor_determinant_exact"] == "-1"


def test_all_normalized_faces_from_actual_signed_matrix_amalgamation():
    data = read("results/run7/normalized_core_ranks.json")
    cores = {r["n"]: r for r in data["normalized_cores"]}
    for boundary in data["alternating_boundaries"]:
        n = boundary["n"]
        for source, records, expected in zip(cores[n]["columns"], boundary["face_records"], boundary["boundary_matrix"]):
            C = cell_from_bases(n, source["bases"]).realization()
            actual = [0]*cores[n-1]["normalized_tile_count"]
            for face, record in enumerate(records):
                if face == n-1:
                    image = [[row[0]-row[-1]]+row[1:-1] for row in C]
                else:
                    image = [row[:face]+[row[face]+row[face+1]]+row[face+2:] for row in C]
                assert _matrix_bases(image) == set(affine.bases(tuple(record["output_affine"])))
                if record["normalized_column"] is not None:
                    actual[record["normalized_column"]] += (-1)**face
            assert actual == expected


def test_normalized_boundary_descends_and_squares_to_zero_exactly():
    data = read("results/run7/normalized_core_ranks.json")
    cores = {r["n"]: r for r in data["normalized_cores"]}
    expected_ranks = [1, 7, 12, 0, 0]
    for boundary, rank in zip(data["alternating_boundaries"], expected_ranks):
        n = boundary["n"]
        lower = cores[n-1]
        rref = [{j: Fraction(v) for j, v in row} for row in lower["rref_rows"]]
        for row, stored in zip(cores[n]["rows"], boundary["projected_parent_boundary_images"]):
            image = [sum(c*boundary["boundary_matrix"][i][j] for i, c in enumerate(row)) for j in range(lower["normalized_tile_count"])]
            assert image == stored
            reduced = list(map(Fraction, image))
            for pivot, basis in zip(lower["pivot_columns"], rref):
                factor = reduced[pivot]
                for j, value in basis.items():
                    reduced[j] -= factor*value
            assert not any(reduced)
        assert _fraction_rank(boundary["induced_quotient_boundary"]) == boundary["boundary_rank_over_Q"] == rank
    for lower, upper in zip(data["alternating_boundaries"], data["alternating_boundaries"][1:]):
        for row in upper["induced_quotient_boundary"]:
            for j in range(lower["target_normalized_dimension"]):
                assert sum(Fraction(x)*Fraction(lower["induced_quotient_boundary"][k][j]) for k, x in enumerate(row)) == 0
