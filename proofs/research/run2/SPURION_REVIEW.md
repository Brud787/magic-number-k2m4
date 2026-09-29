# Independent hostile review of the repaired-parent relation

Reviewer: `/root/spurion`, independently of the author of `SPURION_ATTEMPT.md` and `spurion_relation.py`. Date: 2026-09-05. Reviewed the proof text, implementation, and all ten records in `fixtures/run2/spurion_repaired_candidate.json`. The literal Appendix-A fixture was not changed.

## Verdict and exact scope

**PROVED, using the explicitly identified SOURCE-VERIFIED injectivity inputs:** the argument establishes an all-positive-Z local 5-for-5 replacement for the parent `(91)(2)(345)(678)`, with positive side rows28,34,35,39,45 and negative side B1–B5. Each side consists of injective eight-dimensional tiles, its open tile images are pairwise disjoint, and both closed unions equal the closure of the open parent image.

No fatal gap was found in the linear-fiber proof. The proof does not rely on the misprinted parent or on the printed row38/46 replacement, and does not use canonical-form additivity. Its sample sign evaluations are justified by an independently checked nonvanishing/connectedness argument.

This verdict imports the published all-Z injectivity statement for the spurion itself, from Sections5.1/5.3 of *A cluster of results on amplituhedron tiles*. That paper describes its inverse-functionary argument without a full expanded proof. The present relation proof does not independently reprove that input. The BCFW inputs have exact standard-cell/dihedral/zero-insertion witnesses and use the BCFW tile theorem. These source dependencies must remain visible.

The verdict **does not** establish that the local substitution extends to the literal50-row Appendix tiling, that it is the authors' intended correction, that every local relation is balanced, or that all tilings are connected. It is a separate certified local relation containing a source-known non-BCFW tile. No novelty claim follows.

## 1. Gauge and source cells

For the rotated parent `(12)(3)(456)(789)`, its first, third and fourth projective directions are distinct. A unique projective change of row basis takes them to horizontal, diagonal and vertical directions. The second direction is between the first and third, hence has coordinates proportional to `(u+v,v)` with `u,v>0`. The remaining ambiguity is positive simultaneous scaling of all ten displayed coefficients.

The same normalization is faithful on every selected open wall: the horizontal, diagonal and vertical classes remain nonzero and distinct. At `u=0` or `v=0` only the intervening direction merges with one of its neighbors. At a deleted a-, c- or d-coordinate the corresponding class still has at least one nonzero column. Thus projective coefficient uniqueness really means uniqueness of a Grassmannian source point, and a projective interval of wall coefficients would contradict source-cell injectivity.

The rotated labeling is compatible with positivity: moving old column9 to the front uses `(-C_9,C_1,...,C_8)` in rank two, and external data use `(-Z_9,Z_1,...,Z_8)` in rank six. Their matrix products agree, and both maximal-minor sign conventions remain positive.

All ten wall labels agree with the actual matrix-minor supports and with the fixture's affine permutations. The two other source facets need not be coordinate walls in this globally normalized chart; the proof does not mistakenly identify the projective coefficient simplex with the entire compact source-cell closure.

## 2. Rank eight and the fixed projection pivot

The fiber matrix correctly encodes `C(x)Z=A Y` for some2×2 matrix A, equivalently row containment in Y. Since nonnegative rank-two C maps to rank-two CZ for positive Z, containment is equality of row spaces on the parent and selected open facets.

The rank proof is global. A left-kernel pair `(alpha,beta)` has beta annihilating Y and `Z3,Z7,Z8,Z9`. The determinant

\[
\det(Y_1,Y_2,Z_3,Z_7,Z_8,Z_9)
=-\det(U,Z_3,W,Z_7,Z_8,Z_9)
\]

is strictly negative: U has at least one positive coefficient on1,2, and W at least one on4,5,6. Every nonzero summand on the right is an ordered positive six-minor. Thus beta vanishes. Alpha then annihilates the independent vectors `Z1,...,Z6`, proving rank8.

Deleting the two a-columns leaves an8×8 map. Its left kernel again has beta zero; alpha annihilates `Z3,Z4,Z5,Z6,U,X`. The determinant in that order, with U first and X last, is a strictly positive sum of ordered six-minors. Hence the pivot is invertible for every Y under consideration.

In particular, the normalized kernel basis is intrinsically defined by the a1,a2 coordinates. Although `fiber_matrix` computes it using a local nullspace basis for Y, changes of quotient basis do not change the normalized kernel. Its continuity therefore does not require a global choice of quotient coordinates.

## 3. Injectivity of all ten facets and transversality

For the five directly handled deletions, the9-column fiber matrix has rank8 by the stated determinant argument. The relevant six vectors are:

- after deleting an a-coordinate: the other a-column, `Z3,Z4,Z5,Z6`, and X;
- after deleting a c-coordinate: `Z1,Z2,Z3`, the two remaining c-columns, and X.

