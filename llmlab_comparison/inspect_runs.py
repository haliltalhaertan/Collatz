import json,sys
from pathlib import Path
here=Path(__file__).resolve().parent
for tag in ('deepseek','glm_capped'):
    for folder in (here/tag/'runs').glob('*/directed/directed-*'):
        r=json.loads((folder/'runtime.json').read_text(encoding='utf-8'))
        u=r.get('usage',{})
        out={'model':tag,'status':r.get('status'),'usage':{k:u.get(k) for k in ('calls','wall_seconds','provider_cost_usd','provider_cost_complete','provider_cost_upper_bound_usd')},'lanes':{}}
        for lane in (folder/'lanes').iterdir():
            final=(lane/'RESULT.json').exists()
            p=lane/('RESULT.json' if final else 'PARTIAL.json')
            if not p.exists(): continue
            try: d=json.loads(p.read_text(encoding='utf-8'))
            except json.JSONDecodeError: continue
            x={k:d.get(k) for k in ('status','usage')}
            x['public_chars']=len(d.get('public_findings','') or d.get('content',''))
            if final or '--partial' in sys.argv:
                x['public_findings']=d.get('public_findings') or d.get('content')
                x['first_missing_step']=d.get('first_missing_step')
            out['lanes'][lane.name]=x
        (here/tag/'PUBLIC_REVIEW.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
        if '--brief' in sys.argv:
            for x in out['lanes'].values():
                x.pop('public_findings',None); x.pop('first_missing_step',None)
        print(json.dumps(out,ensure_ascii=False,indent=2))

