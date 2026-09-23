# CP25 base-route kill and C1 Product Barrier continuation

**Date:** 2026-09-21
**Decision:** preserve the base-route `KILL`; retain C1/Product Barrier as `OPEN-NONTRIVIAL`.

## Accepted

- The planned separation “sign + integrality + independent parity-word realizability” is killed: integrality already forces the finite parity word.
- The oriented lift candidate C1 is well-formed for the positive orientation `b=sign(2^m-p^k)`.
- The Product Barrier is a sufficient condition for C1. The reduction is exact and non-circular.
- The remaining core is a bounded, cyclic carry-product inequality.

## Not accepted

- No proof of the Product Barrier.
- No proof of C1.
- No novelty claim.
- No claim excluding nontrivial integer cycles.
- No claim solving Collatz.

## Evidence admitted

- Local exact raw-word C1 scan through `m<=22` for `p=3,5,7`: zero nonintegral premise survivors.
- Local exact Product Barrier scan for `p=3` through `m<=22`: 401,423 nonintegral primitive necklaces, zero falsifiers.
- Local exact Product Barrier scan for every odd `p=3..101` through `m<=16`: 439,934 nonintegral `(p,necklace)` cases, zero falsifiers.
- ChatGPT Web: `OPEN-NONTRIVIAL`; Product Barrier reduction.
- Muse Spark 1.3 proof audit: `OPEN-NONTRIVIAL`; verified `PB => C1` and bounded-carry reduction.
- Muse Spark 1.3 falsifier: `BOUNDED-PASS`; wider ephemeral staircase retained only as agent evidence.
- Jev: `ADVISORY` only; follow-up `needs_lemma=0.67`.

## Literature boundary

Rukhin's dual-radix modular division and prefix/suffix integrality tests are directly relevant prior art (arXiv:1506.07622v8). Before any novelty statement, compare the Product Barrier carry lemma explicitly with that quotient-cylinder machinery.

## Next action

Attempt to prove or falsify the bounded-carry Product Barrier. Prioritize near-resonance words with small `|2^m-p^k|`, where a counterexample is most plausible.

## Canonical report

`research_track/CP25_SIGN_SENSITIVE_CYCLE_PILOT/CP25_C1_LIFT_COHERENCE_REPORT.md`
