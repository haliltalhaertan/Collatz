from collections import Counter
from math import comb
from pathlib import Path
import json

checks=0;rows=[]
for m in range(1,13):
    t=max(1,m//3);counts=Counter()
    for x in range(1,2**m,2):
        y=x;k=0
        for _ in range(m):
            k+=y%2;y=(3*y+1)//2 if y%2 else y//2
        C=2**m*y-3**k*x
        assert 0<y<3**k
        assert 0<=C<=2**(m-k)*(3**k-2**k)
        z=y;j=0
        for _ in range(t):
            j+=z%2;z=(3*z+1)//2 if z%2 else z//2
        counts[k,j]+=1;checks+=1
    for (k,j),n in counts.items():
        bound=comb(t,j)*((3**k+2**t-1)//2**t)*(2**(m-k)+1)
        assert n<=min(comb(m-1,k-1),bound)
    rows.append(dict(m=m,t=t,nonempty_cells=len(counts)))
out=dict(status='PASS',start_checks=checks,rows=rows)
Path(__file__).with_name('HEIGHT_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
