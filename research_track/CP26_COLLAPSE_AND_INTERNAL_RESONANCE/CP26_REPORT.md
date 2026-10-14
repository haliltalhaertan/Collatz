# CP26 — COLLAPSE kapısı ve iç rezonans (proper-prefix) pilotu

Tarih: 2026-09-22/23. Durum: **CHECKPOINT KAPANDI**. Collatz **AÇIK**. Sonlu hesaplar teorem değildir.

## 1. COLLAPSE lemması (CP25 kapanışı) — [PROOF, bağımlılık: LMN 1995]
Aşikâr olmayan pozitif rasyonel döngü adayında x_0 = bB/D < 2^{m+1}.
Kanıt: B ≤ 2^{m-k}(3^k-2^k) ve |2^m-3^k| > (3^k-2^k)/2^{k+1}.
İkincisi k ≥ 17013 için Laurent–Mignotte–Nesterenko (1995) alt sınırından; k ≤ 17012 için exact tamsayı taraması (0 ihlal).
Sonuç: tam gap kelimesi x_0'ı mod 2^{m+1} tek sınıfa kilitler ⇒ residue/bit-uzunluğu/2-adik yerel filtreler integrality (D|B) üzerine yeni bilgi eklemez; çoğu daha zayıftır.

Rota kararları:
| Rota | Karar |
|---|---|
| C1 / Product Barrier | KILL (başarılı olsa bile integrality yeniden üretimi) |
| Carry-band / residue-shell | KILL (stres pilotu: gap'e özgü ayrışma yalnız N≤27; N=28..48'de 0; evidence/cp25_carry_gap_stress_pilot.json) |
| SIGNED_CRT_DEPTH | PARK (m≤16 sağlam, 0 hata; fakat en zor adaylar L=k derinliğinde eleniyor; evidence/cp25_collapse_crt_depth_check.json) |

## 2. CP26 beyin fırtınası (ChatGPT Web, rol E) ve literatür
Adaylar: A global-min proper-prefix bariyeri; B ilk alt geçiş → iç LMN tanığı; C ikinci-dereceden işaretli log; D run-uzunluğu Jensen; E yakın minimumlar → iç rezonans.
Doğrulanan literatür: Hercher 2023 (J. Integer Seq. 26, m-cycle yok m≤91 ⇒ ≥92 yerel minimum; corrigendum mevcut); Barina 2025 (J. Supercomput. 81:810, 2^71'e kadar doğrulama); Simons–de Weger 2005 (Acta Arith. 117); Eliahou 1993 (Discrete Math. 118).
Hercher: 3·2^69 doğrulaması yeterli ⇒ Barina 2^71 ile K > 1.375·10^11 (iki yayımlı sonucun birleşimi).
DOĞRULANMADI: "Wang 2026, m≤95" — hakemli kayıt bulunamadı, kullanılmadı.
Değerlendirme: A doğru ama tanım gereği (minimum minimumdur); D ve büyük ölçüde C Hercher'in reciprocal-sum hattıyla örtüşür; E'nin köprüsü sanı.

## 3. Test: Aday B — INTERNAL_RESONANCE_SCAN (Unreal Agent + bağımsız yerel tekrar)
Kapsam: K=2..18, near-resonant M, b=±1, primitive necklace, **D|B filtresi yok**, Fraction exact.
- 2.532.524 aday (b=+1: 1.818.496; b=-1: 714.028).
- Aday A teorem kontrolü: 0 ihlal; b=-1'de A_t≤1 proper prefix: 0; ilk alt geçiş eksik: 0.
- 3n−1 negatif kontrolleri (1), (5,7), (17..91) korundu.
- Yerel bağımsız tekrar (K≤14, ayrı kod): aday sayıları, tam-döngü-geçiş oranları, S*/K min/medyan ve geçiş histogramları **birebir aynı**.
Bulgu: b=+1'de ilk alt geçişin S*/K medyanı ≈ 0.86–1.0; adayların %42–100'ünde ilk geçiş tam döngüde. Tam-döngü oranı log(2^M/3^K) küçükken (K=5,10,15,17) %96–100'e çıkıyor.
Yorum: küçük rasyonel adaylarda iç rezonans büyük ölçüde global 2^M≈3^K yakınlığının yeniden paketlenmesi. Ancak test rejimi n_min küçük; gerçek döngüde n_min > 2^71 — Aday B'nin olası gücü tam orada. Bu nedenle karar KILL değil.

## 4. Kararlar
| Aday | Karar |
|---|---|
| A | PROOF (elementer), tek başına güçsüz — araç olarak tutulur |
| B | CONDITIONAL / PARK — küçük-ölçek kanıtı olumsuz; büyük-n_min rejimi test edilmedi |
| C | PARK (Hercher ile örtüşme riski) |
| D | KILL (literatür daha güçlü) |
| E | CONJECTURE, test edilmedi |

## 5. Sonraki adım (CP27 adayı)
Aday B'yi n_min ≥ X (X=2^71) koşuluyla sına: rasyonel aday yerine "n_min ≥ X" altında hangi (S,E) iç geçişlerin mümkün olduğunu kısıt çözümüyle belirle; S*/K'nın X büyüdükçe davranışı. Başarı ölçütü: sistematik S*/K ≪ 1.

## 6. Ajan kullanımı
ChatGPT Web: teori/eleştiri (2 tur, bitiş işaretiyle doğrulandı). Unreal Agent (gpt-6-sol, Codex kotası): ilk gerçek görev, 366 sn, sonuçlar yerel tekrar ile birebir. Hiçbir ajan çıktısı kanıt sayılmadı.

---
## DÜZELTME 2026-09-23 (yenilik denetimi sonrası; eski metin değiştirilmedi)
- **LMN bağımlılığı birincil kaynaktan doğrulandı.** Laurent–Mignotte–Nesterenko, J. Number Theory 55 (1995) 285–321, s.288 Corollaire 2: α1,α2 reel, pozitif, çarpımsal bağımsız ise
  log|Λ| ≥ −24,34·D⁴·(max{log b′+0,14, 21/D, 1/2})²·log A1·log A2.
  Uygulama: α1=2, α2=3, D=1, log A1=1, log A2=log 3. b′=m/log 3+k ≤ 3k (m ≤ k·log₂3+1). Sınır b′'de azalan olduğundan b′≤3k yerine koymak geçerlidir.
- **İki aralık:**
  - k ≤ 3.82e+08 (log(3k)+0,14 ≤ 21): log|Λ| ≥ −24,34·log3·21² = −11792,438390. k=17013'te k·ln2 = 11792,512983 yeterli; k=17012'de 11791,819836 yetmez. Eşik 17013 birebir doğru.
  - k > 3.82e+08: gerekli eşitsizlik k·ln2 > 24,34·log3·(log(3k)+0,14)². Sol taraf doğrusal, sağ taraf (log k)² büyür; geçiş noktasında fark ≈ 2.65e+08 > 0 ve türev ln2 − 2·24,34·log3·(log(3k)+0,14)/k > 0, dolayısıyla tüm kuyrukta sağlanır.
- **Durum:** COLLAPSE **[PROOF]** olarak kalır. Yenilik etiketi: NEW-MINOR (LMN + elementer sınır).
- Kanıt: `../NOVELTY_AUDIT_20260923/evidence/lmn1995_corollaire2_verified.txt`, `../NOVELTY_AUDIT_20260923/NOVELTY_AUDIT_REPORT.md`.
