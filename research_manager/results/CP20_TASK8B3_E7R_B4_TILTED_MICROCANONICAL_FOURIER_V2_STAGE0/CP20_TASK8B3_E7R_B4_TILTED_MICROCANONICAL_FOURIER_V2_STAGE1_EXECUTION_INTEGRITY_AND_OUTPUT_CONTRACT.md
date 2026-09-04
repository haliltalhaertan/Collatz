# CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2 — STAGE 1 EXECUTION INTEGRITY AND OUTPUT CONTRACT

This contract is part of the V2 seal. It MUST be canonicalized before any V2 Stage-1 authorization.

## Authorization binding
Future manager authorization MUST explicitly name:
- `authorized_v2_seal_sha256`
- `v2_contract_sha256`
- `authorized_execution_base_sha`

The future computation session must receive all three and the exact Stage-1 invocation must include all three. No future SHA that does not yet exist is frozen by Stage 0.

## Base semantics
`stage0_source_base_sha = 8d274095b0e1acbe1fad0a73ef6a5293364902fc`.
`authorized_execution_base_sha` is a future manager-supplied canonical commit/ref.
Every RUN_WITNESS MUST satisfy `canonical_base_sha == authorized_execution_base_sha`.

## Required pre-T1 order
1. Parse manager-authorized runtime inputs.
2. Verify seal SHA, manifest, all member hashes, ZIP membership uniqueness/order and CRC, dependency hashes, and old-seal blacklist.
3. Verify declared Stage-1 output absence.
4. Validate the future execution base with Git.
5. Atomically write the complete RUN_WITNESS.
6. Validate that witness using the separately sealed V2 witness validator.
7. On any mismatch, write `[B4 V2 STAGE1 INPUT INTEGRITY FAILURE]` and terminate before mathematics.
8. Only after all validations pass, write `...V2_STAGE1_PRE_T1_GATE.json` with status PASS.
9. Append `PRE_T1_GATE PASS` to the execution ledger.
10. Only then may a T-stage ledger append `T1 START`.

There is no permitted code path from invocation to T1 START without PRE_T1_GATE PASS.

## Future execution-base validation
Before Stage-1 mathematics, Git must verify:
- `authorized_execution_base_sha` resolves to a commit;
- it is an ancestor of the fresh Stage-1 working branch HEAD;
- `research_manager/decisions/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE1_AUTHORIZATION.json` is readable at that ref;
- that authorization names the same V2 seal SHA;
- it names the same V2 contract SHA;
- it names the same authorized execution base;
- canonical state at/after that authorization says `STAGE_1_AUTHORIZED_NOT_EXECUTED`.

Any failure produces `[B4 V2 STAGE1 INPUT INTEGRITY FAILURE]` and stops before T1. No repair is permitted under the same authorization.

## One-run discipline
The actual V2 Stage-1 entrypoint may be invoked once only. A failed real invocation consumes that authorization. No in-place repair or rerun is allowed. A new source byte requires a new Stage-0 seal and fresh authorization.

Synthetic witness-validator self-tests do NOT count as Stage-1 execution because they do not invoke the actual Stage-1 entrypoint and perform no mathematics.

## Witness
The complete witness is required to contain task, task_version, stage0_source_base_sha, canonical_base_sha, authorized_execution_base_sha, authorized_seal_sha256, contract_sha256, config_sha256, execution_count_claim, output_absence_precheck, utc_timestamp, pid_or_session_identifier, exact_entrypoint, and preflight_status. No required field may be missing, null, empty, or malformed.

`canonical_base_sha` MUST equal `authorized_execution_base_sha`.
`execution_count_claim` MUST equal 1.
`output_absence_precheck` and `preflight_status` MUST equal PASS.

## Old V1 seal firewall
The consumed V1 SHA
`ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c`
is permanently blacklisted as a V2 authorized seal and must be rejected.

## Ledger and audit stop
Ledger order is PRE_T1_GATE PASS, then T1 START, terminal T1 status, T2 START, and so on. No T-stage record may precede the gate.

Immediate independent-audit stop remains mandatory at:
- genuinely load-bearing B4-N5;
- B4-N6;
- B4-N7/E6-N2;
- load-bearing B4-CT;
- an exact downstream-dependent leading cancellation/non-cancellation theorem.

All post-stop later T stages must be recorded as NOT_EXECUTED.

## Scientific firewall
The V2 launcher and integrity tools perform no B4 mathematics. T1–T8, F1–F10, T7-F1–T7-F5, target and arcs remain the frozen V1 Stage-0 program. Invalid V1 Stage-1 mathematical drafts are forbidden inputs.

## Final persistence
Operational Stage 1, if ever authorized later, is not complete until its result is hashed/manifested, ZIP membership/uniqueness/CRC is verified, Drive persistence and raw read-back SHA verification pass, GitHub persistence/read-back pass, and exact commit/package/manifest identities are recorded.

This Stage-0 contract does not authorize or execute Stage 1.
