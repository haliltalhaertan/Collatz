# CP20_TASK8B3_E7R_B4 — V1 INPUT-INTEGRITY FAILURE CANONICAL CLOSEOUT

Closeout verdict: **[B4 STAGE1 INPUT INTEGRITY FAILURE]**.

The old authorized seal `ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c` is **[CONSUMED — MUST NOT BE REUSED OR REAUTHORIZED]**. The old V1 authorization at `0c0e0e55c490278396f0b8f5033000b80725fb6c` is **[CONSUMED / CLOSED]**. The canonical contract remains `3d9fd4c0c029c135b86c43377aa414c87704f5e6c3dd4a008fa621f3b4f1185e` for provenance only.

The contract required the pre-T1 `RUN_WITNESS` to contain the canonical base SHA. The produced witness omitted that required field. The launcher was invoked exactly once; no rerun occurred. Some T1–T8 draft work occurred before detection, but all such mathematical outputs are **[INVALID / NON-CANONICAL / DO NOT USE]** and are not imported by this integration.

## Scientific state

- B4 V1 Stage 0: **[FROZEN — SCIENTIFIC PROGRAM PRESERVED]**
- B4 V1 Stage 1: **[INPUT INTEGRITY FAILURE — INVALID / NON-CANONICAL]**
- B4-N1: NOT ESTABLISHED
- B4-N2: NOT ESTABLISHED
- B4-N3: NOT ESTABLISHED
- B4-N4: NOT ESTABLISHED
- B4-N5: NOT ESTABLISHED
- B4-N6: NOT ESTABLISHED
- B4-N7: NOT ESTABLISHED
- B4-CT: NOT ESTABLISHED
- E6-N2: **[OPEN]**

The invalid drafts must not influence canonical science.

## Forensic evidence

Failure branch `cp20-e7r-b4-stage1-input-integrity-failure-20260904` @ `f1dce61f3d2ee207a50bd0f46208f49f3901f013`. Failure package SHA-256 `71ad925b3d461e4ceb77293736cee75dfea116c012703e1308e00bc118125ab4`. Forensic manifest SHA-256 `92f787e9f44625186fe4f1e78c85f601523d19a902818babe3ad78547ae10ce7`. Drive folder `1hYTCh3ilo3SfBRPePpNLBGcbQCDrPnsB`; raw read-back PASS. Only the integrity-failure report, failure record, produced witness, exact manifest/hash references, and Drive persistence record are canonicalized. The invalid package contents are not imported to main.

## Main-history provenance

The accidental placeholder `c3062952ffb23754f62fd2dd6f6a6237e8b1d22c` was immediately reverted by `f5269e5ddbf610b2305fafbd90fe2b1346376103`. Compare `0c0e0e55c490278396f0b8f5033000b80725fb6c` → `f5269e5ddbf610b2305fafbd90fe2b1346376103` has net `files: []`. History is preserved and not rewritten.

## Next task

`CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2` — **Tilted / Recentered Microcanonical Fourier Cancellation — Integrity-Repair Reseal**

Stage: `STAGE_0_REPAIR_READY_NOT_DISPATCHED`.

Objective: Produce a fresh Stage-0 seal for the SAME frozen B4 scientific program, with no scientific result imported from the invalid V1 Stage-1 invocation, and repair the execution launcher so that all contract-required witness fields are written and mechanically validated BEFORE T1 can begin. This is an execution-integrity repair, not a scientific route change.

V2 Stage 0 is not executed or dispatched by this closeout.

Nothing in this closeout proves the Collatz conjecture.
