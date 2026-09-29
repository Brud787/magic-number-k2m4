# Certificate index

Release `1.0.0-paper` identifies the [public repository](https://github.com/Brud787/magic-number-k2m4) and reserved Zenodo DOI [10.5281/zenodo.23028034](https://doi.org/10.5281/zenodo.23028034). DOI reservation does not establish publication of the deposit.

Every command below runs from the public repository root or the extracted `publication/` directory after installing [requirements.txt](requirements.txt). Each certificate ID below is accepted by:

```sh
python verify_all.py --certificate ID
```

Use `python verify_all.py --list` for the executable registry and `python verify_all.py` for the complete replay. A successful selected run finishes with `[PASS] certificate ID` and exits zero; it is not the full-release verdict. “Expected exact output” below gives the mathematical values that must be checked, not merely a string to search in a historical log.

Paper locations use section names and stable TeX labels in [paper/main.tex](paper/main.tex). The certificate appendix repeats these IDs. Links are relative to this directory and work in an extracted archive or public repository.

## Data and ID conventions

| Object | IDs / encoding |
|---|---|
| All labeled loopless eight-dimensional sources | `M001`–`M221`; includes admissible and excluded cells |
| Dihedral nine-dimensional parent representatives | `P001`–`P029` |
| Parent facets | `Pnnn-Fnn`, in the parent's literal `facets` order |
| Ten-wall overlap witnesses | `Pnnn-W01`–`Pnnn-W09` for P006, P012, P015, P023, P024 |
| Hostile indicator witnesses | `P005-H01`–`P005-H08`, `P016-H01`–`P016-H08` |
| n = 9 tile columns | `N9-T0001`–`N9-T0942` |
| n = 9 local relation rows | `N9-R0001`–`N9-R0693` |
| n = 9 indicator witnesses/rows | `N9-W0001`–`N9-W0472` |
| Normalized columns / rows | `Nn-Txxx` / `Nn-Rxxx`, exactly as listed in each `normalized/Nn.json` |

Labels in cyclic classes and affine permutations are one-based. JSON array positions, `row`, `column`, `minor_columns`, `pivot_columns`, and selected-row arrays are zero-based. Always apply selected rows and columns in their stored order: sorting them anew can change a determinant's sign. `N9-T0001` and `N9-T001` are different namespaces: the latter is a normalized n = 9 column, not the first full-universe column.

Matrices are row-major integer arrays unless specified otherwise. Exact noninteger entries are strings such as `"-7/3"`, parsed as rational numbers. Sparse RREF rows are lists of `[column_index, exact_coefficient]` pairs. A parent's `relation_vector` is aligned with all its facets, with zero entries on excluded facets; `positive_facets` and `negative_facets` expose its two literal sides. `historical_id` and `historical_relation_id` retain provenance.

The replay code is [verifier/checks.py](verifier/checks.py), with [exact rational linear algebra](verifier/exact.py), [source reconstruction](independent/combinatorics.py), and [membership replay](independent/membership.py). “Independent replay: yes” below means separate from the historical critical producer in the precise sense explained in [independent/README.md](independent/README.md). It never means that this packaging pass obtained independent human peer review.

## MEM-CORES

- **Claim / paper location:** Complete finite list, eleven admissible dihedral types, and loopless counts in the membership section (`thm:membership`, `tab:membershipcores`, `eq:Uncount`).
- **Literal files:** [membership/catalogue.json](certificates/membership/catalogue.json), [historical_cores.json](certificates/membership/historical_cores.json).
- **Verifier / command:** `checks.membership_catalogue`; `python verify_all.py --certificate MEM-CORES`.
- **Expected exact output:** 221 labeled source cells in 24 dihedral types; admissible counts **1, 14, 36, 30, 5** at q = 6,...,10, totaling 86 cells in eleven types. Every source record includes q, s, cyclic classes, sizes, representative, orbit/stabilizer data, status and mechanism.
- **Why this proves the finite claim:** Enumerating cyclic cuts with q + s = 12 exhausts source partitions. The verifier compares every label, classification mechanism and orbit with the archived inventory. Unique support insertion gives `|U_n| = binom(n,6) + 14 binom(n,7) + 36 binom(n,8) + 30 binom(n,9) + 5 binom(n,10)`. The all-Z interpretation uses the paper's complement-five proof, complement obstruction and cited spurion theorem; the enumeration alone does not prove them.
- **Independent replay available:** Yes, standalone combinatorics compared against the historical producer; the release normalizer shares helpers as disclosed.

## MEM-FOUR-MASS

- **Claim / paper location:** The (2,2,2,2) source is not all-Z injective (`thm:membership`, four-mass paragraph).
- **Literal files:** [four_mass.json](certificates/membership/four_mass.json), [four_mass_historical.json](certificates/membership/four_mass_historical.json).
- **Verifier / command:** `checks.four_mass`; `python verify_all.py --certificate MEM-FOUR-MASS`.
- **Expected exact output:** Positive ordered six-minors of Z; nonnegative source two-minors with exactly the stated source bases; distinct source row spaces; invertible rational G and **C1 Z = G (C2 Z)**.
- **Why this proves the claim:** Two distinct positive source points at one positive Z disprove injectivity for every positive Z. Equality of source row spaces is excluded by stacked source rank greater than two. The public G is the inverse of the row operation in the historical certificate, so the displayed identity has the stated direction.
- **Independent replay available:** Yes, direct rational matrix and source-pattern checks from literal coordinates. No generic complex degree or floating-point rank is substituted.

## MEM-SPURION

- **Claim / paper location:** Exact spurion inverse used by witness decisions (membership section and certificate appendix).
- **Literal files:** [spurion_inverse.json](certificates/membership/spurion_inverse.json); [mathematical inverse specification](proofs/research/run6/SPURION_INVERSION.md).
- **Verifier / command:** `checks.spurion_fixture` and `independent.membership.spurion`; `python verify_all.py --certificate MEM-SPURION`.
- **Expected exact output:** The saved positive, mixed-sign and boundary cases reproduce their declared open-inverse decisions; cases declaring a strict inverse satisfy its result and genericity gates. Full witness use is additionally replayed in `N9-INDICATORS` and `LOCAL-TEN-WALL`.
- **Why this proves the finite claim:** The complete three-direction chart gives linear image equations. A one-dimensional 12 × 13 ambient kernel yields nine source coefficients; one strict common sign gives an open preimage, while mixed strict signs plus the three rank-five block gates exclude the closed image. Zero or rank-exceptional cases are not accepted as strict nonmembership. The symbolic completeness proof and published all-Z injectivity remain explicit inputs.
- **Independent replay available:** Yes relative to the historical 8 × 9 quotient inverse, using the adapted secondary ambient system; not a newly independent mathematical proof of spurion injectivity.

## LOCAL-PARENTS

- **Claim / paper location:** Exhaustion and partition of the 29 nine-dimensional parent cores (`thm:local`).
- **Literal files:** [parents.json](certificates/local/parents.json), [PARENTS.md](certificates/local/PARENTS.md), [parents_historical.json](certificates/local/parents_historical.json).
- **Verifier / command:** `checks.parents`; `python verify_all.py --certificate LOCAL-PARENTS`.
- **Expected exact output:** **29** dihedral types (364 labeled loopless parents), sector counts **12 + 10 + 5 + 2**, with respectively 0, 6, 10, 8 admissible facets.
- **Why this proves the finite claim:** Exhaust all cyclic partitions q + s = 13, reconstruct source facets by the specified deletion/merger operations, and classify every facet using the complete membership criterion. The sector's geometric relation-space dimension is justified with the associated relation, overlap and hostile certificates below.
- **Independent replay available:** Yes for enumeration and facets, with the membership theorem as shared mathematical input.

## LOCAL-RELATIONS

- **Claim / paper location:** Literal primitive vectors for all ten 3↔3 and five 5↔5 parents; every local generator is balanced (`thm:local`, `eq:augmentationzero`).
- **Literal files:** [parents.json](certificates/local/parents.json), [PARENTS.md](certificates/local/PARENTS.md), [relations_historical.json](certificates/local/relations_historical.json).
- **Verifier / command:** `checks.parents`; `python verify_all.py --certificate LOCAL-RELATIONS`.
- **Expected exact output:** 15 nonzero primitive integer vectors; ten with three +1 and three −1, five with five +1 and five −1; every vector has **sum 0**. Literal facet IDs are listed on each side in PARENTS.md.
- **Why this proves the finite claim:** Facet labels and coefficients agree exactly with the saved source prototypes, and nonzero coefficients occur precisely on the admissible facets. The fact that these vectors are all-Z geometric relations is the symbolic input in [SIGN_MECHANISMS.md](proofs/research/run4/SIGN_MECHANISMS.md) and [LOCAL_PARENT_THEOREM.md](proofs/research/run4/LOCAL_PARENT_THEOREM.md). Counting signs alone does not establish an image relation.
- **Independent replay available:** Yes for labels, balance and historical comparison; no new independent rederivation of the symbolic geometric sign mechanisms.

## LOCAL-TEN-WALL

- **Claim / paper location:** One-dimensional coefficient-relation kernels for each of the five ten-wall parents (`thm:local`, local-certificate appendix).
- **Literal files:** [overlap_witnesses.json](certificates/local/overlap_witnesses.json) and [overlaps_historical.json](certificates/local/overlaps_historical.json); parent IDs P006, P012, P015, P023, P024. `prototype_to_parent_labels` identifies the historical coordinate representative with the canonical parent, `wall_facet_ids` labels all ten matrix columns, and `equation_facet_ids` gives the two facet IDs in each witness equation.
- **Verifier / command:** `checks.overlaps`; `python verify_all.py --certificate LOCAL-TEN-WALL`.
- **Expected exact output:** **45** exact overlaps, nine for each parent. Every 9 × 10 edge-constraint matrix has **rank 9**, with a selected 9 × 9 minor of absolute determinant **1**, and annihilates its five-plus/five-minus vector.
- **Why this proves the claim:** Each witness stores Z, Y, two exact open-wall source preimages, positive coordinates, invertible image row changes and endpoint wall indices. Exact inverses also check all ten indicators. Each row gives `c_i + c_j = 0`. The rank-nine necessary equations leave at most a one-dimensional relation space; the separately proved nonzero geometric relation realizes that dimension. The bound is obtained at the displayed fixed Z and therefore applies to all-Z relations.
- **Independent replay available:** Yes, exact ambient membership replay and `Fraction` determinants; the nonzero all-Z relation is a retained symbolic input.

## LOCAL-HOSTILE-8

- **Claim / paper location:** The q = 8 hostile parent (P005) has zero all-Z relation space on its eight admissible facets (`thm:local`).
- **Literal files:** [hostile_q8.json](certificates/local/hostile_q8.json), including `ordered_admissible_facets`, eight `target_records`, and `indicator_matrix`; [hostile_index.json](certificates/local/hostile_index.json) maps its columns to canonical facet IDs and its rows to P005-H01,...,P005-H08.
- **Verifier / command:** `checks.hostile(8)`; `python verify_all.py --certificate LOCAL-HOSTILE-8`.
- **Expected exact output:** All **64** membership entries match, all declared strict/generic conditions hold, and the literal **8 × 8 determinant is 1**.
- **Why this proves the claim:** Evaluation on eight certified open neighborhoods forces an all-Z coefficient relation into the kernel of an invertible matrix, hence it is zero. The fixture uses a dihedrally equivalent historical representative of P005; `prototype_to_parent_labels` gives the exact identification, and `column_facet_ids` preserves the actual determinant order.
- **Independent replay available:** Yes, exact inverse reconstruction and rational determinant. The symbolic closure/genericity proposition is shared.

## LOCAL-HOSTILE-9

- **Claim / paper location:** The q = 9 hostile parent (P016) has zero all-Z relation space on its eight admissible facets (`thm:local`).
- **Literal files:** [hostile_q9.json](certificates/local/hostile_q9.json), with the same field conventions as q = 8; [hostile_index.json](certificates/local/hostile_index.json), giving canonical facets and witness IDs P016-H01,...,P016-H08.
- **Verifier / command:** `checks.hostile(9)`; `python verify_all.py --certificate LOCAL-HOSTILE-9`.
- **Expected exact output:** All **64** membership entries match and the exact **8 × 8 determinant is 1**, with strict/generic conditions verified.
- **Why this proves the claim:** The same invertible-open-evaluation argument applies. Match its historical representative to P016 by cyclic class profile, and retain the fixture's actual facet order for its determinant.
- **Independent replay available:** Yes under the same scope as `LOCAL-HOSTILE-8`.

## N9-UNIVERSE

- **Claim / paper location:** The complete n = 9 tile universe has 942 columns (uniform global generation section, `eq:basecase`, n = 9 appendix).
- **Literal files:** [tiles.json](certificates/n9/tiles.json), [local_historical.json](certificates/n9/local_historical.json), [membership catalogue](certificates/membership/catalogue.json).
- **Verifier / command:** `checks.local_n9`, using `independent.combinatorics.tiles`; `python verify_all.py --certificate N9-UNIVERSE`.
- **Expected exact output:** **942** unique canonically ordered columns, `N9-T0001`–`N9-T0942`, with the historical affine labels in exactly the same order.
- **Why this proves the claim:** Enumerate every increasing support and every admissible loopless core, then compare the full labels. The binomial count is 84 + 14·36 + 36·9 + 30 = 942.
- **Independent replay available:** Yes, standalone source reconstruction compared with historical labels.

## N9-LOCAL-RANK

- **Claim / paper location:** R9 has 693 transported local rows and rank 470 (global section and n = 9 appendix).
- **Literal files:** [R9.json](certificates/n9/R9.json), [local_historical.json](certificates/n9/local_historical.json), [relation prototypes](certificates/local/relations_historical.json).
- **Verifier / command:** `checks.local_n9` and `verifier.exact.rank_certificate`; `python verify_all.py --certificate N9-LOCAL-RANK`.
- **Expected exact output:** Reconstructed **693 × 942** matrix equals both saved matrices; selected **470 × 470 determinant −1**; every row is in the published 470-dimensional rational row span; hence **rank 470**.
- **Why this proves the claim:** Dihedral and support transports exhaust the declared local generators. `independent_rows` and `pivot_columns` select the lower-bound minor. `rref` supplies a pivot-normalized rational basis; each input row is exactly reconstructed from its pivot coordinates. This proves the upper bound, separately from the nonzero minor.
- **Independent replay available:** Yes for the transports and rational linear algebra. The 15 literal primitive relations and their symbolic meaning are shared inputs.

## N9-INDICATORS

- **Claim / paper location:** All 472 exact open-neighborhood rows and all 444,624 membership decisions (global section and n = 9 appendix).
- **Literal files:** [witnesses.json](certificates/n9/witnesses.json), [tiles.json](certificates/n9/tiles.json), [A9.json](certificates/n9/A9.json), [indicator_historical.json](certificates/n9/indicator_historical.json).
- **Verifier / command:** `checks.indicator_n9` and `independent.membership.replay_n9`; `python verify_all.py --certificate N9-INDICATORS`.
- **Expected exact output:** **472** witnesses × **942** columns = **444,624** exact decisions. Every reconstructed entry equals both the historical promoted matrix and public A9; the row-major 0/1-byte hash is printed. All 472 source-image equations and **59,472 = 472·126** nonzero four-label twistors are checked.
- **Why this proves the finite claim:** The files give exact Z, each Y and source matrix, source label, generic residual data, and expected row. Reconstruction uses these geometric inputs, not the stored row, to make every decision. Strict inverse signs and nonzero rank/genericity conditions persist on an open neighborhood. This supplies legitimate evaluations of relations modulo lower-dimensional sets under the stated inverse/closure propositions.
- **Independent replay available:** Yes relative to the historical producer, by the adapted secondary ambient solver. This is not a third independent inverse implementation; see the independence statement.

## N9-INDICATOR-RANK

- **Claim / paper location:** Rank A9 = 472 with selected determinant 4 (global section and n = 9 appendix).
- **Literal files:** [A9.json](certificates/n9/A9.json), fields `row_ids`, `column_ids`, `rows`, `minor_columns`; the witnesses above reconstruct `rows`.
- **Verifier / command:** `checks.indicator_n9` and `verifier.exact.determinant`; `python verify_all.py --certificate N9-INDICATOR-RANK`.
- **Expected exact output:** After exact row reconstruction, **det A9[:, minor_columns] = 4** on all rows `N9-W0001`–`N9-W0472` in their stored order.
- **Why this proves the claim:** `minor_columns` lists 472 distinct zero-based column positions; look up their stable IDs in `column_ids`. The nonzero determinant proves rank ≥ 472; there are only 472 rows, proving the matching upper bound.
- **Independent replay available:** Yes, row reconstruction plus `Fraction` determinant arithmetic.

## N9-ANNIHILATION

- **Claim / paper location:** A9 R9ᵀ = 0 (global section and n = 9 appendix).
- **Literal files:** [A9.json](certificates/n9/A9.json), [R9.json](certificates/n9/R9.json), and their reconstruction inputs above.
- **Verifier / command:** `checks.indicator_n9`; `python verify_all.py --certificate N9-ANNIHILATION`.
- **Expected exact output:** Every one of the **472·693 = 327,096** integer scalar products is **0**.
- **Why this proves the finite claim:** Exact multiplication checks every pair of a reconstructed witness row and transported relation row. It is a complete finite consistency check, with no sampled entries. The all-Z inclusion L9 ⊆ K9 still comes from the local theorem, not solely from this product.
- **Independent replay available:** Yes, reconstructed operands and direct integer products.

## N9-KERNEL

- **Claim / paper location:** K9 = L9 (`eq:basecase`).
- **Literal files:** All `N9-*` files above, with the membership and local certificate families.
- **Verifier / command:** The n = 9 certificate chain in [verify_all.py](verify_all.py); `python verify_all.py --certificate N9-KERNEL`.
- **Expected exact output:** **dim L9 = 470; dim ker A9 = 942 − 472 = 470; L9 ⊆ K9 ⊆ ker A9; therefore K9 = L9**, after the prerequisites pass.
- **Why this proves the claim:** The local geometric theorem gives the first inclusion. Open-neighborhood evaluations at one positive Z give the second for all-Z relations. The exact equal dimensions force equality. No assertion that arbitrary finite sampling determines K9 is required.
- **Independent replay available:** Yes for the complete finite arithmetic and reconstruction; the inclusion arguments are symbolic premises identified in [PROOF_DEPENDENCIES.md](PROOF_DEPENDENCIES.md).

## Normalized certificates

These are the six rows of `prop:normalizedranks` and the normalized-certificate appendix. Each file contains canonical `column_ids`, `row_ids`, source/parent labels, literal `rows`, selected row/column indices, exact sparse RREF rows, and the determinant. `columns` and `projected_parent_rows` connect these arrays to source cells. The normalized columns are exactly tiles with no loop in positions 2,...,n; a single loop in position 1 is permitted.

| ID / exact command | Literal file | Columns | Parent rows | Exact rank | dim N(Q) | Selected determinant |
|---|---|---:|---:|---:|---:|---:|
| `python verify_all.py --certificate NORM-6` | [N6.json](certificates/normalized/N6.json) | 1 | 0 | 0 | 1 | 1 (empty) |
| `python verify_all.py --certificate NORM-7` | [N7.json](certificates/normalized/N7.json) | 15 | 7 | 6 | 9 | −1 |
| `python verify_all.py --certificate NORM-8` | [N8.json](certificates/normalized/N8.json) | 50 | 47 | 31 | 19 | 1 |
| `python verify_all.py --certificate NORM-9` | [N9.json](certificates/normalized/N9.json) | 66 | 121 | 54 | 12 | −1 |
| `python verify_all.py --certificate NORM-10` | [N10.json](certificates/normalized/N10.json) | 35 | 141 | 35 | 0 | −1 |
| `python verify_all.py --certificate NORM-11` | [N11.json](certificates/normalized/N11.json) | 5 | 46 | 5 | 0 | 1 |

- **Verifier:** `checks.normalized`, `independent.combinatorics.transported_rows(..., normalized=True)`, and `verifier.exact.rank_certificate`. The original table and matrices remain in [historical.json](certificates/normalized/historical.json).
- **Expected exact output:** Each selected ID's entire row of the table above, after reconstruction of all row and column labels and matrix entries. The n = 10 and n = 11 minors have sizes 35 × 35 and 5 × 5 respectively.
- **Why this proves the finite claim:** Reconstruct the projected parent rows from the classified prototypes, keeping distinct parent rows in the stored order. `independent_row_indices` and `pivot_columns` select a rank-sized minor. `rref_rows` supplies a verified rational span containing every matrix row, proving the upper bound, including n = 7,8,9 where the matrix is not full column rank. In the n = 6 case the row space is zero and det(empty 0 × 0 matrix) = 1 by convention; there is no rank-one assertion. Quotient dimensions are column count minus row rank.
- **Independent replay available:** Yes relative to the historical normalized matrix producer, using standalone source/transport reconstruction and rational certificate checks. The degeneracy quotient's identification is the paper's symbolic argument.

## SUPPORT-CUTOFF

- **Claim / paper location:** At most ten nonloop labels; no normalized generators at n ≥ 12 (`cor:supportbound`, `prop:normalizedranks`, `eq:NQvanish`).
- **Literal files:** [membership catalogue](certificates/membership/catalogue.json), [normalized files](certificates/normalized/), and the support argument in [MEMBERSHIP_CORES.md](proofs/research/run6/MEMBERSHIP_CORES.md).
- **Verifier / command:** Membership and normalized construction checks in `checks`; `python verify_all.py --certificate SUPPORT-CUTOFF`.
- **Expected exact output:** The q + s = 12 classification has q ≤ 10, and the normalized n = 12 column set is empty.
- **Why this proves the claim:** The all-n implication is symbolic: among positions 2,...,n there are at least eleven positions at n ≥ 12, so support size at most ten forces a loop there. Such a generator is degenerate. The n = 12 replay corroborates the boundary case; it is not an extrapolation from empty matrices at finitely many n.
- **Independent replay available:** Yes for enumeration; the universal support implication is the displayed elementary argument.

## N8-UNIT

- **Claim / paper location:** The saved n = 8 indicator certificate admits a signed rational unit functional (Discussion).
- **Literal files:** [unit_n8.json](certificates/auxiliary/unit_n8.json), [indicator_n8.json](certificates/auxiliary/indicator_n8.json).
- **Verifier / command:** Auxiliary unit-vector check in `checks`; `python verify_all.py --certificate N8-UNIT`.
- **Expected exact output:** The saved **103** rational weights satisfy **A8ᵀ λ = 1** on every tile column and **sum λ = 20**; saved indicator decisions are replayed from exact target data.
- **Why this proves the finite claim:** Direct rational multiplication verifies the asserted unit functional on this finite evaluation matrix. Open witness evaluations and the retained membership proposition give its indicator interpretation. This ancillary certificate is not an additional premise of the all-n argument.
- **Independent replay available:** Yes for exact membership replay and vector arithmetic relative to the historical producers.

## N9-UNIT

- **Claim / paper location:** The saved n = 9 indicator certificate admits a signed rational unit functional (Discussion).
- **Literal files:** [unit_n9.json](certificates/auxiliary/unit_n9.json), [A9.json](certificates/n9/A9.json), [witnesses.json](certificates/n9/witnesses.json).
- **Verifier / command:** Auxiliary unit-vector check in `checks`; `python verify_all.py --certificate N9-UNIT`.
- **Expected exact output:** **472** rational weights satisfy **A9ᵀ λ = 1_942** and **sum λ = 50** against the reconstructed matrix.
- **Why this proves the finite claim:** Each of the 942 equalities is checked with exact rational arithmetic. It certifies this saved finite functional, without claiming an n-uniform formula or a canonical choice of weights.
- **Independent replay available:** Yes for the reconstructed operand and exact vector equalities.

## WEIGHT-PROBES

- **Claim / paper location:** The particular saved weights fail to depend only on the tested coarse source metadata (Discussion).
- **Literal files:** [weight_probes.json](certificates/auxiliary/weight_probes.json), the two saved unit vectors and their indicator-witness files above.
- **Verifier / command:** Auxiliary weight-metadata comparison in `checks`; `python verify_all.py --certificate WEIGHT-PROBES`.
- **Expected exact output:** Reproduce the declared metadata group counts and conflicting witness pairs, including same-core-profile/different-weight examples at n = 8 and n = 9.
- **Why this proves the finite claim:** A literal pair with equal tested metadata and unequal exact weights disproves that metadata fit for the saved weight vector. This is exploratory evidence about those particular weights; it does not rule out other unit functionals or a general weight formula.
- **Independent replay available:** Yes for source-profile/support reconstruction and exact weight arithmetic; other metadata fields are grouped as saved. No broader impossibility claim is certified.

## ARTIFACT-HASHES

- **Claim / paper location:** The manuscript and literal release artifacts match the frozen version (reproducibility appendix).
- **Literal file:** [SHA256SUMS.txt](SHA256SUMS.txt), plus every file listed in it.
- **Verifier / command:** `checks.hashes`; `python verify_all.py --certificate ARTIFACT-HASHES`.
- **Expected exact output:** Every listed file exists within the release root and its SHA-256 equals the recorded digest.
- **Why this proves the claim:** It detects byte changes relative to the manifest. It is an integrity check, not mathematical evidence for any matrix claim and not a digital signature authenticating an author. The manifest cannot hash itself; the final replay log is frozen before finalizing and rechecking the manifest, as explained in [REPRODUCIBILITY.md](REPRODUCIBILITY.md).
- **Independent replay available:** Yes with any SHA-256 implementation; no independent reconstruction is needed for a byte comparison.

## Symbolic and external claims

The main Magic Number theorem, adjacent amalgamation, preservation of K and L, the signed simplicial identities, truncation persistence, Dold–Kan, and the augmentation/BCFW comparison are not bare machine assertions. Their inputs and implications are mapped in [PROOF_DEPENDENCIES.md](PROOF_DEPENDENCIES.md). The main theorem depends on the finite families above together with these explicit mathematical and cited premises. No unit-test total is used as a theorem certificate.
