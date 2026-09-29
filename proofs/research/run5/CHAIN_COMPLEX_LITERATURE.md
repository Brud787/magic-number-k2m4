# Run 5: source chains, signed degrees, and indicator generation

Audit date: 2026-09-06. This document distinguishes valid source topology from the additional comparison theorem needed for the amplituhedron. The elementary arguments below are supplied explicitly; they are not attributed to a source as an unstated global generation theorem.

## 1. A source differential is available

**SOURCE-VERIFIED.** Galashin–Karp–Lam prove that the nonnegative Grassmannian is a regular CW complex in its positroid decomposition; each positroid closure is a closed ball. Consequently its oriented cellular chains have incidence numbers ±1 on codimension-one source facets and satisfy d²=0. Olson's Section 4.2 gives the related Grassmannian-chart orientation calculation and its signed boundary rule, with cancellation around rank-two intervals. [Regularity theorem, Theorem 1.1 and Corollary 1.2](https://www.math.ucla.edu/~galashin/papers/boundary.pdf), [Olson, formulas (4.5)–(4.6)](https://arxiv.org/pdf/1411.6363).

These results concern X=Gr≥0(2,n). They do not say that all projected positroid images form a regular CW complex, nor that the amplituhedron map is cellular for the naive family of those images. Identifying source chart orientations does not identify unoriented tile indicators.

**SOURCE-VERIFIED prior art.** Arkani-Hamed and collaborators already organize Yangian-invariant identities by Grassmannian boundaries and one-dimensional residue theorems in Sections 11–12 of *Scattering Amplitudes and the Positive Grassmannian*. Their rank-two tables include finite source types and boundary generators. In particular, the (12)(34)(56)(7)(8) example retains a four-mass term interpreted through a sum over solutions, alongside eight rational contributions. This is direct precedent for the source-boundary route, with a different target from positive-region indicators. The source's general functional-generation assertion is not imported here as an indicator-generation theorem. [Primary PDF, Sections 11–12](https://arxiv.org/pdf/1212.5605).

## 2. The correct generic boundary identity uses real local degrees

**PROVED elementary degree lemma.** Fix a positive external matrix Z, choose an orientation of the real eight-manifold M=Gr(2,6), and orient each source cell. For an eight-dimensional source cell S define, at generic Y,

\[
d_{S,Z}(Y)=\sum_{x\in S:\ f_Z(x)=Y}\operatorname{sgn}\det D(f_Z|_S)_x.
\]

Take Y outside images of the source seven-skeleton and outside the critical values of all eight-dimensional source cells. This omits a semialgebraic subset of dimension at most seven. Full-dimensional maps then have finite regular fibers; collapsed maps contribute zero. For any nine-dimensional source cell P,

\[
\sum_{S\lessdot P}[P:S],d_{S,Z}(Y)=0. \tag{1}
\]

Proof. The source boundary of its closed ball is a topological S^8. Its map to M extends over the closed B^9, so the pushforward of its fundamental class is zero. Compute its degree at a regular Y away from the lower source-boundary strata by summing the local degrees on its open eight-dimensional facets, with their induced boundary orientations. This is precisely (1). The map f_Z is continuous on the entire nonnegative source closure, so the extension is legitimate. Semialgebraic critical-value dimension and compactness of the closure justify the generic finite sum.

For an injective tile map, invariance of domain gives an open image homeomorphic to its open source cell. The local orientation sign is constant, so d_(S,Z) is ± the tile indicator modulo lower-dimensional sets. Orienting that tile's source accordingly gives a positive indicator. For a noninjective cell, d_(S,Z) is a signed real-preimage function, not its image indicator and not its complex algebraic degree.

The [Run 3 four-mass certificate](../run3/MULTIPLICITY.md) exhibits open target neighborhoods with unsigned positive preimage counts 0, 1, and 2 at one positive rational Z. The corresponding signed counts in its displayed source/target chart orientations are 0, +1, and 0; the two sheets have opposite local Jacobian signs. Therefore replacing the four-mass contribution in (1) by a constant 2, by an unsigned image indicator, or by zero is not valid.

Even when every wall is injective, (1) alone does not imply that the sum of its wall coefficients vanishes. Projection of a triangle onto a line gives the identity of one long interval with two consecutive shorter intervals, all mapped with multiplicity one. The rank-two balancedness theorem supplies extra geometry that this general topological identity does not contain.

## 3. Relative chains can be valid without solving the image problem

**PROVED elementary subcomplex lemma.** Let A_coll be the union of all source cells S satisfying dim f_Z(S)≤7 for every positive Z. It is a CW subcomplex. If T is in the source closure of S, continuity gives f_Z(T) contained in closure(f_Z(S)); semialgebraic closure preserves dimension. Thus the condition is downward closed in source Bruhat order. The relative chain complex C_*(X,A_coll) is therefore valid and has d²=0.

