#!/usr/bin/env python3
"""Read-only verifier for a fresh Collatz research handoff.

The verifier distinguishes content integrity from Git-history availability:
- tracked working-tree/index drift from HEAD is rejected (untracked files are
  ignored because recovery tools may intentionally create them);
- a present historical base commit must be an ancestor of HEAD;
- in a shallow clone, a RELEASED historical lock whose base object was not
  fetched is reported as a warning rather than a false corruption failure;
- a HELD lock still requires its base commit and ancestry to be verifiable;
- detached HEAD is accepted only when HEAD exactly matches the expected local
  branch/ref tip, and is reported explicitly;
- every non-directory archive member is hashed and reduced to a deterministic
  member-root, in addition to whole-ZIP SHA/size/count/CRC verification.
"""
from __future__ import annotations
from pathlib import Path
import hashlib,json,subprocess,sys,zipfile

REPO=Path(__file__).resolve().parents[1]
STATE_PATH=REPO/"CURRENT_RESEARCH_STATE.json"
BUILD_PATH=REPO/"CURRENT_ARCHIVE_BUILD.json"
MEMBER_ROOT_PATH=REPO/"CURRENT_ARCHIVE_MEMBER_ROOT.json"
JOURNAL_PATH=REPO/"research_manager"/"RESEARCH_JOURNAL.jsonl"

def digest_file(path):
    h=hashlib.sha256()
    with path.open("rb") as s:
        for b in iter(lambda:s.read(1<<20),b""): h.update(b)
    return h.hexdigest()
def digest_bytes(data): return hashlib.sha256(data).hexdigest()
def archive_member_root(zf):
    root=hashlib.sha256(); count=0
    for item in sorted((x for x in zf.infolist() if not x.is_dir()),key=lambda x:x.filename):
        h=hashlib.sha256()
        with zf.open(item) as s:
            for b in iter(lambda:s.read(1<<20),b""): h.update(b)
        root.update(f"{item.filename}\0{item.file_size}\0{h.hexdigest()}\n".encode("utf-8")); count+=1
    return count,root.hexdigest()
def verify_journal():
    raw_lines=JOURNAL_PATH.read_bytes().splitlines()
    if not raw_lines: raise AssertionError("research journal is empty")
    previous=None
    for index,raw in enumerate(raw_lines,start=1):
        row=json.loads(raw.decode("utf-8"))
        if row["schema"]!="COLLATZ_RESEARCH_JOURNAL_V1": raise AssertionError(f"journal schema mismatch at {index}")
        if row["sequence"]!=index: raise AssertionError(f"journal sequence mismatch at {index}")
        if row["previous_entry_sha256"]!=previous: raise AssertionError(f"journal hash-chain mismatch at {index}")
        previous=digest_bytes(raw)
    return len(raw_lines)
def git_run(*args): return subprocess.run(["git",*args],cwd=REPO,text=True,encoding="utf-8",capture_output=True,check=False)
def git_value(*args):
    p=git_run(*args)
    if p.returncode!=0: raise AssertionError((p.stdout+p.stderr).strip())
    return p.stdout.strip()
def git_ok(*args): return git_run(*args).returncode==0
def git_is_shallow(): return git_value("rev-parse","--is-shallow-repository")=="true"
def commit_exists(sha): return git_ok("cat-file","-e",f"{sha}^{{commit}}")
def require_ancestor(base,tip="HEAD"):
    if not git_ok("merge-base","--is-ancestor",base,tip): raise AssertionError(f"required base commit is not an ancestor of {tip}: {base}")
def verify_tracked_worktree_clean():
    p=git_run("status","--porcelain","--untracked-files=no")
    if p.returncode!=0: raise AssertionError((p.stdout+p.stderr).strip())
    if p.stdout.strip(): raise AssertionError("tracked working tree/index differs from HEAD")
def verify_history_commit(sha,*,required,label,warnings):
    if commit_exists(sha): require_ancestor(sha); return
    if git_is_shallow() and not required:
        warnings.append(f"{label} {sha} is outside shallow history; ancestry was not checked. Use git fetch --unshallow (or deepen the clone) for full historical verification."); return
    raise AssertionError(f"required commit object unavailable: {label}={sha}")
def verify_branch_context(expected,warnings):
    branch=git_value("branch","--show-current")
    if branch:
        if branch!=expected: raise AssertionError(f"branch mismatch: {branch} != {expected}")
        return branch
    head=git_value("rev-parse","HEAD"); matched=[]
    for ref in (f"refs/heads/{expected}",f"refs/remotes/origin/{expected}"):
        if git_ok("show-ref","--verify","--quiet",ref) and git_value("rev-parse",ref)==head: matched.append(ref)
    if not matched: raise AssertionError(f"detached HEAD {head} does not match an available {expected} branch tip")
    warnings.append(f"detached HEAD accepted at expected branch tip: {matched[0]}"); return f"DETACHED@{expected}"

