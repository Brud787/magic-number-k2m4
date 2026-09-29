# The complete local rank-two parent theorem

**PROVED, independently audited.** For k=2,m=4 and arbitrary n, every
constant-coefficient all-Z indicator relation supported on the admissible
codimension-one source facets of a single nine-dimensional positroid parent
is balanced. More precisely, the complete relation space for each parent
is either zero or the one-dimensional span of a primitive balanced 3↔3
or 5↔5 vector. The 29 loopless core cases are all accounted for below.

This is a local theorem. It neither asserts generation of arbitrary tile
relations by parent relations nor proves the Magic Number Conjecture.
No novelty claim is made. The targeted primary-source comparison is in
[FINAL_SCOPE_REVIEW](FINAL_SCOPE_REVIEW.md).

## 1. Exact statement and conventions

Let P be a nine-dimensional positroid cell in Gr^≥0(2,n), n≥7. For each
positive n×6 external matrix Z let f_Z(C)=CZ, interpreted on row spaces.
Write

\[
\mathcal F(P)=\{S:\dim S=8,\ S\lessdot P,\ 
 f_Z|_S\text{ is injective for every positive }Z\}.
\]

These are source facets. Every indexed cell is a genuine all-Z tile map;
dimension or generic differential rank alone does not define this set.
It is a fixed set of source labels independent of Z. Put
T_S(Z)=closure(f_Z(S))=f_Z(closure(S)), and define

\[
\mathcal R_{\rm all}(P)=\left\{c\in\mathbb R^{\mathcal F(P)}:
 \text{for every positive }Z,\quad
 \sum_{S\in\mathcal F(P)}c_S\mathbf1_{T_S(Z)}=0
 \pmod{\text{semialgebraic sets of dimension}<8}\right\}.
\]

The coefficients are independent of both Y and Z. The exceptional set
may depend on Z. Replacing closed tile indicators by open cell-image
indicators does not change this space: the difference is contained in
images of proper source-boundary strata of dimension at most seven.
Compactness of source closures and continuity give the displayed closed
image identity.

**Theorem.** There are precisely the following four sectors, with core
types understood up to increasing loop deletion and dihedral relabeling.

| Sector | Core types | Admissible facets | Complete all-Z relation space |
|---|---:|---:|---|
| Collapsed parent image | 12 | 0 | Zero |
| Complement-five circuit | 10 | 6 | R·epsilon, three +1 and three −1 |
| Reflection or repaired spurion | 5 | 10 | R·epsilon, five +1 and five −1 |
| Hostile four-mass parents | 2 | 8 | Zero |

For every parent in either balanced sector, the positive and negative
facet collections are two multiplicity-one all-Z tilings of the closed
parent image, with disjoint open images within each side. All their
coefficients are geometric image-side coefficients. Consequently

\[
 c\in\mathcal R_{\rm all}(P)\quad\Longrightarrow\quad
 \sum_{S\in\mathcal F(P)}c_S=0.
\]

The twelve collapsed parents have image dimension at most seven for
every positive Z. The seventeen others have image dimension eight for
every positive Z. The latter assertion also follows directly from any
one of their certified facet tiles: its eight-dimensional image lies
in closure(f_Z(P)), and semialgebraic dimension is unchanged by closure.

## 2. Complete source and admissibility accounting

**PROVED / COMPUTATIONALLY-VERIFIED.** The classical rank-two source
description gives dim(P)=q+s−4, with q nonloop labels and s cyclic
parallel classes. Thus q+s=13, and the only support/class pairs are
(7,6),(8,5),(9,4),(10,3),(11,2). Choosing s cyclic cuts gives respectively
7,56,126,120,55 labeled loopless parents. Positive compositions up to
cyclic rotation and reversal give respectively 1,5,10,8,5 core types.
This is the preserved independently checked Run3 source enumeration,
not a new enumeration of complete tilings.

