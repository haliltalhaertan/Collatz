"""Phase-sensitive Gram round 2 for the Collatz tail filter.

Exact identities/inequalities are integer/Fraction based. Decimal square roots are
used only to render finite diagnostic ratios; no floating FFT is used.

This script imports the already-reviewed exact filter/correlation tools from the
repository and recomputes the new round's checks from definitions built on them.
"""
from __future__ import annotations

from collections import defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction as F
from functools import lru_cache
from math import comb, log2
from pathlib import Path
import importlib.util, json, sys

getcontext().prec = 90
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "research_shift_recurrence_20260912"))
sys.path.insert(0, str(ROOT / "research_cross_terms_20260912"))
from exact_moment import actual_filter, cyclic_correlation_exact, moments_from_correlation
import probe

_spec = importlib.util.spec_from_file_location(
    "wcheck", ROOT / "research_w_continuation_20260912" / "check_shell_alignment.py"
)
wcheck = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(wcheck)


def dec(fr: F) -> Decimal:
    return Decimal(fr.numerator) / Decimal(fr.denominator)


def dsqrt(fr: F) -> Decimal:
    if fr < 0:
        raise ValueError(fr)
    return dec(fr).sqrt()


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


@lru_cache(None)
def moments(t: int, j: int, s: int) -> tuple[int, int]:
    if not (1 <= s <= t and 0 <= j <= t):
        return 0, 0
    v = actual_filter(t, j, s)
    corr, _ = cyclic_correlation_exact(v)
    m = moments_from_correlation(corr)
    return int(m["primitive_second_moment"]), int(m["primitive_fourth_moment"])


@lru_cache(None)
def G(t: int, j: int, s: int, d: int) -> int:
    """G_d = sum_{a odd} |phi_j(a)|^2 |phi_{j-d}(3^{-d}a)|^2."""
    if not (1 <= s <= t and d >= 0 and 0 <= j <= t and 0 <= j-d <= t):
        return 0
    if d == 0:
        return moments(t, j, s)[1]
    q = 1 << s
    half = q // 2
    f = actual_filter(t, j, s)
    g = actual_filter(t, j-d, s)
    inv = pow(pow(3, d, q), -1, q)
    uperm = [f[(inv*z) % q] for z in range(q)]
    z = probe.cross(uperm, g)
    dz = [z[b] - z[(b+half) % q] for b in range(q)]
    return half * sum(dz[b]*dz[b] for b in range(half))


@lru_cache(None)
def H0(t: int, j: int, s: int) -> F:
    """Diagonal real-edge Gram energy at scale s.

    It equals 2^(s-1) times N_+ in the parent cross-term notation.
    The direct B/reflection construction avoids any floating spectral phase.
    """
    if not (s >= 1 and 0 <= j <= t):
        return F(0)
    T, J, S = t+1, j, s+1
    q = 1 << (S-1)
    h0 = q // 2
    g = [choose(T-S, J-k) for k in range(S+1)]
    weights = [probe.parity_weight(u, S-1) for u in range(q)]
    v = [g[k] for k in weights]
    w = [g[k+1] for k in weights]
    inv3 = pow(3, -1, q)
    U = [v[(inv3*z) % q] for z in range(q)]
    B = probe.cross(U, w)
    db = [B[b] - B[(b+h0) % q] for b in range(q)]
    RB = sum(db[h]*db[h] for h in range(h0))
    O = sum(db[(3*h+2) % q] * db[(-3*h-1) % q] for h in range(h0))
    Nplus = F(RB+O, 2)
    return F(1 << (s-1)) * Nplus


@lru_cache(None)
def Hd(t: int, j: int, s: int, d: int) -> F:
    """K_{0d}, recovered from the exact parent G_d lift identity."""
    if d == 0:
        return H0(t, j, s)
    if not (1 <= s <= t and d >= 1 and 0 <= j-d <= t):
        return F(0)
    lhs = F(G(t+1, j, s+1, d))
    base = 2*F(
        G(t, j, s, d)
        + G(t, j, s, d+1)
        + G(t, j-1, s, d-1)
        + G(t, j-1, s, d)
    )
    return (lhs-base)/8


def K3(t: int, j: int, s: int) -> list[list[F]]:
    return [
        [H0(t,j,s), Hd(t,j,s,1), Hd(t,j,s,2)],
        [Hd(t,j,s,1), H0(t,j-1,s), Hd(t,j-1,s,1)],
        [Hd(t,j,s,2), Hd(t,j-1,s,1), H0(t,j-2,s)],
    ]


def det3(M: list[list[F]]) -> F:
    a,b,c = M[0]
    d,e,f = M[1]
    g,h,i = M[2]
    return a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)


