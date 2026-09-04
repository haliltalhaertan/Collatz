# CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2 — STAGE 0 INTEGRITY-REPAIR RESEAL HANDOFF

Status: `STAGE_0_REPAIR_READY_NOT_DISPATCHED`. **NOT DISPATCHED.**

Objective: Produce a fresh Stage-0 seal for the SAME frozen B4 scientific program, with no scientific result imported from the invalid V1 Stage-1 invocation, and repair the execution launcher so that all contract-required witness fields are written and mechanically validated BEFORE T1 can begin. This is an execution-integrity repair, not a scientific route change.

This is an execution-integrity repair, not a scientific route change.

The future V2 Stage-0 task must:

1. start from the post-failure canonical main produced by the V1 closeout;
2. preserve the B4 scientific target and frozen T1–T8 / F1–F10 program unless an independently discovered pre-execution defect requires an explicit new seal;
3. NOT read or reuse invalid V1 T1–T8 mathematical drafts;
4. use the V1 forensic failure only to identify the mechanical launcher defect;
5. make `RUN_WITNESS` contain at minimum `canonical_base_sha`, `authorized_seal_sha256`, `config_sha256`, `execution_count_claim`, `output_absence_precheck`, UTC timestamp, PID/session identifier, and exact entrypoint identity;
6. BEFORE any T1 action, mechanically validate the completed witness against a frozen schema;
7. abort before mathematics if any required field is missing, empty, malformed, or inconsistent;
8. preregister a Stage-0 witness self-test on a synthetic/test destination proving: missing `canonical_base_sha` => FAIL; wrong `canonical_base_sha` => FAIL; correct `canonical_base_sha` => PASS;
9. keep the actual Stage-1 launcher once-only;
10. require a new V2 seal and fresh authorization for every source/launcher change.

Contamination control: future V2 Stage 1 must run in a fresh computation session/chat that has not seen invalid V1 T1–T8 mathematical drafts. It may read canonical scientific inputs, the V1 integrity-failure forensic record, the produced defective witness, and the statement of the mechanical defect. It must NOT read invalid V1 mathematical draft outputs.

Do not begin Stage 1, weighted/operator work, or E8 from this handoff alone.
