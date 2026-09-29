# Complete positive inversion of the (3,3,3) spurion

**PROVED, using the independently source-verified all-Z spurion injectivity
theorem.** The open spurion has a complete rational inverse obtained from
one 8×9 linear kernel. A strict sign decision in that inverse, together
with explicitly checked rank gates, certifies either membership in the
open tile or nonmembership in its closed image. Every such decision holds
on an ambient open target neighborhood. There is no unexamined real or
row-gauge branch.

The same proof applies to the three-direction eight-cell profiles (1,4,4)
and (2,3,4), with their permutations, using their preserved all-Z BCFW
injectivity certificates. It does not classify a source from a sampled
rank. The two-direction (5,5) case instead belongs to the separate
complement-five inverse.

The [implementation](../../src/magic_number/run6_spurion_inverse.py)
provides `prepare_spurion(cell,z)` and `inversion(chart,y)` for the Run6
indicator pipeline. The broader `prepare_three_class` accepts the three
admissible profiles above. The [fixture](../../fixtures/run6/spurion_inverse.json)
and [tests](../../tests/test_run6_spurion_inverse.py) are exact regressions
of this proof; they are not its all-Z premise. No prior fixture or source
file is modified.

## 1. Entire positive source chart and its unique gauge

Let the ordered nonloop classes be A,B,D, with three labels each for the
spurion. Delete loops and make a signed cyclic cut at a class boundary.
Write E for the resulting positive 9×6 external matrix. Every point in the
open source cell has a representative

\[
C(x)=\begin{pmatrix}
 a_1&a_2&a_3&b_1&b_2&b_3&0&0&0\\
 0&0&0&b_1&b_2&b_3&d_1&d_2&d_3
\end{pmatrix},\qquad x=(a,b,d)>0,
\tag{1}
\]

unique up to a common positive scalar. Indeed a projectivity sends three
distinct cyclically ordered column directions to horizontal, diagonal,
and vertical. Positive ordered two-minors then force the displayed
coefficients to have one common sign; choose that sign positive. A row
change preserving the two axis directions is diagonal, and preserving
the diagonal direction makes it scalar. This proves both coverage of the
whole positive source and uniqueness of the projective coordinates.

For the other profiles replace each group of three by its actual class
size. There are still nine coefficients because the support has size nine;
three projective directions leave dimension eight. No cross-ratio or
additional order inequality remains in a three-direction chart.

**SOURCE-VERIFIED input.** The source (3,3,3) is the published all-Z
injective spurion; see the preserved [source audit](../SPURION.md) and
*A cluster of results on amplituhedron tiles*, §§5.1–5.3. The other two
profiles have the preserved BCFW certificates. This input is used below
to exclude a positive rank-deficient fiber, not inferred from the new
inverse or from generic degree.

## 2. All positive fibers are linear projective cones

Let Y be any rank-two target plane and choose an exact 6×4 basis Q of
null(Y). Set e_i=E_i Q. The two image rows of (1) are contained in Y
exactly when

\[
M_Yx=0,\qquad
M_Y=\big[(e_i,0)_{i\in A},\ (e_i,e_i)_{i\in B},\ (0,e_i)_{i\in D}\big].
\tag{2}
\]

Here columns are displayed in R4⊕R4, and M_Y has size 8×9. For x>0,
C(x) is nonnegative and rank two. Positive external data preserves its
rank, so containment of both image rows in Y implies equality of the
image plane. Conversely every positive source preimage has chart (1),
so (2) describes the entire positive fiber, not just a local branch.

**PROVED.** At every point in the open tile image, rank M_Y=8. If rank
were at most seven, its kernel would contain a vector independent of a
positive preimage x. Adding sufficiently small positive or negative real
multiples of that vector keeps all nine coordinates positive. Projective
gauge uniqueness gives distinct source row spaces, and (2) gives the same
image plane. This contradicts the independent all-Z injectivity input.

When rank M_Y=8, choose any nonzero maximal minor. The kernel line has
rational coordinates, equivalently the signed cofactors

