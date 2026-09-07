"""One bounded exploratory execution; no producer imports or floating phases."""
from fractions import Fraction
from itertools import chain
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import time

ROOT = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def compositions(n, r):
    if r == 1:
        yield (n,)
    else:
        for k in range(n + 1):
            for rest in compositions(n - k, r - 1):
                yield (k,) + rest

def b_value(a):
    # Horner recurrence gives the same polynomial with no list of phase terms.
    total, power = 0, 1
    for exponent in a:
        total = 3 * total + power
        power *= 2 ** exponent
    return total

def mod_one(q):
    return q % 1

def main():
    output = ROOT / 'RESULTS.json'
    if output.exists():
        raise RuntimeError('One-run output already exists; refusing overwrite')
    start = datetime.now(timezone.utc).isoformat()
    tick = time.perf_counter()
    cases = [(r,n) for r in range(4,9) for n in range(6)] + [(16,1)]
    input_hashes = {'plan_sha256': digest(ROOT / 'PLAN.md'),
                    'source_sha256': digest(Path(__file__))}
    failures = []
    groups = {}
    counts = {}
    residues = set()
    rows = []
    sample = None
    def check(name, passed, r, n, a):
        counts[name] = counts.get(name, 0) + 1
        if not passed:
            failures.append({'test': name, 'r': r, 'n': n, 'a': a})
    for r,n in cases:
        paths = 0
        for z in compositions(n,r):
            paths += 1
            a = tuple(x+1 for x in z)
            b = b_value(a)
            m = 3**r
            u = pow(16,-1,m)
            v = (1-16*u)//m
            check('bezout', 16*u+m*v == 1, r,n,a)
            check('crt_fraction', mod_one(Fraction(b,16*m)-Fraction(u*b,m)-Fraction(v*b,16)) == 0, r,n,a)
            prefix, tail = b_value(a[:3]), b_value(a[3:])
            s = sum(a[:3])
            check('integer_concatenation', b == 3**(r-3)*prefix+2**s*tail, r,n,a)
            check('phase_concatenation', Fraction(b,16*m) == Fraction(prefix,16*27)+Fraction(2**s*tail,16*3**(r-3)), r,n,a)
            # Four explicit terms independently test the modular Horner result.
            residue = (3**(r-1)+3**(r-2)*2**a[0]+3**(r-3)*2**sum(a[:2])+3**(r-4)*2**s)%16
            check('first_three_residue_formula', b%16 == residue, r,n,a)
            key = (r%4,) + tuple(min(x,4) for x in a[:3])
            check('residue_key_consistency', key not in groups or groups[key] == residue, r,n,a)
            groups[key] = residue
            check('oddness', b%2 == 1 and v%2 == 1, r,n,a)
            check('nontrivial_mod16_factor', mod_one(Fraction(v*b,16)) != 0, r,n,a)
            residues.add(residue)
            if r == 16 and z[0] == 1:
                sample = {'r':r,'n':n,'a':a,'B':b,'u':u,'v':v,
                          'project_exponent':str(Fraction(b,16*m)),
                          'ternary_exponent_mod1':str(mod_one(Fraction(u*b,m))),
                          'mod16_exponent_mod1':str(mod_one(Fraction(v*b,16)))}
        expected = math.comb(n+r-1,r-1)
        if paths != expected:
            failures.append({'test':'composition_count','r':r,'n':n,'actual':paths,'expected':expected})
        rows.append({'r':r,'n':n,'paths':paths,'expected_paths':expected})
    result = {'classification':'EXACT FINITE CHECKS ONLY; NOT AN ASYMPTOTIC THEOREM',
              'start_utc':start,'end_utc':datetime.now(timezone.utc).isoformat(),
              'elapsed_seconds':time.perf_counter()-tick, **input_hashes,
              'case_rows':rows,'paths_total':sum(row['paths'] for row in rows),
              'checks_by_name':counts,'failures':failures,'residue_keys':len(groups),
              'observed_B_mod16':sorted(residues),'target_sample':sample,
              'input_hashes_unchanged':input_hashes == {'plan_sha256':digest(ROOT/'PLAN.md'),'source_sha256':digest(Path(__file__))}}
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'paths':result['paths_total'],'checks':sum(counts.values()),
                      'failures':len(failures),'output_sha256':digest(output),
                      'inputs':input_hashes,'elapsed_seconds':result['elapsed_seconds']},indent=2))

if __name__ == '__main__':
    main()
