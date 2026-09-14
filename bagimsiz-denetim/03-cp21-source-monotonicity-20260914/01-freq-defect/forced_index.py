"""THE STRUCTURAL FACT that decides this question.

CLAIM [PROOF, verified exactly below on the whole grid]:
    For every k and every odd xi,   Ehat_k(xi) = Ehat_k(xi + q)
                                    Ohat_k(xi) = Ohat_k(xi + q),   q = 2^s.
  Reason: E_k and O_k are functions on Z/q.  Their Fourier transform is
  q-periodic in the frequency by construction.  Therefore the MERGE side
  carries NO information at the mod-N level: any split of M_merge between the
  two lifts xi and xi+q of a class a mod q is an arbitrary convention, not a
  decomposition of the merge energy.

CONTRAST [PROOF, verified]:  cos(2 pi c_k (xi+q)/N) = - cos(2 pi c_k xi / N),
  so the LIFT side is ANTI-periodic: L^(xi) and L^(xi+q) are genuinely
  different, and only their SUM is an intrinsic quantity attached to a mod q.

CONSEQUENCE.  The unique index on which both M^(a) and L^(a) are well defined
  is  a odd mod q = 2^s.  Refining to mod N = 2^(s+1) forces you to invent a
  merge split; with the natural even split M^(xi)=M^(xi+q)=M^(a)/2 you compare
  half the merge mass against an anti-periodic lift piece, and the sign becomes
  an artefact of that invention (it then fails on essentially every row -- see
  grid.json / gauges.py).  That is a statement about the invented refinement,
  NOT a counterexample to the conjecture.
"""
import sys, os
from fractions import Fraction
from math import comb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cyclo import Cyc, norm2, to_rational, sign_of_real
from source import row, run_gate
from freq import dft

assert run_gate(verbose=False); print("GATE OK\n")
ok_per, ok_anti = True, True
checked = 0
for s in (2, 3, 4, 5):
    for m in range(max(4, s + 1), 11):
        N = 1 << (s + 1); q = 1 << s; d = N // 2
        r = row(m, s); hist = r["hist_hi"]
        for k in range(1, m + 1):
            P = hist[k]
            A = dft([P[z] if z % 2 == 0 else 0 for z in range(N)], s + 1)
            B = dft([P[z] if z % 2 == 1 else 0 for z in range(N)], s + 1)
            ck = pow(3, k, N)
            def Eh(xi):
                return A[xi % N] + Cyc.zpow(d, xi * ck) * B[xi % N]
            def Oh(xi):
                x3 = (3 * xi) % N
                return Cyc.zpow(d, xi) * (B[x3] + Cyc.zpow(d, 3 * xi * ck) * A[x3])
            for xi in range(1, q, 2):
                if not (Eh(xi) - Eh(xi + q)).is_zero(): ok_per = False
                if not (Oh(xi) - Oh(xi + q)).is_zero(): ok_per = False
                # anti-periodicity of the lift weight
                c1 = (Cyc.zpow(d, ck * xi) + Cyc.zpow(d, -ck * xi)).scale(Fraction(1, 2))
                c2 = (Cyc.zpow(d, ck * (xi + q)) + Cyc.zpow(d, -ck * (xi + q))).scale(Fraction(1, 2))
                if not (c1 + c2).is_zero(): ok_anti = False
                checked += 1
print("MERGE-side q-periodicity  Ehat(xi)=Ehat(xi+q), Ohat(xi)=Ohat(xi+q) : %s" % ok_per)
print("LIFT-side q-ANTI-periodicity  cos(..(xi+q)..) = -cos(..xi..)       : %s" % ok_anti)
print("(%d (k,xi) pairs checked exactly over s=2..5, m up to 10)" % checked)
print()
print("=> mod-q is the FORCED common index.  A mod-N refinement of the merge")
print("   side does not exist; inventing one is what produced the earlier")
print("   'negative Delta' readings.")
