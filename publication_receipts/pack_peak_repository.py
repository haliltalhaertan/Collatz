"""Export committed repository files except the separately published large ZIP."""
from pathlib import Path
import subprocess,json,hashlib,zipfile
R=Path(__file__).resolve().parents[1]
O=R/'_verification';O.mkdir(exist_ok=True)
commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R).decode().strip()
raw=subprocess.check_output(['git','ls-tree','-rz',commit],cwd=R)
entries=[]
for row in raw.split(b'\0'):
 if not row:continue
 meta,path=row.split(b'\t',1);mode,kind,obj=meta.split()
 if kind!=b'blob':continue
 path=path.decode('utf-8')
 if path=='Collatz_Research_Archive_CURRENT.zip':continue
 entries.append((path,obj.decode()))
manifest=[];dest=O/'COLLATZ_PEAK_REPOSITORY_20260912.zip'
# One cat-file subprocess avoids a Windows launch for each of 1700 files.
process=subprocess.Popen(['git','cat-file','--batch'],cwd=R,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for path,obj in entries:
  process.stdin.write((obj+'\n').encode());process.stdin.flush()
  header=process.stdout.readline().decode().split();size=int(header[2])
  data=process.stdout.read(size);assert process.stdout.read(1)==b'\n'
  assert len(data)==size
  zi=zipfile.ZipInfo(path,date_time=(1980,1,1,0,0,0));zi.compress_type=zipfile.ZIP_DEFLATED
  z.writestr(zi,data)
  manifest.append({'path':path,'git_blob':obj,'bytes':size,'sha256':hashlib.sha256(data).hexdigest()})
 z.writestr('REPOSITORY_EXPORT_MANIFEST.json',json.dumps({'commit':commit,'separate_archive':'Collatz_Research_Archive_CURRENT.zip','files':manifest},ensure_ascii=False,indent=2))
process.stdin.close();assert process.wait()==0
with zipfile.ZipFile(dest) as z:assert z.testzip() is None
d=dest.read_bytes();record={'commit':commit,'zip':str(dest),'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'files':len(entries)+1,'separate_archive':json.loads((R/'CURRENT_ARCHIVE_BUILD.json').read_text())['archive_sha256']}
(O/'PEAK_REPOSITORY_EXPORT.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record))
