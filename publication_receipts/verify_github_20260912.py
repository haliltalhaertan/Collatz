"""Verify canonical GitHub publication by immutable-commit raw downloads."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote
import urllib.request,subprocess,hashlib,json,io,zipfile,sys
R=Path(__file__).resolve().parents[1]
commit=sys.argv[1]
paths=['CURRENT_RESEARCH_STATE.json','CURRENT_ARCHIVE_BUILD.json','CURRENT_ARCHIVE_MEMBER_ROOT.json','START_HERE_CURRENT_HANDOFF.md','research_manager/RESEARCH_JOURNAL.jsonl','research_manager/decisions/INTEGRATED_RESEARCH_MUSE_W_2026-09-12.json','publication_receipts/DRIVE_READBACK_20260912.json']
for folder in ['research_integration_20260912','research_w_continuation_20260912']:
 paths += [p.relative_to(R).as_posix() for p in sorted((R/folder).iterdir()) if p.is_file() and p.suffix in {'.md','.json','.py'}]
def verify(path):
 url='https://raw.githubusercontent.com/haliltalhaertan/Collatz/'+commit+'/'+quote(path)
 with urllib.request.urlopen(url,timeout=60) as response:data=response.read(100000001)
 expected=subprocess.check_output(['git','show',commit+':'+path],cwd=R)
 assert data==expected,path
 return {'path':path,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
with ThreadPoolExecutor(max_workers=4) as pool:small=list(pool.map(verify,paths))
print('Small canonical and research files matched:',len(small),flush=True)
archive=verify('Collatz_Research_Archive_CURRENT.zip')
build=json.loads((R/'CURRENT_ARCHIVE_BUILD.json').read_text())
assert archive['sha256']==build['archive_sha256']
refs=subprocess.check_output(['git','ls-remote','origin','refs/heads/main','refs/heads/codex/integrated-research-20260912'],cwd=R).decode().splitlines()
assert len(refs)==2 and all(x.split()[0]==commit for x in refs)
out={'schema':'COLLATZ_GITHUB_READBACK_V1','verified_commit':commit,'branches':['main','codex/integrated-research-20260912'],'canonical_archive':archive,'files':small,'all_bytes_equal':True,'scope':'Immutable commit raw-file readback; receipt is committed afterward to avoid self-reference.'}
(R/'publication_receipts/GITHUB_READBACK_20260912.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'commit':commit,'small_files':len(small),'archive_sha256':archive['sha256'],'all_bytes_equal':True}))
