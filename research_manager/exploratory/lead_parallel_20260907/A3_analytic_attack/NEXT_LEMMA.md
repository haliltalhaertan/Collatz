# NEXT_LEMMA.md — exactly ONE proposed narrower falsifiable lemma

Date: 2026-09-07. EXPLORATORY WORKING ARTIFACT, pending the manager's acceptance gate.
This is a **proposal for a future authorized task**, not the execution of one, and not a result.
Nothing here proves the Collatz conjecture. No E6-N2, E7R-B4, B5 or B6 claim is made or implied.

---

## The proposed lemma

> **PREFIX-WINDOW EXTREMALITY LEMMA (PWE).** Fix `delta > 0` and the audited cutoff
> `L_r = ceil(4(1+delta) log r / |log rho|)`, `rho = beta/alpha`. There exist an absolute constant
> `C >= 1` and an `r_0` such that for every integer `r >= r_0` and every integer `0 <= j <= min(n_r, L_r)`,
>
> ```
> | H_{r-4, n_r - j}(j) |  <=  C * | H_{r-4, n_r}(0) | .          (PWE)
> ```
>
> Equivalently, in the exact bridge coordinate of STRUCTURE.md §3, with
> `Psi(m;a,b) = E[ prod_{s=1}^m exp(2 pi i 2^{delta_s}) ]` over the mean-zero bridge from `a` to `b`:
> `|Psi(r-4; a_0 + j, b_r)| <= C |Psi(r-4; a_0, b_r)|` for `0 <= j <= L_r`, where
> `a_0 = -5 alpha = -7.9248` and `b_r = -13 - beta - theta_r`.

**PWE asserts no decay rate whatsoever.** It is a comparison inside one two-parameter family,
along the left-endpoint axis only, over a window of length `O(log r)`.

## What it would buy toward E6-N2

Combining PWE with the audited truncation lemma (T) and `sum_j w_{r,n_r}(j)|D_j| <= 1`:

```
|G_{r,n_r}|  <=  S_r + 4 r^{-1-delta}  <=  C |H_{r-4,n_r}(0)| + 4 r^{-1-delta}.
```

So **E6-N2 would reduce to the single statement `|H_{r-4,n_r}(0)| = O(1/r)`** — one family, left
endpoint pinned at `-5 alpha`, right endpoint `-13-beta-theta_r` with `theta_r in [0,1)`. That
retires, for this route, the item the independent audit lists as `Global offset compactness [OPEN]`:
the drifting-offset / drifting-frequency window collapses to a compact one-parameter family indexed
by `theta_r`. It also makes the proposed triangle-weighted lemma `(S)` a corollary of a *single*
estimate rather than of a uniform family estimate.

It does **not** prove E6-N2, `(S)`, any lower bound, any nonzero coefficient, or Collatz.

## Why this is a genuine step and not a restatement

* It is **not implied by** E6-N2 and **does not imply** it. It is orthogonal in content: a ratio
  bound, with no scale in it.
* It is **provable in principle without any arithmetic equidistribution input**. The natural route is
  monotonicity/coupling: raising the left endpoint `a` of the bridge can only enlarge the set of
  paths on which some row wraps, i.e. can only increase cancellation (UNIFORM_H_ANALYSIS.md §3). A
  proof would need a bridge-comparison / stochastic-domination argument plus control of the four
  low-entropy leading rows, not a "white point" theorem. This is a different toolbox from the one
  that is `[CLOSED]` for direct transfer.
* It is **the exact statement the numerics single out**: the data say the window maximiser is `j = 0`
  for every tested `r >= 60`, which is `(PWE)` with `C = 1`.
* It **cannot be satisfied vacuously**: it is stated on the window only. Over all `j` the analogous
  claim is FALSE — `|H_{m,0}(n_r)| = 1` — so PWE has genuine content tied to the cutoff `L_r`.

## Evidence class if proved

`[PROVED]` — a **structural reduction lemma** for the prefix-bridge route. Explicitly NOT an
asymptotic cancellation theorem, NOT an upper bound of order `1/r`, NOT a profile or coefficient
statement, NOT an E6-N2/E7R-B4 acceptance. It would need its own zero-trust audit and its own
acceptance gate before any downstream use.

## Falsification protocol (what computation would refute it)

Exact (or 30-digit) evaluation of `H_{r-4,n_r-j}(j)` for all `0 <= j <= L_r`, using the existing
`prefix_probe.py` transfer recursion, extended to `r` in the low thousands. Compute

```
R(r) := max_{0 <= j <= min(n_r,L_r)} |H_{r-4,n_r-j}(j)| / |H_{r-4,n_r}(0)| .
```

* PWE is **refuted** if `R(r)` is unbounded (e.g. grows like a power or like `log r`) as `r` grows,
  or if `R(r)` exceeds any fixed candidate `C` on a sequence of `r` with `theta_r` ranging over
  `[0,1)`.
* PWE is **not** confirmed by any finite computation; a finite run only fails to refute it.
* Diagnostic to record alongside: `R(r)` stratified by `theta_r`, since `[NUM]` shows `r|H_0|` is
  almost a pure function of `theta_r` (correlation 0.9882) and a failure, if any, would most likely
  appear at one end of the `theta_r` range.

## Current numerical status (does not constitute proof)

`[NUM]` from `A2_numeric_probe`, `60 <= r <= 600` (541 values of `r`, exact DP, mpmath crosscheck
`2.5e-16`):

* `R(r) = 1.000000` exactly for **every** `r` in `[60, 600]` — zero exceptions. The maximiser is
  `j = 0` throughout. (At `r = 50`, `R = 1.263`; the extremality sets in once the window is past the
  degenerate small-`r` regime, which is why `r_0` is left unspecified in the statement.)
* The consequent inequality is comfortable: `S_r / |H_{r-4,n_r}(0)| = 0.6237, 0.5580, 0.5335, 0.5250,
  0.5173, 0.5145` at `r = 100, 200, 300, 400, 500, 600`, decreasing; `max = 0.72634` over `r >= 60`.
* The `j`-profile `|H_j|/|H_0|` is `r`-stable and strictly decreasing in `j`
  (`r = 600`: `1, .741, .509, .316, .171, .0786, .0287, ...`).

## Compliance check against `prohibited_inferences`

* Does not promote lost pre-recovery E7 conclusions. OK.
* Does not claim the frozen full-window pointwise E7R-B3 contraction; PWE lives on the *disjoint*
  region of the family (left endpoint moving **up**, bounded below), see UNIFORM_H_ANALYSIS.md §3. OK.
* Does not claim `|E[F_{r,4}|S_r=n_r]| = O(1/r)`; PWE contains no rate. OK.
* Does not infer E7R-B4/E6-N2/B5/B6 from B1/B2/B3-CT. OK.
* Does not replace the closed pointwise route with an ad-hoc weighted/operator/L2/spectral route:
  this is a **proposal** and explicitly requires a fresh authorized task and seal before execution.
  It uses no `L^2`/Plancherel rescue — indeed UNIFORM_H_ANALYSIS.md §4 shows such a rescue loses
  `r^{1/2}`. OK.
* Uses no Tao/Si theorem, no unsealed revision, and does not broaden the audited Literature Transfer
  closure. OK.
* Does not start E8; does not claim Collatz; reruns no sealed Stage 1; does not dispatch
  `CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1` Stage 0. OK.
* Proposing a lemma is permitted; executing a new sealed task is not, and none is executed here. OK.
