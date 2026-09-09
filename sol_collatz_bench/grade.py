import json,hashlib,statistics
from pathlib import Path
HERE=Path(__file__).resolve().parent
for n,h in json.loads((HERE/'FROZEN_HASHES.json').read_text()).items(): assert hashlib.sha256((HERE/n).read_bytes()).hexdigest()==h
r=json.loads((HERE/'RESULT.json').read_text()); root=Path(r['artifact_root'])
runtime=json.loads((root/'runtime.json').read_text())
notes={
'b1':'Full trajectory and 8 steps correct; each map application verified.',
'b2':'22=2*11, 34=2*17, 52=4*13; all values and exact valuations correct.',
'b3':'Branch validity n=1 mod4, odd endpoint n=1 mod8, affine expression correct.',
'b4':'Elimination gives 8n=9n+5 and n=-5, excluding positive starts; exact conditions correctly used.',
'b5':'Both convergent sums correct; independence and discarded additive term identified as surrogate assumptions; no universal proof claim.',
'b6':'Rejects finite-to-universal inference and identifies the uncovered range.',
'b7':'Both expectations correct and lower bound 1/2 rules out C/R. Remains within the supplied abstract count example; does not claim an actual Collatz counterexample.',
'b8':'Strong induction handles base, even and odd cases; explicitly distinguishes H from its conditional consequence.'}
rows=[]
for i,note in notes.items():
    d=json.loads((root/'lanes'/i/'RESULT.json').read_text(encoding='utf-8'))
    assert d['status']=='COMPLETED'
    rows.append({'id':i,'score':2,'max_score':2,'grading_note':note,'public_answer':d['public_findings'],'usage':d['usage']})
u=runtime['usage']; out={'method':'Manual principal grading against pre-dispatch frozen answer key; grade.py records reviewed judgments, not an independent automated semantic grader.','score':16,'maximum':16,'fully_correct':8,'questions':8,'provider_cost_usd':u['provider_cost_usd'],'provider_cost_complete':u['provider_cost_complete'],'wall_seconds':u['wall_seconds'],'median_call_seconds':statistics.median(x['usage']['wall_seconds'] for x in rows),'rows':rows}
(HERE/'SCORES.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
