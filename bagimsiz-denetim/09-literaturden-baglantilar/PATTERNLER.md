# Örüntüler ve Yeni Bağlantılar — İkinci Tur

**Tarih:** 2026-08-26
İlk turda beş bağlantı çıkardım. Bu turda daha derine indim ve
**hesaplanabilir bir örüntü** buldum.

---

# ⭐⭐ ANA BULGU — Sürekli kesir örüntüsü

## Gözlem

`α = log₂3`'ün sürekli kesir açılımı:

```
[1; 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 3, …]
                            ↑↑                  ↑↑
```

`23` ve `55` gibi **büyük kısmi bölümler**, `α`'nın olağanüstü iyi
rasyonel yaklaşımları demek. Ve Sturmian kelime teorisinin klasik
sonucu: büyük kısmi bölüm `a_{n+1}`, konverjant periyodu `q_n`'in
**`a_{n+1}` kez tekrarlanması** demektir.

Ölçtüm — `g` kelimesinin `q`-kaydırma altında uyuşması:

| `q` | uyuşma oranı | ilk uyuşmazlık |
|---|---|---|
| 306 | 0,997035 | 0 |
| **665** | **0,999899** | **15.600** |
| 15601 | 0,999932 | 0 |
| 31867 | 0,999988 | 79.334 |

`q = 665` için `g` kelimesi **15.600 adım boyunca tam periyodik**
(`a₉ = 23` tam olarak bunu üretiyor: `665 × 23 ≈ 15.300`).

## Bağlantı: bu, Task 6 Lemma B'nin tetikleyicisi

Controller `a_k = g_k − d_k` bu periyodikliği kısmen miras alıyor.
Ölçüm:

| `q` | `a`'da en uzun ortak blok |
|---|---|
| 306 | 969 |
| 665 | 671 |
| 15601 | **9.967** |
| 31867 | **31.871** |

Yani `a` kelimesinde **binlerce uzunlukta faktör tekrarları** var.

Task 6 Lemma B tam buraya uygulanır: `a[u..u+r−1] = a[v..v+r−1]` ise

```
2^{A(W)} | (n_v − n_u)
```

## Sonuç: Task 6'nın ETKİN versiyonu

Lemma A `n_k ≤ C·k^κ` diyor, ve **sabit `C`, `n₀`'a bağlı**. İkisini
birleştirince çelişki değil, **`n₀` üzerinde etkin bir alt sınır** çıkıyor:

```
C  ≥  2^{A(W)} / (v+r)^κ
```

Hesaplanan:

| `q` | `u` | `r` | `A(W)` | **`log₂ n₀ ≥`** |
|---|---|---|---|---|
| 53 | 31 | 74 | 115 | **107** |
| 306 | 15.296 | 969 | 1.535 | **1.520** |
| 665 | 730 | 671 | 1.062 | **1.050** |
| 15.601 | 21.899 | 9.967 | 15.796 | **15.780** |
| 31.867 | 40.572 | 31.871 | 50.513 | **50.495** |

**Sonsuz bir yörünge için `n₀` sabittir.** Ama `q` büyüdükçe gereken
alt sınır patlıyor — hiçbir sabit `n₀` hepsini karşılayamaz.

Task 6 asimptotik bir çelişki veriyordu; bu onun **sayısal olarak
izlenebilir** hâli. Ve sürekli kesir yapısı **nereye bakılacağını
önceden söylüyor**.

## Bağımsız tutarlılık kontrolü

İki tamamen ayrı hesap, aynı `n₀` büyüme yasasını veriyor:

| Yöntem | Sonuç |
|---|---|
| 2-adic lifting ile sonlu prefix realizörü (önceki deney) | `r = 300` → `n₀ = 2^468` |
| Tekrar argümanı (bu deney) | `q = 665, r = 671` → `n₀ ≥ 2^1050` |

Farklı `r`'ler ama aynı mertebe yasası. Bu, iki mekanizmanın gerçekten
aynı olguyu ölçtüğünün işareti.

## Neden bu bir "bağlantı"

Sürekli kesir teorisi, Sturmian kelime kombinatoriği ve Task 6'nın
2-adic argümanı burada tek noktada buluşuyor. Ve pratik faydası var:

> **Uzun tekrarlar rastgele yerlerde değil, `α`'nın konverjantlarında
> oturuyor. Argümanı test etmek için `q₀, q₁, q₂, …` konumlarına
> bakmak yeterli — tüm kelimeyi taramaya gerek yok.**

**Önerilen Task:** *"Konverjant-tetiklemeli etkin sınırlar"* — her
konverjant `q_n` için `n₀` alt sınırını türet; `q_n → ∞` ile sınırın
patlama hızını `α`'nın irrasyonellik ölçüsüne bağla.

---

# META-ÖRÜNTÜ 1 — Arşivin işleyen her mekanizması aynı formda

Başarılı sonuçları yan yana koyunca:

| Sonuç | Alt sınır (nereden) | Üst sınır (nereden) |
|---|---|---|
| CP17 | aritmetik (carry serisi) | analitik (`K17 < 3`) |
| Task 6 | **aritmetik** (2-adic bölünebilirlik) | kombinatoryal (alfabe sayımı) |
| Task 7 | aritmetik (Task 6'dan) | **kombinatoryal** (Sturmian + basınç) |
| CP19 T3 | aritmetik (kritik segment) | — |

**Örüntü:** her çalışan mekanizma bir **aritmetik alt sınır** ile bir
**kombinatoryal/analitik üst sınır**ı çarpıştırıyor.

Bu, Collatz'ın klasik gerilimini yansıtıyor: `2`'nin yapısı ile `3`'ün
yapısı çatışıyor. Arşiv farkında olmadan hep aynı şablonu kullanmış.

**Öngörü değeri:** yeni bir mekanizma ancak iki ölçü **aynı büyüklük
mertebesine** geldiğinde işe yarar. Task 7'nin Task 6'yı geçmesinin
sebebi tam bu — üst sınırı alt sınıra yaklaştırdı.

---

# META-ÖRÜNTÜ 2 — Bütün başarısızlıklar "sonluluk"ta

FAIL'leri yan yana koyunca ortak cümle çıkıyor:

- CP18 T1–T4: *"nested costs are not independent"*, *"the proposed
  infinite bridge fails"*
- CP20 T3: *"the survivor can avoid them entirely"*
- CP19 T5: *"positive exact LEVEL-2 realizers for every finite prefix"*
- CP18 bariyeri (formalize edilmiş hâli): **sonlu sayıda
  valuation/kongrüans kısıtı, sonlu LEVEL-2 sağlanabilirliğini pozitif
  LEVEL-3 realizerden ayırt edemez**

**Örüntü:** arşivin bütün başarısızlıkları sonlu mekanizmalarda; bütün
başarıları asimptotik ölçülerde.

**Bu, Bağlantı 1'in (Hensel basamakları) neden umut verici olduğunu
açıklıyor:** "sonsuz çok sıfır olmayan basamak" asimptotik bir ifade,
sonlu bir sınıflandırma değil. CP18 bariyerinin yasakladığı türden
değil.

---

# META-ÖRÜNTÜ 3 — Sabitler arasında gizli yapı YOK

Ortaya çıkan 14 sabiti (α, h_3, h_4, h_∞, h(α), K17, K11, κ*, κ_∞*,
π²/48, …) sistematik olarak taradım: tüm ikili oran/fark/çarpım/toplam
kombinasyonları, 12 basamak eşleşme eşiğiyle.

**Bulunanlar** — hepsi zaten bilinen:
```
α / h_B = κ_B*        (tanım)
h_B · κ_B* = α        (aynı)
K11 / ((α+2)/2) = K17 (daha önce bulundum)
```

**Yeni gizli ilişki yok.** `K17 = 2,7429` ile `κ_∞* = 2,7840` yakın
(fark 0,041) ama ilişkisiz; `h_∞ = 0,5693` ile `α−1 = 0,5850` yakın
(fark 0,016) ama ilişkisiz.

**Bu negatif bir sonuç ama değerli:** sabitler bağımsız, yani bu
mekanizmalar gerçekten farklı olguları ölçüyor. Yakınlıklar, hepsinin
`log₂3`'ten türemesinin kaçınılmaz sonucu.

---

# YENİ EKSEN — Furstenberg ×2 ×3 rijitliği

**Boşluk:** `×2 ×3` ölçü rijitliği literatürü (Furstenberg 1967,
Rudolph 1990, Johnson 1992) ile Collatz arasında **bilinen bir bağlantı
bulamadım.** Aramada hiç çıkmadı.

**Neden şaşırtıcı:** Collatz'ın tamamı `2` ile `3`'ün çarpımsal
bağımsızlığı üzerine kurulu. Arşivin temel özdeşliği:

```
2^{A_k} · n_k  =  3^k · n_0 + B_k
```

Bu, `×2` ve `×3` arasında bir denge denklemi.

**Rudolph–Johnson:** `p, q` çarpımsal bağımsızsa, `×p` ve `×q` altında
ergodik invaryant, **pozitif entropili** tek ölçü Lebesgue'dir.

**Spekülatif bağlantı:** arşivin basınç yöntemi zaten entropi hesaplıyor
(`h_B > 0`). Hipotetik bir ıraksak yörünge, `T = R/Z` üzerinde
`{αk mod 1}` orbitiyle bir `×2×3`-ilişkili yapı üretiyor mu? Üretiyorsa
ve entropisi pozitifse, rijitlik teoremi Lebesgue'i zorlar — ama
Lebesgue tam sayılara yoğunlaşmaz.

**Dürüstlük:** bu en spekülatif fikir. `×2×3` rijitliği torus üzerinde
ölçüler hakkında; Collatz tek bir yörünge hakkında. Köprü açık değil.
Ama literatürdeki bu boşluk **kendisi** dikkat çekici.

---

# Öncelik (güncellendi)

| # | İş | Neden | Maliyet |
|---|---|---|---|
| 1 | **Konverjant-tetiklemeli etkin sınırlar** | Hesaplandı, çalışıyor, Task 6'yı etkin yapıyor | **Düşük** |
| 2 | Otomatik dizi taraması | Ucuz, sınıf kapatabilir | Çok düşük |
| 3 | Tekrar dikotomisi (A–B ile Task 6) | Yarısı hazır | Düşük |
| 4 | Hensel basamak yoğunluğu | LEVEL-3'e doğrudan | Orta |
| 5 | Furstenberg ekseni | Yüksek risk, yüksek getiri | Yüksek |

**1. sıra değişti.** Sürekli kesir bulgusu hem hesaplanmış hem ucuz hem
de arşivin elindeki teoremi güçlendiriyor — diğerleri gibi "acaba
taşınır mı" değil, **zaten taşındı.**

---

# Dürüstlük kaydı

Ana bulgu (sürekli kesir → etkin sınır) **hesaplandı ve iki bağımsız
yoldan tutarlı çıktı**, ama denetlenmedi. Özellikle:

- `a` kelimesinin `g`'den ne kadar periyodiklik miras aldığı controller'a
  özgü olabilir; genel zero-critical kelimeler için aynı olmayabilir
- Etkin sınırın `q_n → ∞` davranışı `α`'nın irrasyonellik ölçüsüne
  bağlı ve bu bağ kurulmadı
- Meta-örüntüler gözlemdir, teorem değil

Furstenberg ekseni spekülasyondur.
