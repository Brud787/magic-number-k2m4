# Run 5: Baues, regularity, and the exact scope of connectivity

Audit date: 2026-09-06. The relation spaces in this document use constant coefficients, all positive Z, and equality of indicators modulo sets of dimension less than eight, as in the [Run 4 theorem](../run4/LOCAL_PARENT_THEOREM.md).

## 1. What the published amplituhedron conjectures actually say

**SOURCE-VERIFIED.** Galashin–Lam Definition 7.1 defines a subdivision of a source parent g by cells f≤g in source Bruhat order, requiring full-dimensional images, compatible interiors, and dense coverage. An `(n,k,m)` subdivision is the same labeled collection for every positive Z. Theorem 7.2 transports these subdivisions under affine-permutation inversion, exchanging k and ell=n−k−m. [Primary PDF, Section 7](https://www.math.ucla.edu/~galashin/papers/duality.pdf).

In Section 13.4, a nearly admissible parent has source dimension km+1, full image dimension for every positive Z, and every source facet of the relevant dimension has algebraic degree one or collapsed degree infinity. Conjecture 13.10 proposes two equal-size boundary triangulations, exhaustive among triangulations at every fixed positive Z. Conjecture 13.11 separately proposes connectivity of complete triangulations by the resulting flips. Example 13.12 explains why the degree-two four-mass facet is a genuine excluded case. Problems 13.13 and 13.14 ask for the Baues sphere and regular-subdivision structure.

**Scope distinction.** The preserved rank-two local theorem proves uniform relation-kernel classification on each parent's admissible facet set. Its five ten-wall cases do not establish the stronger fixed-Z uniqueness quantifier at every external matrix. Even complete agreement with the local conjecture would leave connectivity to prove.

Let U_n be the all-Z tile index set and L_n the span of the certified parent relation vectors. The desired linear bridge is

\[
\mathbf1_{\mathcal T}-\mathbf1_{\mathcal T'}\in L_n
\quad\text{for every pair of complete all-Z tilings.}
\]

Flip connectivity is sufficient: sum the signed flip vectors along a path. It is stronger than this linear inclusion, which allows combinations that never define legal intermediate tilings. Neither assertion follows merely from local balancedness.

## 2. A proved special case: n=7 by parity and cyclic polytopes

**PROVED, derived from published theorems; no novelty claim.** Every two all-Z positroid tilings of A_(7,2,4) are joined by all-Z flips supported on nine-dimensional source parents. Their difference is consequently an integral sum of balanced parent relations.

Proof. Here ell=1. Galashin–Lam Theorems 3.5 and 7.2 give a bijection between all-Z rank-two tilings and the rank-one triangulations of the seven-vertex cyclic four-polytope, preserving parent subdivisions under inversion. Triangulations and bistellar moves of an alternating oriented-matroid realization depend only on that oriented matroid; all positive rank-one external data have this alternating oriented matroid. Thus these collections and moves have the required uniform-Z meaning. Rambau's cyclic-polytope connectivity theorem joins any two of them by bistellar flips. The applicable realization convention is stated explicitly in Rambau–Santos, pp. 1–2. [Rambau's paper](https://doi.org/10.1112/S0025579300012055), [Rambau–Santos author PDF](https://personales.unican.es/santosf/Articulos/Old/bauescyclicI.pdf).

Each flip is supported on a six-vertex circuit. In affine four-space its unique circuit coefficients alternate in sign, giving three positive and three negative coefficients. The two simplex triangulations therefore have three pieces each. The associated rank-one source parent has dimension five and affine inversion number one. Inversion preserves that number, so its rank-two parent has dimension 2(7−2)−1=9. Parity transports the two three-piece subdivisions and the legal replacement in the complete tiling. Telescoping along the path proves the stated integral-generation conclusion. This proves a theorem about complete-tiling differences, not the stronger assertion that every arbitrary indicator relation is generated this way.

The n=6 case is trivial because the map is an isomorphism. For n≥8, parity gives ell≥2, so this argument no longer reduces the problem to cyclic polytopes. The n=7 finite classification developed elsewhere in Run 5 is independent evidence, not required for this source-derived argument.

## 3. Why a common-refinement argument does not supply the bridge

**PROVED elementary obstruction.** A tiling is minimal under the source-Bruhat refinement convention. Indeed, an eight-dimensional admissible source cell has no proper source-boundary cell of dimension eight, and an image cannot have dimension greater than its source. Therefore a full-dimensional subdivision by source cells below that tile consists only of that tile itself. Two distinct tilings cannot have a common refinement in this particular poset.

This does not prevent common refinements in a larger geometric category. Finite Boolean combinations of the semialgebraic tile regions give a common semialgebraic partition of two tilings. Its atoms need not be positroid images, and no unit weight or permitted source-parent move has been proved for them. Even for a convex quadrilateral, two triangulations using opposite diagonals require their crossing as a new vertex in a common simplicial refinement. Refinement by the original-vertex simplices is unavailable.

The top-cell image gives a trivial common coarsening. Passing through it in a refinement poset says nothing about expressing the passage as admissible elementary flips. Also, the source positroid stratification being a common refinement of cyclic Schubert stratifications is a different statement about a different space.

## 4. Regular secondary objects and Baues topology

**SOURCE-VERIFIED.** The secondary polytope describes regular triangulations and regular subdivisions of a point configuration. Connectivity of its edge graph gives connectivity inside that regular family. Nonregular cyclic-polytope triangulations exist, already for C(9,4); oriented-matroid lifting subdivisions are a broader class than geometric regular subdivisions. Rambau–Santos Theorem 1.3 places every cyclic triangulation in the former class, not the latter. [Primary PDF, pp. 1–3](https://personales.unican.es/santosf/Articulos/Old/bauescyclicI.pdf).

Mohammadi–Monin–Parisi Section 5 addresses amplituhedra conjugate to polytopes. Its secondary fan and regular dissections are conditional on the stated positivity and combinatorial-independence assumptions. In rank two with m=4 this parameter case is n=7. It is not a theorem producing a secondary polytope whose vertices are every tiling for all n. [Primary PDF, Theorem 5.7, Proposition 5.9, Theorem 5.11 and Remark 5.6](https://arxiv.org/pdf/2010.07254).

**SOURCE-VERIFIED.** Postnikov Section 8.2 explicitly separates generalized Baues topology from flip connectivity: neither implies the other in general. The flip graph uses the minimal subdivisions and the subdivisions immediately covering them, not arbitrary paths in the order complex. Its coherent part is controlled by the fiber polytope. [Primary PDF, p. 16](https://arxiv.org/pdf/1806.05307).

Consequently even a proved sphere theorem for the amplituhedron Baues poset would still need a theorem reducing paths to the relevant rank-zero/rank-one galleries and identifying those galleries with admissible parent replacements. A claimed edge of a “secondary amplituhedron” needs a defined object, a proof that all intended tilings are vertices, and a proof of its edge interpretation. No such general theorem was supplied by this audit.

The precise remaining rank-two target is the linear inclusion in Section 1, or the stronger flip connectivity statement. The local theorem has made the coefficient-sum question automatic **after** that bridge; it has not built the bridge.