The [complete table](CORE_TABLE.md) retains every source facet and its
admissibility certificate. All facets are either certified all-Z tiles,
have the class-complement image-dimension obstruction, or are certified
noninjective four-mass cells. There are no undecided facet types. Source
incidence, affine permutations, necklaces and bases are retained in the
machine records. The concrete prototypes in the proofs are matched to
the preserved inventory by explicit dihedral actions, tested on every
participating facet.

If a parallel class has t≤4 nonloop labels outside it, annihilating its
projective direction gives a nonzero image vector in the fixed external
t-space. Planes meeting this space belong to an incidence locus of
dimension at most (t−1)+4≤7. Positive Z preserves rank on the nonnegative
Grassmannian, so the vector cannot vanish. This proves the twelve parent
collapses and every collapsed facet assertion in the table. A collapsed
parent cannot contain an admissible eight-dimensional facet image.

For the other facets the source certificates are the general BCFW
injectivity theorem, the published spurion injectivity theorem, direct
hyperplane/fiber inversion where supplied here, and the preserved exact
four-mass noninjectivity certificates. Four-mass positive multiplicities
are never replaced by complex algebraic degrees.

## 3. Existence and balancedness of the fifteen geometric relations

**PROVED.** Ten cores have a parallel class with exactly five nonloop
labels outside it. The [complement-five theorem](SMALLER_CORES.md) supplies
a complete source chart, the uniquely recovered positive hyperplane
intersection ray, and the entire affine positive fiber. Compressing its
successive complementary classes gives a positive 7×6 matrix. Its Gale
coefficients alternate by complementary maximal minors. The six actual
wall functions are consecutive slope differences and distinguished-class
coefficients. Their six inward derivatives alternate in sign.

Direct inversion certifies all six walls. The full positive fiber is a
bounded interval with generic endpoints in two distinct open walls.
Lower source strata have image dimension below eight, and the positive
hyperplane functional excludes rank-one endpoint loss. Endpoint
uniqueness, open tile images and compact closures prove the two side
decompositions. The explicit derivatives prove the 3+3 wall-type count;
the interval alone would not do so. The independent [merger proof](MERGER_WALLS.md)
resolves the formerly hidden rank-two (5,5) wall in (1,4,5) and (2,3,5).

Four cores have a genuine orientation-reversing source reflection:
(1,2,1,2,2), (1,3,2,3), (2,4,4), (3,3,4). Complete linear orthant
fiber charts, globally nonzero pivots, independent wall admissibility,
and lower-dimensional exceptional-limit bounds establish their geometric
relations before reflection is used to count wall types. Each reflection
has five source-coordinate transpositions and preserves the target
Grassmannian orientation, so it pairs all ten transverse walls with
opposite image signs. The (3,3,4) parent has four spurion facets, paired
in two opposite-sign pairs. See [q10 proofs](Q10_334.md),
[q9 reflection](SMALLER_CORES.md), and the preserved
[Run3 q8 proof](../run3/LARGER_SUPPORT.md).

The remaining balanced core (1,2,3,3) is the independently certified
repaired spurion parent. Its positive interval proof gives the geometric
relation, while its separate ordered-minor/Plucker computation gives
the wall-type sum 0+2−1−1=0. The literal printed common-parent discrepancy
and the absence of a certified embedding into the printed complete
tiling remain unchanged. See [Run2 proof](../run2/SPURION_ATTEMPT.md) and
[Run3 sign mechanism](../run3/SPURION_SIGN_MECHANISM.md).

## 4. Why these are the entire local relation spaces

Exhibiting a balanced relation is insufficient to establish the theorem.
The additional argument uses exact open overlaps.

**PROVED.** For a known two-sided multiplicity-one facet decomposition,
an open overlap of opposite-side tiles i,j forces c_i+c_j=0 in any
indicator relation. Same-side disjointness excludes all other open
tiles there. Removing the finitely many lower-dimensional boundary
images and the exceptional set of the proposed relation leaves a
nonempty subset on which to evaluate it. A connected overlap graph
therefore forces c to be a scalar multiple of the known sign vector.
The known relation supplies the reverse inclusion.

