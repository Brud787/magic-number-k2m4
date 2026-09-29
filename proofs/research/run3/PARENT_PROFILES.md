# Run 3 parent profiles and bounded coverage

**COMPUTATIONALLY-VERIFIED.** The preserved complete parent catalogs contain
7,112,882 parents at n=7,8,9, respectively, in 1,9,57 ambient dihedral
orbits. The new [machine inventory](../../results/run3/parent_profiles.json)
retains every orbit member, affine representative, cyclic class composition,
loop placement, and source-wall admissibility certificate. It does not
identify different loop placements merely because their loopless cores agree.

**PROVED.** The source equation q+s=13 gives support q=7,...,11. Exact loop
deletion/insertion and dihedral transport reduce the entire specified local
fiber problem to 29 loopless types. See [FINITE_CORES](FINITE_CORES.md) and
its [independent audit](CORE_THEOREM_REVIEW.md). The missing supports beyond
n9 are q10 and q11. Only their loopless cores were enumerated; no complete
n10/n11 source universe or complete tilings were searched.

**COMPUTATIONALLY-VERIFIED.** There are 364 labeled loopless parents:
7,56,126,120,55 by support. Recursive compositions, direct cyclic cuts,
independent basis rotations, and Burnside counts give respectively
1,5,10,8,5 dihedral types. The source classification proves completeness;
the independent implementations check its finite encoding.

In the following table, A counts certified all-Z tile facets, C counts
collapsed facets, and D counts nonadmissible four-mass facets. D is a
source-wall count, not positive image multiplicity. S is the number of
spurion facets within A. These are **COMPUTATIONALLY-VERIFIED** counts using
**SOURCE-VERIFIED / PROVED** certificates. Source-wall classification is
complete in this inventory; relation geometry is not.

| q | Cyclic composition, modulo dihedral action | Labeled cores | Walls | A | C | D | S | Fiber/relation scope |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 7 | 1,1,1,1,1,2 | 7 | 8 | 6 | 2 | 0 | 0 | All-Z Gale 3↔3 |
| 8 | 1,1,1,1,4 | 8 | 9 | 0 | 9 | 0 | 0 | Collapsed parent |
| 8 | 1,1,1,2,3 | 16 | 10 | 6 | 4 | 0 | 0 | Unresolved |
| 8 | 1,1,2,1,3 | 16 | 10 | 6 | 4 | 0 | 0 | Unresolved |
| 8 | 1,1,2,2,2 | 8 | 11 | 8 | 2 | 1 | 0 | Exact disconnected-fiber fixture |
| 8 | 1,2,1,2,2 | 8 | 11 | 10 | 1 | 0 | 0 | New all-Z interval/reflection 5↔5 |
| 9 | 1,1,1,6 | 9 | 10 | 0 | 10 | 0 | 0 | Collapsed parent |
| 9 | 1,1,2,5 | 18 | 11 | 0 | 11 | 0 | 0 | Collapsed parent |
| 9 | 1,1,3,4 | 18 | 11 | 6 | 5 | 0 | 0 | Unresolved |
| 9 | 1,2,1,5 | 9 | 11 | 0 | 11 | 0 | 0 | Collapsed parent |
| 9 | 1,2,2,4 | 18 | 12 | 6 | 6 | 0 | 0 | Unresolved |
| 9 | 1,2,3,3 | 18 | 12 | 10 | 2 | 0 | 1 | Repaired spurion 5↔5; symbolic signs |
| 9 | 1,2,4,2 | 9 | 12 | 6 | 6 | 0 | 0 | Unresolved |
| 9 | 1,3,1,4 | 9 | 11 | 6 | 5 | 0 | 0 | Unresolved |
| 9 | 1,3,2,3 | 9 | 12 | 10 | 2 | 0 | 0 | Distinct from spurion; unresolved |
| 9 | 2,2,2,3 | 9 | 13 | 8 | 2 | 3 | 0 | Conic; admissible-facet cover fails at exact Z |
| 10 | 1,1,8 | 10 | 11 | 0 | 11 | 0 | 0 | Collapsed parent |
| 10 | 1,2,7 | 20 | 12 | 0 | 12 | 0 | 0 | Collapsed parent |
| 10 | 1,3,6 | 20 | 12 | 0 | 12 | 0 | 0 | Collapsed parent |
| 10 | 1,4,5 | 20 | 12 | 6 | 6 | 0 | 0 | Unresolved; full-dimensional merger wall retained |
| 10 | 2,2,6 | 10 | 13 | 0 | 13 | 0 | 0 | Collapsed parent |
| 10 | 2,3,5 | 20 | 13 | 6 | 7 | 0 | 0 | Unresolved; full-dimensional merger wall retained |
| 10 | 2,4,4 | 10 | 13 | 10 | 3 | 0 | 0 | Unresolved |
| 10 | 3,3,4 | 10 | 13 | 10 | 3 | 0 | 4 | Unresolved; four spurion facets |
| 11 | 1,10 | 11 | 10 | 0 | 10 | 0 | 0 | Collapsed parent |
| 11 | 2,9 | 11 | 11 | 0 | 11 | 0 | 0 | Collapsed parent |
| 11 | 3,8 | 11 | 11 | 0 | 11 | 0 | 0 | Collapsed parent |
| 11 | 4,7 | 11 | 11 | 0 | 11 | 0 | 0 | Collapsed parent |
| 11 | 5,6 | 11 | 11 | 6 | 5 | 0 | 0 | All-Z Cramer 3↔3 |

