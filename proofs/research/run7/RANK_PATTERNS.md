# Finite support ranks and the next diagnostic

**COMPUTATIONALLY-VERIFIED (preserved matrices, reconstructed exactly).** The complete local quotient dimensions at n=7,8,9 are 15,103,472. Their filtration by nonloop support has dimensions

| n | Support ≤6 | Support ≤7 | Support ≤8 | Support ≤9 |
|---:|---:|---:|---:|---:|
| 7 | 7 | 15 | | |
| 8 | 28 | 92 | 103 | |
| 9 | 84 | 372 | 471 | 472 |

The corresponding increments per support are 1,8,11,1 at support sizes 6,7,8,9. This suggests

\[
\dim Q_n=\binom n6+8\binom n7+11\binom n8+\binom n9.
\]

**CONJECTURAL at the time this diagnostic was proposed.** Agreement at n≤9 does not prove this formula. A support filtration gives an upper-bound strategy using explicit local reducers, but larger-support relations could identify previously independent classes. No full n10 matrix, indicator experiment or tiling enumeration is needed to state that obstruction.

## Recorded precondition for the bounded normalized diagnostic

Before computing new support10/11 data, the root proposed a sharper test. Suppose adjacent column amalgamation induces simplicial face maps on the quotient and inserting a loop after each label gives degeneracies, with all identities and local-relation preservation proved independently. Quotienting by degeneracies then leaves only columns supported on every label or every label except label1. There are respectively 1,15,50,66,35,5 such columns at n=6,…,11, and none for n≥12.

The proposed normalized quotient dimensions are 1,9,19,12,1,0 at n=6,…,11. A simplicial decomposition would then imply the displayed binomial formula. **These dimensions are predictions here, and the simplicial identities/local-relation transport are separate proof obligations.** The purpose of the next bounded computation is to test those predictions using only projected finite-core matrices. No full n10 relation matrix will be built.

**Kill-tests.** A projected rank different from the predicted normalized rank kills this proposed formula. A face or degeneracy identity failing after dimension/admissibility truncation kills the simplicial mechanism. A single certified parent relation mapping outside the downstairs local span kills quotient functoriality. Passing finite rank checks alone does not discharge either structural obligation.

## Result: the predicted normalized n10 class is absent

**FAILED (normalized prediction), COMPUTATIONALLY-VERIFIED (exact replacement).** The bounded diagnostic found normalized dimensions **1,9,19,12,0,0**, with a determinant−1 minor proving rank35 at n10. Thus the conjectured normalized n10 dimension1 is false. All n10/n11 normalized coordinate vectors have explicit integer reductions by projected local relations.

**Conditional structural consequence.** If the independently audited simplicial quotient structure is established, its dimension decomposition instead gives

\[
\dim Q_n=\binom{n-1}5+9\binom{n-1}6+19\binom{n-1}7+12\binom{n-1}8.
\]

This is the earlier suggested expression minus \(\binom{n-1}9\). It agrees with all previously known n≤9 ranks. The formula is not inferred merely by fitting finite numbers: its use requires the full simplicial identity, degeneracy, and local-relation preservation proof. The finite matrices here supply the normalized dimensions needed by that independent argument, not the argument itself.

## Final structural conclusion

**PROVED, independently reviewed.** The geometric face-map theorem and all simplicial identities have now passed their separate audits. The normalization argument in [GLOBAL_GENERATION](GLOBAL_GENERATION.md), checked in [GLOBAL_PARENT_REVIEW](GLOBAL_PARENT_REVIEW.md), therefore establishes the preceding corrected formula for every n≥6. It also proves K_n=L_n, so this is the actual all-Z indicator quotient dimension.

At n10 the quotient dimension is1674 and the local-relation rank is2141 on3815 tile labels. The initially conjectured quotient1675 and rank2140 are **FAILED**. No full n10 matrix was computed; the conclusion uses the35-column diagnostic, five-column n11 certificate, support bound and proved simplicial structure. The failure is retained above rather than silently replacing the original prediction.
