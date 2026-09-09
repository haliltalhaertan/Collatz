from decimal import Decimal as D, getcontext
from pathlib import Path
import json
getcontext().prec=60
ln2=D(2).ln();a=D(3).ln()/ln2;c=a/2;drift=1-c
Din=D('.001');ep=D('.00025');eta=Din/32;cert=D('5e-10')
rates=dict(base_upper=2*(D('.04')/a)**2/ln2,
 initial=2*(D('.01')/a)**2/ln2,
 affine=(Din*(1+ep)-2*ep)*a*(D('.5')-eta),
 parity=eta**2/(2*ln2),offset=3*eta**2/(2*ln2))
assert Din<rates['base_upper']
assert D('.0001')<rates['initial']
assert ep<Din/(2-Din)
assert eta<ep/(2*(ep+2))
assert 2*eta<ep*(D('.5')-eta)
assert cert<min(rates.values())
assert D('.02')+D('.05')*(c+D('.02'))<D('.1')
assert a/D('.95')<1+c-D('.02')
assert drift*a>D('.1')*D('1.2')
def I(u):
 p=D('.5')+u
 return 1+(p*p.ln()+(1-p)*(1-p).ln())/ln2
E=drift*a/D('1.2')
caps=[]
for z in (E,E/c):
 d=I(z/a);et=d/(2*(4-d));caps.append(dict(zeta=str(z),input_cap=str(d),eta_cap=str(et),certificate_cap=str(I(et))))
target=1-1/D('1.053')
assert all(D(x['certificate_cap'])<target for x in caps)
out=dict(status='PASS',precision_digits=60,certified_exponent=str(cert),rates={k:str(v) for k,v in rates.items()},caps=caps,required_exponent=str(target))
Path(__file__).with_name('PARAMETERS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
