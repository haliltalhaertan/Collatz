"""
Step 2: THE INDUCTION STEP.

Induction hypothesis IH(m-1, s+1):  for all intervals [a,b] in [1,m-1],
    sum_{k=a..b} max(L'_k,0)  <=  sum_{j=max(a-1,2)}^{min(b+2,m-1)} M'_j.
Goal IH(m,s).

The differentiated parent identity gives, with a_k := w'_k (parent difference vars),
    w_k = E'(a_k) + O'(a_{k-1}),                       [exact, R3]
    L_k = (q/(2 n_k)) <w_k, T^{3^k} w_k>               [exact, R1]
        = (q/(2 n_k)) ( LE_k + LO_k + LX_k ),
      LE_k = <E'a_k,   T^{3^k} E'a_k  >
      LO_k = <O'a_{k-1}, T^{3^k} O'a_{k-1}>
      LX_k = <E'a_k, T^{3^k} O'a_{k-1}> + <O'a_{k-1}, T^{3^k} E'a_k>
    M_j = (q/4) ||Y_j||^2 / (n_j n_{j-1}(n_j+n_{j-1})),
      Y_j = n_{j-1} E(w_j) - n_j O(w_{j-1})   with child-level operators.

For the step to close one needs
   (i)  DEMAND CONTRACTION : child sum max(L_k,0) <= (transfer factor) * parent demand
   (ii) SUPPLY PERSISTENCE : child M_j >= (transfer factor) * parent supply
This script measures both, exactly.
"""
import sys, json, itertools
from fractions import Fraction
sys.path.insert(0, r"C:\Users\MDP\collatz-analysis\induction")
from core import source, masses, L_terms, M_terms, E_op, O_op, J, charging_violations
from step1_wform import wvars, L_from_w, M_from_w, G


def dot_shift(x, y, d, N):
    """<x, T^d y> = sum_u x[u] y[(u+d)%N]"""
    return sum(x[u] * y[(u + d) % N] for u in range(N))


def decompose_L(m, s):
    """Exact split of child L_k into E-part, O-part, cross-part."""
    Wp = wvars(m - 1, s + 1)
    N = 1 << (s + 1); q = 1 << s
    n = masses(m)
    Np = 1 << (s + 2)
    out = {}
    for k in range(1, m + 1):
        ak = Wp[k] if k < len(Wp) else [0] * Np
        ak1 = Wp[k - 1] if k - 1 < len(Wp) else [0] * Np
        Ea = E_op(ak, s + 1, pow(3, k))
        Ob = O_op(ak1, s + 1, pow(3, k - 1))
        d = pow(3, k, N)
        LE = dot_shift(Ea, Ea, d, N)
        LO = dot_shift(Ob, Ob, d, N)
        LX = dot_shift(Ea, Ob, d, N) + dot_shift(Ob, Ea, d, N)
        tot = Fraction(q * (LE + LO + LX), 2 * n[k])
        out[k] = dict(LE=Fraction(q * LE, 2 * n[k]),
                      LO=Fraction(q * LO, 2 * n[k]),
                      LX=Fraction(q * LX, 2 * n[k]),
                      L=tot)
    return out


def analyse(m, s):
    """Compare child (m,s) and parent (m-1,s+1) charging data."""
    Lc = L_from_w(m, s); Mc = M_from_w(m, s)
    Lp = L_from_w(m - 1, s + 1); Mp = M_from_w(m - 1, s + 1)
    dec = decompose_L(m, s)
    # sanity
    for k in range(1, m + 1):
        assert dec[k]["L"] == Lc[k], (m, s, k)
    return Lc, Mc, Lp, Mp, dec


if __name__ == "__main__":
    rows = []
    print("m  s | childDemand   parentDemand  | childSupply   parentSupply | D_c/D_p  S_c/S_p")
    for m in range(3, 12):
        for s in range(1, m):
            Lc, Mc, Lp, Mp, dec = analyse(m, s)
            Dc = sum(v for v in Lc.values() if v > 0)
            Dp = sum(v for v in Lp.values() if v > 0)
            Sc = sum(Mc.values())
            Sp = sum(Mp.values())
            rows.append(dict(m=m, s=s, Dc=str(Dc), Dp=str(Dp), Sc=str(Sc), Sp=str(Sp)))
            rd = str(Fraction(Dc, Dp)) if Dp else ("inf" if Dc else "0/0")
            rs = str(Fraction(Sc, Sp)) if Sp else ("inf" if Sc else "0/0")
            print(f"{m:2d} {s:2d} | {str(Dc):>12} {str(Dp):>12} | {str(Sc):>14} {str(Sp):>14} | {rd:>10} {rs:>10}")
    json.dump(rows, open(r"C:\Users\MDP\collatz-analysis\induction\transfer_ratios.json", "w"), indent=1)
