# CP22 — Adversarial brainstorm: "caps + supports suffice" is FALSE

Date: 2026-09-14 · Programme: Collatz research archive · Checkpoint CP22 (follows CP21)
Four parallel Muse Code sessions (ATTACK / DEFEND / FLANK / SCOUT) under a lead researcher.

> **Collatz is NOT solved.** Nothing here bears on the Collatz conjecture. This concerns an
> internal lemma about the *prefix source*. Every finite table is labelled as such and is
> **never** a uniform theorem.

---

## 0. Headline

CP21 ended with a lesson repeated across ~57 dead paths: *arguments that ignore the max-entry cap
and the support get killed.* CP22 tested the converse and **refuted it**:

> **`[FAIL]` A histogram family respecting exact binomial masses, the exact real caps, the true
> real supports, and integrality VIOLATES radius-2 charging on 91 intervals.**

Independently re-verified by the lead from the raw arrays, to the digit: gap
`13498621/176358` at `(20,3)[14,16]`; 91 violating intervals, 31 of them with `L>0` at both
endpoints. So caps + supports are **necessary but not sufficient**. A proof needs a strictly
deeper input — per-stratum *affine realizability*, i.e. which collision patterns the `B_w`
congruence structure actually produces.

Two independent sessions converged on this from opposite directions:
* **ATTACK** (combinatorial): box-constrained `max L_k` exceeds the truth by **10–20×**
  (`k=16`: true `3664/969`, box-max `69280/969`). The real source lives deep inside the box.
* **DEFEND** (analytic): factored cap/support bounds overshoot real supply by **10–70×** on
  1743 of 1744 real intervals, because real `LX` is small by **sign cancellation** that any
  absolute-value bound discards.

---

## 1. Results by session

| session | verdict |
|---|---|
| **ATTACK** | Hot window `m=19..24`, `s=2,3,4` (18 rows): **0 violations**; minimum ratio pinned exactly. Adversarial family respecting caps+supports: **91 violations** `[FAIL]` for the "caps+supports suffice" hope |
| **DEFEND** | Composite `{radius-2 + T6-propagated cap}` induction: **fails with witness** `[FAIL]`. Three published formulas corrected |
| **FLANK** | Route (B) **alive** on 35 new rows — the `0.2017` dip is a fluctuation, not decay. Cap: structural restriction proved, no quantitative gain |
| **SCOUT** | 8 ranked options, 2 cheap kills, a concrete process rule |

---

## 2. ATTACK — the main result

### 2.1 Real rows: no violation, margin pinned exactly

18 new exact rows (`m = 19..24`, `s = 2,3,4`), **zero radius-2 violations**. The narrowest
supply/demand ratio over everything computed:

    29517649 / 28111980   at (20,3) interval [14,16]
    demand 72082/6783,  supply 4216807/377910

Certified strictly inside `(21/20, 1051/1000)` by exact integer arithmetic
(`20·num − 21·den = 1400 > 0`). The lead's earlier value of `1.050` is confirmed, and **nothing
below it** was found.

### 2.2 The mechanism, quantified

Demand comes from **flat** strata; payment comes from **spiky** low-mass neighbours.
At `(20,3)`: `k=14` has max/mean `2304/2261` (nearly flat), `k=15`: `3032/2907`, `k=16`: `356/323`.
Normalised bin-gap energy `G2_j = S_j/(n_j² n_{j−1}²)` rises **~1000×** from interior
(`j=13`: `14723/2856319362`) to tail (`j=18`: `21220/2816883`).

Two tail links carrying **2.7%** of the demand mass pay `1897948/4216807 ≈ 45%` of the binding
supply. The same signature appears at `(18,2)`.

### 2.3 The adversarial family `[FAIL]` — the headline

Exact integer hill-climbing under masses + caps + supports produced a family that satisfies
**all** of the following (lead-verified bin by bin):

| constraint | check |
|---|---|
| binomial masses `n_k = C(m−1,k−1)` | 20/20 strata exact |
| real caps `max_z P_k ≤ cap(m,k,s+1)` | 20/20 strata, none exceeded (`k=11`: 5892 = real 5892) |
| real supports | zero mass outside the real source's support |
| integrality | yes |

and **violates radius-2 charging on 91 intervals**, 31 with `L>0` at both endpoints
(e.g. `[9,15]` gap `22406651/1119195`).

**Consequence for the programme.** The rule "use the cap and the support" is necessary but does
**not** suffice. Any future proof must consume per-stratum affine realizability.

### 2.4 A regime boundary

`(24,2)` has **zero positive `L_k`** (all `L_k ≤ 0`, e.g. `L_2 = −48/23`) — an entirely vacuous
row. Worth probing: is this an even/odd effect or a genuine regime change?

---

## 3. DEFEND — the lead's own idea, killed cleanly

