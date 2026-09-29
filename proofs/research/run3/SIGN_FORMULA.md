# Oriented linear fibers: what the signs mean

**PROVED, independently reviewed.** Let M be a real r×(r+2) matrix
of rank r, with the complementary minor obtained by deleting columns0,1
nonzero. Let K be the unique(r+2)×2 kernel basis with rows0,1 equal to the
identity. Write D_ij for the determinant obtained by deleting columns i,j,
keeping all other columns in order. For i<j,

\[
p_{ij}:=\det(K_i,K_j)=(-1)^{i+j-1}\frac{D_{ij}}{D_{01}}.
\]

The general formula is alternating in i,j. This is the usual complementary
minor/Hodge-dual identity, normalized by p_01=1. It follows, for example,
by taking the maximal wedge of the rows of M and its complementary2-vector;
the coefficient sign is the sign of the permutation(i,j,remaining columns),
namely(-1)^(i+j-1). Thus it is an algebraic identity, not an amplituhedron
specific novelty claim.

Let x=K(a,b), and define the oriented projective tangent
t=K(b,-a). This orientation increases x0/x1 where x1>0. Directly taking the
determinant of the two coefficient vectors gives

\[
t_i x_j-x_i t_j=p_{ij}(a^2+b^2).
\]

At an open coordinate wall x_i=0 with every other coordinate positive, any
j≠i therefore gives

\[
\boxed{\operatorname{sgn}(t_i)=\operatorname{sgn}(p_{ij}).}
\]

This is the image-side endpoint sign: t_i>0 means that the oriented fiber
enters the positive region at that wall; t_i<0 means that it exits.

## Geometric hypotheses and limitations

For an amplituhedron parent, this formula applies when a positive source
chart is a projective positive orthant and its complete fixed-image fiber
is P(ker M_Y∩positive orthant). The parent and selected facets must separately
have the rank, admissibility and lower-stratum properties required by the
linear-fiber theorem. The formula itself does not certify any of them.

Admissibility makes a wall transverse in this situation: if its coordinate
were identically zero on a two-dimensional kernel, a positive point of the
wall would have a projective interval of positive preimages within that wall.
Consequently a continuous endpoint sign cannot change on a connected
admissible-wall parameter space. This uses independently established
injectivity, not balancedness or equality of tiling sizes.

Changing the quotient basis left-multiplies M by an invertible matrix and
multiplies every D_ij by the same determinant. All p_ij are unchanged. A
different oriented kernel basis changes all endpoint signs together when
the orientation is reversed. One must explicitly account for orientation
transitions if no one pivot is valid globally.

