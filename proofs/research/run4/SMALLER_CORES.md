# Seven remaining smaller cores, using two shared mechanisms

**PROVED, independently audited in [MERGER_WALLS](MERGER_WALLS.md) and
[REVIEW](REVIEW.md).** Six previously untreated q8/q9
cores have one common hyperplane/Gale proof of all-Z3↔3 relations. The
remaining q9 core(1,3,2,3) has an all-Z5↔5 interval relation whose wall types
pair under an orientation-reversing reflection. These are local indicator
relations, modulo lower-dimensional sets, with admissibility, positive
fibers and endpoint coverage proved separately. No complete-tiling
extension or relation-generation theorem is asserted. No priority claim
is made for the classical hyperplane, Cramer or Gale ingredients.

## 1. A class with exactly five labels outside it

**PROVED, independently audited (complement-five theorem).** Let P be
a nine-dimensional rank-two positroid parent containing a nonloop parallel
class D whose complement in the nonloop support has exactly five labels.
Its six noncollapsed source facets are admissible all-Z tiles. They form
a multiplicity-one all-Z3↔3 local replacement. Every other source facet is
collapsed for all positive Z.

The hypotheses concern only the source class pattern, not a proposed
relation or cardinality. Delete loops and use the compatible signed cyclic
action to place the five complementary labels first, D last. Let their
successive parallel classes be A1,...,A_ell, and put r=|D|. Since q+s=13,

```
ell+r=7,    q=5+r,    s=ell+1,    1<=ell<=5,    r>=2.
```

Every positive parent representative can be written

```
row1 = (a1,a2,a3,a4,a5, 0,...,0),
row2 = (t_class(i)*a_i on i=1,...,5; d_j on D),
a_i>0, d_j>0, t1<...<t_ell.
```

The t_j are real, not assumed positive. This is the global signed cyclic
source chart with D vertical. Row operations preserving this presentation
rescale the first row positively and apply a common positive affine
transformation to the slopes and a positive common scale to the d_j.

## 2. Recovering the row and the entire fiber

Fix any positive q×6 external matrix Z. Set

```
H=span(Z1,...,Z5), R=sum a_i Z_i,
V_j=sum_(i in A_j) a_i Z_i,
S=sum t_j V_j + sum d_j Z_(D_j),   Y=span(R,S).
```

The five Z_i are independent and

```
ell_H(S):=det(Z1,...,Z5,S)
         =sum d_j det(Z1,...,Z5,Z_(D_j)) > 0.
```

Therefore Y∩H is exactly the line R. Its positive ray, and hence the five
a_i up to a positive common scale, are uniquely determined by Y. Fix that
scale. This fixes all V_j.

