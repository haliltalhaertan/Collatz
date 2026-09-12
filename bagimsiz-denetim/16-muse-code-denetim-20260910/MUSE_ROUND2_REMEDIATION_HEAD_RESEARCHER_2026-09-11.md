# Muse Code Round-2 — Head-Researcher Verification and Remediation

**Date:** 2026-09-11  
**Repository:** `haliltalhaertan/Collatz`  
**PR:** #1, branch `external-audit/muse-code-round1-20260910`  
**Status:** verified remediation on audit PR branch; **not canonical/main yet**.

## Executive verdict

Muse Round-2 remains useful and its new actionable findings were substantially confirmed. It does **not** refute a central mathematical claim or prove Collatz. Its most important new contribution is repository hygiene: several historical exploratory scripts still printed conclusions that the later audit reports had already withdrawn or narrowed.

Round-2 also correctly pointed out that only a selected subset of ZIP members had explicit member hashes in `CURRENT_RESEARCH_STATE.json`. The existing verifier already checked the whole ZIP SHA-256, byte size, member count and CRC, so this was not an unauthenticated 927-member hole. Nevertheless per-member hashing was incomplete. That diagnostic/integrity coverage is now strengthened to all members.

## Round-2 findings verified and fixed

### A. CP19 Task-5 stale exclusion output — CONFIRMED / FIXED

`bagimsiz-denetim/07-geriye-donuk-tarama/seyrek_kritik_genisletme.py` historically printed `SURVIVOR DISLANIR` from a numerical pressure comparison. The later report had already corrected the inference: the CP19 Task-5 survivor does not satisfy the global critical-log hypothesis used by that surface.

The script now prints the numerical surface comparison only as a diagnostic and ends with the current status:

`[CP19 TASK5 SURVIVOR NOT EXCLUDED — HYPOTHESIS MISMATCH]`.

### B. Task 8A stale grid/phase-cost outputs — CONFIRMED / FIXED

The historical Task8A scripts omitted the feasible-domain condition

`rho_1 - rho_2 >= 3 - 2 alpha`

and a finite grid gap was once interpreted as a strict phase cost. The frozen correction says the properly optimized feasible problem recovers CP19 Task 4 exactly and does not provide a strict optimized Sturmian phase cost.

Both scripts were aligned with that status:

- `10-task8a/01_basinc_yuzeyi.py` now enforces the feasible constraint and explicitly labels the finite grid as a diagnostic, not a certified optimizer.
- `10-task8a/02_cp19t4_koprusu.py` no longer turns a grid mismatch into a theorem; it prints the frozen result and the Task-5 hypothesis mismatch.

No claim is made that the edited finite-grid scripts themselves constitute the V3 optimization proof.

### C. D0 transient plateau falsely presented as counterexample — CONFIRMED / FIXED

`12-d0-denetim/02_onebit_lift_ve_kirma.py` used equality over the last four sampled `r_k` values as a proxy for eventual stabilization. The D0 audit report already explains why that is invalid: a finite plateau is not eventual stabilization.

The script now:

- states the algebraic one-bit-lift result as the actual verdict;
- retains the last-four experiment only as a diagnostic;
- explicitly says a nonconstant `R` on such a transient plateau is **not** a counterexample.

### D. D1 finite-inf / liminf confusion — CONFIRMED / FIXED

Two D1 scripts retained historical finite-minimum comparisons that could print `TUTARSIZ` or a false-looking compatibility verdict even though the later tail analysis repaired the test.

- `13-d1-denetim/01_cekirdek_A_B_C.py` now labels the global finite-min comparison as non-asymptotic and directs the reader to the aligned tail test.
- `13-d1-denetim/02_madde10_liminf.py` is now explicitly a diagnostic of the old test's flaw and no longer issues an asymptotic verdict from extrema at different indices.
- `03_madde10_kuyruk.py` remains the current finite tail/trough diagnostic.

