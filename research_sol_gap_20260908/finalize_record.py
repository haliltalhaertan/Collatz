"""Record completed advisory-call costs and analytic artifact provenance only."""
import json,hashlib
from pathlib import Path
from decimal import Decimal
H=Path(__file__).resolve().parent;B=H.parent
result=json.loads((H/'RESULT.json').read_text())
summary=json.loads((Path(result['artifact_root'])/'package/RUN_SUMMARY.json').read_text())
assert summary['usage']['provider_cost_complete']
previous=Decimal(str(json.loads((B/'research_sol_20260908/BUDGET.json').read_text(encoding='utf-8-sig'))['settled_cost_usd']))
cost=Decimal(str(summary['usage']['provider_cost_usd']));total=previous+cost
assert total<=2
budget={'cumulative_ceiling_usd':2,'previous_settled_usd':float(previous),'this_wave_actual_usd':float(cost),'cumulative_actual_usd':float(total),'remaining_usd':float(Decimal(2)-total),'outstanding_openrouter_calls':0,'provider_cost_complete':True,'no_time_cutoff':True,'retries':0}
(H/'BUDGET.json').write_text(json.dumps(budget,indent=2))
root=Path('C:/Users/MDP/Documents/ChatGPT/Collatz/research_manager/exploratory/sync_20260907')
paths=['xub/XUB_FIRST_PASSAGE_REDUCTION.md','xub/XUB_FIRST_PASSAGE_REPRESENTATION_AUDIT.md','xub_pair/XUB_PAIR_OCCUPATION_REDUCTION.md','xub_small_b/XUB_SYMBOL_BLOCK_THEOREM.md','xub_multiscale/XUB_MULTISCALE_MASTER_FINDINGS.md']
manifest={str(root/p):hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths}
(H/'SOURCE_HASHES.json').write_text(json.dumps(manifest,indent=2))
review={'model':'openai/gpt-5.6-sol','reasoning_effort':'low','calls':1,'contribution':'A valid alternative local donor injection: raise a chosen maximum using mass from its next coarse group. It reduces a uniform gap probability to a path-selected donor lower-tail estimate, left open. This is not the complete obstruction proof.','principal_assessment':'Exact weight ratio and injectivity checked. Useful bounded partial result; did not solve the requested uniform gap bound.','schema_issue':'INVALID_CLAIM_STATUS was recorded; claim retained OPEN. This does not replace mathematical review.','cost_usd':float(cost),'duration_seconds':summary['usage']['wall_seconds'],'package_verification':'Byte consistency and CRC passed for 22 members; not formal mathematical verification.'}
(H/'SOL_REVIEW.json').write_text(json.dumps(review,indent=2))
print(json.dumps(budget))
