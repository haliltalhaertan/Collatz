# CP20 Task 8B3 — E7 Recovery + B3 Countertheorem Canonical Integration

## Verdict

**[INTEGRATED — AUDITED RECOVERY + B3 COUNTERTHEOREM]**

This is a management/integration decision only. No new mathematical research was performed, and no Literature Transfer, weighted-operator, or E8 task was executed.

## Canonical evidence

### E7 Recovery V1

- Canonical audit commit: `887aa78c6a3508b70a6277cc09705837aec79edf`
- Audit record: `bagimsiz-denetim/e7-recovery-v1-zero-trust-audit-20260903/CP20_TASK8B3_E7_RECOVERY_V1_ZERO_TRUST_AUDIT_2026-09-03.md`
- Audit verdict: `[AUDIT PASS]`
- Audited Recovery package SHA-256: `3889a381235965d3392f944a0c0b637b7fc6493daf6d07d164b836de0f6df486`
- Audited Recovery pre-run seal SHA-256: `58734a03a2aa7854f9ecb9f079c6db4b3d05191c249ffa6ccd7e629c4085590c`

Accepted with no scope broadening:
- `E7R-B1 [PROVED][AUDITED]`
- `E7R-B2 [PROVED][AUDITED]`, including the conditioned excursion-tail theorem.

### E7R-B3 V1

- Canonical countertheorem audit commit: `3b089518e2dc00730e7bf5d16950d0dc05b4506c`
- Audit record: `bagimsiz-denetim/e7r-b3-v1-zero-trust-audit-20260904/CP20_TASK8B3_E7R_B3_V1_ZERO_TRUST_AUDIT_2026-09-04.md`
- Audit verdict: `[AUDIT PASS]`
- Audited Stage-1 package SHA-256: `5172a6cadfa5d2bbce84564f19d3ba76b1338e51c7a5a96225d8c77ac4b4b186`
- Authorized B3 pre-run seal SHA-256: `acb61ef495bc164c5f55754ea355128bd8105bf7ddec9ff900c2dc16f9646eb3`
- Producer result commit: `b76e9e004cf9310ae0fc4a295b33d0d1c3836a62`

Accepted:
- `B3-CT [PROVED][AUDITED]`.

For the preregistered CF-left endpoints
\[
k_r=\left\lceil u_r n_r/r-W_r\right\rceil,\qquad
\ell_r=\left\lceil v_r n_r/r-W_r\right\rceil,
\]
the audit establishes eventual feasibility and frozen-window membership and
\[
\mathcal K^{(4)}_{u_r,v_r}(k_r,\ell_r)\to1.
\]
Therefore the frozen full-window pointwise statement
\[
\sup_{(k,\ell)\in\mathcal W_r}|\mathcal K^{(4)}_{u_r,v_r}(k,\ell)|=O(1/m_r)
\]
is false.

The accepted scope is exactly the audited pointwise full-window statement. No inference is made against smaller subwindows, averaged/weighted/L2/operator norms, or modified geometries.

## Integrated scientific state

- `E6-N1 [PROVED][AUDITED/ACCEPTED WITH SCOPE REPAIR]`
- `E7R-B1 [PROVED][AUDITED]`
- `E7R-B2 [PROVED][AUDITED]`
- `E7R-B3 frozen pointwise contraction [FALSE][CLOSED]`
- `B3-CT [PROVED][AUDITED]`
- `E7R-B4 / E6-N2 [OPEN]`
- `E7R-B5 [OPEN]`
- `E7R-B6 [OPEN]`

Historical/lost pre-recovery E7 conclusions remain `[UNVERIFIED — ARTIFACTS LOST]` and are not promoted.

The global conditional estimate
\[
|\mathbb E[F_{r,4}\mid S_r=n_r]|=O(1/r)
\]
remains **[OPEN]**.

## Branch decision

The route **uniform pointwise contraction over the entire frozen endpoint window** is formally **[CLOSED]**.

No ad hoc weighted-operator replacement is authorized by this integration.

## Exact next scientific task

Code: `CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1`

Working name: **Tao v7 + Si 2026 Literature Transfer / Exact Normal Form**

The future task has one objective: determine the exact algebraic/parameter correspondence between
\[
\mathbb E[F_{r,4}\mid S_r=n_r]
\]
and its finite phase cocycle and the conditioned affine/Fourier objects used in:

1. Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, using the current arXiv v7;
2. Yuan Si (2026), *A Microcanonical Phase Transition for the Collatz Affine Random Model*.

Stage 0 must determine by exact normal-form comparison whether the project target is an ordinary Fourier coefficient, a derivative/finite-difference/degree-one correction, a critical-profile object, a resonant/nondecaying object, or outside those models. No theorem from Si 2026 is accepted as a dependency merely by analogy or because it appears in a preprint.

## Single next action

> Create and execute Stage 0 only for "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1". Stage 0 must freeze the exact Tao/Si source versions, notation map, permitted algebraic transformations, falsification tests, and any computation before attempting a theorem transfer. No weighted-operator or E8 work is authorized.

This integration does not execute that action.

## Persistence governance

The project-wide milestone completion rule is now:

`result → hashes/manifests → Drive save → Drive read-back → GitHub save/push → GitHub read-back → report`

A completed computation, audit, or manager milestone is not operationally complete until both persistence/read-back legs succeed. A connector/service failure must be reported explicitly and must not be silently represented as successful dual persistence.

## Co-chair cardinality

Historical named co-chair assignments are preserved. Additional head-researcher sessions do not acquire invented identities, signatures, or reviewer assignments. The active-integrator lock controls canonical writes. Existing two-assessment rules continue to apply where a milestone already has two named co-chairs assigned.

Nothing in this integration proves the Collatz conjecture.
