#!/usr/bin/env python3
import argparse, json, re
TASK='CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2'
VERSION='V2'
STAGE0='8d274095b0e1acbe1fad0a73ef6a5293364902fc'
BLOCKED={
 'ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c',
 '2e6d9e1d833fc8dabf02c0e970ccfb06fc86e4cbc9e85cd2e0e61ae3611879ea',
 '66ac975940abb29a1248079ea6e03643ded966da296cf33deb7c7a0f5fa60eac',
}
SHA40=re.compile(r"^[0-9a-f]{40}$")
SHA64=re.compile(r"^[0-9a-f]{64}$")
REQUIRED=['task','task_version','stage0_source_base_sha','canonical_stage0_base_sha','authorization_commit_sha','canonical_base_sha','authorized_seal_sha256','contract_sha256','config_sha256','execution_count_claim','output_absence_precheck','utc_timestamp','pid_or_session_identifier','exact_entrypoint','preflight_status']

def validate(w, expected_canonical_stage0_base_sha, expected_authorization_commit_sha,
             expected_authorized_seal_sha256, expected_contract_sha256, expected_config_sha256):
    errors=[]
    if not isinstance(w,dict): return ['witness_not_object']
    for k in REQUIRED:
        if k not in w: errors.append(f'missing:{k}')
        elif w[k] is None or (isinstance(w[k],str) and not w[k].strip()): errors.append(f'empty:{k}')
    if errors: return errors
    if w['task']!=TASK: errors.append('task')
    if w['task_version']!=VERSION: errors.append('task_version')
    if w['stage0_source_base_sha']!=STAGE0: errors.append('stage0_source_base_sha')
    for k in ('canonical_stage0_base_sha','authorization_commit_sha','canonical_base_sha'):
        if not isinstance(w[k],str) or not SHA40.fullmatch(w[k]): errors.append(f'format:{k}')
    for k in ('authorized_seal_sha256','contract_sha256','config_sha256'):
        if not isinstance(w[k],str) or not SHA64.fullmatch(w[k]): errors.append(f'format:{k}')
    if w['canonical_base_sha']!=w['authorization_commit_sha']: errors.append('canonical_base_vs_authorization_commit')
    if w['canonical_stage0_base_sha']==w['authorization_commit_sha']: errors.append('stage0_and_authorization_commits_not_distinct')
    if w['canonical_stage0_base_sha']!=expected_canonical_stage0_base_sha: errors.append('canonical_stage0_base_sha')
    if w['authorization_commit_sha']!=expected_authorization_commit_sha: errors.append('authorization_commit_sha')
    if w['canonical_base_sha']!=expected_authorization_commit_sha: errors.append('canonical_base_sha')
    if w['authorized_seal_sha256']!=expected_authorized_seal_sha256: errors.append('authorized_seal_sha256')
    if w['authorized_seal_sha256'] in BLOCKED: errors.append('blocked_seal')
    if w['contract_sha256']!=expected_contract_sha256: errors.append('contract_sha256')
    if w['config_sha256']!=expected_config_sha256: errors.append('config_sha256')
    if w['execution_count_claim']!=1: errors.append('execution_count_claim')
    if w['output_absence_precheck']!='PASS': errors.append('output_absence_precheck')
    if w['preflight_status']!='PASS': errors.append('preflight_status')
    return errors

def validate_authorization_model(model, expected_stage0, expected_auth_commit, expected_head, expected_seal, expected_contract):
    errors=[]
    required=['canonical_stage0_base_sha','authorization_commit_sha','execution_head_sha','stage0_is_ancestor_authorization','authorization_is_ancestor_execution_head','authorization_artifact_present','authorization_json','state_stage']
    if not isinstance(model,dict): return ['authorization_model_not_object']
    for k in required:
        if k not in model: errors.append(f'missing:{k}')
    if errors: return errors
    for k in ('canonical_stage0_base_sha','authorization_commit_sha','execution_head_sha'):
        if not isinstance(model[k],str) or not SHA40.fullmatch(model[k]): errors.append(f'format:{k}')
    if model['canonical_stage0_base_sha']!=expected_stage0: errors.append('canonical_stage0_base_sha')
    if model['authorization_commit_sha']!=expected_auth_commit: errors.append('authorization_commit_sha')
    if model['execution_head_sha']!=expected_head: errors.append('execution_head_sha')
    if model['canonical_stage0_base_sha']==model['authorization_commit_sha']: errors.append('stage0_and_authorization_commits_not_distinct')
    if model['stage0_is_ancestor_authorization'] is not True: errors.append('stage0_not_ancestor_of_authorization')
    if model['authorization_is_ancestor_execution_head'] is not True: errors.append('authorization_not_ancestor_of_execution_head')
    if model['authorization_artifact_present'] is not True: errors.append('authorization_artifact_missing')
    auth=model['authorization_json']
    if not isinstance(auth,dict):
        errors.append('authorization_json_not_object')
    else:
        if auth.get('authorized_v2_seal_sha256')!=expected_seal: errors.append('authorization_seal_mismatch')
        if auth.get('v2_contract_sha256')!=expected_contract: errors.append('authorization_contract_mismatch')
        if auth.get('canonical_stage0_base_sha')!=expected_stage0: errors.append('authorization_stage0_base_mismatch')
        if auth.get('stage')!='STAGE_1_AUTHORIZED_NOT_EXECUTED': errors.append('authorization_stage_mismatch')
    if model['state_stage']!='STAGE_1_AUTHORIZED_NOT_EXECUTED': errors.append('state_stage_mismatch')
    return errors

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--witness',required=True)
    ap.add_argument('--canonical-stage0-base-sha',required=True)
    ap.add_argument('--authorization-commit-sha',required=True)
    ap.add_argument('--authorized-seal-sha256',required=True)
    ap.add_argument('--contract-sha256',required=True)
    ap.add_argument('--config-sha256',required=True)
    a=ap.parse_args()
    try: w=json.load(open(a.witness,encoding='utf-8'))
    except Exception as e:
        print('WITNESS VALIDATION: FAIL',type(e).__name__); return 2
    errors=validate(w,a.canonical_stage0_base_sha,a.authorization_commit_sha,a.authorized_seal_sha256,a.contract_sha256,a.config_sha256)
    if errors:
        print('WITNESS VALIDATION: FAIL')
        for e in errors: print(e)
        return 1
    print('WITNESS VALIDATION: PASS'); return 0
if __name__=='__main__': raise SystemExit(main())
