"""Prepare the explicitly authorized integration transaction; no sealed run."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
state=R/'CURRENT_RESEARCH_STATE.json'
d=json.loads(state.read_text(encoding='utf-8'))
now=datetime.now(timezone.utc).isoformat()
base='2461573739147763eb011faf03c344370a184d69'
merge='c10ac750910a2b4736424bd1528c8321f18c8289'
if 'historical_governed_active_task' not in d:d['historical_governed_active_task']=d['active_task']
d['active_task']={'code':'CP20_EXPLORATORY_INTEGRATION_W_20260912','name':'Integrated Muse remediation and actual filtered source energy research','stage':'ACCEPTED','objective':'Accept audited implementation and interpretation repairs; preserve exploratory research and continue quantitative W control. Acceptance describes this integration, not a proof of the open asymptotic bound.','scientific_route_change':False}
d['active_integrator']={'holder':'codex-integrated-research-20260912','scope':'User-authorized snapshot/audit integration, deterministic archive and dual publication, and bounded exploratory W continuation; no consumed B4 execution or new seal.','base_commit':base,'acquired_at':now,'released_at':now,'status':'RELEASED'}
d['continuity']['repository_branch']='main'
d['continuity']['minimum_required_commit']=merge
d['exploratory_research']={'snapshot_commit':'b49f630808b72e40a9da47df89466b3e838fd439','muse_audit_commit':'dc43110d5ae7672aa8a08fecfe95518b20e662c9','integration_merge_commit':merge,'audit_review':'research_integration_20260912/AUDIT_REVIEW.md','latest_prior_report':'research_visible_defect_20260908/REPORT_TR.md','continuation_report':'research_w_continuation_20260912/PROPOSAL.md','W_status':'OPEN','D2_status':'OPEN','collatz_status':'OPEN','scope':'Exploratory evidence is archived with its original epistemic labels; not retroactive acceptance of every historical claim.'}
d['next_action']={'authorization_available':False,'authorized_stage':None,'executed_in_this_transaction':False,'instruction':'Continue separately authorized exploratory analysis of actual high-conductor source-tail alignment sufficient to bound W. Read the 2026-09-12 integration and W continuation reports first. No asymptotic W/D2 bound has been proved. The historical B4 V1/V2 authorizations remain consumed and closed.','prohibited':['reuse or execution of consumed B4 V1/V2 tuples','promote finite checks to asymptotic bounds','use invalid V1 mathematical drafts','claim Collatz proved']}
d['documents']['current_integration_decision']='research_manager/decisions/INTEGRATED_RESEARCH_MUSE_W_2026-09-12.json'
d['updated_at']=now
decision={'schema':'COLLATZ_INTEGRATION_DECISION_V1','date':'2026-09-12','user_authorization':'evet bunlari yap ve arastirmalarimiza kaldigimiz yerden devam edelim','source_commits':d['exploratory_research'],'accepted_scope':'Verified code and interpretation remediation; snapshot preservation. Original exploratory reports are evidence, not blanket theorem acceptance.','historical_sealed_programs':'UNCHANGED; no execution or reseal','next_action':d['next_action']['instruction']}
write(R/d['documents']['current_integration_decision'],decision)
j=R/'research_manager/RESEARCH_JOURNAL.jsonl';raw=j.read_bytes();lines=raw.splitlines()
if json.loads(lines[-1])['event']!='MUSE_SNAPSHOT_INTEGRATION_20260912':
 row={'schema':'COLLATZ_RESEARCH_JOURNAL_V1','sequence':len(lines)+1,'previous_entry_sha256':hashlib.sha256(lines[-1]).hexdigest(),'event':'MUSE_SNAPSHOT_INTEGRATION_20260912','timestamp_utc':now,'task':d['active_task']['code'],'active_stage':'ACCEPTED','decision_sha256':sha(R/d['documents']['current_integration_decision']),'source_merge':merge,'scientific_status':'Collatz, W and D2 remain OPEN; no sealed execution','next_action':d['next_action']['instruction']}
 with j.open('ab') as f:f.write((b'' if raw.endswith(b'\n') else b'\n')+json.dumps(row,ensure_ascii=False,separators=(',',':')).encode()+b'\n')
write(state,d)
print(json.dumps({'state_updated':True,'journal_rows':len(j.read_bytes().splitlines())}))
