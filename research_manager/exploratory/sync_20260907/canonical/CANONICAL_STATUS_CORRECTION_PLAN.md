# Canonical status-correction plan — B4 V2 consumed authorization

Date: 2026-09-07  
Status: **PLAN ONLY — NOT EXECUTED / NOT AUTHORIZED FOR SCIENTIFIC WORK**  
Scope: correct the unsafe canonical status at `origin/main`; preserve exact producer and independent-audit evidence; do not run B4 V2, do not create a V3 seal or authorization, and do not import invalid V1 mathematical drafts.

## 1. Fixed baseline and transaction boundary

- Canonical baseline is `origin/main = 1a6f924fd86352c11f57a95b0382adaf92d15bcd` (`Finalize B4 V2 authorization handoff`).
- The local `main` pointer is stale and MUST NOT be used as an integration base. Before a future integration, fetch and confirm the server-side `refs/heads/main`; abort if it is not the expected baseline or if it moved during review.
- Use a clean, dedicated integration worktree/branch based directly on the freshly fetched `origin/main`. Do not merge the current exploratory checkout or either evidence branch wholesale.
- The canonical `active_integrator` at the baseline is `RELEASED`. A future integration must acquire a new narrow transaction lock before canonical writes:

```json
{
  "holder": "canonical-integrator-b4-v2-status-correction-20260907",
  "scope": "B4 V2 consumed-authorization status correction only: select five exact evidence artifacts, add one manager correction decision, append journal sequence 22, repair root state/handoff, rebuild/verify archive, and perform Drive/GitHub publication read-back; no Stage1/T1-T8 execution, no invalid V1 drafts, no scientific route change, no V3 seal or authorization.",
  "base_commit": "1a6f924fd86352c11f57a95b0382adaf92d15bcd",
  "acquired_at": "<transaction UTC timestamp>",
  "status": "HELD"
}
```

- Prefer a two-commit canonical transaction: (A) lock acquisition from the verified baseline, then (B) the reviewed milestone finalization that releases the lock. Immediately before finalization, verify that the branch still descends from the same fetched canonical base and that no other canonical integrator is `HELD`. In the final state set `status: RELEASED`, preserve `holder`, `scope`, `base_commit`, and `acquired_at`, and add `released_at`.
- No force push, history rewrite, reset of the dirty exploratory checkout, or reuse of the old transaction holder is permitted.

## 2. Exact evidence selection

Both source heads have merge-base exactly `1a6f924fd86352c11f57a95b0382adaf92d15bcd`. Copy the following five paths byte-for-byte by object/path selection, then independently verify both Git blob and SHA-256. Do not cherry-pick or merge the complete branches.

### Producer evidence from `04a66e41864d1d530ead63b1faeaf122048e3069`

1. `research_manager/results/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE0/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE1_INPUT_INTEGRITY_FAILURE.json`
   - Git blob SHA-1: `2e74de7161532fd10dd2cf1893eacf19dda173e9`
   - SHA-256: `1997355b8cc2c505df44175b2467598b0e96ded41ab0e45bf9c4d5b6e06ec30a`
   - Load-bearing contents: status `[B4 V2 STAGE1 INPUT INTEGRITY FAILURE]`; reason `frozen dependency blob mismatch at Phase A: CURRENT_RESEARCH_STATE.json`; `authorization_consumed: true`; `T1_T8: NOT_EXECUTED`; timestamp `2026-09-05T07:17:52.681686+00:00`.

2. `research_manager/results/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE0/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE1_INTEGRITY_STDOUT.txt`
   - Git blob SHA-1: `e3d138a494737151eef85f44a9018aa1427e4c74`
   - SHA-256: `fad5d23d92ba219aeb6057aaa6c70ed798d79b1229f9a31a261cbcbb1f9d5f34`
   - Load-bearing content: the same pre-mathematics frozen-dependency failure line.

