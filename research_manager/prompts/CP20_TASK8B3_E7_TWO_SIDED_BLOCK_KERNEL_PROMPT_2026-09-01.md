# CP20 TASK 8B3 — E7 TWO-SIDED FEYNMAN–KAC BLOCK KERNEL

## Role and single objective

Act as the computation-and-proof session for one proof-led task. Starting only
from the manager-accepted E6-N1 exact conditioned-geometric representation,
prove or refute a quantitative two-sided complex block-kernel contraction
strong enough to imply

\[
\left|\mathbb E[F_{r,4}\mid S_r=n_r]\right|\le C/r,
\qquad n_r=\lfloor\beta r\rfloor-8.
\]

The sole target remains `(d,C)=(-8,4)`. Do not assume the bound. This is not a
request for a Collatz proof.

## Accepted dependency gate

Use E6 only through:

- E6 complete package SHA-256:
  `9511dc8c9bbd0485f159bbfdf2b5f1f784813af156db5085d90e4faccf1be849`;
- E6 final manifest SHA-256:
  `7c0f7ce6de55582cc1e69d12092f1d822cf169d897a0c36e28570e32378731d1`;
- manager integration decision:
  `research_manager/decisions/CP20_TASK8B3_E6_INTEGRATION_2026-09-01.md`.

Recompute the available hashes and both E6 manifests before acting. On any
mismatch return `[INPUT INTEGRITY FAILURE]` and stop without repair.

Accepted exact input is E6-N1 only:

\[
N_r=D_r\,\mathbb E[F_{r,4}\mid S_r=n_r],
\]

with the exact finite phase functional and uniform weak-composition bridge.
E6-N2 through E6-N5 are not accepted.

## Mandatory two-stage seal

### Stage 0 — seal and stop

In this turn only:

1. Derive and state the exact finite block-kernel definitions and their domains
   without inspecting any new output.
2. Freeze one primary block geometry, one endpoint window, one tail event, and
   the exact norm or pointwise inequality to be tested. Choices must be made
   before any E7 output is generated.
3. Freeze all permitted symbolic or small exact checks, source/configuration
   filenames, output schemas, theorem ladder, falsification criteria, and stop
   rules.
4. Create `CP20_TASK8B3_E7_PRE_RUN_SEAL.md`, a manifest covering every pre-run
   byte, and a normalized `CP20_TASK8B3_E7_PRE_RUN_SEAL.zip`.
5. Stop with exactly
   `[PRE-RUN SEAL READY — AWAITING MANAGER AUTHORIZATION]` and report hashes.

Do not execute Stage 1 in the same turn. No new E7 symbolic search,
enumeration, numerical inspection, or proof experiment implemented in code is
authorized before external acceptance of the seal ZIP hash.

### Stage 1 — only after external manager authorization

Run only byte-identical sealed sources and the proof program below. Any change
to a manifested byte, range, window, norm, or route requires a new seal and
pause.

## Exact kernel required before estimates

For `0<=u<v<=r`, `k<=ell`, define the normalized middle bridge kernel

\[
\mathcal K^{(4)}_{u,v}(k,\ell)
=\mathbb E\!\left[
\prod_{s=u+1}^{v}p^{\rm fin}_{s,S_{s-1},4}
\,\middle|\,S_u=k,S_v=\ell
\right].
\]

Write its exact finite weak-composition sum, including the correct phase at
the left boundary, every finite modular exception, and the zero-length or
zero-increment edge cases. Also write the unnormalized complex kernel and the
positive composition-count kernel, and prove the exact concatenation law with
all conditioning weights displayed.

No contraction argument may begin until these identities and domains are
exact.

## Frozen analytic mechanisms

Attack in this order and reject each at its first false equality or missing
uniform estimate.

### B1. Deterministic swap/holonomy pairing

Use adjacent `(0,1)` versus `(1,0)` swaps only through an explicit involution,
bounded-multiplicity pairing, or block decomposition. Quantify unmatched paths,
overlap dependence, and the phase separation. Local holonomy by itself is not
contraction.

