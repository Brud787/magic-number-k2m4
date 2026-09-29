# Six profile-constant covectors of the local quotient

**PROVED, exact small computation plus transport.** The space of weights
depending only on the eleven admissible dihedral source-core types and
annihilating every Run4 parent relation has dimension six. This statement
holds for arbitrary n because every parent relation is transported from
one of the fifteen prototypes, and transport preserves each child's
loopless dihedral class profile.

These are covectors of the **formal local quotient** V_n/L_n. They are
not asserted to be valuations on arbitrary image-indicator classes or
conserved quantities of every tiling for arbitrary n. Those statements
require respectively K_n⊆L_n or D_n⊆L_n.

## Complete small matrix

For each of the fifteen balanced Run4 parent prototypes, sum its signed
coefficients separately within each of the eleven admissible tile types.
The resulting integer matrix P has size15×11 and rank5. A saved5×5 minor
has determinant−1. Independent Fraction elimination and rational RREF
agree. The six integer kernel vectors displayed by the parameter formula
below are independent and annihilate P, establishing the upper bound as
well. Each term retains its original source affine label, coefficient,
and independently checked dihedral class type in
[profile_weights.json](../../results/run6/profile_weights.json).

The twelve collapsed and two hostile parent types have zero admissible
relation space by Run4, so they impose no missing linear condition.
Thus this calculation is complete for profile-constant covectors on the
specified local relation space. It does not assert completeness for more
general label-dependent covectors.

## The full six-parameter family

Every solution, and only a solution, has the following values, where
a,b,c,d,e,f are arbitrary real numbers:

| Dihedral tile type | Weight |
|---|---|
| (1,1,1,1,1,1) | a |
| (1,1,1,2,2) | b+2c−e−f |
| (1,1,2,1,2) | b−c−d+e+f |
| (1,1,3,3) | b |
| (1,2,2,3) | −c+e+f |
| (1,2,3,2) | c |
| (1,3,1,3) | d |
| (1,4,4) | f |
| (2,3,4) | f |
| (3,3,3) spurion | e |
| (5,5) | f |

For integer weights the six parameters are integers because they are
the weights of six listed tile types themselves. Thus the saved six
vectors form an integral basis of this profile-constant annihilator,
not merely a rational spanning family.

Taking all six parameters equal to one gives the ordinary unit covector.
Taking only a=1 gives the count of six-support singleton tiles, formally
unchanged by every local relation. This does not by itself show that all
complete tilings have the same number of those tiles.

## The high-support pattern and its necessary extension

Set e=−1,f=1 and a=b=c=d=0. The resulting covector is

\[
h(T)=\begin{cases}
1,&\text{type }(1,4,4),(2,3,4),\text{ or }(5,5),\\
-1,&\text{type }(3,3,3),\\
0,&\text{all seven smaller types}.
\end{cases}
\]

**PROVED local statement.** Every transported Run4 relation annihilates
h. The +1 on the ten-support (5,5) type is forced by the larger-support
merger prototypes. Omitting that entry would fail those prototype rows.
Thus the observed n9 high-support pattern has an exact all-n *local*
extension, without any n10 global matrix computation.

For the standard n9 BCFW collection, the eleven profile counts in table
order are

\[
(10,10,16,4,4,0,4,1,1,0,0).
\]

Consequently h has total2 there. By the separately audited n9 indicator/generation
theorem D9⊆L9, every complete all-Z n9 tiling satisfies

\[
\#\{\text{loopless BCFW tiles}\}
-\#\{\text{spurion tiles}\}=2.
\]

This finite consequence explicitly depends on global generation at n9;
the prototype compression alone does not prove it. On the six basis
weights obtained by setting one parameter to one, the standard n9 values
are10,30,0,−12,10,12. Any transfer of those values to arbitrary tilings
must cite the same finite generation theorem.

## Kill-tests and limitation

A genuine global indicator relation with nonzero pairing against one of
these weights would show that this local covector does not descend to
the global indicator quotient. A complete-tiling difference with nonzero
pairing would kill local generation at that n. Neither outcome follows
from a hypothetical source boundary chain. Conversely, the existence
of these six covectors does not prove that all global relations are
balanced or locally generated.

This bounded calculation uses only the15 archived prototypes,11 finite
core types, and a known standard n9 tiling. It introduces no larger-n
global relation matrix or exhaustive tiling search. Implementation and
tests are [run6_profile_weights.py](../../src/magic_number/run6_profile_weights.py)
and [test_run6_profile_weights.py](../../tests/test_run6_profile_weights.py).
