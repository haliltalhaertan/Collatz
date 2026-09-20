"""FLANK route-B trend runner -- exact pair-Delta minima on s=4,s=5.

[EXACT COMPUTATION] Signs and identities exact (int/Fraction/Cyc).
Midpoints/intervals are display enclosures for trend discussion only.
Writes flank_Btrend.json with exact Fraction strings.
"""
import sys
sys.set_int_max_str_digits(1000000)
import os
import json
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flank_freq import decompose_row
from flank_cyc import enclosure_mid

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flank_Btrend.json")


def one_row(m, s):
    t0 = time.time()
    R = decompose_row(m, s)
    mids = {}
    ivs = {}
    for a in R["reps"]:
        mid, (lo, hi) = enclosure_mid(R["pairD"][a])
        mids[a] = mid
        ivs[a] = (str(lo), str(hi))
    amin = min(mids, key=lambda a: mids[a])
    return dict(
        m=m, s=s,
        defect=str(R["defect"]), sumPD=str(R["sumPD"]),
        idL=bool(R["idL"]), idM=bool(R["idM"]), idD=bool(R["idD"]),
        eo_ok=bool(R["eo_ok"]),
        periodic_ok=bool(R["periodic_ok"]), anti_ok=bool(R["anti_ok"]),
        pair_sign={str(a): int(R["pair_sign"][a]) for a in R["reps"]},
        perN_negatives=[int(a) for a in R["oddN"] if R["perN_sign"][a] < 0],
        min_pair=int(amin), min_mid=float(mids[amin]),
        min_interval=ivs[amin],
        all_mids={str(a): float(mids[a]) for a in R["reps"]},
        all_intervals={str(a): ivs[a] for a in R["reps"]},
        secs=time.time() - t0,
    )


if __name__ == "__main__":
    grid = [(m, 4) for m in range(5, 25)] + [(m, 5) for m in range(6, 21)]
    rows = []
    for (m, s) in grid:
        print(f"row (m={m},s={s}) ...", flush=True)
        rec = one_row(m, s)
        print(f"  defect={rec['defect']} min_pair={rec['min_pair']} "
              f"min_mid={rec['min_mid']:.6f} signs={sorted(rec['pair_sign'].values())} "
              f"perN_neg={len(rec['perN_negatives'])} idD={rec['idD']} {rec['secs']:.1f}s",
              flush=True)
        rows.append(rec)
    with open(OUT, "w") as f:
        json.dump(dict(rows=rows), f, indent=1)
    print("wrote", OUT)
