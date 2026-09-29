# Complete rank-two m=4 membership cores

**PROVED from the source classification, the direct inversion below, and published spurion injectivity; independently reviewed in [INDICATOR_INDEPENDENT_REVIEW](INDICATOR_INDEPENDENT_REVIEW.md).** Let S be an eight-dimensional positroid cell in Gr≥0(2,n), n≥6. Let q be its nonloop support size and let its cyclic parallel classes have sizes b_1,...,b_s. Then S is injective under the amplituhedron map for **every** positive n×6 matrix if and only if either

\[
\max_i b_i=q-5,
\qquad\text{or}\qquad
(q;s;b_1,b_2,b_3)=(9;3;3,3,3).
\tag{1}
\]

The first family has a class with exactly five complementary nonloop labels. It includes the two-class (5,5) core. Up to signed dihedral transport and inserting loops, there are exactly **eleven admissible source-core types**: ten of the first kind and the spurion. The only noncollapsed excluded type is the four-mass (2,2,2,2) cell. This is a classification of tile-generating cells under the all-Z convention, not a count of tiles in any complete tiling.

The finite source types have direct antecedents in the physics literature; see [LITERATURE_DELTA](LITERATURE_DELTA.md). No novelty claim is made for their list or the finite-support principle.

## 1. Exhaustiveness is a source theorem

The classical rank-two positroid description consists of loops and cyclic interval parallel classes. Its source dimension is q+s−4. Thus dimension eight forces q+s=12, with 2≤s≤q, giving precisely

\[
(q,s)=(6,6),(7,5),(8,4),(9,3),(10,2).
\]

For each q, selecting s cuts among q cyclic gaps enumerates every labeled loopless source cell once. The counts are respectively 1,21,70,84,45, totaling221. Their dihedral composition types number1,3,8,7,5, totaling24. The [exact inventory](../../results/run6/membership_cores.json) records all221 affine labels, and representative necklaces and bases. Independent positive-composition counting verifies the orbit multiplicities, and independent affine formulas verify dimension and encodings.

Here is the complete admissible-core list. Class sizes are written in canonical dihedral order.

| q | Class sizes | Labeled loopless cells | Mechanism |
|---:|---|---:|---|
| 6 | (1,1,1,1,1,1) | 1 | Complement five |
| 7 | (1,1,1,2,2) | 7 | Complement five |
| 7 | (1,1,2,1,2) | 7 | Complement five |
| 8 | (1,1,3,3) | 8 | Complement five |
| 8 | (1,2,2,3) | 16 | Complement five |
| 8 | (1,2,3,2) | 8 | Complement five |
| 8 | (1,3,1,3) | 4 | Complement five |
| 9 | (1,4,4) | 9 | Complement five |
| 9 | (2,3,4) | 18 | Complement five |
| 9 | (3,3,3) | 3 | Published spurion |
| 10 | (5,5) | 5 | Complement five |

The excluded collapsed types are (1,1,1,1,3) at q7; (1,1,1,5),(1,1,2,4),(1,2,1,4) at q8; (1,1,7),(1,2,6),(1,3,5),(2,2,5) at q9; and (1,9),(2,8),(3,7),(4,6) at q10. The remaining excluded type is (2,2,2,2) at q8. This lists all24 types, not just the admissible ones.

There is also an enumeration-free way to isolate the possible noncollapsed mechanisms. If max b_i<q−5, the five possible (q,s) pairs force either q8,s4 with all b_i=2, or q9,s3 with all b_i=3. The q6,q7,q10 averages exclude strict inequality. Equality gives the first case of (1); larger maximum gives the obstruction below. Hence no additional mechanism is being omitted by the finite list.

## 2. The two exclusion mechanisms

If a class D has at most four complementary nonloop labels, a nonzero row functional annihilating its direction gives a nonzero vector in Y supported on those external rows. It cannot vanish after applying Z because the positive amplituhedron map preserves source rank. Thus Y meets a fixed external space H_t of dimension t≤4. The incidence locus of two-planes meeting H_t has dimension at most (t−1)+4=t+3≤7. Therefore the image of S has dimension below eight for every positive Z. An injective map from its open eight-cell would have an open image by invariance of domain, a contradiction.

The remaining excluded (2,2,2,2) type is the four-mass cell. Published nonadmissibility is explicit in Galashin–Lam Example13.12. The preserved [exact four-mass certificate](../run3/MULTIPLICITY.md) independently gives two distinct positive source points with identical image at a positive rational external matrix. A single such matrix disproves all-Z injectivity. No conclusion that the positive multiplicity is two for every Z or every target is used.

## 3. Uniform inversion for the ten complement-five types

Delete loops and use the matching signed cyclic action to put the distinguished class D last and its five complementary labels first. Let A_1,...,A_ell be the successive classes among those five labels and put r=|D|. The dimension equation gives ell+r=6.

The entire open source cell has the chart

\[
C=\begin{pmatrix}
a_1&\cdots&a_5&0&\cdots&0\\
t_{j(1)}a_1&\cdots&t_{j(5)}a_5&d_1&\cdots&d_r
\end{pmatrix},
\quad a_i,d_h>0,\quad t_1<\cdots<t_\ell.
\]

Normalize D to the vertical projective direction. All other directions lie in its ordered complementary interval, so this chart is complete. Slopes may be negative. Its remaining row changes are positive scalings and a common affine change of slopes.

