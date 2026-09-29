# Independent audit of the n8 complete indicator certificate

**Review conclusion: PASS.** This branch independently checked the complete hyperplane/source inverse, closed-preimage exclusions, signed cyclic/loop transport, open-neighborhood argument, and exact rank certificate. The tests do not import the indicator-producing module. No unclassified tile or omitted positive branch was found under the stated hypotheses.

The conclusion concerns the complete 176-tile all-\(Z\) universe at \(k=2,m=4,n=8\), using its preserved complete source admissibility classification. It is not an arbitrary-\(n\) generation theorem.

## The full inverse and its gauge

Every one of the 176 tile sources has a parallel class \(D\) with exactly five complementary nonloop labels. Write their successive classes after a cyclic cut as \(A_1,\ldots,A_\ell,D\), put \(r=|D|\), and let \(q\) be the nonloop count. Source dimension eight gives

\[
q+s=12,\qquad \ell+r=6.
\]

The ordered signed external rows after the cut are positive: the source rank two and external rank six both use a minus sign for labels crossing the cyclic cut. Their matrix product is unchanged after the corresponding source-column transformation. Zero columns are simply omitted. This is exact all-\(Z\) transport, not an assumption that unsigned rotations preserve every external minor.

For a source point in this chart, the first row kills the \(D\) direction and has strictly positive coefficients \(a_i\) on the five complementary labels. Let their external span be \(H\). The image of the second row has strictly positive value under the hyperplane functional

\[
\ell_H(X)=\det(E_1,\ldots,E_5,X).
\]

Consequently \(Y\cap H\) is exactly the first-row line, recovering all five \(a_i\) up to a common positive scale. If its five coefficients have mixed strict signs, neither orientation of this line can arise from a nonnegative source in the valid chart.

When the recovered \(a_i\) are positive, select any second image row \(S\in Y\) with \(\ell_H(S)>0\). Any other nonnegative source preimage can be put into this exact image basis: its second image is \(\alpha S+\beta R\), where applying \(\ell_H\) forces \(\alpha>0\). Dividing by \(\alpha\) and subtracting \((\beta/\alpha)R\) preserves source positivity, slope order, and the source cell/closure. This rules out the missing negative branch.

Compress each complementary class to \(V_j=\sum_{i\in A_j}a_iE_i\). The ordered matrix with rows \(V_1,\ldots,V_\ell,E_{D_1},\ldots,E_{D_r}\) has six rows and positive determinant by termwise expansion in positive ordered maximal minors. Solving its six ambient equations gives the unique slopes \(t_j\) and distinguished-class coefficients \(d_j\). The five inequalities are

\[
t_{j+1}-t_j>0\quad(1\le j<\ell),\qquad d_j>0\quad(1\le j\le r).
\]

These are necessary and sufficient for the open tile source. Their weak versions give all valid-chart closed preimages. The exact fixed-image gauge and invertible compressed system prove completeness; the solve is not merely a Jacobian or generic-degree calculation.

## Why no closed preimage escapes the chart at a witness

The source closure retains original zero minors and zero columns. Rank-two closure strata only delete columns and merge adjacent parallel classes. The following chart failures are all excluded when every four-label twistor of \(Y\) is nonzero.

1. If the whole \(D\) block disappears, the image plane lies in the span of the five complementary rows. It then meets every four-row subspace of that five-space, forcing a zero four-label twistor.
2. If any complementary column disappears while \(D\) survives, there are at most four nonloop labels outside the \(D\) class. A nonzero source row killing \(D\) maps to a nonzero vector supported on those labels. Positive external data preserves rank, so this forces a zero four-label twistor.
3. If \(D\) merges with any complementary class, the enlarged class also has at most four complementary labels. The same nonzero-vector argument applies.

Partial deletion within \(D\), and mergers among complementary classes, are **not** silently excluded. They remain in the recovered chart as \(d_j=0\) or successive slope differences equal to zero. Each saved inverse has all five quantities strictly nonzero. Thus none of these remaining lower source strata occurs at the witnesses.

These cases exhaust possible closed-source preimages through the cyclic parallel-class closure classification. In particular, a negative inverse inequality certifies nonmembership in the **closed** tile, not just failure of one attempted open parametrization.

## Open neighborhoods and evaluation of indicators

At every saved target, all hyperplane pivots are nonzero, every recovered complementary coefficient is nonzero, all 70 four-label twistors are nonzero, and every computed source inequality is strictly nonzero. The relevant recovered lines and inverse coefficients depend rationally on the target in these charts. For the mixed-sign case, the strict sign mixture persists; for the solved case, its inequality signs persist.

It follows that each complete tile-membership decision is constant on an open target neighborhood. Intersecting the finitely many neighborhoods gives one open set on which the entire 176-entry indicator row is constant. Thus evaluation of a relation modulo sets of dimension below eight is legitimate: its exceptional set cannot contain that open set. This is stronger than a table of values at finitely many possibly exceptional points.

## Independent finite checks

**COMPUTATIONALLY-VERIFIED.** Four new tests in tests/test_run5_indicators_independent.py pass in **9.10 seconds**:

