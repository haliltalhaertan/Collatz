from phase_quotient_core import qq,quot
from math import log2
from fractions import Fraction
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent
s=17;t=2*s;j=round(t/log2(3));qq.cache_clear();st=time.perf_counter();v=quot(t,j,s,0);dt=time.perf_counter()-st;ns=qq.cache_info().currsize
out={'status':'PASS','s':s,'states':ns,'direct':1<<s,'ratio':str(Fraction(ns,1<<s)),'seconds':dt,'value':str(v)}
(HERE/'S17_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
