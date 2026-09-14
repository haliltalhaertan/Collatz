# CP21 — Source Monotonicity: per-frequency settlement, induction refutation, cap stabilisation

Date: 2026-09-14 · Programme: Collatz research archive · Checkpoint CP21 (follows Round 8)

> **Collatz is NOT solved.** Nothing in this checkpoint bears on the Collatz conjecture itself.
> All work here concerns an internal lemma about the *prefix source* — a finite combinatorial
> object attached to parity words. A finite table is NEVER a uniform theorem, and every
> statement below carries an explicit status label.

---

## 0. Status labels used

| label | meaning |
|---|---|
| `[PROOF]` | proved, with the argument given, and additionally verified numerically |
| `[EXACT COMPUTATION]` | exact rational/integer arithmetic over a stated finite grid — **not** a theorem |
| `[CONJECTURE]` | believed, unproved |
| `[FAIL]` | attempted and refuted, with exact witness |

---

## 1. Setting

Shortcut map `H(x) = (3x+1)/2` for odd `x`, `x/2` for even `x`.
For odd `h < 2^m` with `k` odd-steps, the prefix source is

    P_{m,k,r}(z) = #{ odd h < 2^m : odd-step count = k, H^m(h) ≡ z (mod 2^r) }

with stratum mass `n_k = C(m-1, k-1)`. Odd-character energy
`J_r(X) = 2^(r-1) Σ_{u<2^(r-1)} (X(u) − X(u+2^(r-1)))²`, and `Ecal(m,r) = Σ_k J_r(P_{m,k,r})/n_k`.

Transfer at `N = 2^(s+1)`, `q = 2^s`, `c_k = 3^k mod N`:

    E_k[z] = P_k[2z mod N] + P_k[(2z − c_k) mod N]
    O_k[z] = P_k[3⁻¹(2z−1) mod N] + P_k[(3⁻¹(2z−1) − c_k) mod N]

**Exact identity (established earlier, re-verified here):**

    Ecal(m,s+1) − Ecal(m+1,s) = M_merge − L_lift,      M_merge ≥ 0

**The open lemma:** `M_merge ≥ L_lift`. Two live candidate routes entered CP21:
**(A) radius-2 charging** and **(B) per-frequency positivity**.

---

## 2. Headline results

| # | Result | Status |
|---|---|---|
| 2.1 | The per-frequency index is **forced** to be mod `q`, not mod `N` | `[PROOF]` |
| 2.2 | Candidate (B) **survives** on the forced index — 118/118 pairs positive | `[EXACT COMPUTATION]` |
| 2.3 | Induction on `m` via the parent identity **fails** — two exact obstructions | `[FAIL]` |
| 2.4 | The max-entry cap **stabilises** in `r` once `2^r ≥ 3^k − 1` | `[EXACT COMPUTATION]` |
| 2.5 | Radius-2 charging extended to `m = 26`: 221 rows, 0 violations | `[EXACT COMPUTATION]` |
| 2.6 | Radius-2 margin is **thin and clustered**: min ratio 1.050 | `[EXACT COMPUTATION]` |

Total exact arithmetic checks across the checkpoint: **≈ 4.9 million**, zero arithmetic failures.

---

## 3. Candidate (B): the index is forced `[PROOF]`

The previous round reported per-frequency positivity at `s=2` but an auditor could not verify
it, because **no decomposition specification existed**. CP21 settles this.

`E_k` and `O_k` are functions on `Z/q`. Therefore their spectra are `q`-periodic:

    Ê_k(ξ) = Ê_k(ξ+q),      Ô_k(ξ) = Ô_k(ξ+q)

while the lift weight is `q`-**anti**-periodic:

    cos(2π c_k (ξ+q)/N) = − cos(2π c_k ξ/N)

Both verified exactly (1294 `(k,ξ)` pairs in the subagent run; independently re-verified by the
lead on 64/64 pairs at `s=3, m=8`).

**Consequence.** The merge side carries *no information* at the mod-`N` level. Splitting `M`
between `ξ` and `ξ+q` is an **invention, not a decomposition**. The unique common index on which
both `M^(a)` and `L^(a)` are well defined is `a` odd mod `q = 2^s`, with the lift contributions of
`ξ` and `ξ+q` **summed**:

    L^(a) = Σ_k (1/n_k) Σ_{ξ ∈ lifts_k(a)} cos(2π 3^k ξ/N) |P̂_k(ξ)|²
    M^(a) = Σ_k Σ_{ξ ∈ lifts_k(a)} |n_{k−1}Ê_k(ξ) − n_k Ô_{k−1}(ξ)|² / (2 n_k n_{k−1}(n_k+n_{k−1}))
    Δ^(a) = M^(a) − L^(a)

