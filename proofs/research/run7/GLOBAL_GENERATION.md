# Uniform indicator generation for rank two, m=4

**PROVED, independently audited in Run7.** The geometric maps, finite
certificates, and normalization argument passed separate hostile reviews.
The consolidated verdict and validation are in [REVIEW](REVIEW.md).

## Statement and scope

For n≥6 let U_n consist of every eight-dimensional rank-two positroid
source cell whose amplituhedron map is injective for every positive n×6
matrix. Let V_n=R^{U_n}. Let L_n be the span of all transported Run4
single-parent geometric relations. Let K_n be the kernel of the map sending
a source label to its family of tile indicators for **all** positive Z,
modulo semialgebraic sets of dimension at most seven. Coefficients are
constant and independent of Z. Write Q_n=V_n/L_n.

The theorem is

\[
K_n=L_n\quad(n\ge6).
\tag{1}
\]

It implies D_n⊆L_n for complete multiplicity-one all-Z tilings, and hence
Magic Number for k=2,m=4. It does not assert flip connectivity, L_n⊆D_n
for arbitrary n, or equality of the kernel at **every fixed** positive Z.

## 1. The geometric maps that supply a global structure

In label number n, define n face maps on source matrices by

\[
d_i(c_1,\ldots,c_n)
=(c_1,\ldots,c_{i+1}+c_{i+2},\ldots,c_n)
\quad(0\le i<n-1),
\]
\[
d_{n-1}(C)=(c_1-c_n,c_2,\ldots,c_{n-1}).
\tag{2}
\]

Let s_i insert a zero column after c_(i+1), for 0≤i<n. Retain a face
image label only when it is an admissible eight-cell, and otherwise send
the basis vector to zero. Set V_n=L_n=K_n=0 for 1≤n≤5.

The [geometric amalgamation proof](AMALGAMATION_PROOF.md) establishes all
of the following without assuming (1):

* Each source face has an exact single-cell image. Dimension-preserving
  maps from admissible eight-cells are positive rational isomorphisms.
* A discarded eight-dimensional image is collapsed, never four-mass.
  Its amplituhedron image has dimension at most seven for every positive
  downstairs matrix.
* Every positive downstairs matrix has a positive external degeneration
  realizing each face. Source rank-loss limits are confined to a
  dimension-four target Schubert locus. Away from finitely many
  lower-dimensional sets, all tile indicators stabilize simultaneously
  on open neighborhoods. This proves d_i K_n⊆K_(n−1).
* The same geometric limit and the **complete one-parent theorem** give
  d_i L_n⊆L_(n−1). A parent maps either to a nine-cell, an eight-cell,
  or a smaller cell; these cases respectively give a one-parent relation,
  a zero scalar multiple of one tile, or zero.
* Zero insertion preserves both K and L by external row restriction.

The [simplicial audit](SIMPLICIAL_AMALGAMATION.md) proves every face and
degeneracy identity, including the minus sign in the wrap face. The
dimension and collapse truncations commute with further faces. Consequently

\[
V_{p+1},\quad L_{p+1},\quad K_{p+1},\quad
\mathcal Q_p:=V_{p+1}/L_{p+1},\quad \mathcal H_p:=K_{p+1}/L_{p+1}
\]

are simplicial real vector spaces in degree p, with $\mathcal H$ a
simplicial subobject of $\mathcal Q$.
Below $N(\mathcal Q)$ and $N(\mathcal H)$ use simplicial degrees; $Q_n$ always
uses the number of source labels. The geometric proof of this statement is the new bridge;
ordinary source cellular boundaries do not supply it.

## 2. Normalization reduces the quotient to small finite matrices

