# The exact circuit-set proposal fails

**FAILED.** The supports of the single-parent rows cannot be the complete
circuit set of a matroid, already at n7. In the preserved21-column order,
the first two parent supports are

\[
C_1=\{15,16,17,18,19,20\},\qquad
C_2=\{4,11,12,13,14,20\}.
\]

Their common element is20. None of the seven parent supports is contained
in (C_1∪C_2)\{20}. This violates unsigned circuit elimination if these
seven supports are declared to be **all** circuits. The literal rows,
all seven supports, and the exact ten-term elimination vector are in
[circuit_elimination_failure.json](../../results/run7/circuit_elimination_failure.json).
The eliminated relation is balanced and already lies in L7.

This does not disprove a matroid with additional circuits. Indeed any
realization matrix for V_n/L_n defines a representable matroid with
dependency space L_n; that construction simply encodes the quotient.
It cannot establish equality with the geometric kernel without a new
argument. Nor are tilings bases in that realization: their sizes6,20,50
differ from quotient ranks15,103,472. Ordinary matroid basis exchange
therefore does not give the required tiling connectivity or generation.

**PROVED in the separately audited main argument.** The useful module
structure is simplicial under signed column addition and zero insertion.
Its exact normalization replaces the failed assertion about a complete
list of matroid circuits. No oriented-matroid axiom is invoked metaphorically.
