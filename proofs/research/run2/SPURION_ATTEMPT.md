# Run 2: a separate repaired-parent relation

This document does not replace the printed Appendix-A fixture. The printed
parent and printed rows38,46 remain inconsistent with the claimed common
parent. The source theorem about the published spurion tiling is preserved.
The relation below uses a different parent and rows39,45 and has its own
geometric argument.

**PROVED, independently reviewed:** the repaired-parent relation
is an all-positive-Z, multiplicity-one local5↔5 replacement. Its proof uses
linear positive fibers, standard-cell injectivity and published spurion
injectivity; it does not infer a geometric identity from a source boundary
or canonical-form identity. This is the intended published type of relation,
not a novelty claim. Its embedding into the literal50-row collection is not
claimed here.

## 1. Exact source identification

Write P=(91)(2)(345)(678), with affine permutation
(3,6,4,5,9,7,8,11,10). Its twelve source facets are independently enumerated
by delete/merge and by bases/affine incidence. The ten selected facets are
Appendix rows28,34,35,39,45 and the five separately printed BCFW insertions
B1,...,B5. The other two facets merge classes(345),(678), or(678),(91).
The printed parent remains (912)(345)(67)(8); its zero-minor obstructions are
recorded in the preserved first-run section of research/SPURION.md.

The two unselected facets have class sizes(1,2,6) and(1,3,5). The
class-complement Schubert bound in PARENT_ENUMERATION.md bounds their image
dimensions by6 and7, respectively, for every positive Z. Thus they are
rigorously collapsed, rather than merely low-rank at the sample.

Rotate labels by old9→new1, old1→new2, ..., old8→new9, using the standard
rank-two twisted cyclic action. Positivity of external data is preserved by
the matching rank-six twisted cyclic action. Thus it suffices to treat

P'=(12)(3)(456)(789).

Its positive chart is the projective positive orthant with coordinates
x=(a1,a2,u,v,c4,c5,c6,d7,d8,d9), represented by

```
C(x) = [a1 a2 u+v c4 c5 c6  0  0  0]
       [ 0  0   v c4 c5 c6 d7 d8 d9].
```

Three distinct class directions have been normalized to horizontal,
diagonal and vertical; the remaining direction lies strictly between the
first two. Only simultaneous scalar multiplication remains. Setting one
coordinate to zero gives ten distinct dimension-eight source facets.

| Coordinate zero | Original label | Side |
|---|---|---|
| a1 | row35 | + |
| a2 | B1 | - |
| u | row45 | + |
| v | row28 (spurion) | + |
| c4 | B5 | - |
| c5 | row39 | + |
| c6 | B3 | - |
| d7 | B4 | - |
| d8 | row34 | + |
| d9 | B2 | - |

All labels are checked by their full basis sets and affine permutations in
src/magic_number/spurion_relation.py. This is a source-incidence check,
independent of the geometric proof that follows.

## 2. The fixed-image fiber is linear

Fix any positive9×6 matrix Z and any Y in the image of P' or one of the ten
open facets. Let E_i denote the class of Z_i in the four-dimensional quotient
V=R^6/Y. Define M_Y:R^10→V⊕V by columns

```
(E1,0),(E2,0),(E3,0),(E3,E3),
(E4,E4),(E5,E5),(E6,E6),(0,E7),(0,E8),(0,E9).
```

Then M_Y x=0 exactly means that both rows of C(x)Z belong to Y. Whenever
C(x) has rank two and nonnegative minors this is equality of row spaces:
the amplituhedron map is defined on all of Gr≥0(2,9). This observation is a
linear equation for the entire fiber, not merely its differential.

Put U=a1Z1+a2Z2, W=c4Z4+c5Z5+c6Z6, X=d7Z7+d8Z8+d9Z9. On P' and on each
selected open facet, U,W,X are all nonzero positive combinations. We can use
Y1=U+(u+v)Z3+W and Y2=vZ3+W+X as a representative of Y.

