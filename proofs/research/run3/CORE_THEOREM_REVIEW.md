# Independent hostile audit: finite cores and the two-class theorem

Reviewer: the parent-enumeration subagent, independently of the author of `FINITE_CORES.md`, `TWO_CLASS_THEOREM.md`, `parent_profiles.py` and `two_class_fibers.py`. This review checks the mathematical reductions and complete fiber argument; passing tests are supplementary evidence.

**PROVED / REVIEWED.** No critical mathematical issue was found in the two-class theorem or finite-core transport reduction as stated. The former certifies the complete full-dimensional two-class parent sector, with its stated even-m extension. The latter does not certify unresolved core geometries or generate arbitrary complete-tiling relations.

## 1. The only full-dimensional two-class profile

A nine-dimensional rank-two source parent has `q+s=13`. With exactly two classes, `q=11`. An image plane contains the line contributed by each class. If one class has size `r<=4`, all image planes meet its fixed external span, of dimension `r`; the Schubert incidence locus has dimension at most `(r-1)+4<=7`. Thus full dimension eight is impossible. The only remaining two-class split is `(5,6)`. This uses an image-dimension bound valid for the parent itself, not an injectivity inference or a bound restricted to eight-dimensional source cells.

For general even `m>=2`, the same calculation has external dimension `d=m+2` and target dimension `2m`. A class of size `r<=m` gives image dimension at most `(r-1)+(d-2)=r+m-1<2m`. Since `q=2m+3`, the only possible full-dimensional split is `(m+1,m+2)`. The selected wall injectivity and inward-fiber argument below also establish that this remaining profile really has full-dimensional image.

## 2. Unique A-ray and exclusion of a second fiber branch

The displayed block matrix parameterizes the source by independent positive projective coefficient rays. This is the correct row-gauge quotient for two classes; imposing only simultaneous scaling would give the wrong dimension.

Let `H_A=span(Z1,...,Z5)`. Its dimension is five by maximal-minor positivity. The functional `ell(X)=det(Z1,...,Z5,X)` is zero on `H_A` and strictly positive on every positive combination of the six subsequent B-rows. Thus for `Y=span(U,V)`, `Y` is not contained in `H_A`, and its intersection with `H_A` is exactly the line through `U`.

A second positive A-coefficient vector with the same image line must be a positive scalar multiple of the first: the five A-rows are independent and both coefficient lists are strictly positive. Hence fixing a representative of this positive ray does not miss a second A-branch.

Every other positive B-vector in `Y` has a unique expression `V'=alpha V+beta U`. Applying `ell` gives `alpha=ell(V')/ell(V)>0`. After the allowed positive rescaling of the B-row, it has the form `V+tU`. This excludes the potentially missing `alpha<0` branch and proves that the entire positive source fiber, not merely a tangent or one connected component, is described by `b+t h` with `h=U Z_B^{-1}`. Independent B-row scaling is explicitly accounted for.

## 3. Cramer signs, boundedness and all selected wall maps

The Cramer formula has the stated sign. Replacing the `j`th row of `Z_B` by `U` computes `h_j det(Z_B)`. Moving `U` from that position to the first row gives the sign `(-1)^(j-1)`. Expanding `U` in the A-rows leaves only increasing external-index maximal minors, all strictly positive. Consequently every `h_j` is nonzero and the signs alternate.

There are both positive and negative `h_j`, so the feasible interval has finite lower and upper endpoints. Because the chosen `b` is strictly positive, zero lies strictly between them. This establishes nonemptiness, boundedness and exactly two endpoints of the complete normalized positive fiber. It does not assume convexity from the source-cell dimension.

On a B-deletion wall, each remaining class has five rows and spans a hyperplane. The determinant `det(Z_A,V)` is positive, and `det(U,Z_(B without j))` is positive in the displayed ordering. Thus neither corresponding image line lies in the other hyperplane. The two source rays are uniquely recovered as the respective intersections of `Y` with these hyperplanes; independence of each five-row list then recovers its positive coefficients. This proves global all-Z injectivity of the full open wall cell. The same argument works with hyperplanes of dimension `m+1` in the stated general-even-m extension.

The separate m4 BCFW recipe is valid: for ten reduced labels, `a=6,b=7,c=8,d=9,n=10` and left rank-one support `{1,...,5}` satisfy the source index and coindependence conditions. Figure 10 then gives one row supported on `{1,...,5}` and the bridge row supported on `{6,...,10}`. The loop embedding recorded for each deleted B-label identifies the desired wall. The direct hyperplane proof already supplies tile injectivity, so the theorem does not depend on extrapolating an enumerator to larger n.

## 4. Full image equality and lower strata

No endpoint can have the B-row vanish: `ell(V+tU)=ell(V)>0`. Its A-row is the fixed nonzero positive ray, supported on disjoint columns. Thus every normalized closed fiber endpoint is a genuine rank-two nonnegative source point. This avoids the rank-one chart-boundary issue that needs separate incidence bounds in the three-anchor orthant proofs.

