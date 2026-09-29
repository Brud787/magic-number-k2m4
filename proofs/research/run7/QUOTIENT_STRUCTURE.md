# What the quotient contains

**COMPUTATIONALLY-VERIFIED.** The following are exact annihilators of the
full preserved local matrices. Group-constant weights were solved over Q;
an independent Fraction implementation reconstructs and checks every
compressed matrix and kernel basis.

| n | dim Q_n | Support-size weights | Core-profile weights | Ambient dihedral weights |
|---:|---:|---:|---:|---:|
|7|15|2|3|3|
|8|103|2|5|11|
|9|472|2|6|35|

Allowing each support set its own profile weights still gives dimensions
3,5,6 in these three cases. Combining these weights with all ambient
dihedral-invariant covectors gives only3,11,35. Thus the tested coarse
statistics do **not** span Q_n*. See the full grouped bases and labels in
[quotient_covectors.json](../../results/run7/quotient_covectors.json).

**PROVED, preserved Run6 input.** Across every n, weights depending only
on the eleven loopless dihedral tile profiles form a six-dimensional
local annihilator. The exact six-parameter table is preserved in
[PROFILE_WEIGHTS](../run6/PROFILE_WEIGHTS.md). The calculations above
show precisely how its visible restrictions grow through n9. They do
not extrapolate arbitrary support-dependent covectors to a six-dimensional
space for all n.

The new structural description is stronger than these coarse statistics:
Q is the simplicial quotient under signed adjacent addition and zero
insertion. Its normalized dimensions are1,9,19,12 in simplicial degrees
5,6,7,8, and zero elsewhere. Consequently Q_n is a direct sum of copies
of those four finite normalized spaces, indexed by increasing surjections.
This is the all-n rank mechanism in [GLOBAL_GENERATION](GLOBAL_GENERATION.md),
subject to its final independent verdict. It does not identify Q_n with
a familiar representation merely from its dimension sequence.

The ordinary augmentation is one covector of Q_n. Once K_n=L_n is proved,
every covector of Q_n descends to the space of all-Z indicator **families**.
Before that theorem, such a descent would have been an unjustified extra
assumption. Nothing here says that every fixed positive Z has the same
indicator kernel, or that coarse covectors alone reconstruct Q_n*.