`M^(a) ≥ 0` termwise `[PROOF]` — each summand is `|·|²` over a positive denominator.

**Correctness criterion:** `Σ_a Δ^(a) = defect` exactly as rationals. Holds on all 41 rows, for
all three stratum-gauge variants tried.

### 3.1 Verdict: SURVIVES `[EXACT COMPUTATION]`

    mandated grid (s ∈ {2,3,4}, m = 4..12):   0 / 118 pairs negative
    extended grid (41 rows incl. s=5, m≤14):  0 negative

Exact minimum on the mandated grid: `≈ 1.366376389…` at `(m,s) = (5,4)`, `a = 3`, an element of
`Z[ζ_32]` whose positivity is certified by rational enclosure (no floating point).
Smallest rational value: `3/2` at `(4,2)`, `a ∈ {1,3}` — **exactly reproducing the prior
session's number**, now with a specification behind it.

### 3.2 Two warnings that must travel with this result

1. **The margin shrinks.** Extended-grid minimum is `≈ 0.2017` at `(13,4)`, `a=5` — an order of
   magnitude below the mandated-grid minimum. This does not look like a robust inequality.
2. **The carrier moves.** The frequency carrying positive lift is not fixed: it tracks `a ≈ q/3`
   (the gauge orbit of `3^{−k}`), fluctuates with `m`, and vanishes entirely on some rows.
   Carriers always appear in conjugate pairs `{a, q−a}`.

### 3.3 Convention sensitivity — a trap recorded for the future

If one refines to mod `N` and splits `M` evenly between the two lifts, `Δ^(a) < 0` appears on
**26/26 rows** (first at `(4,2)`, `a=1`). This is **not a counterexample** — it is an artefact of
an invalid refinement (§3). But it means: **this result must never be quoted without its index.**

---

## 4. Induction on `m`: refuted `[FAIL]`

The parent identity `P_{m,k,s+1} = E^par(Q_k) + O^par(Q_{k−1})`, `Q_j = P_{m−1,j,s+2}`
(verified here as an array identity on 104 levels / 1014 array equalities) suggests an induction
descending from the sparse diagonal `s = m−1`. CP21 tested this and it **fails**.

### 4.1 New derived identities (each verified on 78 levels)

With `w_k[u] = P_k[u] − P_k[u+q]` (top-bit difference, anti-periodic):

* **(R1)** `L_k = (q / 2n_k) · ⟨w_k, T^{3^k} w_k⟩` — L is a negacyclic autocorrelation of `w` alone
* **(R2)** `M_j = (q/4) · ‖Y_j‖² / (n_j n_{j−1}(n_j+n_{j−1}))`, `Y_j = n_{j−1}E(w_j) − n_j O(w_{j−1})`
* **(R3)** `w_k^{(m,s)} = E^par(w'_k) + O^par(w'_{k−1})` — the difference operator intertwines
  with the transfer (77/77)

R1+R2 place both sides in one variable set; R3 is the exact induction step in those variables.
**This formulation is what makes the failure diagnosable rather than vague — it is the durable
product of this line, even though the line died.**

### 4.2 Obstruction A — the hypothesis goes vacuous exactly where it is needed

Substituting R3 into R1 splits child demand three ways:

    L_k = (q/2n_k)( LE_k + LO_k + LX_k )

where `LE_k`, `LO_k` are transferred *diagonal* terms and `LX_k` is a **cross term** pairing two
*different* parent strata — a quantity the parent-level statement never sees.

On **25 real levels** (`m = 3..14`) the parent has total demand `0` (so IH reads `0 ≤ supply`,
vacuous) while the child has strictly positive demand:

| child (m,s) | parent demand | child demand | child supply |
|---|---|---|---|
| (4,2) | 0 | 8/3 | 17/3 |
| (10,9) | 0 | 128/7 | 40256/15 |
| (13,12) | 0 | 11776/99 | 1725149696/45045 |
| (14,12) | 0 | 4096/39 | 722499584/15015 |

**Demand is created from nothing by the transfer.** Mechanism isolated exactly: of 23 positive
child strata on those levels, **18** have positivity driven by `LX_k`, and in **13** the demand
comes *entirely* from `LX` (`LE + LO ≤ 0`). E.g. `(7,6) k=5`: `L = 64/15`, `LE = LO = 0`,
`LX = 64/15`. E.g. `(8,6) k=5`: `LE = 64/35`, `LO = −256/35` (diagonal parts sum negative), the
cross term `64/7` overturns it.

