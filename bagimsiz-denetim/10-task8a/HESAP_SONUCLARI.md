# Task 8A — İlk Hesaplama Aşaması: SONUÇLAR

**Tarih:** 2026-08-26
**Kaynak:** Baş araştırmacının Task 8A önerisi (critical-site density pressure)
**Durum:** Hesaplandı. **Dal kapatılmamalı — engel dayanıyor.**

---

# Yönetici özeti

| Soru | Cevap |
|---|---|
| Küçük kritik yoğunluk engeli hemen yok ediyor mu? | **Hayır.** `ρ = 0,01`'de eşik 2,78 → 2,41 |
| İki kritik tipi ayırmak gerekli mi? | **Evet, asimetri büyük** |
| `ρ_min(κ)` eğrisi çıkarılabildi mi? | **Evet** |
| CP19 T5 survivor'ı bu yüzeyle ne oluyor? | **Dışlanıyor — 3 mertebe eksik** |
| Beklenmedik bulgu | **Yüzey CP19 T4 ile Task 7'yi tek eğride birleştiriyor** |

---

# 1. Analitik sadeleşme (hesabı 1 boyuta indirdi)

Baş araştırmacının üç değişkenli yüzeyi `H(λ, μ₁, μ₂)` için `∂H/∂μᵢ = 0`
kapalı formda çözülüyor:

```
2^{μ₁} = ρ₁·A(λ) / (2−α−ρ₁)        2^{μ₂} = ρ₂·B(λ) / (α−1−ρ₂)
```

Yerine koyunca yüzey **tek değişkene** iniyor:

```
h(ρ₁,ρ₂) = inf_{λ>0} [ (2−α−ρ₁)·log₂A(λ) + (α−1−ρ₂)·log₂B(λ) ] + E₁ + E₂

E₁ = (2−α)log₂(2−α) − (2−α−ρ₁)log₂(2−α−ρ₁) − ρ₁log₂ρ₁
E₂ = (α−1)log₂(α−1) − (α−1−ρ₂)log₂(α−1−ρ₂) − ρ₂log₂ρ₂
```

**Yorum:** `E₁,E₂` λ'dan bağımsız — bunlar *hangi sitelerin kritik
olduğunun* seçim entropisi. Kritik siteler "dondurulmuş" (tek seçenek),
kalan siteler basınç altında. Yapı temiz ve kendini açıklıyor.

*Not:* `μᵢ` **serbest** olmalı (her iki işaret). İlk denememde `μᵢ ≤ 0`
aldım — o "en fazla ρ" kısıtını verir; baş araştırmacının istediği
"tam ρ" için serbest bırakmak gerekiyor.

---

# 2. Asimetri gerçek ve büyük

Aynı toplam yoğunluk `ρ = 0,06`, farklı dağılım:

| `ρ₁` (g=1'de kritik) | `ρ₂` (g=2'de kritik) | `h` | κ eşiği |
|---|---|---|---|
| 0 | 0,06 | 0,6968 | **2,275** |
| 0,03 | 0,03 | 0,8831 | 1,795 |
| 0,06 | 0 | 0,9221 | **1,719** |

`ρ₁` yönünde kaçış **belirgin şekilde daha ucuz**.

**Yapısal sebebi:** `g=1` sitesinde zero-critical seçenekler
`a ∈ {2,3,4,…}` yani defect `d ∈ {−1,−2,…}` — hepsi negatif. Kritik
olmak (`a=1, d=0`) oradaki **tek nötr** seçenek, dolayısıyla `s_k`'yı
korumak için değerli. `g=2` sitesinde ise zaten `d=+1` (`a=1`) mevcut,
kritik olmanın marjinal değeri düşük.

**Baş araştırmacının iki tipi ayırma sezgisi doğrulandı.**

---

# 3. `ρ_min(κ)` — istenen asıl sonuç

> *"Bir survivor varsa kritik site yoğunluğu en az `ρ_min(κ)` olmalıdır."*

| `κ` | benim (41×41 grid) | **arşivin sertifikalı aralığı (V3)** | sapma |
|---|---|---|---|
| 1,06 | 0,3514 | **[0,34622623706156036 , 0,34622623706159286]** | %1,5 |
| 1,5 | 0,0976 | **[0,09160833016625313 , 0,09160833016627168]** | %6,5 |
| 2,0 | 0,0354 | **[0,03144455087148001 , 0,03144455087149200]** | %12 |
| ≥ 2,784 | 0 | **0** — zero-critical yeterli | — |

Benim değerlerim sistematik olarak **üstten** sapıyor; kaba gridin
beklenen davranışı. Arşivin V3 sertifikası yönlü aralık aritmetiğiyle
üretilmiş ve SHA-256 ile doğrulanmış. **Mertebe ve yapı doğru, hassasiyet
onlarınki.**

Eğri monoton: `κ` düştükçe gereken kritik yoğunluk hızla artıyor.

**Bu tam olarak istenen ifade biçimi.**

---

# 4. ⭐ Beklenmedik bulgu — yüzey iki eski sonucu birleştiriyor

Yüzeyin maksimumunu aradım:

```
max h = 1,503981   at (ρ₁, ρ₂) = (0,2497 , 0,1394)
minimum ulaşılabilir κ eşiği = 1,053845
```

