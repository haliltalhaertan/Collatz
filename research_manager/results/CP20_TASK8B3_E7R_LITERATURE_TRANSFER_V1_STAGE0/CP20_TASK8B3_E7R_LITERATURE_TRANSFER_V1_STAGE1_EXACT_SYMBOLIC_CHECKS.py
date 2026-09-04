#!/usr/bin/env python3
"""SEALED STAGE-1 SKELETON. DO NOT EXECUTE WITHOUT MANAGER AUTHORIZATION."""
import argparse
from fractions import Fraction

def require_authorization():
    p = argparse.ArgumentParser()
    p.add_argument("--authorized-stage1", action="store_true")
    p.add_argument("--seal-sha256", required=True)
    a = p.parse_args()
    if not a.authorized_stage1:
        raise SystemExit("STAGE 1 NOT AUTHORIZED")
    return a

def candidate_m3_project_exponent(z):
    """Project-side analytic exponent; comparison to literature is NOT executed."""
    partial = 0
    phi = Fraction(1, 48)
    for s in range(2, len(z)+1):
        partial += z[s-2]
        e = s + partial - 5
        term = Fraction(2**e, 3**s) if e >= 0 else Fraction(1, (2**(-e))*(3**s))
        phi += term
    return phi

def main():
    require_authorization()
    raise SystemExit("AUTHORIZED SHELL ONLY: implement M1-M8 from sealed sources.")

if __name__ == "__main__":
    main()
