import sys,os,json,hashlib,urllib.request,zipfile
from pathlib import Path
from dataclasses import asdict
from datetime import datetime,timezone
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
RUNTIME=HERE.parent/'llmlab_unlimited/runtime'
PARENT=Path('C:/Users/MDP/Documents/ChatGPT/Collatz')
sys.path.insert(0,str(RUNTIME))
from dotenv import dotenv_values
from lab.directed import preflight_directed_task,run_directed_task,verify_directed_task
os.environ['OPENROUTER_API_KEY']=os.environ.get('OPENROUTER_API_KEY') or dotenv_values(Path('C:/Users/MDP/Documents/Default Project/llm-lab/.env')).get('OPENROUTER_API_KEY','')
os.environ['OPENAI_BASE_URL']='https://openrouter.ai/api/v1'
def save(name,d): (HERE/name).write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
manifest=json.loads((HERE.parent/'llmlab_unlimited/RUNTIME_MANIFEST.json').read_text())
for p,h in manifest.items(): assert hashlib.sha256((RUNTIME/p).read_bytes()).hexdigest()==h
cp=HERE/'TASK_CONTRACT.json'
if sys.argv[1]=='prepare':
    with urllib.request.urlopen('https://openrouter.ai/api/v1/models',timeout=30) as r: m=next(x for x in json.load(r)['data'] if x['id']=='openai/gpt-5.6-sol')
    assert 'none' in m['reasoning']['supported_efforts']
    assert float(m['pricing']['prompt'])<=2/1e6 and float(m['pricing']['completion'])<=10/1e6
    save('MODEL_CATALOG_SNAPSHOT.json',{k:m.get(k) for k in ('id','pricing','reasoning')})
    c=json.loads((HERE.parent/'llmlab_luna/TASK_CONTRACT.json').read_text(encoding='utf-8'))
    c.update(task_id='cp20-xub-sol-none-v1',project_id='cp20-xub-sol-none-20260908',created_at=datetime.now(timezone.utc).isoformat())
    c['objective']=c['objective'].replace('fresh Luna five-route pilot','fresh single-lane Sol none pilot')+' max_wall_seconds=0 means no elapsed-time cutoff in this isolated runtime.'
    lane=c['agent_plan']['lanes'][0]
    lane.update(lane_id='sol-none-review',role='Review the marked occupation estimate. Give a checkable proof, actual accessible refutation, or a precise missing lemma. Distinguish necessary conditions from stronger sufficient assumptions.',model=m['id'],reasoning_effort='none',independence_group='sol-none',max_wall_seconds=0,max_cost_usd=.13,input_price_per_million=2,output_price_per_million=10)
    c['agent_plan'].update(lanes=[lane],max_parallel_workers=1)
    c['budget'].update(max_total_llm_calls=1,max_total_tokens=30000,max_total_cost_usd=.13,max_wall_seconds=0,max_parallel_workers=1)
    save('TASK_CONTRACT.json',c)
    g=preflight_directed_task(cp,input_root=PARENT,parent_repo=PARENT,root=HERE/'runs');save('PREFLIGHT.json',g)
    assert g['gate_status']=='FEASIBLE_WITH_LIMITATIONS',g
    print(g['gate_status']);print(hashlib.sha256(cp.read_bytes()).hexdigest())
elif sys.argv[1]=='run':
    assert hashlib.sha256(cp.read_bytes()).hexdigest()==sys.argv[2]
    with (HERE/'DISPATCH_ONCE.json').open('x') as f: json.dump({'calls':1,'max_cost_usd':.13,'time_limit':None},f)
    r=run_directed_task(cp,input_root=PARENT,parent_repo=PARENT,root=HERE/'runs');save('RESULT.json',asdict(r));print(json.dumps(asdict(r)),flush=True)
    if r.package_path:
        v=verify_directed_task('cp20-xub-sol-none-20260908',r.run_id,root=HERE/'runs')
        with zipfile.ZipFile(r.package_path) as z: v.update(crc_error=z.testzip(),members=len(z.infolist()))
        save('VERIFICATION.json',v);print(json.dumps(v),flush=True)