Fix any positive external matrix. Let H=span(Z_1,...,Z_5) and h(X)=det(Z_1,...,Z_5,X). The first image row R lies in H, and the second has h-value equal to a positive sum of the strictly positive h(Z_d), d∈D. Hence Y∩H is a unique line, with its positive ray giving

\[
R=\sum_{i=1}^5a_iZ_i
\]

and determining the a_i up to common positive scale. Set V_j=sum_(i∈A_j)a_iZ_i. The six rows

\[
B=(V_1,...,V_\ell,Z_{D_1},...,Z_{D_r})
\]

are independent: det B expands as a sum of positive coefficients times increasing six-minors of Z. Choose any second image row S_0∈Y with h(S_0)>0. Its unique expansion in B determines t_1,...,t_ell,d_1,...,d_r. The resulting row space is in the open source cell exactly when all consecutive slope differences and all d_h are positive.

To check uniqueness as a source row space, take another positive preimage. Align its first row to R using positive scaling. Its second image row is alpha S_0+beta R with alpha>0, because h is positive on both second rows. A permitted positive rescaling and subtraction align it to S_0. The six-row expansion is unique, so its source row space is the same. This proves all-Z injectivity, including q6 and the q10 two-class case. No BCFW classification or sampled rank is needed.

The inverse is rational on ambient Grassmannian charts: recover Y∩H, solve its five independent coefficients, and invert B. An arbitrary positive Z may require choosing a different nonzero five-column pivot from the convenient one used in a moment-curve implementation. The invariant assertion is the independence of the five external rows and of B, not a specific ambient-coordinate minor.

## 4. Generic closed membership and the spurion core

The complement-five inverse also gives complete closed-image membership away from a proper exceptional set. Require every four-twistor det(Y,Z_I) to be nonzero. If D disappears in a source closure point, Y lies in the five-space H and meets a four-space spanned by four complementary rows. If a complementary column vanishes, or an outside direction merges into D, a functional annihilating D gives a nonzero image vector supported on at most four complementary labels. Each case would force a forbidden zero four-twistor.

Thus any closed preimage on this generic locus has D nonzero and distinct from all other surviving directions, and all five complementary coefficients positive. It lies in the weak chart with nondecreasing slopes and nonnegative d_h. Line recovery and the six-row expansion exhaust it. If the recovered first-row coefficients are strictly mixed, there is no closed preimage; otherwise the weak inequalities decide membership. If all tested coefficients and inequalities are nonzero, they distinguish open membership from closed nonmembership and persist in an open target neighborhood. Their exceptional zero sets are proper because the tile has an open image on which all source inequalities are strict.

The spurion (333) is injective for every positive Z by *A cluster of results on amplituhedron tiles*, Section5.1, with its explicit functionary inverse description. Its modern all-Z status is independent of the printed complete-tiling parent discrepancy audited in earlier runs. Its new kernel-based membership implementation is reviewed separately in Run6; the classification theorem here uses the published injectivity input. [Primary article](https://arxiv.org/abs/2402.15568).

## 5. Exact loop transport and the universe count

For an increasing support I, inserting zero source columns satisfies (j_I C)Z=CZ_I on the entire source closure. Thus fibers, injectivity, positive multiplicities and open or closed membership are exactly those of the core at the positive row submatrix Z_I. Every positive core matrix extends to any prescribed ambient support by the [positive extension lemma](../run2/POSITIVE_EXTENSION.md). Hence this transport is an equivalence of all-Z assertions, including nonadmissibility. The compatible signed dihedral actions preserve the entire map problem. See [FINITE_CORES](../run3/FINITE_CORES.md) for the preserved proof.

Every source cell has a unique support. The admissible loopless counts at support sizes6,...,10 are1,14,36,30,5. Therefore the complete all-Z tile-generating cell universe has cardinality

\[
|U_n|=\binom n6+14\binom n7+36\binom n8+30\binom n9+5\binom n{10}.
\]

This gives |U_8|=176 and |U_9|=942. It is a count of all available tile labels, not Magic Number. Three of the thirty loopless nine-label tiles are spurions; (5,5) supplies the five loopless ten-label tiles.

For comparison, direct enumeration of the364 loopless nine-dimensional source parents gives nonzero Run4 parent-row counts7,40,81,60,11 by support size7,...,11. The admissible facets recover the full parent's basis set in every balanced core, checked independently; different parents therefore cannot give the same nonzero signed row up to overall sign. Exact support transport gives the number of full parent rows

\[
7\binom n7+40\binom n8+81\binom n9+60\binom n{10}+11\binom n{11}.
\]

These counts do not determine the rank of those rows, their quotient dimensions at larger n, or generation of arbitrary image relations. No polynomial extrapolation of quotient ranks is made.

Implementation and checks: [run6_membership_cores.py](../../src/magic_number/run6_membership_cores.py), [tests](../../tests/test_run6_membership_cores.py). The finite source accounting supplements the proof of (1); sample external matrices are not used to certify its positive direction.


**COMPUTATIONALLY-VERIFIED adaptive implementation.** The new Run6 complement-five wrapper chooses a nonzero five-column ambient pivot and applies its column permutation to both Z and Y. The cache key retains that permutation. A positive right-GL6 fixture on the (55) core makes the old moment-specific first-five pivot vanish; the new wrapper still recovers positive membership. The coordinate permutation can reverse the external orientation, but the recovered hyperplane functional is reoriented on D and the compressed matrix remains invertible. This is a bounded single-core regression, not an n10 global kernel calculation.
