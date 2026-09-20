"""Radius-1 witness (18,2)[14,14] + convention trap check. Exact arithmetic."""
from fractions import Fraction
from math import comb
from defend_gate import prefix_hist, transfer, J, autocorr, L_terms, M_terms

m, s = 18, 2
hist = prefix_hist(m, s+1)
L = L_terms(hist, m, s)
# build EO then M
EO = {}
for k in range(1, m+1):
    EO[k] = transfer(hist[k], k, s)
M = M_terms(EO, m, s)
print("L14 =", L[14], " M14 =", M[14], " M15 =", M[15])
# radius-1 window per spec: j in [a, b+1] with lower end a (NOT a-1), clipped to [2,m]
a = b = 14
demand = sum(x for x in [L[k] for k in range(a, b+1)] if x > 0)
lo = max(a, 2); hi = min(b+1, m)
supply = sum(M[j] for j in range(lo, hi+1))
print("demand =", demand, " want 3/35:", demand == Fraction(3,35))
print("supply =", supply, " want 4033/69615:", supply == Fraction(4033,69615))
print("gap =", demand-supply, " want 1934/69615:", (demand-supply) == Fraction(1934,69615))
# trap: shifted lower end max(a-1,2)
lo2 = max(a-1, 2); supply2 = sum(M[j] for j in range(lo2, hi+1))
print("TRAP shifted-window supply =", supply2, " gap2 =", demand-supply2, " (must differ; if gap2<=0 trap hides witness)")
