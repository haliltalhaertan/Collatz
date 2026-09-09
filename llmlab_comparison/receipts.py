import sys,os,json,urllib.request,urllib.error
from pathlib import Path
from urllib.parse import urlencode
from datetime import datetime,timezone
sys.dont_write_bytecode=True
from dotenv import dotenv_values
here=Path(__file__).resolve().parent
key=os.environ.get('OPENROUTER_API_KEY') or dotenv_values(Path('C:/Users/MDP/Documents/Default Project/llm-lab/.env')).get('OPENROUTER_API_KEY')
tag=sys.argv[1]
records=[]
for lane in (here/tag/'runs').glob('*/directed/directed-*/lanes/*'):
    if len(sys.argv)>2 and lane.name!=sys.argv[2]: continue
    p=lane/('RESULT.json' if (lane/'RESULT.json').exists() else 'PARTIAL.json')
    if not p.exists(): continue
    d=json.loads(p.read_text(encoding='utf-8'))
    for attempt in d.get('provider_attempts',[]):
        gid=attempt.get('metadata',{}).get('id')
        if not gid: continue
        record={'lane':lane.name,'id':gid,'retrieved_at':datetime.now(timezone.utc).isoformat()}
        req=urllib.request.Request('https://openrouter.ai/api/v1/generation?'+urlencode({'id':gid}),headers={'Authorization':'Bearer '+key})
        try:
            with urllib.request.urlopen(req,timeout=30) as r: data=json.load(r)['data']
            record['data']={k:data.get(k) for k in ('model','provider_name','total_cost','native_tokens_prompt','native_tokens_completion','native_tokens_reasoning','finish_reason','generation_time','latency','cancelled')}
        except urllib.error.HTTPError as e: record['http_status']=e.code
        records.append(record)
name='PROVIDER_RECEIPTS'+('_INTERIM' if len(sys.argv)>2 else '')+'.json'
(here/tag/name).write_text(json.dumps(records,indent=2),encoding='utf-8')
print(json.dumps(records,indent=2))
