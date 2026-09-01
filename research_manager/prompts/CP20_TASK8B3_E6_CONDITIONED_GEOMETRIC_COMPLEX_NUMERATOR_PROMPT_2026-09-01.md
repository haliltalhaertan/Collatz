# CP20 TASK 8B3 — E6 CONDITIONED-GEOMETRIC COMPLEX NUMERATOR

## Role and single objective

Act as the computation-and-proof session for one proof-led task. Analyze the exact E5 conditioned-geometric bridge at

\[
(d_0,C)=(-8,4),\qquad
n_r=\lfloor\beta r\rfloor-8,
\]

and prove or refute a uniform asymptotic for

\[
N_r:=\mathbb E\!left[F_{r,4}\mathbf1_{\{S_r=n_r\}}\right]
\]

at the critical scale `r^{-3/2}`, with a controlled nonzero phase-dependent coefficient.

This is not a request for a Collatz proof. It is a mechanism-selection and theorem task for one explicit oscillatory numerator.

## Accepted dependency and integrity gate

Use E5 only through the manager integration note and these exact artifacts:

- E5 complete package SHA-256: `3f28f90b29af3a41e1c679593968e9156e9bc3b0882659ec3b8cfa794e9b930d`.
- E5 root manifest SHA-256: `b749117b6d5ba508b46add04623e20ac1c884d2632f1c3a103234767d3217870`.
- E5 diagnostics SHA-256: `7599085a13d8895509946f94195d25a545084ec9285344dcf664c8f559e1eaa6`.
- E5 verifier output SHA-256: `8bbd327d084eb3d3bc381eb075fd787d0b634c167b0c7842f991f9bde2fb667d`.
- Manager integration note: `research_manager/decisions/CP20_TASK8B3_E5_S1_INTEGRATION_2026-09-01.md`.

Recompute all available hashes and the E5 20/20 manifest before acting. On any mismatch, return `[INPUT INTEGRITY FAILURE]` and stop.

Accepted exact input:

\[
G_{r,n}=\mathbb E[F_{r,4}\mid S_r=n],
\]

where `Z_1,...,Z_r` are iid geometric with

\[
\Pr(Z=j)=ba^j,
\qquad \mathbb EZ=\beta,
\qquad \operatorname{Var}(Z)=\sigma^2=\alpha\beta,
\]

\[
S_s=Z_1+\cdots+Z_s,
\qquad
F_{r,4}=\zeta_4\prod_{s=2}^{r}p^{\rm fin}_{s,S_{s-1},4}.
\]

Also accepted:

\[
D_r:=\Pr(S_r=n_r)
=\frac{1+O(r^{-1})}{\sqrt{2\pi\alpha\beta r}}
\]

uniformly for `theta_r={beta r}`. Since

\[
h_{r,4}(d_0-\theta_r)=r\,N_r/D_r,
\]

a bounded nonzero target profile requires `N_r` at scale `r^{-3/2}`.

Do not assume that scale is true.

## Mandatory two-stage seal

### Stage 0 — seal and stop

Before new symbolic searches, exact enumerations, numerical inspection, route selection based on output, or proof experiments implemented in code:

1. Create `CP20_TASK8B3_E6_PRE_RUN_SEAL.md` specifying:
   - input paths and hashes;
   - exact definitions and all finite modular exceptions;
   - the proposed analytic routes below and their falsification criteria;
   - every permitted symbolic/enumerative computation;
   - source and output filenames;
   - stopping and audit rules;
   - the declaration that no new E6 output was inspected.
2. Create a manifest covering the seal, configuration, and every pre-run source file.
3. Create `CP20_TASK8B3_E6_PRE_RUN_SEAL.zip` with normalized contents and report its SHA-256.
4. **STOP** with `[PRE-RUN SEAL READY — AWAITING MANAGER AUTHORIZATION]`.

Do not execute Stage 1 in the same turn. No computation beyond existing E5 data is authorized before the external seal hash is accepted.

