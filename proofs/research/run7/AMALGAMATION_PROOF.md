# Adjacent amalgamation and exact generic indicator degeneration

**PROVED, independently audited in Run7.** For k=2,m=4, adjacent-column
amalgamation, retaining only admissible eight-dimensional image source
cells, sends all-Z tile-indicator relations to all-Z tile-indicator
relations. It also sends every complete all-Z tiling to a complete all-Z
tiling downstairs, after coefficients are first retained as multiplicities.
It sends the complete local parent span into the corresponding downstairs
span. The geometric statements hold for every n≥7, so the downstairs
amplituhedron has at least six labels. Algebraically V_n=0 for n<6 and
all faces out of V_6 are zero; this supplies the remaining simplicial
cutoff. No generation of arbitrary relations is assumed or concluded in
this document.

The preserved [complete tile-core classification](../run6/MEMBERSHIP_CORES.md)
and [complete local parent theorem](../run4/LOCAL_PARENT_THEOREM.md) are
inputs. In particular, the noninjective four-mass cell is not treated as a
tile. All indicator identities below are modulo semialgebraic sets of
dimension at most seven; coefficients do not depend on Z.

## 1. Exact source map

Assume n≥7 and put N=n−1. For an ordinary last adjacent pair define

\[
 F(C)=(c_1,\ldots,c_{n-2},c_{n-1}+c_n).
 \tag{1}
\]

This is a map of row spaces wherever its matrix has rank two. Write a,b
for the last pair and w=a+b. All its ordered minors are either retained
source minors or

\[
 \Delta_{i,w}=\Delta_{i,n-1}+\Delta_{i,n}\quad(i<n-1).
 \tag{2}
\]

There is no cancellation. Thus on each positive source cell S the output
has one fixed rank-two positroid label S′, determined by the union of bases
under merging the two labels. For the cells of dimensions eight and nine
used here it has rank two everywhere. In fact rank loss on the entire
nonnegative Grassmannian occurs at exactly one point: the coordinate
two-plane supported on {n−1,n}. To see this, rank loss makes all minors in
(2) zero, hence makes each of their two nonnegative summands zero. If any
outside column were nonzero, every other column would be parallel to it,
contradicting source rank two. Therefore every outside column is zero.
At that coordinate plane a,b are independent, so w is nonzero and the
output has rank one, not rank zero.

The map is onto the entire cell S′. The following table gives its dimension
and positive fibers; q is the nonloop support size and s the number of
cyclic parallel classes. Recall dim S=q+s−4.

| Last pair in S | Output (q′,s′) | Positive fiber dimension |
|---|---|---:|
| At least one loop | (q,s) | 0 |
| Same nonloop class | (q−1,s) | 1 |
| Distinct classes, both nonsingleton | (q−1,s+1) | 0 |
| Distinct classes, exactly one singleton | (q−1,s) | 1 |
| Two distinct singleton classes | (q−1,s−1) | 2 |

Here and below the rank-two exceptions with too little support are omitted
from a table intended for dim S≥8. A loop is inserted or removed uniquely.
In the same-class case a=t w,b=(1−t)w with 0<t<1. In the two-nonsingleton
case the remaining columns determine both distinct projective directions;
the new singleton direction is strictly between them in cyclic order.
Decomposing w in these two directions gives the unique positive inverse.
This inverse is rational, since it solves a nonsingular two-by-two system.
For precision, if u,v are raw remaining columns in the respective classes,

\[
 a=\frac{\det(w,v)}{\det(u,v)}u,\qquad
 b=\frac{\det(u,w)}{\det(u,v)}v.
 \tag{3}
\]

The cyclic sign convention is essential. When the last class wraps through
label 1, its raw early columns point opposite to its raw final columns.
Consequently the second coefficient in (3) is negative in that raw gauge;
the inverse is positive relative to the signed cyclic class rays. Ordered
minors, or equivalently the new singleton's position between these rays,
prove that (3) gives exactly S. There is no negative or second inverse
branch in the positive source cell.

