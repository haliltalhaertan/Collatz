# V3 integrity gate — dry run results

Executed 2026-09-07T07:17:38.919530+00:00 (report `utc` field). Harness: `DRY_RUN_INTEGRITY_GATE.py`.
Machine-readable record: `DRY_RUN_REPORT.json`. Captured streams: `DRY_RUN_STDOUT.txt`, `DRY_RUN_STDERR.txt` (empty),
`DRY_RUN_EXIT.txt`.

**Verdict: PASS in both directions.** The patched (V3) gate PASSES on a correctly built Phase-A/Phase-B pair and FAILS,
with the exact expected reason string, on four distinct corruptions — including a tampered **scientific** input blob.

## 1. Exact commands

```
# 1. work dir (short path: the repo's artifact filenames exceed Windows MAX_PATH under a deep temp path)
mkdir -p "C:/Users/MDP/AppData/Local/Temp/claude/b4v3"

# 2. run the harness (it performs the clone itself)
cd "C:/Users/MDP/Documents/ChatGPT/Collatz/research_manager/exploratory/lead_parallel_20260907/A1_launcher_repair"
python DRY_RUN_INTEGRITY_GATE.py \
  --repo   "C:/Users/MDP/Documents/ChatGPT/Collatz" \
  --work   "C:/Users/MDP/AppData/Local/Temp/claude/b4v3" \
  --report "…/A1_launcher_repair/DRY_RUN_REPORT.json" \
  > DRY_RUN_STDOUT.txt 2> DRY_RUN_STDERR.txt ; echo "EXIT=$?"
```

The clone the harness performs internally:
`git clone -c core.longpaths=true --no-hardlinks --quiet "C:/Users/MDP/Documents/ChatGPT/Collatz" <work>/clone`,
followed by `git remote remove origin` (so no push is possible), local `user.name`/`user.email`, and
`commit.gpgsign=false`.

**Process exit code: `0`. `DRY_RUN_STDERR.txt` is empty.**

## 2. Redirected stdout, verbatim

```
{
  "verdict": "PASS",
  "v2_root_cause_plumbing": {
    "config_v2_frozen_blob_for_state": "3ba90bbf9e91ddc600235a38a800db90b03a07e0",
    "state_blob_at_src_base_8d27409": "3ba90bbf9e91ddc600235a38a800db90b03a07e0",
    "state_blob_at_real_phase_a_34ac0db": "aa8daf546826853b720356ff96530f0b78ec197d",
    "v2_check_line81_would_fail_at_real_phase_a": true
  }
}
G1: expected=PASS observed=PASS exit=0 reason=None
G2: expected=FAIL observed=FAIL exit=1 reason=Phase-A governance blob mismatch: CURRENT_RESEARCH_STATE.json
G3: expected=FAIL observed=FAIL exit=1 reason=authorization missing phase_a_governance_blobs object
G4: expected=FAIL observed=FAIL exit=1 reason=frozen_dependencies must not list a Phase-A-bound governance file: CURRENT_RESEARCH_STATE.json
G5: expected=FAIL observed=FAIL exit=1 reason=frozen dependency blob mismatch at Phase A: research_manager/results/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE0/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_DEFINITIONS.md
```

The `v2_root_cause_plumbing` block re-derives the V2 root cause inside the clone using `git rev-parse` only — the sealed
V2 launcher is never executed.

## 3. What was built

The clone was created from main `1a6f924fd86352c11f57a95b0382adaf92d15bcd`; `clone_remotes` in the report is the empty
string. Every synthetic commit lives on a `dryrun/*` branch inside the clone:
`dryrun/G1/phaseA`, `dryrun/G1/phaseB`, `dryrun/G2/phaseA`, `dryrun/G2/phaseB`, `dryrun/G3/phaseB`,
`dryrun/G4/phaseA`, `dryrun/G4/phaseB`, `dryrun/G5/phaseA`, `dryrun/G5/phaseB`.

