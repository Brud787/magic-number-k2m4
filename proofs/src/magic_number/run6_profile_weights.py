"""Profile-constant covectors of the formal all-n local-relation quotient."""

from collections import Counter
from itertools import product
from pathlib import Path
import json

from sympy import Matrix

from . import affine
from .bcfw import standard_k2
from .exact_geometry import matrix_rank
from .parent_profiles import composition_type
from .rank2 import cell_from_bases


ROOT = Path(__file__).resolve().parents[2]


def independent_type(sizes):
    values = tuple(sizes)
    return min(sequence[i:]+sequence[:i] for sequence in (values, tuple(reversed(values)))
               for i in range(len(values)))


def profile_weights(a, b, c, d, e, f):
    return (a, b+2*c-e-f, b-c-d+e+f, b, -c+e+f, c, d, f, f, e, f)


def build_profile_weights():
    inventory = json.loads((ROOT/'results/run6/membership_cores.json').read_text())
    cores = [row for row in inventory['cores'] if row['status'] == 'CERTIFIED_TILE']
    types = tuple(tuple(row['dihedral_composition_type']) for row in cores)
    index = {profile: j for j, profile in enumerate(types)}
    prototypes = json.loads((ROOT/'results/run4/sign_relations.json').read_text())['relations']
    rows, records = [], []
    for prototype in prototypes:
        row = [0]*len(types)
        terms = []
        for facet in prototype['signed_admissible_facets']:
            sizes = tuple(map(len, facet['classes']))
            profile = composition_type(sizes)
            assert profile == independent_type(sizes)
            j = index[profile]
            row[j] += facet['coefficient']
            terms.append({'source_affine': facet['affine'], 'class_sizes': sizes,
                          'profile_column': j, 'coefficient': facet['coefficient']})
        rows.append(row)
        records.append({'relation_id': prototype['id'], 'parent_type': prototype['core_type'],
                        'profile_row': row, 'terms': terms})
    matrix = Matrix(rows)
    reduced, pivot_columns = matrix.rref()
    _, independent_rows = matrix.T.rref()
    assert matrix_rank(rows) == len(pivot_columns) == 5
    basis = [list(profile_weights(*(int(i == j) for i in range(6)))) for j in range(6)]
    assert Matrix(basis).rank() == 6 and matrix*Matrix(basis).T == Matrix.zeros(15, 6)
    high = list(profile_weights(0, 0, 0, 0, -1, 1))
    assert high == [0]*7+[1, 1, -1, 1]
    counts = [0]*11
    for row in standard_k2(9):
        cell = cell_from_bases(9, affine.bases(row['affine']))
        counts[index[composition_type(map(len, cell.classes))]] += 1
    return {'claim_tag': 'PROVED',
            'scope': 'ALL_N_PROFILE_CONSTANT_COVECTORS_ANNIHILATING_LOCAL_ROWS_ONLY',
            'proof_reference': 'research/run6/PROFILE_WEIGHTS.md',
            'tile_profile_columns': types, 'prototype_count': len(prototypes),
            'compressed_matrix': rows, 'prototype_records': records,
            'rank_over_Q': 5, 'nullity': 6,
            'independent_rows': independent_rows, 'pivot_columns': pivot_columns,
            'rank_minor': matrix[list(independent_rows), list(pivot_columns)].tolist(),
            'rank_minor_determinant': int(matrix[list(independent_rows), list(pivot_columns)].det()),
            'nonzero_rref_rows': reduced[:5, :].tolist(),
            'integer_nullspace_basis': basis,
            'parameter_order': ['a=w_111111', 'b=w_1133', 'c=w_1232', 'd=w_1313', 'e=w_333', 'f=w_55'],
            'parameter_formula': ['a', 'b+2c-e-f', 'b-c-d+e+f', 'b', '-c+e+f', 'c', 'd', 'f', 'f', 'e', 'f'],
            'high_support_covector': high,
            'unit_covector_parameters': [1]*6,
            'standard_n9_profile_counts': counts,
            'standard_n9_basis_weight_sums': [sum(x*y for x, y in zip(vector, counts)) for vector in basis],
            'standard_n9_high_support_weight_sum': sum(x*y for x, y in zip(high, counts)),
            'warning': 'These are formal local-quotient covectors for arbitrary n. Equality across arbitrary complete tilings needs D_n subset L_n; descent to all indicator classes needs K_n subset L_n.'}


if __name__ == '__main__':
    data = build_profile_weights()
    path = ROOT/'results/run6/profile_weights.json'
    path.write_text(json.dumps(data, indent=2, default=int)+'\n')
    print({'rank': data['rank_over_Q'], 'nullity': data['nullity'],
           'high_support_n9_value': data['standard_n9_high_support_weight_sum']})
