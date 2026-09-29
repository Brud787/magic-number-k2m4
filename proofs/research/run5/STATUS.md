# Run 5 bounded checkpoint — 2026-09-06

**SUCCESS A: complete finite tiling-generation analysis at n=7 and n=8.**
The all-n k=2,m=4 generation problem and Magic Number theorem remain
unproved. This checkpoint stops before a long all-n search.

The Run4 all-parent theorem is an input, not a result re-established here.
Earlier fixtures, failed claims, source discrepancies, and fixed-Z versus
all-Z qualifications remain preserved. Definitions of V_n, L_n, D_n and
the full indicator kernel K_n are in [GENERATION](GENERATION.md).

| Tag | Result | Scope / proof |
|---|---|---|
| PROVED | D7=L7, with dimension 6. Exactly seven complete all-Z tilings exist, each with six tiles; the actual parent-flip graph is C7. | [N7_PROOF](N7_PROOF.md). Complete 21-label universe, exact exclusion at fixed data, all-Z existence by BCFW/parity. A known cyclic-polytope sector, with no novelty claim. |
| PROVED | K8=L8 and D8=L8, with dimension 73. Every complete all-Z n8 tiling has twenty tiles. | [Indicator theorem](N8_INDICATOR_THEOREM.md), [genuine tiling span](N8_FLIP_SPAN.md), [independent audit](INDICATOR_INDEPENDENT_REVIEW.md). Includes the entire 176-label all-Z tile universe. |
| PROVED | All complete all-Z n8 tilings are exactly the binary solutions A chi=1 for the saved 103×176 integer matrix. | The kernel theorem proves sufficiency, including open disjointness and closed coverage. [Finite cases](FINITE_CASES.md). The binary solutions have not been exhaustively enumerated. |
| PROVED | An explicit signed rational functional on the finite tile-indicator space has weight one on every n8 tile and total weight twenty. | [Exact weights](../../results/run5/unit_functional_n8.json). Evaluations mean constant values on certified open neighborhoods; this is neither a positive volume nor an all-n construction. |
| COMPUTATIONALLY-VERIFIED | Full local matrices have 7 rows/rank 6 at n7 and 96 rows/rank 73 at n8. Quotient dimensions are 15 and 103. | [Exact ranks](../../results/run5/generation_ranks.json), [LOCAL_SPAN](LOCAL_SPAN.md). The old restricted seven-support failure is not overwritten. |
| COMPUTATIONALLY-VERIFIED | All 18,128 n8 membership decisions and 7,210 nonzero twistor checks have an independent exact implementation; a maximal indicator minor has determinant 2. | [Independent audit](INDICATOR_INDEPENDENT_REVIEW.md). Strict nonmembership excludes every closed-source branch, and each entire indicator row persists on an open set. |
| COMPUTATIONALLY-VERIFIED | Seventy-four genuine all-Z n8 tilings give 73 independent differences; 152 certified replacements in a retained 153-node tree prove their validity. | [Flip certificate](../../results/run5/tiling_span_witness_n8.json). Discovery stopped at the target rank after 2,440 states; this is not complete tiling enumeration. |
| FAILED | Ordinary source boundaries after discarding inadmissible eight-cells give the desired image chain complex. | Every one of the 96 next-boundary products is nonzero modulo two. [CHAIN_COMPLEX](CHAIN_COMPLEX.md). Changing orientation signs cannot repair this. |
| FAILED | Killing all lower cells below nonadmissible eight-cells repairs the generation proof. | This quotient leaves individual nonempty tiles as cycles. Their augmentation is one and their geometric indicator is nonzero. Its mod-two middle homology has dimension 15; no rational homology rank is inferred. |
| FAILED | Distinct tilings have a common refinement within the source-Bruhat positroid subdivision poset. | Tilings are minimal for that refinement order; arbitrary semialgebraic intersections have a different class of pieces. [BAUES](BAUES.md). |
| SOURCE-VERIFIED | General generation/connectivity is not supplied by the screened Baues, secondary-fan, or source-CW theorems. The counts 176 and 74/73 have prior BCFW/formula antecedents. | [Targeted literature delta](LITERATURE_DELTA.md), cutoff September 6, 2026. No claim of novelty from negative searching. |
| CONJECTURAL | D_n⊆L_n for all n≥9, or a direct equal-cardinality invariant for all n. | No induction or global relation-presentation theorem has been established. Local support at most eleven does not bound support of global tiling differences. |
| CONJECTURAL | Every n8 tiling belongs to the explored flip component. | Linear generation is proved; connectivity of the entire graph is not. The total number of n8 tilings is uncomputed. |

## Why the finite certificate is a proof

**PROVED.** Every all-Z indicator relation annihilates the 103 certified
open indicator rows at one positive Z0. Their exact rank is 103, while
the already-proved all-Z local span has dimension 73. Thus

\[
 L_8\subseteq K_{\mathrm{all},8}\subseteq K_{Z_0,8}
 \subseteq\ker A=L_8.
\]

The complete inverse and open-neighborhood proofs justify the necessary
constraints. Matching dimensions then prove completeness of the kernel;
there is no extrapolation from favorable numerical samples. A separate
genuine-flip certificate supplies L8⊆D8, hence equality. The fixed-Z
kernel conclusion is asserted at the displayed Z0, not at every Z.

## Counterexample search and next decision

**PROVED.** No complete-tiling difference outside L_n, and no unequal
tiling count, exists for n=7 or n=8 under the stated all-Z conventions.
The source quotient's unit cycles are actual counterexamples to that
chain model, not indicator relations or Magic Number counterexamples.
[COUNTEREXAMPLE_SEARCH](COUNTEREXAMPLE_SEARCH.md) keeps those outcomes
separate. No n≥9 global difference was certified or excluded in this pass.

**CONJECTURAL, ranked architectures with explicit kill-tests.**
First, extend the exact indicator-kernel presentation with a controlled
deletion argument; second, seek a uniform unit functional without full
generation; third, construct a corrected relative pushforward complex
retaining real branches. [GENERATION](GENERATION.md) states the precise
missing statements and kill-tests. The n9 spurion source is already
outside the complement-five inverse used here. This is a concrete first
obstruction to extending the successful n8 method.

**COMPUTATIONALLY-VERIFIED.** The baseline passed all 142 tests in 24.76
seconds before modifications. Final tests and the preservation audit
are recorded in [validation.json](../../results/run5/validation.json).
The [review](REVIEW.md) lists dependencies and hostile gates.