def main():
    warnings=[]
    verify_tracked_worktree_clean()
    state=json.loads(STATE_PATH.read_text(encoding="utf-8")); build=json.loads(BUILD_PATH.read_text(encoding="utf-8")); member_record=json.loads(MEMBER_ROOT_PATH.read_text(encoding="utf-8"))
    if state["schema"]!="COLLATZ_CURRENT_RESEARCH_STATE_V1": raise AssertionError("state schema mismatch")
    if build["schema"]!="COLLATZ_CURRENT_ARCHIVE_BUILD_V1": raise AssertionError("build schema mismatch")
    if member_record["schema"]!="COLLATZ_ARCHIVE_MEMBER_ROOT_V1": raise AssertionError("archive member-root schema mismatch")
    allowed={"STAGE_1_AUTHORIZED_NOT_EXECUTED","STAGE_1_RUNNING","RESULT_RETURNED_UNVERIFIED","AUDIT_PENDING","ACCEPTED","STAGE_0_READY_NOT_DISPATCHED","STAGE_0_REPAIR_READY_NOT_DISPATCHED","STAGE_0_RUNNING","PRE_RUN_SEAL_AWAITING_AUTHORIZATION","STAGE_1_INPUT_INTEGRITY_FAILURE_AUTHORIZATION_CONSUMED_CLOSED"}
    if state["active_task"]["stage"] not in allowed: raise AssertionError("unrecognized active stage")
    if not state["next_action"]["instruction"]: raise AssertionError("next action is empty")
    lock=state.get("active_integrator")
    if lock is not None:
        req={"holder","scope","base_commit","acquired_at","status"}; missing=req-set(lock)
        if missing: raise AssertionError(f"active_integrator missing keys: {sorted(missing)}")
        if lock["status"] not in {"HELD","RELEASED"}: raise AssertionError(f"active_integrator status invalid: {lock['status']}")
        if lock["status"]=="HELD" and not lock["holder"]: raise AssertionError("active_integrator is HELD with no holder")
        if not lock["scope"]: raise AssertionError("active_integrator scope is empty")
        verify_history_commit(lock["base_commit"],required=lock["status"]=="HELD",label="active_integrator.base_commit",warnings=warnings)
    minimum=state.get("continuity",{}).get("minimum_required_commit")
    if minimum: verify_history_commit(minimum,required=False,label="continuity.minimum_required_commit",warnings=warnings)
    branch=verify_branch_context(state["continuity"]["repository_branch"],warnings)
    for row in state["integrity"]["repository_files"]:
        if digest_file(REPO/row["path"])!=row["sha256"]: raise AssertionError(f"repository hash mismatch: {row['path']}")
    archive=REPO/build["archive"]
    if archive.name!=state["archive"]["current_archive"]: raise AssertionError("archive name mismatch")
    archive_sha=digest_file(archive)
    if archive_sha!=build["archive_sha256"]: raise AssertionError("current archive hash mismatch")
    if archive.stat().st_size!=build["zip_bytes"]: raise AssertionError("current archive size mismatch")
    if member_record["archive"]!=archive.name or member_record["archive_sha256"]!=archive_sha: raise AssertionError("archive member-root record does not bind to current archive")
    with zipfile.ZipFile(archive) as zf:
        if len(zf.infolist())!=build["member_count"]: raise AssertionError("archive member-count mismatch")
        bad=zf.testzip()
        if bad is not None: raise AssertionError(f"archive CRC failure: {bad}")
        names={x.filename for x in zf.infolist()}
        for row in state["integrity"]["archive_members"]:
            if row["path"] not in names: raise AssertionError(f"archive member missing: {row['path']}")
            if digest_bytes(zf.read(row["path"]))!=row["sha256"]: raise AssertionError(f"archive member hash mismatch: {row['path']}")
        full_count,full_root=archive_member_root(zf)
        if full_count!=member_record["member_count"] or full_count!=build["member_count"]: raise AssertionError("full archive member-root count mismatch")
        if full_root!=member_record["member_root_sha256"]: raise AssertionError("full archive member-root hash mismatch")
    journal_rows=verify_journal()
    print(f"branch={branch}"); print(f"head={git_value('rev-parse','HEAD')}"); print(f"active_task={state['active_task']['code']}"); print(f"active_stage={state['active_task']['stage']}"); print(f"journal_rows={journal_rows}"); print(f"archive_members={build['member_count']}"); print(f"archive_member_root={member_record['member_root_sha256']}"); print(f"archive_sha256={build['archive_sha256']}")
    for w in warnings: print(f"WARNING: {w}")
    print("HANDOFF VERIFICATION: PASS")
if __name__=="__main__":
    try: main()
    except Exception as exc:
        print(f"HANDOFF VERIFICATION: FAIL — {exc}",file=sys.stderr); raise
