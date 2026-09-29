# Run 3: conic fibers, positive multiplicity, and a missing facet cover

**PROVED by an exact finite certificate; independently audited in [REVIEW.md](REVIEW.md).** For the nine-dimensional parent
\[
P=(12)(34)(56)(789),
\]
there is an explicit positive rational external matrix and an open subset of its image which none of its eight admissible source-facet tiles covers. The obstruction is a conic fiber with both endpoints in the same nonadmissible four-mass source facet. This disproves a proposed universal strategy of covering every parent image by its admissible facet tiles. It does not disprove Magic Number, rule out a cover using other tiles, or produce an unbalanced relation among admissible tiles.

At the same fixed external matrix, the positive preimage count of the four-mass facet takes the values zero, one, and two at three explicit target planes. At the two-preimage target the two ordinary local Jacobian signs are opposite. Algebraic degree two therefore cannot be substituted for a constant positive or signed multiplicity in a boundary identity. All multiplicity statements in this document are about this explicit fixed `Z`; the conic chart and its linear rank argument have the all-`Z` scope stated below.

## 1. A global positive source chart and a plane quadric

Let
\[
x=(a_1,a_2,u_3,v_3,u_4,v_4,c_5,c_6,d_7,d_8,d_9)
\]
and
\[
C(x)=\begin{pmatrix}
a_1&a_2&u_3+v_3&u_4+v_4&c_5&c_6&0&0&0\\
0&0&v_3&v_4&c_5&c_6&d_7&d_8&d_9
\end{pmatrix},\qquad
Q(x)=u_3v_4-u_4v_3.
\]
The conditions `x_i>0` and `Q(x)=0`, modulo common positive scaling, parameterize exactly the open source cell `P`. To see completeness, normalize its ordered, distinct directions at `(12),(56),(789)` to `(1,0),(1,1),(0,1)`. A projective transformation of the line taking three distinct directions to these three is unique; the remaining freedom in the matrix is common scaling. The `(34)` direction lies strictly between the first two, so its columns uniquely have the displayed positive `u,v` coordinates. Their proportionality is precisely `Q=0`. Conversely the displayed conditions make exactly the required minors positive or zero.

For fixed `Y` and positive `Z`, let `M_Y` be the eight homogeneous linear equations expressing row containment `C(x)Z subset Y`. The columns of `M_Y` are implemented by projecting the nine external rows into `R^6/Y`. Its kernel is a three-dimensional vector space whenever `Y` lies in the open parent image. In fact projection of this kernel to `(a_1,a_2,d_9)` is an isomorphism. Thus the source fiber is the positive part of a homogeneous quadric in a projective plane. A plane quadric can be singular or reducible; this argument does not assert universal smoothness or connectedness.

Here is a positive-minor proof of the fixed eight-by-eight pivot, valid for every positive `Z` and every `Y=C(x)Z` with `x>0,Q=0`. Write
\[
U=a_1Z_1+a_2Z_2,\quad W=c_5Z_5+c_6Z_6,
\quad X=d_7Z_7+d_8Z_8+d_9Z_9.
\]
A dual dependence on the eight columns other than `(a_1,a_2,d_9)` consists of covectors `alpha,beta` annihilating `Y` such that
\[
\alpha(Z_3)=\alpha(Z_4)=0,\quad
\beta(Z_3)=\beta(Z_4)=\beta(Z_7)=\beta(Z_8)=0,
\quad(\alpha+\beta)(Z_5)=(\alpha+\beta)(Z_6)=0.
\]
Modulo `Z_3,Z_4,Z_7,Z_8`, the two rows of `Y` are `U+W` and `W+d_9Z_9`. Hence
\[
\det(Y_1,Y_2,Z_3,Z_4,Z_7,Z_8)
=\det(U,W,Z_3,Z_4,Z_7,Z_8)
+d_9\det(U+W,Z_9,Z_3,Z_4,Z_7,Z_8)>0.
\]
Every term expands with positive coefficients into ordered positive six-minors; the first summand is strictly positive. It follows that `beta=0`. Then `alpha` annihilates `Z_3,Z_4,Z_5,Z_6,U,X`, whose determinant, in that order with `U` first and `X` last, is strictly positive. Therefore `alpha=0`. This proves the pivot claim. It also applies to the displayed four-mass endpoints, where `d_9=0` while `U,W,X` remain positive nonzero combinations.

