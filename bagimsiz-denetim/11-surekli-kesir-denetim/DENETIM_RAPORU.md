# Sürekli Kesir Bulgusunun Zero-Trust Denetimi

**Tarih:** 2026-08-26
**Denetlenen:** `09-literaturden-baglantilar/PATTERNLER.md` §"Ana bulgu"
**Denetçi:** kendi bulgum — kırmaya çalışarak
**Not:** Kendi işini denetlemenin sınırı burada da geçerli.

---

# VERDICT

```
[VALID AS OBSERVATION — ONE LOAD-BEARING LEMMA MISSING]
```

Mekanizma doğru, sayısal davranış temiz ve beklediğimden **daha güçlü**
çıktı. Ama teorem olması için ispatlanmamış tek bir adım var (§4).

---

# 1. Kırma girişimleri ve sonuçları

## S1 — Her konverjantta uzun blok var mı?

Eğer yalnızca birkaç `q`'da varsa, "sınırsız büyüme" iddiası çöker.

| n | `q_n` | sonraki kısmi bölüm | en uzun blok `r` | `r/q` |
|---|---|---|---|---|
| 3 | 5 | 2 | 10 | 2,000 |
| 4 | 12 | 3 | 51 | 4,250 |
| 5 | 41 | 1 | 45 | 1,098 |
| 6 | 53 | 5 | 74 | 1,396 |
| 7 | 306 | 2 | 969 | 3,167 |
| 8 | 665 | 23 | 671 | 1,009 |
| 9 | 15.601 | 2 | 15.605 | **1,000** |
| 10 | 31.867 | 2 | 31.871 | **1,000** |
| 11 | 79.335 | 1 | 79.339 | **1,000** |
| 12 | 111.202 | 1 | 34.943 | 0,314 |

**Test edilen 10 konverjantın hepsinde uzun blok var.** `r/q` oranı
büyük `q` için tam **1,000**'e oturuyor, minimum 0,314 — sıfıra gitmiyor.

`[GEÇEMEDİ — kırılamadı]`

## S2 — Controller'a mı özgü?

Eğer yalnızca `κ = 1,053` için geçerliyse, bulgu dar kalır.

| kelime | `q=665` blok | `q=15601` blok |
|---|---|---|
| controller `κ=1,053` | 671 | 15.605 |
| controller `κ=1,2` | 671 | 15.607 |
| controller `κ=1,5` | 671 | 15.607 |
| controller `κ=2,0` | 671 | 15.607 |
| **rastgele zero-critical** | **20** | **21** |

**`κ`'dan tamamen bağımsız.** Bulgu controller'a özgü değil — her
kritik-log kontrollü zero-critical kelimede aynı.

Ve rastgele zero-critical kelimede **yok** (20 vs 15.605). Yani yapı
tesadüfi değil; **kritik-log kontrolü şart**.

`[BEKLEDİĞİMDEN GÜÇLÜ — bulgu genelleşiyor]`

## S3 — Lemma C bağımlılığı var mı?

Task 6 Lemma C (`A(u,r) ≥ αr − C_A`) `r ≤ u` gerektiriyor. Blokların
bazılarında `r > u` (örn. `q=53`: `u=31, r=74`). Bu argümanı bozar mı?

**Hayır.** Argüman Lemma C'yi **kullanmıyor**:

```
Lemma B:  2^{A(W)} | (n_v − n_u)          [yalnızca tekrar gerekli]
Lemma A:  n_k ≤ C(n₀)·k^κ                 [konum kısıtı yok]
```

`A(W)` doğrudan toplanarak hesaplanıyor, alttan sınırlanmıyor. `r > u`
durumu zararsız.

`[GEÇEMEDİ — kırılamadı]`

## S4 — Lemma B'nin ikinci kolu boşluk mu?

`n_u = n_v` olursa? → yörünge periyodik → valuation eventually periodic
→ `A_k/k` rasyonel. Ama kritik-log yasası `A_k/k → α` (irrasyonel).
Çelişki. **Her iki kolda da sonuç var.**

`[GEÇEMEDİ — kırılamadı]`

---

# 2. Ortaya çıkan temiz yasa

Etkin sınırın `q` ile ölçeği:

| `q` | `log₂n₀ ≥` | oran |
|---|---|---|
| 665 | 1.050 | 1,5789 |
| 15.601 | 24.714 | 1,5841 |
| 31.867 | 50.495 | 1,5846 |
| 79.335 | **125.729** | **1,5848** |

`α = log₂3 = 1,5850`

Oran `α`'ya **yakınsıyor**. Yani:

```
log₂ n₀  ≳  α · q_n
```

`α` irrasyonel olduğundan sonsuz çoklukta konverjant var, dolayısıyla
sınır **sınırsız** büyüyor. Sabit bir `n₀` hepsini karşılayamaz.

Yasa temiz ve kaynağı açık: `A(W) ≈ α·r` ve `r ≈ q`, düzeltme terimi
`κ log₂(v+r)` ihmal edilebilir.

---

# 3. Ne kadar katkı?

Task 6 zaten "tekrar varsa çelişki" diyor ve `p_a(r) ≥ N_r`
çıkarıyor. Bu bulgunun eklediği:

| Task 6 | Bu bulgu |
|---|---|
| tekrarların **olmaması gerektiğini** kanıtlıyor | tekrarların **nerede olduğunu** söylüyor |
| asimptotik (`yeterince büyük r`) | **etkin** (`q_n`'de somut sınır`) |
| ε-δ dilinde | `log₂n₀ ≳ α·q_n` açık formülü |

Matematikte bu ayrım anlamlıdır (ineffective vs effective bounds).
Ayrıca **rejim farkı** var: Task 6 `u ~ 2^{1,5r}` konumlarına bakıyor,
bu bulgu `u ~ r` konumlarına — farklı ölçek.

---

# 4. ⛔ EKSİK LEMMA — teorem olmasının önündeki tek engel

Sınırsızlık iddiası şuna dayanıyor:

> **(L)** Her konverjant `q_n` için, kritik-log kontrollü zero-critical
> bir kelimede uzunluğu `≥ c·q_n` (`c>0` sabit) olan bir `q_n`-tekrar
> bloğu **vardır**.

**Bu ispatlanmadı.** 10 konverjantta gözlendi, hepsinde `c ≈ 1`.

İspat için gereken malzeme mevcut görünüyor:

1. `g` Sturmian → `g[k] = g[k+q_n]` uzun aralıklarda (klasik: kısmi
   bölüm `a_{n+1}`, konverjant periyodunun `a_{n+1}` kez tekrarı)
2. `a_k = g_k − d_k` ve `d_k ∈ {+1,−1}` (kritik-log kontrolü altında)
3. `s_k` logaritmik → `d` örüntüsü uzun aralıklarda `g`'ye kilitleniyor

(1)+(2)+(3) → `a[k] = a[k+q_n]` uzun blokta. Ama **(3) hassas adım**:
`d_k`'nın tekrar örüntüsünü `s_k`'nın logaritmik yavaşlığından türetmek
gerekiyor, ve bu yapılmadı.

Bu lemma ispatlanırsa bulgu teorem olur. İspatlanmazsa **gözlem**
olarak kalır — değerli ama teorem değil.

---

# 5. Diğer açık noktalar

- **Küçük `q`** (5, 12, 41, 53): Lemma A'nın asimptotik rejimi
  (`s_k = κlog₂k + O(1)` yalnızca büyük `k` için) şüpheli. Bu satırlar
  gösterge, kanıt değil. Büyük `q`'lar sağlam.
- **`C(n₀)` sabiti** tam izlenmedi. `n_k ≤ 2^{C+1}(n₀+c)k^κ` biçiminde
  ama `C` ve `c` açıkça sınırlanmadı. Etkin sınırın kesin sabiti bundan
  etkilenir (mertebesi değil).
- `q = 111.202` satırında `r/q = 0,314` — oran düşüyor. `N = 400.000`
  penceresi bu `q` için yetersiz olabilir. Daha uzun tarama gerekli.

---

# 6. Denetimin kendi sınırı

**Bu denetimi bulgunun sahibi yaptı.** Arşivin doktrini bağımsız denetçi
gerektirir. Bugün Drive'daki bağımsız denetim beni üç yerde düzeltti
(bkz. `DURUM.md`) — aynı şeyin burada da olması muhtemel.

Özellikle §4'teki eksik lemmanın "ispatlanabilir görünmesi" benim
değerlendirmem; bağımsız bir denetçi orada gerçek bir engel bulabilir.
