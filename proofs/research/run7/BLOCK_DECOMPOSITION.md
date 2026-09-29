# Exact support blocks and adjacent amalgamation

**COMPUTATIONALLY-VERIFIED with exact rational arithmetic.** The preserved full local matrices reconstruct as follows. Their column universes remain the complete all-Z admissible source universes, and their rows remain the complete nonzero Run 4 one-parent relations.

| n | Tile columns | Local rows | Local rank | Quotient dimension |
|---:|---:|---:|---:|---:|
| 7 | 21 | 7 | 6 | 15 |
| 8 | 176 | 96 | 73 | 103 |
| 9 | 942 | 693 | 470 | 472 |

Every old file is a read-only input. New exact data are in [rank_data](../../results/run7/rank_data.json) and [block_ranks](../../results/run7/block_ranks.json); source and checks are [run7_blocks.py](../../src/magic_number/run7_blocks.py) and [test_run7_blocks.py](../../tests/test_run7_blocks.py).

## Support filtration and fixed insertions

Let Fq be the image in Qn=Un/Ln of all tile columns with support at most q. Exact ranks are

| n | dim F6 | dim F7 | dim F8 | dim F9 |
|---:|---:|---:|---:|---:|
| 7 | 7 | 15 | | |
| 8 | 28 | 92 | 103 | |
| 9 | 84 | 372 | 471 | 472 |

For a chosen column subset S, the producer uses

\[
\dim\operatorname{im}(U_S\to Q_n)=|S|-\operatorname{rank}L_n
 +\operatorname{rank}(L_n\text{ projected outside }S).
\]

An independent implementation instead reduces each selected coordinate vector to quotient normal form and computes their rational span. These give the same filtration ranks.

**PROVED (transport) / COMPUTATIONALLY-VERIFIED (finite checks).** Inserting a zero column at any fixed position preserves all-Z indicator relations and is injective on the indicator quotient, using positive external-matrix extension to recover the reverse implication. At n7,8,9 the fixed insertion images have dimensions 1,15,103. Their sum over all insertion positions has dimensions 7,92,471, leaving loopless quotient dimensions 8,11,1 respectively.

For all 21,28,36 pairs of omitted labels, the intersection of the two fixed-insertion quotient subspaces equals the image from their common support. Dimensions are 0,1,15 at n7,8,9. The common-support image is manifestly contained in the intersection; equality follows from the exact union/intersection dimension calculation. These finite pair intersections do not by themselves establish a general exact support complex or an all-n direct-sum decomposition.

## The corrected adjacent map on source labels

For ordinary adjacent final labels a=n−1,b=n, form C′ by replacing column a with ca+cb and deleting b. Every ordered minor involving the new column is a sum of two nonnegative old ordered minors. Thus the generic output basis set is exactly the image of the old bases under identifying b with a, discarding repeated-label pairs. There is no sign cancellation. This proves the combinatorial output cell for every positive source parameter point; numerical samples are used only as an independent regression check.

With q nonloop labels and s parallel classes, the source dimension is q+s−4. The output dimension cases are:

| Input columns | Change in q,s | Dimension change |
|---|---|---:|
| At least one loop | q,s unchanged | 0 |
| Same nonloop class | q decreases by1, s unchanged | −1 |
| Different classes, both nonsingleton | q decreases by1, s increases by1 | 0 |
| Exactly one class singleton | q decreases by1, s unchanged | −1 |
| Both classes singleton | q decreases by1, s decreases by1 | −2 |

The first case uses order-preserving relabeling when the surviving nonloop moves. In the different-class case the sum direction lies strictly between the two adjacent projective directions in the signed cyclic chart, creating a new singleton class; the residual classes survive exactly when nonsingleton. The basis-union formula handles wrapping classes without assigning incorrect raw positive coefficients to representative rays.

Define a linear map A on free certified-tile labels by sending a label to this output tile when the output is eight-dimensional and certified admissible, and to zero otherwise. This is initially a **combinatorial map**, not an asserted pushforward of arbitrary tile indicators.

| Transition | Certified tile outputs | Dimension8 non-tile outputs | Dimension7 | Dimension6 |
|---|---:|---:|---:|---:|
| 8→7 | 52 | 2 | 88 | 34 |
| 9→8 | 393 | 16 | 428 | 105 |

