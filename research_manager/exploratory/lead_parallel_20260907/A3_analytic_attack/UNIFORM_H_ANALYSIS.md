# UNIFORM_H_ANALYSIS.md — attack on `sup_{j<=L_r} |H_{r-4,n_r-j}(j)| <= C/r`

Date: 2026-09-07. EXPLORATORY WORKING ARTIFACT, pending the manager's acceptance gate.
Nothing here proves the Collatz conjecture. No claim that `|E[F_{r,4}|S_r=n_r]| = O(1/r)` is made.

Notation and the exact bridge coordinate `delta` are as in STRUCTURE.md §3:
`H_{r-4,n_r-j}(j) = Psi(r-4; a_j, b_r)` with `a_j = j - 5 alpha = j - 7.9248` and
`b_r = -13 - beta - theta_r = -13.5850 - theta_r`, `Psi(m;a,b) = E[ prod_{s=1}^m exp(2 pi i 2^{delta_s}) ]`
over the mean-zero bridge from `a` to `b`, increments `y_s - beta`, `sigma^2 = 0.927144`.

---

## 1. What the data says  [NUM]

From `A2_numeric_probe` (`PROBE_RESULTS.csv`, `WINDOW_TABLE.csv`, exact DP, mpmath crosscheck
`2.5e-16`), for `14 <= r <= 600`:

* `r * max_{j in window} |H_j|` is **flat**, not growing: 46.1 (r=100), 49.3 (200), 46.3 (300),
  48.8 (400), 45.8 (500), 48.5 (600). Log-log slope of `max_j|H_j|` over `r=50..600` is `-1.012`.
* **The maximiser over the window is `j = 0` for every `r` in `[60,600]`** (0 exceptions;
  `max_{j in win}|H_j| / |H_0| = 1.000000` exactly). At `r = 50` it is not (ratio 1.263), so the
  extremality sets in only after the window has grown past the degenerate small-`r` regime.
* `r|H_0|` is almost a pure function of `theta_r = {beta r}`: **correlation(theta_r, r|H_0|) = 0.9882**,
  range `[43.12, 49.28]`, mean 46.17 over `r >= 200`. (`r|G|` : correlation 0.828, range
  `[18.73, 23.17]`, mean 20.54.)
* The `j`-profile `|H_j|/|H_0|` is `r`-stable and decays superlinearly:
  at `r = 600` it is `1, .741, .509, .316, .171, .0786, .0287, .0160, .0078, .0038, .0012, .0007`
  for `j = 0..11` (at `r = 300` : `1, .754, .527, .333, .185, .0866, .0323, .0185, .0093, .0047, ...`).
* Caution recorded: over **all** `j` (outside the window) `max_j |H_j| = 1`, attained at `j = n_r`
  where `k = 0` and the tail average is a single term. The uniform bound is meaningful ONLY on the
  window; this is precisely what the audited truncation lemma (T) is for.

`[NUM] verdict on the literal statement:` `sup_{j<=L_r}|H_j| <= C/r` is **supported with `C ~ 50`**
in `60 <= r <= 600`, with the supremum attained at `j = 0`.

## 2. Proof sketch, step by step

Target `(U)`: exist `C, r0` with `sup_{0<=j<=L_r} |Psi(r-4; a_j, b_r)| <= C/r` for `r >= r0`.

* **(U1) Reduction to `j = 0`.** `sup_{j<=L_r}|Psi(m;a_j,b_r)| <= C' |Psi(m;a_0,b_r)|`.
  `[OPEN]` — this is exactly the lemma proposed in NEXT_LEMMA.md. `[NUM]` holds with `C' = 1`
  for all tested `r >= 60`.
* **(U2) Tilt-invariance and centring.** The microcanonical law equals the `rho`-tilted i.i.d. law
  conditioned on the sum, `rho = beta/alpha`, `p* = 1-rho = 1/log_2 3`. `[PROVED here]` (STRUCTURE §5).
* **(U3) Local CLT for the constraint.** `P_rho(Y_m = k) = (sigma sqrt(2 pi m))^{-1}(1 + o(1))`.
  `[PLAUSIBLE, heuristic]` as stated for the exact lattice; standard for i.i.d. geometric with
  span 1, and `[NUM]`-confirmed to 3 digits at `r = 20000`. Not proved here.
