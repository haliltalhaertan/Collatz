# CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1 — DEFINITIONS

## Frozen project target

Let

`alpha = log_2(3)`,

`T_r = floor(alpha*r) - 8`,

`eta_r = 2^(T_r-4) mod 3^r`.

The audited exact normal form is

`G_r = E[e_(3^r)(eta_r F_r^aff(A_1,...,A_r)) | sum_i A_i = T_r]`.

The research target remains `|G_r| = O(1/r)`.

No separate global mod-16 cocycle exists in this fixed-total observable.

## Tilted reference law

For `p in (0,1)`,

`P_p(A=m) = p(1-p)^(m-1)`, `m=1,2,...`.

Freeze

`p_* = 1/alpha = 1/log_2(3)`

and

`q_* = 1-p_*`.

Then

`E_(p_*)[A] = alpha`

and

`sigma_*^2 = (1-p_*)/p_*^2 = alpha(alpha-1)`.

100-digit reference decimals (diagnostic only):
- `alpha = 1.584962500721156181453738943947816508759814407692481060455752654541098227794358562522280474918088242`
- `p_* = 0.6309297535714574370995271143427608542995856401318804278706549438386852013809148050611726885494517456`
- `q_* = 0.3690702464285425629004728856572391457004143598681195721293450561613147986190851949388273114505482544`
- `sigma_*^2 = 0.9271436279711048275610707159949037869532801413589483457336354015740521722747089375587914891753544635`

## Central total

`delta_r = T_r-alpha*r`.

Because `T_r=floor(alpha*r)-8`,

`-9 < delta_r <= -8`.

## Tilted denominator and numerator

`D_r = P_(p_*)(sum_i A_i=T_r)`

with exact formula

`D_r = binom(T_r-1,r-1) p_*^r q_*^(T_r-r)`.

Define

`chi_r(A) = e_(3^r)(eta_r F_r^aff(A))`

and

`N_r = E_(p_*)[chi_r(A) 1_(sum A_i=T_r)]`.

Conditional-law invariance, if established, yields exactly

`G_r = N_r/D_r`.

The candidate denominator asymptotic

`D_r ~ 1/sqrt(2*pi*sigma_*^2*r)`

is **NOT PROVED IN STAGE 0**.

The sufficient numerator target is

`N_r = O(r^(-3/2))`.

## Frozen Fourier convention

`H_r(t) = E_(p_*)[chi_r(A) exp(i t (sum_i A_i-alpha*r))]`.

Freeze

`N_r = (1/(2*pi)) integral_(-pi)^pi exp(-i t (T_r-alpha*r)) H_r(t) dt`.

The sign/index convention is mechanically checked only on preregistered tiny finite surrogates in Stage 0.

## Frozen deterministic arc split for future Stage 1

No adaptive split is permitted.

For all `r>=1`, define

`L_r = (ln(r+1))^(1/4)`.

- major arc: `|t| <= L_r/sqrt(r)`
- intermediate arc: `L_r/sqrt(r) < |t| <= r^(-1/4)`
- minor arc: `r^(-1/4) < |t| <= pi`

Since `ln(r+1) <= r`, the major endpoint is never larger than the intermediate endpoint.

This split is a preregistered proof decomposition only. Stage 0 makes no decay claim on any arc.
