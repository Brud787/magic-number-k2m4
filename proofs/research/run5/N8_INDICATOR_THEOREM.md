# The complete n=8 indicator kernel

**PROVED, independently audited in [INDICATOR_INDEPENDENT_REVIEW](INDICATOR_INDEPENDENT_REVIEW.md).**
For the complete universe of 176 all-Z admissible source tiles at
k=2,m=4,n=8, the constant-coefficient all-Z indicator kernel equals the
span L8 of the full Run4 parent relations. In particular D8⊆L8, and every
complete all-Z tiling has twenty tiles. This is a finite-n theorem, not
an all-n theorem. It does not require enumeration of complete n8 tilings.

The numerical-looking part is an exact finite rank certificate: 103 open
indicator witnesses give an integer matrix A with a 103×103 minor of
determinant **2**. The completeness of each indicator decision is proved
below. The already proved 73-dimensional local span gives the matching
upper bound; no unenumerated chamber can change the conclusion.

## 1. The complete tile universe and the inversion hypothesis

**PROVED / SOURCE-VERIFIED.** The preserved all-Z source classification
gives precisely 176 admissible eight-dimensional cells at n8. They are
28 cells with six nonloop singleton classes, 112 with seven nonloops and
two double classes, and 36 loopless cells with cyclic class sizes given
by permutations of (3,3,1,1) or (3,2,2,1). Every one has a parallel class
D of size q−5, where q is its nonloop support size. The remaining source
labels either have a class with at most four complementary nonloop
labels, hence collapsed image, or have the certified noninjective
four-mass profile (2,2,2,2). All excluded cells remain in the source
inventory; no sample rank is used for admissibility.

The 176-cell set is checked against the complete existing source catalog,
with independent affine and basis encodings. Its exact order is the
column order of [local_relation_matrix_n8.json](../../results/run5/local_relation_matrix_n8.json).
All these tiles also have the preserved BCFW injectivity certificates.
The following inversion is an independent geometric description needed
for indicator membership, rather than another classification from rank.

Fix one such cell S and delete its loops. Cut the cyclic order immediately
after D so that D is last. Source columns and external rows crossing the
cut both receive the usual minus sign; rank two and external rank six
have the same cyclic twist, and their products agree exactly. Write the
five complementary labels as successive classes A1,...,A_ell and put
r=|D|. Since dim S=q+s−4=8, ell+r=6.

Every open source point has a representative

\[
C=\begin{pmatrix}
 a_1&\cdots&a_5&0&\cdots&0\\
 t_{j(1)}a_1&\cdots&t_{j(5)}a_5&d_1&\cdots&d_r
\end{pmatrix},
\quad a_i,d_h>0,\quad t_1<\cdots<t_\ell.
\]

Normalize the D direction to vertical. The other directions are finite
and ordered on its complementary projective interval; the displayed
conditions are exactly positivity. Common source row changes account
for the usual scaling and translation freedoms. There is no restriction
that the individual slopes themselves be positive.

## 2. Complete rational inversion

Let Z now denote the positive q×6 matrix after this signed cyclic cut.
Set H=span(Z1,...,Z5). It is a hyperplane. The functional

\[
 h(X)=\det(Z_1,\ldots,Z_5,X)
\]

is strictly positive on every external row belonging to D. For any
nonnegative source representative in the displayed chart with D nonzero,
the second image row has positive h-value, and the first lies in H.
Thus Y is not contained in H and Y∩H is a unique line.

Given Y=span(y1,y2), recover this line by

\[
 R_0=h(y_2)y_1-h(y_1)y_2.
\]

Express R0 uniquely in the independent five-row basis of H. If its
five coefficients have mixed strict signs, there is no positive source
preimage in this chart. If they have one common sign, reverse R0 when
necessary and call the resulting positive coefficients a1,...,a5.
Choose S0∈Y with h(S0)>0, for example a suitably signed one of the two
given frame rows. Define the six compressed rows

\[
 B=(V_1,\ldots,V_\ell,Z_D),\qquad
 V_j=\sum_{i\in A_j}a_iZ_i.
\]

The determinant of B is a positive sum of increasing external six-minors:
its blocks are disjoint and in cyclically cut order, and all coefficients
are positive. Hence it is invertible. Write uniquely

\[
 S_0=\sum_{j=1}^{\ell}t_jV_j+\sum_{h=1}^{r}d_hZ_{D_h}.
\]

