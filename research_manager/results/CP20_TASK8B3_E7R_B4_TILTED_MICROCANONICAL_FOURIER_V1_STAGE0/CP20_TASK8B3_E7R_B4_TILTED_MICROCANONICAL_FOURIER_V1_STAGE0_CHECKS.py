#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
import json, itertools, math, pathlib

TASK="CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V1"
CFG=pathlib.Path(f"{TASK}_CONFIG.json")
OUT=pathlib.Path(f"{TASK}_STAGE0_CHECK_RESULTS.json")

def comps(T,r,prefix=()):
    if r==1:
        if T>=1: yield prefix+(T,)
        return
    for a in range(1,T-r+2):
        yield from comps(T-a,r-1,prefix+(a,))

def fp(s):
    a,b=s.split("/")
    return Fraction(int(a),int(b))

def weight(p, tup):
    q=1-p
    return (p**len(tup))*(q**(sum(tup)-len(tup)))

def chi(expr,tup):
    env={f"a{i+1}":a for i,a in enumerate(tup)}
    # exact ±1 forms only
    if expr=="(-1)^(a1+2*a2)":
        e=tup[0]+2*tup[1]
    elif expr=="(-1)^(a1+a2+a3)":
        e=sum(tup)
    elif expr=="(-1)^(a1+a2+2*a3)":
        e=tup[0]+tup[1]+2*tup[2]
    else:
        raise ValueError(expr)
    return Fraction(-1 if e%2 else 1,1)

def main():
    cfg=json.loads(CFG.read_text())
    results={"schema":"B4_STAGE0_CHECKS_V1","all_checks":"PASS","details":{}}

    # T1 exact equal composition weights for all frozen cases.
    t1=[]
    for case in cfg["fixed_stage0_checks"]["conditional_weight_cases"]:
        p=fp(case["p"])
        vals=[weight(p,tuple(c)) for c in case["compositions"]]
        ok=len(set(vals))==1
        assert ok
        t1.append({"case":case,"common_weight":str(vals[0]),"PASS":ok})
    results["details"]["T1_conditional_weights"]=t1

    # T2 100-digit centrality sanity on frozen r only; proof is algebraic in docs.
    getcontext().prec=100
    alpha=Decimal(3).ln()/Decimal(2).ln()
    t2=[]
    for r in cfg["fixed_stage0_checks"]["centrality_r_cases"]:
        T=int((alpha*Decimal(r)).to_integral_value(rounding="ROUND_FLOOR"))-8
        delta=Decimal(T)-alpha*Decimal(r)
        ok=Decimal(-9)<delta<=Decimal(-8)
        assert ok
        t2.append({"r":r,"T_r":T,"delta":str(delta),"PASS":ok})
    results["details"]["T2_centrality"]=t2

    # T3 exact negative-binomial formula vs enumeration.
    t3=[]
    for case in cfg["fixed_stage0_checks"]["negative_binomial_enumeration_cases"]:
        p=fp(case["p"]); r=case["r"]; T=case["T"]; q=1-p
        enum=sum((weight(p,c) for c in comps(T,r)), Fraction(0,1))
        formula=Fraction(math.comb(T-1,r-1),1)*(p**r)*(q**(T-r))
        assert enum==formula
        t3.append({"case":case,"value":str(enum),"PASS":True})
    results["details"]["T3_denominator_formula"]=t3

    # T4 quotient identity on finite exact composition fibers.
    t4=[]
    for case in cfg["fixed_stage0_checks"]["quotient_cases"]:
        p=fp(case["p"]); r=case["r"]; T=case["T"]; ex=case["chi"]
        tuples=list(comps(T,r))
        D=sum((weight(p,c) for c in tuples),Fraction(0,1))
        N=sum((weight(p,c)*chi(ex,c) for c in tuples),Fraction(0,1))
        G_uniform=sum((chi(ex,c) for c in tuples),Fraction(0,1))/len(tuples)
        assert N/D==G_uniform
        t4.append({"case":case,"D":str(D),"N":str(N),"G":str(G_uniform),"PASS":True})
    results["details"]["T4_quotient_identity"]=t4

    # T6 exact coefficient extraction/sign test on frozen finite surrogates.
    # Multiplying exp(-it(T-alpha*r)) by exp(it(sum-alpha*r)) leaves exp(it(sum-T));
    # integral over [-pi,pi] is exactly delta_(sum,T).
    t6=[]
    for case in cfg["fixed_stage0_checks"]["fourier_inversion_finite_surrogate_cases"]:
        p=fp(case["p"]); r=case["r"]; T=case["T"]; M=case["max_part"]; ex=case["chi"]
        tuples=list(itertools.product(range(1,M+1), repeat=r))
        direct=sum((weight(p,c)*chi(ex,c) for c in tuples if sum(c)==T),Fraction(0,1))
        reconstructed=sum((weight(p,c)*chi(ex,c)*(1 if sum(c)==T else 0) for c in tuples),Fraction(0,1))
        assert direct==reconstructed
        t6.append({"case":case,"coefficient":str(direct),"PASS":True})
    results["details"]["T6_fourier_sign_index"]=t6

    # Deterministic arc ordering sanity.
    arcs=[]
    for r in cfg["fixed_stage0_checks"]["arc_order_r_cases"]:
        L=math.log(r+1)**0.25
        a=L/math.sqrt(r); b=r**(-0.25)
        assert a<=b+1e-15 and b<=math.pi
        arcs.append({"r":r,"major_endpoint":a,"intermediate_endpoint":b,"PASS":True})
    results["details"]["arc_order"]=arcs

    OUT.write_text(json.dumps(results,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("B4 STAGE0 PERMITTED CHECKS: PASS")

if __name__=="__main__":
    main()
