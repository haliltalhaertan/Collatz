"""Exact-period finite-state digit-lift/Fourier checks for CP29 (no A cutoff).

Uses numpy float64 for s<=8, and Fraction for independent tiny cases.
Run: python3 cp29_fourier.py ; produces cp29_fourier.json.
"""
import json
from fractions import Fraction
import numpy as np

REFERENCE = '/mnt/c/Users/MDP/collatz-analysis/cp29_chi/chi_s_exact.json'


def geometric_residues(L):
    # P(A=r mod L), r=1,...,L (r=L encodes 0 mod L).
    return np.exp2(-np.arange(1, L + 1, dtype=float)) / (-np.expm1(-L * np.log(2.0)))


def step_brute(prev, s, sample=()):
    """Independent finite-state brute sum of (y,a) for all a modulo order L.

    Returns full p_s and phi_s(u) computed both via p and the transfer operator.
    """
    M = 3 ** s
    L = 2 * 3 ** (s-1)
    base = 3 ** (s-1)
    yy = np.arange(base, dtype=np.int64)
    w = geometric_residues(L)
    p = np.zeros(M)
    for a, wa in enumerate(w, 1):
        mult = pow(pow(2, a, M), -1, M)
        zz = (mult * (1 + 3 * yy)) % M
        p += wa * np.bincount(zz, weights=prev, minlength=M)
    # FFT convention exp(+2pi i ux/M) is obtained with ifft * M.
    fourier = np.fft.ifft(p) * M
    prev_fourier = np.fft.ifft(prev) * base
    recurrence_discrepancy = 0.
    for u in sample:
        via_transfer = 0j
        for a, wa in enumerate(w, 1):
            mult = pow(pow(2, a, M), -1, M)
            v = (u * mult) % M
            via_transfer += wa * np.exp(2j * np.pi * v / M) * prev_fourier[v % base]
        recurrence_discrepancy = max(recurrence_discrepancy, abs(via_transfer - fourier[u]))
    # q(r,t) is induced by the independent joint law J(y,a) = prev[y]w[a].
    q = p.reshape(3, base).T
    lifted = prev[:, None] / 3
    e_digits = M * np.square(q - lifted).sum()
    e_cond = base * np.sum(3 * np.square(q).sum(axis=1) - prev**2)
    primitive = np.array([u for u in range(M) if u % 3], dtype=int)
    e_fourier = np.sum(np.abs(fourier[primitive])**2)
    return p, {'s': s, 'chi': float(M * p @ p),
               'E_digit': float(e_digits), 'E_conditional': float(e_cond),
               'E_Fourier': float(e_fourier),
               'recurrence_max_error': float(recurrence_discrepancy),
               'mass_error': float(abs(sum(p) - 1)),
               'primitive_count': len(primitive)}


def exact_small(n):
    prev = [Fraction(1)]
    for s in range(1, n+1):
        M = 3**s; L = 2*3**(s-1)
        p = [Fraction(0) for _ in range(M)]
        for a in range(1, L+1):
            w = Fraction(1, 2**a - 0) / (1-Fraction(1, 2**L))
            mult = pow(pow(2,a,M),-1,M)
            for y, v in enumerate(prev):
                p[(mult*(1+3*y)) % M] += w*v
        prev = p
    return {'s': n, 'chi': str(M*sum(z*z for z in prev)),
            'p': [str(z) for z in prev]}


def run():
    reference = json.load(open(REFERENCE))
    out = {'status': 'not_proved_G1_G2_G3', 'source': 'https://arxiv.org/html/1909.03562 (and https://arxiv.org/pdf/1909.03562), primary text; Lemma 6.2, Proposition 1.17, equation (1.29)',
           'independent_reference': REFERENCE, 'finite_period_no_A_truncation': True,
           'tests': [], 'exact': [exact_small(s) for s in range(1,4)],
           'identities': {
             'weights': 'w_s(a)=2^{-a}/(1-2^{-L_s}), 1<=a<=L_s, L_s=2*3^(s-1)',
             'fourier': 'phi_s(u)=sum_a w_s(a) exp(2*pi*i*u*2^(-a)/3^s) phi_(s-1)(u*2^(-a) mod 3^(s-1))',
             'joint': 'J_s(y,a)=p_(s-1)(y) w_s(a); q_s(r,t)=sum_{y,a:2^(-a)(1+3y)=r+t*3^(s-1) mod 3^s} J_s(y,a)',
             'conditional': 'E_s=3^(s-1) sum_r p_(s-1)(r)^2 [3 sum_t pi_s(t|r)^2-1], pi=q_s(r,t)/p_(s-1)(r)',
             'unconditional_bound': '0<=E_s<=2 chi_(s-1) (insufficient for G1,G2)'},
           'primary_quotes': {
              'lemma_6_2': 'For each natural number n, the n-Syracuse offset map F_n:(N+1)^n -> Z[1/2] is injective.',
              'prop_1_17': 'Let n >= 1, and let xi in Z/3^n Z be not divisible by 3. Then E e^(-2 pi i xi Syrac(Z/3^n Z)/3^n) <<_A n^(-A) for any fixed A > 0.'}}
    prev = np.ones(1)
    chi_prev = 1.
    for s in range(1,9):
        M = 3**s
        p, rec = step_brute(prev, s, sample=(1, 2, M-1))
        rec['E_difference'] = rec['chi'] - chi_prev
        rec['chi_reference'] = reference[s-1]['chi']
        rec['E_reference'] = reference[s-1]['E']
        rec['max_difference'] = max(abs(rec['chi']-rec['chi_reference']),
             *(abs(rec[k]-rec['E_difference']) for k in ('E_digit','E_conditional','E_Fourier')),
             abs(rec['E_difference']-rec['E_reference']))
        assert rec['max_difference'] < 2.e-9, rec
        assert rec['recurrence_max_error'] < 2.e-9, rec
        assert rec['mass_error'] < 2.e-10, rec
        assert rec['E_digit'] <= 2*chi_prev+1.e-10, rec
        out['tests'].append(rec)
        print(s, rec['chi'], rec['E_digit'], rec['max_difference'], flush=True)
        prev = p; chi_prev = rec['chi']
    # Counterexample: same (X_1 mod 3, S_2 mod 6), different X_2 mod 9.
    ce = []
    for a1,a2 in [(1,3),(3,1)]:
        x1 = pow(pow(2,a1,9),-1,9)
        x2 = (x1 + 3*pow(pow(2,a1+a2,9),-1,9))%9
        ce.append({'a1':a1,'a2':a2,'X1_mod3':x1%3,'S2_mod6':(a1+a2)%6,
                   'X2_mod9':x2, 'top_digit':x2//3})
    assert ce[0]['X2_mod9'] != ce[1]['X2_mod9']
    out['counterexample_prefix_joint'] = ce
    assert [x['chi'] for x in out['exact']] == ['5/3','15/7','177005/67963']
    with open('cp29_fourier.json','w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print('written cp29_fourier.json', flush=True)


if __name__ == '__main__':
    run()
