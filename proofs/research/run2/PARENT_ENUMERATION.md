# Run 2: exact rank-two parents and admissibility filters

This is a bounded extension of the first-run source enumeration. It does not identify a source boundary identity with an image relation. Source files and fixtures from Run 1 remain intact.

## Complete source-parent enumeration

**PROVED (existing source normal form applied).** A nine-dimensional rank-two positroid source cell has `q+s=13`, where `q` is its nonloop count and `s` its number of cyclic parallel classes. Its codimension-one source boundaries arise by deleting an element of a nonsingleton class or merging cyclically adjacent classes. The proof and classical classification references are in [K2.md](../K2.md). Basis containment gives a separate exhaustive incidence test.

**COMPUTATIONALLY-VERIFIED.** All nine-dimensional source cells and all their eight-dimensional source boundaries were enumerated. An independent bounded-affine-permutation enumerator agrees on every affine label, dimension, Grassmann necklace and basis set. For every parent, its generated facets agree with all dimension-eight cells whose full basis set is contained in the parent's basis set.

| Ambient `n` | Nine-dimensional parents | Profiles `(q,s): count` | Source incidences | Dihedral parent orbits |
|---:|---:|---|---:|---:|
| 7 | 7 | `(7,6):7` | 56 | 1 |
| 8 | 112 | `(7,6):56; (8,5):56` | 1,016 | 9 |
| 9 | 882 | `(7,6):252; (8,5):504; (9,4):126` | 8,577 | 57 |

These are counts of source objects. The complete labeled catalogs are `results/run2/parents_n7.json`, `parents_n8.json`, and `parents_n9.json`; no symmetry representatives replace the complete enumeration. Every parent includes a dihedral orbit representative and an explicit action taking it to that representative, sufficient to expand or check the labeled orbit.

Each parent and child record stores the affine permutation, complete basis set, Grassmann necklace, vanishing two-minors, support and cyclic parallel classes. Each incidence stores its codimension, operation, inherited vanishing minors, and every newly vanishing minor. Uncertified image facet, disjointness, union and multiplicity assertions remain `UNKNOWN`. In particular, source incidence orientation signs remain null: ordering a facet list would not establish its orientation.

## Class-complement obstruction

**PROVED (elementary all-Z image-dimension bound; no novelty claim).** Let `S` be an eight-dimensional rank-two cell, let `B` be one of its parallel classes, and let `t=|supp(S)\B|`. If `t<=4`, then for every positive external `n by 6` matrix `Z`,

\[
\dim\widetilde Z(S)\le t+3<8.
\]

In particular, `S` is not an admissible tile source for any positive `Z`.

**Proof.** Set `W=span{Z_i:i in supp(S)\B}`. Positivity of all six-minors implies independence of any at most six external rows, so `dim W=t`. For every representative `C` of the cell choose a nonzero row functional `ell` annihilating the common column direction of `B`. Then `ell C` vanishes on `B` and on all loops. The image plane `Y=rowspan(CZ)` contains `ell CZ in W`. This vector is nonzero because positivity makes `CZ` rank two. Thus every image plane belongs to

\[
\Sigma_W=\{Y\in\mathrm{Gr}(2,6):Y\cap W\ne0\}.
\]

Parameterize its incidence resolution by choosing a line `L subset W`, of dimension `t-1`, then a plane `Y superset L`, of dimension four. Consequently `dim Sigma_W<=t+3`. An injective continuous map from the open eight-ball `S` into the eight-manifold `Gr(2,6)` would have open image by invariance of domain, contrary to containment in this lower-dimensional algebraic locus. This proves both the image-dimension bound and noninjectivity. The argument does not depend on a Jacobian sample. □

This is a standard Schubert incidence calculation. It is a convenient rigorous filter, not a purported new general classification theorem or a sufficient condition for injectivity. It remains valid after inserting any number of loop columns.

**COMPUTATIONALLY-VERIFIED.** The filter leaves `1,21,178,960` eight-dimensional source cells for `n=6,7,8,9`, respectively. These are exactly the counts with a rank-eight witness in the union of the two first-run samples. The equality of these finite counts does not make the filter a sufficient tile test: the four-mass cell passes it and has full generic differential rank.

## Tile-status provenance and scope

**SOURCE-VERIFIED / COMPUTATIONALLY-VERIFIED.** The separate `general_bcfw.py` recipe generator uses the source matrix in the main BCFW paper, together with the all-Z BCFW injectivity theorem. Its counts are `1,21,176,939` for `n=6,7,8,9`. Every certified cell has a concrete source recipe. Identification of the recipe's positroid is exact source algebra, with no external numerical `Z`. The weaker, independent union of zero-inserted dihedral standard KWZ cells has counts `1,21,168,867` and is retained as a crosscheck/subset. Its failure to include all BCFW cells must not be confused with non-BCFW tilehood.

