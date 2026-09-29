# Local relation spaces for the five ten-wall prototypes

**PROVED by exact finite certificates, independently audited in [REVIEW](REVIEW.md).** For each of the five already proved ten-wall parent relations below, the entire space of constant-coefficient all-Z relations among those ten tile indicators is one-dimensional. It is spanned by the existing balanced 5↔5 relation. This is a statement about all relations on each specified facet set, stronger than merely exhibiting one balanced relation. It does not assert generation of relations between arbitrary tiles or connectivity of tilings.

| Prototype | Existing relation proof | Exact positive source seeds examined | Retained overlap edges | Edge-matrix rank |
|---|---|---:|---:|---:|
| `q8:(1,2,1,2,2)` alternating singletons | [Run 3 linear fibers](../run3/LARGER_SUPPORT.md) | 40 | 9 | 9 |
| `q9:(1,2,3,3)` repaired spurion parent | [Run 2 spurion proof](../run2/SPURION_ATTEMPT.md) | 40 | 9 | 9 |
| `q9:(1,3,2,3)` reflected parent | [Run 4 smaller cores](SMALLER_CORES.md) | 40 | 9 | 9 |
| `q10:(3,3,4)` | [Run 4 q10 proof](Q10_334.md) | 40 | 9 | 9 |
| `q10:(2,4,4)` | [Run 4 q10 proof](Q10_334.md) | 40 | 9 | 9 |

The ordered source representatives used in the fixtures are those of the respective source modules; the displayed cyclic size profiles identify their cores up to dihedral symmetry. The source relation proofs establish all-Z injectivity of each selected wall, pairwise disjoint open images on each side, and equality of the two closed unions. Those statements are independent inputs here. Their exact fixture paths and SHA-256 digests are preserved with this new certificate.

## An overlap tree forces a unique relation

Let ten tile images `T_0,...,T_9` have a known relation
\[
\sum_{i=0}^9\epsilon_i\mathbf1_{T_i}=0,
\qquad \epsilon_i\in\{+1,-1\},\quad \sum_i\epsilon_i=0,
\]
with each same-sign collection forming a multiplicity-one tiling of the same region. Fix one external matrix `Z_0`. Form a graph with these ten tile labels as vertices. An edge `ij` is certified by a nonempty open intersection of the open images of `T_i` and `T_j`, with opposite signs.

On that intersection no other same-side open tile occurs, because both side collections have disjoint open images. If using closed tile indicators, remove the finite union of the other tile boundaries; each boundary has dimension below eight, so the intersection still contains a nonempty open subset. Thus any constant-coefficient indicator relation, even one interpreted modulo lower-dimensional sets, imposes
\[
c_i+c_j=0
\]
for every edge.

If the graph is connected, these equations propagate from one vertex and give `c=lambda epsilon`. Equivalently, the matrix with one row `e_i+e_j` for each edge of a spanning tree has rank nine and nullspace `R epsilon`. Since the known relation supplies this one-dimensional subspace, it is the complete relation space at `Z_0`. Every constant-coefficient relation required to hold for all positive external matrices must in particular hold at `Z_0`; its coefficient vector therefore belongs to that same span. Conversely the canonical relation already holds all-Z. This proves the claimed all-Z relation-space equality.

This argument needs neither a complete chamber enumeration nor a classification of all pairwise overlaps. A single certified spanning tree suffices. It also does not prove that the relation space has dimension one at every other fixed positive `Z`: the exact witness graph is constructed at one matrix. The all-Z coefficient-space conclusion follows by restriction to that matrix.

## Exact edge certificates

For each prototype take the rational external rows
\[
Z_i=(1,i,i^2,i^3,i^4,i^5).
\]
All ordered six-minors are positive Vandermonde products. Each source chart uses ten positive homogeneous coordinates and has a one-dimensional projective fiber, as proved in the linked source analyses.

For a positive rational seed `x`, the implementation independently solves the twelve ambient linear equations
\[
C(v)Z=L\,C(x)Z
\]
with ten coefficient unknowns `v` and four unknown entries of the row-change matrix `L`. Their two-dimensional kernel is normalized using the proven pivot of the relevant source chart. Writing its oriented tangent as `h`, the full coefficient interval has endpoints
\[
\ell=\max_{h_i>0}(-x_i/h_i),\qquad
u=\min_{h_i<0}(-x_i/h_i).
\]
If exactly one coefficient vanishes at each endpoint, both endpoints lie in open coordinate wall cells. The source chart is globally complete and all its other coefficients are strictly positive. The existing wall certificates therefore place the two points in genuine all-Z admissible tiles. Their exact target row spaces agree with `C(x)Z` by the displayed invertible row-change matrices. Since open tile images are open by injectivity and invariance of domain, the common target proves a nonempty open intersection.

Only edges joining previously disconnected graph components were retained. The bounded search used at most 99 seeds per prototype and stopped after 40 in all five cases. The first 30 seeds use small positive integers; subsequent seeds give one selected coordinate the positive rational value `1/1000`, cycling through the ten coordinates. No zero-coordinate sample is used as an interior parent seed, and no generic numerical rank is used to assert wall injectivity.

Every retained edge stores the seed, the common target representative, the fiber tangent, both endpoint coefficient vectors and source matrices, the two wall indices, and both exact invertible image row changes. The fixtures also store each wall's affine permutation and bases and the full nine-by-ten edge matrix. All five edge matrices have rank nine and annihilate the known five-plus/five-minus vector.

The independent tests verify all ordered source two-minors and the exact positroid labels of the endpoint matrices. They check image equality by comparing every target two-minor up to a positive scalar, separately from the producer's row-change equation. A graph traversal verifies connectivity, and exact rational linear algebra verifies the kernel and zero coefficient sum.

## Scope and artifacts

The new statements concern precisely five finite sets of ten admissible tiles. They do not imply that arbitrary tiling relations are generated by these sets, that tilings are flip connected, or that all minimal dependencies are balanced. Their use in a parent-core theorem must retain the distinction between a relation on one complete facet set and an arbitrary relation across different parent sets.

Files:

- [Implementation](../../src/magic_number/local_relation_kernels.py)
- [Exact fixture](../../fixtures/run4/local_relation_kernels.json)
- [Machine-readable summary](../../results/run4/local_relation_kernels.json)
- [Independent tests](../../tests/test_local_relation_kernels.py)

```sh
PYTHONPATH=src .venv/bin/python -m magic_number.local_relation_kernels
PYTHONPATH=src .venv/bin/python -m pytest tests/test_local_relation_kernels.py -q
```

The independent proof audit passed. The all-Z geometric side decompositions remain supported by their separate source proofs; this note adds the exact uniqueness-of-relation certificates.
