# Induction on m for RADIUS-2 CHARGING — verdict: FAILS (obstruction isolated)

Date: 2026-09-14. All arithmetic exact (`fractions.Fraction` / Python ints). No floating point anywhere.
Scripts: `C:\Users\MDP\collatz-analysis\induction\{core,step0_validate,step1_wform,step2_induction,step3_obstruction,step4_base_and_checks,step5_mechanism,step6_hypotheses,step7_final}.py`

**Collatz is NOT solved.** Nothing here claims progress on the Collatz conjecture itself; this is an internal lemma-hunt on the prefix source, and the result is negative.

---

## 0. Convention calibration [EXACT COMPUTATION]

Before any new claim, my independent implementation reproduces every published anchor number:

| anchor | published | mine | match |
|---|---|---|---|
| ADVERSARY 1 (3,2): L_lift | 2 | 2 | yes |
| ADVERSARY 1 (3,2): M_merge | 2/3 | 2/3 | yes |
| ADVERSARY 2 (5,2): L_lift | 9 | 9 | yes |
| ADVERSARY 2 (5,2): M_merge | 101/15 | 101/15 | yes |
| radius-1 CE (18,2) [14,14]: demand | 3/35 | 3/35 | yes |
| radius-1 CE (18,2) [14,14]: supply | 4033/69615 | 4033/69615 | yes |
| radius-1 CE (18,2) [14,14]: gap | 1934/69615 | 1934/69615 | yes |

Radius-2 charging on the real source, m = 2..18, s = 1..m-1 (153 rows): **0 violations**; radius-1 on the same grid: **1 violation** (at (18,2), the documented one). Conventions are locked.

---

## 1. PARENT IDENTITY — reproduced [PROOF-reproduction / EXACT COMPUTATION]

    P_{m,k,s+1} = E^par(Q_k) + O^par(Q_{k-1}),   Q_j = P_{m-1,j,s+2}

verified as an **array identity** on 104 levels (m = 2..14, s = 0..m-1), i.e. **1014 independent (m,s,k) array equalities**, zero failures.

### New: three derived identities I needed (each verified on 78 levels, m=2..13, s=1..m-1)

Let `w_k[u] = P_k[u] - P_k[(u+q) mod N]` (the top-bit difference; anti-periodic, `w[u+q] = -w[u]`).

* **(R1)** `L_k = (q / (2 n_k)) * <w_k, T^{3^k} w_k>` — L is a *negacyclic autocorrelation of w alone*. [78/78]
* **(R2)** `M_j = (q/4) * ||Y_j||^2 / (n_j n_{j-1}(n_j+n_{j-1}))`, `Y_j = n_{j-1} E(w_j) - n_j O(w_{j-1})` — M is a *squared norm in the same w variables*. [78/78]
* **(R3) DIFFERENTIATED PARENT IDENTITY**: `w_k^{(m,s)} = E^par(w'_k) + O^par(w'_{k-1})` — the difference operator intertwines with the transfer. [77/77]

R1+R2 put both sides of the conjecture in one variable set; R3 is the exact induction step in those variables. This is the cleanest formulation of the step available and it is what makes the failure diagnosable rather than vague.

---

## 2. The induction, written out

**IH(m-1, s+1):** for all `1 <= a <= b <= m-1`, `sum_{k=a..b} max(L'_k,0) <= sum_{j=max(a-1,2)}^{min(b+2,m-1)} M'_j`.
**Goal(m, s):** the same statement at level (m,s).
**Base:** the diagonal s = m-1 (where the parent map terminates).

Substituting R3 into R1 splits the child demand exactly three ways:

    L_k = (q/(2 n_k)) * ( LE_k + LO_k + LX_k )
      LE_k = <E'a_k,    T^{3^k} E'a_k   >        (parent stratum k alone)
      LO_k = <O'a_{k-1}, T^{3^k} O'a_{k-1}>      (parent stratum k-1 alone)
      LX_k = 2 <E'a_k,  T^{3^k} O'a_{k-1}>_sym   (CROSS term)

The parent's L' controls only diagonal quantities of the form `<a_j, T^{3^j} a_j>`. `LE_k` and `LO_k` are *transferred* diagonal terms and `LX_k` is a genuinely **new off-diagonal pairing between two different parent strata that the parent-level statement never sees**.

---

## 3. VERDICT: **(c) THE STEP FAILS** [FAIL]

Two independent, exactly-witnessed obstructions.

### Obstruction A — the hypothesis goes vacuous exactly where it is needed [EXACT COMPUTATION]

On **25 real levels** (m = 3..14), the parent has *total demand 0* (every `L'_k <= 0`, so IH reads `0 <= supply` — vacuously true, carrying no information) while the **child has strictly positive demand**:

| child (m,s) | parent demand | child demand | child supply |
|---|---|---|---|
| (4,2) | 0 | 8/3 | 17/3 |
| (5,3) | 0 | 2 | 206/15 |
| (7,3) | 0 | 16/5 | 2762/105 |
| (10,2) | 0 | 158/63 | 2804/315 |
| (10,9) | 0 | 128/7 | 40256/15 |
| (13,12) | 0 | 11776/99 | 1725149696/45045 |
| (14,12) | 0 | 4096/39 | 722499584/15015 |

(full list of 25 in `final_report.json`)

No monotone comparison can transport `0 <= S'` into `11776/99 <= S`. **Demand is created from nothing by the transfer**, so the step has no content on precisely these levels. Crucially, `(13,12)` and `(14,13)` are *on/adjacent to the diagonal* — the supposedly easy base region is itself a place where the step is vacuous going forward.

**Mechanism, isolated exactly:** on those levels, **18 of 23** positive child strata have their positivity driven by the cross term `LX_k`, and in **13** of them the demand comes *entirely* from `LX` (`LE + LO <= 0`). Examples:

* (5,4) k=3: `L = 8/3`, `LE = 0`, `LO = 0`, `LX = 8/3` — both parent-diagonal parts vanish.
* (7,6) k=5: `L = 64/15`, `LE = LO = 0`, `LX = 64/15`.
* (10,8) k=8: `L = 64/9`, `LE = LO = 0`, `LX = 64/9`.
* (8,6) k=5: `L = 128/35`, `LE = 64/35`, `LO = -256/35`, `LX = 64/7` — the diagonal parts sum *negative*, the cross term overturns it.

### Obstruction B — logical non-implication, with exact witnesses [EXACT COMPUTATION]

Even where IH is non-vacuous, it does not imply the goal. Searching the class of parent tuples with the **correct binomial masses** (the same class both published adversaries inhabit) and pushing them through the *proved* transfer:

**Witness W(4,2)** — parent (3,3), child (4,2), masses (1,2,1) -> (1,3,3,1), all correct.
Parent arrays on Z/16: `Q_1 = e_14`, `Q_2 = 2·e_6`, `Q_3 = e_4`.
* Parent: `L' = (0,0,0)`, `M' = (0, 16/3, 16/3, 0)` -> **IH holds, 0 violations over all intervals.**
* Child: `P_1=(0,0,0,0,0,0,0,1)`, `P_2=(0,0,1,2,0,0,0,0)`, `P_3=(0,0,1,0,0,0,0,2)`, `P_4=(0,0,0,0,0,0,0,1)`
  `L = (0, 8/3, 8/3, 0)`, `M = (0, 10/3, 0, 4/3, 0)`
* Child **violates** radius-2 on intervals [1,3],[1,4],[2,3],[2,4]: demand **16/3** vs supply **14/3**, gap **2/3**.

**Witness W(6,2)** — parent (5,3), child (6,2), masses (1,4,6,4,1) -> (1,5,10,10,5,1), all correct.
* Parent: `L' = (0,0,0,0,0)`, `M' = (0, 22/5, 62/15, 14/15, 2, 0)` -> **IH holds.**
* Child: `L = (0, 16/5, 8/5, 6/5, 0, 0)`, `M = (0, 8/15, 4/3, 4/5, 10/3, 10/3, 0)`
* Child **violates** on [1,2] and [2,2]: demand **16/5** vs supply **8/3**, gap **8/15**.

Both re-verified independently from the arrays. **Conclusion: {parent identity} + {IH at level (m-1,s+1)} + {binomial masses} is logically insufficient to derive the statement at (m,s).** The witnesses are not pathologies of my code — they satisfy every structural constraint the induction argument was using.

### Transfer directionality (why no uniform factor exists)

On the real grid (m=3..13, 65 levels):
* Demand **inflates** (`D_child > D_parent`) on **21/65** levels, max finite ratio **47/20** at (11,9).
* Supply **contracts** (`S_child < S_parent`) on **64/65** levels, min ratio **48779/173364** at (12,2).

So the transfer moves the two sides in the **wrong directions simultaneously**: it can more than double demand while shrinking supply to ~28%. A factor-`alpha` transport argument would need `D_c/D_p <= alpha <= S_c/S_p`; **no such alpha exists on 33 levels** (20 of them because `D_p = 0 < D_c`, the rest e.g. (7,2): `D_c/D_p = 2` but `S_c/S_p = 1255/2002`; (8,5): `15/14` vs `123/200`).

### Base case — what the diagonal actually gives

