# Final independent scope and prior-art review

Review date: 2026-09-06. Reviewed SIGN_MECHANISMS.md, LOCAL_RELATION_KERNELS.md, COUNTEREXAMPLE_SEARCH.md, the finite-core/transport statement, the independent q10 geometry reviews, and the relevant exact regression tests. This is the final bounded scope audit, not a new literature campaign or a proof of tiling generation.

**Review outcome: PASS for the precise theorem below.** The fixed-\(Z\), all-\(Z\), source-facet, indicator, and multiplicity quantifiers are essential. The proof of each geometric relation and each hostile membership certificate remains a dependency of the final theorem; the finite source count alone is not its proof.

## The theorem that the work supports

For a nine-dimensional rank-two positroid source cell \(P\subset Gr^{\ge0}_{2,n}\), let \(F(P)\) be exactly its eight-dimensional codimension-one source facets whose maps are injective for **every** positive \(n\times6\) external matrix. Fix this tile index set independently of \(Z\). Define

\[
\mathcal R_{\mathrm{all}}(P)=
\left\{c\in\mathbb R^{F(P)}:
\text{for every positive }Z,\quad
\sum_{S\in F(P)}c_S\,\mathbf1_{Z_S(Z)}=0
\text{ modulo semialgebraic sets of dimension }<8
\right\}.
\]

The coefficients are constants independent of both \(Y\) and \(Z\). The lower-dimensional exceptional set may depend on \(Z\). Open or closed tile indicators give the same quotient class because their differences lie in proper source-boundary images.

**PROVED after the recorded geometric and exact-certificate audits.** All nine-dimensional parents reduce to 29 loopless dihedral source cores. Their all-\(Z\) relation spaces are:

| Core sector | Number of core types | All-\(Z\) admissible facets per parent | \(\mathcal R_{\mathrm{all}}(P)\) |
|---|---:|---:|---|
| Collapsed parent image | 12 | 0 | Zero space |
| Complement-five circuit family | 10 | 6 | One-dimensional balanced \(3+3\) span |
| Four reflected and one repaired-spurion family | 5 | 10 | One-dimensional balanced \(5+5\) span |
| Four-mass hostile families | 2 | 8 | Zero space |

Consequently every constant-coefficient all-\(Z\) indicator relation supported on the admissible facets of **any one** nine-dimensional rank-two \(m=4\) source parent has zero coefficient sum. This includes arbitrary real coefficients, not only coefficients \(\pm1\).

The twelve zero spaces in the first row are vacuous spaces on an empty index set; they are not nontrivial cancellation theorems. The two hostile zero spaces are genuine independence results on eight tiles.

## Why the finite and all-\(Z\) steps are legitimate

**PROVED (preserved source reduction).** Rank-two source dimension is \(q+s-4\), so a nine-dimensional parent satisfies \(q+s=13\) and has \((q,s)=(7,6),(8,5),(9,4),(10,3),(11,2)\). The 364 loopless labeled parents have 29 dihedral composition types. The independently implemented composition, affine, and boundary tests cover these types and their complete admissibility partitions. No dimension-only tile classification is being used.

The map identity for loop insertion is \((j_I C)Z=CZ_I\). Row restriction preserves positivity, and the reviewed positive-row extension lemma realizes every positive core matrix as such a restriction with prescribed gaps. Therefore both directions of the all-\(Z\) relation-space identification hold. Dihedral transport also intertwines the maps and preserves the coefficient-sum question. This is why the theorem covers arbitrary \(n\), despite the bounded core supports; it is not finite verification relabeled as an infinite theorem.

**PROVED (stronger circuit statement).** For the ten complement-five types, the symbolic free-inequality construction gives all nine open cross-sign overlaps for every positive \(Z\). The graph is \(K_{3,3}\), so the relation kernel is one-dimensional at **each fixed positive \(Z\)**, on the same six all-\(Z\) admissible tiles. CIRCUIT_KERNEL_REVIEW.md independently checks the construction and the use of open overlaps.

**PROVED by exact finite certificates (five ten-wall types).** The saved spanning-tree edges are exact positive open-wall preimages with equal image planes. Their openness follows from the previously certified tile injectivity, not from a numerical rank. A connected graph gives nine necessary equations on any relation. The already proved nonzero all-\(Z\) canonical relation gives the matching lower bound. Thus the kernel is exactly its span at the displayed positive rational \(Z_0\), and

\[
\mathbb R\epsilon\subseteq\mathcal R_{\mathrm{all}}(P)
\subseteq\mathcal R_{Z_0}(P)=\mathbb R\epsilon.
\]

