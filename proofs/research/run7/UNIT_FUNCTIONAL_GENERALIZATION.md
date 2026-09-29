# Finite weights and the uniform augmentation functional

**COMPUTATIONALLY-VERIFIED.** The saved n8 and n9 weights were rechecked
with exact Fraction arithmetic. They still give unit value on every
tile column and total values20 and50. Their source metadata are recorded
in [unit_weight_probes.json](../../results/run7/unit_weight_probes.json).

The particular saved weights are not functions of their witness seed's
core profile, support set, inverse family, or ambient dihedral orbit.
Concrete pairs with identical metadata but different weights are saved
for each failed proposal. For example rows0 and20 at n8 have the same
source profile and unequal weights; rows0 and9 do so at n9. Every source
profile present in either certificate contains conflicting weights.
These tests kill those formulas for the **saved** weight vectors, not
all possible alternative witness sets or signed valuations.

All103 n8 witnesses and all472 n9 witnesses have distinct complete
four-bracket sign strings. Therefore fitting a function of that string
to these finite weights is vacuous: the data have no repeated sign-string
constraint. No bracket formula or Parke–Taylor deformation is inferred.

**PROVED consequence of the audited global theorem.** Let I_n denote the
span of all-Z tile-indicator families in the product of constructible
function spaces over positive Z, each modulo dimension≤7. Kernel equality
identifies I_n with Q_n. Hence

\[
W_n\left(\sum_S a_S[\mathbf1_{T_S(\cdot)}]\right)=\sum_S a_S
\]

is well-defined and linear: two expressions differ by K_n=L_n, and every
local generator has augmentation zero. Every tile family has weight1.
The amplituhedron family has a BCFW expression with
M(2,n−6,2) terms, giving that value independently of an arbitrary tiling.
Linearity gives additivity for decompositions expressed in this space.

This is an algebraically defined uniform functional on **all-Z families**.
It is not an explicit new rational formula in one target Y, nor a claim
that the saved finite lambda vectors restrict naturally under deletion.
The decisive proof is kernel generation; defining augmentation on Q_n
alone would not have established well-definedness on I_n.
