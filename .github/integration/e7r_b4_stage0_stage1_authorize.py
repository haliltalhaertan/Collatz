#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone, timedelta
from pathlib import Path
import hashlib
import json
import subprocess
import zipfile

REPO = Path.cwd()
REQUIRED_MAIN = "57f670bd531cee8f0f2d6eeb27431243f6e3a479"
STAGE0_BRANCH = "cp20-e7r-b4-tilted-microcanonical-fourier-v1-stage0-20260904"
STAGE0_HEAD = "c83d22f9e3ac8bdc4ec955d14b3d7dca11c3fee1"
TASK = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1"
TASK_NAME = "Tilted / Recentered Microcanonical Fourier Cancellation"
STAGE0_DIR = Path("research_manager/results/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE0")
SEAL_NAME = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_PRE_RUN_SEAL.zip"
MANIFEST_NAME = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_PRE_RUN_SHA256SUMS.txt"
CONTRACT_NAME = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_EXECUTION_INTEGRITY_AND_OUTPUT_CONTRACT.md"
SEAL_SHA = "ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c"
MANIFEST_SHA = "7de830b396fb075b4a97f78dd889ef16e92d66e763e5572af603f016faf33118"
CONTRACT_SHA = "3d9fd4c0c029c135b86c43377aa414c87704f5e6c3dd4a008fa621f3b4f1185e"
CONTRACT_BLOB = "94a15beb7573c860e4891048e705c9f13a156f04"
DRIVE_STAGE0_FOLDER_ID = "1n7sz5_1JFXAqJ1KUWT66Hy9KBzyvwnLI"
DRIVE_SEAL_FILE_ID = "12WfXfOfCHt9XZTSqBYPDfLV7xsZ1bVIY"
LOCK_HOLDER = "canonical-integrator-e7r-b4-stage0-stage1-authorization-20260904"
EXACT_NEXT = "Execute B4 Stage 1 exactly once under the authorized seal and canonical execution-integrity contract, adjudicating T1→T8 in frozen order."
STATE_PATH = Path("CURRENT_RESEARCH_STATE.json")
HANDOFF_PATH = Path("START_HERE_CURRENT_HANDOFF.md")
JOURNAL_PATH = Path("research_manager/RESEARCH_JOURNAL.jsonl")
ARCHIVE_PATH = Path("Collatz_Research_Archive_CURRENT.zip")
BUILD_PATH = Path("CURRENT_ARCHIVE_BUILD.json")
PHASE_A_DECISION = Path("research_manager/decisions/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE0_ACCEPTANCE_AND_CONTRACT_CANONICALIZATION_2026-09-04.md")
PHASE_A_READBACK = Path("research_manager/records/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_PHASE_A_READBACK_2026-09-04.json")
PHASE_B_DECISION = Path("research_manager/decisions/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_AUTHORIZATION_2026-09-04.md")
PHASE_B_PROMPT = Path("research_manager/prompts/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_MANAGER_AUTHORIZATION_PROMPT_2026-09-04.md")


def run(args, *, check=True, text=True, capture=True):
    proc = subprocess.run(args, cwd=REPO, check=False, text=text,
                          stdout=subprocess.PIPE if capture else None,
                          stderr=subprocess.PIPE if capture else None)
    if check and proc.returncode != 0:
        out = proc.stdout if proc.stdout is not None else ""
        err = proc.stderr if proc.stderr is not None else ""
        raise RuntimeError(f"command failed {args}:\n{out}\n{err}")
    return proc


def git(*args: str) -> str:
    return run(["git", *args]).stdout.strip()


def git_bytes(*args: str) -> bytes:
    return run(["git", *args], text=False).stdout


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def now_tr() -> str:
    return datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat()


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def write_state(state: dict) -> None:
    write_json(STATE_PATH, state)


