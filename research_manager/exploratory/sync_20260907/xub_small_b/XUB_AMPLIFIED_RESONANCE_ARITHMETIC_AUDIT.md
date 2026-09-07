# Arithmetic audit of amplified ternary resonance

Date: 2026-09-07

Verdict: `[PASS FOR THE DETERMINISTIC IMPLICATION / OPEN FOR CONDITIONED RARITY]`.

Writing `N=D+2L`, the amplified event means that the centered residue of `2^E modulo 3^N` satisfies

`0<|r_N(E)|<eta*3^D`.

It is automatically impossible only when `eta*3^D<=1`. The rational-grid lower bound `3^(-N)` is otherwise too weak by a factor `eta*3^D`.

The divisibility lemma gives a stronger size obstruction: a positive `L`-step bounded-symbol black run requires its initial nearest integer to satisfy `n_0>=9^L`, hence `z_0>=9^L-eta`. At the original actual boundary start `z_0=2^(1-{beta*t})` lies in `(1,2)`, so the nearest integer is one or two. Therefore even one bounded-symbol black-to-black transition is impossible at that original start.

This gain does not automatically propagate to later run starts. A preceding large pair total can raise the state, invalidate the fixed bounded-symbol threshold across that step, and produce a much larger new nearest integer. The `n_0=0` low-state case is also genuinely separate: divisibility is vacuous and repeated zero symbols can remain black with `|A_0|=1`.

The multiplicative order `ord_(3^N)(2)=2*3^(N-1)` does not settle the required short accessible exponent range `E=O(m)`. Full-period equidistribution is unavailable, and endpoint conditioning makes the exponent path-dependent.

There is no unconditional arithmetic impossibility. For example, with `E=2*3^(N-1)`, LTE gives `2^E=1 mod 3^N`, producing the minimum positive centered residue. These exponents are far outside the actual accessible linear range, so this is not an in-domain counterexample; it refutes only an overbroad denominator- or coprimality-based claim.

The correct open target is a conditioned weighted count over actual run-start indices `j`, actual exponents `E_j,D_j`, the microcanonical endpoint law, exact first-passage data, and predeclared bounded-positive blocks. It must separately control:

1. low-state nearest integer zero;
2. positive amplified resonance;
3. large-symbol interruptions;
4. parity and short-suffix seams.

A bare Diophantine inequality for arbitrary `E,D,L` is neither sufficient nor the correct probabilistic object. No XUB or downstream theorem follows from this audit.