- Each tile's eligible class and cyclic signs are reconstructed independently. Every ordered six-row signed-permutation character is positive, establishing the universal transport sign rather than checking only sampled determinants.
- All \(103\times70=7{,}210\) target twistors are checked by an exterior/Laplace expansion, independently of the producer's projection matrices.
- All \(103\times176=18{,}128\) memberships are recomputed. The second implementation uses a full six-row external frame, then a SymPy solve of the ambient source-coefficient equations. It verifies the recovered image by an exact invertible row change and decides positivity using every ordered two-minor of the original source matrix. All 12,718 mixed-sign exclusions and 5,410 solved candidates agree with the saved indicators.
- The selected \(103\times103\) integer minor has exact determinant **2**, computed in characteristic zero. The entire \(103\times176\) indicator matrix annihilates the transpose of the full \(96\times176\) local relation matrix.

The tests do not import the producer's hyperplane formula, Fraction inverse/solve, twistor projection, or modular echelon code. The source-minor check is separate from its five-inequality membership predicate.

## The resulting exact linear-algebra implication

Let \(R\) be the certified indicator matrix and \(L_8\) the full local relation span. The independently checked ranks give

\[
\operatorname{rank}R=103,\qquad \dim L_8=73,\qquad
R L_8^{\mathsf T}=0,\qquad 103+73=176.
\]

Hence \(\ker R=L_8\). Every indicator relation at this particular positive \(Z_0\) must annihilate all certified open rows, while every local row is already an all-\(Z\) geometric relation. Therefore

\[
L_8\subseteq\ker\Phi_{Z_0}\subseteq\ker R=L_8,
\qquad
\ker\Phi_{\mathrm{all}}=L_8.
\]

This proves the complete constant-coefficient all-\(Z\) indicator-kernel equality at \(n=8\), and equality at the displayed fixed \(Z_0\). It does not assert the same kernel dimension at every other fixed \(Z\).

Any two complete all-\(Z\) tilings at \(n=8\) use the classified tile universe, so their difference lies in this kernel and is balanced. Comparison with the source-certified standard 20-tile BCFW collection then gives 20 tiles in every such tiling. This is the finite \(n=8\) consequence of the exact certificate; it is not the all-\(n\), \(k=2\) Magic Number theorem, nor a construction of legal flip paths.

## Independent audit of the genuine-tiling span

**PROVED, independently reviewed.** The proof and implementation accompanying N8_FLIP_SPAN.md pass a separate bounded read. The induction through a retained local replacement is geometric: the two sides have equal closed unions and each side has disjoint open images for all \(Z\). Any new open tile overlapping an unchanged open tile would meet the dense union of the old side's open images and contradict the old complete tiling. The set checks ensure that every removed tile is present and no added tile was already present.

Every retained nonroot node references an earlier retained parent, so the 153-node ancestral tree proves all 74 selected collections are complete all-\(Z\) tilings, beginning with the independently certified standard collection. The saved differences are integer sums of local rows. Their exact rank-73 minor, together with the independently established \(\dim L_8=73\), gives a difference span equal to \(L_8\). Hence \(L_8\subseteq D_8\). Combined with the complete indicator-kernel result above, \(D_8=L_8\).

The search need not exhaust its component to prove this inclusion; it needs only the saved all-\(Z\) tiling paths and a full-rank spanning certificate. Its stopping counts do not classify all tilings or prove connectivity of the whole tiling graph. No additional test run was needed for this proof/scope audit.

## Independent audit of the complete binary model

**PROVED, independently reviewed.** Let \(A\) be the certified \(103\times176\) indicator matrix, and let \(\chi_0\) be a standard complete tiling incidence vector. Then the complete all-\(Z\) tilings in this tile universe are exactly

\[
\{\chi\in\{0,1\}^{176}:A\chi=\mathbf1_{103}\}.
\]

Necessity follows from the simultaneous open-neighborhood membership certificates and multiplicity-one coverage. For sufficiency, \(A\chi=A\chi_0\) implies

\[
\chi-\chi_0\in\ker A=L_8.
\]

Every local row is an all-\(Z\) indicator identity, so the selected tile indicators sum to the amplituhedron indicator modulo dimension below eight for every positive \(Z\). Two selected open tile images cannot overlap: their nonempty intersection would be ambient open and the sum of the nonnegative selected indicators there would be at least two, contradicting that identity off a lower-dimensional exceptional set.

For coverage, the selected closed union contains the dense generic part of every open tile in the known BCFW tiling. It is closed because it is a finite union of compact source-cell images. Therefore it contains the closure of the BCFW open union, which is the entire amplituhedron. Conversely every selected tile is contained in the amplituhedron. Thus the selected collection is a complete multiplicity-one all-\(Z\) tiling.

This sufficiency argument uses the proved equality \(\ker A=L_8\); an arbitrary finite sampled indicator matrix would not support it. The result is a complete exact-cover model. It does not claim that its binary solutions have been exhaustively enumerated, nor that all solutions lie in the explored flip component.
