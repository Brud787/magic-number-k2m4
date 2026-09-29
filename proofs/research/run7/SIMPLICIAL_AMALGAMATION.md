# The twisted amalgamation simplicial vector spaces

**PROVED, independently audited in Run7.** Let V_n be the free real
vector space on all all-Z admissible eight-dimensional rank-two source
cells on n labels. Put V_n=0 for n<6. Let K_n be the all-Z indicator
kernel modulo semialgebraic sets of dimension at most seven, and let L_n
be the complete Run4 local parent span. Adjacent amalgamation, with the
rank-two cyclic sign at the wrap, and zero insertion define simplicial
vector spaces

\[
 A_p=V_{p+1},\qquad B_p=K_{p+1},\qquad C_p=L_{p+1},
 \qquad Q_p=V_{p+1}/L_{p+1},\qquad H_p=K_{p+1}/L_{p+1}.
 \tag{1}
\]

This document proves only the simplicial structure. It does not infer
that H vanishes from any pattern of numerical ranks. Any application of
normalization requires a separate exact finite certificate and argument.

## 1. Raw column operations and positivity

For n columns x=(x_0,...,x_(n−1)), define

\[
 d_i x=(x_0,...,x_i+x_{i+1},...,x_{n-1})\quad(0\le i<n-1),
\]
\[
 d_{n-1}x=(x_0-x_{n-1},x_1,...,x_{n-2}),
 \tag{2}
\]

and let s_j insert a zero immediately after x_j, 0≤j≤n−1.
These operations commute with all invertible row changes. The ordinary
face has nonnegative ordered minors by the sum formula. The wrap face
does too: for 1≤j≤n−2,

\[
 \det(x_0-x_{n-1},x_j)
 =\det(x_0,x_j)+\det(x_j,x_{n-1}).
 \tag{3}
\]

The wrap sign cannot be replaced by a plus sign. Equivalently let
tau(x)=(-x_(n−1),x_0,...,x_(n−2)); this is the positive rank-two cyclic
action and d_(n−1)=d_0 tau. Its nth power multiplies every column by −1,
which is the row change −I_2 and hence is trivial on source row spaces.
The matching rank-six external action is also signed by −1 and preserves
positivity. Thus the geometric transport in
[AMALGAMATION_PROOF](AMALGAMATION_PROOF.md) applies to every face, including
the wrap. A raw face with rank less than two is treated as zero when
passing to source-cell generators.

## 2. All raw simplicial identities

At every index where both composites are defined (n≥3 for two faces),
the column operations satisfy

\[
 d_i d_j=d_{j-1}d_i\quad(i<j),
 \tag{4}
\]
\[
 d_i s_j=\begin{cases}
 s_{j-1}d_i,&i<j,\\
 \mathrm{id},&i=j\text{ or }i=j+1,\\
 s_jd_{i-1},&i>j+1,
 \end{cases}
 \tag{5}
\]
\[
 s_i s_j=s_{j+1}s_i\quad(i\le j).
 \tag{6}
\]

Here compositions are read right to left, with the appropriate number
of columns at each step. Identity (6) just inserts two zero columns.
For (4), two non-wrap faces either affect disjoint summands or use
associativity. If j=n−1 is the wrap face, the disjoint interior cases
again commute. The two endpoint calculations are

\[
 (x_0-x_{n-1})+x_1=(x_0+x_1)-x_{n-1},
\]
\[
 (x_0-x_{n-1})-x_{n-2}=x_0-(x_{n-2}+x_{n-1}).
\]

For (5), the ordinary cases either erase the inserted zero or shift its
position. If i=n is the last face after a zero insertion, then for j<n−1
subtracting the retained last column commutes with the insertion after
the correspondingly retained column j. For j=n−1 it subtracts the
appended zero and is the identity. The other end case i=j=n−1 merges
the old last column with its appended zero and is also the identity.
This exhausts all boundary indices; no identity relies on an ordinary
unsigned wrap convention.

The simplicial degree-zero group in (1) is zero. There is no required
face from degree zero to degree minus one in an ordinary simplicial
object. Consequently no length-one raw convention is needed. All
identities with a domain V_n=0 are vacuous.

## 3. Why discarding non-tiles respects every identity

