# CP20 TASK8B3 E7R B4 V2 — Zero-Trust Pre-Execution Authorization Audit

Audit date: 2026-09-05
Repository: haliltalhaertan/Collatz
Scope: mechanical authorization/integrity audit only. No Stage 1 mathematics, no T1-T8, no invalid V1 Stage-1 mathematical drafts, no E8, no weighted/operator work.

## PRIMARY VERDICT

[AUDIT FAIL — DO NOT EXECUTE B4 V2 STAGE1]

## Load-bearing reason

The once-only B4 V2 Stage-1 authorization was already consumed by a real invocation of the actual sealed V2 Stage-1 entrypoint on branch `cp20-e7r-b4-v2-stage1-20260905`.

The persisted failure record at commit `04a66e41864d1d530ead63b1faeaf122048e3069` states:

- status: `[B4 V2 STAGE1 INPUT INTEGRITY FAILURE]`
- reason: `frozen dependency blob mismatch at Phase A: CURRENT_RESEARCH_STATE.json`
- authorization_consumed: `true`
- T1_T8: `NOT_EXECUTED`
- utc_timestamp: `2026-09-05T07:17:52.681686+00:00`

The sealed execution contract states that the actual V2 Stage-1 entrypoint may be invoked once only and that a failed real invocation consumes that authorization. Therefore the authorization created at Phase B is no longer available for any future invocation, even though no mathematics began.

## Mechanical root cause

The failure was not a random runner problem. The sealed config freezes `CURRENT_RESEARCH_STATE.json` inside `frozen_dependencies` to Git blob `3ba90bbf9e91ddc600235a38a800db90b03a07e0`, which is the blob at historical source base `8d274095b0e1acbe1fad0a73ef6a5293364902fc`. The launcher then checks every frozen dependency **at the Phase-A commit**. But Phase A `34ac0dbeb8c0ae2fddab706680f1682412b00786` necessarily changed `CURRENT_RESEARCH_STATE.json`; its actual Phase-A blob is `aa8daf546826853b720356ff96530f0b78ec197d`. Therefore the sealed launcher was structurally destined to reject the authorized Phase-A state at this check.

This is an integrity-contract/configuration defect, not a mathematical finding. A future repair must not merely re-authorize the same tuple: it must repair the frozen-dependency semantics (or bind the state file to the correct Phase-A object in a non-self-contradictory way), reseal, canonicalize, and only then issue a new once-only authorization.

## Requirement-by-requirement adjudication

1. PASS — current canonical `main` is `1a6f924fd86352c11f57a95b0382adaf92d15bcd`.
2. PASS — Phase-A `34ac0dbeb8c0ae2fddab706680f1682412b00786` is one commit after historical source base `8d274095b0e1acbe1fad0a73ef6a5293364902fc`; merge-base/ancestry check passed.
3. PASS — Phase-B authorization `f8d778a2113922e3bbb14c86ee2fa5359cee28ea` descends from Phase A.
4. PASS — final main `1a6f924fd86352c11f57a95b0382adaf92d15bcd` descends from Phase B.
5. PASS AS-OF CANONICAL MAIN, BUT NOW STALE — authoritative path is `CURRENT_RESEARCH_STATE.json["active_task"]["stage"]` and main records `STAGE_1_AUTHORIZED_NOT_EXECUTED`. This canonical statement predates the later real invocation and is no longer sufficient evidence that the authorization is unconsumed.
6. PASS — Phase-B authorization record binds exactly seal `11456b7d6f673e5cab6079850731cbda70373b77e4e0f532089d6783fd16c78e` and contract `7f2531743db7c2987d6efa785784852bc6fe066ccc23cfc607296de96f3eb403`, with Phase-A SHA `34ac0dbe...` and stage `STAGE_1_AUTHORIZED_NOT_EXECUTED`.
7. PASS — independently recomputed feasible SHA-256 values from raw Drive ZIP bytes; all requested canonical members match the supplied hashes.
8. PASS — sealed launcher control flow has no path to T1 START before seal/manifest verification, output-absence verification, authorization/canonical-state validation, complete RUN_WITNESS creation, witness validation, PRE_T1_GATE PASS, and gate ledger append. Static source inspection found no T1 START emitter in the launcher.
9. PASS — authoritative state lookup is strictly `active_task.stage`; missing path/wrong stage fails; legacy aliases are consistency checks only and conflicts fail.
10. PASS — source-level synthetic checks were independently re-run: S1-S11 observed expected FAIL behavior, S12 PASS; P1 PASS, P2-P5 expected FAIL, P6 PASS. Static control-flow checker independently returned PASS. These synthetic tests did not invoke the Stage-1 entrypoint.
11. PASS — independent GitHub Actions job-log retrieval for run `33917015405`, job `101166400966` shows checkout ref and actual HEAD `8d274095b0e1acbe1fad0a73ef6a5293364902fc`, command `python tools/verify_handoff.py`, and terminal `HANDOFF VERIFICATION: PASS`.
12. PASS — Drive file `1hWN1mdJdx78jnsOlD2ZXF8htkf9e8QGL` raw bytes were independently obtained; SHA-256 recomputed as `11456b7d6f673e5cab6079850731cbda70373b77e4e0f532089d6783fd16c78e`.
13. PASS — ZIP: 29 members; uniqueness PASS; sorted membership PASS; CRC PASS; manifest membership PASS; every manifested member hash PASS; deterministic rebuild at recorded ZIP metadata/deflate level 9 is byte-for-byte identical and has the same seal SHA.
14. PASS — independent comparison was restricted to canonical valid V1 Stage-0 scientific program files. V2 preserves definitions, falsification plan, outcome ladder, T1-T8 program, target normal form and scientific guardrails; no scientific claim changed. Invalid V1 Stage-1 mathematical drafts were not read.
15. FAIL — the claim that the once-only Stage-1 authorization has not already been consumed is false. A real launcher invocation occurred. It terminated before RUN_WITNESS/PRE_T1_GATE/T1 START because Phase-A `CURRENT_RESEARCH_STATE.json` did not match the frozen dependency blob. Mathematics did not execute, but the sealed contract explicitly consumes authorization on a failed real invocation.
16. PASS FOR CREATION COUNT / FAIL FOR AVAILABILITY — canonical Phase-B state records `authorization_count = 1` and commit search found one canonical `Authorize B4 V2 Stage1` authorization commit, `f8d778a2...`. No competing canonical authorization for a different accepted V2 seal was found. However that single authorization is now consumed, so available authorization count is effectively zero.
17. DERIVED, FORENSIC ONLY — exact sealed real invocation tuple is recorded below. It MUST NOT be invoked again under the consumed authorization.

