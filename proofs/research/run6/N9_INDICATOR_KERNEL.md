# The complete n9 indicator kernel

**PROVED, independently audited.** The full inverse, closed-nonmembership,
all witness entries and exact rank certificates passed separate checks.
See [the independent review](INDICATOR_INDEPENDENT_REVIEW.md).
It concerns k=2,m=4,n=9 and constant coefficients independent of Z.

## Statement and inputs

Let U9 be the complete 942-label all-Z admissible tile universe, V9 its
free real span, and L9 the span of every transported Run4 single-parent
relation. Let K_Z be the kernel of tile indicators at Z modulo
semialgebraic sets of dimension at most seven, and K_all the intersection
of these kernels over all positive external Z. Then

\[
 K_{Z_0}=K_{\rm all}=L_9,\qquad \dim L_9=470,
 \quad Z_{0,i}=(1,i,i^2,i^3,i^4,i^5),\ i=1,\ldots,9.
\]

This implies D9⊆L9 and cardinality fifty for every complete all-Z n9
tiling. The assertion at a fixed Z is confined to this displayed Z0;
equality at every other fixed positive Z is not asserted. L9⊆D9 needs
the separate genuine-tiling witness in [N9_GENERATION](N9_GENERATION.md).

The [universe](N9_TILE_UNIVERSE.md) includes all 939 general BCFW tiles
and all three spurions. The [full local span](N9_LOCAL_SPAN.md) has 693
geometric rows of rational rank 470, from all 882 source parents. The
parent relation proof is the preserved Run4 input. Source incidence,
canonical forms and algebraic degrees do not serve as image identities.

## Two complete inverse mechanisms

The 939 complement-five tiles use the proved Run5 inverse. Its argument
only needs dimension eight and a class with exactly five complementary
nonloop columns; it has no n8 restriction. Cyclic cut, hyperplane line
recovery, a positive six-row compressed matrix, and five strict slope/
coefficient inequalities supply the complete positive source inverse.
Nonzero four-brackets rule out all omitted closed-source charts, exactly
as in [the original proof](../run5/N8_INDICATOR_THEOREM.md).

The remaining three labels have profile (3,3,3). Their [three-direction
inverse](SPURION_INVERSION.md) normalizes the directions to horizontal,
diagonal and vertical. For fixed Y the nine homogeneous coefficients
satisfy an 8×9 linear kernel system. Rank eight gives a single rational
projective candidate; its coordinate signs decide positivity. Rank-
deficient systems cannot have a strictly positive kernel vector by
known all-Z source injectivity and the complete projective source chart.
No complex-degree inference or extra real sheet is involved.

For strict closed decisions, the three matrices [Y;Z_class] must have
full row rank five, all kernel coordinates must be nonzero, and the
fiber matrix must have rank eight. The class gates exclude each merger
and disappearing-direction branch. The remaining source closure lies
in the same nonnegative coordinate chart. Thus a mixed strict kernel
sign certifies absence from the closed tile, not just failure of one
normalization. The implementation checks the gates explicitly even
though global nonzero four-brackets imply them for the spurion.

For every retained witness all these inequalities and pivots are strict.
Their rational dependence on Y makes every membership decision constant
on an ambient open neighborhood. Intersecting the 942 neighborhoods
keeps one common nonempty open region for the full row. An exceptional
set of dimension at most seven cannot contain that region. Therefore
any actual indicator relation must annihilate each saved row.

## Exact witness and rank certificate

**COMPUTATIONALLY-VERIFIED.** The bounded construction used 921 rational
source seeds, rejected three as nongeneric, and retained 472 independent
rows. All source/target data, all 126 nonzero four-bracket residuals per
witness, all three complete spurion certificates, and the entire
472×942 indicator matrix A are saved in
[indicator_kernel_n9.json](../../results/run6/indicator_kernel_n9.json).
The complement-five decisions are reproducible from the saved exact
inputs; they are not left unspecified or assigned from sampled ranks.

There are 444,624 membership decisions: 360,154 strict mixed-hyperplane
exclusions, 83,054 complete six-row source solves, and 1,416 spurion
kernel decisions. The producer caches identical hyperplane recovery
across tiles but retains the unchanged Run5 gauge and inequalities.

Finite-field elimination was only the discovery screen. A separate
characteristic-zero calculation gives rank A=472 and exact determinant
**4** for the selected 472×472 integer minor. Independently, the local
matrix has rank470: an original470×470 minor has determinant−1 and a
stored integer RREF gives the matching upper bound. Exact sparse
multiplication checks A r=0 for every one of the693 local rows.

Consequently ker A=L9 as real or rational vector spaces. Geometric
meaning of the entries then gives the rigorous rank sandwich

\[
 L_9\subseteq K_{\rm all}\subseteq K_{Z_0}\subseteq\ker A=L_9.
\]

The first inclusion holds for every positive Z by Run4. The other bound
comes from necessary open indicator constraints at Z0. Matching ranks
prove completeness of the kernel without enumerating every chamber.
There is no upgrade of fixed-Z tilings to all-Z tilings in this argument.

## Cardinality and the binary model

**PROVED.** Every all-Z tiling vector chi satisfies
A chi=1. The exact rational weights in [UNIT_FUNCTIONAL](UNIT_FUNCTIONAL.md)
satisfy A^T lambda=1_942 and sum(lambda)=50. Thus

\[
 |\mathcal T|=\mathbf1^T\chi=\lambda^TA\chi=50
 =M(2,3,2)=\frac16\binom62\binom63.
\]

Conversely every binary solution A chi=1 is an all-Z tiling: subtract a
known standard tiling chi0, so chi−chi0∈ker A=L9. The all-Z indicator
identity implies multiplicity one off a lower-dimensional set.
Nonnegative binary coefficients preclude overlap of open images; any
such overlap would be ambient open. The finite selected closed union
contains a dense part of each open BCFW tile and is closed, so it covers
the entire amplituhedron. All selected tiles are admissible and lie
inside the amplituhedron. This is a complete exact-cover formulation,
not an exhaustive enumeration of its binary solutions.

## Scope of the architecture

The two inverse mechanisms extend to every n through the finite
[membership-core theorem](MEMBERSHIP_CORES.md). That supplies uniform
membership algorithms and closed decisions on their certified generic
open locus. The global rank sandwich still requires enough independent
rows at the n in question. Neither the finite inverse cores nor the
four determinant/rank numbers here prove that complementary rank is
always attained. The failed deletion map in [DELETION](DELETION.md)
identifies a specific gap in a naive induction.

No n10 global matrix, complete tiling enumeration, or long all-n proof
search was undertaken. The fixed-n theorem and all-n membership theorem
must remain separate in the final status.
