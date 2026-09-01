# CP20 Task 8B3 E5 — S1 Integration Decision

## Manager verdict

**[ACCEPTED — E5-S1 EXACT CONDITIONED-GEOMETRIC BRIDGE]**

E5-S1 is accepted as an exact finite representation. E5-S2 through E5-S5 remain open. No compactness, degree-one inherited cone bound, complex local-limit theorem, moving-boundary transfer, nonzero asymptotic coefficient, polynomial lower bound, or Collatz conclusion is accepted.

## Artifact verification

- Final root manifest SHA-256: `b749117b6d5ba508b46add04623e20ac1c884d2632f1c3a103234767d3217870`.
- Complete package SHA-256: `3f28f90b29af3a41e1c679593968e9156e9bc3b0882659ec3b8cfa794e9b930d`.
- Diagnostics SHA-256: `7599085a13d8895509946f94195d25a545084ec9285344dcf664c8f559e1eaa6`.
- Verifier-output SHA-256: `8bbd327d084eb3d3bc381eb075fd787d0b634c167b0c7842f991f9bde2fb667d`.
- Root manifest: 20/20 independently recomputed hashes matched.
- ZIP-internal manifest: 20/20 hashes matched; 21 ZIP entries including the manifest.
- The deterministic verifier was independently rerun read-only and passed.
- The five pre-run files remained byte-identical to the accepted seal.

## Independent mathematical checks

1. The one-row Green coefficient

   \[
   w_{r,n,k}=\frac{r\,n!\,(r+k-2)!}{k!\,(r+n-1)!}
   \]

   follows by finite same-row induction, including the separate `k=0` boundary multiplier.
2. Its mass is exactly `r/(r-1)`. The normalized coefficient is the beta-binomial cotransition

   \[
   q_{r,n}(k)=\frac{\binom{k+r-2}{r-2}}
   {\binom{n+r-1}{r-1}}.
   \]

3. Induction over rows gives the uniform weak-composition average. Conditioning iid geometric variables on their sum is exactly uniform because every composition of `n` has the same probability `b^r a^n`.
4. An independent direct enumeration compared recurrence values with the complete composition-phase average for 60 cases, `2<=r<=7` and `0<=n<=9`; maximum complex error was `2.238e-16`.
5. The positive target denominator is negative-binomial with variance `alpha beta r`; fixed bounded endpoint displacement gives the stated uniform `r^{-1/2}(1+O(r^{-1}))` local scale.
6. Since `h=rN/D`, a bounded nonzero fixed-target limit requires the complex numerator `N` at scale `r^{-3/2}`. The positive local limit alone contains no non-cancellation information.
7. The cyclotomic criterion is accepted only as a finite exact nonvanishing test: if the root-of-unity sum vanished, divisibility by `Phi_{3^r}` would force its coefficient count to be divisible by three. It supplies no quantitative separation and no proved infinite target subsequence.

## Route disposition

- **[PARK]** Absolute-value maximum principles, global invariant cones, and positive-only local-limit arguments.
- **[OPEN]** The exact conditioned-geometric complex numerator.
- **[OPEN]** The uniform `r^{-3/2}` numerator asymptotic and nonzero phase-profile coefficient.

## Authorized next action

Open one proof-led sealed task to derive or refute the uniform complex numerator estimate at `(d,C)=(-8,4)`. The task must first determine an exact analytic normal form—coefficient/Hadamard, Feynman-Kac bridge, coboundary/martingale, or a rigorously equivalent representation—before attempting an asymptotic theorem. No deeper numerical run is authorized.
