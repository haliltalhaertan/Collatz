#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone, timedelta
from pathlib import Path
import hashlib
import json
import subprocess
import urllib.request
import zipfile

REPO = Path.cwd()
PHASE_A_PRIOR = "6e7757b316646d5eaf350c7acbaecb9c8468f1eb"
LOCK_SHA = "060c9129aac5562e4b2b8c32634159c71579132b"
REQUIRED_BASE = "57f670bd531cee8f0f2d6eeb27431243f6e3a479"
LOCK_HOLDER = "canonical-integrator-e7r-b4-stage0-stage1-authorization-20260904"
STAGE0_BRANCH = "cp20-e7r-b4-tilted-microcanonical-fourier-v1-stage0-20260904"
STAGE0_HEAD = "c83d22f9e3ac8bdc4ec955d14b3d7dca11c3fee1"
TASK = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1"
TASK_NAME = "Tilted / Recentered Microcanonical Fourier Cancellation"
STAGE0_DIR = Path("research_manager/results/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE0")
MANIFEST_NAME = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_PRE_RUN_SHA256SUMS.txt"
CONTRACT_NAME = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_EXECUTION_INTEGRITY_AND_OUTPUT_CONTRACT.md"
ORDER_NAME = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_ORDER.md"
ORDER_PATH = STAGE0_DIR / ORDER_NAME
SEAL_SHA = "ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c"
MANIFEST_SHA = "7de830b396fb075b4a97f78dd889ef16e92d66e763e5572af603f016faf33118"
CONTRACT_SHA = "3d9fd4c0c029c135b86c43377aa414c87704f5e6c3dd4a008fa621f3b4f1185e"
CONTRACT_BLOB = "94a15beb7573c860e4891048e705c9f13a156f04"
ORDER_SHA = "90dbb1b229a6f5d7677251ce250ef377dba36b369a566d9cc0207aff420a333a"
ORDER_BLOB = "a62a0781b5c78f6203401b47329a8584617e8f94"
DRIVE_FOLDER = "1n7sz5_1JFXAqJ1KUWT66Hy9KBzyvwnLI"
DRIVE_SEAL_FILE = "12WfXfOfCHt9XZTSqBYPDfLV7xsZ1bVIY"
DRIVE_URL = f"https://drive.usercontent.google.com/download?id={DRIVE_SEAL_FILE}&export=download&confirm=t"
EXACT_NEXT = "Execute B4 Stage 1 exactly once under the authorized seal and canonical execution-integrity contract, adjudicating T1→T8 in frozen order."

STATE = Path("CURRENT_RESEARCH_STATE.json")
HANDOFF = Path("START_HERE_CURRENT_HANDOFF.md")
JOURNAL = Path("research_manager/RESEARCH_JOURNAL.jsonl")
ARCHIVE = Path("Collatz_Research_Archive_CURRENT.zip")
BUILD = Path("CURRENT_ARCHIVE_BUILD.json")
PHASE_A_REPAIR = Path("research_manager/records/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_PHASE_A_BYTE_PRESERVATION_REPAIR_2026-09-04.md")
PHASE_A_READBACK = Path("research_manager/records/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_PHASE_A_READBACK_2026-09-04.json")
PHASE_B_DECISION = Path("research_manager/decisions/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_AUTHORIZATION_2026-09-04.md")
PHASE_B_PROMPT = Path("research_manager/prompts/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_MANAGER_AUTHORIZATION_PROMPT_2026-09-04.md")


def run(args, *, text=True, check=True):
    p = subprocess.run(args, cwd=REPO, text=text, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if check and p.returncode:
        raise RuntimeError(f"command failed {args}:\n{p.stdout}\n{p.stderr}")
    return p


def git(*args): return run(["git", *args]).stdout.strip()
def git_bytes(*args): return run(["git", *args], text=False).stdout

def sha_bytes(data: bytes) -> str: return hashlib.sha256(data).hexdigest()
def sha_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""): h.update(block)
    return h.hexdigest()

