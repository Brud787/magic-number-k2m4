# Run 2: exact k=2,m=4 relations

Bounded checkpoint, 2026-09-05. The relation space uses semialgebraic tile
indicators modulo subsets of dimension less than eight, separately for
each positive external Z. Every certified relation below holds for all Z.
Closed-union equality and disjoint open images are proved separately;
pointwise equality of sums of **closed** indicators at shared boundaries is
not asserted.

## Independently certified non-BCFW relation

**PROVED.** For the nine-dimensional parent

\[
P=(91)(2)(345)(678),\qquad
f_P=(3,6,4,5,9,7,8,11,10),
\]

the following is a local, multiplicity-one, all-Z tile relation:

\[
[T_{28}]+[T_{34}]+[T_{35}]+[T_{39}]+[T_{45}]
=[B_1]+[B_2]+[B_3]+[B_4]+[B_5].
\]

Here T_j denotes the exact cell on row j of the published Appendix table;
B_i denotes the separately printed five additional BCFW cells. T28 is the
published spurion. The other nine terms have independent BCFW recipe or
direct inversion certificates. All ten terms are admissible for every
positive Z. Their signed coefficient sum is `5-5=0`.

This uses the **separate repaired parent** and rows39,45. It does not
substitute those data into the literal printed fixture. The printed parent
and rows38,46 remain a failed common-parent reconstruction. It is still
conjectural that our corrections express the authors' intended text.

The complete [geometric proof](run2/SPURION_ATTEMPT.md) and
[independent hostile review](run2/SPURION_REVIEW.md) explain the certificate.
After rotating P to `(12)(3)(456)(789)`, normalize three parallel-class
directions. Ten homogeneous positive coefficients give the source matrix

\[
C(x)=\begin{pmatrix}
a_1&a_2&u+v&c_4&c_5&c_6&0&0&0\\
0&0&v&c_4&c_5&c_6&d_7&d_8&d_9
\end{pmatrix}.
\]

The condition `rowspan(C(x)Z)=Y` is an exact eight-equation homogeneous
linear system. Positive determinant expansions prove rank eight and an
invertible projection of its kernel onto `(a1,a2)`, throughout the parent
and the ten selected open walls. Hence the positive projective fiber is
an interval. Wall injectivity proves transversality. Connectedness and
nonvanishing make the endpoint sign constant on each wall for all Z.
An exact rational evaluation then proves the signs, in displayed variable
order, are

`(+,-,+,+,-,+,-,-,+,-)`.

Bounds on the images of simultaneous-wall and rank-one degenerations
exclude a full-dimensional exceptional set. Generic interval endpoints
give one positive and one negative tile. Openness extends disjointness to
the entire open tiles; closure gives equality of the two closed covered
regions. This is certification **Level A**, with a linear description of
each fiber and its inequalities. It uses no conjectural canonical-form
additivity.

The result is one non-BCFW relation prototype, with its dihedral copies.
Embedding this repaired region into the literal fifty-tile Appendix
collection is not certified. No new complete non-BCFW tiling is claimed.

## Other exact relations and source universe

**PROVED / SOURCE-VERIFIED.** Subtracting two known all-Z standard BCFW
tilings and cancelling their common cells gives exact geometric relations.
Seven n7 differences are local `3<->3` moves, one per nine-dimensional
parent. Increasing zero insertion gives 56 n8 local moves. The full
standard-dihedral orbit differences give 21 n7 and 120 n8 rows; the seven
n7 local moves are included in the 21. See [BCFW certificates](run2/BCFW_RELATIONS.md).
These relations are balanced by construction from equally sized BCFW
collections. They cannot serve as an unbiased test of universal
balancedness.

**COMPUTATIONALLY-VERIFIED.** Exact source enumeration and independent
bounded-affine/basis incidence give:

| n | Nine-dimensional parents | Eight-dimensional source incidences | Dihedral parent orbits |
|---:|---:|---:|---:|
| 7 | 7 | 56 | 1 |
| 8 | 112 | 1,016 | 9 |
| 9 | 882 | 8,577 | 57 |