Ve CP19 Task 4'ün sabiti:

```
h(α) = 1,505644      κ₀ = 1,052681
```

**Fark yalnızca 0,0017 (%0,1).**

Yani Task 8A yüzeyi **arşivin iki ayrı sonucunu tek eğrinin iki ucuna
alıyor**:

| Uç | `h` | κ eşiği | Karşılık gelen sonuç |
|---|---|---|---|
| `ρ = 0` | 0,5693 | **2,7840** | Task 7 + güçlendirme |
| `ρ = optimal` | 1,5040 | **1,0538** | CP19 T4 (`κ₀ = 1,0527`) |

> ## ⛔ DÜZELTME (2026-08-26, Drive freeze sonrası)
>
> Bu farkı "Sturmian faz kısıtının entropi maliyeti" diye yorumlamıştım
> ve Task 8A promptuna ispat maddesi koymuştum. **Yanlıştı.**
>
> Dondurulan `CP20_TASK8A_FINAL_FREEZE_DECISION`:
>
> > *"Maximizing h over F recovers CP19 Task 4 **exactly**; there is
> > **no strict optimized Sturmian phase cost**."*
>
> Fark benim 41×41 grid çözünürlüğümün artefaktıydı. Ayrıca feasible
> domain'de hesaba katmadığım bir kısıt var: **`ρ₁ − ρ₂ ≥ 3 − 2α`**.
> Doğru optimizasyon CP19 T4'ü **tam olarak** geri veriyor.
>
> Yani Task 8A, CP19 T4'ten "bir parça daha güçlü" **değil** — o noktada
> onunla **özdeş**. Yüzeyin değeri başka yerde: `ρ = 0` ile `ρ = optimal`
> arasındaki **tüm ara rejimi** parametrize etmesi.

---

# 5. CP19 Task 5 survivor testi

| | değer |
|---|---|
| survivor `κ` | 1,06 |
| survivor kritik yoğunluğu (findings'ten: `1 − 0,999855`) | **0,000145** |
| `ρ_min(1,06)` | **0,3514** |
| oran | **~2.400×** |

Survivor'ın taşıdığı kritik yoğunluk, gerekenden **üç mertebe** düşük.

> ## ⛔ DÜZELTME — SURVIVOR DIŞLANMIYOR
>
> Arşivin dondurduğu karar: `[CP19 TASK5 SURVIVOR NOT EXCLUDED —
> HYPOTHESIS MISMATCH]`. Survivor'ın **logaritmik excursion çekirdekleri**
> global kritik-log yasasını ihlal ediyor; yani Task 8A'nın hipotezi ona
> hiç uygulanmıyor.
>
> Yoğunluk karşılaştırması (0,000145 vs ~0,346) doğru, ama ondan
> "dışlanır" sonucunu çıkarmak yanlıştı — hipotez uyumunu kontrol
> etmemiştim.

---

# 6. Erken kapatma testi — GEÇİLDİ

Baş araştırmacının kriteri: *"Eğer küçük miktarda critical site eklemek
entropy engelimizi hemen yok ediyorsa dalı erkenden kapat."*

| `ρ` | κ eşiği |
|---|---|
| 0 | 2,784 |
| 0,01 | 2,41 |
| 0,1 | 1,56 |
| 0,2 | 1,28 |

Engel **kademeli** düşüyor, çökmüyor. `ρ = 0,01`'de hâlâ `κ ≥ 2,41`.

**Dal açık kalmalı.**

---

# 7. Sıradaki adım (Task 8B'ye giriş)

Yüzey artık şunu söylüyor:

> `κ ≈ 1,06` civarında bir survivor, sitelerinin **%35'inde** kritik
> olmak zorunda — ve bunların çoğu `g=1` sitelerinde.

Bu **çok yoğun** bir kısıt. Task 8B sorusu net:

> Bir pozitif ordinary tam sayı yörüngesi, sitelerinin %35'inde
> `a_k = g_k` koşulunu **sonsuza kadar** sürdürebilir mi?

Baş araştırmacının Sinai/Kontorovich Structure Theorem önerisi tam
buraya oturuyor: belirli valuation dizilerini gerçekleştiren
başlangıçlar açık aritmetik progresyonlarla tarif ediliyorsa, %35
yoğunluklu kritik site koşulunun progresyon yapısıyla uyumu doğrudan
sınanabilir.

---

# Denetim durumu

`[HESAPLANDI — DENETLENMEDİ]`

Denetime gitmeden önce gerekenler:
1. Analitik sadeleşmenin (μ kapalı formu) bağımsız türetimi
2. `μ` serbest bırakmanın Chernoff yönü açısından doğruluğu — "tam ρ"
   kısıtının Legendre dönüşümü titizce kurulmalı
3. Sturmian faz yapısının `ρ₁`/`ρ₂` ayrımıyla etkileşimi (Parikh
   dengeliliği kritik sitelerde de geçerli mi?)
4. `max h` ile `h(α)` arasındaki 0,0017 farkın **yapısal** olduğunun
   ispatı (şu an yalnızca sayısal gözlem)
5. Sabitler rasyonel/aralık aritmetiğiyle