An alternating source-cell boundary operator is a different object. Its
coefficients compare orientations in the source. Image endpoint signs also
depend on the map and the oriented fiber. The cofactor formula is the
missing transport information in a genuinely linear model; source boundary
signs alone do not give it. Olson's *Orientations of BCFW charts on the
Grassmannian* concerns source-chart/boundary orientations and does not
remove the required image-side step ([primary record](https://repo.scoap3.org/records/11636)).
The broader fiber approach is also prior art, including
[arXiv:2010.07254](https://arxiv.org/abs/2010.07254); no general fiber
framework is being claimed new here.

**FAILED as a general balancedness principle:** oriented interval fibers,
transverse walls, and injective wall maps do not force equal numbers of wall
types. Project a triangle whose three vertex images on a line are0,1,2.
The three edge images satisfy

\[
[0,1]+[1,2]-[0,2]=0
\]

modulo endpoints, with coefficient sum1. Every open edge maps injectively,
and generic fibers in the triangle are intervals. This is an elementary
counterexample to the proposed *abstract mechanism*, not an amplituhedron
counterexample. A separate sign-structure theorem is necessary.

## A checkable reflection criterion

**PROVED, independently reviewed.** Let Z vary over a connected positive
external-matrix space, with oriented submersions f_Z:P→B from an oriented
(d+1)-dimensional parent chart to an oriented d-dimensional image manifold.
Assume selected boundary walls are admissible, transverse, and have
image-side signs constant throughout their positive(Z,wall) parameter
spaces. Suppose involutions rho on the external-data family and r on P
freely pair the selected walls and satisfy

```
f_(rho Z) composed with r = g composed with f_Z,
```

where r reverses source orientation and g preserves image orientation.
Then r reverses oriented fiber direction and pairs opposite wall signs.
The coefficient sum of the selected walls is therefore zero. The
hypotheses specify independently checkable source symmetries, submersions,
admissibility and transversality; none assumes balancedness.

The proof is the orientation identity for the exact tangent sequence
0→T(fiber)→T(parent)→T(image)→0. It does not assume the desired coefficient
sum. A wall fixed by the symmetry would have to have both signs and is
therefore incompatible with the transverse, constant-sign hypotheses.
The hypotheses require an actual symmetry and proven submersion and
admissibility, not merely a symmetric-looking source boundary list.

This criterion is applicable to the separately certified n8 parent
(12)(3)(45)(6)(78), as detailed in LARGER_SUPPORT.md. Its reflection acts on
the ten positive homogeneous coordinates by

```
(a1,a2,u,v,c4,c5,w,t,e7,e8)
    -> (e8,e7,t,w,c5,c4,v,u,a2,a1).
```

These are five transpositions, so the positive projective9-dimensional
source chart has its orientation reversed. The corresponding fixed
ambient GL(6) transformation preserves the orientation of Gr(2,6). The
tangent space is Hom(Y,R6/Y), so its orientation sign under G is
sign(det G)^2 sign(det(G|Y))^(-6)=+1. More generally, for even ambient
dimension N, the GL(N) action on Gr(k,N) has sign(det G)^k. The global
kernel pivot proves submersion explicitly: (Y,a1/a2) reconstructs the
positive coefficient vector smoothly through K_Y, giving local source
coordinates with f_Z as projection. The globally oriented one-dimensional
fibers are therefore reversed, and the ten walls pair
with opposite image-side signs. This explains the5↔5 count without using
the independently computed list of ten exact derivatives. It does not
extend automatically to asymmetric source profiles such as the spurion
parent.

## Complete n7 parent sign mechanism

**PROVED, independently reviewed.** For each of the seven
nine-dimensional rank-two parents on seven nonloop labels, its six
admissible facets have alternating3+3 image-side signs. This is a complete
statement about these source parents and their known admissible facets.
It does not use equality of complete BCFW tiling cardinalities.

After a cyclic rotation the parent is(12)(3)(4)(5)(6)(7). Let its representative
C have C1=a v, C2=b v, with a,b>0. Choose v horizontal and the other five
column directions cyclically after it; then det(v,C_i)>0 for i=3,...,7.
Let Z be any positive7×6 external matrix, and set

\[
w_i=(-1)^{i-1}\det Z_{[7]\setminus\{i\}}.
\]

Laplace expansion gives wᵀZ=0, and positivity makes its signs alternate.
Any other representative with the *same matrix image* CZ is C+h wᵀ.
The equation Δ12=0 becomes

\[
(a w_2-b w_1)\det(v,h)=0.
\]

Since w1>0 and w2<0, its first factor is nonzero; hence h=t v. Thus the
entire parent fiber in this image gauge is the affine line C(t)=C+t v wᵀ.
Choosing an image gauge does not reverse positivity: the common bracket
⟨Y3456⟩ is positive throughout this parent and its selected open facets,
because it is the positive sum
Δ17(C)det Z134567+Δ27(C)det Z234567. This fixes the positive orientation of Y.

The admissible facets are deleting column1, deleting column2, and merging
the pairs(34),(45),(56),(67). Their inward wall coordinates are respectively
the two positive column scales and the four positive adjacent minors. Their
derivatives along increasing t are

\[
w_1,\quad w_2,\quad
w_i\det(v,C_{i+1})-w_{i+1}\det(v,C_i)\quad(i=3,4,5,6).
\]

Consecutive w_i have opposite signs, so each latter derivative has sign w_i.
The six signs are therefore +,-,+,-,+,-. The two other source facets merge
(12) with3 or7; they have a class of size3 with complement size4 and are
collapsed by the all-Z class-complement dimension bound. They are not tile
terms discarded on the basis of a numerical rank test.

These signs agree, up to simultaneous reversal, with all seven independently
certified local relations in Run2. Cyclic rotation proves the other six
parents, and increasing zero insertion preserves the argument. This is an
alternating Gale-kernel explanation of the existing3↔3 relations; it is not
a claim of a new general positroid relation theorem.

## Code and tests

src/magic_number/oriented_fibers.py implements complementary minors,
normalized kernel bases, endpoint tangents, the positive corank-one Gale
vector, and all seven n7 signed parent relations. Tests compare every one
with the separately constructed Run2 tiling-difference fixtures. The
spurion-parent application uses the same cofactor identity; its symbolic
sign proof is in SPURION_SIGN_MECHANISM.md.

## Source signs require the map Jacobian

**PROVED (orientation identity).** Fix the outward-normal-first boundary
convention. Let w be a naturally oriented wall basis, n an outward normal,
and eta_W∈{±1} be its source incidence sign: (n,eta_W w) has positive parent
orientation. Orient the fiber so that fiber orientation followed by target
orientation gives the parent orientation. If its tangent t points inward
with sign epsilon_W, then t is −epsilon_W times an outward normal, modulo
wall tangents. Writing j_W=sign Jac(f|W) relative to w and the fixed target
orientation gives

```
orientation(t,w) = -epsilon_W eta_W = j_W,
therefore epsilon_W = -eta_W sign Jac(f|W).
```

Changing the common target or fiber orientation changes one common factor,
not independently chosen factors on different walls. For ten homogeneous
positive coordinates numbered1,...,10, normalize the first surviving
coordinate to1 and order the other eight wall coordinates increasingly.
Relative to the positive projective parent orientation, the outward-first
incidence is eta_i=(-1)^(i+1). This follows directly by moving the outward
normal −∂xi to the first position, including the chart transition for the
first wall.

**COMPUTATIONALLY-VERIFIED (independent exact map derivatives).** For each
of the ten spurion walls and each of the ten alternating-singleton n8
walls, differentiate the normalized target chart

```
Q=(CZ)[:,0:2]^(-1)(CZ)[:,2:6]
```

in row-major order. The derivative is computed directly as
dQ=A^(-1)(dB−dA Q), independently of the kernel/cofactor calculation. At
the positive rational moment-curve Z and the point with all surviving
wall coordinates equal to1, both parents give the Jacobian sign vector

```
(+,+,+,−,−,−,−,+,+,+).
```

One common reversal of this raw target-chart orientation makes
epsilon_i=−eta_i sign Jac(f|W_i) hold for all twenty walls. The exact
rational determinants and chart choices are recorded in
fixtures/run3/spurion_sign_jacobians.json. These checks do not construct
a complete oriented cellular boundary, and finite Jacobian evaluations
alone are not being used to certify arbitrary maps or all-Z relations.

**COMPUTATIONALLY-VERIFIED (nonadmissible regression).** In the same
eight-variable positive chart of the four-mass cell(12)(34)(56)(78), with
coordinates(a2,b3,b4,c5,c6,u,v,w) and final entry vw/u, the two positive
preimages in LARGER_SUPPORT.md have the same normalized Y but Jacobians

```
78400/531441,
-230584300921369395200/2687716502935630973361.
```

Their signs are opposite. Thus the map-Jacobian factor cannot be replaced
by a universally positive degree or suppressed when considering
nonadmissible or repeated-cover source cells. This remains a fixed-Z
noninjectivity/orientation certificate, not a geometric tile relation.

Independent proof audit: [REVIEW.md](REVIEW.md).
