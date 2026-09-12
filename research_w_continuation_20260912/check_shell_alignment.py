"""Exact finite tail-shell budget and actual prefix alignment checks.

No floating-point DFT, no provider calls, no asymptotic inference.
"""
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def walk(x, n):
    weight = 0
    for _ in range(n):
        bit = x & 1
        weight += bit
        x = (3*x+1)//2 if bit else x//2
    return x, weight


def shell_budget(t, j, s):
    n = t-s
    return sum(comb(s-1, h) *
               (choose(n, j-h)-choose(n, j-h-1))**2
               for h in range(s))


def variances(vector):
    q = len(vector)
    previous = F(0)
    result = []
    mean = F(sum(vector), q)
    for s in range(1, q.bit_length()):
        modulus = 1 << s
        means = [F(modulus, q)*sum(vector[u::modulus])-mean
                 for u in range(modulus)]
        energy = sum(x*x for x in means)/modulus
        result.append(energy-previous)
        previous = energy
    return result


def tail_checks():
    cases = 0
    for t in range(1, 11):
        q = 1 << t
        weights = [walk(z, t)[1] for z in range(q)]
        for j in range(t+1):
            total = 0
            mass = comb(t, j)
            for s in range(1, t+1):
                modulus = 1 << s
                half = modulus//2
                aggregate = [sum(weights[z] == j for z in range(u, q, modulus))
                             for u in range(modulus)]
                actual = sum((aggregate[u]-aggregate[u+half])**2
                             for u in range(half))
                expected = shell_budget(t, j, s)
                assert actual == expected
                total += half*actual
                cases += 1
            assert shell_budget(t, j, t) == mass
            assert total == q*mass-mass*mass
    return cases


def panel(r):
    A = (3**r).bit_length()-1
    m = (6*r+4)//5
    t = A-m
    q = 1 << t
    source = Counter()
    for h in range(1, 1 << m, 2):
        y, k = walk(h, m)
        source[k, y % q] += 1
    tails = [walk(z, t)[1] for z in range(q)]
    rows = []
    W = F(0)
    Wflat = F(0)
    for k in range(max(1, r-t), min(m, r)+1):
        j = r-k
        p = [source[k, z] for z in range(q)]
        assert sum(p) == comb(m-1, k-1)
        g = [sum(p[z] for z in range(q)
                 if tails[(z+pow(3, k, q)*a) % q] == j)
             for a in range(q)]
        visible = variances(g)
        for s in range(1, t+1):
            modulus = 1 << s
            half = modulus//2
            projected = [sum(p[u::modulus]) for u in range(modulus)]
            R = sum((projected[u]-projected[u+half])**2 for u in range(half))
            D = shell_budget(t, j, s)
            flat = F(half*R*D, q*q)
            V = visible[s-1]
            # Real arrays give conjugate-pair equal magnitudes. There is one
            # orbit for s=1, and half/2 distinct pairs for every s>=2.
            pair_count = 1 if s == 1 else half//2
            assert 0 <= V <= pair_count*flat
            if s <= 2:
                assert V == flat
            alignment = V/flat if flat else None
            assert flat or V == 0
            W += V
            Wflat += flat
            rows.append(dict(k=k, j=j, s=s, R=R, D=D,
                             V=str(V), flat=str(flat),
                             alignment=str(alignment) if alignment is not None else None))
    return dict(r=r, A=A, m=m, t=t, W=str(W), Wflat=str(Wflat),
                W_over_Wflat=str(W/Wflat),
                max_alignment=max((row for row in rows if row['alignment'] is not None),
                                  key=lambda row: F(row['alignment'])), rows=rows)


if __name__ == '__main__':
    result = dict(status='exact finite checks only', tail_shell_cases=tail_checks(),
                  panels=[panel(r) for r in (5, 10, 12, 14)])
    Path(__file__).with_name('RESULTS.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(dict(tail_shell_cases=result['tail_shell_cases'],
                         panels=[{k:v for k,v in p.items() if k != 'rows'}
                                 for p in result['panels']]), indent=2))
