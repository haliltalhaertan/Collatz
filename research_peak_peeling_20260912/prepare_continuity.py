"""One-time continuity update for the accepted finite peak-peeling audit."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1]
def write(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
j=R/'research_manager/RESEARCH_JOURNAL.jsonl';raw=j.read_bytes();lines=raw.splitlines()
event='ACTUAL_SPECTRAL_PEAK_PEELING_20260912'
assert all(json.loads(line)['event']!=event for line in lines),'Already recorded; do not replay'
now=datetime.now(timezone.utc).isoformat();base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R).decode().strip()
p=R/'CURRENT_RESEARCH_STATE.json';d=json.loads(p.read_text(encoding='utf-8'))
d['active_task']={'code':'CP20_EXPLORATORY_PEAK_PEELING_20260912','name':'Actual cyclic spectral peeling and energy-weighted tail control','stage':'ACCEPTED','objective':'Accept independently checked finite totals and analytic enclosure. Uniform W control, D2 and Collatz remain OPEN.','scientific_route_change':False}
d['active_integrator']={'holder':'codex-peak-peeling-20260912','scope':'User-authorized bounded exploratory continuation and dual publication; no sealed execution','base_commit':base,'acquired_at':now,'released_at':now,'status':'RELEASED'}
d['exploratory_research']['previous_continuation_report']=d['exploratory_research']['continuation_report']
d['exploratory_research']['continuation_report']='research_peak_peeling_20260912/REPORT_TR.md'
d['exploratory_research']['peak_audit']='research_peak_peeling_20260912/INDEPENDENT_AUDIT.md'
d['next_action']['instruction']='Study energy-weighted aggregate tails of actual normalized cyclic multipliers. Prove a uniform integrable tail bound, or identify obstruction; also retain the required W_flat bound. Fixed-L dominance and uniform W/W_flat have not been proved. Read the peak-peeling report and analytic review. Historical consumed B4 authorizations remain closed.'
decision_path='research_manager/decisions/PEAK_PEELING_2026-09-12.json'
decision={'schema':'COLLATZ_EXPLORATORY_DECISION_V1','event':event,'timestamp_utc':now,'source_commit':base,'accepted':'Finite exact W and W_flat at r5..20; independent scalar r12/r20 agreement; exact analytic peeling enclosure','not_established':['interval-certified FFT rankings','uniform W bound','D2','Collatz'],'next_action':d['next_action']['instruction'],'report':d['exploratory_research']['continuation_report'],'sealed_execution':False,'paid_calls':0}
write(R/decision_path,decision);d['documents']['current_exploratory_decision']=decision_path;d['updated_at']=now
row={'schema':'COLLATZ_RESEARCH_JOURNAL_V1','sequence':len(lines)+1,'previous_entry_sha256':hashlib.sha256(lines[-1]).hexdigest(),'event':event,'timestamp_utc':now,'task':d['active_task']['code'],'active_stage':'ACCEPTED','decision_sha256':hashlib.sha256((R/decision_path).read_bytes()).hexdigest(),'scientific_status':'Finite and analytic reductions only; W, D2 and Collatz OPEN','next_action':d['next_action']['instruction']}
with j.open('ab') as f:f.write((b'' if raw.endswith(b'\n') else b'\n')+json.dumps(row,ensure_ascii=False,separators=(',',':')).encode()+b'\n')
write(p,d)
h=R/'START_HERE_CURRENT_HANDOFF.md';old=h.read_text(encoding='utf-8');historical=old[old.index('## Historical B4 V2 closure'):]
intro='''# CURRENT HANDOFF — ACTUAL SPECTRAL PEAK PEELING, 2026-09-12

Current task: `CP20_EXPLORATORY_PEAK_PEELING_20260912`. Read `research_peak_peeling_20260912/REPORT_TR.md`, `ANALYTIC_REVIEW.md` and `INDEPENDENT_AUDIT.md`. The previous integration and W continuation reports remain valid within their stated scope.

Fixed panels r=5..20 were exhaustively evaluated. W and W_flat are exact rationals; independent scalar r12/r20 totals match. FFT pair shares and evaluated U_L bounds are diagnostic. Peeling gives a valid monotone enclosure, but fixed-L dominance and a uniform W/W_flat constant remain unproved. Next: actual source-energy-weighted multiplier tails, together with sufficient W_flat control. W, D2 and Collatz remain OPEN.

Publication artifacts: `CURRENT_ARCHIVE_BUILD.json`, `CURRENT_ARCHIVE_MEMBER_ROOT.json` and `publication_receipts/`. The deterministic canonical ZIP preserves historical members and includes the new exploratory package. External receipts are outside the frozen ZIP to avoid circular hashes.

The following B4 V2 closure is historical governance; it is not the current exploratory task or live authorization.

'''
h.write_text(intro+historical,encoding='utf-8',newline='\n')
print(json.dumps({'journal_rows':len(lines)+1,'event':event}))
