"""Exact finite cylinder certificates; not a statistical trajectory experiment."""
import json
from pathlib import Path

depth = 16
modulus = 1 << depth
initial_a = 27 * modulus
certificates = []
first_hits = {}
for residue in range(modulus):
    initial_b = 20 + 27 * residue
    a, b = initial_a, initial_b
    for step in range(1, depth + 1):
        assert a % 2 == 0
        if b % 2:
            a, b = 3 * a // 2, (3 * b + 1) // 2
        else:
            a, b = a // 2, b // 2
        # All t>=0 share this parity prefix and return to S at this step.
        if a % 27 == 0 and b % 27 == 20 and a <= initial_a and b < initial_b:
            certificates.append({'k_residue': residue, 'step': step,
                                 'output_a': a, 'output_b': b})
            first_hits[step] = first_hits.get(step, 0) + 1
            break

# Independent exact rational-affine verification of every certificate.
from fractions import Fraction
for cert in certificates:
    start = 20 + 27 * cert['k_residue']
    multiplier, intercept = Fraction(1), Fraction(0)
    value = start
    for _ in range(cert['step']):
        if value % 2:
            multiplier *= Fraction(3, 2)
            intercept = (3 * intercept + 1) / 2
            value = (3 * value + 1) // 2
        else:
            multiplier /= 2
            intercept /= 2
            value //= 2
    assert multiplier * initial_a == cert['output_a']
    assert multiplier * start + intercept == cert['output_b']
    assert value == cert['output_b'] < start
    assert cert['output_a'] % 27 == 0 and value % 27 == 20

result = {'depth': depth, 'k_modulus': modulus, 'certified_classes': len(certificates),
          'unresolved_classes': modulus-len(certificates), 'first_hits': first_hits,
          'examples': certificates[:10], 'all_certificates_verified': True,
          'scope': 'Every n=20+27*(r+2^16*t), t>=0 in a certified class reaches a smaller member of S within 16 accelerated steps. Unresolved means only no certificate of this form.'}
Path(__file__).with_name('CERTIFICATES.json').write_text(json.dumps(certificates, separators=(',', ':'))+'\n', encoding='utf-8')
Path(__file__).with_name('RESULT.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, indent=2))
