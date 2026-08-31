# CP20 Task 8B2 — D1 A/B/C Sparse-Injury Geometry Theorem
## Bağımsız zero-trust denetim raporu

**Denetlenen belge:** `CP20_TASK8B2_D1_SPARSE_INJURY_GEOMETRY_THEOREM.md`
(SHA256 `2a129544a56ee18a0466b5b7e370723a085a1ce3441389bb31ddc82cf98afa8f`)
**Denetim promptu:** `..._ZERO_TRUST_AUDIT_PROMPT_V2_MANAGER_STRENGTHENED_2026-08-27` (21 zorunlu madde)
**Tarih:** 2026-08-27

### VERDİCT

```
[PROOF VALID WITH WORDING REPAIR]
```

A, B, C, D, E ve F bölümlerinin **matematiksel içeriği doğru**. İki ifade
düzeltmesi gerekiyor (madde 15 ve 16), ikisi de kanıtın taşıyıcı adımlarına
dokunmuyor. Bölüm G'nin 4. maddesi bir **sonuç değil hedef**; öyle
etiketlenmeli.

Arşivin kendi `CP20_TASK8B2_D1_COUNTEREXAMPLE_REPORT.md` belgesindeki altı
saldırının altısı da bağımsız olarak yeniden üretildi ve aynı sonucu verdi.

---

## Yöntem notu

Arşivin `engine`'lerine bakılmadı. Bütün diziler sıfırdan kuruldu:

```python
B_{k+1} = 3 B_k + 2^{A_k},   A_{k+1} = A_k + a_k
r_k     = -3^{-k} B_k  (mod 2^{A_k})
R_k     = 3^{-k}(2^{A_k} - B_k)  (mod 2^{A_k+1})
```

Kritik-log kontrolörü tamsayı eşikle (float yok) üretildi:
`s ≤ 0` ya da `2^{κ_den · s} ≤ (k+1)^{κ_num}` iken `a_k = g_k - 1`, aksi halde `a_k = g_k + 1`.

---

## Madde madde sonuçlar

| # | Konu | Sonuç |
|---|---|---|
| 1 | `r_{k+1} = r_k + m_k 2^{A_k}`, `0 ≤ m_k < 2^{a_k}` | ✅ 9.688 test, 0 ihlal |
| 2 | `r_0 = 0` indekslemesi + teleskop `r_k = Σ_{j<k} m_j 2^{A_j}` | ✅ 0 ihlal |
| 3 | Kritik-log (yalnız sınırlı `O(1)` hata) ⟹ `a_k` sonunda sınırlı | ✅ `max a_k = 3`, alfabe `{1,2,3}`, κ = 1.053 / 1.5 / 2.0 |
| 4 | Plato aralığı `t_j+1 ≤ k ≤ t_{j+1}`, iki uçta off-by-one | ✅ 5.999 plato noktası, 0 ihlal |
| 5 | Sandviç `2^{A_{t_j}} ≤ r_k+1 ≤ 2^{A_{t_j+1}}` | ✅ 0 ihlal |
| 6 | `ρ_r(k) = ln3·(t_j/k) + O(log t_j/k)` düzgün | ✅ ikinci mertebe terim **işaret ve büyüklükçe tam** tutuyor (aşağıda) |
| 7 | `O(log t_j/t_{j+1}) → 0`, sadece `t_{j+1} ≥ t_j+1` ile | ✅ `\|hata\| ≤ C log t_j/t_{j+1} ≤ C log t_j/t_j → 0`, gizli varsayım yok |
| 8 | `ρ_r` plato üzerinde monoton azalan, min uçta | ✅ 1.480 plato, 0 ihlal |
| 9 | liminf'in `o(1)` hatadan geçişi | ✅ `liminf(x_j+e_j) = liminf x_j`, `e_j → 0` |
| 10 | `liminf t_j/t_{j+1} = 0 ⟺ bir altdizide t_{j+1}/t_j → ∞` | ✅ (ilk testim hatalıydı — aşağıya bkz.) |
| 11 | `r_{k+1} ≡ R_k (mod 2^{A_k+1})` bağımsız türetim | ✅ türetildi + 5.188 test, 0 ihlal |
| 12 | Terminal istisna: `q`'da injury varsa `R_q ≠ r_q` olabilir | ✅ |
| 13 | Somut terminal-injury örneği | ✅ `w=(1,1,1,1,1,1)`, `q=1`, `r_q=1`, `R_q=3 = r_q + 2^{A_q}` |
| 14 | "derinlik `q-1`'e kadar exact prefix" indekslemesi | ✅ tutarlı |
| 15 | **Manager sınırı:** `p=0, r_*=0` başlangıç platosu | ⚠️ düzeltme gerekli — ama managerin düşündüğünden **daha basit** |
| 16 | **Manager niceleyicisi:** tek tam sayı tüm platoları gölgeler mi | ⚠️ düzeltme gerekli — G-4 türemiyor |
| 17 | Yalnız dondurulmuş D0 + exact cylinder + global kritik-log | ✅ |
| 18 | Denetlenmemiş genel-`L`, Task 8A, Task 6, Sturmian, 3-adik yok | ✅ |
| 19 | Yenilik sınıflandırması (muhafazakâr) | ⚠️ A/B/F büyük ölçüde D0'ın yeniden paketlenmesi; **D/E gerçekten yeni** |
| 20 | Verifier'ı iki kez çalıştır + bağımsız saldırı | ✅ iki koşu bit-bit aynı; pencere-kriteri tuzağı test edildi |
| 21 | Paket bütünlüğü, SHA256 manifestosu | ✅ verifier ve sonuç JSON'u yeniden üretiyor |

