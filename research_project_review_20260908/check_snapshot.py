"""Read-only integrity checks; does not substitute for canonical branch validation."""
from pathlib import Path
import hashlib,json,zipfile,subprocess
P=Path(__file__).resolve().parent; R=P.parent
sha=lambda b:hashlib.sha256(b).hexdigest()
s=json.loads((R/'CURRENT_RESEARCH_STATE.json').read_text())
b=json.loads((R/'CURRENT_ARCHIVE_BUILD.json').read_text())
zpath=R/b['archive'];z=zipfile.ZipFile(zpath)
checks={
 'archive_hash':sha(zpath.read_bytes())==b['archive_sha256'],
 'archive_size':zpath.stat().st_size==b['zip_bytes'],
 'archive_members':len(z.infolist())==b['member_count'],
 'archive_crc':z.testzip() is None,
}
files=[dict(path=row['path'],ok=sha((R/row['path']).read_bytes())==row['sha256']) for row in s['integrity']['repository_files']]
members=[]
for row in s['integrity']['archive_members']:
    exists=row['path'] in z.namelist()
    rec=dict(path=row['path'],exists=exists,ok=exists and sha(z.read(row['path']))==row['sha256'])
    try: candidate=row['path'].encode('cp1252').decode('utf-8')
    except (UnicodeEncodeError,UnicodeDecodeError): candidate=None
    if candidate and candidate in z.namelist():
        rec.update(diagnostic_decoded_path=candidate,diagnostic_decoded_hash_match=sha(z.read(candidate))==row['sha256'])
    members.append(rec)
prev=None;count=0
for count,line in enumerate((R/'research_manager/RESEARCH_JOURNAL.jsonl').read_bytes().splitlines(),1):
    row=json.loads(line)
    assert row['sequence']==count and row['previous_entry_sha256']==prev
    prev=sha(line)
checks['journal_chain']=True
branch=subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip()
result=dict(checks=checks,repository_files=files,archive_dependencies=members,journal_rows=count,
 actual_branch=branch,expected_branch=s['continuity']['repository_branch'],
 canonical_handoff_verifier='FAIL: detached checkout branch mismatch; not repaired or rerun as canonical',
 scope='Snapshot byte checks only; no mathematical validation or publication read-back')
(P/'SNAPSHOT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(checks=checks,repository_files_passed=sum(x['ok'] for x in files),repository_files_total=len(files),archive_dependencies_passed=sum(x['ok'] for x in members),archive_dependencies_total=len(members),diagnostic_decoded_hash_matches=sum(x.get('diagnostic_decoded_hash_match',False) for x in members),journal_rows=count,actual_branch=branch,expected_branch=result['expected_branch']),indent=2))
