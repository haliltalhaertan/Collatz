# CP20 Task 7 — Bağımsız Zero-Trust Denetim

**Tarih:** 2026-08-26
**Hedef:** `CP20_TASK7_MAJOR_THEOREM.md` — B=4 zero-critical ağırlıklı-basınç dışlaması
**Doktrin:** Hiçbir teorem, ondalık, kod yolu veya etikete güvenilmedi.
Arşivin engine dosyalarına bakılmadan tüm hesaplar sıfırdan yapıldı.

---

# BİRİNCİL VERDICT

```
[PROOF VALID WITH WORDING REPAIR]
```

Matematiksel içerikte hata bulunamadı. Onarım **kapsam ifadesinde**:
teorem iddia ettiğinden belirgin biçimde **daha geniş** ve findings'in
"hayatta kalan" listesi bir maddede yanlış.

## İstenen kapanış ifadeleri

**Hayatta kalan κ aralığı:**
- B=4 için: `κ ≥ 2,8207161949241867869…`
- Her sınırlı B için: `κ ≥ α/h_B`, ve `h_B` monoton artarak `h_∞`'a çıkar
- **Sınırsız alfabe dahil:** `κ ≥ 2,7840109030009018862…`

**Eşik sertifikası downstream için yeterince titiz mi?**
**Kısmen.** Aralık sertifikası bağımsız hesabımla tutuyor, ama benim
doğrulamam 80 basamak kayan nokta — *kanıt değil*. CP17'de uygulanan
standart (rasyonel/aralık aritmetiği, proof-critical kararda ondalık
yasak) burada da uygulanmalı. `h_4`'ün üstten, `α/h_4`'ün alttan
rasyonel sınırlanması yazılı olarak gösterilmeli.

---

# Madde madde

## Madde 1 — B=4 zero-criticality yerel defect destekleri

Bağımsız türetildi:

| Site | İzinli `a` | Defect `d = g−a` |
|---|---|---|
| `g=1` | `{2,3,4}` | `{−1,−2,−3}` |
| `g=2` | `{1,3,4}` | `{+1,−1,−2}` |

Teoremdeki üreteç fonksiyonuyla birebir uyuşuyor:
`e^{−λ}+e^{−2λ}+e^{−3λ}` ve `e^{λ}+e^{−λ}+e^{−2λ}`. `[VALID]`

## Madde 2 — Sturmian Parikh özdeşliği

`n₂(u,r) = ⌊(α−1)(u+r)⌋ − ⌊(α−1)u⌋`

| Test | İhlal |
|---|---|
| 240.000 `(u,r)` çifti | **0** |

Dengelilik: `r = 1…5000` için her `r`'de **tam iki** Parikh değeri ve
aralarında **tam 1** fark. Sturmian dengelilik özelliği doğrulandı.
`[VALID]`

## Madde 3 — Chernoff işareti ve minimizasyon yönü

Pozitif katsayılı üreteç `P(t) = Σ_S N(S)t^S` için `N(S)·t^S ≤ P(t)` her
`t>0` için, dolayısıyla **`N(S) ≤ P(t)·t^{−S}`**. Minimizasyon `λ` üzerinde
ve belirtilen yönde.

> **DÜZELTME (2026-08-26, Drive freeze sonrası):** bu raporun ilk hâlinde
> sınır `N ≤ P(t)·t^{+S}` diye yazılmıştı — işaret hatası. Arşivin bağımsız
> denetimi bunu *"a real sign/wording bug"* olarak tespit etti ve V3'te
> düzeltildi. `|S| = O(log r)` olduğundan üstel entropi oranı `h_B`
> değişmiyor; yalnızca polinom prefactor etkileniyor.

Bağımsız kontrol: `f''(λ*) = 0,3646 > 0` → gerçek **minimum**, maksimum
değil. Ters çevrilmiş bir işaret bulunamadı. `[VALID]`

## Madde 4 — `O(log r)` defect bandı polinom mu?

`exp(λ*·C_D)` çarpanı; `C_D = κlog₂r + C` alındığında
`exp(λ*κ log₂ r) = r^{λ*κ/ln2}` — **polinom**, üstel değil.
`log₂(·)/r → 0`. `[VALID]`

Sayısal doğrulama (sabit `C_D = 8`, B=4):

| r | `log₂N/r` |
|---|---|
| 10 | 1,21507 |
| 80 | 0,68459 |
| 320 | 0,60004 |
| 640 | 0,57944 |

