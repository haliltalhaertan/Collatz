#!/usr/bin/env python3
"""Calibration gate: implement prefix source from scratch with exact arithmetic."""
from fractions import Fraction
from math import comb

def H(x):
    return (3*x+1)//2 if (x & 1) else x//2

def histograms(m, r):
    """Return dict k -> list length 2^r. P_{m,k,r}(z) counts odd h<2^m with k odds, H^m(h)=z mod 2^r."""
    N = 1 << r
    # k ranges 1..m (since h odd, first step odd so k>=1)
    P = {k: [0]*N for k in range(1, m+1)}
    for h in range(1, 1 << m, 2):
        x = h
        k = 0
        for _ in range(m):
            if x & 1:
                k += 1
                x = (3*x+1)//2
            else:
                x = x//2
        z = x % N
        P[k][z] += 1
    return P

def J_r(vec, r):
    h = 1 << (r-1) if r >= 1 else None
    if r < 1:
        raise ValueError("r>=1 required")
    s = 0
    for u in range(1 << (r-1)):
        d = vec[u] - vec[u + (1 << (r-1))]
        s += d*d
    return Fraction(2**(r-1) * s, 1)

def Ecal(m, r):
    P = histograms(m, r)
    tot = Fraction(0, 1)
    for k in range(1, m+1):
        n_k = comb(m-1, k-1)
        tot += Fraction(J_r(P[k], r), n_k)
    return tot

def transfer_quantities(m, s):
    """Compute I, F, Out, L, M via direct definitions."""
    N = 1 << (s+1)
    q = 1 << s
    P = histograms(m, s+1)
    # I
    I = Fraction(0, 1)
    for k in range(1, m+1):
        n_k = comb(m-1, k-1)
        I += Fraction(J_r(P[k], s+1), n_k)
    # E_k, O_k on Z/q
    rinv = pow(3, -1, N)
    F = Fraction(0, 1)
    Es = {}
    Os = {}
    for k in range(1, m+1):
        n_k = comb(m-1, k-1)
        c_k = pow(3, k, N)
        E = [0]*q
        O = [0]*q
        for z in range(q):
            E[z] = P[k][(2*z) % N] + P[k][(2*z - c_k) % N]
            t = (rinv*((2*z - 1) % N)) % N
            O[z] = P[k][t] + P[k][(t - c_k) % N]
        Es[k] = E
        Os[k] = O
        F += Fraction(J_r(E, s) + J_r(O, s), n_k)
    Out = Ecal(m+1, s)
    L = F - I
    Mme = F - Out
    defect = I - Out
    return {"I": I, "F": F, "Out": Out, "L": L, "M": Mme, "defect": defect, "Es": Es, "Os": Os, "P": P}

def per_stratum(m, s):
    N = 1 << (s+1)
    q = 1 << s
    P = histograms(m, s+1)
    # L_k
    Lk = {}
    for k in range(1, m+1):
        n_k = comb(m-1, k-1)
        # cyclic autocorrelation
        # C(d) = sum_u P(u)P(u+d)
        def C(d):
            d %= N
            tot = 0
            v = P[k]
            for u in range(N):
                tot += v[u]*v[(u+d) % N]
            return tot
        ck = pow(3, k, N)
        Lk[k] = Fraction(q*(C(ck) - C((ck+q) % N)), n_k)
    # M_j via Es, Os
    tq = transfer_quantities(m, s)
    Es = tq["Es"]; Os = tq["Os"]
    Mj = {}
    Mj[1] = Fraction(0, 1)
    Mj[m+1] = Fraction(0, 1)
    for j in range(2, m+1):
        # need E_j (from P_j) and O_{j-1} (from P_{j-1})
        # n_j, n_{j-1} with n for level m
        n_j = comb(m-1, j-1)
        n_jm1 = comb(m-1, j-2)
        E = Es[j]
        O = Os[j-1]
        Y = [n_jm1*E[z] - n_j*O[z] for z in range(q)]
        # J_s(Y)
        Mj[j] = Fraction(J_r(Y, s), n_j*n_jm1*(n_j+n_jm1))
    return {"Lk": Lk, "Mj": Mj, "tq": tq}

