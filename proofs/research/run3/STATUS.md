# Run 3 bounded checkpoint — 2026-09-05

**Run3 SUCCESS C**, restricted to a structurally complete parent sector.
The finite-core reduction and hostile fixtures give useful boundaries for
the next run. They do not establish balancedness of every parent relation
or Magic Number. This pass stops before a general proof search.

| Status | Result | Exact scope and evidence |
|---|---|---|
| COMPUTATIONALLY-VERIFIED | Preserved baseline: 66 tests passed before changes, in 14.31s; 99 prior files hashed. | [Baseline](../../results/run3/baseline.json). Original Run1/2 fixtures and failed claims remain intact. |
| PROVED | The repaired spurion's ten signs have a symbolic explanation: (1−1)+(1+1)+(−1+1−1)+(−1+1−1)=0. | Ordered Cramer minors, one cofactor factorization and a positive Plucker identity; [SPURION_SIGN_MECHANISM](SPURION_SIGN_MECHANISM.md). This is one mechanism, including all symmetry copies. |
| PROVED | Image endpoint signs in a linear projective fiber are normalized complementary-minor signs. The seven n7 parents have alternating 3+3 signs by their positive Gale kernel. | [SIGN_FORMULA](SIGN_FORMULA.md). Rank, wall admissibility and complete fiber hypotheses are separate. |
| PROVED | A source-orientation reversing, target-orientation preserving symmetry pairs constant transverse wall signs oppositely. | Explicit hypotheses and verification for `(12)(3)(45)(6)(78)` in [SIGN_FORMULA](SIGN_FORMULA.md); not a criterion defined by the desired balance. |
| PROVED | The structurally different n8 parent `(12)(3)(45)(6)(78)` has an all-Z, multiplicity-one local 5↔5 relation. | Ten independently certified BCFW walls; exact interval fibers, endpoint completeness and closed union equality in [LARGER_SUPPORT](LARGER_SUPPORT.md). Reflection explains its count. |
| PROVED | Every full-dimensional nine-dimensional rank-two parent with exactly two parallel classes has profile (5,6) and an all-Z local 3↔3 relation. Other two-class profiles are collapsed. | [TWO_CLASS_THEOREM](TWO_CLASS_THEOREM.md), [independent audit](CORE_THEOREM_REVIEW.md). Applies to arbitrary n and loop insertions. Six alternating positive-minor signs force zero wall-type sum. |
| PROVED | The same two-class mechanism works for rank two and every even m≥2, with profile (m+1,m+2). | A restricted `(m+2)/2 ↔ (m+2)/2` local relation, not a theorem for other profiles or complete tilings. |
| PROVED | Every nine-dimensional rank-two parent is a loop insertion/dihedral image of a core with support at most 11. Entire fibers, specified local image relations, topology, real multiplicity and defined algebraic degrees transport exactly. | [FINITE_CORES](FINITE_CORES.md). The reverse all-Z direction uses positive row extension. No complete-tiling extension is inferred. |
| COMPUTATIONALLY-VERIFIED | There are 364 labeled loopless parents in 29 dihedral types; n≤9 misses the support-ten and support-eleven types. All source walls of these cores have retained tile/non-tile certificates. | Independent cut/composition/affine/Burnside checks; [PARENT_PROFILES](PARENT_PROFILES.md), [JSON](../../results/run3/parent_profiles.json). This is not complete image-relation classification. |
| PROVED | The adjacent-singleton n8 parent has an exact disconnected positive fiber: `(-8/75,0) ∪ (1/7,8/37)`. | Exact fixed positive Z; essential quadratic ordering inequality and explicit two positive four-mass preimages, [LARGER_SUPPORT](LARGER_SUPPORT.md). |
| PROVED | The hostile n9 profile (2,2,2,3) has a positive conic fiber model. Its four-mass wall has 0,1,2 positive preimages at three exact targets for the same positive Z; the two sheets have opposite Jacobian signs. | All-Z chart/pivot; exact fixed-Z multiplicity statements in [MULTIPLICITY](MULTIPLICITY.md). Complex degree is not positive multiplicity. |
| PROVED | An explicit open subset of that n9 parent image misses all eight admissible closed facet tiles. | Exact fixed-Z closed-cover obstruction: 3,033 source strata, 2,403 gauge degenerations, 126 nonzero twistors, complete nonnegative conic fiber; [MULTIPLICITY](MULTIPLICITY.md), [review](REVIEW.md). |
| FAILED | Every nine-dimensional parent image can be covered by its admissible source facets. | The preceding open hole disproves this proposed strategy. It supplies neither an unbalanced admissible relation nor a Magic Number counterexample. |
| FAILED | Interval topology, even with all wall maps of degree one, forces equal numbers of wall types; complex degree can replace real positive multiplicity. | The retained degree-one triangle 1↔2 relation and exact four-mass branch fixtures kill these shortcuts. |
| COMPUTATIONALLY-VERIFIED | The sign inventory has 414 certified transported rows from four mechanisms: 315 Gale, 80 reflection, 18 spurion, one two-class prototype. Every certified coefficient sum is zero. | All 1,001 parents through n9 plus the q11 prototype are recorded. 472 unresolved rows have null signs; 116 parents are collapsed. [sign_counts.json](../../results/run3/sign_counts.json). These are not 414 independent mechanisms and do not replace the preserved 215-row Run2 catalog. |
| CONJECTURAL | The remaining parent relation cases are balanced; suitable parent relations generate arbitrary tiling relations; k2,m4 Magic Number. | No generation or all-core verification was attempted. No certified unbalanced admissible tile relation was found in this bounded pass. |

