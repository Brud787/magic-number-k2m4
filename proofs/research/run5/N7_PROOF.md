# Complete n=7 all-Z tilings and their parent-flip graph

**PROVED, with an exact exhaustive finite certificate.** There are precisely
seven all-Z positroid tilings of A(7,2,4), each containing six tiles. They are
exactly the seven distinct dihedral transforms of the standard BCFW tiling.
The graph of elementary replacements supplied by the seven nine-dimensional
rank-two source parents is a seven-cycle. If D7 denotes the span over Q of
all complete-tiling differences and L7 the full Run4 single-parent relation
span, then

\[
D_7=L_7,\qquad \dim D_7=\dim L_7=6.
\]

This is a finite reconstruction of the known cyclic-polytope/parity sector,
with explicit source labels and exact certificates. It is not asserted to be
a new mathematical result, an n≥8 classification, or the infinite k=2 theorem.
Galashin–Lam already state that Magic Number holds when ell=n-k-m=1, by
parity and the cyclic-polytope result. The proof below additionally records
every n=7 tiling and identifies the campaign's actual parent moves.

The files are [the implementation](../../src/magic_number/run5_n7.py),
[the tests](../../tests/test_run5_n7.py), and
[the full certificate](../../results/run5/tilings_n7.json). The local rows are
imported from [the independently built full matrix](../../results/run5/local_relation_matrix_n7.json).
Run5 preserved the 142-test baseline before adding these files.

## 1. Exact all-Z reduction and complete tile universe

**SOURCE-VERIFIED.** We use the tile/tiling convention in
[DEFINITIONS](../DEFINITIONS.md): open cell images are pairwise disjoint;
the finitely many closed tile images cover; no common-face requirement is
added. Galashin–Lam Definition 3.4 uses density of the open images, which is
equivalent to this closed coverage. Their Theorem 3.5 preserves admissibility,
pairwise compatibility, and arbitrary all-Z tilings under parity. In the
bounded affine convention b used by this repository, the dual index is

\[
b=k+f\quad\longmapsto\quad b^*=\ell+f^{-1},
\qquad (k,\ell,m,n)=(2,1,4,7).
\]

