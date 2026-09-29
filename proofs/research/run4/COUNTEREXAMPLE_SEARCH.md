# Run 4: exact obstructions from the two hostile cores

**PROVED by exact finite certificates; independently audited in [REVIEW](REVIEW.md).** Each hostile parent has eight admissible source-facet tiles whose indicator functions are linearly independent at one explicit positive rational external matrix. Consequently neither parent supports any nonzero constant-coefficient all-Z indicator relation among its admissible facets. This excludes balanced as well as unbalanced relations on those eight tiles. The certificate is exact and includes a complete membership decision for every tile at every witness target, together with an open-neighborhood check; it is not inference from finite numerical agreement.

The covering statements differ. The nine-point parent has the open hole proved in Run 3 and therefore admits no all-Z cover of its whole image using its admissible facet tiles. No corresponding covering obstruction is proved for the eight-point parent. Its failure to support a homogeneous indicator relation must not be relabeled as failure to admit a cover.

| Parent | Admissible facets | Rank of exact indicator matrix | Nonzero all-Z relation among these facets | Admissible-facet cover of whole parent |
|---|---:|---:|---|---|
| `P8=(12)(34)(56)(7)(8)` | 8 | 8 | Excluded | Unresolved |
| `P9=(12)(34)(56)(789)` | 8 | 8 | Excluded | Excluded by the Run 3 open hole |

All tilehood statements here use the existing all-Z BCFW recipe certificates. No differential-rank witness is used to certify a tile. The precise theorem is Section 4 below. No novelty claim is made for it.

## 1. The eight-point attempted covering obstruction

The positive chart for `P8` has homogeneous coordinates
\[
x=(a_1,a_2,b_3,b_4,c_5,c_6,u,v,w,t),\qquad
C_8(x)=\begin{pmatrix}
a_1&a_2&b_3&b_4&0&0&-u&-w\\
0&0&b_3&b_4&c_5&c_6&v&t
\end{pmatrix}.
\]
All ten coordinates are positive and the additional order minor is
\[
\Delta=vw-ut>0.
\]
Normalize the distinct nonzero directions of `(12),(34),(56)` to `(1,0),(1,1),(0,1)`. This gives precisely this chart modulo a common positive scale. Its eight admissible facets are the six deletions `a1,a2,b3,b4,c5,c6=0`, the merger `u=0` of `(56)` with `(7)`, and the cyclic merger `t=0` of `(8)` with `(12)`. The four-mass merger `Delta=0` is nonadmissible. The remaining two source facets are collapsed. See the existing [linear-chart proof and fixture](../run3/LARGER_SUPPORT.md).

The Run 3 nine-point four-mass pair, with its loop 9 removed, does not give an eight-point hole. Apply the row transformation `[[1,-1],[0,4]]` to its seed source matrix. At the resulting target and moment-curve external matrix, the normalized eight-point fiber is
\[
\begin{split}
x(r)=\bigg(&1,r,\frac{8r+60}{7},\frac{65r+29}{14},
\frac{1862-398r}{167},\frac{519r-889}{167},\\
&\frac{19-3r}{2},\frac{867r+4079}{334},
\frac{9-r}{6},\frac{887r+1347}{1002}\bigg),
\end{split}
\]
with
\[
\Delta(r)=\frac{(r-3)(897r-1853)}{1002}.
\]
The positive orthant interval is `(889/519,931/199)`. The positive source fiber has the two components
\[
(889/519,1853/897)\ \cup\ (3,931/199).
\]
Both components reach ordinary admissible coordinate walls. Thus importing the nine-point hole into this different parent fails.

A bounded exact search screened 80 positive rational source seeds at `Z_i=(1,i,...,i^5)` and 120 further seeds with strictly increasing positive integer moment-curve nodes. Normalizing `a1+a2=1` makes the orthant fiber a bounded interval. Its endpoint order-minor signs were `(+,+)` in 133 cases and `(-,+)` in 67 cases. No case had both endpoints negative. All 200 external matrices, source seeds, endpoint intervals, and exact order-minor values are retained in [the bounded screen fixture](../../fixtures/run4/hostile_q8_bounded_endpoint_screen.json).

