"""One-time continuity update for the cross-term identities and their limits."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1]
def write(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
j=R/'research_manager/RESEARCH_JOURNAL.jsonl';raw=j.read_bytes();lines=raw.splitlines();event='CROSS_TERM_REFLECTION_20260912'
assert all(json.loads(line)['event']!=event for line in lines),'Already recorded; do not replay'
now=datetime.now(timezone.utc).isoformat();base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R).decode().strip()
p=R/'CURRENT_RESEARCH_STATE.json';d=json.loads(p.read_text(encoding='utf-8'))
d['active_task']={'code':'CP20_EXPLORATORY_CROSS_TERMS_20260912','name':'Exact even cross-term closure and reflection decomposition','stage':'ACCEPTED','objective':'Accept E=NB, positive reflection decomposition and one-step factor-two bound. Scalar iteration is no better than the known trivial bound; uniform W/D2/Collatz remain OPEN.','scientific_route_change':False}
d['active_integrator']={'holder':'codex-cross-terms-20260912','scope':'User-authorized three-agent continuation, exact finite probes and archive/publication; no sealed execution','base_commit':base,'acquired_at':now,'released_at':now,'status':'RELEASED'}
d['exploratory_research']['previous_continuation_report']=d['exploratory_research']['continuation_report']
d['exploratory_research']['continuation_report']='research_cross_terms_20260912/REPORT_TR.md'
d['exploratory_research']['cross_term_audit']='research_cross_terms_20260912/INDEPENDENT.md'
d['next_action']['instruction']='Retain the mixed overlap NB and reflection-positive component N_plus in a weighted affine-channel estimate. Exact E=NB and S=N0+N1+6N_plus+2N_minus are proved; S_even<=S<=2S_even is local and S_even is not W_flat. Naive scalar moment iteration never beats the trivial conjugate-pair bound. Seek growing-family weighted control or a precise obstruction. W_flat and actual source alignment remain open; consumed B4 authorizations remain closed.'
decision_path='research_manager/decisions/CROSS_TERMS_2026-09-12.json'
decision={'schema':'COLLATZ_EXPLORATORY_DECISION_V1','event':event,'timestamp_utc':now,'source_commit':base,'accepted':['Exact even cross=NB','Reflection decomposition and nonnegative combined cross contribution','One-step S_even<=S<=2S_even','Scalar iteration no better than trivial bound','247 main vs independent rows exactly matched'],'not_established':['Uniform W/W_flat<=2','Uniform strict correlation gap','Global mixed-channel closure','W','D2','Collatz'],'next_action':d['next_action']['instruction'],'report':d['exploratory_research']['continuation_report'],'sealed_execution':False,'paid_calls':0,'agents':['cross_identity','cross_attack','cross_independent']}
write(R/decision_path,decision);d['documents']['current_exploratory_decision']=decision_path;d['updated_at']=now
row={'schema':'COLLATZ_RESEARCH_JOURNAL_V1','sequence':len(lines)+1,'previous_entry_sha256':hashlib.sha256(lines[-1]).hexdigest(),'event':event,'timestamp_utc':now,'task':d['active_task']['code'],'active_stage':'ACCEPTED','decision_sha256':hashlib.sha256((R/decision_path).read_bytes()).hexdigest(),'scientific_status':'Exact local identities; naive scalar bound route insufficient; uniform targets OPEN','next_action':d['next_action']['instruction']}
with j.open('ab') as f:f.write((b'' if raw.endswith(b'\n') else b'\n')+json.dumps(row,ensure_ascii=False,separators=(',',':')).encode()+b'\n')
write(p,d)
h=R/'START_HERE_CURRENT_HANDOFF.md';old=h.read_text(encoding='utf-8');historical=old[old.index('## Historical B4 V2 closure'):]
intro='''# CURRENT HANDOFF — CROSS-TERM REFLECTION IDENTITIES, 2026-09-12

Current task: `CP20_EXPLORATORY_CROSS_TERMS_20260912`. Read `research_cross_terms_20260912/REPORT_TR.md`, `IDENTITIES.md`, `ATTACK.md` and `INDEPENDENT.md`. Prior affine recursion and exact-moment tools remain valid.

Proved: even cross term E=NB; S=N0+N1+6N_plus+2N_minus; combined cross contribution nonnegative; S_even<=S<=2S_even. S_even is NOT W_flat. Actual filters saturate Cauchy, so no unconditional strict correlation gap is available. Repeated scalar moment bounds never improve the known trivial conjugate-pair estimate.

Next: preserve mixed overlap and reflection projection in a weighted affine-channel recurrence; control growing actual families or find a scoped obstruction. Uniform W, D2 and Collatz remain OPEN. Exact finite tables and approximate decimal renderings are distinguished in the report. The independent scalar audit matches all247 main small cases.

Publication: `CURRENT_ARCHIVE_BUILD.json`, `CURRENT_ARCHIVE_MEMBER_ROOT.json`, `publication_receipts/`. The deterministic ZIP preserves historical members and includes this reviewed continuation. External receipts remain outside it to avoid recursive hashes.

The following B4 V2 closure is historical governance, not live authorization.

'''
h.write_text(intro+historical,encoding='utf-8',newline='\n')
print(json.dumps({'journal_rows':len(lines)+1,'event':event}))
