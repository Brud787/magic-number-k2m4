# Definitions and convention audit

Audit date: 2026-09-04. The campaign uses the all-​Z convention of Parisi–Sherman-Bennett–Tessler–Williams (PSBTW), not an implicit fixed numerical matrix. Page numbers below are PDF page numbers of the supplied local files. SOURCE-VERIFIED statements record the cited sources; they do not claim new results.

## Grassmannians, positroids, and labels

**SOURCE-VERIFIED.** A point of \(\mathrm{Gr}_{k,n}(\mathbb R)\) is a row space of a full-rank \(k\times n\) matrix \(C\), modulo left multiplication by \(\mathrm{GL}_k\). Write \(\Delta_I(C)\) for its increasing-index maximal minors. A row space is totally nonnegative if a choice of overall orientation makes every \(\Delta_I\geq0\); it is totally positive if every \(\Delta_I>0\). For a realizable support \(\mathcal M\subseteq\binom{[n]}k\),

\[
S_{\mathcal M}=\{C\in\mathrm{Gr}^{\geq0}_{k,n}:\Delta_I(C)>0\iff I\in\mathcal M\}
\]

is a positroid cell. Its support matroid is a positroid. A cell is an open ball; the positroid decomposition is a regular CW complex. A positroid cell, its closure in the nonnegative Grassmannian, and its complex Zariski closure (the positroid variety) are different objects. [PSBTW §2.1, p.5](../literature/magic_number_m2.pdf); [Williams §2.3, Theorem 2.7](../literature/williams_ICM_survey.pdf).

**SOURCE-VERIFIED.** Cells have equivalent combinatorial labels: decorated permutations, bounded affine permutations, Grassmann necklaces, Le diagrams, and move-equivalence classes of reduced plabic graphs. Our bounded affine convention is

\[
b(i+n)=b(i)+n,\quad i\leq b(i)\leq i+n,\quad
\sum_{i=1}^n(b(i)-i)=kn.
\]

A fixed point \(b(i)=i\) is a loop; \(b(i)=i+n\) is a coloop. The Grassmann necklace \(I_i\) is the lexicographically minimal basis in cyclic order beginning at \(i\). A Le diagram has no zero with both a plus somewhere above it in its column and a plus to its left in its row. Its cell dimension equals its number of pluses. Do not infer dimension merely from the number of nonzero Plücker coordinates. [KWZ §2, especially Definitions 2.3–2.4 and Lemma 2.5, pp.4–5](../literature/KWZ_decompositions_amplituhedra.pdf).

## Amplituhedron, tile, and all-Z tiling

**SOURCE-VERIFIED.** Let \(\mathrm{Mat}^{>0}_{n,k+m}\) mean real \(n\times(k+m)\) matrices with all increasing maximal minors strictly positive. This condition concerns maximal minors, not positivity of every matrix entry or every minor of every size. For \(k+m\leq n\),

\[
\widetilde Z:\mathrm{Gr}^{\geq0}_{k,n}\longrightarrow\mathrm{Gr}_{k,k+m},
\qquad [C]\longmapsto[CZ],\qquad
\mathcal A_{n,k,m}(Z)=\widetilde Z(\mathrm{Gr}^{\geq0}_{k,n}).
\]

Total positivity ensures the map is defined on the whole nonnegative Grassmannian. Its target region has dimension \(km\). KWZ and Galashin–Lam sometimes use a \((k+m)\times n\) matrix and multiplication by its transpose; this is the same convention after transposing \(Z\). [PSBTW Definition 2.14, p.8](../literature/magic_number_m2.pdf).

**SOURCE-VERIFIED.** Fix \(Z\). For a positroid cell \(S\), put

\[
Z_S^\circ=\widetilde Z(S),\qquad
Z_S=\overline{\widetilde Z(S)}=\widetilde Z(\overline S).
\]

The equality of the two closed sets follows from continuity and compactness of \(\overline S\). The closed image is a **Grasstope**, without any dimension or injectivity assumption. It is a **tile** when \(\dim S=km\) and \(\widetilde Z|_S\) is injective; \(Z_S^\circ\) is its **open tile**. Injectivity on the open cell does not assert injectivity on its closure. Full generic differential rank alone does not prove global injectivity. [PSBTW Definition 2.16, p.9, Remark 5.19, p.26](../literature/magic_number_m2.pdf); [companion Definition 2.5, p.4](../literature/m4_spurion_tiles.pdf).

**SOURCE-VERIFIED.** A positroid tiling at \(Z\) is a finite collection indexed by distinct cells \(\mathcal C\), such that each \(Z_S\) is a tile,

\[
\mathcal A_{n,k,m}(Z)=\bigcup_{S\in\mathcal C} Z_S,
\qquad
Z_S^\circ\cap Z_{S'}^\circ=\varnothing\quad(S\ne S').
\]