def now_tr(): return datetime.now(timezone(timedelta(hours=3))).replace(microsecond=0).isoformat()

def write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")

def load_state(): return json.loads(STATE.read_text(encoding="utf-8"))
def save_state(s): write_json(STATE, s)

def append_journal(stage, event, evidence, next_action):
    lines = JOURNAL.read_bytes().splitlines()
    row = {
        "active_stage": stage,
        "active_task": TASK,
        "event": event,
        "evidence": evidence,
        "next_action": next_action,
        "previous_entry_sha256": sha_bytes(lines[-1]) if lines else None,
        "schema": "COLLATZ_RESEARCH_JOURNAL_V1",
        "sequence": len(lines) + 1,
        "timestamp": now_tr(),
    }
    with JOURNAL.open("ab") as f:
        f.write(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n")


def refresh_repo_integrity(state):
    for row in state.get("integrity", {}).get("repository_files", []):
        p = Path(row["path"])
        if p == STATE: continue
        if p.is_file(): row["sha256"] = sha_file(p)

def refresh_archive_integrity(state):
    changed = False
    with zipfile.ZipFile(ARCHIVE) as zf:
        names = set(zf.namelist())
        for row in state.get("integrity", {}).get("archive_members", []):
            name = row["path"]
            if name in names:
                actual = sha_bytes(zf.read(name))
                if row.get("sha256") != actual:
                    row["sha256"] = actual; changed = True
    return changed

def stabilize_archive(state):
    refresh_repo_integrity(state); save_state(state)
    run(["python", "tools/build_current_archive.py"])
    for _ in range(4):
        changed = refresh_archive_integrity(state)
        refresh_repo_integrity(state); save_state(state)
        run(["python", "tools/build_current_archive.py"])
        if not changed: break
    out = run(["python", "tools/verify_handoff.py"]).stdout
    if "HANDOFF VERIFICATION: PASS" not in out:
        raise AssertionError("pre-push HANDOFF VERIFICATION failed")


def download_seal_order() -> bytes:
    seal = Path("/tmp/b4_authoritative_seal.zip")
    urllib.request.urlretrieve(DRIVE_URL, seal)
    raw = seal.read_bytes()
    if sha_bytes(raw) != SEAL_SHA: raise AssertionError("Drive seal raw SHA mismatch")
    with zipfile.ZipFile(seal) as zf:
        names = [x.filename for x in zf.infolist()]
        if len(names) != 16 or len(set(names)) != 16 or zf.testzip() is not None:
            raise AssertionError("Drive seal cardinality/CRC failure")
        order = zf.read(ORDER_NAME)
        if sha_bytes(order) != ORDER_SHA: raise AssertionError("Drive ORDER SHA mismatch")
        manifest = zf.read(MANIFEST_NAME)
        if sha_bytes(manifest) != MANIFEST_SHA: raise AssertionError("Drive embedded manifest SHA mismatch")
        contract = zf.read(CONTRACT_NAME)
        if sha_bytes(contract) != CONTRACT_SHA: raise AssertionError("Drive embedded contract SHA mismatch")
    return order


def verify_phase_a_sources(order_raw: bytes):
    ref = f"origin/{STAGE0_BRANCH}"
    manifest = STAGE0_DIR / MANIFEST_NAME
    if sha_file(manifest) != MANIFEST_SHA: raise AssertionError("canonical manifest mismatch before repair")
    rows = [x for x in manifest.read_text(encoding="utf-8").splitlines() if x.strip()]
    if len(rows) != 15: raise AssertionError("manifest row count mismatch")
    sealed = [str(manifest)]
    for line in rows:
        expected, name = line.split("  ", 1)
        p = STAGE0_DIR / name
        if name == ORDER_NAME:
            if sha_bytes(order_raw) != expected: raise AssertionError("ORDER manifest mismatch")
        else:
            if not p.is_file() or sha_file(p) != expected: raise AssertionError(f"canonical sealed member mismatch: {name}")
            if git("rev-parse", f"HEAD:{p.as_posix()}") != git("rev-parse", f"{ref}:{p.as_posix()}"):
                raise AssertionError(f"canonical member blob differs from Stage0 source: {name}")
        sealed.append(str(p))
    if len(sealed) != 16: raise AssertionError("sealed member count != 16")
    cp = STAGE0_DIR / CONTRACT_NAME
    if sha_file(cp) != CONTRACT_SHA or git("rev-parse", f"HEAD:{cp.as_posix()}") != CONTRACT_BLOB:
        raise AssertionError("canonical contract mismatch")
    return sealed


def phase_a_handoff():
    return f"""# START HERE — Current Collatz Research Handoff

Machine-readable authority: `CURRENT_RESEARCH_STATE.json`.

## B4 Phase A — corrected canonical Stage-0 intake

Task: `{TASK}` — **{TASK_NAME}**.

Stage 0 is accepted. Stage 1 remains **NOT AUTHORIZED** and **NOT EXECUTED**.

A prior Phase-A candidate commit `{PHASE_A_PRIOR}` failed its canonical byte read-back because Git text normalization changed the Drive-only sealed `ORDER.md`. No authorization was created from that failed read-back. The repair preserves history and canonicalizes the raw sealed bytes with a path-specific `-text` rule.

Stage-0 branch/head: `{STAGE0_BRANCH}` @ `{STAGE0_HEAD}`.  
Seal SHA-256: `{SEAL_SHA}`. Manifest SHA-256: `{MANIFEST_SHA}`.  
Drive folder: `{DRIVE_FOLDER}`; raw seal read-back: PASS; 16 unique members; CRC PASS; manifested hashes PASS.

The exact contract remains canonical at `{(STAGE0_DIR / CONTRACT_NAME).as_posix()}` with SHA-256 `{CONTRACT_SHA}` and Git blob `{CONTRACT_BLOB}`.

The Drive-only `ORDER.md` is canonicalized byte-for-byte with SHA-256 `{ORDER_SHA}` and Git blob `{ORDER_BLOB}`. All 16 sealed members must pass canonical read-back before Phase B.

`E6-N2` remains `[OPEN]`; no B4-N1...B4-N7 is accepted.

Exact next management action: perform corrected Phase-A GitHub read-back. Phase B is forbidden unless 16/16 sealed members, contract bytes/blob, and NOT-AUTHORIZED state all PASS.

Nothing here proves the Collatz conjecture.
"""


def final_handoff(phase_a_sha):
    return f"""# START HERE — Current Collatz Research Handoff

Machine-readable authority: `CURRENT_RESEARCH_STATE.json`. Recover on branch `main`, run `python tools/verify_handoff.py`, and require `HANDOFF VERIFICATION: PASS` before any research action.

## B4 canonical status

Task: `{TASK}` — **{TASK_NAME}**.

Corrected Phase-A canonicalization commit: `{phase_a_sha}`. Phase-A canonical read-back: **PASS** (16/16 sealed members exact; contract exact; Stage 1 remained NOT AUTHORIZED).

Stage-0 seal SHA-256: `{SEAL_SHA}`. Manifest SHA-256: `{MANIFEST_SHA}`.  
Stage-0 branch/head: `{STAGE0_BRANCH}` @ `{STAGE0_HEAD}`.  
Drive Stage-0 folder: `{DRIVE_FOLDER}`; raw seal read-back PASS. The seal ZIP remains Drive-only; its sealed text/source/config/hash members are preserved on main.

Canonical execution-integrity contract SHA-256: `{CONTRACT_SHA}`; Git blob `{CONTRACT_BLOB}`. It was canonicalized before Phase-B authorization.

## Phase B

Canonical stage: `STAGE_1_AUTHORIZED_NOT_EXECUTED`.

Stage 1 is authorized **ONCE and ONLY** for seal `{SEAL_SHA}`, bound to every condition A–H of canonical contract `{CONTRACT_SHA}`.

Any input-integrity failure terminates `[B4 STAGE1 INPUT INTEGRITY FAILURE]` without execution. T1→T8 are adjudicated in frozen order; T8-A/T8-B only by frozen fallback logic after T7 adjudication. Tilting is not cancellation; Tao p=1/2 and Si central-fiber theorems do not automatically transfer; moving-frequency uniformity is load-bearing; no global mod-16 cocycle may be introduced; B3-CT remains a falsification constraint.

Mandatory audit stop fires at a genuinely load-bearing B4-N5, B4-N6, B4-N7/E6-N2, load-bearing B4-CT, or a downstream-dependent exact leading-coefficient cancellation/non-cancellation theorem. Later T stages become `NOT_EXECUTED`; no rescue mathematics.

`E6-N2` remains `[OPEN]` at authorization. No B4 theorem is accepted by this transaction.

## Exact next action

{EXACT_NEXT}

Stage 1 was **NOT EXECUTED** by this management transaction. No E8 was performed; no weighted/operator work was performed.

Nothing in this authorization proves the Collatz conjecture.
"""


def main():
    git("config", "user.name", "Canonical Integrator")
    git("config", "user.email", "actions@users.noreply.github.com")
    git("fetch", "origin", "main", STAGE0_BRANCH)
    if git("rev-parse", "HEAD") != PHASE_A_PRIOR or git("rev-parse", "origin/main") != PHASE_A_PRIOR:
        raise AssertionError("repair must start from exact failed Phase-A candidate")
    if git("rev-parse", f"origin/{STAGE0_BRANCH}") != STAGE0_HEAD: raise AssertionError("Stage0 HEAD moved")
    state = load_state()
    lock = state["active_integrator"]
    if lock.get("status") != "HELD" or lock.get("holder") != LOCK_HOLDER or lock.get("base_commit") != REQUIRED_BASE:
        raise AssertionError("expected integrator lock is not held")
    if state["active_task"]["stage"] != "PRE_RUN_SEAL_AWAITING_AUTHORIZATION": raise AssertionError("unexpected Phase-A stage")
    if state.get("b4_stage0", {}).get("stage1_authorized") is not False: raise AssertionError("Stage1 already authorized unexpectedly")

    order_raw = download_seal_order()
    sealed = verify_phase_a_sources(order_raw)

    # Disable Git text normalization only for the Drive-only sealed ORDER member.
    attrs = Path(".gitattributes")
    existing = attrs.read_text(encoding="utf-8") if attrs.exists() else ""
    rule = f"{ORDER_PATH.as_posix()} -text\n"
    if rule not in existing:
        if existing and not existing.endswith("\n"): existing += "\n"
        attrs.write_text(existing + rule, encoding="utf-8", newline="\n")
    git("add", str(attrs))
    ORDER_PATH.write_bytes(order_raw)
    git("add", str(ORDER_PATH))
    if git("rev-parse", f":{ORDER_PATH.as_posix()}") != ORDER_BLOB:
        raise AssertionError("index did not preserve raw ORDER blob")

    PHASE_A_REPAIR.parent.mkdir(parents=True, exist_ok=True)
    PHASE_A_REPAIR.write_text(f"""# B4 Phase-A byte-preservation repair

Prior Phase-A candidate: `{PHASE_A_PRIOR}`.

Read-back verdict for that candidate: **FAIL — sealed `ORDER.md` EOL normalization**. Stage 1 remained NOT AUTHORIZED and no Phase-B decision was created.

Repair: add a path-specific `-text` Git attribute and re-stage the exact raw `ORDER.md` bytes independently fetched from Drive seal file `{DRIVE_SEAL_FILE}`.

Raw Drive seal SHA-256: `{SEAL_SHA}`; 16 unique members; CRC PASS.  
Raw ORDER SHA-256: `{ORDER_SHA}`.  
Required Git blob for raw ORDER: `{ORDER_BLOB}`.

This repair changes no scientific content and performs no Stage-1 mathematics. Phase-B authorization remains forbidden until the repaired Phase-A commit passes canonical read-back.
""", encoding="utf-8", newline="\n")

    state = load_state()
    state["b4_stage0"]["phase_a_prior_candidate_commit"] = PHASE_A_PRIOR
    state["b4_stage0"]["phase_a_prior_readback"] = "FAIL_ORDER_EOL_NORMALIZATION"
    state["b4_stage0"]["order_sha256"] = ORDER_SHA
    state["b4_stage0"]["order_git_blob"] = ORDER_BLOB
    state["b4_stage0"]["stage1_authorized"] = False
    state["b4_stage0"]["stage1_executed"] = False
    state["documents"]["active_authorization_decision"] = None
    state["documents"]["active_authorization_prompt"] = None
    state["documents"]["active_research_prompt"] = None
    state["next_action"]["instruction"] = "Perform corrected Phase-A GitHub read-back for 16/16 sealed members and exact contract bytes/blob while Stage 1 remains NOT AUTHORIZED; only after PASS may Phase B be created."
    HANDOFF.write_text(phase_a_handoff(), encoding="utf-8", newline="\n")
    append_journal("PRE_RUN_SEAL_AWAITING_AUTHORIZATION", "B4_PHASE_A_BYTE_PRESERVATION_REPAIR", {
        "prior_phase_a_candidate": PHASE_A_PRIOR,
        "prior_readback": "FAIL_ORDER_EOL_NORMALIZATION",
        "order_git_blob": ORDER_BLOB,
        "order_sha256": ORDER_SHA,
        "seal_sha256": SEAL_SHA,
        "stage1_authorized": False,
        "stage1_executed": False,
    }, "Perform corrected Phase-A canonical read-back; Phase B remains forbidden until PASS.")
    save_state(state)
    git("add", "-A")
    if git("rev-parse", f":{ORDER_PATH.as_posix()}") != ORDER_BLOB: raise AssertionError("ORDER blob changed before repair commit")
    git("commit", "-m", "Repair B4 PhaseA sealed ORDER byte preservation")
    phase_a_sha = git("rev-parse", "HEAD")
    git("push", "origin", "HEAD:main")
    git("fetch", "origin", "main")
    if git("rev-parse", "origin/main") != phase_a_sha: raise AssertionError("repaired Phase-A push/read-back failed")

    # Corrected Phase-A gate: exact 16 sealed members + contract + NOT AUTHORIZED.
    ref = f"origin/{STAGE0_BRANCH}"
    for pstr in sealed:
        p = Path(pstr)
        if p.name == ORDER_NAME:
            raw = git_bytes("cat-file", "blob", f"origin/main:{p.as_posix()}")
            if sha_bytes(raw) != ORDER_SHA or git("rev-parse", f"origin/main:{p.as_posix()}") != ORDER_BLOB:
                raise AssertionError("corrected Phase-A ORDER read-back failed")
        else:
            if git("rev-parse", f"origin/main:{p.as_posix()}") != git("rev-parse", f"{ref}:{p.as_posix()}"):
                raise AssertionError(f"corrected Phase-A sealed member mismatch: {p.name}")
    cp = STAGE0_DIR / CONTRACT_NAME
    if sha_bytes(git_bytes("cat-file", "blob", f"origin/main:{cp.as_posix()}")) != CONTRACT_SHA: raise AssertionError("contract SHA read-back failed")
    if git("rev-parse", f"origin/main:{cp.as_posix()}") != CONTRACT_BLOB: raise AssertionError("contract blob read-back failed")
    rb_state = json.loads(git_bytes("show", "origin/main:CURRENT_RESEARCH_STATE.json").decode("utf-8"))
    if rb_state["active_task"]["stage"] != "PRE_RUN_SEAL_AWAITING_AUTHORIZATION": raise AssertionError("repaired Phase-A stage mismatch")
    if rb_state["b4_stage0"]["stage1_authorized"] is not False: raise AssertionError("repaired Phase-A improperly authorized Stage1")
    if rb_state["documents"].get("active_authorization_decision") is not None: raise AssertionError("authorization decision exists before PhaseB")
    write_json(PHASE_A_READBACK, {
        "contract_git_blob": CONTRACT_BLOB,
        "contract_sha256": CONTRACT_SHA,
        "order_git_blob": ORDER_BLOB,
        "order_sha256": ORDER_SHA,
        "phase_a_commit": phase_a_sha,
        "sealed_members_exact": "16/16",
        "stage1_authorized": False,
        "verdict": "PASS",
    })

    # Phase B: separate authorization decision created only now.
    PHASE_B_DECISION.parent.mkdir(parents=True, exist_ok=True)
    PHASE_B_DECISION.write_text(f"""# {TASK} — PHASE B STAGE-1 AUTHORIZATION

Corrected Phase-A commit: `{phase_a_sha}`.  
Canonical Phase-A read-back: **PASS — 16/16 sealed members exact, contract exact, Stage 1 NOT AUTHORIZED before this decision**.

Authorize Stage 1 **ONCE and ONLY** for seal SHA-256 `{SEAL_SHA}` and bind it to the already-canonical execution-integrity contract SHA-256 `{CONTRACT_SHA}` (Git blob `{CONTRACT_BLOB}`).

The entire canonical contract Sections A–H are incorporated byte-for-byte and mandatory. This explicitly requires: exact seal SHA; exact manifest/member hashes; 16 unique members, ordering/cardinality and CRC PASS; dependency verification; Stage-1 output absence; exactly one pre-T1 RUN_WITNESS with UTC timestamp and execution identity; exact sealed Stage-1 entrypoint; append-only execution ledger; exactly one invocation; no repair/retry/rerun after observed output; immediate stop-rule enforcement; post-stop downstream `NOT_EXECUTED` evidence; final package/manifest hashes and package integrity; Drive save/raw read-back; GitHub result branch/push/read-back.

Any input-integrity failure terminates exactly `[B4 STAGE1 INPUT INTEGRITY FAILURE]` and Stage 1 must not run.

Adjudicate T1→T8 in frozen order. B4-N1...B4-N4 may be established before the direct T7 route. T8-A/T8-B only if the frozen fallback gate is reached after T7 adjudication. Tilting is not cancellation; do not auto-transfer Tao p=1/2 or Si central-fiber theorems; moving `eta_r` uniformity is load-bearing; no independent global mod-16 cocycle; B3-CT remains a falsification constraint.

Mandatory independent-audit stop at genuinely load-bearing B4-N5, B4-N6, B4-N7/E6-N2, load-bearing B4-CT, or any exact downstream-dependent leading-coefficient cancellation/non-cancellation theorem. After stop all later T stages are `NOT_EXECUTED`; no rescue mathematics.

Canonical stage: `STAGE_1_AUTHORIZED_NOT_EXECUTED`.

Exact next action: **{EXACT_NEXT}**

This decision does not execute Stage 1, accepts no B4 theorem, and leaves `E6-N2 [OPEN]`.

Nothing in this authorization proves the Collatz conjecture.
""", encoding="utf-8", newline="\n")

    PHASE_B_PROMPT.parent.mkdir(parents=True, exist_ok=True)
    PHASE_B_PROMPT.write_text(f"""# {TASK} — STAGE-1 MANAGER AUTHORIZATION PROMPT

Status: `STAGE_1_AUTHORIZED_NOT_EXECUTED`.

Execute Stage 1 exactly once and only for seal SHA-256 `{SEAL_SHA}`, bound to canonical contract SHA-256 `{CONTRACT_SHA}` at `{cp.as_posix()}`. Corrected Phase-A commit `{phase_a_sha}` has canonical read-back PASS.

Before any mathematical action satisfy every condition A–H of the canonical contract: exact seal/manifest/member/dependency verification; 16 unique members and CRC; Stage-1 output absence; exactly one pre-T1 RUN_WITNESS with UTC and execution identity; exact sealed entrypoint; append-only ledger; exactly one invocation; no repair/rerun; immediate audit-stop; post-stop NOT_EXECUTED evidence; final package/manifest hashes; Drive save/raw read-back; GitHub result branch/read-back.

On any input failure terminate `[B4 STAGE1 INPUT INTEGRITY FAILURE]` and do not execute Stage 1.

Adjudicate T1→T8 in frozen order under F1...F10 and T7-F1...T7-F5. Tilting is not cancellation; Tao p=1/2 and Si central-fiber theorems do not automatically transfer; moving-frequency uniformity is load-bearing; no independent global mod-16 cocycle; B3-CT remains a falsification constraint. T8-A/T8-B only after direct T7 adjudication opens their frozen fallback gate.

Stop immediately for independent audit at genuinely load-bearing B4-N5, B4-N6, B4-N7/E6-N2, load-bearing B4-CT, or an exact downstream-dependent leading-coefficient cancellation/non-cancellation theorem. Mark later T stages NOT_EXECUTED and do no rescue mathematics.

No E8 is authorized. No weighted/operator work is authorized except the already-frozen T8-B fallback if its gate is actually reached.

Return all contract-required result/provenance/package/hash/Drive/GitHub read-back records. Do not rerun.

Nothing in this authorization proves the Collatz conjecture.
""", encoding="utf-8", newline="\n")

    state = load_state()
    state["active_task"]["stage"] = "STAGE_1_AUTHORIZED_NOT_EXECUTED"
    state["active_integrator"]["status"] = "RELEASED"
    state["active_integrator"]["lock_acquisition_commit"] = LOCK_SHA
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
    state["documents"]["active_authorization_decision"] = PHASE_B_DECISION.as_posix()
    state["documents"]["active_authorization_prompt"] = PHASE_B_PROMPT.as_posix()
    state["documents"]["active_research_prompt"] = PHASE_B_PROMPT.as_posix()
    state["continuity"]["minimum_required_commit"] = phase_a_sha
    state["next_action"]["instruction"] = EXACT_NEXT
    state["next_action"]["stage"] = "STAGE_1_AUTHORIZED_NOT_EXECUTED"
    state["next_action"]["task_code"] = TASK
    HANDOFF.write_text(final_handoff(phase_a_sha), encoding="utf-8", newline="\n")
    append_journal("STAGE_1_AUTHORIZED_NOT_EXECUTED", "B4_STAGE1_AUTHORIZED_AFTER_CORRECTED_PHASE_A_READBACK", {
        "authorization_count": 1,
        "canonical_contract_git_blob": CONTRACT_BLOB,
        "canonical_contract_sha256": CONTRACT_SHA,
        "phase_a_commit": phase_a_sha,
        "phase_a_readback": "PASS",
        "sealed_members_exact": "16/16",
        "seal_sha256": SEAL_SHA,
        "stage1_authorized": True,
        "stage1_executed": False,
    }, EXACT_NEXT)
    save_state(state)

    stabilize_archive(state)
    # Enforce exact raw ORDER in final worktree and rebuilt archive.
    if sha_file(ORDER_PATH) != ORDER_SHA: raise AssertionError("final worktree ORDER raw bytes changed")
    archive_order = f"Collatz Problemi — Araştırma Arşivi/RESEARCH_MANAGEMENT/{ORDER_PATH.relative_to('research_manager').as_posix()}"
    with zipfile.ZipFile(ARCHIVE) as zf:
        if archive_order not in zf.namelist() or sha_bytes(zf.read(archive_order)) != ORDER_SHA:
            raise AssertionError("current archive does not preserve exact sealed ORDER bytes")

    forbidden = {"CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_RUN_WITNESS.json", "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_RESULTS.json", "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_EXECUTION_LEDGER.jsonl"}
    for p in REPO.rglob("*"):
        if p.is_file() and p.name in forbidden: raise AssertionError(f"Stage1 output unexpectedly exists: {p}")

    git("add", "-A")
    if git("rev-parse", f":{ORDER_PATH.as_posix()}") != ORDER_BLOB: raise AssertionError("ORDER index blob changed before PhaseB commit")
    git("commit", "-m", "Authorize B4 Stage1 after corrected PhaseA readback")
    phase_b_sha = git("rev-parse", "HEAD")
    git("push", "origin", "HEAD:main")
    git("fetch", "origin", "main")
    if git("rev-parse", "origin/main") != phase_b_sha: raise AssertionError("PhaseB final push/readback failed")

    final_verify = run(["python", "tools/verify_handoff.py"]).stdout
    if "HANDOFF VERIFICATION: PASS" not in final_verify: raise AssertionError("final published HANDOFF VERIFICATION failed")
    rb = json.loads(git_bytes("show", "origin/main:CURRENT_RESEARCH_STATE.json").decode("utf-8"))
    if rb["active_task"]["stage"] != "STAGE_1_AUTHORIZED_NOT_EXECUTED" or rb["active_integrator"]["status"] != "RELEASED" or rb["stage1_authorization"]["stage1_executed"] is not False:
        raise AssertionError("final canonical state readback failed")
    if git("rev-parse", f"origin/main:{cp.as_posix()}") != CONTRACT_BLOB: raise AssertionError("final contract blob readback failed")
    if sha_bytes(git_bytes("cat-file", "blob", f"origin/main:{ORDER_PATH.as_posix()}")) != ORDER_SHA: raise AssertionError("final ORDER raw readback failed")

    build = json.loads(BUILD.read_text(encoding="utf-8"))
    size = ARCHIVE.stat().st_size
    if size != build["zip_bytes"] or sha_file(ARCHIVE) != build["archive_sha256"]: raise AssertionError("archive/build mismatch")
    headroom = 100_000_000 - size
    Path("FINAL_HANDOFF_VERIFICATION.txt").write_text(final_verify, encoding="utf-8", newline="\n")
    write_json(Path("GITHUB_READBACK.json"), {"contract_git_blob": CONTRACT_BLOB, "contract_sha256": CONTRACT_SHA, "final_main": phase_b_sha, "integrator_lock": "RELEASED", "order_git_blob": ORDER_BLOB, "order_sha256": ORDER_SHA, "phase_a_commit": phase_a_sha, "phase_a_readback": "PASS", "sealed_members_exact": "16/16", "stage": "STAGE_1_AUTHORIZED_NOT_EXECUTED", "stage1_executed": False, "verdict": "PASS"})
    write_json(Path("ARCHIVE_BUDGET.json"), {"archive_bytes": size, "archive_sha256": build["archive_sha256"], "hard_limit_bytes": 100_000_000, "headroom_bytes": headroom})
    write_json(Path("CANONICAL_TRANSACTION_SUMMARY.json"), {"archive_bytes": size, "archive_sha256": build["archive_sha256"], "canonical_contract_sha256": CONTRACT_SHA, "final_main": phase_b_sha, "handoff_verification": "PASS", "headroom_bytes": headroom, "phase_a_commit": phase_a_sha, "phase_a_contract_readback": "PASS", "phase_b_authorization_commit": phase_b_sha, "seal_sha256": SEAL_SHA, "stage1_executed": False})
    Path("PHASE_A_COMMIT.txt").write_text(phase_a_sha + "\n", encoding="utf-8")
    Path("PHASE_B_COMMIT.txt").write_text(phase_b_sha + "\n", encoding="utf-8")
    Path("FINAL_SHA.txt").write_text(phase_b_sha + "\n", encoding="utf-8")
    print(json.dumps({"archive_bytes": size, "archive_sha256": build["archive_sha256"], "contract_sha256": CONTRACT_SHA, "final_sha": phase_b_sha, "headroom": headroom, "phase_a_sha": phase_a_sha, "phase_b_sha": phase_b_sha, "seal_sha256": SEAL_SHA, "stage1_executed": False}, sort_keys=True))

if __name__ == "__main__": main()
