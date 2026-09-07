# Git synchronization map — 2026-09-07

Snapshot time: `2026-09-07T13:39:44+03:00` (Europe/Istanbul)

## Scope and evidentiary limit

This is a read-only Git map. No fetch, checkout, branch creation, reset, merge, cherry-pick, push, or force operation was performed while preparing it. “Remote” below therefore means the locally stored `refs/remotes/origin/*` snapshot, not a fresh server-side enumeration. One concurrent push was nevertheless directly visible in the remote-tracking reflog during the inspection and is recorded below.

This document makes no claim about Drive state.

## Executive state

- Canonical remote-tracking head: `origin/main = 1a6f924fd86352c11f57a95b0382adaf92d15bcd` (`Finalize B4 V2 authorization handoff`). `origin/HEAD` points to the same commit.
- Local `main = 9119a39957705f53060c380acf3e8f4dd6609565`; it is an ancestor of `origin/main` and is **13 commits behind, 0 ahead**. It is a stale local pointer and must not be used as the integration base.
- Checked-out branch: `codex/prefix-bridge-20260906-persistence = d544bf2d072dd442c3f6528d87d9f7c4f86c23ce`.
- Its upstream now matches exactly: `origin/codex/prefix-bridge-20260906-persistence = d544bf2d072dd442c3f6528d87d9f7c4f86c23ce`. Relative to canonical `origin/main`, the prefix branch is `0 behind / 2 ahead`.
- The prefix remote-tracking ref changed concurrently during this audit: it moved by push from `f5f9d613be10cd22e98097fe5285442819291692` at `13:18:34 +03:00` to `d544bf2d072dd442c3f6528d87d9f7c4f86c23ce` at `13:35:34 +03:00`. The latter is the final ref observed for this snapshot.
- Tracked working-tree and index diffs were both empty at the snapshot. Untracked material existed under the two 20260907 research directories, the shared sync directory, and one new prefix persistence-completion note; these are not part of the checked-out commit merely because they are visible in the working tree.

## Canonical-main lineage and stale root state

`origin/main` contains the accepted B4 V2 Stage-0 canonicalization and the once-only authorization lineage ending at `1a6f924`. It does **not** contain the later Stage-1 invocation-failure evidence or the independent pre-execution audit failure.

Consequently the following root files at `origin/main` are stale relative to later preserved evidence branches:

- `CURRENT_RESEARCH_STATE.json` still records `STAGE_1_AUTHORIZED_NOT_EXECUTED`, says the authorization is available, and gives execution as the next action.
- `START_HERE_CURRENT_HANDOFF.md` likewise instructs the once-only B4 V2 Stage-1 execution.
- `CURRENT_ARCHIVE_BUILD.json` is a 2026-09-04 archive snapshot and cannot represent the later 2026-09-05 failure/audit or 2026-09-07 exploratory persistence branches.

The later evidence says the real V2 launcher was invoked once, stopped before T1 because `CURRENT_RESEARCH_STATE.json` had a frozen-dependency blob mismatch at Phase A, consumed the once-only authorization, and executed none of T1–T8. Therefore the root “execute next” instruction must be treated as unsafe/stale until a narrowly reviewed canonical status correction is integrated. This is a synchronization fact, not a new mathematical result.

## Relevant remote branch map

The `behind/ahead` column is `origin/main...branch` (`main-only commits / branch-only commits`) from the local object graph.

