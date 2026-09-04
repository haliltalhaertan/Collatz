# CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2 — STAGE 1 EXECUTION INTEGRITY AND OUTPUT CONTRACT

This contract is part of the repaired V2 Stage-0 seal. It MUST be canonicalized in Phase A before any Stage-1 authorization is created.

## Two-commit authorization semantics
Two distinct Git commit identities are required:

- `canonical_stage0_base_sha`: the Phase-A canonical commit containing the accepted Stage-0 artifacts and this execution contract. It is known before authorization exists.
- `authorization_commit_sha`: the later Phase-B commit containing the Stage-1 authorization decision and canonical state `STAGE_1_AUTHORIZED_NOT_EXECUTED`.

The authorization JSON at Phase B MUST contain:
- `authorized_v2_seal_sha256`
- `v2_contract_sha256`
- `canonical_stage0_base_sha`
- `stage = STAGE_1_AUTHORIZED_NOT_EXECUTED`

The authorization JSON MUST NOT be required to contain `authorization_commit_sha` and MUST NOT be required to equal the SHA of the commit that contains it. `authorization_commit_sha` is supplied to the computation only after Phase B exists.

## Runtime inputs
Future Stage-1 integrity invocation MUST include:
- `--canonical-stage0-base-sha <PHASE_A_SHA>`
- `--authorization-commit-sha <PHASE_B_SHA>`
- `--authorized-seal-sha256 <SEAL_SHA>`
- `--contract-sha256 <CONTRACT_SHA>`

`stage0_source_base_sha = 8d274095b0e1acbe1fad0a73ef6a5293364902fc` remains the historical source base for this Stage-0 program.

## Required pre-T1 Git validation
Before T1, the launcher MUST verify:
1. both `canonical_stage0_base_sha` and `authorization_commit_sha` resolve to commits;
2. `stage0_source_base_sha` is an ancestor of `canonical_stage0_base_sha`;
3. `canonical_stage0_base_sha` is an ancestor of `authorization_commit_sha`;
4. `authorization_commit_sha` is an ancestor of the Stage-1 working HEAD;
5. the authorization JSON is readable at `authorization_commit_sha`;
6. that JSON names the exact authorized V2 seal SHA;
7. that JSON names the exact V2 contract SHA;
8. that JSON names the exact `canonical_stage0_base_sha`;
9. that JSON stage is `STAGE_1_AUTHORIZED_NOT_EXECUTED`;
10. `CURRENT_RESEARCH_STATE.json` at `authorization_commit_sha` contains an `active_task` object whose authoritative `active_task.stage` equals `STAGE_1_AUTHORIZED_NOT_EXECUTED`; any optional legacy stage alias, if present, must agree with `active_task.stage` and may never override it;
11. the canonical Stage-0 load-bearing artifacts and contract at `canonical_stage0_base_sha` match the exact sealed Git blob IDs and SHA-256 hashes recorded by the Stage-0 config.

No authorization JSON field is required to equal the commit SHA that contains the JSON.


## Authoritative canonical state path
The authoritative Phase-B canonical stage is read from:

`CURRENT_RESEARCH_STATE.json["active_task"]["stage"]`

and MUST equal:

`STAGE_1_AUTHORIZED_NOT_EXECUTED`

`active_task` MUST exist and MUST be an object. `active_task.stage` MUST exist. No undocumented top-level `active_stage` field is required. The launcher MUST NOT silently fall back to any alternate schema. If an optional legacy alias such as top-level `active_stage` or `continuity.active_stage` exists, it is a consistency check only; any conflict with `active_task.stage` is an integrity failure before T1.


## Required pre-T1 order
1. Parse manager-authorized runtime inputs.
2. Verify seal SHA, manifest, all member hashes, ZIP membership uniqueness/order and CRC, dependency hashes, and all blocked-seal firewalls.
3. Verify declared Stage-1 output absence.
4. Validate the two-commit authorization chain and Phase-A canonical Stage-0 artifacts.
5. Atomically write the complete RUN_WITNESS.
6. Validate that witness using the separately sealed V2 witness validator.
7. On any mismatch, write `[B4 V2 STAGE1 INPUT INTEGRITY FAILURE]` and terminate before mathematics.
8. Only after all validations pass, write `...V2_STAGE1_PRE_T1_GATE.json` with status PASS.
9. Append `PRE_T1_GATE PASS` to the execution ledger.
10. Only then may a T-stage ledger append `T1 START`.

There is no permitted code path from invocation to T1 START without PRE_T1_GATE PASS.

## Witness semantics
The complete witness MUST contain:
- `stage0_source_base_sha`
- `canonical_stage0_base_sha`
- `authorization_commit_sha`
- `canonical_base_sha`
- `authorized_seal_sha256`
- `contract_sha256`
- `config_sha256`
- `execution_count_claim`
- `output_absence_precheck`
- `utc_timestamp`
- `pid_or_session_identifier`
- `exact_entrypoint`
- `preflight_status`
- task and task version.

Define `canonical_base_sha = authorization_commit_sha`. `canonical_stage0_base_sha` and `authorization_commit_sha` are distinct 40-hex commit identities. No required witness field may be missing, null, empty, or malformed.

## PRE_T1 gate
PRE_T1_GATE PASS MUST contain at minimum status, `canonical_stage0_base_sha`, `authorization_commit_sha`, `canonical_base_sha`, `run_witness_sha256`, `authorized_seal_sha256`, `contract_sha256`, `config_sha256`, and UTC timestamp. No T1 START may precede this gate.

## Blocked seal firewall
The following seals are permanently rejected for future authorization:
- consumed V1 seal `ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c`;
- V2 candidate `2e6d9e1d833fc8dabf02c0e970ccfb06fc86e4cbc9e85cd2e0e61ae3611879ea`;
- V2 candidate `66ac975940abb29a1248079ea6e03643ded966da296cf33deb7c7a0f5fa60eac` with authorization-base self-reference defect.
- V2 candidate `06768aebd233c874fbb2103f3f3ccadca7db5ae76c7f5fb051ab982cf737012f` with canonical-state-path mismatch.

## One-run discipline
The actual V2 Stage-1 entrypoint may be invoked once only under a future explicit manager authorization. A failed real invocation consumes that authorization. Synthetic integrity tests do not invoke the actual Stage-1 entrypoint and execute no mathematics.

## Ledger and audit stop
Ledger order remains PRE_T1_GATE PASS, then T1 START, terminal T1 status, T2 START, and so on. No T-stage record may precede the gate.

Immediate independent-audit stop remains mandatory at genuinely load-bearing B4-N5, B4-N6, B4-N7/E6-N2, load-bearing B4-CT, or an exact downstream-dependent leading cancellation/non-cancellation theorem. All post-stop later T stages remain NOT_EXECUTED.

## Scientific firewall
This repair changes authorization/integrity mechanics only. T1–T8, F1–F10, T7-F1–T7-F5, target normal form, p_*, sigma_*^2, arc split, outcome ladder and audit-stop rules are scientifically unchanged. Invalid V1 Stage-1 mathematical drafts are forbidden inputs.

This Stage-0 contract does not authorize or execute Stage 1, and proves nothing about the Collatz conjecture.
