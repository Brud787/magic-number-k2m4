# Run 4: the hidden merger in the (1,4,5) and (2,3,5) parents

## Precise result

**PROVED.** Let \(Z\) be any positive \(10\times6\) matrix. Partition its ordered labels into

\[
A=\{1,\ldots,a\},\quad B=\{a+1,\ldots,5\},\quad D=\{6,\ldots,10\},
\qquad 1\le a\le4.
\]

For the nine-dimensional source parent \(P=(A)(B)(D)\), let \(M=(A\cup B)(D)\), and let \(D_j\) be the source facet deleting label \(5+j\), \(1\le j\le5\). All six source cells are eight-dimensional, and each amplituhedron map is injective for every positive \(Z\). Their closed images satisfy the local tile relation

\[
\boxed{[Z_M]+[Z_{D_2}]+[Z_{D_4}]
       =[Z_{D_1}]+[Z_{D_3}]+[Z_{D_5}].}
\]

Each side has disjoint open tile images and multiplicity one away from a semialgebraic set of dimension at most seven. Both closed unions equal the closure of the open parent image. Indicator brackets mean equality modulo such lower-dimensional sets. This is a **Level A, all-\(Z\), balanced \(3\leftrightarrow3\)** relation, with coefficient sum zero. There is no claim that this region extends to a complete tiling, no connectivity/generation claim, and no assertion that these are the only boundary decompositions.

The two dihedral composition types are \((1,4,5)\) and \((2,3,5)\). The argument gives their labeled cyclic/reflected copies and their order-preserving loop insertions: restriction to the ten nonloop rows preserves positivity, and signed cyclic/dihedral symmetry preserves the map. The result is local. All six tiles are BCFW; this result introduces no new non-BCFW tile type.

## Why the merger must be retained

**PROVED.** A usual three-direction source chart has rows

\[
\begin{pmatrix}(a_i)_{A}&(b_i)_{B}&0_D\\
0_A&(b_i)_{B}&(d_j)_D\end{pmatrix},\qquad a_i,b_i,d_j>0.
\]

It parametrizes the open parent up to a common projective scaling. In that normalization, the merger \(A\cup B\) can occur through a rank-one matrix limit together with an unbounded row operation. Projective coefficient-boundary inspection alone therefore does not supply the complete Grassmannian boundary or the positive-fiber endpoints. The coordinate below resolves the merger as a finite **rank-two** endpoint; it is not discarded as a rank-one image.

## Hyperplane recovery and the complete fiber

Fix \(Z\). All vectors below are rows in \(\mathbb R^6\). Put

\[
H_F=\operatorname{span}(Z_1,\ldots,Z_5),\quad
H_D=\operatorname{span}(Z_6,\ldots,Z_{10}),
\]
\[
L_D(X)=\det(X,Z_6,\ldots,Z_{10}),\qquad
L_F(X)=\det(Z_1,\ldots,Z_5,X).
\]

Both spans have dimension five. Positivity gives \(L_D(Z_i)>0\) for \(i\le5\) and \(L_F(Z_i)>0\) for \(i\ge6\).

For any \(Y\) in the open parent image, the line \(Y\cap H_F\) is unique and has a unique representative

\[
U=\sum_{i=1}^{5}u_iZ_i,\qquad u_i>0,\quad\sum_i u_i=1.
\]

Indeed, a source representative killing the \(D\)-direction produces this ray; the other row has a positive combination of \(D\)-rows and hence strictly positive \(L_F\), so \(Y\not\subset H_F\). The independent first five rows determine the \(u_i\). Split \(U=A_0+B_0\) according to \(A,B\), and put

\[
\lambda=\frac{L_D(B_0)}{L_D(U)}\in(0,1),\qquad
K=B_0-\lambda U\in H_F\cap H_D.
\]

Since \(L_D(U)>0\), the line \(Y\cap H_D\) is also unique. It has a unique vector \(W\) with \(L_F(W)=1\): if its \(L_F\) were zero, both independent lines \(U,W\) would lie in \(H_F\), contradicting the preceding paragraph. Define unique coordinates

