# Source deletion does not descend through the local relation quotient

**PROVED.** The natural degree-eight source deletion map does not send L_n into L_(n−1), already for n=7, and also for the explicit n8→n7 certificate below. Thus it cannot directly define an induction on the quotient of tile generators by local relations.

## 1. Specify the map before asking it to commute

Let V_n be the free vector space on the all-Z admissible eight-dimensional source cells. For a label j, define delta_j on a generator e_S by deleting j if j is a loop, and by zero if j is a nonloop. Relabel remaining indices increasingly.

This is the dimension-eight part of ordinary source column deletion. Deleting a nonloop from a nonsingleton class lowers q by one and preserves s, so the resulting image source cell has dimension seven. Deleting a singleton also lowers s and gives dimension six, unless rank drops further. Deleting a loop preserves source dimension and tile admissibility by exact positive row restriction/extension.

There is no claimed canonical map between amplituhedron targets for arbitrary fixed Z and the data with one row deleted. This is a precisely specified linear map on source labels; any geometric degeneration recurrence needs its own construction.

## 2. The smallest symbolic obstruction

Take the nine-dimensional loopless seven-label parent with one double parallel class D and five singleton classes. Its all-Z six-wall relation is the complement-five Gale relation. Its admissible facets are deletion of either member of D and the four successive mergers among the five complementary singleton classes. The two other mergers involving D are collapsed.

Let j be one member of D. Exactly one of these six admissible facets has loop j: the facet deleting j. All other terms use j. Therefore delta_j sends the local relation to plus or minus the unique eight-dimensional top-cell generator of Gr≥0(2,6). But there are no nine-dimensional source cells at n=6, so L_6=0. Thus delta_j(L_7) is not contained in L_6.

The projected coefficient sum is ±1. This obstruction uses an already proved all-Z relation and exact source deletion, not a numerical image test. Zero insertion transports it to larger n: choose an embedded seven-label parent containing j in its double class, with j not one of the inserted loops. Its projected row is again a single tile generator, and cannot belong to L_(n−1), whose rows all have coefficient sum zero.

## 3. Exact matrix fixture at n8→n7

The [saved certificate](../../results/run6/deletion_obstruction.json) uses the complete existing96×176 local matrix at n8 and7×21 local matrix at n7. It records the deleted label, full source and target column order, the column projection, the chosen source-parent affine label, its signed local row, and the resulting projected row.

For this fixture the projected row has exactly one nonzero entry, equal to+1. The all-ones covector annihilates every target local row and evaluates to1 on this projected row. This is an exact separating covector proving nonmembership in L_7. Independent tests reconstruct the projection from affine-permutation basis sets, without using the producing parallel-class deletion routine.

## 4. What survives and what is missing

Zero insertion in the opposite direction does preserve the local relations: it preserves the entire image identity on a positive row submatrix. The deletion map is a left inverse on the inserted coordinate subspace, but the counterexample shows that it does not descend to a left inverse on the full relation quotient.

A successful deletion induction would need correction terms for tiles using the removed label, or a different geometric boundary/limit map with its own comparison theorem. Lower-dimensional source strata, boundary images, and real fiber multiplicities cannot simply be discarded in the hope that the remaining eight-dimensional labels retain the relation. This failure does not obstruct every possible recurrence and does not disprove Magic Number.

## 5. A quotient injection that does follow

**PROVED, using the preserved Run5 theorem K_8=L_8.** For every increasing eight-label support I in [n], zero insertion induces an injective map V_8/L_8 → V_n/L_n. This does not require K_n=L_n.

Here K_n denotes all constant-coefficient all-Z tile-indicator relations modulo lower-dimensional sets. Zero insertion sends L_8 into L_n by transport of the certified local relations. Suppose an inserted vector i_I(v) lies in L_n. Since L_n is contained in K_n, its image indicator vanishes modulo lower dimension for every positive ambient external matrix Z. For any prescribed positive eight-row matrix W, the [positive extension lemma](../run2/POSITIVE_EXTENSION.md) provides such a Z with Z_I=W. The target relation then is exactly the eight-label indicator relation for v at W, because the source zero columns do not contribute to CZ. As W was arbitrary, v lies in K_8=L_8. This proves injectivity.

Thus insertion gives useful quotient embeddings even though the natural deletion projection above fails to descend. An inserted complete eight-label tiling covers the amplituhedron determined by that row submatrix; it is not asserted to cover the entire n-label amplituhedron.

**COMPUTATIONALLY-VERIFIED exact support calculation.** The full n9 local matrix has rank470 and942 columns, of which30 are loopless. Its projection onto these30 columns has exact rational rank29, independently computed by the local-matrix agent and saved in the [support-block certificate](../../results/run6/support_blocks.json). The image in V_9/L_9 of the912 generators supported on at most eight labels consequently has dimension

\[
912-\bigl(470-29\bigr)=471.
\]

The whole quotient has dimension472, so its lower-support generators miss exactly one quotient dimension. This finite support calculation rules out the simplest claim that all n9 quotient classes are generated by n8 insertions. It neither gives a deletion recurrence nor determines the behavior at larger support.


**PROVED Run6 corollary.** With the independently audited equality K9=L9, the same positive-extension argument gives an injective map Q9→Qn for every increasing nine-label support and every n≥9. This transports one solved local quotient into a larger one; it does not show that these images exhaust Qn or determine Dn. No all-n generation conclusion follows.
