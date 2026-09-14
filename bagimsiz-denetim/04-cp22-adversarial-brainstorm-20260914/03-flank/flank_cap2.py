"""FLANK cap part 2 -- stabilisation, mod-3 fibre, T4 sweep, dead-cap kills.

[EXACT COMPUTATION] integers/Fractions only.
"""
from fractions import Fraction
from math import comb
import json
import sys
sys.set_int_max_str_digits(1000000)
sys.path.insert(0, ".")
from flank.flank_cap import Bmod_dist, T4_bound, words_mk, B_of_word


def check_stabilisation():
    ct = json.load(open("ref/cap_table.json"))
    # group by (m,k): list over r=2..9
    from collections import defaultdict
    g = defaultdict(dict)
    for key, v in ct.items():
        m, k, r = map(int, key.split(","))
        g[(m, k)][r] = v
    bad = []
    for (m, k), d in sorted(g.items()):
        thresh = pow(3, k) - 1
        # find first r with 2^r>=thresh
        r0 = next(r for r in range(2, 30) if (1 << r) >= thresh)
        vals = [d.get(r, None) for r in range(2, 10)]
        tail = [d[r] for r in range(max(r0, 2), 10) if r in d]
        if len(set(tail)) > 1:
            bad.append(((m, k), r0, vals))
    print(f"stabilisation: {len(g)} (m,k) groups, violations={len(bad)}")
    for b in bad[:5]:
        print("  VIOL", b)
    # spot: (10,4) r0=7
    print("  (10,4) row:", {r: g[(10, 4)][r] for r in sorted(g[(10, 4)])})
    return len(bad) == 0


def check_mod3_fibre():
    print("mod-3 fibre (B_w mod 3 never 0; occupancy saturates 2*3^{k-1}):")
    for (m, k) in [(10, 4), (12, 4), (15, 5), (20, 6), (18, 6)]:
        hist = Bmod_dist(m, k)
        mods3 = {r % 3: 0 for r in hist}
        for r, c in hist.items():
            mods3[r % 3] += c
        nk = comb(m - 1, k - 1)
        print(f"  (m={m},k={k}) n={nk} occ={len(hist)} allowed={2*pow(3,k-1)} "
              f"mass_mod3={mods3} zero_class_mass={mods3.get(0,0)}")


def sweep_T4():
    Mt = json.load(open("ref/M_table.json"))
    worst = (None, Fraction(0))
    viol = []
    for key, trueM in Mt.items():
        m, k = map(int, key.split(","))
        t4 = T4_bound(m, k)
        if t4 < trueM:
            viol.append((key, t4, trueM))
        r = Fraction(t4, trueM)
        if r > worst[1]:
            worst = (key, r, t4, trueM)
    print(f"T4 sweep: {len(Mt)} entries, violations={len(viol)}, worst={worst}")
    # ratios at m-k=8 and 14 as cited
    for key in ["12,4", "18,10", "20,6"]:
        if key in Mt:
            m, k = map(int, key.split(","))
            print(f"  {key}: m-k={m-k} T4={T4_bound(m,k)} true={Mt[key]} "
                  f"ratio={Fraction(T4_bound(m,k),Mt[key])}")
    return viol


def kill_dead_caps():
    Mt = json.load(open("ref/M_table.json"))
    # dead 10: cap <= 2^(m-r) -- need cap_table at some r; find violations
    ct = json.load(open("ref/cap_table.json"))
    nviol = 0
    ex = None
    for key, v in ct.items():
        m, k, r = map(int, key.split(","))
        bound = Fraction(1 << max(m - r, 0), 1 << max(r - m, 0))
        if Fraction(v) > bound:
            nviol += 1
            if ex is None:
                ex = (key, v, str(bound))
    print(f"dead-cap-10 (cap<=2^(m-r)): violations={nviol} e.g. {ex}")
    # dead 11: cap <= absolute constant: M reaches 39
    mx = max(Mt.values())
    print(f"dead-cap-11 (absolute constant): max M={mx} at "
          f"{[k for k,v in Mt.items() if v==mx]}")


if __name__ == "__main__":
    ok1 = check_stabilisation()
    check_mod3_fibre()
    viol = sweep_T4()
    kill_dead_caps()
    print("STAB_OK =", ok1, " T4_VIOL =", len(viol))
