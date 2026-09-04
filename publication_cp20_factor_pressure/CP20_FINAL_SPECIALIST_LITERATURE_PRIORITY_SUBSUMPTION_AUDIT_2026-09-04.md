# CP20 — FINAL SPECIALIST LITERATURE / PRIORITY / SUBSUMPTION AUDIT

**Date:** 2026-09-04
**Role:** adversarial pre-publication novelty auditor. Burden taken as: *try to destroy the novelty claim.*
**Standard applied:** absence of a found paper is not proof of novelty. Where evidence is incomplete, `[UNRESOLVED]` is recorded.

---

# A. TARGET INTEGRITY

| Item | Result |
|---|---|
| Freeze commit `588e282813d5bf97a1fd2f2268e3fa13cd87ddd2` | **VERIFIED** — exists; 2026-09-04 17:36:06 +0300, *"Freeze CP20 manuscript after zero-trust editorial repairs"* |
| `CP20_MANUSCRIPT.tex` blob | `7421c8ac2051800981be548057bc97005c32c05e` (936 lines) |
| `CP20_REFERENCES.bib` blob | `480c10df7ef19da5d19bc6ca507ec1824390dc9c` (118 lines, 11 entries) |
| Final PDF SHA-256 `115edb78…` | **`[UNRESOLVED]` — cannot verify.** `CP20_MANUSCRIPT_FINAL_FREEZE_CANDIDATE_2026-09-04.pdf` is not tracked anywhere in the repository (only unrelated `research_manager/.../si_*/main.pdf` and `tao/tao_1909.03562v7.pdf` exist). The prompt conditions this check on local availability; the file is not locally available |
| Manuscript treated as immutable | Yes — read-only; nothing rewritten |

**Prior repairs confirmed present at the freeze commit** (spot-checked, not reopened):
`Moothathu2012` added to the bibliography and cited at L429 as the originator of prefix-based non-repetitive
subword complexity, with Nicholson–Rampersad correctly demoted to *"later studied"*; the shifted-window
distinction retained and sharpened (*"we use this literature only for terminology and priority"*).

---

# B. EXECUTIVE VERDICT

## `[PUBLICATION NOVELTY PLAUSIBLE — SPECIALIST CONFIRMATION STILL NEEDED]`

No prior theorem located subsumes, anticipates, or trivialises any of the four principal results. **No blocking
defect (§J: NONE).**

The verdict is deliberately not `[PUBLICATION NOVELTY CLEAR…]`. Three of the four result clusters are built on
machinery that is genuinely standard — Chernoff/method-of-types counting, Legendre/variational pressure,
frequency-constrained entropy. The line between *"standard machinery correctly applied to a new object"* and
*"routine corollary of a published general theorem"* is precisely the judgment a human specialist in
combinatorics on words / thermodynamic formalism must make. My analysis places all four clusters on the
correct side of that line, and I give the reasoning in §D, but a keyword-and-citation search by a
non-specialist is not a substitute for that confirmation. The manuscript itself flags this exact residual risk
at L132, and that self-assessment is accurate and should be retained.

Two citation repairs are required (§K), neither affecting novelty.

---

# C. PRINCIPAL THEOREM NOVELTY TABLE

| # | Result | Closest prior work | Classification | Confidence | Action |
|---|---|---|---|---|---|
| 1 | **Thm A** — shifted-window exponential factor complexity, `liminf log₂p_a(r)/r ≥ α/κ` | Moothathu 2012; Nicholson–Rampersad 2016 (invariants); Dubickas 2009 (Collatz coding, linear-type, and its 3x+1 statement is *speculative*); Witteveen 2026 (same affine subtraction, 3-adic reading) | **`[TECHNIQUE OVERLAP]`** — device and terminology prior; theorem not located | Medium-high | None. Attribution already correct |
| 2 | **Thm B** — finite-`B` pressure `limsup ≤ h_B`, hence `κ ≥ α/h_B` | Cramér / method of types (Dembo–Zeitouni; Cover–Thomas) for the counting step | **`[TECHNIQUE OVERLAP]`**; the counting lemma alone is a **`[ROUTINE COROLLARY]`** of Cramér | High | **Cite the standard source** (§K.1) |
| 3 | **Thm C** — uniform envelope, `κ ≥ α/h_∞ > 2.784`, no a priori alphabet bound | Sarig 1999 (countable Markov shifts, Gurevich pressure) | **`[BACKGROUND ONLY]`** | High | Optional citation |
| 4 | **Thm D** — two-type critical-site pressure surface; accumulation densities satisfy `h(ρ) ≥ α/κ` | Pesin–Weiss 2001; Takens–Verbitskiy 2003; Barreira–Saussol 2001 (conditional variational principles) | **`[TECHNIQUE OVERLAP]`** — the *form* of `h(ρ₁,ρ₂)` is a standard frequency-constrained entropy; the *theorem* is not | Medium-high | **Add one conditional-VP citation** (§K.2) |
| 5 | Zero-critical-**density** ⟹ `κ > 2.784` | None located in Collatz literature | **`[NO OVERLAP]`** | Medium | None |
| 6 | Unrestricted endpoint `max h = α log₂α − (α−1)log₂(α−1)` | Classical composition/parity-vector count | **`[BACKGROUND ONLY]`** — see §C.1 | High | None — correctly framed |

