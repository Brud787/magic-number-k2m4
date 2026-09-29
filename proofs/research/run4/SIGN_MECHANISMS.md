# Local sign mechanisms and complete facet-relation spaces

This run keeps two assertions separate: a complete geometric decomposition
of the parent image, and the space of all constant-coefficient relations
on that parent's admissible facets. The latter needs a further argument;
one balanced relation does not by itself exclude a different unbalanced one.
The statements below concern k=2,m=4 only, unless explicitly noted.

## 1. Three mechanisms suffice for the fifteen balanced core types

**PROVED (independently audited).** Ten core types have a parallel class
with exactly five complementary nonloop labels. The unique positive
intersection ray Y∩span(Z_complement) fixes five coefficients. Compress
its successive parallel classes to positive block sums. These sums and
the distinguished-class external rows form a positive 7×6 matrix B.
Its Gale vector is

\[
w_i=(-1)^{i-1}\det B_{[7]\setminus i}.
\]

The entire positive fiber is affine. Its six actual inward inequalities
are the successive differences of complementary slopes and the distinguished
class coefficients. Their derivatives have the signs of w2,...,w7,
namely −,+,−,+,−,+. This simultaneously proves the sign count and retains
the merger walls. Direct hyperplane/affine inversion proves wall
admissibility; bounded interval endpoints prove image equality and
multiplicity one. See [SMALLER_CORES](SMALLER_CORES.md) and the independent
special treatment of the hidden merger in [MERGER_WALLS](MERGER_WALLS.md).

**PROVED (independently audited).** Four other core types have complete
linear positive-orthant fiber charts and genuine orientation-reversing
source reflections, intertwined with orientation-preserving target actions:

| Core | Parent representative | Paired admissible walls |
|---|---|---:|
| (1,2,1,2,2) | (12)(3)(45)(6)(78) | 5 pairs |
| (1,3,2,3) | (123)(4)(567)(89) | 5 pairs |
| (2,4,4) | (1,2,3,4)(5,6)(7,8,9,10) | 5 pairs |
| (3,3,4) | (1,2,3,4)(5,6,7)(8,9,10) | 5 pairs |

The globally nonzero pivots, submersions and transverse admissible walls
are proved before applying the tangent-orientation sequence. The source
coefficient permutation consists of five transpositions; the ambient
GL(6) action preserves Gr(2,6) orientation. Hence each pair has opposite
image-side coefficients. The (3,3,4) proof explicitly pairs its four
spurion facets in two pairs. These are actual source/external symmetries,
not inferred symmetry of source facet counts.

**PROVED (preserved Run3 theorem).** The remaining balanced core is the
asymmetric repaired spurion pattern (1,2,3,3). Its count is the symbolic
positive-minor/Plucker sum 0+2−1−1=0. It is not explained by the reflections
above. The literal printed-parent discrepancy remains preserved.

## 2. The common sign formula and its limits

**PROVED.** For a complete projective linear fiber with rank-eight matrix
M, choose ordered pivot indices p<q and normalized kernel basis K with
pivot rows I2. Let D_ij be the ordered complementary eight-minor. Then

\[
\det(K_i,K_j)=(-1)^{i+j-p-q}\frac{D_{ij}}{D_{pq}},\qquad i<j.
\]

With T=K(x_q,−x_p), at a positive coordinate wall x_i=0,

\[
\epsilon_i=\operatorname{sgn}\det(K_i,K_j)\quad(j\ne i),
\]

using antisymmetry if the indices are reversed. A positive pivot and
separate wall injectivity/transversality justify all-Z constancy. This
includes the spurion and all four reflection prototypes. The coordinate
indices and actual kernel pivot are retained in every fixture.

The complement-five chart is instead a fixed-image affine gauge. For a
wall function g_j its coefficient is sign(dg_j(w)); in particular a merger
has derivative w_(j+1)−w_j, not the sign of an omitted coordinate. The
q10 merger is finite and rank two at tau=0 in its adapted chart. Discarding
it produces a false 2↔3 count.

For arbitrary smooth source/image charts the shared orientation identity
is epsilon_W=−eta_W signJac(f|W), using outward-first boundary orientation.
This is an orientation identity, not a tile or relation certificate. It
does not turn source boundary signs alone into image signs. Four-mass
branches retain their separate real Jacobian signs; the positive count
can be 0,1,2. Their conic or quadratic-order geometry is not forced into
the linear orthant template.

## 3. A local overlap lemma

**PROVED, independently audited.** Suppose admissible open tile images
indexed by finite sets I+ and I− give two multiplicity-one decompositions
of the same closed parent region, with disjoint open images within each
side. Define a bipartite graph by joining i∈I+ to j∈I− when their open
images intersect nontrivially at the fixed external matrix under study.
If a constant-coefficient indicator relation holds modulo lower-dimensional
sets, each edge forces c_i+c_j=0.

Indeed the intersection is nonempty open, and same-side disjointness
excludes all other open tile images there. Closed/open indicator differences
are contained in finitely many lower-dimensional source-boundary images.
Deleting these and the relation's exceptional set leaves a nonempty part
of the intersection. Evaluation there gives precisely the stated equation.
If the graph is connected, all c_i are one common multiple of the
canonical vector epsilon=(+1 on I+,−1 on I−). Conversely that vector is
a relation by the already proved geometric decomposition. Therefore the
entire facet-indicator relation space is one-dimensional.

