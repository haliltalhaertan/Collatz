"""Exact cyclotomic integer arithmetic in Z[zeta_N], N = 2^t (t>=1).

Power basis 1, zeta, ..., zeta^(d-1) with d = N/2 = phi(N), relation zeta^d = -1.
Coefficients are fractions.Fraction (exact).  NO FLOATING POINT ANYWHERE.

Also: rigorous rational-interval sign determination for elements that are real
(i.e. fixed by complex conjugation).  Enclosures of cos/sin(2*pi*j/N) are built
from certified integer-sqrt bounds, so every reported sign is a proof.
"""
from fractions import Fraction
from math import isqrt

# ---------------------------------------------------------------- ring ------

class Cyc:
    __slots__ = ("d", "c")

    def __init__(self, d, c=None):
        self.d = d
        self.c = list(c) if c is not None else [Fraction(0)] * d

    @staticmethod
    def zero(d):
        return Cyc(d)

    @staticmethod
    def const(d, v):
        a = Cyc(d)
        a.c[0] = Fraction(v)
        return a

    @staticmethod
    def zpow(d, e):
        """zeta^e as a ring element (e any integer)."""
        e %= 2 * d
        a = Cyc(d)
        if e < d:
            a.c[e] = Fraction(1)
        else:
            a.c[e - d] = Fraction(-1)
        return a

    def __add__(self, o):
        return Cyc(self.d, [x + y for x, y in zip(self.c, o.c)])

    def __sub__(self, o):
        return Cyc(self.d, [x - y for x, y in zip(self.c, o.c)])

    def __neg__(self):
        return Cyc(self.d, [-x for x in self.c])

    def __mul__(self, o):
        if isinstance(o, Cyc):
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
            return Cyc(d, out)
        return Cyc(self.d, [x * Fraction(o) for x in self.c])

    __rmul__ = __mul__

    def scale(self, f):
        f = Fraction(f)
        return Cyc(self.d, [x * f for x in self.c])

    def conj(self):
        """complex conjugation zeta -> zeta^-1."""
        d = self.d
        out = [Fraction(0)] * d
        out[0] = self.c[0]
        for j in range(1, d):
            out[d - j] = -self.c[j]
        return Cyc(d, out)

    def is_zero(self):
        return all(x == 0 for x in self.c)

    def is_real(self):
        return (self - self.conj()).is_zero()

    def __eq__(self, o):
        return self.d == o.d and all(x == y for x, y in zip(self.c, o.c))

    def __repr__(self):
        return "Cyc(%d,%s)" % (self.d, self.c)


def norm2(a):
    """a * conj(a)  (a real, nonnegative element)."""
    return a * a.conj()


# --------------------------------------------- certified real enclosures ----

def _sqrt_iv(lo, hi, D):
    """certified rational enclosure of sqrt of [lo,hi] (0 <= lo <= hi)."""
    def _lo(x):
        p, q = x.numerator, x.denominator
        n = isqrt(p * q * D * D)
        return Fraction(n, q * D)

    def _hi(x):
        p, q = x.numerator, x.denominator
        n = isqrt(p * q * D * D) + 1
        return Fraction(n, q * D)

    return _lo(lo), _hi(hi)


def _iv_mul(a, b):
    lo1, hi1 = a
    lo2, hi2 = b
    ps = (lo1 * lo2, lo1 * hi2, hi1 * lo2, hi1 * hi2)
    return (min(ps), max(ps))


def _iv_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def _iv_sub(a, b):
    return (a[0] - b[1], a[1] - b[0])


def zeta_enclosures(N, prec=80):
    """Rational intervals enclosing (cos(2 pi j/N), sin(2 pi j/N)) for j=0..N-1.

    Built by exact half-angle recursion for cos(2 pi / N) followed by interval
    complex powers.  Every endpoint is a Fraction; the enclosure is rigorous.
    """
    D = 10 ** prec
    # cos(pi/2) = 0 ; cos(pi/2^k) = sqrt((1+cos(pi/2^(k-1)))/2)
    # 2*pi/N = pi/2^(t-1) with N = 2^t
    t = N.bit_length() - 1
    assert 1 << t == N
    c = (Fraction(0), Fraction(0))          # cos(pi/2)
    for _ in range(t - 2):
        half = ((1 + c[0]) / 2, (1 + c[1]) / 2)
        c = _sqrt_iv(half[0], half[1], D)
    c1 = c                                   # cos(2 pi / N)
    # sin = sqrt(1 - cos^2)  (2*pi/N in (0, pi/2] for N>=4)
    cc = _iv_mul(c1, c1)
    s1 = _sqrt_iv(max(Fraction(0), 1 - cc[1]), 1 - cc[0], D)
    out = [((Fraction(1), Fraction(1)), (Fraction(0), Fraction(0)))]
    cur = ((Fraction(1), Fraction(1)), (Fraction(0), Fraction(0)))
    for _ in range(1, N):
        re = _iv_sub(_iv_mul(cur[0], c1), _iv_mul(cur[1], s1))
        im = _iv_add(_iv_mul(cur[0], s1), _iv_mul(cur[1], c1))
        cur = (re, im)
        out.append(cur)
    return out


_ENC_CACHE = {}


def sign_of_real(a):
    """Exact sign (-1,0,1) of a real element of Z[zeta_N] (Q-coefficients).

    Zero test is exact (power basis is a Q-basis).  Nonzero sign is decided by
    refining rational enclosures until 0 is excluded -- guaranteed to halt.
    """
    if a.is_zero():
        return 0
    d = a.d
    N = 2 * d
    prec = 60
    while True:
        key = (N, prec)
        if key not in _ENC_CACHE:
            _ENC_CACHE[key] = zeta_enclosures(N, prec)
        enc = _ENC_CACHE[key]
        lo = Fraction(0)
        hi = Fraction(0)
        for j, coef in enumerate(a.c):
            if coef == 0:
                continue
            rlo, rhi = enc[j][0]
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


def approx_str(a, digits=24):
    """Decimal *display* string with an explicit enclosure (display only)."""
    d = a.d
    N = 2 * d
    prec = digits + 20
    key = (N, prec)
    if key not in _ENC_CACHE:
        _ENC_CACHE[key] = zeta_enclosures(N, prec)
    enc = _ENC_CACHE[key]
    lo = Fraction(0)
    hi = Fraction(0)
    for j, coef in enumerate(a.c):
        if coef == 0:
            continue
        rlo, rhi = enc[j][0]
        if coef > 0:
            lo += coef * rlo
            hi += coef * rhi
        else:
            lo += coef * rhi
            hi += coef * rlo
    scale = 10 ** digits
    nlo = (lo * scale).numerator // (lo * scale).denominator
    return "%s" % (Fraction(nlo, scale),)


def to_rational(a):
    """If a is rational (only the constant coefficient), return it, else None."""
    if all(x == 0 for x in a.c[1:]):
        return a.c[0]
    return None
