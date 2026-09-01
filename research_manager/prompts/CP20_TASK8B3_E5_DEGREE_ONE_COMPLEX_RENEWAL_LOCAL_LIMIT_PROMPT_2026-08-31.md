# CP20 TASK 8B3 — E5 DEGREE-ONE CENTERED COMPLEX RENEWAL / LOCAL-LIMIT BRIDGE

## Role

Act as the computation-and-proof session for one narrowly authorized research task. The research manager owns direction and will review every theorem, computation, and artifact independently.

The task is not to prove Collatz. It is to prove or decisively refute one bridge mechanism between an exact receding boundary and one fixed structured Fourier target.

## Primary target

Use only the primary pair

\[
(d_0,C)=(-8,4).
\]

Determine whether the exact finite-depth critical recurrence admits a degree-one weighted centered complex-renewal/local-limit theorem strong enough to carry the nonzero boundary flux at `x=-beta r` to the fixed target lattice point

\[
x_r=d_0-\theta_r,
\qquad \theta_r=\{\beta r\}.
\]

The desired endpoint is a rigorous nonzero fixed-target conclusion. A valid negative theorem showing that this mechanism cannot transfer the boundary flux is equally successful. Numerical resemblance to `1/r` is not success.

## Audited dependency bundle

Use E4 only through the following exact hashes and the audit scope overlay:

- E4 audit package SHA-256: `a99185ffc4e9daa527a3ee54b59df8ced02bed65490421ce3f9a028119f8c408`.
- E4 complete package SHA-256: `95190d5cbdb633ad049720897b28c73898be229832549153c1fe9ee03b9c4cb1`.
- Independent E4 audit-output ZIP SHA-256: `3879464dfe12f44661b6a0f7cd188a3b2117a0faed67c9c6b8bf1aa6e5a01796`.
- Manager scope overlay: `CP20_TASK8B3_E4_AUDIT_INTEGRATION_2026-08-31.md`.

Recompute all available hashes before beginning. If any hash fails or a load-bearing file is absent, return `[INPUT INTEGRITY FAILURE]` and stop.

Accepted dependencies are limited to:

1. the exact finite E3 critical recurrence;
2. the exact line coordinate `x=d-theta`;
3. qualified finite/infinite unrolling with the audited tail distinctions;
4. centered positive-kernel increment `Y=beta-J` and exact deterministic rotation discrepancy;
5. pure-exponential spectral obstruction on its audited domains;
6. the nonzero moving-boundary asymptotic.

Do not assume compactness, a degree-one bound, an infinite unrolling tail condition, a fixed point, a nonzero fixed-target profile, canonical remote boundary data, or any numerical fit.

## Mandatory two-stage seal protocol

### Stage 0 — prepare and stop

Before running new E5 computations, inspecting new E5 output values, fitting anything, or attempting adaptive parameter choices:

1. Create `CP20_TASK8B3_E5_PRE_RUN_SEAL.md` containing:
   - exact input paths and SHA-256 hashes;
   - the equations and conventions used;
   - theorem success/failure criteria;
   - every proposed numerical range, precision, checkpoint, and stopping rule;
   - planned output filenames;
   - source filenames to be written;
   - explicit statement that no new E5 output has been inspected.
2. Create `CP20_TASK8B3_E5_PRE_RUN_SHA256SUMS.txt` covering the seal and all pre-run source/configuration files.
3. Package them as `CP20_TASK8B3_E5_PRE_RUN_SEAL.zip` and report its SHA-256.
4. **STOP.** Return only `[PRE-RUN SEAL READY — AWAITING MANAGER AUTHORIZATION]`, the three hashes, file list, and path.

Do not continue to Stage 1 in the same turn. The external transcript and manager response are the chronology witness missing from E4.

### Stage 1 — only after explicit manager authorization

After the manager quotes the accepted seal ZIP hash and explicitly says to continue, execute exactly the sealed task. Any change to ranges, theorem target, precision, code, or stopping rule requires a new seal and another hard pause.

## Exact finite object that must remain primary

Let

