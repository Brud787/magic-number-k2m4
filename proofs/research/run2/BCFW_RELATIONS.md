# Certified BCFW image relations and a limitation of seven-column moves

Run 2, 2026-09-05. This is a bounded source-backed and exact-combinatorial computation. It uses no spurion repair and no sampled amplituhedron membership tests.

## Geometric certification before linear algebra

**SOURCE-VERIFIED.** KWZ Definition 6.2 and Theorem 6.3 identify the standard BCFW cells through pairs of noncrossing paths. The implementation in `src/magic_number/bcfw.py` was established in Run 1 independently of the spurion Appendix. Their images form an all-Z tiling by the standard BCFW tiling theorem, and more generally by the supplied BCFW v3 Theorem 13.3. BCFW cell injectivity is Theorem 8.7. [BCFW v3](https://arxiv.org/abs/2310.17727v3).

Cyclic shifts and reflections produce further all-Z tilings. The signed cyclic action preserves positivity; because m is even, the compatible sign conventions on the source and external data agree. Reflection similarly changes only the prescribed orientation signs. Alternatively, these closure operations on complete BCFW collections are explicit in Definition 13.2. Thus transforming a standard collection gives a source-certified all-Z tiling, not merely a relabeled numerical example.

**PROVED (elementary deduction from these source theorems).** For two such complete collections T and T', set

\[
T_+=T\setminus T',\qquad T_-=T'\setminus T.
\]

Then for every positive Z,

\[
\sum_{S\in T_+}[1_{Z_S}]=\sum_{S\in T_-}[1_{Z_S}],
\]

in the vector space of semialgebraic indicator functions modulo sets of dimension less than eight. This follows by subtracting the two tiling identities. Boundaries are negligible in this quotient: each source boundary has dimension at most seven, and its semialgebraic image cannot have greater dimension. No canonical-form additivity conjecture is used.

Each side has pairwise-disjoint open tiles, inherited from its complete tiling. Moreover, the corresponding closed unions are equal: each tile is the closure of its open image, and an injective continuous map from an eight-dimensional cell to `Gr(2,6)` has open image by invariance of domain. Two finite unions of these regular closed regions cannot differ by a lower-dimensional set. Thus the recorded relations also certify local geometric substitutions whenever their positive side occurs in a tiling.

An increasing insertion of zero columns transfers a relation from support `[7]` into any seven-element subset I of `[8]`. For every positive `8 x 6` matrix Z, the row submatrix Z_I is positive, and `(insert_I C) Z = C Z_I`. This proves the inserted relation for all Z and proves the inserted cells remain tiles. No converse positive-extension statement is needed.

The signs `+1` and `−1` in these image relations come from subtraction of complete tilings. They are not asserted to be the oriented cellular boundary signs of a nine-dimensional source cell.

## An explicit nontrivial 3-for-3 relation

**COMPUTATIONALLY-VERIFIED combinatorial fixture; SOURCE-VERIFIED all-Z geometry via the deduction above.** The first local relation, `n7-G000`, has the common nine-dimensional parent

\[
P=(12)(3)(4)(5)(6)(7),\qquad
f_P=(2,4,5,6,7,8,10).
\]

Its two sides are:

| Sign | Affine permutation | Parallel classes |
|---|---|---|
| + | `(1,4,5,6,7,9,10)` | `(2)(3)(4)(5)(6)(7)` |
| + | `(2,4,5,7,6,8,10)` | `(12)(3)(4)(56)(7)` |
| + | `(2,5,4,6,7,8,10)` | `(12)(34)(5)(6)(7)` |
| − | `(2,4,5,6,8,7,10)` | `(12)(3)(4)(5)(67)` |
| − | `(2,4,6,5,7,8,10)` | `(12)(3)(45)(6)(7)` |
| − | `(4,2,5,6,7,8,10)` | `(1)(3)(4)(5)(6)(7)` |

The two complete six-tile tilings have three common tiles, which are canceled. Every displayed cell has dimension eight; its basis set is contained in that of P, so it is a source facet. The source incidence is independently checked through the bounded-affine encoding. In contrast to the Run 1 spurion issue, this parent and the two complete-tiling witnesses agree exactly.

There are seven distinct standard-dihedral tilings for n=7 and 21 distinct pair differences. Seven of those differences fit a single nine-dimensional parent, each a 3-for-3 relation. All seven possible parents in this source-dimension class occur. The other pair differences have five or six terms on each side. No arbitrary-tiling classification follows from these orbit counts.

For n=8 there are 16 distinct standard-dihedral tilings and 120 pair differences. The reduced positive/negative side sizes are 12,13,18,19,20. None of these complete-orbit differences fits a single nine-dimensional parent. Inserting a zero at each of eight positions in each of the seven n=7 local relations yields **56 distinct certified local 3-for-3 relations** in n=8. Each has a unique nine-dimensional source parent of support seven.

The machine-readable tilings, their explicit dihedral label actions, both sides of every relation, and parent labels are in [`../../results/run2/bcfw_relations.json`](../../results/run2/bcfw_relations.json). Its all-Z witnesses are complete tiling pairs or increasing row-submatrix insertions.

## Exact relation spaces

A column denotes a participating source-certified tile, identified by its bounded affine permutation. A row has `+1` on its positive side and `−1` on its negative side. All ranks below are over Q, checked independently by SymPy and rational Gaussian elimination in `exact_geometry.matrix_rank`.

| Recorded relations | Rows | Participating tile columns | Q-rank | Dimension of the quotient by these rows |
|---|---:|---:|---:|---:|
| n=7 local common-parent relations | 7 | 21 | 6 | 15 |
| n=7 all standard-orbit pair differences | 21 | 21 | 6 | 15 |
| n=8 inserted seven-column local relations | 56 | 140 | 48 | 92 |
| n=8 standard-orbit pair differences | 120 | 144 | 15 | 129 |
| n=8 both families together | 176 | 168 | 63 | 105 |

**COMPUTATIONALLY-VERIFIED.** Each row has coefficient sum zero. Therefore the all-ones covector annihilates this finite relation space. This fact is built into the use of equal-cardinality complete BCFW collections; it provides no evidence that every unknown relation is balanced. The quotient dimensions concern only the displayed free vector spaces modulo the recorded rows, not the true indicator-function quotient and not a classification of all tile weights.

The exact matrices are reconstructible from the relation JSON. Column orders and all rank/quotient data are recorded in [`../../results/run2/relation_linear_algebra.json`](../../results/run2/relation_linear_algebra.json).

## A precise obstruction to the selected move set

**COMPUTATIONALLY-VERIFIED with an elementary linear-algebra implication.** Inside the common 168-column space, let V be the span of the 56 inserted local rows, and W the span of the 120 pair differences of the 16 standard-dihedral tilings. The computation gives

\[
\dim V=48,\qquad\dim W=15,\qquad\dim(V+W)=63,
\]

so `V intersect W = {0}`. The difference of any two distinct orbit tilings is a nonzero element of W and hence is not in V.

A sequence using only the selected 56 local substitutions changes a tiling's incidence vector by a sum of rows in V. Consequently **these 56 selected seven-column moves cannot connect any two distinct members of the 16-element n=8 standard-dihedral orbit**, even if arbitrary intermediate collections are allowed.

This rules out that particular generation proposal. It does not disprove connectivity under all possible geometric flips, and it does not classify eight-column moves. The obstruction indicates that a sufficient move set must include additional relations with genuinely larger support or otherwise enlarge the span. The nine-dimensional-parent catalog maintained by the other Run 2 task is the appropriate next place to seek them.

## Limits and reproduction

No n=9 relation enumeration was launched: n=7 and n=8 already supplied certified nontrivial relations and a decisive limitation of the chosen move set. No form-relation identity, numerical sample, or source-boundary relation was promoted to an image relation without the complete-tiling witness.

```sh
PYTHONPATH=src .venv/bin/python -m magic_number.certified_relations
PYTHONPATH=src .venv/bin/python -m pytest tests/test_certified_relations.py -q
```

The five new tests pass. They check exact complete-tiling witnesses, source dimensions/incidences, insertion at the full matroid-basis level, distinct local relations, and both independent rank calculations. No novelty claim or arbitrary-tiling theorem is made.