For exactly one singleton, split w into the surviving class direction and
the remaining column. If the final class is singleton, take a=t u and
b=w−t u; if the penultimate class is singleton and the final class has an
early residual vector v, take b=−t v and a=w+t v. All required inequalities
are linear in t. They hold for sufficiently small positive t, and define
a nonempty open interval. For two singleton classes choose any outside
column v, with det(v,w)>0. For 0<t<1 put

\[
 a=t w+\epsilon v,\qquad b=(1-t)w-\epsilon v.
\]

For sufficiently small positive epsilon all outside ordered minors remain
positive and det(a,b)=epsilon det(v,w)>0. The full fiber is the nonempty
open region in a∈R² defined by the linear conditions on a,w−a and
det(a,w)>0. This proves surjectivity and the displayed dimension, rather
than merely identifying a necessary zero pattern.

Thus whenever dim S′=dim S≥8, (1) is a positive rational source-cell
isomorphism. In every other case source dimension decreases. Images of
proper source boundaries under (1), where rank two is retained, belong
to closure(S′), by continuity and approximation from S.

## 2. Which full-dimensional outputs may be discarded

Let U_n be the complete set of all-Z admissible eight-dimensional source
cells, and V_n its free real vector space. Define

\[
 \pi(e_S)=\begin{cases}e_{S′},&S′\in U_N,\\0,&\text{otherwise}.\end{cases}
 \tag{4}
\]

The image source label is computed before this truncation. If dim S′<8,
its image under any positive W has dimension at most seven. If dim S′=8
but S′ is not admissible, its image again has dimension at most seven
for every positive W. Here is why the second statement does not silently
discard a degree-two cover.

A dimension-preserving nonloop amalgamation creates a singleton class.
It therefore cannot produce the only noncollapsed excluded eight-cell,
the four-mass profile (2,2,2,2). A loop case preserves the admissible core.
By the complete Run6 classification, every remaining excluded output has
a parallel class with at most four complementary nonloop labels. Its
image is in the corresponding Schubert incidence locus of dimension at
most seven. Equivalently, the only output profiles that actually occur
in this excluded case are (3,1,1,1,1) and (4,2,1,1), arising respectively
from merging the two size-two classes of (3,2,2,1), or the size-two and
size-three classes of (2,3,4). These statements concern complete source
types and all positive external matrices.

The closure of each discarded image also has dimension at most seven:
the positive amplituhedron map is continuous on the compact nonnegative
source Grassmannian, so image(closure S′)=closure(image S′).

## 3. A positive external degeneration for every downstairs matrix

Fix an arbitrary positive N×6 matrix W. Retain its first N rows and append

\[
 Z_n(\epsilon)=W_N-\epsilon W_{N-1}+\epsilon^2W_{N-2}
 -\cdots+(-\epsilon)^{N-1}W_1.
 \tag{5}
\]

Then Z(epsilon) is positive for all sufficiently small epsilon>0. Indeed
consider a six-minor containing the new last row and five old rows I.
Let r be the smallest nonnegative integer for which N−r is not in I.
Its first nonzero term is

\[
 (-1)^r\epsilon^r\det(W_I,W_{N-r}).
\]

Exactly r rows of I exceed N−r, so sorting the determinant supplies
another factor (−1)^r. The leading coefficient is a strictly positive
increasing six-minor of W. There are finitely many minors and r≤5, so
a common positive upper bound on epsilon works. Minors not involving
the appended row are already strictly positive. At epsilon=0 the last
two external rows coincide and

\[
 C Z(0)=F(C)W.
 \tag{6}
\]

Only positive epsilon is used when applying an all-Z identity. The
degenerate matrix itself is used to calculate the limit and its regular
source branches.

## 4. Compactness and every possible escape through rank loss

For a source cell S let T_S(Z)=f_Z(closure S). Consider any epsilon_l→0
and C_l∈closure S with target planes f_(Z(epsilon_l))(C_l)→Y. Compactness
gives a subsequence C_l→C_0. If F(C_0) has rank two, its image under the
positive W has rank two, and (6) gives

\[
 Y\in f_W(\overline{S′}).
\]

