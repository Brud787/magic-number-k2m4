"""Bounded genuine n9 flip walk; retained ancestry certifies every tiling."""

from __future__ import annotations

import hashlib
import json
import random
from fractions import Fraction
from pathlib import Path

from .bcfw import standard_k2
from .run6_local_span import modular_determinant


ROOT = Path(__file__).resolve().parents[2]
LOCAL_PATH = "results/run6/local_relation_matrix_n9.json"
OUTPUT_PATH = "results/run6/tiling_span_witness_n9.json"
SYMMETRY_PATH = "results/run6/tiling_symmetry_completion_n9.json"
PRIME = 1_000_003


def _load():
    return json.loads((ROOT / LOCAL_PATH).read_text())


def _indices(mask):
    return [j for j in range(mask.bit_length()) if mask >> j & 1]


def _mask(indices):
    return sum(1 << j for j in indices)


def _difference(state, base, count):
    return [int(bool(state >> j & 1))-int(bool(base >> j & 1)) for j in range(count)]


def _reduce_mod(row, echelon):
    reduced = {j: x % PRIME for j, x in row.items() if x % PRIME}
    for pivot in sorted(echelon):
        factor = reduced.get(pivot, 0)
        if factor:
            for j, value in echelon[pivot].items():
                updated = (reduced.get(j, 0)-factor*value) % PRIME
                if updated:
                    reduced[j] = updated
                else:
                    reduced.pop(j, None)
    return reduced


