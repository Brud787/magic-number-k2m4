# Final reader-access review

Reviewed on 2026-09-28. Scope: navigation, identifiers, literal-file access,
replay-command registry, and disclosure consistency. This is not a new
mathematical proof audit or a replay of previously checked arithmetic.
The final PDF, readiness report, clean replay log, and hash manifest were
still being prepared and are outside this review's missing-file findings.

| Check | Result |
| --- | --- |
| Executable certificate registry | PASS: `python verify_all.py --list` returns 25 IDs; every ID is present in `CERTIFICATE_INDEX.md`. The six normalized IDs share a clearly labeled table. |
| Manuscript cross-references | PASS: all 24 `\cert{...}` references have matching `cert:...` labels and executable registry entries. The remaining registry ID is the artifact-integrity check. |
| Literal certificate paths in manuscript | PASS: every path under `certificates/`, `verifier/`, `independent/`, and `proofs/` exists. |
| Current reader-facing links | PASS: 112 relative links in 12 top-level, independence, and journal-metadata documents resolve, excluding the explicitly pending final artifacts. |
| Data-field descriptions | PASS: the described R9, A9, normalized-matrix, overlap, hostile-index, and spurion file keys match the literal JSON schemas inspected. Stored matrix order and zero-based array indices are documented. |
| Claim-to-command route | PASS: the index supplies the claim, paper location, literal files, exact selection command, expected mathematical checks, implication, and independence scope. It distinguishes a selected replay from the complete release verdict. |
| Independence disclosure | PASS: the index and `independent/README.md` distinguish historical producers, adapted secondary membership replay, standalone combinatorics, shared prototypes and mathematics, and the absence of new external human peer review. |
| Archive/publication status | PASS: README, release notes, CFF/Zenodo metadata, manuscript, and journal statements explicitly describe a local candidate and placeholders. No actual public deposition, DOI registration, tag creation, or submission is claimed. |
| Licensing and attribution | PASS: code MIT; manuscript/documentation/original data CC BY 4.0; third-party dependencies and literature are excluded from relicensing. The baseline commit is not represented as the release commit. |

Two navigation/wording observations were reported to the coordinating agent:

1. Among 365 relative links in 84 preserved historical proof documents, 18
   links in `proofs/research/DEFINITIONS.md` point to five intentionally omitted
   third-party literature PDFs. These are historical bibliographic links,
   not missing proof-certificate data. The proposed remedy is a current README
   notice directing readers to the live theorem-source links in
   `CITATION_AUDIT.md` and retained bibliographic records, without modifying
   the preserved historical file or redistributing the PDFs.
2. The manuscript describes `independent/` collectively as a new
   reconstructor. For precision, repeat the existing README disclosure that
   its membership module adapts the historical secondary Run 6 ambient
   verifier and is not a third independently invented inverse. This is a
   clarity improvement, not a reported certificate failure.

No publication-critical missing certificate, identifier mismatch, broken
current claim-to-data link, or false archive/independent-human-audit claim
was found within this review's scope. Final compilation, complete exact
replay, and manifest validation remain the coordinator's release checks.

Packaging follow-up: both wording/navigation observations above were resolved
in the final manuscript, proofs README, and citation record. The original
review findings are retained above as provenance.