\[
W=\sum_{j=1}^{5}h_j Z_{5+j},\qquad
K=\sum_{j=1}^{5}k_j Z_{5+j}.
\]

**PROVED (complete positive fiber).** The full fiber in the open parent consists exactly of the Grassmannian row spaces represented by

\[
C(\tau)=
\begin{pmatrix}
(u_i)_A&(u_i)_B&0_D\\
0_A&\tau(u_i)_B&(h_j-\tau k_j)_{j=1}^{5}
\end{pmatrix},
\qquad \tau>0,\quad h_j-\tau k_j>0.
\tag{1}
\]

For completeness, start with any positive source preimage. Killing its \(D\)-direction and normalizing gives exactly the fixed first row \(U\). A second row killing the \(A\)-direction is unique up to positive scale; positivity of minors forces its \(B\)-coefficients to be \(\tau u_i\) with \(\tau>0\) and its \(D\)-coefficients positive. Scale this row so its image has \(L_F=1\); this is permitted because its \(D\)-contribution has positive \(L_F\). Its image is then \(W+sU\). Applying \(L_D\) gives

\[
sL_D(U)=\tau L_D(B_0),\quad s=\tau\lambda.
\]

Consequently its \(D\)-part is exactly \(W-\tau K\), giving (1). Conversely (1) is positive in precisely the parent when the displayed inequalities are strict, and

\[
C(\tau)Z=\begin{pmatrix}U\\W+\tau\lambda U\end{pmatrix}
\]

has row space \(Y\). The gauges make \(\tau\) and the source representative unique. This excludes additional positive branches; no differential-rank or sample-injectivity inference is used.

At \(\tau=0\), with every \(h_j>0\), formula (1) is exactly the \(M=(5,5)\) cell. It has rank two. At every nonnegative feasible \(\tau\), including both endpoints below,

\[
L_F\!\left(\sum_j(h_j-\tau k_j)Z_{5+j}\right)=L_F(W-\tau K)=1.
\tag{2}
\]

Thus the last-class vector never vanishes, and the endpoint source matrix never becomes rank one. This identity also prevents an additional endpoint hidden in a discarded rank-one chart limit.

## Exact signs and the interval

**PROVED.** The seven-vector maximal-minor identity, applied to the ordered vectors \(Z_i,Z_l,Z_6,\ldots,Z_{10}\), gives

\[
k_j=
\frac{(-1)^{j+1}}{L_D(U)}
\sum_{i\in A,\ l\in B}u_i u_l
\det(Z_i,Z_l,Z_6,\ldots,\widehat{Z_{5+j}},\ldots,Z_{10}).
\tag{3}
\]

All determinants in this sum are positive ordered six-minors, all coefficients are positive, and the denominator is positive. Therefore

\[
\operatorname{sgn}(k_1,k_2,k_3,k_4,k_5)=(+,-,+,-,+)
\]

for **every** positive \(Z\) and every positive recovered \(u\). This is a symbolic positivity identity, not continuation from a sample.

The closure of the feasible parameter set is the bounded interval

\[
\left[
\max\left(0,\frac{h_2}{k_2},\frac{h_4}{k_4}\right),
\min\left(\frac{h_1}{k_1},\frac{h_3}{k_3},\frac{h_5}{k_5}\right)
\right].
\tag{4}
\]

For \(Y\) in the open parent image, its endpoints are distinct and the upper endpoint is finite and positive. With increasing \(\tau\), the derivatives of the six inward wall functions are

| Wall | Inward function | Sign |
|---|---|---|
| \(M\) | \(\tau\) | \(+\) |
| \(D_j\) | \(h_j-\tau k_j\) | \((-1)^j\) |

The lower endpoint belongs to \(M,D_2\), or \(D_4\), and the upper endpoint belongs to \(D_1,D_3\), or \(D_5\). Every wall derivative is nonzero. This explains the balancing mechanism: seven-vector alternating circuit signs, with the merger replacing the missing first endpoint inequality.

