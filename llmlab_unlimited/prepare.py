import sys,json,shutil,hashlib,urllib.request
from pathlib import Path
from datetime import datetime,timezone
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
LAB=Path('C:/Users/MDP/Documents/Default Project/llm-lab')
fork=HERE/'runtime'
if fork.exists(): raise RuntimeError('Do not overwrite prepared runtime')
shutil.copytree(LAB/'lab',fork/'lab',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
changes={
'directed_contract.py': [('max_wall_seconds: int = Field(gt=0,','max_wall_seconds: int = Field(ge=0,'),('max_wall_seconds: int = Field(default=120, gt=0,','max_wall_seconds: int = Field(default=120, ge=0,')],
'directed_budget.py': [('self.elapsed() < self.limits.max_wall_seconds,','(self.limits.max_wall_seconds == 0 or self.elapsed() < self.limits.max_wall_seconds),')],
'directed_engine.py': [
('self.cancelled() or self.budget.elapsed() >= self.c.budget.max_wall_seconds','self.cancelled() or (self.c.budget.max_wall_seconds > 0 and self.budget.elapsed() >= self.c.budget.max_wall_seconds)'),
('if time.monotonic() - started >= lane.max_wall_seconds:', 'if lane.max_wall_seconds > 0 and time.monotonic() - started >= lane.max_wall_seconds:'),
('lane.max_wall_seconds - (time.monotonic() - started),','lane.max_wall_seconds - (time.monotonic() - started) if lane.max_wall_seconds else float("inf"),'),
('self.c.budget.max_wall_seconds - self.budget.elapsed(),','self.c.budget.max_wall_seconds - self.budget.elapsed() if self.c.budget.max_wall_seconds else float("inf"),'),
('if time.monotonic() - started > lane.max_wall_seconds and status == "COMPLETED":','if lane.max_wall_seconds > 0 and time.monotonic() - started > lane.max_wall_seconds and status == "COMPLETED":'),
('if self.budget.elapsed() >= self.c.budget.max_wall_seconds:', 'if self.c.budget.max_wall_seconds > 0 and self.budget.elapsed() >= self.c.budget.max_wall_seconds:')],
'directed_provider.py': [
('timeout=min(timeout, 60)', 'timeout=None if timeout == float("inf") else min(timeout, 60)'),
('        text, reasoning, finish, usage = "", "", None, {}', '        kwargs.setdefault("extra_body", {})["provider"] = {"max_price": {"prompt": lane.input_price_per_million, "completion": lane.output_price_per_million}, "sort": "price"}\n        text, reasoning, finish, usage = "", "", None, {}')]
}
for name,pairs in changes.items():
    p=fork/'lab'/name; s=p.read_text(encoding='utf-8')
    for old,new in pairs:
        assert s.count(old)==1,(name,old,s.count(old))
        s=s.replace(old,new)
    p.write_text(s,encoding='utf-8')
with urllib.request.urlopen('https://openrouter.ai/api/v1/models',timeout=30) as r: models=json.load(r)['data']
c=json.loads((HERE.parent/'llmlab_luna/TASK_CONTRACT.json').read_text(encoding='utf-8'))
c.update(task_id='cp20-xub-three-models-no-timeout-v1',project_id='cp20-xub-no-timeout-20260907',created_at=datetime.now(timezone.utc).isoformat())
c['objective']=c['objective'].replace('fresh Luna five-route pilot','fresh three-model five-route pilot')+' In this isolated runtime max_wall_seconds=0 explicitly means no elapsed-time limit. Token and cost limits remain active.'
specs=[('deepseek','deepseek/deepseek-v4-pro-0813',.66,1.98,.04),('glm','z-ai/glm-5.3-flash',.075,.25,.005),('hy4','tencent/hy4-preview',.834,2.501,.05)]
lanes=[]; catalog=[]
for base in c['agent_plan']['lanes']:
    for tag,model,p,q,cap in specs:
        m=next(x for x in models if x['id']==model)
        assert float(m['pricing']['prompt'])*1e6<=p+1e-9 and float(m['pricing']['completion'])*1e6<=q+1e-9
        assert 'high' in m['reasoning']['supported_efforts']
        x=dict(base); x.update(lane_id=base['lane_id'].replace('luna-',tag+'-'),model=model,independence_group='same-model-'+tag,max_wall_seconds=0,input_price_per_million=p,output_price_per_million=q,max_cost_usd=cap)
        lanes.append(x)
        if base==c['agent_plan']['lanes'][0]: catalog.append({k:m.get(k) for k in ('id','pricing','reasoning')})
c['agent_plan']['lanes']=lanes
c['budget'].update(max_total_llm_calls=15,max_total_tokens=450000,max_total_cost_usd=.475,max_wall_seconds=0)
def save(name,d): (HERE/name).write_text(json.dumps(d,indent=2,ensure_ascii=False),encoding='utf-8')
save('TASK_CONTRACT.json',c); save('MODEL_CATALOG_SNAPSHOT.json',catalog)
save('RUNTIME_MANIFEST.json',{str(p.relative_to(fork)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(fork.rglob('*.py'))})
print('Prepared isolated runtime: zero wall limit means disabled, provider SDK timeout None; cost/token caps retained.')
