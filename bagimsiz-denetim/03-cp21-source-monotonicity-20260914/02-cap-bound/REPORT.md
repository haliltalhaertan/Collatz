# Max-entry cap: attack via the 2-adic isometry — no proof of the cap, but four proved lemmas and a structural gain

Date: 2026-09-14 · CP21 · Scripts in this directory

> **Collatz is NOT solved.** This is an internal lemma about the prefix source.
> A finite table is NEVER a uniform theorem.

## Why this matters

`cap(m,k,r) = max_z P_{m,k,r}(z)` is **load-bearing** for the programme's target inequality:
an adversarial family that respected the real supports and the correct binomial masses but
*exceeded* the real caps was shown to break the inequality, and separately the induction attempt
(`../03-induction/`) failed precisely because it used neither the cap nor the support. Yet the cap
was only ever an *observed* fact over a finite grid. This session attacked it.

**Bottom line: the cap is still `[CONJECTURE]`.** But four supporting lemmas were proved, two
natural targets were refuted, and one genuinely useful structural fact was established.

---

## 1. The tool

`[PROOF]` For two distinct words `w, w'` of the same weight `k`:

    v2(B_w - B_w') = v2(h_w - h_w')

From `2^m·e_w = 3^k·h_w + B_w`. Verified on 289,273 word pairs (4.36M checks across the identity
family `I1`–`I7`, zero failures).

## 2. Proved lemmas

**T2 (range)** `1 <= e_w <= 3^k - 1`. *Independently re-verified by the lead: 8,190 cases, 0 violations.*

**T7 (3-adic exact-collision criterion)** — the sharpest result of this line:

    e_w = e_w'   <==>   B_w ≡ B_w'  (mod 3^k)

A collision of endpoints is *exactly* a congruence of the affine offsets mod `3^k`.
*Independently re-verified by the lead: 68,887 word pairs, 0 failures.*

**T4 (B-spread / diameter)** leads to

    M(m,k) <= floor( 2^(m-k)·(3^(k-1) - 2^(k-1)) / 3^k ) + 1

*Independently re-verified by the lead: 135 cells (m=2..16), 0 violations, exact in 48.*

**T6 (parent identity for the cap)**

    P_{m,k,r}(z) = Q_k(a) + Q_k(a-3^k) + Q_{k-1}(c) + Q_{k-1}(c-3^(k-1)),
    Q_j = P_{m-1,j,r+1},  a = 2z mod 2^(r+1),  c = 3^(-1)(2z-1) mod 2^(r+1)

giving `cap(m,k,r) <= 2·cap(m-1,k,r+1) + 2·cap(m-1,k-1,r+1)`.
*Independently re-verified by the lead: 3,224 array equalities from scratch, 0 failures;
corollary holds on 714 cells, 0 violations.*

> **Pitfall recorded.** A naive check of the T6 corollary reports **14 violations**. All 14 are at
> `m = 2`, where the parent level `m-1 = 1` is absent from the table and `.get(key, 0)` silently
> returns `0`, making the bound vacuously `0`. These are **missing data, not violations**. Filter to
> cells whose parent actually exists before reporting.

## 3. Two targets REFUTED `[EXACT COMPUTATION]`

| target | verdict | evidence |
|---|---|---|
| `cap <= 2^(m-r)` | **FALSE** | 123 counterexamples, e.g. `(m,k,r) = (2,1,3)`: cap 1, bound 0 |
| `cap <= C` (absolute constant) | **FALSE** | `M(m,k)` reaches **39** at `(20,6)` |

## 4. The gain: stabilisation `[EXACT COMPUTATION]`

> **Once `2^r >= 3^k - 1`, `cap(m,k,r)` no longer depends on `r`.**

This follows in spirit from T2+T7 (beyond that threshold, congruence mod `2^r` can no longer
merge distinct residues that `3^k` separates), and is verified on 312 cases in this directory.
*Independently re-verified by the lead: 65/65 cases, `m = 3..12`.* The lead additionally checked
stabilisation in `m` at fixed `m-k`, confirmed for `m-k <= 8`.

**Why it is worth having:** an infinite family of quantities `{cap(m,k,r) : r}` collapses to a
**finite** table `M(m,k)`. This moves the cap from "observed on a grid" toward a determinate
object, which is what any future proof will have to bound.

Against `M(m,k)`, the proved bound `Mbnd` gives:

    M-bound:    209 cells, 0 violations, tightness min 1.00 / median 3.00 / max 121.6
    cap-bound:  832 cells, 0 violations, beats trivial n_k in 314 (38%)
    stabilised regime: 308 cells, tightness median 1.00, EXACT in 160

## 5. The obstruction, quantified

The provable interval bound degrades against the truth as `m-k` grows:

| m-k | true max M | provable bound | ratio |
|---|---|---|---|
| 8 | 7 | 86 | 12.3 |
| 11 | 21 | 683 | 32.5 |
| 14 | 39 | 5462 | 140.1 |
| 17 | 11 | 43691 | 3972 |

A square-root-type gap. **The isometry constrains *which* collisions can occur; it does not bound
*how many*.** That is the precise reason the cap remains unproved, and any future attempt needs a
counting input the isometry does not supply.

## 6. Provenance

This directory's agent session was interrupted (subscription quota) after `step5_refined.py` was
written. The lead researcher ran `step3_bounds.py` and `step5_refined.py` to completion, and
re-derived T2, T7, T4 and T6 from scratch in independent code rather than trusting the scripts.
`step4_3adic.py` was left unrun: its `T7r` loop iterates over a range of size `~3^13`, which does
not terminate in reasonable time. Its *conclusions* (the `Mbnd`/`capbnd` tables, the T6 corollary)
were evaluated separately by the lead and are reported above; its `T7r` general-`r` claim is
therefore **NOT verified** and must not be cited.

## 7. Status summary

| claim | status |
|---|---|
| Isometry `v2(B-B') = v2(h-h')` | `[PROOF]`, 4.36M checks |
| T2 range, T7 3-adic criterion, T4 spread, T6 parent identity | `[PROOF]`, all re-verified independently |
| T7r (general `r` criterion) | **unverified** — script never ran |
| Stabilisation `2^r >= 3^k - 1` | `[EXACT COMPUTATION]`, 312 + 65 independent |
| `cap <= 2^(m-r)`, `cap <= C` | `[FAIL]` — refuted |
| **A proved bound on the cap** | **`[CONJECTURE]` — still open** |

## 8. Files

| file | role |
|---|---|
| `collatz_cap_core.py` | source, words, `B_w`, histograms, caps |
| `step1_selftest.py` | calibration against published anchors |
| `step2_isometry.py` | isometry + derived identities (4.36M checks) |
| `step3_bounds.py` | bound candidates, stabilisation, growth check |
| `step4_3adic.py` | **does not terminate** — see §6 |
| `step5_refined.py` | refined bounds, refutations, obstruction table |
| `cap_table.json`, `M_table.json` | computed caps and stabilised values |