These are output shifts, not naive inversion of b. The theorem concerns
all-Z collections; it does not identify the images for independently chosen
fixed matrices Z and Z*. See [Galashin–Lam, §3, Lemma 3.2 and Theorem 3.5](https://www.math.ucla.edu/~galashin/papers/duality.pdf),
also the preserved [local text](../../literature/text/parity_duality_GL.txt).
Their Remark 3.6 identifies the dual k=1 amplituhedron with the projective
cyclic 4-polytope. The common-face subtlety is explicitly addressed in their
footnote 2; our argument only uses open interiors and needs no extra axiom.

**PROVED / COMPUTATIONALLY-VERIFIED.** Every eight-dimensional rank-two
source cell at n=7 has (q,s)=(6,6) or (7,5), by dim S=q+s−4. There are seven
of the first kind and 21 of the second, giving 28 cells. In the latter kind,
seven have one cyclic triple class and fourteen have two disjoint cyclic
adjacent pairs. A triple class has only four labels in its complement, so
the preserved class-complement incidence argument bounds its image dimension
by seven for every positive Z. These seven cannot be tiles.

Equivalently, precisely those seven labels fail the GL bound
i−2≤f(i)≤i+1. The remaining 21 labels map under parity bijectively to all
five-subsets A⊂[7]. The corresponding rank-one open source cell has positive
coordinates exactly on A; every positive 7×5 matrix has independent rows on
A, so its image is an open 4-simplex and the map is injective. GL therefore
certifies all 21 original cells as all-Z admissible. Their membership in the
preserved BCFW tilings provides a second source certificate.

This inventory is complete, not an image-rank filter. Two independent source
enumerators, cyclic parallel classes and bounded affine permutations, give
the same 28 labels. Parity inversion is checked against a rank-one label
constructed independently from its bases/necklace and by a round trip.
The certificate retains all 21 correspondences and all seven exclusions.
Call this complete all-Z tile universe U7.

## 2. A single exact matrix supplies a necessary compatibility test

Choose the dual external rows

\[
z_i=(1,i,i^2,i^3,i^4),\qquad i=1,\ldots,7.
\]

All increasing 5×5 minors are positive Vandermonde determinants. These are
exact fixed data, used solely to rule out additional all-Z collections.
Write Δ_A for the open simplex on the five labels A. We compute exactly when
Δ_A∩Δ_B is nonempty for every distinct pair A,B.

**PROVED (Gale criterion).** Put

\[
\lambda_i=\frac1{\prod_{j\ne i}(i-j)}.
\]

The kernel of the 5×7 matrix with columns z_i is precisely

\[
w_i=\lambda_i(a+bi),\qquad (a,b)\in\mathbb R^2.
\]

Indeed the elementary Lagrange interpolation coefficient identity gives
Σ_i λ_i i^r=0 for 0≤r≤5. The displayed two vectors are independent and the
matrix has rank five. In particular sign λ_i=(−1)^(i−1).

The open simplices intersect exactly when a kernel vector satisfies

\[
w_i>0\ (i\in A\setminus B),\qquad
w_i<0\ (i\in B\setminus A),\qquad
w_i=0\ (i\notin A\cup B).
\tag{1}
\]

Necessity follows by subtracting strictly positive barycentric coordinates.
Conversely, on a shared label choose coefficients
α_i=max(w_i,0)+1 and β_i=max(−w_i,0)+1; on exclusive labels use w_i or −w_i
as appropriate. They are positive and α−β=w. Their sums agree because the
first external column is one, so common normalization gives positive
barycentric coordinates for a common point. No condition is imposed on the
shared coordinates of w.

Here |A∪B| is six or seven, so (1) is decided without approximation:

* If the omitted label is r, then a+bi is a nonzero multiple of i−r.
  Therefore all prescribed signs
  sign(w_i)·sign(λ_i)·sign(i−r), on exclusive labels, must agree.
* If no label is omitted, form the ordered prescribed signs
  sign(w_i)·sign(λ_i) on the exclusive labels. A nonzero affine function
  realizes them if and only if they change at most once. A constant works
  when there is no change; otherwise a zero strictly between the two labels
  straddling the change works. Two changes are impossible for an affine
  function.

This proves both the positive and negative decisions of the pair test.
For all 126 overlapping pairs the artifact contains strictly positive
rational barycentric coordinates on both simplices with exactly equal
images. The other 84 pairs are exactly the compatibility edges.

## 3. Independent feasibility check and exhaustive clique certificate

**COMPUTATIONALLY-VERIFIED, exact rational arithmetic.** A second method
computes a kernel basis by Gaussian elimination directly on the 5×7 moment
matrix, without using the displayed λ formula. It then solves the two-variable
linear feasibility problem (1).

When there is an omitted label, its equality reduces the kernel to a line;
the signed exclusive coefficients must all have the same sign on that line.
When there is no omitted label, rescale the strict inequalities to ≥1.
The constraint normals span R², since every pair of Gale rows is independent.
Thus the feasible polyhedron is pointed; if nonempty it has a vertex.
Enumerating the exact intersections of pairs of active inequalities finds
a feasible vertex if and only if the strict problem is feasible. This gives
an independent decision for all 210 pairs, and every decision agrees.

We next enumerate maximal cliques in the resulting 21-vertex graph by two
different algorithms. Bron–Kerbosch recursively partitions maximal cliques
using a pivot. An independent increasing-label extension enumerates every
clique, retaining all nonmaximal ones, and tests maximality afterward.
It is exhaustive because a clique has a unique increasing sequence of
vertices; all its prefixes occur in the extension recursion. The resulting
numbers of cliques of sizes 0 through 6 are

\[
1,\ 21,\ 84,\ 133,\ 105,\ 42,\ 7,
\]

and no larger clique occurs. Both algorithms find the following seven
maximal cliques. A string such as 12345 denotes the five-subset simplex
support, not an original rank-two cell label; the exact inverse labels are
in the artifact.

| ID | Six simplex supports | Preserved BCFW collection |
|---|---|---|
| C00 | 12345, 12356, 12367, 13456, 13467, 14567 | n7-T06 |
| C01 | 12345, 12356, 12367, 13457, 13567, 34567 | n7-T05 |
| C02 | 12345, 12357, 12567, 13457, 23567, 34567 | n7-T04 |
| C03 | 12346, 12367, 12456, 13467, 14567, 23456 | n7-T02 |
| C04 | 12347, 12456, 12467, 14567, 23456, 23467 | n7-T01 |
| C05 | 12347, 12457, 12567, 23456, 23467, 24567 | n7-T00 |
| C06 | 12347, 12457, 12567, 23457, 23567, 34567 | n7-T03 |

## 4. Why this finite calculation proves all-Z completeness

**PROVED.** Every all-Z rank-two tiling consists of labels from U7. By GL
parity it gives an all-Z rank-one tiling, so in particular a compatible
simplex collection at the exact matrix of §2. It is therefore a clique,
contained in one of the seven maximal cliques in §3.

Each maximal clique has been mapped back to its original rank-two source
labels. Equality with one of the preserved standard-dihedral BCFW tilings
is checked literally, label for label. The BCFW tiling theorem and dihedral
symmetry prove existence for every positive external matrix. GL parity then
also proves each displayed simplex collection tiles at our chosen matrix.

A proper subset of a displayed complete collection cannot itself cover the
cyclic polytope. A missing simplex has nonempty ambient open interior; this
interior is disjoint from every other member's closed simplex, because
otherwise approximation by its open interior would contradict pairwise
open disjointness. In particular removing that simplex leaves uncovered
points. Consequently the candidate clique must be the entire maximal
clique. This proves completeness and the count of seven all-Z tilings.

The quantifier direction is essential: a fixed matrix is sufficient for
exclusion, while all-Z existence is supplied independently. No fixed-Z
compatibility or fixed-Z tiling has been promoted to an all-Z statement.
The argument also does not need a geometric parity map between two chosen
external matrices.

## 5. Genuine parent flips and generation

**PROVED / COMPUTATIONALLY-VERIFIED.** The complete source parent inventory
at n=7 has seven nine-dimensional cells. Run4 proves that each has exactly
six admissible facets and a multiplicity-one all-Z 3↔3 relation; the two
remaining source facets collapse. The full seven rows are imported with
their source-parent and geometric proof references, rather than inferred
from arbitrary canonical-form identities.

For each displayed complete tiling and each relation, the implementation
tests literal applicability: all three removed tiles occur, all three
inserted tiles are absent, and the replacement collection equals another
displayed complete tiling. Thus the saved edges represent actual flips
inside complete all-Z tilings. They are precisely

\[
C00-C01-C02-C06-C05-C04-C03-C00.
\]

Every one of the seven parent relations occurs on one of these seven edges.
The graph of these elementary single-parent flips is C7 and is connected.
This graph specification matters: permitting an arbitrary whole-tiling
replacement as an edge would define a different graph.

Orient an edge and subtract its endpoint incidence vectors in Q^U7. Its
vector is the corresponding primitive local row up to sign. Hence every
generator of L7 belongs to D7. Conversely, telescoping along a cycle path
expresses every pair of complete-tiling incidence vectors as a sum of
applicable edge differences. Completeness of §4 gives D7⊆L7. Therefore
D7=L7, independently of the numerical rank calculation.

Exact Fraction elimination and independent SymPy elimination give rank six
for the seven local rows, rank six for all 21 pair differences, and rank six
for the stacked matrix. The free space on U7 modulo this local span has
dimension 21−6=15. This dimension is not presented as a computation of a
larger, unspecified arbitrary-indicator quotient.

Each local row has three +1 and three −1 coefficients. Connectedness thus
also recovers six tiles in every complete tiling. This finite generation
theorem uses the established completeness of §4; it does not extrapolate
single-parent generation to n≥8.

## 6. Hostile gates and scope

**PROVED.** The admissible universe is complete, all simplex-pair decisions
are exact, and both compatibility and clique enumeration have independent
implementations. Every all-Z existence claim comes from a source theorem;
every flip edge is an applicable geometric replacement. All seven excluded
cells have all-Z image dimension below eight. No degree-two cell or spurion
occurs at n=7; their absence follows from the complete source inventory,
not an assumption that arbitrary tiles are BCFW.

**SOURCE-VERIFIED.** This sector was already accessible through
Galashin–Lam parity and cyclic-polytope triangulations; their §3 explicitly
records Magic Number for ell=1. The contribution here is a reproducible
complete finite fixture and an exact identification of D7 and the campaign's
Run4 parent span. No novelty claim is made, and neither all n≥8 tilings nor
the full k=2 Magic Number conjecture is settled here.
