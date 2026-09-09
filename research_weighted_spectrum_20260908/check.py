"""Small floating-point sanity check; RESULT.md contains the proofs."""
import json
import math
from pathlib import Path
import numpy as np

r, b = 8, 0.8
q = 3**r
L = math.floor(2**(b*r))
J = (q//(6*L)).bit_length()-1
freq = [2**j for j in range(J+1)]
x = np.arange(q)
p = (1 + sum(np.cos(2*np.pi*f*x/q) for f in freq)/(2*r))/q
phi = np.fft.ifft(p)*q
expected = np.zeros(q)
expected[0] = 1
for f in freq:
    expected[f] = expected[q-f] = 1/(4*r)
bias = float(p[:L].sum()*q/L-1)
lower = len(freq)/(4*r)
error = float(np.max(np.abs(phi-expected)))
assert abs(float(p.sum())-1)<1e-12
assert p.min()>0
assert error<1e-12
assert bias>=lower-1e-12
result = dict(r=r, b=b, q=q, L=L, frequencies=freq,
              normalization=float(p.sum()), minimum_mass=float(p.min()),
              max_fourier_error=error, relative_interval_bias=bias,
              proved_lower_bound=lower, status='PASS')
Path(__file__).with_name('CHECK.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
