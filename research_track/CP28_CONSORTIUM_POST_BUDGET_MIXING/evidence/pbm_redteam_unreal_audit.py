import math
import numpy as np

# Tests of two key displayed bounds: (3) Hoeffding bound and (42)-(43) capacity.
# Enumerate fair binary strings to compute the exact deviation probability.
r, w, ell, eps = 1, (1,), 16, 0.4
M = ell-r+1
bad = 0
for bits in range(1 << ell):
    a = sum(tuple((bits >> (i+j)) & 1 for j in range(r)) == w for i in range(M))
    bad += abs(a-M/(1 << r)) > eps*M
bound = 2*r*math.exp(-eps**2*M/r)
print('eq(3): r=%d ell=%d eps=%s; exact=%.9f bound=%.9f' %(r,ell,eps,bad/(1<<ell),bound))
beta = math.log2(3)/2
for j in (3,4):
    val = sum(beta**i for i in range(1,j+1))/2
    print('capacity A%d=%.12f, (42)/(43) sign=%s' %(j,val,val<1 if j==3 else val>1))
# Separate independent check of (28): for delta=.3, c=.99, rho=.001, eps=.001
c, rho, e, delta = .99, .001, .001, .3
print('eq(29): lhs=%.9f > delta=%.9f : %s' %((.5-e)*c*(beta-rho),delta,(.5-e)*c*(beta-rho)>delta))

# Exhaustive shell, vectorizing the EXACT integer Syracuse map.
# At x=1 a=2 and U(x)=1: keep iterating, no early stop.
# uint64 safe in these ranges: 3*x+1 < 2**64 (can check).
for m in range(16,23):
    L = (3*m)//10
    x = np.arange((1<<m)+1,1<<(m+1),2,dtype=np.uint64)
    n = len(x)
    s = np.zeros(n,dtype=np.uint16)
    j = np.zeros(n,dtype=np.uint8)
    counts = np.zeros(n,dtype=np.uint8)
    tau = np.zeros(n,dtype=np.uint8)
    pending = np.ones(n,dtype=bool)
    while np.any(pending):
        ids = np.flatnonzero(pending)
        q = x[ids]
        v = 3*q + np.uint64(1)
        a = np.zeros(len(ids),dtype=np.uint8)
        even = (v & np.uint64(1)) == 0
        while np.any(even):
            v[even] >>= np.uint64(1)
            a[even] += 1
            even = (v & np.uint64(1)) == 0
        # tau=min{j:S_j>m}: current a has index j, and crossing
        # produces tau=j+1. This a_tau-1 must NOT be counted.
        start = (tau[ids] == 0) & (s[ids]+a > m)
        tau[ids[start]] = j[ids[start]]+1
        pick = (tau[ids] != 0) & ~start & (j[ids] >= tau[ids]) & (j[ids] < tau[ids]+L)
        counts[ids[pick]] += (a[pick]==1)
        s[ids] += a
        j[ids] += 1
        x[ids] = v
        pending[ids] = (tau[ids] == 0) | (j[ids] < tau[ids]+L)
    f = counts.astype(np.float64)/L
    print('m=%d N=%d L=%d mean=%.9f var=%.9f' %(m,n,L,f.mean(),f.var()))