**SOURCE-VERIFIED.** Galashin--Lam Example 13.12 explicitly calls the four-mass cell `(12)(34)(56)(78)` nonadmissible. Its cyclic counterpart is therefore also excluded at `n=8`. This uses the explicit nonadmissibility statement, not the algebraic degree-two assertion by itself. The source establishes failure of all-Z admissibility; the catalog does not silently strengthen this to failure for every `Z`.

**SOURCE-VERIFIED.** The three cyclic cells with profile `(3,3,3)` at `n=9` are the published spurion and its cyclic shifts. They are certified all-Z tiles, and they are not BCFW cells. This individual tile certificate does not certify the disputed printed parent/replacement relation.

**COMPUTATIONALLY-VERIFIED (complete finite partition; no novelty claim).** Combining the full source enumeration with these certificates gives:

| `n` | Certified all-Z tiles | Certified non-tiles | Unresolved |
|---:|---:|---:|---:|
| 7 | 21 BCFW | 7 class-complement obstruction | 0 |
| 8 | 176 BCFW | 88 class-complement obstruction + 2 published four-mass exclusions | 0 |
| 9 | 939 BCFW + 3 spurions | 594 class-complement obstruction + 18 loop-extended four-mass exclusions | 0 |

The `n=8,9` results are complete classifications of admissible **source labels for all-Z tile maps** by existing theorem certificates and exhaustive source enumeration. They are not classifications of tilings, proofs that every pair of certified tiles is compatible, or proofs of Magic Number. No novelty is asserted. For `n=9`, transferring the four-mass nonadmissibility certificate through a loop insertion uses the independently proved [positive external-matrix extension lemma](POSITIVE_EXTENSION.md): a positive external matrix witnessing failure in eight rows extends through a prescribed gap, and zero insertion preserves the noninjective source pair and its image. Algebraic degree two alone is not used to fill that gap. The initial uncertainty about those 18 cells is resolved by this explicit geometric argument.

## Candidate relations and aggressive failure fixtures

**PROVED / COMPUTATIONALLY-VERIFIED.** The separately certified BCFW catalog contains seven local `3<->3` relations at `n=7`, one for each of the seven parents. Their order-preserving loop insertions give 56 local `3<->3` relations at `n=8`, exactly one for each parent of support seven. See [BCFW_RELATIONS.md](BCFW_RELATIONS.md). These have all-Z equality of covered closed regions, pairwise disjoint open tile images on either side, multiplicity one off lower-dimensional boundaries, and coefficient sum zero. The relation is obtained by cancelling a common subcollection of two certified complete BCFW tilings, then restricting/embedding to the indicated parent; it is not inferred from source incidence. Parent records reference those relation IDs and keep their signed image coefficients separate from still-unoriented source incidence coefficients.

No geometric relation is asserted for the remaining parents solely from their facet lists. The following histogram deliberately retains the degree-two trap. The first number counts children surviving the class-complement filter; it is not a tile count.

| `n` | Surviving source boundaries | Four-mass-profile boundaries among them | Parents |
|---:|---:|---:|---:|
| 8 | 0 | 0 | 8 |
| 8 | 6 | 0 | 88 |
| 8 | 9 | 1 | 8 |
| 8 | 10 | 0 | 8 |
| 9 | 0 | 0 | 108 |
| 9 | 6 | 0 | 594 |
| 9 | 9 | 1 | 72 |
| 9 | 10 | 0 | 99 |
| 9 | 11 | 3 | 9 |

**FAILED (shortcut).** Treating all full-rank/full-dimensional boundary sources as tiles would admit the nine-boundary families with one four-mass source and the eleven-boundary families with three four-mass sources. Their odd cardinalities are useful warning fixtures, not unbalanced indicator relations. Deleting their nonadmissible components from an oriented source or canonical-form identity is not justified. No coefficient sum is computed for an unsigned or uncertified relation.

## Reproduction and verification

```sh
PYTHONPATH=src .venv/bin/python -m magic_number.parent_relations
PYTHONPATH=src .venv/bin/python -m pytest tests/test_parent_relations.py -q
```

The generator imports the general BCFW source certificates, independently checks all parent and child affine labels and incidence sets, then writes complete JSON catalogs. If `results/run2/bcfw_relations.json` is present, the independently proved local image relations are attached by exact common-parent affine labels. The tests include exhaustive checks through `n=9`, source zero-minor witnesses, orbit expansion, the all-Z rank obstruction, and regressions requiring a separate positive extension certificate when transferring four-mass nonadmissibility through loop columns. They do not infer source orientations from the image relation signs.

**PROVED (integration update after independent review).** The repaired
spurion relation and its18 dihedral copies are now certified separately
in [SPURION_ATTEMPT.md](SPURION_ATTEMPT.md). The final parent catalogs attach
their exact image coefficients to18 n9 parents, retaining their own
positive-fiber proof reference. The other parent relations remain
unresolved. To reproduce these later references, run the parent generator
with `--relations results/relation_catalog.json` after creating that
catalog. The source orientation fields remain null; the separately proved
image signs do not orient the full source boundary.
