# Durum — 2026-08-26 gece

Bu repo, Drive'daki kanonik arşivin **bağımsız kontrol katmanıdır**.
Kanonik kayıt Drive'dadır; burada yapılanlar oraya girdi olur ya da
oradaki sonuçları dışarıdan sınar.

---

## Drive'da bugün dondurulanlar

| Belge | Durum |
|---|---|
| `CP20_TASK6_MAJOR_THEOREM_V3` | `[PROVED][AUDITED][FROZEN]` |
| `CP20_TASK6_STRENGTHENED_COROLLARY_V3` | `[PROVED][AUDITED][FROZEN]` |
| `CP20_TASK7_PRESSURE_GENERALIZATION_THEOREM_V3` | `[PROVED][AUDITED][FROZEN]` |
| `CP20_TASK8A_CRITICAL_SITE_DENSITY_PRESSURE_V3` | `[PROVED][AUDITED][REPAIRED][FROZEN]` |

Dondurulmuş sayısal çekirdek (rasyonel sertifika):

```
h_3 < 523467/1000000        =>  alpha/h_3 > 3.027
h_inf < 56931/100000        =>  alpha/h_inf > 348/125 = 2.784
rho_min(1.06) in [0.34622623706156036, 0.34622623706159286]
rho_min(1.5)  in [0.09160833016625313, 0.09160833016627168]
rho_min(2.0)  in [0.03144455087148001, 0.03144455087149200]
```

## Bu repodaki çalışmanın oraya katkısı

| Repo | Drive'daki karşılığı |
|---|---|
| `04` Task 6 denetimi | bağımsız ikinci denetim; SHA yeniden üretildi |
| `05` Task 7 denetimi | kapsam bulguları (B'den bağımsızlık, `B=∞`) |
| `06` Task 6 güçlendirmesi | **`STRENGTHENED_COROLLARY_V3`'ün girdisi** |
| `07` geriye dönük tarama | CP20 T3 karşı-modelinin geçersizliği |
| `09` sürekli kesir bulgusu | Drive'da karşılığı **yok** — açık katkı |
| `10` Task 8A ön hesabı | `TASK8A` yüzeyinin ilk sayısal keşfi |

---

## ⛔ Bu repoda düzeltilen üç hata

Drive'ın bağımsız denetimi üç yerde beni düzeltti. Hepsi ilgili dosyada
işaretlendi:

**1. Chernoff işareti** (`05`, `06`)
Yazdığım: `N(S) ≤ P(t)·t^{+S}` — **yanlış**.
Doğrusu: `N(S) ≤ P(t)·t^{−S}`.
Denetim raporunun ifadesi: *"a real sign/wording bug"*.
Sonucu değiştirmiyor (`|S| = O(log r)` → yalnızca polinom prefactor),
ama gerçek bir hataydı.

**2. "Sturmian faz maliyeti"** (`10`)
`max h = 1,503981` ile `h(α) = 1,505644` arasındaki `0,0017` farkı
yapısal sanıp Task 8A promptuna ispat maddesi koymuştum.
Gerçek: **grid artefaktı**. Feasible domain'de gözden kaçırdığım kısıt
vardı (`ρ₁ − ρ₂ ≥ 3 − 2α`). Doğru optimizasyon CP19 T4'ü **tam olarak**
geri veriyor; kesin bir faz maliyeti yok. Task 8A o noktada CP19 T4'ten
güçlü değil, onunla **özdeş**.

**3. CP19 T5 survivor'ı** (`07`, `10`)
"Dışlanır" demiştim. Gerçek: **dışlanmıyor** —
`[HYPOTHESIS MISMATCH]`. Survivor'ın logaritmik excursion çekirdekleri
global kritik-log yasasını zaten ihlal ediyor, yani basınç yüzeyinin
hipotezi ona uygulanmıyor. Yoğunluk karşılaştırmam doğruydu; ondan
çıkardığım sonuç yanlıştı.

Ayrıca CP20 T3 için ifadem fazla iddialıydı: FAIL statüsü **değişmiyor**,
yalnızca karşı-modeli geçersiz kılındı.

---

## Doğrulanan sayısal işler

| Kontrol | Ölçek | Sonuç |
|---|---|---|
| CP17 carry özdeşlikleri (tam kesir) | 54.621 test | 0 ihlal |
| Task 6 Lemma B (örtüşen + ayrık) | 3,5 M test | 0 ihlal |
| Sturmian `p_g(r) = r+1` | r = 1..20 | tam |
| Controller SHA-256 | 100.000 sembol | **eşleşti** |
| Sturmian Parikh özdeşliği | 240.000 çift | 0 ihlal |
| `λ*`, `h_4`, `α/h_4` | 50 basamak | birebir |
| `ρ_min(κ)` | 3 nokta | %1–12 üstten (kaba grid) |

---

## Açık katkı: sürekli kesir örüntüsü (`09`)

Drive'da karşılığı yok. `α = log₂3`'ün büyük kısmi bölümleri (23, 55)
uzun faktör tekrarları üretiyor; Task 6 Lemma B buraya uygulanınca
`n₀` üzerinde **etkin alt sınır** çıkıyor:

```
q=53     -> n_0 >= 2^107
q=15601  -> n_0 >= 2^15780
q=31867  -> n_0 >= 2^50495
```

Pratik faydası: uzun tekrarlar rastgele değil, konverjantlarda oturuyor.
Baş araştırmacının 4. maddesine (Baker / continued fractions, high-κ)
doğrudan bağlanıyor.

**Durum:** denetlenmedi, Drive'a girmedi.

---

## Task 8B (Drive'da devam ediyor)

| Modül | Konu | Durum |
|---|---|---|
| B0 / Module A | literature mechanism falsification | denetlenmiş, onarılmış, dondurulmuş |
| B1 | pressure-constrained residue rate extremal search | denetlenmiş, onarılmış, dondurulmuş |
| B2 / Module D | 2-adic rate stabilization + **return word** | D0 audit paketi hazır, güçlendirilmiş prompt |

`return word` ekseni — `09`'daki bağlantı raporunda "taranmamış" diye
işaretlediğim alan — şimdi B2'de kullanılıyor.

---

## Frontier

```
kappa >= alpha/h_inf > 2.784010903...     [FROZEN]
```

Açık kalanlar: yüksek-κ rejimi, kritik siteler (`a_k = g_k`),
kritik-log dışı discrepancy yasaları, ve LEVEL-3 ordinary integrality.

**Collatz çözülmedi.**