**FAILED (proposed extrapolation).** These finite results do not prove an all-Z cover, prove that a particular four-tile subcollection covers the parent, or prove that a hole cannot occur. The no-cover question for `P8` remains unresolved in this bounded run. We stopped that screen and pursued a different exact obstruction.

## 2. Exact tile-indicator matrices

Use `Z_i=(1,i,i^2,i^3,i^4,i^5)` for `i=1,...,n`. Every maximal minor is a strictly positive Vandermonde determinant. The ordered columns for `P8` are
\[
(a_1=0,a_2=0,b_3=0,b_4=0,c_5=0,c_6=0,u=0,t=0).
\]
The indicator matrix at eight rational target planes is
\[
R_8=\begin{pmatrix}
0&0&0&1&0&0&0&0\\
0&0&0&1&1&0&0&0\\
0&0&0&0&1&1&0&0\\
0&0&0&0&0&1&1&0\\
0&1&0&0&1&0&0&0\\
0&1&1&0&0&0&0&0\\
1&0&0&0&0&1&0&0\\
0&0&0&0&1&0&0&1
\end{pmatrix},\qquad \det R_8=1.
\]
The corresponding source seeds are

```text
(6,5,8,2,1,9,5,1,25,4)
(5,3,2,2,1,4,4,7,26/7,3)
(6,8,2,8,5,1,9,8,75/8,3)
(4,3,9,4,1,1,1,9,79/9,7)
(5,1,2,4,4,5,1,3,6,6)
(5,1,1,9,8,6,6,7,87/7,4)
(0,1,1,1,1,1,1,4,1,1)
(1,1,1,1,1,1,1,4,1,0)
```

Each target is the row span of `C8(seed) Z`. The first six seeds lie in the open parent; the last two lie in open admissible facet cells. A point in an open tile is allowed as a witness: the needed condition is avoidance of every tile's boundary, not avoidance of every open tile.

For `P9` use the eleven-coordinate conic chart from [MULTIPLICITY.md](../run3/MULTIPLICITY.md):
\[
C_9(x)=\begin{pmatrix}
a_1&a_2&u_3+v_3&u_4+v_4&c_5&c_6&0&0&0\\
0&0&v_3&v_4&c_5&c_6&d_7&d_8&d_9
\end{pmatrix},\quad Q=u_3v_4-u_4v_3=0.
\]
Its ordered columns are deletion of labels `1,2,3,4,5,6`, merger of `(12)` with `(34)`, and merger of `(34)` with `(56)`. In coordinates the vanishing sets are
\[
\{a_1\},\{a_2\},\{u_3,v_3\},\{u_4,v_4\},
\{c_5\},\{c_6\},\{v_3,v_4\},\{u_3,u_4\}.
\]
The eight-target indicator matrix is
\[
R_9=\begin{pmatrix}
0&1&0&0&1&0&0&0\\
0&0&0&1&0&0&0&0\\
0&1&0&0&0&0&0&0\\
0&0&0&1&0&0&0&1\\
0&1&1&0&0&0&0&0\\
0&0&0&0&1&1&0&0\\
1&0&0&1&0&0&0&0\\
0&0&1&0&0&0&1&0
\end{pmatrix},\qquad \det R_9=1.
\]
The source seeds are

```text
(6,1,12,2,24,4,6,2,8,5,1)
(1,6,15,5,6,2,7,3,1,1,3)
(5,3,12,2,36,6,7,4,1,7,6)
(2,8,4,4,6,6,6,8,2,7,8)
(3,4,6,2,18,6,7,8,7,2,3)
(1,6,40,8,20,4,3,1,6,6,2)
(0,1,1,1,1,1,1,2,1,1,1)
(1,1,1,0,1,0,1,1,1,1,1)
```

The two fixtures [hostile_q8_indicator_rank.json](../../fixtures/run4/hostile_q8_indicator_rank.json) and [hostile_q9_indicator_rank.json](../../fixtures/run4/hostile_q9_indicator_rank.json) contain the exact target matrices, all solved preimages, all nonzero twistor values, source affine labels, and concrete all-Z BCFW recipes for the eight facets. Every matrix entry is an exactly certified indicator, as justified next.

## 3. Completeness and local constancy of membership decisions

**Global chart issue.** Both parents and all their source closures are described by the classical rank-two cyclic parallel-class classification. All source strata in the closure were enumerated twice: once by basis inclusion among all rank-two cells, and once by recursively taking the complete source-facet list. The resulting affine-label sets agree.

