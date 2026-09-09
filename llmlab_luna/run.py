import sys, os, json, hashlib, copy
from pathlib import Path
from datetime import datetime, timezone
from dataclasses import asdict
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
LAB = Path('C:/Users/MDP/Documents/Default Project/llm-lab')
PARENT = Path('C:/Users/MDP/Documents/ChatGPT/Collatz')
sys.path.insert(0, str(LAB))
from dotenv import dotenv_values
from lab.directed import preflight_directed_task, run_directed_task, verify_directed_task
def save(name, data):
    (HERE/name).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
os.environ['OPENROUTER_API_KEY'] = os.environ.get('OPENROUTER_API_KEY') or dotenv_values(LAB/'.env').get('OPENROUTER_API_KEY', '')
os.environ['OPENAI_BASE_URL'] = 'https://openrouter.ai/api/v1'
cp = HERE/'TASK_CONTRACT.json'
if sys.argv[1] == 'prepare':
    import urllib.request
    with urllib.request.urlopen('https://openrouter.ai/api/v1/models', timeout=30) as r:
        m = next(x for x in json.load(r)['data'] if x['id']=='openai/gpt-5.6-luna')
    assert float(m['pricing']['prompt']) <= .2/1e6 and float(m['pricing']['completion']) <= 1.2/1e6
    assert 'high' in m['reasoning']['supported_efforts']
    save('MODEL_CATALOG_SNAPSHOT.json', {k:m.get(k) for k in ('id','pricing','reasoning')})
    c=json.loads((HERE.parent/'llmlab_v2/TASK_CONTRACT.json').read_text(encoding='utf-8'))
    c['task_id']='cp20-xub-luna-five-routes-v1'
    c['project_id']='cp20-xub-luna-20260907'
    c['created_at']=datetime.now(timezone.utc).isoformat()
    c['objective']=c['objective'].replace('This is a fresh V2 pilot, not a resumption of V1.', 'This is a fresh Luna five-route pilot. Each lane must follow its assigned route in its role. Separate calls to the same model are not independent verification.').replace('at most 1200 words','at most 800 words')
    routes=[('counting','Derive exact weak-composition coefficient identities and identify a sufficient occupation bound; preserve first-passage conditioning.'),('cycles','Audit a cyclic-shift or ballot approach, resolving ties, affine shifts, even sampling and odd parity; isolate the first missing lemma.'),('low-state','Analyze low-state occupation through an exact bridge decomposition; do not assume low visits are rare.'),('resonance','Analyze weighted amplified-resonance counting on actual coupled arrays, and its interaction with useful-block occupation.'),('refutation','Adversarially seek an actual accessible counterexample or a necessary condition that could fail. Verify quantifiers; arbitrary endpoints are inadmissible.')]
    base=c['agent_plan']['lanes'][0]
    lanes=[]
    for name,role in routes:
        x=copy.deepcopy(base)
        x.update(lane_id='luna-'+name,role=role,model=m['id'],reasoning_effort='high',independence_group='same-model-luna',max_completion_tokens=8000,max_calls=1,max_tokens=30000,max_cost_usd=.02,max_wall_seconds=600,input_price_per_million=.2,output_price_per_million=1.2)
        lanes.append(x)
    c['agent_plan'].update(lanes=lanes,max_parallel_workers=4)
    c['budget'].update(max_total_llm_calls=5,max_total_tokens=150000,max_tokens_per_lane=30000,max_total_cost_usd=.10,max_wall_seconds=1250,max_parallel_workers=4)
    save('TASK_CONTRACT.json',c)
    gate=preflight_directed_task(cp,input_root=PARENT,parent_repo=PARENT,root=HERE/'runs')
    save('PREFLIGHT.json',gate)
    print(json.dumps(gate)); print(hashlib.sha256(cp.read_bytes()).hexdigest())
elif sys.argv[1]=='run':
    assert hashlib.sha256(cp.read_bytes()).hexdigest()==sys.argv[2]
    with (HERE/'DISPATCH_ONCE.json').open('x') as f:
        json.dump({'max_calls':5,'max_cost_usd':.10,'retries':0},f)
    result=run_directed_task(cp,input_root=PARENT,parent_repo=PARENT,root=HERE/'runs')
    save('RESULT.json',asdict(result)); print(json.dumps(asdict(result)))
    if result.package_path:
        v=verify_directed_task('cp20-xub-luna-20260907',result.run_id,root=HERE/'runs')
        save('VERIFICATION.json',v); print(json.dumps(v))