## 2. The exact fixed external matrix and three target planes

Throughout the remaining calculations
\[
Z_i=(1,i,i^2,i^3,i^4,i^5),\qquad 1\le i\le9.
\]
Every ordered maximal minor is a strictly positive Vandermonde determinant. Normalize `a_1=1`, write `t=a_2,s=d_9`, and use the fixed pivot above to solve all other coordinates linearly in `(1,t,s)`.

The complete reproducible data are in [hostile_conic_multiplicity.json](../../fixtures/run3/hostile_conic_multiplicity.json). The three cases are:

| Positive four-mass preimages | Source seed | Target representative `Y` | Positive parent parameter interval |
|---:|---|---|---|
| 0 | all eleven coordinates 1 | `(8,28,116,532,2612,13468); (7,42,280,2016,15316,120792)` | `(10/37,61/37)` |
| 1 | first ten coordinates 1, `d9=0` | `(8,28,116,532,2612,13468); (6,33,199,1287,8755,61743)` | `(1,125/77)` |
| 2 | `(1,3,12,3,16,4,1,1,5,1,0)` | `(41,143,529,2051,8305,35123); (15,79,461,2905,19289,132529)` | `(1853/897,3)` |

In the zero-preimage case the conic equation and its `s=0` roots are
\[
Q=-\frac4{2457}(2487st-4755s+271t^2-2168t+4165),
\qquad t=4\pm\frac{3\sqrt{5149}}{271}.
\]
Neither root gives positive source coordinates. In the one-preimage case
\[
Q=-\frac7{48}(163st-307s-5t^2+26t-21),
\qquad s=\frac{(t-1)(5t-21)}{163t-307}.
\]
Only the root `t=1` is positive; the other root `21/5` has negative coordinates. The positive parent interval has one endpoint on `d9=0` and the other on the admissible deletion wall `c5=0`. Omitting the nonadmissible wall is already incompatible with the full fiber-boundary equation in this example.

For the two-preimage case,
\[
Q=-\frac{7161st-58373s-897t^2+4544t-5559}{196},
\qquad
s=\frac{(t-3)(897t-1853)}{217(33t-269)}.
\]
The two positive solutions on `d9=0` are the seed above at `t=3` and
\[
\left(1,\frac{1853}{897},\frac{68644}{6279},\frac{175016}{43953},
\frac{5633}{483},\frac{14362}{3381},\frac{14240}{6279},\frac{836}{2093},
\frac{1914}{299},\frac{3110}{2691},0\right).
\]
The tests verify all two-minors, the exact source labels, and image equality by an explicit invertible row-change matrix. These two distinct positive points lie in the same four-mass source `(12)(34)(56)(78)`, with loop 9. Thus this particular external matrix explicitly witnesses its noninjectivity, independent of its already published nonadmissibility certificate.

The quadratic root lists are complete. Positive points on the four-mass cell always have `a1>0`, so the chart cannot miss any such preimage. Exact rational/algebraic sign decisions establish the counts; no floating-point sampling is used.

## 3. Real multiplicity and local degree are different

Orient the affine conic by the tangent `(Q_s,-Q_t)`. At the two positive `d9=0` roots the oriented normal components are `+419/98` and `-419/98`.

A separate computation uses ordinary local coordinates on the four-mass source:
\[
(a_2,r,v_3,v_4,c_5,c_6,d_7,d_8),\quad
u_3=rv_3,\ u_4=rv_4,\ a_1=1,\ d_9=0.
\]
Write the target matrix as `Y=(A|B)`, where `A` is its first two columns. Target coordinates are the eight entries of `A^{-1}B`, flattened by rows. The Jacobian signs at the smaller and larger root are positive and negative respectively. Their exact values are
\[
\frac{5783630776718626693127887302442190976}
{93660165384315673602764368138643228674225},\qquad
-\frac{2298946406400}{26786992617986329}.
\]
At the one-preimage target the Jacobian is `1225/32>0`. All roots are simple and all positive coordinates are strict, so these positive multiplicities and local signs persist in sufficiently small target neighborhoods. Complex degree two, unsigned positive multiplicity, and the sum of real local orientation signs are therefore distinct quantities.

