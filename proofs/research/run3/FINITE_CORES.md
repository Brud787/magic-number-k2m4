# Finite parent cores and exact transport

**PROVED (source reduction).** Every nine-dimensional rank-two positroid
cell has q+s=13, 2<=s<=q, hence

`(q,s)=(7,6),(8,5),(9,4),(10,3),(11,2)`.

Deleting loops leaves a loopless parent of the same dimension; no other
source type exists by the classical cyclic parallel-class classification.
There are `binom(q,13-q)` labeled loopless parents for each support size,
giving `7+56+126+120+55=364`. This is a source count, not a relation count.
Dihedral composition types give29 cores:1,5,10,8,5 by increasing q. The
independent enumeration/composition checks are recorded in parent_profiles.
In particular, n<=9 does **not** contain every structural parent type.

## Transport is an identity of the entire fiber problem

**PROVED.** Let I be an increasing q-element subset of [n]. Zero insertion
`j_I:Gr(2,q)->Gr(2,n)` is a homeomorphism from the core cell and its closure
onto the corresponding looped cell and closure. For every positive n-by-6
external matrix Z,

`(j_I C) Z = C Z_I`.

Thus every source preimage of every Y, every source boundary incidence,
every image region, every real positive fiber and its topology is
identified **exactly**, for this Z, with the core problem for Z_I.
Codimension is unchanged. The same equality holds for the algebraic maps
on the embedded positroid varieties, so their algebraic degrees agree
whenever degree is defined. Oriented local degrees and wall signs agree
after transporting source orientations along j_I; changing a global
orientation reverses all signs and does not affect balancedness.

Selecting increasing rows preserves positive maximal minors. Conversely,
the Run2 [positive extension lemma](../run2/POSITIVE_EXTENSION.md), iterated
through prescribed gaps, extends **every** positive real q-by-6 matrix to
a positive n-by-6 matrix with exactly those original rows. Therefore any
all-positive-Z assertion about these identified core fiber problems holds
for a core if and only if it holds for a chosen loop insertion. This
includes injectivity, disjointness, image equality, multiplicity-one
decomposition, a specified fiber-topology statement, and a specified
signed indicator relation. The assertion is not deduced merely from
nonadmissibility transport; it follows from the full map identity and
surjectivity of positive row restriction.

The identification preserves positive-real preimage counts, and their
variation with Y or Z, rather than replacing them by complex algebraic
degree. No claim that positive multiplicity is constant is needed.

## Dihedral transport

**PROVED.** Signed cyclic relabeling of rank-two columns uses a minus sign
when a column crosses the cyclic cut. The matching signed cyclic
relabeling of rank-six external rows uses the same minus sign. Both
preserve positivity and their matrix products agree. Reflection uses
column reversal and a source row sign change, and external row reversal
with an ambient column sign change to restore six-minor positivity. The
maps then commute up to fixed invertible source/ambient row-coordinate
changes. They are homeomorphisms, preserve positive fibers, injection,
degrees, and image relations, with compatible transported orientations.

No parity-duality theorem is required for this finite reduction. Ordinary
dihedral operations and exact loop insertion suffice. The ordered cyclic
class-size composition determines the loopless source up to these
operations; arbitrary loop placements remain explicit in the ambient
orbit inventory.

## What this does and does not reduce

**PROVED conditional reduction.** A theorem establishing balancedness of
the full specified class of geometric codimension-one parent relations for
each of these29 loopless core types, for every positive core Z, transports
to all n. The core hypotheses themselves must also be transported as
above. Unresolved core geometry is not replaced by a favorable wall count.

This is **not** verification of the29 core cases, and not a reduction of
arbitrary complete-tiling relations to parent relations. Several cores
have disconnected or curved fibers and degree-two walls. The smallest
missing support is q=10 with three classes; q=11 with two classes is the
last missing support. Run3 enumerates those core types directly, without
enumerating the complete n10 or n11 ambient source universe or tilings.
