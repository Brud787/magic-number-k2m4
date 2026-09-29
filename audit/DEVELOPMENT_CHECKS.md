# Development checks

The first two release harness attempts compared integer rows against historical JSON strings, failing Python equality before rank promotion. Normalizing those decimal strings to exact integers fixed serialization comparisons; no numerical entry or mathematical claim changed. The third attempt passed all main finite checks and stopped because SHA256SUMS.txt had not yet been created. These logs are retained separately from the clean replay.

The independent ambient n9 replay uses a different deterministic cyclic cut. Its branch counts are 351871 mixed-hyperplane exclusions, 91337 six-row inversions, and 1416 spurion decisions; all 444624 decisions equal the historical matrix. Branch counts describe the algorithm, not a different matrix.