There is **no requirement** that two closed tiles intersect in a common face. A face-to-face or good tiling is an additional condition, not part of Magic Number. Because the collection is finite, coverage by closed tiles is equivalent to density of the union of open tiles. [PSBTW Definition 2.16, p.9, introduction footnote 1, p.2](../literature/magic_number_m2.pdf).

**SOURCE-VERIFIED.** An **all-Z tiling** is one fixed cell collection \(\mathcal C\) satisfying the preceding conditions for **every** \(Z\in\mathrm{Mat}^{>0}_{n,k+m}\). The regions move with \(Z\); the indexing cells do not. PSBTW Definition 2.17 and Remark 2.18 explicitly adopt this convention and then often suppress “all-Z.” Their footnote 7 says no counterexample to independence of \(Z\) was then known; that is not a proof of independence. A generic-Z tiling requires a specified genericity notion and an appropriate open parameter set; a sample-Z tiling refers to one specified matrix. Neither is silently promoted to all-Z.

## Decomposition conventions and Magic Number

**SOURCE-VERIFIED.** KWZ Conjecture 8.1, p.27, originally asks for **existence** of a cell decomposition with \(M(k,n-k-m,m/2)\) top-dimensional cells. Its footnote 12 explicitly distinguishes disjoint dense images from a proved cell decomposition. The modern universal cardinality formulation is stronger than this existential wording. The Williams survey Conjecture 5.4, p.16, states the cardinality of a positroid tiling; PSBTW introduction, p.2, records the subsequent universal restatement and specifies all-Z in its theorem. [KWZ §8](../literature/KWZ_decompositions_amplituhedra.pdf); [Williams §5](../literature/williams_ICM_survey.pdf); [PSBTW pp.2,9](../literature/magic_number_m2.pdf).

**SOURCE-VERIFIED (formulation), CONJECTURAL (m=4 conclusion).** For even \(m\), the campaign's Magic Number assertion is: every all-Z positroid tiling has

\[
|\mathcal C|=M(k,n-k-m,m/2),\qquad
M(a,b,c)=\prod_{i=1}^a\prod_{j=1}^b\prod_{r=1}^c
\frac{i+j+r-1}{i+j+r-2},
\]

with an empty product equal to 1. For \(m=4\), this is

\[
M(k,n-k-4,2)=\frac1{n-3}\binom{n-3}k\binom{n-3}{k+1}.
\]

For \(k=2\), \(n=6,7,8,9\) give \(1,6,20,50\). These counts alone certify no tiling and prove no infinite family.

## BCFW terminology

**SOURCE-VERIFIED.** The modern **general BCFW cells** are the recursive class generated from rank-zero cells by cyclic shift, reflection, insertion of a zero column, and the BCFW product. The product glues two smaller plabic graphs with a prescribed butterfly graph and raises the rank by one: \(k=k_L+k_R+1\). The indices satisfy the adjacency conditions in the source, so an arbitrary graph gluing is not a BCFW product. A **BCFW tile** is the image of a BCFW cell; proved injectivity holds for every positive \(Z\). [Companion Definitions 2.10–2.17, pp.4–6](../literature/m4_spurion_tiles.pdf); [supplied main BCFW paper §§6–8](../literature/m4_BCFW_tilings.pdf).

**SOURCE-VERIFIED.** A **BCFW tiling** is a collection obtained by iterating the tiling recurrence of the supplied main paper Definition 13.2, proved to tile for every positive Z by Theorem 13.3. A tiling consisting entirely of BCFW tiles need not itself be a BCFW tiling: the companion §5, p.29, explicitly makes this distinction. The **standard BCFW cells** use the standard recursion without rotations/reflections or arbitrary zero insertion: zero insertion is at the penultimate position, with the standard product recursion. They have the noncrossing chord-diagram description (supplied main Definitions 7.7 and 7.12). Their images comprise the **standard BCFW tiling**. In companion Definition 2.15 the recursive clauses shorten the name to “BCFW”; read them in the standard subclass context, using the chord description to disambiguate. The KWZ “BCFW cells” refer to their fixed recursive collection, not automatically the larger modern class. [Companion §2.3 and §3](../literature/m4_spurion_tiles.pdf); [main §§7,13](../literature/m4_BCFW_tilings.pdf); [KWZ §§5–6](../literature/KWZ_decompositions_amplituhedra.pdf).

**SOURCE-VERIFIED (version crosswalk).** The supplied main BCFW PDF is an expanded version whose tilings section is §13. The companion cites an earlier main-paper version as [ELP+23, §12], with Theorems 12.3/12.6 corresponding to the supplied version's Theorems 13.3/13.6. Direct citations to the local main PDF must use its own numbering.

## Twistor coordinates, functionaries, and facets