Every eight-dimensional non-tile output in these two inventories has the class-complement dimension obstruction. None is four-mass. A distinct-class amalgamation creates a singleton and therefore cannot produce the four-mass profile; a loop case preserves the source cell up to relabeling, and the other cases lose dimension.

## Exact finite quotient map and splitting

**PROVED by exact certificates, for these finite transitions.** All 96 rows at n8 map into L7, and all 693 rows at n9 map into L8. Each image is stored together with its exact coefficients in the downstairs rational row basis. The image ranks are6 and73 respectively. Every downstairs tile is hit.

Inserting a final zero column is an exact right inverse on the free tile spaces. Its images of all downstairs local rows lie in the upstairs row span, checked independently. Therefore A induces split surjections

\[
Q_8\longrightarrow Q_7,\quad \dim\ker=88;
\qquad Q_9\longrightarrow Q_8,\quad \dim\ker=369.
\]

The induced quotient matrices and the right-inverse tile columns are explicit. A surjective quotient map alone does not prove generation of arbitrary indicator relations or provide an all-n induction.

**PROVED finite corollary using the preserved complete-kernel theorems.** The standard BCFW tiling vectors map exactly to the standard downstairs tiling vectors: 20 pieces to6, and50 pieces to20, with no repeated output label. For any complete all-Z upstairs tiling χ, the preserved theorem K= L gives χ−χstandard in L. Hence Aχ has the same all-Z indicator as the downstairs standard tiling. It is a nonnegative integer combination of genuine downstairs tile indicators. Any coefficient greater than1, or an overlap of two selected open tile images, would contradict indicator value one on a nonempty open set. Thus every surviving coefficient is1, the interiors are disjoint, and the finite closed union covers the amplituhedron. Accordingly A sends every complete all-Z n8/n9 tiling to a complete all-Z downstairs tiling.

This corollary uses the finite kernel theorems, not an unproved geometric degeneration. It does not prove that every downstairs tiling lifts, nor extend the map theorem to arbitrary n.

## Normalized finite-core diagnostic

The separate [pre-registered diagnostic](N10_DIAGNOSTIC.md) retains only columns with no loops or sole loop1. Its exact results and alternating boundary matrices are stored in [normalized_core_ranks](../../results/run7/normalized_core_ranks.json). They are the quotient by all coordinate degeneracy subspaces together with local relations, independently of whether the proposed simplicial structure has yet been proved.

The normalized quotient dimensions at n6,…,11 are **1,9,19,12,0,0**. In particular the projected n10 matrix has rank35 on35 columns; the predicted surviving n10 class does not exist. Its square minor has determinant−1. Every normalized n10 coordinate vector is explicitly expressed as an integer combination of projected local rows. At n11, rank5 on5 columns gives zero, with determinant+1. Any n≥12 tile has at least one loop among positions2,…,n because eight-dimensional rank-two cells have at most10 nonloop labels, so there are no retained columns.

The normalized alternating face boundaries have ranks1,7,12,0,0 for n7,…,11. Every projected parent row maps to the downstairs projected row span. Independent rational tests verify that the induced consecutive boundary matrices multiply to zero. The wrap face is checked on source matrices as c1←c1−cn, delete n; its ordered minors are again positive sums. These finite matrices do not alone prove all simplicial identities or universal preservation of the local/indicator relation spaces.

## Integration with the separately proved all-n maps

**PROVED, independently reviewed.** The uniform geometric and simplicial arguments now establish the missing structural hypotheses. As verified in [GLOBAL_PARENT_REVIEW](GLOBAL_PARENT_REVIEW.md), exact normalization of H=K/L inside Q=V/L, the preserved H9=0, and the normalized zero certificates above imply H_n=0 for all n. Thus K_n=L_n and

\[
\dim Q_n=\binom{n-1}5+9\binom{n-1}6+19\binom{n-1}7+12\binom{n-1}8.
\]

The all-n result comes from the proved maps plus the exact finite normalized certificates, rather than an extrapolation of the first support table. The earlier1675 prediction at n10 fails; the proved value is1674. Generation by local relations implies balancedness of every all-Z indicator relation and the k2,m4 Magic Number formula. It still does not assert that every local relation extends to a difference of complete tilings, or that the complete tiling flip graph is connected.
