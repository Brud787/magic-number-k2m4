# Final certificate-access review

> Publication metadata update (2026-09-28): this document records the earlier
> certificate-access pass. Its references to repository/DOI placeholders and
> pending replay describe that earlier state. The public repository is now
> [Brud787/magic-number-k2m4](https://github.com/Brud787/magic-number-k2m4), and
> the reserved Zenodo DOI is
> [10.5281/zenodo.23028034](https://doi.org/10.5281/zenodo.23028034).
> Current build and metadata checks are recorded in
> [the final metadata record](audit/final_metadata_validation.json); the original certificate replay is preserved and was not rerun.

Reviewed on 2026-09-28 against the authoritative
`magic_number_k2_m4_preprint.tex`, the public certificate index, literal
release data, and replay implementation.

**Finding:** no new mathematical inconsistency or unresolved
claim-to-certificate access defect was found in this review. Final clean
replay and hash-freeze results were pending when this document was written;
this document does not assert they passed. The release verdict belongs in
[SUBMISSION_READINESS.md](SUBMISSION_READINESS.md), supported by the final
generated logs and manifest.

## Scope and method

This is a fresh review of the prepared supplement as a reader would use
it, following the user's narrowed request. It is not another broad
mathematical audit or a new proof of the theorem. The earlier symbolic
proofs and audits are retained as explicit inputs, rather than accepted as
evidence that the new packaging is automatically correct.

I compared the revised manuscript with
[the preserved original](audit/original_manuscript.tex), traced the paper's
computational IDs into [CERTIFICATE_INDEX.md](CERTIFICATE_INDEX.md) and
[verify_all.py](verify_all.py), inspected the literal arrays and their
metadata, and reviewed how the replay code distinguishes reconstruction,
arithmetic, symbolic premises, and external inputs. Full determinant and
membership computations were not redundantly rerun for this document;
the complete final replay is a separate required release operation.

## Findings

| Review question | Finding and evidence |
|---|---|
| Was the theorem silently broadened, weakened, or replaced? | **PASS.** All six `theorem` environments and both `definition` environments are byte-identical to the preserved original. The all-Z scope, tiling definition, and principal theorem statements were preserved. The added material exposes certificates and their hypotheses. |
| Can a reader follow every computational assertion? | **PASS.** The paper has 24 computational claim IDs. Every referenced ID has a TeX target, an index entry, and an accepted `--certificate ID` command. `ARTIFACT-HASHES` is an additional integrity command. The index maps paper labels to literal files, verifier entry points, expected values, and the precise implication. |
| Does membership exhaustion match the paper? | **PASS at the access/consistency level.** The public catalogue retains admitted and excluded cells, ordered classes, orbit data, and mechanisms. Its stored counts are 1, 14, 36, 30, 5. The code reconstructs the finite list. The index explicitly retains the symbolic complement-five argument, complement obstruction, and published spurion assertion as mathematical inputs. |
| Is four-mass exclusion independently inspectable? | **PASS.** Exact Z, C1, C2, and G are published. The check covers external positivity, both source zero patterns, distinct source row spaces, and the identity C1 Z = G(C2 Z). One positive-Z counterexample is correctly used to exclude all-Z injectivity. |
| Are the local classification and actual relation vectors exposed? | **PASS.** There are 29 public parent records, including canonical facets and literal vectors with positive and negative facet-ID lists. The index distinguishes checking balance from proving the vectors are geometric all-Z relations. The latter remains a symbolic premise. |
| Are local upper bounds connected to genuine witnesses? | **PASS.** The 45 ten-wall witness records are exposed with parent/facet transport maps; the five 9 × 10 constraint matrices are reconstructed from exact decisions. Both hostile fixtures give all eight target records, literal 8 × 8 matrices, determinant order, and canonical facet mappings. Their fixed-Z evaluations constrain all-Z relations in the correct direction. |
| Do the n = 9 literal dimensions agree with the manuscript? | **PASS.** The published R9 has 693 rows of width 942 and a 470-row rational upper-rank basis; its selected-minor field is −1. A9 has 472 rows of width 942, 472 selected minor columns, and determinant field 4. There are 472 witness records. These values match the paper and index. |
| Is a nonzero minor being mistaken for an exact non-full rank? | **PASS.** The replay separately checks an upper certificate: every original row is exactly reconstructed from the published pivot-normalized rational basis. The selected nonzero minor gives the lower bound. This applies to R9 and normalized n = 7, 8, 9. Full-row or full-column bounds supply the appropriate upper bounds elsewhere. |
| Is the indicator matrix merely trusted from a file? | **PASS by implementation inspection.** The replay computes each decision from exact Z, Y and source labels, then compares every entry with the saved row and public matrix. Stored PASS flags are not used as evidence. Generic/strict failures raise errors instead of silently returning nonmembership. The main development replay recorded all 444,624 decisions passing; the final release replay remains a separate gate. |
| Is K9 confused with a finite sampled kernel? | **PASS.** Paper and index state L9 ⊆ K9 ⊆ ker(A9), with the first inclusion supplied by the geometric local theorem and the second by exact open-neighborhood evaluations. The equal dimensions 470 and 942 − 472 force equality. The finite product A9 R9ᵀ = 0 is not substituted for the all-Z local theorem. |
| Do normalized certificates match the six paper rows? | **PASS at the access/consistency level.** Literal data give `(columns, parent rows, rank, quotient dimension)` equal to `(1,0,0,1)`, `(15,7,6,9)`, `(50,47,31,19)`, `(66,121,54,12)`, `(35,141,35,0)`, `(5,46,5,0)`. Selected determinants are 1, −1, 1, −1, −1, 1. The empty n = 6 determinant convention is explicit and does not assert positive rank. |
| Is finite computation overstated as an all-n argument? | **PASS.** The manuscript and dependency map retain the label/degree convention p = n − 1. Amalgamation, zero insertion, signed identities, truncation persistence, normalization, downward propagation, and augmentation are marked as symbolic or external premises. The support argument for all n ≥ 12 is stated separately from the finite n = 12 empty-column check. These proofs were not re-audited here. |
| Is “independent” accurately qualified? | **PASS.** The release reconstructor imports no historical production construction. The membership implementation is identified as an adaptation of the earlier secondary ambient verifier, not a third independently invented algorithm. The release normalizer shares standalone routines with replay. Mathematical conventions, local prototypes, witness inputs, SymPy, and Python exact arithmetic are disclosed shared dependencies. Independent human peer review is not claimed. |
| Are ancillary observations exposed without becoming new theorem premises? | **PASS.** N8-UNIT, N9-UNIT, and WEIGHT-PROBES have literal data and exact commands. Their interpretation is confined to the saved finite weight vectors; no universal impossibility result or additional premise of the all-n theorem is asserted. |
| Are external claims and prior disagreements hidden? | **PASS for release disclosure.** The citation record distinguishes KWZ's existence conjecture from the universal-cardinality formulation, identifies the BCFW and spurion inputs, and records that the earlier printed spurion tiling/common-parent discrepancy is not used. Literature PDFs are intentionally unbundled; the proofs README and citation record explain this and provide source links. This review does not reverify the external theorems. |
| Is the released version unambiguously identified? | **PASS for candidate labeling.** The paper states the date, candidate tag, historical base commit, chosen licenses, and honest repository/DOI placeholders. It does not claim a deposited archive or minted release commit. Hash validation and final source/PDF synchronization must be established by the packaging run. |

## Development evidence and final gates

The retained [development record](audit/DEVELOPMENT_CHECKS.md) explains
the initial exact-integer serialization comparisons and preserves their
failed logs. The third development replay passed the main finite checks
and then stopped because the manifest had not yet been created. Its
failure is visible in [the original log](logs/development_replay_3.txt);
it is not presented as a successful full release run. Different inverse
branch counts are documented as an implementation difference, with
entrywise equality of the reconstructed indicator matrix.

When this review checked every relative file link in the certificate
index, the only absent target was `SHA256SUMS.txt`, which the packaging
process had not yet frozen. That is a pending release operation, not
evidence of a missing geometric witness. The final package must supply
and verify that manifest, generate its clean replay log, and report their
actual results in the readiness report. A development PASS, this access
review, and regression-test totals are each insufficient on their own
for a final release verdict.

## Remaining human actions and limits

No additional research or silent mathematical repair is requested by
this review. Existing mathematical premises remain available for a
referee to examine in the paper and preserved notes. This review makes no
new independent claim that the entire symbolic proof has been re-proved.

Before public submission the human author must approve the prepared
manuscript and licensing metadata, publish the repository/archive, and
replace the explicit repository and Zenodo placeholders with real
identifiers. No automatic submission or external peer review is claimed.