Exclude `.github/workflows/b4v2-stage1-once.yml`: it is execution machinery, is unnecessary for evidentiary closure, and must not create an accidental rerun surface. Exclude the branch's intermediate `.stage1_b4v2/*` history and all other branch commits/files.

### Independent audit from `8fb8d68d3c131d6e11721fd629f1ea879102aedc`

3. `bagimsiz-denetim/e7r-b4-v2-preexec-zero-trust-audit-20260905/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_PREEXEC_ZERO_TRUST_AUDIT_2026-09-05.md`
   - Git blob SHA-1: `ea54d835951de4c2026f5fb12973360d9d8e5298`
   - SHA-256: `81f8908bc15b2b03c9db4f214831b7c73a1116a3b6d50e003597a3e0575ad0c7`

4. `bagimsiz-denetim/e7r-b4-v2-preexec-zero-trust-audit-20260905/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_PREEXEC_ZERO_TRUST_AUDIT_2026-09-05.json`
   - Git blob SHA-1: `fed71aadac38b418d163f78d0cdba20dfcef0fc7`
   - SHA-256: `efda35345d58ee1a0109dbb47b25ef4001c894d449c536ce62ac4ac56117bd1e`

5. `bagimsiz-denetim/e7r-b4-v2-preexec-zero-trust-audit-20260905/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_PREEXEC_ZERO_TRUST_AUDIT_SHA256SUMS_2026-09-05.txt`
   - Git blob SHA-1: `5e55a2d695d3c611b5cc0e08457000ff897dc239`
   - Its two manifested hashes are exactly the MD and JSON SHA-256 values above.

The audit verdict is `[AUDIT FAIL — DO NOT EXECUTE B4 V2 STAGE1]`. The audit records: real sealed entrypoint invoked; RUN_WITNESS not created; PRE_T1_GATE not reached; T1 START not reached; T1–T8 mathematics not executed; the sole once-only authorization consumed. Its root-cause evidence binds sealed expected blob `3ba90bbf9e91ddc600235a38a800db90b03a07e0` from `8d274095b0e1acbe1fad0a73ef6a5293364902fc` against Phase-A actual blob `aa8daf546826853b720356ff96530f0b78ec197d` at `34ac0dbeb8c0ae2fddab706680f1682412b00786`.

## 3. New manager decision

Create a small canonical decision, proposed path:

`research_manager/decisions/CP20_TASK8B3_E7R_B4_V2_STAGE1_INPUT_INTEGRITY_FAILURE_STATUS_CORRECTION_2026-09-07.json`

It must state only:

- accepted evidence heads and the five exact artifact hashes above;
- status `[B4 V2 STAGE1 INPUT INTEGRITY FAILURE — AUTHORIZATION CONSUMED / CLOSED]`;
- the failure is mechanical/integrity-contract configuration, with `NO SCIENTIFIC CHANGE`;
- `real_entrypoint_invoked: true`, `RUN_WITNESS: false`, `PRE_T1_GATE: false`, `T1_START: false`, `T1_T8_executed: false`;
- B4-N1…B4-N7 and B4-CT remain `NOT ESTABLISHED`; E6-N2 remains `[OPEN]`;
- seal `11456b7d6f673e5cab6079850731cbda70373b77e4e0f532089d6783fd16c78e` and authorization commit `f8d778a2113922e3bbb14c86ee2fa5359cee28ea` are consumed and MUST NOT be invoked/reused/re-authorized;
- no invalid V1 draft is accepted or imported;
- no V3 task, seal, execution, or authorization is created by this decision;
- exact next action is administrative stop: await a separate explicit manager transaction, if desired, to design and independently audit a new repair/reseal. This status correction itself dispatches nothing.

## 4. Proposed `CURRENT_RESEARCH_STATE.json` correction

Retain all established scientific checkpoints and old evidence. Apply only the following safety/status changes:

