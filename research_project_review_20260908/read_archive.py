"""Read selected archive documents as text without extracting executables."""
from pathlib import Path
import zipfile,io,hashlib,json,xml.etree.ElementTree as ET
P=Path(__file__).resolve().parent
archive=P.parent/'Collatz_Research_Archive_CURRENT.zip'
z=zipfile.ZipFile(archive)
rows=[]
for n in z.namelist():
    parts=n.split('/')
    selected=(len(parts)==3 and (parts[1].startswith('CP') or parts[1] in ('00_MASTER_INDEX','00_CURRENT_CHECKPOINTS')))
    selected=selected or ('MASTER_FINDINGS' in n and n.endswith('.md'))
    if not selected or not n.lower().endswith(('.txt','.md','.docx')):continue
    if 'PRE_AUDIT' in n or 'PROMPT' in n.upper() or 'Research Log' in n:continue
    data=z.read(n)
    if n.endswith('.docx'):
        dz=zipfile.ZipFile(io.BytesIO(data))
        root=ET.fromstring(dz.read('word/document.xml'))
        ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        txt='\n'.join(''.join(p.itertext()) for p in root.findall('.//w:p',ns))
    else:txt=data.decode('utf-8-sig',errors='replace')
    idx=len(rows)+1;out=f'source_{idx:03d}.txt'
    (P/out).write_text(txt,encoding='utf-8')
    rows.append(dict(id=idx,archive_member=n,sha256=hashlib.sha256(data).hexdigest(),text_file=out,chars=len(txt)))
(P/'ARCHIVE_SELECTION.json').write_text(json.dumps(dict(archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),archive_members=len(z.namelist()),selected=rows),ensure_ascii=False,indent=2),encoding='utf-8')
for r in rows:print(r['id'],r['chars'],r['archive_member'].split('/')[-1])