def adv_quantities(m, s, Padvs):
    """Padvs: dict k->list length N. Compute I, F parts, L_k, M_j, L, M."""
    N = 1 << (s+1)
    q = 1 << s
    I = Fraction(0, 1)
    for k, v in Padvs.items():
        n_k = comb(m-1, k-1)
        assert sum(v) == n_k, (k, sum(v), n_k)
        I += Fraction(J_r(v, s+1), n_k)
    rinv = pow(3, -1, N)
    Es = {}; Os = {}
    F = Fraction(0, 1)
    for k, v in Padvs.items():
        n_k = comb(m-1, k-1)
        c_k = pow(3, k, N)
        E = [0]*q; O = [0]*q
        for z in range(q):
            E[z] = v[(2*z) % N] + v[(2*z - c_k) % N]
            t = (rinv*((2*z - 1) % N)) % N
            O[z] = v[t] + v[(t - c_k) % N]
        Es[k] = E; Os[k] = O
        F += Fraction(J_r(E, s) + J_r(O, s), n_k)
    # per-stratum L_k
    Lk = {}
    for k, v in Padvs.items():
        n_k = comb(m-1, k-1)
        def C(d, v=v):
            d %= N
            return sum(v[u]*v[(u+d) % N] for u in range(N))
        ck = pow(3, k, N)
        Lk[k] = Fraction(q*(C(ck) - C((ck+q) % N)), n_k)
    L = F - I
    # check sum Lk == L
    Lsum = sum(Lk.values(), Fraction(0,1))
    Mj = {}
    Mj[1] = Fraction(0,1)
    Mj[m+1] = Fraction(0,1)
    for j in range(2, m+1):
        n_j = comb(m-1, j-1); n_jm1 = comb(m-1, j-2)
        E = Es[j]; O = Os[j-1]
        Y = [n_jm1*E[z] - n_j*O[z] for z in range(q)]
        Mj[j] = Fraction(J_r(Y, s), n_j*n_jm1*(n_j+n_jm1))
    M = sum(Mj.values(), Fraction(0,1))
    return {"I": I, "F": F, "L": L, "Lk": Lk, "Lsum": Lsum, "Mj": Mj, "M": M, "Es": Es, "Os": Os}

if __name__ == "__main__":
    from fractions import Fraction
    print("=== gate (4,2) ===")
    tq = transfer_quantities(4, 2)
    print({k: str(v) for k, v in tq.items() if k in ("I","F","Out","L","M","defect")})
    print("expect I=40/3 F=16 Out=31/3 L=8/3 M=17/3 defect=3")
    ps = per_stratum(4, 2)
    print("Lk", {k: str(v) for k,v in ps["Lk"].items()})
    print("Mj", {k: str(v) for k,v in ps["Mj"].items()})
    print("sumLk", sum(ps["Lk"].values(), Fraction(0,1)), "sumMj", sum(ps["Mj"].values(), Fraction(0,1)))

    print("=== gate (3,2) ===")
    tq = transfer_quantities(3, 2)
    print({k: str(v) for k, v in tq.items() if k in ("I","F","Out","L","M","defect")})
    print("expect I=12 F=12 Out=8 L=0 M=4")
    ps = per_stratum(3, 2)
    print("Lk", {k: str(v) for k,v in ps["Lk"].items()})
    print("Mj", {k: str(v) for k,v in ps["Mj"].items()})

    print("=== gate (2,1) ===")
    tq = transfer_quantities(2, 1)
    print({k: str(v) for k, v in tq.items() if k in ("I","F","Out","L","M","defect")})
    print("expect I=F=Out=4 L=M=0")
    ps = per_stratum(2, 1)
    print("Lk", {k: str(v) for k,v in ps["Lk"].items()})
    print("Mj", {k: str(v) for k,v in ps["Mj"].items()})

    print("=== ADV1 (3,2) ===")
    P1 = [0,0,1,0,0,0,0,0]
    P2 = [1,0,0,0,0,0,0,1]
    P3 = [0,0,0,0,1,0,0,0]
    aq = adv_quantities(3, 2, {1:P1,2:P2,3:P3})
    print("L", aq["L"], "M", aq["M"], "Lk", aq["Lk"], "Mj", aq["Mj"])
    print("expect L=2 M=2/3")

    print("=== ADV2 (5,2) ===")
    Q1 = [0,0,1,0,0,0,0,0]
    Q5 = [0,0,1,0,0,0,0,0]
    Q2 = [0,3,1,0,0,0,0,0]
    Q3 = [0,3,0,0,2,0,1,0]
    Q4 = [1,0,0,0,3,0,0,0]
    aq = adv_quantities(5, 2, {1:Q1,2:Q2,3:Q3,4:Q4,5:Q5})
    print("L", aq["L"], "M", aq["M"])
    print("expect L=9 M=101/15")

    print("=== radius-1 (18,2) interval [14,14] ===")
    ps = per_stratum(18, 2)
    Lk = ps["Lk"]; Mj = ps["Mj"]
    # radius-1 window: j in [a, b+1] intersect [2,m]? with a=b=14 => j in {14,15}
    a=b=14
    demand = sum(max(Lk[k], Fraction(0,1)) for k in range(a,b+1))
    supply = sum(Mj[j] for j in range(max(a,2), min(b+1,18)+1))
    print("demand", demand, "expect 3/35")
    print("supply", supply, "expect 4033/69615")
    print("gap", demand-supply, "expect 1934/69615")
    print("Lk14", Lk[14], "Mj14", Mj.get(14), "Mj15", Mj.get(15))
