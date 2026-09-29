# Alternating signs for the complete two-class parent sector

**PROVED; independently audited in [CORE_THEOREM_REVIEW.md](CORE_THEOREM_REVIEW.md).** Let P be a nine-dimensional rank-two
positroid cell with exactly two nonloop parallel classes. If its image is
full-dimensional in Gr(2,6), its class sizes are5 and6. Its six
full-dimensional source facets are admissible all-Z tiles and form an
all-Z local3-for-3 replacement. The image-side signs alternate along the
six-element class, so their sum is zero. This holds for arbitrary loop
insertions, cyclic positions and n>=11.

The hypotheses are source-combinatorial and do not assume balancedness or
the existence of the decomposition. The proof establishes both.
No claim of literature-first novelty is made: the mechanism is Cramer's
rule and the alternating oriented matroid of positive maximal minors.

## 1. Source classification and the only full-dimensional profile

Since q+s=13 and s=2, q=11. If either class has size at most4, every image
plane meets its external-row span, a space of dimension at most4. The
class-complement Schubert bound puts the entire parent image in dimension
at most7. (The bound concerns arbitrary image planes and applies to
nine-dimensional parents as well as eight-dimensional cells.) Therefore
the only possible full-dimensional two-class profile is(5,6).

By signed cyclic relabeling and deleting loops, put
`A=(1,...,5)`, `B=(6,...,11)`. Representatives are

`C(a,b) = [a1 ... a5 | 0 ... 0; 0 ... 0 | b1 ... b6]`,

with a,b strictly positive, modulo independent positive rescaling of the
two rows. Thus P is a product of positive projective simplices of
dimensions4 and5. Set `U=sum a_i Z_i`, `V=sum b_j Z_(5+j)` and
`Y=span(U,V)`.

## 2. The entire fiber, including its orientation

The five A-rows are independent. Write H_A for their span. Positivity gives

`ell(V):=det(Z_1,...,Z_5,V)>0`,

since each summand is a positive coefficient times an ordered six-minor.
Therefore V is outside H_A and `Y intersect H_A=R U`. In particular the
positive ray of U, and hence a up to positive scale, is uniquely determined
by Y. The six B-rows form an invertible positive-determinant matrix Z_B.

