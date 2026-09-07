# Prefix-bridge exact numerical probe - REPORT

Status: **[NUM] exploratory numerical evidence only.** Nothing here is a theorem, a proof,
an asymptotic statement, or a canonical result. The range is finite (r <= 600). This report
was written by the research-manager session from the completed data files after the producing
agent was interrupted by a rate limit; the data, scripts and raw stdout are unmodified.

## What was computed

Exact transfer-matrix DP over residues with complex128 accumulation, at the critical target
n_r = floor(beta*r) - 8, beta = log2(3) - 1, for every r from 14 to 600 (587 values):
|G_r|, the exact four-prefix mixture, D_j, H_{r-4,n_r-j}(j), the weights w_{r,n}(j), the
truncated triangle-weighted sum S_r at delta = 0.5 and delta = 1, and the full untruncated
triangle sum.

Implementation verification (VERIFICATION.json): mixture identity against direct DP over 338
cases (r in [5,30], n in [0,12]), max discrepancy 4.97e-16; brute-force enumeration of all
1161 paths for r in [5,8], n in [0,4], max discrepancy 5.98e-16; independent brute force of H
and D, max discrepancy 1.19e-15; exact weight normalisation sum_j w(j) = 1 with zero float
error. The mpmath 30-digit cross-check (MPMATH_CROSSCHECK.json) covers 34 items with max
deviation 2.5e-16 from double precision, well inside the 1e-9 tolerance. Runtime 144 s.

## Finding 1 - r|G_r| is bounded on the computed range

| r band | min r*abs(G_r) | max r*abs(G_r) | mean |
|---|---|---|---|
| 14-50 | 14.000 | 27.706 | 23.637 |
| 51-150 | 21.586 | 27.417 | 24.292 |
| 151-300 | 19.770 | 23.799 | 21.589 |
| 301-450 | 19.081 | 22.170 | 20.499 |
| 451-600 | 18.729 | 21.483 | 20.066 |

Least-squares slope of log|G_r| against log r: -1.125 on [100,300], -1.066 on [300,600],
-1.080 on [200,600]. The product r|G_r| drifts slowly downward (mean 24.29 on [51,150] to
20.07 on [451,600]) rather than growing.

[NUM] On 14 <= r <= 600 the data is consistent with |G_r| of order 1/r with a constant near
20. That is consistent with the OPEN target E6-N2, |E[F_{r,4} | S_r = n_r]| = O(1/r), but
proves nothing: a log-power correction or a change of regime beyond r = 600 is not excluded,
and the descriptive slope is slightly steeper than -1.

## Finding 2 - the triangle-weighted route loses only a constant factor

Ratio S_r / |G_r| for r >= 50: min 1.1786, max 1.1939, mean 1.1853.

Magnitude-weighted phase coherence, |sum_j w D_j H_j| / sum_j w |D_j| |H_j|, computed directly
from WINDOW_TABLE.csv: 0.8388 at r = 100, 0.8441 at r = 300, 0.8462 at r = 600 - stable and
slowly rising. Its reciprocal (1.192, 1.185, 1.182) reproduces the S/|G| ratio exactly.

[NUM] Cancellation BETWEEN prefix classes is worth a bounded factor of about 1.18, not an
r-dependent gain. Consequence for the research plan: on this range the TRIANGLE-WEIGHTED
LOGARITHMIC-PREFIX CANCELLATION LEMMA of derivation section 6 is numerically equivalent in
size to the original signed problem. The derivation and the independent audit both describe it
as a strictly stronger sufficient condition that discards cancellation between prefix classes;
the data shows there is little such cancellation to discard. This does not refute either
document - sufficiency holds either way - but it bears directly on whether the route reduces
difficulty, and neither document claims it does.

## Finding 3 - the logarithmic cutoff is numerically inactive

The ratio of the full untruncated triangle sum to the truncated S_r is 1.00000000 to eight
decimals for every r >= 50 at both delta = 0.5 and delta = 1, and the weight mass inside the
window is 1.0000000000. At r = 600 the window is j <= 39 while n_r = 342, so truncation is
formally active but contributes nothing measurable.

[NUM] The rigorously proved prefix-excess cutoff lemma is a technical convenience here rather
than a load-bearing estimate: the weights already concentrate on j <= 5.

## Finding 4 - each prefix class obeys its own 1/r law, and uniform-H looks true

r*|H_{r-4,n_r-j}(j)| by class, read from WINDOW_TABLE.csv:

| j | r=100 | r=300 | r=600 |
|---|---|---|---|
| 0 | 46.11 | 46.30 | 48.49 |
| 1 | 37.43 | 34.90 | 35.93 |
| 2 | 28.36 | 24.41 | 24.69 |
| 3 | 19.56 | 15.44 | 15.31 |
| 4 | 11.90 | 8.54 | 8.30 |
| 5 | 6.19 | 4.01 | 3.81 |
| 6 | 2.58 | 1.50 | 1.39 |
| 7 | 1.68 | 0.86 | 0.77 |

| r band | min max_j abs(H_j) | max max_j abs(H_j) | min r*max | max r*max |
|---|---|---|---|---|
| 151-300 | 0.15015 | 0.32127 | 43.82 | 49.28 |
| 301-450 | 0.09730 | 0.16043 | 43.34 | 49.09 |
| 451-600 | 0.07279 | 0.10761 | 43.12 | 48.75 |

[NUM] The per-class constants are stable in r: about 46-48 for j=0, 35-36 for j=1, 24.4-24.7
for j=2, 15.3-15.4 for j=3, 8.3-8.5 for j=4, 3.8-4.0 for j=5, then decaying fast. The maximum
over the window, r*max_j|H_j|, stays within 43.1-49.3 for all r >= 151. So the sufficient
condition sup_{j <= L_r} |H_{r-4,n_r-j}(j)| = O(1/r), which implies the triangle bound and
hence the E6-N2 target, is numerically supported with a constant near 46, roughly twice the
constant seen in |G_r| itself. The chain uniform-H => triangle bound => G = O(1/r) is
numerically coherent end to end on this range. All three steps remain OPEN as mathematics.

## Finding 5 - a theta_r dependence not previously recorded

Pearson correlation between theta_r = frac(beta*r) and r|G_r| over r >= 200: 0.8278.
Values of r|G_r| run from about 18.7 at theta near 0 to about 23 at theta near 1.

[NUM] The residual oscillation of r|G_r| is largely explained by the fractional part of beta*r,
that is by where the integer target n_r = floor(beta*r) - 8 sits relative to the real line
beta*r. This is the endpoint-offset drift named in derivation section 4, now measured. Two
consequences for a proof attempt: any constant in an upper bound must be uniform over theta,
and any future nonzero-coefficient or lower-bound claim must be stated as a function of theta
rather than as a single limit, since beta is irrational and theta_r equidistributes.
Separately, arg(D_j H_j) per class is stable and converging in r (class j=0: 1.1033 at r=100,
1.3054 at r=300, 1.3347 at r=600), which suggests a limiting phase profile.

## What this does NOT establish

No bound is proved. |G_r| = O(1/r) (E6-N2) remains [OPEN]. The triangle-weighted lemma remains
[OPEN]. The uniform-H estimate remains [OPEN]. No nonzero coefficient, no lower bound and no
asymptotic is established. No curve fitting was used to claim an exponent; the least-squares
slopes above are descriptive statistics over a finite range. r <= 600 is small for a statement
about r -> infinity.

Nothing in this probe proves any bound or the Collatz conjecture.