## Admissibility, multiplicity, and equality of the two regions

**PROVED (all six wall injectivities).** On every open selected wall the preceding hyperplane recoveries remain valid: all first-five coefficients are positive, and at least four last-five coefficients are positive, giving \(L_D(U)>0\) and positive \(L_F\) of the other row. On \(M\), the two unique hyperplane rays recover the entire source point and \(\tau=0\). On \(D_j\), equation (3) gives \(k_j\ne0\), and its sole missing coefficient forces \(\tau=h_j/k_j\), again uniquely recovering the source point. This is global all-\(Z\) injectivity. Each source wall has dimension eight, so invariance of domain gives an open image in the eight-dimensional target and hence a valid tile.

These direct injectivity proofs agree with independent BCFW source provenance. For \(M\), the reviewed BCFW product on ten labels has left rank-one support \({1,\ldots,5\}\) and product data \(a=6,b=7,c=8,d=9,n=10\). Each \(D_j\), after deleting its loop, appears in the full nine-label general BCFW recipe catalog. The test checks these exact source bases and affine labels, independently of the fiber proof.

**PROVED (coverage and no multiplicity).** The recovered \(u,h,k\) depend rationally and continuously on \(Y\) on the relevant transverse chart. If (4) contains a strictly feasible parameter, the same parameter stays feasible in a neighborhood. Thus the open parent image is open. Every selected open wall image lies in it: move slightly inward from its one active inequality, whose derivative is nonzero, keeping the other five strict.

Outside a semialgebraic set of dimension at most seven, each endpoint activates exactly one inequality. Indeed, two simultaneous active inequalities put (1) in a source boundary stratum of dimension at most seven. At \(\tau>0\) this means at least two deleted \(D\)-labels. At \(\tau=0\) and a deleted \(D\)-label, it is a two-class \((5,4)\) stratum of dimension seven. There are finitely many such strata, and images cannot increase semialgebraic dimension. Equation (2) shows that no endpoint escapes to an undefined rank-one limit.

Every generic parent-image point consequently has exactly one preimage on a positive-sign wall and exactly one on a negative-sign wall. Each side covers the generic open parent image with multiplicity one. Distinct open wall images on the same side are disjoint: any overlap would be open by injectivity and invariance of domain, so would contain a generic point with two same-side endpoints, contradicting (4).

For closed-union equality, a source wall is a boundary of the parent, so its closed image lies in the closure of the parent image. Conversely the generic parent-image points are dense in the open parent image and belong to each of the two finite closed unions. These unions are closed because source cell closures are compact and the positive-\(Z\) amplituhedron map is continuous there. Each therefore contains the closure of the open parent image. Both closed unions equal that closure. Intersections of closed tiles occur only in the allowed lower-dimensional boundaries.

## Remaining source facets really collapse

**PROVED.** For \(a=1\), the source parent has twelve codimension-one facets; for \(a=2\), thirteen. The six selected facets are the merger \(A\cup B\) and the five \(D\)-deletions. Every remaining source facet has a parallel class whose nonloop complement has at most four labels:

- Deleting a label from a nonsingleton \(A\) or \(B\) leaves \(D\) of size five on nine nonloops; its complement has four labels.
- Merging \(B,D\) leaves complement \(A\) of size at most four.
- Merging \(D,A\) leaves complement \(B\) of size at most four.

The reviewed class-complement Schubert bound puts each such image in dimension at most seven. A singleton deletion is not a codimension-one source facet. This accounts for all source facets through the exact rank-two boundary classification. Collapsing these images is a geometric dimension statement; no source boundary chain is being asserted to equal the image relation.

## Exact fixtures and hostile checks

**COMPUTATIONALLY-VERIFIED.** `src/magic_number/merger_fibers.py` constructs the fiber from \(Y\) alone and emits `fixtures/run4/merger_1_4_5.json` and `fixtures/run4/merger_2_3_5.json`. They contain parent and child affine permutations, bases, necklaces, source codimension, new zero-minor witnesses, all six signed coefficients, every omitted-facet dimension witness, exact rational fiber data, and rank-two endpoints.

