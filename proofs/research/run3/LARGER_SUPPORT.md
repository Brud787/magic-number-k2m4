# Run 3: two full-support n=8 parent prototypes

This bounded analysis treats two nine-dimensional rank-two source parents. It produces one certified all-Z local relation and one exact failure of the connected-fiber shortcut. Neither result classifies complete tilings. No novelty is claimed; literature equivalence remains a separate audit.

## 1. Alternating singleton classes: an all-Z 5-for-5 relation

**PROVED.** Let

\[
P=(12)(3)(45)(6)(78)\subset\mathrm{Gr}_{2,8}^{\ge0}.
\]

The ten coordinate walls in the chart below are admissible all-Z BCFW tiles and give an all-Z, multiplicity-one local `5<->5` relation. The covered closed region on either side is the closure of the open parent image. Source incidence, tile injectivity and image equality are proved or sourced separately below.

Normalize the directions of `(12),(45),(78)` to horizontal, diagonal and vertical. The remaining singleton directions lie in the two intervening projective intervals. The full parent is therefore parameterized by the projective positive orthant with ten coordinates

\[
x=(a_1,a_2,u,v,c_4,c_5,w,t,e_7,e_8)>0,
\]

\[
C(x)=\begin{pmatrix}
a_1&a_2&u+v&c_4&c_5&w&0&0\\
0&0&v&c_4&c_5&w+t&e_7&e_8
\end{pmatrix}.
\]

The normalization is unique up to simultaneous scalar multiplication. Positivity of `u,v,w,t` imposes precisely the strict cyclic order of the five directions. The chart is consequently a global parametrization of the positive source cell, not just a differential chart near one point.

**COMPUTATIONALLY-VERIFIED / SOURCE-VERIFIED.** Setting one coordinate to zero gives ten distinct eight-dimensional source facets. Each has an explicit general BCFW recipe in `fixtures/run3/linear_n8_alternating.json`, certified by the source product and the all-Z BCFW injectivity theorem. The complete source-facet enumeration gives eleven facets; the missing one merges `(78)` and `(12)`. Its class profile is `(4,1,2,1)`, and the class-complement argument of Run 2 bounds its image dimension by seven for every positive external matrix. Thus it is rigorously collapsed; no numerical-rank exclusion is used.

## 2. Exact linear fibers, rank and a global pivot

Fix an arbitrary positive `8 by 6` external matrix `Z`, a point `Y` in the open parent image or one of the ten selected open facet images, and let `E_i` be the image of `Z_i` in the four-dimensional quotient `R^6/Y`. The fixed-image fiber is given by `M_Y x=0`, where the ten columns of `M_Y` are

\[
(E_1,0),(E_2,0),(E_3,0),(E_3,E_3),
(E_4,E_4),(E_5,E_5),(E_6,E_6),(0,E_6),(0,E_7),(0,E_8).
\]

This equation means both rows of `C(x)Z` belong to `Y`. For a rank-two nonnegative source representative, positivity of `Z` ensures its image has rank two, so containment is equality of row spaces.

Write

\[
A=a_1Z_1+a_2Z_2,\quad C=c_4Z_4+c_5Z_5,\quad E=e_7Z_7+e_8Z_8.
\]

All three sums are nonzero positive combinations on the parent and on every selected open wall. Representatives of the image plane are

\[
Y_1=A+(u+v)Z_3+C+wZ_6,\qquad
Y_2=vZ_3+C+(w+t)Z_6+E.
\]

**PROVED.** `M_Y` has rank eight throughout this locus. A dual kernel element consists of covectors `alpha,beta`, both annihilating `Y`, with `alpha` killing `Z1,Z2,Z3`, `beta` killing `Z6,Z7,Z8`, and `alpha+beta` killing `Z3,Z4,Z5,Z6`. Hence `beta` also kills `Z3`. But

\[
\det(Y_1,Y_2,Z_3,Z_6,Z_7,Z_8)
=-\det(A,Z_3,C,Z_6,Z_7,Z_8)<0.
\]

The negative sign follows by one transposition; the determinant on the right is a strictly positive sum of ordered six-minors. Thus `beta=0`, and then `alpha` kills the six independent external rows `Z1,...,Z6`, so `alpha=0`.

**PROVED.** Projection of `ker M_Y` onto `(a1,a2)` is an isomorphism. Delete the first two columns of `M_Y`. The same argument still forces `beta=0`. The remaining equations force `alpha` to kill `Z3,Z4,Z5,Z6`, and annihilation of `Y` forces it to kill `A,E`. These six vectors are independent since

\[
\det(A,Z_3,Z_4,Z_5,Z_6,E)>0.
\]

This proves that the remaining eight-column matrix is invertible. It supplies a globally continuous kernel basis `K_Y` whose first two rows are the identity. The kernel and its normalization are independent of any temporary quotient-coordinate choice.

