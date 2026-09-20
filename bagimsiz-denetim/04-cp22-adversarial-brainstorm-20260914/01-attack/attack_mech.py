"""Task 2b: derive exact normalized flatness tables from attack_flat_results.json.
All arithmetic int/Fraction. No floating point.
G2_j = S_j/(n_j^2 n_{j-1}^2) = sum_z gap[z]^2, gap = E_j/n_j - O_{j-1}/n_{j-1} (exact Fraction).
JG2_j = J_j/(n_j^2 n_{j-1}^2) (top-bit surviving part).
P-flatness: max/mean (Fraction), Vn = V/n^2 (Fraction) where V=sum(N*P-n)^2.
Run: python3 attack_mech.py
"""
import sys, json
sys.path.insert(0, "/home/mdp/muse-work/cp22-attack")
from fractions import Fraction

F = "/home/mdp/muse-work/cp22-attack/attack_flat_results.json"
D = json.load(open(F))

def show(key, krange, jrange):
    d = D[key]
    m, s = d["m"], d["s"]
    N = d["N"]
    print(f"=== ({m},{s}) N={N} ===")
    print(" k : n, cap, max/mean, V/n^2, L_k")
    for kk in krange:
        st = d["strata"][str(kk)]
        n = st["n"]; V = st["varnum"]
        print(f" k={kk} n={n} cap={st['cap']} max/mean={st['maxmean']} V/n^2={Fraction(V, n*n)} L={st['L']}")
    print(" j : M_j, S, J, G2=sumgap^2, JG2, max|gap|, J/S")
    for j in jrange:
        li = d["links"][str(j)]
        n_j = d["strata"][str(j)]["n"]
        n_j1 = d["strata"][str(j - 1)]["n"]
        S = li["S"]; J = li["J"]
        den = n_j * n_j * n_j1 * n_j1
        G2 = Fraction(S, den)
        JG2 = Fraction(J, den)
        maxgap = Fraction(li["maxabsD"], n_j * n_j1)
        print(f" j={j} M={li['M']} G2={G2} JG2={JG2} max|gap|={maxgap} J/S={li['JoverS']}")
    print()

for key, kr, jr in [
    ("20,3", range(11, 19), range(11, 20)),
    ("18,2", range(12, 18), range(12, 19)),
    ("22,3", range(12, 19), range(12, 20)),
    ("20,2", range(12, 19), range(12, 20)),
]:
    show(key, kr, jr)

# Binding interval decomposition for (20,3)[14,16]
d = D["20,3"]
print("### (20,3)[14,16] binding decomposition (exact) ###")
dem = sum((Fraction(d["L"][str(k)]) for k in [14, 15, 16]), Fraction(0))
sup = sum((Fraction(d["M"][str(j)]) for j in [13, 14, 15, 16, 17, 18]), Fraction(0))
print(f"demand L14+L15+L16 = {Fraction(d['L']['14'])} + {Fraction(d['L']['15'])} + {Fraction(d['L']['16'])} = {dem}")
for j in [13, 14, 15, 16, 17, 18]:
    print(f"  M{j} = {Fraction(d['M'][str(j)])}")
print(f"supply = {sup}  ratio = {sup/dem}")
print(f"tail share (M17+M18)/supply = {(Fraction(d['M']['17'])+Fraction(d['M']['18']))/sup}")
print(f"interior share (M14+M15+M16)/supply = {(Fraction(d['M']['14'])+Fraction(d['M']['15'])+Fraction(d['M']['16']))/sup}")
# P histograms at k=14..17 for (20,3)
print("### (20,3) raw histograms P (length 16) k=14..17 ###")
for kk in [14, 15, 16, 17]:
    print(f" k={kk}: {d['strata'][str(kk)]['hist']}")
print("### (18,2) raw histograms P (length 8) k=13..16 ###")
d18 = D["18,2"]
for kk in [13, 14, 15, 16]:
    print(f" k={kk}: {d18['strata'][str(kk)]['hist']}")
