# Review of membership cores, the spurion inverse, and complete n9 memberships

**PROVED review verdict: PASS at the stated scope.** The [spurion inverse](SPURION_INVERSION.md) gives a complete open inverse for the already certified all-Z (3,3,3) tile. Its strict branch certifies either open membership or nonmembership in the closed image on an ambient open neighborhood. The review found no missing positive gauge or closure branch. All-Z admissibility remains an independently source-verified input; it is not deduced from generic complex degree or sampled differential rank.

## 1. Source chart and rank

Three distinct cyclic source directions have a unique projective normalization to horizontal, diagonal and vertical, up to a common nonzero scalar. Nonnegative ordered minors permit all nine coefficients to be chosen positive. The remaining scalar is the entire gauge stabilizer, so distinct projective coefficient vectors are distinct source points.

The quotient equations M_Y x=0 are equivalent to containment of both source-image rows in Y. For a positive source point, rank preservation of the amplituhedron map makes this containment equality. If a positive fiber had a kernel of dimension at least two, a sufficiently small perturbation of its positive vector in an independent kernel direction would remain positive and yield distinct source points with the same image. The independently published all-Z injectivity therefore forces rank M_Y=8 at every open image point. This argument is global within the complete positive chart and does not infer injectivity from a rank computation.

## 2. Hostile closure audit

Within-class zero minors persist on closure, so original parallel classes can lose columns or merge but cannot split. If all three directions remain distinct, the nonnegative three-direction chart covers the point. If only two directions remain, at least one surviving direction is supported in a single original class, whether the third original class has disappeared or two original directions have merged. Rank two excludes a one-direction source. Thus every closed point outside the weak chart has image meeting the external span of an original block.

The three rank-five gates therefore eliminate all missing source gauges for (3,3,3). The four-chart description in §4 is exhaustive: the weak chart and the three cyclic two-direction mergers cover all rank-two possibilities, including entire-block deletions and their lower strata. The sign in the cyclic A/D merger is necessary and correct: with columns (a,0),(0,b),(-d,0), both A–B and B–D ordered minors are positive. Each displayed weak chart has only allowed source bases and hence lies in the positroid closure.

At rank eight and with nine nonzero kernel entries, a mixed-sign kernel admits no nonnegative coefficient representative. Under the block gates there is no remaining closed-source branch. A same-sign kernel gives the positive source inverse. Nonzero pivots, block-rank minors and coefficient signs persist on an ambient target neighborhood. The implementation returns undecided on exceptional cases instead of silently treating them as closed nonmembership.

The claimed redundancy of the block gates is also valid: a vector in Y intersected with one external block span would produce a nonzero kernel vector supported on that block. It cannot be proportional to a kernel vector having all nine coordinates nonzero.

## 3. Exact independent audit of the full n9 matrix

**COMPUTATIONALLY-VERIFIED.** The [independent implementation](../../src/magic_number/run6_indicators_independent.py), exercised through its command-line entry point, verified all472 target rows and all942 tile columns in [the n9 witness artifact](../../results/run6/indicator_kernel_n9.json). The [audit record](../../results/run6/indicator_membership_independent.json) saves a hash of all geometric input fields. The checked counts are:

| Check | Exact count |
|---|---:|
| Membership decisions |444,624|
| Complement-five mixed-sign exclusions |360,154|
| Complement-five full ambient inverses |83,054|
| Spurion ambient kernel inversions |1,416|
| Independently nonzero four-label twistors |59,472|

The implementation does not import either the producer membership routines or the spurion quotient inverse. It reconstructs source bases from bounded affine permutations. For complement-five cells it uses a full six-dimensional external frame, reconstructs the ambient source, verifies the row-space equation, and tests every ordered source two-minor. This differs from the producer's five-row hyperplane coefficients and five scalar inequalities. For every spurion decision it solves twelve ambient equations in nine source coefficients and four unknown target row-change coefficients. The resulting12×13 kernel is one-dimensional; the first nine coordinates are nonzero, all three block-rank gates hold, and their normalized values agree with the producer certificate.

Every chosen target is itself checked to be the image of its recorded nonnegative source with the stated affine label. All126 four-label twistors are recomputed independently at each of the472 targets. Consequently the generic closed-membership theorem for the complement-five cells and the strict spurion theorem above apply simultaneously to every column of each row. The finite row is constant on a nonempty ambient open neighborhood, as required to test relations modulo sets of dimension at most seven.

The complete run passed in82.625 seconds. The accompanying [test](../../tests/test_run6_indicators_independent.py) runs the same full independent audit; it does not replace recomputation by accepting the saved success flag.

## 4. Membership-core completeness review

**PROVED, independently reviewed by the root agent: PASS.** The [core classification](MEMBERSHIP_CORES.md) exhausts all eight-dimensional rank-two positroid cells, for every n. The source dimension equation q+s=12 leaves only support sizes6,...,10. The maximum-class alternatives isolate exactly the complement-five cells, the (3,3,3) spurion and the excluded four-mass type, besides cells whose images lie in a Schubert incidence locus of dimension at most seven. The latter cannot be injective by invariance of domain. The four-mass exclusion uses an actual positive two-preimage certificate and positive row extension, not complex degree alone.

The complement-five proof recovers Y intersected with the external five-space, fixes the positive first-row coefficients, and then inverts six compressed external rows. Positivity of their determinant is an expansion into increasing maximal external minors with positive coefficients. Aligning any second candidate preimage by the residual positive row gauge proves global uniqueness. The proof includes the q10 two-class core. Generic closed membership explicitly excludes vanished columns, vanished distinguished class and direction mergers by nonzero four-twistors before applying the weak chart.

The independent finite checks reconstruct all221 loopless source labels through affine permutations and bases, while a separate positive-composition count checks the labeled multiplicities. Exactly86 loopless cells in eleven dihedral types are admissible. Exact support transport gives942 distinct n9 labels,939 complement-five and three spurions. The universe count is a count of potential tile generators, not a tiling count. The prior-art audit explicitly records the older rational-invariant core lists; the classification is not presented as a novelty claim.

This document's author produced the membership-core proof and enumeration; the root agent supplied its independent mathematical review. The full ambient membership arithmetic and the spurion closure review above are independent of their respective producing agents.

## 5. Limits of this review

This audit certifies the full geometric membership matrix and the closure hypotheses needed for the finite rank argument, with source completeness established by the separately reviewed core proof. Exact matrix ranks and the local image relations require their separate certificates. Together those ingredients can prove a finite n9 theorem; this audit alone does not establish all-n generation, arbitrary flip connectivity, a universal canonical-form identity, or the infinite-family Magic Number conjecture.
