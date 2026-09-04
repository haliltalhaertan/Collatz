# CP20 THEOREM INVENTORY

## Publication branch: factor complexity / pressure / critical-site density

Status: `[POST-AUDIT EDITORIAL REPAIRED — NO NEW MATHEMATICS]`

Notation throughout:

- `alpha = log_2 3`;
- `n_{k+1}=(3n_k+1)/2^{a_k}` is a positive odd-only Syracuse orbit;
- `A_k=sum_{i<k}a_i`;
- `F_k=floor(alpha k)`;
- `s_k=F_k-A_k`;
- `p_a(r)` is the number of distinct length-`r` factors of the valuation word;
- global critical-log hypothesis: `s_k=kappa log_2 k+O(1)`, `kappa>1`;
- `g_k=F_{k+1}-F_k in {1,2}`.

## T1 — Polynomial ordinary-state bound

**Status:** `[PROVED][AUDITED][FROZEN]`  
**Source:** Task 6 V3.

Under the critical-log hypothesis,

`n_k = O(k^kappa)`.

The condition `kappa>1` is load-bearing because the normalized affine carry series is summable only in that regime.

**Publication role:** lemma supporting the factor-spacing contradiction.

## T2 — Repeated-factor spacing

**Status:** `[PROVED][AUDITED][FROZEN]`  
**Source:** Task 6 V3.

If the same length-`r` valuation factor `W` occurs at positions `u<v`, subtraction of the exact affine word maps gives

`2^{A(W)} | (n_v-n_u)`.

Under the critical-log hypotheses, equality `n_u=n_v` would force eventual periodicity and hence a rational limiting valuation average, contradicting `A_k/k -> alpha` with `alpha` irrational. Therefore

`|n_v-n_u| >= 2^{A(W)}`.

**Publication role:** arithmetic separation mechanism.

**Novelty caution:** repeated-factor divisibility as a general Collatz mechanism is not to be advertised as new; close prior versions occur in earlier work and in Witteveen 2026. In particular, Witteveen's `3^r` endpoint divisibility and the present `2^{A(W)}` start-value divisibility are dual coprime consequences of the same affine subtraction identity.

## T3 — Local valuation mass

**Status:** `[PROVED][AUDITED][FROZEN]`  
**Source:** Task 6 V3.

In the counting windows `u>=r`,

`A(u,r)=A_{u+r}-A_u >= alpha r-C`

for a fixed constant `C`.

**Publication role:** converts repeated factors into exponentially large ordinary-state separation.

## T4 — Exponential factor-complexity lower theorem

**Status:** `[PROVED][AUDITED][FROZEN]`  
**Source:** Task 6 V3.

For every fixed `epsilon` satisfying

`0 < epsilon < alpha/kappa`, 

the exponentially long start window

`N_r=floor(2^{(alpha/kappa-epsilon)r})`

contains asymptotically distinct length-`r` factors. Hence

`liminf_{r->infinity} log_2 p_a(r)/r >= alpha/kappa`.

The theorem is independent of any valuation-alphabet bound.

**Publication role:** first principal theorem.

## T5 — Zero-critical weighted-pressure upper theorem

**Status:** `[PROVED][AUDITED][FROZEN]`  
**Sources:** Task 6 strengthened V3; Task 7 V3.

Let `B>=3` be finite. Assume

`1 <= a_k <= B`

for every `k`, and zero-criticality

`a_k != g_k`

for every `k`. Define

`h_B = inf_lambda [(2-alpha) log_2(sum_{a=2..B} exp(lambda(1-a))) + (alpha-1) log_2(sum_{1<=a<=B,a!=2} exp(lambda(2-a)))]`.

Then

`limsup_{r->infinity} log_2 p_a(r)/r <= h_B`.

The proof uses:

- the exact defect identity `sum d_i=s_{u+r}-s_u`;
- the critical-log `O(log r)` defect band;
- the coefficient inequality `N(S)<=P(t)t^{-S}`;
- Sturmian balance and the `r+1` phase-factor count.

**Publication role:** second principal theorem.

## T6 — Finite-alphabet entropy-pressure obstruction

**Status:** `[PROVED][AUDITED][FROZEN]`  
**Sources:** Task 6 strengthened V3; Task 7 V3; combination with T4.

Under the finite-`B` hypotheses of T5 (`B>=3`, `1<=a_k<=B`, pointwise zero-criticality) and the critical-log hypothesis, combining T4 and T5 gives

`alpha/kappa <= h_B`,

therefore

`kappa >= alpha/h_B`.

Certified special case: under the `B=3` hypotheses (`1<=a_k<=3`, zero-critical, critical-log),

`kappa > 3.027`.

## T7 — Uniform no-a-priori-alphabet-bound obstruction

