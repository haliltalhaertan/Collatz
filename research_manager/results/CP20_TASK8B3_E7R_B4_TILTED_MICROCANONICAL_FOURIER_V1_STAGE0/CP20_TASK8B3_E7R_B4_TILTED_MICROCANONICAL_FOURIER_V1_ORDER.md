# CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1
# STAGE 0 — FALSIFICATION-FIRST PRE-RUN SEAL

ROLE

You are the computation/proof specialist.

Execute STAGE 0 ONLY.

Do NOT execute Stage 1.
Do NOT prove E6-N2.
Do NOT begin E8.
Do NOT begin a weighted/operator rescue.
Do NOT alter canonical main.
Do NOT claim that tilting itself gives cancellation.
Do NOT claim that Tao or Si already applies after tilting.

Repository:
haliltalhaertan/Collatz

Required canonical main:
57f670bd531cee8f0f2d6eeb27431243f6e3a479

Task code:
CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1

Name:
Tilted / Recentered Microcanonical Fourier Cancellation

Canonical stage on entry:
STAGE_0_READY_NOT_DISPATCHED

==================================================
0. CANONICAL INTAKE
==================================================

Fetch origin/main.

Require:

HEAD == 57f670bd531cee8f0f2d6eeb27431243f6e3a479

or that this commit is an ancestor of the synchronized canonical main with
no intervening scientific state that supersedes B4.

Run:

python tools/verify_handoff.py

Require:

HANDOFF VERIFICATION: PASS

Read at minimum:

CURRENT_RESEARCH_STATE.json
START_HERE_CURRENT_HANDOFF.md

research_manager/decisions/
CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_AUDITED_INTEGRATION_2026-09-04.md

research_manager/results/
CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_AUDIT_STOP/
CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_REPORT.md

bagimsiz-denetim/
e7r-literature-transfer-v1-zero-trust-audit-20260904/
CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_ZERO_TRUST_AUDIT_2026-09-04.md

Accepted scientific dependencies only:

E6-N1
[PROVED][AUDITED/ACCEPTED WITH SCOPE REPAIR]

E7R-B1
[PROVED][AUDITED]

E7R-B2
[PROVED][AUDITED]

B3-CT
[PROVED][AUDITED]

LT-N1 ... LT-N5
[PROVED][AUDITED]

LT-CT
[PROVED][AUDITED]

E6-N2 remains:
[OPEN]

Closed route:

Direct transfer/application of the FROZEN Tao v7 / Si 2026 analytic
theorems to the exact project microcanonical fiber.

Do not reopen that route by merely changing the reference probability
measure.

==================================================
1. FROZEN EXACT TARGET
==================================================

Freeze:

alpha = log_2(3)

T_r = floor(alpha*r) - 8

eta_r = 2^(T_r-4) mod 3^r

and the audited exact normal form

G_r
=
E[
  e_{3^r}(eta_r F_r^aff(A_1,...,A_r))
  |
  sum_i A_i = T_r
].

The research target remains

|G_r| = O(1/r).

No separate global mod-16 cocycle exists in this fixed-total observable.

==================================================
2. TILTED REFERENCE LAW
==================================================

Define, for p in (0,1),

P_p(A=m) = p (1-p)^(m-1),
m = 1,2,...

so

E_p[A] = 1/p.

Freeze the candidate centralizing parameter

p_* = 1/alpha.

Then

E_{p_*}[A] = alpha.

Let

q_* = 1-p_*.

Variance:

sigma_*^2
=
(1-p_*)/p_*^2
=
alpha(alpha-1).

IMPORTANT:

Tilting changes only the UNCONDITIONED reference law.

It does NOT change the target conditional law if exact conditional-law
invariance is established.

Tilting by itself supplies zero Fourier cancellation.

==================================================
3. STAGE-0 CORE QUESTIONS T1–T8
==================================================

Do not adjudicate these as final theorems in Stage 0.

Freeze them as the exact Stage-1 program and perform only the pure algebra /
definition checks explicitly permitted below.

-------------------------
T1 — CONDITIONAL-LAW INVARIANCE
-------------------------

Candidate exact identity:

For every p in (0,1), conditional on

sum_i A_i = T,

the iid Geom(p) law is uniform over positive compositions of T into r parts.

Reason to be checked:

For every such composition a,