If F(C_0) has rank one, Section 1 says C_0 is precisely the coordinate
plane on the last pair. Choose continuous source frames near that point
converging to the two coordinate rows. Their two image rows converge to
W_N. Since W_N is nonzero and lies in the limit of the target planes,
W_N∈Y. This argument allows arbitrary relative rates of epsilon_l and
C_l approaching the boundary. Hence

\[
 \limsup_{\epsilon\downarrow0}T_S(Z(\epsilon))
 \subseteq f_W(\overline{S′})\cup\Sigma_W,
 \qquad
 \Sigma_W=\{Y:W_N\in Y\},\quad\dim\Sigma_W=4.
 \tag{7}
\]

In particular if Y is outside the closed right side, there is an open
neighborhood O of Y and epsilon_0>0 such that O is disjoint from the
upstairs closed tile for every 0<epsilon<epsilon_0. Otherwise a sequence
of counterexamples would contradict (7). This is a strict closed
nonmembership statement, not a comparison of rational canonical forms.

## 5. Strict generic indicators, with multiplicity retained

Fix W. For each surviving S′, exclude the image of its proper source
boundary and the critical values of f_W restricted to S′. Both are
semialgebraic sets of dimension at most seven. For critical values this
follows from the rank theorem/Sard's theorem in semialgebraic charts;
the map is analytic and injective on an eight-cell, so invariance of
domain gives an open image and its differential cannot have rank below
eight everywhere. Exclude also every discarded closed image from Section
2, including all outputs of source dimension below eight as well as all
collapsed eight-dimensional outputs, and Sigma_W. There are finitely many source labels for fixed n, so the
union E_W still has dimension at most seven.

At Y outside E_W in f_W(S′), the source map F:S→S′ is the positive
rational isomorphism of Section 1. Its unique inverse source C lies in
the open S, and f_(Z(0))|S=f_W F has nonsingular differential at C.
The parameter-dependent inverse function theorem in source and target
charts therefore gives a common neighborhood O of Y and epsilon_0>0
such that every point of O is in f_(Z(epsilon))(S) for all sufficiently
small positive epsilon. Positivity is strict at C and persists. At a
point outside f_W(closure S′), Section 4 gives the opposite strict
conclusion. Once boundary images have been excluded these are all cases.
For discarded outputs Section 4 applies everywhere outside E_W.

After taking finite intersections of neighborhoods, all tile decisions
hold simultaneously. Explicitly, for each Y outside E_W there are O and
epsilon_0 on which

