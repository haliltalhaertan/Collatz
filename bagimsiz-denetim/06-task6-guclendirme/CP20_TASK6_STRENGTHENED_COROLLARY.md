# CP20 TASK 6 — STRENGTHENED COROLLARY

## Pressure Upper Bound Replacing the Crude Alphabet Count

Date: 2026-08-26

Status: `[STRENGTHENING CANDIDATE — INDEPENDENT AUDIT REQUIRED]`

**Provenance.** This document replaces §6–§7 of `CP20_TASK6_MAJOR_THEOREM.md`.
The Task-6 §5 lower entropy theorem is used **unchanged**. The upper bound is
the Task-7 weighted-pressure method applied backward to the bounded-alphabet
case that Task 6 handled with a crude count. No new mechanism is introduced.

This corollary is **not frozen** and must not be used downstream before an
independent zero-trust audit.

---

## 1. What is being replaced

Task 6 §6 established the upper bound

```
p_a(r) <= (r+1)(B-1)^r        =>   limsup log_2 p_a(r)/r <= log_2(B-1).
```

That count uses **only** the alphabet restriction `a_k in {1,...,B}` together
with zero-criticality `a_k != g_k`. It discards hypothesis (H1),

```
s_k = kappa log_2 k + O(1),
```

which is already assumed by the theorem. The strengthening below keeps every
hypothesis of Task 6 and simply stops discarding (H1).

---

## 2. Setup (unchanged from Task 6)

Let `alpha = log_2 3`, `F_k = floor(alpha k)`, `g_k = F_{k+1} - F_k in {1,2}`,
and `s_k = F_k - sum_{i<k} a_i`. Hypotheses:

- (H1) `s_k = kappa log_2 k + O(1)`
- (H2) `kappa > 1`
- (H3) `1 <= a_k <= B`
- (H4) `a_k != g_k` for every `k`  (zero-criticality)

Local defect `d_k = g_k - a_k`. Zero-criticality gives the exact supports

```
g_k = 1  =>  a_k in {2,...,B},        d_k in {-1,...,-(B-1)}
g_k = 2  =>  a_k in {1,3,...,B},      d_k in {+1,-1,...,-(B-2)}.
```

---

## 3. The pressure constant

Define, for `2 <= B <= infinity`,

```
h_B = inf_{lambda in R} [
        (2-alpha) log_2 ( sum_{a=2}^{B} e^{lambda(1-a)} )
      + (alpha-1) log_2 ( sum_{a=1, a!=2}^{B} e^{lambda(2-a)} )
      ].
```

The weights `2-alpha` and `alpha-1` are the asymptotic densities of the
`g=1` and `g=2` sites in the Sturmian word `g`.

For `B = infinity` the two inner sums are geometric and converge for every
`lambda > 0`:

```
sum_{a>=2} e^{lambda(1-a)}          = q/(1-q),
sum_{a>=1, a!=2} e^{lambda(2-a)}    = e^{lambda} + q/(1-q),      q = e^{-lambda}.
```

---

## 4. Pressure upper bound

**Theorem P.** Under (H1)–(H4),

```
limsup_{r->infinity} log_2 p_a(r) / r  <=  h_B.
```

*Proof outline.* Three ingredients, each already audited in Task 7:

1. **Defect band.** For a factor starting at `u`, the total defect is
   `s_{u+r} - s_u = kappa log_2((u+r)/u) + O(1)`, hence bounded in absolute
   value by `kappa log_2(r+1) + C = O(log r)`, uniformly in `u`.

2. **Chernoff.** With positive-coefficient generating function
   `P(t) = sum_S N(S) t^S` having nonnegative coefficients,
   `N(S) t^S <= P(t)` for every `t>0`, hence `N(S) <= P(t) t^{-S}`.
   A band `|S| = O(log r)` contributes `exp(lambda * O(log r)) = poly(r)`,
   which vanishes after dividing `log_2(.)` by `r`.

3. **Sturmian Parikh balance.** For fixed `r`, the number of `g=2` sites in a
   window is `n_2(u,r) = floor((alpha-1)(u+r)) - floor((alpha-1)u)`, which
   takes exactly two values differing by exactly `1`. Hence the generating
   function is phase-independent up to a bounded multiplicative factor, and
   the `r+1` distinct `g`-factors contribute a factor `r+1`.

Minimising over `lambda` yields `h_B`. Finitely many starting positions
before the asymptotic regime add a constant, which also vanishes. ∎

---

## 5. Combination with the Task-6 lower theorem

Task 6 §5 proves, **independently of the alphabet**,

```
liminf_{r->infinity} log_2 p_a(r) / r  >=  alpha / kappa.
```

Since `liminf <= limsup`,

```
alpha / kappa  <=  h_B        =>        kappa >= alpha / h_B.
```

---

## 6. Numerical values