\[
\kappa_i=(-1)^i\det(M_Y\text{ with column }i\text{ removed}),
\qquad i=0,\ldots,8.
\]

The implementation uses one exact row reduction instead of nine determinant
computations. It records the eight pivot columns, their exact nonzero
minor, the free coordinate normalized to one, and the resulting kernel
vector. The open inverse is complete:

\[
Y\in T^\circ\iff
\operatorname{rank}M_Y=8\ \text{and the kernel coordinates have one strict common sign}.
\tag{3}
\]

For a positive answer, use the positive representative of the kernel in
(1). A rank-deficient M_Y excludes open membership by the preceding
injectivity argument. A zero kernel coordinate or mixed signs excludes
open membership directly by the complete chart. These exclusions alone
do not decide every closed-boundary case; that issue is treated next.

All statements concern real fibers. No use is made of complex algebraic
degree, Jacobian rank as an admissibility test, or a selected target frame
orientation. Replacing Y's frame leaves its nullspace unchanged. Replacing
Q by another quotient basis multiplies M_Y on the left by two copies of
an invertible matrix; its kernel is unchanged.

## 3. Closed-source branches and the rank gates

The closure of the source retains the within-class zero minors and all
loops. Thus original classes can lose columns or merge, but cannot split.
Consider a rank-two source point in this closure.

If all three original classes survive with distinct directions, the point
has chart (1) with nonnegative coefficients and a nonzero coefficient in
each group. It is therefore included in the weak version of (2).

Every other closed-source point has at most two surviving directions.
If all three original classes survive, at least two have merged; one of
the two directions is supported entirely in a single original class.
If an entire original class vanishes, rank two forces the surviving
directions to be supported in the two remaining original classes. In
either case, a nonzero row of a suitable source representative has support
in one original class. Rank preservation gives a nonzero image vector in
the external space of that class. Hence

\[
Y\cap W_G\ne0\quad\text{for some }G\in\{A,B,D\},
\qquad W_G=\operatorname{span}\{E_i:i\in G\}.
\tag{4}
\]

This argument includes all cyclic merger orientations, whole-block
deletions, and lower strata within those cases. It does not assume the
closed chart is merely a coordinate orthant.

The strict inverse checks

\[
\operatorname{rank}\begin{pmatrix}Y\\E_G\end{pmatrix}=2+|G|,
\qquad G=A,B,D.
\tag{5}
\]

For the spurion these are three rank-five tests. Every external block is
independent, so (5) is equivalent to Y∩W_G=0, and excludes all missing
gauges in (4). The implementation saves a nonzero square minor for each
test. The pipeline's stronger condition that all external four-label
twistors are nonzero implies (5): any nonzero intersection with W_G,
where |G|≤4, would force a zero twistor after extending G to four labels.
The inverse checks (5) itself, so no hidden genericity promise is required.

There is also a useful redundancy: if rank M_Y=8 and every kernel
coordinate is nonzero, then (5) already follows. A nonzero vector in
Y∩W_G would give a kernel vector supported only on G, by (2) and external
block independence, contradicting the unique kernel line having all
nine coordinates nonzero. In particular the rank gates do not discard
any open tile point. Their explicit minors make the closure and openness
certificate directly reviewable.

Assume now that rank M_Y=8, every kernel coordinate is nonzero, and (5)
holds. Every possible closed preimage must be in the weak three-direction
chart. Its coefficient vector would be a nonnegative representative of
the unique kernel line. Therefore exactly one of the following holds:

* All kernel coordinates have one sign: Y belongs to the open tile.
* The kernel has mixed strict signs: Y is outside the **closed** tile.

This establishes the claimed strict closed-indicator decision. A zero
kernel coordinate, rank drop, or failed gate is returned as `None` by
`inversion`; it is not silently interpreted as closed nonmembership.

## 4. A full semialgebraic description on the exceptional strata

For completeness, closed membership even on the exceptional locus has
the following finite description. In cut order A,B,D, take the four
source patterns