The degree functions of Section 2 vanish on its eight-dimensional generators that are killed by this quotient. Thus, in degree eight, the signed-degree map descends through this relative quotient and kills the images of nine-dimensional boundaries. This is a statement about the full signed-degree target, which still includes noninjective facets.

One can also adjoin closures of every nonadmissible eight-dimensional cell to A_coll. That is again a legitimate subcomplex; its relative differential still squares to zero. **The obstruction is not automatically failure of d²=0.** The signed-degree map generally fails to descend through this larger quotient, because it kills a nonadmissible source generator whose signed degree function is nonzero. The one-positive-preimage four-mass example is an explicit witness.

In the opposite direction, retaining only admissible eight-cells and declaring their projected boundaries to be a differential needs an actual choice of lower-dimensional chain groups and a proof. The word “admissibility” does not by itself define a subcomplex or a cellular target structure.

## 4. A direct kill-test for projected source boundaries

**PROVED from the preserved hostile certificates.** Each hostile Run 4 parent has eight admissible source facets whose fixed-Z indicator functions are linearly independent. In a regular CW complex its source cellular boundary has incidence ±1 on every one of these facets. Deleting all collapsed and nonadmissible facets leaves a nonzero vector supported on those eight tiles. No choice of the remaining orientation signs can turn that vector into an indicator relation, because their entire relation space is zero. [Exact open-neighborhood certificates](../run4/COUNTEREXAMPLE_SEARCH.md), [complete local theorem](../run4/LOCAL_PARENT_THEOREM.md).

This refutes the proposed rule “project the source nine-boundary onto admissible tile generators and obtain an image relation.” It does not refute (1), which retains the required signed real-preimage functions of the nonadmissible facets. It also does not rule out larger combinations of source boundaries in which all unwanted contributions cancel before projection.

## 5. The exact missing chain comparison

Let C_8 be the full oriented source eight-chain space, and let Phi_Z send its generators to the signed-degree functions of Section 2, modulo functions supported in dimension below eight. Then Phi_Z d_9=0. Let V_adm be the coordinate span of all-Z admissible tiles, reoriented to give positive indicators. Let L_n be the span of the separately certified balanced parent relations.

A possible route would prove that every complete all-Z tiling difference lies in L_n by first lifting it to combinations of source boundaries and then eliminating nonadmissible contributions. The required comparison contains at least two separate assertions:

1. The relevant all-Z indicator kernel inside V_adm is generated by source boundaries in an explicitly chosen relative chain complex.
2. Its intersection with V_adm reduces to the already certified admissible parent relations, with the necessary uniform coefficients and orientations.

Neither assertion follows from source contractibility. For example, because X is a ball, the long exact sequence gives H_8(X,A_coll) isomorphic to reduced H_7(A_coll), which need not vanish without further information. A tiling difference can have zero image indicator without its source boundary vanishing. Killing the whole seven-skeleton makes every eight-chain a relative cycle, but does not make every such cycle a boundary. Exactness of a correctly defined source complex and faithfulness of an image-comparison map are different questions.

This is the appropriate interpretation of Run 5 finite boundary and indicator ranks: they can certify a particular comparison, find a counterexample, or isolate its dimension defect. They cannot promote source d²=0 into a global tiling-generation theorem by itself.

## 6. Forms and constructible pushforwards do not remove the hypotheses

**SOURCE-VERIFIED.** Euler-characteristic pushforward of constructible functions is additive and functorial, with finite-fiber values equal to unsigned point counts. It is different from signed degree. The source tile's open cell has compactly supported Euler characteristic one in dimension eight, but tile interfaces also contribute under decompositions; this does not define a universal unit-weight valuation modulo lower-dimensional sets. [Baryshnikov–Ghrist, Euler integration over definable functions](https://www2.math.upenn.edu/~ghrist/preprints/definable.pdf).

**SOURCE-VERIFIED.** Brown–Dupont constructs a canonical-form map on relative homology for genus-zero pairs. The 2026 positive-genus result of Koefler–Pavlov–Sinn prevents applying that hypothesis automatically to the ordinary ambient amplituhedron pair for general m=4, k≥3 and sufficiently large n. It leaves k=2 undecided and does not refute positive geometry in its original sense. [Brown–Dupont](https://arxiv.org/pdf/2501.03202), [Koefler–Pavlov–Sinn, Theorem 5.1](https://arxiv.org/pdf/2601.11142).

Residue identities, form identities, signed-degree identities, and indicator identities therefore require separate comparison maps. A source-chain or canonical-form proof remains plausible only after specifying and proving those maps on arbitrary tiles and on the hostile noninjective cells that arise in intermediate source boundaries.
