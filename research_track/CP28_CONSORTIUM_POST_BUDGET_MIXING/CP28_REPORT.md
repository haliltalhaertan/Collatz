# CP28 — Consortium Free Brainstorm → Post-Budget Mixing (PBM)

Status: **CLOSED**. Collatz remains **OPEN**. Nothing here is a proof of Collatz.

## 1. Process (new CP28 order)
- **T0 free round:** ChatGPT Web, Muse 1.3 and Unreal Agent each proposed four theories A–D with no gates. Earlier routes were banned. That gave 12 theories.
- **T1 anonymous ranking:** Theories were shuffled as T1–T12 and scored on M/Y/U/K. Borda top 5: T10 (31), T3 (30), T7 (26), T9 (25), T12 (22).
- **Sequential deep review:** Hermes pre-computed each core quantity locally. Members voted blind. Muse dropped out of the later rounds (subscription quota exhausted). At the user's instruction, Unreal Agent in a fresh session served as the second independent auditor.

## 2. Verdicts on ranked theories
| # | Theory | Verdict | Reason |
|---|---|---|---|
| T10 | Brownian invariance of log-orbit | PARK | For j≤m it is Terras + Donsker (known). For j>m full parity TV ≥ 1−2^{m−j}. Exact m=16..24: deviation starts at j/m≈1,05–1,13, noise level. |
| T3 | Hazard law | PARK/KILL | No signal beyond ~1σ. Removing the +1 term leaves the stopping distribution unchanged. |
| T7 | Entropy debt | KILL | Reduces to Terras bijection + Cramér, I*=0,05498. Logic error: +1 growth ≠ low valuation. |
| T9 | 3-adic branching pressure | KILL | Exact: the mod-3^h inverse-tree growth rate equals the independent model (e.g. 255/256, h=1..5). Column sums are constant, so there is no h-dependence. Audited by ChatGPT and UA. |
| T12 | Head/tail bit locking | KILL | Pre-registered MI test: signal ≤ noise, p=0,09–1,0, shrinking with m. |

## 3. The wall (consortium consensus)
The Terras bijection gives exact randomness for the first ≈m parity steps ("free part"). Every statistic inside that range reduces to a textbook result. Beyond it, the steps are set by carries, and pointwise independence is as hard as Collatz. Both ChatGPT and Unreal named the same **missing lemma**: *post-budget pattern frequencies*.

## 4. Result: PBM theorem (audited proof sketch)
Definitions:
- T(n)=n/2 or (3n+1)/2; U(x)=(3x+1)/2^{a(x)}; β=log₂√3.
- X_m is a uniform odd number in [2^m,2^{m+1}).
- S_j=Σ_{i<j}a_i and τ=min{j: S_j>m}.
- N_k=#{τ≤i<τ+⌊δm⌋ : a_i=k}.

**Theorem (PBM).** For every fixed k≥1:
- **(a)** for 0<δ<β/2≈0,396, N_k/⌊δm⌋ → 2^{−k} in probability;
- **(b)** the same holds for every 0<δ<1.

**Proof route:** Inselmann, arXiv:2402.03276v3.
- Tools used: Def 2.6, Lemma 2.7, Lemma 2.8, Prop 2.4, **Lemma 2.16** (S *-dense ⇒ {n: T^{⌊log₂n⌋}(n)∈S} *-dense) and **Theorem 3.1** with λ=β.
- Method: a pattern set P (Hoeffding over residue classes mod |w|, prefix union, no linear zero-runs) is shown to be *-dense. It is then pulled back by F=T^{⌊log₂·⌋}.
- Part (b) needs **four** post-budget blocks: F^{-1}(P∩F^{-1}P∩F^{-2}P∩F^{-3}P). Capacity (β+β²+β³+β⁴)/2 = 1,1563 > 1.
- Three blocks are not enough: capacity 0,9591 < 1. This error was caught by UA in audit 1 and fixed.
- Full text: `evidence/pbm_writeup_chatgpt.txt`.

**Audit trail:**
1. Skeleton (ChatGPT). Adversarial audit by ChatGPT and UA: 7 gaps and 1 indexing error found.
2. Full write-up (ChatGPT) closing G1–G7.
3. **UA line audit:** C1–C6 all correct → (a) PROOF, (b) PROOF.
4. **UA fresh-session red team:** read the source HTML itself, attacked 3 weakest steps, ran a numerical check → **MINOR REVISION, no fatal error.** The requested clarity fixes are:
   - Lemma C ratios should read log F^{j+1}/log F^j → β and log F^j/log x → β^j. The write-up display shows the inverse ratio; this is a typo.
   - State the quantifier order (fix η, m→∞, then η↓0).
   - Say explicitly what happens when the cutoff falls in a gap.
5. Hermes verified the Lemma 2.16 and Theorem 3.1 statements against the PDF.

**Label:** PROOF-with-minor-revisions (independent audits: UA×2, ChatGPT author). Muse audit is pending; its quota was exhausted.

**Novelty (honest):** PBM is a corollary of Inselmann's tools. The new element is that the post-budget valuation-pattern frequency statement is stated explicitly and proved. No literature source for it was found, and none was ruled out.

## 5. Finite exact evidence (not proof)
`cp28_pbm_check.py`, δ=0,25, all odd x in the shell:

| m | N | L | freq a=1 | a=2 | a=3 | TV(block sum vs iid Geom) |
|---|---|---|---|---|---|---|
| 14 | 8192 | 3 | 0,4920 | 0,2537 | 0,1278 | 0,0145 |
| 16 | 32768 | 4 | 0,4928 | 0,2549 | 0,1269 | 0,0169 |
| 18 | 131072 | 4 | 0,4963 | 0,2524 | 0,1258 | 0,0081 |
| 20 | 524288 | 5 | 0,4972 | 0,2518 | 0,1251 | 0,0048 |
| 22 | 2097152 | 5 | 0,4988 | 0,2509 | 0,1251 | 0,0023 |

- UA's independent code gives the same a=1 frequency at m=16 (0,492775).
- **Residual dependence:** the correlation between height at τ and the post-budget block is real (2–8σ). Its raw size decays like ~2^{−0,24m}…2^{−0,35m}. ChatGPT and UA independently predicted 2^{−0,2925m}. The prediction is heuristic.
- **Pattern windows beyond 2m:** [2m,3m] converges slowly; [3m,4m] still deviates strongly at m≤22. This is consistent with PBM (b)'s window ≤(1+2δ)m<3m. It is also a warning against extending PBM further without new input.

## 6. Status and next
- PBM is a small but real intermediate result that goes past the Terras wall. It does not advance Collatz itself: it is an almost-all statement and does not handle individual orbits.
- Next:
  - Muse line audit when its quota returns.
  - Apply the red-team fixes to the write-up.
  - Consortium question: can PBM be iterated to growing δ (log m blocks) with *-density exponent control? That is the natural limit of this bridge.
- Remaining theories T2, T4–T6, T8, T11: record-orbits GO/PARK, universality PARK/PARK; others not reviewed.
