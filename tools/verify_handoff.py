#!/usr/bin/env python3
"""Read-only verifier for a fresh Collatz research handoff.

The verifier distinguishes content integrity from Git-history availability:
- a present historical base commit must be an ancestor of HEAD;
- in a shallow clone, a RELEASED historical lock whose base object was not
  fetched is reported as a warning rather than a false corruption failure;
- a HELD lock still requires its base commit and ancestry to be verifiable;
- detached HEAD is accepted only when HEAD exactly matches the expected local
  branch/ref tip, and is reported explicitly.
"""

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


def git_run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=REPO, text=True, encoding="utf-8", capture_output=True, check=False)


def git_value(*args: str) -> str:
    proc = git_run(*args)
    if proc.returncode != 0:
        raise AssertionError((proc.stdout + proc.stderr).strip())
    return proc.stdout.strip()


def git_ok(*args: str) -> bool:
    return git_run(*args).returncode == 0


def git_is_shallow() -> bool:
    return git_value("rev-parse", "--is-shallow-repository") == "true"


def commit_exists(sha: str) -> bool:
    return git_ok("cat-file", "-e", f"{sha}^{{commit}}")


def require_ancestor(base: str, tip: str = "HEAD") -> None:
    if not git_ok("merge-base", "--is-ancestor", base, tip):
        raise AssertionError(f"required base commit is not an ancestor of {tip}: {base}")


def verify_history_commit(sha: str, *, required: bool, label: str, warnings: list[str]) -> None:
    if commit_exists(sha):
        require_ancestor(sha)
        return
    if git_is_shallow() and not required:
        warnings.append(f"{label} {sha} is outside shallow history; ancestry was not checked. Use git fetch --unshallow (or deepen the clone) for full historical verification.")
        return
    raise AssertionError(f"required commit object unavailable: {label}={sha}")


def verify_branch_context(expected: str, warnings: list[str]) -> str:
    branch = git_value("branch", "--show-current")
    if branch:
        if branch != expected:
            raise AssertionError(f"branch mismatch: {branch} != {expected}")
        return branch
    head = git_value("rev-parse", "HEAD")
    candidates = (f"refs/heads/{expected}", f"refs/remotes/origin/{expected}")
    matched = []
    for ref in candidates:
        if git_ok("show-ref", "--verify", "--quiet", ref) and git_value("rev-parse", ref) == head:
            matched.append(ref)
    if not matched:
        raise AssertionError(f"detached HEAD {head} does not match an available {expected} branch tip")
    warnings.append(f"detached HEAD accepted at expected branch tip: {matched[0]}")
    return f"DETACHED@{expected}"


def main() -> None:
    warnings: list[str] = []
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    build = json.loads(BUILD_PATH.read_text(encoding="utf-8"))
    if state["schema"] != "COLLATZ_CURRENT_RESEARCH_STATE_V1":
        raise AssertionError("state schema mismatch")
    if build["schema"] != "COLLATZ_CURRENT_ARCHIVE_BUILD_V1":
        raise AssertionError("build schema mismatch")
    allowed_stages = {"STAGE_1_AUTHORIZED_NOT_EXECUTED", "STAGE_1_RUNNING", "RESULT_RETURNED_UNVERIFIED", "AUDIT_PENDING", "ACCEPTED", "STAGE_0_READY_NOT_DISPATCHED", "STAGE_0_REPAIR_READY_NOT_DISPATCHED", "STAGE_0_RUNNING", "PRE_RUN_SEAL_AWAITING_AUTHORIZATION", "STAGE_1_INPUT_INTEGRITY_FAILURE_AUTHORIZATION_CONSUMED_CLOSED"}
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
        verify_history_commit(lock["base_commit"], required=lock["status"] == "HELD", label="active_integrator.base_commit", warnings=warnings)

    minimum_required = state.get("continuity", {}).get("minimum_required_commit")
    if minimum_required:
        verify_history_commit(minimum_required, required=False, label="continuity.minimum_required_commit", warnings=warnings)

    branch = verify_branch_context(state["continuity"]["repository_branch"], warnings)

    for row in state["integrity"]["repository_files"]:
        path = REPO / row["path"]
        if digest_file(path) != row["sha256"]:
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
    for warning in warnings:
        print(f"WARNING: {warning}")
    print("HANDOFF VERIFICATION: PASS")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"HANDOFF VERIFICATION: FAIL — {exc}", file=sys.stderr)
        raise
