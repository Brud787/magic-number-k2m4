# Run 5: genuine tilings span every local relation at n=8

**PROVED by a finite exact certificate, using the preserved all-Z geometric flip theorem.** Let U_8 be the certified 176-cell all-Z tile universe, let L_8 be the 73-dimensional rational span of the 96 Run 4 parent relations, and let D_8 be the rational span of differences of complete all-Z positroid tilings. Then

\[
L_8\subseteq D_8.
\]

More precisely, seventy-four explicit complete all-Z tilings in the flip component of one standard tiling have a 73-dimensional difference span, equal to L_8. This does not assert that every tiling lies in this component, nor enumerate all tilings. The reverse inclusion D_8⊆L_8 is established by the separate [indicator-kernel theorem](N8_INDICATOR_THEOREM.md), whose [independent membership audit](INDICATOR_INDEPENDENT_REVIEW.md) passed.

## 1. Inputs and the geometric induction

The source inputs are [the complete local relation matrix](../../results/run5/local_relation_matrix_n8.json) and [the known standard-dihedral tilings](../../results/run5/known_tiling_span_n8.json). Their exact file hashes and the full column order are retained in the new certificate. The base is the first recorded standard-dihedral tiling, `n8-T00`; its all-Z tiling provenance is the BCFW theorem, with the independently implemented KWZ standard-cell construction and dihedral transport. See [LOCAL_SPAN](LOCAL_SPAN.md).

Each local row is supported on the admissible source facets of one nine-dimensional positroid parent. The [Run 4 theorem](../run4/LOCAL_PARENT_THEOREM.md) proves that the positive and negative sides separately tile the same closed parent image, for every positive external matrix. At n=8 the 96 rows consist of 88 six-term rows and eight ten-term rows. Their side sizes are respectively 3+3 and 5+5.

Suppose T is a complete all-Z tiling and contains every tile on one side A of such a relation, with none of the opposite side B. Replace A by B. Its closed union is unchanged because the two sides have equal closed union. The new tiles have mutually disjoint open images by the local theorem. They also have disjoint open images from the unchanged tiles: otherwise a nonempty open intersection with an unchanged tile would meet the dense union of the old side's open images, contradicting the old tiling. All tiles remain all-Z admissible. This proves by induction that every state reached by these replacements is a complete all-Z tiling.

The algorithm explicitly checks side containment and absence of the added tiles. It does not use sampled image membership to authorize a replacement. The 3+3/5+5 balance also preserves twenty tiles in every reached state, although that alone says nothing about unreached tilings.

## 2. The bounded search and retained proof data

[run5_flip_span.py](../../src/magic_number/run5_flip_span.py) performs deterministic breadth-first search from the base, using the 96 integer rows in their preserved order and both directions. States are exact subsets of the 176 columns. The cap is 3,000 discovered states. An incremental rank calculation modulo 1,000,003 selects independent differences, and the search stops immediately upon selecting 73 of them.

The actual stopping data are:

| Quantity | Value |
|---|---:|
| Discovered states, including the base | 2,440 |
| States processed, with the last expansion partial | 2,229 |
| Selected independent differences | 73 |
| Explicit selected tilings, including the base | 74 |
| Retained nodes in their ancestral proof tree | 153 |
| Longest retained selected path | 13 flips |
| Distinct local rows used in the retained tree | 74 |
| Exact rank of the saved square minor over Q | 73 |

The [certificate](../../results/run5/tiling_span_witness_n8.json) does not retain a putative complete tiling list. It retains the base; the selected tilings as column subsets; each full integer difference vector; a square 73×73 minor; and the ancestral paths needed to prove their tiling status. Each tree edge records its predecessor, local row, direction, relation identifier, and source-parent affine permutation. Integer local-row coefficients reconstruct every selected difference exactly.

The modular calculation is only a discovery screen. The saved minor is checked by the separate `Fraction` Gaussian-elimination implementation in `exact_geometry.matrix_rank`. Its exact full rank gives a lower bound of 73 over Q. Every selected difference is an integer sum of the preserved local rows, whose full rank is independently known to be 73. Therefore the difference span is **exactly** L_8, with no modular-rank extrapolation.

## 3. The linear consequence and its limits

Let H be the span of the 73 saved differences. The geometric induction proves H⊆D_8. The saved integral path decompositions prove H⊆L_8. The independently verified ranks give dim H=dim L_8=73, hence H=L_8 and L_8⊆D_8.

The separate complete-indicator certificate proves D_8⊆L_8, so the two results combine to give D_8=L_8. This file supplies the inclusion through actual complete tilings; it does not assume the published BCFW formula-rank computation and does not infer a global flip path from linear span equality.

The numbers 176 and 74 have antecedents in Bourjaily's BCFW formula computation, documented in [LITERATURE_DELTA](LITERATURE_DELTA.md). The present proof artifact independently supplies all-Z geometric paths and exact linear certificates for the required inclusion. No priority claim follows from this comparison.

## 4. Verification

**COMPUTATIONALLY-VERIFIED:** the three new tests pass. They replay every retained replacement using sets rather than the producer's bit masks; verify all integer difference decompositions; verify the independent rational minor rank; check every participating source cell has dimension eight and is below its recorded nine-dimensional parent using the independent affine-permutation basis implementation; and reject a reversed initial proof step.

```sh
PYTHONPATH=src .venv/bin/python -m magic_number.run5_flip_span
PYTHONPATH=src .venv/bin/python -m pytest tests/test_run5_flip_span.py -q
```

Recorded result: **3 passed in 0.36 seconds**. The geometric side equalities and base tiling theorem remain explicit mathematical dependencies. This was a bounded spanning search, not a classification of all complete tilings or a proof of their flip connectivity.
