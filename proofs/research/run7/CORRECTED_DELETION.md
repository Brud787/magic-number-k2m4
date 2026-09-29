# Naive deletion defects and the requirements on a correction

**PROVED.** For every n≥6 and every fixed label j in [n+1], the degree-eight source deletion map satisfies

\[
\delta_j(L_{n+1})=V_n.
\tag{1}
\]

Here V_n is the free vector space on all-Z admissible eight-dimensional rank-two positroid cells, and L_n is the span of the certified local parent relations from Run4. Thus naive deletion has defects spanning the entire target tile space, even at a fixed insertion position. This strengthens the single-counterexample obstruction from [Run6](../run6/DELETION.md). It does not rule out a corrected map: adjacent-column amalgamation supplies a concrete correction under separate examination.

No new image relation is assumed in this argument. All relation inputs are the preserved fifteen balanced parent prototypes and their signed dihedral and loop transports. All twelve collapsed parent types and both parents with zero all-Z admissible-facet relation space remain explicitly without a nonzero row.

## 1. The exact defect of any one parent row

For an admissible source label S in [n+1], define delta_j(e_S) by deleting j and relabeling if j is a loop, and by zero if j is a nonloop. Deleting a nonloop lowers the source dimension, so this is precisely the degree-eight part of ordinary source deletion. It is a map on source labels, without an assumed map between arbitrary fixed-Z amplituhedron targets.

Let r_P=sum epsilon_S e_S be the primitive Run4 row of a balanced nine-dimensional parent P.

* If j is a loop of P, every facet retains that loop. Deletion gives the transported parent relation on [n], with every coefficient unchanged.
* If j is a nonloop of P, the only possible source facet in which j becomes a loop is the coordinate-deletion facet P\j. It exists in dimension eight exactly when j belongs to a nonsingleton class. Merger facets retain every nonloop, and deleting another column retains j. Hence

\[
\delta_j(r_P)=
\begin{cases}
\epsilon_{P\setminus j}\,e_{\operatorname{del}_j(P\setminus j)},
&P\setminus j\text{ is an admissible source facet},\\
0,&\text{otherwise}.
\end{cases}
\tag{2}
\]

The sign is the actual geometric image coefficient in the preserved row, not an invented source-boundary orientation. Every nonzero defect is a signed single tile. The cases with no parent relation have no defect row to compute: their records contain null, not a proposed source-boundary vector.

## 2. Complete prototype audit

**COMPUTATIONALLY-VERIFIED exact accounting.** The [certificate](../../results/run7/deletion_defects.json) retains every coefficient and affine label in all136 label decisions across the fifteen nonzero prototypes. There are82 signed singleton defects and54 zero defects.

| Parent class-size type | Signed singleton defects | Zero defects |
|---|---:|---:|
| (1,1,1,1,1,2) |2|5|
| (1,1,1,2,3) |3|5|
| (1,1,2,1,3) |3|5|
| (1,2,1,2,2) |6|2|
| (1,1,3,4) |4|5|
| (1,2,2,4) |4|5|
| (1,2,3,3) |8|1|
| (1,2,4,2) |4|5|
| (1,3,1,4) |4|5|
| (1,3,2,3) |8|1|
| (1,4,5) |5|5|
| (2,3,5) |5|5|
| (2,4,4) |10|0|
| (3,3,4) |10|0|
| (5,6) |6|5|

The fourteen absent rows are recorded with the exact Run4 categories: twelve `COLLAPSED`, two `NO_NONZERO_ALL_Z_FACET_RELATION`. The latter are (1,1,2,2,2) and (2,2,2,3). Their absence is essential in deciding whether a proposed enlargement really supplies a defect.

The [implementation](../../src/magic_number/run7_deletion.py) performs deletion on sparse signed rows. The [independent tests](../../tests/test_run7_deletion.py) recognize loops directly from bounded affine permutations, reconstruct basis sets using cyclic Gale inequalities, and check the source deletion and every coefficient against the literal preserved Run4 rows. They also insert a loop into every slot of every prototype and verify that deletion recovers the entire original row. Five tests passed in2.90 seconds.

## 3. Every tile is a defect at every fixed slot

First disregard the slot. For a complement-five tile, enlarge a distinguished class by one new label. The result is a nine-dimensional complement-five parent, with the original tile as its coordinate-deletion facet. This includes (5,5)→(5,6). For the spurion, enlarge any class: (3,3,3)→(3,3,4). The local parent theorem supplies a balanced row in each case, and (2) gives the desired signed tile defect.

A fixed insertion slot requires more care because a new label can only enlarge a class adjacent to that cyclic gap. The following source argument resolves that issue uniformly.

**Slot lemma.** For any admissible tile S and any cyclic gap between consecutive nonloop labels, at least one class adjoining the gap can be enlarged to a parent with a nonzero Run4 relation.

An enlargement has dimension nine and contains S as a coordinate facet. It cannot be a collapsed parent, because an admissible eight-dimensional tile image lies in its closed image. By the complete local parent theorem, failure to have a nonzero row therefore means precisely one of the two hostile profiles.

