"""TASK 8A — pressure-surface exploratory diagnostic.

Historical closed-form reduction is retained, but the current script enforces
the feasible-domain constraint recorded by the frozen Task8A decision:
    rho_1 - rho_2 >= 3 - 2*alpha.

IMPORTANT: the finite grids below are diagnostics only. They are not the V3
certified optimizer and must not be used to claim a strict Sturmian phase cost
or to exclude the CP19 Task-5 survivor. The frozen conclusions are:
- correctly optimized surface recovers CP19 Task 4 exactly at its maximum;
- CP19 Task-5 survivor is NOT excluded because of a hypothesis mismatch.
"""
from mpmath import mp, mpf, exp, log, findroot, diff
mp.dps=30
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
        lam=findroot(lambda L:diff(f,L),mpf('1.6'))
        if lam<=0: return None
    except Exception: return None
    E1=xlx(M1)-xlx(w1)-xlx(r1)
    E2=xlx(M2)-xlx(w2)-xlx(r2)
    return f(lam)+E1+E2

print(f"rho_1 < {mp.nstr(M1,7)}   rho_2 < {mp.nstr(M2,7)}")
print(f"feasible constraint: rho_1-rho_2 >= {mp.nstr(FEAS,9)}\n")
print("LEGACY FINITE-GRID DIAGNOSTIC — not a certified optimizer")
print(f"{'rho_1':>7} {'rho_2':>7} {'toplam':>8} {'h':>11} {'kappa esigi':>12}")
for r1,r2 in [(0,0),('0.01',0),(0,'0.01'),('0.05','0.05'),('0.1','0.1'),('0.2',0),(0,'0.2'),('0.2','0.2'),('0.3','0.4')]:
    r1,r2=mpf(r1),mpf(r2); v=h(r1,r2)
    if v is None:
        print(f"{mp.nstr(r1,4):>7} {mp.nstr(r2,4):>7} {mp.nstr(r1+r2,4):>8} {'INFEASIBLE':>11}")
    else:
        e=A/v if v>0 else mp.inf
        print(f"{mp.nstr(r1,4):>7} {mp.nstr(r2,4):>7} {mp.nstr(r1+r2,4):>8} {mp.nstr(v,8):>11} {mp.nstr(e,8):>12}")

print("\nFINITE GRID max h (diagnostic only):")
best=None
for i in range(41):
    for j in range(41):
        # avoid singular boundary points M1/M2
        r1,r2=M1*i/41,M2*j/41
        v=h(r1,r2)
        if v is not None and (best is None or v>best[0]): best=(v,r1,r2)
print(f"  grid max h = {mp.nstr(best[0],10)} at rho_1={mp.nstr(best[1],6)}, rho_2={mp.nstr(best[2],6)}")
print("  DO NOT interpret grid gap as a phase cost.")
print("  FROZEN RESULT: the correctly optimized feasible problem recovers CP19 Task 4 exactly.")

print("\nrho_min(kappa) — coarse feasible-grid diagnostic")
print(f"{'kappa':>8} {'gereken h':>11} {'rho_min(grid)':>14} {'(r1*,r2*)':>20}")
for kap in ('1.06','1.5','2.0','2.5','2.784','2.9'):
    k=mpf(kap); hedef=A/k; en=None
    for i in range(41):
        for j in range(41):
            r1,r2=M1*i/41,M2*j/41; v=h(r1,r2)
            if v is not None and v>=hedef:
                t=r1+r2
                if en is None or t<en[0]: en=(t,r1,r2)
    if en:
        print(f"{kap:>8} {mp.nstr(hedef,8):>11} {mp.nstr(en[0],7):>14} ({mp.nstr(en[1],4)}, {mp.nstr(en[2],4)})")
    else:
        print(f"{kap:>8} {mp.nstr(hedef,8):>11} {'not found':>14}")

print("\nCP19 Task-5 status: NOT EXCLUDED — HYPOTHESIS MISMATCH.")