Note `(13,12)` and `(14,13)` are on/adjacent to the diagonal — **the supposedly easy base region
is itself where the step is vacuous going forward.**

### 4.3 Obstruction B — logical non-implication, with exact witnesses

Even where IH is non-vacuous it does not imply the goal. Two witnesses with **correct binomial
masses**, inside the image of the transfer, satisfying IH at the parent, **violating** at the child:

**W(4,2)** — parent `(3,3)` on `Z/16`: `Q_1 = e_14`, `Q_2 = 2·e_6`, `Q_3 = e_4`.
Parent `L' = (0,0,0)`, `M' = (0, 16/3, 16/3, 0)` → IH holds, 0 violations.
Child `L = (0, 8/3, 8/3, 0)`, `M = (0, 10/3, 0, 4/3, 0)` → violates on `[1,3],[1,4],[2,3],[2,4]`:
demand **16/3** vs supply **14/3**, gap **2/3**.

**W(6,2)** — parent `(5,3)`, masses `(1,4,6,4,1) → (1,5,10,10,5,1)`.
Parent `L' = 0` everywhere → IH holds. Child violates on `[1,2]`, `[2,2]`: demand **16/5** vs
supply **8/3**, gap **8/15**.

**Conclusion:** `{parent identity} + {IH} + {binomial masses}` is **logically insufficient**.

### 4.4 Directionality — no uniform transport factor exists

On the real grid (`m = 3..13`, 65 levels): demand **inflates** on 21/65 levels (max ratio 47/20
at `(11,9)`); supply **contracts** on 64/65 levels (min ratio 48779/173364 at `(12,2)`).
A factor-`α` argument needs `D_c/D_p ≤ α ≤ S_c/S_p`; **no such α exists on 33 levels.**

### 4.5 Adversary consistency gate — PASSED

A correct derivation must **not** prove the inequality for the known adversaries ADV1 `(3,2)`
and ADV2 `(5,2)`, which violate it. Checked: no step of the attempted derivation ever concludes
the inequality. Sharper finding: **ADV1 is not in the image of the transfer** (exhaustive search
over all 256 parent configurations at `(2,3)` with correct masses → zero preimages), so the
parent identity alone already excludes it.

But **W(4,2) and W(6,2) *are* in the image**, have correct masses, satisfy IH — and violate.
They are excluded from the real source only by the **max-entry cap** and the **support**:
W(4,2) has per-`k` caps `[1,2,2,1]` where the real source at `(4,2)` has `[1,1,1,1]`.
**The attempted induction used neither cap nor support anywhere — which is exactly why it failed.**

### 4.6 What would be needed to revive it

A strictly stronger induction hypothesis that (i) is non-vacuous when all `L'_k ≤ 0`,
(ii) controls the off-diagonal pairings `⟨E'a_k, T^{3^k} O'a_{k−1}⟩`, and (iii) carries the real
source's cap and support down the parent chain. Not attempted.

---

## 5. The max-entry cap: no proof, but a structural gain `[EXACT COMPUTATION]`

`cap(m,k,r) = max_z P_{m,k,r}(z)` is **load-bearing** (§4.5, and an earlier adversarial family
that respected supports and masses but exceeded the real caps broke the target inequality), yet
it was only ever an observed fact. CP21 attacked it via the 2-adic isometry

    v₂(B_w − B_w') = v₂(h_w − h_w')     (same-weight words; 4.36M exact pair checks, 0 failures)

**The cap itself remains unproved.** But four supporting lemmas were proved along the way, each
re-derived from scratch and re-verified by the lead researcher in independent code:

| lemma | statement | independent re-verification |
|---|---|---|
| **T2** range | `1 ≤ e_w ≤ 3^k − 1` | 8,190 cases, 0 violations |
| **T7** 3-adic criterion | `e_w = e_w'` ⟺ `B_w ≡ B_w' (mod 3^k)` | 68,887 pairs, 0 failures |
| **T4** spread | `M(m,k) ≤ ⌊2^(m−k)(3^(k−1)−2^(k−1))/3^k⌋ + 1` | 135 cells, 0 violations, exact in 48 |
| **T6** parent identity | `cap(m,k,r) ≤ 2·cap(m−1,k,r+1) + 2·cap(m−1,k−1,r+1)` | 3,224 array equalities, 714 cells, 0 violations |

**T7 is the sharpest:** an endpoint collision is *exactly* a congruence of affine offsets mod `3^k`.