Four independent regression tests pass. They check (3) using a separate Fraction determinant implementation; image-basis-independent ray recovery including a negative determinant basis change; each of the six endpoint inverse formulas, including the hidden merger; source incidence from independent affine bases; and actual BCFW recipe bases. Numerical input in these fixtures is only an exact regression of the symbolic proof, never the all-\(Z\) certificate.

## Targeted prior-art delta and limits

Bounded check on 2026-09-06: searched the specific nearly-admissible/13.10 and amplituhedron-fiber/Gale terms, reopened GL §13.4 and the MPP paper, and checked the fiber paper's positivity hypothesis. This supplements the earlier audit; it is not a search-based novelty certificate.

**SOURCE-VERIFIED (inherited targeted audit).** [Galashin--Lam §13.4](https://www.math.ucla.edu/~galashin/papers/duality.pdf) already poses balanced parent replacements and connectivity as separate conjectures. The present result proves the existence/balancedness portion for these profiles; it does not prove the uniqueness-of-triangulations clause or connectivity. The seven-vector alternating circuit identity is classical; see the primary sources and precise scope in `research/run3/LITERATURE_DELTA.md`. The [Mohammadi--Monin--Parisi fiber approach](https://arxiv.org/pdf/2010.07254) already studies amplituhedron fibers and secondary constructions, with its stated hypotheses. This proof verifies the necessary positivity, complete positive fiber, endpoint, and tile conditions directly for the two profiles. It does not import arbitrary-tile canonical-form additivity. No priority or novelty claim is made.

**FAILED shortcut.** Counting just the five visible last-class coordinate deletions in the original three-anchor orthant would give an apparent \(2\leftrightarrow3\) discrepancy. The hidden rank-two merger is the sixth genuine endpoint wall and restores the exact \(3\leftrightarrow3\) relation. This is not an unbalanced indicator relation or a Magic Number counterexample.

## Independent audit of the shared complement-five theorem

**PROVED, independently reviewed by the merger subtask.** The proof in `research/run4/SMALLER_CORES.md`, Sections 1–5, was checked separately after the two-merger proof above had been derived. Its image-basis gauge is valid: positivity of the distinguished-class contribution forces the rescaling coefficient alpha to be positive, and subtraction of a multiple of the fixed first row preserves all slope differences. Thus it recovers the entire positive fiber without imposing an incompatible extra zero-slope normalization.

The compressed seven-row matrix has positive ordered six-minors by a termwise expansion with disjoint ordered supports. The actual merger derivatives are differences of adjacent Gale coefficients, not the coefficients alone. Adjacent opposite signs imply that these differences have the next coefficient's sign; together with the distinguished-class deletions, they give six alternating signs. Each selected wall stays in the hyperplane recovery chart and has a nonzero affine derivative, yielding global injectivity. A fixed strictly positive hyperplane functional prevents all distinguished-class coefficients from vanishing at an endpoint. Both-sign derivatives bound the fiber; simultaneous walls belong to finite source strata of dimension at most seven. These facts validate multiplicity one, generic endpoint coverage, openness, and equality of the two closed unions. No failed gate or unbalanced relation was found. This proof independently contains the two-merger cases above, up to a common orientation reversal.

**PROVED, independently reviewed by the merger subtask.** Section 6's reflected `(1,3,2,3)` proof also passes the targeted audit. The two stated pivot factors expand into positive ordered minors on the parent and each selected open wall. Its coordinate involution is the actual signed label reflection, has five transpositions, and preserves the target Grassmannian orientation while reversing the source orientation. Global pivot, wall injectivity and connectedness supply the needed submersion and constant transverse signs. In the normalized endpoint chart, a rank-one source limit actually forces the singleton coordinate v to vanish as well; the paper's stated larger incidence family in the span of labels 4,8,9 is a valid upper bound of dimension six, so the extra vanishing only strengthens its exceptional-set estimate. The reflection balances the ten wall types without inferring balancedness from sampled signs.
