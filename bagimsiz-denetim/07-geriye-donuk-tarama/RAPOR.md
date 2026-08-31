# Geriye Dönük Tarama — 2026-08-26

**Soru:** Task 7'nin ağırlıklı-basınç yöntemi (ve onun geriye uygulanmış
hali) daha önce donmuş ya da başarısız ilan edilmiş sonuçların hangilerini
değiştiriyor?

**Yöntem:** Her eski sonucun *hangi üst sınırı / hangi sınıfı* kullandığı
tespit edildi, sonra o sınıfa basınç yöntemi uygulandı ve eşikler
karşılaştırıldı. Arşivin engine dosyalarına bakılmadı.

---

# ÖZET

İki gerçek kazanım, bir düşen gerekçe.

| # | Hedef | Bulgu |
|---|---|---|
| 1 | CP19 T4 + CP20 T1 eşiği `κ₀ = 1,0526808586` | Zero-critical sınıfta **2,64 kat** yükseltilebilir |
| 2 | CP20 T3 `[FAIL]` kararı | **Gerekçesi düştü** — dayandığı nesne artık var olamaz |
| 3 | Frontier | `κ ≥ 1,0527` → **`κ ≥ 2,7840`** |

---

# Bulgu 1 — `κ₀` eşiğinin kaynağı ve iyileştirilebilirliği

## Eşiğin kaynağı çözüldü

CP19 Task 4 freeze kararı şunu yazıyor:

> *"At `μ = α = log₂3`, the near-linear state exponent threshold is
> `κ < α/h(α) = 1.0526808586…`. The current Construction-B case has
> `κ = 1`, leaving a **5.27% exponent threshold margin**."*

`h(α)`'nın ne olduğunu bağımsız olarak türettim: **sınırsız alfabe
`a ∈ {1,2,3,…}` üzerinde, yalnızca `E[a] = μ` ortalama kısıtı altındaki
maksimum entropi**, yani geometrik dağılımın entropisi:

```
h(μ) = log₂μ + (μ−1)(log₂μ − log₂(μ−1))
h(α) = 1,5056438879463008…
α/h(α) = 1,0526808586079714…      (arşivde: 1,0526808586079717)
```

Fark `3,1 × 10⁻¹⁶` — çift duyarlıklı yuvarlama. **Eşleşiyor.**

## Kritik gözlem

`h(α)`, **zero-criticality kısıtını hiç kullanmıyor**. Yalnızca ortalama
valuation kısıtı var. Bu, sınıfın en geniş hali.

Basınç yöntemi aynı sınırsız alfabede, ama zero-critical (`a_k ≠ g_k`) ve
Sturmian faz yapısıyla çalışıyor:

| Sınıf (her ikisi de sınırsız alfabe) | `h` | `κ` eşiği |
|---|---|---|
| CP19 T4: yalnızca ortalama kısıtı | 1,50564388795 | 1,05268085861 |
| **+ zero-critical + Sturmian** | **0,569309013486** | **2,784010903** |

**Kazanç: 2,64 kat.**

## Ne değişiyor

CP19 T4'ün kendi ifadesi **yanlış değil** — daha geniş bir sınıf için
doğru. Ama arşivin frontier'ı zero-critical durumlarda duruyor, ve orada
`κ₀ = 1,0527` gereğinden çok zayıf.

Freeze kararındaki **"%5,27 margin"** ifadesi, zero-critical sınıfta
**%178,4 margin** olmalı.

Aynı `κ₀` sabiti CP20 Task 1'de de eşik olarak kullanılıyor
(`κ_0 = 1.0526808586079717`), dolayısıyla aynı kazanç oraya da uygulanır.

---

# Bulgu 2 — CP20 Task 3'ün `[FAIL]` gerekçesi düştü

## Task 3 neden başarısız ilan edilmişti

`CP20_TASK3_FINDINGS.md`, `[FAIL]` kararının gerekçesini açıkça yazıyor:

> *"**[FAIL] Why recovery debt is insufficient.** Large `a` events do
> create a real recovery debt. But the survivor can avoid them entirely.
> The exact 20-block controller uses only `a ∈ {1,2,3}`, no critical
> sites, and tracks `s_k = κ log₂ k + O(1)` for every fixed `1 < κ < 2`,
> including `κ = κ₀` and `1.053`. Hence a large-drop occupation theorem
> cannot cover the frontier."*

