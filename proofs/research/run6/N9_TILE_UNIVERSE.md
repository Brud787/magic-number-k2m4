# Complete n9 all-Z tile source universe

**SOURCE-VERIFIED / PROVED (preserved classification), COMPUTATIONALLY-VERIFIED (new inventory).** The complete eight-dimensional rank-two all-Z admissible source universe at n=9 has 942 cells: 939 general BCFW cells and three cyclic spurion cells. The other 612 of the 1554 source cells are excluded by the preserved exact certificates: 594 class-complement image-dimension obstructions and 18 loop embeddings of the nonadmissible four-mass source.

This run reconstructs that classification from the preserved [Run 2 child-status catalog](../../results/run2/child_status_n9.json); it does not infer injectivity from dimension, differential rank, or numerical samples. BCFW cells retain their explicit general BCFW recipes and the reviewed source theorem. The three non-BCFW cells retain the published spurion certificate and cyclic symmetry. Four-mass loop exclusions use the preserved positive row-extension proof, which transports failure of all-Z admissibility; they are not asserted to fail injectivity at every positive matrix.

The new [complete inventory](../../results/run6/tile_universe_n9.json) fixes lexicographic affine-permutation column order and records every tile's bases, Grassmann necklace, parallel classes, loops, support, class profile, admissibility certificate, proof reference and dihedral orbit with explicit transport actions.

| Nonloop support size | Certified tile count |
|---:|---:|
| 6 | 84 |
| 7 | 504 |
| 8 | 324 |
| 9 | 30 |

**COMPUTATIONALLY-VERIFIED.** There are 61 dihedral orbits: two of size 3, fourteen of size 9 and forty-five of size 18. The orbit records partition all 942 labels. Direct transformations of basis sets independently check both membership and the recorded actions.

**COMPUTATIONALLY-VERIFIED.** Every one of the 939 BCFW labels has a parallel class whose complement in the nonloop support consists of exactly five labels. None of the three spurions has this property: their profile is (3,3,3), so every class complement has six labels. The inventory lists all qualifying class indices and chooses the first when one exists.

The complement-five flag establishes applicability of a source profile, not by itself a closed-image membership certificate. The Run 6 indicator branch must prove and check complete membership, including closure and cyclic-sign conventions, separately. In particular, the three spurions cannot be sent silently through the complement-five inverse.

The producer is [run6_local_span.py](../../src/magic_number/run6_local_span.py), function `tile_inventory()`. Independent checks in [test_run6_local_span.py](../../tests/test_run6_local_span.py) enumerate all dimension-eight bounded affine permutations, recover necklaces and bases independently, compare the complete preserved certificate partition, and verify every dihedral orbit using basis label maps. No old research or artifact file is modified.