This graph is a graph of overlapping tiles within ONE parent, not a graph
of complete tilings. Its use establishes a local relation-space bound;
no generation/connectivity theorem for arbitrary tilings is invoked.

## 4. Every opposite pair overlaps in the circuit family

**PROVED, independently audited in [CIRCUIT_KERNEL_REVIEW](CIRCUIT_KERNEL_REVIEW.md).**
For each complement-five parent and every positive Z, the preceding
overlap graph is the complete graph K3,3.

Fix any five positive first-row coefficients a. This fixes B,w and the
six nonzero alternating inward derivatives l_h. The six source inequality
values u_h consist of successive slope differences followed by distinguished
class coefficients. They are freely assignable positive numbers: choose
the initial slope zero and take successive partial sums of its prescribed
differences. This sets the initial source representative, not the initial
slope along its subsequent fixed-image fiber.

For any i with l_i>0 and j with l_j<0, choose

\[
u_i=l_i,\qquad u_j=-l_j,\qquad u_h=2|l_h|\ (h\ne i,j).
\]

The complete positive fiber has inequalities u_h+tau*l_h>0. It is exactly
−1<tau<1. At −1 only wall i is active; at +1 only wall j is active.
All other inequalities are strict at both endpoints. The complete-fiber
theorem excludes rank-one endpoints and provides two positive open-wall
source points with the same image. Both selected tile images are open,
so their intersection is a nonempty open set. This constructs every
opposite pair, for every positive Z, without numerical sign continuation.

Thus for all ten circuit core types the relation space at EACH fixed
positive Z is exactly the span of the balanced 3↔3 relation. The all-Z
relation space is the same span. The construction is recorded in
`circuit_overlap.py`; exact regressions realize its nine pairs on each of
the ten cores. This also verifies the former seven-support and two-class
special cases without treating their symmetry copies as new mechanisms.

## 5. Exact connected overlap witnesses for the ten-wall families

**PROVED by exact finite certificates, independently audited in [REVIEW](REVIEW.md).**
For each of the four reflection cores and the repaired spurion core, a
fixed positive rational moment-curve Z admits a connected overlap witness
graph on all ten admissible walls. Each saved edge consists of two exact
positive open-wall source representatives with equal image row spaces.
The nine selected edges form a spanning tree. Their incidence matrix has
rank nine, with kernel the canonical balanced coefficient vector.

The graph lemma supplies the entire relation-space conclusion: at this
fixed Z, every relation is a multiple of the already proved canonical
5↔5 relation. Requiring the relation for all positive Z therefore gives
the same one-dimensional all-Z kernel. This does not assert dimension
one at every other fixed positive Z.

These are realizable OPEN-overlap witnesses, not a sampled chamber matrix
whose completeness has been presumed. Each edge supplies a rigorously
necessary equation on any possible relation. The existing nonzero
canonical relation supplies the matching upper bound on indicator rank.
No enumeration of all chambers is required for the resulting equality of
relation spaces. The exact source points, source affine labels, invertible
row changes and integer incidence matrices are independently checked in
the [local overlap artifacts and proof](LOCAL_RELATION_KERNELS.md).

## 6. The hostile kernels are zero

**PROVED by exact finite certificates, independently reviewed.** For each
of the two four-mass hostile core types, eight exact target neighborhoods
give an 8×8 indicator matrix of determinant one. Every membership and
nonmembership decision is complete: the source closure/gauge audit,
all nonzero twistors, complete rational wall inversions, and strictly
nonzero remaining coordinates certify a constant indicator vector on an
open neighborhood. The determinant is checked independently with Fraction
elimination.

Consequently their eight admissible facet indicators have no nonzero
relation at the displayed fixed Z, and no constant-coefficient all-Z
relation. This excludes ordinary local replacements supported on those
facets. It does not exclude a relation using additional tiles, nor decide
whether a single admissible-facet cover of the q8 parent exists. Only
the q9 parent's missing-cover region is proved. See
[COUNTEREXAMPLE_SEARCH](COUNTEREXAMPLE_SEARCH.md).

## 7. What the completed local calculation implies

**PROVED, independently audited.** For every nine-dimensional rank-two
parent, every constant-coefficient all-Z indicator relation supported on
its admissible codimension-one facets has coefficient sum zero. For the
fifteen non-hostile noncollapsed core types its relation space is a
one-dimensional balanced span; for the two hostile types it is zero;
the twelve collapsed types have no admissible full-dimensional facets.
Exact loop and dihedral transport makes this a statement for arbitrary n.

In particular, distinct all-Z multiplicity-one local replacements using
only the facets of a single parent are its canonical 3↔3 or 5↔5
replacement, up to exchanging the sides. For a multiplicity-one all-Z
tiling of a balanced parent by a subset of these facets, subtract the
canonical positive-side tiling. The difference is lambda*epsilon and
has entries in {−1,0,1}. The 0/1 coefficient condition forces lambda=0 or
the opposite-side choice. Thus the two displayed tilings are the only
such multiplicity-one all-Z facet tilings. Overlapping covers are not
classified by this argument.

This last assertion remains restricted to the parent's admissible source
facets and to fixed cell collections valid for all Z. It does not classify
covers using other contained tiles, establish uniqueness for every fixed
Z in the ten-wall cases, or prove that arbitrary tiling differences are
generated by parent relations. No Magic Number theorem follows without
that separate generation input, which Run4 does not pursue.
