# D1 A/B/C — Independent Zero-Trust Audit Verdict

*(baş araştırmacıya olduğu gibi kopyalanabilir)*

---

## VERDICT

```
[PROOF VALID WITH WORDING REPAIR]
```

Audited against `CP20_TASK8B2_D1_ZERO_TRUST_AUDIT_PROMPT_V2_MANAGER_STRENGTHENED_2026-08-27`,
all 21 mandatory items. No archive engine was read; every sequence was rebuilt
from the definitions.

**Sections A, B, C, D, E, F are mathematically sound.** Two wording repairs are
required (items 15, 16). Neither touches a load-bearing step. All six attacks in
your own `D1_COUNTEREXAMPLE_REPORT.md` were independently reproduced with the
same outcomes.

---

## Numerical status

| Item | Result |
|---|---|
| 1–2 chunk algebra + telescoping | 9,688 tests, 0 violations |
| 3 bounded alphabet under critical-log | `max a_k = 3`, alphabet `{1,2,3}` at κ = 1.053 / 1.5 / 2.0 |
| 4–5 plateau interval + sandwich | 5,999 plateau points, 0 violations |
| 6 trough asymptotic | second-order coefficient is exactly `−κ`; residual `O(1/t)` |
| 8 monotone `ρ_r` on plateau | 1,480 plateaus, 0 violations |
| 11 `r_{k+1} ≡ R_k (mod 2^{A_k+1})` | derived independently; 5,188 tests, 0 violations |
| 13 terminal-injury example | `w=(1,1,1,1,1,1)`, `q=1`: `r_q=1`, `R_q=3 = r_q + 2^{A_q}` |
| 20 verifier re-run ×2 | bit-identical JSON both runs; matches manifest hash |
| 21 package integrity | `CP20_TASK8B2_D1_VERIFY.py` SHA256 reproduces exactly |

**Sharper than stated (item 6).** Your `O(log t_j/k)` has an exact coefficient:

```
ρ_r(t_{j+1}) = ln3·(t_j/t_{j+1}) − κ·ln(t_j)/t_{j+1} + O(1/t_{j+1})
```

Confirmed at κ = 1.053, 1.5, 2.0 with residual ≈ 2×10⁻⁵. You may promote this
into section D; it is free and it makes the trough asymptotic quantitative.

---

## REPAIR 1 (item 15) — simpler than the manager's boundary suggests

The manager asked you to restrict "positive ordinary integer" to post-injury
plateaus, or to assume `r_* > 0` separately. **Neither is necessary — positivity
is derivable.**

`r_1 = −3^{−1} (mod 2^{a_0})` is always **odd**, so `r_1 ≥ 1 > 0 = r_0`. Hence
`k = 0` is *always* an injury index. Consequently `p ≥ 1` is forced (a plateau
with `p = 0` would need `r_0 = r_1`, impossible), and since `r` is
non-decreasing, `r_* ≥ r_1 > 0`.

Verified: `a_0 = 1…24` — `r_1` never 0 or even; `4^6 = 4,096` words — no `r_1 = r_0`,
no decreasing `r`.

**Minimal insertion into the section-F lemma:**

> Since `r_1 = −3^{−1} (mod 2^{a_0})` is odd, `k = 0` is always an injury index;
> hence `p ≥ 1` and, `r` being non-decreasing, `r_* ≥ r_1 > 0`. Positivity
> therefore requires no separate hypothesis.

---

## REPAIR 2 (item 16) — section G item 4 is a TARGET, not a consequence

