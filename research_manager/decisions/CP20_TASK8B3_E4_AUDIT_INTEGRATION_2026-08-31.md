# CP20 Task 8B3 E4 — Audit Integration Decision

## Manager verdict

**[ACCEPTED WITH REPAIR — CRITICAL-WALK ROUTE DECISION]**

The independent verdict `[AUDIT PASS WITH REPAIR — CRITICAL-WALK ROUTE DECISION]` is accepted for research-direction purposes. The accepted dependency is the combination of the unchanged E4 package, the independent audit outputs, and the scope corrections in this note. No claim of compactness, convergence, fixed-target nontriviality, or Collatz is accepted.

## Verified provenance

- E4 audit package SHA-256: `a99185ffc4e9daa527a3ee54b59df8ced02bed65490421ce3f9a028119f8c408`.
- E4 complete package SHA-256: `95190d5cbdb633ad049720897b28c73898be229832549153c1fe9ee03b9c4cb1`.
- Independent audit-output ZIP SHA-256: `3879464dfe12f44661b6a0f7cd188a3b2117a0faed67c9c6b8bf1aa6e5a01796`.
- Independent audit-output manifest: 5/5 payload hashes matched both in the output folder and inside the ZIP.
- Auditor-reported source gates: E4 28/28 and frozen E3 23/23.
- Independent reduced-recurrence checks: six complex checkpoints, maximum error `2.058e-14`.
- Boundary table recomputation: 40/40 rows, maximum recorded difference zero.

## Accepted exact/proved dependency

1. The half-open cylinder-to-line map `x=d-theta` is an exact measurable and norm-preserving conjugacy to

   \[
   \kappa(x)=a\kappa(x-1)+b p_C(x)\kappa(x+\beta).
   \]

2. Finite same-phase unrolling with its explicit remainder is exact.
3. Infinite unrolling is accepted only under the corresponding pointwise, essential-supremum, or representative-uniform condition `a^{-m}K_m -> 0` as `m -> -infinity`.
4. The positive renewal kernel has centered increment `Y=beta-J`, and deterministic branch discrepancy is exact without an iid branch model.
5. The complex-operator spectral-radius obstruction is accepted for pure exponential weighted `L-infinity` on its stated domain.
6. Extension to asymptotically exponential or patched weights requires fixed-translation ratio limits and, for the infinite unrolled kernel, uniform summable domination. No universal-weight obstruction is accepted.
7. The finite recurrence has a nonzero moving-boundary asymptotic with linear critical size and limiting phase `L_C`.
8. Polynomial allowance degree below one cannot be uniformly inherited. Degree one remains only the weakest surviving candidate, not a proved bound.

## Required documentary repairs

- Interpret the missing `+` before the finite-unrolling remainder in the E4 falsification report as a transcription error; the primary derivation is authoritative.
- Separate pointwise, essential-supremum, and representative-uniform tail limits.
- Restrict bare `BV_loc` closure to the finite-shift operator, or add a global growth/moment condition before applying the infinite unrolled operator.
- Treat “predeclaration predates inspection” as a package assertion, not independently certified chronology; ZIP timestamps were normalized and no external seal was supplied.

The frozen E4 artifacts are not edited. This note is the scope overlay for downstream work.

## Still open

- A uniform degree-one finite-depth bound or tightness theorem.
- Compactness in a topology retaining fixed-target values.
- A canonical transfer from `x=-beta r` to a fixed target.
- A nonzero fixed-target limiting profile.
- Uniqueness or classification of fixed points in the linear-growth class.

## Authorized next action

Open exactly one sealed task: derive or refute a degree-one weighted centered complex-renewal/local-limit theorem that transfers the inherited nonzero moving-boundary flux to the primary fixed pair `(d0,C)=(-8,4)`. The task begins with a hard pre-run seal pause. No new numerical output may be inspected before the manager records the seal hash and authorizes execution.
