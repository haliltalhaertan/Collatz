# Independent zero-trust audit of the BLL theorem application

Date: 2026-09-07

Verdict: **`[PASS WITH SCOPE REPAIRS — BLL/KUB CLOSED FOR FIXED-START ARRAYS]`**

Audited object: `BLL_THEOREM_APPLICATION.md`, checked independently against the project definitions and the published primary source.

## Checks

1. **Correct process:** PASS. The theorem is applied to the reflected walk `R=-X`, whose increment is `beta-Y`.
2. **Shifted lattice:** PASS. The maximal parameters are `(h,c)=(1,beta)`. Writing `c=-beta` after reflection would be wrong.
3. **Centering and scale:** PASS. `E(beta-Y)=0`, `Var(beta-Y)=alpha*beta`, and `a_m=sqrt(alpha*beta*m)` is valid.
4. **Positivity convention:** PASS. The project's `X_t<=0` event maps to weak nonnegativity of `R`; the matching kernel is `q_m^+`. Strict positivity is not silently substituted.
5. **G accessibility:** PASS. With `m=r`, `y_r-x_G=m*beta-n_r`.
6. **H_0 accessibility:** PASS. With `m=r-4`, `y_r-x_H=m*beta-n_r`; retaining the index `theta_r` is harmless because the theorem allows any accessible triangular endpoint sequence.
7. **Uniform regime:** PASS. Both starts are fixed and `y_r` lies in a fixed compact positive interval, hence `x,y=o(a_m)`.
8. **Theorem statement:** PASS. Proposition 4.1, equation (4.5), explicitly covers the general `(h,c)`-lattice setting and is uniform in the required small-endpoint regime.
9. **BLL inference:** PASS. Compact boundedness of the renewal factors yields `p_m^0=O(m^(-3/2))` on the accessible arrays.
10. **KUB inference:** PASS. Combining BLL, the free `m^(-1/2)` lower bound, and exact modulus domination gives `|K_m^0|=O(m^(-1))`.

## Binding scope repairs

- Do not say the bound holds for arbitrary continuum values of `theta`; inaccessible conditioning events are undefined or zero by convention. State it on the actual accessible arrays.
- State the result asymptotically, with finite admissible indices absorbed separately if a global constant is desired.
- Distinguish degenerate `r=14,15` from the nondegenerate range `r>=16`.
- Restrict the conclusion to the two fixed starts and barrier zero.
- Do not extend it to the full `j`-dependent PWE window.
- Do not infer the crossing bound, a complex asymptotic coefficient, nonvanishing, E6-N2/B4, or Collatz.

## Route decision

The prior conditional label on KUB is discharged. The next load-bearing estimate for the selected killed/crossing decomposition is

```text
XUB: sup over the actual accessible arrays of
| E_a[ product_(t=0)^(m-1) q(X_t); tau_0<=m | X_m=b_r ] |
<= C/m.
```

This is not a positive ballot estimate: the crossing probability may be large, so XUB requires genuine complex/arithmetic cancellation or a different direct representation. XUB is sufficient for this splitting route, not logically necessary for every possible proof route.

Nothing audited here proves Collatz.