**Status:** `[PROVED][AUDITED][FROZEN]`  
**Source:** Task 7 V3.

For the formal `B=infinity` envelope, the partition sums converge for `lambda>0` and exact interval arithmetic certifies

`h_infinity < 56931/100000`,

hence

`alpha/h_infinity > 348/125 = 2.784`.

Thus every zero-critical positive ordinary critical-log Syracuse orbit satisfies

`kappa >= alpha/h_infinity > 2.784`.

Informational high-precision value:

`alpha/h_infinity ≈ 2.78401090300090189`.

**Wording requirement:** say “without an a priori valuation-alphabet bound,” not “unbounded valuations.” The critical-log law itself forces bounded defects along a fixed trajectory.

## T8 — Critical-site density pressure surface

**Status:** `[PROVED][AUDITED][POST-AUDIT REPAIRED][FROZEN]`  
**Source:** Task 8A V3 + final freeze decision.

A critical site satisfies `a_k=g_k`.

Type 1: `g_k=1,a_k=1`.  
Type 2: `g_k=2,a_k=2`.

Let

`M_1=2-alpha`, `M_2=alpha-1`,

and define the feasible region

`F={(rho_1,rho_2): 0<=rho_1<=M_1, 0<=rho_2<=M_2, rho_1-rho_2>=M_1-M_2}`.

Put `P=M_1-rho_1`, `Q=M_2-rho_2`,

`A(t)=1/(t-1)`, `B(t)=t+1/(t-1)` for `t>1`,

and

`E_i(rho_i)=M_i log_2 M_i -(M_i-rho_i)log_2(M_i-rho_i)-rho_i log_2 rho_i`.

Then

`h(rho_1,rho_2)=E_1+E_2+inf_{t>1}[P log_2 A(t)+Q log_2 B(t)]`

on `F`.

For every audited Task-6 scale family

`N_r=floor(2^{(alpha/kappa-epsilon_r)r})`,

with

`0 < epsilon_r < alpha/kappa`,

`epsilon_r->0`, and `r epsilon_r->infinity`, every accumulation point `rho` of the multiplicative-window type-critical density pair lies in `F` and satisfies

`h(rho)>=alpha/kappa`.

**Publication role:** third principal theorem.

## T9 — Natural-density corollary

**Status:** `[PROVED][AUDITED][FROZEN]`.

If global natural type-critical densities exist, their vector `rho` lies in `F` and satisfies

`h(rho)>=alpha/kappa`.

## T10 — Zero critical-density corollary

**Status:** `[PROVED][AUDITED][FROZEN]`.

If only

`#{k<N : a_k=g_k}=o(N)`,

then pointwise zero-criticality is unnecessary and the same threshold follows:

`kappa >= alpha/h_infinity > 2.784`.

This is a strict hypothesis-form strengthening of T7.

## T11 — Certified minimum critical-density requirements

**Status:** `[CERTIFIED NUM][FROZEN COROLLARY]`.

Define

`rho_min(kappa)=inf{rho_1+rho_2 : rho in F, h(rho)>=alpha/kappa}`.

Frozen interval certificates give

- `rho_min(1.06) in [0.3462262370615603636914, 0.3462262370615928578729]`;
- `rho_min(1.5) in [0.0916083301662531377156, 0.0916083301662716819078]`;
- `rho_min(2.0) in [0.0314445508714800107814, 0.0314445508714920087543]`.

**Publication role:** quantitative phase-diagram examples, not substitutes for the exact theorem.

## T12 — CP19 endpoint consistency

**Status:** `[PROVED][AUDITED][FROZEN]`.

Maximizing `h` over the feasible density region recovers the older unrestricted CP19 Task-4 entropy exactly. There is no strict optimized “Sturmian phase cost.”

**Publication role:** internal consistency check / contextual corollary; not a headline novelty claim.

# Post-audit extraction note

The 2026-09-04 independent zero-trust publication audit returned `[PASS WITH EDITORIAL REPAIRS]`. This file incorporates the blocking extraction repairs without adding mathematics: T4 now carries the exact `0<epsilon<alpha/kappa` range; T5 restores the finite-alphabet hypothesis `1<=a_k<=B`; T6 carries the same finite-`B` hypotheses and an explicit source line; T8 uses the stricter audited V3 scale-family quantifiers.

# Excluded theorem candidates

The following must not be promoted into the manuscript theorem inventory without a new audit:

- arbitrary-`N` full-scale Task-8A accumulation extension;
- continued-fraction effective-repeat theorem candidate;
- any E7R/B4 Fourier decay statement;
- any general statement excluding CP19 Task-5 survivor;
- any general Collatz convergence, no-cycle, or no-divergence conclusion.