The lead proposed: fold the cap into the induction, since T6 already supplies a propagation law
`cap(m,k,r) ≤ 2·cap(m−1,k,r+1) + 2·cap(m−1,k−1,r+1)`.

**Result `[FAIL]`, with exact witness.** T6 itself holds (156/156, tight at `(5,3,2)`), so
propagation closes. But T6's bound is **too loose to exclude the witness the real cap excludes**:

| k | T6 bound | W(4,2) pile | **real** cap |
|---|---|---|---|
| 2 | 4 | 2 | **1** |
| 3 | 4 | 2 | **1** |

`W(4,2)` satisfies parent radius-2 *and* all T6-propagated caps, yet the child violates
(demand `16/3` vs supply `14/3`, 4 intervals). Lead-verified from the raw arrays.

So `{radius-2 ∧ T6-cap}` is **not inductively closed**. Dead path #14.

Further: with the **true** caps and supports, per-stratum factored bounds still exceed real
supply on **1743/1744** intervals (e.g. `(9,2) k=5`: `L = 34/35`, support-bound `296/5`,
supply `458/105`). Only one interval closes. **Absolute-value bounds structurally cannot close
the step** — real `LX` is small by sign cancellation that they discard.

`|LX_k| ≤ 8q²·C_E·C_O/n_k` was proved (sound on 438/438 strata, and the cap **does** enter here),
but the tightest ratio is `32/3` and typical ratios are 10–60×. Too loose to transport demand.

### 3.1 Three published formulas corrected — read this before reusing CP21

DEFEND could not reproduce three formulas as stated in the CP21 report. The lead investigated:
**the mathematics is right, the CP21 write-up was under-specified.** Both readings were run.

| formula | CP21 text | correct statement |
|---|---|---|
| **R3** | `w_k = E'(w'_k) + O'(w'_{k−1})` | holds **only** when `w` is kept at full length `N = 2^(s+1)` as an anti-periodic vector. Under the natural length-`q` reading it is **false** — counterexample `(4,2) k=3`: true `[-1,0,0,0]`, predicted `[1,0,0,0]` |
| **R1** | `L_k = (q/2n_k)⟨w_k,T^{3^k}w_k⟩` | the `1/2` belongs to the `N`-point convention; under a `q`-point inner product the factor is `q/n_k` |
| **LX** | `LX_k = 2⟨A, T^{3^k}B⟩` | `T^d` is **not** symmetric here; the cross term has two parts. `(7,6) k=5`: `LXa = 0`, `LXb = 64/15` |

DEFEND's corrected signed form (verified 58/58 levels) shows the transfer of `w` needs sign data
from a **mod-2N lift**, and **~37% of the signs are −1** — not a minor slip but a structural fact:
the differentiated identity requires one bit beyond mod `N`.

**Action taken:** the CP21 report's §4.1 must be read with these specifications. Recorded here
rather than silently amended, because the CP21 artefact is already published.

---

## 4. FLANK — route (B) is not dying

CP21 flagged that (B)'s minimum fell from `1.366` at `(5,4)` to `0.2017` at `(13,4)` — an order
of magnitude — and called the route fragile. **That reading was wrong.** 35 new exact rows
(`s=4`: `m=5..24`; `s=5`: `m=6..20`), all pair-positive, `Σ_a Δ^(a) = defect` exactly every row:

| m (s=4) | 12 | **13** | 14 | 15 | … | 22 | 23 | 24 |
|---|---|---|---|---|---|---|---|---|
| min Δ | 2.27 | **0.2017** | 8.15 | 4.18 | … | 11.51 | 13.58 | **21.26** |

The `0.2017` is an **isolated fluctuation**, not decay: the sequence rebounds immediately and
**grows** with `m`. Same at `s=5` (`2.26 → 13.09`). No `c/m` or `c·ρ^m` decay fits.

The forced-index proof was independently re-verified: `Ê/Ô` exactly `q`-periodic, lift weight
exactly `q`-anti-periodic, and the invalid mod-`N` refinement produces spurious negatives on all
35 rows — confirming it is an invention, not a decomposition.

**Correction to CP21's "the margin is shrinking" claim: not supported by the extended grid.**

### 4.1 Cap: a proved structural restriction, but no counting gain

`[PROOF]` **`B_w ≢ 0 (mod 3)`**, so only `2·3^(k−1)` of the `3^k` residue classes are reachable.
Lead-verified: 16,382 words, **zero** with `B ≡ 0 (mod 3)`; occupancy of the allowed set is
94–100% (`(13,4)`: 54/54 = 100%).

This calibrates the collision count: a birthday estimate over the **full** `3^k` is off by ~1.58×,
while over the **allowed** `2·3^(k−1)` it matches within **~5%** (`(20,6)`: obs/exp `1.05`).
So collisions behave allowed-uniformly.

