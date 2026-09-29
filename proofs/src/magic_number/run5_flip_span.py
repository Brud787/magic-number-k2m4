"""Bounded discovery of a basis of genuine all-Z tiling differences at n=8.

Every traversal uses a proved Run4 two-sided geometric replacement. Search
stops at target rank or the state cap; it is not complete tiling enumeration.
The output retains only independent tilings and the ancestral proof tree.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from sympy import Matrix


ROOT = Path(__file__).resolve().parents[2]
LOCAL_PATH = "results/run5/local_relation_matrix_n8.json"
BASE_PATH = "results/run5/known_tiling_span_n8.json"
OUTPUT_PATH = "results/run5/tiling_span_witness_n8.json"
PRIME = 1_000_003


def _load(relative_path):
    return json.loads((ROOT / relative_path).read_text())


def _hash(relative_path):
    return hashlib.sha256((ROOT / relative_path).read_bytes()).hexdigest()


def _mask(indices):
    return sum(1 << j for j in indices)


def _indices(mask):
    return [j for j in range(mask.bit_length()) if (mask >> j) & 1]


def _difference(mask, base, count):
    return [((mask >> j) & 1) - ((base >> j) & 1) for j in range(count)]


def _add_modular_row(row, echelon):
    reduced = [x % PRIME for x in row]
    for pivot, basis in echelon:
        factor = reduced[pivot]
        if factor:
            reduced = [(x - factor * y) % PRIME for x, y in zip(reduced, basis)]
    if not any(reduced):
        return False
    pivot = next(j for j, x in enumerate(reduced) if x)
    inverse = pow(reduced[pivot], -1, PRIME)
    echelon.append((pivot, [(x * inverse) % PRIME for x in reduced]))
    echelon.sort(key=lambda item: item[0])
    return True


def build_certificate(max_states=3000, target_rank=73):
    if not 1 <= max_states <= 3000 or not 1 <= target_rank <= 73:
        raise ValueError("This bounded task permits at most 3000 states and rank 73")
    local, known = _load(LOCAL_PATH), _load(BASE_PATH)
    columns, rows = local["column_affine_permutations"], local["rows"]
    index = {tuple(window): j for j, window in enumerate(columns)}
    base_record = next(t for t in known["tilings"] if t["id"] == known["base_tiling"])
    base = _mask(index[tuple(window)] for window in base_record["cells"])
    assert base.bit_count() == 20 and len(columns) == 176 and len(rows) == 96
    moves = []
    for i, row in enumerate(rows):
        assert set(row) <= {-1, 0, 1} and sum(row) == 0
        plus = _mask(j for j, c in enumerate(row) if c == 1)
        minus = _mask(j for j, c in enumerate(row) if c == -1)
        moves.extend(((i, 1, minus, plus), (i, -1, plus, minus)))

    states, parents, steps = [base], [None], [None]
    seen = {base: 0}
    echelon, selected = [], []
    cursor = 0
    legal_attempts = 0
    stop_reason = None
    while cursor < len(states) and stop_reason is None:
        state = states[cursor]
        for row_index, direction, removed, added in moves:
            if state & removed != removed or state & added:
                continue
            legal_attempts += 1
            child = (state ^ removed) | added
            assert child.bit_count() == 20
            if child in seen:
                continue
            if len(states) == max_states:
                stop_reason = "STATE_CAP"
                break
            child_id = len(states)
            seen[child] = child_id
            states.append(child)
            parents.append(cursor)
            steps.append((row_index, direction))
            if _add_modular_row(_difference(child, base, len(columns)), echelon):
                selected.append(child_id)
                if len(selected) == target_rank:
                    stop_reason = "TARGET_RANK_REACHED"
                    break
        cursor += 1
    if stop_reason is None:
        stop_reason = "REACHED_COMPONENT_EXHAUSTED"

    # Retain only the ancestors needed to prove the selected tilings.
    retained = {0}
    for child_id in selected:
        while child_id is not None and child_id not in retained:
            retained.add(child_id)
            child_id = parents[child_id]
    proof_nodes = []
    for node_id in sorted(retained):
        record = {"node_id": node_id, "parent_node_id": parents[node_id]}
        if node_id:
            row_index, direction = steps[node_id]
            relation = local["relations"][row_index]
            record.update({"local_row_index": row_index, "local_relation_id": relation["id"],
                           "direction": direction,
                           "source_parent_affine": relation["parent_affines"][0]})
        proof_nodes.append(record)
    differences = [_difference(states[i], base, len(columns)) for i in selected]
    pivots = tuple(Matrix(differences).rref()[1]) if differences else ()
    assert len(pivots) == len(selected)
    tilings = []
    for node_id, difference in zip(selected, differences):
        path, coefficients = [], [0] * len(rows)
        current = node_id
        while current:
            path.append(current)
            row_index, direction = steps[current]
            coefficients[row_index] += direction
            current = parents[current]
        tilings.append({"node_id": node_id, "tile_columns": _indices(states[node_id]),
                        "difference_from_base": difference,
                        "ancestral_node_path": list(reversed(path)),
                        "integer_local_coefficients": coefficients})
    return {
        "n": 8, "k": 2, "m": 4,
        "scope": "BOUNDED_GENUINE_ALL_Z_FLIP_WITNESSES_FOR_TILING_DIFFERENCE_SPAN",
        "local_matrix_reference": LOCAL_PATH, "local_matrix_sha256": _hash(LOCAL_PATH),
        "base_reference": BASE_PATH, "base_reference_sha256": _hash(BASE_PATH),
        "base_tiling_id": base_record["id"], "base_tile_columns": _indices(base),
        "column_affine_permutations": columns,
        "local_geometric_proof": "research/run4/LOCAL_PARENT_THEOREM.md",
        "base_provenance": known["provenance"],
        "state_cap": max_states, "target_rank": target_rank, "stop_reason": stop_reason,
        "discovered_state_count": len(states), "expanded_state_count": cursor,
        "legal_directed_moves_examined": legal_attempts,
        "retained_proof_node_count": len(proof_nodes), "proof_nodes": proof_nodes,
        "independent_tilings": tilings, "independent_difference_count": len(selected),
        "modular_screen_prime": PRIME, "rank_over_Q": len(pivots),
        "nonzero_square_minor_columns": pivots,
        "total_explicit_tiling_count_including_base": len(selected) + 1,
        "not_claimed": "Enumeration of all tilings or connectivity of the full flip graph",
    }


def verify_certificate(data):
    """Replay the retained geometry certificates and exact integer identities."""
    local, known = _load(LOCAL_PATH), _load(BASE_PATH)
    assert data["local_matrix_sha256"] == _hash(LOCAL_PATH)
    assert data["base_reference_sha256"] == _hash(BASE_PATH)
    assert data["column_affine_permutations"] == local["column_affine_permutations"]
    columns, rows = data["column_affine_permutations"], local["rows"]
    index = {tuple(window): j for j, window in enumerate(columns)}
    base_source = next(t for t in known["tilings"] if t["id"] == data["base_tiling_id"])
    base_set = {index[tuple(window)] for window in base_source["cells"]}
    assert sorted(base_set) == data["base_tile_columns"] and len(base_set) == 20
    states, paths = {}, {}
    for node in data["proof_nodes"]:
        node_id, parent = node["node_id"], node["parent_node_id"]
        assert node_id not in states
        if node_id == 0:
            assert parent is None
            states[node_id], paths[node_id] = base_set, []
            continue
        assert parent in states and parent < node_id
        row_index, direction = node["local_row_index"], node["direction"]
        assert direction in (-1, 1)
        relation = local["relations"][row_index]
        assert node["local_relation_id"] == relation["id"]
        assert node["source_parent_affine"] in relation["parent_affines"]
        assert relation["scope"] == "ALL_Z_GEOMETRIC_INDICATOR_RELATION"
        removed = {j for j, c in enumerate(rows[row_index]) if direction * c == -1}
        added = {j for j, c in enumerate(rows[row_index]) if direction * c == 1}
        assert removed <= states[parent] and not (added & states[parent])
        assert len(removed) == len(added) in (3, 5)
        states[node_id] = (states[parent] - removed) | added
        paths[node_id] = paths[parent] + [node_id]
        assert len(states[node_id]) == 20
    difference_rows = []
    for tiling in data["independent_tilings"]:
        node_id = tiling["node_id"]
        assert tiling["tile_columns"] == sorted(states[node_id])
        assert tiling["ancestral_node_path"] == paths[node_id]
        expected = [int(j in states[node_id]) - int(j in base_set) for j in range(len(columns))]
        assert expected == tiling["difference_from_base"]
        coefficients = tiling["integer_local_coefficients"]
        assert len(coefficients) == len(rows) and all(type(c) is int for c in coefficients)
        assert [sum(c * row[j] for c, row in zip(coefficients, rows))
                for j in range(len(columns))] == expected
        assert sum(expected) == 0
        difference_rows.append(expected)
    from .exact_geometry import matrix_rank
    pivot_columns = data["nonzero_square_minor_columns"]
    minor = [[row[j] for j in pivot_columns] for row in difference_rows]
    rank = matrix_rank(minor) if minor else 0  # Independent Fraction elimination.
    assert rank == len(minor) == len(pivot_columns) == data["rank_over_Q"]
    assert rank == data["independent_difference_count"]
    assert len(data["proof_nodes"]) == data["retained_proof_node_count"]
    assert data["discovered_state_count"] <= data["state_cap"] <= 3000
    return {"replayed_proof_nodes": len(states), "rank_over_Q": rank,
            "fraction_minor_rank": rank, "all_explicit_tilings_have_twenty_tiles": True}


def main():
    data = build_certificate()
    audit = verify_certificate(data)
    data["independent_exact_audit"] = audit
    (ROOT / OUTPUT_PATH).write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({key: data[key] for key in (
        "stop_reason", "discovered_state_count", "expanded_state_count",
        "retained_proof_node_count", "independent_difference_count", "rank_over_Q")}, indent=2))


if __name__ == "__main__":
    main()