### Stage 1 — only after manager authorization

Run only byte-identical sealed sources and the proof program below. Any source, range, or method change requiring new computation requires a new seal and pause.

## Exact analytic normal form — first required result

Define the unnormalized composition sum

\[
A_r(n):=\sum_{z_1+\cdots+z_r=n}F_{r,4}(z_1,\ldots,z_r),
\qquad
\mathcal A_r(z):=\sum_{n\ge0}A_r(n)z^n.
\]

Independently prove or repair

\[
A_r(n)=\sum_{k=0}^{n}p^{\rm fin}_{r,k,4}A_{r-1}(k),
\]

and the candidate Hadamard/coefficient identity

\[
\mathcal A_r(z)
=\frac{1}{1-z}
\left(P^{\rm fin}_{r,4}\odot\mathcal A_{r-1}\right)(z),
\qquad
P^{\rm fin}_{r,4}(z)=\sum_{k\ge0}p^{\rm fin}_{r,k,4}z^k.
\]

Verify the base row and the finite negative-exponent prefix. Relate the desired probability numerator exactly to the coefficient:

\[
N_r=b^r a^{n_r}A_r(n_r).
\]

No asymptotic step may begin until these identities, domains, and coefficient conventions are exact.

## Competing proof mechanisms

Attack the following mechanisms in the stated order. Reject a mechanism at its first false equality or missing uniform bound; do not blend incompatible heuristics.

### M1. Multiplicative coboundary or martingale decomposition

Determine whether the phase cocycle can be written exactly or with a summable controlled defect as

\[
p^{\rm fin}_{s,S_{s-1},4}
=\frac{U_s(S_s)}{U_{s-1}(S_{s-1})}
\bigl(1+R_s\bigr),

\]

or whether a centered additive/martingale difference decomposition exists whose accumulated error is uniform under `S_r=n_r`.

If this is impossible, prove the obstruction; do not merely report that an ansatz failed.

### M2. Coefficient/Hadamard saddle analysis

Use the exact generating recurrence to determine whether a Cauchy-integral saddle expansion exists near the positive negative-binomial saddle. Control the Hadamard phase multiplier on the full contour, not only near the real saddle. Establish or refute a spectral/resolvent expansion with a degree-one critical mode.

Any contour deformation must respect the exponentially growing periods and finite modular phases. A formal saddle expansion without a uniform off-saddle bound is `[OPEN]`.

### M3. Conditioned Feynman-Kac bridge

Treat `F_{r,4}` as an exact multiplicative functional of the conditioned geometric bridge. Derive a block or two-sided bridge decomposition and seek a uniform estimate for the complex transition kernel. The proof must control:

- middle-time fluctuations of order `sqrt(r)`;
- paths entering `S_s-beta s>0`;
- the non-Lipschitz/lacunary phase `exp(2 pi i 2^{x-5})`;
- endpoint conditioning and dense `theta_r`;
- finite `1/r` cotransition corrections.

A Brownian-bridge approximation alone is invalid because the phase is not uniformly smooth on the fluctuation window.

### M4. Arithmetic block cancellation

Exploit the exact `3^s`-cyclotomic and doubling structure only if it yields a quantitative block estimate. The finite criterion

\[
3\nmid\binom{n+r-1}{r-1}\implies A_r(n)\ne0
\]

is accepted but insufficient. Determine whether root-of-unity filters, base-3 carry structure, or complete blocks give polynomial-scale separation or instead force stronger cancellation.

An infinite exact-nonzero subsequence without a polynomial lower bound does not solve the target.

## Required theorem ladder

Classify the strongest result:

- **E6-N1:** exact coefficient/Hadamard or equivalent Feynman-Kac normal form;
- **E6-N2:** uniform upper bound `N_r=O(r^{-3/2})` at the target;
- **E6-N3:** uniform phase-profile asymptotic

  \[
  N_r=\frac{c_4(\theta_r)}{\sqrt{2\pi\alpha\beta}\,r^{3/2}}
  +o(r^{-3/2});
  \]

