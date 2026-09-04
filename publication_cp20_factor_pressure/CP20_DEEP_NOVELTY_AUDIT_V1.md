# CP20 DEEP NOVELTY AUDIT V1

## Factor-complexity / pressure / critical-site density paper

Date: 2026-09-04  
Status: `[PUBLICATION NOVELTY AUDIT — NO NOVELTY CERTIFICATE]`

## Executive verdict

No source located in this audit states the same quantitative theorem chain as the frozen CP20 Task-6/7/8A results.

However, a strong novelty correction is mandatory. The following ingredients are already present in prior Collatz/Syracuse work and must not be presented as new in isolation:

- symbolic or word-complexity analysis of Collatz codings;
- Sturmian/mechanical-word methods;
- repeated-factor arithmetic/divisibility obstructions;
- entropy barriers in Collatz-related languages;
- qualitative exclusion of low-complexity or highly repetitive residual itineraries.

The defensible novelty target is the specific quantitative synthesis:

1. an exponential lower factor-complexity rate `alpha/kappa` for a positive ordinary Syracuse orbit satisfying the global critical-log law;
2. a deterministic weighted-pressure upper rate for zero-critical valuation words;
3. the resulting universal `kappa > 2.784` obstruction without an a priori alphabet bound;
4. the two-type critical-site density pressure surface and certified `rho_min(kappa)` requirements.

Verdict:

`[NO EQUIVALENT THEOREM FOUND — STRONG CLOSE PRIOR ART EXISTS — LIKELY NOVEL SYNTHESIS]`

This is not a formal historical priority certificate.

---

# 1. Highest-risk contemporary source: Witteveen 2026

**Source.** Sven Witteveen, *Entropy barriers for bounded-amplitude Collatz cycles*. Public GitHub preprint repository `kulltc/collatz-entropy-barriers`; initial paper release commit `fc0854799b094fa04250ce8309279609276f3c58`, dated 2026-07-27.

## What it proves

The paper studies positive cycles of the accelerated odd Collatz map through the amplitude

`R(C)=x_max/x_min`.

Its main claims include:

- exclusion of nontrivial primitive positive cycles with `R(C)<=2`;
- a positive-entropy exclusion for sufficiently long cycles at amplitude `R<=12/5`;
- an exact/certified entropy calculation for a bounded-amplitude zero-budget language.

The proof architecture explicitly combines:

- local harmonic localization;
- a mechanical/Sturmian factor language;
- factor-complexity counting;
- repeated-factor divisibility;
- Diophantine approximation / linear forms;
- exact certificate computation.

A representative repeated-factor lemma states that if the same exponent factor of length `s` occurs twice around a primitive cycle, then a `3^s` divisibility condition holds for the corresponding endpoint difference; sufficiently long factors therefore occur at most once relative to the cycle width.

## Overlap with CP20

**Real overlap:** high.

Both programmes use an affine word identity, repeated exponent/valuation factors, word complexity, Sturmian/mechanical structure, and entropy-style counting.

Therefore the CP20 manuscript must NOT say:

- “we introduce factor complexity to the Collatz problem”;
- “we are the first to use Sturmian complexity for Collatz”;
- “we introduce repeated-factor divisibility”;
- “we introduce entropy barriers for Collatz.”

## Why it does not subsume CP20 Task 6/7/8A

The mathematical objects and conclusions differ substantially.

Witteveen works with **hypothetical positive cycles under a bounded-amplitude condition**. CP20 works with a **positive ordinary odd-only Syracuse orbit satisfying the global critical-log discrepancy law**

`s_k=kappa log_2 k+O(1)`.

Witteveen's mechanical-language argument is local to the bounded-amplitude cycle regime. CP20 Task 6 instead derives the asymptotic quantitative lower rate

`liminf log_2 p_a(r)/r >= alpha/kappa`.

CP20 Task 7 then derives a different deterministic pressure upper bound from the critical-log defect band and zero-criticality, and Task 8A resolves critical sites into a two-density pressure surface.

No equivalent of the CP20 `h_B`, `h(rho_1,rho_2)`, `kappa>2.784`, or `rho_min(kappa)` theorem was located in the Witteveen manuscript.

**Classification:** `[STRONG CLOSE PRIOR ART — DISTINCT THEOREM REGIME]`.

---

# 2. Highest-risk structural source: docbgm2002/collatz-things

