# CP23 — Strategic review: the intended chain to Collatz is broken

Date: 2026-09-14 · Collatz research archive · Checkpoint CP23 (follows CP22)
Four parallel Muse Code strategy sessions (CARTOGRAPH / BARRIER / SALVAGE / REDIRECT).
No session was allowed to work on radius-2 charging, the cap, or per-frequency positivity.

> **Collatz is NOT solved.** This checkpoint contains no progress toward it — it contains a
> proof that the programme's intended route cannot reach it.

---

## 0. Headline: the route is dead, with a proof

The programme's working chain was:

    1. a counterexample has an orbit
    2. the orbit's residues mod 2^r behave somehow
    3. if Collatz MIXES, a counterexample has nowhere to hide
    4. mixing requires non-uniformity to decrease
    5. that is the open target  Ecal(m,s+1) >= Ecal(m+1,s)

**Step 3 is FALSE.** `[PROOF]` + `[EXACT COMPUTATION]`, verified independently by the lead:

> `3n+1` and `3n−1` have **identical** `Ecal` tables — same total, same per-stratum, and hence the
> same defect and the same target inequality. Lead-verified on **50/50** `(m,r)` pairs and **30/30**
> defect rows, zero differences.
>
> **But `3n−1` provably has nontrivial cycles:** `5 → 7 → 10 → 5`, and
> `17 → 25 → 37 → 55 → 82 → 41 → 61 → 91 → 136 → 68 → 34 → 17`.

Therefore any proof of the target inequality would apply verbatim to `3n−1`, where cycles exist.
**The inequality cannot exclude a cycle.** Mixing in this programme's sense is *compatible* with
counterexamples.

Structural reason `[PROOF]`: `H_{3n-1}(−x) = −H_{3n+1}(x)`; the two maps share the same `B_w`,
odd residues pair as `h ↔ 2^m − h`, endpoints map by `u ↦ −u + 3^k`, and `J_r` is invariant under
that map. The energy functional is **blind to the sign of the affine constant** — exactly the
datum that decides whether cycles exist.

`5n+1` gives the same verdict: mixes on 118/118 exact rows, yet cycles (`1 → 3 → 8 → 4 → 2 → 1`).

---

## 1. Second, independent kill: the chain also breaks earlier

CARTOGRAPH graded all 8 links of the fully expanded chain:

| link | statement | grade |
|---|---|---|
| L1 | one-step monotonicity `Ecal(m,s+1) ≥ Ecal(m+1,s)` | `[CONJECTURE]` — the open target |
| **L2** | iteration ⇒ fixed-resolution decay `Ecal(m,r) → 0` | **`[FAIL]`** |
| L3 | top-bit `J_r` control ⇒ full mixing | `[KNOWN BARRIER]` (Fourier ≥ 1/2) |
| **L4** | census uniformity ⇒ orbit control | **`[NOT EVEN FORMULATED]`** |
| L5 | typical behaviour ⇒ no divergent orbit | `[KNOWN BARRIER]` (B1) |
| L6 | typical behaviour ⇒ no cycle | `[KNOWN BARRIER]` |
| L7 | finite windows ⇒ one infinite orbit | `[KNOWN BARRIER]` (B2/CP18) |
| L8 | no cycles + no divergence ⇒ Collatz | `[PROOF]` — classical |

**The only proved link is the last one, and it is already in the literature.**

### L2 refuted `[EXACT COMPUTATION]`

The target is monotonicity along the **diagonal** (`m+r` constant). Mixing needs decay at
**fixed resolution** (`r` fixed, `m → ∞`). These are different, and the data kills the second.
Lead-verified, `r = 2`:

    m:  1    2    3    4     5     6    7     8     9     10    11    12
    E:  2    4    4    8    10.33  7.6  8.6   8.38  9.51 10.67 12.34 14.23

Not decaying — oscillating and **growing**. Same at `r = 3`. So even granting L1, no mixing follows.

### What the target would actually buy `[PROOF]`

