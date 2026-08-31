"""
Bagimsiz kontrol: CP20 Task 6, Lemma B.

Iddia: bir Syracuse yorungesinde ayni valuation kelimesi W iki farkli
konumda (u < v) geciyorsa, 2^{A(W)} sayisi (n_v - n_u) farkini tam boler.

Arsivdeki engine'lere GUVENMIYORUZ. Sifirdan yaziyoruz.
"""
from math import gcd

def syracuse(n0, steps):
    """odd-only Syracuse: n -> (3n+1)/2^a, a = v_2(3n+1). (durumlar, valuationlar)"""
    ns, avs = [n0], []
    n = n0
    for _ in range(steps):
        m = 3 * n + 1
        a = (m & -m).bit_length() - 1      # v_2(m)
        n = m >> a
        avs.append(a)
        ns.append(n)
        if n == 1:
            break
    return ns, avs

def check(n0, steps, rmin=3, rmax=14):
    ns, av = syracuse(n0, steps)
    L = len(av)
    tested = failed = 0
    for r in range(rmin, rmax + 1):
        if L < r + 2:
            break
        seen = {}
        for u in range(L - r + 1):
            W = tuple(av[u:u + r])
            if W in seen:
                for uu in seen[W]:
                    AW = sum(W)
                    diff = ns[u] - ns[uu]
                    tested += 1
                    if diff % (2 ** AW) != 0:
                        failed += 1
                        print(f"  IHLAL: n0={n0} r={r} u={uu} v={u} A(W)={AW}")
                seen[W].append(u)
            else:
                seen[W] = [u]
    return tested, failed

total_t = total_f = 0
# Uzun yorungeleri olan bircok baslangic noktasi
for n0 in range(3, 200000, 2):
    t, f = check(n0, 400)
    total_t += t
    total_f += f

print(f"Test edilen tekrar-cifti sayisi : {total_t:,}")
print(f"Bolunebilirlik ihlali            : {total_f}")
print()

# Ikinci kontrol: n_u == n_v olabiliyor mu? (Lemma B'nin ikinci yarisi)
esit = 0
for n0 in range(3, 50000, 2):
    ns, av = syracuse(n0, 400)
    gorulen = {}
    for i, x in enumerate(ns):
        if x in gorulen:
            esit += 1
        gorulen[x] = i
print(f"Ayni durumun tekrari (dongu disi): {esit}  <- 1-dongusu haric beklenen: yalnizca 1,1,1...")