## C.1 Cluster 6 is a classical quantity, and the manuscript already treats it as one

I verified the identity independently:

`α·H(1/α) = α log₂α − (α−1)log₂(α−1)`, where `H` is binary entropy.

This is exactly the exponential growth rate of `C(⌊αk⌋−1, k−1)` — the number of ways to write the total
exponent `⌊αk⌋` as an ordered sum of `k` positive integers, i.e. the count of length-`k` Collatz exponent
sequences with the critical total exponent. That binomial count is standard background in the 3x+1 cycle
literature.

**This is not a defect.** The manuscript presents `eq:cp19` purely as a consistency check — *"the optimized
phase contribution is recovered exactly; there is no additional strict 'Sturmian phase cost'"* — and makes no
novelty claim for it. Correctly classified as `[BACKGROUND ONLY]`.

---

# D. GENERAL-THEOREM SUBSUMPTION SEARCH

Candidate-theorem tests, per the required 10-point schema (condensed to the load-bearing fields).

## D.1 Takens–Verbitskiy — conditional variational principle

1. **Citation:** F. Takens, E. Verbitskiy, *On the variational principle for the topological entropy of certain non-compact sets*, **Ergodic Theory and Dynamical Systems 23** (2003) 317–348. **DOI `10.1017/s0143385702000913`** (verified, Crossref).
2. **Year:** 2003.
3. **Hypotheses:** continuous map on a compact metric space with the specification property; continuous observable `φ`.
4. **Conclusion:** `h_top({x : lim (1/n)Σφ(T^i x) = a}) = sup{h_μ(T) : ∫φ dμ = a}` — the entropy of a Birkhoff level set equals a constrained measure-theoretic supremum.
5. **Manuscript result affected:** Thm D (Cluster 4).
6. **Mapping:** the valuation shift with the Sturmian phase as a skew-product base; `φ` = indicator of critical sites; `a = ρ`. Under that map, `h(ρ₁,ρ₂)` is recognisable as a frequency-constrained entropy of exactly the type the theorem computes.
7. **Mapping quality:** **routine for the *quantity* `h(ρ)`; impossible for the *theorem*.**
8. **What remains necessary:** everything that makes Thm D a theorem. A conditional variational principle says *how large a level set is*. It says nothing about which level set a **particular deterministic arithmetic orbit** lands in. Thm D's content is that the empirical critical-site densities of a real Syracuse orbit must accumulate in `{h ≥ α/κ}`, and that comes from combining the counting upper bound with **Thm A's arithmetic lower bound** on realised factor complexity. No variational principle supplies Thm A.
9. **Classification:** **`[TECHNIQUE OVERLAP]`** — genuine background for the pressure surface's form; not subsuming.

## D.2 Barreira–Saussol — variational principles and mixed multifractal spectra

1. **Citation:** L. Barreira, B. Saussol, *Variational principles and mixed multifractal spectra*, **Transactions of the AMS 353** (2001) 3919–3944. **DOI `10.1090/s0002-9947-01-02844-6`** (verified, Crossref).
2. Same structural verdict as D.1: computes spectra of level sets; supplies no statement about a fixed arithmetic sequence.
3. **Classification:** **`[BACKGROUND ONLY]`**.

## D.3 Sarig — thermodynamic formalism for countable Markov shifts

