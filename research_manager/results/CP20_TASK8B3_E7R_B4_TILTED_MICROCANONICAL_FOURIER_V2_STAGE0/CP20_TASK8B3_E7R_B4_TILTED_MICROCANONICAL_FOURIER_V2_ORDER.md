# CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2 — STAGE 0 REPAIR ORDER

Status: **STAGE 0 REPAIR ONLY — NO STAGE 1**

This V2 package is an execution-integrity reseal of the canonical V1 Stage-0 scientific program. It performs no B4 mathematics and establishes none of B4-N1…B4-N7, B4-CT, or E6-N2.

## Contamination barrier
Permitted sources are canonical scientific state on main, canonical V1 Stage-0 scientific-program artifacts, the canonical V1 integrity-failure closeout/forensic integrity evidence, the defective produced RUN_WITNESS, and the mechanical launcher defect. Invalid V1 T1–T8 mathematical drafts, theorem drafts, numerical conclusions, and draft-preservation-only files are forbidden.

## Frozen science
T1–T8, F1–F10, T7-F1–T7-F5, target, p_*, sigma_*^2, Fourier convention, deterministic arc split, and outcome ladder are unchanged.

## Mechanical repair
1. Separate `stage0_source_base_sha` from future `authorized_execution_base_sha`.
2. Require a complete RUN_WITNESS with `canonical_base_sha == authorized_execution_base_sha`.
3. Validate the witness with a separately sealed validator.
4. Require a PRE_T1_GATE PASS artifact before any T1 START.
5. Bind future authorization to exact V2 seal SHA, contract SHA, and execution-base SHA.
6. Refuse the consumed V1 seal `ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c`.
7. Preserve one-real-run discipline and append-only execution ledger.

## Stage-0 allowed execution
Only witness/schema self-tests, static control-flow checks, seal/manifest/hash checks, deterministic comparisons, and contamination-diff classification are executed.

## Stop
Stage 0 stops after reseal/persistence. Stage 1 and T1–T8 remain NOT EXECUTED.
