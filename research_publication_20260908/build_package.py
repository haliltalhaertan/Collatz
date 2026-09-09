"""Package an explicit allowlist of completed public research artifacts."""
from pathlib import Path
import json,hashlib,zipfile
H=Path(__file__).resolve().parent;B=H.parent
groups={
'research_sol_20260908':['PRINCIPAL_ANALYSIS.md','REPORT_TR.md','BUDGET.json'],
'research_sol_gap_20260908':['COARSE_GRID_OBSTRUCTION_PROOF.md','INDEPENDENT_AUDIT.md','NEXT_ACTION.md','REPORT_TR.md','CONSTANT_CHECKS.json','check_constants.py','SOL_REVIEW.json','BUDGET.json','SOURCE_HASHES.json'],
'research_coarse_windows_20260908':['ALL_LOG_COEFFICIENTS_PROOF.md','SUBLOG_COROLLARY.md','INDEPENDENT_AUDIT.md','NEXT_ACTION.md','REPORT_TR.md','BUDGET.json']}
files={f'{directory}/{name}':(B/directory/name).read_bytes() for directory,names in groups.items() for name in names}
readme='''# CP20 coarse occupation research — 2026-09-08, V1

Latest result: the origin-aligned disjoint-block marked Laplace C/R helper bound fails for every fixed L=floor(c log R), c>0, on an actual accessible overshoot-summed G suffix sequence. A separately audited extension covers specified shorter scales above sqrt(log R).

Start with research_coarse_windows_20260908/REPORT_TR.md and ALL_LOG_COEFFICIENTS_PROOF.md. Earlier folders document the progression; their narrower open questions are superseded by the latest folder where explicitly settled.

The positive helper bound is refuted in the stated scope. The complex suffix estimate, XUB, and Collatz remain OPEN. These exploratory artifacts do not execute or reopen a closed B4 stage and do not change canonical research status.

This package contains proofs, review summaries, source hashes, fixed-constant checks and cost summaries. It contains no API credentials or raw model streams. Cumulative OpenRouter research cost: $0.061356 of a $2.00 ceiling. No new call was made in the final included turn.

The package is a snapshot of the three completed analytic turns, before the ongoing dense-pair continuation. The SHA256SUMS.json manifest covers every member other than itself.
'''
files['README.md']=readme.encode()
manifest={p:hashlib.sha256(v).hexdigest() for p,v in files.items()}
files['SHA256SUMS.json']=json.dumps(manifest,indent=2).encode()
package=H/'CP20_COARSE_OCCUPATION_20260908_V1.zip'
with zipfile.ZipFile(package,'w',zipfile.ZIP_DEFLATED) as z:
 for p,v in files.items():
  info=zipfile.ZipInfo(p,date_time=(2026,9,8,0,0,0)); info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,v)
with zipfile.ZipFile(package) as z:
 assert z.testzip() is None
 assert all(hashlib.sha256(z.read(p)).hexdigest()==h for p,h in manifest.items())
receipt={'package':str(package),'bytes':package.stat().st_size,'members':len(files),'sha256':hashlib.sha256(package.read_bytes()).hexdigest(),'internal_manifest_entries':len(manifest),'github_repository':'haliltalhaertan/Collatz','proposed_branch':'codex/coarse-occupation-20260908','drive_folder_id':'1Tg5P5wfILAgKYg-CiUmJS60kzdRFL2AU','upload_status':'PREPARED_NOT_UPLOADED'}
(H/'PACKAGE_RECEIPT.json').write_text(json.dumps(receipt,indent=2))
(H/'GITHUB_FILES.json').write_text(json.dumps({f'research_manager/exploratory/sync_20260908/coarse_occupation/{p}':v.decode('utf-8') for p,v in files.items()},ensure_ascii=False))
print(json.dumps(receipt))
