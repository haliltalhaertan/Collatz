# B4 V2 Stage-1 launcher — defect analysis from source

Task: `CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2`
Analysed file: `research_manager/results/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE0/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE1.py`
(157 lines, sha256 `9222d0e0a8079e3560bc880520dd5ead44869f5fd4fa541520e225c841b8a732`, git blob `d8439a34620b2db4f7b06f1d889e2b0543354a65`)
Supporting files: `..._CONFIG.json` (sha256 `2fbc7bd0…`), `..._WITNESS_VALIDATOR.py`, `..._STATIC_CONTROL_FLOW_CHECK.py`.
Repository state used for verification: main `1a6f924`, Phase A `34ac0db`, Phase B `f8d778a`, Stage-0 source base `8d27409`.
Analysis date: 2026-09-07. Method: static reading of the source plus read-only `git rev-parse` / `git show` against the real object store. **The sealed launcher was never executed.**

---

## 1. Control flow: CLI arguments → the failing check

| Step | Line(s) | What happens |
|---|---|---|
| 1 | `137–142` | `main()` parses seven required arguments: `--config`, `--seal`, `--canonical-stage0-base-sha`, `--authorization-commit-sha`, `--authorized-seal-sha256`, `--contract-sha256`, `--output`. |
| 2 | `144` | `config=json.load(open(a.config,encoding='utf-8'))` — the config is read from the **working tree**, not from git. |
| 3 | `145` | `config['stage0_source_base_sha']` must equal the hard-coded constant `STAGE0_SOURCE` (`8d274095…`, line 6). |
| 4 | `146–147` | config-declared contract SHA and the on-disk contract file must both equal `--contract-sha256`. |
| 5 | `148` → `83–103` | `verify_seal`: blocked-seal list, seal file SHA, ZIP CRC, member uniqueness, sorted member order, manifest membership and per-member hashes, sealed-config-vs-on-disk-config, sealed-contract-vs-`--contract-sha256`. |
| 6 | `149` → `105–106` | `output_absence`: none of `--output`, RUN_WITNESS, PRE_T1_GATE, EXECUTION_LEDGER, INPUT_INTEGRITY_FAILURE may already exist. |
| 7 | `150` → `43` | `verify_authorization_chain(stage0_base, authorization_commit, seal_sha, contract_sha, config)` is entered. `stage0_base` = `--canonical-stage0-base-sha` = Phase A = `34ac0db`. |
| 8 | `44–49` | Both SHAs resolve to commits; they are distinct; `8d27409` ⊑ `stage0_base` ⊑ `authorization_commit` ⊑ `HEAD` (ancestry). |
| 9 | `50–55` | The authorization JSON is read **at the Phase-B commit** and its four fields are matched. |
| 10 | `56–70` | `CURRENT_RESEARCH_STATE.json` is read **at the Phase-B commit** and `active_task.stage` must be `STAGE_1_AUTHORIZED_NOT_EXECUTED`; legacy aliases must agree. |
| 11 | `71–77` | Each `canonical_stage0_artifacts` entry is checked **at the Phase-A commit** for both git blob SHA-1 and SHA-256. |
| 12 | **`78–81`** | **Each `frozen_dependencies` entry is checked at the Phase-A commit against a blob recorded at seal time. This is where the run of 2026-09-05 died.** |
| — | `151–154` | (never reached) witness write, witness validation, gate write, ledger append, results write, `PRE-T1 INTEGRITY GATE: PASS`. |

The failing block, quoted verbatim from the source:

```python
78	    for path,blob in config['frozen_dependencies'].items():
79	        try: got=git('rev-parse',f'{stage0_base}:{path}')
80	        except Exception: fail('frozen dependency unreadable at Phase A: '+path)
81	        if got!=blob: fail('frozen dependency blob mismatch at Phase A: '+path)
```

`fail()` (lines `28–34`) writes `{TASK}_STAGE1_INPUT_INTEGRITY_FAILURE.json` with `'authorization_consumed':True` and raises
`SystemExit('[B4 V2 STAGE1 INPUT INTEGRITY FAILURE] '+msg)`.

The observed 2026-09-05 message — `frozen dependency blob mismatch at Phase A: CURRENT_RESEARCH_STATE.json` — is produced by **line 81 and by no other line in the file**. The string literal is unique in the source.

## 2. Root cause: CONFIRMED from the source and the object store

The sealed config contains (`..._CONFIG.json`, `frozen_dependencies`):

```json
"CURRENT_RESEARCH_STATE.json": "3ba90bbf9e91ddc600235a38a800db90b03a07e0"
```

Line 79 evaluates `git rev-parse 34ac0db:CURRENT_RESEARCH_STATE.json`. Measured against the real repository:

