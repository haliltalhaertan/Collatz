#!/usr/bin/env python3
import copy, importlib.util, json, pathlib, sys
HERE=pathlib.Path(__file__).resolve().parent
TASK='CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2'
VAL=HERE/'CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_WITNESS_VALIDATOR.py'
spec=importlib.util.spec_from_file_location("v2validator",VAL)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
base_sha="1"*40; seal="2"*64; contract="3"*64; config="4"*64
good={
 "task":TASK,"task_version":"V2","stage0_source_base_sha":'8d274095b0e1acbe1fad0a73ef6a5293364902fc',
 "canonical_base_sha":base_sha,"authorized_execution_base_sha":base_sha,
 "authorized_seal_sha256":seal,"contract_sha256":contract,"config_sha256":config,
 "execution_count_claim":1,"output_absence_precheck":"PASS",
 "utc_timestamp":"2026-09-04T00:00:00+00:00","pid_or_session_identifier":"synthetic:selftest",
 "exact_entrypoint":"synthetic witness only; real Stage1 launcher NOT invoked","preflight_status":"PASS"
}
expected={"S1":"FAIL","S2":"FAIL","S3":"FAIL","S4":"FAIL","S5":"FAIL","S6":"FAIL",
"S7":"FAIL","S8":"FAIL","S9":"FAIL","S10":"FAIL","S11":"FAIL","S12":"PASS"}
cases=[]
def add(name, mut):
    x=copy.deepcopy(good); mut(x); cases.append((name,x))
add("S1",lambda x:x.pop("canonical_base_sha"))
add("S2",lambda x:x.__setitem__("canonical_base_sha",""))
add("S3",lambda x:x.__setitem__("canonical_base_sha","xyz"))
add("S4",lambda x:x.__setitem__("canonical_base_sha","5"*40))
add("S5",lambda x:x.pop("authorized_execution_base_sha"))
add("S6",lambda x:x.__setitem__("authorized_execution_base_sha","6"*40))
add("S7",lambda x:x.__setitem__("authorized_seal_sha256","7"*64))
add("S8",lambda x:x.__setitem__("contract_sha256","8"*64))
add("S9",lambda x:x.__setitem__("config_sha256","9"*64))
add("S10",lambda x:x.__setitem__("execution_count_claim",2))
add("S11",lambda x:x.__setitem__("output_absence_precheck","FAIL"))
cases.append(("S12",copy.deepcopy(good)))
results={}
for name,x in cases:
    errs=m.validate(x,base_sha,seal,contract,config)
    outcome="PASS" if not errs else "FAIL"
    results[name]={"expected":expected[name],"observed":outcome,"errors":errs}
overall=all(v["expected"]==v["observed"] for v in results.values())
out={"schema":f"{TASK}_WITNESS_SELFTEST_RESULTS_V2","overall":"PASS" if overall else "FAIL",
     "real_stage1_entrypoint_invoked":False,"mathematics_executed":False,"cases":results}
(HERE/f"{TASK}_WITNESS_SELFTEST_RESULTS.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
if overall:
    print("SELFTEST PASS")
    raise SystemExit(0)
print("SELFTEST FAIL")
raise SystemExit(1)
