# CP20 TASK 8B3 — E4 WEIGHTED-OFFSET COMPACTNESS & CRITICAL WALK

## Role

You are the mathematical computation/proof session. This is a narrowly scoped
route-decision task after E3. Work adversarially. Re-derive every claimed
operator identity, try to break the proposed weighted compactness route, and
do not choose a different Collatz branch.

The research-manager session, not this session, owns downstream strategy.

## Mandatory input gate

Read the complete E3 package under:

`./_extracted/Collatz Problemi — Araştırma Arşivi/CP20/Task 8 — Literature Reconnaissance and Branch Selection/Task 8B0 — Literature Mechanism Falsification/Module D — 2-adic Start-Rate + Return-Word Recurrence/Module E — Critical-Mass Endpoint Anti-Concentration/E3 — Quasiperiodic Critical-Ray Transfer/`

At minimum read:

- `CP20_TASK8B3_E3_MASTER_FINDINGS.md`
- `CP20_TASK8B3_E3_LIMIT_EQUATION_DERIVATION.md`
- `CP20_TASK8B3_E3_THEOREM_ATTEMPTS.md`
- `CP20_TASK8B3_E3_FALSIFICATION_REPORT.md`
- `CP20_TASK8B3_E3_PREDECLARATION.md`
- `CP20_TASK8B3_E3_VERIFY.py`
- `SHA256SUMS.txt`

Before new work:

1. verify all 23 E3 manifest entries;
2. rerun the unchanged E3 verifier;
3. confirm `ALL E3 VERIFIER ASSERTIONS: PASS`;
4. confirm the E3 package is not modified by E4.

If any check fails, stop with `[INPUT INTEGRITY FAILURE]`.

## Frozen E3 starting point

Let

\[
\alpha=\log_2 3,
\qquad
\beta=\alpha-1,
\qquad
T\theta=\{\theta-\beta\},
\]

and

\[
P_{d,C}(\theta)
=\exp\!\left(2\pi i\,2^{d-1-C-\theta}\right).
\]

The necessary limiting equation derived in E3 is

\[
K_{d,C}(\theta)
=aK_{d-1,C}(\theta)
+bP_{d,C}(\theta)
K_{d+\varepsilon(\theta),C}(T\theta),
\tag{LE}
\]

where

\[
a=\frac\beta\alpha,
\qquad
b=\frac1\alpha,
\qquad
a+b=1,
\]

and

\[
\varepsilon(\theta)=
\begin{cases}
1,&0\le\theta<\beta,\\
0,&\beta\le\theta<1.
\end{cases}
\]

E3 proves neither convergence to a profile nor nontriviality. The zero profile
solves (LE). The offset axis is infinite, finite truncations are not closed,
and no inherited boundary condition in \(d\) is known.

Primary target pair:

\[
(d_0,C)=(-8,4).
\]

Secondary robustness pair:

\[
(d_0,C)=(-8,7).
\]

A theorem for every \((d,C)\) is not required. One explicit primitive pair
with a rigorous subexponential lower bound is sufficient to close the simple
uniform pointwise exponential high-conductor route.

## Main decision question

Determine whether the exact finite recurrence supplies a **closed weighted
offset boundary condition** strong enough to:

1. control truncation of the infinite offset axis uniformly in depth;
2. obtain compactness, or a rigorous substitute, for the scaled critical
   sequence;
3. pass to a solution of (LE); and
4. exclude the zero solution for the primary pair.

If this route is impossible in all natural weighted spaces, prove the precise
obstruction and identify the correct critical-walk/renewal replacement.

## Mandatory Phase 1 — exact unrolling and critical-walk structure

Re-derive or refute the following candidate transformation. Do not accept it
from this prompt.

Starting from (LE), repeatedly substitute the same-phase \(d-1\) term. For a
bounded fixed point, check whether the boundary remainder vanishes and whether
one obtains

\[
\boxed{
K_{d,C}(\theta)
=\sum_{j\ge0}ba^jP_{d-j,C}(\theta)
K_{d-j+\varepsilon(\theta),C}(T\theta).
}
\tag{U}
\]

Mandatory checks:

1. Prove the exact finite-\(J\) identity including its remainder.
2. State the weakest growth condition as \(d\to-\infty\) that makes the
   remainder vanish. Do not assume boundedness if a weaker natural condition
   follows from the finite recursion.
3. Verify that the coefficient masses satisfy
   \(\sum_{j\ge0}ba^j=1\).