In each case their determinant has a strictly positive ordered-minor expansion. Since the wall's positive coefficient chart is faithful, its one-dimensional linear kernel gives global projective uniqueness over each image Y. This is stronger than a differential-rank test and establishes injectivity.

The u-wall and the three d-walls have checked KWZ standard-cell witnesses. The v-wall is exactly the rotated source-known spurion. For these walls, source injectivity implies the deleted-column matrix has rank8: if its kernel had dimension at least two, a positive wall coefficient vector would have a nearby nonconstant positive projective family in that kernel. The source chart's faithfulness rules out hidden gauge redundancy. This proves transversality at every open wall point.

## 4. All-Z orientation signs

The vector `K_Y(a2,-a1)` gives the increasing orientation of the normalized projective coordinate. After normalizing `a1+a2=1`, its derivative in a1 is positive, proportional to `a1²+a2²`. This also handles the cases `a1=0` and `a2=0` without an orientation singularity.

Its coordinate normal to an open wall cannot vanish: otherwise the two-dimensional kernel would be contained in that wall, contradicting the deleted-column rank8 result. The normal value depends continuously on positive external data and positive wall coefficients. The latter space is a positive projective orthant. The external-data space is connected because it is a GL⁺(6) bundle over the positive Grassmannian top cell. Therefore each wall's normal sign is constant on the entire all-Z parameter domain.

**COMPUTATIONALLY-VERIFIED by a separate implementation.** I independently recomputed the ten sign evaluations using a12×14 ambient linear system `C(x)Z=A Y`, with four explicit row-change variables A. This avoids the implementation's four-dimensional quotient/nullspace construction. Fixing a1,a2 and inverting the remaining12×12 block gave the same derivatives:

`1, -1, 28/9, 12/7, -922/189, 590/189, -166/189, -64/27, 44/27, -10/27`.

I also independently reconstructed every nonnull standard-recipe witness from its KWZ affine label, stated dihedral action and increasing support. The resulting full basis sets agree with the fixture's target cells. These finite checks verify the exact witnesses; the preceding analytic argument supplies their all-Z scope.

## 5. Interval fibers and exceptional loci

The fixed a1,a2 projection is an isomorphism on the two-dimensional linear kernel. Consequently a nonzero nonnegative kernel vector cannot have `a1=a2=0`; every such ray is captured by normalization `a1+a2=1`. The feasible set is a closed interval in `0<=a1<=1`, and a positive parent coefficient vector supplies an interior point. No unbounded branch or second positive fiber component is omitted.

At least one coordinate vanishes at each endpoint. The locus with at least two zero coefficients and rank-two C is parameterized by finitely many projective faces of dimension at most7, so its image dimension is at most7. This remains valid if the chart loses faithfulness on some lower face: image dimension can only decrease.

If C has rank one while `a1+a2=1`, its horizontal a-columns force every column to be horizontal. Nonnegativity then forces the entire second row to vanish, namely `v=c4=c5=c6=d7=d8=d9=0`. Its nonzero image line lies in `span(Z1,Z2,Z3)`. Such lines have dimension at most2, and the two-planes containing a fixed line have dimension4, giving an exceptional incidence image of dimension at most6. Rank zero is impossible under the normalization. Thus generic endpoint coverage omits no full-dimensional locus.

The open parent image is open because the pivot remains invertible near a given Y and its positive coefficient solution persists. Generic Y in this open image has exactly two endpoints, one in a positive wall and one in a negative wall according to the globally fixed orientation signs. At a selected open wall, transversality gives a nearby coefficient vector on the same fiber with every coordinate positive. Thus all selected open wall images actually lie in the open parent image, not merely its closure.

## 6. Exact disjointness and closed coverage

Source-cell injectivity and invariance of domain make each selected open tile image open in `Gr(2,6)`. If two same-side images intersected, their intersection would be a nonempty open set. It would contain a point outside the dimension-at-most7 exceptional locus, contradicting uniqueness of the oriented interval endpoint. Hence disjointness is exact, not merely almost everywhere.

Each tile is the closure of its open image. This uses the compactness of the source-cell closure and continuity of the amplituhedron map on the nonnegative Grassmannian. Each selected open facet image lies in the parent image, so each closed tile lies in its closure. Conversely generic endpoint coverage is dense in the open parent image, and each side's finite union of closed tiles contains that dense subset. Each side therefore contains the entire closure of the parent image. The two closed unions are equal, including all lower strata.

## Remaining gates

The local all-Z relation passes the definition, arbitrary-source identification, non-BCFW regression, source incidence, exact geometric additivity, and endpoint/multiplicity gates at its stated finite scope. The independent exact sign check passes the finite-computation gate. General classification, generation/connectivity, global50-tile embedding and novelty remain unproved and outside this verdict.
