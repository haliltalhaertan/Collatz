"""Independent exact audit; no producer imports and no sealed-source access."""
from fractions import Fraction
from math import comb
import json

def words(total, length):
    if length == 1:
        yield (total,)
    else:
        for x in range(total + 1):
            for suffix in words(total-x, length-1):
                yield (x,) + suffix

def integer_phase(z):
    acc = 0
    prefix = 0
    for i, x in enumerate(z):
        acc += 3 ** (len(z)-i-1) * 2 ** prefix
        prefix += x+1
    return acc

counts = {"row_identity": 0, "four_prefix_identity": 0,
          "prefix_mass": 0, "prefix_tail_union": 0}
for r in range(5, 9):
    for n in range(5):
        denominator = comb(n+r-1, r-1)
        weights = [Fraction(comb(j+3,3)*comb(n-j+r-5,r-5), denominator)
                   for j in range(n+1)]
        assert sum(weights) == 1
        counts["prefix_mass"] += 1
        for cutoff in range(n+1):
            tail_mass = sum(weights[cutoff+1:])
            threshold = cutoff//4+1
            marginal = (Fraction(comb(n-threshold+r-1,r-1),denominator)
                        if threshold <= n else Fraction(0))
            assert tail_mass <= 4*marginal
            assert marginal <= Fraction(n,n+r-1)**threshold
            counts["prefix_tail_union"] += 1
        for z in words(n,r):
            B = integer_phase(z)
            phase = Fraction(B,16*3**r)
            row_phase = Fraction(1,48)
            prefix_z = z[0]
            for s in range(2,r+1):
                exponent = s+prefix_z-5
                row_phase += (Fraction(2**exponent,3**s) if exponent >= 0
                              else Fraction(1,2**(-exponent)*3**s))
                prefix_z += z[s-1]
            assert row_phase == phase
            counts["row_identity"] += 1
            J = sum(z[:4])
            split = Fraction(integer_phase(z[:4]),1296)
            split += Fraction(2**J * integer_phase(z[4:]),3**r)
            assert split == phase
            counts["four_prefix_identity"] += 1

print(json.dumps({"status":"PASS", "arithmetic":"exact Fraction and integers",
                  "range":{"r":[5,8],"n":[0,4]},"counts":counts},indent=2))
