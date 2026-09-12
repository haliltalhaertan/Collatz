"""Certified integer-convolution moments of the actual Collatz tail filter.

No FFT, floating-point reconstruction, third-party dependency, or modular prime
assumption is used. Kronecker substitution delegates multiplication to Python's
arbitrary-precision integer arithmetic; this is not an O(n log n) claim.
"""
from fractions import Fraction
from math import comb
from pathlib import Path
from time import perf_counter
import json


def parity_weight(u, s):
    k = 0
    for _ in range(s):
        bit = u & 1
        k += bit
        u = (3 * u + 1) // 2 if bit else u // 2
    return k


def actual_filter(t, j, s):
    if not 0 <= s <= t:
        raise ValueError('Require 0 <= s <= t')
    weights = [comb(t-s, j-k) if 0 <= j-k <= t-s else 0
               for k in range(s+1)]
    return [weights[parity_weight(u, s)] for u in range(1 << s)]


def cyclic_correlation_exact(v):
    """C[d] = sum_u v[u] v[u+d mod n], for nonnegative integer v.

    Each linear convolution coefficient <= sum(v[u]**2), by Cauchy-Schwarz
    applied to the two truncated/reordered vectors. Hence base B strictly
    above that sum precludes all carries between packed coefficients.
    """
    if not v or any(not isinstance(x, int) or x < 0 for x in v):
        raise ValueError('Nonempty nonnegative integer vector required')
    n = len(v)
    bound = sum(x*x for x in v)
    width = max(1, (bound.bit_length() + 7) // 8)
    # If bound is exactly a power of 256, bit_length adds the required byte.
    base = 1 << (8*width)
    assert base > bound
    packed = int.from_bytes(b''.join(x.to_bytes(width, 'little') for x in v), 'little')
    reverse = int.from_bytes(b''.join(x.to_bytes(width, 'little') for x in reversed(v)), 'little')
    product = packed * reverse
    raw = product.to_bytes((2*n-1)*width, 'little')
    coeff = [int.from_bytes(raw[p:p+width], 'little')
             for p in range(0, len(raw), width)]
    assert max(coeff) <= bound
    c = [coeff[n-1]] + [coeff[n-1+d]+coeff[d-1] for d in range(1, n)]
    assert c[0] == bound
    assert all(c[d] == c[-d] for d in range(1, n))
    assert sum(c) == sum(v)**2
    return c, {'coefficient_bound': str(bound), 'packing_bytes_per_coefficient': width,
               'packed_operand_bits_upper': 8*width*n}


def moments_from_correlation(c):
    n = len(c)
    if n < 2 or n & (n-1):
        raise ValueError('Power-of-two length >= 2 required')
    H = n//2
    second = H*(c[0]-c[H])
    fourth = H*sum((c[d]-c[d+H])**2 for d in range(H))
    concentration = Fraction(H*fourth, second*second) if second else None
    return {'primitive_second_moment': str(second),
            'primitive_fourth_moment': str(fourth),
            'C_Y_exact': str(concentration) if concentration is not None else None,
            'C_Y_display': float(concentration) if concentration is not None else None}


def direct_correlation(v):
    n = len(v)
    return [sum(v[u]*v[(u+d) % n] for u in range(n)) for d in range(n)]


def run():
    checks = []
    for t, j in [(10, 6), (12, 8), (14, 9), (60, 38)]:
        for s in range(2, 9):
            v = actual_filter(t, j, s)
            start = perf_counter()
            c, _ = cyclic_correlation_exact(v)
            packed_seconds = perf_counter()-start
            start = perf_counter()
            direct = direct_correlation(v)
            direct_seconds = perf_counter()-start
            assert c == direct
            checks.append({'t': t, 'j': j, 's': s, 'all_shifts_equal': True,
                           'packed_seconds': packed_seconds, 'direct_seconds': direct_seconds,
                           **moments_from_correlation(c)})
    # Degenerate/carry-boundary cases independently exercise packing.
    edge_checks = 0
    for v in [[0]*8, [1]*8, [16, 0], [0, 256, 0, 256], [1, 2, 3, 4], [255]*16]:
        c, _ = cyclic_correlation_exact(v)
        assert c == direct_correlation(v)
        edge_checks += 1
    panels = []
    for s in [8, 10, 12, 14]:
        start = perf_counter()
        v = actual_filter(60, 38, s)
        filter_seconds = perf_counter()-start
        start = perf_counter()
        c, certificate = cyclic_correlation_exact(v)
        correlation_seconds = perf_counter()-start
        start = perf_counter()
        m = moments_from_correlation(c)
        moment_seconds = perf_counter()-start
        row = {'t': 60, 'j': 38, 's': s, 'n': len(v), **m, **certificate,
               'filter_seconds': filter_seconds, 'correlation_seconds': correlation_seconds,
               'moment_seconds': moment_seconds}
        panels.append(row)
    record = {'scope': 'Exact finite moments of actual parity-weight filters. No uniform estimate.',
              'algorithm': 'Byte-aligned Kronecker substitution with proved no-carry bound',
              'checks': checks, 'edge_checks': edge_checks, 'panels': panels}
    path = Path(__file__).with_name('algorithm_results.json')
    path.write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps({'direct_comparisons': len(checks), 'edge_checks': edge_checks,
                      'panels': panels}, indent=2))


if __name__ == '__main__':
    run()