Granting L1: each diagonal carries a bounded monotone sequence converging to some unidentified
`L ≥ 0`, **with no rate**. No fixed-resolution limit, one-bit projections only, shifting resolution.
**Zero orbit theorems follow.**

### The missing link, stated

CARTOGRAPH named and wrote out the statement the programme has been assuming (the "Transfer
Thesis"): *∃ fixed r, δ(m)→0, c>0 such that (∀ large m: Ecal(m,r) ≤ δ(m)) ⇒ every orbit reaches 1.*

**No statement of this shape exists anywhere in the programme or, to the session's knowledge, in
the literature.** Step 3 was never a conjecture. It was a hope.

---

## 2. The barriers: the lead was half wrong

BARRIER formalised both barriers at three strengths each.

**B1 (measure-zero escape) — PARTIAL.**
* `[PROOF]` B1-weak: density-1 does not imply all.
* `[PROOF]` B1-medium: averaged bounds are stable under density-0 changes, so **averaging alone**
  can never exclude one orbit. **This is correct and is the true core.**
* `[JUDGEMENT]` B1-strong ("no mixing programme can ever reach every-case") — **not a theorem, and
  false as a universal.** Mixing+rigidity patterns yielding every-case results exist.

**B2 (finite-information wall) — PARTIAL.**
* `[PROOF]` B2-weak: `∀m∃n` does not give `∃n∀m`.
* `[PROOF]` B2-medium: compactness gives a **2-adic** realiser, not an integer one. The real wall
  is `Z_2 ⇒ N`.
* `[FAIL]` B2-strong ("no finite-window argument can exclude an infinite object") — **refuted**.
  Induction, descent, bound+check and the cycle equation are all finite-window arguments that work.

**Conway/Kurtz–Simon undecidability — NOT a barrier here.** Those results quantify over
**parametrised families** of generalized Collatz maps, not the fixed `3n+1` map. Family-hardness
does not imply member-hardness. The moral runs the *other* way: a proof must use 3-specific facts,
which is exactly what assets A1/A3/A4 are.

---

## 3. Cycles: more tractable, but the engine is missing

A cycle of length `m`, weight `k` satisfies `[PROOF, from A1]`

    x = B_w / D,    D = 2^m − 3^k,    D | B_w,  and the quotient's word must equal w

The integrality requirement is a genuine **bridge** — the very thing B2 says is missing elsewhere.
Lead-verified as a filter: of **212,629** enumerated words, only **9** pass, all of them the trivial
`x=1` cycle and its repetitions. Elimination rate **99.9958%**.

But `[JUDGEMENT]` the assets do not drive it:
* `[PROOF]` `gcd(D,6) = 1` always. A2 is 2-adic, A3 is 3-adic — the cycle divisor lives on
  **disjoint prime support**. Structural mismatch.
* `[EXACT COMPUTATION]` `D`-divisibility runs at or below chance, and conditioning on the A3
  collision class **never enriches it**.
* `[PROOF]` `3n−1` shares the same `B_w` with cycles at `D < 0`, so any `B_w`-based cycle attack
  must be **sign-sensitive**; any `±D`-symmetric argument is dead on arrival.

The missing engine is lower bounds for `|2^m − 3^k|` — Diophantine approximation, which this
programme does not own. Note also that 1-cycles (Steiner 1977) and 2-cycles (Simons–de Weger 2005)
are **already excluded** in the literature by exactly that machinery.

### A note on a "finding" the lead killed himself

From A1+A4 in three lines: a cycle element can never be divisible by 3. True, verified, and also
**already standard** — it appears in the literature as a routine step. Recorded with zero novelty
value, as a calibration example of what the assets do and do not buy.

---

## 4. What the programme actually owns

SALVAGE assessed all ten assets:

| asset | verdict |
|---|---|
| A1 affine form | **(a) certainly classical** |
| A3 collision criterion `e_w = e_w' ⟺ B_w ≡ B_w' (mod 3^k)` | **(b) plausibly new** |
| A6 cap stabilisation (`2^r ≥ 3^k − 1`) | **(b) plausibly new** |
| A2, A4, A5, A7, A8 | (c) unclear / likely reformulation |
| A9, A10 | original but narrow audience |

**Strongest standalone unit:** A3 + A4 + the counting corollary —

> Same-stratum endpoint collision ⟺ `B`-congruence mod `3^k`; `B` is never `0 mod 3`; therefore
> per stratum, #distinct endpoints = #occupied `B`-classes `≤ 2·3^(k−1)`.

This describes the endpoint-collision structure of parity words **completely**. Verified to `m=16`
with zero failures; occupancy saturates (54/54 at `(12,4)`).

SALVAGE flagged one step of the converse as unverified and load-bearing. **The lead closed it:**
`B ≡ B' (mod 3^k)` forces `3^k | (e − e')`, so the gap is `0` or `≥ 3^k`; but T2 gives
`1 ≤ e ≤ 3^k − 1`, so `|e − e'| ≤ 3^k − 2 < 3^k`. Hence `e = e'`. Verified: 8,534 `B`-congruent
pairs, **all** with endpoint gap exactly zero; T2 clean on 32,766 cases and tight
(e.g. `k=2`: `e=8 = 3^k−1`).

`[JUDGEMENT]` The export market is **arithmetic dynamics, not Collatz**: `B_w` generalises verbatim
to `(px+q)/2`-type maps.

---

## 5. Recommendation

REDIRECT ranked 12 directions by expected value. Grinding the current target ranked **last — below
stopping entirely** (probability 0.05, and its chained value is zero after the chain-kill).

Adopted:

1. **Analogue filter, mandatory.** Every existing and future claim must be tested against `3n−1`
   and `5n+1`. If a claim holds there too, it cannot be about Collatz specifically. This filter
   produced this session's largest result in minutes of compute. **Make it a ship-gate.**
2. **Freeze the mixing target.** Not because it is false — it looks true — but because CP23 proves
   it cannot do the job it was chosen for.
3. **Write up the negative result.** The chain-kill, the 69-entry failure library, the 239-row
   dataset, and the A3/A4 theorem. Negative results *as* the deliverable.
4. **Seek outside eyes.** Zero human review and zero formal verification so far. `ccchallenge.org`
   has 375 catalogued sources, 6 formalisations awaiting audit, and **zero auditors**; this
   programme has an audit methodology and no formalisation. Exact complementary fit.
5. **One timeboxed technical bet:** a sign-sensitive cycle lemma, two weeks, with a pre-registered
   kill condition. It is the only direction that evades both B1 and B2.

---

## 6. Status

| item | status |
|---|---|
| Collatz conjecture | open, untouched |
| Intended chain (mixing ⇒ no counterexample) | **`[FAIL]`** — step 3 refuted by the `3n−1` witness |
| Target `M_merge ≥ L_lift` | `[CONJECTURE]`, 239 rows — **now known not to imply anything about Collatz** |
| A3 + A4 + counting corollary | `[PROOF]`, gap closed, publishable |
| Cycles | more tractable, engine not owned |
| Human / formal verification | **none, ever** — the largest near-term risk |

### Honest translation

`Ecal(4,3) = 40/3` describes the 8 odd starts below 16, run 4 steps. "239 rows, 0 violations" means
this shifting-resolution non-increase held 239 times at small scale. It says **nothing** about any
larger integer, longer orbit, general uniformity, cycles, or divergence — and after CP23, we know
it cannot.

### On the lead's self-assessment

The lead had said "no measurable progress toward Collatz." Two sessions disagreed in opposite
directions: CARTOGRAPH called it **too kind** (links 2–4 are missing before the barriers are even
reached); BARRIER called it **too harsh for cycles, lemma stock, and proved obstructions**.
Both are right about different halves. The accurate statement: *the programme has real assets and
a broken route.*

---

## 7. Files

```
01-cartograph/   chain grading, L2 refutation, Transfer Thesis statement
02-barrier/      B1/B2 formalisation at three strengths, Conway analysis, cycles
03-salvage/      A1-A10 novelty assessment, strongest standalone theorem
04-redirect/     12 ranked directions, the 3n-1 kill, cycle computations
05-session-logs/ the four Muse Code transcripts
```