## Independently recomputed hashes

- authorized Drive seal ZIP: `11456b7d6f673e5cab6079850731cbda70373b77e4e0f532089d6783fd16c78e`
- manifest: `7f48807db5733c85759324d4f94e357aa6941de0ecd911b4180f5bc2101d6dcb`
- contract: `7f2531743db7c2987d6efa785784852bc6fe066ccc23cfc607296de96f3eb403`
- config: `2fbc7bd09ab2cae89095b537342cf63c85f53f821d4ddf21c7860a2ec53b1f4b`
- launcher: `9222d0e0a8079e3560bc880520dd5ead44869f5fd4fa541520e225c841b8a732`
- witness schema: `c6e12499f3de2acb7fa34be81a4b54d5d0424abb351ca2fcbbc3ab7808447f01`
- PRE_T1 gate schema: `b6d7fe7602c291690d82d2bcde292403712003be1433878b247b22f1b24b55e2`
- validator: `59c7c81511602469387160cdd5e737eb862b40fb91950ed599147ad2aa699bdd`
- witness self-test results: `10132ba0a0e52a2ebee658174076824362ffe53f243cb1a44499df6f00477433`
- static-control results: `e52c52e572c1382d581278988f3917ee200472bdcb5efab5079bd56e5860aaaf`
- scientific diff report: `f4e2d05554976f898d6fbc943cf79e330d8869007f7ae83bac8858dd15c864a2`

## Exact consumed invocation tuple — DO NOT INVOKE

Canonical main HEAD checked by workflow before invocation:
`1a6f924fd86352c11f57a95b0382adaf92d15bcd`

Phase-A Stage0 base SHA:
`34ac0dbeb8c0ae2fddab706680f1682412b00786`

Phase-B authorization commit SHA:
`f8d778a2113922e3bbb14c86ee2fa5359cee28ea`

Authorized seal SHA:
`11456b7d6f673e5cab6079850731cbda70373b77e4e0f532089d6783fd16c78e`

Contract SHA:
`7f2531743db7c2987d6efa785784852bc6fe066ccc23cfc607296de96f3eb403`

Config SHA:
`2fbc7bd09ab2cae89095b537342cf63c85f53f821d4ddf21c7860a2ec53b1f4b`

Exact launcher:
`research_manager/results/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE0/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE1.py`

Exact CLI that was used:

```text
python \
  research_manager/results/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE0/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE1.py \
  --config research_manager/results/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE0/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_CONFIG.json \
  --seal /tmp/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_PRE_RUN_SEAL.zip \
  --canonical-stage0-base-sha 34ac0dbeb8c0ae2fddab706680f1682412b00786 \
  --authorization-commit-sha f8d778a2113922e3bbb14c86ee2fa5359cee28ea \
  --authorized-seal-sha256 11456b7d6f673e5cab6079850731cbda70373b77e4e0f532089d6783fd16c78e \
  --contract-sha256 7f2531743db7c2987d6efa785784852bc6fe066ccc23cfc607296de96f3eb403 \
  --output research_manager/results/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE0/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE1_RESULTS.json
```

This tuple is forensic evidence only. Reusing it would violate the sealed one-run discipline.

## Stage-1 execution trace adjudication

Real entrypoint invocation: YES.
RUN_WITNESS created: NO.
Witness validator PASS: NO (not reached).
PRE_T1_GATE created/PASS: NO.
Execution ledger PRE_T1_GATE PASS: NO.
Execution ledger T1 START: NO.
T1-T8 mathematics: NOT EXECUTED.
Stage-1 scientific result: NONE.
Authorization consumed: YES.

The failure occurred before mathematical execution, at the frozen Phase-A dependency check for `CURRENT_RESEARCH_STATE.json`.

## Scientific state retained unchanged

B4-N1 = NOT ESTABLISHED
B4-N2 = NOT ESTABLISHED
B4-N3 = NOT ESTABLISHED
B4-N4 = NOT ESTABLISHED
B4-N5 = NOT ESTABLISHED
B4-N6 = NOT ESTABLISHED
B4-N7 = NOT ESTABLISHED
B4-CT = NOT ESTABLISHED
E6-N2 = [OPEN]

Nothing in this audit proves the Collatz conjecture.

## Required corrective action before any future B4 V2 Stage-1 attempt

Do not rerun the consumed authorization. The repository must first perform a new mechanical repair/reseal or otherwise correct the Phase-A frozen dependency mismatch, then create a fresh explicit once-only authorization with a new authorization record/state transition and independently audit that new authorization before any real launcher invocation. This audit does not authorize such work and does not perform it.