**FAILED (constant-degree shortcut).** Under the usual regularity, orientation, and compactness hypotheses, the boundary of a real one-dimensional fiber gives a pointwise identity
\[
\sum_F\ \sum_{x\in F^{>0}:\ \widetilde Z(x)=y}
\epsilon(x,y)=0.
\]
One may group the inner sums as signed real-preimage functions of `y`. This is not a sum of fixed signs over wall types, and replacing those functions by complex degrees is unjustified. Even injectivity alone does not force the constant coefficient sum to vanish: project a triangle with vertex coordinates `0,1,2` to the horizontal axis. The long edge maps once onto `(0,2)`, while the other two map once onto `(0,1)` and `(1,2)`. Away from their endpoints the resulting identity has one term versus two, although every map has degree one. Additional amplituhedron structure would be needed to force balance. No all-parent or all-tiling signed-degree theorem is claimed here.

## 4. Excluding every admissible closed facet image

The eight admissible facets of `P` are deleting one of columns `1,2,3,4,5,6`, merging `(12)` with `(34)`, and merging `(34)` with `(56)`. Each has an explicit all-Z BCFW recipe, copied into [hostile_closed_facet_exclusion.json](../../fixtures/run3/hostile_closed_facet_exclusion.json). The remaining source facets are the three nonadmissible four-mass walls obtained by deleting `7,8,9`, and the two collapsed mergers involving `(789)`. These thirteen facets form the complete source-facet list by the rank-two source classification. The two B mergers are present in the conic chart as `v3=v4=0` and `u3=u4=0`; omitting them would invalidate a closed-image exclusion.

Let `Y_*` be the two-preimage target in Section 2. A full projective chart audit and a source-closure audit show that **the only closed source-facet image containing `Y_*` is the four-mass facet with loop 9**. Here are the details, including source degenerations where normalizing three directions is impossible.

