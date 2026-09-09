# CP20 TASK 8B3 — E1 HIGH-CONDUCTOR REQUIRED DECAY

**Status:** `[EXACT SUFFICIENCY CALCULATION]` + `[OPEN]` existence theorem.

For `t>T`, the same conductor-wise Fourier-kernel L1 bound yields

`E_high <= 3^(-r) sum_(t>T) poly(t) 3^t sup_(cond=3^t)|phi|`.

The target short-interval scale is `2^((b-alpha+o(1))r)`.

## Model 1: uniform-in-high-block exponential rate
If `|phi| <= 2^(-delta r)` uniformly for all `t>T`, then

`E_high <= poly(r) 2^(-delta r)`.

A strict sufficient condition is

`delta > alpha-b`.

## Model 2: conductor-proportional rate
If `|phi| <= 2^(-c t)`, then the exponent to maximize over `s=t/r in [tau,1]` is

`-alpha + (alpha-c)s`.

A strict sufficient condition is again

`c > alpha-b`.

(If `c>=alpha`, the bound is automatically stronger.)

## Model 3: mixed rate
If

`|phi| <= 2^(-c t - d(r-t))`,

then it suffices that

`max_(s in [tau,1]) [(alpha-c)s - d(1-s)] < b`.

If the slope `alpha-c+d >= 0`, this reduces to `c>alpha-b`.
If the slope is negative, it reduces to

`tau(alpha-c) - d(1-tau) < b`.

## Required rates by interval exponent
- b=0.80: delta_min/c_min > 0.784963
- b=1.00: delta_min/c_min > 0.584963
- b=1.20: delta_min/c_min > 0.384963
- b=1.35: delta_min/c_min > 0.234963
- b=1.45: delta_min/c_min > 0.134963
- b=1.52: delta_min/c_min > 0.064963

## Compatibility with E0 and numerics
The E0 obstruction lies at fixed conductor `t=1`, which is placed in the low block; therefore it does not contradict a high-conductor theorem.

Finite structured primitive data are adversarial for a uniform O(1) mass band. For offset d=-3, observed base-2 rates `-log2|phi|/r` at r=13..18 are approximately:
0.1014, 0.0872, 0.0985.
These finite rates are above the requirement for b=1.52 (`alpha-b≈0.06496`) but far below the requirement for b<=1.45. This is numerical evidence only, not an asymptotic obstruction.
