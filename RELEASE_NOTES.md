# Prepared release: 1.0.0-paper

Suggested GitHub tag: `v1.0.0-paper`. This tag has not been created by the
publication packaging task. No repository upload, archive deposition, DOI
registration, or journal/arXiv submission is claimed.

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
after installation. Read `SUBMISSION_READINESS.md` and the generated clean
replay log for the verified status of this particular release. Regression
tests are separate engineering checks, not replacements for certificates.

Code is MIT licensed. The manuscript, documentation, and original data are
CC BY 4.0 licensed. See `LICENSE` for scope and `LICENSES/` for the full texts.

Provenance before publication edits: Git commit
`284c19a88a8e1327f139d4e3c58d16c751610b73`. This is a baseline identifier, not a
commit containing the prepared release. The actual release commit must be
recorded after the human author reviews and commits the package. The hash
manifest identifies the prepared artifact bytes independently of Git.

Before public deposition the human author should:

1. Review the manuscript and readiness report, including any reported blockers.
2. Commit the intended release; record that commit in the availability statement.
3. Create the public repository and `v1.0.0-paper` release tag.
4. Deposit the matching release in Zenodo, reviewing `.zenodo.json` and the
   component-specific licenses before submission.
5. Replace `[ZENODO DOI TO BE INSERTED AFTER RELEASE]` and any repository URL
   placeholders with real identifiers, regenerate paper copies and hashes,
   and verify the final release again.
6. Upload the prepared arXiv and journal source packages manually when ready.

The source manuscript title, author information, publication metadata, and
license choices should be confirmed by the author before public deposition.