An endpoint tie imposes at least two B-coordinates equal to zero. Such source strata have dimension at most `4+3=7`; in general dimension at most `m+(m-1)=2m-1`. Their images are lower-dimensional. There are finitely many of these strata, so generic endpoint counting is justified. The five A-deletion walls have the independently proved collapsed-image bound and do not appear as hidden endpoints of a fiber over the open parent image, since that fiber fixes a strictly positive A-ray.

The openness assertion admits the following explicit local justification. Near an image plane `Y0` not contained in `H_A`, its intersection line with `H_A` varies smoothly. Normalize its positive A-coefficients by a fixed positive affine condition. Choose a local frame of the nearby planes and a continuous section `V(Y)` agreeing with the original `V` at `Y0`, then normalize `ell(V(Y))` to the original positive value. All six B-coefficients in the fixed basis `Z_B` remain positive near `Y0`. This yields nearby positive parent preimages and proves openness without an unproved global choice of B-section.

Every selected wall moves inward into the parent along the nonzero coordinate derivative `h_j`, so its open image lies in the open parent image. Generic endpoint uniqueness gives multiplicity one, and wall injectivity plus invariance of domain makes each wall image open. Any same-side overlap would be open and would meet the generic locus, contradicting endpoint uniqueness. The same-side interiors are therefore exactly disjoint.

The closed finite side unions equal the closure of the parent image: one containment follows from source incidence, and the other from dense generic endpoint coverage and closedness of the finite unions. Compactness of source closures justifies using closed images. This proves an indicator-class relation with admissible tiles and closed covered-region equality, rather than merely an oriented source or canonical-form identity.

Evenness enters the **wall-type count**: `m+2` is even, so the alternating nonzero Cramer signs occur equally often. Cancellation of the two endpoints of each individual fiber alone would not establish equality of the numbers of wall types. The proof identifies this extra algebraic input explicitly.

## 5. Source core completeness and dihedral types

The five support/class possibilities follow directly from `q+s=13`, `2<=s<=q`:

`(q,s)=(7,6),(8,5),(9,4),(10,3),(11,2)`.

Choosing `s` cuts in a labeled q-cycle gives respectively `7,56,126,120,55` loopless source labels, totaling 364. Each cut set determines exactly one cell and can be recovered from its class boundaries. These counts concern source parents only.

The loopless composition types up to cyclic order reversal are `1,5,10,8,5`, totaling 29. As a separate small combinatorial check, the q8 types consist of one `(4,1,1,1,1)` arrangement, two `(3,2,1,1,1)` arrangements and two `(2,2,2,1,1)` arrangements. The q9 types consist of counts `1,2,2,2,2,1` for sorted profiles `(6,1,1,1),(5,2,1,1),(4,3,1,1),(4,2,2,1),(3,3,2,1),(3,2,2,2)`. For three classes the dihedral action permutes all three parts, giving the eight partitions of ten into three positive parts; for two classes it gives the five unordered splits of eleven. This independently checks the profile counts beyond the code's composition canonicalizer.

`loopless_parents`, `composition_type` and `core_of` implement the stated source constructions. Ambient label orbits retain loop placements, while the core records discard only loops and dihedral placement. The code does not identify an arbitrary untested fiber topology from its wall count; unresolved cases remain explicit.

## 6. Both directions of fiber transport

For zero insertion on an increasing support `I`, `(j_I C)Z=C Z_I` is an exact matrix identity. Deletion is its inverse on source row spaces with the prescribed zero columns, including their closures. Thus all positive preimages, their topology, source boundaries and image regions are preserved for each fixed external matrix. Positive restriction alone proves transport from an all-Z core assertion to every loop insertion.

The reverse implication requires more than positive restriction. The previously reviewed positive-row extension lemma supplies it: any positive real core matrix extends through any prescribed sequence of gaps while retaining its original rows. Therefore a counterexample to a specified all-Z **local core-fiber assertion** also extends to the chosen loop insertion. This applies to injectivity, specified local unions/relations, disjointness, multiplicity and fiber topology. It does not claim that a complete tiling of the smaller amplituhedron becomes a complete tiling of the larger amplituhedron.

The dihedral transport also has compatible matrix identities. For reflection, let `R` reverse labels, choose a source two-row sign matrix `D2` of determinant `-1`, and choose an ambient six-column sign matrix `D6` of determinant `-1`. Then `D2 C R` and `R Z D6` preserve the relevant ordered-minor positivity, and their product is `D2 C Z D6`. This identifies positive fibers by invertible source and ambient changes. Signed cyclic actions likewise match because rank two and external rank six have the same cyclic sign `-1`. In the stated general-even-m extension the external rank remains even, so this matching persists.

Algebraic degree is preserved only for the identified restricted maps when it is defined; positive preimage counts are preserved directly and are not inferred from degree. Transporting source/target orientations preserves the specified wall signs up to a global convention change, which does not affect a zero coefficient sum.

**Review conclusion.** The two-class local theorem survives the stated admissibility, all-Z, multiplicity, boundary and sign-count gates. The 29-core reduction is an exact source/fiber reduction with a proved converse external-data extension. Neither claim supplies missing core certificates or a parent-relation generation theorem for arbitrary tilings. No further prototype search was conducted in this audit.
