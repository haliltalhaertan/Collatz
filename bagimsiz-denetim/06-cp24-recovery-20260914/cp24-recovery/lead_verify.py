"""CP24 recovery: bounded exact checks and deduplicated archive audit.
Finite tests are evidence, not universal proofs. Original files are read only.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from collections import defaultdict
from functools import lru_cache
import json, hashlib

BASE=Path(__file__).resolve().parent.parent
OUT=Path(__file__).resolve().parent

def read(rel): return json.loads((BASE/rel).read_text(encoding='utf-8'))

def trajectory(h,m,b):
    x=h; B=0; w=[]
    for i in range(m):
        odd=x%2; w.append(odd)
        B=(3*B+(1<<i)) if odd else B
        x=(3*x+b)//2 if odd else x//2
    return tuple(w),sum(w),B,x

@lru_cache(None)
def source(m,r,b):
    out=defaultdict(lambda:[0]*(1<<r))
    for h in range(1,1<<m,2):
        w,k,B,e=trajectory(h,m,b)
        assert (1<<m)*e==3**k*h+b*B
        out[k][e%(1<<r)]+=1
    return dict(out)

def J(p):
    q=len(p)//2
    return q*sum((p[z]-p[z+q])**2 for z in range(q))

def energy(m,r,b):
    return sum((F(J(p),comb(m-1,k-1)) for k,p in source(m,r,b).items()),F(0))

def normalise(row):
    return {'m':row['m'],'s':row['s'],
            'lift':str(F(row.get('lift',row.get('L')))),
            'merge':str(F(row.get('merge',row.get('M')))),
            'defect':str(F(row['defect'])),
            'L':{int(k):F(v) for k,v in row.get('lift_terms',row.get('Lterms')).items()},
            'M':{int(k):F(v) for k,v in row.get('merge_terms',row.get('Mterms')).items()}}

result={}
assert energy(4,3,1)==F(40,3) and energy(5,2,1)==F(31,3)
result['gate']={'E_4_3':'40/3','E_5_2':'31/3'}
old_extension=read('cp21_lead_extension_m25_m26.json')['rows']
result['quarantined_original_extension']={'file':'cp21_lead_extension_m25_m26.json','rows':len(old_extension),'merge_sum_mismatch_rows':sum(sum(F(v) for v in r['merge_terms'].values())!=F(r['merge']) for r in old_extension),'reason':'Per-stratum merge sums disagree with stored totals; fresh trajectory reconstruction also disagrees. Original preserved; corrected rows used below.'}
paths=['r8-hunt-scratch/hunt_grid.json','cp24-recovery/corrected_extension.json','cp22-attack-files/attack_hot_results.json']
unique={}; batches=[]; conflicts=[]
for path in paths:
    rows=read(path)['rows']; added=0
    for row in rows:
        r=normalise(row); key=(r['m'],r['s'])
        if key in unique:
            old=unique[key]
            for f in ('lift','merge','defect'):
                if old[f]!=r[f]: conflicts.append([list(key),f,old[f],r[f]])
            for f in ('L','M'):
                for k in set(old[f])|set(r[f]):
                    if old[f].get(k,F(0))!=r[f].get(k,F(0)): conflicts.append([list(key),f,k])
        else: unique[key]=r; added+=1
    batches.append({'file':path,'rows':len(rows),'new_unique_rows':added})
assert not conflicts,conflicts
intervals=binding=violations=0
for (m,s),r in unique.items():
    assert sum(r['L'].values())==F(r['lift'])
    assert sum(r['M'].values())==F(r['merge'])
    assert F(r['merge'])-F(r['lift'])==F(r['defect'])
    for a in range(1,m+1):
        for b in range(a,m+1):
            dem=sum(max(r['L'].get(k,F(0)),F(0)) for k in range(a,b+1))
            sup=sum(r['M'].get(j,F(0)) for j in range(max(a-1,2),min(b+2,m)+1))
            intervals+=1; binding+=int(dem>0); violations+=int(dem>sup)
result['radius_archive']={'batches':batches,'unique_rows':len(unique),'conflicts':conflicts,
 'intervals':intervals,'positive_demand_intervals':binding,'violations':violations,
 'scope':'Recomputed from archived L/M fractions; not a fresh enumeration of every source.',
 'row_keys':sorted(unique)}

oldB=read('freq_defect/final.json')['D']['table']
newB=read('cp22-flank-files/flank/flank_Btrend.json')['rows']
a={(r['m'],r['s']) for r in oldB}; b={(r['m'],r['s']) for r in newB}
assert len(a)==len(oldB) and len(b)==len(newB)
lookup={(r['m'],r['s']):F(r['defect']) for r in oldB}
for r in newB:
    key=(r['m'],r['s'])
    if key in lookup: assert lookup[key]==F(r['defect'])
result['frequency_coverage']={'old':len(a),'later':len(b),'overlap':len(a&b),'new_unique':len(b-a),'union':len(a|b),
 'scope':'Coverage and common defect values only; cyclotomic signs not rerun here. Gauge D versus later convention requires separate review.',
 'row_keys':sorted(a|b)}

reflection=0; cycle_rows=[]
for m in range(1,15):
    counters={b:{'words':0,'positive_integral_candidates':0,'consistent':0} for b in (-1,1)}
    for h in range(1,1<<m,2):
        wm,km,Bm,em=trajectory(h,m,-1)
        wp,kp,Bp,ep=trajectory((1<<m)-h,m,1)
        assert wm==wp and km==kp and Bm==Bp and em+ep==3**km
        reflection+=1
        for b in (-1,1):
            w,k,B,e=trajectory(h,m,b); D=(1<<m)-3**k
            c=counters[b]; c['words']+=1
            if (b*B)%D: continue
            x=(b*B)//D
            if x<=0: continue
            c['positive_integral_candidates']+=1
            w2,_,_,e2=trajectory(x,m,b)
            assert x%2==1 and w2==w and e2==x
            c['consistent']+=1
    cycle_rows.append({'m':m,'plus':counters[1],'minus':counters[-1]})
result['reflection']={'checks':reflection,'failures':0,'m_range':[1,14]}
result['self_consistency']={'rows':cycle_rows,'failures':0,'scope':'Positive integral b*B/D; period divides m, not necessarily primitive m.'}

norm=[]
for m in range(1,13):
    r=2; total=1<<(m-1); E=energy(m,r,1)
    weighted=F(0)
    for k,p in source(m,r,1).items():
        n=comb(m-1,k-1)
        weighted+=F(n,total)*J([F(v,n) for v in p])
    assert weighted==E/total
    norm.append({'m':m,'r':r,'raw':str(E),'normalised':str(weighted)})
result['normalisation']={'formula':'sum_k (n_k/2^(m-1))*J_r(P_k/n_k) = Ecal(m,r)/2^(m-1)', 'rows':norm}

# Authenticate real caps/supports independently, not just from witness truePh.
w=read('cp22-attack-files/attack_witness.json');m=w['m'];s=w['s']
truth=source(m,s+1,1)
assert all(truth[int(k)]==v for k,v in w['truePh'].items())
for k,arr in w['Ph'].items():
    k=int(k);real=truth[k]
    assert len(arr)==len(real) and all(type(x) is int and x>=0 for x in arr)
    assert sum(arr)==comb(m-1,k-1) and max(arr)<=max(real)
    assert all((x>0)==(y>0) for x,y in zip(arr,real))
result['attack_constraints']={'m':m,'s':s,'independent_real_histogram_match':True,'exact_support_equality':True,'mass_cap_integrality':True}
manifest=json.loads((OUT/'original_manifest.json').read_text())
assert all(hashlib.sha256((OUT/r['path']).read_bytes()).hexdigest()==r['sha256'] for r in manifest)
result['original_files_unchanged']=True
(OUT/'lead_verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
summary={k:v for k,v in result.items() if k not in ('self_consistency','normalisation')}
summary['radius_archive']={k:v for k,v in result['radius_archive'].items() if k!='row_keys'}
summary['frequency_coverage']={k:v for k,v in result['frequency_coverage'].items() if k!='row_keys'}
summary['cycles']={str(b):sum(r['plus' if b==1 else 'minus']['consistent'] for r in cycle_rows) for b in (-1,1)}
summary['normalisation_examples']=[norm[3],norm[11]]
print(json.dumps(summary,indent=2))