Any other positive B-vector V' in Y has `V'=alpha V+beta U`. Its positive
B-coefficients imply `ell(V')>0`, while ell(U)=0, so alpha>0. Rescale V' by
alpha. **Every** positive source preimage is then uniquely represented by

`V(t)=V+t U`, equivalently `b(t)=b+t h`, where `h=U Z_B^{-1}`.

There is no second branch from alpha<0. This is a full fiber calculation,
not a differential-rank argument. The increasing t direction supplies a
global fiber orientation once the positive ray U has been chosen; positive
rescaling of U changes its speed, not its sign.

## 3. The symbolic wall signs and why they balance

Let the B-rows in order be B1,...,B6. Cramer's rule gives

\[
h_j=(-1)^{j-1}\,
\frac{\sum_{i=1}^{5}a_i\,
\det(Z_i,B_1,\ldots,\widehat{B_j},\ldots,B_6)}
{\det(B_1,\ldots,B_6)}.
\]

Every determinant in the fraction is an **ordered positive** maximal
minor. Hence the six h_j are nonzero, with signs `+,-,+,-,+,-`, for every
positive Z and every a>0. This is one symbolic formula, not six unrelated
evaluations or a sign-constancy inference from one sample.

The positive fiber is exactly

`max_(h_j>0)(-b_j/h_j) < t < min_(h_j<0)(-b_j/h_j)`.

It is a nonempty bounded interval because t=0 is feasible and both signs
occur. Its closed endpoints are obtained by replacing the strict
inequalities with weak ones. The wall b_j=0 points inward at the lower
endpoint for h_j>0 and at the upper endpoint for h_j<0. Therefore its
image-side coefficient is exactly `epsilon_j=(-1)^(j-1)`.

**This is the additional sign-count input.** Alternation on an even set
of six walls gives three of each sign. Topology alone gives cancellation
at the two endpoints of each individual fiber; the positive-minor formula
controls how many distinct wall types have either sign.

## 4. Wall admissibility, multiplicity and coverage

The source facets are the11 single-column deletions; merging two classes
would reduce rank and is not a positroid facet in Gr(2,11). Deleting one
A-column gives profile(4,6), whose image dimension is at most7 by the
Schubert bound. Deleting B_j gives profile(5,5).

For a(5,5) wall, each class spans a hyperplane. Positivity gives
`det(Z_A,V)>0` and, up to the fixed row-order sign,
`det(U,Z_(B without j))>0`. Thus the two positive image lines are uniquely
`Y intersect H_A` and `Y intersect H_(B without j)`. Their five independent
external basis rows recover both positive coefficient rays uniquely.
This proves all-Z injectivity of every selected wall. It also gives
rational inversion on the open wall image. At m4 these cells have a
separate general BCFW witness: on the reduced ten labels, take the
left BCFW product with `a=6,b=7,c=8,d=9,n=10` and rank-one support1,...,5.
Its two rows have the disjoint five-element supports above.

The open parent image is open: intersections with H_A and the normalization
ell(V)=constant vary continuously near any such Y, preserving positive
a- and b-coefficients. Generic Y has one coordinate vanishing at each
interval endpoint. A tie between two endpoint constraints belongs to an
image of a source stratum with two B-zeros, of dimension at most7.
The vector b(t) cannot vanish identically: ell(V(t))=ell(V)>0. Every endpoint
therefore gives a nonnegative rank-two source point; no projective-gauge
rank-one boundary is omitted.

It follows that generic Y has exactly one positive-wall endpoint and one
negative-wall endpoint, with multiplicity one. Every selected open wall
image lies in the open parent image, by the nonzero inward derivative h_j.
Each wall image is open by injectivity and invariance of domain. Any
same-side overlap would be open and would contradict generic endpoint
uniqueness. Thus open images on each side are exactly disjoint. Taking
closures, using source compactness and density, proves that both finite
closed unions equal the closure of the open parent image.

This gives the indicator identity modulo dimension<8,

`[B-delete1]+[B-delete3]+[B-delete5]
 =[B-delete2]+[B-delete4]+[B-delete6]`,

with genuine admissible tiles. It is a local geometric relation; no
extension inside a specified complete tiling is established.

## 5. Transport and the role of m

The exact map identity and positive-row extension in
[FINITE_CORES.md](FINITE_CORES.md) transport this statement to arbitrary
loop insertions and cyclic/reflection positions. Thus this verifies the
**entire two-class sector** of nine-dimensional parents, including ruling
out all other two-class profiles as full-dimensional parents. It does
not settle the other parent sectors.

The same proof works for rank2 and **any even m>=2**: a parent of dimension
2m+1 with two classes has total support2m+3, and the full-dimensional case
has class sizes(m+1,m+2). The smaller class spans a hyperplane in R^(m+2);
the larger is a basis. Its m+2 wall signs alternate by the same Cramer
formula. There are `(m+2)/2` on each side. This extension explains precisely
where evenness enters this restricted mechanism. It is not a theorem
about all rank-two parent profiles or complete amplituhedron tilings.

## Verification and kill-tests

`two_class_fibers.py` records the six m4 signs and complete exact endpoint
preimages. Tests compare inverse-matrix coefficients with a separate
Fraction determinant computation and identify the BCFW wall recipe.
The independent audit in CORE_THEOREM_REVIEW.md checks the full fiber,
positive orientation, all endpoints, admissibility, and even-m extension.

An error in recovering the unique A-ray, the alpha>0 argument, positive
minor signs, or boundary completeness would kill the proof. The largest
potential omission is a second fiber branch; the ell(V') argument excludes
it explicitly. No assumption about degrees of four-mass cells appears.