This does not prove \(\mathcal R_Z(P)=\mathbb R\epsilon\) at every other fixed \(Z\). No complete chamber enumeration is needed: necessary overlap equations already provide the required rank bound.

**PROVED by exact finite certificates (two hostile types).** Every displayed indicator-matrix row is certified on an open target neighborhood through complete rational preimage decisions and the source-closure/gauge audit. The exact determinant-one matrices imply \(\mathcal R_{Z_0}(P)=0\), hence \(\mathcal R_{\mathrm{all}}(P)=0\). The openness is essential because an indicator relation is only required away from a lower-dimensional set. A table of values at potentially exceptional sample points would not suffice.

**COMPUTATIONALLY-VERIFIED.** This reviewer reran the local-overlap, hostile-certificate, and parent-profile tests: **18 passed in 6.62 seconds**. The overlap tests use exact image Plücker coordinates independently of the producing row-change equations; the hostile tests and core checks retain their independent implementations. These regressions support the exact finite certificates. They do not replace the symbolic all-\(Z\) geometric proofs.

## Covering and generation limits

The one-dimensional balanced kernel implies precisely two **multiplicity-one all-\(Z\) facet tilings** of each balanced parent image. Subtract one canonical side from another such 0/1 indicator decomposition; the resulting coefficient vector is a scalar multiple of the canonical sign vector. The binary coefficients force either the same side or the opposite side.

The multiplicity-one qualification must remain explicit. An ordinary overlapping cover may include both canonical sides, so uniqueness is false for unrestricted covers. The wording “only two all-\(Z\) facet covers” should always mean multiplicity-one facet tilings, not arbitrary set-theoretic covers.

For the hostile eight-point parent, independence of the facet indicators does **not** decide whether a single admissible-facet tiling of the parent image exists. Such a covering question is inhomogeneous: it involves the parent indicator as an additional term. The attempted hole search is inconclusive and must remain so. The nine-point hostile parent has the separate, proved open-hole obstruction from Run 3. Conflating these two covering statuses would exceed the work.

Neither zero hostile kernel excludes relations involving extra tiles outside these source facets. Neither a balanced parent kernel nor their complete 29-core inventory proves that arbitrary tiling differences decompose into these parent relations. Fixed-\(Z\) tile collections allowed to vary with \(Z\), \(Z\)-dependent relation coefficients, arbitrary contained tiles, larger source relations, and generation/connectivity of complete tilings are outside the theorem.

## Targeted primary-source comparison

**SOURCE-VERIFIED.** Galashin–Lam Definition 7.1 defines a subdivision of a parent using source cells below that parent in Bruhat order. Section 13.4, Conjecture 13.10, proposes two equal-size boundary triangulations and uniqueness at every fixed positive \(Z\) for a nearly admissible parent. Conjecture 13.11 separately proposes connectivity of complete triangulations. The present work proves the stated uniform all-\(Z\) facet-relation classification and corresponding uniform facet-tiling uniqueness. Its five ten-wall families do not supply the stronger uniqueness quantifier at every fixed \(Z\). The hostile four-mass warning is already explicit in their Example 13.12. [Primary paper, Definition 7.1 and §13.4, printed pp. 18 and 48–49](https://www.math.ucla.edu/~galashin/papers/duality.pdf).

**SOURCE-VERIFIED.** Mohammadi–Monin–Parisi already develops amplituhedron fiber methods, Gale/secondary constructions, and Grassmann polytopes with linear fibers. Their §5 secondary-fan conclusions retain the stated positivity and combinatorial-independence hypotheses; §7.3 discusses individual positroid-cell images. This is established methodology. Run 4 verifies the needed positive-fiber, wall, endpoint, and relation-kernel conditions for its source-core families, rather than importing an unconditional theorem about arbitrary \(m=4\) tiles. [Primary paper, §§5 and 7.3](https://arxiv.org/pdf/2010.07254).

**SOURCE-VERIFIED.** Łukowski–Parisi–Williams proves the positive-tropical-Grassmannian secondary-fan description for regular positroid subdivisions of the hypersimplex and studies its \(m=2\) amplituhedron connection. Those theorems do not supply the missing \(m=4\) parent-relation generation statement. [Primary paper and publication record](https://arxiv.org/abs/2002.06164), [published article](https://academic.oup.com/imrn/article/2023/19/16778/7046307).

The bounded search checked nearly-admissible balanced flips, rank-two amplituhedron relations, and secondary amplituhedron/positroid fibers, alongside the cited primary sections. This establishes the comparison above, not priority. No absence-of-search-result argument or novelty assertion is made.
