# Magic Number for k = 2, m = 4: computational supplement

This directory makes the existing preprint's finite computational certificates available for exact replay. Start with [CERTIFICATE_INDEX.md](CERTIFICATE_INDEX.md): every computational claim has a stable certificate ID, literal data, an executable check, and the mathematical meaning of a successful check.

Read the [18-page manuscript](paper/paper.pdf) or its [LaTeX source](paper/main.tex). The appendix specifies the finite objects and verification conditions; the index supplies direct file links and commands.

The release is prepared locally for public deposition. Suggested release tag: `v1.0.0-paper`. Repository URL: **[PUBLIC REPOSITORY URL TO BE INSERTED]**. Archive DOI: **[ZENODO DOI TO BE INSERTED AFTER RELEASE]**. These placeholders do not denote an existing public deposit.

## Verify

From this directory, with Python and the pinned dependencies installed:

```sh
python verify_all.py
```

To inspect or replay one claim:

```sh
python verify_all.py --list
python verify_all.py --certificate N9-KERNEL
python verify_all.py --certificate NORM-10
```

The verifier uses exact rational arithmetic, rebuilds all 444,624 entries of the principal n = 9 indicator matrix from its geometric witnesses, checks both bounds for each nontrivial rank claim, and checks the frozen artifact hashes. An exceptional membership input or any mismatch fails the replay. A successful full run ends with:

```text
ALL PUBLICATION-CRITICAL CERTIFICATES PASSED
```

[REPRODUCIBILITY.md](REPRODUCIBILITY.md) gives installation, environment, timing, deterministic replay, and clean-run instructions. [SUBMISSION_READINESS.md](SUBMISSION_READINESS.md) records the actual release status; the line above certifies the implemented finite checks, not an independent proof of the paper's symbolic or cited inputs.

## Find a certificate

| Paper claim | Start here |
|---|---|
| Complete tile classification, counts 1, 14, 36, 30, 5 | [MEM-CORES](CERTIFICATE_INDEX.md#mem-cores) |
| Four-mass exclusion and spurion inverse | [MEM-FOUR-MASS](CERTIFICATE_INDEX.md#mem-four-mass), [MEM-SPURION](CERTIFICATE_INDEX.md#mem-spurion) |
| 29 parents; literal balanced relations | [LOCAL-PARENTS](CERTIFICATE_INDEX.md#local-parents), [LOCAL-RELATIONS](CERTIFICATE_INDEX.md#local-relations), [human-readable catalogue](certificates/local/PARENTS.md) |
| 45 ten-wall witnesses; two hostile determinants | [LOCAL-TEN-WALL](CERTIFICATE_INDEX.md#local-ten-wall), [LOCAL-HOSTILE-8](CERTIFICATE_INDEX.md#local-hostile-8), [LOCAL-HOSTILE-9](CERTIFICATE_INDEX.md#local-hostile-9) |
| 942 tiles, 693 relations, rank 470 | [N9-UNIVERSE](CERTIFICATE_INDEX.md#n9-universe), [N9-LOCAL-RANK](CERTIFICATE_INDEX.md#n9-local-rank) |
| 472 witnesses, rank 472, determinant 4, annihilation | [N9-INDICATORS](CERTIFICATE_INDEX.md#n9-indicators), [N9-INDICATOR-RANK](CERTIFICATE_INDEX.md#n9-indicator-rank), [N9-ANNIHILATION](CERTIFICATE_INDEX.md#n9-annihilation) |
| Finite K9 = L9 certificate chain | [N9-KERNEL](CERTIFICATE_INDEX.md#n9-kernel) |
| Normalized dimensions 1, 9, 19, 12, 0, 0 | [NORM-6 through NORM-11](CERTIFICATE_INDEX.md#normalized-certificates) |
| Discussion's saved signed unit functionals | [N8-UNIT](CERTIFICATE_INDEX.md#n8-unit), [N9-UNIT](CERTIFICATE_INDEX.md#n9-unit), [WEIGHT-PROBES](CERTIFICATE_INDEX.md#weight-probes) |

## Contents and scope

- `paper/`: the revised manuscript source and its compiled PDF.
- `certificates/`: literal rational witnesses, integer matrices, canonical catalogues, and preserved historical inputs.
- `verifier/`: exact certificate checks and rational rank/determinant verification.
- `independent/`: standalone combinatorial reconstruction and the adapted secondary ambient membership replay; [independence statement](independent/README.md).
- `proofs/`: preserved mathematical explanations and historical reviews supporting the symbolic premises.
- `tests/`: engineering checks, separate from mathematical certificates.
- `logs/`: actual replay records; `audit/` retains provenance and the baseline inventory.

[PROOF_DEPENDENCIES.md](PROOF_DEPENDENCIES.md) separates finite computations from symbolic arguments and external theorems. The package concerns the existing rank-two, m = 4 all-Z theorem. A finite indicator matrix supplies necessary equations on all-Z relations; its kernel is identified with K9 only through the paper's local theorem and dimension argument. Neither sampled membership nor passing unit tests alone proves the all-n theorem.

The research repository is preserved in place. Release copies add stable IDs without overwriting historical results. The original root README describes an early research stage; this supplement and the authoritative `magic_number_k2_m4_preprint.tex` identify the manuscript packaged here.

## License and citation

Code is licensed under MIT. The manuscript and certificate data are licensed under CC BY 4.0; see [LICENSE](LICENSE) for the scope and attribution details. Use [CITATION.cff](CITATION.cff) when citing the release and replace the repository/DOI placeholders only after actual deposition. AI tools are not authors; the manuscript's disclosure describes their assistance and the human author's responsibility.
