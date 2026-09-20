"""Feasibility probe for top candidate T1: bounded word-level no-cycle (m<=12).

Exact integer arithmetic only. Checks Hp (expect zero nontrivial passes),
Hm (expect witnesses, e.g. q=5 at m=3), F5 5n+1 (expect witness m=5,q=1).
"""
def Hp(x):
    return (3 * x + 1) // 2 if (x & 1) else x // 2

def Hm(x):
    return (3 * x - 1) // 2 if (x & 1) else x // 2

def F5(x):
    return (5 * x + 1) // 2 if (x & 1) else x // 2

def word_endpoint(h, m, f):
    x = h
    w = []
    for _ in range(m):
        w.append(x & 1)
        x = f(x)
    return tuple(w), x

def B3(word):
    B = 0
    for i, wi in enumerate(word):
        if wi:
            B = 3 * B + (1 << i)
    return B

def B5(word):
    B = 0
    for i, wi in enumerate(word):
        if wi:
            B = 5 * B + (1 << i)
    return B

def probe_hp(M=12):
    out = {}
    for m in range(1, M + 1):
        passes = []
        for h in range(1, 1 << m, 2):
            w, e = word_endpoint(h, m, Hp)
            k = sum(w)
            B = B3(w)
            D = (1 << m) - pow(3, k)
            if D <= 0:
                continue
            if B % D != 0:
                continue
            q = B // D
            if q <= 0 or q % 2 == 0:
                continue
            wq, eq = word_endpoint(q, m, Hp)
            if wq == w and eq == q:
                passes.append((w, k, B, D, q))
        # nontrivial = passes with q != 1
        nontriv = [p for p in passes if p[4] != 1]
        out[m] = (len(passes), len(nontriv), passes[:2])
    return out

def probe_hm(M=6):
    out = {}
    for m in range(1, M + 1):
        passes = []
        for h in range(1, 1 << m, 2):
            w, e = word_endpoint(h, m, Hm)
            k = sum(w)
            B = B3(w)
            D = (1 << m) - pow(3, k)
            if D >= 0:
                continue
            if B % (-D) != 0:
                continue
            q = B // (-D)
            if q <= 0 or q % 2 == 0:
                continue
            wq, eq = word_endpoint(q, m, Hm)
            if wq == w and eq == q:
                passes.append((w, k, B, D, q))
        out[m] = (len(passes), passes[:4])
    return out

if __name__ == "__main__":
    hp = probe_hp(12)
    print("Hp m<=12 (total_passes, nontrivial_q!=1, examples):")
    for m in sorted(hp):
        print(f"  m={m}: {hp[m][0]} {hp[m][1]} {hp[m][2]}")
    hm = probe_hm(6)
    print("Hm m<=6 (total_passes, examples):")
    for m in sorted(hm):
        print(f"  m={m}: {hm[m][0]} {hm[m][1]}")
    # 5n+1 witness
    w = (1, 1, 0, 0, 0)
    B = B5(w)
    D = (1 << 5) - pow(5, 2)
    q = B // D
    wq, eq = word_endpoint(q, 5, F5)
    print(f"F5 witness w={w} B={B} D={D} q={q} selfconsistent={wq==w and eq==q}")
    seq = [1]
    x = 1
    for _ in range(5):
        x = F5(x)
        seq.append(x)
    print(f"F5 cycle seq={seq} closed={seq[-1]==1}")