---

## Madde 6/7/9 — ikinci mertebe terim

Teorem `O(log t_j/k)` diyor. Bu terimin **tam katsayısı** `-κ`:

```
ρ_r(t_{j+1}) = ln3·(t_j/t_{j+1}) − κ·ln(t_j)/t_{j+1} + O(1/t_{j+1})
```

Sayısal doğrulama (κ = 1.053 kontrolörü, adım ~6000):

| `t_j` | `t_{j+1}` | gözlenen | `ln3·t_j/t` | 2. mertebe dahil | kalan |
|---|---|---|---|---|---|
| 5989 | 5992 | 1.096548 | 1.098062 | 1.096534 | +0.000014 |
| 5992 | 5993 | 1.096920 | 1.098429 | 1.096901 | +0.000020 |
| 5996 | 5999 | 1.096518 | 1.098063 | 1.096536 | −0.000018 |

κ = 1.5 ve κ = 2.0 kontrolörlerinde de kalan `O(1/t)` mertebesinde. Bu, D
bölümünün `A_t ln2 = t ln3 − κ ln t + O(1)` adımının **tam** olduğunun
bağımsız doğrulaması.

---

## ⛔ MADDE 10 — kendi testimin hatası (teoremin hatası DEĞİL)

İlk koşuda madde 10 için `TUTARSIZ` bastırdım: ölçülen `liminf ρ_r ≈ 1.0920`
ile formülün verdiği `ln3·min(t_j/t_{j+1}) = 0.7324`. **Bu bir teorem kusuru
değil, testimin kusuruydu.** İki ayrı hata:

1. **İki farklı indeks kümesi kıyaslandı.** `ρ` minimumunu `k ∈ [1864, 6000]`
   üzerinde, oran minimumunu `j ∈ [1, 3726]` üzerinde aldım. `ρ` minimumu
   `k = 1946`'da, oran minimumu `(t_j, t_{j+1}) = (2, 3)`'te çıkıyor. Farklı
   yerler; kıyas geçersiz.
2. **`liminf` yerine `inf` alındı.** `liminf` bir *kuyruk* kavramı. Kuyruğu
   ilerlettikçe fark sıfıra gidiyor:

| kuyruk | `inf t_j/t_{j+1}` | `ln3 ×` bu | `inf ρ(trough)` | fark |
|---|---|---|---|---|
| `t_j ≥ 1` | 0.666667 | 0.732408 | 0.769511 | +0.037102 |
| `t_j ≥ 100` | 0.961039 | 1.055809 | 1.028462 | −0.027347 |
| `t_j ≥ 1000` | 0.995035 | 1.093157 | 1.086083 | −0.007075 |
| `t_j ≥ 3000` | 0.998353 | 1.096803 | 1.093984 | −0.002818 |