4. Interpret the unphased offset increment carefully. With the correct
   orientation, derive or refute
   \[
   \Delta d=\varepsilon(\theta)-j.
   \]
5. Use unique ergodicity of the irrational rotation, not an independence
   assumption, to derive or refute the candidate average drift
   \[
   -\frac{a}{b}+\int_0^1\varepsilon(\theta)\,d\theta
   =-\beta+\beta=0.
   \]
6. Compute the corresponding second moment/variance when meaningful and
   distinguish an exact deterministic cocycle statement from a probabilistic
   analogy.
7. Determine whether the zero-drift identity is the structural reason no
   one-sided exponential offset weight yields a strict contraction.

Classify (U), the drift identity, and every operator consequence separately.
An elementary exact reformulation alone does not trigger the audit stop rule.

Deliver:

`CP20_TASK8B3_E4_EXACT_UNROLLING_AND_CRITICAL_WALK.md`.

## Mandatory Phase 2 — weighted-space feasibility theorem or obstruction

Test the following spaces systematically:

- weighted \(\ell^\infty\) in offset;
- weighted \(\ell^1\) in offset;
- polynomial weights \((1+|d-d_0|)^p\);
- one-sided and two-sided exponential weights;
- bounded variation or another phase-regularity norm compatible with the
  branch at \(\beta\);
- an analytic/generating-function offset norm if naturally induced by the
  exact Hadamard identity.

For each candidate space:

1. define the norm exactly;
2. prove whether (LE) or (U) is bounded on it;
3. compute a rigorous norm/spectral-radius bound where possible;
4. determine whether the branch matching and dense rotation orbit preserve
   the space;
5. determine whether the finite-depth scaled family is uniformly bounded in
   that norm;
6. prove or refute a uniform finite-offset truncation error for the target
   component \(d_0=-8\);
7. identify the boundary data inherited from the actual finite recursion,
   rather than imposing zero, reflecting, or periodic boundaries by choice.

### Exponential-weight falsification test

Derive the exact exponential moment associated with the candidate increment
law, with all orientation signs checked. Determine whether zero average drift
and convexity force the best exponential-weight bound to occur at the
unweighted point with value at least one. This must be proved for the actual
deterministic rotation/branch cocycle; an iid random-walk calculation is only
a heuristic until transferred rigorously.

### Required route decision

Return one of:

- a closed weighted space with a proved uniform tail/truncation estimate;
- a theorem that the natural exponential weighted spaces cannot contract,
  plus the weakest surviving polynomial/renewal framework;
- an explicit unresolved inequality that prevents either decision.

Deliver:

`CP20_TASK8B3_E4_WEIGHTED_SPACE_DECISION.md`.

## Mandatory Phase 3 — inherited boundary and nontriviality

The limit equation is homogeneous. Compactness without nontriviality is not
enough.

Attempt each of the following:

### N1 — finite-depth normalization survives the limit

Trace the \(r=1\) base data through an exact path expansion. Determine whether
some normalized mass, functional, residue, or boundary flux remains nonzero at
the critical target after scaling by \(r\).

### N2 — complex cone for the negative-offset sector

For \(C=4\) and offsets near/below \(d_0=-8\), the explicit phase angle is
small. Quantify this exactly. Seek a forward/backward invariant complex sector
or angular-separation estimate. Account for leakage to increasing offsets;
do not prove a cone only for a truncation that the exact dynamics leaves.

### N3 — recurrent phase block lower bound

Seek a rigorously recurrent phase block on which the unrolled kernel has
controlled phase and offset leakage. Prove or refute that repeated visits
preserve a polynomial amount of amplitude for the primary pair.

### N4 — invariant functional / adjoint eigenvector

Search for a bounded nonzero functional on the proved weighted space that is
preserved, or has a controlled renewal equation, and evaluates nontrivially on
the inherited finite-depth data.

### N5 — zero-only theorem

Attempt the opposite conclusion: prove that every fixed point satisfying the
actual inherited boundary/growth condition is zero. If successful, state
whether this invalidates the \(1/r\) profile or only shows that the chosen
topology/boundary condition is wrong.

For every failed attack, record the first missing inequality or quantifier.

Deliver:

`CP20_TASK8B3_E4_NONTRIVIALITY_ATTEMPTS.md`.

## Mandatory Phase 4 — bounded confirmatory diagnostics

Do not extend the general depth beyond \(r=8000\). E4 is a proof-structure
task, not another depth race.

Before inspecting new offset data, predeclare a small diagnostic design. The
recommended maximum scope is:

- \(C\in\{4,7\}\);
- offsets \(-64\le d\le32\);
- selected depths from \(\{1000,2000,4000,6000,8000\}\);
- phase-profile blocks already present in E3 where reusable;
- finite truncations with multiple boundary choices only as sensitivity
  diagnostics, never as theorem evidence.

Use these diagnostics to:

1. estimate offset-tail growth/decay and propose candidate weights;
2. test sensitivity of \(d_0=-8\) to remote boundaries;
3. locate offset leakage under the unrolled kernel;
4. test whether a negative-offset complex cone is numerically plausible;
5. detect whether polynomial rather than exponential offset localization is
   the stable finite-depth model.

All such conclusions remain `[NUM]` unless proved independently. Reuse E3 raw
data rather than recomputing it when possible.

## Prohibited moves

- Do not run a broader/deeper generic search as the main task.
- Do not assume the branch symbols are independent Bernoulli variables.
- Do not infer a local-limit theorem from zero drift alone.
- Do not impose artificial finite-offset boundary conditions and then call
  their fixed point canonical.
- Do not claim compactness from phase bin stability.
- Do not infer nontriviality from finite lower bounds on \(6800\le r\le8000\).
- Do not require a theorem uniform over all \((d,C)\) when one explicit pair
  is enough.
- Do not reopen the full uniform high-conductor exponential theorem.
- Do not reopen CP19 parked high-half/cross-adic branches.
- Do not use Task 8A beyond its frozen audited core.
- Do not overwrite E2 or E3 artifacts.
- Do not use machine-specific absolute paths in scripts.
- Do not claim Collatz is solved.

## Audit stop rule

Stop ordinary work and build an independent zero-trust audit package if any of
the following is proved:

1. a closed weighted-offset compactness theorem inherited from the exact
   finite recurrence;
2. a nonzero limiting profile or infinite-subsequence polynomial lower bound
   for an explicit primitive pair;
3. a zero-only theorem under a genuinely inherited boundary condition;
4. a theorem excluding the natural weighted compactness route and replacing
   it with a rigorous critical renewal/local-limit framework;
5. another result that changes viability of the simple uniform pointwise
   high-conductor route.

Do not use a load-bearing result downstream before independent audit.

## Required E4 outputs

Create a new E4 folder. Do not modify frozen or historical folders.

Minimum outputs:

1. `CP20_TASK8B3_E4_MASTER_FINDINGS.md`
2. `CP20_TASK8B3_E4_EXACT_UNROLLING_AND_CRITICAL_WALK.md`
3. `CP20_TASK8B3_E4_WEIGHTED_SPACE_DECISION.md`
4. `CP20_TASK8B3_E4_NONTRIVIALITY_ATTEMPTS.md`
5. `CP20_TASK8B3_E4_FALSIFICATION_REPORT.md`
6. `CP20_TASK8B3_E4_STRATEGIC_VERDICT.md`
7. predeclaration for every new numerical diagnostic
8. scripts and machine-readable data needed to reproduce diagnostics
9. deterministic verifier and saved verifier output
10. `SHA256SUMS.txt`
11. complete ZIP package
12. audit prompt/package only if the stop rule fires

Scripts must use paths relative to their own location. Record exact runtime,
commands, numeric types, wall time, and code hashes. JSON output must be
deterministically ordered.

## Final verdict format

Return exactly one primary verdict:

- `[AUDIT CANDIDATE — NONZERO CRITICAL PROFILE]`
- `[AUDIT CANDIDATE — ZERO-ONLY INHERITED BOUNDARY THEOREM]`
- `[AUDIT CANDIDATE — CRITICAL-WALK ROUTE DECISION]`
- `[LEAD — CLOSED WEIGHTED COMPACTNESS SURVIVES]`
- `[FAIL — NATURAL WEIGHTED COMPACTNESS OBSTRUCTED]`
- `[OPEN — NO CLOSED SPACE OR NONTRIVIALITY DECISION]`

Then answer in order:

1. Was (U) proved, repaired, or refuted?
2. Is the zero-drift identity exact for the actual deterministic cocycle?
3. Which weighted spaces are rigorously closed?
4. Is there a uniform truncation/tail bound inherited from finite depth?
5. Was compactness proved?
6. Was zero excluded, or proved unique?
7. What new material is only numerical?
8. Did the audit stop rule fire?
9. What single next action should the research manager take?

Nothing in E4 may be described as a proof of Collatz.
