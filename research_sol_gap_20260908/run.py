import sys,os,json,hashlib,zipfile
from pathlib import Path
from dataclasses import asdict
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
sys.path.insert(0,str(BASE/'llmlab_unlimited/runtime'))
from dotenv import dotenv_values
from lab.directed import preflight_directed_task,run_directed_task,verify_directed_task
os.environ['OPENROUTER_API_KEY']=os.environ.get('OPENROUTER_API_KEY') or dotenv_values(Path('C:/Users/MDP/Documents/Default Project/llm-lab/.env')).get('OPENROUTER_API_KEY','')
os.environ['OPENAI_BASE_URL']='https://openrouter.ai/api/v1'
def save(n,d): (HERE/n).write_text(json.dumps(d,indent=2,ensure_ascii=False),encoding='utf-8')
for n,h in json.loads((HERE/'FROZEN_HASHES.json').read_text()).items(): assert hashlib.sha256((HERE/n).read_bytes()).hexdigest()==h
cp=HERE/'TASK_CONTRACT.json'
if sys.argv[1]=='preflight':
    g=preflight_directed_task(cp,input_root=BASE,parent_repo=BASE,root=HERE/'runs');save('PREFLIGHT.json',g);print(json.dumps(g))
elif sys.argv[1]=='run':
    assert json.loads((HERE/'PREFLIGHT.json').read_text())['gate_status']=='FEASIBLE_WITH_LIMITATIONS'
    with (HERE/'DISPATCH_ONCE.json').open('x') as f: json.dump({'calls':1,'max_cost_usd':.08,'retries':0},f)
    r=run_directed_task(cp,input_root=BASE,parent_repo=BASE,root=HERE/'runs');save('RESULT.json',asdict(r));print(json.dumps(asdict(r)),flush=True)
    if r.package_path:
        v=verify_directed_task('xub-gap-20260908',r.run_id,root=HERE/'runs')
        with zipfile.ZipFile(r.package_path) as z:v.update(crc_error=z.testzip(),members=len(z.infolist()))
        save('VERIFICATION.json',v);print(json.dumps(v),flush=True)
