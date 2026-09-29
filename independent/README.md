# Reconstruction and independence

The word “independent” here describes a construction or arithmetic implementation relative to the historical producer. It does not mean independent human peer review, a formally verified proof assistant, or software without shared mathematical assumptions.

| Component | Role | Independence and shared inputs |
|---|---|---|
| Historical research modules and JSON artifacts | Primary generators and frozen witnesses | Preserved as provenance; their recorded PASS flags are not accepted as verification. |
| [`combinatorics.py`](combinatorics.py) | Standalone reconstruction of source partitions, facets, tile universes, transported and normalized rows | Imports no `magic_number` production code. Uses the published cyclic-class description, dimension equation, admissibility theorem, and the 15 literal signed relation prototypes. |
| [`membership.py`](membership.py) | Secondary exact ambient inverse replay | Adapts the historical Run 6 secondary verifier. It is not a third independently invented inverse. It imports standalone class decoding and SymPy, not the producer's membership or quotient-inverse code. |
| [`../verifier/exact.py`](../verifier/exact.py) | Rational determinant and row-span checks | Uses Python `Fraction` arithmetic, independently of the historical matrix producer and SymPy rank decisions. |
| [`../verifier/checks.py`](../verifier/checks.py) | Release checks and comparisons | Calls these reconstructors, compares literal artifacts, and assembles the finite implications. This wrapper is not an additional independent verifier of them. |
| [`../build_catalogues.py`](../build_catalogues.py) | Release ID assignment and normalization | Shares `combinatorics.py` with replay. Thus the release normalizer and reconstructor are not independent of each other; comparison against historical producer artifacts supplies the separate construction. |

## Combinatorial reconstruction

A source is encoded by the full set of its nonzero unordered two-minors. Choosing cyclic gaps reconstructs all interval partitions with q + s = 12 or 13. Facets arise by deleting a member of a nonsingleton class or merging neighboring classes. The code derives bounded affine labels from Grassmann necklaces, inserts supports, and applies dihedral relabelings. Normalized columns keep only no loops or a single loop at position 1. These steps do not import the historical enumeration or matrix-building functions.

The literal 15 primitive relation vectors are mathematical input. Reconstruction checks their facet labels, balance, and transports; it does not independently reprove their all-Z geometric signs. Those signs are supported by the retained source proofs and the paper's local theorem. Likewise, the implemented admissibility predicate uses the proved membership criterion; a successful finite enumeration does not prove the external spurion theorem.

## Membership replay

For complement-five cells, the secondary replay works in a full six-row external frame. It recovers the intersection with the complementary five-space, solves in the compressed six-vector basis, constructs the complete source, checks its image equation, and tests all source two-minors. A mixed strict sign in the first intersection coefficients excludes membership before the full solve. The historical producer instead used its own quotient/hyperplane implementation.

For the spurion, the secondary replay solves twelve ambient equations in nine source coefficients and four target row-frame coefficients. The historical producer solved an 8 × 9 quotient system. The release checks a one-dimensional ambient kernel, nonzero source coefficients, and the three rank-five merger-exclusion conditions. Exceptional inputs raise an error in strict witness replay; they do not silently produce zero.

Both methods share the mathematical chart, positivity and closure propositions, the saved rational Z and Y, and SymPy's exact linear algebra. The release performs fresh decisions at every principal n = 9 matrix entry. Agreement is with the literal historical indicator rows, not with a historical status report. See [the original secondary-review description](../proofs/research/run6/INDICATOR_INDEPENDENT_REVIEW.md) for provenance, including the distinct historical branch counts.

## Boundaries of independence

No new broad mathematical audit is claimed by this packaging work. The archived reviews record their original authorship and dependencies. They are retained evidence of the earlier research process, not substitute public peer review. The uniform arguments—geometric descent, signed simplicial identities, truncation persistence, normalization, and the final augmentation step—remain human-readable mathematical premises. The [dependency map](../PROOF_DEPENDENCIES.md) marks them separately from the finite computations.