* **(U4) Barrier decomposition.** Split on `E := { delta_s <= -T for all 1 <= s <= m }` for a fixed
  threshold `T` (the "no-wrap" event). On `E` every row factor satisfies
  `|exp(2 pi i 2^{delta_s}) - 1| <= 2 pi 2^{-T}`, so `|E[prod ; E] - P(E)| <= 2 pi m 2^{-T}`.
  `[PROVED here]` (elementary, same telescoping as the B3 countertheorem, applied in the opposite
  direction). **Note the sting: this term is useful only if `T >= log_2 m + O(1)`, i.e. `T` must
  grow, and then `P(E)` is a barrier probability at a growing depth.**
* **(U5) Barrier probability.** For a mean-zero bridge of length `m` with `O(1)` endpoints,
  `P(delta stays below level 0) ~ 2|a||b|/(sigma^2 m)`. `[PLAUSIBLE, heuristic]` (standard
  Brownian-bridge/ballot asymptotics; not proved for this lattice bridge here).
  Numerically `2|a_0||b|/sigma^2 = 2*7.9248*13.585/0.9271 = 232`, vs the observed `r|H_0| ~ 46`;
  same order, a factor ~5 out, consistent with the barrier being effectively at `-T`, not at 0.
  **This is the mechanism that produces the conjectured `1/r` scale.**
* **(U6) Equidistribution off the barrier event.** `|E[prod ; E^c]| = o(1/m)`.
  `[OPEN] — THIS IS THE SINGLE HARDEST STEP.** It says: conditioned on the walk wrapping at least
  once at depth `> -T`, the `3`-adic phase product equidistributes strongly enough to beat `1/m`.
  It is the microcanonical analogue of Tao's "white point" Fourier input, and its direct transfer
  from Tao v7 / Si 2026 is `[CLOSED]` by the audited Literature Transfer decision. Nothing in the
  present analysis supplies it.

**Isolated hardest step: (U6).** (U1) is a genuine but separable difficulty (NEXT_LEMMA.md);
(U4)–(U5) are classical-in-shape; (U6) carries all the arithmetic.

## 3. Why the B3 countertheorem does NOT kill this window — and where it would

B3-CT `[PROVED][AUDITED]` produces a family of endpoints for which the block kernel tends to **1**:
it pushes the walk `W_r` **below** the wrapping threshold, so no row wraps and the telescoped product
is `1 + o(1)`. In the present coordinates, that is `Psi(m; a, b)` with `a` (or `b`) pushed to
`-W_r`, `W_r -> infinity`; the barrier probability then tends to 1.

The prefix window does the **opposite**: `a_j = j - 5 alpha` moves **up** with `j`, and
`b_r` is pinned at `-13.585 - theta_r`. Raising `a` can only shrink the no-wrap set. So `[PLAUSIBLE,
heuristic]` `|H_j|` should be non-increasing in `j` — and `[NUM]` confirms it decisively (§1), with
a visible collapse once `j` passes `5 alpha = 7.9248`, the exact height at which the FIRST row
`exp(2 pi i 2^{j - 5 alpha})` starts to wrap: at `r = 600`, `r|H_j|` = 48.5, 35.9, 24.7, 15.3, 8.30,
3.81, 1.39, 0.774, 0.377, 0.184, 0.059 for `j = 0..10`.

**Consequence to record.** The B3-CT counterfamily lives at `a -> -infinity`; the prefix window lives
at `a in [-7.92, L_r - 7.92]`, i.e. bounded below and moving up. The two are disjoint regions of the
same `Psi(m;a,b)` family. `[PROVED here]` that they are disjoint; `[OPEN]` whether the window region
admits a uniform bound. **Any future attempt to enlarge the reduction so that the LEFT endpoint is
pushed DOWN (e.g. by conditioning on small prefixes, or by a mirrored suffix split) re-enters the
B3-CT region and is refuted in advance.** This is a concrete, reusable stop rule.

## 4. The extra Fourier variable, and the exact `r^{1/2}` loss  [PROVED here]

Tao 2019 controls the **unconditioned** Syracuse random variable: one Fourier variable, on the
`3`-adic side, and a "white point" argument gives decay of the characteristic function.

The microcanonical fibre introduces **exactly one extra dual variable `phi in T`, conjugate to the
total sum `Y_m`**, through the inversion (STRUCTURE §5)

```
H_{m,k}(j) = P_rho(Y_m=k)^{-1} INT_0^1 Phi_m(j,phi) e(-phi k) dphi,
Phi_m(j,phi) = E_rho[ (3-adic phase product) * e(phi Y_m) ]  (i.i.d., no conditioning).
```

`P_rho(Y_m=k)^{-1} = sigma sqrt(2 pi m)(1+o(1)) = 2.412 sqrt(m)(1+o(1))`. `[NUM]`-confirmed §5.

**The loss, stated exactly.** Suppose one had the strongest plausible unconditioned input,
`sup_{phi} |Phi_m(j,phi)| <= A/m` — i.e. a Tao-strength bound holding uniformly in the new variable.
Then the trivial `L^infty` estimate of the `phi`-integral gives only

```
|H_{m,k}(j)| <= 2.412 sqrt(m) * (A/m) = 2.412 A * m^{-1/2}.
```

So even a perfect uniform-in-`phi` unconditioned bound of strength `1/m` yields only `m^{-1/2}` after
conditioning. **To reach `O(1/m)` one needs `INT_0^1 |Phi_m(j,phi)| dphi = O(m^{-3/2})`, i.e. an
`L^1(dphi)` bound one full power of `m^{1/2}` stronger than the pointwise bound.** `[PROVED here]`

Naive Plancherel/Cauchy–Schwarz over `phi` does not recover it, and in fact does worse. Writing
`c_k = E_rho[ (phase product) 1_{Y_m=k} ]`, so `Phi_m(j,phi) = sum_k c_k e(phi k)`:

```
INT_0^1 |Phi_m| dphi <= ( INT_0^1 |Phi_m|^2 dphi )^{1/2} = ( sum_k |c_k|^2 )^{1/2}
                     <= ( max_k P_rho(Y_m=k) * sum_k P_rho(Y_m=k) )^{1/2} = O(m^{-1/4}),
