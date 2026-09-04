#!/usr/bin/env python3
import ast, json, pathlib, re, sys
HERE=pathlib.Path(__file__).resolve().parent
TASK='CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2'
src=(HERE/f"{TASK}_STAGE1.py").read_text(encoding="utf-8")
tree=ast.parse(src)
imports=set()
for n in ast.walk(tree):
    if isinstance(n,ast.Import):
        imports.update(x.name.split(".")[0] for x in n.names)
    if isinstance(n,ast.ImportFrom) and n.module:
        imports.add(n.module.split(".")[0])
forbidden=sorted(imports & {"numpy","scipy","mpmath","sympy"})
main_node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=="main")
segment=ast.get_source_segment(src,main_node)
tokens=["verify_seal(","output_absence(","verify_future_base(","write_witness(","validate_witness(","write_gate(","append_pre_t1_gate_ledger("]
positions={t:segment.find(t) for t in tokens}
ordered=all(positions[t]>=0 for t in tokens) and [positions[t] for t in tokens]==sorted(positions[t] for t in tokens)
checks={
 "runtime_authorized_execution_base_arg":"--authorized-execution-base-sha" in src,
 "runtime_authorized_seal_arg":"--authorized-seal-sha256" in src,
 "runtime_contract_sha_arg":"--contract-sha256" in src,
 "complete_witness_before_gate":ordered,
 "gate_checked_before_ledger":"if not GATE.exists()" in src and "PRE_T1_GATE is not PASS" in src,
 "no_T1_START_emission":'"T1 START"' not in src and "'T1 START'" not in src,
 "old_v1_seal_blacklist":'ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c' in src,
 "integrity_failure_literal":"[B4 V2 STAGE1 INPUT INTEGRITY FAILURE]" in src,
 "no_math_packages":not forbidden,
 "validator_separate_import":"WITNESS_VALIDATOR.py" in src,
 "future_git_base_checks":all(x in src for x in ["cat-file","merge-base","git(\"show\"","rev-parse"])
}
overall=all(checks.values())
out={"schema":f"{TASK}_STATIC_CONTROL_FLOW_RESULTS_V2","overall":"PASS" if overall else "FAIL",
     "checks":checks,"forbidden_math_imports":forbidden,"call_positions":positions,
     "T1_T8_executed":False}
(HERE/f"{TASK}_STATIC_CONTROL_FLOW_RESULTS.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print("STATIC CONTROL FLOW PASS" if overall else "STATIC CONTROL FLOW FAIL")
raise SystemExit(0 if overall else 1)
