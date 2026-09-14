"""
Step 3: THE OBSTRUCTION, made exact.

Two separate experiments.

(A) VACUITY OF THE HYPOTHESIS.  Find levels (m,s) where the PARENT (m-1,s+1)
    has total demand 0 (so IH(m-1,s+1) reads "0 <= supply": vacuous) while the
    CHILD (m,s) has strictly positive demand.  On such a level no monotone
    comparison can transport the parent statement to the child.

(B) LOGICAL NON-IMPLICATION.  The child is a deterministic image of the parent,
    so "IH does not imply the goal" must be shown over a CLASS.  Take the class
    of all parent array tuples with the correct binomial masses (the same class
    the two published adversaries live in), push them through the transfer, and
    search for a member where the PARENT inequality HOLDS for every interval but
    the CHILD inequality FAILS.  Such a witness proves: parent-inequality alone
    (+ masses + the parent identity) is logically insufficient.
"""
import sys, json, itertools
from fractions import Fraction
sys.path.insert(0, r"C:\Users\MDP\collatz-analysis\induction")
from core import masses, L_terms, M_terms, E_op, O_op, charging_violations, source
from step1_wform import L_from_w, M_from_w


def demand_supply(L, M, m, a, b, radius=2):
    demand = sum(x for x in (L[k] for k in range(a, b + 1)) if x > 0)
    lo, hi = max(a - 1, 2), min(b + radius, m)
    supply = sum(M[j] for j in range(lo, hi + 1)) if lo <= hi else Fraction(0)
    return demand, supply


# ---------------------------------------------------------------- experiment A
def expA(mmax=13):
    hits = []
    for m in range(3, mmax + 1):
        for s in range(1, m):
            Lc = L_from_w(m, s)
            Lp = L_from_w(m - 1, s + 1)
            Dc = sum(v for v in Lc.values() if v > 0)
            Dp = sum(v for v in Lp.values() if v > 0)
            if Dp == 0 and Dc > 0:
                Mc = M_from_w(m, s)
                hits.append((m, s, Dc, sum(Mc.values())))
    return hits


# ---------------------------------------------------------------- experiment B
def child_from_parent(Qs, m, s):
    """Qs[k] = parent array (length 2^(s+2)) for k=0..m-1.  Returns child P_k."""
    Np = 1 << (s + 2)
    P = [tuple([0] * (1 << (s + 1)))] * (m + 2)
    P = list(P)
    for k in range(1, m + 1):
        qk = Qs[k] if k < len(Qs) else [0] * Np
        qk1 = Qs[k - 1] if k - 1 < len(Qs) else [0] * Np
        A = E_op(qk, s + 1, pow(3, k))
        B = O_op(qk1, s + 1, pow(3, k - 1))
        P[k] = tuple(a + b for a, b in zip(A, B))
    P[0] = tuple([0] * (1 << (s + 1)))
    return P


def all_violations(L, M, m, radius=2):
    return charging_violations(L, M, m, radius)


def expB_3_2():
    """Child (3,2) <- parent (2,3).  Parent masses n'_1 = n'_2 = 1, so the parent
    is exactly a pair of point masses on Z/8.  Exhaustive: 64 configurations."""
    m, s = 3, 2
    mp, sp = 2, 3
    Np = 1 << (sp + 1)          # 16?  no: parent arrays live at modulus 2^(s+2)=2^4
    Np = 1 << (s + 2)
    out = []
    for p in range(Np):
        for r in range(Np):
            Q = [[0] * Np for _ in range(mp + 2)]
            Q[1][p] = 1
            Q[2][r] = 1
            # parent-level L',M' at level (mp,sp) -- parent modulus 2^(sp+1)=2^(s+2) OK
            Lp = L_terms(Q, mp, sp); Mp = M_terms(Q, mp, sp)
            pv = all_violations(Lp, Mp, mp)
            P = child_from_parent(Q, m, s)
            Lc = L_terms(P, m, s); Mc = M_terms(P, m, s)
            cv = all_violations(Lc, Mc, m)
            if not pv and cv:
                out.append(dict(p=p, r=r,
                                childL={k: str(v) for k, v in Lc.items()},
                                childM={k: str(v) for k, v in Mc.items()},
                                viol=[(a, b, str(d), str(su)) for a, b, d, su in cv],
                                P=[list(x) for x in P[1:m + 1]]))
    return out


def expB_general(m, s, trials, seed=12345):
    """Random search over parent tuples with correct binomial masses."""
    import random
    rnd = random.Random(seed)
    mp = m - 1
    Np = 1 << (s + 2)
    npar = masses(mp)
    found = []
    for _ in range(trials):
        Q = [[0] * Np for _ in range(mp + 2)]
        for k in range(1, mp + 1):
            for _i in range(npar[k]):
                Q[k][rnd.randrange(Np)] += 1
        Lp = L_terms(Q, mp, s + 1); Mp = M_terms(Q, mp, s + 1)
        if all_violations(Lp, Mp, mp):
            continue                     # parent already violates -> useless
        P = child_from_parent(Q, m, s)
        Lc = L_terms(P, m, s); Mc = M_terms(P, m, s)
        cv = all_violations(Lc, Mc, m)
        if cv:
            found.append(dict(Q=[list(x) for x in Q[1:mp + 1]],
                              P=[list(x) for x in P[1:m + 1]],
                              childL={k: str(v) for k, v in Lc.items()},
                              childM={k: str(v) for k, v in Mc.items()},
                              parentL={k: str(v) for k, v in Lp.items()},
                              parentM={k: str(v) for k, v in Mp.items()},
                              viol=[(a, b, str(d), str(su)) for a, b, d, su in cv]))
            if len(found) >= 3:
                break
    return found


if __name__ == "__main__":
    print("=== (A) parent demand 0 but child demand > 0 ===")
    hits = expA(13)
    for m, s, Dc, Sc in hits:
        print(f"  child (m,s)=({m},{s})  parent ({m-1},{s+1}): parentDemand=0, "
              f"childDemand={Dc}, childSupply={Sc}")
    print("  count:", len(hits))

    print()
    print("=== (B1) exhaustive parent search, child (3,2) <- parent (2,3) ===")
    w = expB_3_2()
    print("  witnesses (parent OK, child VIOLATES):", len(w))
    for x in w[:5]:
        print("   parent point masses p,r =", x["p"], x["r"])
        print("   child P_k =", x["P"])
        print("   child L =", x["childL"], " child M =", x["childM"])
        print("   violating intervals:", x["viol"])

    print()
    print("=== (B2) random parent search, larger levels ===")
    res = {}
    for (m, s, t) in [(4, 2, 6000), (5, 2, 6000), (4, 3, 4000), (5, 3, 3000), (6, 2, 4000)]:
        f = expB_general(m, s, t)
        res[f"{m},{s}"] = f
        print(f"  child ({m},{s}): witnesses found = {len(f)}")
        if f:
            x = f[0]
            print("    parent Q =", x["Q"])
            print("    child  P =", x["P"])
            print("    parentL =", x["parentL"], " parentM =", x["parentM"])
            print("    childL  =", x["childL"], " childM  =", x["childM"])
            print("    child violating intervals:", x["viol"])
    json.dump({"A": [[m, s, str(d), str(sv)] for m, s, d, sv in hits],
               "B1": w, "B2": res},
              open(r"C:\Users\MDP\collatz-analysis\induction\obstruction_report.json", "w"),
              indent=1)
