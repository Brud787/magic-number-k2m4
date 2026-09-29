# Independent review of the all-n normalization argument

**PROVED / REVIEWED: PASS.** This review checks the structural inference in [GLOBAL_GENERATION](GLOBAL_GENERATION.md) separately from this agent's production of the finite normalized matrices. The geometric amalgamation and simplicial proofs were read in full. The finite35/5 certificates also have the separate literal-basis implementation in the independent normalized audit, so the global argument does not rely solely on its producer reviewing its own matrix.

## Checked dependencies

The face map on K uses an arbitrary positive downstairs matrix and an explicit positive degeneration upstairs. The compactness argument accounts for the unique rank-loss source point and its dimension-four target locus. The regular surviving branch gives strict membership on a common neighborhood; the limsup argument gives strict nonmembership there. This correctly handles exceptional sets depending on the degeneration parameter: a nonzero constant on an open neighborhood cannot be an almost-everywhere-zero upstream relation. The argument applies to all admissible labels, including spurions, and retains multiplicities before deducing their absence for complete tilings.

Preservation of L follows from exact parent-image incidence and the complete local-parent theorem. It never assumes K=L. Zero insertion preserves both relation spaces. The signed wrap face and all face/degeneracy identities are compatible with the dimension cutoff and the persistent class-complement obstruction. A discarded four-mass intermediate cannot arise from an admissible source under a dimension-preserving face. The lower cutoff Vn=0 for n≤5 is consistent with the simplicial identities; every face from the sole n6 cell loses source dimension.

## Normalization and the degree shift

The object in simplicial degree p is V_(p+1), so in label number n the degeneracies into that degree insert loops at positions2,…,n. Label1 is deliberately not among those insertion positions. Conversely, any admissible label having a loop at one of those positions is a zero insertion of an admissible smaller label, using the complete core classification/positive-extension equivalence. Thus Eq3 identifies the actual degeneracy quotient, not a chosen approximation.

The normalized quotient is the complement of the degeneracy subspace, and normalization is exact by [Stacks Lemmas14.23.6 and14.23.8](https://stacks.math.columbia.edu/tag/0194). Its faithfulness is [Stacks Lemma14.24.1](https://stacks.math.columbia.edu/tag/019D). These primary references were checked directly. In particular, this use requires vanishing of every normalized group, not merely vanishing of its homology.

The rows surviving the coordinate projection are exhaustive: a parent having a loop at any position2,…,n has that loop in every source facet, so its entire row vanishes in the projection. The only remaining parents are loopless or have sole loop1, exactly the records generated from the complete Run4 prototypes. The finite data give NQ_(n−1)=0 at n10,11. The support bound q≤10 leaves no normalized columns at n≥12. Therefore NQ_p=0 for every p≥9.

## The kernel inference

K9=L9 is a preserved theorem. Smaller H_r=K_r/L_r vanish either by their preserved certificates or by zero insertion to n9 followed by the face left inverses, which preserve L. Thus H_(p+1)=0 for p≤8.

Because L⊆K⊆V and all three are simplicial, H is a simplicial subobject of Q. Exact normalization gives NH↪NQ. For p≤8 its source group vanishes; for p≥9 its target group vanishes. Hence every group of NH is zero. Faithfulness, or the standard decomposition by degeneracies, forces H=0. This proves K_n=L_n for every n≥6. There is no unproved tiling connectivity or extension premise in this implication.

## Numerical formulas and scope

There are binomial(n−1,p) increasing surjections [n−1] onto[p]. With normalized dimensions1,9,19,12 in degrees5,6,7,8, respectively, this gives

\[
\dim Q_n=\binom{n-1}5+9\binom{n-1}6+19\binom{n-1}7+12\binom{n-1}8.
\]

At n10 this is1674; the complete tile universe has3815 columns, so rank L10=2141. This is a structural consequence, not a full n10 matrix computation. The earlier proposed1675 remains explicitly recorded as failed.

For complete all-Z tilings their differences lie in K=L. Every local generator has zero coefficient sum, so comparison with the standard BCFW count gives

\[
|\mathcal T|=\frac{(n-3)(n-4)^2(n-5)}{12}
=\frac1{n-3}\binom{n-3}2\binom{n-3}3.
\]

The values1,6,20,50 at n6,…,9 and the displayed algebra agree. The proof gives D_n⊆L_n for all n. It does not prove L_n⊆D_n for all n, flip connectivity, every-fixed-Z kernel equality, or the arbitrary-k m4 conjecture. No novelty assertion follows from this review.