\[
 \mathbf1_{T_S(Z(\epsilon))}(Y')
   =\mathbf1_{T_{\pi S}(W)}(Y')
 \quad(Y'\in O, 0<\epsilon<\epsilon_0, S\in U_n),
 \tag{8}
\]

where the right side is zero for pi S=0. This is generic strict indicator
degeneration for the complete admissible universe, not just BCFW cells.
If several source tiles have the same nonzero image label, their separate
indicators in (8) must be added with their separate coefficients.

For the entire amplituhedron, every downstairs source has an upstairs
source obtained by inserting a zero final column, with exactly the same
image for every epsilon. Thus A_N(W)⊆A_n(Z(epsilon)) without a limiting
argument. The compactness argument on the entire source Grassmannian
gives the reverse generic limit outside Sigma_W. Excluding the boundary
of A_N(W), of dimension at most seven, makes this strict on neighborhoods
as well. The standard BCFW tiling, or its open tile images with their
lower-dimensional source boundaries, supplies this boundary bound and
the density of the interior. It follows that the amplitude indicator
also obeys (8) with A in place of S.

## 6. Transport of all-Z relations and complete tilings

Let K_n be the kernel of all-Z tile indicators modulo dimension at most
seven, with constant real coefficients. **Then pi K_n⊆K_N.** Fix W and
c∈K_n. At a point outside the finite exceptional set in Section 5, (8)
gives an open neighborhood where all indicators, and hence their linear
combination, have a constant eventual value. For each sufficiently small
positive epsilon the upstairs relation is zero off a set of dimension
at most seven. A nonzero constant value on this open neighborhood is
impossible. Therefore the downstairs combination vanishes away from a
set of dimension at most seven. W was arbitrary. This argument does not
assume that a chosen point avoids exceptional sets depending on epsilon;
the open neighborhood is what makes the implication valid.

Now let T be a complete all-Z tiling and let b be its binary source-label
vector. Apply the same argument to

\[
 \sum_{S\in T}\mathbf1_{T_S(Z)}=\mathbf1_{A_n(Z)}.
\]

The output pi b initially has nonnegative integer coefficients, and the
downstairs sum equals the amplitude indicator generically for every W.
No coefficient can exceed one: an admissible tile has a nonempty open
image, and a repeated coefficient would make the sum at least two there.
The same open-set argument excludes intersections between the open images
of distinct selected tiles. Their closed images lie inside A_N(W).
Their finite closed union contains its dense generic subset, so it covers
all of A_N(W). Thus pi b is a binary vector and specifies a complete
all-Z tiling. Lower-dimensional common boundaries are retained in this
closed coverage assertion. Multiplicity one is a consequence, not an
input to the degeneration.

## 7. Uniform preservation of the full local parent span

Let L_n be the span of all signed dihedral and loop transports of the
fifteen nonzero Run4 parent prototypes. Consider a generator r supported
on admissible eight-dimensional facets of one nine-dimensional parent P.
Let P′ be its exact image source cell under (1). The map is defined on
P and on all its eight-dimensional facets; Section 1 gives their exact
image cells and their closure incidences.

If dim P′=9, F:P→P′ is a positive rational isomorphism. Every nonzero
image of a participating facet is an eight-dimensional cell in closure
P′, hence a codimension-one positroid facet. Consequently pi r is an
all-Z relation supported on the admissible facets of P′, by Section 6.
The complete local parent theorem puts it in L_N, including the case
where that theorem gives the zero relation space.

If dim P′=8, every surviving eight-dimensional facet image must equal
P′: closure incidence between distinct positroid cells strictly lowers
dimension. If P′ is not admissible there are no surviving terms. Otherwise
pi r is a scalar multiple of its single tile indicator. Section 6 and
the tile's nonempty open image force that scalar to be zero. If dim P′≤7
every term is zero by the same dimension and closure-incidence argument.
This proves

\[
 \pi L_n\subseteq L_N.
 \tag{9}
\]

This deduction uses the already complete one-parent relation theorem;
it does not assume global generation K_n=L_n. The independent Run7
finite matrix checks at n8 and n9 verify actual signed coefficients,
rather than replacing the proof of (9).

## 8. Other adjacent positions, splitting, and limits of this result

For any ordinary adjacent pair use the matching signed cyclic action to
move it to the last pair and transport the argument back. The wrap face
uses (c_1−c_n,c_2,...,c_(n−1)); its sign follows from the rank-two cyclic
action. The matching rank-six signed cyclic action on external data
preserves positivity and intertwines every map, so all preceding claims
hold for that face as well. Zero insertion is an exact map on source
closures and external row restrictions. It sends K_N into K_n and L_N
into L_n, with the corresponding amalgamation as a left inverse. The
positive extension input is needed when interpreting an all-Z assertion
in both directions, and is already proved in the preserved transport
lemmas.

The companion [simplicial proof](SIMPLICIAL_AMALGAMATION.md) checks every
identity and the nonadmissible truncation. Neither a description of the
kernel of an individual quotient map nor an all-n generation theorem
follows just from surjectivity or splitting. Those require additional
arguments, separately audited.

**Independent review.** The separate Run7 deletion/structural agent read
Sections 1–8 and checked the cyclic source inverse, every rank-loss limit,
the arbitrary-W positive degeneration, the open-neighborhood treatment of
varying exceptional sets, multiplicity-one promotion, and the one-parent
local-span descent. The review found no mathematical gap. Its requested
clarification that all source-dimension-drop outputs enter E_W is included
in Section 5. The parent agent's final Run7 review records the overall
dependency audit; no larger conclusion is needed by this document.
