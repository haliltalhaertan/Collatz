# CP20 Task 6 — Bağımsız Sayısal Doğrulama (kısmi)

**Tarih:** 2026-08-26
**Kapsam:** Drive arşivindeki `CP20_TASK6_MAJOR_THEOREM.md` teorem adayının
sayısal olarak test edilebilir bileşenleri.

> **Bu bir denetim (audit) DEĞİLDİR.** Bu, arşivin talep ettiği bağımsız
> zero-trust auditin yalnızca *hesaplama* ayağının bir kısmıdır
> (audit prompt madde 10). Resmî verdict verilmemiştir.
> Arşivdeki engine dosyalarına bakılmadan, sıfırdan yazılmış kodla yapılmıştır.

## Test edilen iddialar

### 1. Lemma B — tekrarlanan faktör bölünebilirliği

**İddia:** Aynı valuation kelimesi `W` bir Syracuse yörüngesinde `u < v`
konumlarında geçiyorsa, `2^A(W)` sayısı `n_v − n_u` farkını tam böler.

**Yöntem:** `n0 = 3, 5, ..., 199999` için her yörüngenin ilk 400 adımı,
uzunluk `r = 3..14` arası tüm tekrarlanan faktörler.

| Ölçüm | Sonuç |
|---|---|
| Test edilen tekrar çifti | **6.363.065** |
| Bölünebilirlik ihlali | **0** |

Arşivin kendi kaydı 753.763 kontrol bildiriyor; bu çalışma bağımsız kodla
yaklaşık 8 kat daha geniş bir örneklemde aynı sonucu veriyor.

**Ek kontrol:** `n_u = n_v` (durum tekrarı) hiç gözlenmedi — Lemma B'nin
"eşit durum" kolunun boş olduğu, en azından bu aralıkta, doğrulandı.

### 2. Sturmian sayım (Bölüm 6)

**İddia:** `g_k = ⌊α(k+1)⌋ − ⌊αk⌋` kelimesi Sturmian'dır, `p_g(r) = r + 1`.

**Yöntem:** α = log₂3, 120 basamak hassasiyetle, 200.000 sembol,
`r = 1..20` için farklı faktörlerin doğrudan sayımı.

**Sonuç:** `r = 1..20` aralığında **her r için tam olarak `r+1`**. İhlal yok.

### 3. Controller'ın varlığı (audit prompt madde 7)

**Soru:** Teoremin dışladığı nesne gerçekten var mı? Yani κ = 1.053 ile
`a_k ∈ {1,2,3}`, `a_k ≠ g_k`, `s_k = κ·log₂k + O(1)` sağlayan bir
*sembolik* dizi kurulabiliyor mu?

Bu önemli: eğer böyle bir dizi sembolik olarak bile kurulamıyorsa,
teorem boş bir sınıfı dışlıyor olurdu.

**Yöntem:** Geri beslemeli (greedy) inşa — her adımda `s_k`'yı hedefe
en yakın tutan izinli sembol seçilir. 200.000 adım.

| Ölçüm | Sonuç |
|---|---|
| Alfabe ihlali (`a_k ∉ {1,2,3}`) | 0 |
| Zero-critical ihlali (`a_k = g_k`) | 0 |
| Sapma `E_k = s_k − κ·log₂k` aralığı | **4,3040** (min −3,3041 / maks +0,9999) |

Sapma 200.000 adımda sınırlı kaldı — `O(1)` izleme yasasıyla tutarlı.

> **Uyarı:** Bu sonlu bir hesaptır ve `O(1)` yasasının **ispatı değildir**.
> Audit prompt madde 7 bunu açıkça yasaklıyor: sonlu hesap kabul edilmemeli.
> Bu madde hâlâ açık.

### 4. Gözlenen faktör karmaşıklığı

Teoremin çelişkisi şu iki sayının karşılaştırmasına dayanıyor:

| Büyüklük | Değer |
|---|---|
| Teoremin gerektirdiği alt sınır `α/κ` | **1,505188** bit/sembol |
| Zero-critical B=3 dilinin üst sınırı `log₂(B−1)` | **1,0** bit/sembol |

Controller kelimesinde fiilen ölçülen değerler:

| r | p_a(r) | log₂p_a(r)/r |
|---|---|---|
| 5 | 11 | 0,6919 |
| 10 | 30 | 0,4907 |
| 15 | 62 | 0,3969 |
| 20 | 99 | 0,3315 |
| 25 | 148 | 0,2884 |

Gözlenen karmaşıklık yalnızca teoremin alt sınırının (1,505) değil,
zero-critical üst sınırın (1,0) da **çok altında** ve r arttıkça düşüyor.
Yani çelişki iddia edilenden daha geniş bir marjla oluşuyor.

## Kâğıt üzerinde okunan ispat adımları

Aşağıdakiler kod ile değil, elle takip edilerek kontrol edildi.
Bu adımlarda **hata bulunamadı**; bu, denetimden geçtikleri anlamına gelmez.

- **Lemma A** (`n_k = O(k^κ)`): `A_j − αj = −s_j − {αj} = −κlog₂j + O(1)`
  → `2^(A_j−αj) = O(j^−κ)` → κ>1 olduğu için toplam yakınsıyor →
  `B_k/3^k = O(1)`; ve `3^k/2^A_k = 2^(s_k+{αk}) = O(k^κ)`. Tutarlı.
- **Lemma C** (`A(u,r) ≥ αr − C_A`): `r ≤ u` kısıtı altında
  `s_{u+r} − s_u = κlog₂((u+r)/u) + O(1) = O(1)` — bu kısıt teoremde
  `u ≥ N_r` ile sağlanıyor, ve `N_r` r'de üstel büyüdüğü için `r ≪ N_r`. Tutarlı.
- **Ana çelişki:** `|n_v−n_u| ≤ O(N_r^κ) = 2^((α−κε)r+O(1))` ile
  `|n_v−n_u| ≥ 2^(αr−C_A)` karşılaştırması; κε > 0 olduğu için büyük r'de
  çelişki. Nicelik sırası (ε önce, sonra r) doğru kurulmuş.
- **Bölüm 6 sayma argümanı:** her konum `g`-faktörü tarafından belirlenen
  ≤ (B−1)^r seçenek kümesine düşüyor, `g`-faktör sayısı r+1
  → `p_a(r) ≤ (r+1)(B−1)^r`. Sayma doğru.

## Açık kalan denetim maddeleri

Bu çalışma audit promptunun **yalnızca 10. maddesinin bir kısmını** karşılıyor.
Kapatılmayanlar:

- **Madde 7** — controller'ın `O(1)` izleme yasasının *ispatı*
  (sonlu hesap yeterli değil, ve bu çalışma da sonlu).
- **Madde 9** — literatür örtüşmesi. Özellikle SanMin Wang'ın
  E-dizisi teoremleri (Teorem 4.13) ve tekrarlanan-önek teoremi.
  **Novelty doğrulanmamıştır** ve bu, arşivin kendi ifadesiyle açık bir madde.
- Madde 1–6, 8 — kâğıt üstünde okundu, resmî adversarial denetim yapılmadı.

## Durum

`[SAYISAL BİLEŞENLER DOĞRULANDI — RESMÎ DENETİM VERDICT'İ YOK]`

Arşivin STOP kuralı yürürlükte kalmalıdır: teorem downstream kullanılmamalı,
CP20 Task 7'ye geçilmemelidir.

## Çalıştırmak için

```bash
python3 01_lemma_b_tekrar_faktor_bolunebilirligi.py   # ~14 sn
python3 02_sturmian_ve_controller.py                  # ~31 sn
```

Ek bağımlılık yok, yalnızca Python standart kütüphanesi.
