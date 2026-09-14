"""Reproduce historical slicing bug; assert correct folding and limits.
Historical source: session 20260914_102430_a9543e, message 7451,
row(): P=P[:N], arr=arr[:q], Pf=...[:N].
All outputs are read-only versus original archive; corrected artifacts separate.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json
from recompute_extension import histogram,fold,calc,J
ROOT=Path(__file__).resolve().parent
H={m:{int(k):v for k,v in json.loads((ROOT/f'hist_m{m}.json').read_text()).items()} for m in (25,26)}
# Need full r=7 for exact emulation of the old output-prefix truncation.
H[27]=histogram(27,7)
(ROOT/'hist_m27_r7.json').write_text(json.dumps(H[27]))
old=json.loads((ROOT.parent/'cp21_lead_extension_m25_m26.json').read_text())['rows']
checks=[]
for r in old:
 m,s=r['m'],r['s'];N=1<<(s+1);q=1<<s
 sliced={k:v[:N] for k,v in H[m].items()}
 buggy,_,_=calc(sliced,m,s)
 wrongout=sum((F(J(v[:q]),comb(m,k-1)) for k,v in H[m+1].items()),F(0))
 buggy['output']=str(wrongout);buggy['merge']=str(F(buggy['fine'])-wrongout);buggy['defect']=str(F(buggy['input'])-wrongout)
 fields=('input','fine','output','lift','merge','defect','lift_terms','merge_terms')
 assert all(buggy[f]==r[f] for f in fields),(m,s,[f for f in fields if buggy[f]!=r[f]])
 correct=fold(H[m],s+1)
 assert all(sum(v)==comb(m-1,k-1) for k,v in correct.items())
 lost=sum(sum(v)-sum(sliced[k]) for k,v in correct.items())
 checks.append({'m':m,'s':s,'all_historical_fields_reproduced_by_slice_bug':True,'input_starts_lost':lost,'output_starts_lost':sum(sum(v)-sum(v[:q]) for v in H[m+1].values())})
# Red control: a one-point input at residue 7 mod 8 must land at 3 mod 4.
vec={1:[0,0,0,0,0,0,0,1]}
assert fold(vec,2)=={1:[0,0,0,1]} and vec[1][:4]!=fold(vec,2)[1]
(ROOT/'truncation_regression.json').write_text(json.dumps({'bug_reproductions':checks,'red_control_rejected':True,'correct_fold_mass_conservation':True},indent=2))
print(json.dumps(checks,indent=2));print('REGRESSION_OK')