Each synthetic **Phase A** is built on top of `8d27409` (the launcher's `STAGE0_SOURCE`) by: checking the accepted
Stage-0 directory out of `34ac0db` byte-for-byte; applying `V3_STAGE1.patch`, `V3_CONFIG.patch`, `V3_CONTRACT.patch`
(all three apply cleanly — the harness asserts the resulting launcher and contract SHA-256 equal the values declared in
`V3_PATCH_HASHES.json`, `7cd46c5a…` and `0380a742…`); re-running the sealed static control-flow checker on the patched
launcher; recomputing `canonical_stage0_artifacts`; regenerating the seal manifest; building a synthetic seal ZIP; and
then performing the integrator rewrite of `CURRENT_RESEARCH_STATE.json` and `START_HERE_CURRENT_HANDOFF.md` — i.e.
reproducing exactly the condition that broke V2.

Each synthetic **Phase B** is a direct child of its Phase A carrying the authorization JSON (with
`phase_a_governance_blobs` unless the case suppresses it) and the state stage `STAGE_1_AUTHORIZED_NOT_EXECUTED`.

Confirmations recorded for every build: `static_control_flow_on_patched_launcher: "PASS"`,
`canonical_artifact_entries_recomputed_differently_from_patch: []` (the patch's recorded hashes reproduce exactly),
`v2_frozen_state_blob_would_match_at_phase_a: false` (the Phase-A state blob never equals the V2 frozen value — the
defect condition is genuinely present in every synthetic Phase A).

## 4. Case-by-case results

| case | what is wrong | exit | failure reason (from `…_STAGE1_INPUT_INTEGRITY_FAILURE.json`) | witness | gate | ledger |
|---|---|---|---|---|---|---|
| **G1** | nothing — correct pair | **0** | *(none)* | written | written | `["PRE_T1_GATE"]` |
| **G2** | Phase-A state blob ≠ the blob bound by the authorization | 1 | `Phase-A governance blob mismatch: CURRENT_RESEARCH_STATE.json` | absent | absent | `[]` |
| **G3** | V2-style authorization, no `phase_a_governance_blobs` | 1 | `authorization missing phase_a_governance_blobs object` | absent | absent | `[]` |
| **G4** | V2-style config re-listing the state file in `frozen_dependencies` | 1 | `frozen_dependencies must not list a Phase-A-bound governance file: CURRENT_RESEARCH_STATE.json` | absent | absent | `[]` |
| **G5** | **a frozen SCIENTIFIC input altered inside Phase A** | 1 | `frozen dependency blob mismatch at Phase A: …_V1_STAGE0/…_V1_DEFINITIONS.md` | absent | absent | `[]` |

**G1 (the PASS direction).** Phase A `a8188b0e0e4cf651bc55f01ed78e65291e9c8b40`, Phase B
`c385b7dcfdde472a66a4bbf05dd9fa9098ab8ac6`, synthetic seal sha256 `b2c1b5da72fbfb70…`. Launcher stdout:

```
B4 V2 STAGE1 PRE-T1 INTEGRITY GATE: PASS
T1–T8 NOT EXECUTED by integrity launcher.
```

The run witness and the PRE_T1_GATE were written, the execution ledger contains exactly one event `PRE_T1_GATE`, the
results file records `{"T1":"NOT_EXECUTED", …, "T8":"NOT_EXECUTED"}`, and **no T1 START was emitted**. The Phase-A state
blob was `9404ce9200ab92e33bb1791e72d2daf7067ad585` — i.e. a value that did not and could not exist at seal time, which
is precisely what V2 could not express and V3 now binds.

**G5 (the scientific-tamper direction, required by the task).** The frozen scientific input
`research_manager/results/…_V1_STAGE0/…_V1_DEFINITIONS.md` was altered inside Phase A:
sealed blob `49b40e67af1b22b2b8ffc74d319f7484b94f3adc` → Phase-A blob `838bb12cf9a7cb28aa9b93ee3ad04f89f906debd`.
The gate halted at the unmodified `frozen_dependencies` loop, before writing any witness or gate file. The V3 patch
therefore did **not** weaken the protection of scientific inputs.

## 5. Safety properties asserted by the run

Recorded in `DRY_RUN_REPORT.json` and true of every case:
`sealed_v2_launcher_executed: false`, `real_seal_used: false`, `real_authorization_tuple_used: false`,
`T1_T8_executed: false`, `authorization_granted_by_this_run: false`, `t1_start_emitted: false`.
All work happened inside the throwaway clone under `C:/Users/MDP/AppData/Local/Temp/claude/b4v3`; the clone has no
remote. The real repository was verified clean before and after: `git status --porcelain` reports only the untracked
`research_manager/exploratory/` working directory.

## 6. Harness fixes made to get the run to work

The harness inherited from the interrupted earlier session did not run. Four defects were found and fixed; all four were
in the **harness**, none in the V3 patches.

1. **Windows MAX_PATH.** `git clone` into the deep session scratchpad failed with ~50 × `Filename too long` and
   `fatal: unable to checkout working tree`. Fix: clone with `-c core.longpaths=true` (written into the new repo's config
   and used for its own checkout) plus an explicit `git config core.longpaths true`, and run under the shorter work dir
   `C:/Users/MDP/AppData/Local/Temp/claude/b4v3`.
2. **Six sealed members are not tracked in the repository.** The seal manifest lists the V2 scientific program documents
   (`…_V2_DEFINITIONS.md`, `…_V2_FALSIFICATION_PLAN.md`, `…_V2_ORDER.md`, `…_V2_OUTCOME_LADDER.md`,
   `…_V2_T1_T8_PROGRAM.md`, `…_V2_TARGET_NORMAL_FORM.md`), which exist only inside the real seal ZIP; the harness crashed
   with `FileNotFoundError`. Fix: build the synthetic seal from an in-memory member map, filling those six with
   deterministic placeholder bytes. This is sound because the launcher cross-checks only the CONFIG and CONTRACT members
   against on-disk files (`…_STAGE1.py:102–103`); every other seal check — CRC, ordering, uniqueness, manifest
   membership, per-member hash — is exercised identically. Recorded as `synthetic_seal_members_not_in_repo_tree` (6).
3. **`.gitattributes` line-ending normalisation.** The repo sets `* text=auto eol=lf` while `core.autocrlf=true`, so the
   SHA-256 the launcher sees (`git show <commit>:<path>`, i.e. blob bytes) is not the SHA-256 of the working-tree file.
   The harness recomputed `canonical_stage0_artifacts` from disk, producing a spurious
   `Phase-A Stage0 SHA256 mismatch: …_STATIC_CONTROL_FLOW_RESULTS.json` in **all five** cases. Fix: recompute both
   identifiers from the blob git will actually serve (`git hash-object -w` then `git cat-file blob`).
4. **False-positive T1-START detector.** `any('T1' in event …)` matched the legitimate ledger event `PRE_T1_GATE`, so G1
   was scored FAIL despite exit code 0 and correct output. Fix: match `re.fullmatch(r'T1[ _-]?START', …)` on the event
   name and additionally scan stdout for the literal `T1 START`.

One deliberate extension: **case G5 did not exist.** The inherited harness covered G1–G4, none of which tampers a
scientific input. G5 was added, and `dry_run_gate_cases`/`dry_run_gate_expected` in the V3 config were regenerated to
declare it (`make_v3_patches.py` re-run). That regeneration changed only the config
(`v3_config_sha256` `6a79b2cd…` → `27e2e0a9a314403d9132c60241dce22e1d40c2182687a14a99af172a4b8df772`); the patched
launcher and contract hashes are unchanged (`7cd46c5a…`, `0380a742…`), and the launcher/contract patches were not
regenerated in substance.

## 7. What this run does **not** show

It does not exercise the real seal, the real authorization tuple, or the sealed V2 launcher. It does not validate a V3
seal (none exists). It does not test defects C3 or C4 of `LAUNCHER_DEFECT_ANALYSIS.md`, which the patches do not address.
The synthetic seal's six placeholder members mean seal *content* fidelity for those documents is untested — only the seal
*mechanism* is.

---

Nothing in this document authorizes a B4 V2 Stage-1 run. No mathematics was executed: T1–T8 remained `NOT_EXECUTED` in
every case and no T1 START was emitted. The V2 once-only authorization was consumed on 2026-09-05; a new once-only
authorization requires an explicit manager transaction.
