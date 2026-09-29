# Run 4 bounded checkpoint — 2026-09-06

**PROVED / SUCCESS D.** The local k=2,m=4 parent relation problem is
complete at the stated all-Z scope. For every n and every nine-dimensional
rank-two positroid parent P, every constant-coefficient all-Z indicator
relation on P's admissible codimension-one source facets has coefficient
sum zero. Its complete relation space is either zero or one balanced
3↔3/5↔5 span. See the [precise theorem and proof](LOCAL_PARENT_THEOREM.md)
and [independent scope audit](FINAL_SCOPE_REVIEW.md).

This is the local parent theorem, not Magic Number. No relation-generation
or complete-tiling enumeration was launched. The run stops after the
independent hostile audit.

| Status | Result | Evidence / qualification |
|---|---|---|
| COMPUTATIONALLY-VERIFIED | Untouched baseline: 100 tests passed in 20.51 seconds. | [Baseline](../../results/run4/baseline.json); 149 old files hashed before changes. |
| PROVED / COMPUTATIONALLY-VERIFIED | All 29 loopless dihedral cores and every source facet are retained. Run3's exact split 12 collapsed / 4 balanced / 2 hostile / 11 untreated becomes 12 / 15 / 2 / 0. | [Complete table](CORE_TABLE.md), [machine inventory](../../results/run4/core_status.json). The classical source count is 364 labeled loopless parents. |
| PROVED | Every one of the eleven previously untreated cores has a geometric all-Z, multiplicity-one balanced decomposition. | Six smaller circuit cores, two merger cores, two q10 reflection cores and the q9 reflection core. Full source charts, boundaries, admissibility, signs and covered regions are proved separately. |
| PROVED | Ten cores share one complement-five positive Gale mechanism giving 3↔3. | [Smaller-core theorem](SMALLER_CORES.md), [independent merger proof](MERGER_WALLS.md). Alternating wall derivatives retain every relevant merger. |
| PROVED | Four cores have actual orientation-reversing reflections giving 5↔5. The (3,3,4) parent includes four spurion facets. | [q10 proof](Q10_334.md); [two independent q10 reviews](Q10_REVIEW.md); q9 and preserved q8 proofs. |
| PROVED | The remaining balanced core is the separate repaired spurion mechanism, preserved from Run2/3. | Its sign sum is 0+2−1−1; this remains distinct from interval topology and from the literal printed fixture. |
| PROVED | The six-facet circuit indicator kernel is exactly its balanced span at **every fixed positive Z**. | Symbolic K3,3 open overlaps; [independent audit](CIRCUIT_KERNEL_REVIEW.md). |
| PROVED | Each ten-facet all-Z indicator kernel is exactly its balanced span. | Five exact open-overlap spanning trees of rank nine at one positive Z; [proof](LOCAL_RELATION_KERNELS.md). This fixed witness bounds the uniform all-Z kernel, without asserting the same fixed-Z kernel at every Z. |
| PROVED | Both hostile cores have zero all-Z relation kernel on their eight admissible facets. | Exact open-neighborhood 8×8 indicator matrices, both determinant one; complete membership inversions and independent arithmetic checks in [counterexample branch](COUNTEREXAMPLE_SEARCH.md). |
| PROVED | No unbalanced constant-coefficient all-Z relation can use only admissible facets of any single nine-dimensional parent. | Complete kernel classification plus exact loop insertion, positive extension and dihedral transport. This goes beyond reporting balanced examples. |
| PROVED | Each balanced parent has exactly two multiplicity-one all-Z tilings using its admissible source facets. | Binary coefficients and the one-dimensional kernel. Arbitrary overlapping covers and extra contained tiles are outside this assertion. |
| FAILED, preserved | Interval geometry alone, complex-degree substitution, and universal admissible-facet parent coverage are insufficient. | Triangle relation, disconnected fiber, variable four-mass positive multiplicity and conic open hole remain unchanged. |
| CONJECTURAL / UNRESOLVED | A single admissible-facet tiling of the hostile q8 parent; arbitrary-tiling relation generation; k=2,m=4 Magic Number. | Homogeneous indicator independence does not decide the first, and local balance does not prove the latter two. |

**COMPUTATIONALLY-VERIFIED.** The final suite passes **142 tests in 24.70
seconds**. The exact preservation audit records 142 unchanged prior files
and seven exact-prefix campaign appends, with no historical rewrites;
see [validation.json](../../results/run4/validation.json).
New machine records contain fifteen prototype relations grouped into
three mechanisms, not fifteen independent mechanisms. The old 215-row
catalog, Run3 transported rows, failed claims and printed spurion data
are preserved.

## What controls the signed wall count?

**PROVED.** In the largest family, total positivity gives an alternating
seven-row Gale vector, and the actual six boundary inequalities inherit
six alternating nonzero derivatives. In four further cores, a real source
reflection reverses fiber orientation while preserving target orientation.
The repaired spurion needs its separate positive-minor identity. These
are wall-type constraints beyond interval endpoints. Exact overlap
connectivity then proves that no different coefficient relation escapes
the balanced span. For the hostile cores, the extra order/quadric and
positive multiplicity structure leads instead to indicator independence.

## Ranked mechanisms and explicit kill-tests

1. **PROVED: complement-five Gale family.** Check the recovered positive
   hyperplane ray, positive compressed seven-row matrix, complete affine
   fiber and all six wall derivatives. Any missing positive branch,
   zero complementary minor, omitted merger or noninjective selected wall
   would invalidate an application. The theorem's exact complement-five
   hypothesis makes these checks independent of balancedness.
2. **PROVED: genuine reflection family.** Verify the matrix intertwining
   C(Px)=HC(x)J, signed external positivity, source and target orientation
   characters, and absence of fixed transverse walls. A merely symmetric
   boundary inventory does not pass. The four spurion facets are retained
   in the q10 regression.
3. **PROVED: complete local kernel certificates.** For ten-wall families,
   each spanning-tree edge must be an open overlap of two genuine tiles
   and same-side disjointness must already be proved. For hostile cores,
   nonmembership must exhaust every positive closed-facet preimage and
   remain valid on an open neighborhood. An omitted gauge, branch,
   vanishing denominator, exceptional witness, or rank deficiency kills
   the proposed certificate. Independent exact checks pass these tests.

**SOURCE-VERIFIED.** The targeted comparison with Galashin–Lam, fiber
methods, and secondary-fan results is recorded in
[FINAL_SCOPE_REVIEW](FINAL_SCOPE_REVIEW.md). Their fixed-Z uniqueness and
global connectivity questions remain distinct. No absence of a search
match is used as a novelty certificate.
