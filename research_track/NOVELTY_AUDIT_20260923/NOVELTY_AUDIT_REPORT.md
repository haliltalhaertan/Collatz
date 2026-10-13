# NOVELTY AUDIT 2026-09-23 — Whole-programme novelty scan (CP01–CP28)

Status: **CLOSED (audit)**. Collatz remains **OPEN**.

## 1. Method
- **Pass 1 (breadth).** Seven isolated Unreal Agent sessions, one per era: CP01–13, CP14–19, CP20 T1–7, CP20 T8/E7, research_* 09-08..09-13 + audit layer, CP21–24, CP25–28.
  - 391 claims extracted.
  - Each labelled KNOWN / SUPERSEDED / PARTIAL / STANDARD / NEW-CANDIDATE / INTERNAL / FLAWED, with primary-source quotes.
  - 233 references were opened by the agents and 11 were not.
  - Searches used object words as well as method words.
- **Pass 2 (depth).** Eight Unreal sessions re-examined all 50 NEW-CANDIDATEs. For each claim they:
  - quoted the exact statement;
  - identified the weakest step and ran an exact check;
  - applied a triviality test;
  - ran ≥6 literature queries, including a Lagarias bibliography full-text grep and citation lists of Garcia–Tal and Rozier;
  - scored value 0–5 and gave a final verdict.
- **Coordinator checks.** The coordinator opened the key primary sources itself, see §4. An independent cross-check from another chat session was also incorporated.