**SOURCE-VERIFIED.** If \(Y\in\mathrm{Gr}_{k,k+m}\) has representative rows \(y_1,\ldots,y_k\), then

\[
\langle\!\langle Yi_1\cdots i_m\rangle\!\rangle
=\det(y_1,\ldots,y_k,Z_{i_1},\ldots,Z_{i_m}).
\]

The coordinates are antisymmetric in the external indices and defined up to a common scale from the representative of \(Y\). They arise by pullback of Plücker coordinates on \(\mathrm{Gr}_{m,n}\). A **functionary** is a homogeneous polynomial in twistor coordinates. Its **definite sign on a cell image** in the companion Definition 2.9 means the sign is constant for every point of that open image and every positive \(Z\), with compatible orientation conventions. Cluster variables on \(\mathrm{Gr}_{4,n}\) give some such functionaries; a cluster variable and its pullback at fixed \(Z\) should be distinguished. [Companion Definitions 2.8–2.9, p.4](../literature/m4_spurion_tiles.pdf).

**SOURCE-VERIFIED.** A cell facet \(S'\) has \(S'\subset\partial S\) and \(\dim S'=\dim S-1\). It gives a tile facet only if \(Z_{S'}\subset\partial Z_S\) and its image has codimension one. A source facet can collapse and a functionary vanishing on a source boundary need not cut out a tile facet. Standard BCFW tile facets are classified by the frozen variables of their tile cluster algebra (companion Theorem 4.1); the general BCFW analogue is stated as Claim 4.25 with its proof omitted. These results are not a facet classification for arbitrary tiles. The spurion has nine quadratic facet functionaries (§5.3), so restricting arbitrary facets to linear twistor minors is false.

## Canonical forms and the precise unproved step

**SOURCE-VERIFIED.** A positive geometry consists of an oriented real semialgebraic region in a complex projective variety with a unique rational top form having simple poles on its algebraic boundary components and recursively normalized residues. Positroid cell closures in their positroid varieties are positive geometries. The canonical form is \(\bigwedge_i d\log t_i\) in appropriate positive network coordinates, with orientation fixed. The assertion is not that every arbitrary positive coordinate change preserves a dlog volume form. [Companion Definition 7.1 and Theorem 7.8, pp.37–39](../literature/m4_spurion_tiles.pdf).

**SOURCE-VERIFIED (definition), CONJECTURAL (general positive-geometry/additivity claim).** For a tile, the companion Definition 7.10 defines its **candidate canonical form**

\[
\widetilde\Omega(Z_S)=(\widetilde Z|_S^{-1})^*\Omega(S).
\]

The source distinguishes this from proving the tile is a positive geometry with that rational canonical form (Conjecture 7.11), proving the amplituhedron is a positive geometry (Conjecture 7.9), and proving the sum over any tiling is its canonical form and is tiling-independent (Conjecture 7.12). For BCFW tiles, Proposition 7.14 gives an explicit wedge of four dlog coordinate-functionary ratios per bridge; this computes the candidate form and does not by itself resolve those arbitrary-tile conjectures. Any literature update superseding these conjectures must be stated separately with its hypotheses.

## Parity and T-duality

**SOURCE-VERIFIED.** Put \(\ell=n-k-m\). Galashin–Lam Theorem 3.5 preserves all-Z admissibility, disjointness, and arbitrary all-Z tilings under parity for even \(m\). Their affine index is \(f\) of average shift zero: the actual bounded cell index is \(b=k+f\), and the dual bounded index is \(\ell+f^{-1}\). Thus parity preserves the number of cells and exchanges \(k,\ell\). It is not naive inversion of \(b\), nor a stated fixed-fiber map for arbitrary chosen \(Z,Z'\). Their Conjecture 3.8 separates fixed-Z from all-Z claims. [Galashin–Lam, pp.4–6](https://www.math.ucla.edu/~galashin/papers/duality.pdf). Parity gives no interchange with \(m/2\); MacMahon's numerical symmetry alone supplies no such geometric theorem.

**SOURCE-VERIFIED.** For \(m=2\), T-duality relates rank \(k+1\) hypersimplex tiles to rank \(k\) amplituhedron tiles through their common bicolored-subdivision labels. The precise tiling theorem is

\[
\{\Gamma_\sigma\}_{\sigma\in\mathcal C}\text{ tiles }\Delta_{k+1,n}
\quad\Longleftrightarrow\quad
\{Z_\sigma\}_{\sigma\in\mathcal C}\text{ is an all-Z tiling of }\mathcal A_{n,k,2}.
\]

This is a combinatorial correspondence between tilings of spaces of generally different dimensions, not a homeomorphism of those spaces. It is not parity duality and is not an established \(m=4\) correspondence. [PSBTW Theorems 2.12,2.20,2.22, pp.8–10](../literature/magic_number_m2.pdf).