The diagonal base is genuinely easy and I confirm it [EXACT COMPUTATION, m=2..12, 0 violations]: max entry <= 5, most rows have *zero* positive strata, and margins are enormous (m=12: demand 0, supply 53966336/3465). But the base being trivial is irrelevant — **the failure is entirely in the step**, and worse, the step is *vacuous in the forward direction from near-diagonal levels* (obstruction A hits (13,12), (14,13)). The base carries no usable information downward.

---

## 4. Adversary consistency check [required sanity gate — PASSED]

A correct derivation must **not** prove the inequality for ADV1 or ADV2, since both violate it.

* My argument proves **nothing** — it is a failure analysis — so it trivially cannot prove anything false. Gate passes vacuously but meaningfully: I explicitly checked that no step of the attempted derivation (R1/R2/R3 + monotone transport) ever concludes the inequality.
* Sharper: I checked where the real source's structure *would* have to enter. **ADV1 is NOT in the image of the transfer** — exhaustive search over all 256 parent configurations at (2,3) with correct masses finds **zero preimages** mapping to ADV1's arrays. So the parent identity alone already excludes ADV1; a transport argument would not need caps/support to kill it.
* **But my own witnesses W(4,2), W(6,2) ARE in the image** (constructed through it), have correct binomial masses, satisfy IH at the parent — and violate the child inequality. This is the decisive point: the parent identity's image constraint is *not* strong enough.
* **Where the real structure must enter (and where my attempt does not use it):** the witnesses are excluded from the real source only by (H1) the per-stratum max-entry cap and (H2) the support. W(4,2) has per-k caps `[1,2,2,1]` where the real source at (4,2) has `[1,1,1,1]`; its *parent* already exceeds the real (3,3) cap (2 vs 1). Supports also disagree: W(4,2)'s `P_1` sits at `u=7`, the real one at `u=1`. This matches the archive's recorded dead-path lesson (ADV2 breaks caps -> "max-entry cap is load-bearing"). **My attempted induction uses neither cap nor support anywhere — which is exactly why it fails.** Any argument that did close while using only masses + parent identity would be provably wrong, since W(4,2)/W(6,2) satisfy both and violate the conclusion.

---

## 5. What remains unproved [exact statement]

RADIUS-2 CHARGING remains **[CONJECTURE]**, unproved:

> For all m >= 2, all s in [1,m-1], all 1 <= a <= b <= m:
> `sum_{k=a..b} max(L_k,0) <= sum_{j=max(a-1,2)}^{min(b+2,m)} M_j`,
> where L, M are built from the **real** prefix source `P_{m,k,s+1}`.

Status: 153 exact rows (m=2..18), 0 violations, 1923 binding intervals — but no proof.

Induction on m via the parent map is now a **dead path**, with two exact witness families. To revive it, one would need a strictly stronger induction hypothesis that (i) is non-vacuous when all `L'_k <= 0`, (ii) controls the *off-diagonal* pairings `<E'a_k, T^{3^k} O'a_{k-1}>` between adjacent parent strata, and (iii) carries the real source's per-stratum max-entry cap and support down the parent chain. Candidate open sublemma, itself unproved:

> **[CONJECTURE, untested at scale]** There is a cap function `cap_k(m,s) = max_u P_{m,k,s+1}[u]` that is (a) inductively propagated by the transfer and (b) strong enough to bound `|LX_k|`. Observed real values at s=2: (4,2)`[1,1,1,1]`, (8,2)`[1,2,4,5,8,5,2,1]`, (12,2)`[1,2,10,24,45,64,64,44,23,8,3,1]`.

I did **not** prove this, and did not test it beyond recording the values.

---

## 6. Files

* `C:\Users\MDP\collatz-analysis\induction\core.py` — exact source, operators, L/M, charging test, parent identity
* `C:\Users\MDP\collatz-analysis\induction\step0_validate.py` — adversary calibration + parent identity (1014 array identities)
* `C:\Users\MDP\collatz-analysis\induction\step1_wform.py` — R1/R2/R3 derived identities
* `C:\Users\MDP\collatz-analysis\induction\step2_induction.py` — induction setup, LE/LO/LX decomposition, transfer ratios
* `C:\Users\MDP\collatz-analysis\induction\step3_obstruction.py` — obstructions A and B, witness search
* `C:\Users\MDP\collatz-analysis\induction\step4_base_and_checks.py` — witness re-verification, diagonal base, directionality
* `C:\Users\MDP\collatz-analysis\induction\step5_mechanism.py` — cross-term mechanism, caps/supports
* `C:\Users\MDP\collatz-analysis\induction\step6_hypotheses.py` — candidate extra hypotheses (all refuted or unproved)
* `C:\Users\MDP\collatz-analysis\induction\step7_final.py` — final convention confirmation + consolidated data
* JSON data: `parent_identity_report.json`, `transfer_ratios.json`, `obstruction_report.json`, `diagonal_base.json`, `final_report.json`
