import urllib.request,hashlib,json,zipfile,io
from pathlib import Path
H=Path(__file__).resolve().parent
url='https://drive.google.com/uc?export=download&id=1Q87AE6EnNM6-vf4n9Ycbc5Tz035y9SIz'
with urllib.request.urlopen(url,timeout=60) as response:
 data=response.read(1000000)
expected=json.loads((H/'PACKAGE_RECEIPT.json').read_text())
assert len(data)==expected['bytes'],f'Unexpected response size: {len(data)}'
assert hashlib.sha256(data).hexdigest()==expected['sha256'],'Downloaded bytes differ'
with zipfile.ZipFile(io.BytesIO(data)) as z:
 assert z.testzip() is None
 manifest=json.loads(z.read('SHA256SUMS.json'))
 assert all(hashlib.sha256(z.read(p)).hexdigest()==h for p,h in manifest.items())
(H/'DRIVE_READBACK.zip').write_bytes(data)
receipt={'file_id':'1Q87AE6EnNM6-vf4n9Ycbc5Tz035y9SIz','url':'https://drive.google.com/file/d/1Q87AE6EnNM6-vf4n9Ycbc5Tz035y9SIz/view?usp=drivesdk','parent_id':'1Tg5P5wfILAgKYg-CiUmJS60kzdRFL2AU','bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'raw_byte_equality':'PASS','manifest_entries_verified':len(manifest)}
(H/'DRIVE_READBACK.json').write_text(json.dumps(receipt,indent=2))
print(json.dumps(receipt))
