import json,hashlib,sys,subprocess
from pathlib import Path
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent; BASE=HERE.parent
cases=[
('b1','Compute the standard Collatz trajectory starting at 6 up to its FIRST visit to 1, inclusive. Give the full list and the number of applications of T.', '[6,3,10,5,16,8,4,2,1]; 8 steps.'),
('b2','Let U(n)=(3n+1)/2^v2(3n+1) on positive odd n. Starting at 7, give the next three U-values and the three exact exponents v2.', 'Values 11,17,13; exponents 1,1,2.'),
('b3','For standard T, consider the three-step branch word odd,even,even. Derive T^3(n), specify the residue class of positive n making this word valid, and the stronger residue class making T^3(n) odd.', '(3n+1)/4; valid n=1 mod 4; odd output iff n=1 mod 8.'),
('b4','Can an odd-only Collatz cycle of exactly two U-steps have successive exact exponents k1=1,k2=2? Derive the cycle equation and decide whether a positive integer start exists.', 'Second iterate (9n+5)/8; 8n=9n+5 -> n=-5; no positive integer cycle.'),
('b5','In a HEURISTIC surrogate, k is independently sampled with P(k=j)=2^-j for j>=1 and the additive +1 is discarded, giving multiplier A=3/2^k. Compute E[A] and E[log A] exactly. Does negative expected log drift prove deterministic Collatz convergence? Explain.', 'E A=1; E log A=log3-2log2=log(3/4)<0. No: independence/distribution and neglected additive term are surrogate assumptions, not a proof for all deterministic orbits.'),
('b6','A program verifies that every integer 1<=n<=1000000 reaches 1. A proposed proof says: there are no counterexamples in that interval, therefore every positive integer reaches 1. Is the implication valid? State exactly what was proved and what is missing.', 'Invalid. Finite range only, assuming correct verification. Missing argument covering every larger integer; no universal theorem follows.'),
('b7','In a proposed Collatz occupation argument, a random count N_R is 0 with probability 1/2 and R with probability 1/2. For fixed lambda>0 compute E[N_R] and E[exp(-lambda N_R)]. Can a large mean by itself establish E[exp(-lambda N_R)]<=C/R with C independent of R?', 'Mean R/2; Laplace (1+exp(-lambda R))/2>=1/2, so no. Need lower-tail control. This is an abstract logical counterexample, not an actual Collatz orbit counterexample.'),
('b8','Assume H: every odd integer n>1 has a standard Collatz iterate T^k(n) that is a positive integer strictly below n. Prove that H would imply that every positive integer reaches 1. Distinguish proving the implication from proving H.', 'Strong induction or smallest counterexample: even reduces immediately; odd H reduces after finite steps to smaller convergent integer. Base1. H itself remains unproved here.')]
def save(name,x): (HERE/name).write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')
save('QUESTIONS.json',[{'id':i,'question':q} for i,q,a in cases])
save('ANSWER_KEY_FROZEN.json',{'created_at':datetime.now(timezone.utc).isoformat(),'scoring':'Per item 0 incorrect/missing, 1 correct core answer with substantive missing required detail, 2 all required facts and reasoning correct. All-or-nothing exact-match rate reported separately as items scoring 2. Manual principal grading; not a standardized or blind benchmark. Time/cost are secondary. No retries or question changes after dispatch.','answers':[{'id':i,'expected':a} for i,q,a in cases]})
c=json.loads((BASE/'llmlab_sol_low/TASK_CONTRACT.json').read_text(encoding='utf-8'))
c.update(task_id='collatz-sol-low-mini-benchmark-v1',project_id='collatz-sol-low-bench-20260908',parent_task_id='LOCAL_MINI_BENCHMARK',parent_state_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=BASE,text=True).strip(),created_at=datetime.now(timezone.utc).isoformat(),objective='Answer ONLY the question assigned in your lane role. This is a small educational Collatz benchmark, not an attempt to prove the conjecture. Put your answer and concise checkable justification in findings, at most 400 words. Do not claim a proof of an unproved premise. No tools. No elapsed time limit; finite token and cost limits.',inputs=[],input_manifests=[])
c['primary_claim']={'claim_id':'BENCHMARK-ANSWER','statement':'The response correctly solves its assigned exercise.','status_at_start':'OPEN','quantifiers':'Only the specified exercise; no universal Collatz claim unless explicitly conditional.','definitions':['Standard Collatz map on positive integers: T(n)=n/2 for even n, T(n)=3n+1 for odd n.','v2(m) is the largest k>=0 with 2^k dividing positive integer m.','log means natural logarithm.']}
c['scope']={'included':['Eight fixed educational questions and local logical checks.'],'excluded':['Canonical research state changes','Numerical searches','External tools','General proof claims beyond supplied assumptions']}
c['allowed_methods']=['Elementary arithmetic','Algebra','Conditional proof','Logical counterexample'];c['forbidden_methods']=['Inventing a proof of the Collatz conjecture'];c['stop_rules']=['BUDGET_EXHAUSTED','USER_STOP']
base=c['agent_plan']['lanes'][0];lanes=[]
for i,q,a in cases:
    x=dict(base);x.update(lane_id=i,role=q,input_paths=[],max_completion_tokens=1500,max_tokens=15000,max_cost_usd=.04,visible_inputs=['task_contract','definitions'])
    lanes.append(x)
c['agent_plan'].update(lanes=lanes,max_parallel_workers=4)
c['budget'].update(max_total_llm_calls=8,max_total_tokens=120000,max_tokens_per_lane=15000,max_total_cost_usd=.32,max_parallel_workers=4)
save('TASK_CONTRACT.json',c)
save('FROZEN_HASHES.json',{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ('TASK_CONTRACT.json','QUESTIONS.json','ANSWER_KEY_FROZEN.json')})
print('8 cases prepared; answer key is NOT a model input.')