On a generator S∈U_n apply the exact source image rule from Section 1
of AMALGAMATION_PROOF, then keep its label if it is again an admissible
eight-cell and otherwise put zero. Degeneracies simply insert loops.
We must check that an intermediate zero cannot become an admissible
eight-cell later on one side of (4)–(6).

Rank loss cannot be repaired by later linear combinations or by inserting
zero columns. A source-dimension drop cannot be repaired either: the
subsequent source maps are rational maps on their rank-two domains, and
their image dimensions do not exceed their source dimensions. Equivalently
the explicit positive source-image table gives a nonincrease at every
step. Zero insertion preserves source dimension exactly.

The remaining possibility is an eight-dimensional nonadmissible
intermediate. The complete tile-core classification and the new singleton
created by any dimension-preserving nonloop amalgamation show that such
an intermediate cannot be four-mass. It has a parallel class D with at
most four complementary nonloop columns. This obstruction is persistent
under any further face that preserves source dimension:

* A face involving a loop preserves the same obstruction.
* A face between two distinct nonsingleton classes, neither D, decreases
  q by one and leaves |D| unchanged; the complement decreases by one.
* Such a face involving D decreases both q and |D| by one, so its
  complement is unchanged. The residual D is nonempty.

All other nonloop faces decrease source dimension. In particular if D
were singleton, a face removing its last column is already in that
dimension-decreasing case. Thus every subsequent dimension-eight image
still has a class with at most four complementary nonloops and is
collapsed for every positive external matrix. Loop insertion leaves the
obstruction unchanged. No sequence can repair a discarded intermediate.

The raw identities give equal final column matrices on the original
source cell, not merely equal source dimensions or sample bases. Their
nonnegative minor supports therefore give the same final source label.
If one branch has a discarded intermediate, the preceding persistence
argument says its raw final label is also discarded; the equal other
branch is consequently discarded. Otherwise both branches retain their
raw equality. This proves (4)–(6) on the truncated free spaces V_n.

The lower cutoff is compatible. U_6 consists only of the top cell with
six singleton classes, and every face lowers its source dimension, so
all faces V_6→V_5 are zero. Degeneracies from V_6 insert a loop; either
neighboring face that removes the inserted zero returns that same tile,
as required by (5). More generally, dimension monotonicity prevents any
path through a lower group from returning to dimension eight except
when a zero insertion was not actually truncated. All identities with
nonzero domain and codomain are covered by the argument above.

## 4. Descent of both relation spaces

The uniform geometric theorem in AMALGAMATION_PROOF proves d_i(K_n)⊆K_(n−1)
and d_i(L_n)⊆L_(n−1) for every face i. Its hypotheses explicitly use all-Z
relations, positive external degenerations for each arbitrary downstairs
matrix, complete admissibility, multiplicities, and strict neighborhood
limits. A fixed-Z sampled relation is not included in this assertion.

For zero insertion j_I, the identity (j_I C)Z=C Z_I holds on the entire
source closure. The restricted external matrix Z_I is positive. Thus
every all-Z relation on the smaller source labels remains an all-Z
relation on their inserted labels. Every parent relation is likewise
the transported relation of the zero-inserted parent. Hence degeneracies
preserve both K and L. Finally L⊆K is the already proved geometric local
relation theorem, independently of any claim about their equality.

Since the operations on these subspaces are restrictions of the operations
on V, their simplicial identities are inherited. Passing to either
quotient gives the identities in (1) as well. In particular

\[
 0\longrightarrow H_\bullet\longrightarrow Q_\bullet
 \longrightarrow (V/K)_\bullet\longrightarrow0
\]

is a degreewise exact sequence of simplicial vector spaces. Exactness
after a normalization functor is a separate standard theorem to be cited
and checked if it is used. Neither finite rank extrapolation nor
all-Z generation is built into the definition of these spaces.

**Independent review.** The separate Run7 deletion/structural agent
checked the raw wrap identities, all truncation cases, the lower cutoff,
and the degree shift in (1), and found no mathematical gap. The unnecessary
length-two double-face claim was removed before completion: such a
composite would leave the nonaugmented simplicial index range. The finite
normalization certificates and any global consequence remain separately
reviewed inputs to a subsequent theorem.
