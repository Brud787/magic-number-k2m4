# Why the repaired spurion relation has five terms on each side

**PROVED, independently reviewed.** The signs of the already
certified repaired spurion relation follow from three uniform symbolic
calculations: ordered-basis Cramer signs, one factorized complementary
minor, and a positive Plucker-ratio identity. No numerical Z or ten
unrelated wall samples are needed in this argument.

We retain the chart and notation of research/run2/SPURION_ATTEMPT.md:

```
C = [a1 a2 u+v c4 c5 c6  0  0  0]
    [ 0  0   v c4 c5 c6 d7 d8 d9],
U=a1Z1+a2Z2, W=c4Z4+c5Z5+c6Z6, X=d7Z7+d8Z8+d9Z9,
Y1=U+(u+v)Z3+W, Y2=vZ3+W+X.
```

All nonvanishing chart coordinates are positive. The globally valid kernel
pivot is(a1,a2), and its orientation increases a1/a2. Rank, injectivity,
transversality and the resulting local geometric relation were independently
proved in Run2; they are not being inferred from the signs proved below.

## 1. Cramer alternation controls six walls

Use the ordered basis B=(Z1,Z2,Z3,Z7,Z8,Z9) of R6. Each Z_l for l=4,5,6 has
coordinates with signs

```
             Z1 Z2 Z3 Z7 Z8 Z9
sign          +  -  +  +  -  + .
```

Indeed each coordinate is a positive ordered6-minor divided by det B,
with the sign introduced by moving the inserted label to its ordered
position. Consequently

W=A1 Z1−A2 Z2+A3 Z3+A7 Z7−A8 Z8+A9 Z9,

where every A_i is strictly positive. The same statement holds when one
c-coordinate vanishes, because two positive summands remain in W.

Parameterize the projective fiber by requiring its image row difference
to be Y1−tY2. Its coefficients in the basis B determine

\[
\begin{aligned}
a_1(t)&=a_1+(1-t)A_1,& a_2(t)&=a_2-(1-t)A_2,\\
u(t)&=u+(1-t)(v+A_3),\\
d_7(t)&=t d_7-(1-t)A_7,&
d_8(t)&=t d_8+(1-t)A_8,&
d_9(t)&=t d_9-(1-t)A_9.
\end{aligned}
\]

The point at hand is t=1. Since a1 decreases and a2 increases with t, this
parameter runs opposite to the fixed increasing-a1/a2 orientation. At the
respective walls these formulas give image-side signs

```
a1:+, a2:−, u:+, d7:−, d8:+, d9:−.
```

This is a single ordered-minor sign argument. No individual wall rank
sample enters it. Existence and uniqueness of the remaining coefficients
along this parameter follow from the already proved global kernel pivot.

## 2. One cofactor factorization controls all three c-walls

Write B_I=⟨Y Z_I⟩ for the ordered four-bracket, with the sign of the displayed
Y representative. Complementary determinants of the quotient matrix M_Y
can be written in these brackets, up to a common *positive* square factor
from the quotient-coordinate choice. The pivot determinant factors as

\[
D_{01}=-B_{3456}B_{3789}>0.
\]

Here B3456=det(U,Z3,Z4,Z5,Z6,X)>0 and
B3789=−det(U,Z3,W,Z7,Z8,Z9)<0, by ordered positive-minor expansions.

Number chart coordinates from0. For the c-coordinate i∈{4,5,6}, delete
column1 (a2) and column i from M_Y. Subtract the surviving top E3 column
from the diagonal E3 column. The resulting block determinant immediately
factors as

\[
D_{1i}=B_{13,J}B_{3789},\qquad
J=\{4,5,6\}\setminus\{i\},
\]

where J is in increasing order. On the wall c_i=0,

\[
B_{13,J}=-a_2\det(Z_1,Z_2,Z_3,Z_J,X)<0.
\]

Both factors are negative, so D1i>0. The normalized kernel cofactor formula
from SIGN_FORMULA.md gives

K_i0=(-1)^(i+1)D1i/D01.

Since a2>0 on each open c-wall, this is its endpoint sign. Thus the entire
middle class has signs c4:−, c5:+, c6:−. The coordinate indices and labels
coincide here because the chart includes both u and v before c4.

## 3. The v-wall has a positive Plucker-ratio certificate

The remaining wall v=0 is the spurion(123)(456)(789). Its transversality was
proved from its known all-Z injectivity; therefore its endpoint sign cannot
change on its connected positive chart. We determine that sign at a
symbolic boundary limit, for an arbitrary positive Z, rather than at a
numerical external matrix.

Set u=c5=c6=d8=d9=0 while retaining a1,a2,c4,d7>0 and v=0. The pivot
determinant remains strictly positive by the same formulas in Section2,
so the kernel and its wall derivative extend continuously to this limit.
Direct block-Laplace expansion of the complementary determinant gives

\[
D_{13}=a_2c_4d_7(a_1F_2+a_2F_1),
\]

up to the same positive quotient factor, where z_I denotes an ordered
6-minor of Z and

\[
\begin{aligned}
F_2&=z_{123467}z_{145789}-z_{123457}z_{146789},\\
F_1&=z_{123467}z_{245789}-z_{123457}z_{246789}.
\end{aligned}
\]