### E. Task-6 counterexample-discipline wording — CONFIRMED / FIXED

`04-cp20-task6-denetim/madde08_karsi_ornek_disiplini.py` contained two overstatements:

1. the `kappa=0.5` construction was described only as violating H2, although the realized finite construction also displays linear drift and therefore fails H1;
2. a random zero-critical example with `|s_N|=37289` at `N=60000` was called `sqrt(k)`-scale despite being visibly linear-scale in that finite sample.

The script now reports `s_N/N` directly, identifies H1/H2 separately, and does not use the incorrect square-root description.

## Handoff/archive integrity hardening

### Full 1008-member content root

For the currently published archive

- archive SHA-256: `f9a501670013f59ae56c3249e7e2daa9ff47d8b7ee1b50ba58acafd769acef12`
- member count: `1008`

all non-directory members were independently SHA-256 hashed. A deterministic root over sorted records

`path \0 uncompressed_size \0 member_sha256 \n`

is

`ef7d1d3572d0043b9b4fdeaebebfc45f8eeb4bc772550dbb9135e4525a7b1255`.

`CURRENT_ARCHIVE_MEMBER_ROOT.json` records this identity. `build_current_archive.py` now regenerates the member-root record when the archive is rebuilt, and `verify_handoff.py` now re-hashes **every archive member** and checks the root in addition to whole-ZIP SHA/size/count/CRC and the selected legacy state hashes.

### Git context / worktree integrity

The handoff verifier now also:

- rejects tracked working-tree or index drift from `HEAD` (untracked recovery outputs are ignored);
- checks ancestry with `merge-base --is-ancestor` when historical commit objects are available;
- handles missing historical objects in shallow clones as warnings only for released historical locks, never for a held lock;
- accepts detached HEAD only when it exactly matches the expected branch tip.

A historical `base_commit` is intentionally required to be an **ancestor**, not equal to HEAD; equality would be incorrect because the recorded base is historical by design.

## Journal external anchor

Muse correctly noted that an internally consistent hash chain without a second-medium anchor can be rewritten wholesale by an actor controlling the same repository. A same-repository constant would not solve that.

A Drive-side external snapshot anchor was therefore created for canonical `main` commit

`2461573739147763eb011faf03c344370a184d69`

and journal Git blob

`3f218adf24bab61f8fd4e74643306fbdadd577f1`.

Drive file ID: `1iB7TGc-BkY4IdLx4UjrZnRbyqqVqP11t`  
Local SHA-256 before upload: `837221871765bc3895047ef807ac35708e85a95dd985cb4f5ba9aaf332b04182`.

This is an independent-medium snapshot anchor, **not** claimed to be an immutable cryptographic timestamp authority. A future signed/timestamped release attestation would be stronger.

## Round-1 remediation still standing

The Round-1 repairs remain in force: controller raw-byte SHA serialization, exact integer threshold floor, stdlib pressure/continued-fraction scripts, rational interval certificates for `h_3` and `h_infinity`, B=4/r=640 table correction record, portable GOREV001 checker, explicit Collatz-cycle detection, and Git-context regression tests.

## What is intentionally NOT done yet

**PR #1 is not merged into `main`.** The current ZIP and its 1008-member root describe the pre-remediation published archive. The audit/tool changes on this PR branch are intentionally not represented as a new canonical archive build.

Before merge/canonical acceptance, the repository publication policy still requires an integrator transaction that rebuilds the deterministic archive from the accepted branch contents, regenerates the member root/build record, verifies the resulting archive, updates any required state/handoff/journal records, and performs GitHub/Drive read-back.

Therefore the correct current status is:

- Muse audit findings: reviewed and actionable defects repaired on PR branch;
- PR branch: improved and auditable;
- `main`: unchanged;
- canonical archive: not yet rebuilt from these repairs;
- Collatz: open;
- main research bottleneck: the required asymptotic bound on actual `W` (or helper `D_2`) remains open.
