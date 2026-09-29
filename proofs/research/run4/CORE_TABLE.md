# Complete 29-core accounting

**PROVED**, with source counts **COMPUTATIONALLY-VERIFIED** against the preserved Run3 inventory. Every row retains every codimension-one source facet. A kernel below means the space of constant-coefficient all-Z indicator relations on that single parent's admissible facets, modulo dimension below eight.

Run3 accounting is exactly 12 collapsed / 4 balanced / 2 hostile / 11 untreated. Run4 accounting is 12 collapsed / 15 balanced / 2 zero-relation obstructions / 0 untreated. The 29 cores represent 364 labeled loopless parents, and exact transport covers every loop placement.

| q | Dihedral class-size core | Source facets | Admissible | Collapsed facets | Four-mass | Spurion facets | Run3 | Run4 result | Kernel dim. |
|---:|---|---:|---:|---:|---:|---:|---|---|---:|
| 7 | (1,1,1,1,1,2) | 8 | 6 | 2 | 0 | 0 | balanced | 3↔3 | 1 |
| 8 | (1,1,1,1,4) | 9 | 0 | 9 | 0 | 0 | collapsed | Collapsed parent | 0 |
| 8 | (1,1,1,2,3) | 10 | 6 | 4 | 0 | 0 | untreated | 3↔3 | 1 |
| 8 | (1,1,2,1,3) | 10 | 6 | 4 | 0 | 0 | untreated | 3↔3 | 1 |
| 8 | (1,1,2,2,2) | 11 | 8 | 2 | 1 | 0 | hostile | No nonzero all-Z facet relation | 0 |
| 8 | (1,2,1,2,2) | 11 | 10 | 1 | 0 | 0 | balanced | 5↔5 | 1 |
| 9 | (1,1,1,6) | 10 | 0 | 10 | 0 | 0 | collapsed | Collapsed parent | 0 |
| 9 | (1,1,2,5) | 11 | 0 | 11 | 0 | 0 | collapsed | Collapsed parent | 0 |
| 9 | (1,1,3,4) | 11 | 6 | 5 | 0 | 0 | untreated | 3↔3 | 1 |
| 9 | (1,2,1,5) | 11 | 0 | 11 | 0 | 0 | collapsed | Collapsed parent | 0 |
| 9 | (1,2,2,4) | 12 | 6 | 6 | 0 | 0 | untreated | 3↔3 | 1 |
| 9 | (1,2,3,3) | 12 | 10 | 2 | 0 | 1 | balanced | 5↔5 | 1 |
| 9 | (1,2,4,2) | 12 | 6 | 6 | 0 | 0 | untreated | 3↔3 | 1 |
| 9 | (1,3,1,4) | 11 | 6 | 5 | 0 | 0 | untreated | 3↔3 | 1 |
| 9 | (1,3,2,3) | 12 | 10 | 2 | 0 | 0 | untreated | 5↔5 | 1 |
| 9 | (2,2,2,3) | 13 | 8 | 2 | 3 | 0 | hostile | No nonzero all-Z facet relation | 0 |
| 10 | (1,1,8) | 11 | 0 | 11 | 0 | 0 | collapsed | Collapsed parent | 0 |
| 10 | (1,2,7) | 12 | 0 | 12 | 0 | 0 | collapsed | Collapsed parent | 0 |
| 10 | (1,3,6) | 12 | 0 | 12 | 0 | 0 | collapsed | Collapsed parent | 0 |
| 10 | (1,4,5) | 12 | 6 | 6 | 0 | 0 | untreated | 3↔3 | 1 |
| 10 | (2,2,6) | 13 | 0 | 13 | 0 | 0 | collapsed | Collapsed parent | 0 |
| 10 | (2,3,5) | 13 | 6 | 7 | 0 | 0 | untreated | 3↔3 | 1 |
| 10 | (2,4,4) | 13 | 10 | 3 | 0 | 0 | untreated | 5↔5 | 1 |
| 10 | (3,3,4) | 13 | 10 | 3 | 0 | 4 | untreated | 5↔5 | 1 |
| 11 | (1,10) | 10 | 0 | 10 | 0 | 0 | collapsed | Collapsed parent | 0 |
| 11 | (2,9) | 11 | 0 | 11 | 0 | 0 | collapsed | Collapsed parent | 0 |
| 11 | (3,8) | 11 | 0 | 11 | 0 | 0 | collapsed | Collapsed parent | 0 |
| 11 | (4,7) | 11 | 0 | 11 | 0 | 0 | collapsed | Collapsed parent | 0 |
| 11 | (5,6) | 11 | 6 | 5 | 0 | 0 | balanced | 3↔3 | 1 |

## Mechanisms and scope

The ten complement-five circuit cores have 3↔3 relations; four genuine reflection cores and the asymmetric repaired spurion core have 5↔5 relations. The exact circuit overlap graph is K3,3 for every positive Z. For the five ten-wall cores, fixed rational positive-Z overlap trees prove that the all-Z relation kernel is exactly the known balanced span.

The two hostile cores have exact full-rank 8×8 indicator certificates at one positive Z. Thus neither admits any nonzero all-Z relation on these eight facets. The q9 conic parent has a proved admissible-facet cover hole. A single such cover of the q8 disconnected parent remains unresolved; the homogeneous relation classification does not decide it.

The complete local theorem, including all-n transport and precise limits, is in [LOCAL_PARENT_THEOREM](LOCAL_PARENT_THEOREM.md). Machine records retain affine permutations, bases, necklaces, exact source incidences, proof references and explicit prototype-to-inventory relabelings in [core_status.json](../../results/run4/core_status.json) and [sign_relations.json](../../results/run4/sign_relations.json). No source core is removed, and no generation theorem for arbitrary tilings is asserted.
