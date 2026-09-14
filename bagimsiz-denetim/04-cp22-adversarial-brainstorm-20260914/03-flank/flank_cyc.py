"""FLANK exact cyclotomic arithmetic in Z[zeta_N], N=2^t -- from-scratch.

[EXACT COMPUTATION] Power basis 1,z,...,z^{d-1}, d=N/2, relation z^d=-1.
Coefficients are fractions.Fraction. No floats in any returned value.
Real signs via certified rational-interval enclosures (integer-sqrt bounds).
"""
from fractions import Fraction
from math import isqrt


class Zeta2:
    __slots__ = ("d", "c")

    def __init__(self, d, coeffs=None):
        self.d = d
        self.c = list(coeffs) if coeffs is not None else [Fraction(0)] * d

    @staticmethod
    def zero(d):
        return Zeta2(d)

    @staticmethod
    def one(d):
        a = Zeta2(d)
        a.c[0] = Fraction(1)
        return a

    @staticmethod
    def root(d, e):
        e %= 2 * d
        a = Zeta2(d)
        if e < d:
            a.c[e] = Fraction(1)
        else:
            a.c[e - d] = Fraction(-1)
        return a

    def __add__(self, o):
        assert self.d == o.d
        return Zeta2(self.d, [x + y for x, y in zip(self.c, o.c)])

    def __sub__(self, o):
        assert self.d == o.d
        return Zeta2(self.d, [x - y for x, y in zip(self.c, o.c)])

    def __neg__(self):
        return Zeta2(self.d, [-x for x in self.c])

    def __mul__(self, o):
        if isinstance(o, Zeta2):
            assert self.d == o.d
            d = self.d
            out = [Fraction(0)] * d
            for i, ai in enumerate(self.c):
                if ai == 0:
                    continue
                for j, bj in enumerate(o.c):
                    if bj == 0:
                        continue
                    k = i + j
                    if k < d:
                        out[k] += ai * bj
                    else:
                        out[k - d] -= ai * bj
            return Zeta2(d, out)
        f = Fraction(o)
        return Zeta2(self.d, [x * f for x in self.c])

    __rmul__ = __mul__

    def scale(self, f):
        return self * Fraction(f)

    def star(self):
        """complex conjugation: z -> z^{-1}."""
        d = self.d
        out = [Fraction(0)] * d
        out[0] = self.c[0]
        for j in range(1, d):
            out[d - j] = -self.c[j]
        return Zeta2(d, out)

    def is_zero(self):
        return all(x == 0 for x in self.c)

    def is_real(self):
        return (self - self.star()).is_zero()

    def __eq__(self, o):
        return self.d == o.d and all(x == y for x, y in zip(self.c, o.c))

    def __repr__(self):
        return f"Zeta2(d={self.d},{self.c})"


def abs2(a):
    return a * a.star()


def as_rational(a):
    if all(x == 0 for x in a.c[1:]):
        return a.c[0]
    return None


def _sqrt_bounds(lo, hi, D):
    def flo(x):
        return Fraction(isqrt(x.numerator * x.denominator * D * D),
                        x.denominator * D)

    def fhi(x):
        return Fraction(isqrt(x.numerator * x.denominator * D * D) + 1,
                        x.denominator * D)
    return flo(lo), fhi(hi)


def _mul_iv(A, B):
    opts = (A[0] * B[0], A[0] * B[1], A[1] * B[0], A[1] * B[1])
    return (min(opts), max(opts))


def _add_iv(A, B):
    return (A[0] + B[0], A[1] + B[1])


def _sub_iv(A, B):
    return (A[0] - B[1], A[1] - B[0])


def _zeta_intervals(N, prec):
    t = N.bit_length() - 1
    assert 1 << t == N and t >= 1
    D = 10 ** prec
    # cos(pi/2)=0; halve angles down to 2pi/N
    c = (Fraction(0), Fraction(0))
    for _ in range(t - 2):
        half = ((Fraction(1) + c[0]) / 2, (Fraction(1) + c[1]) / 2)
        c = _sqrt_bounds(half[0], half[1], D)
    c1 = c
    cc = _mul_iv(c1, c1)
    s1 = _sqrt_bounds(max(Fraction(0), 1 - cc[1]), 1 - cc[0], D)
    table = [((Fraction(1), Fraction(1)), (Fraction(0), Fraction(0)))]
    cur = table[0]
    for _ in range(1, N):
        re = _sub_iv(_mul_iv(cur[0], c1), _mul_iv(cur[1], s1))
        im = _add_iv(_mul_iv(cur[0], s1), _mul_iv(cur[1], c1))
        cur = (re, im)
        table.append(cur)
    return table


_ENC = {}


def certified_sign(a):
    """[EXACT COMPUTATION] Exact sign of a real element: 0 exact, else enclosure."""
    if a.is_zero():
        return 0
    assert a.is_real(), "sign only defined for real elements"
    N = 2 * a.d
    prec = 60
    while True:
        key = (N, prec)
        if key not in _ENC:
            _ENC[key] = _zeta_intervals(N, prec)
        tab = _ENC[key]
        lo = Fraction(0)
        hi = Fraction(0)
        for j, coef in enumerate(a.c):
            if coef == 0:
                continue
            rlo, rhi = tab[j % N][0]
            if coef > 0:
                lo += coef * rlo
                hi += coef * rhi
            else:
                lo += coef * rhi
                hi += coef * rlo
        if lo > 0:
            return 1
        if hi < 0:
            return -1
        prec *= 3
        if prec > 60 * 27:
            raise RuntimeError("enclosure did not resolve sign")


def enclosure_mid(a, digits=24):
    """Display-only float-like enclosure midpoint (NOT a claimed result)."""
    N = 2 * a.d
    key = (N, digits + 20)
    if key not in _ENC:
        _ENC[key] = _zeta_intervals(N, digits + 20)
    tab = _ENC[key]
    lo = Fraction(0)
    hi = Fraction(0)
    for j, coef in enumerate(a.c):
        if coef == 0:
            continue
        rlo, rhi = tab[j % N][0]
        if coef > 0:
            lo += coef * rlo
            hi += coef * rhi
        else:
            lo += coef * rhi
            hi += coef * rlo
    return float(lo + hi) / 2.0, (lo, hi)