**Source.** Public GitHub repository `docbgm2002/collatz-things`, especially `docs/repunit/integral_escape_frontier.md` and `CLAIM_LEDGER.md`.

Chronology is material: the foundational integral-escape commit `bb21fd327dd0ef388f2eae9bc15503905d6d263f` is dated 2026-07-13, before CP20 Task 6. A later July 19 commit continues the programme.

## Relevant prior claims

The July integral-escape programme already records qualitative theorems of the following kind:

- a reusable periodic-prefix / inverse-height criterion excluding certain aperiodic residual words;
- exclusion of every Sturmian intercept in a balanced critical-slope `q=3` block language;
- exclusion of bounded-critical-discrepancy words with Diophantine exponent greater than one;
- in particular, discharge of such words when factor complexity is linear;
- later refinements combining repetition surplus with discrepancy budgets and endpoint/inverse-height costs.

The current claim ledger labels these IEF12–IEF21 and related statements as proved within that repository, often using known Bugeaud–Kim repetition theory or Baker-type inputs.

## Overlap with CP20

This is a more serious conceptual overlap than the earlier CP20 novelty audit recognized. It already combines:

- Collatz/Syracuse residual itineraries;
- symbolic repetitions;
- word complexity;
- critical discrepancy;
- Diophantine/repetition exponents;
- arithmetic integrality obstruction.

Therefore CP20 cannot claim that “low word complexity is incompatible with Collatz integrality” as a new general principle.

## Why it does not subsume CP20

The `collatz-things` theorems operate on a special **balanced `q=3`, `{3,4}` block / repunit-tail residual language** and obtain qualitative no-realizer statements from periodic approximation and inverse-height arguments.

CP20 Task 6 is formulated directly for an arbitrary positive ordinary Syracuse valuation word satisfying the global critical-log law and gives a quantitative global entropy lower rate:

`liminf log_2 p_a(r)/r >= alpha/kappa`.

Task 7 places a deterministic pressure upper rate on zero-critical valuation words, and Task 8A quantifies how much critical-site density is necessary when zero-criticality is relaxed.

No theorem matching this `alpha/kappa` lower rate + `h_B` pressure upper rate + critical-density surface was located in `collatz-things`.

**Classification:** `[STRONG CLOSE PRIOR ART — DIFFERENT RESIDUAL LANGUAGE AND CONCLUSION]`.

---

# 3. Dubickas 2009 — complexity of Collatz-related codings

**Source.** Artūras Dubickas, *On integer sequences generated by linear maps*, Glasgow Mathematical Journal 51 (2009), 243–252, DOI `10.1017/S0017089508004655`.

The Collatz-related result gives a linear lower bound for the complexity of a parity-type coding under divergence assumptions.

## Comparison

- Dubickas: parity / linear-map coding; linear factor-complexity lower bound.
- CP20: valuation word; much stronger exponential rate, but under the much stronger global critical-log assumption.

Thus CP20 does not supersede Dubickas in hypothesis scope, and Dubickas does not imply the CP20 rate theorem.

**Classification:** `[KNOWN CLOSE COMPLEXITY PRECEDENT — NOT EQUIVALENT]`.

---

# 4. López–Stoll 2009 — Sturmian conjugacy

**Source.** Josefine López and Peter Stoll, *The 3x+1 Conjugacy Map over a Sturmian Word*, Integers 9 (2009), 141–162, DOI `10.1515/INTEG.2009.014`.

This work studies the 3x+1 conjugacy map when the 2-adic input is Sturmian/mechanical and investigates complexity of the image.

## Comparison

- López–Stoll: Sturmian parity/2-adic conjugacy input.
- CP20: the Beatty/Sturmian phase word `g_k` serves as a background phase against which valuation defects and critical sites are counted.

The use of “Sturmian + Collatz + complexity” is therefore definitely not new. The CP20 novelty, if any, lies in the quantitative critical-log pressure construction.

**Classification:** `[KNOWN STURMIAN PRECEDENT — DIFFERENT OBJECT]`.

---

# 5. Wang 2019 — E-sequence / valuation language

**Source.** SanMin Wang, *An E-sequence approach to the 3x+1 problem*, arXiv:1809.02278; Symmetry 11 (2019), 1415.

Wang works directly with exponent/valuation sequences and proves several divergence criteria involving valuation sums, repeated prefixes, and mechanical sequences.

The earlier CP20 audit already identified Wang's repeated-prefix criterion as a genuine algebraic neighbour of Task 6.