`h_4 = 0,56190`'a **yukarıdan** yaklaşıyor. Fazlalık `0,01754`;
öngörülen prefactor katkısı `log₂(exp(λ*·8))/640 = 0,0277` — aynı
mertebede, tutarlı.

## Madde 5 — Kritik-log yasasından global üst sınıra geçiş

Asimptotik rejim öncesindeki sonlu başlangıçlar: `u < u₀` olan konumlar
en fazla `u₀` ek faktör katar (sabit), `log₂(·)/r`'de kaybolur.

Her faktörün defect toplamı `s_{u+r} − s_u = κlog₂((u+r)/u) + O(1)`;
`u` küçükken `O(log r)`, `u ≥ r` iken `O(1)` — her durumda bant
`O(log r)` içinde. Madde 4 bunu kapsıyor.

Ayrıca faktörün **ara** prefix toplamları da kısıtlı; bu gerçek sayımı
daha da azaltır, yani üst sınır fazlasıyla geçerli kalır. `[VALID]`

## Madde 6 — Basınç fonksiyonu, dışbükeylik, sertifika

Bağımsız hesap (mpmath, 80 basamak):

| Büyüklük | Hesaplanan | Arşivde |
|---|---|---|
| `λ*` | 1,5330136684139087818253460674861024575235320530573 | **aynı** |
| `h_4` | 0,56190073413740076092680318182803927479638935199516 | **aynı** |
| `α/h_4` | 2,8207161949241867869006891038446082915753302064363 | **aynı** |

50 basamağa kadar birebir. Sertifika aralığı
`[2,82071619492418598…, 2,82071619492418758…]` — hesaplanan değer
aralığın içinde. `f''(λ*) > 0` → tek minimum. `[VALID]` *(titizlik notu
yukarıda)*

## Madde 7 — Bağımsız sonlu sayımlar

Arşivin iki engine'i kullanılmadan, sıfırdan dinamik programlama ile
`N(r, C_D)` sayıldı (B=3 ve B=4, `C_D ∈ {0,2,8}`, `r` = 10…640).
Oranlar ilgili `h_B` değerlerine yakınsıyor.

Faz bağımlılığı ölçüldü: `N(r,0)` fazlar arasında ~15–17 kat değişiyor —
**sabit** çarpan, `r` ile büyümüyor, asimptotikte etkisiz. `[REPRODUCED]`

## Madde 8 — Task 6 ile birleştirme, eşitsizlik yönü

```
α/κ  ≤  liminf log₂p_a(r)/r  ≤  limsup log₂p_a(r)/r  ≤  h_4
```
⟹ `α/κ ≤ h_4` ⟹ `κ ≥ α/h_4`. Yön doğru.

Task 6'nın §5 alt sınır teoremi **alfabeden bağımsız** (yalnızca Lemma
A/B/C kullanıyor), dolayısıyla B=4'e uygulanabilir. `[VALID]`

⚠️ **Prosedürel bulgu:** Task 7 belgesi "**Frozen** CP20 Task 6" diyor.
Task 6 **donmuş değil** — bugünkü denetimim `PROOF VALID WITH WORDING
REPAIR` verdi ve onarım henüz yapılmadı. Onarım controller lemmasındaydı,
Task 7'nin kullandığı §5 alt sınırında değil; dolayısıyla matematiksel
risk düşük. Ama etiket yanlış ve düzeltilmeli.

## Madde 9 — Park edilmiş CP19 high-half mekanizması geri geldi mi?

**Hayır.** Argüman yalnızca Sturmian kombinatoriği + Chernoff basıncı
kullanıyor. Hiçbir yerde 2-adic endpoint biti, büyüyen hassasiyet ya da
cross-adic yapı taşınmıyor. `[TEMİZ]`

## Madde 10 — Karşı-örnek üretme girişimi

| Saldırı | Sonuç |
|---|---|
| Parikh özdeşliğini kırmak | Başarısız (0/240.000) |
| Dengeliliği bozan bir `r` bulmak | Başarısız (r ≤ 5000) |
| Minimizasyon yönünü ters çevirmek | Başarısız (`f'' > 0`) |
| Sabit `C_D` ile `h_4`'ü kalıcı aşmak | Başarısız (yukarıdan yakınsıyor) |
| Faz seçimiyle üstel fark yaratmak | Başarısız (sabit ~17 kat) |

Karşı-örnek bulunamadı.

