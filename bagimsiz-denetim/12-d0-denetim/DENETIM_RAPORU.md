# CP20 Task 8B2 — D0 Bağımsız Zero-Trust Denetimi

**Tarih:** 2026-08-26
**Hedef:** D0 rate/stabilization teoremi
**Prompt:** `CP20_TASK8B2_D0_ZERO_TRUST_AUDIT_PROMPT_V2_MANAGER_STRENGTHENED`
**Yöntem:** Arşivin engine'lerine bakılmadı; tüm kod sıfırdan yazıldı.

---

# BİRİNCİL VERDICT

```
[PROOF VALID WITH WORDING REPAIR]
```

Çekirdek cebir ve ana ekvivalans doğru. Onarım **M3'te** (wording), ve
**M1** teoremi ikiye ayırmayı gerektiriyor.

## İstenen kapanış ifadeleri

**A. Global güçlendirme (kritik-log olmadan) geçerli mi?**
**EVET.** Doğrulandı — ayrıntı §M1.

**B. Her ekvivalansın minimal hipotezleri:**

| İfade | Gereken hipotez |
|---|---|
| `LEVEL-3 realizer var ⟺ r_k stabilize` | **yalnızca `a_k ≥ 1`** |
| `r_k stabilize ⟺ ρ_r(k) → 0` | **yalnızca `a_k ≥ 1`** |
| `⟺ limsup ρ_r < ln3` | **kritik-log gerekli** |
| `realizer yok ⟹ limsup ρ_r = ln3` | **kritik-log gerekli** |

**C. `liminf=0, limsup=ln3` wording'i onarım gerektiriyor mu?**
**EVET** — manager'ın M3 tespiti doğru.

**D. D0 dondurulabilir mi?** **Evet**, A ve C onarımlarından sonra.

**E. D1–D5 devam edebilir mi?** **Evet.**

---

# Zorunlu kontroller

## Madde 1–2 — `B_v` özdeşliği ve nesting

`B_v = 3^{v−u}B_u + Σ_{i=u}^{v−1} 3^{v−1−i}2^{A_i}` ve
`r_v ≡ r_u (mod 2^{A_u})`:

| Test | İhlal |
|---|---|
| 52.190 | **0** |

`[VALID]`

## Madde 3–5 — injury yukarı, `r_{k+1} ≥ 2^{A_k} ≥ 2^k`

`r_{k+1} ≡ r_k (mod 2^{A_k})`, her ikisi de aralıkta ⟹
`r_{k+1} = r_k + m·2^{A_k}`, `m ∈ {0,…,2^{a_k}−1}`.
Injury ⟺ `m ≥ 1` ⟹ `r_{k+1} ≥ 2^{A_k}`. Ve `a_j ≥ 1 ⟹ A_k ≥ k`.

| Test | İhlal | Gözlenen min oran |
|---|---|---|
| 6.430 injury | **0** | **0,693147** = `ln2` tam |

`[VALID]`

## Madde 7–8 — `R_k ∈ {r_k, r_k+2^{A_k}}` ve `R` nesting

| Kontrol | Test | İhlal |
|---|---|---|
| `R_k` iki seçenekten biri | 4.137 | **0** |
| `R` nesting mod `2^{A_u+1}` | 24.018 | **0** |

`[VALID]`

## Madde 9 — one-bit lift ⚠️ (ve kendi hatam)

**İlk sayısal testim karşı-örnek verdi: 78 r-stabil örnekten 46'sında
`R` stabilize etmiyordu.** Somut örneği açtım — **karşı-örnek geçersiz.**

Test kriterim "son 4 adımda `r` sabit" idi. Ama incelenen örnekte `r_k`
defalarca sıçrıyor (`1 → 33 → 545 → 131.617 → …`); son 4 adımdaki
sabitlik **geçici plato**, gerçek stabilizasyon değil.

**Doğru cebir:**