Every parent and child retains its affine permutation, necklace, bases,
zero minors and incidence witnesses. Candidate *cellular boundary*
orientation signs remain null where not derived. Certified image signs
are stored separately. This run has not built a general oriented source
chain differential, and does not call its unsigned facet lists relations.

**PROVED / SOURCE-VERIFIED / COMPUTATIONALLY-VERIFIED.** Source certificates
give complete all-Z admissibility classifications of the dim8 source labels
at n8 and n9: `176 tiles + 90 non-tiles`, and
`939 BCFW + 3 spurion tiles + 612 non-tiles`, respectively. The non-tile
proofs use the class-complement Schubert dimension bound and explicit
four-mass nonadmissibility, with a proved positive-row extension for loop
insertions. They do not infer global injectivity from differential rank.
See [parent catalog and proof scope](run2/PARENT_ENUMERATION.md).

## Counterexample search and exact linear algebra

**COMPUTATIONALLY-VERIFIED.** Every certified row currently has coefficient
sum zero. No unbalanced **certified** indicator relation was found. No
exhaustive search of the full indicator kernel, all semialgebraic chambers,
or all source-parent signed image relations has been completed.

**FAILED (specific proposed shortcut).** The enumeration finds parents with
nine surviving full-dimensional source boundaries, one of them four-mass,
and parents with eleven surviving boundaries, three of them four-mass.
These are deliberately retained as asymmetric/multiplicity test cases.
Counting them as tiles, or deleting the nonadmissible terms from a form
identity, supplies no image equality. Thus none is a certified unbalanced
relation. This reproduces the warning in Galashin--Lam Example 13.12.

**COMPUTATIONALLY-VERIFIED with a PROVED linear-algebra implication.** At n8,
the 56 seven-support local rows have rank48; differences of the 16 standard
dihedral tilings have rank15; their combined rank is63. These two spans
intersect only at zero. Therefore the chosen 56 moves cannot connect any
two distinct tilings in that orbit, even with arbitrary intermediate
collections. This kills the proposed sufficiency of **that move set**.
It says nothing against connectivity using all geometric flips.

The combined n8 rows involve 168 tiles and leave a quotient of dimension105.
Including all 176 certified source tiles leaves dimension113. Thus these
constraints do not determine a unique linear weight. The all-ones
covector annihilates the recorded relation span. None of these quotient
dimensions is the dimension of the true tile-indicator quotient.

The machine-readable [relation catalog](../results/relation_catalog.json)
contains signed terms, certification level, all-Z scope, coefficient sum,
BCFW content, source origin, symmetry action and proof/fixture references.
It sorts unbalanced rows first, then non-BCFW involvement, support and n.
Printed, repaired-candidate and certified fixtures are separate objects.
Exact integer/rational matrices and ranks are in
`results/run2/certified_relation_linear_algebra.json`.

**COMPUTATIONALLY-VERIFIED.** There are215 catalog rows:21 n7,176 n8,18 n9.
The18 n9 dihedral copies involve156 tiles (153 BCFW and3 spurions) and have
rank18, leaving quotient dimension138 on those columns. All942 certified
n9 source tiles would leave dimension924 modulo these same rows. Thus the
spurion sector does not determine a unique functional either. The targeted
multiplicity screen records89 parents in
`results/run2/unbalanced_search.json`.

Uniqueness convention: relation equations alone allow many linear weight
assignments. If a functional is additionally required to equal one on
**every** generating tile, it is unique on their span whenever it exists.
The unsolved issue is whether that prescribed assignment descends through
all true indicator relations, not whether it admits several unit values.

## Ranked explanations and kill-tests

**FAILED (convex-fiber-only balancedness).** A concrete counterexample to
that general implication is the triangle `x1+x2+x3=1`, `xi>=0`, projected
by `y=x2+2*x3`. Its positive fibers are intervals. The three open edges
map injectively to `(0,1)`, `(1,2)` and `(0,2)`, yielding
`[(0,2)]-[(0,1)]-[(1,2)]=0` modulo zero-dimensional sets, with coefficient
sum `-1`. The exact chamber rows are `(1,1,0)` and `(1,0,1)`, with kernel
vector `(1,-1,-1)`. This is **outside the k2,m4 tile universe** and is not
a Magic Number counterexample. It proves why an additional m4-specific
sign-count constraint is required beyond interval endpoint geometry.

