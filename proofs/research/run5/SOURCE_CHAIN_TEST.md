# The ordinary source boundary fails as an image-relation complex

**FAILED, exact mod-2 obstruction.** At n=8, apply ordinary seven-dimensional
source-facet incidence to the full 176-dimensional admissible tile space.
Every one of the 96 certified geometric local parent relations has a
nonzero source boundary. Thus the ordinary source differential cannot be
used as the next map after these geometric relation generators.

**PROVED / COMPUTATIONALLY-VERIFIED.** A natural source quotient restores
the equation d8 d9=0 over F2, but its middle homology has dimension 15.
Worse, eight individual admissible tile basis vectors are cycles in this
quotient. A nonempty tile is not a zero geometric indicator. This supplies
an explicit kill-test for identifying these formal source cycles with
image relations.

These conclusions concern a formal source-chain proposal. They produce no
unbalanced geometric indicator relation, no unequal-size flip, and no
Magic Number counterexample.

## 1. The three objects being tested

Use coefficients F2 throughout the n=8 test. This avoids assuming or
reconstructing any oriented source boundary signs. The ordinary positroid
cell decomposition is regular CW, so a codimension-one source incidence
has coefficient one mod two. Let

\[
C_j^{\rm src}=\mathbb F_2\langle\text{all j-dimensional rank-two source cells}\rangle.
\]

Exact source enumeration gives

\[
\dim C_7^{\rm src}=504,\quad
\dim C_8^{\rm src}=266,\quad
\dim C_9^{\rm src}=112.
\]

All dimensions and incidences use source cells, without interpreting their
images as facets. The facet operation lists are checked independently by
enumerating every candidate lower cell and testing complete basis inclusion
at dimension difference one. On the complete source inventory, the product
of the ordinary mod-2 boundary maps is zero for every one of the 112 parents.
This is both a source CW fact and an exact regression check.

Let F8=F2^U8 be the free space on the 176 all-Z admissible eight-cells, with
inclusion i:F8→C8^src. Let P9=F2^96 be the free space on the full Run4
geometric local relation generators. Define

\[
d_9:P_9\longrightarrow F_8
\]

using the geometric coefficients reduced mod two. All those coefficients
are ±1, so the mod-2 column is precisely the set of admissible facets of
its balanced parent. This domain is not the full 112-dimensional source
nine-cell group: the collapsed and hostile parents give no geometric
relation generator. Define the proposed next map

\[
d_8^{\rm raw}=\partial_8^{\rm src}\circ i.
\]

The source differential and geometric relation coefficients are different
objects, even when their mod-2 supports agree on admissible facets.

## 2. The unquotiented test fails for every local relation

**COMPUTATIONALLY-VERIFIED, exact.** The matrix d8^raw has rank 176 over F2.
In particular it has no nonzero kernel on the admissible tile space.
The product d8^raw d9 has 96 nonzero columns out of 96, with 1,680 nonzero
entries. Its column support sizes are:

| Number of source seven-cells in the boundary | Number of geometric relation columns |
|---:|---:|
| 10 | 8 |
| 14 | 56 |
| 25 | 16 |
| 26 | 16 |

Every residue is checked to equal the ordinary source boundary of the
omitted nonadmissible eight-dimensional facets of that parent. This is
exactly what the full source identity boundary-squared-zero predicts.
The inadmissible facets cannot simply be dropped while keeping the next
ordinary source boundary unchanged.

This mod-2 failure also obstructs any integer version with the same support
and incidence coefficients ±1: an integer zero product would reduce to zero
mod two. No choice of source orientations repairs this support-level failure.
The argument does not equate source signs with image-side signs.

## 3. The minimal coordinate quotient makes a formal complex

There are 90 nonadmissible eight-cells in the complete source inventory:
88 have the all-Z image-dimension obstruction and two are the certified
noninjective four-mass cells. Let N7 be the coordinate subspace generated
by every seven-dimensional source cell lying in the closure of any of these
90 eight-cells. Because the dimension difference is one, enumerating their
source facets enumerates exactly this set. There are 408 such lower cells,
leaving 504−408=96 coordinate classes in

\[
Q_7=C_7^{\rm src}/N_7.
\]

Let d8^quot be d8^raw followed by the quotient map. Then

\[
d_8^{\rm quot}d_9=0.
\]

**PROVED.** For each geometric parent column, its raw boundary equals the
boundary of its omitted nonadmissible source facets, by the full ordinary
source identity. Every seven-cell in the latter boundary is killed in Q7.
Thus the quotient identity follows structurally; the exact matrix product
independently checks it for all 96 columns.

This establishes a three-term complex over F2,