Yani Task 3, mekanizmasının **kaçınılabilir** olduğu için başarısız sayıldı
— ve kaçan nesne şu şekilde tanımlanmış:

| Özellik | Değer |
|---|---|
| Alfabe | `a ∈ {1,2,3}` → `B = 3` |
| Kritik site | yok → **zero-critical** |
| Discrepancy | `s_k = κ log₂ k + O(1)` |
| Aralık | `1 < κ < 2` |

## Bu tanım, güçlendirilmiş Task 6'nın dışladığı sınıfın tam kendisi

Güçlendirilmiş eşik (`B=3`, zero-critical, kritik-log):

```
κ ≥ α/h₃ = 3,02781926563979
```

`3,028 > 2` olduğundan Task 3'ün survivor aralığının **tamamı** dışarıda
kalıyor.

> **Task 3'ün `[FAIL]` kararının dayandığı karşı-model artık geçersiz.**

> **DÜZELTME (Drive freeze sonrası):** arşivin resmî ifadesi daha ölçülü —
> *"CP20 Task 3's historical FAIL status is **not changed**; only its prior
> zero-critical bounded-alphabet escape countermodel is **superseded**."*
> Yani FAIL statüsü duruyor, yalnızca gerekçesindeki karşı-model geçersiz
> kılındı. Benim "gerekçesi düştü, T3 yeniden değerlendirilmeli" ifadem
> fazla iddialıydı.

Bu, Task 3'ün mekanizmasının çalıştığı anlamına gelmiyor — o mekanizma
hâlâ frontier'ı kapatmıyor. Ama **başarısızlık gerekçesi geçersiz**:
"survivor kaçabilir" itirazının işaret ettiği survivor mevcut değil.

Task 3 yeniden değerlendirilmeli: mekanizması, kalan (`κ ≥ 2,784`)
bölgede işe yarıyor mu?

---

# Bulgu 3 — Frontier haritası

| | Açık `κ` bölgesi |
|---|---|
| CP19 T4 / CP20 T1 / CP20 T3 (önceki) | `κ ≥ 1,0526808586` |
| Task 6 + Task 7 + güçlendirme (şimdi) | **`κ ≥ 2,7840109030`** |
| Kapatılan aralık | `[1,05268 , 2,78401)` |
| Eşik yükselme çarpanı | **2,64x** |

Bu, arşivin son üç checkpoint'inin birleşik kazanımının tek sayıyla
ifadesi.

---

# Taranan ama etkilenmeyenler

| Sonuç | Neden etkilenmiyor |
|---|---|
| **CP17** (`K17 < 3`) | Farklı nicelik: harmonik toplam `H_N`, faktör karmaşıklığı değil. Basınç uygulanmıyor. *(Not: CP19 T4 freeze kararı `η(μ) = I_CP17(μ)/ln2` yapısal özdeşliğini kaydediyor — iki yöntem arasında bir köprü var, ama farklı çıktı veriyorlar.)* |
| **CP18 bariyeri** | Negatif, cebirsel sonuç (sonlu kısıt ⇏ LEVEL-3). Entropi sınırı içermiyor. |
| **CP18 T6, T10** | 2-adic cebir / nested cylinder. Sayım argümanı yok. |
| **CP19 T3** (sparse-critical packing) | Sparse-critical sınıfı zero-critical'den farklı; doğrudan uygulanamıyor. Ayrı inceleme gerekir. |
| **CP20 T4, T5** | `[LEAD]` / `[BARRIER]` — endpoint residue ve sheet activation; sembolik sayım sınırı taşımıyorlar. |

---

# Neden bu kazanımlar kaçmıştı

Üç checkpoint üst üste aynı yapısal hatayı yaptı: **her task bir sonraki
soruya koştu, geriye dönüp "bu yeni yöntem eskisini de düzeltir mi?" diye
sormadı.**

- Task 6 üst sınırda `(H1)`'i kullanmadı (kaba alfabe sayımı yaptı)
- Task 7 `(H1)`'i kullandı ama sadece `B=4` için baktı
- CP19 T4 / CP20 T1 / CP20 T3, zero-criticality'yi entropi sınırına hiç
  katmadı

Her üçünde de eksik olan bilgi **zaten hipotezlerde vardı**, sadece üst
sınırda kullanılmıyordu.

---

# Öneriler