1. **PROVED for the spurion prototype; CONJECTURAL as a broader mechanism:
   oriented positive fibers.** A faithful source chart with linear fiber
   constraints, compact projective interval fibers, admissible transverse
   walls and controlled lower strata yields a signed image relation.
   Positive determinant expansions make wall signs all-Z. The unresolved
   additional property is an equal number of positive and negative wall
   types. Convexity alone does not imply this. **Kill-test:** find an
   admissible parent with all hypotheses and unequal endpoint-sign counts.
   That would give an unbalanced local decomposition, still requiring a
   complete-tiling extension to contradict Magic Number. Multiple parallel
   columns in the fourth unfixed direction introduce proportionality
   equations; disconnected or branched fibers kill this linear model's
   direct extension. Profile `(2,2,2,3)` is a concrete test.

2. **CONJECTURAL: degree and oriented incidence constraints on admissible
   parent relations.** A relation complex retaining image degrees and
   collapsed/internal strata might explain why the remaining signed
   degree-one walls balance. GL's nearly-admissible hypothesis is relevant
   prior art, not a proved answer. **Kill-test:** compute a parent with
   mixed degree-one/degree-two boundaries exactly; show that eliminating
   multiplicities either produces a genuine unequal-size tile relation or
   fails to preserve the image identity. Ordinary source boundary signs
   alone are not the desired coefficients.

3. **CONJECTURAL: a common refinement with a unit functional.** The now
   classified n8 source universe permits a finite exact relation problem.
   A realizable, complete semialgebraic chamber refinement could test the
   full indicator kernel, including coefficients beyond ±1. **Kill-test:**
   an exact kernel vector with nonzero coefficient sum immediately kills
   the unit functional on that universe. A sampled chamber matrix cannot
   certify its absence. A uniqueness claim is already killed for the
   present recorded relation constraints by their large quotient dimension.

**PROVED limited consequence.** Any linear weight respecting the repaired
relation and assigning one to its nine BCFW tiles must assign one to its
spurion: `w(spurion)+4=5`. Cyclic transport gives this for each of the three
n9 spurions. This does not construct such a weight on the true relation
space; unknown BCFW-only or mixed relations can still obstruct it.

## Stop boundary

This run reaches **SUCCESS A**: an independently certified non-BCFW local
relation. Dihedral copies do not count as independent structural
mechanisms. No general parent balancedness theorem, no generation theorem,
no arbitrary complete-tiling cardinality theorem, and no Magic Number
counterexample is claimed. The next unresolved task is exact larger-support
parent geometry, rather than an exhaustive complete-tiling search.

The [targeted prior-art check](run2/LITERATURE_DELTA.md) records overlapping
fiber/Baues work and its scope. No novelty claim rests on negative searches.

---

## Run 3: independent sign mechanisms and hostile fibers

**PROVED.** The repaired spurion's sign count is now symbolic:
`(1−1)+(1+1)+(−1+1−1)+(−1+1−1)=0`. The four groups are the pivot pair,
split singleton, and two three-element classes. A positive Plucker-ratio
identity controls the spurion wall. The proof and its all-Z/admissibility
dependencies are in [SPURION_SIGN_MECHANISM](run3/SPURION_SIGN_MECHANISM.md).

**PROVED.** The new n8 parent `(12)(3)(45)(6)(78)` has ten admissible BCFW
walls in an all-Z 5↔5 relation. Reflection reverses parent orientation,
preserves target orientation and pairs wall signs oppositely. The complete
two-class nine-dimensional sector has only the full-dimensional (5,6)
profile and an all-Z 3↔3 relation with alternating Cramer signs. See
[LARGER_SUPPORT](run3/LARGER_SUPPORT.md), [SIGN_FORMULA](run3/SIGN_FORMULA.md),
and [TWO_CLASS_THEOREM](run3/TWO_CLASS_THEOREM.md). These are geometric local
relations, with injectivity, endpoint completeness and closed coverage.

