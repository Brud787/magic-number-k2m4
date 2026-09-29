# Independent review of Run 2 admissibility certificates

Reviewer: the parent-enumeration subagent, separately from the author of `positive_extension.py` and `general_bcfw.py`. This is a mathematical audit of the two certificates, not merely a rerun of their tests. Review date: 2026-09-05.

## Positive external-row extension

**PROVED / REVIEWED.** The lemma and implementation in [POSITIVE_EXTENSION.md](POSITIVE_EXTENSION.md) and `src/magic_number/positive_extension.py` are valid for the stated even external dimension, including `d=6` used here. No critical issue was found.

For the append construction, let `J` be an increasing `(d-1)`-subset and let `r` be the first missing index in the descending list `q,q-1,...,q-d+1`. Such an `r` exists since `J` has only `d-1` elements. All earlier determinant terms vanish because their rows occur in `J`. Exactly the `r` larger indices occur in `J`, so moving the first missing row from the last determinant position to its increasing position makes exactly `r` transpositions. The resulting determinant sign cancels the `(-1)^r` coefficient. The leading coefficient is therefore an old positive maximal minor. This argument establishes positivity for arbitrary positive input matrices, rather than only moment-curve inputs.

The code's common rational bound is sufficient. After dividing a new-minor polynomial by its leading epsilon power, write it as `D + sum_{j>=1} c_j epsilon^j`. For `0<epsilon<=1/2`, the absolute tail is at most `epsilon sum |c_j|`; the code imposes `epsilon<=D/(2 sum |c_j|)` whenever that sum is nonzero. Every new maximal minor is consequently positive, with a strict margin. Old maximal minors are unchanged. The code computes these determinant coefficients with `Fraction` arithmetic.

The prescribed-gap signed rotation is also correct. Rotating a suffix ahead of a negated prefix preserves every ordered `d`-minor: if `t` selected rows cross the cut, the total sign is

\[
(-1)^t(-1)^{t(d-t)}=1\quad\text{for even }d.
\]

After appending to `(suffix,-prefix)`, rotate the resulting positive list to `(-prefix,w,-suffix)` and multiply every row by `-1`. Global row negation preserves even-order minors and yields precisely `(prefix,-w,suffix)`, the implementation's output. This explicitly justifies the final minus sign. It also covers the endpoint gaps: `after=0` inserts `-w` before the old list; `after=q` starts from the globally negated old list and gives the ordinary positive append row.

**PROVED / REVIEWED.** Transfer of failure of all-Z injectivity through a loop insertion follows with its stated quantifier. Choose the positive external matrix witnessing noninjectivity and the two distinct nonnegative source row spaces. Insert a positive external row while inserting zero columns in the source representatives. Both matrix products are unchanged. The distinct source row spaces remain distinct because deleting the inserted zero column recovers them. Hence the embedded cell fails all-Z injectivity. Neither this argument nor the Galashin--Lam input says it fails at every positive external matrix.

The mathematical lemma applies to real input even though the executable routine targets rational input. A possibly irrational Galashin--Lam witness is therefore sufficient; no unproved rational-witness assumption is required. The paper's explicit nonadmissibility assertion is the input. Algebraic degree two by itself is not used.

## General rank-two BCFW recipes

**SOURCE-VERIFIED / REVIEWED.** The product matrix matches the actual Figure 10 and equation (19) in the local `literature/m4_BCFW_tilings_v3_2026.pdf`, PDF pp. 27 and 29. Figure 10 was rendered and visually inspected during this review, in addition to reading its formulas and equation (19).

For `(k_L,k_R)=(1,0)`, Figure 10 has upper row `A`, modified entry

\[
A'_a=A_a+(\alpha/\beta)A_b,
\]

and final entry `(-1)^(k_R+1) A_n=-A_n`. The lower bridge row has entries `alpha,beta,gamma,delta,epsilon` at `a,b,c,d,n`. The implementation's left branch makes exactly these changes and returns rows in the same order.

For `(k_L,k_R)=(0,1)`, the upper bridge has `alpha,beta,-gamma,-delta,-epsilon`, while the lower row has

\[
B'_d=B_d+(\delta/\varepsilon)B_n,
\qquad
B'_c=B_c+(\gamma/\delta)B'_d.
\]

The implementation updates `d` before `c`, so `B'_c` includes the required `gamma/epsilon` multiple of `B_n`; it then negates exactly the three bridge entries at `c,d,n`. A reverse update order would be incorrect, but that error is absent.

The enumerated index domains agree with Notation 6.1: `N_L={1,...,a,b,n}`, `N_R={b,...,c,d,n}`, with `b=a+1`, `c=n-2`, `d=n-1`. Each rank-one factor has exactly five positive support entries as in Example 7.5. The coindependence hypotheses of Proposition 6.8 hold directly: a five-element support cannot be contained in either the three-element forbidden set on the left or the four-element forbidden set on the right. The rank-zero factor satisfies them by convention.

**SOURCE-VERIFIED / REVIEWED.** Identification from one positive source parameter point is legitimate here because Proposition 6.8 identifies the image of the entire positive product domain with one positroid cell. The chosen all-one rational point therefore identifies that fixed source cell. This is not a sampled external-Z injectivity inference. The all-Z tile certificate comes separately from the BCFW injectivity theorem.

**PROVED / REVIEWED (recipe scope).** The rank-two generation reduction is exhaustive for the general BCFW class of Definition 7.1. Its last rank-increasing product has one rank-one and one rank-zero factor; the rank-one choices are all five-element supports by Example 7.5. Operations following that last product are zero insertions and dihedral actions. Their composite is represented by a cyclic-order-preserving or cyclic-order-reversing embedding, hence by an increasing embedding followed by an ambient dihedral action, as enumerated. Earlier operations on the rank-one factor are already covered by its arbitrary five-element support. Duplicate recipes are correctly identified through the complete basis set and affine label.

No critical mathematical or sign issue was found in the audited certificates. These checks validate the stated finite admissibility partition; they do not certify any additional image relation, relation-generation theorem, or complete-tiling classification.
