import sys, os, json, hashlib, copy, urllib.request, zipfile
from pathlib import Path
from datetime import datetime, timezone
from dataclasses import asdict
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
LAB=Path('C:/Users/MDP/Documents/Default Project/llm-lab')
PARENT=Path('C:/Users/MDP/Documents/ChatGPT/Collatz')
sys.path.insert(0,str(LAB))
from dotenv import dotenv_values
from lab.directed import preflight_directed_task, run_directed_task, verify_directed_task
os.environ['OPENROUTER_API_KEY']=os.environ.get('OPENROUTER_API_KEY') or dotenv_values(LAB/'.env').get('OPENROUTER_API_KEY','')
os.environ['OPENAI_BASE_URL']='https://openrouter.ai/api/v1'
SPECS=[('deepseek','deepseek/deepseek-v4-pro-0813',.66,1.98,.04),('glm','z-ai/glm-5.3-flash',.075,.25,.005)]
def save(path,data):
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
if sys.argv[1]=='prepare':
    with urllib.request.urlopen('https://openrouter.ai/api/v1/models',timeout=30) as r:
        models=json.load(r)['data']
    plan=[]
    for tag,model,p,q,cap in SPECS:
        folder=HERE/tag
        folder.mkdir(exist_ok=True)
        assert not (folder/'DISPATCH_ONCE.json').exists()
        m=next(x for x in models if x['id']==model)
        assert float(m['pricing']['prompt'])*1e6<=p+1e-9 and float(m['pricing']['completion'])*1e6<=q+1e-9
        assert 'high' in m['reasoning']['supported_efforts']
        save(folder/'MODEL_CATALOG_SNAPSHOT.json',{k:m.get(k) for k in ('id','canonical_slug','pricing','reasoning','supported_parameters')})
        c=json.loads((HERE.parent/'llmlab_luna/TASK_CONTRACT.json').read_text(encoding='utf-8'))
        c['task_id']=f'cp20-xub-{tag}-five-routes-v1'
        c['project_id']=f'cp20-xub-{tag}-20260907'
        c['created_at']=datetime.now(timezone.utc).isoformat()
        c['objective']=c['objective'].replace('fresh Luna five-route pilot',f'fresh {model} five-route pilot')
        for lane in c['agent_plan']['lanes']:
            lane.update(lane_id=lane['lane_id'].replace('luna-',tag+'-'),model=model,independence_group='same-model-'+tag,input_price_per_million=p,output_price_per_million=q,max_cost_usd=cap)
        c['budget']['max_total_cost_usd']=5*cap
        cp=folder/'TASK_CONTRACT.json'
        save(cp,c)
        gate=preflight_directed_task(cp,input_root=PARENT,parent_repo=PARENT,root=folder/'runs')
        save(folder/'PREFLIGHT.json',gate)
        assert gate['gate_status']=='FEASIBLE_WITH_LIMITATIONS',gate
        plan.append({'tag':tag,'hash':hashlib.sha256(cp.read_bytes()).hexdigest(),'max_cost_usd':5*cap,'gate':gate['gate_status']})
    save(HERE/'PLAN.json',plan)
    print(json.dumps(plan))
elif sys.argv[1]=='run':
    assert hashlib.sha256((HERE/'PLAN.json').read_bytes()).hexdigest()==sys.argv[2]
    plan=json.loads((HERE/'PLAN.json').read_text())
    for item in plan:
        folder=HERE/item['tag']; cp=folder/'TASK_CONTRACT.json'
        assert hashlib.sha256(cp.read_bytes()).hexdigest()==item['hash']
        with (folder/'DISPATCH_ONCE.json').open('x') as f:
            json.dump(item,f)
        print('START '+item['tag'],flush=True)
        r=run_directed_task(cp,input_root=PARENT,parent_repo=PARENT,root=folder/'runs')
        save(folder/'RESULT.json',asdict(r))
        print(json.dumps(asdict(r)),flush=True)
        if r.package_path:
            c=json.loads(cp.read_text(encoding='utf-8'))
            v=verify_directed_task(c['project_id'],r.run_id,root=folder/'runs')
            with zipfile.ZipFile(r.package_path) as z:
                v['crc_error']=z.testzip(); v['members']=len(z.infolist())
            save(folder/'VERIFICATION.json',v)
            print(json.dumps(v),flush=True)
            assert v['ok'] and v['crc_error'] is None
