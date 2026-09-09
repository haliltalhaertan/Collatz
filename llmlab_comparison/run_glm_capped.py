import sys,os,json,hashlib,importlib.util,zipfile
from pathlib import Path
from dataclasses import asdict
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
LAB=Path('C:/Users/MDP/Documents/Default Project/llm-lab')
PARENT=Path('C:/Users/MDP/Documents/ChatGPT/Collatz')
sys.path.insert(0,str(LAB))
from dotenv import dotenv_values
from lab.directed import preflight_directed_task,run_directed_task,verify_directed_task
folder=HERE/'glm_capped'; folder.mkdir(exist_ok=True)
def save(name,d): (folder/name).write_text(json.dumps(d,indent=2,ensure_ascii=False),encoding='utf-8')
os.environ['OPENROUTER_API_KEY']=os.environ.get('OPENROUTER_API_KEY') or dotenv_values(LAB/'.env').get('OPENROUTER_API_KEY','')
os.environ['OPENAI_BASE_URL']='https://openrouter.ai/api/v1'
source=(LAB/'lab/directed_provider.py').read_text(encoding='utf-8')
needle='        text, reasoning, finish, usage = "", "", None, {}'
assert source.count(needle)==1
source=source.replace(needle,'''        kwargs.setdefault("extra_body", {})["provider"] = {
            "max_price": {"prompt": 0.075, "completion": 0.25},
            "sort": "price"
        }
'''+needle)
adapter=folder/'capped_provider.py'
if sys.argv[1]=='prepare':
    assert not (folder/'DISPATCH_ONCE.json').exists()
    adapter.write_text(source,encoding='utf-8')
spec=importlib.util.spec_from_file_location('capped_glm_provider',adapter)
module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
provider=module.DirectedProvider()
cp=folder/'TASK_CONTRACT.json'
if sys.argv[1]=='prepare':
    c=json.loads((HERE/'glm/TASK_CONTRACT.json').read_text(encoding='utf-8'))
    c['project_id']='cp20-xub-glm-capped-20260907'
    c['task_id']='cp20-xub-glm-capped-five-routes-v1'
    save('TASK_CONTRACT.json',c)
    gate=preflight_directed_task(cp,input_root=PARENT,parent_repo=PARENT,provider=provider,root=folder/'runs')
    save('PREFLIGHT.json',gate)
    binding={'contract':hashlib.sha256(cp.read_bytes()).hexdigest(),'adapter':hashlib.sha256(adapter.read_bytes()).hexdigest(),'routing':{'max_price':{'prompt':.075,'completion':.25},'sort':'price'}}
    save('BINDING.json',binding)
    print(gate['gate_status']); print(hashlib.sha256((folder/'BINDING.json').read_bytes()).hexdigest())
elif sys.argv[1]=='run':
    assert hashlib.sha256((folder/'BINDING.json').read_bytes()).hexdigest()==sys.argv[2]
    b=json.loads((folder/'BINDING.json').read_text())
    assert hashlib.sha256(cp.read_bytes()).hexdigest()==b['contract']
    assert hashlib.sha256(adapter.read_bytes()).hexdigest()==b['adapter']
    with (folder/'DISPATCH_ONCE.json').open('x') as f: json.dump(b,f)
    r=run_directed_task(cp,input_root=PARENT,parent_repo=PARENT,provider=provider,root=folder/'runs')
    save('RESULT.json',asdict(r)); print(json.dumps(asdict(r)))
    if r.package_path:
        v=verify_directed_task('cp20-xub-glm-capped-20260907',r.run_id,root=folder/'runs')
        with zipfile.ZipFile(r.package_path) as z: v.update(crc_error=z.testzip(),members=len(z.infolist()))
        save('VERIFICATION.json',v); print(json.dumps(v))