| Role | Remote-tracking ref | Head | Behind / ahead | Relationship and disposition |
|---|---|---:|---:|---|
| Canonical | `origin/main` | `1a6f924fd86352c11f57a95b0382adaf92d15bcd` | `0 / 0` | Canonical baseline; preserve without force or history rewrite. |
| B4 V1 Stage 0 | `origin/cp20-e7r-b4-tilted-microcanonical-fourier-v1-stage0-20260904` | `c83d22f9e3ac8bdc4ec955d14b3d7dca11c3fee1` | `11 / 5` | Historical frozen V1 branch; divergent, not a wholesale merge candidate. |
| B4 V1 failure | `origin/cp20-e7r-b4-stage1-input-integrity-failure-20260904` | `f1dce61f3d2ee207a50bd0f46208f49f3901f013` | `7 / 4` | Historical invalid/non-canonical invocation failure evidence; preserve as evidence branch. |
| V1 closeout / V2 handoff | `origin/integration-e7r-b4-v1-failure-closeout-v2-handoff-20260904` | `477d59ef1c38cda017bef00eeedb568bb0e9968b` | `5 / 2` | Divergent historical integration branch; relevant canonical effects already appear later in main lineage. |
| V2 initial reseal | `origin/cp20-e7r-b4-tilted-microcanonical-fourier-v2-stage0-reseal-20260904` | `1399e7831c7582fcf715a693c9db4f4a3d1184a5` | `3 / 17` | Blocked handoff candidate; preserve, do not merge wholesale. |
| V2 state-path verification | `origin/cp20-e7r-b4-v2-statepath-handoff-verify-20260904` | `df4cdae09558498dbbf505cf7fc3b89f6d5322b2` | `3 / 1` | Repair/verification side branch from pre-canonical base; preserve. |
| V2 accepted Stage-0 source | `origin/cp20-e7r-b4-v2-stage0-finalization-handoff-20260904` | `85f3daa617aaa245eb2b43c5b0cc425d669bb927` | `3 / 60` | Accepted source branch whose selected snapshot was canonicalized into main; do not merge its full history into current main. |
| Governance runner | `origin/b4-v2-governance-runner-no-more-branches-20260905` | `e7823e6d1828857c5a954bf6e4626e9a06166662` | `3 / 2` | Historical workflow branch; not canonical content. |
| Persistence recovery | `origin/b4-v2-persistence-recovery-20260905` | `5084dbd2c219cbbd42604c2683af0feef667e132` | `0 / 1` | Direct child of `origin/main`; read-only recovery workflow only. Review independently before any integration. |
| V2 real invocation evidence | `origin/cp20-e7r-b4-v2-stage1-20260905` | `04a66e41864d1d530ead63b1faeaf122048e3069` | `0 / 23` | Direct lineage from `origin/main`; net adds a workflow plus two failure-evidence files. Records authorization consumed and T1–T8 not executed. |
| V2 independent audit | `origin/cp20-e7r-b4-v2-preexec-zero-trust-audit-20260905` | `8fb8d68d3c131d6e11721fd629f1ea879102aedc` | `0 / 6` | Direct lineage from `origin/main`; three audit artifacts. Verdict: `[AUDIT FAIL — DO NOT EXECUTE B4 V2 STAGE1]`. |
| Publication audit | `origin/cp20-publication-factor-pressure-v1-20260904` | `2263dc3fc777431845eaaf0cdbc9916851937c40` | `7 / 36` | Publication-only divergent lineage containing the manuscript and specialist audit; not on canonical main. |
| JNT package | `origin/cp20-submission-jnt-v1-20260904` | `4cdbcf31823dadb09d0814b8af5b7790dcbdee2f` | `7 / 44` | Descends from the publication branch and adds JNT preparation/package material; not on canonical main. |
| Prefix exploration | `origin/codex/prefix-bridge-20260906-persistence` | `d544bf2d072dd442c3f6528d87d9f7c4f86c23ce` | `0 / 2` | Directly based on canonical `origin/main`; holds audited exploratory prefix package and persistence-status note. It is not canonical B4 acceptance. |

### Alias cluster

The following remote-tracking names all point to the same historical commit `8d274095b0e1acbe1fad0a73ef6a5293364902fc` (`Close B4 V1 integrity failure and hand off V2 reseal`):

- `origin/b4-v2-governance-runner-20260905`
- `origin/b4-v2-governance-runner-actual-20260905`
- `origin/b4-v2-governance-runner-actual2-20260905`
- `origin/b4-v2-governance-runner-actual3-20260905`
- `origin/b4-v2-governance-runner-exec-20260905`
- `origin/b4-v2-governance-runner-live-20260905`
- `origin/b4-v2-governance-runner-live2-20260905`
- `origin/b4-v2-governance-runner-stop-20260905`
- `origin/canonical-integrator-b4-v2-intake-auth-20260905`
- `origin/canonical-integrator-b4-v2-intake-auth-executor-20260905`
- `origin/canonical-integrator-b4-v2-intake-auth-finalizer-20260905`
- `origin/canonical-integrator-b4-v2-intake-auth-run-20260905`

These aliases do not represent twelve different scientific states. They are multiple remote names for one object and should be retained only as historical workflow provenance, not independently merged.

## Exact later B4 V2 evidence absent from canonical main

At `04a66e4`, the persisted JSON states:

- status: `[B4 V2 STAGE1 INPUT INTEGRITY FAILURE]`
- reason: `frozen dependency blob mismatch at Phase A: CURRENT_RESEARCH_STATE.json`
- `authorization_consumed: true`
- `T1_T8: NOT_EXECUTED`

