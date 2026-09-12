"""One-time continuity update for reviewed affine shift recursion."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1]
def write(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
j=R/'research_manager/RESEARCH_JOURNAL.jsonl';raw=j.read_bytes();lines=raw.splitlines();event='AFFINE_SHIFT_RECURSION_20260912'
assert all(json.loads(line)['event']!=event for line in lines),'Already recorded; do not replay'
now=datetime.now(timezone.utc).isoformat();base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R).decode().strip()
p=R/'CURRENT_RESEARCH_STATE.json';d=json.loads(p.read_text(encoding='utf-8'))
d['active_task']={'code':'CP20_EXPLORATORY_AFFINE_SHIFT_20260912','name':'Exact affine joint parity recursion and integer fourth moments','stage':'ACCEPTED','objective':'Accept proved affine closure and single-shift computational bound, independently checked algorithms and finite results. Uniform W, D2 and Collatz remain OPEN.','scientific_route_change':False}
d['active_integrator']={'holder':'codex-affine-shift-20260912','scope':'User-authorized research with three agents, archive integration and dual publication; no sealed execution','base_commit':base,'acquired_at':now,'released_at':now,'status':'RELEASED'}
d['exploratory_research']['previous_continuation_report']=d['exploratory_research']['continuation_report']
d['exploratory_research']['continuation_report']='research_shift_recurrence_20260912/REPORT_TR.md'
d['exploratory_research']['shift_audit']='research_shift_recurrence_20260912/ADVERSARIAL.md'
d['exploratory_research']['reviewed_supplements']=['research_concentration_audit_20260912/REPORT_TR.md','research_galois_audit_20260912/REPORT_TR.md']
d['next_action']['instruction']='Use the exact affine shift recursion to seek weighted control of signed sibling differences and their mixed/dilated/reflected channel cross terms. One-shift poly(s)2^(s/2) computation and fast integer convolution are established; scalar global moment closure and uniform C_Y/W bounds are not. Retain actual source-filter alignment and W_flat targets. Historical consumed B4 authorizations remain closed.'
decision_path='research_manager/decisions/AFFINE_SHIFT_2026-09-12.json'
decision={'schema':'COLLATZ_EXPLORATORY_DECISION_V1','event':event,'timestamp_utc':now,'source_commit':base,'accepted':['Exact affine pair recursion','O(sqrt(s)2^(s/2)) single-shift state count, with polynomial arithmetic factors','Exact integer-convolution moment algorithm with no-carry certificate','Finite checks and explicit asymptotic limits'],'not_established':['Literature priority','Scalar global fourth-moment closure','Uniform C_Y or W bound','D2','Collatz'],'next_action':d['next_action']['instruction'],'report':d['exploratory_research']['continuation_report'],'sealed_execution':False,'paid_calls':0,'agents':['shift_recurrence','attack_shift','moment_algorithm']}
write(R/decision_path,decision);d['documents']['current_exploratory_decision']=decision_path;d['updated_at']=now
row={'schema':'COLLATZ_RESEARCH_JOURNAL_V1','sequence':len(lines)+1,'previous_entry_sha256':hashlib.sha256(lines[-1]).hexdigest(),'event':event,'timestamp_utc':now,'task':d['active_task']['code'],'active_stage':'ACCEPTED','decision_sha256':hashlib.sha256((R/decision_path).read_bytes()).hexdigest(),'scientific_status':'Proved computational reduction; uniform analytic bounds and Collatz OPEN','next_action':d['next_action']['instruction']}
with j.open('ab') as f:f.write((b'' if raw.endswith(b'\n') else b'\n')+json.dumps(row,ensure_ascii=False,separators=(',',':')).encode()+b'\n')
write(p,d)
h=R/'START_HERE_CURRENT_HANDOFF.md';old=h.read_text(encoding='utf-8');historical=old[old.index('## Historical B4 V2 closure'):]
intro='''# CURRENT HANDOFF — AFFINE SHIFT RECURSION, 2026-09-12

Current task: `CP20_EXPLORATORY_AFFINE_SHIFT_20260912`. Read `research_shift_recurrence_20260912/REPORT_TR.md`, `RECURRENCE.md`, `ADVERSARIAL.md` and `ALGORITHM.md`. Earlier concentration and Galois claim audits are now included in the canonical archive too.

Established: exact affine-pair closure; one specified shift uses at most O(sqrt(s)2^(s/2)) states, with additional polynomial/bit arithmetic costs; exact no-carry integer convolution computes finite fourth moments. Independent affine comparisons and direct moment comparisons pass. Larger timings are finite host measurements. Full fourth-moment scalar closure and uniform C_Y, W, D2, Collatz bounds remain OPEN.

Next: signed sibling-difference channels under the affine recursion, especially dilated/reflected cross terms, with actual source-filter and W_flat weights. A small cache is not a moment bound. Do not assume the filter is flat: exact (t,j)=(60,38) measurements reach C_Y approximately109.56 at s18.

Publication artifacts: `CURRENT_ARCHIVE_BUILD.json`, `CURRENT_ARCHIVE_MEMBER_ROOT.json`, `publication_receipts/`. Deterministic canonical ZIP preserves historical static members and incorporates all versioned exploratory supplements. External publication receipts remain outside it to avoid hash recursion.

The following B4 V2 closure is historical governance, not live authorization.

'''
h.write_text(intro+historical,encoding='utf-8',newline='\n')
print(json.dumps({'journal_rows':len(lines)+1,'event':event}))
