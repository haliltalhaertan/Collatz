from math import comb,log2
from fractions import Fraction as F
from pathlib import Path
import json
rows=[]
for r in (16,32,64,128,256):
 A=(3**r).bit_length()-1;m=(6*r+4)//5;t=A-m;B=2**t
 total=comb(A-1,r-1);mu=F(total,B)
 origin=(total//B)*2**(r//16)
 q,u=divmod(total-origin,B-1)
 assert q>=0 and max(origin,q+bool(u))<=2**(m-1)
 assert origin+(B-1-u)*q+u*(q+1)==total
 squares=origin**2+(B-1-u)*q*q+u*(q+1)**2
 cv2=F(B*squares-total**2,total**2)
 R=F(B*origin,total)
 assert (R-1)**2<=(B-1)*cv2
 rows.append(dict(r=r,A=A,m=m,t=t,blocks=B,total=total,origin=origin,other_low=q,other_high=q+1,other_high_count=u,origin_ratio=str(R),cv2=str(cv2),finite_origin_loss=log2(R)/r,finite_cv_decay=-log2(cv2)/r))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(status='PASS',scope='Synthetic block histogram; not actual Collatz block counts',rows=rows),indent=2))
print(json.dumps([dict(r=row['r'],loss=row['finite_origin_loss'],variance_decay=row['finite_cv_decay']) for row in rows],indent=2))