\[
\mathbb F_2^{96}\xrightarrow{d_9}
\mathbb F_2^{176}\xrightarrow{d_8^{\rm quot}}
\mathbb F_2^{96}.
\]

It does not construct a chain model for image indicators. In particular,
the four-mass cells are removed because they are inadmissible, not because
their image dimension is lower. Quotienting their source boundaries is a
formal operation requiring independent geometric justification.

## 4. Exactness and the geometric interpretation both fail

**COMPUTATIONALLY-VERIFIED.** Two independent mod-2 elimination algorithms
give

\[
\operatorname{rank}d_9=73,\qquad
\operatorname{rank}d_8^{\rm quot}=88.
\]

Consequently the middle homology of this formal complex has dimension

\[
\dim H_8=176-88-73=15.
\]

The computation is over F2; it is not a rational image-relation rank or a
complete-tiling difference rank. In particular its numerical value 15 is
not used to identify it with any other 15-dimensional space in the campaign.

There is a direct geometric kill-test as well. Eight individual admissible
tile columns have zero d8^quot boundary. For example take the all-Z tile
whose source has singleton classes

\[
(2)(3)(4)(6)(7)(8),\qquad\text{loops }1,5,
\]

and affine window

\[
(1,4,6,7,5,8,10,11).
\]

Each of its six seven-dimensional source facets lies in the closure of a
nonadmissible eight-cell and is therefore killed in Q7. The artifact saves
an explicit such nonadmissible parent for each facet, checked by dimensions
and full basis inclusion. Thus its single basis vector e_T is a cycle.
Its augmentation is 1 mod two, whereas all local relation columns have
augmentation zero, so e_T is not in im d9. Exact rank augmentation gives
the same conclusion for all eight individual cycle columns.

**PROVED.** These unit cycles cannot be zero geometric indicator classes:
each is a certified all-Z tile with nonempty open eight-dimensional image.
This excludes the implication

\[
d_8^{\rm quot}c=0\quad\Longrightarrow\quad
\sum_T c_T[T]=0
\]

even with mod-2 indicators, using c=e_T. It also shows that a unit
augmentation does not vanish on all cycles of this formal source quotient.
These are spurious source cycles, not unbalanced tile relations.

## 5. The n=7 parity simplex chain passes its separate regression

**PROVED / COMPUTATIONALLY-VERIFIED.** In n=7, use the exact parity label
dictionary from [N7_PROOF](N7_PROOF.md). The 21 admissible rank-two labels
correspond to all five-subsets of [7]. On the full abstract simplex on seven
vertices, the ordinary oriented simplicial maps give

\[
\mathbb Q^7=C_5\xrightarrow{\partial_5}
\mathbb Q^{21}=C_4\xrightarrow{\partial_4}
\mathbb Q^{35}=C_3.
\]

For an increasing simplex (v0,…,vj), use
∂[v0,…,vj]=Σ_i(−1)^i[v0,…,v̂i,…,vj]. Then

\[
\partial_4\partial_5=0,\qquad
\operatorname{rank}\partial_5=6,\qquad
\operatorname{rank}\partial_4=15,\qquad H_4=0.
\]

This is the standard simplex-chain exactness in positive degrees, checked
again by the explicit integer matrices. After identifying the C4 basis by
the parity dictionary, all seven full local n7 parent rows agree with the
seven ∂5 columns up to recorded overall orientations. Every ∂5 column has
three +1 and three −1 entries.

This is an abstract simplex chain after a source-label correspondence. It
is not asserted to be the ordinary rank-two positroid CW differential or
to transport arbitrary image relations through parity. The separate
[n=7 completeness proof](N7_PROOF.md) establishes the exact geometric
consequence D7=L7 by classifying all tilings and checking the actual C7
flip graph; that conclusion does not rely on either of those extra claims.

## 6. Reproduction and scope

The [implementation](../../src/magic_number/run5_source_chain.py) retains
all source cells, sparse incidences, geometric columns, product residues,
quotient indices, all eight spurious unit cycles, and the n7 integer chain
matrices in [the artifact](../../results/run5/source_chain_test.json).
The [tests](../../tests/test_run5_source_chain.py) check complete incidence
by a separate basis-inclusion implementation, all full source products,
both mod-2 rank implementations, exact closure witnesses, and saved-artifact
reproduction. No complete n8 tiling enumeration is used.

**FAILED.** Ordinary source boundary as the differential detecting geometric
local relations. **FAILED.** Exactness or geometric completeness of the
coordinate quotient by nonadmissible source closures. **PROVED.** The
explicitly scoped F2 quotient chain identity and the independent n7 abstract
simplicial regression. These outcomes isolate a missing geometric step
rather than replacing it with source-cell homology.
