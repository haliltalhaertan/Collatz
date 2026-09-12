# Independent scalar audit of the cross-channel contraction

Date: 2026-09-12. Status: **PASS, within the finite grid below**.

This implementation was written from the definitions in the previous
`research_shift_recurrence_20260912/ALGORITHM.md`, without reading, importing,
or sharing the main cross-term probe implementation. It uses Python scalar
integers, explicit shortcut steps, and nested sums. No FFT, packed integer
convolution, or repository correlation helper is used.

## Scope and exact checks

Every `t=2,...,10`, every `j=0,...,t`, and every
`s=2,...,min(t,7)` was checked: **313 complete filter cases**.
The depth cap of 7 was prescribed before execution. There is no random sampling.
The run took approximately 0.41 seconds on this host; this is not a benchmark.

Write `n=2^s, q=n/2, h0=q/2`, and keep
`g(k)=binom(t-s,j-k)` fixed when defining the child arrays.
The shortcut map is `x -> x/2` on even inputs and `(3x+1)/2`
on odd inputs. Both parent and child odd-step counts were computed directly.

For each case the audit independently constructs all shifts of:

- `C(d)=sum_u v(u)v(u+d)`, where `v(u)=g(K_s(u))`.
- `A0(d)=sum_u a(u)a(u+d)`, `A1(d)=sum_u b(u)b(u+d)`,
  where `a(u)=g(K_(s-1)(u))`, `b(u)=g(K_(s-1)(u)+1)`.
- `B(d)=sum_u a(u)b(3u+d)`.

All array indices are reduced modulo their own array length.
**All 11,004 parent correlation identities passed**:

```
C(2h)   = A0(h) + A1(3h)
C(2h+1) = B(3h+2) + B(-3h-1),    h=0,...,q-1.
```

Writing `Delta Z(d)=Z(d)-Z(d+h0)`, every sibling-difference identity
also passed. For `h=0,...,h0-1`, the four channel vectors are

```
x_h = Delta A0(h)
y_h = Delta A1(3h)
z_h = Delta B(3h+2)
w_h = Delta B(-3h-1).
```

The audit checked exact equality between direct parent norms and

```
N_even = sum x_h^2 + sum y_h^2 + 2 sum x_h y_h
N_odd  = sum z_h^2 + sum w_h^2 + 2 sum z_h w_h.
```

Every channel Cauchy bound was checked as an integer square inequality
`cross^2 <= 4 norm_left norm_right`; the looser
`abs(cross) <= norm_left+norm_right` was checked separately.

## What the signs actually do

| Cross term | Positive cases | Negative cases | Zero cases |
|---|---:|---:|---:|
| Even | 227 | 0 | 86 |
| Odd | 79 | 119 | 115 |
| Sum of even and odd | 185 | 0 | 128 |

Thus the odd cross term **can be negative or positive** on actual filters.
Dropping all cross terms does not give an upper bound: the total is strictly
positive in 185 cases. The even term and total were nonnegative on this grid,
but **no all-scale nonnegativity theorem is claimed**.

There were 86 even-channel and 45 odd-channel Cauchy equalities with both
channel norms nonzero. This count uses squared equality and therefore includes
both signs. It must not be presented as 45 cases of positive saturation.

The largest measured amplification occurred at `(t,s,j)=(9,4,5)`:

```
channel squared norms = (8406, 3750, 5550, 5550)
diagonal contribution = 23256
even cross term        = 11100
odd cross term         = 11000
total cross term       = 22100
actual parent norm     = 45356

total cross / diagonal = 325/342
parent norm / diagonal = 667/342 ~= 1.9502924.
```

The two branches can therefore nearly double the diagonal-only estimate in a
small genuine filter. This is a concrete obstruction to treating the cross
terms as negligible; it is not an asymptotic impossibility result for a
constant-factor bound.

## Limits

This independent implementation validates the exact contraction and norm
decomposition on the stated grid. It does not validate larger cases solely
because the formulas match here. The symbolic derivation remains necessary.
Nor does it establish the sought weighted source/filter estimate, uniform
cross-term decay, or a scalar moment closure.

The complete integer rows, including each sign, equality flag, norm, and exact
rational ratio, are in `independent_results.json`.

## Complete reproduction program

Run the following Python program from the repository root. It imports only the
standard library and regenerates `independent_results.json`. It writes no
other repository files and makes no network or provider calls.