As written, G-4 ("one fixed positive ordinary integer shadowing essentially
every such exceptionally long plateau") does **not** follow from A/B/C/F, and on
the literal reading it is false: every injury has `m_{t_j} ≥ 1`, so
`r_{t_j+1} > r_{t_j}` — `r` is strictly increasing and **consecutive plateaus
carry strictly different witnesses**.

Measured consecutive plateau witnesses (random `{1,2}` word, 60 steps):

```
1, 3, 11, 27, 91, 603, 4699, 12891, …
```

**Required restatement:**

> 4. *(target for D1-D/D1-E, not derived here)* a single ordinary integer `n₀`
>    agreeing with `r_*` on every such exceptionally long plateau. Sections A–F
>    supply only a **per-plateau** witness, and these witnesses are strictly
>    increasing in `j`.

---

## Minor: `R_0` sentinel

`affine()` initialises `R = [0]`. The correct depth-0 exact lift is `R_0 = 1`
(`c_0 = r_0 = 0` must be odd). Harmless today — `check_word()` never reads it,
because `k = 0` is always an injury and the `if r[k+1]==r[k]` branch never fires
there. But any future extension that reads `R_0` will be silently wrong. Please
set it to `1` or leave an explicit comment.

---

## Novelty classification (item 19, conservative)

| Section | Classification |
|---|---|
| A | restatement of D0 (`m_k` is just `r_{k+1}−r_k` named in units of `2^{A_k}`) |
| B | one-line consequence of `s_{k+1}−s_k = g_k − a_k` |
| C | new but immediate from the canonical ranges |
| **D + E** | **genuinely new structural corollary** — `liminf ρ_r = ln3 · liminf t_j/t_{j+1}` has no D0 counterpart |
| F | restatement of D0's exact-cylinder lemma, plus the correct terminal exception |
| G | not a result; a target list |

The load-bearing novelty is **D/E**. Narrowing the escape scenario from "sparse
injuries" to "**multiplicatively diverging injury gaps**" is a real gain.

---

## Strategic conjunction (audited as requested)

The conjunction is correct, and D1 alone **does not** force `liminf ρ_r = 0` —
it supplies an *equivalence* only. Zero liminf closes only if Kramer's separate
positive-liminf obstruction is imposed from outside. Section H's "No such
sparse-injury branch is excluded" is accurate and appropriately unambitious.

---

## FINDING D (beyond the audit) — a plateau IS a genuine Syracuse orbit

This came out of the audit and bears directly on your new D1-D/D1-E target
(*"sonsuz kaçış için gereken giderek devleşen exact-realizer platolar gerçekten
kurulabilir mi?"*). It uses only frozen D0 objects.

**Definition.** `c_k := (3^k r_k + B_k)/2^{A_k}` — D0's depth-`k` quotient.

**Characterization** (10,432 tests, 0 violations):

```
no injury at k   ⟺   a_k ≤ v₂(3 c_k + 1),
and then          c_{k+1} = (3 c_k + 1)/2^{a_k}.
```

**Rigidity** (5,238 in-plateau steps, 0 violations). If `a_k < v₂(3c_k+1)`
strictly, then `c_{k+1}` is even, so `v₂(3c_{k+1}+1) = 0 < 1 ≤ a_{k+1}` and step
`k+1` **must** injure. Therefore:

> Inside any plateau of length ≥ 2, `a_k = v₂(3c_k + 1)` with **exact equality**;
> only the plateau's final step may be slack, and that step ends the plateau.

Four consequences:

1. **A plateau is literally a Syracuse orbit segment of an ordinary integer.**
   "Shadowing" is not a metaphor.
2. `r_0 = 0 ⟹ c_0 = 0 ⟹ v₂(1) = 0 ⟹ a_0 ≤ 0`, impossible. This is the
   *structural reason* behind Repair 1.
3. **Minimal realizer.** The least positive integer realizing a word
   `w = (a_0…a_{L−1})` is exactly `r_L(w)`. Brute-force checked on 120 words,
   0 discrepancies.
4. **A long plateau costs exactly what it buys.** `log₂ r_L / L → A_L/L → α`
   (L=400: 530/400 = 1.325; L=1600: 2167/1600 = 1.354; α = 1.585), so
   `ln(1+r_*)/L → ln3`. Arbitrarily long plateaus *can* be built — but they do
   not lower `ρ_r`. Zero liminf still requires plateau length to grow
   **super-linearly against the whole prior history**, which is exactly what
   D/E says, reached independently.

**Warning for D1-D.** An *infinite* plateau is equivalent to a divergent
(non-cycling) Collatz trajectory. So "can ever-growing exact-realizer plateaus
be built forever?" **is the LEVEL-3 problem itself**, not an attack surface
independent of it. D1-D should be set up with that equivalence stated up front,
or the search risks assuming what it is trying to establish.

---

## Freeze recommendation

* **D1 A/B/C may be frozen** once Repairs 1 and 2 are applied (both one-liners).
* **D1-D adversarial recursive-countermodel search may resume before D1-E.** Its
  target surface (the multiplicative-gap subsequence) is now precisely defined
  and does not depend on D1-E's Sturmian/continued-fraction machinery. Attach
  Finding D's equivalence as an explicit guard at the top of D1-D.