### B2. Arithmetic residue mixing

Lift block phases to exact powers of `omega_{3^v}` and formulate a quantitative
discrepancy or Fourier coefficient estimate for residue counters. A finite
nonzero criterion, an exact-zero test, or a complete-period argument is
insufficient. Any mixing norm must imply an explicit complex-kernel saving.

### B3. Two-sided bridge contraction

Prove or refute, on the predeclared central block and endpoint window, a bound
of the form

\[
|K^{(4)}_{u,v}(k,\ell)|
\le \eta_{v-u}K^+_{u,v}(k,\ell),
\qquad \eta_m=O(1/m),
\]

or a rigorously stated alternative whose concatenation gives the target
`C/r` conditional expectation bound. Uniformity must include the dense
endpoint phase and exact finite cotransition corrections.

### B4. Excursion-tail closure

Prove a conditional bridge tail estimate strong enough to discard paths
outside the frozen window at `o(1/r)` after normalization. It must explicitly
control positive centered excursions where the lacunary phase is not uniformly
Lipschitz. A Brownian heuristic or an unconditioned tail bound alone is
insufficient.

## Falsification targets

Actively attempt to prove one of the following:

1. a phase-aligned family of central endpoints prevents every uniform
   `O(1/m)` block contraction in the frozen window;
2. residue counters retain a nondecaying Fourier mode not determined by the
   endpoint phase;
3. the required excursion tail cannot be `o(1/r)` for the frozen geometry;
4. concatenation loses the local saving through endpoint or finite-row
   corrections;
5. no block/window choice in the sealed class preserves target evaluation and
   gives a polynomial saving.

Failure of one pairing, norm, or window is not a route-closing theorem unless
the quantifiers cover the full sealed class.

## Theorem ladder

- **E7-B1:** exact normalized/unnormalized block kernels and concatenation law;
- **E7-B2:** rigorous conditional excursion-tail bound at the frozen geometry;
- **E7-B3:** quantitative complex block contraction on the frozen window;
- **E7-B4:** uniform target bound
  `|E[F_{r,4}|S_r=n_r]|=O(1/r)`, hence E6-N2;
- **E7-B5:** first-order asymptotic with a controlled coefficient;
- **E7-B6:** controlled nonvanishing or a fixed-target polynomial lower bound.

A rigorous countertheorem closing the full sealed block-kernel class is also a
route-changing result.

## Computation policy

No new depth run is authorized. Do not extend any target sequence, exceed
`r=8000`, add a fit, plot, phase bin, frequency grid, precision level, adaptive
window, rescue calculation, or post-output model choice. Stage 0 may only seal
small exact kernel/concatenation checks whose fixed ranges are justified before
inspection. All finite computations remain `[NUM]` or `[CERTIFIED NUM]`.

## Audit and stop rules

If E7-B3 or higher, E6-N2 or higher, a quantitative arithmetic-cancellation
theorem, a different rigorous scale, or a route-closing countertheorem is
obtained, stop downstream work and prepare an independent zero-trust audit
package.

If only E7-B1 or E7-B2 survives, identify the first missing estimate and
recommend exactly one follow-up or park the conditioned-geometric numerator
route.

## Required Stage 1 answers

1. What exact block kernels and concatenation law were proved?
2. What block geometry, endpoint window, and tail event were frozen?
3. Did B1 produce a quantitative pairing contraction?
4. Did B2 produce quantitative residue mixing?
5. Was the complex block contraction proved?
6. Was the conditional excursion tail closed at `o(1/r)`?
7. Was E6-N2 or any higher theorem obtained?
8. What remains numerical only?
9. Did the audit stop rule fire?
10. Should the numerator route continue or be parked, and what is the single
    next action?

End with exactly:
`Nothing in this task proves Collatz unless a separate complete proof has been supplied and independently audited.`