For q10/q11 walls, increasing loop deletion either reaches an already
classified n<=9 cell or the two-class (5,5) cell. The latter has the direct
hyperplane inversion and separate BCFW recipe in
[TWO_CLASS_THEOREM](TWO_CLASS_THEOREM.md). No extrapolation from a Jacobian
sample, degree, or favorable facet count is used. Every individual wall
record and the transport proof are retained in the JSON inventory.

## Three larger-support prototypes and a fourth core

**PROVED.** The alternating-singleton n8 parent `(12)(3)(45)(6)(78)` has a
global projective positive-orthant chart. Its complete fibers are intervals,
and its ten admissible walls give the all-Z relation proved in
[LARGER_SUPPORT](LARGER_SUPPORT.md). Reflection explains balancedness.

**PROVED (exact fixed Z).** The adjacent-singleton n8 parent
`(12)(34)(56)(7)(8)` has an extra quadratic positivity inequality. Its
complete positive fiber in the archived fixture is two disjoint intervals.
The omitted four-mass wall cannot be treated as an ordinary tile.

**PROVED.** The n9 parent `(12)(34)(56)(789)` has a conic fiber model, rather
than a positive orthant alone. **PROVED (exact fixed Z):** its three
archived targets exhibit 0,1,2 positive four-mass preimages; one open part of
the parent image misses all eight admissible closed facet tiles. See
[MULTIPLICITY](MULTIPLICITY.md). This is a failure of the proposed cover
strategy, not an unbalanced admissible relation.

**PROVED.** The support-eleven (5,6) core has a complete affine-interval
fiber calculation and an alternating 3↔3 relation for every positive Z.
All other two-class parents are collapsed. This is a structurally complete
sector theorem, and includes every loop insertion.

## Sign inventory and what it counts

**COMPUTATIONALLY-VERIFIED, using the four proved mechanisms.**
[sign_counts.json](../../results/run3/sign_counts.json) includes all 1,001
parents through n9 and the (5,6) prototype. Its 414 certified rows comprise
315 Gale transports, 80 n8 reflection transports, 18 spurion copies, and
one two-class prototype. They all have coefficient sum zero. There are
472 unresolved rows and 116 collapsed parents; their coefficient sums are
null, not zero. The original 215-row Run2 catalog remains unchanged.

The 414 rows are **four prototype families**, not 414 independent
confirmations. The Gale and two-class families share alternating-circuit
algebra; the four catalog mechanism IDs do not mean four unrelated theories.
Twelve of the 29 core types have the proved parent-image collapse bound.
Of the other seventeen, four have certified parent decompositions, two
have hostile fiber/cover obstructions, and eleven remain untreated here.
This is not verification of local balancedness for all 29 cores.

**CONJECTURAL (next finite targets).** The q10 `(3,3,4)` core is particularly
useful because four of its ten admissible walls are spurions. The
`(1,4,5)` and `(2,3,5)` cores test boundary completeness: their admissible
wall list includes a merger into (5,5), which a naive coordinate-deletion
list would miss. No global signs or fiber topology for these cores are
asserted in this bounded pass.
