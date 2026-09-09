import pathlib, subprocess, json, hashlib, zipfile, re, base64
R=pathlib.Path(__file__).resolve().parent.parent
O=R/'research_full_sync_20260908'
tracked=set(subprocess.check_output(['git','ls-files','-z'],cwd=R).decode().split('\0'))
files=[]; excluded=[]; suspects=[]; redacted={}
secret=re.compile(rb'(?:sk-or-v1-[a-zA-Z0-9]{20,}|sk-[a-zA-Z0-9]{40,}|gh[pousr]_[a-zA-Z0-9]{25,}|-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----)')
for p in sorted(R.rglob('*')):
 if not p.is_file(): continue
 rel=p.relative_to(R).as_posix()
 reason=None
 if rel.startswith('research_full_sync_20260908/'): continue
 if '.git' in p.relative_to(R).parts or '__pycache__' in p.parts or p.suffix in ('.pyc','.pyo'): reason='git metadata or generated cache'
 elif 'private' in p.relative_to(R).parts or p.suffix in ('.key','.sqlite3','.guard','.flag') or p.name.startswith('.env'): reason='private runtime or authentication material'
 if reason: excluded.append({'path':rel,'reason':reason}); continue
 data=p.read_bytes()
 if secret.search(data):
  data=secret.sub(b'[REDACTED_CREDENTIAL]',data);redacted[rel]=data;excluded.append({'path':rel,'reason':'credential substring redacted in exported copy; original retained locally'})
 if p.suffix=='.zip' and rel not in tracked:
  with zipfile.ZipFile(p) as z:
   bad=[n for n in z.namelist() if n.endswith('.key') or '/private/' in n or secret.search(z.read(n))]
  if bad: excluded.append({'path':rel,'reason':'archive contains private runtime material; safe loose files retained'});continue
 files.append({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob_sha':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),'tracked':rel in tracked})
if suspects: raise SystemExit('Credential pattern matches in: '+json.dumps(suspects))
index='''# Collatz araştırması — tam çalışma kopyası, 8 Eylül 2026

Son araştırma: [Görünen sapma raporu](research_visible_defect_20260908/REPORT_TR.md) ve [kuyruk sıfırlarının sınıflandırması](research_visible_defect_20260908/ZERO_CLASSIFICATION.md).

Bu kayıt önceki kanonik arşivi, tüm yerel araştırma klasörlerini, kodları, denetimleri ve güvenli LLM deney çıktılarını birlikte saklar. Eski raporlar tarihsel kayıtlardır; sonraki düzeltmelerle birlikte okunmalıdır. Özellikle research_attack_round_20260908 ve research_reassessment_20260908 içindeki merkezleme düzeltmesini dikkate alın.

Collatz problemi açık. Sonlu hesaplar asimptotik bir teorem değildir. Son sonlu-cebir sonucu yüksek hassasiyetli tam görünmezlik uzayını belirtilen operatör için dışlar; katsayı alt sınırı veya Collatz yakınsaması vermez. Bu yedekleme yeni deney, model çağrısı veya kapalı aşama yetkilendirmesi değildir.

SNAPSHOT_MANIFEST.json dosya boyutlarını, SHA256 ve Git blob kimliklerini içerir. Kimlik doğrulama anahtarları, özel çalışma veritabanları ve geçici dosyalar EXCLUSIONS.json içinde gerekçeleriyle listelenmiştir; araştırma kaynakları değiştirilmemiştir.
'''
(R/'RESEARCH_INDEX_20260908.md').write_text(index,encoding='utf-8')
p=R/'RESEARCH_INDEX_20260908.md';d=p.read_bytes()
files=[f for f in files if f['path']!=p.name]+[{'path':p.name,'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'git_blob_sha':hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest(),'tracked':False}]
(O/'SNAPSHOT_MANIFEST.json').write_text(json.dumps(files,ensure_ascii=False,indent=2),encoding='utf-8')
(O/'EXCLUSIONS.json').write_text(json.dumps(excluded,ensure_ascii=False,indent=2),encoding='utf-8')
extra=[O/'SNAPSHOT_MANIFEST.json',O/'EXCLUSIONS.json',pathlib.Path(__file__)]
with zipfile.ZipFile(O/'COLLATZ_FULL_RESEARCH_20260908.zip','w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:z.writestr(f['path'],redacted.get(f['path'],(R/f['path']).read_bytes()))
 for p in extra:z.write(p,p.relative_to(R).as_posix())
with zipfile.ZipFile(O/'COLLATZ_FULL_RESEARCH_20260908.zip') as z:
 assert z.testzip() is None
 for f in files:assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
new=[R/f['path'] for f in files if not f['tracked']]+extra
entries=[];binary=[]
for p in new:
 rel=p.relative_to(R).as_posix();d=redacted.get(rel,p.read_bytes())
 try:content=d.decode('utf-8');assert '\0' not in content
 except (UnicodeDecodeError,AssertionError):binary.append({'path':rel,'content':base64.b64encode(d).decode()});continue
 entries.append({'path':rel,'mode':'100644','type':'blob','content':content})
(O/'tree_entries.json').write_text(json.dumps(entries,ensure_ascii=False),encoding='utf-8')
(O/'binary_entries.json').write_text(json.dumps(binary),encoding='utf-8')
d=(O/'COLLATZ_FULL_RESEARCH_20260908.zip').read_bytes()
receipt={'files':len(files)+len(extra),'source_files':len(files),'excluded':len(excluded),'new_text_files':len(entries),'new_binary_files':len(binary),'zip_bytes':len(d),'zip_sha256':hashlib.sha256(d).hexdigest(),'zip_md5':hashlib.md5(d).hexdigest(),'zip_crc_and_manifest':'PASS'}
(O/'PACKAGE_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8');print(json.dumps(receipt))