**COMPUTATIONALLY-VERIFIED.** The separate
[Run3 sign inventory](../results/run3/sign_counts.json) records every parent
through n9, plus the (5,6) prototype. Its 414 certified rows have zero
coefficient sum: four mechanisms with their transports, not 414 mechanisms.
472 unresolved and 116 collapsed parents retain null coefficient sums.
The original `results/relation_catalog.json` is unchanged. No complete
indicator-kernel or relation-generation calculation is inferred from this
inventory; the prior failed seven-support generation claim is preserved.

**PROVED (hostile fixed-Z results).** An adjacent-singleton n8 parent has
two positive fiber intervals. The n9 (2,2,2,3) parent has a conic model and
0,1,2 positive four-mass preimages at three exact target planes. Its two
positive four-mass sheets have opposite local orientations. An exact open
part of this parent image misses every admissible closed source-facet
tile. [MULTIPLICITY](run3/MULTIPLICITY.md) audits the complete source closure
and records precisely why a cover using those facets is impossible.

**FAILED:** the rule “remove the nonadmissible walls and obtain a tile
decomposition of every parent.” **CONJECTURAL:** a correct replacement
mechanism for curved/disconnected fibers, general local balancedness, and
sufficient generation. No unbalanced admissible relation was certified.
The degree-one triangle still shows why pointwise endpoint cancellation
does not imply a constant coefficient sum over wall types.


---

## Run 4 — complete single-parent all-Z relation spaces

**PROVED.** The 29 loopless nine-dimensional rank-two parent cores now
have complete constant-coefficient all-Z facet-indicator kernels:
12 empty admissible-facet sets, 10 balanced six-facet one-dimensional
spans, 5 balanced ten-facet one-dimensional spans, and 2 zero kernels on
eight admissible facets. Exact loop/dihedral transport extends the theorem
to every n. Every relation supported on the admissible source facets of
one parent is balanced, with arbitrary real constant coefficients allowed.

This strengthens existence of balanced examples. Symbolic K3,3 overlaps
prove the entire circuit kernel at every positive Z; exact spanning trees
and already proved side decompositions determine the five ten-wall all-Z
kernels; exact open-neighborhood indicator matrices exclude every nonzero
all-Z relation for the two hostile facet sets. No complete chamber
list is assumed. Each finite witness supplies a rigorously necessary
relation equation on a nonempty open region.

**PROVED.** A nontrivial multiplicity-one all-Z replacement using only
one parent's admissible facets is its canonical 3↔3 or 5↔5 replacement,
up to reversing sides. Unrestricted overlapping covers and relations
involving extra tiles are outside this claim.

The old 215-row catalog and its interpretation remain unchanged. New
prototype records, exact source relabelings and complete kernel proofs
are in [sign_relations.json](../results/run4/sign_relations.json) and
[LOCAL_PARENT_THEOREM](run4/LOCAL_PARENT_THEOREM.md). **CONJECTURAL:** these
local relations generate arbitrary complete-tiling differences. Run4
stops at the reviewed local theorem and does not pursue generation.


---

## Run 5 — complete finite global relation spans

**PROVED.** At n7 the complete-tiling difference span equals the full
single-parent span: D7=L7, rank6. At n8 the full constant-coefficient
all-Z indicator kernel is exactly the parent span: K8=L8, rank73.
Seventy-four certified complete tilings give the reverse containment
L8⊆D8; hence D8=L8. Every relation in these spaces is balanced.
The full n8 matrix has96 rows, including56 seven-support and40 eight-
support rows. The old restricted-span failure is preserved; it does not
apply to this full matrix.

An exact103×176 matrix of simultaneous open indicator neighborhoods has
rank103 and kernelL8. Membership includes every admissible source label
and excludes all closed-source preimages in the zero entries. Thus the
kernel proof is not a sampled chamber guess. Exact ranks and integer
local decompositions are in [generation_ranks.json](../results/run5/generation_ranks.json)
and [LOCAL_SPAN](run5/LOCAL_SPAN.md). The original215-row catalog is unchanged.

**CONJECTURAL.** D_n⊆L_n for all n≥9. Neither local support bounded by11,
nor finite equality at n8, supplies a global generation theorem.
[N8_INDICATOR_THEOREM](run5/N8_INDICATOR_THEOREM.md) and
[GENERATION](run5/GENERATION.md) state the precise proved scope and next kill-tests.