Doğru testte (`ρ` yalnız trough'larda, aynı `j` üzerinde) fark kuyrukta
`−0.0015` mertebesinde ve bu tam olarak `−κ ln t_j/t_{j+1}` terimi.
**Madde 10 doğrulandı.**

> Bunu D0 denetimindeki madde-9 hatamla aynı ailede kaydediyorum: her iki
> seferde de kriteri yanlış indeks kümesi üzerinde kurmuştum. Aynı tür hata
> başka bir maddede fark edilmeden kalmış olabilir.

---

## ⛔ MADDE 11 — ikinci kendi hatam (yine sentinel/indeks)

İlk koşuda 5.688 testte 500 ihlal gördüm. İhlallerin dağılımına baktığımda
**hepsi `k = 0`'da**: arşivin `affine()` fonksiyonu `R = [0]` sentinel'i ile
başlıyor, oysa doğru değer `R_0 = 1` (`c_0 = r_0 = 0` tek olmalı ⟹ `R_0 = 0 + 2^0`).

Bu **zararsız**: `check_word()` bu değeri hiç kullanmıyor, çünkü `k = 0`'da
her zaman injury var (madde 15) ve `if r[k+1] == r[k]` dalı orada hiç
çalışmıyor. `k ≥ 1` için yeniden koştuğumda 5.188 test, 0 ihlal.

Yine de not düşülmeli: bu sentinel ileride `R_0`'ı kullanan bir uzantıda
sessizce yanlış sonuç verir.

---

## ⚠️ MADDE 15 — manager sınırı: düzeltme gerekli, ama daha basiti var

Manager'ın uyarısı: "F lemması yazıldığı haliyle `p=0, r_*=0` başlangıç
platosunu içerebilir; bu yüzden 'pozitif sıradan tam sayı' yalnız
injury-sonrası platolar için (veya `r_* > 0` ayrıca varsayılırsa) haklı."

**Bulgu: `r_* > 0` ayrıca varsayılmak zorunda değil — türeyen bir olgu.**

`r_1 = -3^{-1} (mod 2^{a_0})` her zaman **tek**, dolayısıyla `r_1 ≥ 1 > 0 = r_0`.
Yani **`k = 0` daima bir injury indeksidir.** Bunun sonucu:

* `p = 0` olan (uzunluğu ≥ 1) bir plato **imkânsız** — `r_0 = r_1` olamaz;
* `r` kesin artan olduğundan her plato için `r_* ≥ r_1 > 0`.

Doğrulama: `a_0 = 1…24` için `r_1` hiç 0 ya da çift çıkmadı; `4^6 = 4.096`
kelimede `r_1 = r_0` olan yok, `r` azalan olan yok.

**Minimal ifade düzeltmesi** (F lemmasına tek satır):

> Since `r_1 = -3^{-1} (mod 2^{a_0})` is odd, `k = 0` is always an injury
> index; hence `p ≥ 1` and, `r` being non-decreasing, `r_* ≥ r_1 > 0`.
> Positivity therefore needs no separate hypothesis.

---

## ⚠️ MADDE 16 — manager niceleyicisi: bölüm G-4 bir SONUÇ DEĞİL

Bölüm G'nin 4. maddesi:

> "one fixed positive ordinary integer shadowing essentially every such
> exceptionally long plateau"

Bu **A/B/C/F'den türemiyor**, ve düz okunuşuyla **yanlış**. Her injury'de
`m_{t_j} ≥ 1` olduğundan `r_{t_j+1} = r_{t_j} + m·2^{A_{t_j}} > r_{t_j}`; yani
`r` kesin artan ve **ardışık platoların `r_*` değerleri hep farklı**.

Ölçülen ardışık plato tanıkları (rastgele `{1,2}` kelimesi, 60 adım):

```
1, 3, 11, 27, 91, 603, 4699, 12891, ...   (hepsi farklı, kesin artan)
```

**Gerekli düzeltme:** G bölümünün 4. maddesi "derived consequence" olarak
değil, açıkça **D1-D/D1-E için hedef (target/desideratum)** olarak
etiketlenmeli. Örnek ifade:

> 4. *(target, not derived here)* a single ordinary integer `n_0` whose
>    2-adic expansion agrees with `r_*` on every such exceptionally long
>    plateau. Sections A–F give only a **per-plateau** witness `r_*`, and
>    these witnesses are strictly increasing in `j`.

---

## Madde 19 — yenilik sınıflandırması (muhafazakâr)

| Bölüm | Sınıflandırma |
|---|---|
| A (chunk expansion) | **D0'ın yeniden ifadesi.** `m_k` sadece `r_{k+1}-r_k`'nın `2^{A_k}` cinsinden adı. |
| B (alfabe sınırı) | **Bir satırlık sonuç.** `s_{k+1}-s_k = g_k - a_k` özdeşliğinden doğrudan. |
| C (plato sandviçi) | **Yeni ama âşikâr.** İki uçtaki kanonik aralıklardan çıkıyor. |
| D + E (liminf özdeşliği) | **GERÇEKTEN YENİ yapısal sonuç.** `liminf ρ_r = ln3 · liminf t_j/t_{j+1}` D0'da yok. |
| F (sonlu realizer lemması) | **D0'ın exact-cylinder lemmasının yeniden ifadesi** + doğru terminal istisnası. |
| G | Sonuç değil, hedef listesi (bkz. madde 16). |

Yani paketin **taşıyıcı yeniliği D/E**. Kaçış senaryosunu "seyrek injury"den
"**çarpımsal olarak devleşen injury boşlukları**"na daraltması gerçek bir
kazanç.

---

## BULGU D (denetimin ötesinde) — plato = gerçek bir Syracuse yörüngesi

Denetim sırasında D1'in soruları için bağımsız bir yapı çıktı. Bunu ayrıca
raporluyorum çünkü baş araştırmacının D1-D/D1-E hedefini doğrudan etkiliyor.

**Tanım.** `c_k := (3^k r_k + B_k) / 2^{A_k}` (D0'ın derinlik-`k` bölümü).

**Karakterizasyon (10.432 testte 0 ihlal):**

```
k'da injury YOK   ⟺   a_k ≤ v₂(3 c_k + 1)
ve o durumda      c_{k+1} = (3 c_k + 1) / 2^{a_k}
```

**Rijitlik (5.238 plato-içi adımda 0 ihlal):** eğer `a_k < v₂(3c_k+1)` kesin
eşitsizse `c_{k+1}` çift olur, dolayısıyla `v₂(3c_{k+1}+1) = 0 < 1 ≤ a_{k+1}`
ve `k+1`'de **zorunlu injury**. Yani:

> Uzunluğu ≥ 2 olan bir platoda `a_k = v₂(3c_k + 1)` **tam eşitlik** zorunludur
> (yalnız platonun son adımı gevşek olabilir, o da platoyu bitirir).

**Sonuç 1.** Bir plato, sıradan bir tam sayının **gerçek Syracuse yörünge
parçasıdır** — "shadowing" mecazi değil, birebir.

**Sonuç 2.** `r_0 = 0 ⟹ c_0 = 0 ⟹ v₂(3·0+1) = v₂(1) = 0 ⟹ a_0 ≤ 0` imkânsız.
Madde 15'teki "k=0 daima injury" olgusunun **yapısal nedeni** budur.

**Sonuç 3 (minimal realizer).** Bir `w = (a_0…a_{L-1})` kelimesini
gerçekleştiren en küçük pozitif tam sayı **tam olarak `r_L(w)`**'dir.
Brute-force ile 120 kelimede 0 fark.

**Sonuç 4 (platonun bedeli).** `log₂ r_L / L → A_L/L → α`:

| `L` | `A_L` | `log₂ r_L` | `log₂ r_L / L` |
|---|---|---|---|
| 100 | 136 | 133 | 1.330 |
| 400 | 530 | 530 | 1.325 |
| 1600 | 2168 | 2167 | 1.354 |

Yani `ln(1+r_*)/L → ln3`. **Uzun plato kurulabilir, ama `ρ_r`'yi düşürmez:**
platonun tanığı tam olarak satın aldığı kadar büyür. `liminf ρ_r = 0` için
plato uzunluğunun tüm geçmişe göre **süper-lineer** büyümesi şart — D/E'nin
söylediği şeyin ta kendisi, bağımsız yoldan.

**Sonuç 5 (D1-D için uyarı).** Sonsuz plato ⟺ ıraksayan/döngüsel-olmayan bir
Collatz yörüngesi. Yani "sonsuza kadar devleşen exact-realizer platolar
gerçekten kurulabilir mi?" sorusu **LEVEL-3 probleminin kendisidir**, ondan
bağımsız bir saldırı yüzeyi değil. D1-D bu eşdeğerliği bilerek kurgulanmalı;
aksi halde döngüsel bir argümana girme riski var.

---

## Madde 20-21 — paket

* `CP20_TASK8B2_D1_VERIFY.py` SHA256 manifestoyla **birebir uyuşuyor**
  (`2abbd616…fdbfe77c3`).
* İki kez çalıştırıldı: her iki koşuda da 6.561 exact + 3.500 rastgele kelime,
  194.362 chunk, 27.445 non-injury exact-cylinder, 181.153 sandviç kontrolü,
  hepsi PASS. Üretilen JSON iki koşuda **bit-bit aynı** ve manifestodaki
  `ea6eb9f8…fd25bb3a` ile uyuşuyor.
* **Bağımsız saldırı — "uzun geçici plato" tuzağı:** D0 madde-9'da kendi
  düştüğüm hata. "Son 4 adımda `r` sabit ⟹ plato" penceresi test edildi:
  4.000 kelimeden 17'si kriteri sağlıyor, bunların 5'inde `R_L ≠ r_L`, yani
  **pencere kriteri yanıltıcı**. Arşivin verifier'ı bu tuzağa düşmüyor:
  pencere değil `if r[k+1] == r[k]` gerçek bir-adım testi kullanıyor. Doğru.

---

## Stratejik yorum (promptun istediği)

Soru: "D1 geçerliyse ve Kramer'in ayrı pozitif-liminf engeli de dayatılırsa,
hayatta kalan bir non-realizer'ın sonsuz çok injury + çarpımsal olarak
keyfî büyük injury boşlukları altdizisi taşıması gerekir. Bu doğru
bağlaç mı, ve D1 tek başına `liminf ρ_r = 0`'ı dayatıyor mu?"

**Bağlaç doğru.** D1 tek başına `liminf ρ_r = 0`'ı **dayatmıyor** — D1 yalnız
bir *eşdeğerlik* veriyor (`liminf ρ_r = ln3 · liminf t_j/t_{j+1}`). Sıfır
liminf ancak dışarıdan (Kramer'in pozitif-liminf engeli) dayatılırsa bağlaç
kapanır. Bu, teoremin H bölümündeki "No such sparse-injury branch is
excluded" ifadesiyle tutarlı ve **fazla iddia edilmemiş**. Bu noktada
teoremin kapsam disiplini doğru.

---

## Dondurma tavsiyesi

* **D1 A/B/C dondurulabilir** — madde 15 ve 16 ifade düzeltmeleri
  uygulandıktan sonra. İkisi de tek satırlık; taşıyıcı adımlara dokunmuyor.
  (Ek olarak `R_0 = 1` sentinel notu koda düşülmeli.)
* **D1-D adversarial recursive-countermodel araması D1-E'den ÖNCE
  başlayabilir.** Gerekçe: D1-D'nin hedef yüzeyi (çarpımsal boşluk altdizisi)
  artık kesin tanımlı ve D1-E'nin Sturmian/sürekli-kesir makinesine bağımlı
  değil. **Ancak** Bulgu D'deki eşdeğerlik (sonsuz plato ⟺ LEVEL-3) D1-D'nin
  başına açık bir uyarı olarak konmalı; aksi halde arama, çözmeye çalıştığı
  problemi varsayan bir kurguya kayabilir.
