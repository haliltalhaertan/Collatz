"""Debug R3d failure on (4,2)."""
from defend_gate import prefix_hist
from defend_R import w_of, Emap, Omap, Epar, Opar

m, s = 4, 2
N = 1 << (s+1); q = 1 << s; Np = 1 << (s+2)
hist = prefix_hist(m, s+1)
Q = prefix_hist(m-1, s+2)
for k in range(1, m+1):
    w = w_of(hist[k], s)
    Qk = Q[k] if (1 <= k <= m-1) else [0]*Np
    Qk1 = Q[k-1] if (1 <= k-1 <= m-1) else [0]*Np
    Mp = 1 << (s+1)
    wk = [Qk[v]-Qk[v+Mp] for v in range(Mp)]
    wk1 = [Qk1[v]-Qk1[v+Mp] for v in range(Mp)]
    # direct diffs of parent pieces
    A = Epar(Qk, k, s+1); B = Opar(Qk1, k-1, s+1)
    dA = [A[u]-A[u+q] for u in range(q)]
    dB = [B[u]-B[u+q] for u in range(q)]
    Ep = Emap(wk, k, s); Op = Omap(wk1, k-1, s)
    print("k=%d w=%s" % (k, w))
    print("  dA=%s Ep=%s match=%s" % (dA, Ep, dA == Ep))
    print("  dB=%s Op=%s match=%s" % (dB, Op, dB == Op))
    print("  w==dA+dB:", w == [a+b for a, b in zip(dA, dB)])
