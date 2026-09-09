"""Exact rational/integer checks for displayed constants, not a depth experiment."""
from fractions import Fraction as F
from math import factorial
import json
from pathlib import Path
assert 2**158 < 3**100 < 2**159
rate_lower=-F(7,1000)+F(1001,1000)*(F(58,129)-F(1,1000))
pi_lower=F(100,159)**2*(2*F(29,79)+3*F(29,79)**2)
assert sum(F(7)**k/factorial(k) for k in range(8))>590
assert rate_lower>F(11,25)>F(5,12)
assert F(12,5)*rate_lower>1
assert pi_lower>F(4,9)
assert sum(F(5,6)**k/factorial(k) for k in range(4))>F(9,4)
out={'method':'Exact integer and rational inequalities only; no numerical path experiment',
     'checks_passed':7,'rate_lower_exact':str(rate_lower),'pi_lower_exact':str(pi_lower),
     'scientific_scope':'Supports fixed constants in analytic proof; not a formal proof checker.'}
Path(__file__).with_name('CONSTANT_CHECKS.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))
