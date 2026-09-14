"""DEFEND calibration gate -- from-scratch implementation (no ref/ imports).
Exact arithmetic only: int + fractions.Fraction. No floats.
"""
from fractions import Fraction
from math import comb

def H(x):
    return (3*x+1)//2 if (x & 1) else x//2

def prefix_hist(m, r):
    """P_{m,k,r}: dict k -> list length 2^r. Brute force over odd h<2^m."""
    R = 1 << r
    res = {k: [0]*R for k in range(1, m+1)}
    for h in range(1, 1 << m, 2):
        x = h
        k = 0
        for _ in range(m):
            if x & 1:
                x = (3*x+1)//2
                k += 1
            else:
                x //= 2
        res[k][x % R] += 1
    return res

def J(X, r):
    half = 1 << (r-1)
    tot = 0
    for u in range(half):
        d = X[u]-X[u+half]
        tot += d*d
    return Fraction(half*tot)

def Ecal(m, r, hist=None):
    if hist is None:
        hist = prefix_hist(m, r)
    tot = Fraction(0)
    for k in range(1, m+1):
        tot += J(hist[k], r)/comb(m-1, k-1)
    return tot

def transfer(P, k, s):
    N = 1 << (s+1); q = 1 << s
    ck = pow(3, k, N)
    rinv = pow(3, -1, N)
    E = [0]*q; O = [0]*q
    for z in range(q):
        E[z] = P[(2*z) % N] + P[(2*z-ck) % N]
        w = (rinv*(2*z-1)) % N
        O[z] = P[w] + P[(w-ck) % N]
    return E, O

def row(m, s, hist_hi=None, hist_out=None):
    if hist_hi is None:
        hist_hi = prefix_hist(m, s+1)
    if hist_out is None:
        hist_out = prefix_hist(m+1, s)
    I = Ecal(m, s+1, hist_hi)
    Out = Ecal(m+1, s, hist_out)
    F = Fraction(0)
    EO = {}
    for k in range(1, m+1):
        E, O = transfer(hist_hi[k], k, s)
        EO[k] = (E, O)
        F += (J(E, s)+J(O, s))/comb(m-1, k-1)
    return dict(m=m, s=s, I=I, F=F, Out=Out, L=F-I, M=F-Out,
                defect=I-Out, hist_hi=hist_hi, EO=EO)

def autocorr(P, d):
    N = len(P)
    return sum(P[u]*P[(u+d) % N] for u in range(N))

def L_terms(hist_hi, m, s):
    N = 1 << (s+1); q = 1 << s
    out = {}
    for k in range(1, m+1):
        P = hist_hi[k]
        d = pow(3, k, N)
        out[k] = Fraction(q*(autocorr(P, d)-autocorr(P, (d+q) % N)), comb(m-1, k-1))
    return out

def M_terms(EO, m, s):
    q = 1 << s
    out = {1: Fraction(0), m+1: Fraction(0)}
    for j in range(2, m+1):
        nj = comb(m-1, j-1); njm = comb(m-1, j-2)
        Ej = EO[j][0]; Oj1 = EO[j-1][1]
        D = [njm*Ej[z]-nj*Oj1[z] for z in range(q)]
        out[j] = Fraction(J(D, s), nj*njm*(nj+njm))
    return out

def generic_LM(Pdict, m, s):
    """L_lift, M_merge for ARBITRARY supports Pdict[k] (list length N). Masses n_k used as given."""
    N = 1 << (s+1); q = 1 << s
    I = sum(J(Pdict[k], s+1)/comb(m-1, k-1) for k in range(1, m+1))
    F = Fraction(0); EO = {}
    for k in range(1, m+1):
        E, O = transfer(Pdict[k], k, s)
        EO[k] = (E, O)
        F += (J(E, s)+J(O, s))/comb(m-1, k-1)
    # Out needs child P'_{m+1}; for adversaries Out is defined via merge identity instead.
    # Compute M via merge identity directly (equals F-Out by [PROVED] identity).
    M = Fraction(0); per = {}
    for j in range(2, m+1):
        nj = comb(m-1, j-1); njm = comb(m-1, j-2)
        D = [njm*EO[j][0][z]-nj*EO[j-1][1][z] for z in range(q)]
        v = Fraction(J(D, s), nj*njm*(nj+njm))
        per[j] = v; M += v
    per[1] = Fraction(0); per[m+1] = Fraction(0)
    L = F - I
    return I, F, M, L, per, EO

if __name__ == "__main__":
    ok = True
    def chk(got, want, tag):
        global ok
        good = (got == want)
        ok = ok and good
        print("  %-18s got %-10s want %-10s %s" % (tag, got, want, "OK" if good else "MISMATCH"))
    print("GATE:")
    r = row(4, 2)
    chk(r["I"], Fraction(40,3), "(4,2) I"); chk(r["F"], Fraction(16), "(4,2) F")
    chk(r["Out"], Fraction(31,3), "(4,2) Out"); chk(r["L"], Fraction(8,3), "(4,2) L")
    chk(r["M"], Fraction(17,3), "(4,2) M"); chk(r["defect"], Fraction(3), "(4,2) defect")
    r = row(3, 2)
    chk(r["I"], Fraction(12), "(3,2) I"); chk(r["F"], Fraction(12), "(3,2) F")
    chk(r["Out"], Fraction(8), "(3,2) Out"); chk(r["L"], Fraction(0), "(3,2) L")
    chk(r["M"], Fraction(4), "(3,2) M")
    r = row(2, 1)
    chk(r["I"], Fraction(4), "(2,1) I"); chk(r["F"], Fraction(4), "(2,1) F")
    chk(r["Out"], Fraction(4), "(2,1) Out"); chk(r["L"], Fraction(0), "(2,1) L")
    chk(r["M"], Fraction(0), "(2,1) M")
    # ADVERSARY 1
    P1 = {1: [0,0,1,0,0,0,0,0], 2: [1,0,0,0,0,0,0,1], 3: [0,0,0,0,1,0,0,0]}
    I, F, M, L, per, EO = generic_LM(P1, 3, 2)
    chk(L, Fraction(2), "ADV1 L"); chk(M, Fraction(2,3), "ADV1 M")
    # ADVERSARY 2
    P2 = {1: [0,0,1,0,0,0,0,0], 2: [0,3,1,0,0,0,0,0], 3: [0,3,0,0,2,0,1,0],
          4: [1,0,0,0,3,0,0,0], 5: [0,0,1,0,0,0,0,0]}
    I, F, M, L, per, EO = generic_LM(P2, 5, 2)
    chk(L, Fraction(9), "ADV2 L"); chk(M, Fraction(101,15), "ADV2 M")
    print("GATE_OK =", ok)
