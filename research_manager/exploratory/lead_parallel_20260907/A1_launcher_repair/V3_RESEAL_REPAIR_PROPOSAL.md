# V3 reseal repair proposal — frozen-dependency semantics

Scope: repair the integrity contract of `CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2` Stage-1 so that a future,
separately authorized run can reach the pre-T1 gate. **No scientific content is touched.**
Artifacts this document explains: `V3_STAGE1.patch`, `V3_CONFIG.patch`, `V3_CONTRACT.patch`, `V3_PATCH_HASHES.json`,
`derived_v3_files/` (the three patched files as produced by `make_v3_patches.py`).
Date: 2026-09-07.

---

## 1. What must be fixed

From `LAUNCHER_DEFECT_ANALYSIS.md` §2–§3: `frozen_dependencies` conflates two kinds of input under one seal-time,
commit-independent binding, and then checks both at the Phase-A commit (`…_STAGE1.py:78–81`):

* **immutable scientific inputs** — the V1 Stage-0 program documents and the V1 closeout decision. Their blobs at seal
  time and at Phase A are the same object (verified: identical at `8d27409`, `34ac0db`, `f8d778a`). Freezing them at seal
  time is correct and is the only thing that makes the run reproducible.
* **live governance files** — `CURRENT_RESEARCH_STATE.json` and `START_HERE_CURRENT_HANDOFF.md`. The canonical integrator
  *rewrites* these as part of the very transaction that creates Phase A and Phase B. Their Phase-A blob does not exist,
  and cannot be predicted, when the seal is built.

Any repair must keep the first property intact while making the second expressible.

## 2. The three candidate semantics

**(a) Exclude the live state file from `frozen_dependencies`; bind the Phase-A state by a post-Phase-A hash recorded in
the authorization JSON.**
Correct in mechanism. Too narrow as stated: it names only the state file, and leaves
`START_HERE_CURRENT_HANDOFF.md` — the same class of file, rewritten by the same integrator one commit later — inside
`frozen_dependencies` (defect C2). A repair that leaves a same-class latent defect standing is not acceptable after two
consumed authorizations.

**(b) Bind by a content-subset hash over scientific fields only.** Rejected on four independent grounds.
(i) It puts a *parser and a canonicaliser* inside the trust boundary: the launcher would have to load
`CURRENT_RESEARCH_STATE.json`, select fields, canonicalise them and hash the result — a new, unsealed, drifting schema in
the middle of the integrity gate. `JOURNAL_SCHEMA_DRIFT.md` documents exactly this failure mode occurring elsewhere in
the same governance stack. (ii) The resulting digest is not a git object, so it cannot be verified from the object store
by `git rev-parse`/`git show`; the check would no longer be content-addressed. (iii) Everything outside the chosen subset
becomes unbound — a strictly larger tamper surface than today. (iv) `CURRENT_RESEARCH_STATE.json` has no scientific
subset to extract: it is a governance file end to end.

**(c) Two-tier: seal-time blobs for scientific inputs, Phase-A-time blobs for governance files.** ← **RECOMMENDED.**

## 3. Recommendation: (c), implemented by the mechanism of (a) generalised

Adopt **(c)**. The implementation is exactly the mechanism option (a) describes, lifted from one hard-coded file to a
declared set, so that both governance files — and any future one — are covered by construction:

* The Stage-0 config gains `phase_a_bound_governance_files`, an explicit list of the files the integrator is expected to
  rewrite. Both governance files are removed from `frozen_dependencies`.
* The launcher refuses to run if any declared governance file still appears in `frozen_dependencies`. The V2 defect
  becomes an *immediate, named, pre-mathematics failure of the configuration* rather than a mismatch discovered by
  accident three checks later.
* Each declared governance file must have, at the Phase-A commit, exactly the blob recorded under
  `phase_a_governance_blobs` in the **Phase-B** authorization JSON — which is written after Phase-A read-back and can
  therefore know the value. The binding stays content-addressed (a git blob SHA-1, resolvable with `git rev-parse`); only
  the *time at which the expected value is fixed* moves from seal time to Phase-B time.
