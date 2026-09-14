"""
CP23 chain-kill: independent verification by the lead researcher.

CLAIM UNDER TEST (REDIRECT session):
    3n+1 and 3n-1 have IDENTICAL Ecal tables, hence the identical target inequality.
    But 3n-1 provably HAS nontrivial cycles.
    => proving the target cannot exclude a cycle => the intended chain's step 3 is FALSE.

This script is written from scratch and shares no code with the agent session.
Exact arithmetic only. Run:  python cp23_chain_kill_verification.py

Collatz is NOT solved; this file contains a NEGATIVE result about a proof route.
"""
from fractions import Fraction
from math import comb


def Hp(x):                       # 3n+1 shortcut map
    return (3 * x + 1) // 2 if x & 1 else x // 2


def Hm(x):                       # 3n-1 shortcut map
    return (3 * x - 1) // 2 if x & 1 else x // 2


def H5(x):                       # 5n+1 shortcut map
    return (5 * x + 1) // 2 if x & 1 else x // 2


def Ecal(m, r, step):
    """Odd-character energy of the prefix source, exact."""
    q = 1 << r
    strata = {}
    for h in range(1, 1 << m, 2):
        x, k = h, 0
        for _ in range(m):
            if x & 1:
                k += 1
            x = step(x)
        strata.setdefault(k, [0] * q)[x % q] += 1
    total = Fraction(0)
    for k, arr in strata.items():
        half = len(arr) // 2
        J = half * sum((arr[u] - arr[u + half]) ** 2 for u in range(half))
        total += Fraction(J, comb(m - 1, k - 1))
    return total


def find_cycle(start, step, limit=200):
    x, path = start, []
    for _ in range(limit):
        path.append(x)
        x = step(x)
        if x == start:
            return path
    return None


def main():
    print("=" * 66)
    print("TEST 1 — do 3n+1 and 3n-1 share the Ecal table?")
    print("=" * 66)
    same = diff = 0
    for m in range(2, 12):
        for r in range(1, 6):
            if Ecal(m, r, Hp) == Ecal(m, r, Hm):
                same += 1
            else:
                diff += 1
                print(f"   DIFFERS at (m={m}, r={r})")
    print(f"   identical: {same}   differing: {diff}")
    assert diff == 0, "Ecal tables differ - the kill does not hold"

    print()
    print("=" * 66)
    print("TEST 2 — is the DEFECT (the target quantity) also identical?")
    print("=" * 66)
    rows = 0
    for m in range(2, 11):
        for s in range(1, min(m, 5)):
            dp = Ecal(m, s + 1, Hp) - Ecal(m + 1, s, Hp)
            dm = Ecal(m, s + 1, Hm) - Ecal(m + 1, s, Hm)
            assert dp == dm, f"defect differs at (m={m}, s={s})"
            rows += 1
    print(f"   defect identical on {rows} rows, zero differences")

    print()
    print("=" * 66)
    print("TEST 3 — does 3n-1 actually have nontrivial cycles?")
    print("=" * 66)
    for start in (5, 17):
        c = find_cycle(start, Hm)
        print(f"   start {start:>3}: cycle of length {len(c)}: {c}")
    print(f"   5n+1 cycle from 1: {find_cycle(1, H5)}")

    print()
    print("=" * 66)
    print("CONCLUSION")
    print("=" * 66)
    print("   The target inequality is IDENTICAL for 3n+1 and 3n-1.")
    print("   3n-1 has nontrivial cycles; 3n+1 (conjecturally) does not.")
    print("   Therefore no proof of the target can distinguish them,")
    print("   and it cannot exclude a cycle.")
    print()
    print("   The step 'mixing => no counterexample' is FALSE as stated.")
    print()
    print("   Structural reason: H_{3n-1}(-x) = -H_{3n+1}(x); both maps share")
    print("   the same B_w, and J_r is invariant under u -> -u + 3^k.")
    print("   The energy functional is BLIND to the sign of the affine constant")
    print("   -- precisely the datum that decides whether cycles exist.")


if __name__ == "__main__":
    main()