At `8fb8d68`, the final audit states:

- verdict: `[AUDIT FAIL — DO NOT EXECUTE B4 V2 STAGE1]`
- the real entrypoint invocation occurred;
- RUN_WITNESS, PRE_T1_GATE, T1 START, and all T1–T8 mathematics were not reached;
- the single authorization is no longer available;
- a future attempt requires a new mechanical repair/reseal, fresh explicit authorization, and independent audit.

These two branches are complementary: the producer branch preserves the invocation evidence; the audit branch independently adjudicates it. Neither is included in `origin/main` at this snapshot.

## 20260907 untracked artifact-to-remote comparison

The following working-tree directories were untracked:

- `research_manager/exploratory/lead_parallel_20260907/`
- `research_manager/exploratory/math_20260907/`

Inventory result:

- total files: `59`
- source/report/result files: `58`
- generated Python cache: `1` (`math_20260907/M4_theta_profile/__pycache__/theta_profile.cpython-314.pyc`)
- byte-identical blobs found in any `refs/remotes/origin/*` history: **0 of 59**

Therefore none of the 20260907 files can be called GitHub-persisted from the observed remote-tracking graph.

There is an important local-only nuance: an internal Codex turn-diff capture tree, `refs/codex/turn-diffs/captures/1788777005002/144df11c-3af1-40d0-b0ae-45d68a147f29/base = b45019293546362c1acafd155dc53ab458c596e4`, contains byte-identical versions of the 58 non-cache files. This is **not** a local branch, remote branch, GitHub ref, or durable publication guarantee. It must not be counted as synchronization. The `.pyc` cache has no such match and should be excluded from any research package.

## Safe no-force integration topology

The recommended topology is additive and review-gated:

1. Keep `origin/main` at `1a6f924` unchanged until a dedicated canonical-status correction is reviewed. Never force-push or rewrite it.
2. Do not use stale local `main` (`9119a39`) as a base. In a clean dedicated integration worktree, first fast-forward the local pointer to the observed `origin/main`; do not merge the current exploratory checkout into local main.
3. Create one narrow status-correction integration branch from `origin/main`. Bring in only the final V2 invocation-failure evidence and final independent audit artifacts, preserving their exact bytes and provenance. Review the resulting root-state edits so that `CURRENT_RESEARCH_STATE.json` and `START_HERE_CURRENT_HANDOFF.md` change from “authorized/execute next” to “authorization consumed/do not execute.” Do not import invalid V1 drafts or claim T1–T8 execution.
4. Treat the publication lineage as a separate publication product. Because `cp20-submission-jnt-v1-20260904` descends from `cp20-publication-factor-pressure-v1-20260904`, preserve their order but do not merge either divergent branch wholesale into canonical research main. If canonical pointers are desired, integrate only a reviewed small manifest/status record that references the publication branch heads and exact artifacts.
5. Keep `codex/prefix-bridge-20260906-persistence` as an exploratory preservation branch. Do not merge it into main as B4 acceptance; any future selected lemma must pass a separate scientific acceptance/audit gate.
6. Package the 20260907 work in new, clearly labelled exploratory preservation branch(es) based on `origin/main`, excluding `__pycache__`/`.pyc`. A sensible split is one branch for `lead_parallel_20260907` and one for `math_20260907`, each with its own manifest and epistemic labels. Their current internal Codex capture is not sufficient persistence.
7. After each proposed push, independently re-read the exact remote branch head and compare the committed tree/hashes. Only after that verification should any small canonical integration PR be considered.

Conceptually:

```text
origin/main @ 1a6f924  (canonical; no force)
├── canonical-status-correction   <- selected exact failure + audit records; reviewed root-state repair
├── codex/prefix-bridge-... @ d544bf2  (exploratory preservation; already remote)
├── exploratory/lead-parallel-20260907  (new preservation branch; not yet remote)
├── exploratory/math-20260907           (new preservation branch; not yet remote)
└── publication references only         (publication branches remain separate products)
```

## Bottom line

The canonical remote-tracking main is intact at `1a6f924`, but its root handoff/state is stale and unsafe because the later V2 invocation failure and audit failure live only on separate remote branches. The prefix preservation branch is now synchronized at `d544bf2`. The publication/JNT branches remain separate divergent products. None of the 59 visible 20260907 files is present in any observed `origin/*` history; 58 exist only in an internal local Codex capture and one is disposable bytecode. The safe path is additive, branch-scoped, hash-verified integration with no force and no wholesale merge of historical/divergent branches.
