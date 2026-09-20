"""Re-derive R1/R2/R3 from scratch; verify on many exact levels. No ref/ imports."""
from fractions import Fraction
from math import comb
from defend_gate import prefix_hist, transfer, J, autocorr, L_terms, M_terms

def w_of(P, s):
    N = 1 << (s+1); q = 1 << s
    assert len(P) == N
    return [P[u]-P[u+q] for u in range(q)]

def Tpow(w, d, s):
    """Negacyclic shift by d: (T^d w)[u] = sgn * w[(u+d) mod q], sgn=+1 iff (u+d) mod N < q."""
    N = 1 << (s+1); q = 1 << s
    d %= N
    out = [0]*q
    for u in range(q):
        t = (u+d) % N
        sgn = 1 if t < q else -1
        out[u] = sgn*w[t % q]
    return out

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def Emap(A, k, s):
    """Same formula as transfer-E, but generic input length N -> output length q."""
    N = 1 << (s+1); q = 1 << s
    c = pow(3, k, N)
    return [A[(2*z) % N]+A[(2*z-c) % N] for z in range(q)]

def Omap(A, k, s):
    N = 1 << (s+1); q = 1 << s
    c = pow(3, k, N); rinv = pow(3, -1, N)
    out = []
    for z in range(q):
        t = (rinv*(2*z-1)) % N
        out.append(A[t]+A[(t-c) % N])
    return out

def Epar(Q, k, sp):
    """Parent operator: input length 2^(sp+1) -> output length 2^sp. Here sp=s+1."""
    Np = 1 << (sp+1); qp = 1 << sp
    c = pow(3, k, Np)
    return [Q[(2*z) % Np]+Q[(2*z-c) % Np] for z in range(qp)]

def Opar(Q, k, sp):
    Np = 1 << (sp+1); qp = 1 << sp
    c = pow(3, k, Np); rinv = pow(3, -1, Np)
    out = []
    for z in range(qp):
        t = (rinv*(2*z-1)) % Np
        out.append(Q[t]+Q[(t-c) % Np])
    return out

