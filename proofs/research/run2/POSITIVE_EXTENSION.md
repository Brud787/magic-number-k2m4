# Positive row extension and loop nonadmissibility

**PROVED (elementary lemma; no novelty claim).** Every real matrix with all
ordered maximal minors positive and an even number d of columns can have a
row inserted at any prescribed position while preserving every original
row and strict positivity of all maximal minors. Rational input admits a
rational extension. Here d=6.

First append a row to positive rows v1,...,vq, q>=d. Set

`w(epsilon) = sum_{r=0}^{d-1} (-epsilon)^r v_{q-r}`.

For an ordered (d-1)-subset J of old rows, let r be the first index for which
v_(q-r) is absent from J. It exists among the last d rows. All earlier terms
in `det(v_J,w)` vanish. Moving v_(q-r) from the last determinant position
to its increasing position crosses exactly r selected rows. Its determinant
sign cancels the coefficient sign (-1)^r. Thus the leading nonzero
coefficient of this polynomial in epsilon is a strictly positive ordered
maximal minor. Finitely many polynomials are involved, so sufficiently small
positive epsilon makes all of them positive simultaneously. Old minors are
unchanged.

For an explicit rational bound, write each nonzero polynomial as
`epsilon^r (D + sum_{t>r} c_t epsilon^(t-r))`, with D>0. Choose epsilon no
larger than 1/2 and D/(2 sum |c_t|) for each nonempty tail. Then the absolute
tail is at most D/2. This is the exact bound implemented in
`src/magic_number/positive_extension.py`.

For insertion after row i, apply the append construction to
`(v_(i+1),...,v_q,-v_1,...,-v_i)`. This signed cyclic rotation preserves
positive maximal minors when d is even. Move the appended row back across
the cyclic cut with a minus sign. The result is
`(v_1,...,v_i,-w,v_(i+1),...,v_q)`, retaining all old rows. To check the signed
cyclic assertion directly, a d-minor containing t rows moved across the cut
acquires sign `(-1)^t (-1)^(t(d-t))=1` for even d.

**PROVED (consequence).** If a positroid cell fails all-Z injectivity, inserting
loop columns preserves that failure. Choose the positive external matrix
and two distinct source points witnessing noninjectivity. Extend that
matrix as above and insert zero columns in both source points. Their images
are unchanged, and they remain distinct. This is an existence argument for
a bad positive external matrix, not a claim of noninjectivity for every Z.

**SOURCE-VERIFIED input.** Galashin--Lam, *Parity duality for the
amplituhedron*, Example 13.12, explicitly states nonadmissibility of the
four-mass cell, beyond its degree-two calculation. Its centered permutation
is `[2,1,4,3,6,5,8,7]`; the bounded window adds 2. Its cyclic parallel-class
description is `(81)(23)(45)(67)`. A cyclic translate is `(12)(34)(56)(78)`.
The lemma therefore certifies the all-Z nonadmissibility of its loop
insertions, including the eighteen nine-label cells in the Run 2 catalog.

Scope: this excludes those cells from the modern all-Z tile class. It does
not classify their behavior at each individual positive Z, and does not
turn their canonical-form or degree relations into tile relations.