| `B` | crude `log_2(B-1)` | pressure `h_B` | crude threshold | **pressure threshold** | gain |
|---|---|---|---|---|---|
| 3 | 1,000000000 | 0,523466681 | 1,5849625 | **3,0278193** | 1,91x |
| 4 | 1,584962501 | 0,561900734 | 1,0000000 | **2,8207162** | 2,82x |
| 5 | 2,000000000 | 0,567913141 | 0,7924813 | **2,7908537** | 3,52x |
| 6 | 2,321928095 | 0,569032730 | 0,6826062 | **2,7853626** | 4,08x |
| 8 | 2,807354922 | 0,569297781 | 0,5645750 | **2,7840658** | 4,93x |
| 10 | 3,169925001 | 0,569308553 | 0,5000000 | **2,7840132** | 5,57x |
| ∞ | — | 0,569309013486 | — | **2,7840109030** | — |

High-precision values:

```
h_3       = 0.5234666806924647163881066066720...
kappa_3*  = alpha/h_3 = 3.0278192656397885198691874092...

h_infinity      = 0.5693090134858005365743948...
kappa_infinity* = 2.7840109030009018862080361...
lambda*_infinity = 1.5967952491040467491086690...
```

---

## 7. The B=3 improvement

Task 6 concluded, for `B = 3`:

```
kappa >= alpha = 1.5849625007211562        (crude)
```

Theorem P gives, under the **same hypotheses**:

```
kappa >= alpha/h_3 = 3.0278192656397885    (pressure)
```

An improvement by a factor of **1,91**. The excluded range widens from
`1 < kappa < 1.585` to `1 < kappa < 3.028`.

---

## 8. Why the crude bound was structurally inadequate

For `B >= 5` we have `log_2(B-1) >= 2 > alpha`, hence

```
alpha / log_2(B-1) < 1.
```

Since (H2) already assumes `kappa > 1`, the crude bound **excludes nothing at
all** for `B >= 5`. It is not merely weaker — it is vacuous. Even at `B = 4`
it gives exactly `kappa >= 1`, which is again vacuous.

So the crude alphabet count was informative **only at `B = 3`**, and even
there it lost a factor of nearly two. The pressure bound is uniformly
informative: it yields a threshold above `2.78` for every `B`, unbounded
alphabets included.

---

## 9. Uniform statement

Because `h_B` is increasing in `B` and converges to `h_infinity`, a single
statement covers every case:

> Let a positive ordinary odd-only Syracuse orbit have a zero-critical
> valuation word satisfying `s_k = kappa log_2 k + O(1)` with `kappa > 1`.
> Then, **with no restriction on the valuation alphabet**,
> ```
> kappa >= alpha / h_infinity = 2.7840109030009018862...
> ```
> In particular the entire range `1 < kappa < 2.784` admits no positive
> ordinary realization.

This subsumes Task 6 (`B=3`), Task 7 (`B=4`), and the previously
"untouched" unbounded-valuation case.

---

## 10. Numerical verification performed

Independent dynamic-programming enumeration of

```
N(r, C_D) = #{ zero-critical words of length r over the Sturmian phase
               with total defect |S| <= C_D }
```

written from scratch, without either supplied engine:

| `B` | `r` | band | `log_2 N / r` | `h_B` |
|---|---|---|---|---|
| 3 | 1280 | `C_D = 2` | 0,520476 | 0,523467 |
| 3 | 1280 | `C_D = kappa log_2 r` | 0,532044 | 0,523467 |
| 4 | 640 | `C_D = 8` | 0,579440 | 0,561901 |

Fixed-band rows approach `h_B` from below; growing-band rows approach it from
above, with the excess matching the predicted prefactor
`log_2 exp(lambda* C_D) / r`.

Parikh identity verified on 240.000 `(u,r)` pairs, zero violations;
balance (exactly two values, differing by exactly 1) verified for
`r <= 5000`.

Second derivative `f''(lambda*) > 0` confirmed at every `B` tested, so the
minimiser exists and is unique.

---

## 11. Scope — unchanged

This corollary does **not** touch:

- critical sites (`a_k = g_k`);
- discrepancy laws other than the critical-logarithmic one;
- the surviving range `kappa >= 2.784...`.

It is **not** a proof of the Collatz conjecture.

---

## 12. Audit requirement

`[UNAUDITED STRENGTHENING CANDIDATE]`

Required before freezing:

1. Re-derive Theorem P independently, in particular the passage from the
   per-factor defect band to the global Chernoff estimate.
2. Reproduce `h_3` and `h_infinity` **in rational / interval arithmetic**.
   The values above were computed in 80-digit floating point and are not a
   rigorous certificate. Apply the CP17 standard: no decimal may carry a
   proof-critical sign decision.
3. Confirm that replacing Task 6 §6–§7 by this corollary leaves the Task-6
   §5 lower theorem untouched, and that no downstream document depends on
   the old crude constant `alpha`.