```
r_{k+1} ≡ R_k  (mod 2^{A_k+1})   ve   r_{k+1} = r_*  (stabilizasyon)
R_k = r_* + 2^{A_k} olsaydı:
    r_* ≡ r_* + 2^{A_k}  (mod 2^{A_k+1})  ⟹  2^{A_k} ≡ 0 (mod 2^{A_k+1})  YANLIŞ
⟹ R_k = r_*
```

Gerçek stabilizasyon `R`'yi de stabilize etmeye **zorluyor**. `[VALID]`

*Not:* `R_k`'nın sıçraması, `a_k = 1` olduğunda `r_{k+1} = R_k` demek —
yani sıçrama habercisi. Tutarlı.

## Madde 10 — `r_* > 0` ve tek

| r-stabil örnek | `r_* = 0` | `r_*` çift |
|---|---|---|
| 103 | **0** | **0** |

`[VALID]`

## Madde 11 — gerçek `n_0` ⟹ `r_k = n_0` eventually

925 gerçek Syracuse yörüngesi, `2^{A_k} > n_0` olduktan sonra:
**0 ihlal.** `[VALID]`

## Madde 20 — kritik-log dışı örnekler

| kelime | injury | `r` stabilize | `limsup ρ_r` | tavan `A_k ln2/k` |
|---|---|---|---|---|
| `a_k = 1` (all-ones) | 399 | hayır | 0,6931 | **0,6931** |
| `(1,2)^∞` | 399 | hayır | 1,0397 | **1,0397** |
| `a_k = 2` | **0** | **evet** | 0,0020 → 0 | 1,3863 |

`a_k = 2` gerçek 1-döngüsü (`n=1`), tek realizer'lı örnek — ve tek
stabilize eden. Teoremin doğru çalıştığının temiz kontrolü.

**Ek bulgu:** iki nonstabilizing örnekte `limsup ρ_r` **tavana eşit**.
Bu, M2'nin genel hâlini düşündürüyor (§Ek bulgu).

## Madde 21 — kırma: sonsuz injury + `ρ_r → 0`?

**İmkânsız.** Injury ⟹ `ρ_r(k+1) ≥ k·ln2/(k+1) → ln2 > 0`.
3.000 rastgele kelimede en düşük kuyruk injury oranı **1,270** (≫ `ln2`).
Karşı-örnek yok. `[VALID]`

## Madde 22 — kırma: kritik-log + nonstabilizing + `limsup < ln3`?

**İmkânsız.** Kritik-log ⟹ `A_k ln2/k → ln3`. Sonsuz injury ⟹
`ρ_r(k+1) ≥ A_k ln2/(k+1) → ln3`. Tavan da `ln3`. Yani `limsup = ln3`
zorunlu. `[VALID]`

## Madde 24 — Task 8A / Task 6 / 3-adic kullanımı

D0'ın ispatında basınç, repeated-factor teoremi veya 3-adic endpoint
rate **kullanılmıyor**. Yalnızca `B_k` rekürans cebiri + 2-adic nesting.
`[TEMİZ]`

---

# Manager'ın ön gözlemleri

## M1 — global güçlendirme ✅ **DOĞRU**

İlk üç ifade kritik-log hipotezine **hiç ihtiyaç duymuyor**:

```
LEVEL-3 realizer var  ⟺  r_k stabilize  ⟺  ρ_r(k) → 0
```

- (⟹) Injury ⟹ `r_{k+1} ≥ 2^{A_k} ≥ 2^k` ⟹ `ρ_r(k+1) ≥ ln(1+2^k)/(k+1) → ln2`.
  Sonsuz injury ⟹ `limsup ρ_r ≥ ln2 > 0`.