def schur_upper(M: list[list[F]]) -> tuple[F, F, F]:
    """Return center, residual-product, and actual K01.

    The rigorous upper is center + sqrt(residual_product).  No Decimal is needed
    to verify the inequality: if K01>center, square both sides exactly.
    """
    a,b,c = M[0][0], M[1][1], M[2][2]
    x,z,y = M[0][1], M[0][2], M[1][2]
    if c == 0:
        assert z == 0 and y == 0
        return F(0), a*b, x
    center = z*y/c
    ra = a-z*z/c
    rb = b-y*y/c
    assert ra >= 0 and rb >= 0
    residual = ra*rb
    if x > center:
        assert (x-center)*(x-center) <= residual
    return center, residual, x


def gram_psd_checks() -> dict:
    checked = 0
    det_zero = 0
    schur_tight = 0
    for t in range(5, 25):
        for s in range(2, min(t,8)+1):
            for j in range(2, t+1):
                M = K3(t,j,s)
                a,b,c = M[0][0], M[1][1], M[2][2]
                x,z,y = M[0][1], M[0][2], M[1][2]
                assert a >= 0 and b >= 0 and c >= 0
                assert a*b-x*x >= 0
                assert a*c-z*z >= 0
                assert b*c-y*y >= 0
                D = det3(M)
                assert D >= 0
                if D == 0:
                    det_zero += 1
                center,residual,actual = schur_upper(M)
                if actual > center:
                    if (actual-center)*(actual-center) == residual:
                        schur_tight += 1
                elif residual == 0 and actual == center:
                    schur_tight += 1
                checked += 1
    return dict(cases=checked, determinant_zero=det_zero, schur_upper_tight_cases=schur_tight)


def g1_bounds(t: int, j: int, s: int):
    """Bounds for parent G1 from child d=0,1,2 phase block."""
    if s < 3 or j < 2:
        return None
    T, S = t-1, s-1
    base = 2*F(
        G(T,j,S,1)+G(T,j,S,2)+G(T,j-1,S,0)+G(T,j-1,S,1)
    )
    actual = F(G(t,j,s,1))
    old = F(6*G(T,j,S,1)+6*G(T,j-1,S,1)+2*G(T,j,S,2)+2*G(T,j-1,S,0))
    M = K3(T,j,S)
    a,b = M[0][0],M[1][1]
    u2 = dec(base) + Decimal(8)*dsqrt(a*b)
    center,residual,_ = schur_upper(M)
    u3 = dec(base) + Decimal(8)*(dec(center)+dsqrt(residual))
    return actual,old,u2,u3


def critical_audit() -> dict:
    rho = 1/log2(3)
    rows=[]
    strict_old = 0
    strict_u2 = 0
    for t in range(8,31):
        jc = round(rho*t)
        for j in range(max(2,jc-1), min(t-1,jc+1)+1):
            for s in range(3,min(t,10)+1):
                out = g1_bounds(t,j,s)
                if out is None:
                    continue
                actual,old,u2,u3 = out
                if u3 < dec(old): strict_old += 1
                if u3 < u2: strict_u2 += 1
                rows.append(dict(
                    t=t,j=j,s=s,actual_G1=str(actual),old_phase_blind=str(old),
                    U2_display=str(u2),U3_display=str(u3),
                    U3_over_old_display=str(u3/dec(old)) if old else None,
                    U3_over_actual_display=str(u3/dec(actual)) if actual else None,
                ))
    best=min(rows,key=lambda r: Decimal(r["U3_over_old_display"]))
    worst=max(rows,key=lambda r: Decimal(r["U3_over_old_display"]))
    return dict(
        scope="t=8..30; j=round(t/log2(3)) +/-1 clipped to interior; s=3..min(t,10); exact Gram checks, Decimal only for displayed radicals",
        cases=len(rows),strictly_below_old_phase_blind=strict_old,strictly_below_2x2=strict_u2,
        best_U3_over_old=best,worst_U3_over_old=worst,rows=rows
    )


def fixed_family() -> list[dict]:
    out=[]
    for s in (4,6,8,10,12):
        actual,old,u2,u3 = g1_bounds(60,38,s)
        out.append(dict(
            t=60,j=38,s=s,actual_G1=str(actual),
            U3_over_old_display=str(u3/dec(old)),
            U3_over_actual_display=str(u3/dec(actual)),
            U2_over_old_display=str(u2/dec(old)),
        ))
    return out


def add_matrix(A,B,scale=F(1)):
    for i in range(3):
        for j in range(3):
            A[i][j] += scale*B[i][j]


def matrix_schur_display(M):
    center,residual,actual = schur_upper(M)
    upper = dec(center)+dsqrt(residual)
    return actual, upper


