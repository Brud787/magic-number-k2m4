# Independent audit of the all-n generation argument

**PROVED review verdict: PASS, with the indexing clarification below.** The all-n argument in [GLOBAL_GENERATION](GLOBAL_GENERATION.md) follows from the independently reviewed geometric amalgamation theorem, the signed simplicial identities, the complete membership-core theorem, the preserved n9 indicator-kernel theorem, and the exact normalized zero certificates. No substantive mathematical gap was found in those new implications. This verdict concerns constant-coefficient **all-Z** indicator relations and all-Z tilings. It does not establish every fixed-Z kernel, flip connectivity, or L_n=D_n for arbitrary n.

The distinction between label number n and simplicial degree p=n−1 is essential. The root agent was asked to state the last step as K_r/L_r=0 for label counts r≤9, equivalently H_p=0 for simplicial degrees p≤8. The phrase H_(p+1)=0 in that step would mix the two conventions. This is a notation correction to the draft, not an additional hypothesis.

## 1. Independent geometric review

The review read all eight sections of [AMALGAMATION_PROOF](AMALGAMATION_PROOF.md). The following are the decisive checks.

**Entire source image and inverse.** Adjacent column addition has nonnegative ordered minors equal to sums of original minors. The output cell is determined by the whole source zero pattern. The source classification distinguishes loops, same-class pairs, two surviving class directions, and disappearing singleton classes. In the dimension-preserving nonloop case, both old class directions survive, and decomposing the new column in those two directions is a unique rational inverse. The signed cyclic convention correctly handles an early raw column representing the opposite ray of a wrapping class. The dimension-drop cases are onto their indicated lower-dimensional cells; they are not treated as eight-dimensional inverses.

**Rank loss and all boundary escape rates.** Rank loss on the full nonnegative source can occur only at the coordinate two-plane supported on the merged pair. Vanishing of the output minors forces their nonnegative summands to vanish separately; any surviving outside column would then force all columns parallel, contradicting rank two. Continuous source frames near that coordinate plane show that every limiting target contains the duplicated external row. The exceptional target locus has dimension four. This reasoning permits arbitrary relative rates of the source boundary limit and external degeneration, so it rules out the possible unexamined blow-up branch.

**Discarded outputs.** A dimension-preserving nonloop amalgamation creates a singleton. It cannot produce the noncollapsed four-mass type. A loop operation preserves the original admissible core. The remaining eight-dimensional excluded outputs are therefore collapsed by the class-complement obstruction. All lower-dimensional output sources are also discarded by their dimension bound. Their closed target images have dimension at most seven. The author explicitly added the lower-dimensional outputs to the exceptional-set description following this review's clarity request.

**Generic indicator convergence is strict on neighborhoods.** For each arbitrary positive downstairs W, the supplied alternating external-row perturbation is positive for every sufficiently small positive parameter. Compactness excludes closed upstairs membership uniformly near a point outside the closed limiting image and the rank-loss locus. At a regular point of a surviving output tile, the rational source isomorphism and a parameter-dependent inverse function theorem give uniform open membership near that point. Critical and source-boundary images are semialgebraic of dimension at most seven. A finite common exceptional set and finite neighborhood intersections suffice for all source labels at a fixed n.

**All-Z relation descent.** A fixed target point need not avoid the upstairs exceptional sets for every perturbation parameter. The proof correctly uses a whole open neighborhood with an eventual constant indicator vector. A nonzero value of a relation there would contradict its vanishing modulo dimension at most seven at each positive parameter. This proves d_i K_n⊆K_(n−1) for every arbitrary downstairs W, with no unproved interchange of pointwise exceptional sets and limits.

**Local relation descent is not circular.** If a parent output has dimension nine, every surviving output facet is a genuine codimension-one positroid facet of that parent, and its image row is in the already classified one-parent indicator kernel. If the parent output has dimension eight, every surviving output facet label must coincide with that parent label; the resulting scalar relation on one nonempty open tile is zero. Smaller output parents contribute zero. Thus d_i L_n⊆L_(n−1) uses the preserved local theorem and the new K descent, never the global equality K=L being proved.

**Tiling multiplicities.** The degeneration first retains all nonnegative integer multiplicities. The downstream generic amplitude identity forces each multiplicity at most one and excludes overlapping open tiles. Compact closed images and density of the generic set then recover the full closed cover. No multiplicity-one assumption was smuggled into the limit argument. This tiling descent is sound, although the global generation proof needs only the relation descent.

## 2. Independent simplicial and truncation review

All four sections of [SIMPLICIAL_AMALGAMATION](SIMPLICIAL_AMALGAMATION.md) were checked. The last face must be (c_1−c_n,c_2,...,c_(n−1)). With this sign, the two endpoint face-face identities reduce to associativity and x−y−z=x−(y+z); the mixed identities remove an inserted zero or commute its position past the wrap. Degeneracies insert zeros after existing labels. These are genuine simplicial identities in degree n−1. As an additional exact regression, the symbolic column implementation checked all identities for lengths2 through14. The proof, rather than that finite check, establishes all lengths. A raw face from degree zero to degree minus one is unnecessary, and the draft was clarified accordingly.

