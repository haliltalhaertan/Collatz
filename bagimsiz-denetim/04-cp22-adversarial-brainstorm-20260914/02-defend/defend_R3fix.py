"""Corrected differentiated parent identity (R3 fixed with explicit signs) + LE/LO/LX split.
Exact arithmetic only. No ref/ imports.
"""
from fractions import Fraction
from math import comb
from defend_gate import prefix_hist, transfer, J, autocorr, L_terms, M_terms
from defend_R import w_of, Tpow, dot, Epar, Opar

def corrected_parent_diffs(Qk, Qk1, k, s):
    """Return (A, B) length-q arrays with A=d(E^par(Qk)), B=d(O^par(Qk1)),
    plus sign arrays. Qk,Qk1 length N2=2^{s+2}."""
    N = 1 << (s+1); q = 1 << s; N2 = 1 << (s+2)
    A = Epar(Qk, k, s+1); B = Opar(Qk1, k-1, s+1)
    dA = [A[u]-A[u+q] for u in range(q)]
    dB = [B[u]-B[u+q] for u in range(q)]
    # closed-form signed maps from parent diffs Wk[v]=Qk[v]-Qk[v+N]
    Wk = [Qk[v]-Qk[v+N] for v in range(N)]
    Wk1 = [Qk1[v]-Qk1[v+N] for v in range(N)]
    cE = pow(3, k, N2); cO = pow(3, k-1, N2); rho = pow(3, -1, N2)
    sE = [0]*q; sO1 = [0]*q; sO2 = [0]*q
    fA = [0]*q; fB = [0]*q
    for u in range(q):
        v2 = (2*u-cE) % N2
        sE[u] = 1 if v2 < N else -1
        fA[u] = Wk[(2*u) % N] + sE[u]*Wk[v2 % N]
        t1 = (rho*(2*u-1)) % N2; t2 = (t1-cO) % N2
        sO1[u] = 1 if t1 < N else -1
        sO2[u] = 1 if t2 < N else -1
        fB[u] = sO1[u]*Wk1[t1 % N] + sO2[u]*Wk1[t2 % N]
    return dA, dB, fA, fB, sE, sO1, sO2

def check_corrected(m, s):
    N = 1 << (s+1); q = 1 << s; N2 = 1 << (s+2)
    hist = prefix_hist(m, s+1)
    Q = prefix_hist(m-1, s+2)
    L = L_terms(hist, m, s)
    ok_form = True; ok_split = True
    nontrivial_sign = 0; total_sign = 0
    detail = {}
    for k in range(1, m+1):
        w = w_of(hist[k], s)
        Qk = list(Q[k]) if (1 <= k <= m-1) else [0]*N2
        Qk1 = list(Q[k-1]) if (1 <= k-1 <= m-1) else [0]*N2
        dA, dB, fA, fB, sE, sO1, sO2 = corrected_parent_diffs(Qk, Qk1, k, s)
        if dA != fA or dB != fB:
            ok_form = False
        if [a+b for a, b in zip(dA, dB)] != w:
            ok_form = False
        nontrivial_sign += sum(1 for x in sE if x == -1) + sum(1 for x in sO1+sO2 if x == -1)
        total_sign += 3*q
        # LE/LO/LX split of L_k = (q/n)<w,Tw>
        Tw = lambda v: Tpow(v, pow(3, k, N), s)
        nk = comb(m-1, k-1)
        LE = dot(dA, Tw(dA)); LO = dot(dB, Tw(dB)); LX = 2*dot(dA, Tw(dB))
        if Fraction(q*(LE+LO+LX), nk) != L[k]:
            ok_split = False
        detail[k] = dict(L=L[k], LE=Fraction(q*LE, nk), LO=Fraction(q*LO, nk),
                         LX=Fraction(q*LX, nk))
    return ok_form, ok_split, nontrivial_sign, total_sign, detail

if __name__ == "__main__":
    levels = [(m, s) for m in range(2, 13) for s in range(1, m+1) if m <= 10 or s <= 2]
    nf = ns = 0; nneg = 0; ntot = 0
    lx_pure = []  # strata with LE+LO<=0 < LX (LX-driven)
    for (m, s) in levels:
        ok_form, ok_split, nneg_l, ntot_l, detail = check_corrected(m, s)
        nf += ok_form; ns += ok_split; nneg += nneg_l; ntot += ntot_l
        print("(m=%d,s=%d) corrected-R3=%s split=%s negsigns=%d/%d" % (m, s, ok_form, ok_split, nneg_l, ntot_l))
        for k, d in detail.items():
            if d["L"] > 0 and d["LE"]+d["LO"] <= 0 and d["LX"] == d["L"] - (d["LE"]+d["LO"]):
                if d["LE"]+d["LO"] <= 0 < d["LX"]:
                    lx_pure.append((m, s, k, d))
    print("levels=%d corrected-R3=%d split=%d negsigns=%d/%d" % (len(levels), nf, ns, nneg, ntot))
    print("LX-driven positive strata (LE+LO<=0<LX): %d e.g." % len(lx_pure))
    for t in lx_pure[:12]:
        print("  ", t[0], t[1], "k=%d" % t[2], {kk: str(vv) for kk, vv in t[3].items()})
