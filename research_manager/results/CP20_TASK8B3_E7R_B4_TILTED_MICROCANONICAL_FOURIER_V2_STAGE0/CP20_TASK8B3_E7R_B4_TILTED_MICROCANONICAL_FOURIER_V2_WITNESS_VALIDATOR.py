#!/usr/bin/env python3
import argparse, json, re, sys
TASK='CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2'
VERSION="V2"
STAGE0='8d274095b0e1acbe1fad0a73ef6a5293364902fc'
OLD='ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c'
SHA40=re.compile(r"^[0-9a-f]{40}$")
SHA64=re.compile(r"^[0-9a-f]{64}$")
REQUIRED=['task', 'task_version', 'stage0_source_base_sha', 'canonical_base_sha', 'authorized_execution_base_sha', 'authorized_seal_sha256', 'contract_sha256', 'config_sha256', 'execution_count_claim', 'output_absence_precheck', 'utc_timestamp', 'pid_or_session_identifier', 'exact_entrypoint', 'preflight_status']

def validate(w, expected_authorized_execution_base_sha, expected_authorized_seal_sha256,
             expected_contract_sha256, expected_config_sha256):
    errors=[]
    if not isinstance(w,dict):
        return ["witness_not_object"]
    for k in REQUIRED:
        if k not in w: errors.append(f"missing:{k}")
        elif w[k] is None or (isinstance(w[k],str) and not w[k].strip()):
            errors.append(f"empty:{k}")
    if errors: return errors
    if w["task"]!=TASK: errors.append("task")
    if w["task_version"]!=VERSION: errors.append("task_version")
    if w["stage0_source_base_sha"]!=STAGE0: errors.append("stage0_source_base_sha")
    for k in ("canonical_base_sha","authorized_execution_base_sha"):
        if not isinstance(w[k],str) or not SHA40.fullmatch(w[k]): errors.append(f"format:{k}")
    for k in ("authorized_seal_sha256","contract_sha256","config_sha256"):
        if not isinstance(w[k],str) or not SHA64.fullmatch(w[k]): errors.append(f"format:{k}")
    if w["canonical_base_sha"]!=w["authorized_execution_base_sha"]: errors.append("canonical_vs_authorized_base")
    if w["authorized_execution_base_sha"]!=expected_authorized_execution_base_sha: errors.append("authorized_execution_base_sha")
    if w["canonical_base_sha"]!=expected_authorized_execution_base_sha: errors.append("canonical_base_sha")
    if w["authorized_seal_sha256"]!=expected_authorized_seal_sha256: errors.append("authorized_seal_sha256")
    if w["authorized_seal_sha256"]==OLD: errors.append("old_v1_seal_blacklisted")
    if w["contract_sha256"]!=expected_contract_sha256: errors.append("contract_sha256")
    if w["config_sha256"]!=expected_config_sha256: errors.append("config_sha256")
    if w["execution_count_claim"]!=1: errors.append("execution_count_claim")
    if w["output_absence_precheck"]!="PASS": errors.append("output_absence_precheck")
    if w["preflight_status"]!="PASS": errors.append("preflight_status")
    return errors

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--witness",required=True)
    ap.add_argument("--authorized-execution-base-sha",required=True)
    ap.add_argument("--authorized-seal-sha256",required=True)
    ap.add_argument("--contract-sha256",required=True)
    ap.add_argument("--config-sha256",required=True)
    a=ap.parse_args()
    try: w=json.load(open(a.witness,encoding="utf-8"))
    except Exception as e:
        print("WITNESS VALIDATION: FAIL", type(e).__name__)
        return 2
    errors=validate(w,a.authorized_execution_base_sha,a.authorized_seal_sha256,
                    a.contract_sha256,a.config_sha256)
    if errors:
        print("WITNESS VALIDATION: FAIL")
        for e in errors: print(e)
        return 1
    print("WITNESS VALIDATION: PASS")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