def source_weighted_panel(r: int) -> dict:
    pan=wcheck.panel(r)
    t=pan["t"]
    eligible=[]
    pointwise2=Decimal(0)
    actual=F(0)
    by_j=defaultdict(lambda:[[F(0) for _ in range(3)] for __ in range(3)])
    by_s=defaultdict(lambda:[[F(0) for _ in range(3)] for __ in range(3)])
    globalM=[[F(0) for _ in range(3)] for __ in range(3)]
    for row in pan["rows"]:
        j,s = row["j"],row["s"]
        w=F(row["flat"])
        if not w or j<2 or s<2:
            continue
        M=K3(t,j,s)
        eligible.append((j,s,w))
        actual += w*M[0][1]
        pointwise2 += dec(w)*dsqrt(M[0][0]*M[1][1])
        add_matrix(by_j[j],M,w)
        add_matrix(by_s[s],M,w)
        add_matrix(globalM,M,w)
    def grouped(groups):
        total=Decimal(0)
        for M in groups.values():
            _,up=matrix_schur_display(M)
            total += up
        return total
    global_up=matrix_schur_display(globalM)[1]
    j_up=grouped(by_j)
    s_up=grouped(by_s)
    act=dec(actual)
    return dict(
        r=r,t=t,eligible_rows=len(eligible),actual_weighted_H1=str(actual),
        pointwise_2x2_display=str(pointwise2),
        fixed_stratum_j_grouped_3x3_display=str(j_up),
        conductor_s_grouped_3x3_display=str(s_up),
        single_global_3x3_display=str(global_up),
        j_grouped_over_pointwise_display=str(j_up/pointwise2) if pointwise2 else None,
        j_grouped_slack_over_pointwise_slack_display=str((j_up-act)/(pointwise2-act)) if pointwise2!=act else None,
    )


def delta_base(t:int,l:int)->int:
    return choose(t-1,l)-choose(t-1,l-1)


def canon_pairs(pairs):
    return tuple(sorted(pairs))

_state_sets={}
@lru_cache(None)
def Q4(t:int,j:int,n:int,C:int,pairs:tuple)->int:
    N=1<<n
    C%=N
    pairs=canon_pairs(pairs)
    _state_sets.setdefault(n,set()).add((C,pairs))
    if n==1:
        prod=1
        for d,eps in pairs:
            prod*=delta_base(t,j-d)
        return (-1 if C&1 else 1)*prod
    q=N//2
    r=pow(3,-1,q)
    c=(4*r-1)%N
    mus=[]
    for d,eps in pairs:
        mu=(eps*pow(pow(3,d,N),-1,N))%N
        mus.append(mu)
    total=0
    for mask in range(16):
        if (C+mask.bit_count())&1:
            continue
        sm=0
        new=[]
        for i,(d,eps) in enumerate(pairs):
            if (mask>>i)&1:
                sm+=mus[i]
                new.append((d+1,eps))
            else:
                new.append((d,eps))
        num=C+c*sm
        assert num%2==0
        total += 2*Q4(t-1,j,n-1,(num//2)%q,canon_pairs(tuple(new)))
    return total


def full_phase_checks() -> dict:
    comparisons=0
    for t in range(2,10):
        for s in range(1,min(t,6)+1):
            for j in range(t+1):
                Q4.cache_clear(); _state_sets.clear()
                val=Q4(t,j,s,0,canon_pairs(((0,1),(0,1),(0,-1),(0,-1))))
                assert val==G(t,j,s,0)
                comparisons+=1
    counts=[]
    for s in range(2,13):
        Q4.cache_clear(); _state_sets.clear()
        t=max(2*s,s+2)
        j=round(t/log2(3))
        val=Q4(t,j,s,0,canon_pairs(((0,1),(0,1),(0,-1),(0,-1))))
        assert val==G(t,j,s,0)
        counts.append(dict(s=s,phase_states=Q4.cache_info().currsize,direct_residues=1<<s,
                           state_over_residues=str(F(Q4.cache_info().currsize,1<<s))))
    return dict(exact_M4_comparisons=comparisons,state_count_root_family=counts)


def nonclosure_toy() -> dict:
    return dict(
        current_magnitudes="(1,1,1) in both examples",
        current_real_edges="(sqrt(2)/2, sqrt(2)/2) in both examples",
        next_phase="lambda^2=i",
        next_diagonal_example_A="6-4*sqrt(2)",
        next_diagonal_example_B="6+4*sqrt(2)",
        conclusion="real-edge Gram plus magnitudes alone is not a closed next-scale state"
    )


def main():
    out=dict(
        status="proved local Gram lemmas + exact finite checks + scoped negative closure result",
        gram_psd=gram_psd_checks(),
        critical_g1=critical_audit(),
        fixed_family=fixed_family(),
        source_weighted=[source_weighted_panel(r) for r in (10,12,14)],
        full_phase_character_recurrence=full_phase_checks(),
        real_gram_nonclosure_toy=nonclosure_toy(),
    )
    (HERE/"RESULTS.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    summary={
        "gram_psd":out["gram_psd"],
        "critical_g1":{k:v for k,v in out["critical_g1"].items() if k!="rows"},
        "fixed_family":out["fixed_family"],
        "source_weighted":out["source_weighted"],
        "full_phase_character_recurrence":out["full_phase_character_recurrence"],
        "real_gram_nonclosure_toy":out["real_gram_nonclosure_toy"],
    }
    (HERE/"RESULTS_SUMMARY.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2))

if __name__=="__main__":
    main()