## What controls the signed number of wall types?

The four catalog mechanism IDs name four source prototype families. They
are not four unrelated theories: the Gale and two-class arguments share
the same classical alternating-circuit algebra. The broad explanations
found here are positive-minor sign structure and orientation-reversing
symmetry.

**PROVED on the stated classes:** interval geometry supplies the indicator
identity; ordered positive-minor signs or an orientation-reversing symmetry
supply the separate zero coefficient sum. For the spurion the sum is
0+2−1−1. For the complete two-class sector, the six basis coefficients
alternate because their Cramer numerators are ordered positive minors.
For the new n8 parent, reflection pairs opposite signs.

**FAILED as a universal explanation:** cancellation of oriented endpoints
does not imply a constant sum over wall types. The actual topological
identity is pointwise in Y and retains all signed real preimages. The
four-mass fixtures show both repeated wall types with opposite orientations
and a parent region where no admissible facet endpoint occurs at all.
Thus a general proof needs more than degree-one wall labels or convexity.

## Ranked next explanations and explicit kill-tests

1. **PROVED on prototypes; CONJECTURAL beyond them: positive-minor sign
   structure on the remaining finite cores.** Next useful core: `(3,3,4)`,
   whose ten admissible walls include four spurions. Kill the proposed
   extension if a required determinant changes sign, a source chart omits
   a full-dimensional endpoint, or certified image coefficients have
   unequal counts. A favorable table of admissible facets is insufficient.
2. **PROVED conditional criterion; CONJECTURAL new applications: reflection
   pairing.** Check actual source/external symmetries, a global submersion,
   and constant transverse signs. A fixed admissible wall, the wrong
   orientation character, or a failure of the intertwining map kills that
   application. It does not address asymmetric spurion-like profiles.
3. **CONJECTURAL: signed real-preimage functions retaining internal
   strata.** This may organize curved or disconnected fibers, but it
   supplies no unit functional yet. The triangle relation kills any claim
   that topology or constant degree alone finishes the argument. Replacing
   the 0/1/2 positive counts by 2, or deleting a four-mass endpoint, kills
   the proposed construction immediately.

The complete decision record is [candidates.json](../../results/run3/candidates.json).
The q10 `(1,4,5)` and `(2,3,5)` cores are additional boundary-completeness
tests: each has an admissible (5,5) merger that cannot be omitted from a
coordinate-wall list. Their image geometry was not launched in this pass.

## Scope, prior work and stopping point

**SOURCE-VERIFIED.** The relevant circuit, cofactor and orientation tools
are classical; GL already separates balanced parent flips, uniqueness and
connectivity. The targeted [literature delta](LITERATURE_DELTA.md) records
that scope. No literature-first novelty is claimed for these mechanisms.

**PROVED restricted theorem, not full Magic Number:** the two-class sector
meets Run3 SUCCESS C. The 29-core reduction is proved, but the other sectors
remain incomplete, so SUCCESS D is not claimed. No unbalanced admissible
local relation or complete-tiling counterexample was certified. No claim
that such a relation cannot exist follows from the search.

Final validation and preservation evidence are in
[validation.json](../../results/run3/validation.json). The independent
[review](REVIEW.md) identifies every unproved scope extension. This bounded
pass is complete; no long proof search or complete-tiling enumeration is
left running.

**COMPUTATIONALLY-VERIFIED final validation:** all **100 tests passed in
20.10s**. Of the 99 prior files, 95 are byte-for-byte unchanged and the four
updated campaign pages retain their complete prior contents as exact
prefixes. All required Run3 outputs and local research links are present.