```

giving `|H| = O(sqrt(m) * m^{-1/4}) = O(m^{1/4})` — **worse than the trivial bound 1**.
`[PROVED here]` The reason is structural: `Phi_m(., phi)` is *not* spread over the circle; the
conditioning mass lives on a `phi`-window of width `~ m^{-1/2}` (the local-CLT scale), and
Cauchy–Schwarz against the FULL circle throws away exactly the factor `|supp|^{1/2} = m^{-1/4}`,
which combined with the `m^{1/2}` prefactor is the advertised `m^{1/2}` deficit.

**Therefore:** the microcanonical problem cannot be reduced to a uniform-in-`phi` unconditioned
estimate by any `L^2`/Plancherel device. It requires a **joint** local-limit statement in
`(phi, 3-adic frequency)`: cancellation in the arithmetic direction that persists, with the right
`L^1(dphi)` weight, across the local-CLT window in `phi`. That joint statement is precisely what
`E7R-B4 / CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1` names, and it is `[OPEN]` and
not dispatched. No such theorem is claimed here.

## 5. Verdict on `(U)`

* **`(U)` as literally stated is `[PLAUSIBLE, heuristic]` TRUE**, with `C ~ 50`, on the evidence of
  §1 and the barrier mechanism of §2. `[NUM]` only; not proved.
* **`(U)` is NOT an obstruction-free route.** Its `j = 0` instance is an E6-N2-strength statement for
  the same bridge family (STRUCTURE §6). Proving `(U)` is strictly harder than E6-N2.
* **No obstruction was found that makes `(U)` false.** The three candidate obstructions were tested
  and each fails to bite:
  * *off-central conditioning* — the conditioning is off-central only w.r.t. the CANONICAL law; under
    the tilt `rho = beta/alpha` it is exactly central (local-CLT scale). `[PROVED here]`
  * *`2^j` resonating with a low-order character mod `3^t`* — `ord_{3^t}(2) = 2 * 3^{t-1}`, so no
    `j <= L_r = O(log r)` is resonant; and in the `delta` coordinate `2^j` is not a frequency at all,
    only a shift of the left endpoint. `[PROVED here]`
  * *offset drift making some `j` decay slower than `1/r`* — the drift raises `a_j`, which by §3
    can only increase cancellation; `[NUM]` `|H_j|` is strictly decreasing in `j` on the whole window
    for every tested `r >= 60`. The a-priori worry that `sup_j` grows like `(log r)/r` is **refuted
    by the data**: `r * max_j |H_j| / log r` FALLS (12.8 at `r=50` → 7.6 at `r=600`).
* **The true scale is `1/r`, not `r^{-1/2}`**, on the evidence of §1 (log-log slope `-1.01` for
  `max_j|H_j|`, `-1.08` for `|G|` and for `S_r`) and the barrier heuristic (U5). `[NUM]` +
  `[PLAUSIBLE, heuristic]`. But `r|G|` and `r|H_0|` **do not converge**: they are almost-periodic in
  `theta_r` (correlations 0.83 and 0.99). Any target of the form "`r|G| -> c`" is therefore
  `[PLAUSIBLE, heuristic] FALSE as stated`; the correct object is a profile `Phi(theta)`.
* `[OPEN]` (U6) remains the whole content.