* An authorization JSON without `phase_a_governance_blobs` (a V2-style authorization) is rejected. The new field cannot
  be silently omitted.

Why (c) and not (a) alone: (c) states the invariant — *every input is bound by a git blob; scientific inputs are bound at
seal time, integrator-written inputs at Phase-B time; nothing is unbound and nothing is bound to a value that cannot
exist* — and the declared list makes that invariant checkable rather than remembered. Why (c) and not (b): (c) adds no
parser, no new digest format and no new schema to the trust boundary; it reuses the git blob identity the launcher
already relies on everywhere else.

Note what is **not** relaxed. The governance files remain bound exactly as tightly as before — one exact blob each, no
wildcards, no "ignore this file", no ranges. What changes is *who records the expected value and when*. Trust does not
move from the seal to the integrator either, because the authorization JSON is itself sealed into the run by
`--authorized-seal-sha256`/`--contract-sha256` and is read from the Phase-B commit whose ancestry is checked.

## 4. Precisely what the patches change

`V3_STAGE1.patch` — 13 added lines, **0 removed, 0 modified** (verified by unified diff: 13 `+`, 0 `-`).
Launcher goes 157 → 170 lines; sha256 `9222d0e0…` → `7cd46c5a7e9c74e8e204dbea0d40085b0b34c146406e640de0543be46079bfb2`,
git blob `d8439a34…` → `91479908ae8e3e3ab1c785a58e9b4a4f4cb2b1a7`.
1. One entry appended to `BLOCKED`: the consumed V2 seal `11456b7d6f673e5cab6079850731cbda70373b77e4e0f532089d6783fd16c78e`.
   It can never be re-authorized.
2. Inside `verify_authorization_chain`, immediately before the existing `frozen_dependencies` loop: read
   `phase_a_bound_governance_files` from the config (fail if absent or empty), and fail if any of them appears in
   `frozen_dependencies`.
3. Immediately after that loop: read `phase_a_governance_blobs` from the authorization JSON (fail if absent or not an
   object), require each entry to be 40 lowercase hex characters, and compare it to `git rev-parse <phase_a>:<path>`.
The existing `frozen_dependencies` loop is untouched, so tampering with a scientific input still fails exactly as before.

`V3_CONFIG.patch` — sha256 `2fbc7bd0…` → `27e2e0a9a314403d9132c60241dce22e1d40c2182687a14a99af172a4b8df772`.
Removes the two governance files from `frozen_dependencies` (the other six entries keep byte-identical values); adds
`phase_a_bound_governance_files`, `frozen_dependencies_semantics`, `authorization_model.phase_a_governance_binding`,
`future_authorization.phase_a_governance_blobs_definition` and `phase_a_governance_blobs` in
`future_authorization.required_fields`; appends the consumed V2 seal to `blocked_seal_blacklist`; adds
`dry_run_gate_cases`/`dry_run_gate_expected` (G1–G5); bumps `schema` to
`…_TWO_COMMIT_AUTHORIZATION_STATEPATH_PHASE_A_GOVERNANCE_BINDING_V5`; and updates the two `canonical_stage0_artifacts`
entries that the patches necessarily change — the launcher and the contract — plus `contract.sha256`.

`V3_CONTRACT.patch` — sha256 `7f253174…` → `0380a742cc7bcfc3f5036eabe191722bfc8da4bc2a656e5628e8baf4219c9b6b`,
git blob `49a8571f…` → `0538d87d1c2a38c83435fe8f356284cfde1618bc`.
Documents `phase_a_governance_blobs` as a required authorization field, adds gate clauses 12 and 13, adds a
"Frozen dependency semantics" section naming the 2026-09-05 defect, and records the consumed V2 seal in the blocked list.

The config/contract cross-references are self-consistent: the patched config's `contract.sha256` and its
`canonical_stage0_artifacts` entries for the launcher and the contract equal the recomputed hashes of the patched files
(`V3_PATCH_HASHES.json`, and re-derived independently by the dry-run harness — see `DRY_RUN_RESULTS.md`, field
`canonical_artifact_entries_recomputed_differently_from_patch: []`).

## 5. No scientific change — proof

