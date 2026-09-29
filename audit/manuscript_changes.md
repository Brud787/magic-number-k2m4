# Manuscript certificate-access changes

Authoritative source: `magic_number_k2_m4_preprint.tex`.

Scope: expose the existing computational proof to readers. The theorem
statements, mathematical scope, all-Z convention, tiling definition,
amalgamation argument, simplicial argument, and global proof architecture
were preserved. This pass did not initiate another proof audit or research
campaign.

## Certificate access

- Added linked stable certificate IDs beside every finite proof family and
  the supplementary unit-functional observations: 24 computational claim IDs total.
- Expanded Appendix A into a claim/data/check/conclusion specification for
  membership classification, four-mass noninjectivity, spurion inverse
  fixtures, local parent vectors, ten-wall overlaps, hostile determinants,
  the complete n=9 matrix chain, normalized matrices, and support cutoff.
- Documented rational encodings, array-index conventions, matrix ordering,
  row/column/witness IDs, full and per-family replay commands, exact rank
  upper certificates, and the empty determinant convention at n=6.
- Matched the inverse specification to `independent/membership.py`,
  including exceptional-input errors, complement-five signs and source
  pattern checks, the ambient spurion nullspace, and openness conditions.
- Distinguished the finite spurion inverse fixtures from the externally
  supplied all-Z injectivity assertion; no finite fixture is presented as
  proving that uniform assertion.
- Explained independent reconstruction and shared dependencies honestly:
  separate construction code, shared mathematical conventions and local
  prototypes, and common exact arithmetic libraries.
- The final access review prompted explicit wording that the ambient
  membership component adapts the historical secondary verifier and that
  release normalization shares standalone combinatorial routines.
- Added a compact dependency table and references to the supplement's
  certificate index, reproducibility guide, hash manifest, readiness report,
  and preserved symbolic notes.

## Metadata and attribution

- Fixed the manuscript date to September 28, 2026 and called the prepared
  supplement a publication candidate.
- Corrected the introduction's attribution using the primary task's
  verified sources: KWZ Conjecture 8.1 asserts existence of a tiling of
  MacMahon cardinality; Galashin–Lam Conjecture 3.9 formulates equal
  cardinality for all tilings.
- Updated the already verified KWZ, Galashin–Lam, and spurion references to
  their journal metadata, and identified BCFW arXiv v3 with its date and
  theorem numbers supplied by the primary citation check. Other references
  were retained.
- Added code/data availability wording with candidate tag `v1.0.0-paper`,
  historical base commit `284c19a88a8e1327f139d4e3c58d16c751610b73`, and
  explicit repository/Zenodo placeholders. No deposition is claimed.
- Recorded the user's chosen MIT license for code and CC BY 4.0 license
  for manuscript and data.
- Replaced the general acknowledgment with factual OpenAI ChatGPT/Codex
  assistance roles and explicit human-author responsibility.

## Checks performed during editing

- `git diff --check -- magic_number_k2_m4_preprint.tex`: passed.
- All 24 computational claim labels were found; no `\cert{...}` reference
  lacked a label.
- The n=9 local minor value and the six normalized determinant values in
  the appendix were compared to the literal public JSON fields.
- PDF compilation and release source/PDF synchronization are performed by
  the primary packaging process, with its logs retained in the supplement.

No historical research artifact was changed by this editing task. The
existing tiling definition already allowed shared closed boundaries and
required disjoint open images; it was not changed.