These are the complete candidate source coordinates. They give a positive
source point exactly when the five inequalities

\[
 t_{j+1}-t_j>0\ (1\le j<\ell),\qquad d_h>0\ (1\le h\le r)
\tag{1}
\]

hold. Indeed they are precisely all nonzero ordered source two-minor
conditions in the chart, and the matrix product has image rows R0,S0.
The source has rank two because the complementary and D coefficients
are nonzero and have the required signs.

This inversion misses no row-space branch. For any other positive
preimage, its first image row is a positive multiple of R0. Rescale it
to R0. Its second image row is alpha*S0+beta*R0 with alpha>0, since h
is positive on it. The permitted positive second-row rescaling and
subtraction of beta*R0 align it to S0. They preserve the signs of all
d_h and successive slope differences. The unique six-row expansion
then recovers the same source row space. Mixed signs of the recovered
first-row coefficients cannot be repaired by a different frame.

For the exact Vandermonde fixture, the implementation uses the first
five ambient columns as an invertible H-basis pivot. That particular
pivot is not asserted for an arbitrary positive external matrix; the
geometric argument uses any independent five-column pivot. The arbitrary-Z
invertibility used in the proof is that of the six compressed rows B.

## 3. Closed tiles and open-neighborhood nonmembership

The witness targets satisfy every four-bracket det(Y,Z_I)≠0 for
I∈binom([8],4). This eliminates every potentially missing closed-source
chart as follows.

If D disappears entirely, the source image plane is contained in H,
the span of the five complementary rows. It then meets each four-space
spanned by four of those rows, forcing a zero four-bracket. If an outside
column disappears, or an outside direction merges into the D direction,
a nonzero row functional killing D yields a nonzero image vector
supported on at most four complementary rows. This again forces a zero
four-bracket. Rank preservation on the nonnegative Grassmannian guarantees
that this vector cannot map to zero.

Consequently every preimage in closure(S) at a witness retains D and
all five nonzero complementary coefficients, with D distinct from the
other directions. It lies in the weak version of the displayed chart:
a_i>0, t1≤...≤t_ell, d_h≥0, with some nonzero D coefficient. No source
closure operation can split an original parallel class. The same line
recovery and six-row expansion therefore exhaust **all closed-facet
preimages**, including any lower-dimensional boundary points.

Every witness has nonzero recovered a_i. If they are mixed, the tile
is absent even as a closed image. Otherwise every candidate quantity in
(1) is strictly nonzero. Thus either every inequality is positive and
the point lies in the open tile image, or some is negative and the point
is outside its closed image. None of these decisions is made on a tile
boundary.

All pivots, four-brackets, a_i and tested inequalities are continuous
rational functions near the target. Their strict signs persist on an
open neighborhood. Each row of the indicator matrix is therefore valid
on a nonempty ambient open region, not just at an isolated rational point.
The finite union of such boundary exceptions for all 176 tiles can be
avoided at once. This is what legitimizes evaluation of relations defined
only modulo sets of dimension below eight.

## 4. The exact rank certificate

Set Z_i=(1,i,i²,i³,i⁴,i⁵), i=1,...,8. All external six-minors are
strictly positive Vandermonde determinants. The bounded construction
considered 176 rational source seeds, one in each admissible cell;
one seed was rejected as nongeneric. It retained 103 indicator vectors
whose independence was first detected by exact finite-field elimination.
Every retained target is the image of its saved nonnegative source matrix.

The [complete fixture](../../fixtures/run5/indicator_kernel_n8.json) records
the external data, column labels, signed cyclic charts, source and target
matrices, all 70 nonzero four-bracket residual determinants, and all
176 membership decisions for each of the 103 targets. This is 18,128
exact indicator decisions. It also records the selected 103 columns.
The square minor on those columns has exact integer determinant 2,
independently recomputed by a separate elimination implementation.

Let A be this 103×176 integer indicator matrix. The full Run4 local
matrix has 96 rows spanning L8 of rational dimension 73; every row has
coefficient sum zero. The source-parent and all-Z image certificates are
independent inputs. Direct multiplication verifies that A annihilates
all 96 rows. Since det(A_selected)=2,

\[
 \rank A=103,\qquad \dim\ker A=73,\qquad \ker A=L_8.
\]