P_p(A_1=a_1,...,A_r=a_r)
=
p^r (1-p)^(T-r),

which depends only on T.

Therefore candidate conclusion:

Law_{p_*}(A | sum A_i=T_r)
=
Law_{1/2}(A | sum A_i=T_r),

and hence the exact project G_r may be evaluated under P_{p_*} after
conditioning.

Stage 0 may verify this pure finite algebra exactly.

It must NOT infer any decay from it.

-------------------------
T2 — CENTRALITY UNDER THE TILT
-------------------------

Freeze:

E_{p_*}[sum A_i] = alpha*r.

Since

T_r = floor(alpha*r)-8,

define

delta_r = T_r-alpha*r.

Freeze exact range:

-9 < delta_r <= -8.

Thus the target total differs from the tilted mean by O(1).

Stage 0 may verify this pure algebra.

Also record explicitly:

This DOES NOT put the project into Si's frozen theorem regime
s=2n+O(sqrt(n log n)).

The numerical ratio T_r/r is still asymptotic to alpha != 2.

Changing the reference law does not change the deterministic ratio s/n in
Si's theorem.

This is a mandatory guardrail.

-------------------------
T3 — EXACT DENOMINATOR
-------------------------

Define

D_r
=
P_{p_*}(sum_i A_i=T_r).

Freeze the exact negative-binomial formula:

D_r
=
C(T_r-1,r-1)
p_*^r
q_*^(T_r-r).

Freeze the candidate local-limit asymptotic:

D_r
~
1 / sqrt(2*pi*sigma_*^2*r)

with

sigma_*^2=alpha(alpha-1),

because T_r-alpha*r=O(1).

Stage 1 must prove this rigorously with a uniform error sufficient for the
later quotient.

Stage 0 may symbolically verify the exact formula but must not label the
asymptotic proved unless a full proof is explicitly part of the Stage-0
scope, which it is NOT.

-------------------------
T4 — EXACT MICROCANONICAL NUMERATOR
-------------------------

Define

chi_r(A)
=
e_{3^r}(eta_r F_r^aff(A)).

Define

N_r
=
E_{p_*}[
  chi_r(A)
  1_{sum_i A_i=T_r}
].

Conditional-law invariance should give the exact relation

G_r = N_r / D_r.

Freeze this as the central reduction.

Stage 0 may verify the definition-level identity.

-------------------------
T5 — REQUIRED NUMERATOR SCALE
-------------------------

Given the denominator scale D_r ~ c r^(-1/2), freeze the precise target:

N_r = O(r^(-3/2))

is sufficient to obtain

G_r = O(1/r).

Also record:

A mere bound

N_r = O(r^(-1/2))

is useless for E6-N2.

A bound

N_r = o(r^(-1/2))

is still insufficient unless its quantitative rate reaches an extra 1/r.

This prevents qualitative-decay overclaim.

-------------------------
T6 — FOURIER INVERSION IN THE TOTAL-SUM VARIABLE
-------------------------

Freeze an exact Fourier-inversion representation.

One acceptable normalization is:

H_r(t)
=
E_{p_*}[
  chi_r(A)
  exp(i t (sum_i A_i-alpha*r))
].

Then

N_r
=
(1/(2*pi))
integral_{-pi}^{pi}
  exp(-i t (T_r-alpha*r))
  H_r(t)
dt.

Stage 1 must derive the exact convention and sign.

Stage 0 must freeze one convention and mechanically test it on finite small
cases.

No asymptotic integral estimate is authorized in Stage 0.

-------------------------
T7 — NEW JOINT FOURIER / RENEWAL THEOREM TARGET
-------------------------

The central scientific question is NOT:

"Does Tao's existing theorem now apply?"

It does not follow from the audit.

Freeze instead the NEW theorem-development question:

Can one prove sufficiently strong bounds for the joint transform

H_r(t)
=
E_{p_*}[
  e_{3^r}(eta_r F_r^aff)
  e^{it(sum A_i-alpha*r)}
]

uniformly over the t-ranges required by Fourier inversion, strongly enough
that its integral is O(r^(-3/2))?

The future proof may be organized into:

major arc:
|t| <= L_r / sqrt(r)

intermediate arc

minor arc

but Stage 0 must NOT choose adaptive L_r after seeing results.

If such a split is sealed, choose the complete deterministic scale now.

Mandatory falsification questions:

T7-F1:
Does the Tao white-point/renewal proof use p=1/2 in a load-bearing identity
that fails for p_*?

T7-F2:
Does the tilted transfer operator acquire a unit-modulus eigenvalue or
resonance at eta_r preventing the required bound?

T7-F3:
Does H_r(0) remain too large for N_r=O(r^-3/2)?

T7-F4:
Can a central t-neighborhood produce a nonzero leading local-limit term of
order r^-1/2, which would kill the route unless an exact cancellation occurs?

T7-F5:
Is any proposed cancellation merely numerical rather than algebraic?

No claim of leading-coefficient cancellation is accepted without exact
derivation.

-------------------------
T8 — PRE-REGISTERED ALTERNATIVE MECHANISMS
-------------------------

Freeze but DO NOT execute two fallback branches:

T8-A:
Saddlepoint / Edgeworth expansion of the joint tilted transform.

Primary question:
Does the leading coefficient vanish exactly?
If yes, identify the first surviving term.
If no, record the obstruction.

T8-B:
Endpoint-weighted / cotransition block decomposition.

Primary question:
Can the global conditional expectation be controlled by actual endpoint
weights even though the frozen full-window pointwise contraction is false?

These are fallbacks only.

Stage 1 must NOT jump to them until the direct tilted joint-transform route
has been adjudicated according to the sealed stop/failure logic.

==================================================
4. IMPORTANT LOGICAL GUARDRAILS
==================================================

Freeze all of the following explicitly.

G1.
Exponential tilting is a change of proof measure, not a change of the
conditional project object.

G2.
Centrality under P_{p_*} does NOT make Si's frozen s~2n theorem applicable.

G3.
Tao Proposition 1.17 is proved for the original Syracuse Geom(2) reference
law. No theorem under Geom(p_*) is inherited automatically.

G4.
The exact conditional-law invariance is useful only if a new unconditioned
joint-transform theorem can be proved under P_{p_*}.

G5.
Do not infer O(1/r) from qualitative Rajchman decay, o(1), polynomial decay
of unspecified order, or an unconditioned Fourier bound without the total-sum
Fourier variable.

G6.
The frequency eta_r depends on r and T_r:

eta_r = 2^(T_r-4) mod 3^r.

Uniformity in this moving primitive frequency is part of the theorem target.

G7.
No separate global mod-16 cocycle is available to force a cancellation.

G8.
B3-CT remains valid and must be treated as a falsification constraint on any
blockwise mechanism.

==================================================
5. FUTURE OUTCOME LADDER
==================================================

Freeze the Stage-1 outcome ladder.

B4-N1
Exact tilt conditional-law invariance.

B4-N2
Exact tilted denominator formula + rigorous local limit
D_r ~ c_* r^(-1/2).

B4-N3
Exact total-sum Fourier inversion for N_r.

B4-N4
A valid deterministic major/intermediate/minor arc decomposition for the
joint transform.

B4-N5
A load-bearing joint-transform estimate beyond existing Tao/Si theorems.

B4-N6
N_r = O(r^(-3/2)).

B4-N7
E6-N2:
|G_r| = O(1/r).

Route-specific countertheorem:

B4-CT

A rigorous obstruction showing that the frozen tilted joint-transform route,
with its exact target and permitted mechanisms, cannot yield the required
numerator scale.

Do NOT let B4-CT silently claim E6-N2 is false unless it actually proves
that stronger statement.

==================================================
6. MANDATORY FUTURE AUDIT STOP
==================================================

Stage 1 must stop immediately for independent audit if it produces any of:

B4-N5 with a genuinely new load-bearing joint Fourier theorem;

B4-N6;

B4-N7 / E6-N2;

a load-bearing B4-CT closing the tilted route;

any theorem that identifies an exact leading-coefficient cancellation or
non-cancellation on which the rest of the proof depends.

No downstream rescue after such a stop.

==================================================
7. FIXED STAGE-1 FALSIFICATION TESTS
==================================================

Preregister now.

F1
Conditional-law invariance fails because some composition weights depend on
more than the total.

F2
p_*=1/alpha does not centralize T_r.

F3
Denominator is not Theta(r^-1/2).

F4
Fourier inversion normalization/indexing is inconsistent.

F5
The required numerator scale is weaker/stronger than O(r^-3/2) because the
denominator scale was misstated.