| commit | role | blob of `CURRENT_RESEARCH_STATE.json` |
|---|---|---|
| `8d27409` | Stage-0 source base (`STAGE0_SOURCE`, line 6) | `3ba90bbf9e91ddc600235a38a800db90b03a07e0` ← the frozen value |
| `34ac0db` | **Phase A** (`--canonical-stage0-base-sha`) | `aa8daf546826853b720356ff96530f0b78ec197d` |
| `f8d778a` | Phase B (`--authorization-commit-sha`) | `70217bdeeafba29a0978f4d95abbbc4c0aff9655` |
| `1a6f924` | canonical main at execution time | `42b168c86d8d92464edead501e840bb530b5c504` |

The frozen value is the blob **one commit before Phase A**. `git show --stat 34ac0db` shows `CURRENT_RESEARCH_STATE.json | 84 +++---` — Phase A *is* the commit that rewrites the state file (it stamps `active_task.stage`, `active_integrator`, `b4_v2_stage0`, `documents`, `next_action`). The very same commit is required by lines 71–77 to carry the canonicalised Stage-0 artifacts, so Phase A cannot be moved earlier either.

Therefore `got != blob` at line 81 holds **for every possible choice of Phase A that satisfies the rest of the contract**. The check is not merely wrong for one run; it is unsatisfiable by construction. The audit's mechanical root cause (`bagimsiz-denetim/e7r-b4-v2-preexec-zero-trust-audit-20260905/…AUDIT_2026-09-05.json`, `mechanical_root_cause`) is **CONFIRMED, from the source and from the object store, independently of the audit.**

Cross-check that the rest of the freeze list is fine: of the eight `frozen_dependencies` entries, **exactly one** mismatches at `34ac0db` — `CURRENT_RESEARCH_STATE.json`. The other seven (the V1 Stage-0 scientific documents and the V1 closeout decision) are byte-identical at `8d27409`, `34ac0db` and `f8d778a`. All twelve `canonical_stage0_artifacts` entries match at `34ac0db` on both blob and SHA-256. The defect is confined to the governance-file semantics of `frozen_dependencies`.

---

## 3. Every other check, classified

Enumeration is exhaustive over the comparison sites in the file (`==`/`!=`/`in`/membership tests reachable from `main`).

### CONFIRMED

**C1 — `frozen_dependencies` seal-time blobs validated at the Phase-A commit (lines 78–81).**
The defect above. Evidence: blob table in §2. Reason string reproduced verbatim by the 2026-09-05 run.

**C2 — `START_HERE_CURRENT_HANDOFF.md` in `frozen_dependencies` is the same defect, dormant only by commit ordering (lines 78–81).**
Same class as C1: the file is rewritten by the same canonical integrator. In the CI script `.github/scripts/b4_v2_canonical_integrate.py` (branch `origin/b4-v2-governance-runner-no-more-branches-20260905`) the handoff is written at line 61, i.e. in the **third** commit of the transaction, not in Phase A. Measured blobs: `e2009a91…` at `8d27409`, `34ac0db` and `f8d778a`; `a80715633857fd110fd0e4145a469215de09b434` at `1a6f924` (`git show --stat 1a6f924` lists `START_HERE_CURRENT_HANDOFF.md | 65 ++---`). Had the integrator emitted the handoff in Phase A — which nothing in the contract forbids — line 81 would have fired on this path instead. Classified CONFIRMED (a live self-contradiction between the freeze semantics and the governance protocol), not merely plausible.

**C3 — an integrity-contract defect consumes the once-only authorization identically to a tamper (lines 28–34).**
`fail()` writes `'authorization_consumed':True` for *every* failure reason, including failures caused by the sealed configuration being unsatisfiable. There is no distinguished exit for "the seal contradicts itself" versus "an input was tampered with". This is the mechanism by which two authorizations (V1 2026-09-04, V2 2026-09-05) were burned with zero mathematics executed. It is a governance-level design defect, not a false comparison.

**C4 — the witness validator is executed from the working tree without any hash check (lines 119–124).**
```python
120	    vp=HERE/f'{TASK}_WITNESS_VALIDATOR.py'; spec=importlib.util.spec_from_file_location('v2validator',vp)
121	    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
```
`HERE` is the launcher's own directory (line 14). The sealed manifest **does** carry this file (`59c7c81511602469387160cdd5e737eb862b40fb91950ed599147ad2aa699bdd  …_WITNESS_VALIDATOR.py`) and the config **does** carry its blob (`9f40af0f…`), but neither is consulted before `exec_module`. Contrast lines 102–103, which do cross-check the config and the contract against the seal. A modified on-disk validator would be loaded and executed, and would then be the thing that decides whether the run witness is acceptable. Not a cause of the 2026-09-05 failure; a real gap in the trust boundary.

### PLAUSIBLE

