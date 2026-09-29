"""Independent replay of bounded genuine flips and finite symmetry completion."""

import hashlib
import json
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

from magic_number import affine
from magic_number.bcfw import standard_k2


@lru_cache(maxsize=None)
def read(path):
    return json.loads(Path(path).read_text())


def _column_determinant(matrix):
    """Independent column elimination, recording the pivot-row permutation."""
    size = len(matrix)
    basis, pivot_order = {}, []
    answer = Fraction(1)
    for j in range(size):
        column = {i: Fraction(matrix[i][j]) for i in range(size) if matrix[i][j]}
        for pivot in sorted(basis):
            multiplier = column.get(pivot, Fraction(0))
            if multiplier:
                for i, value in basis[pivot].items():
                    reduced = column.get(i, Fraction(0))-multiplier*value
                    if reduced:
                        column[i] = reduced
                    else:
                        column.pop(i, None)
        if not column:
            return Fraction(0)
        pivot = min(column)
        value = column[pivot]
        answer *= value
        pivot_order.append(pivot)
        basis[pivot] = {i: x/value for i, x in column.items()}
    inversions = sum(pivot_order[i] > pivot_order[j] for i in range(size) for j in range(i+1, size))
    return (-1)**inversions*answer


@lru_cache(maxsize=1)
def replay_walk():
    data = read("results/run6/tiling_span_witness_n9.json")
    local = read(data["local_matrix_reference"])
    assert hashlib.sha256(Path(data["local_matrix_reference"]).read_bytes()).hexdigest() == data["local_matrix_sha256"]
    assert data["column_affine_permutations"] == local["column_affine_permutations"]
    columns, rows = local["column_affine_permutations"], local["rows"]
    index = {tuple(window): j for j, window in enumerate(columns)}
    base = frozenset(index[row["affine"]] for row in standard_k2(9))
    assert len(base) == 50 and sorted(base) == data["base_tile_columns"]
    signed_sides = [({j for j, c in enumerate(row) if c == -1},
                     {j for j, c in enumerate(row) if c == 1}) for row in rows]
    states, nodes = {}, {}
    for node in data["proof_nodes"]:
        node_id, parent = node["node_id"], node["parent_node_id"]
        assert node_id not in states
        nodes[node_id] = node
        if node_id == 0:
            assert parent is None
            states[node_id] = base
            continue
        assert parent in states and parent < node_id
        i, direction = node["local_row_index"], node["direction"]
        assert direction in (-1, 1)
        relation = local["relations"][i]
        assert node["local_relation_id"] == relation["id"]
        assert node["source_parent_affine"] in relation["parent_affines"]
        assert relation["scope"] == "ALL_Z_GEOMETRIC_INDICATOR_RELATION"
        removed, added = signed_sides[i][::direction]
        assert removed <= states[parent] and not (added & states[parent])
        assert len(removed) == len(added) in (3, 5)
        states[node_id] = frozenset((states[parent]-removed) | added)
        assert len(states[node_id]) == 50
    for tiling in data["independent_tilings"]:
        node_id = tiling["node_id"]
        assert sorted(states[node_id]) == tiling["tile_columns"]
        expected = [int(j in states[node_id])-int(j in base) for j in range(942)]
        assert expected == tiling["difference_from_base"] and sum(expected) == 0
        path, coefficients, current = [], {}, node_id
        while current:
            path.append(current)
            node = nodes[current]
            i = node["local_row_index"]
            coefficients[i] = coefficients.get(i, 0)+node["direction"]
            current = node["parent_node_id"]
        assert list(reversed(path)) == tiling["ancestral_node_path"]
        assert sorted((i, c) for i, c in coefficients.items() if c) == list(map(tuple, tiling["integer_local_coefficients"]))
        reconstructed = [0]*942
        for i, coefficient in tiling["integer_local_coefficients"]:
            removed, added = signed_sides[i]
            for j in removed:
                reconstructed[j] -= coefficient
            for j in added:
                reconstructed[j] += coefficient
        assert reconstructed == expected
    return states, nodes


