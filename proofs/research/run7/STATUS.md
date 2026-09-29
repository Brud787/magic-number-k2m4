# Run 7: uniform rank-two generation

**PROVED — SUCCESS F.** For k=2,m=4 and every n≥6,

\[
K_n=L_n,\qquad D_n\subseteq L_n.
\]

Consequently every complete multiplicity-one all-Z positroid tiling has

\[
M(2,n-6,2)=\frac1{n-3}\binom{n-3}{2}\binom{n-3}{3}
=\frac{(n-3)(n-4)^2(n-5)}{12}
\]

tiles. The [complete argument](GLOBAL_GENERATION.md) passed two separate
global proof reviews and independent geometric and finite-certificate
checks. This is the all-n k2,m4 theorem; no arbitrary-k claim is made.

**PROVED — new global mechanism.** Signed adjacent-column addition and
zero insertion make the tile spaces, local spans and all-Z kernels into
simplicial vector spaces. The geometric proof accounts for every positive
source branch, collapsed output, multiplicity and rank-loss limit.
It repairs ordinary deletion rather than assuming deletion works.

**COMPUTATIONALLY-VERIFIED / PROVED — complete finite normalized gate.**
The normalized quotient dimensions for source label numbers6,...,11 are
1,9,19,12,0,0. The critical n10/n11 determinants are−1 and+1. The support
bound gives zero normalized groups at every later label number. Exact
normalization of the inclusion K/L↪V/L, together with K9=L9, then forces
K/L=0 for all n. No full n10 matrix or indicator computation is needed.

**PROVED — all-n rank formula.**

\[
\dim(V_n/L_n)=\binom{n-1}{5}+9\binom{n-1}{6}
+19\binom{n-1}{7}+12\binom{n-1}{8}.
\]

Subtracting from the preserved complete tile count gives rank L_n=dim K_n.
At n10 this implies quotient1674 and local rank2141; these are structural
consequences of the normalized proof, not a full n10 matrix calculation.

**FAILED — retained hostile prediction.** The initial support-polynomial
guess gave quotient1675 at n10. The35-column diagnostic killed it.
The literal prediction, data and correction remain in
[RANK_PATTERNS](RANK_PATTERNS.md) and [N10_DIAGNOSTIC](N10_DIAGNOSTIC.md).

**PROVED — deletion obstruction fully classified.** At every fixed slot,
ordinary deletion satisfies delta_j(L_(n+1))=V_n. All136 prototype-label
cases and798 fixed-slot tile witnesses are recorded. Adjacent addition
supplies the necessary broad correction through a finite source rule.

**PROVED — scope limits.** This proof concerns constant all-Z coefficients
and all-Z tilings. It does not establish every fixed-Z indicator kernel,
flip connectivity, or L_n⊆D_n for arbitrary n. It makes no novelty claim
from the targeted literature search. Earlier runs remain historical,
unchanged artifacts; this file records the new campaign state.

**COMPUTATIONALLY-VERIFIED — baseline.** All201 existing tests passed in
130.74 seconds before changes. The315 baseline artifacts are recorded by
SHA-256 in [baseline.json](../../results/run7/baseline.json). Final test and
preservation results are recorded in [validation.json](../../results/run7/validation.json).

The bounded run ends after final verification. No further proof search,
complete-tiling enumeration, or change of k or m is underway.

**COMPUTATIONALLY-VERIFIED final validation:** all220 tests passed in140.19 seconds. The preservation audit is in `results/run7/validation.json`.
