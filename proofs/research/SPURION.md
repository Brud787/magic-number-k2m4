# Spurion regression and source-data audit

Status date: 2026-09-05. This file distinguishes the published geometric result from exact local checks of its printed combinatorics.

## Sources read

Even-Zohar–Lakrec–Parisi–Sherman-Bennett–Tessler–Williams, *A cluster of results on amplituhedron tiles*, local `literature/m4_spurion_tiles.pdf`, especially Definitions 2.5–2.17, Theorem 4.1, Sections 5–7, and Appendix A (local PDF pp. 4–6, 16–18, 29–42). [arXiv:2402.15568](https://arxiv.org/abs/2402.15568), [published article](https://doi.org/10.1007/s11005-024-01854-4). The journal HTML and author-hosted PDF agree on the crucial printed replacement indices. The parent agent also visually inspected the original local PDF pp. 31 and 42: `results/spurion_pdf_page_31.png`, `results/spurion_pdf_page_42.png`.

The companion paper references theorem numbers in an older version of *Cluster algebras and tilings for the m=4 amplituhedron*. Our local copy of that main paper has changed numbering. Cite the companion's self-contained definitions/results by its own numbering, rather than silently transplanting its cross-reference numbers to the newer PDF. The main paper's local Definition 3.5, equation (2), gives the chain-polynomial convention below; its Definitions 3.12–3.14 give tiles, tilings, and facets.

## The non-BCFW tile

**SOURCE-VERIFIED.** Section 5.1 identifies the source cell with three nonloop parallel classes `(123)(456)(789)`, and asserts injectivity of the amplituhedron map using a parametrization by functionaries. Section 5.2 reports an all-positive-Z tiling containing one of its cyclic shifts. The geometric proof is explicitly presented as a sketch in Section 5.3.1, not as a numerical experiment.

**PROVED (elementary obstruction to being a BCFW cell, using the published BCFW row-support property).** Every nonzero linear functional on a two-dimensional vector space vanishes on at most one of three distinct projective directions. Consequently every nonzero row in every representative of this cell has at least six nonzero entries. The BCFW construction admits a representative with a row supported on five entries (Section 5.1 cites the main paper's Section 6). Thus the spurion is not a BCFW cell.

The Appendix A spurion is the cyclic variant

\[
(345)(678)(912),\qquad f=(2,6,4,5,9,7,8,12,10),
\]

which is row 28. Do not confuse this variant with the unshifted `(123)(456)(789)` used for the facet formulas.

## Literal published 5-for-5 data

The complete literal table, all 50 rows and both encodings, is in [`fixtures/spurion_a9_2_4.json`](fixtures/spurion_a9_2_4.json). It retains source errors if present and is not silently repaired.

Appendix A says to remove the following five rows from the spurion collection to obtain a BCFW collection:

| Row | Affine permutation | Parallel classes |
|---|---|---|
| 28 | `(2,6,4,5,9,7,8,12,10)` | `(345)(678)(912)` |
| 34 | `(3,6,4,5,9,8,7,11,10)` | `(91)(2)(345)(68)` |
| 35 | `(3,6,4,5,10,7,8,11,9)` | `(1)(2)(345)(678)` |
| 38 | `(3,6,5,4,8,7,11,9,10)` | `(891)(2)(35)(67)` |
| 46 | `(6,3,4,9,5,7,8,10,11)` | `(1)(234)(678)(9)` |

It says to insert these five BCFW cells:

| Position | Affine permutation | Parallel classes |
|---|---|---|
| B1 | `(1,6,4,5,9,7,8,11,12)` | `(2)(345)(678)(9)` |
| B2 | `(3,6,4,5,9,7,11,8,10)` | `(91)(2)(345)(67)` |
| B3 | `(3,6,4,9,5,7,8,11,10)` | `(91)(2)(34)(678)` |
| B4 | `(3,7,4,5,9,6,8,11,10)` | `(91)(2)(345)(78)` |
| B5 | `(4,6,3,5,9,7,8,11,10)` | `(91)(2)(45)(678)` |

**COMPUTATIONALLY-VERIFIED.** All 55 printed affine permutations agree with their parallel-class encodings. All have dimension 8. The literal set replacement changes five distinct labels into five distinct new labels: both collections contain 50 labels, with 45 labels in common. Two implementations check classes, bases, Grassmann necklaces, and affine permutations; the independent rank-two implementation additionally checks dimension and sample-Z differential rank. These statements do not certify that either collection geometrically tiles an amplituhedron.

## Reproduction failure in the printed common-parent argument

**FAILED (literal reconstruction of the published common-parent flip).** Section 5.3.1 prints the parent affine permutation

\[
\nu=(2,6,4,5,8,7,9,12,10).
\]

Its source cell has classes `(912)(345)(67)(8)` and dimension 9. The displayed ambient `Gr_{2,6}` there must itself be a typo: a length-nine affine permutation labels a cell of `Gr_{2,9}`. More substantially, none of B1–B5 lies in this parent's closure, and only row 28 of the five listed removed cells does. This is a vanishing-minor obstruction, independent of amplituhedron geometry. For example, the parent has `Delta_29=0` but B1 has `Delta_29>0`; it has `Delta_12=0` but B2–B5 have `Delta_12>0`.

There is a natural *different* dimension-nine parent

\[
P=(91)(2)(345)(678),\qquad f_P=(3,6,4,5,9,7,8,11,10).
\]

Its source facets include all five B1–B5. Its other facets that occur in the 50-row Appendix table are exactly **28, 34, 35, 39, 45**, rather than the printed **28, 34, 35, 38, 46**. The discrepancy is not PDF text-extraction noise: it appears in both encodings and the rendered source.

Two particularly short certificates are:

- On `P`, `Delta_68=0`; on row 38, `Delta_68>0`. Thus row 38 cannot lie in the closure of `P`.
- On `P`, `Delta_19=0`; on row 46, `Delta_19>0`. Thus row 46 cannot lie in the closure of `P`.

`P` has 12 source facets. Eight arise by deleting one column from a nonsingleton class; four arise by merging adjacent classes. Ten have sample-Z map differential rank 8; the other two have ranks 6 and 7 in the exact sample and merge into class sizes `(1,2,6)` and `(1,3,5)`, respectively. The latter two are not being called tiles. The rank-two agent independently reproduced the same 12-facet list and ten/full-rank split.

**CONJECTURAL (possible source repair only).** Replacing parent `nu` by `f_P` and changing removed rows 38,46 to 39,45 restores the ten-facet combinatorics. It does **not** yet establish a geometric 5-for-5 equality. No such correction has been applied to the literal fixture, and no claim that the published 50-row spurion tiling is false follows merely from this mismatch. The full published geometric flip has therefore not been independently reproduced in this run.

## Facet/functionary regression

For four-bracket twistors write

\[
\langle abc\mid de\mid fgh\rangle_Y
=\langle abcd\rangle_Y\langle efgh\rangle_Y
-\langle abce\rangle_Y\langle dfgh\rangle_Y.
\]

Section 5.3 supplies the following nine facet functionaries for the unshifted spurion:

\[
\begin{aligned}
(a_1,a_2,a_3)&=(\langle123|65|789\rangle_Y,
\langle123|64|789\rangle_Y,\langle123|54|789\rangle_Y),\\
(a_4,a_5,a_6)&=(\langle789|23|456\rangle_Y,
\langle789|13|456\rangle_Y,\langle789|12|456\rangle_Y),\\
(a_7,a_8,a_9)&=(\langle456|89|123\rangle_Y,
\langle456|79|123\rangle_Y,\langle456|78|123\rangle_Y).
\end{aligned}
\]

**SOURCE-VERIFIED.** The signs on the open tile are `(-,+,-,-,+,-,-,+,-)`. The nine hypersurfaces are its facets; their cluster variables are compatible. Their prescribed signs determine the open tile. Remark 5.1 says the tile has no facet on the physical boundary of the amplituhedron. Thus cluster adjacency survives the non-BCFW regression and is not itself a BCFW classification criterion.

The source Figure 18 has additional label errors: the local PDF repeats the name `a7` for the expression that must be `a9`, and repeats `s1`. The journal HTML gives a malformed `a9=<567|78|123>`. The displayed nine above follow the unambiguous threefold cyclic rule in the body and are the formulas used by the code. These caption errors are kept distinct from the more substantial flip-label discrepancy.

**COMPUTATIONALLY-VERIFIED (one exact Z).** Set `Z_i=(1,i,i^2,i^3,i^4,i^5)` for `i=1,...,9`; all maximal minors are positive Vandermonde products. Use

\[
C=\begin{pmatrix}1&b&c&d&e&f&0&0&0\\0&0&0&d&e&f&g&h&i\end{pmatrix},
\qquad(b,c,d,e,f,g,h,i)=(2,3,4,5,6,7,8,9).
\]

Exact evaluation gives

\[
(a_1,\ldots,a_9)=29255954595840000\,(-4,5,-6,-1,2,-3,-7,8,-9).
\]

This verifies the published signs at a rational fixture. It is not a proof of the all-Z sign characterization or injectivity. The underlying source chart covers the open three-parallel-class cell: a projective change of basis sends its three cyclically ordered directions to those displayed, and positive rescalings fix the first column.

## Canonical forms: what is actually available

**SOURCE-VERIFIED.** Definition 7.10 defines the *candidate* form by transporting the positroid cell's canonical form through the inverse amplituhedron map. Proposition 7.14 gives, for BCFW recipes,

\[
\widetilde\Omega(Z_S)=\bigwedge_{r=1}^{k}
 d\log\frac{\beta_r}{\alpha_r}\wedge
 d\log\frac{\gamma_r}{\alpha_r}\wedge
 d\log\frac{\delta_r}{\alpha_r}\wedge
 d\log\frac{\varepsilon_r}{\alpha_r}.
\]

For standard BCFW tiles, Proposition 7.16 gives a wedge of `4k` dlogs in any tile cluster. Theorem 6.7 provides the birational identification of an open standard BCFW tile with the positive part of its cluster variety. None of those standard-BCFW results automatically includes arbitrary tiles.

The paper does **not** print a dedicated closed formula for the spurion's canonical 8-form. Its nine functionaries, sign characterization, and Definition 7.10 provide a route to one. At the exact sample above, signed ratios to `a4` recover the eight positive parameters, suggesting the dlog coordinates

`(-a5/a4, a6/a4, a1/a4, -a2/a4, a3/a4, a7/a4, -a8/a4, a9/a4)`.

**CONJECTURAL (candidate reconstruction, not an invariant).** Before identifying the wedge of those eight dlogs with the spurion candidate form for arbitrary Z, prove the rational inverse identities and the source-form normalization. An arbitrary positive diffeomorphism alone is insufficient to identify the canonical form with a dlog wedge.

Conjectures 7.9, 7.11, and 7.12 explicitly leave positive geometry of the amplituhedron, positive geometry of arbitrary tiles with these candidate forms, and tiling additivity unproved in this source. The text even labels the general positive-geometry additivity statement “Heuristic 7.5.” These facts are blockers for an unconditional unit-weight argument.

A common normalization of a dlog form in *different tile-dependent coordinates* is not a common linear functional on ambient rational forms. Every positive-dimensional cell can have a normalized chart without any resulting conservation of the number of pieces. This is the central obstruction exposed by the spurion comparison.

## Reproduction commands

```sh
PYTHONPATH=src .venv/bin/python -m magic_number.spurion
PYTHONPATH=src .venv/bin/python -m pytest tests/test_spurion.py -q
```

The first regenerates the exact combinatorial audit printed in [`fixtures/spurion_combinatorial_audit.json`](fixtures/spurion_combinatorial_audit.json). The tests preserve the literal fixture and explicitly require the source-parent discrepancy to remain detected.

---

## Run 2: separate repaired relation now certified

The first-run audit above is preserved verbatim. **FAILED:** the printed
common-parent incidence still fails for the exact zero-minor reasons
already recorded. It is not silently corrected.

**PROVED.** The different parent `(91)(2)(345)(678)` independently supports
the local all-Z relation

\[
[T_{28}]+[T_{34}]+[T_{35}]+[T_{39}]+[T_{45}]
=[B_1]+[B_2]+[B_3]+[B_4]+[B_5].
\]

Its coefficient sum is zero. Every term is an admissible tile, each side
has disjoint open tile images, and the two finite closed unions equal the
closure of the parent image. This is a geometric relation modulo lower
dimension, certified at Level A. The proof uses exact linear positive
fibers and oriented interval endpoints; it does not rely on the disputed
printed parent or canonical-form additivity.

The complete [proof](run2/SPURION_ATTEMPT.md) and
[independent review](run2/SPURION_REVIEW.md) retain the published individual
spurion injectivity input explicitly. An independent ambient-system test
reproduces all ten exact endpoint derivatives. The other two source facets
have class-complement image-dimension obstructions, now proved for every Z
rather than inferred from their first-run sample ranks.

Three separately named machine fixtures are retained:

- [PRINTED](../fixtures/run2/spurion_printed.json): literal parent and rows.
- [REPAIRED-CANDIDATE](../fixtures/run2/spurion_repaired_candidate.json): historical pre-review coordinates and exact evaluations.
- [CERTIFIED](../fixtures/run2/spurion_certified.json): separate reviewed all-Z relation and proof provenance.

**CONJECTURAL:** the repaired data describe the authors' intended correction.
Embedding this repaired flip in the literal fifty-row collection is still
uncertified. No new complete tiling or correction to the publication was
sent externally. The18 dihedral copies in the relation catalog all derive
from this one prototype; they are not18 independent non-BCFW mechanisms.
