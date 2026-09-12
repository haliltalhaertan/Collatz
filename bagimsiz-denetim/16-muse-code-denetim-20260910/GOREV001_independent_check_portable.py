#!/usr/bin/env python3
from fractions import Fraction
from math import comb
import json
from pathlib import Path
import argparse

PANELS = (5, 10, 12, 14)

def H(x):
    return x // 2 if x % 2 == 0 else (3*x + 1) // 2

def iterate_with_weight(x, steps):
    k = 0
    y = x
    for _ in range(steps):
        if y & 1:
            k += 1
        y = H(y)
    return y, k

def binom0(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0

def rat(x):
    x = x if isinstance(x, Fraction) else Fraction(x)
    return {"frac": str(x), "num": x.numerator, "den": x.denominator}

def conditional_energy(values, s):
    q = len(values); n = 1 << s; lift = q // n
    means = []
    for u in range(n):
        total = sum((values[a] for a in range(u, q, n)), Fraction(0))
        means.append(total / lift)
    return sum((v*v for v in means), Fraction(0)) / n

def conductor_layers(values):
    q = len(values); t = q.bit_length() - 1; prev = Fraction(0); out = {}
    for s in range(1, t+1):
        cur = conditional_energy(values, s); out[s] = cur - prev; prev = cur
    return out

def ramanujan_power2(n, d):
    d %= n
    if n == 2: return 1 if d == 0 else -1
    half = n // 2
    if d == 0: return half
    if d == half: return -half
    return 0

def cyclic_autocorr(arr):
    n = len(arr)
    return [sum(arr[(v+d) % n] * arr[v] for v in range(n)) for d in range(n)]

def primitive_product_sum_exact(f, g):
    n = len(f); cf = cyclic_autocorr(f); cg = cyclic_autocorr(g); total = 0
    for d in range(n):
        for e in range(n): total += cf[d] * cg[e] * ramanujan_power2(n, d+e)
    return total

def aggregate_mod(P, s):
    n = 1 << s; out = [0] * n
    for z, c in enumerate(P): out[z % n] += c
    return out

def prefix_histograms(m, t):
    q = 1 << t; P = {}
    for h in range(1, 1 << m, 2):
        y, k = iterate_with_weight(h, m)
        P.setdefault(k, [0] * q); P[k][y % q] += 1
    return P

def tail_indicators(t):
    q = 1 << t; weights = [iterate_with_weight(z, t)[1] for z in range(q)]
    return {j: [1 if w == j else 0 for w in weights] for j in range(t+1)}

def panel(r):
    A = (3**r).bit_length() - 1; m = (6*r + 4) // 5; t = A - m; q = 1 << t
    assert t >= 1
    P = prefix_histograms(m, t); T = tail_indicators(t)

    normalization = {}
    for k in range(1, m+1):
        observed = sum(P.get(k, [0]*q)); expected = binom0(m-1, k-1)
        normalization[str(k)] = {"observed": observed, "expected": expected, "ok": observed == expected}
    assert all(v["ok"] for v in normalization.values())

    tail_cardinality = {}
    for j in range(t+1):
        obs = sum(T[j]); exp = binom0(t, j)
        tail_cardinality[str(j)] = {"observed": obs, "expected": exp, "ok": obs == exp}
    assert all(v["ok"] for v in tail_cardinality.values())

    contributing=[]; Gk={}; Bk={}; Vk={}; ek={}; D2_terms={}; R_by_k={}; eR_by_k={}; V_layers_k={}; V_layers_fourier_k={}
    for k in range(1, m+1):
        j=r-k; Nk=binom0(m-1,k-1)
        if Nk == 0 or not (0 <= j <= t): continue
        contributing.append(k); Pk=P.get(k,[0]*q); Tj=T[j]; d=pow(3,k,q)
        gka=[]
        for a in range(q):
            shift=(d*a)%q
            gka.append(sum(c*Tj[(shift+z)%q] for z,c in enumerate(Pk) if c))
        Gk[k]=gka
        pk=Fraction(binom0(t,j),q); Bki=Fraction(Nk)*pk; Bk[k]=Bki
        centered=[Fraction(x)-Bki for x in gka]
        Vki=sum((x*x for x in centered),Fraction(0))/q; Vk[k]=Vki
        eki=sum((Fraction(c)-Fraction(Nk,q))**2 for c in Pk); ek[k]=eki
        Rs={}; e_from_R=Fraction(0)
        for s in range(1,t+1):
            Ps=aggregate_mod(Pk,s); half=1<<(s-1)
            R=sum((Ps[u]-Ps[u+half])**2 for u in range(half)); Rs[s]=R
            e_from_R += Fraction((1<<(s-1))*R,q)
        assert e_from_R == eki; R_by_k[k],eR_by_k[k]=Rs,e_from_R
        layers=conductor_layers(centered); assert sum(layers.values(),Fraction(0)) == Vki; V_layers_k[k]=layers
        flayers={}
        for s in range(1,t+1):
            Ps=aggregate_mod(Pk,s); n=1<<s
            Fs=[binom0(t-s,j-iterate_with_weight(u,s)[1]) for u in range(n)]
            flayers[s]=Fraction(primitive_product_sum_exact(Ps,Fs),q*q); assert flayers[s] == layers[s]
        V_layers_fourier_k[k]=flayers; D2_terms[k]=eki*pk*pk

    L=len(contributing); W=sum(Vk.values(),Fraction(0)); D2=sum(D2_terms.values(),Fraction(0)); qD2=q*D2
    G=[sum(Gk[k][a] for k in contributing) for a in range(q)]
    B=sum(Bk.values(),Fraction(0)); B_vandermonde=Fraction(binom0(A-1,r-1),q); assert B == B_vandermonde
    centered_G=[Fraction(x)-B for x in G]; assert sum(centered_G,Fraction(0)) == 0
    V=sum((x*x for x in centered_G),Fraction(0))/q; total_layers=conductor_layers(centered_G); assert sum(total_layers.values(),Fraction(0)) == V
    direct_G0=sum(1 for h in range(1,1<<m,2) if iterate_with_weight(h,A)[1] == r); assert direct_G0 == G[0]
    ineq_V_LW=V <= L*W; ineq_W_qD2=W <= qD2; origin_dev2=(Fraction(G[0])-B)**2; ineq_origin=origin_dev2 <= (q-1)*V
    assert ineq_V_LW and ineq_W_qD2 and ineq_origin
    fine_share=total_layers[t]/V if V else Fraction(0)
    return {"r":r,"A":A,"m":m,"t":t,"q":q,"contributing_k":contributing,"L":L,"normalization":normalization,"tail_cardinality":tail_cardinality,"B":rat(B),"B_vandermonde":rat(B_vandermonde),"G0":G[0],"direct_G0":direct_G0,"V":rat(V),"W":rat(W),"D2":rat(D2),"qD2":rat(qD2),"V_le_LW":{"ok":ineq_V_LW,"lhs":rat(V),"rhs":rat(L*W)},"W_le_qD2":{"ok":ineq_W_qD2,"lhs":rat(W),"rhs":rat(qD2)},"origin_bound":{"ok":ineq_origin,"lhs":rat(origin_dev2),"rhs":rat((q-1)*V)},"finest_total_V_layer":rat(total_layers[t]),"finest_total_V_share":rat(fine_share),"finest_total_V_share_decimal":float(fine_share),"total_V_layers":{str(s):rat(v) for s,v in total_layers.items()},"per_k":{str(k):{"j":r-k,"N_k":binom0(m-1,k-1),"P_k":P.get(k,[0]*q),"G_k":Gk[k],"B_k":rat(Bk[k]),"V_k":rat(Vk[k]),"e_k":rat(ek[k]),"R":{str(s):R_by_k[k][s] for s in R_by_k[k]},"e_from_R":rat(eR_by_k[k]),"V_layers_projection":{str(s):rat(v) for s,v in V_layers_k[k].items()},"V_layers_exact_fourier_product":{str(s):rat(v) for s,v in V_layers_fourier_k[k].items()},"D2_term":rat(D2_terms[k])} for k in contributing},"G":G}

def boundary_example():
    m,k,t,j=3,2,2,1; q=1<<t; P=prefix_histograms(m,t); Pk=P[k]; Nk=sum(Pk); T=tail_indicators(t); Tj=T[j]; pk=Fraction(binom0(t,j),q)
    e=sum((Fraction(c)-Fraction(Nk,q))**2 for c in Pk); d=pow(3,k,q); G=[sum(Pk[z]*Tj[(d*a+z)%q] for z in range(q)) for a in range(q)]; B=Fraction(Nk)*pk
    V=sum((Fraction(x)-B)**2 for x in G)/q; qD2=q*e*pk*pk; Rs={}; eR=Fraction(0)
    for s in range(1,t+1):
        Ps=aggregate_mod(Pk,s); half=1<<(s-1); R=sum((Ps[u]-Ps[u+half])**2 for u in range(half)); Rs[s]=R; eR += Fraction((1<<(s-1))*R,q)
    assert eR == e; assert Pk == [1,0,1,0]; assert Tj == [0,1,1,0]; assert G == [1,1,1,1]; assert e == 1 and V == 0 and qD2 == 1
    return {"m":m,"k":k,"t":t,"j":j,"q":q,"P":Pk,"T":Tj,"G":G,"B":rat(B),"e":rat(e),"R":{str(s):Rs[s] for s in Rs},"e_from_R":rat(eR),"V":rat(V),"qD2":rat(qD2),"expected_corrected_null_example_match":True}

def main():
    parser=argparse.ArgumentParser(description="Independent exact GOREV001 finite checker")
    parser.add_argument("--output-dir",default=".",help="Directory for RESULTS.json and ACTUAL_OUTPUT.txt (default: current directory)")
    parser.add_argument("--no-reference-check",action="store_true",help="Run internal exact identities without asserting archived regression values")
    args=parser.parse_args(); output_dir=Path(args.output_dir).resolve(); output_dir.mkdir(parents=True,exist_ok=True)
    out={"task":"COLLATZ_CHAT_TASK_001_W_AUDIT","role":"DENETIM","arithmetic":"integers + fractions.Fraction; no floating DFT equality claims","parity_count_order":"oddness counted before each H step","panels":[panel(r) for r in PANELS],"boundary_example":boundary_example()}
    expected={5:("37/4","37/4",1.0),10:("819/32","2915/32",0.540717),12:("2795/4","21195/8",0.945426),14:("274211/256","4612387/256",0.706960)}; comparison={}
    for p in out["panels"]:
        r=p["r"]; wexp,qdexp,shareexp=expected[r]
        comparison[str(r)]={"W_exact_match":p["W"]["frac"]==wexp,"qD2_exact_match":p["qD2"]["frac"]==qdexp,"finest_share_computed":p["finest_total_V_share_decimal"],"finest_share_reference_6dp":shareexp,"finest_share_matches_6dp":round(p["finest_total_V_share_decimal"],6)==round(shareexp,6)}
        if not args.no_reference_check: assert all([comparison[str(r)]["W_exact_match"],comparison[str(r)]["qD2_exact_match"],comparison[str(r)]["finest_share_matches_6dp"]])
    out["fixed_commit_report_comparison"]=comparison
    (output_dir/"RESULTS.json").write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding="utf-8")
    lines=["COLLATZ_CHAT_TASK_001_W_AUDIT — independent exact finite computation","Parity counted BEFORE each H step. No project diagnostic code imported."]
    for p in out["panels"]:
        all_layers=all(pd["V_layers_projection"]==pd["V_layers_exact_fourier_product"] for pd in p["per_k"].values()); all_eR=all(pd["e_k"]==pd["e_from_R"] for pd in p["per_k"].values())
        lines.append(f"r={p['r']} A={p['A']} m={p['m']} t={p['t']} q={p['q']} L={p['L']} G0={p['G0']} B={p['B']['frac']} V={p['V']['frac']} W={p['W']['frac']} qD2={p['qD2']['frac']} fineVshare={p['finest_total_V_share_decimal']:.12f}")
        lines.append(f"  checks: V<=L*W={p['V_le_LW']['ok']} W<=qD2={p['W_le_qD2']['ok']} origin={p['origin_bound']['ok']} G0_direct={p['direct_G0']==p['G0']} conductor_layers_exact={all_layers} e/R={all_eR}")
    b=out["boundary_example"]; lines.append(f"boundary m=3 k=2 t=2 j=1: P={b['P']} T={b['T']} G={b['G']} e={b['e']['frac']} V={b['V']['frac']} qD2={b['qD2']['frac']}")
    (output_dir/"ACTUAL_OUTPUT.txt").write_text("\n".join(lines)+"\n",encoding="utf-8"); print("\n".join(lines))

if __name__ == "__main__": main()