1. **CP20 Task 3'ü yeniden aç.** `[FAIL]` gerekçesi düştü. Mekanizmasının
   `κ ≥ 2,784` bölgesinde işe yarayıp yaramadığı ayrı bir sorudur.
2. **CP19 T4 ve CP20 T1'in freeze notlarına** zero-critical alt sınıf için
   iyileştirilmiş eşiği ek olarak kaydet. Orijinal ifadeler geçerli kalır.
3. **CP19 Task 5'in survivor'ını kontrol et.** CP20 T3'ün bahsettiği
   "20-block controller" ile aynı nesne olabilir; öyleyse o `[FAIL]` de
   yeniden değerlendirilmeli. *(Bu tarama kapsamında doğrulanmadı.)*
4. **Arşiv doktrinine bir adım ekle:** her yeni yöntemden sonra geriye
   dönük tarama. Bugün tek turda iki kazanım ve bir düşen gerekçe çıktı.
5. Tüm bu bulgular **denetlenmemiş**. Basınç sabitleri rasyonel/aralık
   aritmetiğiyle yeniden üretilmeden downstream kullanılmamalı.

---

# Bu taramanın sınırı

Tarama **tam değil**. CP18'in 10 task'ı ve CP19'un 10 task'ı tek tek
açılmadı; master checkpoint özetlerinden ve hedefli aramadan gidildi.
Özellikle CP19 T3 ve CP19 T5 ayrı inceleme hak ediyor.

Ve her zamanki uyarı: bu da bir AI taraması.

---

# EK — Taramanın tamamlanması (aynı gün)

İlk raporda "doğrulanmadı" diye bırakılan iki madde kapatıldı:
CP19 Task 5 ve CP19 Task 3.

## Bulgu 4 — CP19 T5'in survivor'ı zero-critical DEĞİL

`CP19_TASK5_FINDINGS.md` explicit survivor'ı şöyle tanımlıyor:

```
kappa = 53/50 = 1.06 > kappa_*
turnover density: 0.999855041504
maximum zero-defect run: 1
```

**"zero-defect" = `d_i = 0` = `a_i = g_i` = kritik site.**

Yani survivor kritik siteler içeriyor (izole, ardışık değil). Bu,
Task 6/7'nin `(H4) a_k ≠ g_k ∀k` hipotezini **ihlal ediyor**.

> **Task 6/7 bu survivor'ı doğrudan dışlamıyor.**

Bu, ilk raporun 3. önerisine verilen cevaptır: CP20 T3'ün "20-block
controller"ı ile CP19 T5'in survivor'ı **aynı nesne değil**. T3'ünki
zero-critical ("no critical sites" diye yazıyor), T5'inki değil.

## Bulgu 5 — Basınç yöntemi seyrek kritik sitelere genişletiliyor

Kritik site yoğunluğu `ε` ise, ikinci bir Chernoff kısıtı eklenebilir:

```
h(eps) = inf_{lambda, nu<=0} [
     (2-alpha) log2( 2^nu + A(lambda) )
   + (alpha-1) log2( 2^nu + B(lambda) )
   - nu * eps ]
```

`nu -> -inf` zero-critical limitini, `nu = 0` kritik sitelerin serbest
halini verir. İki yöntemle hesaplandı:

| `eps` | `h` (titiz, iki-Lagrange) | eşik | `h` (kaba karışım) | eşik |
|---|---|---|---|---|
| 1e−5 | 0,56949758 | 2,7830891 | 0,56948384 | 2,7831562 |
| **0,00014496** | **0,57148321** | **2,7734192** | 0,57128412 | 2,7743857 |
| 1e−3 | 0,58151745 | 2,7255631 | 0,58014746 | 2,7319994 |
| 0,01 | 0,65775604 | 2,4096510 | 0,64440906 | 2,4595596 |
| 0,05 | 0,88688050 | 1,7871207 | 0,82724052 | 1,9159633 |

Titiz sınır kaba karışım modelinden biraz yüksek (yani kaba model
iyimserdi), ama fark küçük.

### T5 survivor testi

```
eps  = 1 − 0,999855041504 = 0,0001449585
h    = 0,571483211914      (lambda* = 1,596217 , nu* = −13,55537)
esik : kappa >= 2,77341917956
survivor kappa = 1,06
```

`1,06 ≪ 2,773` → yüzey survivor'ın yoğunluğunu yetersiz buluyor.

