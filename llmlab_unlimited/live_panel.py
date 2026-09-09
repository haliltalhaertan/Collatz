import json,time
from pathlib import Path
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
BASE=Path(__file__).resolve().parent
RUN=BASE/'runs/cp20-xub-no-timeout-20260907/directed/directed-53f918e671c64edb9c8a73dce44dab8a'
C=json.loads((BASE/'TASK_CONTRACT.json').read_text(encoding='utf-8'))
cache={}
def read(p):
    try:
        d=json.loads(p.read_text(encoding='utf-8')); cache[str(p)]=d; return d
    except (OSError,ValueError): return cache.get(str(p),{})
def snapshot():
    r=read(RUN/'runtime.json'); lanes=[]
    for lane in C['agent_plan']['lanes']:
        root=RUN/'lanes'/lane['lane_id']; p=read(root/'PARTIAL.json'); f=read(root/'RESULT.json')
        attempts=f.get('provider_attempts') or p.get('provider_attempts') or []
        a=attempts[-1] if attempts else {}; usage=f.get('usage') or a.get('usage') or {}
        public=f.get('public_findings') or p.get('content') or ''
        if not isinstance(public,str): public=json.dumps(public,ensure_ascii=False)
        # Whitelisted public content and scalar telemetry only. Never serve raw files,
        # hidden reasoning, reasoning_details, prompts, credentials or signed secrets.
        lanes.append({'id':lane['lane_id'],'model':lane['model'],'status':f.get('status') or ('Yanıt geliyor' if public else 'Düşünüyor' if attempts else 'Sırada'),
            'provider':a.get('metadata',{}).get('provider','—'),'public':public,
            'reasoning_chars':len(p.get('reasoning') or ''),'reasoning_tokens':usage.get('reasoning_tokens'),
            'completion_tokens':usage.get('completion_tokens'),'cost':usage.get('cost_usd'),
            'age':round(time.time()-(root/'PARTIAL.json').stat().st_mtime,1) if (root/'PARTIAL.json').exists() else None})
    u=r.get('usage',{})
    return {'status':r.get('status','Bekleniyor'),'calls':u.get('calls',0),'cost':u.get('provider_cost_usd'),
        'cost_complete':u.get('provider_cost_complete',False),'seconds':u.get('wall_seconds',0),
        'complete':len(r.get('completed_lanes',[])),'lanes':lanes}
