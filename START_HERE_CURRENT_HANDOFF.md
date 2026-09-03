# START HERE — Current Collatz Research Handoff

This is the single entry point for a new LLM, researcher, or recovery session.
Do not infer the active task from filenames, chat history, or the newest-looking report. The machine-readable authority is `CURRENT_RESEARCH_STATE.json`.

## Recovery sequence

1. Confirm branch `main` and fetch `origin/main` without discarding local work.
2. Read `CURRENT_RESEARCH_STATE.json` completely.
3. Run `python tools/verify_handoff.py` and require `HANDOFF VERIFICATION: PASS`.
4. Read, in order:
   - `research_manager/RESEARCH_MANAGEMENT_PROTOCOL.md`
   - `research_manager/CONTINUITY_PROTOCOL.md`
   - `research_manager/decisions/CP20_TASK8B3_E7_RECOVERY_B3_AUDIT_INTEGRATION_2026-09-04.md`
   - the E7 Recovery zero-trust audit
   - the E7R-B3 zero-trust countertheorem audit.
5. Restore the current archive only into a fresh recovery tree if needed.
6. Execute only `next_action` from `CURRENT_RESEARCH_STATE.json`.

## Current accepted scientific state

- `E6-N1 [PROVED][AUDITED/ACCEPTED WITH SCOPE REPAIR]`
- `E7R-B1 [PROVED][AUDITED]`
- `E7R-B2 [PROVED][AUDITED]`, including the conditioned excursion-tail theorem.
- `E7R-B3 frozen pointwise contraction [FALSE][CLOSED]`
- `B3-CT [PROVED][AUDITED]`
- `E7R-B4 / E6-N2 [OPEN]`
- `E7R-B5 [OPEN]`
- `E7R-B6 [OPEN]`

Historical/lost pre-recovery E7 conclusions remain `[UNVERIFIED — ARTIFACTS LOST]`.

The global conditional estimate
`|E[F_{r,4} | S_r=n_r]| = O(1/r)` remains **[OPEN]**.

Nothing here proves Collatz.

## Audited milestone hashes

E7 Recovery V1:
- audit commit `887aa78c6a3508b70a6277cc09705837aec79edf`
- complete package SHA-256 `3889a381235965d3392f944a0c0b637b7fc6493daf6d07d164b836de0f6df486`
- pre-run seal SHA-256 `58734a03a2aa7854f9ecb9f079c6db4b3d05191c249ffa6ccd7e629c4085590c`

E7R-B3 V1:
- audit commit `3b089518e2dc00730e7bf5d16950d0dc05b4506c`
- Stage-1 package SHA-256 `5172a6cadfa5d2bbce84564f19d3ba76b1338e51c7a5a96225d8c77ac4b4b186`
- authorized pre-run seal SHA-256 `acb61ef495bc164c5f55754ea355128bd8105bf7ddec9ff900c2dc16f9646eb3`
- producer result commit `b76e9e004cf9310ae0fc4a295b33d0d1c3836a62`

The audited CF-left family lies in the frozen full pointwise window eventually and satisfies
`mathcal K^(4)_(u_r,v_r)(k_r,ell_r) -> 1`.
Therefore the old full-window `O(1/m_r)` pointwise route is closed.

## Exact next scientific task

Code: `CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1`

Working name: **Tao v7 + Si 2026 Literature Transfer / Exact Normal Form**

Exact next action:

> Create and execute Stage 0 only for "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1". Stage 0 must freeze the exact Tao/Si source versions, notation map, permitted algebraic transformations, falsification tests, and any computation before attempting a theorem transfer. No weighted-operator or E8 work is authorized.

Do **not** execute the Literature Transfer Stage 0 merely by recovering this handoff. Dispatch/execute it only as the next explicit scientific operation. No weighted-operator or E8 work is authorized before that Stage-0 discipline is established.

The future Stage 0 must freeze exact source versions and determine by algebraic normal-form comparison whether the project target is an ordinary Fourier coefficient, derivative/finite-difference/degree-one correction, critical-profile object, resonant/nondecaying object, or outside the cited models. Yuan Si 2026 supplies no accepted theorem dependency by analogy alone.

## Closed route

Formally closed:
**uniform pointwise contraction over the entire frozen endpoint window**.

This closure does not by itself refute a separately sealed weighted, averaged, L2/operator, smaller-subwindow, or modified-geometry statement.

## Mandatory persistence cycle

Every completed computation, audit, or manager milestone automatically closes with:

`result → hashes/manifests → Drive save → Drive read-back → GitHub save/push → GitHub read-back → report`

The user does not need to separately request saving. A subordinate operation is not operationally complete until both persistence/read-back legs succeed unless a connector/service failure is explicitly reported.

## Co-chair/session caution

Historical named co-chair assignments are preserved. Additional head-researcher sessions do not acquire invented identities, signatures, or reviewer roles. Canonical writes are controlled by the active-integrator lock. A cardinality mismatch alone is not a scientific blocker.

Nothing in the current research state proves the Collatz conjecture.
