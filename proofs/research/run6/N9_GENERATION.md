# Genuine finite generation of the n9 local span

**PROVED with exact finite certificates.** Every vector in the full 470-dimensional local relation span L9 belongs to the rational span D9 of differences between complete all-Z n9 tilings. A bounded legal-flip walk supplies 461 independent differences. Finite dihedral transport of its already certified tilings supplies the remaining nine dimensions. No additional flip search is used for the symmetry completion.

The reverse inclusion D9 contained in L9 is a separate consequence of the Run 6 full indicator-kernel certificate. The construction here proves L9 contained in D9 directly: every displayed vector is a genuine difference of two complete all-Z tilings, belongs to L9 by exact row reduction, and the 470 displayed vectors are independent.

## What the bounded walk did and did not do

**COMPUTATIONALLY-VERIFIED.** Starting from the standard 50-piece BCFW tiling, the seeded walk applies only the Run 4 multiplicity-one 3-to-3 and 5-to-5 replacements. At each step it checks that the removed side is present and the added side is absent. It prefers a currently available independent relation, otherwise a rarely visited successor. The walk stops at the authorized cap of 15000 distinct states after 14999 steps, with rank **461**, short of the target 470. This cap and partial result are preserved in the [walk certificate](../../results/run6/tiling_span_witness_n9.json).

The artifact retains 12857 ancestral nodes sufficient to certify 461 independent selected tilings, together with the base. Every retained node names its source parent, local row and direction. Each selected tiling retains its complete 50-column set, actual difference from the base, exact ancestral path and integer coefficients in local rows. The 461-by-461 minor of the actual tiling-difference matrix has determinant **+1**.

**PROVED (inductive geometry).** The base collection is an all-Z BCFW tiling. Each retained step replaces one certified multiplicity-one local decomposition by the other decomposition of exactly the same closed region. Thus coverage, interior disjointness and multiplicity one persist for every positive matrix. Every retained node is a complete all-Z tiling. This proof uses the geometric Run 4 theorem; source boundary incidence alone would not justify the step.

The bounded walk itself does not span L9. It is not a complete tiling enumeration and establishes no connectivity statement for the entire tiling graph.

## Finite symmetry completion

The one-step signed cyclic symmetry transports each already certified complete tiling and its BCFW base to another pair of complete all-Z tilings. This yields a genuine difference even though no path from the original base to its cyclic transform is asserted.

**COMPUTATIONALLY-VERIFIED.** Among the 461 cyclic images of the selected differences, nine enlarge the span from rank 461 to rank 470. They come from ancestral nodes 96, 118, 1955, 1956, 1959, 7806, 9753, 11366 and 12856. Every action is the label map i to i+1 modulo nine, with the source and external sign conventions covered by the preserved dihedral transport theorem.

The [symmetry-completion artifact](../../results/run6/tiling_symmetry_completion_n9.json) records both complete tilings for every extra difference, the original selected node, the transport action, and hashes of the unchanged input certificates. The combined 470-by-470 actual-difference minor has determinant **−1**. Independent basis label maps verify each transport, and exact reduction against the stored local RREF verifies that all nine additional vectors lie in L9.

Therefore the 470 independent genuine tiling differences form a basis of L9. The symmetry step adds **zero** new flip states; it is a finite audit of the saved witnesses after the walk cap was reached.

## Independent checks and limits

The producer is [run6_flip_span.py](../../src/magic_number/run6_flip_span.py). The checks in [test_run6_flip_span.py](../../tests/test_run6_flip_span.py) independently:

- replay every retained replacement as a set operation and verify the source-certified base;
- reconstruct all selected differences from their exact ancestral integer local coefficients;
- verify cyclic images through full positroid basis sets;
- compute both determinants by a separate rational **column** elimination, while the producer uses rational row elimination;
- reduce every added cyclic difference against the complete local matrix.

No completeness of the walk's component, connectivity of all complete n9 tilings, or all-n generation theorem is claimed. Combined with the separate full kernel theorem this yields the finite equality D9=L9; it does not supply an induction to arbitrary n.