1. **Exclude all failures of the three-direction gauge.** In every source stratum of the closure of `P`, the surviving elements of each original block remain parallel. Say that the gauge is valid when `(12),(56),(789)` each has a surviving nonzero column and their three directions are distinct. There are exactly 3033 rank-two positroid strata in this closure. A basis-inclusion enumeration and an independent recursive source-facet traversal agree on all their affine labels. Exactly 2403 strata fail the gauge criterion. For every one of them the certificate records a parallel class whose complementary nonloop support has at most four elements.

   This is an exclusion by exact Schubert incidence, not by a sampled Jacobian. A row functional killing that parallel class gives a nonzero vector of the image plane supported on the complementary external rows. Extending those at most four row indices to a four-set `I` forces `det(Y,Z_I)=0`. All 126 such determinants at `Y_*` are explicitly nonzero. Thus no gauge-invalid source stratum, including any lower-dimensional or wrap-around merger, can map to `Y_*`. The elementary incidence argument is also recorded in [Run 2's class-complement proof](../run2/PARENT_ENUMERATION.md#class-complement-obstruction). The complete finite source list and an individual obstruction witness for every excluded stratum are preserved; this completeness check does not depend on source-facet image-rank guesses.

2. **The remaining nonnegative chart is complete.** With three distinct nonzero anchor directions, the normalization of Section 1 remains unique on the source closure. Its coordinates are nonnegative; the other original direction can now coincide with either neighboring anchor, and original columns can vanish. Conversely these are exactly the degenerations described by nonnegative coefficients and `Q=0`, provided the three anchor blocks remain nonzero and distinct.

   The omitted projective line `a1=0` meets the kernel conic at the two points `K(0,0,1)` and `K(0,1,299/2387)`. The former has negative `u3,u4,d8`; the latter has negative `c5,d8`. Here `K` is the exact kernel basis with rows `(a1,a2,d9)=I_3`. These normalizations cover all potentially nonnegative points with `a1=0`, so neither point is a valid nonnegative source preimage. With `a1=1`, the only apparent exceptional value for solving the conic for `s`, namely `t=269/33`, does not solve the conic at all: its non-`s` term is nonzero.

3. **The entire nonnegative locus has just two boundary points.** Substitution of the exact rational graph gives
\[
\begin{split}
x(t)=\bigg(&1,t,
\frac{6(3t-43)(3t+481)}{49(33t-269)},
\frac{3(3t+481)(21t-97)}{98(33t-269)},\\
&\frac{2(3t-43)(429t+673)}{49(33t-269)},
\frac{(21t-97)(429t+673)}{98(33t-269)},
-\frac{19t-71}{14},\frac{9t-13}{14},\\
&\frac{18411t^2+7909t-373876}{217(33t-269)},
-\frac{4029t^2-63683t+265458}{651(33t-269)},
\frac{(t-3)(897t-1853)}{217(33t-269)}\bigg).
\end{split}
\]
Exact rational-inequality elimination gives `x_i(t)>=0` if and only if `1853/897<=t<=3`. Every coordinate is strictly positive in the interior. At either endpoint only `d9` vanishes. Consequently every boundary preimage is in the open source stratum with loop 9. It belongs to none of the closures of the other twelve source facets, since those require an additional zero source minor or column that this source stratum does not have.

These three steps prove the claimed closed-image exclusion; they address the mergers absent from the strict positive chart and every lower-dimensional source degeneration. In particular all eight admissible closed tile images miss `Y_*`.

4. **There is an open hole, not just an exceptional target point.** At `t=5/2`, all eleven coordinates are positive, `s=779/161882`, and `Q_s=11563/56!=0`. The fixed linear pivot remains invertible for all sufficiently nearby target planes. The implicit function theorem therefore gives a positive source solution at every nearby target, holding `t=5/2` and solving for `s`. Hence `Y_*` belongs to the interior of the parent image in `Gr(2,6)`. Each closed source-facet image is compact and therefore closed. The finite union of the eight admissible images misses `Y_*`, so a neighborhood of `Y_*` inside the parent image misses their union as well.

**Precise obstruction.** This parent image cannot be tiled or covered by any selection of its eight admissible source-facet tiles at this `Z`. This also excludes an all-Z construction that would cover this parent using those facet tiles. It does not exclude relations supported on smaller regions, additional tiles whose source cells are not its facets, or a tiling of the full amplituhedron. It gives no unbalanced admissible-tile relation.

## 5. Literature scope and verification

The four-mass nonadmissibility is already stated in Galashin--Lam, *Parity duality for the amplituhedron*, Example 13.12; see [the primary paper](https://www.math.ucla.edu/~galashin/papers/duality.pdf) and the [Run 2 source audit](../run2/PARENT_ENUMERATION.md). No novelty claim is made for that nonadmissibility, its degree-two description, or conic descriptions familiar from four-mass geometry. The local contribution here is the exact hostile fixture and the complete source-closure exclusion needed to test the proposed parent-facet route. Failure to locate an equivalent fixture would not certify novelty.

Implementation: [conic_fibers.py](../../src/magic_number/conic_fibers.py). The tests independently verify image row spaces through ambient row-change equations, source minors, all quadratic roots and signs, the complete positive and nonnegative parameter intervals, projective exceptional points, ordinary local Jacobians, the two source-closure enumerations, all gauge-obstruction witnesses, and the open-image implicit-function certificate. No numerical generic-Z evidence is upgraded to an all-Z theorem.

```sh
PYTHONPATH=src .venv/bin/python -m magic_number.conic_fibers
PYTHONPATH=src .venv/bin/python -m pytest tests/test_conic_fibers.py -q
```

The independent proof review covers Section 4, including its exact finite completeness certificate and the closed source strata outside the positive chart. No further search or conjectural extension is part of this bounded task.