- **E6-N4:** `c_4` is proved nonzero at a controlled phase or on a controlled subsequence;
- **E6-N5:** a nonzero fixed-target asymptotic or polynomial subsequence lower bound for the original structured Fourier quantity.

If the correct scale differs from `r^{-3/2}`, a rigorous alternative asymptotic or no-go theorem is route-changing success.

## Uniformity and non-cancellation requirements

Every asymptotic must state:

- whether it is uniform for all `theta in [0,1)` or only along the rotation orbit;
- the topology/regularity of `c_4`;
- an explicit error term or a quantified `o(1)`;
- how finite modular exceptions are absorbed;
- why paths with large positive centered displacement do not invalidate the estimate;
- why the leading coefficient exists;
- an independent argument that the coefficient is not identically zero.

Numerical phase-bin stabilization is not a nonzero-coefficient proof.

## Falsification targets

Actively attempt to prove one of these negative outcomes:

1. the normalized sequence `r^{3/2}N_r` has incompatible subsequences not captured by `theta_r`;
2. the coefficient depends on hidden path-scale data beyond endpoint phase;
3. the numerator has a different power or stretched/exponential scale;
4. all candidate critical coefficients vanish by exact arithmetic cancellation;
5. no topology preserving target evaluation is tight under the conditioned complex bridge.

Failure of one analytic technique is not a no-go theorem.

## Computation policy

No deeper numerical run is authorized. Do not compute any new value with `r>8000`, and do not extend the E5 target series.

Stage 0 may predeclare only:

- small exact composition/cyclotomic checks needed to validate identities;
- symbolic coefficient checks;
- read-only reuse of sealed E5 outputs;
- fixed-precision comparisons that do not expand depth or select a model after inspection.

No new fit, plot, phase-bin choice, rescue range, or adaptive frequency grid is allowed. All computation remains `[NUM]` or `[CERTIFIED NUM]` and cannot establish N2-N5.

## Audit and stop rules

If E6-N2 or higher, a different rigorous asymptotic scale, a quantitative arithmetic cancellation theorem, or a route-closing no-go theorem is obtained, stop downstream work and prepare an independent zero-trust audit package.

If only E6-N1 is obtained, report the first missing operator, contour, bridge, or arithmetic estimate and recommend exactly one repaired follow-up—or park the route.

## Required Stage 1 deliverables

1. `CP20_TASK8B3_E6_EXACT_NUMERATOR_NORMAL_FORM.md`
2. `CP20_TASK8B3_E6_COBOUNDARY_MARTINGALE_ATTEMPT.md`
3. `CP20_TASK8B3_E6_HADAMARD_SADDLE_ATTEMPT.md`
4. `CP20_TASK8B3_E6_FEYNMAN_KAC_BRIDGE_ATTEMPT.md`
5. `CP20_TASK8B3_E6_ARITHMETIC_CANCELLATION_ATTEMPT.md`
6. `CP20_TASK8B3_E6_FALSIFICATION_REPORT.md`
7. `CP20_TASK8B3_E6_MASTER_FINDINGS.md`
8. sealed source/configuration, verifier, manifests, and packages for any computation

Use `[EXACT]`, `[PROVED]`, `[CERTIFIED NUM]`, `[NUM]`, `[OPEN]`, `[FAIL]`, and `[PARK]` precisely.

## Required final answers

1. What exact numerator normal form was proved?
2. Which of M1-M4 survives, and why?
3. Was `N_r=O(r^{-3/2})` proved?
4. Was a uniform `r^{-3/2}` asymptotic proved?
5. Was the coefficient proved nonzero?
6. Was a fixed-target lower bound obtained?
7. What remains numerical only?
8. Did the audit stop rule fire?
9. Should the conditioned-geometric bridge continue or be parked?
10. What is the single highest-information next action?

End with: `Nothing in this task proves Collatz unless a separate complete proof has been supplied and independently audited.`
