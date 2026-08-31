# CP20 TASK 8A — RESEARCH PROMPT

## Critical-Site Density Pressure

Date: 2026-08-26
Status: `[COMPUTATIONAL PHASE DONE — THEOREM PHASE OPEN]`

---

## 0. What is already done

The first computational phase has been carried out. **Do not redo it;
verify it and build the theorem on it.** Results and code:
`10-task8a/HESAP_SONUCLARI.md`, `01_basinc_yuzeyi.py`,
`02_cp19t4_koprusu.py`.

Established numerically:

- the three-variable surface reduces analytically to one variable;
- the two critical-site types are **strongly asymmetric**;
- `rho_min(kappa)` was computed;
- the surface interpolates between Task 7 (`rho=0`) and CP19 T4
  (`rho=optimal`) to within 0.1%;
- CP19 T5's explicit survivor fails the density requirement by three
  orders of magnitude.

## 1. Setting (unchanged from Task 6/7)

`alpha = log_2 3`, `F_k = floor(alpha k)`, `g_k = F_{k+1}-F_k in {1,2}`,
`s_k = F_k - sum_{i<k} a_i`. Hypotheses (H1) `s_k = kappa log_2 k + O(1)`,
(H2) `kappa > 1`.

Task 7 assumed additionally `a_k != g_k` for every `k`. **Task 8A drops
that assumption.**

Define the critical indicator `c_k = 1{a_k = g_k}` and split by type:

```
rho_1 = density of { k : g_k = 1 and a_k = 1 }      (rho_1 <= 2-alpha)
rho_2 = density of { k : g_k = 2 and a_k = 2 }      (rho_2 <= alpha-1)
```

## 2. The surface

With Lagrange multipliers `lambda` (total defect) and `mu_1, mu_2`
(critical counts, **free sign** — the constraint is equality, not
inequality):

```
H(lambda,mu_1,mu_2) = (2-alpha) log_2( 2^{mu_1} + A(lambda) )
                    + (alpha-1) log_2( 2^{mu_2} + B(lambda) )
                    - mu_1 rho_1 - mu_2 rho_2

A(lambda) = sum_{a>=2} e^{lambda(1-a)}
B(lambda) = sum_{a>=1, a!=2} e^{lambda(2-a)}
```

Solving `dH/dmu_i = 0` in closed form gives

```
2^{mu_1} = rho_1 A/(2-alpha-rho_1),    2^{mu_2} = rho_2 B/(alpha-1-rho_2)
```

and the surface collapses to

```
h(rho_1,rho_2) = inf_{lambda>0} [ (2-alpha-rho_1) log_2 A(lambda)
                                + (alpha-1-rho_2) log_2 B(lambda) ]
                 + E_1 + E_2

E_1 = (2-alpha)log_2(2-alpha) - (2-alpha-rho_1)log_2(2-alpha-rho_1) - rho_1 log_2 rho_1
E_2 = (alpha-1)log_2(alpha-1) - (alpha-1-rho_2)log_2(alpha-1-rho_2) - rho_2 log_2 rho_2
```

`E_1,E_2` are the selection entropy of *which* sites are critical;
critical sites are frozen (one symbol), the rest sit under pressure.

## 3. Target theorem

Combine with the frozen Task 6 lower bound
`liminf log_2 p_a(r)/r >= alpha/kappa`:

```
alpha/kappa  <=  h(rho_1,rho_2)
```

**Required statement:**

> If a positive ordinary odd-only Syracuse orbit satisfies (H1),(H2),
> then its critical-site densities must satisfy
> `h(rho_1,rho_2) >= alpha/kappa`. In particular the total critical
> density is at least `rho_min(kappa)`, with
> `rho_min(kappa) = 0` for `kappa >= alpha/h(0,0) = 2.7840109...`
> and `rho_min(1.06) ≈ 0.351`.

## 4. Mandatory tasks

1. **Derive the closed form for `mu_i` independently.** Verify the sign
   convention: the equality constraint requires free `mu`; an inequality
   constraint (`<= rho`) would force `mu <= 0` and give a different
   surface. State which one the Chernoff step actually licenses.
2. **Justify the Parikh step in the presence of critical sites.**
   Task 7 relied on Sturmian balance (two Parikh values differing by 1).
   Check whether the `rho_1`/`rho_2` split preserves this, since the
   critical positions are themselves selected relative to `g`.
3. **Prove or refute the asymmetry structurally.** The computation shows
   `rho_1` is the cheaper escape direction. Give the reason in the
   generating function, not only numerically.
4. ~~**Explain the gap to CP19 T4.**~~ **RESOLVED — no gap.** The
   frozen V3 establishes that maximizing `h` over the feasible domain `F`
   (including the constraint `rho_1 - rho_2 >= 3 - 2*alpha`) recovers
   CP19 Task 4 **exactly**; there is no strict optimized Sturmian phase
   cost. The apparent `0.0017` difference was a grid artefact in the
   preliminary computation. Task 8A does **not** strengthen CP19 T4 at
   that point — it coincides with it, and its value lies in
   parametrizing the whole intermediate regime.
5. **Rigorous certificate.** Reproduce `h(0,0)`, `max h` and at least
   three points of `rho_min(kappa)` in rational/interval arithmetic.
   No decimal may carry a proof-critical sign decision (CP17 standard).
6. **Counterexample discipline.** Test against: `rho_1 = 2-alpha`
   (all `g=1` sites critical); `rho_2 = alpha-1`; the degenerate corner
   `rho_1+rho_2 -> 1` (surface must give `h -> 0`); `kappa <= 1`;
   eventually periodic words.
7. **Literature.** Compare against the July 2026 preprint *"Entropy
   barriers for bounded-amplitude Collatz cycles"*, which reportedly
   uses mechanical/Sturmian factor languages, repeated-factor
   divisibility, entropy and Perron–Frobenius certificates in one
   pipeline. Its theorem targets bounded-amplitude **cycles**; ours
   targets critical-log **orbit realization**. Establish precisely
   whether the pressure surfaces coincide.

## 5. Verdict format

One of: `[PROVED]`, `[PROVED WITH WORDING REPAIR]`, `[FIXABLE GAP]`,
`[MAJOR GAP]`, `[FALSE — COUNTEREXAMPLE]`.

Separately state: the exact `rho_min(kappa)` curve; whether CP19 T5's
survivor is excluded; whether Task 8A subsumes CP19 T4; whether the
result can be frozen.

Do not state that Collatz is solved.

## 6. Downstream (Task 8B, do not start yet)

If Task 8A proves, the frontier becomes: *a survivor at `kappa ≈ 1.06`
must be critical at ~35% of its sites, concentrated on `g=1` positions.*
Task 8B asks whether a single positive ordinary integer can sustain that
density forever — using the Sinai/Kontorovich structure theorem
(arithmetic progressions realizing prescribed valuation prefixes) and
ordinary-state arithmetic.
