"""
Step 1: DERIVED ("differentiated") parent identity + reformulation of L and M
as quadratic forms in the top-bit difference variables w.

Definitions (child level (m,s), N = 2^(s+1), q = 2^s):
    w_k[u] = P_k[u] - P_k[(u+q) % N]        (anti-periodic: w[u+q] = -w[u])

CLAIMS (each verified exactly below):
  (R1)  L_k = q * G_k(3^k) / (2 n_k),   G_k(d) = sum_{u<N} w_k[u] w_k[(u+d)%N]
        => |L_k| <= q ||w_k||^2 / (2 n_k)      (Cauchy-Schwarz, negacyclic isometry)
  (R2)  Delta_{q/2} E_op(P,s,c) = E_op(w,s,c)   and likewise for O_op
        => M_j = (q/4) * ||Y_j||^2 / (n_j n_{j-1}(n_j+n_{j-1})),
           Y_j = n_{j-1} E_op(w_j,s,3^j) - n_j O_op(w_{j-1},s,3^{j-1})   (length q)
  (R3)  DIFFERENTIATED PARENT IDENTITY:
           w_k^{(m,s)} = E_op(w'_k, s+1, 3^k) + O_op(w'_{k-1}, s+1, 3^{k-1})
        where w'_j is the parent (m-1,s+1) difference variable.
        i.e. the top-bit difference intertwines with BOTH transfer operators.
"""
import sys
from fractions import Fraction
sys.path.insert(0, r"C:\Users\MDP\collatz-analysis\induction")
from core import source, masses, L_terms, M_terms, E_op, O_op, J


def wvars(m, s):
    """w_k = Delta_q P_{m,k,s+1}, full length N=2^(s+1), anti-periodic."""
    P = source(m, s + 1)
    N = 1 << (s + 1)
    q = 1 << s
    W = []
    for k in range(0, m + 2):
        Pk = P[k] if k < len(P) else [0] * N
        W.append([Pk[u] - Pk[(u + q) % N] for u in range(N)])
    return W


def G(w, d, N):
    return sum(w[u] * w[(u + d) % N] for u in range(N))


def L_from_w(m, s):
    W = wvars(m, s)
    N = 1 << (s + 1); q = 1 << s
    n = masses(m)
    return {k: Fraction(q * G(W[k], pow(3, k, N), N), 2 * n[k]) if n[k] else Fraction(0)
            for k in range(1, m + 1)}


def M_from_w(m, s):
    W = wvars(m, s)
    n = masses(m)
    q = 1 << s
    out = {1: Fraction(0), m + 1: Fraction(0)}
    for j in range(2, m + 1):
        Ej = E_op(W[j], s, pow(3, j))
        Oj = O_op(W[j - 1], s, pow(3, j - 1))
        Y = [n[j - 1] * a - n[j] * b for a, b in zip(Ej, Oj)]
        num = Fraction(q, 4) * sum(y * y for y in Y)
        out[j] = num / (n[j] * n[j - 1] * (n[j] + n[j - 1]))
    return out


def check_differentiated_parent(m, s):
    """w_k^{(m,s)} == E'(w'_k) + O'(w'_{k-1})."""
    W = wvars(m, s)
    Wp = wvars(m - 1, s + 1)
    ok = True
    for k in range(1, m + 1):
        wpk = Wp[k] if k < len(Wp) else [0] * (1 << (s + 2))
        wpk1 = Wp[k - 1] if k - 1 < len(Wp) else [0] * (1 << (s + 2))
        rhs = [a + b for a, b in zip(E_op(wpk, s + 1, pow(3, k)),
                                     O_op(wpk1, s + 1, pow(3, k - 1)))]
        if list(W[k]) != rhs:
            ok = False
    return ok


if __name__ == "__main__":
    r1 = r2 = r3 = 0; bad = []
    for m in range(2, 14):
        for s in range(1, m):
            L1 = L_terms(source(m, s + 1), m, s); L2 = L_from_w(m, s)
            M1 = M_terms(source(m, s + 1), m, s); M2 = M_from_w(m, s)
            if L1 == L2: r1 += 1
            else: bad.append(("R1", m, s))
            if M1 == M2: r2 += 1
            else: bad.append(("R2", m, s))
            if m >= 3 and check_differentiated_parent(m, s): r3 += 1
            elif m >= 3: bad.append(("R3", m, s))
    print("R1 (L as negacyclic autocorr of w)  verified on", r1, "levels")
    print("R2 (M as norm of Y in w-variables)  verified on", r2, "levels")
    print("R3 (DIFFERENTIATED parent identity) verified on", r3, "levels")
    print("failures:", bad)

    # Cauchy-Schwarz bound sanity
    worst = None
    for m in range(2, 12):
        for s in range(1, m):
            W = wvars(m, s); N = 1 << (s + 1); q = 1 << s; n = masses(m)
            for k in range(1, m + 1):
                nrm = sum(x * x for x in W[k])
                bound = Fraction(q * nrm, 2 * n[k])
                Lk = L_from_w(m, s)[k]
                assert abs(Lk) <= bound, (m, s, k)
                if nrm:
                    rat = Fraction(Lk, bound)
                    if worst is None or rat > worst[0]:
                        worst = (rat, m, s, k)
    print("max L_k / CS-bound over scanned grid:", worst[0], "at (m,s,k)=", worst[1:])
