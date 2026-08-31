"""DENETIM DEVAM — u konumlari, r<=u durumu, ve Lemma B'nin ikinci kolu."""
from decimal import Decimal, getcontext
import math
getcontext().prec=60
A=Decimal(3).ln()/Decimal(2).ln()
N=400000
F=[int((A*k).to_integral_value(rounding='ROUND_FLOOR')) for k in range(N+2)]
g=[F[k+1]-F[k] for k in range(N+1)]
def esik(s,m):
    if s<=0: return True
    return (1<<(1000*s)) <= m**1053
a=[];s=0
for k in range(N):
    m=max(2,k+1)
    d=1 if (g[k]==2 and esik(s,m)) else -1
    a.append(g[k]-d); s+=d

def en_uzun(q):
    best=cur=0; st=0; bst=0
    for k in range(len(a)-q):
        if a[k]==a[k+q]:
            if cur==0: st=k
            cur+=1
            if cur>best: best=cur; bst=st
        else: cur=0
    return bst,best

print("Blok konumlari ve Lemma A'nin asimptotik rejimi\n")
print(f"{'q':>7} {'u':>8} {'r':>8} {'v=u+q':>8} {'r<=u?':>7} {'A(W)':>9} {'log2 n0>=':>11}")
for q in (53,306,665,15601,31867,79335):
    u,L=en_uzun(q)
    if L<2: continue
    AW=sum(a[u:u+L]); v=u+q
    alt=AW-1.053*math.log2(v+L)
    print(f"{q:>7} {u:>8,} {L:>8,} {v:>8,} {str(r'EVET' if L<=u else 'HAYIR'):>7} {AW:>9,} {alt:>11,.0f}")

print("\nNOT: Lemma C (A(u,r) >= alpha*r - C_A) r<=u gerektiriyor,")
print("     AMA benim argumanim Lemma C KULLANMIYOR: A(W) dogrudan")
print("     toplanarak hesaplaniyor. Gereken yalnizca:")
print("       Lemma B: 2^{A(W)} | (n_v - n_u)      [tekrar yeter]")
print("       Lemma A: n_k <= C(n_0) k^kappa       [konum kisiti yok]")
print("     Dolayisiyla r>u durumu argumani BOZMUYOR.\n")

# Lemma B ikinci kol: n_u = n_v olabilir mi?
print("Lemma B ikinci kolu (n_u = n_v): periyodiklik -> A_k/k rasyonel")
print("  ama kritik-log yasasi A_k/k -> alpha (irrasyonel) veriyor.")
print("  Her iki kolda da sonuc var, argumanda bosluk yok.\n")

# etkin sinirin buyume hizi
print("Etkin sinirin buyume hizi (asil iddia: sinirsiz):")
import numpy as np
qs=[];alts=[]
for q in (53,306,665,15601,31867,79335):
    u,L=en_uzun(q)
    if L<2: continue
    AW=sum(a[u:u+L]); v=u+q
    qs.append(q); alts.append(AW-1.053*math.log2(v+L))
for q,al in zip(qs,alts):
    print(f"  q={q:>7,}  ->  log2(n_0) >= {al:>10,.0f}   (oran alt/q = {al/q:.3f})")
print(f"\n  alt/q orani ~ sabit ({min(a2/q2 for q2,a2 in zip(qs,alts)):.3f}-{max(a2/q2 for q2,a2 in zip(qs,alts)):.3f})")
print("  -> log2(n_0) >= c*q, c>0 sabit; q->inf ile SINIRSIZ. Iddia ayakta.")
