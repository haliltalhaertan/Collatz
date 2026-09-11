"""Task 8A / CP19 T4 bridge — corrected diagnostic.

The historical finite search suggested a small (~0.0017) entropy gap. The
frozen Task 8A decision records that this was a grid/feasible-domain artifact:
with the missing constraint rho_1-rho_2 >= 3-2*alpha and correct optimization,
the surface recovers CP19 Task 4 exactly. This script therefore does NOT use a
finite grid mismatch as a theorem or as evidence for a strict phase cost.
"""
from mpmath import mp, mpf, exp, log, findroot, diff
mp.dps=40
A=log(3)/log(2); M1=2-A; M2=A-1; FEAS=3-2*A

def l2(x): return log(x)/log(2)
Af=lambda l: exp(-l)/(1-exp(-l))
Bf=lambda l: exp(l)+exp(-l)/(1-exp(-l))
def xlx(x): return mpf(0) if x<=0 else x*l2(x)

def feasible(r1,r2):
    return 0 <= r1 < M1 and 0 <= r2 < M2 and r1-r2 >= FEAS

def h(r1,r2):
    if not feasible(r1,r2): return None
    w1,w2=M1-r1,M2-r2
    f=lambda lam:w1*l2(Af(lam))+w2*l2(Bf(lam))
    try:
        lam=findroot(lambda L:diff(f,L), mpf('1.6'))
        if lam<=0: return None
    except Exception:
        return None
    return f(lam)+xlx(M1)-xlx(w1)-xlx(r1)+xlx(M2)-xlx(w2)-xlx(r2)

h_alpha=l2(A)+(A-1)*(l2(A)-l2(A-1))
print(f"CP19 T4 geometrik maksimum entropi h(alpha) = {mp.nstr(h_alpha,20)}")
print(f"CP19 T4 esigi alpha/h(alpha)               = {mp.nstr(A/h_alpha,20)}")
print(f"feasible constraint rho_1-rho_2 >= {mp.nstr(FEAS,12)}\n")

# Finite search is retained only as a regression/diagnostic, not as a proof of
# the optimized maximum. Avoid singular boundary points.
b=None
for i in range(1,161):
    r1=M1*mpf(i)/161
    for j in range(0,161):
        r2=M2*mpf(j)/161
        v=h(r1,r2)
        if v is not None and (b is None or v>b[0]): b=(v,r1,r2)

print("FINITE FEASIBLE-GRID DIAGNOSTIC (not a certified optimizer):")
print(f"  grid max h = {mp.nstr(b[0],18)} at (rho_1,rho_2)=({mp.nstr(b[1],8)}, {mp.nstr(b[2],8)})")
print(f"  grid gap to h(alpha) = {mp.nstr(abs(b[0]-h_alpha),8)}")
print("  This finite-grid gap is NOT a phase-cost theorem.")
print()
print("FROZEN/CORRECT STATUS:")
print("  Correctly optimized feasible Task 8A surface recovers CP19 Task 4 exactly.")
print("  There is NO strict optimized Sturmian phase cost at that endpoint.")
print("  CP19 Task-5 survivor is NOT excluded by this surface (hypothesis mismatch).")
