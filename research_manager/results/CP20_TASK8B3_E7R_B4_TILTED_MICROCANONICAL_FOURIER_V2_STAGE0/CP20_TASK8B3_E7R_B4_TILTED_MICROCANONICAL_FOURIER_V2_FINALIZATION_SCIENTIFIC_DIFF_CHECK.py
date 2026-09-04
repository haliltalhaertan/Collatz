#!/usr/bin/env python3
import hashlib,json,pathlib,zipfile,sys
TASK='CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2'
CANDIDATE_SHA='2e6d9e1d833fc8dabf02c0e970ccfb06fc86e4cbc9e85cd2e0e61ae3611879ea'
SCI=['CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_DEFINITIONS.md', 'CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_FALSIFICATION_PLAN.md', 'CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_ORDER.md', 'CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_OUTCOME_LADDER.md', 'CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_T1_T8_PROGRAM.md', 'CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_TARGET_NORMAL_FORM.md', 'CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2_STAGE1_EXECUTION_INTEGRITY_AND_OUTPUT_CONTRACT.md']
root=pathlib.Path(__file__).resolve().parent
candidate=pathlib.Path(sys.argv[1])
h=lambda b: hashlib.sha256(b).hexdigest()
assert h(candidate.read_bytes())==CANDIDATE_SHA
rows=[]
with zipfile.ZipFile(candidate) as z:
    for n in SCI:
        old=z.read(n); new=(root/n).read_bytes()
        rows.append({'file':n,'candidate_sha256':h(old),'final_sha256':h(new),'byte_identical':old==new})
verdict='NO SCIENTIFIC CHANGE' if all(r['byte_identical'] for r in rows) else 'SCIENTIFIC_CHANGE'
out={'schema':TASK+'_FINALIZATION_SCIENTIFIC_DIFF_REPORT_V1','blocked_candidate_seal_sha256':CANDIDATE_SHA,'comparisons':rows,'allowed_differences':['HANDOFF_EVIDENCE_ADDITION','PRE_RUN_STATUS_FINALIZATION','MANIFEST_REBUILD','SEAL_REBUILD','HASH_UPDATE'],'forbidden_scientific_change_detected':verdict!='NO SCIENTIFIC CHANGE','verdict':verdict}
(root/(TASK+'_SCIENTIFIC_DIFF_REPORT.json')).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print('SCIENTIFIC DIFF:')
print(verdict)
raise SystemExit(0 if verdict=='NO SCIENTIFIC CHANGE' else 2)
