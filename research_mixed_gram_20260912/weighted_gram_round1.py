"""Mixed-Gram round 1: exact lift identity, overlap hierarchy, and falsification tests.

All inequalities and reported finite comparisons use exact integer/Fraction arithmetic.
No floating FFT is used. The script imports the repository's certified exact correlation
engine for actual-filter moments and the already-audited cross-term probe for NB/N+/N-.
"""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction
from math import comb, log2
from pathlib import Path
import importlib.util, json, sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
sys.path.insert(0,str(ROOT/"research_shift_recurrence_20260912"))
sys.path.insert(0,str(ROOT/"research_cross_terms_20260912"))
from exact_moment import actual_filter, cyclic_correlation_exact, moments_from_correlation
import probe

_spec=importlib.util.spec_from_file_location("wcheck",ROOT/"research_w_continuation_20260912"/"check_shell_alignment.py")
wcheck=importlib.util.module_from_spec(_spec); _spec.loader.exec_module(wcheck)

def C(n,k):
    return comb(n,k) if 0 <= k <= n else 0

@lru_cache(None)
def actual_moments(t:int,j:int,s:int):
    if not (1 <= s <= t and 0 <= j <= t):
        return (0,0)
    v=actual_filter(t,j,s)
    corr,_=cyclic_correlation_exact(v)
    m=moments_from_correlation(corr)
    return int(m["primitive_second_moment"]), int(m["primitive_fourth_moment"])

def actual_A(t,j,s):
    return actual_moments(t,j,s)[1]

@lru_cache(None)
def actual_G(t:int,j:int,s:int,d:int)->int:
    """G_d=sum_{a odd}|phi_j(a)|^2 |phi_{j-d}(3^{-d}a)|^2."""
    if not (1 <= s <= t and d >= 0 and 0 <= j <= t and 0 <= j-d <= t):
        return 0
    if d == 0:
        return actual_A(t,j,s)
    q=1<<s
    half=q//2
    f=actual_filter(t,j,s)
    g=actual_filter(t,j-d,s)
    inv=pow(pow(3,d,q),-1,q)
    # Cross correlation Z(b)=sum_u f(u) g(3^d u+b).
    uperm=[f[(inv*z)%q] for z in range(q)]
    Z=probe.cross(uperm,g)
    DZ=[Z[b]-Z[(b+half)%q] for b in range(q)]
    N=sum(DZ[b]**2 for b in range(half))
    return half*N

@lru_cache(None)
def U_H(t:int,j:int,s:int,d:int)->int:
    """Phase-blind closed hierarchy upper bound for G_d.

    d=0 uses the exact A recurrence with |C|<=B.
    d>=1 uses the nearest-neighbor distance recurrence proved in REPORT_TR.md.
    """
    if not (1 <= s <= t and d >= 0 and 0 <= j <= t and 0 <= j-d <= t):
        return 0
    if s == 1:
        dj=C(t-1,j)-C(t-1,j-1)
        dk=C(t-1,j-d)-C(t-1,j-d-1)
        return (dj*dk)**2
    if d == 0:
        return 2*(U_H(t-1,j,s-1,0)+U_H(t-1,j-1,s-1,0))+12*U_H(t-1,j,s-1,1)
    return (6*U_H(t-1,j,s-1,d)+6*U_H(t-1,j-1,s-1,d)
            +2*U_H(t-1,j,s-1,d+1)+2*U_H(t-1,j-1,s-1,d-1))

def U_iter(t,j,s):
    if s == 1:
        return U_H(t,j,1,0)
    total=0
    for h in range(s):
        delta=C(t-s,j-h)-C(t-s,j-h-1)
        total += C(s-1,h)*delta**4
    return 4*(8**(s-2))*total

def exact_operator_identity_checks():
    # Spectral-lift form of the already-proved cross identity:
    # A_parent = 2(A0+A1)+8G1+4C1, with G1=H*NB and C1=H*O.
    checked=0
    for t in range(3,11):
        for s in range(2,min(t,7)+1):
            H=1<<(s-2)
            for j in range(t+1):
                row=probe.panel(t,j,s,False)
                lhs=int(row["primitive_fourth_moment"])
                A0=actual_A(t-1,j,s-1)
                A1=actual_A(t-1,j-1,s-1)
                G1=H*int(row["RB"])
                C1=H*int(row["odd_cross"])
                rhs=2*(A0+A1)+8*G1+4*C1
                assert lhs == rhs
                checked += 1
    return checked

def hierarchy_inequality_checks():
    # Exact actual-filter verification of
    # G_d' <= 6(G_d(j)+G_d(j-1))+2(G_{d+1}(j)+G_{d-1}(j-1)), d>=1.
    checked=0
    equality=[]
    worst=None
    for t in range(4,11):
        for s in range(2,min(t,6)+1):
            for j in range(t+1):
                for d in range(1,min(j,4)+1):
                    lhs=actual_G(t,j,s,d)
                    rhs=(6*actual_G(t-1,j,s-1,d)+6*actual_G(t-1,j-1,s-1,d)
                         +2*actual_G(t-1,j,s-1,d+1)+2*actual_G(t-1,j-1,s-1,d-1))
                    assert lhs <= rhs
                    checked += 1
                    if lhs:
                        ratio=Fraction(rhs,lhs)
                        if worst is None or ratio>worst[0]:
                            worst=(ratio,t,j,s,d)
                        if ratio == 1:
                            equality.append((t,j,s,d))
    return checked,worst,equality