But this is a **pigeonhole *lower* bound on the max, not an upper bound** — the wrong direction.
The sharpest provable ceiling remains T4 (0 violations on 209 entries); T6 adds nothing at the
sampled points. Forward-T7r containment is circular for counting (the `t`-class sizes are the
unbounded quantity). `[FAIL]` no quantitative improvement.

---

## 5. SCOUT — options and process

8 options generated and ranked by expected value. Two killed on the spot (lead-verified):

* `[FAIL]` `F = I` i.e. `L_lift ≡ 0` — killed at `(4,2)`: `L = 8/3`
* `[FAIL]` `L_k ≥ 0` per stratum — killed at `(4,3)`: `L_3 = −8/3`; **113** negative `L_k` for
  `m ≤ 10`. So the `max(L_k,0)` in radius-2 charging is **not** removable.

Top-ranked live options: extend the exact grid past `m=26` with full interval audit (O6);
cap+support-respecting adversarial campaign (O1 — **now upgraded to top priority by ATTACK's
result**); Lean pilot on the undisputed kernel (O5).

SCOUT self-demoted its own Cauchy–Schwarz and anti-concentration options to probability `1/20`,
citing the 140× cap-ratio degradation — an honest call that DEFEND's measurements then confirmed.

### 5.1 Process rule adopted

Direct response to CP21's T7r incident (an agent attached `[PROOF]` to a false statement; it
survived only because the script had never been executed):

> No AI-authored statement carries `[PROOF]` until **(i)** an executable exact-arithmetic script
> at an absolute path reproduces it from scratch, **and (ii)** a second independent agent
> re-implements the check by a different code path and confirms. Until then: `[CONJECTURE]`.
>
> Every new proposal must name the dead path it most resembles and the ingredient (cap, support,
> transfer-image, affine realizability) that distinguishes it — or it is returned without review.
>
> Every sign/index convention must be tested **both ways**, citing the `(18,2)[14,14]` window trap
> as the template.

CP22 validates this rule twice over: DEFEND caught the CP21 under-specification precisely because
it re-implemented independently, and ATTACK's headline was confirmed only because the lead
re-derived it from the raw arrays.

---

## 6. Status after CP22

| item | status |
|---|---|
| `M_merge ≥ L_lift` (target) | **open** |
| Radius-2 charging | `[CONJECTURE]` — 239 rows, 0 violations, no proof |
| Per-frequency positivity (B) | `[CONJECTURE]` — 76 rows, **not** decaying |
| "caps + supports suffice" | **`[FAIL]`** — 91-interval witness |
| `{radius-2 ∧ T6-cap}` induction | **`[FAIL]`** — W(4,2) witness |
| Max-entry cap bound | `[CONJECTURE]` — T4 stands; structure proved, counting open |

### 6.1 Where the fragility actually is

The lead measured the target at the **global** level across 221 rows:

| level | narrowest margin |
|---|---|
| target `M_merge ≥ L_lift` | **2.13×** |
| charging intervals | **1.050×** |

`defect/M` never approaches zero (still 1.08–1.67 at `m=26`). Only **5 of 221 rows** have
`L_lift > 0` at all, the largest at `m=11`.

**So the fragility is in the proof method, not in the target.** If radius-2 charging falls, the
target does not fall with it — we only learn that this route fails. CP21's framing of "both live
routes look fragile" over-stated the danger to the target itself.

---

## 7. Dead paths added by CP22

14. `{radius-2 charging ∧ T6-propagated cap}` as an induction hypothesis — W(4,2) satisfies both
    at the parent and violates at the child; T6's bound (4) re-admits what the real cap (1) excludes
15. "caps + supports + masses + integrality suffice for radius-2" — 91-interval witness at `(20,3)`
16. `F = I` / `L_lift ≡ 0` — `(4,2)`, `L = 8/3`
17. `L_k ≥ 0` per stratum — `(4,3)`, `L_3 = −8/3`, 113 cases for `m ≤ 10`
18. Absolute-value factored cap/support bounds for the induction step — overshoot supply 10–70×
    on 1743/1744 real intervals; real `LX` is small by sign cancellation
19. Forward-T7r as a counting tool for the cap — circular (`t`-class sizes are the unbounded quantity)

---

## 8. Files

```
01-attack/        hot-window scan, mechanism analysis, the 91-interval witness
02-defend/        R1/R2/R3 re-derivation and corrections, LX bound, composite kill
03-flank/         route (B) 35-row trend, B_w mod 3^k distribution, cap bounds
04-scout/         option generation, cheap kills, gate
05-session-logs/  the four Muse Code session transcripts
```

All scripts are standalone Python with exact arithmetic (`int` / `fractions.Fraction` /
cyclotomic integers). Floats appear only in trend *discussion*, never in a claimed result.
