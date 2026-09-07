# Independent audit of the XUB symbolic-block theorem

Date: 2026-09-07

Verdict: `[REPAIR, THEN PASS]`.

The audit independently re-derived and accepted the exact microcanonical pair/singleton law, conditional probability generating function, saddle tilt, Bernoulli block law before endpoint conditioning, conditional Chernoff bound, uniform Stirling denominator, actual G/H centrality identity, logarithmic block abundance, critical/supercritical fixed-grid absence, and the parity singleton factor.

Four repairs were required and incorporated into `XUB_SYMBOL_BLOCK_THEOREM.md`:

1. `log` is natural, `ell>=1`, `K>=1`, and `R` is two-sided comparable to `m`.
2. The abundance constants are existential and depend on the fixed parameters; one arbitrary constant cannot serve both the threshold and exponential rate.
3. Absence at and above the critical block length uses an explicit remaining-endpoint local-mass ratio. The crude `sqrt(R)` conditioning bound is insufficient for the sharp threshold.
4. A length-`ell` useful block with all `ell` entry states black supplies only `ell-1` black-to-black transitions. The correct alternative is therefore a white contracting entry or `9^(ell-1)` amplification. A claim of `9^ell` would require a separately defined guard symbol.

After these repairs the symbolic theorem and its seam-safe consequence pass. The audit does not establish arithmetic whiteness, conditioned resonance rarity, the low-state estimate, XUB, or Collatz.