**PROVED: M_Y has rank8 on this entire locus.** An element of the dual kernel
is a pair α,β of covectors annihilating Y such that α annihilates Z1,Z2,Z3;
β annihilates Z3,Z7,Z8,Z9; and α+β annihilates Z4,Z5,Z6. The determinant

det(Y1,Y2,Z3,Z7,Z8,Z9) = -det(U,Z3,W,Z7,Z8,Z9)

is strictly negative: its negative is a sum of positive coefficients times
ordered positive6-minors of Z. Consequently β=0. Then α annihilates Z1,...,Z6,
so α=0.

**PROVED: projection ker(M_Y)→R² onto coordinates(a1,a2) is an isomorphism.**
Delete both corresponding columns from M_Y. The same dual argument first
forces β=0. It then forces α to annihilate Z3,Z4,Z5,Z6 and Y, hence U and X.
But

det(U,Z3,Z4,Z5,Z6,X)>0

by the ordered positive-minor expansion. Thus the remaining8×8 matrix is
invertible. This gives a globally fixed orientation of each two-dimensional
kernel, independent of the quotient basis used to compute M_Y.

## 3. Admissibility of all ten facets

**PROVED: deleting a1, a2, c4, c5 or c6 gives an injective all-Z tile map.**
For the matrix M_Y with one such column deleted, the first determinant in
Section2 again forces β=0. If an a-column was deleted, α annihilates the
other a-column, Z3,Z4,Z5,Z6 and X; these six vectors have strictly positive
determinant. If a c-column was deleted, α annihilates Z1,Z2,Z3, the two other
c-columns, and X; these six vectors again have strictly positive determinant.
The matrix with nine columns therefore has rank8. Its kernel has dimension1,
which is precisely uniqueness of the projective positive source coefficient
vector over Y. No generic-rank-to-injectivity inference is used.

**SOURCE-VERIFIED with exact recipe witnesses:** u=0 and the three d=0 facets
are standard KWZ BCFW cells after cyclic/reflection operations and inserting
zero columns. The machine-readable fixture provides the standard path pair,
its affine permutation, dihedral operation and ordered nonloop support.
Standard BCFW injectivity is valid for all positive external data; selecting
rows indexed by the support preserves positivity, and the standard twisted
cyclic/reflection operations preserve the all-Z statement. These exact
recipe identifications are separate from the label assertion in the
misprinted common-parent paragraph.

**SOURCE-VERIFIED:** v=0 is the(123)(456)(789) spurion, whose all-Z injectivity
is stated and obtained by the inverse functionaries in Sections5.1 and5.3
of *A cluster of results on amplituhedron tiles*. The proof here uses that
already established tile property, not its disputed tiling/common-parent
argument. The non-BCFW local relation itself is certified independently.

Each remaining source-verified injectivity statement also implies that the
corresponding nine-column matrix has rank8: otherwise its kernel has
dimension≥2 and a positive point in the open wall has a nontrivial nearby
positive projective interval of preimages in that same wall, contradicting
injectivity. Thus every one of the ten walls is transverse to the fiber.

## 4. Endpoint signs are all-Z statements

Choose the kernel basis K_Y with its a1,a2 rows equal to the identity. At a
positive point x of a selected wall, the vector

K_Y·(a2,-a1)

fixes the increasing orientation of the projective coordinate a1/a2; this
also extends through the endpoints a1=0 or a2=0. Its wall coordinate is
nonzero by the preceding transverse-wall argument. It is continuous in the
positive matrix Z and the source wall parameters. The space of such pairs
is connected: an open positroid cell and the space of positive external
matrices are connected (the latter is the positive Grassmannian top cell
with the connected GL⁺(6) choice of basis). Consequently its sign is constant.

An exact rational evaluation at the positive moment-curve matrix
Z_i=(1,i,i²,i³,i⁴,i⁵), with all nonvanishing source coordinates equal to1,
therefore determines the sign for every positive Z and every point of the
open facet. The ten derivatives, in chart-coordinate order, are

