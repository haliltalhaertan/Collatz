# CP20 TASK 8B3 — E3 CRITICAL-BRIDGE ASYMPTOTIC

## Role

You are the mathematical computation/proof session for the Collatz research project. Work as an adversarial proof engineer, not as the research manager. Your job is to re-derive, falsify, compute, and, only if justified, prove. Do not choose a new research branch beyond the decision rules in this prompt.

Use the local project workspace and read the complete E2 package before doing any new work. The E2 package is under:

`./_extracted/Collatz Problemi — Araştırma Arşivi/CP20/Task 8 — Literature Reconnaissance and Branch Selection/Task 8B0 — Literature Mechanism Falsification/Module D — 2-adic Start-Rate + Return-Word Recurrence/Module E — Critical-Mass Endpoint Anti-Concentration/E2 — Structured Primitive Resonance/`

At minimum, read and verify:

- `CP20_TASK8B3_E2_MASTER_FINDINGS.md`
- `CP20_TASK8B3_E2_STRUCTURED_RECURSION.md`
- `CP20_TASK8B3_E2_ASYMPTOTIC_FALSIFICATION_REPORT.md`
- `CP20_TASK8B3_E2_TASK6_RATE_TRADEOFF.md`
- `CP20_TASK8B3_E2_EXACT_ENGINE.py`
- `CP20_TASK8B3_E2_VERIFY.py`
- all JSON data used by the verifier
- `SHA256SUMS.txt`

First reproduce the E2 verifier and all 15 E2 manifest hashes. If either fails, stop and report `[INPUT INTEGRITY FAILURE]` without continuing.

## Frozen status entering E3

Treat the following as the only authorized starting status:

1. The structured family is defined by
   \[
   F_{r,A,C}:=\phi_{r,A}(2^{A-C}),
   \qquad
   G_{r,n,C}:=F_{r,r+n,C}.
   \]

2. The exact reduced recursion is
   \[
   G_{r,n,C}
   =
   \frac{n}{r+n-1}G_{r,n-1,C}
   +
   \frac{r-1}{r+n-1}
   e_{3^r}(2^{r+n-1-C})G_{r-1,n,C}.
   \]

3. The base case is
   \[
   G_{1,n,C}=e_3(2^{-C}).
   \]

4. Let
   \[
   \alpha=\log_2 3,
   \qquad
   \beta=\alpha-1,
   \qquad
   A_r(d)=\lfloor\alpha r\rfloor+d,
   \qquad
   n_r(d)=A_r(d)-r=\lfloor\beta r\rfloor+d.
   \]

5. E2 numerics through \(r=2200\) strongly favor an approximately \(1/r\) structured resonance for adversarial fixed \(d,C\), but no polynomial lower bound, nonzero subsequential limit, or asymptotic theorem is proved.

6. The current branch verdict is:

   `[LEAD — SUBEXPONENTIAL RESONANCE NUMERICALLY SURVIVES]`.

Do not silently import any stronger claim.

## Primary research question

For fixed integers \(d,C\), determine whether the critical-line sequence

\[
F_{r,A_r(d),C}=G_{r,n_r(d),C}
\]

has a rigorous polynomial/subexponential obstruction to uniform exponential decay.

The preferred theorem targets, in order, are:

### Target T1 — infinite-subsequence lower bound

Prove for at least one explicit fixed pair \((d,C)\), and preferably for a stated nonempty class of pairs, that there exist finite \(K\), positive \(c\), and infinitely many \(r\) such that

\[
|F_{r,A_r(d),C}|\ge c r^{-K}.
\]

Even a rigorously specified phase subsequence is acceptable.

### Target T2 — critical-bridge asymptotic

Prove a sharper relation of the form

\[
rF_{r,A_r(d),C}
=K_{d,C}(\{\alpha r\})+o(1),
\]

or an explicitly repaired variant, with \(K_{d,C}\) nonzero on at least one phase interval or on an infinite phase subsequence.

### Target T3 — rigorous alternative scaling

If \(1/r\) is false, identify and rigorously justify the correct alternative scale. A numerical fit alone is not sufficient.

Any valid T1 or T2 theorem forces \(\liminf_r[-r^{-1}\log_2|F|]=0\) for a primitive/full-conductor family and would close the simple uniform exponential high-conductor route. That is load-bearing and triggers the audit stop rule below.