**5.1 The launcher contains no mathematics in either version.** Its own header is
`# INTEGRITY ORCHESTRATOR ONLY. NO B4 MATHEMATICS.` (line 2), and this is mechanically enforced by the sealed
`…_STATIC_CONTROL_FLOW_CHECK.py`, which asserts `no_math_packages`, `no_T1_START_emission`, `gate_checked_before_ledger`
and `integrity_failure_literal`. That checker, unmodified, was run against the **patched** launcher inside the dry-run
clone and returned `STATIC CONTROL FLOW PASS` on every build (recorded as
`static_control_flow_on_patched_launcher: "PASS"` in `DRY_RUN_REPORT.json` for G1, G4 and G5). There are consequently no
"T1–T8 mathematical code sections" in this file to change: a diff restricted to the math sections is a diff over the
empty set. Token scan over both versions returns the identical set `{T1, T8}`, occurring only in the literals
`{'T1'…'T8'}: 'NOT_EXECUTED'` and in filenames.

**5.2 The launcher diff is purely additive and confined to `verify_authorization_chain` + `BLOCKED`.**
13 inserted lines, 0 deleted, 0 modified. The T1–T8 result block (`…'T1_T8':{f'T{i}':'NOT_EXECUTED' …}`), the
`forbidden_stage0` firewall behaviour and both terminal print statements are byte-identical.

**5.3 The config's scientific sections are byte-identical.** Key-by-key comparison of the V2 config against
`derived_v3_files/…_CONFIG.json`:

```
IDENTICAL  scientific_program            IDENTICAL  allowed_stage0_execution
IDENTICAL  forbidden_stage0              IDENTICAL  canonical_state
IDENTICAL  canonical_v1_stage0_scientific_source_commit
IDENTICAL  selftest_case_meaning         IDENTICAL  selftest_expected
IDENTICAL  task / task_version / stage0_source_base_sha / stage0_only
IDENTICAL  stage1_authorized / working_branch
```

`sha256(canonical-JSON(scientific_program))` is `d70c199141821e5ecf458df230740f9192e2dbe0a49f27af69a2e0702f2bd91b`
in **both** versions — `G_r`, `T_r`, `alpha_definition`, `eta_r`, `arc_split` (major / intermediate / minor, with
`adaptive_changes_forbidden: true`), `fourier_convention` and the F1–F10 / T7-F1–T7-F5 falsification list are unchanged
to the byte. `stage1_authorized` remains `false`. The only changed config keys are
`authorization_model`, `blocked_seal_blacklist`, `canonical_stage0_artifacts` (launcher + contract entries only),
`contract`, `frozen_dependencies`, `future_authorization`, `schema`, plus the four newly added integrity keys — every one
of them an integrity-contract key.

**5.4 No scientific input loses its binding.** The six scientific/closeout entries of `frozen_dependencies` are retained
with byte-identical blob values; only the two governance files were removed, and they were removed *into* a stricter,
explicitly-checked binding rather than out of the contract. Dry-run case G5 demonstrates that altering a frozen
scientific input at Phase A still halts the gate.

Classification, matching the independent audit: **integrity-contract / configuration defect; no scientific change.**
B4-N1…B4-N7, B4-CT and E6-N2 are untouched and remain `NOT ESTABLISHED` / `[OPEN]`.

## 6. What still has to happen outside these patches

A V3 seal must be built and hashed; the CI integrator must be taught to write `phase_a_governance_blobs` into the Phase-B
authorization JSON after Phase-A read-back; the seal manifest must be regenerated for the patched members; and a **new**
once-only authorization must be granted. None of that is done here.

Defects C3 (a contract defect consumes the authorization exactly like a tamper) and C4 (the witness validator is executed
from disk without a hash check) from `LAUNCHER_DEFECT_ANALYSIS.md` are **not** addressed by these patches and are left as
open recommendations; C3 in particular is the reason two authorizations were burned and deserves a manager decision
before the third is issued.

---

Nothing in this document authorizes a B4 V2 Stage-1 run. The V2 once-only authorization was consumed on 2026-09-05; a new
once-only authorization requires an explicit manager transaction.
