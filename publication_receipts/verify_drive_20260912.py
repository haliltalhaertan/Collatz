"""Byte readback of the two explicitly published Drive archives."""
from pathlib import Path
import urllib.request,urllib.parse,re,html,hashlib,json,zipfile,io
R=Path(__file__).resolve().parents[1]
files=[('15g7c7z-lfmpLNNcx5na6mIhXziJIepBk',93418973,'426d1a7abbb4800c69b9b3ce80dc9dedf274b342c0ad186d2c2c79c9c3fd1037'),('1lHIdMhRvQ851CUmhTp4_bO9TRdM1T1P6',32676136,'9f356e3a6f8b92e8e8f787501f7c460260252d7ca6daa05e9aef69246ff88b40')]
out=[]
for fid,size,expected in files:
 with urllib.request.urlopen('https://drive.google.com/uc?export=download&id='+fid,timeout=60) as r:data=r.read(100000001)
 if data.startswith(b'<!DOCTYPE html>'):
  page=data.decode();action=html.unescape(re.search(r'<form[^>]+action="([^"]+)"',page)[1])
  assert action=='https://drive.usercontent.google.com/download'
  fields=dict(re.findall(r'<input type="hidden" name="([^"]+)" value="([^"]*)"',page))
  assert fields['id']==fid
  with urllib.request.urlopen(action+'?'+urllib.parse.urlencode(fields),timeout=60) as r:data=r.read(100000001)
 assert len(data)==size,(fid,len(data))
 assert hashlib.sha256(data).hexdigest()==expected,fid
 with zipfile.ZipFile(io.BytesIO(data)) as z:assert z.testzip() is None
 out.append({'id':fid,'bytes':len(data),'sha256':expected,'byte_readback':'PASS','crc':'PASS'})
 print(json.dumps(out[-1]),flush=True)
(R/'publication_receipts/DRIVE_READBACK_20260912.json').write_text(json.dumps({'files':out,'folder_id':'1Tg5P5wfILAgKYg-CiUmJS60kzdRFL2AU','snapshot_commit':'b98b1cad85ab07e33f2a8b9c1359c1782748944f'},indent=2)+'\n',encoding='utf-8',newline='\n')