## 3. Wall transversality and orientation

**PROVED using SOURCE-VERIFIED tile injectivity.** Removing any one wall column from `M_Y` leaves rank eight at every point in that open wall. Otherwise its kernel would have dimension at least two; positivity of the other nine coordinates would give a nonconstant local projective interval of preimages inside the same wall. The global source-wall chart and the all-Z BCFW injectivity theorem exclude this possibility. This argument establishes wall transversality from injectivity, rather than inferring injectivity from a differential rank.

Orient each projective fiber by the tangent

\[
T_Y(x)=K_Y(a_2,-a_1)^T.
\]

Its wall component is nonzero by transversality. The sign is continuous on the product of the positive external-matrix space and the open source wall. This product is connected: the positive Grassmannian top cell and the positive projective wall chart are connected, and the oriented change-of-basis group `GL^+(6)` is connected. The sign is therefore constant for every positive `Z` and every point of the open wall.

**COMPUTATIONALLY-VERIFIED, with the preceding all-Z nonvanishing proof.** Exact evaluations at `Z_i=(1,i,i^2,...,i^5)` with all nonvanishing source coordinates equal to one give:

| Zero coordinate | Exact transverse derivative | Relation coefficient |
|---|---:|---:|
| `a1` | `1` | `+1` |
| `a2` | `-1` | `-1` |
| `u` | `14/3` | `+1` |
| `v` | `7/6` | `+1` |
| `c4` | `-125/24` | `-1` |
| `c5` | `85/24` | `+1` |
| `w` | `-7/6` | `-1` |
| `t` | `-14/3` | `-1` |
| `e7` | `5/3` | `+1` |
| `e8` | `-1/3` | `-1` |

Every derivative is independently recomputed by solving the ambient twelve-equation system `C(x)Z=H Y`, with four additional row-operation unknowns, without choosing quotient coordinates. The samples fix already-proved constant signs; finite evaluations alone would not establish these signs for all `Z`.

## 4. Closed region equality and multiplicity one

**PROVED.** For any `Y` in the open parent image, the nonnegative projective kernel is an interval with nonempty interior. Normalize `a1+a2=1`: the global pivot identifies the closed kernel cone section with a closed interval inside `0<=a1<=1`, cut out by ten linear inequalities. It is bounded, and its endpoints have opposite inward orientation.

Outside a lower-dimensional exceptional set, each endpoint has exactly one zero coordinate and is therefore in one selected open facet. Here are the needed exceptional-set bounds. Rank-two coefficient vectors with two or more zero coordinates range over finitely many projective faces of dimension at most seven, so their image has dimension at most seven. If `C(x)` has rank one while `a1+a2=1`, its second row must vanish. This forces `v=c4=c5=w=t=e7=e8=0`; the image of its nonzero row is a line in `span(Z1,Z2,Z3)`. Choosing such a line has dimension at most two, and choosing a two-plane containing it has dimension four, so the corresponding exceptional incidence image has dimension at most six. Rank-deficient coefficient matrices therefore do not hide an additional full-dimensional family of endpoints.

The open parent image is open: a positive solution persists under small changes of `Y` by the smooth global kernel pivot. Conversely, every open selected wall image lies in this open parent image, because its transverse fiber direction moves from the wall into the strictly positive orthant. Off the exceptional set, the two endpoints thus give one preimage in a positive-coefficient wall and one in a negative-coefficient wall, with multiplicity one.

Each selected open tile image is open by injectivity and invariance of domain. If two images on the same side intersected, the intersection would be nonempty open and would contain a point outside the exceptional set, contrary to uniqueness of the appropriate fiber endpoint. Thus same-side open tile images are exactly disjoint.

Finally, compactness of the source cell closures makes each closed tile the closure of its open image. Source incidence puts every selected closed image in the closure of the parent image, while generic endpoint coverage gives the reverse inclusion for each finite side union. The two closed unions are therefore equal. Lower-dimensional boundaries affect neither the indicator-class identity nor multiplicity one on open tiles.

Consequently the Level A, all-Z relation is

\[
[T_{a_1}]+[T_u]+[T_v]+[T_{c_5}]+[T_{e_7}]
-[T_{a_2}]-[T_{c_4}]-[T_w]-[T_t]-[T_{e_8}]=0.
\]

