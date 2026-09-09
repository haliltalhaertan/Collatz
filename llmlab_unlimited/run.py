import sys,os,json,hashlib,zipfile
from pathlib import Path
from dataclasses import asdict
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
PARENT=Path('C:/Users/MDP/Documents/ChatGPT/Collatz')
sys.path.insert(0,str(HERE/'runtime'))
from dotenv import dotenv_values
from lab.directed import preflight_directed_task,run_directed_task,verify_directed_task
from lab.directed_contract import Budget,Lane
from lab.directed_provider import DirectedProvider
os.environ['OPENROUTER_API_KEY']=os.environ.get('OPENROUTER_API_KEY') or dotenv_values(Path('C:/Users/MDP/Documents/Default Project/llm-lab/.env')).get('OPENROUTER_API_KEY','')
os.environ['OPENAI_BASE_URL']='https://openrouter.ai/api/v1'
cp=HERE/'TASK_CONTRACT.json'
def save(name,d): (HERE/name).write_text(json.dumps(d,indent=2,ensure_ascii=False),encoding='utf-8')
manifest=json.loads((HERE/'RUNTIME_MANIFEST.json').read_text())
for p,digest in manifest.items(): assert hashlib.sha256((HERE/'runtime'/p).read_bytes()).hexdigest()==digest,p
if sys.argv[1]=='preflight':
    import lab.directed_provider as dp
    from types import SimpleNamespace
    captured={}
    class Stream:
        def __enter__(self): return iter([])
        def __exit__(self,*a): pass
    class Client:
        def __init__(self,**kw):
            captured['client']=kw
            self.chat=SimpleNamespace(completions=SimpleNamespace(create=self.create))
        def create(self,**kw): captured['request']=kw; return Stream()
        def __enter__(self): return self
        def __exit__(self,*a): pass
    original=dp.OpenAI; dp.OpenAI=Client
    c=json.loads(cp.read_text(encoding='utf-8'))
    lane=Lane.model_validate(c['agent_plan']['lanes'][0]); budget=Budget.model_validate(c['budget'])
    assert lane.max_wall_seconds==budget.max_wall_seconds==0
    try: DirectedProvider().call(lane,'offline check',lambda *a:None,lambda:False,float('inf'),'offline-no-dispatch')
    finally: dp.OpenAI=original
    assert captured['client']['timeout'] is None
    assert captured['client']['max_retries']==0
    assert captured['request']['extra_body']['provider']['max_price']=={'prompt':.66,'completion':1.98}
    for p in (HERE/'runtime/lab').glob('directed*.py'): compile(p.read_text(encoding='utf-8'),str(p),'exec')
    gate=preflight_directed_task(cp,input_root=PARENT,parent_repo=PARENT,root=HERE/'runs')
    save('PREFLIGHT.json',gate)
    assert gate['gate_status']=='FEASIBLE_WITH_LIMITATIONS',gate
    print('Offline adapter checks passed; '+gate['gate_status'])
    print(hashlib.sha256(cp.read_bytes()).hexdigest())
elif sys.argv[1]=='run':
    assert hashlib.sha256(cp.read_bytes()).hexdigest()==sys.argv[2]
    with (HERE/'DISPATCH_ONCE.json').open('x') as f: json.dump({'calls':15,'cost_ceiling':.475,'time_limit':None,'retries':0},f)
    r=run_directed_task(cp,input_root=PARENT,parent_repo=PARENT,root=HERE/'runs')
    save('RESULT.json',asdict(r)); print(json.dumps(asdict(r)),flush=True)
    if r.package_path:
        v=verify_directed_task('cp20-xub-no-timeout-20260907',r.run_id,root=HERE/'runs')
        with zipfile.ZipFile(r.package_path) as z: v.update(crc_error=z.testzip(),members=len(z.infolist()))
        save('VERIFICATION.json',v); print(json.dumps(v),flush=True)