---

# ONARIM GEREKTİREN BULGULAR

## Bulgu A — Teorem B=4'e özel değil

`h_B`'yi genel `B` için hesapladım:

| B | `h_B` | `κ_B* = α/h_B` |
|---|---|---|
| 3 | 0,523466680692 | **3,02781926564** |
| 4 | 0,561900734137 | 2,82071619492 |
| 6 | 0,569032730466 | 2,78536262655 |
| 10 | 0,569308552992 | 2,78401315489 |
| 16 | 0,569309013454 | 2,78401090316 |

`h_B` monoton artıyor ve hızla **sabitleniyor**.

## Bulgu B — Sınırsız alfabe de kapsanıyor

`B → ∞` limitinde geometrik seriler yakınsıyor (`e^{−λ*} = 0,2025 < 1`):

```
λ*_∞ = 1,596795249104046749…
h_∞  = 0,569309013485800536…
κ_∞* = 2,784010903000901886…      (f'' = 0,4034 > 0, gerçek minimum)
```

**Sonuç:** basınç argümanı sınırlı alfabeye bağlı değil. Geçerliyse,
**sınırsız valuationlu** zero-critical kritik-log diziler için de
`1 < κ < 2,784…` dışlanır.

Ama Task 7 findings, "surviving / untouched" listesinde açıkça
**"unbounded valuations"** yazıyor. Bu **yanlış** — kendi yöntemi onu
kapsıyor. Kapsam ifadesi düzeltilmeli.

## Bulgu C — Task 6'nın B=3 sonucu bu yöntemle iki kat güçleniyor

Task 6, B=3 için **kaba** alfabe sayımı kullanıyordu: `p_a(r) ≤ (r+1)2^r`,
yani entropi `≤ 1`, sonuç `κ ≥ α ≈ 1,585`.

Aynı basınç yöntemi B=3'e uygulanınca `h_3 = 0,5235` ve
**`κ ≥ 3,0278`** — Task 6'nın sonucunun neredeyse iki katı.

Bu, findings'te hiç geçmiyor. Task 7 kendi yönteminin geriye dönük
kazanımını fark etmemiş.

---

# Genel değerlendirme

Task 7'nin fikri Task 6'dan **daha güçlü**: Task 6 kaba alfabe sayımı
yapıyordu, Task 7 kritik-log kısıtını büyük-sapma cezası olarak
kullanıyor. Bu, doğru yönde gerçek bir yöntemsel sıçrama.

Ve sonuç, üç bulgu birleştiğinde şu tek ifadeye toplanıyor:

> Zero-critical, kritik-logaritmik, **herhangi bir** valuation
> alfabesiyle (sınırsız dahil) pozitif ordinary Syracuse yörüngesi
> `1 < κ < 2,784…` aralığında var olamaz.

Bu, arşivin yazdığından belirgin biçimde geniş bir ifade.

**Hâlâ tamamen açık:** kritik siteler (`a_k = g_k`) ve kritik-logaritmik
olmayan discrepancy yasaları. `κ ≥ 2,784` da açık. Collatz çözülmedi.

# Öneriler

1. Kapsam ifadesini düzelt: teorem her `B` ve `B=∞` için geçerli;
   "unbounded valuations" hayatta kalan listesinden çıkarılmalı.
2. Bulgu C'yi Task 6'ya geri uygula (B=3 eşiği 1,585 → 3,028).
3. Eşik sertifikasını rasyonel/aralık aritmetiğiyle yeniden üret
   (CP17 standardı).
4. "Frozen CP20 Task 6" etiketini düzelt — Task 6 onarım bekliyor.
5. Onarımlar sonrası dondurulabilir.

# Denetimin kendi sınırı

Task 6 denetimindeki uyarı burada da geçerli: bu da bir AI denetimi.
Sabitler ve sayımlar bağımsız üretildi, ama Chernoff'tan `p_a(r)`'ye
geçişin **ölçü-teorik inceliği** kâğıt üzerinde takip edildi ve sayısal
olarak test edilemez. Oradaki bir hata bu yöntemle yakalanmazdı.

## Çalıştırmak için

```bash
python3 01_h4_sabiti_ve_capraz_kontrol.py   # mpmath gerekir
python3 02_bagimsiz_dp_sayimi.py
python3 03_kapsam_taramasi_B.py
python3 04_sinirsiz_alfabe.py
python3 05_sturmian_parikh.py
```
