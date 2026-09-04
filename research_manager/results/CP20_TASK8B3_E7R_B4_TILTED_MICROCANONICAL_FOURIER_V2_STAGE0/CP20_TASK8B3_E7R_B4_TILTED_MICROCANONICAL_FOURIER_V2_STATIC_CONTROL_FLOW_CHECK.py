#!/usr/bin/env python3
import ast, json, pathlib
HERE=pathlib.Path(__file__).resolve().parent
TASK='CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2'
src=(HERE/f'{TASK}_STAGE1.py').read_text(encoding='utf-8')
tree=ast.parse(src)
imports=set()
for n in ast.walk(tree):
    if isinstance(n,ast.Import): imports.update(x.name.split('.')[0] for x in n.names)
    if isinstance(n,ast.ImportFrom) and n.module: imports.add(n.module.split('.')[0])
forbidden=sorted(imports & {'numpy','scipy','mpmath','sympy'})
main_node=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main')
segment=ast.get_source_segment(src,main_node)
tokens=['verify_seal(','output_absence(','verify_authorization_chain(','write_witness(','validate_witness(','write_gate(','append_pre_t1_gate_ledger(']
pos={t:segment.find(t) for t in tokens}
ordered=all(pos[t]>=0 for t in tokens) and [pos[t] for t in tokens]==sorted(pos[t] for t in tokens)
checks={
 'runtime_canonical_stage0_base_arg':'--canonical-stage0-base-sha' in src,
 'runtime_authorization_commit_arg':'--authorization-commit-sha' in src,
 'runtime_authorized_seal_arg':'--authorized-seal-sha256' in src,
 'runtime_contract_sha_arg':'--contract-sha256' in src,
 'old_self_referential_arg_removed':'--authorized-execution-base-sha' not in src,
 'authorization_json_not_required_to_name_own_commit':"auth.get('authorization_commit_sha')" not in src and 'auth.get(\"authorization_commit_sha\")' not in src,
 'stage0_to_authorization_ancestry_check':'canonical_stage0_base_sha is not ancestor of authorization_commit_sha' in src,
 'authorization_to_head_ancestry_check':'authorization_commit_sha is not ancestor of execution HEAD' in src,
 'authorization_artifact_read_at_auth_commit':"git('show',f'{authorization_commit}:{AUTH_PATH}')" in src,
 'phase_a_artifact_blob_and_sha256_checks':'Phase-A Stage0 Git blob mismatch' in src and 'Phase-A Stage0 SHA256 mismatch' in src,
 'complete_witness_before_gate':ordered,
 'gate_checked_before_ledger':'PRE_T1_GATE is not PASS' in src,
 'no_T1_START_emission':'"T1 START"' not in src and "'T1 START'" not in src,
 'blocked_seal_firewall':all(x in src for x in ['ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c','2e6d9e1d833fc8dabf02c0e970ccfb06fc86e4cbc9e85cd2e0e61ae3611879ea','66ac975940abb29a1248079ea6e03643ded966da296cf33deb7c7a0f5fa60eac']),
 'integrity_failure_literal':'[B4 V2 STAGE1 INPUT INTEGRITY FAILURE]' in src,
 'no_math_packages':not forbidden,
 'validator_separate_import':'WITNESS_VALIDATOR.py' in src,
}
overall=all(checks.values())
out={'schema':f'{TASK}_STATIC_CONTROL_FLOW_RESULTS_TWO_COMMIT_V3','overall':'PASS' if overall else 'FAIL','checks':checks,'forbidden_math_imports':forbidden,'call_positions':pos,'T1_T8_executed':False,'real_stage1_entrypoint_invoked':False}
(HERE/f'{TASK}_STATIC_CONTROL_FLOW_RESULTS.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print('STATIC CONTROL FLOW PASS' if overall else 'STATIC CONTROL FLOW FAIL')
raise SystemExit(0 if overall else 1)