| Parent | All source-closure strata | Strata lacking three distinct nonzero anchor directions |
|---|---:|---:|
| `P8` | 1,999 | 1,621 |
| `P9` | 3,033 | 2,403 |

For each stratum in the second column of counts, the fixture records a parallel class with at most four complementary nonloop labels. Such a stratum forces a zero twistor: a row functional killing that class gives a nonzero vector in the image plane supported on those at most four external rows. Extending their indices to a four-set `I` forces `det(Y,Z_I)=0`. This is the established [class-complement argument](../run2/PARENT_ENUMERATION.md#class-complement-obstruction). All 70 twistors are nonzero at each `P8` witness, and all 126 are nonzero at each `P9` witness. Hence every possible source preimage in either parent closure has a valid three-direction gauge. This includes potential lower-dimensional preimages in a closed tile image.

**Eight-point wall equations.** The row-containment equations `C8(x) Z subset Y` have an exact rank-eight matrix and a two-dimensional kernel. The chosen pivot makes its coordinates `(a1,a2)`. Normalize `a1+a2=1`, which is legitimate for every nonnegative source preimage with a surviving anchor `(12)`. The resulting affine line meets each of the eight coordinate wall hyperplanes at exactly one point. Every intersection is computed rationally. At each intersection every other coordinate is nonzero and `Delta` is nonzero. The point belongs to that tile precisely when its other nine coordinates and `Delta` are all positive. This is a complete decision, including absence: every nonnegative closed-facet preimage has just been included, and no solved point lies in a further source boundary.

**Nine-point wall equations.** The row-containment matrix has an exact rank-eight pivot with kernel coordinates `(a1,a2,d9)`. Let `K` denote that kernel basis and `Q(K(a,b,d))` its homogeneous quadric. Each wall given by two vanishing coefficients cuts out a unique projective kernel point; both equations automatically imply `Q=0`. Its `a1` coordinate is nonzero at every witness, and the point is normalized to `a1=1`.

For `a1=0`, set `(a,b,d)=(0,1,s)` and solve the resulting linear equation `Q=0`. For the other single-coordinate walls use `(a,b,d)=(1,r,s)`, first solve the wall equation for `r`, then the linear equation `Q=0` for `s`. Every denominator and linear coefficient needed here is exactly nonzero at the witness targets.

There is one potentially omitted projective direction `(a,b)=(0,0)`. It cannot represent a rank-two nonnegative source. Indeed `C9(K(0,0,1))` has its first row supported on labels `3,4,5,6`. Since `det(Y,Z3,Z4,Z5,Z6)` is nonzero, that first row must map to zero. The four external rows are independent, so the first row itself vanishes. Therefore `c5=c6=0`, `u3=-v3`, and `u4=-v4`; the source matrix has rank one. This also proves that the `d9` coefficient in the kernel's `c5,c6` coordinates is zero and the `d9^2` coefficient in `Q` is zero, explaining the linear solves rather than assuming a numerical factorization persists.

No other projective point is omitted. A point on `a1=0` with `a2=0` is the excluded direction just discussed. On either `c5=0` or `c6=0`, imposing `a1=0` forces `a2=0` because the `a2` coefficient is nonzero in the fixture. On each double-coordinate wall the unique projective kernel point was solved directly. Thus the eight displayed candidates exhaust all nonnegative closed-facet preimages. Every coefficient not prescribed to vanish is strictly nonzero. Positivity of these other coefficients is exactly the open-facet membership condition.

**Open neighborhoods.** Nonzero pivot determinants, nonzero twistors, nonzero solved coefficients, and, for `P8`, the nonzero order minor are open conditions on the target plane. The solved candidate coordinates depend rationally on the target in such a neighborhood. Consequently the complete eight-entry membership vector remains constant on a nonempty open neighborhood of each witness. This explicitly handles indicator identities understood only away from lower-dimensional boundaries: the certificate is not supported on exceptional points.

The tests independently eliminate the twelve ambient equations `C(x)Z=L Y`, with four unknown entries of `L`, to recover each kernel without forming `R6/Y`. They also check image row spaces and test positivity using all ordered two-minors, independently of the coordinate sign criterion. The rank-two source-closure and gauge-degeneration audits are checked separately.

## 4. The precise nonrelation theorem

**PROVED, independently audited.** Let `F1,...,F8` be the eight all-Z admissible source facets of either `P8` or `P9`, and let `Tj(Z)` be their tile images. If constants `c1,...,c8` satisfy
\[
\sum_{j=1}^8 c_j\,\mathbf1_{T_j(Z)}(Y)=0
\]
for every positive external matrix `Z`, away from a lower-dimensional exceptional set of target planes, then every `cj=0`.

**Proof.** Use the single moment-curve matrix and the eight witness neighborhoods above. A lower-dimensional set cannot contain any of these open neighborhoods. Evaluation on each neighborhood therefore gives `R_n c=0`. Since `det R_n=1`, it follows that `c=0`. The proof even excludes a nonzero constant-coefficient relation at this one fixed `Z`; requiring the relation for all `Z` only weakens what needs to be refuted. The same conclusion applies to closed tile indicators or open tile indicators, since these neighborhoods meet no tile boundary. Square.

In particular there is no local replacement supported entirely on these admissible facets with multiplicity-one tilings on both sides: equality of covered regions and disjoint open images would yield just such a nonzero indicator relation after cancelling common tiles. This does not exclude a relation involving additional tiles whose source cells are not these facets, a relation including the nonadmissible four-mass source with variable real multiplicities, or abstract source-boundary identities. The proof does not infer indicator relations from canonical forms or topological boundaries.

For `P9`, the separate Run 3 open-hole theorem additionally rules out a cover of its entire parent image by these eight tiles. For `P8`, a cover would be an inhomogeneous identity involving the parent indicator, so independence of the eight facet indicators does not decide it. A claim that both hostile cores admit no admissible-facet cover would exceed the established result.

## 5. Finite scope, status, and reproduction

This branch treated precisely the two hostile cyclic source-parent profiles `q8:(1,1,2,2,2)` and `q9:(2,2,2,3)`. It did not enumerate tilings or screen arbitrary uncertified tile families. The other eleven untreated cores were assigned to separate proof branches. No credible unbalanced relation among admissible tiles was found here; the stronger obstruction is that these particular eight-tile sets admit no nonzero relation at all.

Artifacts are generated by [run4_hostile.py](../../src/magic_number/run4_hostile.py), and the concise machine-readable status is [counterexample_search.json](../../results/run4/counterexample_search.json). The 200 endpoint samples remain explicitly computational evidence with no all-Z covering conclusion. The two invertible indicator matrices, in contrast, are exact finite certificates for the stated functional-independence theorem because every entry and its neighborhood has been proved.

```sh
PYTHONPATH=src .venv/bin/python -m magic_number.run4_hostile
PYTHONPATH=src .venv/bin/python -m pytest tests/test_run4_hostile.py -q
```

Independent hostile review of Sections 3–4 passed; see [REVIEW](REVIEW.md). Existing Run 3 source files and fixtures were read without modification.

## 6. Complete parent scope after the other branches were reviewed

**PROVED.** The assembled [local parent theorem](LOCAL_PARENT_THEOREM.md)
excludes an unbalanced constant-coefficient all-Z indicator relation on
the admissible facets of every one of the 29 cores. This is stronger than
a failed search for examples: the twelve collapsed cores have no relevant
tiles, the fifteen balanced cores have complete one-dimensional balanced
relation kernels, and the two hostile kernels above are zero. It remains
restricted to one parent's facets and says nothing about relations using
additional tiles.

The counterexample branch did not discard the four-mass terms and recount
the survivors. It instead solved all ordinary-wall preimages exactly and
found indicator independence. It also tested the apparent merger 2↔3
count: the omitted (5,5) merger supplies the sixth wall and the genuine
relation is 3↔3. The four spurion walls of (3,3,4) have coefficients
+,-,+,- in their exact source order; their actual reflection pairs them.

**FAILED (specific proposed shortcuts).** Interval endpoints alone,
complex-degree substitution for positive multiplicity, universal
admissible-facet parent coverage, and deleting merger walls do not prove
balancedness. The earlier triangle, disconnected interval, variable
four-mass multiplicities and conic open hole remain active regression
fixtures. A 200-sample q8 screen found no hole, but proves no covering
theorem and is not part of the all-Z relation-space proof.