HTML='''<!doctype html><html lang="tr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>LLM Lab · Canlı deneme</title><style>
*{box-sizing:border-box}body{margin:0;background:#0b1220;color:#e6edf7;font:15px system-ui,sans-serif}main{max-width:1450px;margin:auto;padding:28px}h1{font-size:28px;margin:0 0 8px}header p{color:#9dadc4;margin:8px 0 20px;line-height:1.6}.pulse{display:inline-block;width:9px;height:9px;background:#4ee2b1;border-radius:50%;margin-right:8px}.stats{display:flex;gap:12px;flex-wrap:wrap;margin:22px 0}.stat{background:#152137;border:1px solid #283853;border-radius:12px;padding:15px 22px;min-width:150px}.stat strong{font-size:23px;display:block;margin-top:5px}.muted,small{color:#9dadc4}.toolbar{display:flex;align-items:center;gap:18px;margin-bottom:20px;flex-wrap:wrap}select,button{padding:9px 14px;border-radius:8px;background:#17253b;color:#e6edf7;border:1px solid #3a4e6c}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(350px,1fr));gap:16px}.card{border:1px solid #2a3a54;border-top:3px solid #4ee2b1;background:#111d30;border-radius:12px;overflow:hidden}.card[data-model="glm"]{border-top-color:#b29aff}.card[data-model="hy4"]{border-top-color:#ffa96b}.head{padding:18px;border-bottom:1px solid #29384f}.title{font-weight:700;font-size:18px}.badge{display:inline-block;margin:10px 0;padding:4px 9px;border-radius:20px;background:#22344f;font-size:12px}.metrics{display:flex;gap:14px;flex-wrap:wrap;font-size:12px;color:#b8c7da}.answer{padding:18px;white-space:pre-wrap;overflow-wrap:anywhere;max-height:430px;overflow:auto;line-height:1.6;font-size:13px;font-family:ui-monospace,Consolas,monospace}.empty{color:#90a2bb;font-family:system-ui}.error{color:#ffb2b2}footer{color:#9dadc4;margin-top:25px;line-height:1.6;font-size:13px}label{cursor:pointer}</style>
<main><header><h1><span class="pulse"></span>LLM Lab · Canlı deneme</h1><p>DeepSeek V4 Pro 0813 · GLM 5.3 Flash · Tencent Hy4 Preview<br>Süre sınırı yok · 15 yaklaşım · 4 eşzamanlı çağrı · toplam bütçe 0,475 $</p></header>
<div class="stats"><div class="stat">Durum<strong id="status">Bağlanıyor</strong></div><div class="stat">Tamamlanan<strong id="complete">—</strong></div><div class="stat">Çağrı<strong id="calls">—</strong></div><div class="stat">Geçen süre<strong id="elapsed">—</strong></div><div class="stat">Bildirilen ücret<strong id="cost">—</strong><small id="costnote"></small></div></div>
<div class="toolbar"><select id="filter" aria-label="Model seç"><option value="all">Tüm modeller</option><option value="deepseek">DeepSeek</option><option value="glm">GLM</option><option value="hy4">Tencent Hy4</option></select><label><input type="checkbox" id="active"> Sıradakileri gizle</label><button id="pause">Görünümü duraklat</button><small id="connection" aria-live="polite"></small></div><div class="grid" id="grid"></div>
<footer>Her 2 saniyede yenilenir. Düşünme karakter sayısı yalnızca akışın ilerlediğini gösterir; token sayısı veya matematiksel başarı ölçüsü değildir. Ham iç düşünme dökümü gösterilmez. Nihai yanıt bölümü modelin yayımladığı cevap akışıdır; tamamlanmamış metin değişebilir. Ücret bilgisi sağlayıcıdan geç gelebilir. Görünümü duraklatmak model çağrılarını durdurmaz.</footer></main>
<script>
const $=id=>document.getElementById(id), names={counting:'Kesin sayım',cycles:'Çevrim / ballot','low-state':'Düşük durumlar',resonance:'Rezonans',refutation:'Karşıörnek arama'}, cards=new Map();let paused=false,last=null;
const nf=new Intl.NumberFormat('tr-TR'), money=x=>x==null?'—':x.toFixed(5)+' $';
function draw(s){last=s;$('status').textContent=s.status;$('complete').textContent=s.complete+' / 15';$('calls').textContent=s.calls;$('elapsed').textContent=Math.floor(s.seconds/60)+' dk '+Math.floor(s.seconds%60)+' sn';$('cost').textContent=money(s.cost);$('costnote').textContent=s.cost_complete?'Tüm ücretler geldi':'Kesin toplam değil';
for(const l of s.lanes){const group=l.id.split('-')[0];let el=cards.get(l.id);if(!el){el=document.createElement('article');el.className='card';el.dataset.model=group;el.innerHTML='<div class="head"><div class="title"></div><small class="route"></small><br><span class="badge"></span><div class="metrics"></div></div><div class="answer"></div>';cards.set(l.id,el);$('grid').append(el)}
el.hidden=($('filter').value!=='all'&&$('filter').value!==group)||($('active').checked&&l.status==='Sırada');el.querySelector('.title').textContent={deepseek:'DeepSeek V4 Pro',glm:'GLM 5.3 Flash',hy4:'Tencent Hy4 Preview'}[group];el.querySelector('.route').textContent=(names[l.id.slice(group.length+1)]||l.id)+' · '+l.provider;el.querySelector('.badge').textContent=l.status;el.querySelector('.metrics').textContent='Düşünme akışı: '+nf.format(l.reasoning_chars)+' karakter · '+(l.reasoning_tokens==null?'token bilgisi bekleniyor':nf.format(l.reasoning_tokens)+' düşünme tokenı')+' · '+money(l.cost)+' · son veri: '+(l.age==null?'—':l.age+' sn önce');
const a=el.querySelector('.answer'), near=a.scrollHeight-a.scrollTop-a.clientHeight<40;const value=l.public||'Nihai yanıt henüz gelmedi. Düşünme akışının ilerlemesini yukarıdaki sayaçtan izleyebilirsin.';if(a.textContent!==value){a.textContent=value;if(near)a.scrollTop=a.scrollHeight}a.classList.toggle('empty',!l.public)}}
async function tick(){if(paused)return;try{const r=await fetch('/state',{cache:'no-store'});if(!r.ok)throw Error(r.status);draw(await r.json());$('connection').textContent='Son güncelleme: '+new Date().toLocaleTimeString('tr-TR');$('connection').className=''}catch(e){$('connection').textContent='Bağlantı kurulamadı; tekrar deneniyor.';$('connection').className='error'}}
$('pause').onclick=()=>{paused=!paused;$('pause').textContent=paused?'Canlı görünümü sürdür':'Görünümü duraklat';if(!paused)tick()};$('filter').onchange=$('active').onchange=()=>{if(last)draw(last)};tick();setInterval(tick,2000);
</script></html>'''
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/state': payload=json.dumps(snapshot(),ensure_ascii=False).encode(); kind='application/json'
        elif self.path=='/': payload=HTML.encode(); kind='text/html'
        else: self.send_error(404); return
        self.send_response(200);self.send_header('Content-Type',kind+'; charset=utf-8');self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff');self.end_headers();self.wfile.write(payload)
    def log_message(self,*args): pass
if __name__=='__main__':
    print('Live panel: http://127.0.0.1:8768',flush=True)
    ThreadingHTTPServer(('127.0.0.1',8768),Handler).serve_forever()
