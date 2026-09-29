# The finite n9 unit functional

**PROVED, independently audited.** The saved rational vector lambda has472 entries and
satisfies exactly

\[
 A_9^T\lambda=\mathbf1_{942},\qquad \sum_i\lambda_i=50.
\]

The selected indicator minor has determinant4. All weights are integers
or half-integers;177 are negative and70 are zero. The solve is over Q,
and every one of the942 column weights is checked independently with
Python Fraction arithmetic. The [machine vector](../../results/run6/unit_functional_n9.json)
contains every coefficient.

On the span of tile indicator classes, evaluate each function by its
constant value on the corresponding certified open witness neighborhood.
These evaluations are well-defined modulo lower-dimensional sets.
Their lambda-weighted sum assigns one to each tile. Every complete
all-Z tiling gives A9 chi=1, so its cardinality is50.

The normalization is checked three ways: the MacMahon triple product
M(2,3,2), the Narayana expression (1/6)binom(6,2)binom(6,3), and finite
plane-partition enumeration all give50. The independently source-certified
standard BCFW collection has50 labels and satisfies every saved equation.
This normalization does not assume arbitrary tilings already have50 tiles.

## Comparison and limits

At n8 the chosen103-neighborhood functional had30 negative weights,
denominators at most2, and total20. At n9 the chosen472-neighborhood
functional has177 negative weights, denominators at most2, and total50.
These similarities are exact properties of the chosen finite certificates.
They do not identify a canonical bracket formula or an n-uniform weight.
The witness sets depend on source seeds and pivot choices. There is no
proved restriction map taking this lambda9 to the saved lambda8.

A linear functional on the local quotient V_n/L_n is already supplied
by augmentation because every local row is balanced. Making it a
functional on actual indicator classes requires that it annihilate all
of K_n; making it constant only on complete tilings requires the weaker
annihilation of D_n. Those missing assertions must not be replaced by
naming the quotient functional.

**CONJECTURAL.** An explicit n-uniform signed-neighborhood or bracket
functional with unit value on all eleven membership cores. A new core
weight differing from one, failure of additivity, or a certified
unbalanced indicator relation kills the universal unit-functional route.
Only unequal complete tilings would disprove Magic Number itself.