1. **Citation:** O. M. Sarig, *Thermodynamic formalism for countable Markov shifts*, **Ergodic Theory and Dynamical Systems 19** (1999) 1565–1593. **DOI `10.1017/s0143385799146820`** (verified, Crossref).
2. **Relevance:** Cluster 3 — `h_∞` with `S_{1,∞}=1/(e^λ−1)`, `S_{2,∞}=e^λ+1/(e^λ−1)` has the shape of a countable-state (Gurevich) pressure.
3. **Why it does not subsume:** the manuscript is careful in exactly the way that defuses this risk. It never claims `h_∞` *is* the entropy of a countable-alphabet shift, and never invokes a variational principle for it. It calls `h_∞` a **formal envelope** and uses only (i) monotonicity `h_B ≤ h_{B+1} ≤ h_∞` and (ii) a certified rational bound. The logical step — critical-log ⟹ `d_k` bounded ⟹ `g_k∈{1,2}` ⟹ `a_k` bounded ⟹ *some* finite `B` is valid for the trajectory ⟹ `κ ≥ α/h_B ≥ α/h_∞` — is elementary and Syracuse-specific.
4. **Classification:** **`[BACKGROUND ONLY]`**. The manuscript is **not** rediscovering a countable-alphabet variational principle; it deliberately avoids needing one.

## D.4 Cramér / method of types — the counting lemma