\[
\alpha=\log_2 3,\qquad \beta=\alpha-1,\qquad
\theta_r=\{\beta r\},\qquad x=d-\theta_r.
\]

For the feasible lattice

\[
\mathcal L_r=\{-\beta r+n:n\in\mathbb Z_{\ge0}\},
\]

write

\[
h_{r,C}(x)=H_{r,d,C}.
\]

Independently re-derive from E3, including the finite-domain threshold and all edge cases,

\[
h_{r,C}(x)
=A_r(x)h_{r,C}(x-1)
+B_r(x)p_C(x)h_{r-1,C}(x+\beta),
\]

where the candidate coefficients are

\[
A_r(x)=\frac{\beta r+x}{\alpha r+x-1},
\qquad
B_r(x)=\frac{r}{\alpha r+x-1},
\qquad
p_C(x)=\exp(2\pi i,2^{x-1-C}).
\]

Do not accept these formulas without checking them against the frozen recurrence. State separately the `n=0` boundary rule and any small-`r` or modular-inverse exceptions.

The exact moving boundary is

\[
x=-\beta r,
\qquad h_{r,C}(-\beta r)=rL_{r,C},
\qquad L_{r,C}\to L_C\ne0.
\]

All asymptotic work must be tied back to this finite triangular problem. A free-standing solution of the limiting homogeneous equation is insufficient.

## Required proof program

### P1. Exact finite renewal / Green representation

Unroll the same-row term only until the true boundary, retaining the exact `1/r` coefficient corrections. Derive a finite positive-kernel/complex-phase representation with:

- the exact boundary remainder;
- exact total mass or mass defect;
- exact dependence on `(r,x)`;
- correct time and space orientation;
- no artificial value outside `mathcal L_r`.

Where possible, express the coefficient after `j` same-row moves using factorials, Gamma functions, or beta-binomial/negative-binomial quantities. Identify the actual finite-depth path measure before invoking a limiting geometric walk.

### P2. Degree-one a priori control or obstruction

Prove one of the following, on a domain sufficient to communicate from the moving boundary to `x_r`:

\[
\sup_r\sup_{x\in\mathcal D_r}
\frac{|h_{r,4}(x)|}{1+|x|}<\infty,
\]

with an explicitly stated corridor `mathcal D_r`, or a weaker tightness/equicontinuity estimate that still preserves the boundary flux and fixed-target evaluation.

If no such estimate can hold, give a rigorous counterexample or lower-growth obstruction arising from the exact finite recurrence. Do not infer failure merely from artificial-boundary sensitivity.

### P3. Centered local-limit / renewal estimate

Derive the correct inhomogeneous triangular-array walk induced by the exact finite coefficients. Then prove, with constants and uniformity ranges, the local-limit or renewal estimate needed across a distance of order `r` from `-beta r` to `x_r`.

The theorem must address:

- zero drift and variance scale;
- the exact `1/r` perturbations of the limiting kernel;
- lattice/nonlattice structure caused by translations by `1` and `beta`;
- the deterministic phase factor `p_4`;
- accumulation of phase error along paths;
- leakage through the region `x>-8`;
- uniformity in the dense phase sequence `theta_r`;
- the contribution of all intermediate row-boundary injections, not only a single direct same-row path.

A real positive-kernel local-limit theorem alone is insufficient unless it is upgraded to the complex recurrence with a quantified non-cancellation statement.

### P4. Boundary-to-target transfer coefficient

Construct or identify an explicit transfer coefficient, Green function, renewal amplitude, or invariant functional `Q_4` for which the finite recurrence yields a statement of the form

\[
h_{r,4}(x_r)=\mathcal A_4(\theta_r)+o(1)
\]

uniformly along the rotation orbit, or another theorem strong enough to imply a polynomial subsequence lower bound at `d_0=-8`.

Prove that the leading coefficient is nonzero. It is not enough that the moving-boundary slope is nonzero; the transfer map from that slope to the target must itself be shown nonzero. Any cone, adjoint functional, Wronskian, renewal residue, or Fourier representation used for non-cancellation must be derived from the finite problem.

### P5. Limiting equation and uniqueness, only after finite control