def check_level(m, s):
    N = 1 << (s+1); q = 1 << s
    hist = prefix_hist(m, s+1)
    L = L_terms(hist, m, s)
    # --- R1: compare L_k vs q/n*<w,Tw> and q/2n*<w,Tw>
    r1_full = {}; r1_half = {}
    for k in range(1, m+1):
        w = w_of(hist[k], s)
        Tw = Tpow(w, pow(3, k, N), s)
        ip = dot(w, Tw)
        r1_full[k] = Fraction(q*ip, comb(m-1, k-1))
        r1_half[k] = Fraction(q*ip, 2*comb(m-1, k-1))
    r1_full_ok = all(r1_full[k] == L[k] for k in range(1, m+1))
    r1_half_ok = all(r1_half[k] == L[k] for k in range(1, m+1))
    # --- R2: Y from sibling-diffs of E,O vs direct w-maps
    EO = {k: transfer(hist[k], k, s) for k in range(1, m+1)}
    M = M_terms(EO, m, s)
    r2_ok = True; r2_detail = {}
    for j in range(2, m+1):
        nj = comb(m-1, j-1); njm = comb(m-1, j-2)
        Ej, Oj1 = EO[j][0], EO[j-1][1]
        D = [njm*Ej[z]-nj*Oj1[z] for z in range(q)]
        # sibling diff length q/2
        half = q//2
        Y = [D[u]-D[u+half] for u in range(half)]
        normY = sum(y*y for y in Y)
        cand_half = Fraction((q//2)*normY, nj*njm*(nj+njm))  # (q/2)||Y||^2/den
        # w-map route: E(w_j), O(w_{j-1}) as sibling diffs of E_j,O_{j-1}?
        wj = w_of(hist[j], s); wj1 = w_of(hist[j-1], s)
        # direct: dE[u] = W[2u]+W[2u-c] with W antiperiodic extension of w
        def wext(w, t):
            t %= N
            return w[t] if t < q else -w[t-q]
        cj = pow(3, j, N); cj1 = pow(3, j-1, N)
        rinv = pow(3, -1, N)
        dE = [(wext(wj,(2*u)%N)+wext(wj,(2*u-cj)%N)) for u in range(half)]
        # check dE equals sibling diff of E_j
        dE_check = [Ej[u]-Ej[u+half] for u in range(half)]
        dO = []
        for u in range(half):
            t1 = (rinv*(2*u-1)) % N; t2 = (t1-cj1) % N
            dO.append(wext(wj1,t1)+wext(wj1,t2))
        dO_check = [Oj1[u]-Oj1[u+half] for u in range(half)]
        maps_ok = (dE == dE_check and dO == dO_check)
        Yw = [njm*dE[u]-nj*dO[u] for u in range(half)]
        assert Yw == Y  # same by construction once maps verified
        # task-formula (q/4)||Yq||^2 with Yq length-q duplicated
        normYq = 2*normY
        cand_task = Fraction(q*normYq, 4*nj*njm*(nj+njm))
        good = (cand_half == M[j] and cand_task == M[j] and maps_ok)
        r2_ok = r2_ok and good
        r2_detail[j] = (M[j], cand_half, cand_task, maps_ok)
    # --- R3: parent identity + differentiated identity (needs m>=2)
    r3_ok = None; r3d_ok = None
    if m >= 2:
        Q = prefix_hist(m-1, s+2)
        # parent identity P = Epar(Q_k)+Opar(Q_{k-1})
        r3_ok = True
        for k in range(1, m+1):
            A = Epar(Q[k] if k <= m-1 else [0]*(1 << (s+2)), k, s+1)
            B = Opar(Q[k-1] if k-1 >= 1 else [0]*(1 << (s+2)), k-1, s+1)
            lhs = list(hist[k])
            rhs = [a+b for a, b in zip(A, B)]
            if lhs != rhs:
                r3_ok = False
        # differentiated: w = Emap(w'_k)+Omap(w'_{k-1}), w' length N
        Np = 1 << (s+2)
        r3d_ok = True
        for k in range(1, m+1):
            w = w_of(hist[k], s)
            Qk = Q[k] if (1 <= k <= m-1) else [0]*Np
            Qk1 = Q[k-1] if (1 <= k-1 <= m-1) else [0]*Np
            # parent diffs length N=2^{s+1}
            Mp = 1 << (s+1)
            wk = [Qk[v]-Qk[v+Mp] for v in range(Mp)]
            wk1 = [Qk1[v]-Qk1[v+Mp] for v in range(Mp)]
            Ep = Emap(wk, k, s)
            Op = Omap(wk1, k-1, s)
            rhs = [a+b for a, b in zip(Ep, Op)]
            if rhs != w:
                r3d_ok = False
    return dict(L=L, r1_full_ok=r1_full_ok, r1_half_ok=r1_half_ok,
                r2_ok=r2_ok, r3_ok=r3_ok, r3d_ok=r3d_ok)

if __name__ == "__main__":
    levels = [(m, s) for m in range(2, 11) for s in range(1, m+1) if not (m > 8 and s > 3)]
    # cap cost: m=10,s=3 needs 2^10 loop fine; keep all m<=10
    n_full = n_half = n_r2 = n_r3 = n_r3d = 0
    bad = []
    for (m, s) in levels:
        r = check_level(m, s)
        n_full += r["r1_full_ok"]; n_half += r["r1_half_ok"]
        n_r2 += r["r2_ok"]; n_r3 += (r["r3_ok"] is True); n_r3d += (r["r3d_ok"] is True)
        if not (r["r1_full_ok"] and r["r2_ok"] and r["r3_ok"] and r["r3d_ok"]):
            bad.append((m, s, r))
        print("(m=%d,s=%d) R1_full=%s R1_half=%s R2=%s R3=%s R3d=%s" % (
            m, s, r["r1_full_ok"], r["r1_half_ok"], r["r2_ok"], r["r3_ok"], r["r3d_ok"]))
    print("levels=%d full=%d half=%d r2=%d r3=%d r3d=%d" % (len(levels), n_full, n_half, n_r2, n_r3, n_r3d))