For each of the ten circuit cores, a symbolic construction realizes all
nine cross-sign pairs for **every** positive Z. The six free positive
inequality values can be chosen so that any prescribed positive wall
is the unique endpoint at tau=−1 and any prescribed negative wall the
unique endpoint at tau=+1. This proves a K3,3 overlap graph and the
one-dimensional relation space at each fixed positive Z. The construction
and independent audit are in [SIGN_MECHANISMS](SIGN_MECHANISMS.md) and
[CIRCUIT_KERNEL_REVIEW](CIRCUIT_KERNEL_REVIEW.md).

For each of the five ten-wall cores, exact positive rational source
pairs at a positive moment-curve external matrix give a spanning tree
on its ten walls. All ninety endpoint sources are independently verified
by rational source minors and image Plucker coordinates. Openness follows
from tile injectivity and invariance of domain. The nine tree equations
have rank nine and balanced one-dimensional kernel. Thus, at the displayed
matrix Z0 and for constant all-Z coefficients,

\[
 \mathbb R\epsilon\ \subseteq\ \mathcal R_{\rm all}(P)
 \ \subseteq\ \mathcal R_{Z_0}(P)=\mathbb R\epsilon.
\]

The two inclusions prove equality. They do not assert the same kernel
dimension at every other fixed Z. A complete chamber enumeration is
unnecessary because the exact open witnesses provide necessary equations
of sufficient rank. See [LOCAL_RELATION_KERNELS](LOCAL_RELATION_KERNELS.md).

## 5. The two obstruction cores

**PROVED by exact finite certificates.** For (1,1,2,2,2) and (2,2,2,3),
the eight admissible facet indicators give an invertible 8×8 matrix at
eight exact target neighborhoods for one positive rational Z0. Both
determinants are one, independently checked with Fraction elimination.

These are complete indicator decisions, including nonmembership in
closed tiles. The source closure/gauge audit exhausts the potentially
missing charts; nonzero twistors exclude the omitted lower-span strata.
Complete rational inversions on each ordinary wall retain all possible
positive preimages. All pivot and sign tests are strict, so each indicator
row persists on an open neighborhood. Evaluation of any relation modulo
lower-dimensional sets is therefore legitimate. It follows that
R_Z0(P)=0 and hence R_all(P)=0. Details, actual matrices and failed cover
attempts remain in [COUNTEREXAMPLE_SEARCH](COUNTEREXAMPLE_SEARCH.md).

The q9 parent's open hole excludes any all-Z tiling of its entire image
by admissible facets. The q8 parent's possible **single** admissible-facet
tiling remains undecided. Its homogeneous relation space is nevertheless
fully determined: it cannot support two different all-Z decompositions
using only these eight facets. This distinction is necessary; independence
does not solve an inhomogeneous covering problem.

## 6. Transport to every n and the exact local consequence

**PROVED (preserved exact transport).** For increasing support I, zero
insertion satisfies (j_I C)Z=CZ_I, identifying the entire source/fiber/image
problem, all facet incidences and multiplicities. Positive row restriction
and the converse positive-row extension lemma identify the two all-Z
relation spaces, not just one inclusion. Dihedral actions similarly
intertwine the maps. See [FINITE_CORES](../run3/FINITE_CORES.md) and its
[independent audit](../run3/CORE_THEOREM_REVIEW.md). Thus the complete
29-core relation-space classification transports to every n.

Any two multiplicity-one all-Z local tile decompositions of the same
region, using only admissible facets of one parent, have a difference
in R_all(P). For the
two hostile parents that difference is zero. For each balanced parent,
it is a multiple of a vector nonzero on every admissible facet. Binary
tile-incidence coefficients force either identical decompositions or
exactly the two canonical sides, up to reversal. In particular the two
canonical sides are the only multiplicity-one all-Z facet tilings of
that parent's closed image. Arbitrary overlapping covers are excluded
from this uniqueness statement.

This theorem does not address additional tiles whose source cells are
not facets of this parent, relations across several parents, coefficients
depending on Z, or the generation of complete-tiling differences. The
finite local problem is complete in the stated all-Z indicator sense.
The campaign stops at its hostile audit before generation work.
