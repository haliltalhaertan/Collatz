# CP29 — χ_s collision energy: structure identities, s ≤ 18 data, open growth question

Status: **CLOSED (partial / negative)**. The identities are proved and audited. **The growth rate of χ_s is still OPEN.** Collatz remains **OPEN**.

## 1. Question
Let A_i be iid with P(A=a)=2^{-a} (a≥1). Set X_0=0 and X_s = 2^{-A}(1+3X_{s-1}) mod 3^s, using a fresh A at each step. This is the finite Syracuse variable of Tao 2019 (arXiv:1909.03562, (1.22) and Remark 1.13; the word order is reversed).
- χ_s = 3^s Σ_y P(X_s=y)².
- E_s = χ_s − χ_{s−1}, with χ_0 = 1.

Known bound: χ_s = O(s⁴) (CP17).

Targets:
- (G1) sup E_s < ∞;
- (G2) any bound better than O(s⁴);
- (G3) E_s → ∞.

**None of the three was reached.**

## 2. Proved identities (all elementary; INTERNAL tools, not results)
| ID | Statement | Label |
|---|---|---|
| I1 | q_s = q_{s−1}/3 + r_s, where r_s = P(collision, A_1≠A'_1). Hence E_s = 3^s r_s. Identical words contribute exactly 1. r_1=2/9, r_2=10/189 | [PROOF] |
| I2 | E_s = 3^{s−1} Σ_{l≠0} 4^{−\|l\|} C_s(l mod 3^{s−1}), where C_s(j)=P(T'≡4^j T mod 3^s) and T=1+3X_{s−1} | [PROOF] |
| I3 | E_s = 3^s Σ_{r,t}(q_s(r,t) − p_{s−1}(r)/3)², hence 0 ≤ E_s ≤ 2χ_{s−1}. This is only an exponential bound | [PROOF] |
| I4 | v_3(X−X') alone is not a Markov state. Mod 9 → 27, the pairs (1,2) and (2,4) give P = 16400/786429 vs 1280/786429 | [PROOF] |
| I5 | Cross-overlap form: E_s = 3^s Σ_{a≠b} 2^{−a−b} Σ_y ν_{a,s}(y) ν_{b,s}(y) | [PROOF] (SELFSIM arm) |
| I6 | sup E<∞ ⇒ χ=O(s); E_s→∞ ⇒ χ_s/s→∞; unbounded E alone does not refute O(s). Example: E_{2^k}=k, all other E_j=0 | [PROOF] |

**The single missing inequality (G1):** sup_s 3^{s−1} Σ_{l≠0} 4^{−|l|} C_s(l) < ∞. Equivalently, a uniform bound on the weighted cross-overlap energy in I5.
- Tao 2019 Lemma 6.2 gives injectivity of the rational offset map.
- Tao 2019 Prop 1.17 gives single-frequency decay.
- Neither controls a sum over ~2·3^{s−1} frequencies. Both were checked in the primary text.

## 3. Numerics (full-support floating-point transfer; not exact rational)
| s | χ_s | E_s | 3^s·max p_s |
|---|---|---|---|
| 3 | 2.604431823 | 0.461574680 | |
| 6 | 4.000329912 | 0.466168761 | |
| 7 | 4.465821342 | 0.465491430 (dip) | |
| 10 | 5.865789026 | 0.467387418 | 84.18 |
| 16 | 8.684947713 | 0.471351643 | 960.34 |
| 17 | 9.156767868 | 0.471820155 | 1440.57 |
| 18 | 9.629001325 | 0.472233457 | 2160.913 |

Independent implementations:
- Hermes FFT transfer (s ≤ 16).
- NUMERIC arm: FFT-free float64 transfer (s ≤ 18).
- Referee: separate code, np.longdouble for s=17–18, 75-digit Decimal for s ≤ 10.

Agreement and error bounds:
- All implementations agree to ≤ 5·10⁻¹³.
- Against 60–75-digit arithmetic for s ≤ 10, the difference is ≤ 4·10⁻¹⁵.
- These are agreement and practical error figures, not a certified global error bound.

Behaviour of E_s:
- It rises slowly with shrinking steps.
- It is not monotone (6→7).
- Model fits (constant, 1/s, log s, 1/log s, s^{−1/2}) are exploratory only. **Finite data do not decide** between E_s → c and E_s ~ c·log s.

## 4. Self-similar framing (SELFSIM arm): verdict B — right language, no closing theorem
- X_∞ ∈ Z_3 has law μ = Σ_a 2^{−a}(f_a)_*μ, with f_a(x)=2^{−a}(1+3x). Each f_a is a 3-adic similarity of ratio 1/3 [PROOF].
- Σ_a 4^{−a} = 1/3 = ratio, so this is the formally critical L² case [PROOF]. Overlaps exist, so the actual correlation dimension is not proved by this.
- No exact map overlap exists, by Tao Lemma 6.2 plus different 3-adic slopes for different lengths [PROOF]. But in the infinite alphabet **there is no positive minimal separation**: 2^{2·3^{m−1}} ≡ 1 (mod 3^m), so the infimum of the distances is 0 [PROOF]. Uniform exponential separation therefore fails.
- Literature opened in primary form (finite real IFS; none gives sup E_s<∞ or O(s·polylog)):

  | Source | Result |
  |---|---|
  | Shmerkin arXiv:1609.07802 | Thm 6.2, 6.6 |
  | Hochman arXiv:1212.1873 | Thm 1.1 |
  | Varjú arXiv:1602.00261 | Thm 1 |
  | Breuillard–Varjú arXiv:1510.04043 | |
  | Kittle–Kogler arXiv:2409.18936 | |
  | Hare–Vávra arXiv:2307.07375 | p-adic, finite IFS |
  | Shmerkin arXiv:1907.07121 | |

  Even a transferred "dimension 1" would only give χ_s = 3^{o(s)}. Truncating to a finite alphabet breaks criticality.
- Promising missing condition: a **weighted** near-overlap estimate. Very close cylinders carry tiny weights.

## 5. Audits and process
- **UA referee** (clean session, own code): I1–I6 all DOĞRU; s=17–18 reproduced.
- **Hermes** exact Fraction check (`cp29_verify.py`): r_1, r_2, χ_1–χ_3, the I4 fractions; I2/I3 to ≤ 3·10⁻¹⁵ (s ≤ 8).
- Authors were the PAIR, FOURIER, NUMERIC and SELFSIM arms (Unreal). ChatGPT and Muse were not used this round, because the user requested Unreal only.
- Second clean audit: only the identities are claimed, and they are elementary. Referee + coordinator exact reproduction is recorded as sufficient for *identities*. No growth theorem is claimed.
- Coordinator brief error: the Tao "Def. 1.8" reference is corrected to (1.22) / Remark 1.13.
- Novelty: I1–I5 are INTERNAL/TRIVIAL tools. The value of this checkpoint is the precise reduction to one inequality and the separation obstacle.

## 6. Next (not started)
1. PARK χ_s as an honestly documented open side question (recommended). Even full success sharpens a NEW-MINOR side lemma.
2. Attack the single inequality via a weighted near-overlap / correlation-decay estimate for C_s(l).
3. Return to the main programme.

## 7. Files
- `cp29_verify.py`, `cp29_verify.json`: coordinator exact/float checks.
- `chi_s_exact.py`: FFT transfer.
- `evidence/`:
  - 5 briefs and 5 final reports (pair, fourier, numeric, referee, selfsim);
  - arm codes and JSONs;
  - `cp29_transfer.c`;
  - referee code and JSON;
  - SELFSIM separation code and data, plus its literature query log.
- Copyrighted PDFs are excluded.
