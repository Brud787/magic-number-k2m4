# Submission readiness

This report covers the local `v1.0.0-paper` candidate prepared on
2026-09-28. The task was narrowed to exposing and replaying the existing
certificates, without a new broad mathematical audit. The theorem and proof
architecture are retained. **READY FOR EXTERNAL REVIEW** means that a referee
can access and replay this supplement; it does not assert peer acceptance,
public deposition, or a new proof of the symbolic premises.

The standalone full run exited zero in **97.731 seconds**, using Python
3.14.6, SymPy 1.14.0, and exact rational arithmetic. Its unedited
[log](logs/final_clean_replay.txt) ends with
`ALL PUBLICATION-CRITICAL CERTIFICATES PASSED`. The 30 PASS lines and final
verdict match [the expected output](logs/expected_output.txt). The log was
then frozen and the final artifact manifest checked again.

`PASS — retained` below identifies previously audited symbolic input,
preserved and linked for human review; it does not mean that Python verified
that argument or that this packaging pass re-proved it.

| Publication-critical component | Status | Evidence / exact scope |
|---|---|---|
| Theorem scope matches the existing proof | PASS | All six theorem environments and both definitions equal the original manuscript; no broadened or weakened theorem. [Changes](audit/manuscript_changes.md) |
| Every computational paper claim is accessible | PASS | 24 computational claim IDs, plus artifact integrity; literal files, commands and implications in [CERTIFICATE_INDEX.md](CERTIFICATE_INDEX.md) |
| Membership classification replayed | PASS | `MEM-CORES`: 221 labeled records, 24 dihedral types; admitted counts 1,14,36,30,5 |
| Local parent classification replayed | PASS | `LOCAL-PARENTS`: 29 types, partition 12+10+5+2, exact facets |
| Four-mass certificate replayed | PASS | `MEM-FOUR-MASS`: positive Z, two distinct positive source planes, exact image row change |
| Spurion inversion replayed | PASS | `MEM-SPURION`: 19 exact cases; generic inversions also replayed at the local/n9 witnesses; all-Z injectivity remains the declared published input |
| Literal local relations exposed and balanced | PASS | `LOCAL-RELATIONS`: all 15 vectors and exact zero sums; geometric all-Z validity remains the retained local proof |
| Ten-wall certificates replayed | PASS | `LOCAL-TEN-WALL`: 45 exact witnesses, five rank-nine tree matrices |
| Hostile certificates replayed | PASS | `LOCAL-HOSTILE-8`, `LOCAL-HOSTILE-9`: every entry reconstructed, both determinants 1 |
| n=9 tile universe replayed | PASS | `N9-UNIVERSE`: exactly 942 canonically identified columns |
| n=9 local rank replayed | PASS | `N9-LOCAL-RANK`: 693 rows; rank 470, selected determinant −1 and exact row-span upper certificate |
| All 444624 membership decisions replayed | PASS | `N9-INDICATORS`: 472 witnesses; entrywise equality with public and historical A9 |
| n=9 indicator rank replayed | PASS | `N9-INDICATOR-RANK`: exact selected 472-square determinant 4, hence rank 472 |
| A9 R9ᵀ = 0 replayed | PASS | `N9-ANNIHILATION`: every entry checked exactly |
| K9=L9 chain verified | PASS — mixed | `N9-KERNEL`: dimensions 470 and 942−472; inclusions explicitly conditional on retained local and strict-neighborhood propositions |
| Normalized n=6,...,11 replayed | PASS | `NORM-6` through `NORM-11`: all column/row lists rebuilt; ranks 0,6,31,54,35,5 with both bounds |
| n=10 determinant −1 replayed | PASS | `NORM-10`: selected 35-square minor |
| n=11 determinant 1 replayed | PASS | `NORM-11`: selected 5-square minor |
| Support cutoff | PASS — mixed | `SUPPORT-CUTOFF`: support catalogue and n=12 normalized emptiness; all-n pigeonhole argument retained |
| Amalgamation and descent | PASS — retained | [Existing proof](proofs/research/run7/AMALGAMATION_PROOF.md), manuscript; no new broad audit |
| Simplicial identities audited | PASS — retained | [Existing simplicial proof](proofs/research/run7/SIMPLICIAL_AMALGAMATION.md), including signed wrap; not a finite replay conclusion |
| Truncation persistence audited | PASS — retained | Same existing proof and manuscript argument; no new claim of independent re-proof |
| Dold–Kan argument audited | PASS — retained | [Global generation](proofs/research/run7/GLOBAL_GENERATION.md), p=n−1 convention, external normalization references |
| Magic Number deduction audited | PASS — retained | Existing augmentation/BCFW comparison, [dependency map](PROOF_DEPENDENCIES.md) |
| External citations verified | PASS — source record | [CITATION_AUDIT.md](CITATION_AUDIT.md) identifies exact inputs and limits; external theorems are not computer certificates |
| Tiling definition consistent | PASS | Existing closed cover/open-disjoint definition retained unchanged |
| Ancillary finite observations exposed | PASS | `N8-UNIT`, `N9-UNIT`, `WEIGHT-PROBES`; distinct from main theorem premises |
| Manuscript matches certificates | PASS | [Final access review](FINAL_REFEREE_AUDIT.md); all paper IDs indexed, literal dimensions and selected determinants consistent |
| Clean standalone verifier passes | PASS | Fresh standalone copy, no production-construction imports, pinned installed dependencies; [metadata](logs/final_clean_replay_metadata.json) |
| Regression safeguards | PASS | Original suite: 240 passed, 0 failed; new verifier guards: 6 passed. [Baseline](audit/baseline_tests.json), [guard log](logs/verifier_guard_tests.txt) |
| arXiv package compiles | PASS | Self-contained `main.tex`; isolated build byte-identical to 18-page release PDF; [build record](audit/package_validation.json) |
| Release source/PDF binding | PASS | Authoritative source and three source copies identical; release/journal PDFs match; source and PDF digests recorded |
| Historical artifacts preserved | PASS | 1620 original files unchanged; only authoritative manuscript revised, with original retained. [Preservation check](audit/preservation.json) |
| Release hashes verified | PASS | [SHA256SUMS.txt](SHA256SUMS.txt) covers frozen paper, certificates, verifier, expected output and actual final replay; `ARTIFACT-HASHES` rerun after log freeze |
| Licenses and disclosure | PASS | Author-authorized MIT code, CC BY 4.0 manuscript/data; AI assistance disclosed without AI authorship |

No unresolved finite-certificate failure or hidden mathematical repair was
found. The development serialization-check failures are preserved and
explained in [the development record](audit/DEVELOPMENT_CHECKS.md). The final
replay rebuilt the original mathematical matrices without altering them.
The theorem's symbolic arguments remain subject to normal external review.

Manual publication steps remain: human-author review; commit/tag the release;
publish the repository and deposit the supplement; replace the visible URL,
release-commit and Zenodo DOI placeholders; rebuild and rehash any changed
paper copies; and submit the prepared sources. No upload, DOI, or external
submission has been claimed or performed. These are publication logistics,
not unresolved certificate failures.

SUBMISSION STATUS: READY FOR EXTERNAL REVIEW
