#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import hashlib

NEGATIVE_CASES = ((2,0),(2,1),(2,2),(3,0),(3,1),(4,0))

def frac_mod1(x: Fraction) -> Fraction:
    return x - (x.numerator // x.denominator)

def analytic_phase_fraction(s: int, j: int) -> Fraction:
    if s == 1 and j == 0:
        return Fraction(1,48)
    if s < 2 or j < 0:
        raise ValueError((s,j))
    e=s+j-5
    if e >= 0:
        return frac_mod1(Fraction(2**e,3**s))
    return Fraction(1,(2**(-e))*(3**s))

def inverse_correction_fraction(s: int, j: int) -> Fraction:
    e=s+j-5
    if e >= 0:
        return frac_mod1(Fraction(pow(2,e,3**s),3**s))
    t=-e
    mod=3**s
    rho=pow(2**t,-1,mod)
    h=(2**t*rho-1)//mod
    return frac_mod1(Fraction(rho,mod)-Fraction(h,2**t))

def unified_fraction(s: int, j: int) -> Fraction:
    if s == 1 and j == 0:
        return Fraction(1,48)
    if s < 2 or j < 0:
        raise ValueError((s,j))
    M=(2**max(0,5-s))*(3**s)
    R=pow(2,j+max(0,s-5),M)
    return frac_mod1(Fraction(R,M))

def weak_compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for x in range(total+1):
        for tail in weak_compositions(total-x,parts-1):
            yield (x,)+tail

def project_exponent_from_z(z):
    # Independent implementation: no import/call of sealed candidate helper.
    partial=0
    out=Fraction(1,48)
    for s in range(2,len(z)+1):
        partial += z[s-2]
        out += analytic_phase_fraction(s,partial)
    return frac_mod1(out)

def affine_offset(a):
    r=len(a)
    out=Fraction(0,1)
    for m in range(1,r+1):
        suffix=sum(a[m-1:])
        out += Fraction(3**(r-m),2**suffix)
    return out

def affine_character_exponent(a):
    r=len(a)
    T=sum(a)
    return frac_mod1(Fraction(2**T,16*3**r)*affine_offset(a))

def run_checks():
    neg=[]
    for s,j in NEGATIVE_CASES:
        aa=analytic_phase_fraction(s,j)
        bb=inverse_correction_fraction(s,j)
        cc=unified_fraction(s,j)
        if not (aa==bb==cc):
            raise AssertionError((s,j,aa,bb,cc))
        neg.append({'s':s,'j':j,'fraction':f'{aa.numerator}/{aa.denominator}'})
    # Also verify the unified representation on a wider exact grid.
    grid=0
    for s in range(2,13):
        for j in range(0,18):
            if analytic_phase_fraction(s,j) != unified_fraction(s,j):
                raise AssertionError(('grid',s,j))
            if analytic_phase_fraction(s,j) != inverse_correction_fraction(s,j):
                raise AssertionError(('inverse',s,j))
            grid += 1
    # Exhaustive finite corroboration of M3 across small weak compositions.
    cases=0
    for r in range(1,7):
        for n in range(0,7):
            for z in weak_compositions(n,r):
                a=tuple(x+1 for x in z)
                lhs=project_exponent_from_z(z)
                rhs=affine_character_exponent(a)
                if lhs != rhs:
                    raise AssertionError(('M3',r,n,z,lhs,rhs))
                cases += 1
    return {
      'negative_cases':neg,
      'unified_grid_cases':grid,
      'm3_exhaustive_small_cases':cases,
      'all_checks':'PASS'
    }

if __name__ == '__main__':
    import json
    print(json.dumps(run_checks(),indent=2,sort_keys=True))