Both are strictly positive. To see this without an unsupported difference
of positive quantities, take the alternating-twisted orthogonal complement
of Z in Gr>0(3,9), with Plucker coordinates p_I=z_[9]\I, up to one positive
normalization. Then uniformly for r=1,2,

\[
F_r=p_{589}p_{r36}-p_{689}p_{r35}.
\]

Two ordinary three-term Plucker identities yield the positive Laurent
expression

\[
\boxed{p_{358}F_r
=p_{589}p_{r38}p_{356}+p_{r35}p_{389}p_{568}>0.}
\]

For completeness, the two identities used are

\[
p_{r36}p_{358}-p_{r35}p_{368}=p_{r38}p_{356},\qquad
p_{368}p_{589}-p_{358}p_{689}=p_{389}p_{568}.
\]

Every minor on the right is positive and p358>0. Hence D13>0 at the limit.
The cofactor sign for i=3 is positive, so the v-wall endpoint sign is + in
a neighborhood of that limit inside the open wall. Transversality and
connectedness extend it to the whole wall for each positive Z. This uses
injectivity independently of any cardinality assertion and is therefore
not a circular balancedness argument.

## 4. The resulting conservation and its precise scope

The full oriented coefficient vector is

```
(a1,a2,u,v,c4,c5,c6,d7,d8,d9)
( +, −,+,+, −, +, −, −, +, −).
```

Its sum is structurally

\[
(1-1)+(1+1)+(-1+1-1)+(-1+1-1)=0.
\]

The two pivot walls cancel; the split singleton contributes+2; the two
three-element classes each contribute−1. Together with the independently
proved local indicator identity, this explains the repaired5↔5 count.

This proves a sign theorem for the repaired spurion source pattern and its
cyclic/reflection/zero-insertion images. It is not a classification of all
four-class parent patterns and gives no relation-generation theorem.
The Plucker-ratio argument is standard determinant algebra; no claim of
novel positivity technology is made.

**Kill-tests for extension:** a nontransverse admissible wall would invalidate
the sign-continuation step; a sign-indefinite analogue of F_r would invalidate
the special-class count; nonlinear positive fibers or rank-one endpoint
incidence of full image dimension would invalidate the endpoint relation
mechanism. Finally, even convex interval fibers alone can have unbalanced
wall relations, as the triangle example in SIGN_FORMULA.md shows.

## Exact verification

src/magic_number/oriented_fibers.py implements the common cofactor formula.
Tests verify every kernel2-minor against independent exact elimination,
check the two Plucker identities, and compare the resulting signs with the
previously archived direct wall evaluations. Those archived evaluations
are regressions, not the proof of the symbolic sign theorem above.

## A--F: separate geometric inputs from the wall-type count

Each assertion below is **PROVED** at the repaired-parent scope; the
geometric proofs A--E are preserved in Run2 and have been rechecked against
the symbolic calculation. No implication from A--E alone to F is used.

| Item | Actual reason | Dependencies |
|---|---|---|
| A. One-dimensional fiber | Ten homogeneous source coordinates, eight independent image-containment equations, and a globally nonzero (a1,a2) pivot give a two-dimensional kernel before projectivizing. | Rank two, external dimension six, quotient dimension four, explicit source profile. Dimension subtraction alone is insufficient. |
| B. Positive fiber is an interval | The complete source chart is a projective positive orthant. The fixed image equations are linear. Normalizing a1+a2=1 gives a bounded intersection of half-lines. | Three normalized projective directions, one singleton between them, cyclic positivity, linearity. It fails when proportionality or an additional order inequality remains. |
| C. Generic walls are transverse | All ten selected walls are independently admissible; a nontransverse coordinate wall would contain a positive projective interval of distinct preimages. | The published spurion and BCFW injectivity theorems, plus the full linear source chart and pivot. Differential rank alone is not used to certify a tile. |
| D. Signs are all-Z constant | A continuous nonzero normal component on the connected positive wall/external-data space cannot change sign. The calculations above determine that sign by ordered minors and a positive identity. | Total positivity, connectedness, proven nonvanishing and a common oriented pivot. No finite sample is promoted by itself. |
| E. Image identity has multiplicity one | Generic interval endpoints lie in single open admissible walls. Two-zero strata have image dimension at most seven; rank-one chart limits force an image line in span(Z1,Z2,Z3), an exceptional incidence family of dimension at most six. Injectivity and open-image arguments give disjointness; compact source closures give closed union equality. | Complete endpoint audit, positivity, global injectivity, and lower-dimensional strata retained before passing to indicator classes. |
| F. Five wall TYPES have each sign | The symbolic coefficient sum is (1−1)+(1+1)+(−1+1−1)+(−1+1−1)=0. The two signs at the split singleton are both positive; each three-element class has alternating net sign −1. | Ordered positive six-minors, cofactor parity, the specific cyclic class pattern, and the positive Plucker-ratio identity for v. This is the separate balance mechanism. |

The twisted orthogonal complement used for the positive Plucker identity is
linear-algebraic duality of external positive subspaces. It does not invoke
amplituhedron parity duality or turn this problem into the m2 Magic Number
theorem. Parameter count explains A; evenness and ordered-minor signs enter
F. The reflection explanation of the new n8 prototype is different: this
asymmetric spurion parent has no corresponding stabilizing reflection.

Independent proof audit: [REVIEW.md](REVIEW.md).