1. `active_task.stage` → `STAGE_1_INPUT_INTEGRITY_FAILURE_AUTHORIZATION_CONSUMED_CLOSED`; retain task code and `scientific_route_change: false`; revise the objective to say the V2 execution-integrity attempt is closed without mathematics.
2. `b4_v2_reseal.stage` and `b4_v2_stage0.stage` → the same closed status.
3. In `b4_v2_stage0`:
   - retain `authorization_count: 1` as the historical creation count;
   - set `available_authorization_count: 0`, `authorization_consumed: true`, `stage1_authorized: false`, `stage1_authorization_status: "[CONSUMED / CLOSED — MUST NOT REUSE]"`;
   - retain `stage1_executed: false` and `T1_T8_executed: false`;
   - add the real invocation trace (`real_entrypoint_invoked: true`, `run_witness_created: false`, `pre_t1_gate_reached: false`, `t1_start_reached: false`, `mathematics_executed: false`), failure reason/timestamp, producer head `04a66e4…`, audit head `8fb8d68…`, and audit verdict.
4. Add `audited_evidence.e7r_b4_v2_preexec_failure` with both evidence heads, the five artifact identities, verdict, consumed seal/authorization tuple, mechanical root cause, and explicit `scientific_state_changed: false`.
5. Add the five canonical paths plus the new manager-decision path under `documents` with unambiguous names (`b4_v2_stage1_failure_record`, `b4_v2_stage1_failure_stdout`, `b4_v2_preexec_audit_report`, `b4_v2_preexec_audit_json`, `b4_v2_preexec_audit_manifest`, `b4_v2_status_correction_decision`). Keep the historical authorization decision path as provenance, but it must no longer be labelled active; rename its key to `historical_consumed_authorization_decision` or add a clear consumed-status companion field.
6. Replace `next_action` with an unauthorizing stop object, for example:

```json
{
  "authorized_stage": null,
  "authorization_available": false,
  "executed_in_this_transaction": false,
  "instruction": "Do not execute or rerun B4 V2 Stage 1. Its sole once-only authorization was consumed by the 2026-09-05 real invocation, which failed before RUN_WITNESS, PRE_T1_GATE, T1 START, or T1-T8 mathematics. Await a separate explicit manager transaction for any future repair/reseal; no V3 is authorized or dispatched.",
  "prohibited": [
    "reuse or reauthorization of the consumed V2 tuple",
    "B4 V2 Stage1 execution or rerun",
    "invalid V1 drafts",
    "claim that T1-T8 executed",
    "claim any B4-N1...B4-N7 or B4-CT result",
    "V3 seal, authorization, or execution without a separate explicit manager transaction",
    "E8",
    "unauthorized weighted/operator work"
  ]
}
```

7. Append matching entries to `prohibited_inferences`: consumed V2 authorization cannot be reused; the invocation produced no mathematics; no V3 authorization exists; failure is not a scientific result.
8. Preserve `scientific_checkpoint` unchanged except, if desired, add a governance-only closed item clearly labelled as such; do not add a proved/false mathematical statement.
9. The legacy top-level `stage1_authorization` currently names the V1 seal `ec26…` yet says `STAGE_1_AUTHORIZED_NOT_EXECUTED`. Resolve this safety ambiguity narrowly: mark it explicitly as historical B4 V1, `status: "[CONSUMED / CLOSED]"`, `stage1_authorized: false`, and keep `stage1_executed: false`. Do not repurpose that legacy block for V2.
10. Update `updated_at` to the transaction timestamp. Update `active_integrator` as described in section 1 and release it only at finalization.
11. Do not manually invent archive hashes in `integrity.archive_members`; rebuild deterministically, then populate only values produced by the archive tooling and independently rechecked.

## 5. Proposed `START_HERE_CURRENT_HANDOFF.md`

Replace the unsafe execution handoff with a short failure closeout that records:

- canonical task and closed status;
- the original Phase-A, Phase-B, seal, contract, config, and manifest hashes as forensic identity only;
- producer evidence head/path/hash and independent audit head/path/hash;
- exact trace: real invocation YES; RUN_WITNESS NO; PRE_T1_GATE NO; T1 START NO; T1–T8 NOT EXECUTED; authorization CONSUMED;
- mechanical root cause and `NO SCIENTIFIC CHANGE`;
- B4-N1…B4-N7/B4-CT `NOT ESTABLISHED`, E6-N2 `[OPEN]`, Collatz not proved;
- prominent `DO NOT EXECUTE OR REUSE THE V2 TUPLE` warning;
- exact next action: no execution authorized; await a separate explicit manager repair/reseal transaction. Explicitly state `V3 NOT AUTHORIZED / NOT DISPATCHED`;
- invalid V1 T1–T8 drafts remain `[INVALID / NON-CANONICAL / DO NOT USE]`.

Delete every imperative that tells a reader to execute V2 Stage 1.

## 6. Append-only journal event

Append exactly one new UTF-8/LF JSON line; do not edit sequences 1–21. The baseline tail is sequence 21, and its exact line SHA-256 (excluding newline) is:

`f00f80b4b0f394b4c08711e03271e519974ef43ede4094fc82b030e3416b6f72`

Proposed event shape (serialize as one deterministic compact JSON line; substitute only the actual transaction timestamp and final decision SHA-256 if recorded):

```json
{"T1_T8_executed":false,"active_stage":"STAGE_1_INPUT_INTEGRITY_FAILURE_AUTHORIZATION_CONSUMED_CLOSED","authorization_available":false,"authorization_consumed":true,"event":"B4_V2_STAGE1_INPUT_INTEGRITY_FAILURE_STATUS_CORRECTED","evidence":{"audit_commit":"8fb8d68d3c131d6e11721fd629f1ea879102aedc","audit_report_sha256":"81f8908bc15b2b03c9db4f214831b7c73a1116a3b6d50e003597a3e0575ad0c7","audit_verdict":"[AUDIT FAIL — DO NOT EXECUTE B4 V2 STAGE1]","failure_reason":"frozen dependency blob mismatch at Phase A: CURRENT_RESEARCH_STATE.json","invocation_commit":"04a66e41864d1d530ead63b1faeaf122048e3069","invocation_failure_sha256":"1997355b8cc2c505df44175b2467598b0e96ded41ab0e45bf9c4d5b6e06ec30a","mathematics_executed":false,"pre_t1_gate":false,"real_entrypoint_invoked":true,"run_witness":false,"scientific_state_changed":false,"stdout_sha256":"fad5d23d92ba219aeb6057aaa6c70ed798d79b1229f9a31a261cbcbb1f9d5f34","t1_start":false},"next_action":"Do not execute or rerun the consumed B4 V2 authorization; await a separate explicit manager transaction for any future repair/reseal. No V3 is authorized or dispatched.","previous_entry_sha256":"f00f80b4b0f394b4c08711e03271e519974ef43ede4094fc82b030e3416b6f72","schema":"COLLATZ_RESEARCH_JOURNAL_V1","sequence":22,"task":"CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2","timestamp_utc":"<transaction UTC timestamp>"}
```

## 7. Archive, verification, persistence, and publication order