Only after P1-P4 provide the required inherited bounds may you pass to a subsequential or full limiting profile. If a profile `kappa_4` is obtained, state:

- topology and mode of convergence;
- degree-one left boundary condition;
- seam/representative convention;
- whether the conditional infinite unrolling is justified in that topology;
- uniqueness within the inherited boundary class;
- why `kappa_4` is nonzero on, or communicates nontrivially with, the target interval `[-9,-8]`.

Do not use Banach contraction in an exponentially tilted space; E4 audited that route as unavailable.

## Falsification program

Actively try to refute the bridge before promoting it:

1. Look for exact cancellation of the boundary transfer coefficient.
2. Test whether degree-one mass escapes to `-infinity` under every topology retaining point values.
3. Check whether different finite-depth subsequences or phase representatives produce incompatible target profiles.
4. Search for nonunique fixed points with the same left slope but different target values.
5. Determine whether the right-leakage region destroys all invariant complex cones.
6. Separate failure of one proof technique from failure of the bridge theorem itself.

The first invalid equality or missing uniform quantifier must be recorded immediately.

## Bounded computation policy

E5 is proof-led. Computation may only:

- verify exact formulas on small enumerated cases;
- test sealed local-limit normalizations and transfer coefficients;
- search for counterexamples within predeclared ranges;
- compare independent implementations and precision levels.

Unless the Stage 0 seal explicitly declares a smaller range, the absolute depth ceiling remains `r=8000`; it may not be increased after inspection. Existing E3/E4 data may be read only after their hashes pass. New fits or plots are `[NUM]` and cannot establish asymptotics or non-cancellation.

## Success ladder and stop rules

Classify the strongest achieved result:

- **E5-S1:** exact finite renewal/Green representation only;
- **E5-S2:** inherited degree-one bound or a rigorous obstruction;
- **E5-S3:** uniform centered complex local-limit/renewal estimate;
- **E5-S4:** nonzero boundary-to-target transfer coefficient;
- **E5-S5:** fixed-target nonzero asymptotic or rigorous polynomial subsequence lower bound.

Mandatory audit stop: if E5-S3, E5-S4, E5-S5, or another route-changing theorem is obtained, do not begin downstream Collatz work. Package it for independent audit and stop.

Failure stop: if a load-bearing bridge statement is false, package the counterexample or no-go theorem and recommend whether to park the entire critical-bridge route.

## Stage 1 deliverables

After authorization, produce at minimum:

1. `CP20_TASK8B3_E5_EXACT_FINITE_RENEWAL.md`
2. `CP20_TASK8B3_E5_DEGREE_ONE_BOUND_OR_OBSTRUCTION.md`
3. `CP20_TASK8B3_E5_COMPLEX_LOCAL_LIMIT_ATTEMPT.md`
4. `CP20_TASK8B3_E5_BOUNDARY_TO_TARGET_TRANSFER.md`
5. `CP20_TASK8B3_E5_FALSIFICATION_REPORT.md`
6. `CP20_TASK8B3_E5_MASTER_FINDINGS.md`
7. source, tests, machine-readable diagnostics, and saved outputs for every computation
8. deterministic verifier
9. SHA-256 manifest
10. complete ZIP
11. independent-audit ZIP and zero-trust audit prompt if an audit stop fires

Every statement must be labeled `[EXACT]`, `[PROVED]`, `[CERTIFIED NUM]`, `[NUM]`, `[OPEN]`, `[FAIL]`, or `[PARK]`.

## Required final answers after Stage 1

1. What exact finite renewal representation was proved?
2. Was a degree-one inherited bound or tightness theorem proved?
3. Was a uniform complex local-limit/renewal theorem proved?
4. Was the moving-boundary flux transferred to `(-8,4)`?
5. Was the transfer coefficient proved nonzero?
6. Was a fixed-target asymptotic or polynomial subsequence lower bound proved?
7. Which claims remain numerical only?
8. Did the audit stop rule fire?
9. Should this critical-bridge route continue, be repaired, or be parked?
10. What is the single highest-information next action?

End with: `Nothing in this task proves Collatz unless a separate complete proof has been supplied and independently audited.`