> **Pitfall recorded.** A naive check of the T6 corollary reports **14 violations** — all at `m=2`,
> where the parent level is absent from the table and `.get(key,0)` silently returns `0`, making the
> bound vacuously `0`. Missing data, not violations. Filter to cells whose parent exists.

**T7r (general `r`) — the stated `iff` is FALSE `[FAIL]`, but one direction survives and it is the
direction that matters.** The script asserted

    e_w = e_w' (mod 2^r)   <==>   exists t, |t| <= (3^k-2)/2^r,  B_w - B_w' = 2^(m+r)*t  (mod 3^k)

Run to completion it gives **356,259 failures out of 2,896,792 checks (12%)**. Independently
re-derived by the lead: the minimal counterexample is `(m,k,r) = (4,2,1)`, words `h=1` and `h=13`
with `e=1`, `e'=8` — the `t`-condition holds while the endpoints do **not** collide mod 2.

Splitting by direction (lead, 17,808 checks):

| direction | result |
|---|---|
| `e = e' (mod 2^r)` implies `exists t` | **2,032 ok, 0 broken** — holds |
| `exists t` implies `e = e' (mod 2^r)` | 2,032 ok, **2,143 broken** — fails |

So the `t`-condition is **necessary but not sufficient**: the admissible `t`-range is too generous
and over-counts. Crucially, **an upper bound on the cap only needs the necessary direction**, which
is why `Mbnd`/`capbnd` survive intact (832 cells, 0 violations) despite the `iff` being false.
The `iff` must be struck from the record; the forward implication may be cited.

### 5.1 Two natural targets REFUTED

* `cap ≤ 2^(m−r)` is **FALSE** — 123 counterexamples (e.g. `(m,k,r) = (2,1,3)`: cap 1 vs bound 0)
* `cap ≤ C` for an absolute constant is **FALSE** — `M(m,k)` reaches 39 at `(20,6)`

### 5.2 The gain: stabilisation

> **Once `2^r ≥ 3^k − 1`, `cap(m,k,r)` no longer depends on `r`.**

Verified on 312 cases in the subagent run; independently re-verified by the lead on 65/65 cases
(`m = 3..12`). Writing `M(m,k)` for the stabilised value, a bound was proved against it with
**0 violations on 832 cells**, beating the trivial bound `n_k` in 381 (46%), and in the
stabilised regime (308 cells) it is **exact in 268 of them** (median tightness 1.00).

This converts an infinite family of quantities into a **finite** table — a real step from
"observed on a grid" toward a theorem, though **the cap itself remains unproved**.

### 5.3 The obstruction, quantified

The provable interval bound degrades against the truth as `m−k` grows:

| m−k | true max M | provable bound | ratio |
|---|---|---|---|
| 8 | 7 | 86 | 12.3 |
| 11 | 21 | 683 | 32.5 |
| 14 | 39 | 5462 | 140.1 |
| 17 | 11 | 43691 | 3972 |

A square-root-type gap. The isometry constrains *which* collisions can occur but does not by
itself bound *how many*.

---

## 6. Radius-2 charging: extended and stress-tested `[EXACT COMPUTATION]`

**Statement.** For all `m ≥ 2`, `s ∈ [1, m−1]`, and all `1 ≤ a ≤ b ≤ m`:

    Σ_{k=a..b} max(L_k, 0) ≤ Σ_{j=max(a−1,2)}^{min(b+2,m)} M_j

### 6.1 Extension to m = 26

Eleven new rows computed by the lead (`m=25`, `s=1..6`; `m=26`, `s=2..6`), requiring enumeration
to `m=27` (67M odd starts). Results:

| test | result |
|---|---|
| monotonicity (defect ≥ 0) | 11/11 |
| **radius-2 charging** | **0 violations** |
| `M ≥ L⁺` | 11/11 |
| new rows with `L > 0` | none |
| binding-interval share | **72%** |

Cumulative: **221 exact rows, 0 radius-2 violations.**

The binding share rose from 53% (old grid, per the CP21 audit) to 72% on the new rows — the
statement does more work as the grid grows. `(26,2)` produced **five new radius-1 witnesses**
(cuts `[13,13]`…`[15,15]`), confirming radius-1's failure is systematic, not incidental.

### 6.2 The margin is thin and clustered — where to hunt

Using the proved necessary condition (a minimal violating interval must have `L > 0` at **both**
endpoints), 1690 candidate intervals were ranked by supply/demand ratio:

| row | interval | ratio |
|---|---|---|
| **(20,3)** | [14,16] | **1.050** |
| (20,3) | [14,17] | 1.147 |
| (21,3) | [14,16] | 1.158 |
| (22,2) | [15,16] | 1.253 |

The narrowest margin is **5%**, and the twelve narrowest all sit in
`m ∈ {20,21,22}`, `s ∈ {2,3}`, `k ≈ 14–17` — **the same region where radius-1 collapses.**
If a counterexample exists, it is there. Blind grid extension is the wrong search strategy;
deepening this window is the right one.

*Honest caveat:* no evidence that the margin narrows *with* `m` — rows at `m = 25, 26` showed
nothing this tight. "Thin in places" is supported; "narrowing" is not.

---

## 7. Corrections to prior rounds

Three mislabellings from Round 8 were caught by the read-only audit and confirmed independently:

1. **`s=1` is degenerate on one side only.** Only the *lift* vanishes (`L ≡ 0`, 23/23 rows);
   `M > 0` on 22/23. The earlier claim "both sides vanish" is **wrong**. `s=1` rows carry zero
   information about lift/charging and must not be counted as evidence for it.
2. **"pointwise-k charging fails, 8 witnesses" was mislabelled.** True pointwise (`L_k > M_k`)
   fails **46** times; the **8** figure belongs to radius-1 singleton (`L_k > M_k + M_{k+1}`).
   The quoted supply `4033/69615` is a neighbour sum, not `M_14`.
3. **"0 violations on 210 rows" must be quoted with its vacuity rate.** 47% of the 29,835
   intervals have zero demand; excluding `s=1`, the binding share is ≈58%.

---

## 8. What is open

| item | status |
|---|---|
| `M_merge ≥ L_lift` (the target) | **open** |
| Radius-2 charging | `[CONJECTURE]` — 221 rows, 0 violations, no proof |
| Per-frequency positivity `Δ^(a) ≥ 0` | `[CONJECTURE]` — 41 rows, margin shrinking |
| Max-entry cap bound | `[CONJECTURE]` — stabilised, still unproved |
| Induction on `m` | `[FAIL]` — dead path, two exact witnesses |

**Methodological note, repeated from the archive's own audit layer:** every result in this
checkpoint was produced and checked by AI systems. Sign errors and mislabellings are caught
reliably (three were, §7). Errors of the form "this entire strategy is categorically
misconceived" are *not* reliably caught. Formalisation in Lean, or review by a human expert,
remains worth more than further rounds of the same kind.

---

## 9. Files

```
01-freq-defect/     candidate (B): exact Z[ζ_N], forced-index proof, 41-row grid
02-cap-bound/       cap attack: isometry verification, refutations, stabilisation
03-induction/       induction refutation: R1/R2/R3, obstructions A/B, witnesses
04-lead-extension/  m=25,26 rows (JSON) + CP21 literature sweep
05-muse-sessions/   Muse Code session logs (BRIDGE, AUDIT, PROVE)
```

Reproduce: each directory's scripts are standalone Python (exact arithmetic; `numpy` only for
enumeration in the lead extension).

---

## 10. Literature (swept 2026-09-14) — open actions

* **arXiv:2607.24844** Fernández–Ibáñez, *Christoffel Words as Extremal Structures in Collatz
  Dynamics* (Jul 2026). Proves Christoffel words are the unique maximisers of `C_min` and derives
  explicit lower bounds for orbit minima. **Two actions:** (i) quantitatively compare against the
  archive's frozen CP19 T3 (novelty risk — same shape of statement); (ii) note in the archive that
  CP06's Christoffel refutation concerned a *different* object (2-adic least realiser `R_j(v)`,
  not Archimedean `C_min`) — otherwise a future reader will think one of them is wrong.
* **ccchallenge.org** — a live project formalising the Collatz literature in Lean: 375 catalogued
  sources, 6 formalisations awaiting audit, **0 auditors**. This is the concrete answer to the gap
  the archive itself records ("no human or Lean verification anywhere; the AI–AI audit loop is its
  own ceiling"). Suggested: have the Task 6+7 pressure clamp formalised.
* **arXiv:2603.11066 v5** (Chang, Apr 2026) — newer than the version the archive swept; adds a
  "Sturmian obstruction", a Carry Contamination Theorem, and an unconditional 2-adic measure
  contraction `μ₂(T_j) ≤ 0.522^{jD}`. The Sturmian language collides directly with this
  programme's phase-word machinery. Unaudited preprint — treat with care.
* **Knight 2026**, *Collatz high cycles do not exist*, Discrete Math 349(3) — touches Side B.