F6
Tao's p=1/2 machinery has a load-bearing step with no p_* analogue.

F7
A resonant central contribution forces N_r to be larger than the target scale.

F8
Any claimed leading cancellation disappears under exact arithmetic or exact
symbolic expansion.

F9
B3-CT contradicts a proposed uniform block contraction used by the tilted
proof.

F10
The tilted route simply repackages the already-closed direct Tao/Si theorem
transfer without proving a new theorem.

==================================================
8. STAGE-0 PERMITTED COMPUTATION
==================================================

Permitted:

- exact symbolic verification of T1/T2/T3 exact formula/T4;
- exact finite check of the chosen Fourier-inversion convention;
- exact rational/algebraic manipulation;
- deterministic syntax/static checks;
- fixed tiny sanity cases needed to validate indexing.

Not permitted:

- asymptotic decay fitting;
- adaptive r search;
- adaptive t search;
- large-r numerical evidence for N_r;
- spectral experiments chosen after seeing outcomes;
- claiming an Edgeworth coefficient;
- claiming a new renewal theorem;
- proving E6-N2;
- weighted/operator calculations;
- E8.

If tiny finite cases are used, freeze all cases before execution in CONFIG.

==================================================
9. REQUIRED STAGE-0 ARTIFACTS
==================================================

Create at minimum:

1.
CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_ORDER.md

2.
CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_CANONICAL_INPUTS.md

3.
CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_DEFINITIONS.md

4.
CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_TARGET_NORMAL_FORM.md

5.
CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_T1_T8_PROGRAM.md

6.
CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_FALSIFICATION_PLAN.md

7.
CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_OUTCOME_LADDER.md

8.
CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_CONFIG.json

9.
CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_OUTPUT_SCHEMA.json

10.
A deterministic Stage-1 skeleton if useful.

11.
CRITICAL REQUIREMENT:

CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_EXECUTION_INTEGRITY_AND_OUTPUT_CONTRACT.md

This contract must already exist in the Stage-0 seal.

It must require before any Stage-1 execution:

- exact authorized seal hash verification;
- exact manifest verification;
- ZIP member count/uniqueness/CRC;
- all dependency hashes;
- proof that no Stage-1 output already exists;
- one-run witness;
- UTC timestamp;
- exact execution entrypoint;
- append-only M/T-stage execution ledger;
- stop-rule enforcement;
- evidence that post-stop downstream stages were NOT_EXECUTED;
- final manifest/package hashes;
- Drive/GitHub persistence read-back.

The future canonical integrator must canonicalize this contract BEFORE Stage-1
authorization/execution.

12.
CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_PRE_RUN_SEAL.md

13.
CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_PRE_RUN_SHA256SUMS.txt

14.
CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_PRE_RUN_SEAL.zip

==================================================
10. LARGE-ARTIFACT POLICY
==================================================

Current canonical archive is already close to the 100,000,000-byte builder
limit.

Do not duplicate historical or Literature Transfer binary packages.

Stage-0 GitHub artifacts should be text/source/config/hash material only.

If a complete bundle is needed, store it on Drive and put only its manifest,
hash and Drive identifier on GitHub.

Do not delete old artifacts for headroom.

==================================================
11. PERSISTENCE GATE
==================================================

This Stage-0 task is not operationally complete until:

Stage-0 result
→ hashes/manifests
→ seal ZIP CRC
→ Drive save
→ Drive read-back
→ GitHub working branch save/push
→ GitHub read-back
→ final report.

Do not write canonical main.

Use a dedicated working branch.

==================================================
12. TERMINAL STATUS
==================================================

STOP after Stage 0.

Do not request or self-authorize Stage 1.

Final status must be:

[CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1
— STAGE 0 FROZEN — AWAITING MANAGER AUTHORIZATION]

Final report must include only:

- canonical base commit;
- working branch + commit SHA;
- exact p_* and sigma_*^2 definitions;
- T1–T8 inventory;
- fixed falsification inventory F1–F10;
- future outcome ladder;
- Stage1 execution-integrity contract present: YES/NO;
- pre-run seal ZIP SHA-256;
- manifest SHA-256;
- member count + CRC;
- Drive location/read-back;
- GitHub read-back;
- explicit confirmation Stage 1 was NOT executed.

Nothing in this task proves the Collatz conjecture.