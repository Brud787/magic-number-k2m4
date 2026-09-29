# Prepared release: 1.0.0-paper

Public repository: [Brud787/magic-number-k2m4](https://github.com/Brud787/magic-number-k2m4).
Reserved Zenodo DOI: [10.5281/zenodo.23028034](https://doi.org/10.5281/zenodo.23028034).
Intended GitHub tag: `v1.0.0-paper`. The metadata-only packaging task does not
create a tag, upload files, publish the reserved deposit, or submit to a journal
or arXiv.

The release gives readers access to the existing computational certificates
for the manuscript's fixed `k=2, m=4` theorem. `CERTIFICATE_INDEX.md` maps each
machine-dependent assertion to a stable certificate ID, literal files, its
mathematical role, and an exact replay command. The public package preserves
the necessary historical artifacts and provides normalized catalogues for
reader navigation.

The one-command entry point is:

```sh
python verify_all.py
```

Install the pinned runtime dependencies first, as documented in
`REPRODUCIBILITY.md`. Verification is exact and requires no network access
after installation. Read `SUBMISSION_READINESS.md` and the preserved clean
replay log for the verified certificate status. The final
metadata-only pass checks compilation, links, metadata, and artifact integrity;
it does not recompute certificates or conduct another proof audit. Regression
tests are separate engineering checks, not replacements for certificates.

Code is MIT licensed. The manuscript, documentation, and original data are
CC BY 4.0 licensed. See `LICENSE` for scope and `LICENSES/` for the full texts.

Provenance before publication edits: Git commit
`284c19a88a8e1327f139d4e3c58d16c751610b73`. This is a baseline identifier, not a
commit containing the prepared release. A release commit has not been assigned
by this packaging task. The hash manifest identifies the prepared artifact
bytes independently of Git.

Before public deposition the human author should:

1. Review the manuscript and readiness report, including any reported blockers.
2. Copy the complete contents of the working repository's `publication/`
   directory into the public GitHub repository root, including `.zenodo.json`.
3. Commit the intended release and create the `v1.0.0-paper` release tag.
4. Upload `submission/magic-number-v1.0.0-paper.zip` and the matching
   `publication/paper/paper.pdf` from the working repository to the Zenodo
   deposit reserved as `10.5281/zenodo.23028034`, reviewing `.zenodo.json` and the
   component-specific licenses before submission.
5. Upload `submission/magic-number-arxiv-source.zip` to arXiv and use the
   prepared journal source package when ready. These paths refer to the
   working repository; the release ZIP retains the `publication/` wrapper.

The source manuscript title, author information, publication metadata, and
license choices should be confirmed by the author before public deposition.
