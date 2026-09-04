# CP20 PUBLICATION BRANCH — STATUS

## Factor Complexity, Pressure, and Critical-Site Density

Date: 2026-09-04  
Branch: `cp20-publication-factor-pressure-v1-20260904`  
Base commit: `0c0e0e55c490278396f0b8f5033000b80725fb6c`  
Status: `[POST-AUDIT EDITORIAL REPAIRED — MANUSCRIPT DRAFT AUTHORIZED]`

This branch is editorial/publication work only. It does not alter the canonical research state and does not introduce new mathematics.

## 1. Frozen mathematical dependency spine

Only the following audited/frozen CP20 results are admitted as theorem dependencies:

1. `CP20_TASK6_MAJOR_THEOREM_V3_AUDITED_FROZEN`
   - repeated-factor spacing;
   - polynomial ordinary-state bound under the global critical-log law;
   - exponential factor-complexity lower bound
     `liminf log_2 p_a(r)/r >= alpha/kappa`.

2. `CP20_TASK6_STRENGTHENED_COROLLARY_V3_AUDITED_FROZEN`
   - deterministic weighted-pressure upper bound for zero-critical words under a finite valuation bound `1<=a_k<=B`;
   - finite-alphabet threshold `kappa >= alpha/h_B`;
   - uniform no-a-priori-alphabet-bound envelope.

3. `CP20_TASK7_PRESSURE_GENERALIZATION_THEOREM_V3_AUDITED_FROZEN`
   - canonical formulation of the zero-critical pressure theorem;
   - certified consequence `alpha/h_infinity > 348/125 = 2.784`.

4. `CP20_TASK8A_CRITICAL_SITE_DENSITY_PRESSURE_THEOREM_V3` together with
   `CP20_TASK8A_FINAL_FREEZE_DECISION_2026-08-26`
   - audited feasible pressure region;
   - two-regime uniformity repair;
   - critical-site density accumulation theorem;
   - certified `rho_min(kappa)` values.

## 2. Explicitly excluded from this paper

The following are not admitted as theorem dependencies here:

- `CP20_TASK8A_FULL_SCALE_ACCUMULATION_LEMMA.md` — still an audit-extension candidate rather than part of the frozen spine;
- the E7/E7R/B4 microcanonical Fourier programme — scientifically separate and still active;
- the continued-fraction repeat-pattern observation whose load-bearing long-repeat lemma remains unproved;
- CP19 Task-5 exclusion claims — the recorded status is hypothesis mismatch, not exclusion;
- any claim that the Collatz conjecture, divergent-orbit problem, or nontrivial-cycle problem has been solved.

## 3. Publication thesis

The proposed paper should center the following quantitative chain:

`critical-log law`

`=> exponential lower factor-complexity rate`

`+ deterministic pressure upper rate`

`=> kappa threshold`

`=> critical-site density pressure surface`.

The canonical headline consequences are:

- `liminf_{r->infinity} log_2 p_a(r)/r >= alpha/kappa`;
- for finite `B>=3`, under `1<=a_k<=B` and pointwise zero-criticality, `limsup log_2 p_a(r)/r <= h_B` and hence `kappa>=alpha/h_B`;
- without specifying a finite alphabet bound in advance,
  `kappa >= alpha/h_infinity > 2.784`;
- if the total critical-site count is `o(N)`, pointwise zero-criticality is not needed for the same `>2.784` consequence;
- the frozen Task-8A density surface gives certified lower requirements on critical-site density, including
  `rho_min(1.06) ≈ 0.3462262371`,
  `rho_min(1.5) ≈ 0.0916083302`, and
  `rho_min(2.0) ≈ 0.0314445509`.

## 4. Independent publication audit

The 2026-09-04 independent zero-trust publication audit returned:

`[PASS WITH EDITORIAL REPAIRS]`.

The audit found no prior source subsuming a principal theorem, no proof-critical constant or inequality mistranscription, no hidden dependency on an unfrozen result, and no chronology failure. It did identify one blocking extraction defect: the finite-alphabet hypothesis `1<=a_k<=B` had been omitted from the working T5 statement, propagating to the `B=3` T6 wording. It also requested restoration of the exact Task-6 epsilon range and a stronger related-work comparison with Witteveen 2026.

Those repairs are editorial restorations from frozen sources and do not change the mathematics.

## 5. Novelty gate

Status:

`[NO EQUIVALENT THEOREM FOUND — STRONG CLOSE PRIOR ART EXISTS — SPECIALIST CHECK PENDING]`

A fresh comparison identified two particularly important pre-existing 2026 sources that must be discussed explicitly:

- Sven Witteveen, *Entropy barriers for bounded-amplitude Collatz cycles*, GitHub preprint released 2026-07-27. It already uses exponent-factor complexity, a mechanical/Sturmian language, repeated-factor divisibility, and an entropy barrier in the bounded-amplitude cycle setting.
- `docbgm2002/collatz-things`, whose July 2026 integral-escape programme contains IEF12–IEF21, including qualitative exclusions based on Sturmian repetition, bounded critical discrepancy, Diophantine exponent, and low-complexity residual block words.

These sources prevent any claim that factor complexity, Sturmian methods, repeated-factor divisibility, or entropy barriers are being introduced to Collatz for the first time.

The Witteveen comparison must be made at architecture level as well as ingredient level: its repeated-factor `3^r` endpoint divisibility and the CP20 `2^{A(W)}` start-value divisibility are dual coprime consequences of the same affine subtraction, and the broad strategy of comparing an entropy rate against a Diophantine/discrepancy parameter to obtain a threshold predates CP20. The claimed contribution is therefore the different hypothesis class and the quantitative outputs, not ownership of that architecture.

The presently defensible novelty target is narrower:

> a quantitative entropy-pressure obstruction for arbitrary positive ordinary Syracuse orbits satisfying the global critical-log discrepancy law, with an exponential factor-complexity lower rate, a deterministic weighted-pressure upper rate, a universal `kappa > 2.784` threshold under zero/sparse critical density, and a two-type critical-site density pressure surface.

Current label:

`[LIKELY NOVEL AS A QUANTITATIVE SYNTHESIS — SPECIALIST PRIORITY CHECK REQUIRED]`.

The remaining open publication risk is possible abstract subsumption from combinatorics-on-words results outside Collatz under different terminology. This does not block drafting, but it must be addressed before submission.

## 6. Working title

Preferred:

**Factor-Complexity and Pressure Barriers for Critical-Log Syracuse Valuation Words**

Alternative:

**Entropy–Pressure Constraints on Critical-Log Syracuse Orbits**

## 7. Next publication action

The blocking extraction repairs identified by the independent audit are now integrated into the publication package. The next permitted action is to draft `CP20_MANUSCRIPT.tex` from the repaired theorem inventory and outline.

Do not submit the paper until the remaining specialist literature-risk item has been addressed and the finished manuscript has undergone a fresh publication-level zero-trust audit.
