#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone, timedelta
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import textwrap

REPO = Path.cwd()
REQUIRED_MAIN = "9119a39957705f53060c380acf3e8f4dd6609565"
RESULT_BRANCH = "cp20-e7r-literature-transfer-v1-stage1-audit-stop-20260904"
RESULT_HEAD = "93201a44924562eddb951d083370e42e0ec8bf00"
AUDIT_BRANCH = "cp20-e7r-literature-transfer-v1-zero-trust-audit-20260904"
AUDIT_HEAD = "594517c1f0a27c9335ee10aa287cb5054210be7d"
AUTH_SEAL = "403633178f22f703d83f8e7ffaddc9e416a0d733eaa203f7b7cf796d343b7c79"
STAGE1_PACKAGE = "978d8b90c58131dcf350699920a241fee7a7d7b4c2abeff5cb1ea45da96e120e"
STAGE1_MANIFEST = "f8afcf1778722bd8715a78792d9855c65c0849c8fc722f00096fd67bc6c9d4c4"
AUDIT_FULL = "9c99922b314523090444ea4f665015b4e161eb48c151b3c6a054331601306a45"
AUDIT_REPRO = "e2dfd4cae002751abf8b22ae3da8ca1e14050af2e9e391039c753cf0b46976f5"
AUDIT_REPRO_RESULTS = "22a6ed55fff981e07d8b07ac4fd6a914173cebdc51519962f7453f8b10df7276"
AUDIT_VERDICTS = "d19495edf4461c61cc07cca8e6777ce6932107547657ed54f178fdaf39419426"
NEXT_TASK = "CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1"

R = Path("research_manager/results/CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_AUDIT_STOP")
A = Path("bagimsiz-denetim/e7r-literature-transfer-v1-zero-trust-audit-20260904")
DECISION = Path("research_manager/decisions/CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_AUDITED_INTEGRATION_2026-09-04.md")
STATE = Path("CURRENT_RESEARCH_STATE.json")
HANDOFF = Path("START_HERE_CURRENT_HANDOFF.md")
JOURNAL = Path("research_manager/RESEARCH_JOURNAL.jsonl")

RESULT_FILES = [
    "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_AUDIT_STOP.md",
    "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_DRIVE_PERSISTENCE_RECORD.json",
    "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_INDEPENDENT_FINITE_PHASE.py",
    "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_MECHANICAL_RESULTS.json",
    "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_PACKAGE_RECORD.json",
    "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_PROVENANCE.json",
    "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_REPORT.md",
    "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_RESULT.json",
    "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_SHA256SUMS.txt",
]
AUDIT_FILES = [
    "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_ZERO_TRUST_AUDIT_2026-09-04.md",
    "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_ZERO_TRUST_AUDIT_SHA256SUMS_2026-09-04.txt",
]


def run(*args: str, capture: bool = False) -> str:
    p = subprocess.run(args, cwd=REPO, text=True, encoding="utf-8", capture_output=capture, check=False)
    if p.returncode:
        if capture:
            sys.stderr.write(p.stdout + p.stderr)
        raise RuntimeError(f"command failed ({p.returncode}): {' '.join(args)}")
    return p.stdout.strip() if capture else ""


def sha_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def upsert(rows: list[dict], path: str, digest: str) -> None:
    for row in rows:
        if row["path"] == path:
            row["sha256"] = digest
            return
    rows.append({"path": path, "sha256": digest})


def now_tr() -> str:
    return datetime.now(timezone(timedelta(hours=3))).isoformat(timespec="seconds")


def verify_refs() -> None:
    assert run("git", "rev-parse", "HEAD", capture=True) == REQUIRED_MAIN
    assert run("git", "rev-parse", f"origin/{RESULT_BRANCH}", capture=True) == RESULT_HEAD
    assert run("git", "rev-parse", f"origin/{AUDIT_BRANCH}", capture=True) == AUDIT_HEAD
    assert run("git", "merge-base", REQUIRED_MAIN, RESULT_HEAD, capture=True) == REQUIRED_MAIN
    assert run("git", "merge-base", REQUIRED_MAIN, AUDIT_HEAD, capture=True) == REQUIRED_MAIN


