#!/usr/bin/env python3
"""Read-only verifier for a fresh Collatz research handoff."""

from __future__ import annotations

from pathlib import Path
import hashlib
import json
import subprocess
import sys
import zipfile


REPO = Path(__file__).resolve().parents[1]
STATE_PATH = REPO / "CURRENT_RESEARCH_STATE.json"
BUILD_PATH = REPO / "CURRENT_ARCHIVE_BUILD.json"
JOURNAL_PATH = REPO / "research_manager" / "RESEARCH_JOURNAL.jsonl"


def digest_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def verify_journal() -> int:
    raw_lines = JOURNAL_PATH.read_bytes().splitlines()
    if not raw_lines:
        raise AssertionError("research journal is empty")
    previous = None
    for index, raw in enumerate(raw_lines, start=1):
        row = json.loads(raw.decode("utf-8"))
        if row["schema"] != "COLLATZ_RESEARCH_JOURNAL_V1":
            raise AssertionError(f"journal schema mismatch at {index}")
        if row["sequence"] != index:
            raise AssertionError(f"journal sequence mismatch at {index}")
        if row["previous_entry_sha256"] != previous:
            raise AssertionError(f"journal hash-chain mismatch at {index}")
        previous = digest_bytes(raw)
    return len(raw_lines)


def git_value(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=REPO,
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise AssertionError(proc.stdout + proc.stderr)
    return proc.stdout.strip()


def main() -> None:
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    build = json.loads(BUILD_PATH.read_text(encoding="utf-8"))
    if state["schema"] != "COLLATZ_CURRENT_RESEARCH_STATE_V1":
        raise AssertionError("state schema mismatch")
    if build["schema"] != "COLLATZ_CURRENT_ARCHIVE_BUILD_V1":
        raise AssertionError("build schema mismatch")
    allowed_stages = {
        "STAGE_1_AUTHORIZED_NOT_EXECUTED",
        "STAGE_1_RUNNING",
        "RESULT_RETURNED_UNVERIFIED",
        "AUDIT_PENDING",
        "ACCEPTED",
        "STAGE_0_READY_NOT_DISPATCHED",
        "STAGE_0_RUNNING",
        "PRE_RUN_SEAL_AWAITING_AUTHORIZATION",
    }
    if state["active_task"]["stage"] not in allowed_stages:
        raise AssertionError("unrecognized active stage")
    if not state["next_action"]["instruction"]:
        raise AssertionError("next action is empty")

    lock = state.get("active_integrator")
    if lock is not None:
        required = {"holder", "scope", "base_commit", "acquired_at", "status"}
        missing = required - set(lock)
        if missing:
            raise AssertionError(f"active_integrator missing keys: {sorted(missing)}")
        if lock["status"] not in {"HELD", "RELEASED"}:
            raise AssertionError(f"active_integrator status invalid: {lock['status']}")
        if lock["status"] == "HELD" and not lock["holder"]:
            raise AssertionError("active_integrator is HELD with no holder")
        if not lock["scope"]:
            raise AssertionError("active_integrator scope is empty")
        git_value("cat-file", "-e", f"{lock['base_commit']}^{{commit}}")

    branch = git_value("branch", "--show-current")
    if branch != state["continuity"]["repository_branch"]:
        raise AssertionError(f"branch mismatch: {branch}")

    for row in state["integrity"]["repository_files"]:
        path = REPO / row["path"]
        actual = digest_file(path)
        if actual != row["sha256"]:
            raise AssertionError(f"repository hash mismatch: {row['path']}")

    archive = REPO / build["archive"]
    if archive.name != state["archive"]["current_archive"]:
        raise AssertionError("archive name mismatch")
    if digest_file(archive) != build["archive_sha256"]:
        raise AssertionError("current archive hash mismatch")
    if archive.stat().st_size != build["zip_bytes"]:
        raise AssertionError("current archive size mismatch")

    with zipfile.ZipFile(archive) as zf:
        if len(zf.infolist()) != build["member_count"]:
            raise AssertionError("archive member-count mismatch")
        bad = zf.testzip()
        if bad is not None:
            raise AssertionError(f"archive CRC failure: {bad}")
        names = {item.filename for item in zf.infolist()}
        for row in state["integrity"]["archive_members"]:
            if row["path"] not in names:
                raise AssertionError(f"archive member missing: {row['path']}")
            if digest_bytes(zf.read(row["path"])) != row["sha256"]:
                raise AssertionError(f"archive member hash mismatch: {row['path']}")

    journal_rows = verify_journal()
    print(f"branch={branch}")
    print(f"head={git_value('rev-parse', 'HEAD')}")
    print(f"active_task={state['active_task']['code']}")
    print(f"active_stage={state['active_task']['stage']}")
    print(f"journal_rows={journal_rows}")
    print(f"archive_members={build['member_count']}")
    print(f"archive_sha256={build['archive_sha256']}")
    print("HANDOFF VERIFICATION: PASS")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"HANDOFF VERIFICATION: FAIL — {exc}", file=sys.stderr)
        raise