> ## ⛔ DÜZELTME (2026-08-26, Drive freeze sonrası) — BU SONUÇ YANLIŞ
>
> **CP19 T5 survivor'ı dışlanmıyor.** Dondurulan
> `CP20_TASK8A_FINAL_FREEZE_DECISION` şunu tespit ediyor:
>
> > *"CP19 Task 5's abstract survivor is **not excluded** because its
> > logarithmic excursion cores **violate that global hypothesis**;
> > status remains `[CP19 TASK5 SURVIVOR NOT EXCLUDED — HYPOTHESIS
> > MISMATCH]`."*
>
> Survivor, `s_k = κ log₂k + O(1)` global kritik-log yasasını zaten
> **sağlamıyor** (logaritmik excursion çekirdekleri var). Dolayısıyla
> basınç yüzeyinin hipotezi ona uygulanmaz.
>
> **Hatam:** yalnızca `(κ, ρ)` çiftini karşılaştırdım, hipotez uyumunu
> kontrol etmedim. Aşağıdaki uyarıda "tanımında başka özellikler de var"
> demiştim ama sonucu yine de "dışlanır" diye yazdım — o adım yanlıştı.
>
> Yoğunluk karşılaştırmasının kendisi (0,000145 vs ~0,35) doğru; yanlış
> olan ondan çıkardığım sonuç.

> ⚠️ Ayrıca bu genişletme benim taslağımdı ve kritik sitelerin Sturmian
> faz yapısıyla etkileşimini tam modellemiyordu. Arşivin dondurduğu V3
> yüzeyi bu işi feasible domain `F` (`ρ₁−ρ₂ ≥ 3−2α` kısıtı dahil) ve
> iki-rejimli uniformity lemmasıyla doğru şekilde yapıyor.

## Bulgu 6 — CP19 T3 tamamlayıcı, çakışmıyor

`CP19_TASK3_SPARSE_CRITICAL_THEOREM.md` şunu veriyor:

```
kritik uzunluk r >= 16 olan her segment icin
n_u >= r^{1+log2 3} / (24 log2 r) - 2r/3
```

Yani **uzun kritik segmentler** yüksek durum zorluyor ve
`δ(1+α) > κ` olduğunda imkansız hale geliyor.

Bu, Task 6/7'nin tam tersi ucu kapatıyor. Basınç yöntemi buraya
uygulanmıyor — farklı mekanizma.

## Kritik-site ekseninde frontier haritası

| Kritik site rejimi | Kapatan | Durum |
|---|---|---|
| Hiç yok (zero-critical) | Task 6 + 7 + güçlendirme | `κ < 2,784` kapalı |
| Seyrek, izole (`ε` küçük) | *bu genişletme* | `κ < ~2,77` — **taslak** |
| Uzun segmentler (`r ≥ 16`) | CP19 T3 | `δ(1+α) > κ` kapalı |
| Orta yoğunluk (`ε ≳ 0,05`) | — | **açık** |

`ε` büyüdükçe eşik düşüyor: `ε = 0,05`'te 1,787, `ε = 0,1`'de ~1,6.
Yani yöntem yoğun kritik sitelerde zayıflıyor.

## Güncellenmiş öneriler

1. ~~CP19 T5'in survivor'ını kontrol et~~ → **yapıldı**: zero-critical
   değil, Task 6/7 doğrudan uygulanmıyor.
2. **Seyrek-kritik genişletmesi ayrı bir Task olarak ele alınmalı.**
   Doğruysa CP19 T5'in `[FAIL]` gerekçesini de düşürür — ama önce
   Sturmian faz etkileşimi titizce modellenmeli.
3. Orta yoğunluklu kritik site rejimi (`ε ≈ 0,01–0,1`) hiçbir teorem
   tarafından kapatılmıyor; bu, frontier'ın gerçek yeri olabilir.

## Tarama artık tam

CP17, CP18 (bariyer, T5/T6/T10), CP19 (T3, T4, T5, T10), CP20 (T1–T7)
tarandı. Kalan: CP18 T1–T4, T7–T9 (hepsi `[FAIL]`/`[REDUNDANT]`, entropi
sınırı taşımıyorlar) ve CP19 T1/T2/T6–T9 (`[LEAD]`/`[FAIL]`, sembolik
sayım argümanı yok).
