# Run 2 targeted prior-art check

Date: 2026-09-05. This supplements, without restarting or replacing, the
first-run audit. Search outcomes are not novelty certificates.

Queries used: `amplituhedron rank two tile classification 176 939 spurion flip
positive fibers`; `amplituhedron balanced flips nearly admissible Galashin
Lam Conjecture 13.10`; `amplituhedron positroid subdivision linear fibers
Baues nine dimensional`.

**SOURCE-VERIFIED.** [Galashin--Lam, §13.4](https://www.math.ucla.edu/~galashin/papers/duality.pdf)
already formulates balanced nearly-admissible-parent flips (Conjecture
13.10) separately from connectivity (13.11). Example 13.12 explicitly
excludes the four-mass cell from admissibility, describes its degree-two
contribution alongside eight degree-one boundaries, and warns that the
resulting form expression is not a triangulation. This is precisely the
odd-boundary/multiplicity trap retained in Run 2. Local source incidences
do not prove either conjecture.

**SOURCE-VERIFIED.** [Mohammadi--Monin--Parisi, *Triangulations and Canonical
Forms of Amplituhedra: a fiber-based approach beyond polytopes*](https://arxiv.org/abs/2010.07254)
develops a birational fiber parametrization and secondary amplituhedra for
the conjugate-to-polytope case `n-k-1=m`. The abstract explicitly restricts
its projective-space/hyperplane-arrangement application to that case.
This is direct prior art for investigating fibers, and includes the n7
ambient setting here. The present n9 result concerns a particular
nine-dimensional source parent. We do not import a theorem about all of
its fibers or all parent relations from that abstract. No novelty is
claimed for the fiber approach or the corrected intended spurion flip.

**SOURCE-VERIFIED.** The [published spurion paper, §5](https://link.springer.com/article/10.1007/s11005-024-01854-4)
already gives the individual spurion tile's injectivity and its two cyclic
translates, and describes a non-BCFW five-for-five replacement. Run 2 uses
its individual tile theorem. The separate parent correction is not
silently assigned to the printed proof.

**SOURCE-VERIFIED / COMPUTATIONALLY-VERIFIED.** The supplied main BCFW v3
Table 1 lists 176 and 939 general BCFW tiles for n8 and n9. The source-matrix
recipe implementation reproduces those counts; they are not new
enumerations claimed without attribution. The all-Z source classification
in Run 2 additionally supplies an exhaustive partition of our source
universe using existing injectivity/nonadmissibility theorems and an
elementary image-dimension bound. It is not presented as a literature-first
classification.

**FAILED (unjustified transfer).** The search also returns m2 positroid
subdivision and tropical results. Neither gives an m4 chamber completeness,
unit-weight, or flip generation theorem. No such statement is used.

Retrieval limit: the BCFW v3 web fetch returned a cache miss, and the old
fiber paper's experimental arXiv HTML returned 404. BCFW claims were checked
against the supplied full local v3 PDF, not inferred from the failed web
fetch. Only the fiber paper's accessible abstract-level scope is reported
above. This bounded check makes no claim to exhaust every equivalent
result, and reaches September 5 rather than the rest of September 2026.