The hostile profile (1,1,2,2,2) can be reached from an admissible eight-cell only by enlarging a singleton of a seven-label tile with class sizes1,1,1,2,2. The hostile profile (2,2,2,3) can be reached from an admissible eight-cell only by enlarging a singleton of an eight-label tile with sizes1,2,2,3: deleting a coordinate of its size-three class instead produces the excluded four-mass tile (2,2,2,2). Thus enlarging a nonsingleton class never causes either obstruction.

If the gap touches a nonsingleton class, choose it. Otherwise the two adjoining classes are singletons. Both choices could fail only in the seven-label case, since the eight-label hostile predecessor has just one singleton. In the seven-label case there is a third singleton. For enlarging the first neighbor to leave the hostile profile, the second and third singletons must be adjacent; for enlarging the second neighbor to fail, the first and third must be adjacent. Along with the original adjacency of the two gap neighbors, this would give a triangle in the five-class cycle. That is impossible. At least one enlargement is balanced. This proves the slot lemma.

For a source with loops, an insertion position determines a gap between the nearest surrounding nonloop labels. The same lemma applies. Insert the new nonloop into the chosen class and retain all existing loops. The resulting parent row is certified by exact support and dihedral transport. Deleting the new label in this row gives ±e_S by (2). This proves (1) for every prescribed j, not merely after varying j or summing over slots.

**COMPUTATIONALLY-VERIFIED independent finite regression.** All86 labeled loopless admissible tiles and every q+1 linear insertion slot were checked:798 slot decisions, all with at least one balanced-parent witness. The certificate retains each witness parent, chosen class, relation ID, transport action and signed coefficient. The independent check identifies allowable enlargements from the two neighboring colors in the cyclic word, then reconstructs every parent basis set directly. This finite verification supplements the slot lemma; it is not an enumeration of tilings or a sampled-Z argument.

## 4. What any linear correction must do

Suppose a corrected map has the form D_j=delta_j+C_j and is required to send L_(n+1) into L_n. Let pi_n:V_n→Q_n=V_n/L_n be the quotient projection. For every local relation r,

\[
\pi_n C_j(r)=-\pi_n\delta_j(r).
\]

By (1), the right-hand side ranges over all of Q_n. Consequently

\[
\pi_n C_j(L_{n+1})=Q_n.
\tag{3}
\]

This is an exact necessary condition on the correction itself. A correction supported on a small fixed list of target directions cannot work if their quotient span is proper. At n8 and n9 the correction images must already span quotient dimensions103 and472, respectively. A finite rule on profiles can still produce that many differently labeled outputs; finite profile dependence is not ruled out.

Checking only total coefficients is much weaker. The necessary scalar equations are sum_S epsilon_S sum(C_j(e_S))=−epsilon_deleted for a nonzero defect, and zero otherwise. Assigning unit total coefficient to every nonloop correction would solve these scalar equations because all parent rows are balanced, but it would not prove the vector identities modulo L_n. Nor does subtracting a defect separately for each parent define a linear map on tile generators: one tile appears in many parent rows and all constraints must agree.

## 5. Adjacent-column amalgamation as a concrete correction

The independent geometric branch studies C↦(c_1,...,c_(n−2),c_(n−1)+c_n), followed by retaining dimension-eight admissible outputs. This can supply nonloop corrections that ordinary deletion omits. It depends only on adjacent source classes and their sizes, not a matrix row-reduction choice.

At source level, if either adjacent column is a loop, the surviving column gives a source isomorphism of dimension eight. If both columns are nonloops in distinct nonsingleton classes, their sum becomes a new singleton direction between the two surviving class directions. The support size falls by one and the class count rises by one, preserving dimension eight. Its source inverse decomposes the new column uniquely into positive multiples of those two surviving directions. The source dimension falls when the columns lie in the same class, or when at least one of two distinct classes is a singleton.

The matrix branch has checked that the resulting linear map, zero on dimension drops and nonadmissible outputs, sends all96 n8 parent rows into L7 and all693 n9 rows into L8. Its induced quotient maps are surjective, with kernel dimensions88 and369. The separate [amalgamation proof](AMALGAMATION_PROOF.md), independently reviewed here, now establishes the all-n statement by strict generic indicator degeneration. It controls rank-loss limits, excludes full-dimensional nonadmissible outputs by their collapse obstruction, retains multiplicities, and proves both pi K_n⊆K_(n−1) and pi L_n⊆L_(n−1). These results are compatible with (3): the extra nonloop terms have enough quotient range to cancel the naive defects.

The generic degeneration and all-n descent do not follow from the two finite matrix checks alone. Their full proof and the [simplicial identity audit](SIMPLICIAL_AMALGAMATION.md) are separate ingredients. The exact naive defect theorem and slot lemma in this document were independently reviewed by the amalgamation agent; the source basis and slot certificates above supply an additional independent implementation.