def test_every_ancestral_step_and_integer_tiling_difference_is_exact():
    data = read("results/run6/tiling_span_witness_n9.json")
    states, _ = replay_walk()
    assert data["stop_reason"] == "STATE_CAP"
    assert data["discovered_state_count"] == data["state_cap"] == 15000
    assert data["walk_step_count"] == 14999 <= data["step_cap"] == 30000
    assert len(states) == data["retained_proof_node_count"] == 12857
    assert data["independent_difference_count"] == 461


def test_walk_actual_difference_minor_has_independent_exact_determinant_one():
    data = read("results/run6/tiling_span_witness_n9.json")
    columns = data["difference_minor_ambient_columns"]
    minor = [[row["difference_from_base"][j] for j in columns] for row in data["independent_tilings"]]
    assert len(minor) == len(columns) == data["rank_over_Q"] == 461
    assert _column_determinant(minor) == Fraction(data["difference_minor_determinant_exact"]) == 1


def test_nine_symmetry_extras_are_genuine_tiling_differences_by_basis_maps():
    replay_walk()
    data = read("results/run6/tiling_symmetry_completion_n9.json")
    walk = read(data["base_certificate_reference"])
    local = read(data["local_matrix_reference"])
    assert hashlib.sha256(Path(data["base_certificate_reference"]).read_bytes()).hexdigest() == data["base_certificate_sha256"]
    assert hashlib.sha256(Path(data["local_matrix_reference"]).read_bytes()).hexdigest() == data["local_matrix_sha256"]
    original = {row["node_id"]: row for row in walk["independent_tilings"]}
    column_by_bases = {frozenset(affine.bases(tuple(window))): j for j, window in enumerate(local["column_affine_permutations"])}
    assert len(data["extra_differences"]) == 9 and data["new_flip_states"] == 0
    for extra in data["extra_differences"]:
        source = original[extra["source_node_id"]]
        direction, shift = extra["dihedral_action"]["direction"], extra["dihedral_action"]["shift"]
        def image_column(column):
            bases = affine.bases(tuple(local["column_affine_permutations"][column]))
            image = frozenset(tuple(sorted(((direction*(i-1)+shift) % 9+1,
                                           (direction*(j-1)+shift) % 9+1))) for i, j in bases)
            return column_by_bases[image]
        positive = set(map(image_column, source["tile_columns"]))
        negative = set(map(image_column, walk["base_tile_columns"]))
        assert len(positive) == len(negative) == 50
        assert sorted(positive) == extra["positive_tiling_columns"]
        assert sorted(negative) == extra["negative_tiling_columns"]
        assert extra["difference"] == [int(j in positive)-int(j in negative) for j in range(942)]


def test_complete_470_difference_minor_and_membership_in_local_span():
    data = read("results/run6/tiling_symmetry_completion_n9.json")
    walk, local = read(data["base_certificate_reference"]), read(data["local_matrix_reference"])
    rows = [r["difference_from_base"] for r in walk["independent_tilings"]] + [r["difference"] for r in data["extra_differences"]]
    columns = data["difference_minor_ambient_columns"]
    assert len(rows) == len(columns) == data["rank_over_Q"] == local["rank_over_Q"] == 470
    assert _column_determinant([[row[j] for j in columns] for row in rows]) == Fraction(data["difference_minor_determinant_exact"]) == -1
    reduced_basis = [{j: Fraction(x) for j, x in row} for row in local["rref_nonzero_rows"]]
    # Extra transformed differences lie in L9 independently of the indicator theorem.
    for extra in data["extra_differences"]:
        vector = extra["difference"]
        actual = {}
        for coefficient, row in zip((vector[j] for j in local["pivot_columns"]), reduced_basis):
            if coefficient:
                for j, value in row.items():
                    actual[j] = actual.get(j, Fraction(0))+coefficient*value
        assert {j: x for j, x in actual.items() if x} == {j: Fraction(x) for j, x in enumerate(vector) if x}