1. Fresh-fetch and pin the actual remote `main`; require the expected base or restart review on the new base.
2. Create a clean dedicated worktree/branch from that remote object; acquire the narrow `active_integrator` lock. Confirm no other held lock/transaction and no unrelated working-tree content.
3. Select the five exact blobs by commit/path. Recompute all five Git blob IDs and SHA-256 values; verify the audit manifest 2/2; verify producer JSON parses and stdout exactly agrees.
4. Independently inspect the two source commit ancestry/diffs; confirm no workflow, invalid V1 draft, `.stage1_b4v2` residue, exploratory result, or unrelated branch content entered the candidate tree.
5. Write and review the manager correction decision, append journal sequence 22 with the recomputed previous-line hash, update `CURRENT_RESEARCH_STATE.json`, and update `START_HERE_CURRENT_HANDOFF.md`.
6. Validate JSON and JSONL; independently recompute the journal chain; grep all root/current handoff material for stale actionable phrases such as `STAGE_1_AUTHORIZED_NOT_EXECUTED`, `Execute CP20_TASK8B3...V2 Stage 1`, and `[AUTHORIZED ONCE — NOT EXECUTED]`. Historical sealed/authorization records may retain historical text, but current root state/handoff must not present it as live authority.
7. Rebuild `Collatz_Research_Archive_CURRENT.zip` using `python tools/build_current_archive.py`; update `CURRENT_ARCHIVE_BUILD.json`; verify deterministic repeat build, member uniqueness/order/CRC, size limit, and inclusion/hash of the five evidence files, decision, journal tail, state, and handoff.
8. Run `python tools/verify_handoff.py` and require exact `HANDOFF VERIFICATION: PASS`. Also run any archive extraction/read-back verifier prescribed by the repository. Failure stops the transaction; it does not authorize a workaround execution.
9. Release `active_integrator` in the final milestone commit only after all local checks pass. Confirm the final staged path set is narrow and expected; confirm no scientific program bytes changed.
10. Persist the completed milestone/archive to the designated Drive location and perform raw-byte read-back. Record IDs, archive SHA-256, member count, and explicit PASS/FAIL. A connector failure must be recorded as blocked, never as success.
11. Immediately fetch remote `main` again. If it moved, stop and rebase/review non-destructively; never force. Push only after the base/concurrency check passes.
12. GitHub read-back: resolve server-side `refs/heads/main`, read back the five evidence blobs, manager decision, root state, handoff, journal tail, and `CURRENT_ARCHIVE_BUILD.json`; compare hashes/contents with the reviewed transaction.
13. Report final canonical commit, current archive SHA-256/member count, active closed status, exact no-execution next action, Drive read-back verdict, GitHub read-back verdict, and released lock.

## 8. Zero-trust review checklist

- [ ] Server-side `main` freshly verified; no stale local-main base used.
- [ ] Both evidence heads descend directly from/merge-base to the pinned canonical baseline.
- [ ] Exactly five selected evidence paths; all Git blob IDs and SHA-256 values match this plan.
- [ ] Audit SHA256SUMS verifies 2/2 against raw selected bytes.
- [ ] Producer JSON and stdout agree on failure reason and pre-mathematics stop.
- [ ] Workflow and temporary `.stage1_b4v2` material excluded.
- [ ] No invalid V1 Stage-1 mathematical draft read, copied, summarized, or used.
- [ ] Historical creation count remains one; available authorization count is zero.
- [ ] V2 seal/authorization tuple marked consumed and non-reusable everywhere current state is read.
- [ ] T1–T8 remain `NOT EXECUTED`; no B4-N1…B4-N7/B4-CT claim promoted.
- [ ] E6-N2 remains `[OPEN]`; no Collatz-proof claim.
- [ ] Failure classified mechanical/governance, not mathematical.
- [ ] No V3 seal, authorization, dispatch, or implied permission created.
- [ ] Journal is append-only, sequence 22, and previous-entry hash is independently verified from raw sequence-21 bytes.
- [ ] Root state, handoff, and decision agree on the exact next action.
- [ ] Active-integrator holder/scope/base are exact; lock is released only in the final milestone state.
- [ ] Archive deterministic rebuild/read-back passes and contains the corrected canonical surface.
- [ ] `tools/verify_handoff.py` returns exact PASS.
- [ ] Staged-path review shows no unrelated tracked or exploratory files.
- [ ] Drive raw-byte read-back passes or is explicitly reported blocked.
- [ ] GitHub server-side read-back passes; no force push/history rewrite occurred.

## 9. Non-goals

This transaction does not integrate prefix-bridge work, 2026-09-07 exploratory mathematics, publication/JNT branches, launcher-repair proposals, or any new theorem. It does not fix or reseal the B4 mechanism. It only makes canonical recovery truthful and safe: the V2 once-only authorization is consumed, no T1–T8 mathematics ran, and there is currently no authorized next execution.
