#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone, timedelta
from pathlib import Path
import hashlib
import json
import subprocess
import zipfile

REPO = Path.cwd()
REQUIRED_BASE = "57f670bd531cee8f0f2d6eeb27431243f6e3a479"
EXISTING_LOCK_SHA = "060c9129aac5562e4b2b8c32634159c71579132b"
LOCK_HOLDER = "canonical-integrator-e7r-b4-stage0-stage1-authorization-20260904"
STAGE0_BRANCH = "cp20-e7r-b4-tilted-microcanonical-fourier-v1-stage0-20260904"
STAGE0_HEAD = "c83d22f9e3ac8bdc4ec955d14b3d7dca11c3fee1"
TASK = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1"
TASK_NAME = "Tilted / Recentered Microcanonical Fourier Cancellation"
STAGE0_DIR = Path("research_manager/results/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE0")
MANIFEST_NAME = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_PRE_RUN_SHA256SUMS.txt"
CONTRACT_NAME = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_EXECUTION_INTEGRITY_AND_OUTPUT_CONTRACT.md"
SEAL_SHA = "ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c"
MANIFEST_SHA = "7de830b396fb075b4a97f78dd889ef16e92d66e763e5572af603f016faf33118"
CONTRACT_SHA = "3d9fd4c0c029c135b86c43377aa414c87704f5e6c3dd4a008fa621f3b4f1185e"
CONTRACT_BLOB = "94a15beb7573c860e4891048e705c9f13a156f04"
DRIVE_STAGE0_FOLDER_ID = "1n7sz5_1JFXAqJ1KUWT66Hy9KBzyvwnLI"
DRIVE_SEAL_FILE_ID = "12WfXfOfCHt9XZTSqBYPDfLV7xsZ1bVIY"
EXACT_NEXT = "Execute B4 Stage 1 exactly once under the authorized seal and canonical execution-integrity contract, adjudicating T1→T8 in frozen order."

STATE = Path("CURRENT_RESEARCH_STATE.json")
HANDOFF = Path("START_HERE_CURRENT_HANDOFF.md")
JOURNAL = Path("research_manager/RESEARCH_JOURNAL.jsonl")
ARCHIVE = Path("Collatz_Research_Archive_CURRENT.zip")
BUILD = Path("CURRENT_ARCHIVE_BUILD.json")
PHASE_A_DECISION = Path("research_manager/decisions/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE0_ACCEPTANCE_AND_CONTRACT_CANONICALIZATION_2026-09-04.md")
PHASE_A_READBACK = Path("research_manager/records/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_PHASE_A_READBACK_2026-09-04.json")
PHASE_B_DECISION = Path("research_manager/decisions/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_AUTHORIZATION_2026-09-04.md")
PHASE_B_PROMPT = Path("research_manager/prompts/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_MANAGER_AUTHORIZATION_PROMPT_2026-09-04.md")


