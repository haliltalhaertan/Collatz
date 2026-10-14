#!/usr/bin/env python3
"""Assemble referee's independent computations and stated rounded claims."""
import json
from decimal import Decimal
small=json.load(open('cp29_small.json'))
large=json.load(open('cp29_large.json'))
extended=json.load(open('cp29_extended.json'))
claimed={16:('8.684947712648','0.471351643393','960.34'),17:('9.156767868074','0.471820155426',None),18:('9.629001325254','0.472233457180','2160.91')}
for row in small['precision']:
    if row['claimed_E'] is not None:
        row['E_minus_claim']=str(Decimal(row['E'])-Decimal(row['claimed_E']))
for s,(c,e,m) in claimed.items():
    row=extended[s-1]
    row['chi_minus_claim']=str(Decimal(str(row['chi']))-Decimal(c))
    row['E_minus_claim']=str(Decimal(str(row['E']))-Decimal(e))
    if m is not None:
        row['scaled_max_minus_claim']=str(Decimal(str(row['max_scaled']))-Decimal(m))
report={
 'language':'tr',
 'method':{'high_precision':'cp29_small.py; decimal 75 digits; geometric tail exactly resummed for s<=5; truncate A at 285 for s>=6, probability mass lost per transition 2^-285; chi total error <= 2*(3^10)*10*2^-285 (~2e-80), plus decimal rounding',
  'large':'cp29_large.py; numpy float64 density h_s(y)=3^s*p_s(y), 1D array; independent affine inverse gather on blocks of one million elements, maximum two consecutive levels in RAM; truncate A at 56; 3^18=387420489, maximum total-variation error over 18 transitions <= 18*2^-56; machine roundoff ~1e-12 in chi.',
  'memory':'free -g: 15 GiB total, 14 GiB available; ran both s=17 and s=18',
  'I4':'cp29_small.py: modulo 27, ord_27(2)=18, probability of A congruent a mod 18 is 2^(18-a)/(2^18-1)'},
 'verdicts':{
  'I1':{'decision':'DOĞRU','reason':'A=A\u2032 has probability 1/3 and forces equality iff previous residues coincide. χ_s-χ_{s-1}=3^s r_s; identical words contribute 3^s*(1/3)^s=1.','r1':'2/9','r2':'10/189'},
  'I2':{'decision':'DOĞRU','reason':'K=A\u2032-A has P(K=2l)=4^-|l|/3; equality forces K even; ord_{3^s}(4)=3^(s-1). K=0 contributes q_{s-1}/3.'},
  'I3':{'decision':'DOĞRU','reason':'sum_t q_s(r,t)=p_{s-1}(r); expanding squares yields E_s; by 0<=sum_t q_s(r,t)^2<=p_{s-1}(r)^2, 0<=E_s<=2χ_{s-1}.'},
  'I4':{'decision':'DOĞRU','reason':'With integer x,y reduced modulo 9, outputs taken modulo 27 and powers 2^-A reduced modulo 27; event is v_3(u-u\u2032)>=3. Conditional probabilities differ even with old valuation 0.','probabilities':small['I4']},
  'I5':{'decision':'DOĞRU','reason':'All displayed values agree within stated decimal rounding; unrounded density maxima differ from two-decimal values by under 0.005.','high_precision':small['precision'],'float64':large,'longdouble':extended},
  'I6':{'decision':'DOĞRU','reason':'telescoping; bounded E forces O(s), E_j tending to infinity forces diverging Cesaro means; unbounded spikes E_{2^k}=k and otherwise 0 leave χ_s=O(s).'}
 }
}
with open('cp29_referee.json','w') as f:json.dump(report,f,ensure_ascii=False,indent=2)
print('cp29_referee.json generated')