For a simplicial vector space X, its normalized group in degree p is
isomorphic to its degree-p space modulo the images of all degeneracies
from degree p−1. Normalization is exact and detects the zero object.
These are the standard normalization and Dold–Kan results, not new
homological assertions about positroid cells.
[Stacks, quotient by degeneracies](https://stacks.math.columbia.edu/tag/019A),
[exact normalization](https://stacks.math.columbia.edu/tag/019B),
[Dold–Kan](https://stacks.math.columbia.edu/tag/019D).

Here s_i inserts a loop in one of the positions **2,...,n**. Therefore

\[
N(\mathcal Q)_{n-1}\cong
V_n\big/\bigl(L_n+
\langle e_S:S\text{ has a loop in }\{2,\ldots,n\}\rangle\bigr).
\tag{3}
\]

This quotient must not be confused with removing **all** loop-containing
columns. A label with its only loop at1 survives (3). The ordinary
normalized complex and its degeneration subspace are justified by the
proved simplicial identities, not by declaring unwanted source cells zero.

The complete membership-core theorem bounds tile support by10. Thus the
surviving columns are precisely the loopless n-label tiles and the
(n−1)-label loopless tiles inserted with their only loop at1. A parent
with a loop in2,...,n contributes a zero projected row, since all its
facets retain that loop. The remaining rows come exactly from loopless
parents or parents with their only loop at1. The fifteen certified
prototypes give the following complete matrices:

| n | Surviving tile columns | Nonzero projected parent rows | Exact rank | dim N(\mathcal Q)_(n−1) |
|---:|---:|---:|---:|---:|
|6|1|0|0|1|
|7|15|7|6|9|
|8|50|47|31|19|
|9|66|121|54|12|
|10|35|141|35|0|
|11|5|46|5|0|

The saved maximal-minor determinants in order are1,−1,1,−1,−1,1.
Rational RREF supplies each rank upper bound. The critical35×35 and5×5
nonvanishing minors are independently reconstructed from literal source
transports and checked by Fraction elimination. For n≥12 there are no
surviving columns, by the support bound. Therefore

\[
N(\mathcal Q)_p=0\qquad(p\ge9).
\tag{4}
\]

The [finite certificate](../../results/run7/normalized_core_ranks.json)
and [independent audit](../../results/run7/normalized_independent_review.json)
are exhaustive for (3). No full n10 relation matrix, new indicator matrix,
or complete-tiling enumeration is used.

## 3. The global kernel cannot acquire a new normalized class

Run6 proves K_9=L_9. All smaller K_r/L_r vanish as well: insert zeros to
nine labels, use K_9=L_9, and apply the corresponding face left inverses.
Those faces preserve L, so no injectivity assumption on a formal
uncontrolled deletion is needed. Thus K_r/L_r=0 for label numbers r≤9,
equivalently $\mathcal H_p=0$ for simplicial degrees p≤8.

Since normalization is exact, $\mathcal H\hookrightarrow\mathcal Q$ gives
$N(\mathcal H)\hookrightarrow N(\mathcal Q)$. For p≤8, $\mathcal H_p=0$,
so $N(\mathcal H)_p=0$. For p≥9, (4) forces $N(\mathcal H)_p=0$.
Hence $N(\mathcal H)$ is the zero
normalized complex in every degree. Faithfulness of normalization gives
$\mathcal H=0$. This proves (1).

This is an induction through a proved simplicial structure. It is not
extrapolation from three ranks. The two high-degree zero certificates
and the support bound exclude all later new classes; exactness of
normalization then excludes them in the geometric kernel subobject.

## 4. Rank formula and the failed first extrapolation

The simplicial decomposition counts increasing surjections [n−1]→[p].
Their number is binomial(n−1,p), so the finite normalized dimensions give

\[
\dim Q_n=\binom{n-1}{5}+9\binom{n-1}{6}
+19\binom{n-1}{7}+12\binom{n-1}{8}.
\tag{5}
\]

Subtract this from the preserved complete tile count

\[
\dim V_n=\binom n6+14\binom n7+36\binom n8
+30\binom n9+5\binom n{10}
\]

to obtain rank L_n=dim K_n for all n. Binomials outside their range mean0.
At n10, (5) gives1674 and rank L_10=2141. The initially proposed1675 was
**FAILED** by the35-column diagnostic; that failure remains archived.

## 5. Magic Number corollary

If T,T′ are two complete all-Z tilings, their difference belongs to K_n.
By (1) it belongs to L_n. Every Run4 local generator has coefficient sum
zero, so |T|=|T′|. Comparing with a certified standard BCFW tiling gives

\[
|T|=M(2,n-6,2)
=\frac1{n-3}\binom{n-3}{2}\binom{n-3}{3}
=\frac{(n-3)(n-4)^2(n-5)}{12}.
\tag{6}
\]

The value at n6 is1, and at n7,8,9 it is6,20,50. The count follows from
the accepted MacMahon convention and the preserved all-Z BCFW theorem.
This corollary concerns k=2,m=4 for arbitrary n; it is not full m4 for
arbitrary k. No novelty claim is inferred from the literature search.
