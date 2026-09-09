import os
import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone
from dataclasses import asdict

sys.dont_write_bytecode = True
LAB = Path('C:/Users/MDP/Documents/Default Project/llm-lab')
PARENT = Path('C:/Users/MDP/Documents/ChatGPT/Collatz')
HERE = Path(__file__).resolve().parent
ROOT = HERE / 'runs'
sys.path.insert(0, str(LAB))
from dotenv import dotenv_values
from lab.directed import preflight_directed_task, run_directed_task, verify_directed_task

def save(name, data):
    (HERE / name).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

def credentials():
    key = os.environ.get('OPENROUTER_API_KEY') or dotenv_values(LAB / '.env').get('OPENROUTER_API_KEY')
    if not key:
        raise RuntimeError('OpenRouter credential unavailable')
    os.environ['OPENROUTER_API_KEY'] = key
    os.environ['OPENAI_BASE_URL'] = 'https://openrouter.ai/api/v1'

mode = sys.argv[1]
contract_path = HERE / 'TASK_CONTRACT.json'
if mode == 'prepare':
    import urllib.request
    with urllib.request.urlopen('https://openrouter.ai/api/v1/models', timeout=30) as response:
        models = json.load(response)['data']
    old = PARENT / 'research_manager/exploratory/sync_20260907/llm_lab_pilot/CP20_XUB_LLMLAB_REAL_PILOT_V1_TASK_CONTRACT.json'
    c = json.loads(old.read_text(encoding='utf-8'))
    c['task_id'] = 'cp20-xub-marked-occupation-advisory-v2'
    c['project_id'] = 'cp20-xub-llmlab-pilot-v2-20260907'
    c['parent_state_commit'] = 'ad289d9623661ab927c89ac798c55ba42d7abd2c'
    c['created_at'] = datetime.now(timezone.utc).isoformat()
    c['created_by'] = 'codex-principal-recovery-successor'
    c['objective'] += (' This is a fresh V2 pilot, not a resumption of V1. Prioritize a concise, inspectable public final answer: at most 1200 words in findings. If the main estimate cannot be established, stop the attempted proof and explicitly report OPEN with the first missing inequality, its quantifiers, and why the displayed reductions do not prove it. Do not spend the entire response pursuing a full proof. Give checkable mathematical arguments in the final findings; unsupported theorem invocations and model agreement are not evidence.')
    catalog = {}
    for lane in c['agent_plan']['lanes']:
        m = next(x for x in models if x['id'] == lane['model'])
        if 'low' not in m.get('reasoning', {}).get('supported_efforts', []):
            raise RuntimeError('Low reasoning support not confirmed')
        p, q = float(m['pricing']['prompt']) * 1e6, float(m['pricing']['completion']) * 1e6
        if p > lane['input_price_per_million'] or q > lane['output_price_per_million']:
            raise RuntimeError('Live price exceeds planned ceiling')
        lane['reasoning_effort'] = 'low'
        lane['max_completion_tokens'] = 8000 if lane['depends_on'] else 12000
        lane['max_wall_seconds'] = 600
        catalog[lane['model']] = {k: m.get(k) for k in ('id', 'pricing', 'reasoning', 'supported_parameters')}
    c['budget']['max_wall_seconds'] = 1200
    save('MODEL_CATALOG_SNAPSHOT.json', {'retrieved_at': datetime.now(timezone.utc).isoformat(), 'url': 'https://openrouter.ai/api/v1/models', 'models': catalog})
    save('TASK_CONTRACT.json', c)
    credentials()
    gate = preflight_directed_task(contract_path, input_root=PARENT, parent_repo=PARENT, root=ROOT)
    save('PREFLIGHT.json', gate)
    print(json.dumps(gate, ensure_ascii=False, indent=2))
    print('CONTRACT_SHA256', hashlib.sha256(contract_path.read_bytes()).hexdigest())
elif mode == 'run':
    credentials()
    digest = hashlib.sha256(contract_path.read_bytes()).hexdigest()
    expected = sys.argv[2]
    if digest != expected:
        raise RuntimeError('Contract changed after review')
    # Exclusive marker makes accidental repeat invocation fail before any model call.
    with (HERE / 'DISPATCH_ONCE.json').open('x', encoding='utf-8') as f:
        json.dump({'contract_sha256': digest, 'started_at': datetime.now(timezone.utc).isoformat(), 'max_calls': 3, 'max_cost_usd': 0.75, 'retries': 0}, f)
    result = run_directed_task(contract_path, input_root=PARENT, parent_repo=PARENT, root=ROOT)
    save('RESULT.json', asdict(result))
    print(json.dumps(asdict(result), indent=2))
    if result.package_path:
        verified = verify_directed_task('cp20-xub-llmlab-pilot-v2-20260907', result.run_id, root=ROOT)
        save('VERIFICATION.json', verified)
        print(json.dumps(verified, indent=2))
else:
    raise RuntimeError('Unknown mode')
