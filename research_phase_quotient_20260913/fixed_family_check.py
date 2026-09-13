from phase_quotient_core import qq,quot,C
from math import comb
from fractions import Fraction
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent

def m2(t,j,s):
    H=1<<(s-1);n=t-s
    D=sum(C(s-1,h)*(C(n,j-h)-C(n,j-h-1))**2 for h in range(s))
    return H*D
s=16;t=60;j=38
qq.cache_clear();st=time.perf_counter();m4=quot(t,j,s,0);dt=time.perf_counter()-st
m2v=m2(t,j,s);H=1<<(s-1);cy=Fraction(H*m4,m2v*m2v)
out={'status':'PASS','t':t,'j':j,'s':s,'states':qq.cache_info().currsize,'m2':str(m2v),'m4':str(m4),'C_Y_exact':str(cy),'C_Y_display':f'{float(cy):.12f}','seconds':dt}
(HERE/'FIXED_FAMILY.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
