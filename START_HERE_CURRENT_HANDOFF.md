# START HERE — Current Collatz Research Handoff

Machine-readable authority: `CURRENT_RESEARCH_STATE.json`. Recover on branch `main`, run `python tools/verify_handoff.py`, and require `HANDOFF VERIFICATION: PASS` before any research action.

## B4 V1 canonical closeout

B4 V1 Stage 0: **[FROZEN — SCIENTIFIC PROGRAM PRESERVED]**.

B4 V1 Stage 1: **[INPUT INTEGRITY FAILURE — INVALID / NON-CANONICAL]**. The pre-T1 `RUN_WITNESS` omitted the contract-required canonical base SHA. The launcher was invoked once; no rerun occurred. All subsequent V1 T1–T8 mathematical drafts are **[INVALID / NON-CANONICAL / DO NOT USE]** and are not canonical evidence.

Old V1 seal `ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c`: **[CONSUMED — MUST NOT BE REUSED OR REAUTHORIZED]**. Old V1 authorization: **[CONSUMED / CLOSED]**.

B4-N1 through B4-N7 and B4-CT are all **NOT ESTABLISHED**. `E6-N2` remains **[OPEN]**. The invalid drafts must not influence canonical science.

Forensic source: `cp20-e7r-b4-stage1-input-integrity-failure-20260904` @ `f1dce61f3d2ee207a50bd0f46208f49f3901f013`; package SHA-256 `71ad925b3d461e4ceb77293736cee75dfea116c012703e1308e00bc118125ab4`; forensic manifest SHA-256 `92f787e9f44625186fe4f1e78c85f601523d19a902818babe3ad78547ae10ce7`; Drive folder `1hYTCh3ilo3SfBRPePpNLBGcbQCDrPnsB` with raw read-back PASS. Canonical main contains only the forensic failure report/record, produced defective witness, manifest/hash references, and Drive persistence provenance — not invalid mathematical draft contents.

Main provenance only: accidental placeholder `c3062952ffb23754f62fd2dd6f6a6237e8b1d22c` was immediately reverted by `f5269e5ddbf610b2305fafbd90fe2b1346376103`. Compare `0c0e0e55c490278396f0b8f5033000b80725fb6c` → `f5269e5ddbf610b2305fafbd90fe2b1346376103` has net `files: []`. History was not rewritten.

## Exact next task

Code: `CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2`

Name: **Tilted / Recentered Microcanonical Fourier Cancellation — Integrity-Repair Reseal**

Stage: `STAGE_0_REPAIR_READY_NOT_DISPATCHED`

Objective: Produce a fresh Stage-0 seal for the SAME frozen B4 scientific program, with no scientific result imported from the invalid V1 Stage-1 invocation, and repair the execution launcher so that all contract-required witness fields are written and mechanically validated BEFORE T1 can begin. This is an execution-integrity repair, not a scientific route change.

V2 Stage 0 must repair the launcher/witness path before any future T1 action, including frozen-schema validation and the preregistered canonical-base witness self-tests. It must not read or reuse invalid V1 T1–T8 drafts. Any future V2 Stage 1 must run in a fresh computation session/chat uncontaminated by those drafts.

V2 Stage 0 is **NOT DISPATCHED** and was not executed by this closeout. No Stage-1 rerun, weighted/operator work, E8, or new mathematics is authorized by recovery alone.

Nothing in this closeout proves the Collatz conjecture.
