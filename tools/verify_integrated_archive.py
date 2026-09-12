"""Integration coverage, static preservation and reproducibility verification.

Run --refresh-integrity before building, then run without arguments after the
build. Verification receipts live outside the archive, avoiding hash recursion.
"""
from pathlib import Path
import hashlib,io,json,subprocess,sys,zipfile
import build_current_archive as b
R=b.REPO
def sha(data):return hashlib.sha256(data).hexdigest()
if '--refresh-integrity' in sys.argv:
 p=R/'CURRENT_RESEARCH_STATE.json';d=json.loads(p.read_text(encoding='utf-8'))
 dynamic={n:f for f,n in b.dynamic_entries()}
 for row in d['integrity']['repository_files']:
  assert row['path']!='CURRENT_RESEARCH_STATE.json'
  row['sha256']=sha((R/row['path']).read_bytes())
 for row in d['integrity']['archive_members']:
  if row['path'] in dynamic:
   assert dynamic[row['path']]!=p
   row['sha256']=sha(dynamic[row['path']].read_bytes())
 # Bind the new accepted reports and reproducibility sources explicitly.
 existing={x['path'] for x in d['integrity']['repository_files']}
 for folder in ['research_integration_20260912','research_w_continuation_20260912','research_peak_peeling_20260912','research_concentration_audit_20260912','research_galois_audit_20260912','research_shift_recurrence_20260912','research_cross_terms_20260912']:
  for f in sorted((R/folder).iterdir()):
   if not f.is_file() or f.suffix not in {'.md','.py','.json'}:continue
   rel=f.relative_to(R).as_posix()
   if rel not in existing:d['integrity']['repository_files'].append({'path':rel,'sha256':sha(f.read_bytes())})
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 print('Integrity bindings refreshed; build and verify before publication.')
else:
 original=subprocess.check_output(['git','show','2461573739147763eb011faf03c344370a184d69:Collatz_Research_Archive_CURRENT.zip'],cwd=R)
 current=b.OUTPUT.read_bytes()
 with zipfile.ZipFile(io.BytesIO(original)) as old,zipfile.ZipFile(io.BytesIO(current)) as new:
  assert old.testzip() is None and new.testzip() is None
  static=0
  for item in old.infolist():
   if item.is_dir() or any(item.filename.startswith(prefix) for prefix in b.DYNAMIC_PREFIXES):continue
   assert old.read(item)==new.read(item.filename),item.filename
   static+=1
  dynamic=b.dynamic_entries()
  for path,name in dynamic:assert new.read(name)==path.read_bytes(),name
  exploratory=b.exploratory_entries()
  assert any(n.endswith('/research_w_continuation_20260912/PROPOSAL.md') for _,n in exploratory)
  assert any(n.endswith('/research_integration_20260912/AUDIT_REVIEW.md') for _,n in exploratory)
  count=len(new.infolist())
 before=sha(current)
 subprocess.run([sys.executable,str(R/'tools/build_current_archive.py')],cwd=R,check=True,stdout=subprocess.DEVNULL)
 assert sha(b.OUTPUT.read_bytes())==before,'Non-deterministic second build'
 out={'schema':'COLLATZ_INTEGRATED_ARCHIVE_VERIFICATION_V1','original_archive_sha256':sha(original),'archive_sha256':before,'static_members_byte_preserved':static,'dynamic_members_byte_equal':len(dynamic),'exploratory_members':len(exploratory),'total_members':count,'second_build_byte_identical':True,'crc':'PASS','scope':'Archive bytes and membership; not proof of archived scientific claims'}
 dest=R/'publication_receipts';dest.mkdir(exist_ok=True)
 receipt_name=sys.argv[sys.argv.index('--receipt')+1] if '--receipt' in sys.argv else 'BUILD_VERIFICATION_20260912.json'
 assert Path(receipt_name).name==receipt_name and receipt_name.endswith('.json')
 (dest/receipt_name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps(out))