def rational_determinant(matrix):
    work = [{j: Fraction(x) for j, x in enumerate(row) if x} for row in matrix]
    answer = Fraction(1)
    for k in range(len(work)):
        pivot = next((i for i in range(k, len(work)) if work[i].get(k)), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            work[k], work[pivot] = work[pivot], work[k]
            answer = -answer
        coefficient = work[k][k]
        answer *= coefficient
        tail = {j: value/coefficient for j, value in work[k].items() if j != k}
        for i in range(k+1, len(work)):
            factor = work[i].pop(k, Fraction(0))
            if factor:
                for j, value in tail.items():
                    reduced = work[i].get(j, Fraction(0))-factor*value
                    if reduced:
                        work[i][j] = reduced
                    else:
                        work[i].pop(j, None)
    return answer


def build_certificate(max_states=15000, max_steps=30000, seed=9062026, progress=False):
    if not 1 <= max_states <= 15000 or not 1 <= max_steps <= 30000:
        raise ValueError("The authorized bounded walk permits 15000 states and 30000 steps")
    local = _load()
    columns, rows = local["column_affine_permutations"], local["rows"]
    index = {tuple(window): j for j, window in enumerate(columns)}
    base_sources = list(standard_k2(9))
    base = _mask(index[row["affine"]] for row in base_sources)
    assert base.bit_count() == 50 and len(columns) == 942 and len(rows) == 693
    target = local["rank_over_Q"]
    moves = []
    restricted = []
    for i, row in enumerate(rows):
        assert sum(row) == 0 and set(row) <= {-1, 0, 1}
        plus = _mask(j for j, value in enumerate(row) if value == 1)
        minus = _mask(j for j, value in enumerate(row) if value == -1)
        moves.extend(((i, 1, minus, plus), (i, -1, plus, minus)))
        restricted.append({j: row[p] for j, p in enumerate(local["pivot_columns"]) if row[p]})
    rng = random.Random(seed)
    states, parents, transitions = [base], [None], [None]
    seen, visits = {base: 0}, {base: 1}
    echelon, dependent, selected = {}, set(), []
    selected_edge_rows = []
    current, steps, legal_examined = 0, 0, 0
    stop = "STEP_CAP"
    while steps < max_steps:
        state = states[current]
        legal = [move for move in moves if state & move[2] == move[2] and not state & move[3]]
        legal_examined += len(legal)
        if not legal:
            stop = "NO_LEGAL_FLIP"
            break
        rng.shuffle(legal)
        chosen, independent_reduction = None, None
        for move in legal:
            row_index = move[0]
            if row_index in dependent:
                continue
            reduced = _reduce_mod(restricted[row_index], echelon)
            if reduced:
                chosen, independent_reduction = move, reduced
                break
            dependent.add(row_index)
        if chosen is None:
            # Deterministic seeded exploration prefers unvisited or rarely visited states.
            chosen = min(legal, key=lambda move: visits.get((state ^ move[2]) | move[3], 0))
        row_index, direction, removed, added = chosen
        child = (state ^ removed) | added
        assert child.bit_count() == 50
        if child not in seen:
            if len(states) == max_states:
                stop = "STATE_CAP"
                break
            seen[child] = len(states)
            states.append(child)
            parents.append(current)
            transitions.append((row_index, direction))
        child_id = seen[child]
        if independent_reduction is not None:
            # All previously visited state differences lie in the accumulated edge span.
            assert child_id == len(states)-1 and parents[child_id] == current
            pivot = min(independent_reduction)
            inverse = pow(independent_reduction[pivot], -1, PRIME)
            echelon[pivot] = {j: value*inverse % PRIME for j, value in independent_reduction.items()}
            dependent.add(row_index)
            selected.append(child_id)
            selected_edge_rows.append(row_index)
        current = child_id
        visits[child] = visits.get(child, 0)+1
        steps += 1
        if progress and (steps % 1000 == 0 or independent_reduction is not None and len(selected) % 50 == 0):
            print(json.dumps({"steps": steps, "states": len(states), "rank_lower_bound": len(selected)}), flush=True)
        if len(selected) == target:
            stop = "TARGET_RANK_REACHED"
            break
    retained = {0}
    for node in selected:
        while node is not None and node not in retained:
            retained.add(node)
            node = parents[node]
    proof_nodes = []
    for node in sorted(retained):
        record = {"node_id": node, "parent_node_id": parents[node]}
        if node:
            row_index, direction = transitions[node]
            record.update({"local_row_index": row_index, "direction": direction,
                           "local_relation_id": local["relations"][row_index]["id"],
                           "source_parent_affine": local["relations"][row_index]["parent_affines"][0]})
        proof_nodes.append(record)
    tilings = []
    for node in selected:
        coefficients, path, ancestor = {}, [], node
        while ancestor:
            path.append(ancestor)
            row_index, direction = transitions[ancestor]
            coefficients[row_index] = coefficients.get(row_index, 0)+direction
            ancestor = parents[ancestor]
        tilings.append({"node_id": node, "tile_columns": _indices(states[node]),
                        "difference_from_base": _difference(states[node], base, len(columns)),
                        "ancestral_node_path": list(reversed(path)),
                        "integer_local_coefficients": [[i, c] for i, c in sorted(coefficients.items()) if c]})
    # The independent edge rows give a cheap rational lower certificate. Their
    # independent tiling differences have the same span by chronological induction.
    restricted_edges = [restricted[i] for i in selected_edge_rows]
    pivot_columns = sorted(echelon)
    edge_minor = [[row.get(j, 0) for j in pivot_columns] for row in restricted_edges]
    residue = modular_determinant(edge_minor, PRIME)
    assert residue
    ambient_pivots = [local["pivot_columns"][j] for j in pivot_columns]
    difference_minor = [[tiling["difference_from_base"][j] for j in ambient_pivots]
                        for tiling in tilings]
    difference_determinant = str(rational_determinant(difference_minor))
    return {"n": 9, "k": 2, "m": 4, "claim_tag": "COMPUTATIONALLY-VERIFIED",
            "scope": "BOUNDED_GENUINE_ALL_Z_TILING_DIFFERENCE_WITNESSES",
            "local_matrix_reference": LOCAL_PATH,
            "local_matrix_sha256": hashlib.sha256((ROOT / LOCAL_PATH).read_bytes()).hexdigest(),
            "column_affine_permutations": columns,
            "base_provenance": "KWZ Definition 6.2 / Theorem 6.3 standard k2 BCFW tiling, generated by bcfw.standard_k2(9)",
            "base_source_records": base_sources, "base_tile_columns": _indices(base),
            "local_geometric_proof": "research/run4/LOCAL_PARENT_THEOREM.md",
            "seed": seed, "state_cap": max_states, "step_cap": max_steps,
            "target_rank": target, "stop_reason": stop, "walk_step_count": steps,
            "discovered_state_count": len(states), "legal_moves_examined": legal_examined,
            "proof_nodes": proof_nodes, "retained_proof_node_count": len(proof_nodes),
            "independent_tilings": tilings, "independent_difference_count": len(selected),
            "selected_edge_row_indices": selected_edge_rows,
            "edge_minor_ambient_columns": ambient_pivots,
            "edge_minor_determinant_modulus": PRIME, "edge_minor_determinant_residue": residue,
            "difference_minor_ambient_columns": ambient_pivots,
            "difference_minor_determinant_exact": difference_determinant,
            "rank_over_Q": len(selected), "total_explicit_tiling_count_including_base": len(selected)+1,
            "rank_proof": "The stored actual tiling-difference minor has the stated exact nonzero determinant; upper bound is the number of selected vectors. Edge independence supplies a separate modular discovery certificate.",
            "not_claimed": "Enumeration of complete tilings, full flip connectivity, or an all-n generation theorem"}


def symmetry_completion(data):
    """Finite symmetries of saved witnesses; no additional flip walk."""
    from . import affine
    local = _load()
    columns, pivots = local["column_affine_permutations"], local["pivot_columns"]
    by_bases = {frozenset(affine.bases(tuple(window))): j for j, window in enumerate(columns)}
    all_bases = [affine.bases(tuple(window)) for window in columns]
    rows = [tiling["difference_from_base"] for tiling in data["independent_tilings"]]
    echelon = {}
    def insert(row):
        reduced = _reduce_mod({j: row[p] for j, p in enumerate(pivots) if row[p]}, echelon)
        if not reduced:
            return False
        pivot = min(reduced)
        inverse = pow(reduced[pivot], -1, PRIME)
        echelon[pivot] = {j: x*inverse % PRIME for j, x in reduced.items()}
        return True
    assert all(insert(row) for row in rows)
    extras, examined = [], 0
    for direction in (1, -1):
        for shift in range(9):
            if direction == 1 and shift == 0:
                continue
            mapping = {i: (direction*(i-1)+shift) % 9+1 for i in range(1, 10)}
            column_map = [by_bases[frozenset(tuple(sorted((mapping[i], mapping[j]))) for i, j in bases)]
                          for bases in all_bases]
            for original in data["independent_tilings"]:
                row = [0]*len(columns)
                for j, value in enumerate(original["difference_from_base"]):
                    row[column_map[j]] = value
                examined += 1
                if insert(row):
                    extras.append({"source_node_id": original["node_id"],
                                   "dihedral_action": {"direction": direction, "shift": shift},
                                   "positive_tiling_columns": sorted(column_map[j] for j in original["tile_columns"]),
                                   "negative_tiling_columns": sorted(column_map[j] for j in data["base_tile_columns"]),
                                   "difference": row,
                                   "proof_reference": "Dihedral transport of the retained genuine all-Z tiling and its standard BCFW base"})
                    rows.append(row)
                if len(echelon) == local["rank_over_Q"]:
                    break
            if len(echelon) == local["rank_over_Q"]:
                break
        if len(echelon) == local["rank_over_Q"]:
            break
    ambient_columns = [pivots[j] for j in sorted(echelon)]
    minor = [[row[j] for j in ambient_columns] for row in rows]
    determinant = rational_determinant(minor)
    assert determinant
    return {"n": 9, "k": 2, "m": 4, "claim_tag": "COMPUTATIONALLY-VERIFIED",
            "scope": "FINITE_DIHEDRAL_TRANSPORT_OF_ALREADY_CERTIFIED_TILING_DIFFERENCES",
            "base_certificate_reference": OUTPUT_PATH,
            "base_certificate_sha256": hashlib.sha256((ROOT / OUTPUT_PATH).read_bytes()).hexdigest(),
            "local_matrix_reference": LOCAL_PATH,
            "local_matrix_sha256": hashlib.sha256((ROOT / LOCAL_PATH).read_bytes()).hexdigest(),
            "initial_difference_count": len(data["independent_tilings"]),
            "extra_differences": extras, "symmetry_images_examined": examined,
            "rank_over_Q": len(rows), "target_rank": local["rank_over_Q"],
            "difference_minor_ambient_columns": ambient_columns,
            "difference_minor_determinant_exact": str(determinant),
            "new_flip_states": 0,
            "not_claimed": "A flip path from the original base to its dihedral transforms, full flip connectivity, or all-n generation"}


def main():
    data = build_certificate(progress=True)
    (ROOT / OUTPUT_PATH).write_text(json.dumps(data, indent=2)+"\n")
    print(json.dumps({key: data[key] for key in ("stop_reason", "walk_step_count", "discovered_state_count", "retained_proof_node_count", "independent_difference_count", "rank_over_Q")}, indent=2))
    symmetry = symmetry_completion(data)
    (ROOT / SYMMETRY_PATH).write_text(json.dumps(symmetry, indent=2)+"\n")
    print(json.dumps({"finite_symmetry_completed_rank": symmetry["rank_over_Q"],
                      "extra_differences": len(symmetry["extra_differences"]),
                      "new_flip_states": symmetry["new_flip_states"]}, indent=2))


if __name__ == "__main__":
    main()