Let K_Z0 be the actual indicator-class kernel on the entire 176-tile
universe at this Z0. The open-neighborhood proof above gives
K_Z0⊆ker A. Run4 gives L8⊆K_Z0. Hence

\[
 K_{Z_0}=\ker A=L_8.
\]

Likewise for the uniform all-Z kernel K_all,

\[
 L_8\subseteq K_{\rm all}\subseteq K_{Z_0}=L_8.
\]

This proves K_all=L8 and D8⊆L8. A complete chamber list is unnecessary:
necessary equations of sufficient rank, together with a matching known
relation span, determine the kernel. Finite favorable agreement alone
would not have done so.

## 5. The finite unit functional and cardinality

**PROVED consequence.** The all-ones tile covector vanishes on L8, so
it lies in the row span of A. The saved rational vector lambda satisfies

\[
 A^T\lambda=\mathbf1_{176},\qquad
 \sum_{i=1}^{103}\lambda_i=20.
\]

The [exact weights](../../results/run5/unit_functional_n8.json) have
denominators at most two; thirty are negative. No positive volume or
positive atomic measure is claimed.

For any complete all-Z tiling T, its indicator vector satisfies
A*chi_T=1_103: on each witness neighborhood, remove the finitely many
tile boundaries and use multiplicity-one coverage. Since all tile
indicators are constant there, the equation holds for the recorded row.
Therefore

\[
 |T|=\mathbf1^T\chi_T=\lambda^TA\chi_T=20.
\]

Equivalently, on the finite span of these tile-indicator classes define
evaluation by the constant value on each witness neighborhood and take
the weighted sum with coefficients lambda. This is a well-defined
linear functional modulo lower-dimensional sets, assigns one to each
of the 176 tiles, and assigns twenty to the amplituhedron. It is a
neighborhood-value functional on this finite tile span, not raw point
evaluation on every constructible function modulo lower-dimensional sets.
The BCFW normalization also gives M(2,2,2)=20 independently.

This proves equal cardinality at n8 and the requested inclusion for n8.
It does not prove a uniform construction of lambda for arbitrary n,
enumerate all n8 tilings, or establish their flip connectivity. The separate
[bounded flip certificate](N8_FLIP_SPAN.md) supplies 74 genuine all-Z
tilings with a 73-dimensional difference span. It proves L8⊆D8; together
with this indicator theorem, it gives **D8=L8**.

## 6. A complete finite exact-cover model without enumeration

**PROVED, independently audited.** A binary vector chi on the 176 tiles
is a complete all-Z tiling if and only if A*chi=1_103. Necessity follows
from the open-neighborhood argument above. For sufficiency, subtract a
fixed standard BCFW tiling vector chi0. Then A*(chi−chi0)=0, so
chi−chi0 belongs to L8 and is an all-Z indicator relation. Thus the
selected tiles sum to the amplituhedron indicator modulo dimension below
eight for every positive Z.

Their nonnegative binary coefficients force open images to be disjoint:
any open overlap would contradict the indicator equality on a nonempty
open set. The finite union of their closed images contains a dense subset
of every standard BCFW open tile, and hence contains the closures of all
those tiles. It therefore covers the entire amplituhedron. Each tile
already lies inside the amplituhedron. This proves sufficiency, including
the boundary and multiplicity-one requirements.

The resulting 103-row exact-cover model is rigorous for all-Z tilings;
its equivalence is not inferred from sampled cover agreement. No claim
that its rows enumerate every chamber is needed. We stop without
exhausting its binary solutions because the complete generation and
cardinality conclusions at n8 have already been obtained. The model is
retained for future enumeration with that stopping boundary explicit.

## 7. Prior art and proof scope

**SOURCE-VERIFIED.** The 176 Yangian-invariant labels and a rank-74
space of BCFW formula vectors occur in the earlier physics literature.
Equal twenty-term formula vectors of rank 74 have a difference span of
rank 73. A later wording about 74 identities must not be silently read
as 74 independent geometric indicator relations. The exact source
comparison, including that wording issue, is preserved in
[LITERATURE_DELTA](LITERATURE_DELTA.md).

No novelty claim is made for these counts or for this finite theorem.
The present proof does not use equality of canonical forms as a geometric
relation. Its extra input is a complete indicator-membership certificate
on the entire all-Z admissible tile universe. Independent proof and
arithmetic audits, including the binary-model equivalence and bounded
flip-path inclusion, passed before promotion in the campaign status.
