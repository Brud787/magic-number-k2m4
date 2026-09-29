# Complete finite generation results

**PROVED.** The bounded run settles the requested generation problem at
n7 and n8, with exact rational certificates and independent geometric
audits. It does not infer an all-n theorem from these cases.

| n | dim V_n | Parent rows | rank L_n | rank D_n | rank(D_n+L_n) | dim V_n/L_n | dim D_n/(D_n∩L_n) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 7 | 21 | 7 | 6 | 6 | 6 | 15 | 0 |
| 8 | 176 | 96 | 73 | 73 | 73 | 103 | 0 |

All rows have coefficient sum zero, and so do all complete-tiling
differences in these two cases. The trivial n6 case has one source tile
and one tiling because the external 6×6 matrix is invertible. The tile
counts 1,6,20 agree with M(2,n−6,2).

## n7: complete enumeration and actual connectivity

**PROVED.** There are exactly seven all-Z tilings, each containing six
tiles. Parity identifies the complete 21-tile universe with five-subset
simplices of a cyclic four-polytope. Exact Gale feasibility determines
all 210 pair decisions at one positive matrix. The compatibility graph
has exactly seven maximal cliques, independently enumerated twice. Each
is literally the parity label set of a known all-Z BCFW tiling, while
any hypothetical further all-Z collection must lie in one of these
cliques. This gives exclusion from fixed data and existence from an
independent all-Z theorem.

The seven actual Run4 parent flips form C7, and every local row occurs
on an edge. Thus D7=L7 and the genuine flip graph is connected. Details
and all source labels are in [N7_PROOF](N7_PROOF.md) and
[tilings_n7.json](../../results/run5/tilings_n7.json). The result is a
known cyclic-polytope/parity sector reconstructed exactly, with no novelty
claim.

## n8: full generation without full tiling enumeration

**PROVED.** The full Run4 relation set has 96 distinct parent rows:
56 seven-support rows and 40 eight-support rows. Their combined rank
is 73. This is the full set of relevant local generators; it is not the
old restricted seven-support span, whose failure remains preserved.
All 176 certified all-Z tile labels participate.

The [complete indicator certificate](N8_INDICATOR_THEOREM.md) proves
ker Phi_all,8=L8 using 103 independent open indicator rows, each with
complete rational membership/nonmembership decisions on all 176 tiles.
Its determinant-2 minor is exact. This supplies D8⊆L8 for **every**
complete all-Z tiling, not merely the known BCFW orbit.

The separate [bounded flip-span certificate](N8_FLIP_SPAN.md) gives
74 all-Z tilings with a 73-dimensional difference span. Their validity
is proved by replaying 152 genuine local replacements in a retained
153-node ancestral tree. The bounded discovery stopped at its target
rank after 2,440 states, below its 3,000-state cap. This proves the
reverse inclusion and hence D8=L8. It does not prove that every tiling
belongs to that component, nor that only those discovered tilings exist.

**PROVED.** The entire all-Z tiling set has the exact finite formulation

\[
 \{\chi\in\{0,1\}^{176}:A\chi=\mathbf1_{103}\}.
\]

The sufficiency uses full kernel equality and positivity, so this is
not a merely necessary sampled cover model. Rigorous enumeration is
therefore reduced to a finite exact-cover problem. Its binary solutions
were not exhausted: the requested finite generation theorem already
follows from the rank certificates. The complete number of n8 tilings
and connectivity of its entire flip graph remain unreported.

An exact signed rational neighborhood functional assigns unit weight to
all 176 tiles and total weight twenty to the amplituhedron. Thus every
complete all-Z n8 tiling has twenty pieces. No all-n functional is
constructed. Machine ranks, the exact-cover model, and weights are in
[generation_ranks.json](../../results/run5/generation_ranks.json),
[exact_cover_model_n8.json](../../results/run5/exact_cover_model_n8.json),
and [unit_functional_n8.json](../../results/run5/unit_functional_n8.json).

## Limits on extension

**CONJECTURAL.** The analogous generation theorem for n≥9. The first
new tile profile is the genuine spurion, outside the simple complement-five
inverse used for all n8 tiles. The Run4 local theorem already handles its
parent relations, but does not give a global kernel presentation.
No n9 complete-tiling enumeration or long all-n search was started.
