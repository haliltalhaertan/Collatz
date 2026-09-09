import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
H=Path(__file__).resolve().parent;B=H.parent
c=json.loads((B/'research_sol_20260908/TASK_CONTRACT.json').read_text())
c.update(task_id='xub-maximum-gap-local-question',project_id='xub-gap-20260908',created_at=datetime.now(timezone.utc).isoformat())
c['primary_claim'].update(claim_id='GAP-LOWER-BOUND',statement='Find a rigorous bounded-step advance on the maximum-gap probability under the endpoint-only uniform composition law.',quantifiers='R=dn, n>=2, d grows like a fixed positive constant times log R, K/R approaches beta=log2(3)-1. B>0 fixed. No first-passage transfer claimed.')
roles=[('gap','Let U_1,...,U_n be totals of n disjoint d-coordinate blocks from a uniform weak composition of K into R=dn coordinates. Their mass is proportional to product_i binom(U_i+d-1,d-1), sum U_i=K. Put s_j=sum_(i<=j) U_i-jK/n, j=0,...,n-1. Delta is largest minus second-largest s_j, with zero for tied maxima. For fixed B>0, prove a positive uniform lower bound P(Delta>B)>=c_B>0 as d~a log R grows, or give a precise obstruction. Focus on one elementary injection/comparison of the exact weights, or a fully justified bound on the number of vertices within B of the maximum. No Brownian heuristic as proof, no unsupported theorem citations, no claim about Collatz. If unable, return the most specific missing finite inequality and any proved partial result. At most 650 words.')]
x=dict(c['agent_plan']['lanes'][0]);x.update(lane_id='gap',role=roles[0][1],independence_group='gap',max_completion_tokens=4000,max_tokens=20000,max_cost_usd=.08)
c['agent_plan'].update(lanes=[x],max_parallel_workers=1)
c['budget'].update(max_total_llm_calls=1,max_total_tokens=20000,max_tokens_per_lane=20000,max_total_cost_usd=.08,max_parallel_workers=1)
c['scope']['included']=['One bounded analytic question on exact weighted compositions.']
(H/'TASK_CONTRACT.json').write_text(json.dumps(c,indent=2))
(H/'FROZEN_HASHES.json').write_text(json.dumps({'TASK_CONTRACT.json':hashlib.sha256((H/'TASK_CONTRACT.json').read_bytes()).hexdigest()}))
previous=json.loads((B/'research_sol_20260908/BUDGET.json').read_text(encoding='utf-8-sig'))
assert previous['outstanding_openrouter_calls']==0 and previous['settled_cost_usd']+.08<=2
(H/'BUDGET.json').write_text(json.dumps({'cumulative_ceiling_usd':2,'previous_settled_usd':previous['settled_cost_usd'],'this_wave_reserved_usd':.08,'calls':1,'retries':0,'time_limit':None},indent=2))
runner=(B/'research_sol_20260908/run.py').read_text().replace("'calls':3,'max_cost_usd':.24","'calls':1,'max_cost_usd':.08").replace('xub-grid-review-20260908','xub-gap-20260908')
(H/'run.py').write_text(runner)
print('One small Sol low call reserved: $0.08; cumulative maximum $0.121352.')