1. **Citations:** A. Dembo, O. Zeitouni, *Large Deviations Techniques and Applications*, 2nd ed., Springer 1998 (Cramér's theorem, Thm 2.2.3); T. M. Cover, J. A. Thomas, *Elements of Information Theory*, 2nd ed., Wiley 2006 (method of types, Ch. 11).
2. **Conclusion:** the exponential growth rate of the number of words with a prescribed additive statistic is the Legendre transform of the log-moment generating function.
3. **Manuscript result affected:** `eq:chernoff` and the derivation of `h_B` (Thm B).
4. **Mapping:** **exact.** Two site types with Sturmian densities `M₁=2−α`, `M₂=α−1`; per-type defect supports `D₁={−1,…,−(B−1)}`, `D₂={+1,−1,…,−(B−2)}`; constraint `ΣD = S = O(log r)`. The bound `N(S) ≤ P₁^{n₁}P₂^{n₂}e^{−λS}` and `h_B = inf_λ[M₁log₂P₁ + M₂log₂P₂]` are precisely the two-type Chernoff/method-of-types computation.
5. **What remains necessary:** the Syracuse-specific inputs — that the phase word is Sturmian with those exact densities, that zero-criticality produces those exact supports, that the critical-log law confines `S` to an `O(log r)` band (hence only polynomial overhead), and above all Thm A, without which `h_B` bounds nothing about `κ`.
6. **Classification:** the **counting lemma in isolation is `[ROUTINE COROLLARY]`**; **Thm B is `[TECHNIQUE OVERLAP]`, not subsumed.**
7. **Consequence:** because the counting step *is* routine, it must be cited as such. See §K.1 — this is the one place where the manuscript's otherwise-scrupulous "no novelty for ingredients" posture is not backed by a concrete reference.

## D.5 Combinatorics-on-words route to Thm A

Searched for a packaged general theorem of the form *"polynomial state growth + exponential separation of
repeated factors ⟹ exponential factor complexity"* across subword complexity, non-repetitive complexity,
recurrence/repetition functions, return words, Morse–Hedlund generalisations, and complexity of codings of
dynamical systems. **No such general theorem located.**

The classical results run the other way or are far weaker: Morse–Hedlund gives only `p(n) ≥ n+1` for aperiodic
words; Dubickas's proven complexity bounds are linear-type and for a different (parity / `⌊px/q⌋`) coding, with
his 3x+1 statement explicitly speculative. The manuscript's argument is elementary but depends on the exact
Syracuse affine identity, `2`–`3` coprimality, and `n_k=O(k^κ)` — inputs no general word-combinatorial theorem
supplies. **`[NO OVERLAP]`**; `[UNRESOLVED]` only in the weak sense that a negative search result is not a proof.

---

# E. COLLATZ-SPECIFIC PRIOR ART SEARCH

Sources examined or re-examined: Lagarias (1985 survey; 2021 overview), Lagarias–Weiss 1992, Terras/Everett
stopping-time line, Applegate–Lagarias, Simons–de Weger `m`-cycle programme, Eliahou, Wirsching, Tao
(2019/2020 Syracuse random variables and equidistribution), Wang 2019, Dubickas 2009, López–Stoll 2009,
Witteveen 2026, `docbgm2002/collatz-things` (July 2026), plus 2025–2026 arXiv sweeps on Collatz entropy,
complexity, valuation, parity-vector and transfer-operator formulations.

| Finding | Effect |
|---|---|
| No prior Collatz/Syracuse statement of the form *zero critical density ⟹ `κ > 2.784`* located | Cluster 5 `[NO OVERLAP]` |
| No prior Collatz theorem giving an exponential factor-complexity **rate** for the valuation word | Cluster 1 not anticipated |
| No prior Collatz two-type critical-site density pressure surface located | Cluster 4 not anticipated |
| The `α log₂α − (α−1)log₂(α−1)` composition count is classical background | Cluster 6 `[BACKGROUND ONLY]`, correctly framed |
| Witteveen 2026 and `collatz-things` 2026 remain the two closest sources | Chronology re-confirmed in the previous audit (single commit 2026-07-27; and `bb21fd3` 2026-07-13 with repo HEAD 2026-08-03 — both wholly prior to the 2026-08-26 freeze, with no possibility of later-edit contamination). Both already disclosed at theorem-comparison depth, including the dual-divisibility reading and the shared threshold architecture |
| Recent transfer-operator / spectral-gap Syracuse work (a 2026 source already mirrored in this repository under the E7R branch) | Different observable (Fourier/equidistribution); E7R is explicitly excluded from this manuscript. `[NO OVERLAP]` |
| arXiv 2603.11066 (*Exploring Collatz Dynamics with Human–LLM Collaboration*, 2026) touches adjacent objects — a θ-variable growing only on blocks of average valuation `< log₂3`, and a "deterministic discrepancy" statement | Thematically adjacent, different results. `[NO OVERLAP]`; optional to mention. Not load-bearing |

---

# F. COMBINATORICS-ON-WORDS SEARCH

- **Moothathu 2012** (*Eulerian entropy and non-repetitive subword complexity*, Theoret. Comput. Sci. **420**, 80–88, DOI `10.1016/j.tcs.2011.11.013`) — originator of the invariant. **Now correctly credited at L429.** `[BACKGROUND ONLY]`.
- **Nicholson–Rampersad 2016** (Discrete Appl. Math. **208**, 114–122, DOI `10.1016/j.dam.2016.03.010`) — prefix-based *initial* non-repetitive complexity; computes it for Thue–Morse, Fibonacci, Tribonacci. The manuscript's window `[N_r, 2N_r−r]` is **not** a prefix, and the manuscript says so explicitly and declines to identify the two invariants. `[BACKGROUND ONLY]`.
- **Morse–Hedlund 1940** — Sturmian `p(r)=r+1` and the two-Parikh-vector fact, used as background with no novelty claim. `[BACKGROUND ONLY]`.
- No generalisation of these invariants to arbitrary shifted windows that would yield the `α/κ` rate was located.

---

# G. THERMODYNAMIC-FORMALISM / LARGE-DEVIATION SEARCH

Covered in §D.1–D.4. Summary: **the machinery is standard and the manuscript says so** (L120 "No novelty is
claimed for the individual ingredients"; L616 conceding Legendre/variational pressure as standard). What the
literature does not supply, in any formulation located, is a bridge from a constrained-language entropy to a
constraint on a **fixed arithmetic orbit**. That bridge is Thm A, and it is the load-bearing novelty of the
paper. Every subsumption attempt in §D fails at the same point.

---

# H. PRIORITY AND ATTRIBUTION FINDINGS

Every sentence containing *introduce / first / new / novel / previously / known / classical / standard / due to
/ follows from / inspired by* was swept.

| Location | Assessment |
|---|---|
| L120 "No novelty is claimed for the individual ingredients…" | Accurate and appropriately broad |
| L126 "repeated-factor divisibility itself is not a new device"; threshold architecture "already occurs there" | Both concessions accurate; the dual `3`-adic / `2`-adic reading is stated correctly |
| L132 residual abstract-subsumption risk self-flagged | **Accurate. Retain verbatim** — this audit confirms it as the correct open risk |
| L429 Moothathu / Nicholson–Rampersad | **Corrected and now accurate** |
| L616 Pesin–Weiss framing ("standard… does not form part of the novelty claim") | Accurate; correctly background-only |
| L116 "and introduce a two-dimensional pressure surface" | Mild implicit priority claim, but for the **Syracuse-specific two-type surface**, which no located source contains. Defensible as written |
| L104, L146, L503, L707 "first" | Ordinal usage only ("the first mechanism", "our first principal theorem"). No priority content |
| L926, L929 table rows | "factor complexity in a Collatz setting is not claimed as new"; "Sturmian Collatz methods are not claimed as new". Accurate |
| **The Chernoff / method-of-types step (L477–488)** | **Missing citation** — see §K.1. This is the only implicit priority exposure remaining: a routine standard computation presented with no attribution |

Classification of the one finding: **missing citation (type 2)**, *not* wrong attribution, *not* insufficient
prior-art discussion, *not* theorem subsumption.

---

# I. PESIN–WEISS BIBLIOGRAPHIC CHECK

**VERIFIED ACCURATE.** Crossref returns:

> Yakov Pesin; Howard Weiss, *The multifractal analysis of Birkhoff averages and large deviations*,
> in **Global Analysis of Dynamical Systems**, **2001**, pp. **419–431**.
> DOI `10.1887/0750308036/b1058c18` (IOP original) — also reissued as `10.1201/9781420034288-18`.

Authors, title, book, year and page range all match the manuscript's `.bib` entry exactly. The
`publisher = {Institute of Physics Publishing}, address = {Bristol}` fields are consistent with the IOP DOI
prefix. The previous audit's `[UNVERIFIED]` flag is now **discharged**. Optional: add the DOI.

---

# J. BLOCKING DEFECTS

## NONE

No stop-rule condition (1–6) is met:

1. No prior theorem fully subsumes a principal theorem.
2. No principal theorem is a routine corollary presented as new — the one genuinely routine component (the counting lemma) is a *step*, not a presented theorem, and the manuscript already disclaims ingredient novelty.
3. No major priority attribution is wrong (the Moothathu defect from the previous audit is repaired).
4. No missing citation changes the novelty assessment — §K.1 and §K.2 add rigour and attribution, not new prior art.
5. No general theorem falsifies a central novelty claim.
6. No hidden hypothesis gap exposed by literature comparison.

---

# K. NONBLOCKING CITATION / WORDING REPAIRS

**K.1 (recommended, attribution-strengthening).** Cite the standard source for the counting step at
`eq:chernoff` (L477–488). The bibliography currently contains **no** large-deviations or information-theory
reference — the sole grep match is the phrase "Large Deviations" inside the Pesin–Weiss *title*. Suggested
sentence after `eq:chernoff`:

> This is the standard Chernoff / method-of-types bound for the number of words with a prescribed additive
> statistic; see e.g. Dembo–Zeitouni or Cover–Thomas. We claim no novelty for this step.

Add to the `.bib`:

```bibtex
@book{DemboZeitouni1998,
  author    = {Amir Dembo and Ofer Zeitouni},
  title     = {Large Deviations Techniques and Applications},
  edition   = {2nd},
  publisher = {Springer},
  series    = {Stochastic Modelling and Applied Probability},
  volume    = {38},
  year      = {1998}
}
```

**K.2 (recommended).** At the Legendre representation (L608–616), add one conditional-variational-principle
reference alongside Pesin–Weiss, so the "standard machinery" concession names the closest general results:

```bibtex
@article{TakensVerbitskiy2003,
  author  = {Floris Takens and Evgeny Verbitskiy},
  title   = {On the Variational Principle for the Topological Entropy of Certain Non-Compact Sets},
  journal = {Ergodic Theory and Dynamical Systems},
  volume  = {23}, pages = {317--348}, year = {2003},
  doi     = {10.1017/S0143385702000913}
}
```

**K.3 (optional).** At the `B=∞` envelope (§7), one sentence noting that partition functions of this shape are
studied as Gurevich pressure for countable Markov shifts (Sarig, ETDS **19** (1999) 1565–1593,
DOI `10.1017/S0143385799146820`), while stating that the manuscript uses `h_∞` only as a monotone envelope and
invokes no variational principle. This pre-empts the most likely specialist objection to Cluster 3.

**K.4 (optional).** Add the Pesin–Weiss DOI.

**K.5 (housekeeping).** The freeze PDF is not tracked in the repository, so its stated SHA-256 cannot be
verified by any downstream auditor. Either commit the PDF or record the hash against a retrievable artifact.

---

# L. FINAL FREEZE DECISION

## `[FINAL FREEZE APPROVED AFTER CITATION REPAIRS]`

The frozen mathematics is unaffected. Repairs K.1 and K.2 are additive citations plus one disclaiming
sentence each; K.3–K.5 are optional.

**Freeze is not submission-readiness.** The specialist confirmation named in §B remains an open pre-submission
gate, exactly as the manuscript's own L132 states.

---

# M. EXACT NEXT ACTION

**Apply citation repairs K.1 and K.2, recompile, then obtain a human specialist review — from a
combinatorics-on-words or thermodynamic-formalism referee — of the single question in §D: whether Theorems B
and D are more than a standard constrained-entropy computation bridged to arithmetic by Theorem A.**

That is the only remaining novelty question this audit could not close, and it is not closable by literature
search alone.

---

**Nothing in this report claims that the Collatz conjecture has been proved.**