```
1, -1, 28/9, 12/7, -922/189, 590/189, -166/189,
-64/27, 44/27, -10/27.
```

This use of exact evaluations is justified by a proven nonvanishing and
connectedness argument; a finite sample is not being promoted on its own.
The signs give precisely the table in Section1.

## 5. Equality, disjointness, multiplicity and lower strata

For Y in the open image of P', the projectivized nonnegative kernel cone
is an interval with nonempty interior. Indeed ker(M_Y) has dimension2;
positive x exists; and normalizing a1+a2=1 identifies its closure with a
closed interval cut out by ten linear inequalities inside0≤a1≤1. All other
coordinates are linear functions of(a1,a2). The interval is bounded and its
two endpoints have opposite inward orientation.

For generic Y, each endpoint has exactly one vanishing coordinate. Here is
the precise exceptional-set bound. A coefficient vector with at least two
zeros and rank-two C lies in a finite union of projective faces of dimension
at most7, so its amplituhedron image has dimension at most7. If C has rank1,
then a1+a2=1 forces its second row to vanish: v=c4=c5=c6=d7=d8=d9=0.
Its image is a line in the three-dimensional span(Z1,Z2,Z3). Such lines
have at most2 parameters, and the2-planes containing each have dimension4.
Their incidence image in Gr(2,6) has dimension at most6. Rank-one C therefore
does not create an unaccounted full-dimensional set of endpoint images.

The image of the open parent is open: in the explicit kernel basis,
a positive solution persists under sufficiently small changes of Y.
Outside the exceptional set just described, the two fiber endpoints thus
give exactly one preimage in a + facet and one in a - facet. Conversely, at
any open selected facet, transversality allows movement into the positive
parent along one side of the fiber. Each side therefore covers the same
open parent image with multiplicity one outside lower-dimensional sets.

Each facet map is a continuous injection from an8-dimensional open cell to
Gr(2,6), so invariance of domain makes its image open. If two same-side open
images intersected, their intersection would be nonempty open and would
meet the complement of the exceptional set. That contradicts unique
endpoint coverage. Hence same-side open tile images are exactly disjoint,
not just disjoint almost everywhere.

Finally each closed tile is the closure of its open image, since the source
cell closure is compact and the amplituhedron map is continuous on it. Both
finite closed unions equal the closure of the parent image: one inclusion
follows from source-facet incidence; the other follows from generic endpoint
coverage and density in the open parent image. Thus the two closed covered
regions are equal. Lower-dimensional common boundaries affect neither
the indicator-class identity modulo lower dimension nor multiplicity one
on the open tiles.

## 6. Exact relation and scope

**PROVED, independently reviewed:**

```
[row28]+[row34]+[row35]+[row39]+[row45]
   -[B1]-[B2]-[B3]-[B4]-[B5] = 0
```

as tile indicator classes modulo lower-dimensional subsets, for every
positive Z. The coefficient sum is exactly5−5=0. Both sides are local
multiplicity-one decompositions of the same closed region. This is LevelA
symbolic region equality through an exact linear-fiber description, rather
than LevelC canonical-form additivity.

It gives no proof that the printed row38/46 replacement is this relation,
no verified extension of this repaired local relation to the literal full
Appendix tiling, no classification of other local relations, and no
generation or Magic Number theorem.

**FAILED (literal printed common-parent reconstruction):** its exact zero
minor contradictions persist. **CONJECTURAL:** the identified parent and
row corrections reflect the authors' intended printed proof. The separate
relation does not require that editorial conjecture.

## Reproduction

```
PYTHONPATH=src .venv/bin/python -m magic_number.spurion_relation
PYTHONPATH=src .venv/bin/python -m pytest tests/test_spurion_relation.py -q
```

Independent verification: [SPURION_REVIEW.md](SPURION_REVIEW.md) checks the proof and recomputes endpoint signs using an ambient linear system. The published individual spurion injectivity input is retained explicitly. Root review also checked the rank, orientation and exceptional-locus arguments.
