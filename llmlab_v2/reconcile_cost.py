import os
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlencode

sys.dont_write_bytecode = True
from dotenv import dotenv_values
here = Path(__file__).resolve().parent
lab = Path('C:/Users/MDP/Documents/Default Project/llm-lab')
key = os.environ.get('OPENROUTER_API_KEY') or dotenv_values(lab / '.env').get('OPENROUTER_API_KEY')
if not key:
    raise RuntimeError('Credential unavailable')
review = json.loads((here / 'PUBLIC_REVIEW.json').read_text(encoding='utf-8'))
generation = review['lanes']['qwen-independent-refuter']['provider_attempts'][0]['metadata']['id']
url = 'https://openrouter.ai/api/v1/generation?' + urlencode({'id': generation})
request = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + key})
record = {'retrieved_at': datetime.now(timezone.utc).isoformat(), 'operation': 'GET existing generation metadata; no model dispatch', 'generation_id': generation}
try:
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)['data']
    allowed = ('id', 'model', 'provider_name', 'total_cost', 'usage', 'tokens_prompt', 'tokens_completion', 'native_tokens_prompt', 'native_tokens_completion', 'native_tokens_reasoning', 'finish_reason', 'native_finish_reason', 'generation_time', 'latency', 'streamed', 'cancelled', 'created_at')
    record['status'] = 'FOUND'
    record['data'] = {k: data.get(k) for k in allowed if k in data}
except urllib.error.HTTPError as exc:
    record.update(status='UNAVAILABLE', http_status=exc.code)
except Exception as exc:
    record.update(status='UNAVAILABLE', error_type=type(exc).__name__)
(here / 'PROVIDER_COST_READBACK.json').write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(record, ensure_ascii=False, indent=2))