def critical_hierarchy_audit():
    # Prescribed after deriving the hierarchy: critical band +/-1,
    # t=8..30, s<=10. Exact, exhaustive in this finite box.
    rho=1/log2(3)
    rows=[]
    lt_triv=eq_triv=lt_iter=0
    for t in range(8,31):
        jc=round(rho*t)
        for j in range(max(1,jc-1),min(t-1,jc+1)+1):
            for s in range(2,min(t,10)+1):
                m2,m4=actual_moments(t,j,s)
                if not m4:
                    continue
                uh=U_H(t,j,s,0)
                ui=U_iter(t,j,s)
                triv=Fraction(m2*m2,2)
                if Fraction(uh,1)<triv: lt_triv+=1
                if Fraction(uh,1)==triv: eq_triv+=1
                if uh<ui: lt_iter+=1
                rows.append({
                    "t":t,"j":j,"s":s,
                    "actual_M4":str(m4),
                    "hierarchy_U":str(uh),
                    "old_U_iter":str(ui),
                    "trivial_M2sq_over_2":str(triv),
                    "U_over_actual":str(Fraction(uh,m4)),
                    "U_over_trivial":str(Fraction(uh,1)/triv) if triv else None,
                    "U_over_Uiter":str(Fraction(uh,ui)) if ui else None,
                })
    return {
        "scope":"t=8..30; j=round(t/log2(3)) +/-1 clipped to interior; s=2..min(t,10); exact; no sampling",
        "cases":len(rows),
        "hierarchy_strictly_below_trivial":lt_triv,
        "hierarchy_equal_trivial":eq_triv,
        "hierarchy_below_old_scalar_Uiter":lt_iter,
        "rows":rows,
    }

def reflection_counterexample():
    chain=[]
    for t,j,s in [(11,6,4),(10,6,3),(9,6,2)]:
        row=probe.panel(t,j,s,False)
        RB=int(row["RB"])
        Nm=Fraction(row["reflection_minus_norm"])
        Np=Fraction(row["reflection_plus_norm"])
        R0=int(row["R0"]); R1=int(row["R1"]); S=int(row["total_energy"])
        chain.append({
            "t":t,"j":j,"s":s,"N0":str(R0),"N1":str(R1),"NB":str(RB),
            "Nplus":str(Np),"Nminus":str(Nm),
            "Nminus_over_NB":str(Nm/RB) if RB else None,
            "node_ratio_2S_over_N0plusN1":str(Fraction(2*S,R0+R1)) if R0+R1 else None,
        })
    assert chain[0]["Nminus"]=="0" and chain[0]["NB"]!="0"
    assert chain[1]["Nminus"]=="0" and chain[1]["NB"]!="0"
    return chain

def small_source_weighted_reflection():
    # Diagnostic only. Use already-frozen true-source panels, and only s>=2
    # where the reflection split is defined as in the cross-term note.
    out=[]
    for r in (10,12,14):
        pan=wcheck.panel(r)
        t=pan["t"]
        num=Fraction(0); den=Fraction(0); zero=[]
        for row in pan["rows"]:
            s=row["s"]
            if s<2: continue
            flat=Fraction(row["flat"])
            if not flat: continue
            cr=probe.panel(t,row["j"],s,False)
            RB=int(cr["RB"])
            if not RB: continue
            d=Fraction(cr["reflection_minus_norm"])/RB
            num += flat*d
            den += flat
            if d==0:
                zero.append({"k":row["k"],"j":row["j"],"s":s})
        out.append({
            "r":r,"t":t,
            "Wflat_weighted_Nminus_over_NB_s_ge_2":str(num/den) if den else None,
            "decimal":float(num/den) if den else None,
            "zero_reflection_deficit_rows":zero,
        })
    return out

def main():
    identity_count=exact_operator_identity_checks()
    hcount,worst,equality=hierarchy_inequality_checks()
    critical=critical_hierarchy_audit()
    counter=reflection_counterexample()
    weighted=small_source_weighted_reflection()
    out={
        "status":"analytic lemmas in REPORT_TR.md; exact finite checks here",
        "operator_identity_cases":identity_count,
        "hierarchy_inequality_cases":hcount,
        "hierarchy_worst_rhs_over_actual_Gd":{
            "ratio":str(worst[0]),"t":worst[1],"j":worst[2],"s":worst[3],"d":worst[4]
        } if worst else None,
        "hierarchy_equality_cases":equality,
        "critical_hierarchy_audit":critical,
        "two_scale_reflection_counterexample":counter,
        "small_source_weighted_reflection_diagnostic":weighted,
    }
    (HERE/"RESULTS.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({
        "operator_identity_cases":identity_count,
        "hierarchy_inequality_cases":hcount,
        "hierarchy_equality_cases":len(equality),
        "critical_summary":{k:v for k,v in critical.items() if k!="rows"},
        "two_scale_reflection_counterexample":counter,
        "small_source_weighted_reflection_diagnostic":weighted,
    },indent=2))

if __name__=="__main__":
    main()