## Mandatory Phase 1 — re-derive the critical-line dynamics

Independently derive all of the following. Do not copy them as assumptions.

1. Express the phase on the critical line exactly in terms of
   \(\theta_r=\{\alpha r\}=\{\beta r\}\). Check carefully all fixed \(d,C\), including negative values, and all sufficiently large-domain conditions.

2. Determine exactly how the \((r-1,n)\) term maps between offset indices. If
   \[
   \varepsilon_r=\lfloor\beta r\rfloor-\lfloor\beta(r-1)\rfloor\in\{0,1\},
   \]
   derive the correct recurrence coupling among \(d-1\), \(d\), and \(d+\varepsilon_r\).

3. Derive the rotation relation between \(\theta_r\) and \(\theta_{r-1}\), including the exact discontinuity convention for \(\varepsilon_r\).

4. Introduce the scaled family
   \[
   H_{r,d,C}:=rG_{r,n_r(d),C}
   \]
   and derive its exact finite-\(r\) recurrence, including every \(1/r\) correction.

5. From that exact recurrence, derive or refute the candidate limiting functional/cohomological equation for a phase profile \(K_{d,C}(\theta)\). State the function space, discontinuity set, offset coupling, and boundary/growth conditions in \(d\). A formal equation without a well-posed uniqueness/existence framework is only `[LEAD]`.

6. Check edge cases: \(n=0\), \(r=1\), negative offsets before the feasible range, large positive/negative fixed \(C\), and phase points approaching the rotation discontinuity.

Deliver this phase as `E3_LIMIT_EQUATION_DERIVATION.md` with statuses attached to every statement.

## Mandatory Phase 2 — falsification-first computation

The computation is not allowed to assume \(1/r\). Try to break it.

1. Extend targeted computations substantially beyond \(r=2200\) for a small predeclared adversarial set, at minimum:

   - \(d\in\{-8,-5,-3,0,3\}\);
   - \(C\in\{0,2,4,7,10\}\);
   - include the E2 record pairs \((-8,4)\) and \((-8,7)\).

2. Use the reduced recursion, not brute-force composition enumeration except for small validation cases.

3. Predeclare the maximum depth based on resource feasibility. Prefer targeted depth over a broad shallow grid. Record wall time, peak memory, numeric type, platform, and code SHA-256.

4. Track at least:

   - \(|F_r|\);
   - \(r|F_r|\);
   - \(r^p|F_r|\) for several predeclared \(p\);
   - \(\gamma_r=-r^{-1}\log_2|F_r|\);
   - local power exponents on multiple disjoint tail windows;
   - complex phase, not only magnitude;
   - \(H_{r,d,C}\) binned by \(\theta_r\);
   - approach to the rotation discontinuity from both sides.

5. Test at least these competing hypotheses:

   - H1: \(F_r\asymp r^{-1}\) with bounded quasiperiodic amplitude;
   - H2: \(F_r\asymp r^{-p}\) with \(p\ne1\);
   - H3: stretched exponential decay;
   - H4: rare near-zero phase cancellations destroy any uniform polynomial lower bound but leave a nonzero infinite subsequence;
   - H5: the apparent scaling is a finite-precision artifact.

6. Run independent high-precision checks at predeclared sparse depths. Compare complex values, not just magnitudes. Do not select checkpoints after seeing favorable output.

7. Search explicitly for sign/phase cancellation events and for subsequences where \(r|F_r|\) is bounded away from zero. Continued-fraction denominators may be tested but must not be treated as the mechanism unless proved.

8. Produce deterministic machine-readable data and a verifier that checks small exact enumeration, reduced-recursion agreement, saved-data dimensions, predeclared checkpoints, and all reported summary statistics.

Numerics must be labelled `[NUM]` or `[CERTIFIED NUM]`; no finite depth may be promoted to an asymptotic claim.

## Mandatory Phase 3 — proof attacks

Run the following proof attacks in parallel conceptually, but report them separately.

### P1 — compactness plus nontrivial subsequential profile

Seek uniform bounds/equicontinuity or an appropriate weaker compactness principle for the phase-indexed scaled family. Determine whether subsequential limits solve the limiting equation. Then prove or disprove that every admissible limit can be identically zero.