## Comparison

- Wang provides valuation/E-sequence language and repeated-prefix arithmetic.
- CP20 extends the repetition mechanism to arbitrary repeated factors in exponential counting windows and combines it with a polynomial ordinary-state bound to obtain an exponential factor-complexity rate.

No equivalent global rate theorem was located.

**Classification:** `[STRONG ALGEBRAIC PRIOR ART — TASK-6 SYNTHESIS STILL DISTINCT]`.

---

# 6. Lagarias–Weiss and stochastic large-deviation literature

Lagarias–Weiss and related stochastic Collatz models use entropy and large-deviation methods to describe random or branching approximations to Collatz dynamics.

The methodological vocabulary overlaps with Task 7, but the mathematical object differs:

- stochastic probability / branching model in the literature;
- deterministic language counting with a Chernoff generating function and a Sturmian phase in Task 7.

No direct deterministic `h_B` theorem was located.

**Classification:** `[METHODOLOGICAL PRIOR ART — DISTINCT DETERMINISTIC COUNT]`.

---

# 7. Tao / modern Syracuse random-variable line

Tao's Syracuse random-variable framework and later microcanonical work are essential context for the broader project, especially E7R. They are not the closest antecedents of the Task-6/7/8A theorem chain.

They should appear in the introduction only if useful for positioning probabilistic/entropy methods around Syracuse dynamics. The manuscript should not suggest that Task 7 is a corollary of Tao's Fourier-mixing theorem; it is not.

**Classification:** `[BACKGROUND / DIFFERENT OBSERVABLE]`.

---

# 8. Additional 2026 screening

Several recent 2026 Collatz preprints and repositories concerning finite valuation words, terminal congruence obstructions, compression spectra, and generalized threshold phenomena were screened at the title/abstract or source level. None located in this pass states the CP20 quantitative factor-complexity/pressure/density theorem.

Because contemporary Collatz work is rapidly changing and many results first appear in repositories rather than journals, this screening must be repeated immediately before public submission.

---

# 9. Component-by-component novelty adjudication

## Definitely not novel in isolation

- odd-only affine word identity;
- Sturmian/mechanical complexity facts;
- repeated-factor/prefix divisibility as an arithmetic mechanism;
- using word complexity to constrain Collatz-type itineraries;
- entropy or large-deviation language around Collatz;
- qualitative exclusion of low-complexity residual words.

## No equivalent theorem located

- the Task-6 quantitative rate
  `liminf log_2 p_a(r)/r >= alpha/kappa`
  for arbitrary positive ordinary critical-log Syracuse orbits;
- the zero-critical weighted-pressure upper rate `h_B`;
- the uniform no-a-priori-alphabet-bound threshold `kappa>2.784`;
- the Task-8A feasible two-type pressure surface `h(rho_1,rho_2)`;
- the frozen critical-density accumulation theorem;
- certified `rho_min(kappa)` constraints.

## Current novelty label

`[LIKELY NOVEL AS A QUANTITATIVE SYNTHESIS — SPECIALIST PRIORITY CHECK REQUIRED]`.

---

# 10. Allowed and forbidden manuscript language

## Allowed

- “We prove…” followed by the exact theorem.
- “We obtain a quantitative entropy-pressure obstruction…”
- “Our result differs from earlier symbolic approaches by treating the global critical-log valuation regime and producing an explicit exponential complexity rate and critical-density pressure surface.”
- “We are not aware of an equivalent theorem under these hypotheses.”

## Forbidden without a stronger historical audit

- “the first application of factor complexity to Collatz”;
- “the first entropy barrier for Collatz”;
- “the first Sturmian approach to Collatz”;
- “we introduce repeated-factor divisibility”;
- “the first proof that low-complexity Collatz words are impossible.”

---

# 11. Publication recommendation

Proceed with the paper. The fresh sources narrow the novelty claim but do not erase the frozen theorem chain.

The paper should be sold on **quantitative theorem shape**, not on ownership of the underlying ingredients:

`exponential lower complexity rate + deterministic pressure upper rate + critical-density phase surface`.

Before submission, perform one specialist human literature pass focused on:

1. post-2009 combinatorics-on-words treatments of Collatz/Syracuse;
2. 2025–2026 repository/preprint work on valuation languages;
3. factor complexity under Diophantine or discrepancy constraints outside Collatz, where an abstract theorem could subsume Task 6 or Task 7 under another terminology.
