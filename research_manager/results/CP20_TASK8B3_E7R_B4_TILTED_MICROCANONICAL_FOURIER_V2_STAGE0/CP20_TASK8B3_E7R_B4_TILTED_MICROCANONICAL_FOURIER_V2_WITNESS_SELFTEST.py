#!/usr/bin/env python3
import copy, importlib.util, json, pathlib
HERE=pathlib.Path(__file__).resolve().parent
TASK='CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2'
VAL=HERE/f'{TASK}_WITNESS_VALIDATOR.py'
spec=importlib.util.spec_from_file_location('v2validator',VAL)
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
stage0='1'*40; authc='2'*40; head='3'*40; seal='4'*64; contract='5'*64; config='6'*64
witness={
 'task':TASK,'task_version':'V2','stage0_source_base_sha':'8d274095b0e1acbe1fad0a73ef6a5293364902fc',
 'canonical_stage0_base_sha':stage0,'authorization_commit_sha':authc,'canonical_base_sha':authc,
 'authorized_seal_sha256':seal,'contract_sha256':contract,'config_sha256':config,
 'execution_count_claim':1,'output_absence_precheck':'PASS','utc_timestamp':'2026-09-04T00:00:00+00:00',
 'pid_or_session_identifier':'synthetic:selftest','exact_entrypoint':'synthetic only; real Stage1 launcher NOT invoked','preflight_status':'PASS'
}
model={
 'canonical_stage0_base_sha':stage0,'authorization_commit_sha':authc,'execution_head_sha':head,
 'stage0_is_ancestor_authorization':True,'authorization_is_ancestor_execution_head':True,
 'authorization_artifact_present':True,
 'authorization_json':{'authorized_v2_seal_sha256':seal,'v2_contract_sha256':contract,'canonical_stage0_base_sha':stage0,'stage':'STAGE_1_AUTHORIZED_NOT_EXECUTED'},
 'state_stage':'STAGE_1_AUTHORIZED_NOT_EXECUTED'
}
expected={f'S{i}':'FAIL' for i in range(1,12)}; expected['S12']='PASS'
expected.update({'P1':'PASS','P2':'FAIL','P3':'FAIL','P4':'FAIL','P5':'FAIL','P6':'PASS'})
results={}
def witness_case(name, mutate):
    w=copy.deepcopy(witness); mutate(w)
    errs=m.validate(w,stage0,authc,seal,contract,config)
    results[name]={'expected':expected[name],'observed':'PASS' if not errs else 'FAIL','errors':errs}
def model_case(name, mutate):
    x=copy.deepcopy(model); mutate(x)
    errs=m.validate_authorization_model(x,stage0,authc,head,seal,contract)
    results[name]={'expected':expected[name],'observed':'PASS' if not errs else 'FAIL','errors':errs}
def state_case(name,state):
    errs=m.validate_canonical_state(copy.deepcopy(state))
    results[name]={'expected':expected[name],'observed':'PASS' if not errs else 'FAIL','errors':errs}
witness_case('S1',lambda w:w.pop('canonical_stage0_base_sha'))
witness_case('S2',lambda w:w.__setitem__('canonical_stage0_base_sha','9'*40))
witness_case('S3',lambda w:w.pop('authorization_commit_sha'))
witness_case('S4',lambda w:w.__setitem__('authorization_commit_sha','malformed'))
model_case('S5',lambda x:x.__setitem__('stage0_is_ancestor_authorization',False))
model_case('S6',lambda x:x.__setitem__('authorization_is_ancestor_execution_head',False))
model_case('S7',lambda x:x.__setitem__('authorization_artifact_present',False))
model_case('S8',lambda x:x['authorization_json'].__setitem__('authorized_v2_seal_sha256','7'*64))
model_case('S9',lambda x:x['authorization_json'].__setitem__('v2_contract_sha256','8'*64))
model_case('S10',lambda x:x['authorization_json'].__setitem__('canonical_stage0_base_sha','9'*40))
model_case('S11',lambda x:x['authorization_json'].__setitem__('stage','WRONG_STAGE'))
errs=m.validate(witness,stage0,authc,seal,contract,config)+m.validate_authorization_model(model,stage0,authc,head,seal,contract)
results['S12']={'expected':'PASS','observed':'PASS' if not errs else 'FAIL','errors':errs}
state_case('P1',{'active_task':{'stage':'STAGE_1_AUTHORIZED_NOT_EXECUTED'}})
state_case('P2',{})
state_case('P3',{'active_task':{}})
state_case('P4',{'active_task':{'stage':'WRONG_STAGE'}})
state_case('P5',{'active_task':{'stage':'STAGE_1_AUTHORIZED_NOT_EXECUTED'},'active_stage':'CONFLICTING_STAGE'})
state_case('P6',{'active_task':{'stage':'STAGE_1_AUTHORIZED_NOT_EXECUTED'},'active_stage':'STAGE_1_AUTHORIZED_NOT_EXECUTED'})
overall=all(v['expected']==v['observed'] for v in results.values())
out={'schema':f'{TASK}_WITNESS_SELFTEST_RESULTS_TWO_COMMIT_STATEPATH_V4','overall':'PASS' if overall else 'FAIL','real_stage1_entrypoint_invoked':False,'mathematics_executed':False,'cases':results}
(HERE/f'{TASK}_WITNESS_SELFTEST_RESULTS.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print('SELFTEST PASS' if overall else 'SELFTEST FAIL')
raise SystemExit(0 if overall else 1)
