# Run 4 hostile proof audit

**PROVED / REVIEWED.** The complete [local parent theorem](LOCAL_PARENT_THEOREM.md)
passes the stated gates at its exact constant-coefficient all-Z,
single-parent, admissible-source-facet scope. This is Run4 SUCCESS D.
It is not a Magic Number theorem, a complete-tiling classification, or a
generation theorem. The bounded run stops after this audit.

## Independent reviews and arithmetic

The q10 (3,3,4)/(2,4,4) proof was authored by the root and audited
independently by two other agents. [Q10_REVIEW](Q10_REVIEW.md) checks the
global pivots, actual symmetries, rank-one endpoint bounds and all twenty
image normals using ambient elimination. [Q10_INDEPENDENT_REVIEW](Q10_INDEPENDENT_REVIEW.md)
separately verifies the geometric argument. The signed external reflection
character is checked on all 420 six-subsets in the two prototypes.

The six smaller circuit cases and reflected q9 case were authored by
one agent and reviewed independently by the root and the merger author.
The merger author supplied a separate complete hyperplane chart and
inversion, reviewed by the root and the smaller-core author. The corrected
q9 rank-one estimate explicitly sets v=0 as well and strengthens the
already valid exceptional image bound from six to five. No claim depended
on that stronger estimate.

The root's complement-five K3,3 construction and complete fixed-Z relation
kernel were independently audited in [CIRCUIT_KERNEL_REVIEW](CIRCUIT_KERNEL_REVIEW.md).
The initial slope is set to zero only for the starting representative;
it is allowed to move along the actual fixed-image fiber. This avoids
losing a fiber direction through an unallowed extra normalization.

The five ten-wall overlap certificates were authored by the hostile agent
and audited by the root. Every edge has two positive open-wall sources
with the same target plane; known tile injectivity makes the intersection
open. Same-side disjointness supplies exactly two nonzero indicators
there, and graph connectivity supplies the complete rank bound. The
known all-Z relation supplies the matching reverse inclusion. No complete
chamber enumeration is assumed. Ninety archived endpoint sources and
their exact target Plucker coordinates were checked again by an independent
implementation using only Python Fraction arithmetic, without the
producer's Sympy kernel or row-change solve. The five graph constraints
were independently propagated by graph traversal.

The hostile q8/q9 independence proofs were authored by the hostile agent
and audited by the root. The review checked all of the following:

- Exhaustive source-closure sets agree between basis inclusion and
  recursive facet enumeration: 1,999 and 3,033 strata. Every failed
  three-anchor gauge, respectively 1,621 and 2,403 strata, has the stated
  class-complement obstruction. Nonzero twistors exclude all of them
  at each witness and in a neighborhood.
- The q8 complete affine line has one transverse intersection with each
  ordinary wall, and every remaining coordinate and order minor is
  nonzero. Positivity or its failure is therefore a complete closed-tile
  membership decision, stable on an open target neighborhood.
- The q9 double-coordinate walls are solved projectively, not by assuming
  a convenient affine patch. On the single-coordinate walls the excluded
  direction a1=a2=0 is rank one: its first row maps into both Y and
  span(Z3,Z4,Z5,Z6), whose intersection is zero by the nonzero twistor.
  Independence of those four rows forces the first row to vanish. This
  also forces the structurally zero quadratic term and justifies linear
  inversion in a neighborhood; it is not a fortuitous sample factorization.
- Every denominator and remaining coefficient is strict and nonzero.
  Thus the indicator matrices are certified on open neighborhoods,
  which is essential for relations modulo lower-dimensional sets.
- A second implementation of ambient row-containment equations checks
  each kernel and wall candidate. All ordered source minors independently
  verify source positivity. Fraction elimination independently gives
  determinant one for both saved 8×8 indicator matrices.

The final independent [scope and primary-source audit](FINAL_SCOPE_REVIEW.md)
passed. It identified and corrected one wording issue: uniqueness applies
to **multiplicity-one facet tilings**, not arbitrary overlapping covers.
The union of both canonical sides is an overlapping cover and must not
be excluded by a binary-coefficient argument.

The assembled theorem received a final consistency read. It passed
after making explicit that two local decompositions must cover **the
same region** before their difference is asserted to be a relation.
This is now stated in Section 6; the core counts, all-Z transport and
multiplicity-one uniqueness match the reviewed claim.

## The ten hostile gates

| Gate | Outcome and precise evidence |
|---|---|
| Complete core accounting | PASS: preserved 12/4/2/11 becomes 12/15/2/0. All 29 types, all 364 labeled loopless parents, all source facets retained. |
| Complete boundaries | PASS: all source facets matched by affine labels and bases. Both (5,5) merger walls are present. Collapsed mergers and other lower strata remain explicit. |
| Admissibility | PASS: independent all-Z source certificates or direct inversion for every tile. The complete prior inventory has no unknown facets. |
| Full fiber | PASS for each claimed relation: complete affine or projective-linear chart, normalization, order conditions and exceptional endpoints proved. Hostile fibers retain their quadratic/conic conditions. |
| Image-side sign | PASS: actual kernel derivatives or complementary minors, with a source/target reflection calculation where used. Source boundary signs alone are not substituted. |
| All-Z | PASS: symbolic positivity and nonvanishing/connectedness establish all-Z geometric relations. Exact fixed-Z witnesses only bound uniform all-Z relation kernels where that weaker argument suffices. |
| Multiplicity | PASS: generic full positive-fiber endpoints and independent wall injection prove multiplicity one. Four-mass variable positive multiplicity is retained and excluded from ordinary tile sums. |
| Covered region | PASS for all fifteen balanced cores: same-side open disjointness and equality of finite closed unions with the closed parent image. Hostile q8 single coverage remains unresolved. |
| Balance and completeness | PASS: ten K3,3 graphs, five spanning trees, two invertible indicator matrices, and twelve empty admissible-facet sets determine every local all-Z coefficient kernel. |
| Independence | PASS: separate proof audits, different kernel eliminations, direct source/target minors, Fraction arithmetic and independent graph traversal. |

## What the proof does not repair

**FAILED, preserved.** The literal published spurion common-parent fixture
remains discrepant. The repaired parent theorem stays separate from it,
and no embedding into the printed fifty-tile collection is claimed.

**FAILED, preserved.** Interval topology alone does not balance wall types.
Linear ambient equations do not guarantee connected positive fibers.
Complex degree does not equal the number of positive preimages. Universal
coverage of a parent by its admissible facets fails in the q9 conic fixture.

**CONJECTURAL / UNRESOLVED.** A single admissible-facet tiling for the
hostile q8 parent; the fixed-Z uniqueness question at every Z for the
five ten-wall cores; generation of arbitrary tiling relations by these
parent relations; k=2,m=4 Magic Number. The current local theorem does
not claim any of these. It also does not assert priority over the
targeted primary literature.

## Validation and preservation

**COMPUTATIONALLY-VERIFIED.** The untouched baseline was 100 passing tests
in 20.51 seconds. The final full-suite result and the 149-file history
audit are recorded in [validation.json](../../results/run4/validation.json).
New exact fixtures and proof regressions are stored separately under
Run4. Previous source, tests, fixtures and result catalogs are unchanged;
top-level campaign notes receive only appended, clearly dated updates.
No complete-tiling enumeration or relation-generation search was launched.