## 2. Headline results
| Item | Verdict |
|---|---|
| CP02–CP19 "divergent-orbit sparsity" line (H_N bounds CP09–CP12, CP17 limsup H_N/lnln N ≤ 2.7429, s_k ≤ log2 k + C impossible, CP18 T5, CP19 T4) | **SUPERSEDED** by Garcia–Tal, Acta Arith. 90 (1999) 245–250 (doi 10.4064/aa-90-3-245-250) and, made explicit, by Curry, Zenodo doi 10.5281/zenodo.22087163 (2026-08-24): Prop 3.1 Σ1/x<∞; Thm 4.1 B≤1; Cor 4.3 B<1/β*=1.0358567; Thm 2.3 β*=0.9653844, γ*=0.6090897. Coordinator opened the PDF. |
| CP20 κ band 1<κ≤2.784 (T6/T7 pressure) | NEW-MINOR. Conditional (zero-critical + exact log law). Not covered by Garcia–Tal/Curry (B<1.036), but follows quickly from T7-02. |
| CP17 mod-3^n collision energy χ_n = O(n^4) | Correct; no equivalent found; **NEW-MINOR** (coordinator downgrade from the agent's NEW-STRONG). The exact χ_n is far below the bound (§3). |
| CP19 T3 critical-segment lower bound n_0 ≳ r^{2.585}/log r | Correct under its hypotheses; **NEW-MINOR** (coordinator downgrade). Source label was "candidate — independent audit required, not frozen"; pass 1 wrongly quoted it as PROVED. The true minimal realiser grows ~2^{1.4r} (r=16: 1.03e7; r=48: 3.4e20). |
| CP26 COLLAPSE (x0 < 2^{m+1}) | **PROOF stands.** LMN 1995 Corollaire 2 verified from the primary source (§4); threshold 17013 exact. Novelty: NEW-MINOR (LMN + elementary bound). |
| CP27 Lemma V | TRIVIAL (floor-sum construction). |
| CP28 PBM | TRIVIAL as a standalone result: a routine corollary of Inselmann 2024 Lemma 2.16 + Thm 3.1. The CP28 proof stays valid. |
| CP23 3n+1 / 3n−1 sign blindness | TRIVIAL identity (affine equation + x↦−x). Its value is as a negative warning. |
| Continued-fraction "n_0 ≥ 2^107, 2^15780, 2^50495" (bagimsiz-denetim/09, DURUM.md) | **FLAWED**: these are lower bounds on the unknown constant C(n_0), not on n_0. The script's own docstring says so, and audit 11 §5 had warned. |
| CP02 first crossing K ≥ 72,057,431,991 | NEW-MINOR/SUPERSEDED-equivalent: same location as the Hercher + Barina bound; not an improvement. |
| Remaining NEW-CANDIDATEs (50 total) | 31 TRIVIAL, 10 NEW-MINOR, 5 UNRESOLVED (CP21 conjectures M_merge ≥ L_lift, radius-2 charging, C1), 1 FLAWED, 1 SUPERSEDED. |

## 3. χ_s follow-up (CP17 energy)
- Exact untruncated transfer computation (`chi_s_exact.py`) for s = 1..16.
- It agrees with an independent Unreal code (s ≤ 15, Decimal 45 digits) and with an independent cross-check session (s ≤ 15).
- Exact values: χ_1 = 5/3, χ_2 = 15/7, χ_3 = 177005/67963.
- Increments E_s: 0.4616 (s=3), 0.4667 (s=9), 0.4674 (s=10), 0.4708 (s=15), 0.4714 (s=16), still rising slowly.
- Fits over s = 6..16: a + b·s, a + b·log s and a + b/s are all close. The data do not decide between linear growth and s·log s growth. The earlier "E_s → 7/15" guess is **withdrawn**.

Proved identities [PROOF]:
- χ_s = 1 + Σ_{j≤s} E_j;
- E_j = Σ_{u primitive mod 3^j} |φ_j(u)|² = 3^j Σ_y (p_j(y) − p_{j−1}(y mod 3^{j−1})/3)² ≥ 0.
- The diagonal contribution (same A-word on both copies) is exactly 1.

**Open target:** bound the off-diagonal collision term, i.e. sup_j E_j < ∞. Tao 2019 Lemma 6.2 and Prop 1.17 do not give it directly.

## 4. Coordinator primary-source checks
- **Curry 2026:** PDF opened; Prop 3.1, Thm 2.3, Thm 4.1, Thm 4.2, Cor 4.3 and the reference list (Garcia–Tal [1]) confirmed.
- **Garcia–Tal 1999:** Crossref record confirmed. Its content is taken from agent reads.
- **Laurent–Mignotte–Nesterenko 1995, J. Number Theory 55, 285–321** (open archive, scanned PDF read page by page):
  - p.286 defines Λ = b2 log α2 − b1 log α1.
  - p.288, **Corollaire 2** (α1, α2 real positive, multiplicatively independent): log|Λ| ≥ −24.34 D⁴ (max{log b′ + 0.14, 21/D, 1/2})² log A1 log A2.
  - Application with α1=2, α2=3, D=1: b′ ≤ 3k, giving log|Λ| ≥ −11792.438390.
  - k=17013: k ln2 = 11792.512983 (sufficient); k=17012: 11791.819836 (not sufficient). This matches CP26 exactly.
- **Inselmann 2024:** Lemma 2.16 and Theorem 3.1 checked in CP28.

## 5. Corrections to earlier records
- CP26: add the source note (LMN Corollaire 2 verified) and the novelty label NEW-MINOR.
- CP28: PBM novelty is TRIVIAL/corollary; the proof status is unchanged.
- bagimsiz-denetim/09 and DURUM.md: the "n_0 ≥ 2^…" figures are bounds on C(n_0) — **WITHDRAWN** as n_0 bounds.
- Earlier statements that "CP17 is the programme's strongest original result" are withdrawn in favour of the SUPERSEDED verdict.
- Label checks must run in both directions: pass 1 inflated CP19 T3, and the cross-check session deflated CP17.

## 6. Files
- `evidence/pass1/`: 7 briefs, 7 reports, merged ledger (391 claims).
- `evidence/pass2/`: 8 briefs, 8 reports and JSONs, DEEP_MERGED.json.
- `evidence/lmn1995_corollaire2_verified.txt`, `evidence/cp17_linear_unreal.txt`.
- `chi_s_exact.py`, `chi_s_exact.json`.

---
## CORRECTION 2026-09-23 (same day, after commit bc4bbc7)
- `chi_s_exact.py` is a **full-support, untruncated float64/FFT** transfer computation, not exact rational arithmetic. Total-mass error ≤ 4·10⁻¹⁶. Exact rationals were obtained only for s ≤ 3 (χ_1=5/3, χ_2=15/7, χ_3=177005/67963). Unreal's independent Decimal(45-digit) code agrees for s ≤ 15.
- CP26/LMN: the k > 3.82·10⁸ tail uses max{log(3k)+0.14, 21} = log(3k)+0.14. The required inequality k·ln2 > 24.34·log3·(log(3k)+0.14)² holds because of monotonicity; see the CP26 report correction.