```python
from math import comb
from fractions import Fraction
from collections import Counter
from pathlib import Path
import json,time
started=time.perf_counter()
def kword(x,s):
    k=0
    for _ in range(s):
        e=x%2
        k+=e
        x=(3*x+1)//2 if e else x//2
    return k
def choose(n,k):
    return comb(n,k) if 0<=k<=n else 0
def corr(a,b):
    n=len(a)
    return [sum(a[u]*b[(u+d)%n] for u in range(n)) for d in range(n)]
rows=[]
identities=0
signs={z:Counter() for z in ('even','odd','total')}
for t in range(2,11):
  for s in range(2,min(t,7)+1):
    n=2**s;q=n//2;h0=q//2
    ks=[kword(u,s) for u in range(n)]
    kl=[kword(u,s-1) for u in range(q)]
    for j in range(t+1):
      v=[choose(t-s,j-k) for k in ks]
      a=[choose(t-s,j-k) for k in kl]
      b=[choose(t-s,j-k-1) for k in kl]
      C=corr(v,v);A0=corr(a,a);A1=corr(b,b)
      B=[sum(a[u]*b[(3*u+d)%q] for u in range(q)) for d in range(q)]
      for h in range(q):
        assert C[2*h]==A0[h]+A1[(3*h)%q]
        assert C[2*h+1]==B[(3*h+2)%q]+B[(-3*h-1)%q]
        identities+=2
      d0=[A0[d]-A0[(d+h0)%q] for d in range(q)]
      d1=[A1[d]-A1[(d+h0)%q] for d in range(q)]
      db=[B[d]-B[(d+h0)%q] for d in range(q)]
      x=[d0[h] for h in range(h0)]
      y=[d1[(3*h)%q] for h in range(h0)]
      z=[db[(3*h+2)%q] for h in range(h0)]
      w=[db[(-3*h-1)%q] for h in range(h0)]
      for h in range(h0):
        assert C[2*h]-C[2*h+q]==x[h]+y[h]
        assert C[2*h+1]-C[2*h+1+q]==z[h]+w[h]
      N0=sum(xx*xx for xx in x);N1=sum(yy*yy for yy in y)
      N2=sum(zz*zz for zz in z);N3=sum(ww*ww for ww in w)
      ce=2*sum(xx*yy for xx,yy in zip(x,y))
      co=2*sum(zz*ww for zz,ww in zip(z,w))
      even=sum((C[2*h]-C[2*h+q])**2 for h in range(h0))
      odd=sum((C[2*h+1]-C[2*h+1+q])**2 for h in range(h0))
      assert even==N0+N1+ce and odd==N2+N3+co
      base=N0+N1+N2+N3
      assert even+odd==base+ce+co
      assert abs(ce)<=N0+N1 and abs(co)<=N2+N3
      assert ce*ce<=4*N0*N1 and co*co<=4*N2*N3
      for label,value in [('even',ce),('odd',co),('total',ce+co)]:
        signs[label]['positive' if value>0 else 'negative' if value<0 else 'zero']+=1
      rows.append(dict(t=t,s=s,j=j,parent_sibling_norm=even+odd,diagonal=base,
        even_cross=ce,odd_cross=co,total_cross=ce+co,
        even_norm=even,odd_norm=odd,channel_norms=[N0,N1,N2,N3],
        cross_over_diagonal=str(Fraction(ce+co,base)) if base else None,
        even_cauchy_equality=ce*ce==4*N0*N1 and N0*N1>0,
        odd_cauchy_equality=co*co==4*N2*N3 and N2*N3>0))
nonzero=[r for r in rows if r['diagonal']]
summary={'cases':len(rows),'scalar_correlation_identities':identities,
 'signs':{k:dict(v) for k,v in signs.items()},
 'max_cross_ratio':max(nonzero,key=lambda r:Fraction(r['cross_over_diagonal'])),
 'min_cross_ratio':min(nonzero,key=lambda r:Fraction(r['cross_over_diagonal'])),
 'even_nontrivial_cauchy_equalities':sum(r['even_cauchy_equality'] for r in rows),
 'odd_nontrivial_cauchy_equalities':sum(r['odd_cauchy_equality'] for r in rows),
 'elapsed_seconds':time.perf_counter()-started}
out={'status':'PASS','scope':'All t=2..10, j=0..t, s=2..min(t,7). No sampling.',
 'implementation':'Independent scalar shortcut steps and nested integer sums. No imports of repository probe or FFT/Kronecker code.',
 'summary':summary,'rows':rows}
p=Path('research_cross_terms_20260912');p.mkdir(exist_ok=True)
(p/'independent_results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,indent=2))
```


## Follow-up: stronger identity and independent implementation comparison

After the initial grid was fixed and run, the parent researcher supplied the
stronger identity E=RB and requested an explicit cross-check. All **313**
independent rows satisfy exactly:

```
independent even_cross = 2*RB
channel_norms[2] = channel_norms[3] = RB
even_norm <= parent_sibling_norm <= 2*even_norm.
```

The factor two matters: this audit includes the coefficient 2 in the displayed
cross terms; the main implementation stores E and O before multiplying by 2.
The finite checks agree with the separately derived general identity; these
checks alone are not its proof.

I then compared all **247** rows of the main `RESULTS.json` direct-check grid
with the matching independent `(t,j,s)` row. Total energy, even energy, odd
energy, uncoupled energy, both cross terms after adjusting the factor of two,
and R0,R1,RB **all matched exactly**. Main large-family rows are outside this
independent direct-enumeration comparison.

The JSON stores this audit in
`followup_identity_and_cross_implementation_audit`. The reproduction code
above regenerates the initial independent grid; the follow-up is reproduced
by joining that grid to `RESULTS.json` on `(t,j,s)` and checking the identities
and field correspondences stated here.
