"""Independent positivity, image, graph, and kernel checks for local relations."""
from itertools import combinations
from sympy import Matrix, zeros
from magic_number.local_relation_kernels import FAMILIES, spanning_tree_fixture
from magic_number.rank2 import cell_from_bases


def test_five_overlap_spanning_trees_connect_all_ten_walls_within_the_bound():
    for name in FAMILIES:
        fixture = spanning_tree_fixture(name)
        assert fixture['connected'] and fixture['seeds_used'] <= 99
        assert len(fixture['spanning_tree']) == 9
        adjacency = {i:set() for i in range(10)}
        for edge in fixture['spanning_tree']:
            i,j = (p['wall_index'] for p in edge['endpoints'])
            adjacency[i].add(j)
            adjacency[j].add(i)
        reached,pending = set(),[0]
        while pending:
            node = pending.pop()
            if node in reached: continue
            reached.add(node)
            pending.extend(adjacency[node]-reached)
        assert reached == set(range(10))


def test_every_overlap_is_certified_by_two_positive_sources_and_exact_image_pluckers():
    for name in FAMILIES:
        fixture = spanning_tree_fixture(name)
        z = Matrix(fixture['external_matrix'])
        n = fixture['n']
        for edge in fixture['spanning_tree']:
            y = Matrix(edge['target_representative'])
            for endpoint in edge['endpoints']:
                index = endpoint['wall_index']
                coordinates = endpoint['source_coefficients']
                assert coordinates[index] == 0
                assert all(value > 0 for j,value in enumerate(coordinates) if j != index)
                c = Matrix(endpoint['source_matrix'])
                values = {pair:c[:,[i-1 for i in pair]].det()
                          for pair in combinations(range(1,n+1),2)}
                assert all(value >= 0 for value in values.values())
                cell = cell_from_bases(n,[pair for pair,value in values.items() if value > 0])
                assert cell.affine == fixture['walls'][index]['affine']
                mapped = c*z
                ratio = mapped[:,:2].det()/y[:,:2].det()
                assert ratio > 0
                # Independent of the producer's2x2 image row-change solve.
                for pair in combinations(range(6),2):
                    assert mapped[:,list(pair)].det() == ratio*y[:,list(pair)].det()


def test_every_local_relation_kernel_is_exactly_the_known_balanced_span():
    for name in FAMILIES:
        fixture = spanning_tree_fixture(name)
        incidence = Matrix(fixture['edge_incidence_matrix'])
        coefficients = Matrix(fixture['canonical_relation_coefficients'])
        assert incidence.rank() == 9
        assert incidence*coefficients == zeros(9,1)
        basis = incidence.nullspace()
        assert len(basis) == 1
        assert basis[0] == coefficients*basis[0][0]/coefficients[0]
        assert sum(coefficients) == 0
        assert list(coefficients).count(1) == list(coefficients).count(-1) == 5
