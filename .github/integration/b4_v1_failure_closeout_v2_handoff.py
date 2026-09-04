#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone, timedelta
from pathlib import Path
import hashlib
import json
import subprocess
import urllib.request

REPO = Path.cwd()
REQUIRED_MAIN = "f5269e5ddbf610b2305fafbd90fe2b1346376103"
OLD_AUTH_COMMIT = "0c0e0e55c490278396f0b8f5033000b80725fb6c"
PLACEHOLDER_COMMIT = "c3062952ffb23754f62fd2dd6f6a6237e8b1d22c"
REVERT_COMMIT = REQUIRED_MAIN
FAILURE_BRANCH = "cp20-e7r-b4-stage1-input-integrity-failure-20260904"
FAILURE_COMMIT = "f1dce61f3d2ee207a50bd0f46208f49f3901f013"
OLD_SEAL = "ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c"
OLD_CONTRACT = "3d9fd4c0c029c135b86c43377aa414c87704f5e6c3dd4a008fa621f3b4f1185e"
FAILURE_PACKAGE_SHA = "71ad925b3d461e4ceb77293736cee75dfea116c012703e1308e00bc118125ab4"
FORENSIC_MANIFEST_SHA = "92f787e9f44625186fe4f1e78c85f601523d19a902818babe3ad78547ae10ce7"
FAILURE_DRIVE_FOLDER = "1hYTCh3ilo3SfBRPePpNLBGcbQCDrPnsB"
FAILURE_PACKAGE_FILE = "1T9G831PyU6E11-FGJnaT_dEr4WMzPRAg"
FAILURE_MANIFEST_FILE = "1dGgNLgFBB7l7mbc094aK3XIbO5_lhir9"
HOLDER = "canonical-integrator-e7r-b4-v1-failure-closeout-v2-reseal-handoff-20260904"
TASK_V1 = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1"
TASK_V2 = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2"
V2_NAME = "Tilted / Recentered Microcanonical Fourier Cancellation — Integrity-Repair Reseal"
V2_STAGE = "STAGE_0_REPAIR_READY_NOT_DISPATCHED"
V2_OBJECTIVE = (
    "Produce a fresh Stage-0 seal for the SAME frozen B4 scientific program, with no scientific result imported "
    "from the invalid V1 Stage-1 invocation, and repair the execution launcher so that all contract-required "
    "witness fields are written and mechanically validated BEFORE T1 can begin. This is an execution-integrity "
    "repair, not a scientific route change."
)
FAIL_DIR = Path("research_manager/results/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_INPUT_INTEGRITY_FAILURE")
FORENSIC_NAMES = [
    "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_INPUT_INTEGRITY_FAILURE_REPORT.md",
    "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_INPUT_INTEGRITY_FAILURE_RECORD.json",
    "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_RUN_WITNESS_AS_PRODUCED.json",
    "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_INPUT_INTEGRITY_FAILURE_DRIVE_PERSISTENCE.json",
]
MANIFEST_NAME = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_INPUT_INTEGRITY_FAILURE_SHA256SUMS.txt"
PACKAGE_REF_NAME = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1_STAGE1_INPUT_INTEGRITY_FAILURE_PACKAGE_REFERENCE.json"
DECISION = Path("research_manager/decisions/CP20_TASK8B3_E7R_B4_V1_INPUT_INTEGRITY_FAILURE_CLOSEOUT_2026-09-04.md")
PROVENANCE = Path("research_manager/records/CP20_TASK8B3_E7R_B4_V1_MAIN_PLACEHOLDER_REVERT_PROVENANCE_2026-09-04.json")
V2_PROMPT = Path("research_manager/prompts/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE0_REPAIR_RESEAL_PROMPT_2026-09-04.md")
STATE = Path("CURRENT_RESEARCH_STATE.json")
HANDOFF = Path("START_HERE_CURRENT_HANDOFF.md")
JOURNAL = Path("research_manager/RESEARCH_JOURNAL.jsonl")
ARCHIVE = Path("Collatz_Research_Archive_CURRENT.zip")
BUILD = Path("CURRENT_ARCHIVE_BUILD.json")
ARCHIVE_ROOT = "Collatz Problemi — Araştırma Arşivi"


def run(args, *, check=True, text=True):
    p = subprocess.run(args, cwd=REPO, check=False, capture_output=True, text=text)
    if check and p.returncode != 0:
        raise RuntimeError(f"command failed: {args}\nstdout={p.stdout}\nstderr={p.stderr}")
    return p


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


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def now_tr() -> str:
    return datetime.now(timezone(timedelta(hours=3))).isoformat(timespec="seconds")


