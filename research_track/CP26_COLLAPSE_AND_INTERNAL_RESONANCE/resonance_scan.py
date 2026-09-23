#!/usr/bin/env python3
"""Exact finite near-resonance scan; no divisibility/integrality filtering.

Run: python3 resonance_scan.py [--max-k 18] [--seconds-per-k 600]
All decisions use integers or Fraction. Floats occur only during JSON reporting.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

INTEGRALITY_FILTER_USED = False
assert INTEGRALITY_FILTER_USED is False


def primitive_necklaces(k, total):
    """FKM recursion: one lexicographically least word per primitive necklace.

    Sum pruning is exact; p == k ensures aperiodicity. Alphabet is positive.
    """
    a = [0] * (k + 1)

    def walk(t, p, remaining):
        if t > k:
            if p == k and remaining == 0:
                yield tuple(a[1:])
            return
        upper = remaining - (k - t)
        low = a[t - p]
        if low >= 1 and low <= upper:
            a[t] = low
            yield from walk(t + 1, p, remaining - low)
        for value in range(max(low + 1, 1), upper + 1):
            a[t] = value
            yield from walk(t + 1, t, remaining - value)

    yield from walk(1, 1, total)


def exact_quantiles(values):
    if not values:
        return {key: None for key in ('min', 'q25', 'median', 'q75', 'max')}
    values.sort()
    n = len(values)
    indices = (0, (n - 1) // 4, (n - 1) // 2, 3 * (n - 1) // 4, n - 1)
    # Conversion only at the reporting boundary; all sorting and decisions exact.
    return dict(zip(('min', 'q25', 'median', 'q75', 'max'),
                    (float(values[i]) for i in indices)))


def orbit(word, b):
    k = len(word)
    m = sum(word)
    d = (1 << m) - 3 ** k
    assert b * d > 0
    denom = abs(d)
    powers = [3 ** i for i in range(k)]
    position = 0
    B = 0
    for j, gap in enumerate(word):
        B += powers[k - 1 - j] << position
        position += gap
    assert position == m
    p = B
    points = []
    for gap in word:
        points.append(p)
        numerator = 3 * p + b * denom
        quotient, remainder = divmod(numerator, 1 << gap)
        assert remainder == 0 and quotient > 0
        p = quotient
    assert p == B, 'periodic rational candidate must close'
    return points, denom, B, d


def blocks(word, points, denom):
    ends = [i for i, gap in enumerate(word) if gap >= 2]
    if not ends:
        return [], []
    starts = [(i + 1) % len(word) for i in ends]
    # Identical denominator, but deliberately compare the Fraction local minima.
    minimum = min(Fraction(points[i], denom) for i in starts)
    start = next(i for i in starts if Fraction(points[i], denom) == minimum)
    ordered = []
    nstates = []
    index = start
    while True:
        initial = index
        s = 1
        while word[index] == 1:
            index = (index + 1) % len(word)
            s += 1
        last_gap = word[index]
        index = (index + 1) % len(word)
        ordered.append((s, last_gap))
        nstates.append(points[initial])
        if index == start:
            break
    assert len(ordered) == len(ends)
    assert sum(s for s, _ in ordered) == len(word)
    assert sum(s - 1 + gap for s, gap in ordered) == sum(word)
    return ordered, nstates


def measure(word, b, totals, save_example=False):
    points, denom, B, D = orbit(word, b)
    ordered, nstates = blocks(word, points, denom)
    if not ordered:
        totals['q0_skipped'] += 1
        return
    totals['candidates'] += 1
    q = len(ordered)
    n0 = Fraction(nstates[0], denom)
    assert n0 == min(Fraction(p, denom) for p in nstates)
    pow3, pow2, C_num = 1, 1, 0  # A_t=pow3/pow2; C_t=C_num/pow2
    S, E = 0, 0
    first = None
    crossing_count = 0
    open_interval = None
    for t, (s, gap) in enumerate(ordered, start=1):
        e = s - 1 + gap
        three_s = 3 ** s
        C_num = three_s * C_num + (three_s - (1 << s)) * pow2
        pow3 *= three_s
        pow2 <<= e
        S += s
        E += e
        target = nstates[t % q]
        # Exact affine identity, including closing prefix. Both sides built
        # independently: integer orbit above versus block affine coefficients.
        assert target * pow2 == pow3 * nstates[0] + b * C_num * denom, (word, b, t)
        A = Fraction(pow3, pow2)
        C = Fraction(C_num, pow2)
        assert Fraction(target, denom) == A * n0 + b * C, (word, b, t)
        if t < q:
            if b == 1:
                if (A - 1) * n0 + C < 0:
                    totals['theorem_violations'] += 1
            else:
                if A <= 1:
                    totals['proper_prefix_A_le_1'] += 1
                    totals['theorem_violations'] += 1
                if (A - 1) * n0 - C < 0:
                    totals['theorem_violations'] += 1
        if b == 1:
            below = pow3 < pow2
            previous_below = (pow3 // three_s) < (pow2 >> e)
            if below and not previous_below:
                crossing_count += 1
                open_interval = S
            if previous_below and not below:
                assert open_interval is not None
                totals['S_intervals'][f'{open_interval}:{S}'] += 1
                open_interval = None
            if first is None and below:
                first = (t, S, C / n0)
    assert S == len(word) and E == sum(word)
    if b == 1:
        if open_interval is not None:
            totals['S_intervals'][f'{open_interval}:{S}'] += 1
        totals['crossings_histogram'][str(crossing_count)] += 1
        if first is None:
            totals['first_crossing_missing'] += 1
        else:
            t, first_S, ratio = first
            totals['S_over_K'].append(Fraction(first_S, len(word)))
            totals['t_over_q'].append(Fraction(t, q))
            totals['C_over_n0'].append(ratio)
            totals['full_cycle_count'] += (t == q)
    if save_example:
        return {'word': list(word), 'orbit': [str(Fraction(p, denom)) for p in points],
                'blocks': [list(z) for z in ordered], 'q': q,
                'integral_label_only': (B % abs(D) == 0)}


def control_cases():
    controls = {}
    examples = [(5, 7), (17, 25, 37, 55, 41, 61, 91)]
    for cycle in examples:
        gaps = []
        for x, y in zip(cycle, cycle[1:] + cycle[:1]):
            numerator = 3 * x - 1
            assert numerator % y == 0
            quotient = numerator // y
            assert quotient > 0 and quotient & (quotient - 1) == 0
            gaps.append(quotient.bit_length() - 1)
        word = tuple(gaps)
        assert word in ((1, 2), (1, 1, 1, 2, 1, 1, 4))
        report = {'candidates': 0, 'q0_skipped': 0, 'theorem_violations': 0,
                  'proper_prefix_A_le_1': 0}
        detail = measure(word, -1, report, True)
        assert report['theorem_violations'] == report['proper_prefix_A_le_1'] == 0
        assert tuple(int(Fraction(x)) for x in detail['orbit']) == cycle
        supplied = (1, 2) if len(cycle) == 2 else (1, 1, 2, 1, 1, 1, 4)
        supplied_is_rotation = any(word == supplied[i:] + supplied[:i] for i in range(len(word)))
        controls[str(cycle)] = {'given_gaps': list(supplied), 'given_gaps_are_rotation': supplied_is_rotation,
                                 'verified_gaps': list(word), 'verified_cycle': True,
                                 'scan': report, 'details': detail}
    # This is outside K >= 2; n=1 is the actual b=-1 fixed point, q=0.
    trivial = {'candidates': 0, 'q0_skipped': 0, 'theorem_violations': 0}
    trivial_detail = measure((1,), -1, trivial, True)
    assert trivial_detail is None and Fraction(3 * 1 - 1, 2) == 1
    controls['trivial_x1'] = {'b': -1, 'word': [1], 'q': 0, 'scan': trivial}
    # One single change to the first example: periodic extension of its
    # original starting point fails to close. Local affine identities remain
    # true even for NON-periodic trajectories; do not falsely claim otherwise.
    original = (1, 2)
    damaged = (1, 1)
    original_start = Fraction(5)
    step1 = (3 * original_start - 1) / 2
    ending = (3 * step1 - 1) / 2
    assert ending != original_start
    rational_points, den, _, _ = orbit(damaged, -1)
    controls['single_gap_perturbation'] = {
        'original_word': list(original), 'changed_word': list(damaged),
        'original_start': str(original_start), 'original_start_after_changed_word': str(ending),
        'original_cycle_does_not_close': True,
        'changed_word_rational_candidate_start': str(Fraction(rational_points[0], den)),
        'changed_word_has_own_periodic_rational_candidate': True,
        'closing_affine_identity_at_original_start_fails': True,
        'local_affine_identity_is_universal_not_claimed_broken': True}
    return controls


def empty_counts(b):
    common = {'candidates': 0, 'q0_skipped': 0, 'theorem_violations': 0}
    if b == -1:
        common['proper_prefix_A_le_1'] = 0
    else:
        common.update(first_crossing_missing=0, full_cycle_count=0,
                      S_over_K=[], t_over_q=[], C_over_n0=[],
                      crossings_histogram=Counter(), S_intervals=Counter())
    return common


def report_counts(counts, b):
    if b == -1:
        return counts
    n = counts['candidates'] - counts['first_crossing_missing']
    assert n == len(counts['S_over_K']) == len(counts['C_over_n0'])
    for key in ('S_over_K', 't_over_q', 'C_over_n0'):
        counts[key + '_quantiles'] = exact_quantiles(counts.pop(key))
    counts['full_cycle_crossing_fraction'] = (counts.pop('full_cycle_count') / n if n else None)
    counts['crossings_histogram'] = dict(sorted(counts['crossings_histogram'].items(), key=lambda z: int(z[0])))
    counts['S_intervals'] = dict(sorted(counts['S_intervals'].items(), key=lambda z: tuple(map(int, z[0].split(':')))))
    return counts


def self_test():
    # Independently compare generated necklaces to exhaustive enumeration for
    # small sizes; no cyclic duplicate, no imprimitive word, no missed class.
    from itertools import product
    for k in range(2, 7):
        for m in range(k + 1, k + 5):
            expected = set()
            for word in product(range(1, m - k + 2), repeat=k):
                if sum(word) != m:
                    continue
                rotations = [word[i:] + word[:i] for i in range(k)]
                if word == min(rotations) and len(set(rotations)) == k:
                    expected.add(word)
            got = list(primitive_necklaces(k, m))
            assert len(got) == len(set(got)) and set(got) == expected, (k, m)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-k', type=int, default=18)
    parser.add_argument('--seconds-per-k', type=int, default=600)
    parser.add_argument('--output', default='results.json')
    args = parser.parse_args()
    assert 2 <= args.max_k <= 18 and args.seconds_per_k > 0
    began_ns = time.monotonic_ns()
    self_test()
    controls = control_cases()
    result = {'config': {'min_K': 2, 'max_K': args.max_k,
                         'seconds_per_K_limit': args.seconds_per_k,
                         'integrality_filter_used': INTEGRALITY_FILTER_USED,
                         'enumeration': 'FKM primitive lex-min necklaces with fixed sum',
                         'quantile_method': 'sorted nearest rank at floor((n-1)*p)',
                         'crossing_interval': 'S at entrance below 1 : S at first exit to >=1, or K',
                         'completed_through_K': 1},
              'per_K': {}, 'negative_controls': controls, 'seconds': 0}
    for k in range(2, args.max_k + 1):
        t0_ns = time.monotonic_ns()
        m0 = (3 ** k).bit_length() - 1
        entry = {}
        timeout = False
        for b, m, label in ((-1, m0, 'b-1'), (1, m0 + 1, 'b+1')):
            counts = empty_counts(b)
            processed = 0
            for word in primitive_necklaces(k, m):
                if processed % 2048 == 0 and time.monotonic_ns() - t0_ns > args.seconds_per_k * 1_000_000_000:
                    timeout = True
                    break
                measure(word, b, counts)
                processed += 1
            entry[label] = report_counts(counts, b)
            entry[label]['M'] = m
            entry[label]['complete'] = not timeout
            if timeout:
                result['config']['stop_reason'] = (f'K={k} exceeded {args.seconds_per_k} seconds '
                                                    f'after {processed} b={b} necklaces')
                break
        entry['seconds'] = (time.monotonic_ns() - t0_ns) / 1_000_000_000
        result['per_K'][str(k)] = entry
        if not timeout:
            result['config']['completed_through_K'] = k
        result['seconds'] = (time.monotonic_ns() - began_ns) / 1_000_000_000
        Path(args.output).write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
        print(f'K={k} time={entry["seconds"]:.1f}s ' + ' '.join(
            f'{label}={entry[label]["candidates"]}' for label in ('b-1', 'b+1') if label in entry),
            flush=True)
        if timeout:
            break
    print('SHA-256:', hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), flush=True)


if __name__ == '__main__':
    main()
