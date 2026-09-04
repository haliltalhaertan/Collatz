#!/usr/bin/env python3
# INTEGRITY ORCHESTRATOR ONLY. NO B4 MATHEMATICS.
import argparse, datetime, hashlib, importlib.util, json, os, pathlib, shlex, subprocess, sys, zipfile
TASK='CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2'
VERSION='V2'
STAGE0_SOURCE='8d274095b0e1acbe1fad0a73ef6a5293364902fc'
BLOCKED={
 'ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c',
 '2e6d9e1d833fc8dabf02c0e970ccfb06fc86e4cbc9e85cd2e0e61ae3611879ea',
 '66ac975940abb29a1248079ea6e03643ded966da296cf33deb7c7a0f5fa60eac',
 '06768aebd233c874fbb2103f3f3ccadca7db5ae76c7f5fb051ab982cf737012f',
}
AUTH_PATH='research_manager/decisions/CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE1_AUTHORIZATION.json'
HERE=pathlib.Path(__file__).resolve().parent
WITNESS=HERE/f'{TASK}_STAGE1_RUN_WITNESS.json'
GATE=HERE/f'{TASK}_STAGE1_PRE_T1_GATE.json'
LEDGER=HERE/f'{TASK}_STAGE1_EXECUTION_LEDGER.jsonl'
FAILURE=HERE/f'{TASK}_STAGE1_INPUT_INTEGRITY_FAILURE.json'

def hbytes(b): return hashlib.sha256(b).hexdigest()
def hfile(p): return hbytes(pathlib.Path(p).read_bytes())
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*args): return subprocess.check_output(['git',*args],text=True,stderr=subprocess.STDOUT).strip()
def git_bytes(*args): return subprocess.check_output(['git',*args],stderr=subprocess.STDOUT)
def atomic_json(path,obj):
    tmp=path.with_name(path.name+f'.tmp.{os.getpid()}')
    tmp.write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n',encoding='utf-8'); os.replace(tmp,path)
def fail(msg):
    rec={'status':'[B4 V2 STAGE1 INPUT INTEGRITY FAILURE]','reason':str(msg),'utc_timestamp':utc(),'authorization_consumed':True,'T1_T8':'NOT_EXECUTED'}
    try:
        fd=os.open(FAILURE,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o644)
        with os.fdopen(fd,'w',encoding='utf-8') as f: json.dump(rec,f,indent=2,sort_keys=True); f.write('\n')
    except FileExistsError: pass
    raise SystemExit('[B4 V2 STAGE1 INPUT INTEGRITY FAILURE] '+str(msg))

def require_commit(sha,label):
    try: git('cat-file','-e',sha+'^{commit}')
    except Exception: fail(label+' does not resolve to commit')
