# Independent hostile audit of the q10 interval proofs

**PROVED, independently reviewed.** The proofs in Q10_334.md for the
(3,3,4) and(2,4,4) cores pass this audit. The reviewer separately read the
proof and q10_parent_fibers.py, checked the signs and orientation claims,
and recomputed the twenty endpoint coefficients using an ambient linear
system rather than the implementation's quotient-space matrix. No
unresolved mathematical obstruction was found. This audit does not claim
novelty, relation generation, or an extension to a complete tiling.

## Source and full-fiber gates

Three distinct cyclic projective directions can be normalized uniquely to
horizontal, diagonal and vertical, up to the common positive scalar. Thus
the ten-coordinate positive orthant really is the entire parent chart in
both profiles. There is no fourth-direction proportionality constraint or
ordering inequality left to impose. This distinguishes these parents from
the previously rejected four-mass/conic shortcuts.

All thirteen source facets are accounted for: ten single-column deletions
and three cyclic mergers. The deletion cores are exactly eight-dimensional
n9 sources with independent all-Z certificates, transported by increasing
zero insertion. In(4,3,3), the four A deletions are the(3,3,3) spurion cores;
the remaining six are BCFW. All ten(4,2,4) deletions are BCFW. Each merger
has complement at most four and is rigorously collapsed. In particular,
no merger comparable to the(5,5) wall in the other q10 profiles is lost.

The linear equations M_Y x=0 express the complete image containment
condition. For nonnegative rank-two source matrices, positivity of Z
ensures full image rank, so this is equality of image planes. The source
chart therefore identifies the whole positive fiber, rather than merely
its tangent space or complex algebraic degree.

## Rank and pivot gates

The rank-eight argument is valid throughout each parent and all ten open
walls. A dual covector alpha kills the four A rows and the vectors V,W.
Their six-vector determinant is a positive ordered-minor sum, forcing
alpha=0. Beta then kills the six distinct B∪D external rows and is zero.

The two claimed pivot factors were independently checked by block
elimination. For(4,3,3), deleting b6,b7 leaves four top-only A columns,
one diagonal B5 column and three bottom-only D columns. Its determinant
is B1234 B5,8,9,10. The first factor is positive; the second is negative
because its surviving b6 and b7 terms each move Z5 past one later B label.
At an open wall these two coefficients cannot both vanish, so the product
stays strictly nonzero. For(4,2,4), deleting b5,b6 leaves separate top and
bottom blocks, with the two positive factors B1234 and B7,8,9,10.

These prove a global two-coordinate kernel pivot on the required locus.
Wall transversality follows independently from certified injectivity:
otherwise an open positive wall point would have a nonconstant projective
interval of positive preimages inside the same wall. The kernel pivot and
wall charts provide actual smooth inverse local coordinates(Y,pivot ratio),
so the claimed submersion and sign-continuation arguments are justified.

## Reflection and orientation gates

The(4,3,3) reflection really exchanges the two three-element classes while
reversing the four-element class. Its signed-column matrix J satisfies
J²=I, and the symbolic identity C(Px)=H C(x)J holds for ten independent
source variables. The H in the document sends a positive diagonal
column to a negative vertical column and a positive vertical column to a
negative diagonal column; J's six minus signs restore positivity exactly.
For(4,2,4), ordinary reversal and the source row swap give the corresponding
symbolic identity.

The external positivity argument is universal. For(4,3,3), selecting r
rows from the first four gives total sorting/sign parity
15−r(6−r)+6−r, which is odd for every integer r. Therefore every ordered
six-minor of JZ is negative for every positive Z. Ordinary reversal gives
the same negative sign for(4,2,4). Multiplication by an ambient G with
negative determinant restores positivity. G may be taken to be the
involution diag(−1,1,1,1,1,1), making the full family action literally
involutive if desired. No positivity claim depends on a numerical Z.

Each source permutation consists of five transpositions and reverses the
positive projective9-dimensional orientation. The corresponding ambient
GL6 action preserves the orientation of Gr(2,6), since its orientation
character is sign(det G)^2. The exact tangent sequence of the proved
submersion therefore reverses fiber orientation. Constant wall signs pair
oppositely under the actual symmetry. This establishes the5+5 count
independently of the sample coefficient vectors, including both pairs of
spurion walls in(4,3,3).

## Endpoint, multiplicity and closure gates

In the pivot-sum normalization, every positive fiber is a bounded interval
inside the nonnegative kernel cone and has nonempty interior. The global
pivot excludes other positive branches. Rank-two points with at least two
zero coordinates lie in source strata of dimension at most seven.

The rank-one coefficient limit is correctly retained. Because a B pivot
is active, a rank-one source matrix has a nonzero diagonal column. All A
and D coefficients must then vanish. Its image line lies in span(Z_B),
whose projective line family has dimension b−1, and containing2-planes
have four further parameters. The total incidence bound is b+3≤6. This
also captures image limits requiring unbounded row operations; it is not
legitimate simply to remove such coefficient limits, and the proof does
not do so.

Consequently generic endpoints lie in exactly one selected admissible
wall and have multiplicity one. Parent-image openness follows from the
smooth positive kernel coordinates. Open wall images are open by
injectivity and invariance of domain, so a same-side overlap would meet
the generic locus and contradict endpoint uniqueness. Compact source
closures and density then give equality of both closed covered unions.
No canonical-form axiom or source-boundary identity is used instead of
these geometric steps.

## Independent exact calculations

**COMPUTATIONALLY-VERIFIED.** In addition to symbolic source reflection,
the sorting/sign character was checked on all210 six-element subsets for
each J. All420 characters are−1. This finite parity check concerns a
signed permutation and hence applies to every positive external matrix.

For each of the twenty open coordinate walls, an independent ambient
system used fourteen unknowns: ten source coefficients and four entries
of H, in the twelve equations C(x)Z=HY. Appending the two pivot
normalizations gives an invertible14×14 system. Its two kernel-coordinate
solutions reproduce the implementation's signs without choosing quotient
coordinates:

```
(4,3,3): (+,-,+,-, -, +,-, +,-,+),
(4,2,4): (+,-,+,-, +,-, +,-,+,-).
```

These are exact rational regressions of signs whose constancy has already
been proved. They are not the all-Z injectivity or balancedness proof.

## Related merger proof

The reviewer also read MERGER_WALLS.md. Its complete positive gauge,
the positivity forcing lambda∈(0,1), the seven-vector expansion of K,
the five alternating k_j signs, the genuine rank-two tau=0 merger and the
identity L_F(W−tau K)=1 all check out. That last identity prevents a
missing rank-one endpoint. Its tau>0 plus five deletion inequalities give
the stated3↔3 signs and correct complete interval. This agrees with the
independently derived complement-five theorem, including the actual
successive-slope derivatives rather than bare Gale coefficients.