def download_drive(file_id: str, dest: Path) -> None:
    url = f"https://drive.usercontent.google.com/download?id={file_id}&export=download&confirm=t"
    urllib.request.urlretrieve(url, dest)


def verify_journal(lines: list[bytes]) -> str:
    prev = None
    for i, raw in enumerate(lines, start=1):
        row = json.loads(raw.decode("utf-8"))
        assert row["schema"] == "COLLATZ_RESEARCH_JOURNAL_V1"
        assert row["sequence"] == i
        assert row["previous_entry_sha256"] == prev
        prev = sha256_bytes(raw)
    return prev


def append_journal(lines: list[bytes], event: dict) -> None:
    prev = verify_journal(lines)
    event["sequence"] = len(lines) + 1
    event["previous_entry_sha256"] = prev
    event["schema"] = "COLLATZ_RESEARCH_JOURNAL_V1"
    raw = json.dumps(event, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    lines.append(raw)


def upsert_path_hash(rows: list[dict], path: str, digest: str) -> None:
    for row in rows:
        if row.get("path") == path:
            row["sha256"] = digest
            return
    rows.append({"path": path, "sha256": digest})


def local_from_archive_member(path: str) -> Path | None:
    rm = f"{ARCHIVE_ROOT}/RESEARCH_MANAGEMENT/"
    tooling = f"{ARCHIVE_ROOT}/REPOSITORY_TOOLING/"
    continuity = f"{ARCHIVE_ROOT}/CONTINUITY/"
    if path.startswith(rm):
        return Path("research_manager") / path[len(rm):]
    if path.startswith(tooling):
        return Path("tools") / path[len(tooling):]
    if path.startswith(continuity):
        suffix = path[len(continuity):]
        if suffix in {"START_HERE_CURRENT_HANDOFF.md", "CURRENT_RESEARCH_STATE.json"}:
            return Path(suffix)
    return None


def arc_for_repo(path: Path) -> str:
    p = path.as_posix()
    if p.startswith("research_manager/"):
        return f"{ARCHIVE_ROOT}/RESEARCH_MANAGEMENT/{p[len('research_manager/'):]}"
    if p.startswith("tools/"):
        return f"{ARCHIVE_ROOT}/REPOSITORY_TOOLING/{p[len('tools/'):]}"
    if p == "START_HERE_CURRENT_HANDOFF.md":
        return f"{ARCHIVE_ROOT}/CONTINUITY/START_HERE_CURRENT_HANDOFF.md"
    raise ValueError(p)


def main() -> None:
    if git("rev-parse", "HEAD") != REQUIRED_MAIN:
        raise AssertionError("checkout HEAD is not required current main")
    git("fetch", "origin", "main", FAILURE_BRANCH)
    if git("rev-parse", "origin/main") != REQUIRED_MAIN:
        raise AssertionError("origin/main moved before transaction")
    if git("rev-parse", f"origin/{FAILURE_BRANCH}") != FAILURE_COMMIT:
        raise AssertionError("failure branch head mismatch")
    if git("merge-base", OLD_AUTH_COMMIT, REQUIRED_MAIN) != OLD_AUTH_COMMIT:
        raise AssertionError("old authorization is not ancestor of required main")
    if git("diff", "--name-only", f"{OLD_AUTH_COMMIT}..{REQUIRED_MAIN}"):
        raise AssertionError("expected net files=[] between old authorization and required main")
    if int(git("rev-list", "--count", f"{OLD_AUTH_COMMIT}..{REQUIRED_MAIN}")) != 2:
        raise AssertionError("placeholder/revert history is not exactly two commits")

    state = json.loads(STATE.read_text(encoding="utf-8"))
    if state.get("active_integrator", {}).get("status") == "HELD":
        raise AssertionError("active integrator lock already HELD")
    if state["active_task"]["code"] != TASK_V1:
        raise AssertionError("unexpected active task before closeout")

    # Independent raw-hash verification only. Do not inspect the invalid package contents.
    pkg_tmp = Path("/tmp/b4_v1_failure_package.zip")
    man_tmp = Path("/tmp/b4_v1_failure_manifest.txt")
    download_drive(FAILURE_PACKAGE_FILE, pkg_tmp)
    download_drive(FAILURE_MANIFEST_FILE, man_tmp)
    if sha256_file(pkg_tmp) != FAILURE_PACKAGE_SHA:
        raise AssertionError("failure package Drive raw SHA mismatch")
    if sha256_file(man_tmp) != FORENSIC_MANIFEST_SHA:
        raise AssertionError("forensic manifest Drive raw SHA mismatch")

    # Acquire lock as its own canonical commit.
    acquired = now_tr()
    state["active_integrator"] = {
        "holder": HOLDER,
        "scope": "B4 V1 Stage-1 input-integrity failure canonical closeout plus V2 reseal handoff only; no Stage-1 rerun, no invalid T1–T8 mathematics intake, no new mathematics, no weighted/operator work, no E8, and no V2 Stage-0 execution.",
        "base_commit": REQUIRED_MAIN,
        "acquired_at": acquired,
        "status": "HELD",
    }
    write_json(STATE, state)
    git("add", STATE.as_posix())
    git("commit", "-m", "Acquire integrator lock for B4 V1 failure closeout")
    lock_commit = git("rev-parse", "HEAD")
    state = json.loads(STATE.read_text(encoding="utf-8"))
    state["active_integrator"]["lock_acquisition_commit"] = lock_commit
    write_json(STATE, state)
    git("add", STATE.as_posix())
    git("commit", "--amend", "--no-edit")
    lock_commit = git("rev-parse", "HEAD")
    # Amend changed SHA; record actual final acquisition commit in state and amend once more if needed.
    state = json.loads(STATE.read_text(encoding="utf-8"))
    state["active_integrator"]["lock_acquisition_commit"] = lock_commit
    write_json(STATE, state)
    git("add", STATE.as_posix())
    git("commit", "--amend", "--no-edit")
    lock_commit = git("rev-parse", "HEAD")
    # Do not self-reference the lock commit further; base_commit is the load-bearing stale-base field.
    git("push", "origin", "HEAD:main")
    git("fetch", "origin", "main")
    if git("rev-parse", "origin/main") != lock_commit:
        raise AssertionError("lock commit read-back failed")

    # Copy only the explicitly whitelisted forensic evidence. Never enumerate/import invalid drafts.
    FAIL_DIR.mkdir(parents=True, exist_ok=True)
    forensic_sha256 = {}
    for name in FORENSIC_NAMES:
        rel = (FAIL_DIR / name).as_posix()
        data = git_bytes("show", f"origin/{FAILURE_BRANCH}:{rel}")
        (FAIL_DIR / name).write_bytes(data)
        forensic_sha256[name] = sha256_bytes(data)

    # Validate only forensic record/witness mechanics, not mathematics.
    record = json.loads((FAIL_DIR / FORENSIC_NAMES[1]).read_text(encoding="utf-8"))
    witness = json.loads((FAIL_DIR / FORENSIC_NAMES[2]).read_text(encoding="utf-8"))
    if record.get("status") != "[B4 STAGE1 INPUT INTEGRITY FAILURE]":
        raise AssertionError("forensic failure verdict mismatch")
    if record.get("authorized_seal_sha256") != OLD_SEAL or record.get("contract_sha256") != OLD_CONTRACT:
        raise AssertionError("forensic seal/contract mismatch")
    if record.get("entrypoint_invocations_observed") != 1 or record.get("rerun_performed") is not False:
        raise AssertionError("forensic once-only/rerun record mismatch")
    if record.get("draft_mathematics_valid") is not False or record.get("scientific_state_changed") is not False:
        raise AssertionError("forensic invalid-draft/scientific-state classification mismatch")
    if "canonical_base_sha" in witness:
        raise AssertionError("produced witness unexpectedly contains canonical_base_sha")
    if witness.get("authorized_seal_sha256") != OLD_SEAL or witness.get("execution_count_claim") != 1:
        raise AssertionError("produced witness seal/count mismatch")

    # Preserve exact raw forensic manifest, but never materialize the invalid package on main.
    (FAIL_DIR / MANIFEST_NAME).write_bytes(man_tmp.read_bytes())
    package_ref = {
        "schema": "B4_V1_FORENSIC_PACKAGE_REFERENCE_V1",
        "failure_branch": FAILURE_BRANCH,
        "failure_branch_commit": FAILURE_COMMIT,
        "drive_folder_id": FAILURE_DRIVE_FOLDER,
        "package_drive_file_id": FAILURE_PACKAGE_FILE,
        "package_sha256": FAILURE_PACKAGE_SHA,
        "package_materialized_on_main": False,
        "forensic_manifest_drive_file_id": FAILURE_MANIFEST_FILE,
        "forensic_manifest_sha256": FORENSIC_MANIFEST_SHA,
        "drive_raw_readback": "PASS",
        "invalid_mathematical_contents_imported_to_main": False,
    }
    write_json(FAIL_DIR / PACKAGE_REF_NAME, package_ref)

    provenance = {
        "schema": "B4_V1_MAIN_PLACEHOLDER_REVERT_PROVENANCE_V1",
        "old_authorization_commit": OLD_AUTH_COMMIT,
        "temporary_placeholder_commit": PLACEHOLDER_COMMIT,
        "immediate_revert_commit": REVERT_COMMIT,
        "compare_base": OLD_AUTH_COMMIT,
        "compare_head": REVERT_COMMIT,
        "net_files": [],
        "history_rewritten": False,
        "classification": "PROVENANCE_ONLY",
    }
    write_json(PROVENANCE, provenance)

    DECISION.parent.mkdir(parents=True, exist_ok=True)
    DECISION.write_text(f"""# CP20_TASK8B3_E7R_B4 — V1 INPUT-INTEGRITY FAILURE CANONICAL CLOSEOUT\n\nCloseout verdict: **[B4 STAGE1 INPUT INTEGRITY FAILURE]**.\n\nThe old authorized seal `{OLD_SEAL}` is **[CONSUMED — MUST NOT BE REUSED OR REAUTHORIZED]**. The old V1 authorization at `{OLD_AUTH_COMMIT}` is **[CONSUMED / CLOSED]**. The canonical contract remains `{OLD_CONTRACT}` for provenance only.\n\nThe contract required the pre-T1 `RUN_WITNESS` to contain the canonical base SHA. The produced witness omitted that required field. The launcher was invoked exactly once; no rerun occurred. Some T1–T8 draft work occurred before detection, but all such mathematical outputs are **[INVALID / NON-CANONICAL / DO NOT USE]** and are not imported by this integration.\n\n## Scientific state\n\n- B4 V1 Stage 0: **[FROZEN — SCIENTIFIC PROGRAM PRESERVED]**\n- B4 V1 Stage 1: **[INPUT INTEGRITY FAILURE — INVALID / NON-CANONICAL]**\n- B4-N1: NOT ESTABLISHED\n- B4-N2: NOT ESTABLISHED\n- B4-N3: NOT ESTABLISHED\n- B4-N4: NOT ESTABLISHED\n- B4-N5: NOT ESTABLISHED\n- B4-N6: NOT ESTABLISHED\n- B4-N7: NOT ESTABLISHED\n- B4-CT: NOT ESTABLISHED\n- E6-N2: **[OPEN]**\n\nThe invalid drafts must not influence canonical science.\n\n## Forensic evidence\n\nFailure branch `{FAILURE_BRANCH}` @ `{FAILURE_COMMIT}`. Failure package SHA-256 `{FAILURE_PACKAGE_SHA}`. Forensic manifest SHA-256 `{FORENSIC_MANIFEST_SHA}`. Drive folder `{FAILURE_DRIVE_FOLDER}`; raw read-back PASS. Only the integrity-failure report, failure record, produced witness, exact manifest/hash references, and Drive persistence record are canonicalized. The invalid package contents are not imported to main.\n\n## Main-history provenance\n\nThe accidental placeholder `{PLACEHOLDER_COMMIT}` was immediately reverted by `{REVERT_COMMIT}`. Compare `{OLD_AUTH_COMMIT}` → `{REVERT_COMMIT}` has net `files: []`. History is preserved and not rewritten.\n\n## Next task\n\n`{TASK_V2}` — **{V2_NAME}**\n\nStage: `{V2_STAGE}`.\n\nObjective: {V2_OBJECTIVE}\n\nV2 Stage 0 is not executed or dispatched by this closeout.\n\nNothing in this closeout proves the Collatz conjecture.\n""", encoding="utf-8", newline="\n")

    V2_PROMPT.parent.mkdir(parents=True, exist_ok=True)
    V2_PROMPT.write_text(f"""# {TASK_V2} — STAGE 0 INTEGRITY-REPAIR RESEAL HANDOFF\n\nStatus: `{V2_STAGE}`. **NOT DISPATCHED.**\n\nObjective: {V2_OBJECTIVE}\n\nThis is an execution-integrity repair, not a scientific route change.\n\nThe future V2 Stage-0 task must:\n\n1. start from the post-failure canonical main produced by the V1 closeout;\n2. preserve the B4 scientific target and frozen T1–T8 / F1–F10 program unless an independently discovered pre-execution defect requires an explicit new seal;\n3. NOT read or reuse invalid V1 T1–T8 mathematical drafts;\n4. use the V1 forensic failure only to identify the mechanical launcher defect;\n5. make `RUN_WITNESS` contain at minimum `canonical_base_sha`, `authorized_seal_sha256`, `config_sha256`, `execution_count_claim`, `output_absence_precheck`, UTC timestamp, PID/session identifier, and exact entrypoint identity;\n6. BEFORE any T1 action, mechanically validate the completed witness against a frozen schema;\n7. abort before mathematics if any required field is missing, empty, malformed, or inconsistent;\n8. preregister a Stage-0 witness self-test on a synthetic/test destination proving: missing `canonical_base_sha` => FAIL; wrong `canonical_base_sha` => FAIL; correct `canonical_base_sha` => PASS;\n9. keep the actual Stage-1 launcher once-only;\n10. require a new V2 seal and fresh authorization for every source/launcher change.\n\nContamination control: future V2 Stage 1 must run in a fresh computation session/chat that has not seen invalid V1 T1–T8 mathematical drafts. It may read canonical scientific inputs, the V1 integrity-failure forensic record, the produced defective witness, and the statement of the mechanical defect. It must NOT read invalid V1 mathematical draft outputs.\n\nDo not begin Stage 1, weighted/operator work, or E8 from this handoff alone.\n""", encoding="utf-8", newline="\n")

    # Append provenance and closeout/V2-ready events without rewriting history.
    lines = JOURNAL.read_bytes().splitlines()
    verify_journal(lines)
    append_journal(lines, {
        "active_stage": "STAGE_1_INPUT_INTEGRITY_FAILURE_CLOSEOUT",
        "active_task": TASK_V1,
        "event": "B4_V1_MAIN_PLACEHOLDER_REVERT_PROVENANCE",
        "timestamp": now_tr(),
        "evidence": {
            "old_authorization_commit": OLD_AUTH_COMMIT,
            "temporary_placeholder_commit": PLACEHOLDER_COMMIT,
            "revert_commit": REVERT_COMMIT,
            "net_files": [],
            "history_rewritten": False,
        },
        "next_action": "Canonically close the B4 V1 input-integrity failure without importing invalid mathematics, then hand off V2 Stage 0 repair reseal as not dispatched.",
    })
    append_journal(lines, {
        "active_stage": V2_STAGE,
        "active_task": TASK_V2,
        "event": "B4_V1_INPUT_INTEGRITY_FAILURE_CLOSED_V2_RESEAL_READY",
        "timestamp": now_tr(),
        "evidence": {
            "failure_verdict": "[B4 STAGE1 INPUT INTEGRITY FAILURE]",
            "old_seal_sha256": OLD_SEAL,
            "old_seal_status": "[CONSUMED — MUST NOT BE REUSED OR REAUTHORIZED]",
            "old_authorization_status": "[CONSUMED / CLOSED]",
            "failure_branch_commit": FAILURE_COMMIT,
            "failure_package_sha256": FAILURE_PACKAGE_SHA,
            "forensic_manifest_sha256": FORENSIC_MANIFEST_SHA,
            "drive_raw_readback": "PASS",
            "entrypoint_invocations_observed": 1,
            "rerun_performed": False,
            "invalid_drafts_canonicalized": False,
            "scientific_state_changed": False,
            "e6_n2": "[OPEN]",
            "v2_stage0_dispatched": False,
        },
        "next_action": "Prepare and execute Stage 0 only for CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2 under the recorded integrity-repair reseal requirements; do not read invalid V1 T1–T8 drafts and do not execute V2 Stage 1, weighted/operator work, or E8.",
    })
    JOURNAL.write_bytes(b"\n".join(lines) + b"\n")

    # Update canonical state exactly as a failure closeout and V2 repair-ready handoff.
    state = json.loads(STATE.read_text(encoding="utf-8"))
    state["active_task"] = {
        "code": TASK_V2,
        "name": V2_NAME,
        "stage": V2_STAGE,
        "objective": V2_OBJECTIVE,
        "scientific_route_change": False,
    }
    state["b4_v1_closeout"] = {
        "stage0_status": "[FROZEN — SCIENTIFIC PROGRAM PRESERVED]",
        "stage1_status": "[INPUT INTEGRITY FAILURE — INVALID / NON-CANONICAL]",
        "old_seal_sha256": OLD_SEAL,
        "old_seal_status": "[CONSUMED — MUST NOT BE REUSED OR REAUTHORIZED]",
        "old_contract_sha256": OLD_CONTRACT,
        "old_authorization_commit": OLD_AUTH_COMMIT,
        "old_authorization_status": "[CONSUMED / CLOSED]",
        "failure_branch": FAILURE_BRANCH,
        "failure_branch_commit": FAILURE_COMMIT,
        "failure_package_sha256": FAILURE_PACKAGE_SHA,
        "forensic_manifest_sha256": FORENSIC_MANIFEST_SHA,
        "drive_folder_id": FAILURE_DRIVE_FOLDER,
        "drive_raw_readback": "PASS",
        "entrypoint_invocations_observed": 1,
        "rerun_performed": False,
        "invalid_drafts_status": "[INVALID / NON-CANONICAL / DO NOT USE]",
        "invalid_drafts_imported_to_main": False,
        "invalid_drafts_may_influence_canonical_science": False,
        "claims": {
            "B4-N1": "NOT ESTABLISHED",
            "B4-N2": "NOT ESTABLISHED",
            "B4-N3": "NOT ESTABLISHED",
            "B4-N4": "NOT ESTABLISHED",
            "B4-N5": "NOT ESTABLISHED",
            "B4-N6": "NOT ESTABLISHED",
            "B4-N7": "NOT ESTABLISHED",
            "B4-CT": "NOT ESTABLISHED",
            "E6-N2": "[OPEN]",
        },
        "main_history_provenance": {
            "temporary_placeholder_commit": PLACEHOLDER_COMMIT,
            "revert_commit": REVERT_COMMIT,
            "compare_base": OLD_AUTH_COMMIT,
            "compare_head": REVERT_COMMIT,
            "net_files": [],
            "history_rewritten": False,
        },
    }
    if "b4_stage0" in state:
        state["b4_stage0"]["status"] = "[FROZEN — SCIENTIFIC PROGRAM PRESERVED]"
        state["b4_stage0"]["stage1_authorized_historically"] = True
        state["b4_stage0"]["stage1_authorized"] = False
        state["b4_stage0"]["stage1_authorization_status"] = "[CONSUMED / CLOSED]"
        state["b4_stage0"]["seal_status"] = "[CONSUMED — MUST NOT BE REUSED OR REAUTHORIZED]"
        state["b4_stage0"]["stage1_execution_status"] = "[INPUT INTEGRITY FAILURE — INVALID / NON-CANONICAL]"
    state["b4_v2_reseal"] = {
        "task": TASK_V2,
        "name": V2_NAME,
        "stage": V2_STAGE,
        "objective": V2_OBJECTIVE,
        "stage0_dispatched": False,
        "stage0_executed": False,
        "scientific_program_preserved": True,
        "scientific_route_change": False,
        "contamination_control": {
            "fresh_stage1_session_required": True,
            "may_read": [
                "canonical scientific inputs",
                "V1 integrity-failure forensic record",
                "produced defective witness",
                "statement of the mechanical defect",
            ],
            "must_not_read": ["invalid V1 T1–T8 mathematical draft outputs"],
        },
        "witness_required_fields": [
            "canonical_base_sha",
            "authorized_seal_sha256",
            "config_sha256",
            "execution_count_claim",
            "output_absence_precheck",
            "UTC timestamp",
            "PID/session identifier",
            "exact entrypoint identity",
        ],
        "witness_self_test": {
            "missing_canonical_base_sha": "FAIL",
            "wrong_canonical_base_sha": "FAIL",
            "correct_canonical_base_sha": "PASS",
            "synthetic_test_destination_only": True,
        },
    }
    state.setdefault("documents", {})
    state["documents"]["accepted_checkpoint_decision"] = DECISION.as_posix()
    state["documents"]["active_authorization_decision"] = None
    state["documents"]["active_authorization_prompt"] = None
    state["documents"]["active_research_prompt"] = V2_PROMPT.as_posix()
    state["documents"]["b4_v1_failure_record"] = (FAIL_DIR / FORENSIC_NAMES[1]).as_posix()
    state["documents"]["b4_v1_defective_witness"] = (FAIL_DIR / FORENSIC_NAMES[2]).as_posix()
    state["documents"]["b4_v1_forensic_package_reference"] = (FAIL_DIR / PACKAGE_REF_NAME).as_posix()
    state["documents"]["b4_v2_stage0_repair_prompt"] = V2_PROMPT.as_posix()
    state.setdefault("continuity", {})["minimum_required_commit"] = lock_commit
    state.setdefault("next_action", {})["instruction"] = "Prepare and execute Stage 0 only for CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2 under the recorded integrity-repair reseal requirements; do not read or reuse invalid V1 T1–T8 mathematical drafts. Do not execute V2 Stage 1, weighted/operator work, or E8."
    state["next_action"]["prohibited"] = [
        "rerun or reauthorize B4 V1 Stage 1",
        "reuse old V1 seal",
        "inspect, adjudicate, summarize, import, or use invalid V1 T1–T8 mathematical drafts",
        "new mathematics in this closeout",
        "weighted/operator work",
        "E8",
        "V2 Stage 0 execution in this closeout",
    ]

    HANDOFF.write_text(f"""# START HERE — Current Collatz Research Handoff\n\nMachine-readable authority: `CURRENT_RESEARCH_STATE.json`. Recover on branch `main`, run `python tools/verify_handoff.py`, and require `HANDOFF VERIFICATION: PASS` before any research action.\n\n## B4 V1 canonical closeout\n\nB4 V1 Stage 0: **[FROZEN — SCIENTIFIC PROGRAM PRESERVED]**.\n\nB4 V1 Stage 1: **[INPUT INTEGRITY FAILURE — INVALID / NON-CANONICAL]**. The pre-T1 `RUN_WITNESS` omitted the contract-required canonical base SHA. The launcher was invoked once; no rerun occurred. All subsequent V1 T1–T8 mathematical drafts are **[INVALID / NON-CANONICAL / DO NOT USE]** and are not canonical evidence.\n\nOld V1 seal `{OLD_SEAL}`: **[CONSUMED — MUST NOT BE REUSED OR REAUTHORIZED]**. Old V1 authorization: **[CONSUMED / CLOSED]**.\n\nB4-N1 through B4-N7 and B4-CT are all **NOT ESTABLISHED**. `E6-N2` remains **[OPEN]**. The invalid drafts must not influence canonical science.\n\nForensic source: `{FAILURE_BRANCH}` @ `{FAILURE_COMMIT}`; package SHA-256 `{FAILURE_PACKAGE_SHA}`; forensic manifest SHA-256 `{FORENSIC_MANIFEST_SHA}`; Drive folder `{FAILURE_DRIVE_FOLDER}` with raw read-back PASS. Canonical main contains only the forensic failure report/record, produced defective witness, manifest/hash references, and Drive persistence provenance — not invalid mathematical draft contents.\n\nMain provenance only: accidental placeholder `{PLACEHOLDER_COMMIT}` was immediately reverted by `{REVERT_COMMIT}`. Compare `{OLD_AUTH_COMMIT}` → `{REVERT_COMMIT}` has net `files: []`. History was not rewritten.\n\n## Exact next task\n\nCode: `{TASK_V2}`\n\nName: **{V2_NAME}**\n\nStage: `{V2_STAGE}`\n\nObjective: {V2_OBJECTIVE}\n\nV2 Stage 0 must repair the launcher/witness path before any future T1 action, including frozen-schema validation and the preregistered canonical-base witness self-tests. It must not read or reuse invalid V1 T1–T8 drafts. Any future V2 Stage 1 must run in a fresh computation session/chat uncontaminated by those drafts.\n\nV2 Stage 0 is **NOT DISPATCHED** and was not executed by this closeout. No Stage-1 rerun, weighted/operator work, E8, or new mathematics is authorized by recovery alone.\n\nNothing in this closeout proves the Collatz conjecture.\n""", encoding="utf-8", newline="\n")

    # Release lock in the final milestone state (remote remains HELD until final push).
    state["active_integrator"]["status"] = "RELEASED"
    state["active_integrator"]["released_at"] = now_tr()

    # Refresh integrity hashes for all existing mutable repository files and add new evidence.
    integrity = state.setdefault("integrity", {})
    repo_rows = integrity.setdefault("repository_files", [])
    for row in repo_rows:
        p = Path(row["path"])
        if p.is_file() and p != STATE:
            row["sha256"] = sha256_file(p)
    new_repo_files = [
        HANDOFF, JOURNAL, DECISION, PROVENANCE, V2_PROMPT,
        *(FAIL_DIR / n for n in FORENSIC_NAMES),
        FAIL_DIR / MANIFEST_NAME,
        FAIL_DIR / PACKAGE_REF_NAME,
    ]
    for p in new_repo_files:
        upsert_path_hash(repo_rows, p.as_posix(), sha256_file(p))
    repo_rows.sort(key=lambda r: r["path"])

    archive_rows = integrity.setdefault("archive_members", [])
    for row in archive_rows:
        local = local_from_archive_member(row["path"])
        if local is not None and local.is_file() and local != STATE:
            row["sha256"] = sha256_file(local)
    for p in new_repo_files:
        upsert_path_hash(archive_rows, arc_for_repo(p), sha256_file(p))
    archive_rows.sort(key=lambda r: r["path"])
    write_json(STATE, state)

    # Build deterministic archive from the final local state, then commit everything.
    run(["python", "tools/build_current_archive.py"])
    build = json.loads(BUILD.read_text(encoding="utf-8"))
    headroom = 100_000_000 - int(build["zip_bytes"])
    if headroom <= 0:
        raise AssertionError("archive has no GitHub headroom")

    git("add", "-A")
    git("commit", "-m", "Close B4 V1 integrity failure and hand off V2 reseal")
    final_commit = git("rev-parse", "HEAD")

    # Real verifier on the exact final commit before publication.
    verify = run(["python", "tools/verify_handoff.py"]).stdout
    if "HANDOFF VERIFICATION: PASS" not in verify:
        raise AssertionError("handoff verifier did not PASS")
    Path("FINAL_HANDOFF_VERIFICATION.txt").write_text(verify, encoding="utf-8", newline="\n")

    # Fail closed if main changed while the lock was held.
    git("fetch", "origin", "main")
    if git("rev-parse", "origin/main") != lock_commit:
        raise AssertionError("origin/main changed while integrator lock was held")
    git("push", "origin", "HEAD:main")
    git("fetch", "origin", "main")
    if git("rev-parse", "origin/main") != final_commit:
        raise AssertionError("final main read-back SHA mismatch")

    remote_state = json.loads(git_bytes("show", "origin/main:CURRENT_RESEARCH_STATE.json").decode("utf-8"))
    if remote_state["active_integrator"]["status"] != "RELEASED":
        raise AssertionError("remote lock is not RELEASED")
    if remote_state["active_task"]["code"] != TASK_V2 or remote_state["active_task"]["stage"] != V2_STAGE:
        raise AssertionError("remote V2 task/stage mismatch")
    if remote_state["b4_v1_closeout"]["old_seal_status"] != "[CONSUMED — MUST NOT BE REUSED OR REAUTHORIZED]":
        raise AssertionError("remote old-seal retirement mismatch")
    if remote_state["b4_v1_closeout"]["claims"]["E6-N2"] != "[OPEN]":
        raise AssertionError("remote E6-N2 mismatch")
    for name in FORENSIC_NAMES:
        rel = (FAIL_DIR / name).as_posix()
        if git_bytes("show", f"origin/main:{rel}") != git_bytes("show", f"origin/{FAILURE_BRANCH}:{rel}"):
            raise AssertionError(f"forensic byte read-back mismatch: {name}")
    if sha256_bytes(git_bytes("show", f"origin/main:{(FAIL_DIR / MANIFEST_NAME).as_posix()}")) != FORENSIC_MANIFEST_SHA:
        raise AssertionError("canonical forensic manifest read-back mismatch")

    readback = {
        "status": "PASS",
        "final_main_sha": final_commit,
        "lock_commit": lock_commit,
        "lock_status": "RELEASED",
        "active_task": TASK_V2,
        "active_stage": V2_STAGE,
        "old_seal_status": "[CONSUMED — MUST NOT BE REUSED OR REAUTHORIZED]",
        "old_authorization_status": "[CONSUMED / CLOSED]",
        "forensic_files_byte_equal_to_failure_branch": f"{len(FORENSIC_NAMES)}/{len(FORENSIC_NAMES)}",
        "forensic_manifest_sha256": FORENSIC_MANIFEST_SHA,
        "invalid_math_imported": False,
        "v2_stage0_executed": False,
    }
    write_json(Path("GITHUB_READBACK.json"), readback)
    summary = {
        "closeout_verdict": "[B4 V1 STAGE 1 — INPUT INTEGRITY FAILURE — CANONICALLY CLOSED]",
        "final_main_sha": final_commit,
        "lock_commit": lock_commit,
        "failure_branch_commit": FAILURE_COMMIT,
        "failure_package_sha256": FAILURE_PACKAGE_SHA,
        "forensic_manifest_sha256": FORENSIC_MANIFEST_SHA,
        "old_seal_sha256": OLD_SEAL,
        "old_seal_status": "[CONSUMED — MUST NOT BE REUSED OR REAUTHORIZED]",
        "old_authorization_status": "[CONSUMED / CLOSED]",
        "claims": remote_state["b4_v1_closeout"]["claims"],
        "archive_sha256": build["archive_sha256"],
        "archive_bytes": build["zip_bytes"],
        "archive_members": build["member_count"],
        "archive_headroom_bytes": headroom,
        "handoff_verification": "PASS",
        "github_readback": "PASS",
        "drive_forensic_raw_readback": "PASS",
        "next_task": TASK_V2,
        "next_stage": V2_STAGE,
        "v2_stage0_executed": False,
        "stage1_rerun_performed": False,
    }
    write_json(Path("CANONICAL_CLOSEOUT_SUMMARY.json"), summary)
    write_json(Path("ARCHIVE_BUDGET.json"), {
        "archive_sha256": build["archive_sha256"],
        "archive_bytes": build["zip_bytes"],
        "github_builder_hard_limit_bytes": 100_000_000,
        "headroom_bytes": headroom,
    })
    Path("FINAL_SHA.txt").write_text(final_commit + "\n", encoding="utf-8")
    Path("LOCK_COMMIT.txt").write_text(lock_commit + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