def acquire_lock() -> str:
    s = json.loads(STATE.read_text(encoding="utf-8"))
    old = s.get("active_integrator", {})
    assert old.get("status") == "RELEASED", old
    s["active_integrator"] = {
        "holder": "canonical-integrator-e7r-literature-stage1-audit-20260904",
        "scope": "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1 audited Stage-1 canonical integration only; no Stage-1 rerun, no new mathematics, no weighted/operator work, no E8, and no execution of the next research task.",
        "base_commit": REQUIRED_MAIN,
        "acquired_at": now_tr(),
        "status": "HELD",
    }
    STATE.write_text(json.dumps(s, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    run("git", "config", "user.name", "Canonical Integrator")
    run("git", "config", "user.email", "actions@users.noreply.github.com")
    run("git", "add", str(STATE))
    run("git", "commit", "-m", "Acquire integrator lock for audited Literature Transfer V1 integration")
    lock_sha = run("git", "rev-parse", "HEAD", capture=True)
    run("git", "push", "origin", "HEAD:main")
    remote = run("git", "ls-remote", "origin", "refs/heads/main", capture=True).split()[0]
    assert remote == lock_sha
    Path("LOCK_SHA.txt").write_text(lock_sha + "\n")
    return lock_sha


def copy_small_records() -> None:
    for name in RESULT_FILES:
        run("git", "checkout", f"origin/{RESULT_BRANCH}", "--", str(R / name))
    for name in AUDIT_FILES:
        run("git", "checkout", f"origin/{AUDIT_BRANCH}", "--", str(A / name))
    forbidden = [
        R / "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_COMPLETE_PACKAGE.zip",
        R / "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_PRE_RUN_SEAL.zip",
        R / "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_EXECUTION.py",
        R / "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_EXECUTION_STDOUT.txt",
    ]
    assert not any(p.exists() for p in forbidden)
    assert all(p.stat().st_size < 1_000_000 for p in [*(R / x for x in RESULT_FILES), *(A / x for x in AUDIT_FILES)])


def validate_records() -> None:
    pkg = json.loads((R / "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_PACKAGE_RECORD.json").read_text())
    assert pkg["package_sha256"] == STAGE1_PACKAGE
    assert pkg["manifest_sha256"] == STAGE1_MANIFEST
    assert pkg["stage1_execution_count"] == 1 and pkg["zip_crc"] == "PASS"
    assert pkg["downstream_math_after_stop"] is False
    mech = json.loads((R / "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_MECHANICAL_RESULTS.json").read_text())
    assert mech["authorized_seal_sha256"] == AUTH_SEAL
    assert mech["stage1_execution_count_this_run"] == 1
    assert mech["sealed_candidate_helper_used_as_evidence"] is False
    drive = json.loads((R / "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_DRIVE_PERSISTENCE_RECORD.json").read_text())
    assert drive["expected_package_sha256"] == STAGE1_PACKAGE == drive["readback_package_sha256"]
    assert drive["readback_byte_compare"] == "PASS" and drive["readback_verdict"] == "PASS"
    audit_report = A / AUDIT_FILES[0]
    assert sha_file(audit_report) == AUDIT_FULL
    rows = (A / AUDIT_FILES[1]).read_text().splitlines()
    assert {x.split()[0] for x in rows} == {AUDIT_FULL, AUDIT_REPRO, AUDIT_REPRO_RESULTS, AUDIT_VERDICTS}
    text = audit_report.read_text()
    for required in (
        "[AUDIT PASS — DIRECT TAO/SI THEOREM TRANSFER CLOSED]",
        "[EXECUTION INTEGRITY PASS WITH DOCUMENTATION GAP]",
        "[PACKAGE INTEGRITY PASS]",
        "M8: [PASS — NO DIRECT THEOREM MATCH]",
        "LT-CT: [PROVED — AUDITED]",
    ):
        assert required in text


def write_decision() -> None:
    DECISION.parent.mkdir(parents=True, exist_ok=True)
    DECISION.write_text(textwrap.dedent(r"""\
        # CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1 — Audited Stage-1 Canonical Integration

        ## Integration verdict

        **[LITERATURE TRANSFER V1 — AUDITED AND CANONICALLY INTEGRATED]**

        This is a canonical management/integration decision only. Stage 1 was not rerun. No new mathematics, weighted/operator work, E8 work, or next-task execution was performed.

        ## Authoritative provenance

        - Canonical authorization base: `9119a39957705f53060c380acf3e8f4dd6609565`
        - Stage-1 result branch HEAD: `93201a44924562eddb951d083370e42e0ec8bf00`
        - Authorized Stage-0 seal SHA-256: `403633178f22f703d83f8e7ffaddc9e416a0d733eaa203f7b7cf796d343b7c79`
        - Stage-1 complete-package SHA-256: `978d8b90c58131dcf350699920a241fee7a7d7b4c2abeff5cb1ea45da96e120e`
        - Stage-1 manifest SHA-256: `f8afcf1778722bd8715a78792d9855c65c0849c8fc722f00096fd67bc6c9d4c4`
        - Zero-trust audit HEAD: `594517c1f0a27c9335ee10aa287cb5054210be7d`
        - Audit verdict: `[AUDIT PASS — DIRECT TAO/SI THEOREM TRANSFER CLOSED]`
        - Execution integrity: `[EXECUTION INTEGRITY PASS WITH DOCUMENTATION GAP]`
        - Package integrity: `[PACKAGE INTEGRITY PASS]`

        Audit artifact SHA-256:
        - full audit: `9c99922b314523090444ea4f665015b4e161eb48c151b3c6a054331601306a45`
        - independent reproduction: `e2dfd4cae002751abf8b22ae3da8ca1e14050af2e9e391039c753cf0b46976f5`
        - reproduction results: `22a6ed55fff981e07d8b07ac4fd6a914173cebdc51519962f7453f8b10df7276`
        - verdict record: `d19495edf4461c61cc07cca8e6777ce6932107547657ed54f178fdaf39419426`

        ## Accepted audited scientific state

        - `LT-N1 [PROVED][AUDITED]`
        - `LT-N2 [PROVED][AUDITED]`
        - `LT-N3 [PROVED][AUDITED]`
        - `LT-N4 [PROVED][AUDITED]`
        - `LT-N5 [PROVED][AUDITED]`
        - `LT-N6 [NOT PROVED]`
        - `LT-N7 [NOT PROVED]`
        - `LT-CT [PROVED][AUDITED]`
        - `M1 PASS`
        - `M2 PASS`
        - `M3 PASS`
        - `M4 PASS`
        - `M5 PASS`
        - `M6 PASS`
        - `M7 PASS — CONSISTENCY CLASSIFICATION ONLY`
        - `M8 PASS — NO DIRECT THEOREM MATCH`

        `E6-N2` remains **[OPEN]**.

        ## Exact accepted normal form

        `T_r = floor((log_2 3) r)-8`

        `eta_r = 2^(T_r-4) mod 3^r`

        `G_r = E[e_{3^r}(eta_r F_r^aff) | sum_i A_i = T_r]`.

        No independent global mod-16 cocycle survives in this fixed-total observable; the dyadic factor is absorbed into the primitive 3-adic frequency.

        ## Closed route — exact scope only

        Closed: **Direct application/transfer of the frozen Tao v7 / Si 2026 analytic theorems to the exact project microcanonical fiber.**

        This closure MUST NOT be broadened. It does not close adaptations requiring a new theorem, exponential tilting/recentered measures, off-central microcanonical Fourier analysis, weighted/cotransition operators, saddlepoint/Edgeworth methods, or modified geometry.

        ## Documentation gap

        The proposed pre-execution `STAGE1_EXECUTION_INTEGRITY_AND_OUTPUT_CONTRACT_ADDENDUM` was not canonicalized before execution. The independent audit verdict is `[EXECUTION INTEGRITY PASS WITH DOCUMENTATION GAP]`. No rerun is required or authorized. Historical authorization records are left unchanged. For every future once-only run, the pre-run execution-integrity contract must be canonicalized before authorization/execution.

        ## Archive-budget policy

        The large authoritative Stage-1 package remains on Drive and is referenced by SHA-256. Canonical `main` stores only small result/audit reports, JSON records, hashes/manifests, Drive identifiers and small reproducibility source. No historical artifact is deleted for headroom, and no sealed PDFs/source archives/Stage-0 ZIPs are duplicated from result branches.

        ## Next scientific target — not executed here

        `CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1` — **Tilted / Recentered Microcanonical Fourier Cancellation**

        Stage: `STAGE_0_READY_NOT_DISPATCHED`

        Objective: determine whether the exact project microcanonical law can be recentered by an exponential/geometric tilt with mean `log_2(3)`, and whether a new joint Fourier local-limit theorem at `eta_r=2^(T_r-4) mod 3^r` can yield `|G_r|=O(1/r)`.

        This is a new theorem-development route. Tao's existing theorem is not claimed to apply after tilting. A future Stage 0 must freeze/falsify T1–T8 exactly as recorded in `CURRENT_RESEARCH_STATE.json`. This integration does not dispatch or execute that Stage 0.

        Nothing in this integration proves the Collatz conjecture.
        """), encoding="utf-8", newline="\n")


def update_state_and_journal(lock_sha: str) -> None:
    s = json.loads(STATE.read_text(encoding="utf-8"))
    lock = s["active_integrator"]
    assert lock["status"] == "HELD" and lock["base_commit"] == REQUIRED_MAIN
    lock["lock_acquisition_commit"] = lock_sha
    lock["status"] = "RELEASED"

    objective = "Determine whether the exact project microcanonical law can be recentered by an exponential/geometric tilt with mean log_2(3), and whether a new joint Fourier local-limit theorem at the primitive frequency eta_r = 2^(T_r-4) mod 3^r can yield |G_r| = O(1/r)."
    s["active_task"] = {
        "code": NEXT_TASK,
        "name": "Tilted / Recentered Microcanonical Fourier Cancellation",
        "stage": "STAGE_0_READY_NOT_DISPATCHED",
        "objective": objective,
        "target": {"C": 4, "d": -8, "primitive_frequency": "eta_r = 2^(T_r-4) mod 3^r"},
    }
    lt = s.setdefault("literature_transfer_v1", {})
    lt["stage1_result"] = {
        "status": "[AUDITED AND CANONICALLY INTEGRATED]",
        "result_branch": RESULT_BRANCH,
        "result_branch_head": RESULT_HEAD,
        "authorized_stage0_seal_sha256": AUTH_SEAL,
        "complete_package_sha256": STAGE1_PACKAGE,
        "manifest_sha256": STAGE1_MANIFEST,
        "package_location": "Drive only for large package; canonical main carries small records and hashes",
        "stage1_rerun_in_integration": False,
        "downstream_math_after_stop": False,
        "normal_form": {
            "T_r": "floor((log_2 3) r)-8",
            "eta_r": "2^(T_r-4) mod 3^r",
            "G_r": "E[e_{3^r}(eta_r F_r^aff) | sum_i A_i = T_r]",
            "global_mod16_cocycle": "none; dyadic factor absorbed into primitive 3-adic frequency",
        },
        "mappings": {"M1": "PASS", "M2": "PASS", "M3": "PASS", "M4": "PASS", "M5": "PASS", "M6": "PASS", "M7": "PASS — CONSISTENCY CLASSIFICATION ONLY", "M8": "PASS — NO DIRECT THEOREM MATCH"},
        "lt_ladder": {"LT-N1": "[PROVED][AUDITED]", "LT-N2": "[PROVED][AUDITED]", "LT-N3": "[PROVED][AUDITED]", "LT-N4": "[PROVED][AUDITED]", "LT-N5": "[PROVED][AUDITED]", "LT-N6": "[NOT PROVED]", "LT-N7": "[NOT PROVED]", "LT-CT": "[PROVED][AUDITED]"},
        "e6_n2": "[OPEN]",
    }
    lt["zero_trust_audit"] = {
        "audit_branch": AUDIT_BRANCH,
        "audit_branch_head": AUDIT_HEAD,
        "verdict": "[AUDIT PASS — DIRECT TAO/SI THEOREM TRANSFER CLOSED]",
        "execution_integrity": "[EXECUTION INTEGRITY PASS WITH DOCUMENTATION GAP]",
        "package_integrity": "[PACKAGE INTEGRITY PASS]",
        "artifact_sha256": {"full_audit": AUDIT_FULL, "independent_reproduction": AUDIT_REPRO, "reproduction_results": AUDIT_REPRO_RESULTS, "verdict_record": AUDIT_VERDICTS},
    }
    lt["closed_route"] = {
        "statement": "Direct application/transfer of the frozen Tao v7 / Si 2026 analytic theorems to the exact project microcanonical fiber.",
        "scope": "EXACT — DO NOT BROADEN",
        "not_closed": ["adaptations of Tao/Si mechanisms requiring a new theorem", "exponential tilting / recentered measures", "off-central microcanonical Fourier analysis", "weighted/cotransition operators", "saddlepoint/Edgeworth methods", "modified geometry"],
    }
    s["documentation_gap"] = {
        "task": "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1 Stage 1",
        "missing_preexecution_record": "STAGE1_EXECUTION_INTEGRITY_AND_OUTPUT_CONTRACT_ADDENDUM",
        "audit_verdict": "[EXECUTION INTEGRITY PASS WITH DOCUMENTATION GAP]",
        "rerun_required": False,
        "rerun_authorized": False,
        "historical_authorization_rewritten": False,
        "future_once_only_rule": "Pre-run execution-integrity contracts must be canonicalized before authorization/execution.",
    }
    drive = json.loads((R / RESULT_FILES[1]).read_text())
    s["archive"]["budget_policy"] = {
        "github_builder_hard_limit_bytes": 100000000,
        "large_stage1_package_materialized_on_main": False,
        "large_stage1_package_sha256": STAGE1_PACKAGE,
        "large_stage1_package_drive_folder_id": drive["drive_folder_id"],
        "large_stage1_package_drive_file_id": drive["drive_package_file_id"],
        "large_stage1_package_drive_readback": "PASS",
        "canonical_main_policy": "small reports/JSON/hashes/manifests/Drive identifiers/small reproducibility source only; no duplicated sealed PDFs/source archives/Stage-0 seal ZIPs; no historical deletion for headroom",
    }
    future = [
        "T1 exact conditional-law invariance under geometric tilting",
        "T2 choice p_* = 1/log_2(3) and centrality of T_r under that tilted law",
        "T3 exact Fourier-inversion representation of the microcanonical numerator",
        "T4 denominator local limit P_{p_*}(sum A_i=T_r) ~ c r^(-1/2)",
        "T5 required numerator target O(r^(-3/2))",
        "T6 whether Tao-style white-point/renewal estimates can be generalized uniformly in the additional Fourier variable dual to the total sum",
        "T7 saddlepoint / Edgeworth alternative",
        "T8 endpoint-weighted block-operator alternative if the direct tilted route fails",
    ]
    s["next_task_stage0_requirements"] = future
    s["next_action"] = {
        "authorized_stage": "STAGE_0_ONLY",
        "executed_in_this_transaction": False,
        "instruction": "Prepare/execute Stage 0 only for CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1 in a future transaction, first freezing and falsifying T1–T8. Do not infer that Tao existing theorem applies after tilting. This canonical integration does not dispatch or execute Stage 0.",
        "prompt": None,
        "requires_user_or_external_result": False,
    }
    s["returned_result"] = {"acceptance_status": "LITERATURE_TRANSFER_V1_AUDIT_PASS_CANONICALLY_INTEGRATED", "stage1_package_sha256": STAGE1_PACKAGE, "stage1_manifest_sha256": STAGE1_MANIFEST, "audit_head": AUDIT_HEAD, "audit_verdict": "[AUDIT PASS — DIRECT TAO/SI THEOREM TRANSFER CLOSED]", "e6_n2": "[OPEN]"}
    sc = s.setdefault("scientific_checkpoint", {})
    for x in ["LT-N1 [PROVED][AUDITED]", "LT-N2 [PROVED][AUDITED]", "LT-N3 [PROVED][AUDITED]", "LT-N4 [PROVED][AUDITED]", "LT-N5 [PROVED][AUDITED]", "LT-CT [PROVED][AUDITED]"]:
        if x not in sc.setdefault("accepted", []): sc["accepted"].append(x)
    if "E6-N2 [OPEN]" not in sc.setdefault("open", []): sc["open"].append("E6-N2 [OPEN]")
    exact = "Direct application/transfer of the frozen Tao v7 / Si 2026 analytic theorems to the exact project microcanonical fiber [CLOSED]"
    if exact not in sc.setdefault("closed", []): sc["closed"].append(exact)
    s["continuity"]["minimum_required_commit"] = lock_sha
    s["continuity"]["future_once_only_contract_rule"] = "Pre-run execution-integrity contracts must be canonicalized before authorization/execution."
    docs = s.setdefault("documents", {})
    docs["accepted_checkpoint_decision"] = str(DECISION)
    docs["active_authorization_decision"] = None
    docs["active_authorization_prompt"] = None
    docs["active_research_prompt"] = None
    docs["literature_transfer_stage1_result"] = str(R / "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_STAGE1_REPORT.md")
    docs["literature_transfer_stage1_audit"] = str(A / AUDIT_FILES[0])
    prohibited = s.setdefault("prohibited_inferences", [])
    for x in [
        "Do not broaden the audited Literature Transfer closure beyond direct application/transfer of the frozen Tao v7 / Si 2026 analytic theorems to the exact project microcanonical fiber.",
        "Do not claim that Tao existing theorem applies after exponential/geometric tilting.",
        "Do not rerun Literature Transfer V1 Stage 1 to repair the documentation gap.",
        "Do not execute CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1 Stage 0 as part of this integration.",
    ]:
        if x not in prohibited: prohibited.append(x)

    lines = JOURNAL.read_bytes().splitlines()
    assert lines
    last = json.loads(lines[-1].decode("utf-8"))
    row = {
        "active_stage": "STAGE_0_READY_NOT_DISPATCHED",
        "active_task": NEXT_TASK,
        "event": "LITERATURE_TRANSFER_V1_AUDITED_STAGE1_CANONICALLY_INTEGRATED",
        "evidence": {"required_main": REQUIRED_MAIN, "integrator_lock_acquisition_commit": lock_sha, "result_branch_head": RESULT_HEAD, "authorized_stage0_seal_sha256": AUTH_SEAL, "stage1_package_sha256": STAGE1_PACKAGE, "stage1_manifest_sha256": STAGE1_MANIFEST, "audit_branch_head": AUDIT_HEAD, "audit_verdict": "[AUDIT PASS — DIRECT TAO/SI THEOREM TRANSFER CLOSED]", "execution_integrity": "[EXECUTION INTEGRITY PASS WITH DOCUMENTATION GAP]", "package_integrity": "[PACKAGE INTEGRITY PASS]", "lt_ct": "[PROVED][AUDITED]", "e6_n2": "[OPEN]", "stage1_rerun": False, "new_mathematics": False, "large_stage1_package_on_main": False, "large_stage1_package_drive_readback": "PASS"},
        "next_action": "Future Stage 0 only for CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1; freeze/falsify T1–T8 first. Not dispatched by this integration.",
        "previous_entry_sha256": sha_bytes(lines[-1]),
        "schema": "COLLATZ_RESEARCH_JOURNAL_V1",
        "sequence": last["sequence"] + 1,
        "timestamp": now_tr(),
    }
    raw = json.dumps(row, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")
    with JOURNAL.open("ab") as f:
        f.write(raw + b"\n")

    selected = [DECISION, JOURNAL, *(R / x for x in RESULT_FILES), *(A / x for x in AUDIT_FILES)]
    repo_rows = s["integrity"]["repository_files"]
    arc_rows = s["integrity"]["archive_members"]
    for p in selected:
        rel = p.as_posix()
        digest = sha_file(p)
        upsert(repo_rows, rel, digest)
        if rel.startswith("research_manager/"):
            arc = "Collatz Problemi — Araştırma Arşivi/RESEARCH_MANAGEMENT/" + rel[len("research_manager/"):]
        elif rel.startswith("bagimsiz-denetim/"):
            arc = "Collatz Problemi — Araştırma Arşivi/INDEPENDENT_AUDITS/CANONICAL_ZERO_TRUST/" + rel[len("bagimsiz-denetim/"):]
        else:
            continue
        upsert(arc_rows, arc, digest)
    s["updated_at"] = now_tr()
    STATE.write_text(json.dumps(s, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def write_handoff() -> None:
    HANDOFF.write_text(textwrap.dedent(r"""\
        # START HERE — Current Collatz Research Handoff

        Machine-readable authority: `CURRENT_RESEARCH_STATE.json`. Recover on branch `main`, run `python tools/verify_handoff.py`, and require `HANDOFF VERIFICATION: PASS` before any research action.

        ## Current audited milestone

        `CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1` is **[AUDITED AND CANONICALLY INTEGRATED]**.

        Accepted: LT-N1–LT-N5 `[PROVED][AUDITED]`; LT-N6/LT-N7 `[NOT PROVED]`; LT-CT `[PROVED][AUDITED]`; M1–M6 `PASS`; M7 `PASS — CONSISTENCY CLASSIFICATION ONLY`; M8 `PASS — NO DIRECT THEOREM MATCH`.

        `E6-N2` remains **[OPEN]**.

        Zero-trust verdict: **[AUDIT PASS — DIRECT TAO/SI THEOREM TRANSFER CLOSED]**. Execution integrity: **[EXECUTION INTEGRITY PASS WITH DOCUMENTATION GAP]**. Package integrity: **[PACKAGE INTEGRITY PASS]**.

        ## Exact accepted normal form

        `T_r = floor((log_2 3) r)-8`

        `eta_r = 2^(T_r-4) mod 3^r`

        `G_r = E[e_{3^r}(eta_r F_r^aff) | sum_i A_i = T_r]`.

        No independent global mod-16 cocycle survives in this fixed-total observable; the dyadic factor is absorbed into the primitive 3-adic frequency.

        ## Exact closed route

        Only this route is closed: **Direct application/transfer of the frozen Tao v7 / Si 2026 analytic theorems to the exact project microcanonical fiber.**

        Do NOT broaden this closure. New theorem adaptations, exponential tilting/recentering, off-central Fourier analysis, weighted/cotransition operators, saddlepoint/Edgeworth methods and modified geometry are not closed by LT-CT.

        ## Documentation gap

        `STAGE1_EXECUTION_INTEGRITY_AND_OUTPUT_CONTRACT_ADDENDUM` was not canonicalized before the preserved Stage-1 run. No rerun is required or authorized. Historical authorization records were not rewritten. Future once-only runs must canonicalize pre-run execution-integrity contracts before authorization/execution.

        ## Archive safety

        The authoritative large Stage-1 package remains on Drive by SHA-256. Do not duplicate sealed PDFs, source archives, Stage-0 seal ZIPs or the large Stage-1 package onto canonical `main`; do not delete historical artifacts merely to create headroom.

        ## Exact next scientific task

        Code: `CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1`

        Name: **Tilted / Recentered Microcanonical Fourier Cancellation**

        Stage: `STAGE_0_READY_NOT_DISPATCHED`

        Objective: determine whether the exact project microcanonical law can be recentered by an exponential/geometric tilt with mean `log_2(3)`, and whether a new joint Fourier local-limit theorem at primitive frequency `eta_r=2^(T_r-4) mod 3^r` can yield `|G_r|=O(1/r)`.

        This is new theorem development. Do not claim Tao's existing theorem applies after tilting.

        A future Stage 0 must first freeze/falsify T1 exact tilt invariance; T2 `p_*=1/log_2(3)` centrality; T3 numerator Fourier inversion; T4 denominator LLT `~c r^(-1/2)`; T5 numerator `O(r^(-3/2))`; T6 uniform white-point/renewal generalization in the extra Fourier variable; T7 saddlepoint/Edgeworth alternative; and T8 endpoint-weighted block-operator alternative.

        Do not dispatch or execute that Stage 0 merely by recovering this handoff.

        Nothing in the current research state proves the Collatz conjecture.
        """), encoding="utf-8", newline="\n")


def build_and_finalize(lock_sha: str) -> tuple[str, dict]:
    p = subprocess.run([sys.executable, "tools/build_current_archive.py"], cwd=REPO, text=True, encoding="utf-8", capture_output=True, check=False)
    Path("ARCHIVE_BUILD_STDOUT.txt").write_text(p.stdout + p.stderr, encoding="utf-8")
    if p.returncode:
        raise RuntimeError("archive build failed")
    build = json.loads(Path("CURRENT_ARCHIVE_BUILD.json").read_text())
    assert build["zip_bytes"] < 100_000_000
    budget = {"archive_sha256": build["archive_sha256"], "archive_bytes": build["zip_bytes"], "hard_limit_bytes": 100_000_000, "headroom_bytes": 100_000_000 - build["zip_bytes"], "member_count": build["member_count"]}
    Path("ARCHIVE_BUDGET.json").write_text(json.dumps(budget, indent=2, sort_keys=True) + "\n")

    run("git", "add", "CURRENT_RESEARCH_STATE.json", "START_HERE_CURRENT_HANDOFF.md", "CURRENT_ARCHIVE_BUILD.json", "Collatz_Research_Archive_CURRENT.zip", "research_manager", "bagimsiz-denetim")
    run("git", "commit", "-m", "Integrate audited Literature Transfer V1 Stage1 result")
    final_sha = run("git", "rev-parse", "HEAD", capture=True)
    v = subprocess.run([sys.executable, "tools/verify_handoff.py"], cwd=REPO, text=True, encoding="utf-8", capture_output=True, check=False)
    Path("HANDOFF_VERIFICATION.txt").write_text(v.stdout + v.stderr, encoding="utf-8")
    if v.returncode or "HANDOFF VERIFICATION: PASS" not in v.stdout:
        raise RuntimeError("HANDOFF verification failed")
    run("git", "fetch", "origin", "main")
    assert run("git", "rev-parse", "origin/main", capture=True) == lock_sha
    run("git", "push", "origin", "HEAD:main")
    assert run("git", "ls-remote", "origin", "refs/heads/main", capture=True).split()[0] == final_sha
    manifest = {
        "schema": "CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1_AUDITED_CANONICAL_PERSISTENCE_V1",
        "main_commit_sha": final_sha,
        "archive_sha256": build["archive_sha256"],
        "archive_bytes": build["zip_bytes"],
        "archive_headroom_bytes": 100_000_000 - build["zip_bytes"],
        "archive_members": build["member_count"],
        "handoff_verification": "PASS",
        "integration_verdict": "[LITERATURE TRANSFER V1 — AUDITED AND CANONICALLY INTEGRATED]",
        "next_task": NEXT_TASK,
        "next_stage": "STAGE_0_READY_NOT_DISPATCHED",
        "stage1_rerun": False,
        "new_mathematics": False,
        "weighted_operator_work": False,
        "e8_work": False,
        "next_task_executed": False,
    }
    Path("PERSISTENCE_MANIFEST.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    Path("FINAL_SHA.txt").write_text(final_sha + "\n")
    return final_sha, build


def main() -> None:
    verify_refs()
    lock_sha = acquire_lock()
    copy_small_records()
    validate_records()
    write_decision()
    update_state_and_journal(lock_sha)
    write_handoff()
    final_sha, build = build_and_finalize(lock_sha)
    print(json.dumps({"final_sha": final_sha, "archive_sha256": build["archive_sha256"], "archive_bytes": build["zip_bytes"], "headroom": 100_000_000 - build["zip_bytes"]}, sort_keys=True))


if __name__ == "__main__":
    main()
