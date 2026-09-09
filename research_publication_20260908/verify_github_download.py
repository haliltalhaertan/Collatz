import urllib.request,hashlib,json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote
H=Path(__file__).resolve().parent
commit='eb4818a2dbfa946d7752783d1722b02cb8520a72'
files=json.loads((H/'GITHUB_FILES.json').read_text(encoding='utf-8'))
def verify(item):
 path,content=item
 url=f'https://raw.githubusercontent.com/haliltalhaertan/Collatz/{commit}/{quote(path)}'
 with urllib.request.urlopen(url,timeout=60) as r: data=r.read(1000000)
 expected=content.encode('utf-8')
 assert data==expected,f'GitHub byte mismatch: {path}'
 return {'path':path,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
with ThreadPoolExecutor(max_workers=4) as pool: verified=list(pool.map(verify,files.items()))
receipt={'repository':'haliltalhaertan/Collatz','branch':'codex/coarse-occupation-20260908','commit':commit,'files_verified':len(verified),'all_bytes_match':True,'files':verified,'zip_snapshot_sha256':'491170f09c45b74ea4bc5c35979be3a791292dd40fc168f4c227499c7534b7b5'}
(H/'GITHUB_READBACK.json').write_text(json.dumps(receipt,indent=2))
print(json.dumps({k:v for k,v in receipt.items() if k!='files'}))
