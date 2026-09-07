# XUB paired-increment occupation reduction

Date: 2026-09-07

Status: exploratory analytic continuation with exact algebraic components. It is not an E7/B4 result and does not authorize a sealed computation.

## 1. Correct post-crossing suffix

Cut at the exact first-passage time `s` and use the memoryless suffix already established in the XUB first-passage record:

`q(a'_s)^(-1) L_(m-s+1)(a'_s,b)`.

Put `L=m-s+1`, `K=n-c_s(a)`, and `L=2J+epsilon`, where `epsilon` is zero or one. Conditional on the accessible endpoint total `K`, the `L` geometric increments are exactly uniform over weak compositions of `K`; the geometric tilt cancels.

For pair totals `B_j=Y_(2j-1)+Y_(2j)` and, when `epsilon=1`, a final singleton `V`,

`P(B_1=b_1,...,B_J=b_J,V=v | S_L=K) = prod_j(b_j+1) / binom(K+L-1,L-1)`,

on `sum_j b_j+v=K`. Given the totals, the within-pair splits are independent and uniform on `{0,...,b_j}`. These identities are exact.

If the overshoot itself is fixed rather than memorylessly summed, the first fictitious increment cannot be treated as a uniform split. Isolate it and, if needed, one parity increment; pair only complete true-future increments. A globally fixed pair that straddles the crossing seam is invalid.

## 2. Exact pair operator

At pair-entry state `x`, conditional on `B=b`, the split-averaged two-step phase is

`A_b(x) = q(x)/(b+1) * sum_(u=0)^b q(x+u-beta)`,

and the exit state is `x'=x+b-2 beta`, independent of the split. For `b=1`,

`|A_1(x)| = |cos(pi 2^(x-beta))|`.

For `0<eta<=1/2`, call a pair entry white when `dist(2^(x-beta),Z)>=eta`. Every white `B=1` occurrence contributes at most `exp(-c_eta)`, where `c_eta=-log cos(pi eta)>0`. If `N_eta` counts white `B=1` occurrences, split averaging therefore gives the exact modulus bound `exp(-c_eta N_eta)`.

## 3. Raw B=1 symbols are not scarce

Ignoring arithmetic whiteness, the microcanonical bridge has linearly many `B=1` symbols in the central-slope regime. Tilt pair totals by

`P_t(B=b)=(b+1)(1-t)^2 t^b`, with `t=K/(K+2J)`.

Conditioning on the total removes the tilt factor. If `K/J` remains in a compact subinterval of `(0,infinity)`, then `P_t(B=1)=2(1-t)^2t` is uniformly positive. A uniform lattice local-limit lower bound for the total costs only `O(sqrt(J))`; hence, for fixed `lambda>0`,

`E[exp(-lambda N_1) | total=K] <= C sqrt(J) exp(-cJ)`.

The same estimate survives the optional terminal singleton after summing it. The exact reduction and tilt calculation are proved here; a publication-level use should spell out the uniform local-limit constant.

There is also an exact next-pair hazard. With `R` raw increments and remaining sum `K_rem`,

`P(B_next=1 | history,endpoint) = 2(R-1)(R-2)K_rem / ((K_rem+R-1)(K_rem+R-2)(K_rem+R-3))`.

Thus this hazard is uniformly positive in any regular cone `0<a<=K_rem/R<=b<infinity` away from finite endpoint exceptions.

## 4. Reduction to white opportunities

Let `W_eta` count predictable pair entries in a regular central bridge region whose current phase is white, and let `N_eta` count those entries at which `B=1` also occurs. If the regular-cone hazard is at least `p_*>0`, an exponential supermartingale gives, for every `w>=0`,

`E[exp(-c_eta N_eta) | endpoint] <= exp(-kappa_eta w) + P(W_eta<w | endpoint)`,

where `kappa_eta=-log(1-p_*(1-exp(-c_eta)))>0`.

Consequently, linear white occupation is unnecessary. It suffices to prove, uniformly on the actual accessible coupled central arrays and with both parity alignments handled,

`P(W_eta^reg < A log m | endpoint and exact first-passage data) <= C/m`,

for a fixed `A>1/kappa_eta`. This is the new load-bearing estimate.

## 5. Arithmetic dynamics

Writing `theta_j=2^(x_j-beta)`, pair totals drive

`theta_(j+1)=theta_j 2^(B_j) 4/9`.

In particular `B=1` multiplies `theta` by `8/9`. On the actual boundary starts, these phases have growing powers of three in the denominator. The unresolved question is therefore quantitative avoidance of near-integer ternary residues along a conditioned negative-binomial pair-total bridge, not scarcity of the raw symbol `B=1`.

## Classification

- uniform-composition and pair-total laws: `[PROVED]`;
- conditional uniform split and exact pair operator: `[PROVED]`;
- exact hazard identity: `[PROVED]`;
- central-slope exponential abundance of raw `B=1`: `[PROVED WITH STANDARD UNIFORM-LLT INPUT]`;
- supermartingale transfer from white opportunities to contraction: `[PROVED]`;
- logarithmically many white opportunities on the actual coupled arrays: `[OPEN — LOAD-BEARING]`;
- XUB, E6-N2/B4, a nonzero profile, polynomial lower bounds, and Collatz: `[OPEN / NOT PROVED]`.