def require_ancestor(older,newer,label):
    try: subprocess.check_call(['git','merge-base','--is-ancestor',older,newer],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    except Exception: fail(label)

def verify_authorization_chain(stage0_base,authorization_commit,seal_sha,contract_sha,config):
    require_commit(stage0_base,'canonical_stage0_base_sha')
    require_commit(authorization_commit,'authorization_commit_sha')
    if stage0_base==authorization_commit: fail('canonical_stage0_base_sha and authorization_commit_sha must be distinct')
    require_ancestor(STAGE0_SOURCE,stage0_base,'stage0_source_base_sha is not ancestor of canonical_stage0_base_sha')
    require_ancestor(stage0_base,authorization_commit,'canonical_stage0_base_sha is not ancestor of authorization_commit_sha')
    require_ancestor(authorization_commit,'HEAD','authorization_commit_sha is not ancestor of execution HEAD')
    try: auth=json.loads(git('show',f'{authorization_commit}:{AUTH_PATH}'))
    except Exception: fail('authorization artifact unreadable at authorization_commit_sha')
    if auth.get('authorized_v2_seal_sha256')!=seal_sha: fail('authorization seal mismatch')
    if auth.get('v2_contract_sha256')!=contract_sha: fail('authorization contract mismatch')
    if auth.get('canonical_stage0_base_sha')!=stage0_base: fail('authorization canonical_stage0_base_sha mismatch')
    if auth.get('stage')!='STAGE_1_AUTHORIZED_NOT_EXECUTED': fail('authorization stage mismatch')
    try: state=json.loads(git('show',f'{authorization_commit}:CURRENT_RESEARCH_STATE.json'))
    except Exception: fail('canonical state unreadable at authorization_commit_sha')
    if not isinstance(state,dict): fail('canonical state is not an object')
    if 'active_task' not in state: fail('canonical state missing active_task')
    active_task=state['active_task']
    if not isinstance(active_task,dict): fail('canonical state active_task is not an object')
    if 'stage' not in active_task: fail('canonical state missing active_task.stage')
    stage=active_task['stage']
    if stage!='STAGE_1_AUTHORIZED_NOT_EXECUTED': fail('canonical state active_task.stage does not say STAGE_1_AUTHORIZED_NOT_EXECUTED')
    aliases=[]
    if 'active_stage' in state: aliases.append(('active_stage',state['active_stage']))
    continuity=state.get('continuity')
    if isinstance(continuity,dict) and 'active_stage' in continuity: aliases.append(('continuity.active_stage',continuity['active_stage']))
    for label,value in aliases:
        if value!=stage: fail('canonical state legacy stage alias conflicts with active_task.stage: '+label)
    for path,expected in config['canonical_stage0_artifacts'].items():
        try: blob=git('rev-parse',f'{stage0_base}:{path}')
        except Exception: fail('Phase-A Stage0 artifact unreadable: '+path)
        if blob!=expected['git_blob_sha1']: fail('Phase-A Stage0 Git blob mismatch: '+path)
        try: data=git_bytes('show',f'{stage0_base}:{path}')
        except Exception: fail('Phase-A Stage0 artifact bytes unreadable: '+path)
        if hbytes(data)!=expected['sha256']: fail('Phase-A Stage0 SHA256 mismatch: '+path)
    for path,blob in config['frozen_dependencies'].items():
        try: got=git('rev-parse',f'{stage0_base}:{path}')
        except Exception: fail('frozen dependency unreadable at Phase A: '+path)
        if got!=blob: fail('frozen dependency blob mismatch at Phase A: '+path)

def verify_seal(seal,authorized_sha,contract_sha,config_path):
    if authorized_sha in BLOCKED: fail('blocked candidate seal rejected')
    if hfile(seal)!=authorized_sha: fail('seal SHA mismatch')
    with zipfile.ZipFile(seal) as z:
        if z.testzip() is not None: fail('ZIP CRC failure')
        names=z.namelist()
        if len(names)!=len(set(names)): fail('duplicate ZIP member')
        if names!=sorted(names): fail('ZIP membership order not deterministic')
        manifest_name=f'{TASK}_PRE_RUN_SHA256SUMS.txt'
        if manifest_name not in names: fail('manifest missing')
        manifested={}
        for line in z.read(manifest_name).decode('utf-8').splitlines():
            hh,n=line.split('  ',1)
            if n in manifested: fail('duplicate manifest member')
            manifested[n]=hh
        if set(manifested)!=(set(names)-{manifest_name}): fail('manifest membership mismatch')
        for n,hh in manifested.items():
            if hbytes(z.read(n))!=hh: fail('member hash mismatch: '+n)
        cfgname=f'{TASK}_CONFIG.json'; contractname=f'{TASK}_STAGE1_EXECUTION_INTEGRITY_AND_OUTPUT_CONTRACT.md'
        if hbytes(z.read(cfgname))!=hfile(config_path): fail('external/sealed config mismatch')
        if hbytes(z.read(contractname))!=contract_sha: fail('sealed contract SHA mismatch')

def output_absence(output):
    if any(p.exists() for p in [pathlib.Path(output),WITNESS,GATE,LEDGER,FAILURE]): fail('Stage1 output already exists')

def write_witness(a):
    exact='python '+' '.join(shlex.quote(x) for x in sys.argv)
    obj={'task':TASK,'task_version':VERSION,'stage0_source_base_sha':STAGE0_SOURCE,
      'canonical_stage0_base_sha':a.canonical_stage0_base_sha,
      'authorization_commit_sha':a.authorization_commit_sha,
      'canonical_base_sha':a.authorization_commit_sha,
      'authorized_seal_sha256':a.authorized_seal_sha256,'contract_sha256':a.contract_sha256,'config_sha256':hfile(a.config),
      'execution_count_claim':1,'output_absence_precheck':'PASS','utc_timestamp':utc(),
      'pid_or_session_identifier':f'pid:{os.getpid()}','exact_entrypoint':exact,'preflight_status':'PASS'}
    atomic_json(WITNESS,obj); return obj

def validate_witness(a):
    vp=HERE/f'{TASK}_WITNESS_VALIDATOR.py'; spec=importlib.util.spec_from_file_location('v2validator',vp)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    w=json.loads(WITNESS.read_text(encoding='utf-8'))
    errs=m.validate(w,a.canonical_stage0_base_sha,a.authorization_commit_sha,a.authorized_seal_sha256,a.contract_sha256,hfile(a.config))
    if errs: fail('RUN_WITNESS validation: '+';'.join(errs))

def write_gate(a):
    atomic_json(GATE,{'status':'PASS','canonical_stage0_base_sha':a.canonical_stage0_base_sha,
      'authorization_commit_sha':a.authorization_commit_sha,'canonical_base_sha':a.authorization_commit_sha,
      'run_witness_sha256':hfile(WITNESS),'authorized_seal_sha256':a.authorized_seal_sha256,
      'contract_sha256':a.contract_sha256,'config_sha256':hfile(a.config),'utc_timestamp':utc()})

def append_pre_t1_gate_ledger():
    if not GATE.exists() or json.loads(GATE.read_text(encoding='utf-8')).get('status')!='PASS': fail('PRE_T1_GATE is not PASS')
    with LEDGER.open('a',encoding='utf-8') as f:
        f.write(json.dumps({'event':'PRE_T1_GATE','status':'PASS','utc_timestamp':utc(),'gate_sha256':hfile(GATE)},sort_keys=True)+'\n')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--config',required=True); ap.add_argument('--seal',required=True)
    ap.add_argument('--canonical-stage0-base-sha',required=True); ap.add_argument('--authorization-commit-sha',required=True)
    ap.add_argument('--authorized-seal-sha256',required=True); ap.add_argument('--contract-sha256',required=True); ap.add_argument('--output',required=True)
    a=ap.parse_args()
    try:
        config=json.load(open(a.config,encoding='utf-8'))
        if config.get('stage0_source_base_sha')!=STAGE0_SOURCE: fail('config stage0 source base')
        if config.get('contract',{}).get('sha256')!=a.contract_sha256: fail('manager/config contract SHA mismatch')
        if hfile(HERE/config['contract']['filename'])!=a.contract_sha256: fail('local contract SHA mismatch')
        verify_seal(a.seal,a.authorized_seal_sha256,a.contract_sha256,a.config)
        output_absence(a.output)
        verify_authorization_chain(a.canonical_stage0_base_sha,a.authorization_commit_sha,a.authorized_seal_sha256,a.contract_sha256,config)
        write_witness(a); validate_witness(a); write_gate(a); append_pre_t1_gate_ledger()
        atomic_json(pathlib.Path(a.output),{'task':TASK,'integrity_preflight':'PASS','pre_t1_gate':'PASS','T1_T8':{f'T{i}':'NOT_EXECUTED' for i in range(1,9)},'stage1_complete':False,'next_permitted_action':'T1 START may be appended only by an authorized proof session after re-reading PRE_T1_GATE PASS'})
        print('B4 V2 STAGE1 PRE-T1 INTEGRITY GATE: PASS')
        print('T1–T8 NOT EXECUTED by integrity launcher.')
    except SystemExit: raise
    except Exception as e: fail(type(e).__name__+': '+str(e))
if __name__=='__main__': main()