\[
\begin{array}{c|ccc}
 &A&B&D\\\hline
C_3&(a,0)&(b,b)&(0,d)\\
C_{AB}&(a,0)&(b,0)&(0,d)\\
C_{BD}&(a,0)&(0,b)&(0,d)\\
C_{DA}&(a,0)&(0,b)&(-d,0).
\end{array}
\]

Every displayed coefficient a,b,d is coordinatewise nonnegative. Impose
rank C_sigma=2 and C_sigma E Q=0. Then

\[
Y\in T\iff
\text{one of these four systems has a solution}.
\tag{6}
\]

Necessity is the complete closure classification above. Sufficiency
follows because each pattern is a nonnegative rank-two source in closure(S)
(its allowed bases are a subset of those of S), and positive external
data preserves rank. The minus sign in the last pattern is required for
the cyclic A/D merger: it makes both A–B and B–D ordered minors positive.

This is a finite union of linear feasibility problems with weak and strict
inequalities. In C3, rank two means at least two of the three group sums
are strictly positive; split into three alternatives. In each merger
pattern it means that both direction-group sums are strictly positive.
One may additionally normalize the total coefficient sum to one.
For rational Y,E, any feasible system has rational witnesses. Formula
(6) is an exact semialgebraic description, not a sampled boundary test.
The implementation used for the indicator pipeline deliberately takes
the faster strict branch of §3; it does not advertise a solver for all
the exceptional systems in (6).

## 5. Open persistence and the modulo-dimension gate

At a returned strict certificate, the target two-column pivot, the
8×8 fiber pivot, and the three block-rank minors are nonzero. Fix those
same pivots in a neighborhood. The quotient, normalized kernel, and
gate minors are rational continuous functions there. The nine nonzero
kernel signs persist, so the same indicator value holds on a nonempty
ambient open neighborhood in Gr(2,6).

Consequently a constant-coefficient relation of tile indicators modulo
sets of dimension at most seven must annihilate any complete witness
row containing this spurion certificate. Its exceptional set cannot
contain that open neighborhood. This is the exact purpose of the strict
inverse in the n=9 kernel computation. A value at an isolated rational
target would not suffice.

## 6. Cyclic, reflection, and zero-insertion transport

The cut uses each nonloop label exactly once in cyclic order. A column
crossing the cut gets a minus sign in both source and external data,
so the product is unchanged. For any selected six external rows, moving
r crossed labels from the end to the beginning contributes
(−1)^(r(6−r)), and their individual row signs contribute (−1)^r.
Their product is +1. The corresponding two-row character is also +1.
Thus all increasing maximal external minors and source two-minor signs
are preserved. The implementation reconstructs the original source by
undoing precisely these signs and retaining every loop as a zero column.

For ordinary reversal J of the labels, choose an ambient G with det G<0
and the source row-swap H. Then Z'=JZG has positive increasing six-minors,
since reversal of six rows has sign −1. Also C'=HCJ is nonnegative,
because source row swap and reversal each reverse two-minor sign. The
identity C'Z'=HCZG transports the whole image and closure. A reversal of
the three blocks swaps the first and last directions; the positive chart
has the same form. Cyclic cuts after this reversal are already covered.

An increasing support embedding simply selects the corresponding rows
of a positive external matrix. Those rows remain positive, and inserted
source columns are zero. The inverse therefore applies to all cyclic,
reflected, and zero-inserted spurion labels with the same proof. No
fixed-matrix symmetry is mistaken for a theorem at every Z.

## 7. Independent verification and remaining scope

The tests solve the twelve ambient equations C(x)E=HY with four unknown
row-change entries, independently of the producer's quotient basis and
Fraction elimination. They compare the unique nine-coordinate kernel,
verify all original ordered source minors, independently recompute every
saved determinant, exercise all nine coordinate facets and three merger
gauges, test signed cyclic/loop transport, and compare with the published
spurion functionary regression.

**PROVED scope.** Complete positive inversion for these certified
three-direction tiles, and exact strict closed-indicator certificates.
This theorem neither identifies a canonical form nor proves any new
tiling relation or full kernel rank by itself. The subsequent rank
argument must still account for every other admissible tile and verify
its own exact determinant certificate.