Its coefficient sum is exactly zero. Cyclic/reflection transforms and order-preserving loop insertions transport this certified relation; they do not prove generation of all relations. The separate [reflection criterion](SIGN_FORMULA.md#a-checkable-reflection-criterion) explains the sign pairing without the evaluation table: reflection reverses the nine-dimensional source orientation and preserves the eight-dimensional target orientation. The global pivot proves submersion, and all ten walls have constant transverse signs. The criterion therefore pairs their signs oppositely. It is a theorem under explicit geometric hypotheses, not a balance assertion inferred merely from a symmetric facet list.

## 5. Adjacent singleton classes: the quadratic obstruction

**PROVED.** The other parent

\[
Q=(12)(34)(56)(7)(8)
\]

has a different positive fiber geometry. Normalize its three nonsingleton directions to horizontal, diagonal and vertical. Its chart is

\[
C_Q(x)=\begin{pmatrix}
a_1&a_2&b_3&b_4&0&0&-u&-w\\
0&0&b_3&b_4&c_5&c_6&v&t
\end{pmatrix},\qquad x>0,
\]

with the additional essential inequality

\[
\Delta_{78}=vw-ut>0.
\]

All other increasing two-minors are automatically nonnegative with the required support. The inequality orders the two free singleton directions in the same projective interval. The homogeneous image-fiber equations are still linear, but their intersection with the source chart also retains this quadratic inequality.

Its eight ordinary linear walls are the six anchor-coordinate deletions, `u=0` and `t=0`; all are certified BCFW tiles. The wall `vw=ut` merges `(7),(8)` and is the nonadmissible four-mass source `(12)(34)(56)(78)`. Two further source facets merge adjacent double classes into a class of size four, and their image dimensions are at most seven by the class-complement bound. The apparent nine-boundary full-rank pattern therefore contains a non-tile and cannot be used as a nine-term tile-indicator relation.

## 6. An exact disconnected fiber and positive four-mass pair

**PROVED by an explicit exact fixed-Z certificate.** Let `Z_i=(1,i,...,i^5)` for `i=1,...,8`. Its six-minors are strictly positive Vandermonde products. Take

\[
x_0=(1,1,1,1,1,1,1,4,1,4),
\]

and define

\[
h=(1,-1,53/16,-59/16,75/8,-37/8,21/4,35/4,17/4,23/4).
\]

The entire normalized image fiber through `x0` is `x(s)=x0+s h`; its matrix of quotient equations has rank eight, and the independent ambient system gives the same tangent. The strict positive-orthant condition is exactly

\[
-8/75<s<8/37,
\]

whereas direct substitution gives

\[
\Delta_{78}(x(s))=s(7s-1).
\]

Hence the actual positive-parent fiber is the disconnected union

\[
(-8/75,0)\ \cup\ (1/7,8/37).
\]

The two quadratic endpoints, `s=0` and `s=1/7`, give distinct positive points of the same four-mass source cell with the same amplituhedron image. Explicit representatives are

\[
C_0=\begin{pmatrix}1&1&1&1&0&0&-1&-1\\0&0&1&1&1&1&4&4\end{pmatrix},
\]

\[
C_1=\begin{pmatrix}
8/7&6/7&165/112&53/112&0&0&-7/4&-45/28\\
0&0&165/112&53/112&131/56&19/56&21/4&135/28
\end{pmatrix}.
\]

All ordered two-minors are nonnegative and precisely the four pair minors `12,34,56,78` vanish for each matrix. Their row spaces are distinct: `Delta13/Delta23` is `1` for `C0` and `4/3` for `C1`. Yet direct exact multiplication verifies

\[
C_1Z=\frac1{112}\begin{pmatrix}123&-15\\1&137\end{pmatrix} C_0Z,
\]

with positive nonzero determinant `8433/6272`. This is a positive real noninjectivity witness, stronger than a degree-two or differential-rank observation, and independently verifies the relevant Galashin--Lam nonadmissibility input at one explicit positive external matrix.

The two ordinary fiber endpoints are the BCFW walls `c5=0` at `s=-8/75` and `c6=0` at `s=8/37`; their order minors are `1048/5625` and `152/1369`, respectively, both positive. Their presence does not allow the quadratic boundary contribution to be discarded. No image relation among the eight admissible ordinary walls has been certified by this calculation.

**FAILED (structural shortcut).** A nine-dimensional rank-two parent need not have connected positive image fibers even when the ambient homogeneous fiber equations are linear. Adjacent free directions can produce a quadratic positivity constraint, two fiber intervals, and repeated images of a nonadmissible boundary. Consequently convex interval endpoint arguments require a proved orthant/convex-fiber hypothesis. This fixture does not give an unbalanced tile relation or a Magic Number counterexample.

## Reproduction

```sh
PYTHONPATH=src .venv/bin/python -m magic_number.linear_parent_fibers
PYTHONPATH=src .venv/bin/python -m pytest tests/test_linear_parent_fibers.py -q
```

Fixtures: `fixtures/run3/linear_n8_alternating.json` and `fixtures/run3/linear_n8_adjacent_disconnected.json`. The four new tests pass; they independently check all ten orientations using ambient elimination, the complete source-facet partition, the essential quadratic inequality and the explicit distinct positive four-mass preimages with equal image row spaces. No long enumeration of complete tilings was performed.