- (⟸) Sonlu injury ⟹ `r_k = r_*` ⟹ `ρ_r(k) = ln(1+r_*)/k → 0`.
- Realizer ⟹ `2^{A_k} > n_0` olunca `r_k = n_0` (madde 11'de doğrulandı).
- One-bit lift nesting ile çalışıyor (madde 9).

**Kullanılan tek hipotez: `a_k ≥ 1`.**

**Öneri (manager'ınkiyle aynı):** teoremi ikiye ayır —
(i) genel pozitif-üstel-kelime stabilizasyon teoremi;
(ii) kritik-log keskinleştirmesi, eşik `ln3`.

## M2 — kritik-log keskinleştirmesi ✅ **DOĞRU**

Kritik-log ⟹ `A_k = αk − κlog₂k + O(1)` ⟹ `A_k ln2/k → ln3`.

- **Tavan:** `r_k < 2^{A_k}` ⟹ `ρ_r(k) ≤ A_k ln2/k → ln3`
- **Injury spike:** `r_{k+1} ≥ 2^{A_k}` ⟹ `ρ_r(k+1) ≥ (A_k ln2/k)·k/(k+1) → ln3`
- Sonsuz injury ⟹ `limsup ρ_r = ln3`

Nicelik yapısı ve `O(log k/k)` terimleri tutarlı. `[VALID]`

## M3 — wording sorunu ✅ **DOĞRU, ONARIM GEREKLİ**

D0 tek başına `liminf ρ_r = 0`'ı **zorlamıyor**. Teorem yalnızca
`limsup ρ_r = ln3` veriyor; `liminf ρ_r > 0` ile birlikte de tutarlı.

Osilatör şekil (`liminf=0, limsup=ln3`) ancak Kramer'in positive-liminf
obstruction'ından kaçınma **ek olarak** istendiğinde tek kalan olur.

**Metinde bu ayrım açıkça yazılmalı.** Bu, verdict'in wording repair
kısmıdır.

---

# ⭐ Ek bulgu — M2'nin genel hâli

Madde 20 ölçümleri, sonsuz injury durumunda `limsup ρ_r`'nin **tavana
eşit** olduğunu gösteriyor:

| kelime | `limsup ρ_r` | `lim A_k ln2/k` |
|---|---|---|
| all-ones | 0,6931 | 0,6931 |
| `(1,2)^∞` | 1,0397 | 1,0397 |

Bu, kritik-log'a özgü değil. Genel ifade:

> Sonsuz injury ⟹ `limsup ρ_r = lim_k A_k ln2 / k` (tavan),
> ve kritik-log bu limiti `ln3` yapar.

Bu, D0'ı **kritik-log'dan tamamen bağımsız** bir çatıya oturtur; M1'in
önerdiği ayrımın doğal tamamlayıcısı. Teorem metnine eklenmeye değer.

*(Bu, bu denetimin ek gözlemidir; kanıt taslağı yok, sayısal.)*

---

# Novelty (madde 27) — kısmi

D0'ın çekirdeği (`r_k` nesting + injury sıçraması) **temel 2-adic
cebirdir** ve CP18 Task 6/10'un "unique 2-adic realizer" ifadesine çok
yakın. Yeni olan, bunun bir **oran** (`ρ_r`) diliyle ifade edilip
`ln3` eşiğine bağlanması.

Kramer 2026 (`arXiv:2607.10041`) exponent-code uzayında 2-adic start /
3-adic endpoint temsilcileri kullanıyor ve kendisini **diagnostic**
olarak konumluyor. D0'ın `liminf` obstruction'ı ile ilişkisi M3'te
zaten işaretlenmiş.

**Aşırı novelty iddiası yapılmamalı** — çekirdek cebir standart.
Katkı: oran formülasyonu + eşik.

---

# Denetimin kendi sınırı

Bu da bir AI denetimi. Bugün Drive'daki bağımsız denetim beni üç ayrı
yerde düzeltti; burada da mümkün.

Özellikle: madde 9'da **önce yanlış bir karşı-örnek ürettim** ve ancak
somut örneği elle açınca test kriterimin hatalı olduğunu gördüm. Aynı
tür hata başka bir maddede fark edilmeden kalmış olabilir.

Sayısal testler sonlu kelimelerde; "eventually stabilize" gibi
asimptotik ifadeler sonlu kesitte **tam** test edilemez — cebirsel
argümanlara dayandım.
