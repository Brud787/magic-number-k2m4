# Full local relation spans at n=7 and n=8

**COMPUTATIONALLY-VERIFIED, with exact certificates.** In the complete all-\(Z\) admissible rank-two tile universes, the transported Run 4 parent relations have the following ranks:

| \(n\) | Complete tile universe | All source parents | Nonzero parent rows | \(\dim_{\mathbb Q}L_n\) | \(\dim_{\mathbb Q}(U_n/L_n)\) |
|---:|---:|---:|---:|---:|---:|
| 7 | 21 | 7 | 7 | 6 | 15 |
| 8 | 176 | 112 | 96 | 73 | 103 |

Here \(U_n\) is the free rational vector space on the certified all-\(Z\) tile source labels, and \(L_n\) is the span of **all** nonzero one-parent relations supplied by the complete Run 4 theorem, transported to \([n]\). The displayed quotient is the algebraic quotient by these parent relations; it is not yet asserted here to be the actual indicator-function quotient.

Every known complete standard-dihedral BCFW tiling difference belongs to this full local span. This is checked for all 21 pairs of the seven known \(n=7\) tilings and all 120 pairs of the sixteen known \(n=8\) tilings. The known \(n=8\) difference subspace has rank 15; adjoining it to \(L_8\) leaves rank 73. No separating covector against these known tiling differences exists.

## Source and geometric inputs

**SOURCE-VERIFIED / PROVED (preserved inputs).** The complete tile universes come from the all-Z admissibility classification in the preserved Run 2 child-status catalogs: 21 of 28 eight-dimensional sources at \(n=7\), and 176 of 266 at \(n=8\). The latter universe consists of the 176 general BCFW source cells; its other sources were already excluded by exact dimension or four-mass certificates. No source cell is included from differential rank alone.

The signed prototype relations are read directly from the preserved Run 4 sign-relations artifact and carry its all-\(Z\) geometric proofs. For each prototype of support \(q\le n\), every dihedral action on the \(q\) nonloop labels and every increasing \(q\)-element support insertion into \([n]\) is applied. Each row is then normalized by one common sign so its first nonzero entry is positive. Duplicate row vectors are identified, retaining every source-parent label and every transport action.

The complete ambient parent inventory is independently checked against bounded affine permutations of source dimension nine. The relation-generation table is:

| Ambient universe | Support of parent | Balanced parents / rows | Collapsed parents | Hostile parents |
|---|---:|---:|---:|---:|
| \(n=7\) | 7 | 7 | 0 | 0 |
| \(n=8\) | 7 | 56 | 0 | 0 |
| \(n=8\) | 8 | 40 | 8 | 8 |

Each balanced parent contributes its complete one-dimensional facet relation space, as proved in Run 4. The row support equals exactly the parent's set of all-\(Z\) admissible facets. The collapsed and hostile parents have zero facet-relation kernel and contribute no nonzero rows. Thus the 96-row \(n=8\) matrix is the **full** one-parent matrix, including eight-support circuit and reflection types; it is not the old seven-support subset.

All 21 or 176 tile columns participate in the corresponding full matrix. At \(n=8\), 88 rows have six nonzero entries and eight rows have ten. Their coefficient sums are all zero because they are the certified \(3\leftrightarrow3\) and \(5\leftrightarrow5\) relations.

## Exact linear algebra and the previous obstruction

**COMPUTATIONALLY-VERIFIED.** The 56 seven-support rows have rank 48. The 40 eight-support rows have rank 40. Their combined rank is 73, so the two row spaces intersect in dimension 15:

\[
48+40-73=15.
\]

The preserved Run 2 result about seven-support moves remains valid: its rank-48 span meets the rank-15 standard-dihedral tiling-difference space only in zero. This was explicitly a theorem about the smaller move set.

**FAILED (bounded counterexample attempt against the full move set).** Testing the same known complete-tiling differences against the complete 96-row matrix produces no outside vector. Every one is in \(L_8\). Consequently these examples do not refute the Run 5 full local-span proposal. This is a recheck with the larger source-parent universe, not repetition of the old seven-support obstruction.

The implementation first chooses exact independent rows and pivot columns. It solves the restricted invertible rational system for each difference from one fixed base tiling, then verifies equality in **every** tile column. All six \(n=7\) and fifteen \(n=8\) relative-base certificates have integer row coefficients; in these certificates each nonzero coefficient is \(+1\) or \(-1\). Subtracting the certificates gives every pair difference, checked separately using Fraction arithmetic.

These integer decompositions are formal sums of valid geometric relations. They do not give an order of realizable local replacements through intermediate complete tilings. No path in a tiling graph is claimed by this calculation.

## Stored certificates and independent checks

Machine files:

- [Full n7 matrix](../../results/run5/local_relation_matrix_n7.json)
- [Full n8 matrix](../../results/run5/local_relation_matrix_n8.json)
- [Known n7 tiling-difference decompositions](../../results/run5/known_tiling_span_n7.json)
- [Known n8 tiling-difference decompositions](../../results/run5/known_tiling_span_n8.json)

The column order is lexicographic in bounded affine permutations, stored as **column_affine_permutations**. The **rows** field is the complete integer matrix. Tile records retain bases, necklaces, parallel classes and all-\(Z\) admissibility provenance. Parent records retain full labeled source data, their admissible facets, sector, and relation-row indices. Relation records retain every prototype/dihedral/insertion origin. The tiling files retain both full all-\(Z\) tilings and exact coefficients in the local rows.

**COMPUTATIONALLY-VERIFIED.** Four new tests pass in 2.33 seconds. The checks include:

- complete labeled parent coverage from an independent affine-window enumeration;
- independent transformation of the actual basis sets for every retained transport origin;
- exact ranks checked with Fraction Gaussian elimination separately from the producer's SymPy reduction;
- every one of the 21 and 120 complete-tiling pair differences reconstructed from exact saved local coefficients, with their tiling sets checked against the preserved source-certified fixtures.

The producer is [run5_local_span.py](../../src/magic_number/run5_local_span.py). Its public functions are **build_local_matrix(n)** and **known_tiling_span(n)** for \(n=7,8\).

    PYTHONPATH=src .venv/bin/python -m magic_number.run5_local_span
    PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_run5_local_span.py

## What supplies the missing global kernel bound at n8

**PROVED in the separate Run 5 indicator certificate.** The rank computations in this file alone establish \(L_8\subseteq\ker\Phi_8\) and inclusion of the known standard-dihedral difference family. The complete membership theorem and determinant-two rank certificate in [N8_INDICATOR_THEOREM](N8_INDICATOR_THEOREM.md), independently checked in [INDICATOR_INDEPENDENT_REVIEW](INDICATOR_INDEPENDENT_REVIEW.md), supply the additional bound and prove equality with the complete all-\(Z\) indicator kernel.

The independent genuine-flip ancestry certificate in [N8_FLIP_SPAN](N8_FLIP_SPAN.md) supplies \(L_8\subseteq D_8\), yielding \(D_8=L_8\) when combined with the indicator theorem. Neither conclusion should be inferred solely from the standard-orbit row decompositions here. The separate n7 branch also has its own completeness and actual flip-path certificates.

No complete \(n=8\) tiling enumeration, open-ended source enumeration, or new literature audit was launched in this subtask. These finite results do not settle the all-\(n\) generation question or connectivity of the entire \(n=8\) tiling graph.