### P2 — transfer/cocycle formulation

Recast the critical-line dynamics as an irrational-rotation cocycle or transfer operator with finite/infinite offset coupling. Identify whether a conserved quantity, invariant functional, renewal identity, or nonzero forcing prevents exponential collapse.

### P3 — direct infinite-subsequence lower bound

Try to avoid a full asymptotic theorem. Isolate a positive-measure or recurrent phase region on which the one-step coefficients and phase avoid destructive cancellation, then prove enough stability across returns to obtain a polynomial lower bound on infinitely many depths.

### P4 — generating function / singular perturbation

Investigate whether the surplus recursion has a generating-function representation whose dominant singularity in the critical scaling yields the observed \(1/r\) law. All exchanges of limits, coefficient extraction, and uniformity in phase must be justified.

### P5 — counter-obstruction construction

Attempt to construct a rigorous cancellation mechanism showing that the proposed nonzero phase profile cannot exist or that zeros accumulate too strongly. A valid negative result is valuable and must be reported.

For every proof attempt, state the exact point of failure if incomplete. Do not hide a missing uniformity estimate behind asymptotic notation.

## Prohibited moves

- Do not attempt the full uniform high-conductor exponential theorem.
- Do not treat an empirical \(1/r\) fit as a theorem.
- Do not claim that closing the simple Fourier route proves Collatz.
- Do not reopen CP19 parked high-half/cross-adic machinery.
- Do not multiply dependent entropy/Fourier savings as if independent.
- Do not use Task 8A beyond its frozen audited core.
- Do not tune \(d,C\), depth windows, precision checkpoints, or fit models after seeing the output without marking the analysis exploratory and rerunning on a fresh holdout range.
- Do not overwrite E0/E1/E2 artifacts.
- Do not use absolute machine-specific paths in scripts.

## Audit stop rule

Immediately stop ordinary research and package an independent zero-trust audit candidate if you obtain any of the following:

1. a rigorous infinite-subsequence polynomial lower bound;
2. a rigorous nonzero phase-profile asymptotic;
3. a universal theorem ruling out every such polynomial/subexponential obstruction;
4. another theorem that changes whether the simple uniform high-conductor route is viable.

Do not use such a theorem downstream before independent audit. Produce an audit prompt that attacks quantifiers, phase discontinuities, offset coupling, uniformity, nontriviality, numerical dependence, and primitive/full-conductor scope.

## Required outputs

Create a new E3 output folder; do not modify the frozen E2 folder. At minimum return:

1. `CP20_TASK8B3_E3_MASTER_FINDINGS.md`
2. `CP20_TASK8B3_E3_LIMIT_EQUATION_DERIVATION.md`
3. `CP20_TASK8B3_E3_FALSIFICATION_REPORT.md`
4. `CP20_TASK8B3_E3_THEOREM_ATTEMPTS.md`
5. `CP20_TASK8B3_E3_STRATEGIC_VERDICT.md`
6. exact/reduced computation engine(s)
7. deterministic verifier and saved verifier output
8. machine-readable summary data and enough raw data to reproduce every table/fit
9. `SHA256SUMS.txt`
10. complete ZIP package
11. audit package and audit prompt only if the stop rule fires

All scripts must use paths relative to their own location. JSON must be deterministically ordered. Record software/runtime versions and command lines.

## Final verdict format

Return exactly one primary branch verdict:

- `[AUDIT CANDIDATE — RIGOROUS SUBEXPONENTIAL OBSTRUCTION]`
- `[AUDIT CANDIDATE — RIGOROUS POSITIVE-RATE THEOREM]`
- `[LEAD — CRITICAL-BRIDGE PROFILE SURVIVES]`
- `[FAIL — 1/R SCALING FALSIFIED; REPLACEMENT IDENTIFIED]`
- `[OPEN — NO THEOREM, NO STABLE REPLACEMENT]`

Then answer, in order:

1. What was re-derived exactly?
2. What was falsified?
3. What is only numerical?
4. Was T1, T2, or T3 proved?
5. What exact proof gap remains?
6. Did the audit stop rule fire?
7. What is the single highest-information next action for the research manager?

Do not claim Collatz is solved.