def proc(args, *, text=True, check=True):
    p = subprocess.run(args, cwd=REPO, text=text, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if check and p.returncode:
        raise RuntimeError(f"command failed {args}:\n{p.stdout}\n{p.stderr}")
    return p


def git(*args):
    return proc(["git", *args]).stdout.strip()


def git_bytes(*args):
    return proc(["git", *args], text=False).stdout


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest_file(path: Path) -> str:
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


def load_state() -> dict:
    return json.loads(STATE.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    write_json(STATE, state)


def append_journal(stage: str, event: str, evidence: dict, next_action: str) -> None:
    lines = JOURNAL.read_bytes().splitlines()
    prev = digest_bytes(lines[-1]) if lines else None
    row = {
        "active_stage": stage,
        "active_task": TASK,
        "event": event,
        "evidence": evidence,
        "next_action": next_action,
        "previous_entry_sha256": prev,
        "schema": "COLLATZ_RESEARCH_JOURNAL_V1",
        "sequence": len(lines) + 1,
        "timestamp": now_tr(),
    }
    encoded = json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    with JOURNAL.open("ab") as f:
        f.write(encoded + b"\n")


def verify_and_checkout_stage0() -> list[str]:
    ref = f"origin/{STAGE0_BRANCH}"
    tracked = git("ls-tree", "-r", "--name-only", ref, str(STAGE0_DIR)).splitlines()
    if not tracked:
        raise AssertionError("authoritative Stage-0 directory missing")
    git("checkout", ref, "--", str(STAGE0_DIR))

    # Preserve every tracked Stage-0 artifact byte-for-byte.
    for path in tracked:
        if git("hash-object", path) != git("rev-parse", f"{ref}:{path}"):
            raise AssertionError(f"Stage-0 byte mismatch: {path}")

    manifest = STAGE0_DIR / MANIFEST_NAME
    contract = STAGE0_DIR / CONTRACT_NAME
    if digest_file(manifest) != MANIFEST_SHA:
        raise AssertionError("Stage-0 manifest SHA mismatch")
    if digest_file(contract) != CONTRACT_SHA:
        raise AssertionError("execution contract SHA mismatch")
    if git("hash-object", str(contract)) != CONTRACT_BLOB:
        raise AssertionError("execution contract Git blob mismatch")

    # The seal ZIP is deliberately Drive-only. Verify the 16 sealed members from
    # the authoritative branch manifest; the raw ZIP SHA/CRC was independently
    # read back from Drive during canonical intake before this transaction.
    rows = [line for line in manifest.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(rows) != 15:
        raise AssertionError("Stage-0 manifest must contain 15 member rows")
    sealed = [str(manifest)]
    for line in rows:
        expected, name = line.split("  ", 1)
        path = STAGE0_DIR / name
        if not path.is_file():
            raise AssertionError(f"manifested Stage-0 member missing: {name}")
        if digest_file(path) != expected:
            raise AssertionError(f"manifested Stage-0 member hash mismatch: {name}")
        sealed.append(str(path))
    if len(sealed) != 16 or len(set(sealed)) != 16:
        raise AssertionError("sealed member cardinality mismatch")

    forbidden = {
        "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_RUN_WITNESS.json",
        "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_RESULTS.json",
        "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_EXECUTION_LEDGER.jsonl",
    }
    for path in tracked:
        if Path(path).name in forbidden:
            raise AssertionError(f"Stage-1 output exists on Stage-0 branch: {path}")
    return sealed


def phase_a_handoff() -> str:
    cp = (STAGE0_DIR / CONTRACT_NAME).as_posix()
    return f"""# START HERE — Current Collatz Research Handoff

Machine-readable authority: `CURRENT_RESEARCH_STATE.json`.

## B4 Phase A — canonical Stage-0 intake

Task: `{TASK}` — **{TASK_NAME}**.

**B4 Stage 0 is accepted. Stage 1 is NOT AUTHORIZED and NOT EXECUTED.**

Authoritative Stage-0 branch/head: `{STAGE0_BRANCH}` @ `{STAGE0_HEAD}`.  
Stage-0 seal SHA-256: `{SEAL_SHA}`.  
Stage-0 manifest SHA-256: `{MANIFEST_SHA}`.  
Seal integrity from canonical intake: 16 unique members, CRC PASS, manifested hashes PASS.  
Drive Stage-0 folder: `{DRIVE_STAGE0_FOLDER_ID}`.  
Drive seal file: `{DRIVE_SEAL_FILE_ID}`. Raw Drive seal read-back: PASS.

The seal ZIP remains Drive-only under archive policy. Its 16 sealed members are preserved byte-for-byte on canonical `main` from the authoritative Stage-0 branch.

The exact immutable execution-integrity contract is canonicalized without rewrite at `{cp}`.  
Contract SHA-256: `{CONTRACT_SHA}`.  
Contract Git blob: `{CONTRACT_BLOB}`.

`E6-N2` remains `[OPEN]`. No B4-N1...B4-N7 is accepted by Stage 0.

### Exact next management action

Perform Phase-A GitHub read-back. Require all 16 sealed member blobs to be byte-identical to the Stage-0 branch, require the contract SHA/blob to match, and require Stage 1 to remain NOT AUTHORIZED. Phase B is forbidden unless all checks PASS.

No weighted/operator work or E8 work is authorized. Nothing here proves the Collatz conjecture.
"""


def final_handoff(phase_a_sha: str) -> str:
    cp = (STAGE0_DIR / CONTRACT_NAME).as_posix()
    return f"""# START HERE — Current Collatz Research Handoff

Machine-readable authority: `CURRENT_RESEARCH_STATE.json`. Recover on branch `main`, run `python tools/verify_handoff.py`, and require `HANDOFF VERIFICATION: PASS` before any research action.

## B4 accepted Stage 0 and two-phase authorization

Task: `{TASK}` — **{TASK_NAME}**.

Phase-A canonicalization commit: `{phase_a_sha}`. Phase-A canonical GitHub read-back: **PASS**.

Stage-0 seal SHA-256: `{SEAL_SHA}`.  
Stage-0 manifest SHA-256: `{MANIFEST_SHA}`.  
Authoritative branch/head: `{STAGE0_BRANCH}` @ `{STAGE0_HEAD}`.  
Drive Stage-0 folder: `{DRIVE_STAGE0_FOLDER_ID}`; Drive seal raw read-back: PASS.  
The Drive-only seal ZIP is referenced by exact SHA; all 16 sealed members are byte-identical on canonical `main`.

Execution-integrity contract path: `{cp}`  
Contract SHA-256: `{CONTRACT_SHA}`  
Contract Git blob: `{CONTRACT_BLOB}`

The contract was canonicalized in Phase A before authorization. Phase B authorizes Stage 1 **ONCE and ONLY** for the above seal and explicitly binds every condition A–H of the already-canonical contract.

Canonical stage: `STAGE_1_AUTHORIZED_NOT_EXECUTED`.

`E6-N2` remains `[OPEN]`. No B4 theorem is accepted by authorization.

Stage 1 must adjudicate frozen T1→T8 in order. T8-A/T8-B may be entered only under the frozen fallback logic after direct T7 adjudication. Tilting is not cancellation; Tao p=1/2 and Si central-fiber results do not automatically transfer; moving `eta_r` uniformity is load-bearing; no independent global mod-16 cocycle may be introduced; B3-CT remains a falsification constraint.

Mandatory independent-audit stop fires at a genuinely load-bearing B4-N5, B4-N6, B4-N7/E6-N2, a load-bearing B4-CT, or an exact downstream-dependent leading-coefficient cancellation/non-cancellation theorem. After a stop all later T stages are `NOT_EXECUTED`; no rescue mathematics.

Any input-integrity failure must terminate as `[B4 STAGE1 INPUT INTEGRITY FAILURE]` and Stage 1 must not run.

## Exact next action

{EXACT_NEXT}

Stage 1 was **NOT EXECUTED** by this management transaction. No weighted/operator work and no E8 work was performed.

Nothing in this authorization proves the Collatz conjecture.
"""


def refresh_repository_integrity(state: dict) -> None:
    for row in state.get("integrity", {}).get("repository_files", []):
        p = Path(row["path"])
        if p == STATE:
            continue
        if p.is_file():
            row["sha256"] = digest_file(p)


def refresh_archive_integrity(state: dict) -> bool:
    changed = False
    with zipfile.ZipFile(ARCHIVE) as zf:
        names = set(zf.namelist())
        for row in state.get("integrity", {}).get("archive_members", []):
            name = row["path"]
            if name in names:
                actual = digest_bytes(zf.read(name))
                if row.get("sha256") != actual:
                    row["sha256"] = actual
                    changed = True
    return changed


def stabilize_archive(state: dict) -> None:
    refresh_repository_integrity(state)
    save_state(state)
    proc(["python", "tools/build_current_archive.py"])
    for _ in range(3):
        changed = refresh_archive_integrity(state)
        refresh_repository_integrity(state)
        save_state(state)
        proc(["python", "tools/build_current_archive.py"])
        if not changed:
            break
    # Verify after final deterministic build.
    out = proc(["python", "tools/verify_handoff.py"]).stdout
    if "HANDOFF VERIFICATION: PASS" not in out:
        raise AssertionError("pre-push HANDOFF VERIFICATION failed")


def main() -> None:
    git("config", "user.name", "Canonical Integrator")
    git("config", "user.email", "actions@users.noreply.github.com")
    git("fetch", "origin", "main", STAGE0_BRANCH)
    if git("rev-parse", "HEAD") != EXISTING_LOCK_SHA or git("rev-parse", "origin/main") != EXISTING_LOCK_SHA:
        raise AssertionError("resume requires the exact existing lock commit")
    if git("rev-parse", f"origin/{STAGE0_BRANCH}") != STAGE0_HEAD:
        raise AssertionError("Stage-0 branch HEAD mismatch")
    proc(["git", "merge-base", "--is-ancestor", REQUIRED_BASE, STAGE0_HEAD])

    state = load_state()
    lock = state.get("active_integrator", {})
    if lock.get("status") != "HELD" or lock.get("holder") != LOCK_HOLDER or lock.get("base_commit") != REQUIRED_BASE:
        raise AssertionError("existing canonical lock is not the expected B4 lock")
    sealed_members = verify_and_checkout_stage0()

    # PHASE A — no Stage-1 authorization in this commit.
    state = load_state()
    state["active_integrator"]["lock_acquisition_commit"] = EXISTING_LOCK_SHA
    state["active_task"]["stage"] = "PRE_RUN_SEAL_AWAITING_AUTHORIZATION"
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
        "seal_zip_materialized_on_main": False,
        "sealed_members_canonicalized_byte_for_byte": 16,
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
    na["instruction"] = "Perform Phase-A canonical GitHub read-back and verify all 16 sealed member blobs and the exact execution-integrity contract while Stage 1 remains NOT AUTHORIZED. Proceed to separate Phase B only after PASS."
    na["task_code"] = TASK
    na["stage"] = "PRE_RUN_SEAL_AWAITING_AUTHORIZATION"

    PHASE_A_DECISION.parent.mkdir(parents=True, exist_ok=True)
    PHASE_A_DECISION.write_text(f"""# {TASK} — PHASE A STAGE-0 ACCEPTANCE + CONTRACT CANONICALIZATION

Manager verdict: **[ACCEPT B4 STAGE 0]**

Canonical base: `{REQUIRED_BASE}`  
Stage-0 branch/head: `{STAGE0_BRANCH}` @ `{STAGE0_HEAD}`

Stage-0 seal SHA-256: `{SEAL_SHA}`  
Stage-0 manifest SHA-256: `{MANIFEST_SHA}`  
Seal integrity: 16 unique members, CRC PASS, manifested hashes PASS.  
Drive folder: `{DRIVE_STAGE0_FOLDER_ID}`  
Drive seal file: `{DRIVE_SEAL_FILE_ID}`  
Raw Drive seal read-back: PASS.

The seal ZIP remains Drive-only under archive policy. Every one of its 16 sealed members is preserved byte-for-byte from the authoritative Stage-0 branch on canonical main.

The exact immutable execution-integrity contract is canonicalized without rewrite at `{(STAGE0_DIR / CONTRACT_NAME).as_posix()}`.  
Contract SHA-256: `{CONTRACT_SHA}`  
Contract Git blob: `{CONTRACT_BLOB}`.

`E6-N2` remains `[OPEN]`; no B4-N1...B4-N7 is accepted.

**STAGE 1 IS NOT AUTHORIZED IN PHASE A AND HAS NOT BEEN EXECUTED.**

Phase B is forbidden until canonical GitHub read-back passes for all sealed member blobs, the contract hash/blob, and the NOT-AUTHORIZED state.

Nothing in this decision proves the Collatz conjecture.
""", encoding="utf-8", newline="\n")
    HANDOFF.write_text(phase_a_handoff(), encoding="utf-8", newline="\n")
    append_journal(
        "PRE_RUN_SEAL_AWAITING_AUTHORIZATION",
        "B4_STAGE0_ACCEPTED_CONTRACT_CANONICALIZED",
        {
            "contract_git_blob": CONTRACT_BLOB,
            "contract_sha256": CONTRACT_SHA,
            "drive_raw_seal_readback": "PASS",
            "drive_stage0_folder_id": DRIVE_STAGE0_FOLDER_ID,
            "seal_sha256": SEAL_SHA,
            "sealed_member_count": 16,
            "sealed_members_byte_preserved": True,
            "stage0_head": STAGE0_HEAD,
            "stage0_manifest_sha256": MANIFEST_SHA,
            "stage1_authorized": False,
            "stage1_executed": False,
        },
        "Perform Phase-A GitHub read-back; Phase B is forbidden unless all sealed-member/contract hashes match and Stage 1 remains NOT AUTHORIZED.",
    )
    save_state(state)
    git("add", "-A")
    git("commit", "-m", "Canonicalize B4 Stage0 and execution contract")
    phase_a_sha = git("rev-parse", "HEAD")
    git("push", "origin", "HEAD:main")
    git("fetch", "origin", "main")
    if git("rev-parse", "origin/main") != phase_a_sha:
        raise AssertionError("Phase-A push/read-back failed")

    # PHASE-A canonical read-back gate.
    ref = f"origin/{STAGE0_BRANCH}"
    sealed_blob_matches = 0
    for path in sealed_members:
        if git("rev-parse", f"origin/main:{path}") != git("rev-parse", f"{ref}:{path}"):
            raise AssertionError(f"Phase-A sealed member blob mismatch: {path}")
        sealed_blob_matches += 1
    cp = (STAGE0_DIR / CONTRACT_NAME).as_posix()
    rb_contract = git_bytes("show", f"origin/main:{cp}")
    rb_state = json.loads(git_bytes("show", "origin/main:CURRENT_RESEARCH_STATE.json").decode("utf-8"))
    if digest_bytes(rb_contract) != CONTRACT_SHA or git("rev-parse", f"origin/main:{cp}") != CONTRACT_BLOB:
        raise AssertionError("Phase-A contract read-back failed")
    if rb_state["active_task"]["stage"] != "PRE_RUN_SEAL_AWAITING_AUTHORIZATION":
        raise AssertionError("Phase-A stage mismatch")
    if rb_state.get("b4_stage0", {}).get("stage1_authorized") is not False:
        raise AssertionError("Phase-A improperly authorized Stage 1")
    if rb_state.get("documents", {}).get("active_authorization_decision") is not None:
        raise AssertionError("Phase-A has an authorization decision unexpectedly")
    write_json(PHASE_A_READBACK, {
        "contract_git_blob": CONTRACT_BLOB,
        "contract_sha256": CONTRACT_SHA,
        "phase_a_commit": phase_a_sha,
        "sealed_member_blob_matches": sealed_blob_matches,
        "stage1_authorized": False,
        "verdict": "PASS",
    })

    # PHASE B — separate authorization only after Phase-A PASS.
    PHASE_B_DECISION.parent.mkdir(parents=True, exist_ok=True)
    PHASE_B_DECISION.write_text(f"""# {TASK} — PHASE B STAGE-1 AUTHORIZATION

Phase-A canonicalization commit: `{phase_a_sha}`  
Phase-A GitHub canonical read-back: **PASS** (16/16 sealed member blobs exact; contract hash/blob exact; Stage 1 NOT AUTHORIZED).

## ONCE-ONLY AUTHORIZATION

Authorize Stage 1 **ONCE and ONLY** for seal SHA-256:
`{SEAL_SHA}`

Bind this authorization explicitly to the already-canonical execution-integrity contract SHA-256:
`{CONTRACT_SHA}`

Canonical contract path: `{cp}`  
Canonical contract Git blob: `{CONTRACT_BLOB}`.

The exact canonical contract is incorporated by reference byte-for-byte and **every condition A–H is mandatory without exception**, including:

- exact seal SHA verification;
- exact manifest verification, all manifested member hashes, 16 unique members, required ordering/cardinality and CRC PASS;
- exact frozen dependency verification;
- Stage-1 output absence before execution;
- exactly one pre-T1 `RUN_WITNESS` with UTC timestamp, execution identity/session identifier, authorized seal, canonical base and output-absence verdict;
- exact sealed Stage-1 entrypoint/config/seal invocation;
- append-only execution ledger;
- exactly one invocation;
- no repair, source modification, retry or rerun after observed output;
- immediate stop-rule enforcement;
- post-stop `NOT_EXECUTED` evidence for every downstream T stage and no rescue mathematics;
- final result/package creation with exact package/manifest hashes and membership/uniqueness/CRC verification;
- Drive save plus raw byte/hash read-back;
- GitHub result branch persistence without force plus GitHub read-back.

Any input-integrity failure must terminate exactly as `[B4 STAGE1 INPUT INTEGRITY FAILURE]` and Stage 1 must not run.

Adjudicate frozen T1→T8 in order. Stage 1 may establish B4-N1...B4-N4 before adjudicating the direct T7 joint-transform route. T8-A/T8-B are allowed only by the frozen fallback logic after direct T7 adjudication.

Tilting is not cancellation. Tao p=1/2 and Si central-fiber theorems do not automatically transfer. Moving-frequency uniformity is load-bearing. No independent global mod-16 cocycle may be introduced. B3-CT remains a standing falsification constraint.

Mandatory independent-audit stop: genuinely load-bearing B4-N5; B4-N6; B4-N7/E6-N2; load-bearing B4-CT; or an exact downstream-dependent leading-coefficient cancellation/non-cancellation theorem. All later T stages become `NOT_EXECUTED`; no rescue mathematics.

Canonical stage after this authorization: `STAGE_1_AUTHORIZED_NOT_EXECUTED`.

Exact next action: **{EXACT_NEXT}**

This authorization does not execute Stage 1 and accepts no B4 theorem. `E6-N2` remains `[OPEN]`.

Nothing in this authorization proves the Collatz conjecture.
""", encoding="utf-8", newline="\n")

    PHASE_B_PROMPT.parent.mkdir(parents=True, exist_ok=True)
    PHASE_B_PROMPT.write_text(f"""# {TASK} — STAGE-1 MANAGER AUTHORIZATION PROMPT

Status: `STAGE_1_AUTHORIZED_NOT_EXECUTED`.

Execute B4 Stage 1 exactly once and only for authorized seal SHA-256 `{SEAL_SHA}`, bound to canonical execution-integrity contract SHA-256 `{CONTRACT_SHA}` at `{cp}`. Phase-A canonicalization commit is `{phase_a_sha}` and Phase-A read-back is PASS.

Before any mathematical action, satisfy every condition A–H of the canonical contract byte-for-byte: seal/manifest/member/dependency checks; 16 unique members and CRC; output absence; exactly one pre-T1 RUN_WITNESS with UTC and execution identity; exact sealed entrypoint; append-only ledger; exactly one invocation; no repair/rerun; immediate stop; post-stop NOT_EXECUTED evidence; final package/manifest hashes; Drive save/raw read-back; GitHub result branch/read-back.

On any input-integrity failure terminate `[B4 STAGE1 INPUT INTEGRITY FAILURE]` and do not run Stage 1.

Adjudicate T1→T8 in frozen order under F1...F10 and T7-F1...T7-F5. Tilting is not cancellation; do not auto-transfer Tao p=1/2 or Si central-fiber theorems; moving-frequency uniformity is load-bearing; introduce no independent global mod-16 cocycle; B3-CT remains a falsification constraint. T8-A/T8-B only after direct T7 adjudication permits fallback.

Stop immediately for independent audit at a genuinely load-bearing B4-N5, B4-N6, B4-N7/E6-N2, a load-bearing B4-CT, or a downstream-dependent exact leading-coefficient cancellation/non-cancellation theorem. Mark later T stages NOT_EXECUTED and do no rescue mathematics.

No E8 is authorized. No weighted/operator work is authorized except the already-frozen T8-B fallback if and only if its gate is reached.

Return the complete contract-required result/provenance/package/hash/Drive/GitHub read-back records. Do not rerun.

Nothing in this authorization proves the Collatz conjecture.
""", encoding="utf-8", newline="\n")

    state = load_state()
    state["active_task"]["stage"] = "STAGE_1_AUTHORIZED_NOT_EXECUTED"
    state["active_integrator"]["status"] = "RELEASED"
    state["active_integrator"]["lock_acquisition_commit"] = EXISTING_LOCK_SHA
    state["b4_stage0"]["stage1_authorized"] = True
    state["b4_stage0"]["stage1_executed"] = False
    state["b4_stage0"]["phase_a_canonicalization_commit"] = phase_a_sha
    state["b4_stage0"]["phase_a_readback"] = "PASS"
    state["stage1_authorization"] = {
        "authorization_count": 1,
        "authorized_seal_sha256": SEAL_SHA,
        "canonical_contract_git_blob": CONTRACT_BLOB,
        "canonical_contract_sha256": CONTRACT_SHA,
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
    HANDOFF.write_text(final_handoff(phase_a_sha), encoding="utf-8", newline="\n")
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
    save_state(state)

    # Final archive/continuity closeout. No Stage-1 code is invoked.
    stabilize_archive(state)

    forbidden = {
        "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_RUN_WITNESS.json",
        "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_RESULTS.json",
        "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_EXECUTION_LEDGER.jsonl",
    }
    for p in REPO.rglob("*"):
        if p.is_file() and p.name in forbidden:
            raise AssertionError(f"Stage-1 output unexpectedly exists: {p}")

    git("add", "-A")
    git("commit", "-m", "Authorize B4 Stage1 under canonical execution contract")
    phase_b_sha = git("rev-parse", "HEAD")
    git("push", "origin", "HEAD:main")
    git("fetch", "origin", "main")
    if git("rev-parse", "origin/main") != phase_b_sha:
        raise AssertionError("Phase-B/final push read-back failed")

    final_verify = proc(["python", "tools/verify_handoff.py"]).stdout
    if "HANDOFF VERIFICATION: PASS" not in final_verify:
        raise AssertionError("final published HANDOFF VERIFICATION failed")
    rb_state = json.loads(git_bytes("show", "origin/main:CURRENT_RESEARCH_STATE.json").decode("utf-8"))
    rb_contract = git_bytes("show", f"origin/main:{cp}")
    if digest_bytes(rb_contract) != CONTRACT_SHA or git("rev-parse", f"origin/main:{cp}") != CONTRACT_BLOB:
        raise AssertionError("final contract read-back failed")
    if rb_state["active_task"]["stage"] != "STAGE_1_AUTHORIZED_NOT_EXECUTED":
        raise AssertionError("final stage read-back mismatch")
    if rb_state["active_integrator"]["status"] != "RELEASED":
        raise AssertionError("final lock read-back not RELEASED")
    if rb_state["stage1_authorization"]["stage1_executed"] is not False:
        raise AssertionError("final state does not say Stage 1 NOT EXECUTED")

    build = json.loads(BUILD.read_text(encoding="utf-8"))
    archive_bytes = ARCHIVE.stat().st_size
    if archive_bytes != build["zip_bytes"] or digest_file(ARCHIVE) != build["archive_sha256"]:
        raise AssertionError("archive/build record mismatch")
    headroom = 100_000_000 - archive_bytes

    Path("FINAL_HANDOFF_VERIFICATION.txt").write_text(final_verify, encoding="utf-8", newline="\n")
    write_json(Path("GITHUB_READBACK.json"), {
        "contract_git_blob": CONTRACT_BLOB,
        "contract_sha256": CONTRACT_SHA,
        "final_main": phase_b_sha,
        "integrator_lock": "RELEASED",
        "phase_a_commit": phase_a_sha,
        "phase_a_readback": "PASS",
        "sealed_member_blob_matches": 16,
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
        "canonical_contract_sha256": CONTRACT_SHA,
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
        "phase_a_sha": phase_a_sha,
        "phase_b_sha": phase_b_sha,
        "seal_sha256": SEAL_SHA,
        "stage1_executed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
