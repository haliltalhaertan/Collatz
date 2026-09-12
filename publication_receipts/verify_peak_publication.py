"""Verify this research turn's Drive archives or immutable GitHub bytes."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request,urllib.parse,re,html,hashlib,json,zipfile,io,subprocess,sys
R=Path(__file__).resolve().parents[1]
def write(name,data):(R/'publication_receipts'/name).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
if sys.argv[1]=='drive':
 spec=json.loads((R/'publication_receipts/PEAK_UPLOADS_20260912.json').read_text())
 out=[]
 for file in spec['files']:
  fid=file['id']
  with urllib.request.urlopen('https://drive.google.com/uc?export=download&id='+fid,timeout=60) as response:data=response.read(100000001)
  if data.startswith(b'<!DOCTYPE html>'):
   page=data.decode();action=html.unescape(re.search(r'<form[^>]+action="([^"]+)"',page)[1])
   assert action=='https://drive.usercontent.google.com/download'
   fields=dict(re.findall(r'<input type="hidden" name="([^"]+)" value="([^"]*)"',page));assert fields['id']==fid
   with urllib.request.urlopen(action+'?'+urllib.parse.urlencode(fields),timeout=60) as response:data=response.read(100000001)
  assert len(data)==file['bytes'] and hashlib.sha256(data).hexdigest()==file['sha256'],fid
  with zipfile.ZipFile(io.BytesIO(data)) as z:assert z.testzip() is None
  out.append({**file,'byte_readback':'PASS','crc':'PASS'});print(json.dumps(out[-1]),flush=True)
 write('DRIVE_READBACK_PEAK_20260912.json',{'snapshot_commit':spec['snapshot_commit'],'folder_id':spec['folder_id'],'files':out})
elif sys.argv[1]=='github':
 commit=sys.argv[2]
 paths=['CURRENT_RESEARCH_STATE.json','CURRENT_ARCHIVE_BUILD.json','CURRENT_ARCHIVE_MEMBER_ROOT.json','START_HERE_CURRENT_HANDOFF.md','research_manager/RESEARCH_JOURNAL.jsonl','research_manager/decisions/PEAK_PEELING_2026-09-12.json','publication_receipts/DRIVE_READBACK_PEAK_20260912.json']
 paths += [p.relative_to(R).as_posix() for p in sorted((R/'research_peak_peeling_20260912').iterdir()) if p.is_file() and p.suffix in {'.md','.py','.json'}]
 def verify(path):
  url='https://raw.githubusercontent.com/haliltalhaertan/Collatz/'+commit+'/'+urllib.parse.quote(path)
  with urllib.request.urlopen(url,timeout=60) as response:data=response.read(100000001)
  expected=subprocess.check_output(['git','show',commit+':'+path],cwd=R);assert data==expected,path
  return {'path':path,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
 with ThreadPoolExecutor(max_workers=4) as pool:small=list(pool.map(verify,paths))
 print('Small files matched: '+str(len(small)),flush=True)
 archive=verify('Collatz_Research_Archive_CURRENT.zip')
 refs=subprocess.check_output(['git','ls-remote','origin','refs/heads/main','refs/heads/codex/integrated-research-20260912'],cwd=R).decode().splitlines()
 assert len(refs)==2 and all(line.split()[0]==commit for line in refs)
 out={'verified_commit':commit,'files':small,'canonical_archive':archive,'all_bytes_equal':True,'scope':'Receipt added after verified commit to avoid self-reference'}
 write('GITHUB_READBACK_PEAK_20260912.json',out);print(json.dumps({'commit':commit,'archive':archive,'all_bytes_equal':True}))
else:raise ValueError('Expected drive or github')