Truncating a source image to zero requires a separate proof. Rank loss cannot be repaired by further column combinations. Source dimension cannot increase under a later source map or zero insertion. A discarded eight-dimensional intermediate is collapsed, and its distinguished class with at most four outside nonloops survives every dimension-preserving face: outside count either remains the same or decreases. A face that removes its last possible direction lowers dimension. Therefore a discarded intermediate cannot later become an admissible eight-cell. This proves that truncation preserves the raw identities; it does not merely compare final dimensions.

Zero insertion preserves K by the exact image identity using the positive external row submatrix, and preserves L by transported parent relations. Along with the independently checked face descent, K and L are simplicial subspaces of V and H=K/L is a simplicial subobject of Q=V/L.

## 3. Independent critical finite certificate

**COMPUTATIONALLY-VERIFIED.** The [independent verifier](../../src/magic_number/run7_normalized_independent.py) does not call the producer's normalization or transport routines. It reconstructs all surviving generators from the complete loopless membership cores, computes affine basis sets independently, and substitutes label maps directly into literal Run4 basis sets. Every retained projected row has an explicit parent and geometric prototype origin.

| Source label count | Complete surviving columns | Certified projected rows | Literal transports checked | Independent Fraction determinant |
|---:|---:|---:|---:|---:|
|10|35|141|188|−1|
|11|5|46|52|+1|

The selected35×35 and5×5 minors therefore eliminate every column in those normalized quotients. Column completeness includes tiles whose only loop is at label1, as well as loopless tiles; it does not discard every loop-containing tile. The [audit record](../../results/run7/normalized_independent_review.json) preserves the results. Its independent test passed in0.36 seconds. No full n10 matrix or new numerical target sampling was used.

For these two zero conclusions a certified subset of relations with full column rank would suffice; the verifier actually checks every saved projected row. The lower normalized dimensions1,9,19,12 used in the Hilbert formula come from the separate complete finite rank certificate and its local-matrix review. They are not needed to establish high-degree vanishing once the two full-rank minors and support cutoff are known.

## 4. The homological implication and its exact scope

The required standard facts are that normalization is the quotient by degeneracies up to canonical splitting, is exact, and detects the zero simplicial object. These are supplied respectively by [Stacks Lemma14.23.6](https://stacks.math.columbia.edu/tag/019A), [Lemma14.23.8](https://stacks.math.columbia.edu/tag/019B), and [the Dold–Kan theorem and faithfulness lemma](https://stacks.math.columbia.edu/tag/019D). They apply to real vector spaces. No claim about cellular homology of the amplituhedron is required.

For source n, the degenerate generator span is exactly the span of tiles with a loop at some position2,...,n. Quotienting Q_n by it is V_n modulo that generator span and L_n. The finite projections compute precisely this quotient. A tile has at most ten nonloop labels, so at n≥12 it necessarily has a loop at some position at least2. Thus no normalized generator survives there. Together with the two independently verified zero matrices, N(Q)_p=0 for every simplicial degree p≥9.

The preserved theorem K_9=L_9 gives the same equality at each smaller label count by zero insertion followed by face left inverses; those faces preserve L by the independent geometric theorem above. Consequently H_p=0 for p≤8. Exactness of normalization gives N(H)↪N(Q). In degrees at most8 the source is already zero; in degrees at least9 the target is zero. Hence N(H)=0, and faithfulness gives H=0 in every degree. This proves K_n=L_n for every n≥6.

This is a finite reduction through a proved simplicial structure, not rank extrapolation. It needs no uncomputed normalized boundary map and no n10 membership matrix. The earlier predicted extra normalized n10 dimension is explicitly false, so its removal is a verified change rather than a fitted continuation.

Finally, complete all-Z tiling differences belong to K_n=L_n. The coefficient-sum functional annihilates every primitive Run4 generator, with its geometric signs and real coefficients. Comparing any such tiling to a certified standard BCFW tiling therefore gives

\[
|\mathcal T|=\frac{(n-3)(n-4)^2(n-5)}{12}.
\]

The conclusion is the infinite rank-two m=4 family. It does not prove m=4 at other k, fixed-Z-only tiling cardinality, or connectivity of tilings under local moves. The count follows from the proved all-Z family kernel; a constant unit functional on every arbitrary fixed-Z indicator space is not asserted. No priority or novelty claim is inferred from a negative literature search.

## 5. Review independence and retained premises

This reviewer independently checked the new amalgamation and simplicial proofs written by the geometric agent and the global deduction written by the root agent. The reviewer also produced the independent35/5 finite verification and, in Run6, independently checked all444,624 n9 membership decisions including the three spurion columns. The membership-core proof was produced by this reviewer and independently reviewed by the root agent, as recorded in Run6. The Run4 geometric local theorem and the source-verified BCFW/spurion inputs remain explicit premises with their preserved earlier audits. This review does not replace those premises with an appeal to the new global conclusion.
