#!/usr/bin/env python3
import argparse, hashlib, json, pathlib, zipfile, datetime, os, sys

TASK="CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1"
def sha256(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--seal", required=True)
    ap.add_argument("--authorized-seal-sha256", required=True)
    ap.add_argument("--output", required=True)
    args=ap.parse_args()

    seal=pathlib.Path(args.seal)
    if sha256(seal) != args.authorized_seal_sha256:
        raise SystemExit("[B4 STAGE1 INPUT INTEGRITY FAILURE] seal hash mismatch")
    with zipfile.ZipFile(seal) as z:
        if z.testzip() is not None:
            raise SystemExit("[B4 STAGE1 INPUT INTEGRITY FAILURE] ZIP CRC")
        names=z.namelist()
        if len(names)!=len(set(names)) or names!=sorted(names):
            raise SystemExit("[B4 STAGE1 INPUT INTEGRITY FAILURE] ZIP membership/order")
        manifest_name=f"{TASK}_PRE_RUN_SHA256SUMS.txt"
        manifest=z.read(manifest_name).decode("utf-8")
        for line in manifest.splitlines():
            h,n=line.split("  ",1)
            if hashlib.sha256(z.read(n)).hexdigest()!=h:
                raise SystemExit("[B4 STAGE1 INPUT INTEGRITY FAILURE] member hash")

    output=pathlib.Path(args.output)
    witness=pathlib.Path(f"{TASK}_STAGE1_RUN_WITNESS.json")
    ledger=pathlib.Path(f"{TASK}_STAGE1_EXECUTION_LEDGER.jsonl")
    declared=[output,witness,ledger]
    if any(p.exists() for p in declared):
        raise SystemExit("[B4 STAGE1 INPUT INTEGRITY FAILURE] Stage1 output already exists")

    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    witness.write_text(json.dumps({
        "task":TASK,
        "utc_timestamp":now,
        "authorized_seal_sha256":args.authorized_seal_sha256,
        "config_sha256":sha256(args.config),
        "pid":os.getpid(),
        "output_absence_precheck":"PASS",
        "execution_count_claim":1
    }, sort_keys=True, indent=2)+"\n", encoding="utf-8")
    ledger.write_text(json.dumps({
        "utc_timestamp":now,
        "event":"STAGE1_ENTRYPOINT_STARTED",
        "T1_T8_status":"NOT_EXECUTED_PENDING_AUTHORIZED_PROOF_SESSION"
    }, sort_keys=True)+"\n", encoding="utf-8")
    output.write_text(json.dumps({
        "task":TASK,
        "integrity_preflight":"PASS",
        "scientific_adjudication":"MUST_CONTINUE_IN_AUTHORIZED_PROOF_SESSION_IN_T1_TO_T8_ORDER",
        "stage1_complete":False
    }, sort_keys=True, indent=2)+"\n", encoding="utf-8")
    print("B4 STAGE1 INTEGRITY PREFLIGHT: PASS")
    print("T1–T8 mathematical adjudication is not performed by this launcher.")

if __name__=="__main__":
    main()