There is no missing negative or second fiber branch in the image gauge.
For any other positive preimage, first normalize its R' to R. Its second
image row is S'=alpha S+beta R. Positivity of its D coefficients gives
ell_H(S')>0, while ell_H(S)>0 and ell_H(R)=0; hence alpha>0. Dividing the
second source row by alpha and subtracting(beta/alpha) times the first row
are allowed determinant-positive row operations. They preserve all slope
differences and positivity of all D coefficients. Thus every positive
preimage has a representative with the exact matrix image(R,S).

In that fixed image gauge, the complete fiber equation is

```
sum t_j V_j + sum d_j Z_(D_j) = S.
```

Let B be the7×6 matrix with ordered rows

```
(V1,...,V_ell, Z_(D1),...,Z_(Dr)).
```

**PROVED:** B is positive. Each of its ordered six-minors expands into
positive coefficients times ordered six-minors of Z. All blocks have
disjoint increasing supports, so every term has positive sign, and at
least one term occurs. This proof works for every positive choice of a_i
and every positive Z.

Define the nonzero alternating Gale vector

```
w_i=(-1)^(i-1) det(B with row i deleted), i=1,...,7.
```

Then wᵀB=0 and every solution is exactly

```
(t1,...,t_ell,d1,...,dr)(tau)
    =(t1,...,t_ell,d1,...,dr)(0) + tau*w.
```

No normalization t1=0 is imposed in this fixed image gauge. Imposing that
extra condition without changing the second image row would incorrectly
discard the fiber. The source inequalities are the successive differences
t_(j+1)−t_j>0 and the d_j>0.

## 3. Six alternating image-side signs and direct admissibility

The ordered wall inequalities and their derivatives are

```
t_(j+1)-t_j : w_(j+1)-w_j, j=1,...,ell-1;
d_j         : w_(ell+j),   j=1,...,r.
```

Consecutive Gale coefficients have opposite signs, so the derivative of
each difference has sign w_(j+1). Combining the two lists gives precisely
the six signs of w2,w3,...,w7:

```
(-,+,-,+,-,+).
```

There are three of each sign for every positive Z. This is one symbolic
positive-minor calculation, not six individually sampled Jacobians and
not a subtraction of equal-size complete tilings.

The corresponding source walls are merging consecutive complementary
classes A_j,A_(j+1), or deleting one column of D. Each is dimension eight.
On each open wall the five a_i remain positive and D still has at least one
positive column, because r>=2. Thus the same hyperplane recovery and entire
affine fiber calculation apply. Its one defining linear wall condition has
nonzero derivative, so it determines the unique tau. This proves global
injectivity on every wall, for every positive Z. In particular these are
admissible tiles independently of a BCFW classification or a sample rank.

All other source facets are retained and certified collapsed. Deleting a
complementary column leaves only four labels outside D. Merging D with a
neighboring complementary class leaves at most four labels outside the
enlarged class. The class-complement Schubert bound puts every such image
in dimension at most seven. The complete source facet rule consists of
these deletions and adjacent merges, so no additional facet type is omitted.

## 4. Geometric relation, boundaries and multiplicity

The positive fiber is cut out by six strict affine inequalities in tau.
At an interior parent point tau=0 is feasible. The six derivatives have
both signs, so the feasible set is a nonempty bounded open interval.
Its two finite endpoints satisfy all the weak inequalities. The D-vector
cannot vanish altogether there: ell_H(S) is fixed strictly positive.
Consequently these endpoints are rank-two nonnegative source points,
with no omitted rank-one incidence family.

Generic endpoints lie in one selected open source wall. Ties between two
constraints belong to source strata of dimension at most seven: two merges
or deletions lower q+s by at least two; mixed cases do the same. There are
finitely many such strata, so their images are lower-dimensional. Each
generic fiber therefore has exactly one positive-sign and one negative-sign
wall endpoint, with multiplicity one.

The parent image is open. Indeed R(Y)=Y∩H varies smoothly on the transverse
locus, its five coefficients remain positive locally, and the rank-six
compressed system smoothly recovers nearby solutions with the same strict
slope differences and positive d_j. Equivalently, a local choice of the
free affine fiber parameter and Y gives smooth source coordinates. Each
selected open wall image lies in that open parent image because its
nonzero inward derivative moves into all strict source inequalities.

Each wall image is open by injectivity and invariance of domain. A
same-side overlap would be open and meet the generic locus, contradicting
unique endpoint coverage. Thus open tile images on each side are exactly
disjoint. Both closed finite unions equal the closure of the parent image:
one inclusion follows from source incidence and compact source closures;
the other follows from generic coverage and density. This proves an exact
Level A indicator identity modulo dimension<8, with three admissible tiles
on each side, for every positive Z.

Loop insertion and compatible dihedral actions transport the entire fiber
problem by the previously proved exact transport theorem. This is a theorem
about the complete complement-five parent class, not just the six fixtures.

## 5. The six new smaller-core instances

The distinguished class is placed last in the following representatives:

| Core type | Sizes of the complementary classes | Size of D | Selected/collapsed walls |
|---|---|---:|---:|
| (1,1,1,2,3) | (1,1,1,2) | 3 | 6 / 4 |
| (1,1,2,1,3) | (1,1,2,1) | 3 | 6 / 4 |
| (1,1,3,4) | (1,1,3) | 4 | 6 / 5 |
| (1,2,2,4) | (1,2,2) | 4 | 6 / 6 |
| (1,2,4,2) | (2,1,2) | 4 | 6 / 6 |
| (1,3,1,4) | (1,3,1) | 4 | 6 / 5 |

**COMPUTATIONALLY-VERIFIED:** the machine fixture independently constructs
the source bases/affine labels of all six selected walls for each row,
checks the complete facet partition and records exact image-preserving
fiber endpoints. All six coefficient sums are zero. The theorem, rather
than these rational examples, supplies all-Z certification.

The same class includes the n7 Gale parent, the q10 class-five merger
parents and the q11 two-class(5,6) parent previously handled by related
special arguments. The general mechanism keeps the slope differences and
the genuine merger walls explicitly.

## 6. The final q9 core: a reflected interval

**PROVED, independently audited.** The parent

```
P=(123)(4)(567)(89)
```

has the positive homogeneous chart

```
x=(a1,a2,a3,u,v,b5,b6,b7,c8,c9)>0,
C=[a1 a2 a3 u+v b5 b6 b7  0  0;
    0  0  0   v b5 b6 b7 c8 c9].
```

Normalize the three nonsingleton directions to horizontal, diagonal and
vertical. The singleton lies between the first two, so this is the entire
source cell with only common scalar redundancy. Its ten coordinate walls
are eight column deletions and two adjacent merges. Every one has an exact
general BCFW recipe in the fixture and hence all-Z injectivity. The two
remaining source facets merge(567),(89) or(89),(123); both have an enlarged
class of size five and image dimension at most seven.

For E_i=Z_i mod Y, the linear image matrix has columns

```
(E1,0),(E2,0),(E3,0),(E4,0),(E4,E4),
(E5,E5),(E6,E6),(E7,E7),(0,E8),(0,E9).
```

The kernel has a global pivot(c8,c9). Indeed delete the last two columns
and subtract column(E4,0) from(E4,E4); the block determinant factors as

```
<Y1234> * <Y4567>.
```

Up to a common positive quotient-coordinate factor, both brackets are
strictly positive. Put U=sum a_iZi, W=sum b_iZi, X=c8Z8+c9Z9. Then

```
<Y1234>=det(Z1,Z2,Z3,Z4,W,X)>0,
<Y4567>=det(U,Z4,Z5,Z6,Z7,X)>0.
```

These are positive ordered-minor sums throughout the parent and every
selected open wall. Thus rank is eight and the pivot is globally smooth.
Wall injectivity makes every selected coordinate cut transverse, by the
same within-wall positive-kernel contradiction used in earlier runs.

Normalize c8+c9=1. The nonnegative kernel is a bounded projective interval
with positive interior. Two-coordinate-zero rank-two strata have image
dimension at most seven. At a possible rank-one coefficient point the
nonzero vertical D class forces the entire first row to vanish; this sets
a1=a2=a3=u=v=b5=b6=b7=0. Its nonzero image is a line in span(Z8,Z9), whose
containing-two-plane incidence family has dimension at most five. Thus
generic endpoints are precisely the selected open admissible walls.
The established interval, transversality, openness and compact-closure
argument proves disjointness, multiplicity one and equality of both closed
covered regions exactly as in Sections3–4 and the prior interval theorem.

For balance, there is an actual reflection, not just a symmetric count.
The signed label reflection fixes4, exchanges1↔7,2↔6,3↔5,8↔9, and after
the source row transformation [[1,0],[1,-1]] acts on coordinates by

```
(a1,a2,a3,u,v,b5,b6,b7,c8,c9)
  ->(b7,b6,b5,v,u,a3,a2,a1,c9,c8).
```

The two external rows at8,9 and the corresponding source columns receive
the compatible cyclic signs; an ambient determinant-negative correction
restores external positivity. This is the standard exact dihedral
intertwining, and the displayed source chart verifies its coefficient
action directly. There are five coordinate transpositions, reversing
orientation of the9-dimensional projective source chart. The corresponding
ambient GL6 action preserves Gr(2,6) orientation. The global kernel pivot
supplies an actual submersion, so the previously proved orientation-sequence
lemma reverses fiber orientation and freely pairs opposite wall signs.
Hence the ten walls form a5↔5 relation without using a sign-count table.

**COMPUTATIONALLY-VERIFIED with prior sign constancy:** exact evaluations
in the globally oriented(c8,c9) kernel give coefficients

```
(+,-,+,-,+,-,+,-,+,-)
```

in the displayed coordinate order. The source/external parameter space is
connected and every wall is transverse, so these evaluations identify
already constant all-Z signs. Reflection, rather than these samples,
explains their zero sum. The fixture records all ten source labels and
BCFW recipes.

## 7. Scope beyond m4 and kill-tests

The complement-five argument extends verbatim to rank2 and even m: replace
five by m+1 and external dimension six by m+2. A(2m+1)-dimensional parent
with a class having exactly m+1 outside labels has ell+r=m+3 compressed
positive vectors. Its m+2 slope/deletion wall derivatives have the signs
of w2,...,w_(m+3); alternation balances precisely because m+2 is even.
All other source facets have outside support at most m, putting their
images in dimension at most2m−1. This is a restricted structural family,
not a statement about arbitrary parent patterns or complete tilings.

Kill-tests are explicit: failure of unique positive hyperplane recovery,
a negative-alpha fiber branch, sign-indefinite compressed maximal minors,
an additional full-dimensional endpoint stratum, or a noninjective
selected wall would invalidate the complement-five theorem. Each is
excluded above. Removing the exact-complement hypothesis destroys the
hyperplane recovery, and no claim is made there. The reflected q9 proof
requires its actual orthant chart and symmetry; neither holds for the
previously identified four-mass/conic hostile cores.

## Reproduction

```
PYTHONPATH=src .venv/bin/python -m magic_number.smaller_parent_fibers
PYTHONPATH=src .venv/bin/python -m pytest tests/test_smaller_parent_fibers.py -q
```

Fixture: fixtures/run4/smaller_core_relations.json. Previous run files are
unchanged. Independent proof audit is required before final promotion.