def append_journal(active_stage: str, event: str, evidence: dict, next_action: str) -> None:
    raw_lines = JOURNAL_PATH.read_bytes().splitlines()
    previous = sha256_bytes(raw_lines[-1]) if raw_lines else None
    row = {
        "active_stage": active_stage,
        "active_task": TASK,
        "event": event,
        "evidence": evidence,
        "next_action": next_action,
        "previous_entry_sha256": previous,
        "schema": "COLLATZ_RESEARCH_JOURNAL_V1",
        "sequence": len(raw_lines) + 1,
        "timestamp": now_tr(),
    }
    encoded = json.dumps(row, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")
    with JOURNAL_PATH.open("ab") as f:
        f.write(encoded + b"\n")


def refresh_repository_integrity(state: dict) -> None:
    for row in state.get("integrity", {}).get("repository_files", []):
        path = Path(row["path"])
        if path == STATE_PATH:
            continue
        if path.is_file():
            row["sha256"] = sha256_file(path)


def refresh_archive_integrity(state: dict) -> bool:
    changed = False
    with zipfile.ZipFile(ARCHIVE_PATH) as zf:
        names = set(zf.namelist())
        for row in state.get("integrity", {}).get("archive_members", []):
            name = row["path"]
            if name in names:
                actual = sha256_bytes(zf.read(name))
                if row.get("sha256") != actual:
                    row["sha256"] = actual
                    changed = True
    return changed


def verify_stage0_checkout() -> list[str]:
    stage0_ref = f"origin/{STAGE0_BRANCH}"
    tracked = git("ls-tree", "-r", "--name-only", stage0_ref, str(STAGE0_DIR)).splitlines()
    if not tracked:
        raise AssertionError("Stage-0 directory is empty on authoritative branch")
    git("checkout", stage0_ref, "--", str(STAGE0_DIR))
    for path in tracked:
        expected_blob = git("rev-parse", f"{stage0_ref}:{path}")
        actual_blob = git("hash-object", path)
        if actual_blob != expected_blob:
            raise AssertionError(f"Stage-0 byte preservation failure: {path}")

    seal = STAGE0_DIR / SEAL_NAME
    manifest = STAGE0_DIR / MANIFEST_NAME
    contract = STAGE0_DIR / CONTRACT_NAME
    if sha256_file(seal) != SEAL_SHA:
        raise AssertionError("Stage-0 seal SHA mismatch")
    if sha256_file(manifest) != MANIFEST_SHA:
        raise AssertionError("Stage-0 manifest SHA mismatch")
    if sha256_file(contract) != CONTRACT_SHA:
        raise AssertionError("execution contract SHA mismatch")
    if git("hash-object", str(contract)) != CONTRACT_BLOB:
        raise AssertionError("execution contract Git blob mismatch")

    with zipfile.ZipFile(seal) as zf:
        infos = zf.infolist()
        names = [i.filename for i in infos]
        if len(names) != 16 or len(set(names)) != 16:
            raise AssertionError("Stage-0 seal member cardinality failure")
        if zf.testzip() is not None:
            raise AssertionError("Stage-0 seal CRC failure")
        manifest_bytes = zf.read(MANIFEST_NAME)
        if sha256_bytes(manifest_bytes) != MANIFEST_SHA:
            raise AssertionError("embedded manifest SHA mismatch")
        rows = [line for line in manifest_bytes.decode("utf-8").splitlines() if line.strip()]
        if len(rows) != 15:
            raise AssertionError("embedded manifest row count mismatch")
        for line in rows:
            digest, name = line.split("  ", 1)
            if name not in zf.namelist():
                raise AssertionError(f"manifested member missing: {name}")
            if sha256_bytes(zf.read(name)) != digest:
                raise AssertionError(f"manifested hash mismatch: {name}")
        if sha256_bytes(zf.read(CONTRACT_NAME)) != CONTRACT_SHA:
            raise AssertionError("embedded execution contract mismatch")

    forbidden_outputs = [
        "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_RUN_WITNESS.json",
        "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_RESULTS.json",
        "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_EXECUTION_LEDGER.jsonl",
    ]
    branch_paths = set(git("ls-tree", "-r", "--name-only", stage0_ref).splitlines())
    for name in forbidden_outputs:
        if any(p.endswith("/" + name) or p == name for p in branch_paths):
            raise AssertionError(f"Stage-1 output unexpectedly exists on Stage-0 branch: {name}")
    return tracked


def phase_a_handoff() -> str:
    contract_path = (STAGE0_DIR / CONTRACT_NAME).as_posix()
    return f"""# START HERE — Current Collatz Research Handoff

Machine-readable authority: `CURRENT_RESEARCH_STATE.json`.

## B4 two-phase governance status

Task: `{TASK}` — **{TASK_NAME}**.

**PHASE A COMPLETE — B4 STAGE 0 ACCEPTED; STAGE 1 NOT AUTHORIZED.**

The exact immutable Stage-1 execution-integrity contract has been canonicalized byte-for-byte at:
`{contract_path}`

Contract SHA-256: `{CONTRACT_SHA}`  
Contract Git blob from the authoritative Stage-0 branch: `{CONTRACT_BLOB}`

Accepted Stage-0 seal SHA-256: `{SEAL_SHA}`  
Stage-0 manifest SHA-256: `{MANIFEST_SHA}`  
Seal: 16 unique members, CRC PASS, manifested hashes PASS.  
Authoritative Stage-0 branch/head: `{STAGE0_BRANCH}` @ `{STAGE0_HEAD}`.  
Drive Stage-0 folder: `{DRIVE_STAGE0_FOLDER_ID}`; raw seal read-back: PASS.

`E6-N2` remains **[OPEN]**. No B4-N1 through B4-N7 is accepted by this Stage-0 intake.

Stage 1 is **NOT AUTHORIZED** and **NOT EXECUTED** in this Phase-A state. No weighted/operator work and no E8 work is authorized.

## Exact next management action

Perform canonical GitHub read-back of Phase A and require: the contract exists on `main`, its exact SHA-256/blob matches, and Stage 1 remains NOT AUTHORIZED. Only if all checks PASS may a separate Phase-B Stage-1 authorization decision be created.

Nothing in this Stage-0 acceptance proves the Collatz conjecture.
"""


def final_handoff(phase_a_sha: str) -> str:
    contract_path = (STAGE0_DIR / CONTRACT_NAME).as_posix()
    return f"""# START HERE — Current Collatz Research Handoff

Machine-readable authority: `CURRENT_RESEARCH_STATE.json`. Recover on branch `main`, run `python tools/verify_handoff.py`, and require `HANDOFF VERIFICATION: PASS` before any research action.

## B4 canonical status

Task: `{TASK}` — **{TASK_NAME}**.

**B4 Stage 0 is accepted.** Phase-A canonicalization commit: `{phase_a_sha}`.

The exact immutable Stage-1 execution-integrity contract was canonicalized before authorization at:
`{contract_path}`

Contract SHA-256: `{CONTRACT_SHA}`  
Contract Git blob: `{CONTRACT_BLOB}`

Authorized Stage-0 seal SHA-256: `{SEAL_SHA}`  
Stage-0 manifest SHA-256: `{MANIFEST_SHA}`  
Stage-0 branch/head: `{STAGE0_BRANCH}` @ `{STAGE0_HEAD}`.  
Drive Stage-0 folder: `{DRIVE_STAGE0_FOLDER_ID}`; Stage-0 seal raw read-back: PASS.

Phase-A canonical GitHub read-back: **PASS**. The contract existed with exact bytes/hash/blob and Stage 1 remained NOT AUTHORIZED before Phase B.

## Stage-1 authorization

Stage: `STAGE_1_AUTHORIZED_NOT_EXECUTED`.

Stage 1 is authorized **ONCE and ONLY** for seal `{SEAL_SHA}`, explicitly bound to the already-canonical contract SHA-256 `{CONTRACT_SHA}`. Every condition A–H of that canonical contract is mandatory without exception.

Stage 1 must adjudicate the frozen T1→T8 program in order. T8-A/T8-B may be entered only according to the frozen fallback logic after the direct T7 route is actually adjudicated.

Standing guardrails: tilting itself is not cancellation; Tao's existing p=1/2 theorem does not automatically transfer; Si's central `s~2n` theorem does not become applicable merely by changing reference measure; moving-frequency uniformity in `eta_r` is load-bearing; no independent global mod-16 cocycle may be introduced; B3-CT remains a falsification constraint.

Mandatory independent-audit stop fires immediately at a genuinely load-bearing B4-N5, B4-N6, B4-N7/E6-N2, a load-bearing B4-CT, or a downstream-dependent exact leading-coefficient cancellation/non-cancellation theorem. After a stop, all later T stages are `NOT_EXECUTED` and no rescue mathematics is permitted.

Any Stage-1 input-integrity failure must terminate as `[B4 STAGE1 INPUT INTEGRITY FAILURE]` and Stage 1 must not run.

`E6-N2` remains **[OPEN]** at authorization time. No B4 theorem is accepted by this authorization.

## Exact next action

{EXACT_NEXT}

Stage 1 has **NOT BEEN EXECUTED** by this canonical management transaction. No weighted/operator work and no E8 work was performed.

Nothing in this authorization proves the Collatz conjecture.
"""


def main() -> None:
    git("config", "user.name", "Canonical Integrator")
    git("config", "user.email", "actions@users.noreply.github.com")
    git("fetch", "origin", "main", STAGE0_BRANCH)
    if git("rev-parse", "HEAD") != REQUIRED_MAIN:
        raise AssertionError("checkout is not required canonical main")
    if git("rev-parse", "origin/main") != REQUIRED_MAIN:
        raise AssertionError("origin/main moved before transaction")
    if git("rev-parse", f"origin/{STAGE0_BRANCH}") != STAGE0_HEAD:
        raise AssertionError("Stage-0 branch HEAD mismatch")
    run(["git", "merge-base", "--is-ancestor", REQUIRED_MAIN, STAGE0_HEAD])

    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if state["active_integrator"]["status"] != "RELEASED":
        raise AssertionError("active_integrator lock is not RELEASED")
    if state["active_task"]["code"] != TASK or state["active_task"]["stage"] != "STAGE_0_READY_NOT_DISPATCHED":
        raise AssertionError("canonical active task/stage mismatch")

    # First canonical write: acquire lock only.
    state["active_integrator"] = {
        "acquired_at": now_tr(),
        "base_commit": REQUIRED_MAIN,
        "holder": LOCK_HOLDER,
        "scope": "B4 Stage-0 canonical intake plus two-phase Stage-1 authorization only; no Stage-1 execution, no new mathematics, no weighted/operator work, and no E8.",
        "status": "HELD",
    }
    write_state(state)
    git("add", str(STATE_PATH))
    git("commit", "-m", "Acquire integrator lock for B4 two-phase authorization")
    lock_sha = git("rev-parse", "HEAD")
    git("push", "origin", "HEAD:main")
    git("fetch", "origin", "main")
    if git("rev-parse", "origin/main") != lock_sha:
        raise AssertionError("lock commit GitHub read-back failure")

    # PHASE A — canonicalize Stage 0 + exact contract; keep Stage 1 unauthorized.
    tracked = verify_stage0_checkout()
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    state["active_integrator"]["lock_acquisition_commit"] = lock_sha
    state["active_task"]["stage"] = "PRE_RUN_SEAL_AWAITING_AUTHORIZATION"
    state.setdefault("b4_stage0", {})
    state["b4_stage0"] = {
        "accepted": True,
        "accepted_claims": [],
        "contract_git_blob": CONTRACT_BLOB,
        "contract_sha256": CONTRACT_SHA,
        "drive_raw_seal_readback": "PASS",
        "drive_seal_file_id": DRIVE_SEAL_FILE_ID,
        "drive_stage0_folder_id": DRIVE_STAGE0_FOLDER_ID,
        "manifest_sha256": MANIFEST_SHA,
        "seal_crc": "PASS",
        "seal_member_count": 16,
        "seal_member_hashes": "PASS",
        "seal_sha256": SEAL_SHA,
        "stage0_branch": STAGE0_BRANCH,
        "stage0_head": STAGE0_HEAD,
        "stage1_authorized": False,
        "stage1_executed": False,
        "status": "[ACCEPT B4 STAGE 0]",
    }
    state["b4_frozen_program"] = {
        "T1": "conditional-law invariance",
        "T2": "tilted centrality",
        "T3": "denominator / local limit",
        "T4": "numerator and G_r=N_r/D_r",
        "T5": "required N_r=O(r^-3/2) scale",
        "T6": "exact total-sum Fourier inversion",
        "T7": "new tilted joint Fourier/renewal theorem",
        "T8-A": "saddlepoint/Edgeworth fallback",
        "T8-B": "endpoint-weighted/cotransition fallback",
        "falsifications": "F1...F10 and T7-F1...T7-F5 frozen",
    }
    docs = state.setdefault("documents", {})
    docs["accepted_checkpoint_decision"] = PHASE_A_DECISION.as_posix()
    docs["active_authorization_decision"] = None
    docs["active_authorization_prompt"] = None
    docs["active_research_prompt"] = None
    docs["b4_stage1_execution_contract"] = (STAGE0_DIR / CONTRACT_NAME).as_posix()
    na = state.setdefault("next_action", {})
    na["instruction"] = "Perform Phase-A canonical GitHub read-back and verify the exact execution-integrity contract is present byte-for-byte while Stage 1 remains NOT AUTHORIZED. Proceed to separate Phase B only after PASS."
    na["task_code"] = TASK
    na["stage"] = "PRE_RUN_SEAL_AWAITING_AUTHORIZATION"

    PHASE_A_DECISION.parent.mkdir(parents=True, exist_ok=True)
    PHASE_A_DECISION.write_text(f"""# {TASK} — PHASE A STAGE-0 ACCEPTANCE + CONTRACT CANONICALIZATION

Manager verdict: **[ACCEPT B4 STAGE 0]**

Canonical base: `{REQUIRED_MAIN}`  
Authoritative Stage-0 branch/head: `{STAGE0_BRANCH}` @ `{STAGE0_HEAD}`

Accepted Stage-0 seal SHA-256: `{SEAL_SHA}`  
Stage-0 manifest SHA-256: `{MANIFEST_SHA}`  
Seal integrity: 16 unique members; CRC PASS; manifested hashes PASS.

The exact immutable Stage-1 execution-integrity contract is canonicalized byte-for-byte, without rewrite or paraphrase, at `{(STAGE0_DIR / CONTRACT_NAME).as_posix()}`.

Contract SHA-256: `{CONTRACT_SHA}`  
Authoritative Stage-0 Git blob: `{CONTRACT_BLOB}`.

Drive Stage-0 folder: `{DRIVE_STAGE0_FOLDER_ID}`  
Drive seal file: `{DRIVE_SEAL_FILE_ID}`  
Raw Drive seal read-back: PASS.

`E6-N2` remains `[OPEN]`. No B4-N1...B4-N7 is accepted by this intake.

**STAGE 1 IS NOT AUTHORIZED IN PHASE A. STAGE 1 HAS NOT BEEN EXECUTED.**

Phase B is forbidden until canonical GitHub read-back verifies the exact contract and the NOT-AUTHORIZED state.

Nothing in this decision proves the Collatz conjecture.
""", encoding="utf-8", newline="\n")

    HANDOFF_PATH.write_text(phase_a_handoff(), encoding="utf-8", newline="\n")
    append_journal(
        "PRE_RUN_SEAL_AWAITING_AUTHORIZATION",
        "B4_STAGE0_ACCEPTED_CONTRACT_CANONICALIZED",
        {
            "contract_git_blob": CONTRACT_BLOB,
            "contract_sha256": CONTRACT_SHA,
            "drive_raw_seal_readback": "PASS",
            "drive_stage0_folder_id": DRIVE_STAGE0_FOLDER_ID,
            "seal_sha256": SEAL_SHA,
            "stage0_branch_head": STAGE0_HEAD,
            "stage0_manifest_sha256": MANIFEST_SHA,
            "stage0_sealed_files_preserved_byte_for_byte": len(tracked),
            "stage1_authorized": False,
            "stage1_executed": False,
        },
        "Perform Phase-A canonical GitHub read-back; proceed to a separate Stage-1 authorization only if contract hash/blob and NOT-AUTHORIZED state all pass.",
    )
    write_state(state)
    git("add", "-A")
    git("commit", "-m", "Canonicalize B4 Stage0 and execution contract")
    phase_a_sha = git("rev-parse", "HEAD")
    git("push", "origin", "HEAD:main")
    git("fetch", "origin", "main")
    if git("rev-parse", "origin/main") != phase_a_sha:
        raise AssertionError("Phase-A commit GitHub read-back failure")

    contract_path = (STAGE0_DIR / CONTRACT_NAME).as_posix()
    rb_contract = git_bytes("show", f"origin/main:{contract_path}")
    rb_contract_sha = sha256_bytes(rb_contract)
    rb_contract_blob = git("rev-parse", f"origin/main:{contract_path}")
    rb_state = json.loads(git_bytes("show", "origin/main:CURRENT_RESEARCH_STATE.json").decode("utf-8"))
    phase_a_pass = (
        rb_contract_sha == CONTRACT_SHA
        and rb_contract_blob == CONTRACT_BLOB
        and rb_state["active_task"]["stage"] == "PRE_RUN_SEAL_AWAITING_AUTHORIZATION"
        and rb_state.get("b4_stage0", {}).get("stage1_authorized") is False
        and rb_state.get("documents", {}).get("active_authorization_decision") is None
    )
    if not phase_a_pass:
        raise AssertionError("PHASE A READ-BACK FAIL — Phase B forbidden")
    write_json(PHASE_A_READBACK, {
        "contract_blob_readback": rb_contract_blob,
        "contract_sha256_readback": rb_contract_sha,
        "phase_a_commit": phase_a_sha,
        "stage1_authorized_readback": False,
        "verdict": "PASS",
    })

    # PHASE B — separate Stage-1 authorization, only after Phase-A read-back PASS.
    PHASE_B_DECISION.parent.mkdir(parents=True, exist_ok=True)
    PHASE_B_DECISION.write_text(f"""# {TASK} — PHASE B STAGE-1 AUTHORIZATION

Phase-A canonicalization commit: `{phase_a_sha}`  
Phase-A canonical GitHub read-back: **PASS**.

## Authorization

Stage 1 is authorized **ONCE and ONLY** for the immutable Stage-0 seal SHA-256:

`{SEAL_SHA}`

This authorization is explicitly bound to the already-canonical execution-integrity contract SHA-256:

`{CONTRACT_SHA}`

Canonical contract path: `{contract_path}`  
Canonical contract Git blob: `{CONTRACT_BLOB}`.

The full canonical contract is incorporated by reference **byte-for-byte**. Every condition in Sections A–H is mandatory, including without limitation:

- exact authorized seal SHA verification;
- exact manifest byte/member verification, 16 unique members, sorted-name/cardinality and CRC checks;
- dependency verification against the frozen canonical base and prerequisite blobs;
- declared Stage-1 output absence before execution;
- exactly one pre-T1 `RUN_WITNESS` carrying UTC timestamp, authorized seal, canonical base, execution identity/session identifier and output-absence verdict;
- the exact sealed Stage-1 entrypoint and exact config/seal arguments;
- an append-only T/M execution ledger;
- exactly one invocation and no source repair, modification, retry or rerun after observed output;
- immediate mandatory stop-rule enforcement;
- post-stop evidence marking every later T-stage `NOT_EXECUTED`, with no rescue mathematics;
- final result/package creation, exact manifest/package SHA-256, membership/uniqueness/CRC verification;
- Google Drive save plus raw byte/hash read-back;
- GitHub result-branch persistence without force plus GitHub read-back.

Any pre-execution input-integrity failure must terminate exactly as:

`[B4 STAGE1 INPUT INTEGRITY FAILURE]`

and Stage 1 must not run.

## Frozen scientific scope

Adjudicate T1→T8 in frozen order. Stage 1 may establish B4-N1 through B4-N4 and then adjudicate the direct T7 joint-transform route. T8-A/T8-B are permitted only according to the frozen fallback logic after the direct T7 route has actually been adjudicated.

Tilting itself is not cancellation. Tao p=1/2 and Si central-fiber theorems do not automatically transfer. Moving `eta_r` frequency-uniformity is load-bearing. No independent global mod-16 cocycle may be introduced. B3-CT remains a falsification constraint.

Mandatory independent-audit stop: B4-N5 if genuinely load-bearing; B4-N6; B4-N7/E6-N2; a load-bearing B4-CT; or any exact leading-coefficient cancellation/non-cancellation theorem on which downstream work depends. After a stop, later T stages are `NOT_EXECUTED` and no rescue mathematics is allowed.

Stage after this decision: `STAGE_1_AUTHORIZED_NOT_EXECUTED`.

Exact next action: **{EXACT_NEXT}**

This decision does not execute Stage 1 and does not accept any B4 theorem. `E6-N2` remains `[OPEN]`.

Nothing in this authorization proves the Collatz conjecture.
""", encoding="utf-8", newline="\n")

    PHASE_B_PROMPT.parent.mkdir(parents=True, exist_ok=True)
    PHASE_B_PROMPT.write_text(f"""# {TASK} — STAGE-1 MANAGER AUTHORIZATION PROMPT

Authorization status: `STAGE_1_AUTHORIZED_NOT_EXECUTED`.

Execute Stage 1 **exactly once** and only under all of the following bindings:

- authorized seal SHA-256: `{SEAL_SHA}`;
- already-canonical execution-integrity contract SHA-256: `{CONTRACT_SHA}`;
- canonical contract path: `{contract_path}`;
- Phase-A canonicalization commit: `{phase_a_sha}`;
- Phase-A read-back verdict: `PASS`.

Before any mathematical action, satisfy every condition A–H of the canonical execution-integrity contract byte-for-byte. On any input-integrity failure terminate as `[B4 STAGE1 INPUT INTEGRITY FAILURE]` and do not run Stage 1.

Adjudicate T1→T8 in the frozen order and obey the frozen F1...F10 and T7-F1...T7-F5 falsifications. Do not treat tilting as cancellation, do not auto-transfer Tao p=1/2 or Si central-fiber theorems, require moving-frequency uniformity, introduce no independent global mod-16 cocycle, and keep B3-CT as a standing falsification constraint.

Fire the mandatory independent-audit stop immediately at a genuinely load-bearing B4-N5, B4-N6, B4-N7/E6-N2, a load-bearing B4-CT, or a downstream-dependent exact leading-coefficient cancellation/non-cancellation theorem. Mark all later T stages `NOT_EXECUTED`; do no rescue mathematics.

T8-A/T8-B may begin only if the frozen fallback logic permits them after direct T7 adjudication.

No weighted/operator work outside the frozen T8-B fallback and no E8 work is authorized.

Return the complete result/provenance/package/hash/Drive/GitHub read-back record required by the canonical contract. Do not rerun.

Nothing in this authorization proves the Collatz conjecture.
""", encoding="utf-8", newline="\n")

    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    state["active_task"]["stage"] = "STAGE_1_AUTHORIZED_NOT_EXECUTED"
    state["active_integrator"]["status"] = "RELEASED"
    state["active_integrator"]["lock_acquisition_commit"] = lock_sha
    state["b4_stage0"]["stage1_authorized"] = True
    state["b4_stage0"]["stage1_executed"] = False
    state["b4_stage0"]["phase_a_canonicalization_commit"] = phase_a_sha
    state["b4_stage0"]["phase_a_readback"] = "PASS"
    state["stage1_authorization"] = {
        "authorization_count": 1,
        "authorized_seal_sha256": SEAL_SHA,
        "canonical_contract_sha256": CONTRACT_SHA,
        "canonical_contract_git_blob": CONTRACT_BLOB,
        "phase_a_commit": phase_a_sha,
        "phase_a_readback": "PASS",
        "stage1_executed": False,
        "status": "STAGE_1_AUTHORIZED_NOT_EXECUTED",
    }
    docs = state["documents"]
    docs["active_authorization_decision"] = PHASE_B_DECISION.as_posix()
    docs["active_authorization_prompt"] = PHASE_B_PROMPT.as_posix()
    docs["active_research_prompt"] = PHASE_B_PROMPT.as_posix()
    state.setdefault("continuity", {})["minimum_required_commit"] = phase_a_sha
    na = state.setdefault("next_action", {})
    na["instruction"] = EXACT_NEXT
    na["task_code"] = TASK
    na["stage"] = "STAGE_1_AUTHORIZED_NOT_EXECUTED"
    HANDOFF_PATH.write_text(final_handoff(phase_a_sha), encoding="utf-8", newline="\n")
    append_journal(
        "STAGE_1_AUTHORIZED_NOT_EXECUTED",
        "B4_STAGE1_AUTHORIZED_AFTER_CONTRACT_READBACK",
        {
            "authorization_count": 1,
            "canonical_contract_git_blob": CONTRACT_BLOB,
            "canonical_contract_sha256": CONTRACT_SHA,
            "phase_a_commit": phase_a_sha,
            "phase_a_readback": "PASS",
            "seal_sha256": SEAL_SHA,
            "stage1_authorized": True,
            "stage1_executed": False,
        },
        EXACT_NEXT,
    )
    write_state(state)

    # Final archive + integrity stabilization; no Stage-1 entrypoint is invoked anywhere in this transaction.
    refresh_repository_integrity(state)
    write_state(state)
    run(["python", "tools/build_current_archive.py"])
    if refresh_archive_integrity(state):
        write_state(state)
        refresh_repository_integrity(state)
        write_state(state)
        run(["python", "tools/build_current_archive.py"])
    else:
        refresh_repository_integrity(state)
        write_state(state)
        run(["python", "tools/build_current_archive.py"])

    # One final archive-member refresh if needed, then one final deterministic rebuild.
    if refresh_archive_integrity(state):
        write_state(state)
        refresh_repository_integrity(state)
        write_state(state)
        run(["python", "tools/build_current_archive.py"])

    # Validate before final commit while still on main.
    pre_verify = run(["python", "tools/verify_handoff.py"]).stdout
    if "HANDOFF VERIFICATION: PASS" not in pre_verify:
        raise AssertionError("pre-push handoff verification did not PASS")

    # Ensure forbidden Stage-1 outputs have not appeared.
    forbidden_outputs = {
        "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_RUN_WITNESS.json",
        "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_RESULTS.json",
        "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_EXECUTION_LEDGER.jsonl",
    }
    for p in REPO.rglob("*"):
        if p.is_file() and p.name in forbidden_outputs:
            raise AssertionError(f"Stage 1 output exists unexpectedly: {p}")

    git("add", "-A")
    git("commit", "-m", "Authorize B4 Stage1 under canonical execution contract")
    phase_b_sha = git("rev-parse", "HEAD")
    git("push", "origin", "HEAD:main")
    git("fetch", "origin", "main")
    if git("rev-parse", "origin/main") != phase_b_sha:
        raise AssertionError("Phase-B/final GitHub read-back failure")

    # Final canonical GitHub read-back and verifier on the published commit.
    final_verify = run(["python", "tools/verify_handoff.py"]).stdout
    if "HANDOFF VERIFICATION: PASS" not in final_verify:
        raise AssertionError("final published handoff verification did not PASS")
    rb_contract_final = git_bytes("show", f"origin/main:{contract_path}")
    rb_state_final = json.loads(git_bytes("show", "origin/main:CURRENT_RESEARCH_STATE.json").decode("utf-8"))
    if sha256_bytes(rb_contract_final) != CONTRACT_SHA:
        raise AssertionError("final contract SHA read-back mismatch")
    if git("rev-parse", f"origin/main:{contract_path}") != CONTRACT_BLOB:
        raise AssertionError("final contract blob read-back mismatch")
    if rb_state_final["active_task"]["stage"] != "STAGE_1_AUTHORIZED_NOT_EXECUTED":
        raise AssertionError("final active stage mismatch")
    if rb_state_final["active_integrator"]["status"] != "RELEASED":
        raise AssertionError("final integrator lock not released")
    if rb_state_final.get("stage1_authorization", {}).get("stage1_executed") is not False:
        raise AssertionError("final state does not record Stage 1 NOT EXECUTED")

    build = json.loads(BUILD_PATH.read_text(encoding="utf-8"))
    archive_bytes = ARCHIVE_PATH.stat().st_size
    if archive_bytes != build["zip_bytes"]:
        raise AssertionError("archive build-record byte mismatch")
    if sha256_file(ARCHIVE_PATH) != build["archive_sha256"]:
        raise AssertionError("archive build-record SHA mismatch")
    headroom = 100_000_000 - archive_bytes

    Path("FINAL_HANDOFF_VERIFICATION.txt").write_text(final_verify, encoding="utf-8", newline="\n")
    write_json(Path("GITHUB_READBACK.json"), {
        "contract_git_blob": CONTRACT_BLOB,
        "contract_sha256": CONTRACT_SHA,
        "final_main": phase_b_sha,
        "integrator_lock": "RELEASED",
        "phase_a_commit": phase_a_sha,
        "phase_a_readback": "PASS",
        "stage": "STAGE_1_AUTHORIZED_NOT_EXECUTED",
        "stage1_executed": False,
        "verdict": "PASS",
    })
    write_json(Path("ARCHIVE_BUDGET.json"), {
        "archive_bytes": archive_bytes,
        "archive_sha256": build["archive_sha256"],
        "hard_limit_bytes": 100_000_000,
        "headroom_bytes": headroom,
    })
    write_json(Path("CANONICAL_TRANSACTION_SUMMARY.json"), {
        "archive_bytes": archive_bytes,
        "archive_sha256": build["archive_sha256"],
        "contract_sha256": CONTRACT_SHA,
        "final_main": phase_b_sha,
        "handoff_verification": "PASS",
        "headroom_bytes": headroom,
        "phase_a_commit": phase_a_sha,
        "phase_a_contract_readback": "PASS",
        "phase_b_authorization_commit": phase_b_sha,
        "seal_sha256": SEAL_SHA,
        "stage1_executed": False,
    })
    Path("PHASE_A_COMMIT.txt").write_text(phase_a_sha + "\n", encoding="utf-8")
    Path("PHASE_B_COMMIT.txt").write_text(phase_b_sha + "\n", encoding="utf-8")
    Path("FINAL_SHA.txt").write_text(phase_b_sha + "\n", encoding="utf-8")
    print(json.dumps({
        "archive_bytes": archive_bytes,
        "archive_sha256": build["archive_sha256"],
        "contract_sha256": CONTRACT_SHA,
        "final_sha": phase_b_sha,
        "headroom": headroom,
        "lock_sha": lock_sha,
        "phase_a_sha": phase_a_sha,
        "phase_b_sha": phase_b_sha,
        "seal_sha256": SEAL_SHA,
        "stage1_executed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