**P1 — `output_absence` mixes CWD-relative and launcher-relative paths (lines 105–106).**
```python
106	    if any(p.exists() for p in [pathlib.Path(output),WITNESS,GATE,LEDGER,FAILURE]): fail('Stage1 output already exists')
```
`WITNESS`/`GATE`/`LEDGER`/`FAILURE` are absolute (`HERE/…`, lines 15–18) but `pathlib.Path(output)` resolves against the process CWD. Two invocations from different working directories can write two different `--output` files while each passes its own absence pre-check. The one-run discipline survives via `FAILURE`/`WITNESS`, which are CWD-independent, so this is a weakening rather than a hole — hence PLAUSIBLE.

**P2 — every `git` call inherits the process CWD (lines 23–24).**
`git(*args)` runs with no `cwd=`. The commit-scoped reads (lines 50, 56, 72, 75, 79) and `HEAD` (line 49) therefore describe *whatever repository the caller happened to be standing in*, which is not required to be the repository that contains the launcher. A run started from a stale clone would validate a stale `HEAD`. No evidence this occurred.

**P3 — working-tree vs committed divergence is only partly covered (lines 144, 147, 102).**
The config (144) and contract (147) are read from disk and cross-checked against the seal, which is sound. But the launcher never asserts that `HEAD` is clean or that the on-disk Stage-0 directory equals `HEAD`'s tree. Combined with C4 this means the executed code path is anchored to the seal for exactly two files and to nothing for the rest.

**P4 — `require_ancestor(authorization_commit,'HEAD',…)` (line 49) binds to an unpinned symbolic ref.**
Any descendant of Phase B satisfies it, including one that has since re-written governance state. That is intentional (execution happens later than authorization), but it means "the state the launcher validated" and "the state the repository is in" are two different things by design, and only the former is recorded in the witness.

### NOT A DEFECT

**N1 — `canonical_stage0_artifacts` validated at the Phase-A commit (lines 71–77).** Superficially the same shape as C1, but satisfiable: these twelve files are *created* by Phase A with exactly the sealed bytes. Verified: all twelve match at `34ac0db` on both `git_blob_sha1` and `sha256`. Includes the launcher's own blob — a self-reference that is nevertheless satisfiable, because the sealed bytes and the committed bytes have the same origin.

**N2 — the authorization JSON is not required to name its own commit (lines 50–55).** The config marks `authorization_commit_sha` as `forbidden_required_field`, and the launcher only checks `authorized_v2_seal_sha256`, `v2_contract_sha256`, `canonical_stage0_base_sha`, `stage`. This is the *repair* of an earlier defect (`…_AUTHORIZATION_BASE_SELF_REFERENCE_REPAIR_RECORD.json`, blocked seal `66ac9759…`). Confirmed clean: no expected value here is computed from a commit later than the one it validates.

**N3 — canonical state read at the Phase-B commit (lines 56–70).** The stage `STAGE_1_AUTHORIZED_NOT_EXECUTED` is written *by* Phase B, so reading it *at* Phase B is coherent. Verified against `f8d778a`. The alias-consistency rule (lines 65–70) compares two fields inside the *same* file version — no cross-commit comparison.

**N4 — seal internals (lines 84–103).** Blocked-seal list, seal SHA, ZIP CRC, duplicate members, sorted member order, manifest membership and per-member hashes, sealed-vs-on-disk config, sealed contract SHA. All are within-artifact comparisons with no commit dependence.

**N5 — `config['stage0_source_base_sha']` vs the `STAGE0_SOURCE` constant (line 145).** Compares a sealed value to a compiled-in value; both are fixed at seal time. Satisfiable and verified.

**N6 — witness self-consistency (`…_WITNESS_VALIDATOR.py:24–42`) and `write_gate`/ledger (lines 126–135).** Every comparison is against a value the launcher itself just produced or received on the command line. No cross-commit expectation.

### Answering the three named sub-questions directly

- *Checks comparing state-file hashes across commits that must differ*: exactly one — lines 78–81 applied to `CURRENT_RESEARCH_STATE.json` (C1), plus the same construct latent on `START_HERE_CURRENT_HANDOFF.md` (C2).
- *Checks binding to the authorization commit in a way that cannot exist at seal time*: **none**. The sealed config records no Phase-A or Phase-B SHA; the authorization commit SHA arrives only as a runtime argument (line 140) and the authorization JSON is explicitly forbidden from self-referencing (N2). This class was already repaired before V2.
- *Checks whose expected value is computed from a commit later than the one they validate*: **none in that direction.** The V2 defect is the mirror image — the expected value is computed from a commit **earlier** than the one it validates (`8d27409` used to validate `34ac0db`).

---

## 4. Scope statement

Nothing in this document authorizes a B4 V2 Stage-1 run. The sealed launcher was not executed and no seal, argument tuple or authorization artifact was supplied to it. The V2 once-only authorization was consumed on 2026-09-05; a new once-only authorization requires an explicit manager transaction.
