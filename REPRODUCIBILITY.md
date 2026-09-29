# Exact replay

Public repository: [Brud787/magic-number-k2m4](https://github.com/Brud787/magic-number-k2m4). Reserved Zenodo DOI: [10.5281/zenodo.23028034](https://doi.org/10.5281/zenodo.23028034), version `1.0.0-paper`. The DOI is reserved; publication of the deposit is a separate step. The public repository root contains the supplement files; the ZIP retains the enclosing `publication/` directory.

## Environment

The release was prepared with Python **3.14.6**, SymPy **1.14.0**, and mpmath **1.3.0**, on macOS **26.5.1**, Darwin arm64. The verifier uses Python's exact integers and `fractions.Fraction`, and SymPy's rational matrix operations. No floating-point rank, determinant, or membership decision is accepted. mpmath is SymPy's dependency; floating-point arithmetic is not a proof mechanism.

The frozen dependencies are in [requirements.txt](requirements.txt). Other Python/platform combinations are not claimed as tested merely because they should support these operations. No TeX installation is required to replay the certificates.

## Install and run

Run these commands from the public repository root or the extracted `publication/` directory:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python verify_all.py
```

On Windows, use `.venv\Scripts\python.exe` instead. Package installation may require network access. Verification after installation uses only local files and requires no account, API key, network service, or proprietary solver.

For an offline installation, download the dependency wheels on a connected machine:

```sh
python3 -m pip download -r requirements.txt -d wheels
```

Copy the release and wheels to the target machine, then install with:

```sh
.venv/bin/python -m pip install --no-index --find-links wheels -r requirements.txt
.venv/bin/python verify_all.py
```

To select a certificate, use its stable ID from [the index](CERTIFICATE_INDEX.md):

```sh
.venv/bin/python verify_all.py --list
.venv/bin/python verify_all.py --certificate MEM-FOUR-MASS
.venv/bin/python verify_all.py --certificate N9-KERNEL
.venv/bin/python verify_all.py --certificate NORM-10
```

Selection may run prerequisite checks or a whole matrix family. A rank check on A9 must first reconstruct its witness rows. Only the unselected full run can issue the full-publication success verdict. Process exit status is zero on success and nonzero on failure. Do not use `python -O` or set `PYTHONOPTIMIZE`: the verifier explicitly requires active assertions.

## What is reconstructed

1. Cyclic rank-two partitions reconstruct the entire membership catalogue, the 29 parent types and their facets, the n = 9 tile universe, and transported local and normalized rows. These are compared to the preserved exact artifacts.
2. Exact inverse calculations recompute the memberships at the local and n = 9 witnesses. All 472 × 942 = 444,624 principal indicator decisions are checked, including excluded tiles. Source positivity, image equations, external positivity, and the declared strict generic conditions are checked as applicable.
3. Every claimed rank has an explicit nonzero selected minor for a lower bound and either a verified rational row-span certificate or the matrix dimension for its upper bound. The product A9 R9ᵀ is checked entry by entry.
4. Auxiliary saved unit vectors and the Discussion's finite weight comparisons are replayed separately from the main proof chain.
5. The hash manifest checks the frozen public artifacts. Regression tests are engineering safeguards and do not replace these certificate checks.

The theorem still uses the symbolic membership/inverse arguments, geometric local relation proofs, simplicial descent, and cited external theorems stated in the paper. See [PROOF_DEPENDENCIES.md](PROOF_DEPENDENCIES.md).

## Determinism, caches, and resources

Replay uses the saved rational witnesses in their frozen order. It performs no random search and has no random seed to choose. Historical trial numbers and search seeds are provenance; they are not rerun to generate replacement witnesses. The verifier does not accept a cached PASS flag or skip membership decisions because a frozen matrix exists. Its reuse of external frames and inverses is confined to in-memory caches for the current process.

The preserved clean replay from the certificate-packaging pass took **97.731 seconds** and reported **185,712,640 bytes** of peak resident memory on the tested machine. Allow a few minutes, several hundred megabytes of working memory, and about 200 MB of extracted release space, with additional space for the Python environment. These are planning estimates, not a cross-platform performance guarantee; [the preserved replay log](logs/final_clean_replay.txt) and [machine-generated metadata](logs/final_clean_replay_metadata.json) record the actual run.

The reconstructed A9 is compared entry-for-entry to both the public matrix and the historical promoted matrix. The log also prints a SHA-256 digest of its row-major sequence of 0/1 bytes. This digest concerns mathematical matrix entries, not JSON whitespace. Historical JSON copies retain their original bytes; normalized catalogues add IDs and may have different JSON serialization.

Diagnostic branch counts can differ from a historical replay because an equivalent cyclic cut may expose mixed-sign exclusion at a different stage. The publication replay initially counted 91,337 six-row solves, 351,871 mixed-sign exclusions, and 1,416 spurion inversions, totaling 444,624. Equality of every matrix entry, positivity, and the exact strictness conditions are the acceptance criteria; agreement of internal branch counts is not.

## Clean replay and hashes

A new interpreter process is sufficient to clear every verification cache. A fresh extraction and new virtual environment also test that no files from the research checkout are needed. From that extraction:

```sh
.venv/bin/python verify_all.py > replay-local.txt 2>&1
```

Inspect the process exit status and the final line. Preserve the full output on failure. A new replay may differ from the supplied log in elapsed time or platform metadata while checking the same exact mathematical objects. Do not regenerate frozen certificate data or the published manifest to make a failed comparison pass.

[SHA256SUMS.txt](SHA256SUMS.txt) covers the frozen manuscript, PDF, certificates, verifier sources, documentation, expected replay output and supplied final clean log. It cannot hash itself. During release preparation the clean replay is captured outside the package, then copied into the package and frozen; the manifest is finalized and checked again with `ARTIFACT-HASHES`. This avoids writing a log while checking its own hash. Readers should write fresh output to a new local file, as above, and must not overwrite `logs/final_clean_replay.txt`. A local replay log is not a new frozen certificate. `ARTIFACT-HASHES` checks the manifest without rebuilding or modifying it.

The final metadata-only pass inserts the public repository URL and reserved DOI, rebuilds the manuscript and submission packages, and refreshes hashes. Its checks are limited to compilation, links, metadata, and artifact integrity. It does not rerun mathematical certificates, conduct a broad proof audit, or alter theorem scope or proof content. The supplied clean replay remains evidence from the earlier certificate-packaging pass.

The normalizer `build_catalogues.py` is a release-maintenance tool, not a required verification step. Its inputs are preserved copies, and its output is frozen before replay. Re-running it is unnecessary for readers and changes release artifacts; compare the independently reconstructed mathematical data through `verify_all.py` instead.

## Manuscript build

The 18-page release PDF was built with Tectonic **0.17.0**, with
`SOURCE_DATE_EPOCH=1790553600`. The source contains its bibliography and needs
no separate `.bib`, figures, or private style files. From a copy of `paper/`:

```sh
SOURCE_DATE_EPOCH=1790553600 tectonic --untrusted --keep-logs main.tex
```

The first build can download Tectonic's TeX bundle. Add `--only-cached` for an
offline build after that bundle is installed. The final release and isolated
arXiv builds both used `--only-cached` and produced byte-identical PDFs; see
[the build record](audit/package_validation.json) and [build log](logs/paper_build.txt).
The distributed `paper.pdf` is the resulting `main.pdf` renamed for clarity.
TeX reported only underfull spacing warnings in the dependency table and
availability paragraph, with no overfull boxes or unresolved references.
Certificate replay does not invoke TeX.

## Regression baseline and failure policy

Before manuscript/package edits, the existing repository suite recorded **240 passed, 0 failed**, in **142.43 s**; see [audit/baseline_tests.json](audit/baseline_tests.json). This baseline includes historical engineering tests and is distinct from publication certificate verification.

Missing witnesses, a count/rank/determinant disagreement, an exceptional membership input, a reconstruction mismatch, or a hash mismatch must stop promotion of the affected claim. Keep the complete failing output and the original artifacts. Do not overwrite historical data, substitute numerical tolerances, or interpret an undecided inverse as nonmembership. The final status is reported in [SUBMISSION_READINESS.md](SUBMISSION_READINESS.md).
