# CP20 Task 6 — Bağımsız Zero-Trust Denetim

**Tarih:** 2026-08-26
**Hedef:** `CP20_TASK6_MAJOR_THEOREM.md`
**Doktrin:** İspatı doğrulamak değil, **kırmak** için çalışıldı.
Arşivdeki hiçbir engine dosyasına bakılmadı; tüm kod sıfırdan yazıldı.

---

# BİRİNCİL VERDICT

```
PROOF VALID WITH WORDING REPAIR
```

Ana teorem (§1–§7) geçerli. Tek onarım **controller'ın sınırlı-takip
lemmasında**, ana teoremde değil (ayrıntı: Madde 7).

## Ayrı ayrı istenen cevaplar

| Soru | Cevap |
|---|---|
| Faktör-karmaşıklığı alt teoremi geçerli mi? | **Evet** |
| Zero-critical `B=3` korolları geçerli mi? | **Evet** |
| Tam `κ=1,053` controller dışlanıyor mu? | **Evet** (controller'ın varlığı ayrıca doğrulandı) |
| Sonuç iddia edildiği gibi genelleşiyor mu? | **Evet**, `α/κ ≤ log₂(B−1)` biçiminde |
| Herhangi bir adım gizlice park edilmiş high-half argümanı mı? | **Hayır** — hiçbir yerde büyüyen endpoint-bit durumu taşınmıyor |
| Teorem literatürde zaten var mı? | **Bulunamadı** (ayrı rapor: `02-.../LITERATUR_RAPORU.md`) |
| Dondurulup downstream kullanılabilir mi? | **Evet**, onarım yapıldıktan sonra |
| Collatz çözüldü mü? | **Hayır** |

---

# Madde madde

## Madde 1 — İndeksleme, affine formül, örtüşen occurrence'lar

`2^{A(W)} n_{u+r} = 3^r n_u + B_W` özdeşliğinin her iki konumda **aynı**
`B_W` ile geçtiği doğrulandı: `B_W` yalnızca `W`'nin harflerine bağlı
(`B_W = Σ_{i<r} 3^{r−1−i} 2^{A(W_{<i})}`), konuma değil. Çıkarma geçerli.

Audit promptu özellikle **örtüşen** occurrence'ları soruyordu. Ayrı ayrı
test edildi:

| Durum | Test | İhlal |
|---|---|---|
| Örtüşen (`v−u < r`) | 439.234 | **0** |
| Ayrık (`v−u ≥ r`) | 3.065.970 | **0** |

İspat yalnızca `W`'nin iki kez **geçmesini** kullanıyor, konumların ayrık
olmasını değil — örtüşme yapısal olarak önemsiz. `[VALID]`

## Madde 2 — Eşit-durum boşluğu

`n_u = n_v` ise determinizm gereği `n_{u+j} = n_{v+j}` her `j` için;
`a_k = v₂(3n_k+1)` yalnızca `n_k`'ya bağlı olduğundan valuation kelimesi
eventually periodic olur. Eventually periodic kelime → `A_k/k` rasyonel
limite gider. Ama hipotez `s_k = κlog₂k + O(1)` → `A_k/k → α` irrasyonel.
Çelişki.

Ön-periyodik kısım sonlu olduğu için limiti etkilemez; minimal olmayan
periyot da rasyonelliği bozmaz. Boşluk yok.

Ampirik: 50.000 yörüngede 1-döngüsü dışında **sıfır** durum tekrarı.
`[VALID]`

## Madde 3 — Polinom durum sınırı (Lemma A)

`B_k/3^k = (1/3)Σ_{j<k} 2^{A_j−αj}` — tüm terimler **pozitif**, `j=0`
terimi `2^0 = 1` (mevcut ve doğru). `A_j − αj = −s_j − {αj} = −κlog₂j+O(1)`
→ `2^{A_j−αj} = O(j^{−κ})`; `κ>1` → yakınsak → `B_k/3^k = O(1)`.
`3^k/2^{A_k} = 2^{s_k+{αk}} = O(k^κ)`. Çarpım: `n_k = O(k^κ)`.

Gizli bir alt sınır gerekmiyor; teorem yalnızca üst sınırı kullanıyor.
(Aslında `n_k = Θ(k^κ)` de çıkarılabilir, ama gerekmiyor.) `[VALID]`

## Madde 4 — Yerel valuation kütlesi (Lemma C)

`A(u,r) = (F_{u+r}−F_u) − (s_{u+r}−s_u)`.
`F_{u+r}−F_u ≥ αr−1` her zaman.
`s_{u+r}−s_u = κlog₂((u+r)/u) + (e_{u+r}−e_u)`; `r ≤ u` iken
`κlog₂((u+r)/u) ≤ κlog₂2 = κ`, ve `|e_{u+r}−e_u| ≤ 2C`.
Yani `|s_{u+r}−s_u| ≤ κ+2C` — **`u` ve `r`'den gerçekten bağımsız**.

`r ≤ u` kısıtı zorunlu ve teoremde `u ≥ N_r` ile sağlanıyor (`N_r`,
`r`'de üstel olduğundan `r ≪ N_r`). `[VALID]`

## Madde 5 — Faktör-karmaşıklığı alt sınırı, nicelik sırası

`N_r = ⌊2^{(α/κ−ε)r}⌋` seçimi denetlendi:

- `r ≪ N_r`: `α/κ = 1,505 > 1` olduğundan `ε` küçükken `N_r` üstel — ✓
- `[N_r, 2N_r−r]` aralığında `N_r−r+1 ~ N_r` başlangıç konumu — ✓
- Durum üst sınırı bu aralıkta uniform: `n_k ≤ C₁(2N_r)^κ` — ✓
- Tekrarlanan faktör çelişkisi:
  `C₁2^κ2^{(α−κε)r} < 2^{αr−C_A}` ⟺ `C₁2^κ2^{C_A} < 2^{κεr}`;
  sol taraf **sabit**, sağ taraf `r→∞` ile sonsuz — ✓
- `liminf ≥ α/κ − ε` her `ε>0` için → `liminf ≥ α/κ` — ✓

**Nicelik sırası doğru:** önce `ε` sabitleniyor, sonra `r→∞`. Ters
sıralama yok. Hipotezleri sağlayıp daha küçük faktör karmaşıklığı veren
bir dizi arandı; bulunamadı (bulunması Lemma A/B/C ile çelişirdi).
`[VALID]`

## Madde 6 — Zero-critical üst karmaşıklık

`g_k − 1 = ⌊(k+1)(α−1)⌋ − ⌊k(α−1)⌋`, `α−1` irrasyonel → Sturmian →
`p_g(r) = r+1`. `r = 1..20` için doğrudan sayımla **tam olarak `r+1`**
(ihlal yok).

`p_a(r) ≤ (r+1)(B−1)^r`: her konum, kendi `g`-faktörünün belirlediği
`(B−1)^r` boyutlu bir kümeye düşer; `g`-faktörü sayısı `r+1`.

Promptun sorduğu incelik — *bir `a`-faktörü birden fazla `g`-faktörüyle
ilişkilendirilebilir mi?* — evet, ilişkilendirilebilir, ama bu birleşim
kümesini **küçültür** (örtüşme), büyütmez. Üst sınır geçerli kalır.

Üç farklı zero-critical kelimede test edildi (controller, rastgele,
adversarial); `r = 5,10,15,20` için hepsinde sağlandı. `[VALID]`

## Madde 7 — Controller hipotezleri ⚠️ ONARIM

**Bağımsız yeniden kurulum başarılı.** Yalnızca
`CP20_TASK6_CONTROLLER_DEFINITION.md`'deki kural kullanılarak
(bang-bang: `d_k = +1` ⟺ `g_k=2` ve `s_k ≤ q_k`), eşik tam sayı
formunda (`2^{1000s_k} ≤ m^{1053}`, float yok), 100.000 sembol üretildi:

```
SHA256 hesaplanan : 31d2db3d10ec0610f1c17fc86a6b485f6e8a378ed7696d5b41ad48e51980e1d2
SHA256 arşivde    : 31d2db3d10ec0610f1c17fc86a6b485f6e8a378ed7696d5b41ad48e51980e1d2
                    EŞLEŞTİ
```

*(Serileştirme ham byte; arşiv bunu belgelemiyor — küçük bir
dokümantasyon eksiği.)*

Doğrulananlar: `a_k ∈ {1,2,3}` ✓, `a_k ≠ g_k` her konumda ✓, `κ>1` ✓,
`κ<α` ✓.

**ONARIM GEREKEN NOKTA.** Sınırlı-takip lemmasının son adımı:

> *"A negative episode can drop by at most 2 per single step. Hence its
> lowest point occurs within a uniformly bounded initial part of the
> episode. A coarse bound such as −41 ≤ z_k ≤ 1 follows."*

"Hence" burada bir ispat değil, bir sezgi. Sonucun **doğru** olduğuna
ikna oldum ve rekonstrüksiyonu şu argümanla tamamladım:

- `z ≤ 0` olan her 20-adımlık blokta `z_{k+20} ≥ z_k + 1`
  (blokta 11–12 tane `g=2` kazanç, 9–8 tane `g=1` kayıp → net `s` artışı
  `≥ 2`; `q` artışı `≤ 1`)
- adım başına düşüş `≤ 2` → blok içi düşüş `≤ 40`
- `z₀ = −1` → `z ≥ −41`

Bu, `−41` sayısının nereden geldiğini açıklıyor ve iddiayı kurtarıyor.
Ama **metinde yazılı değil** — yazılmalı.

Ampirik olarak sınır fazlasıyla gevşek: gözlenen aralık `z ∈ [−2, 1]`
(k ≥ 100, 100.000 adım). İddia edilen `[−41, 1]`.

`[VALID AFTER WORDING REPAIR]`

## Madde 8 — Karşı-örnek disiplini

Her aday karşı-örneğin **hangi hipotezle** bloklandığı tespit edildi:

| Aday | Bloklayan | Neden |
|---|---|---|
| `a_k = 2` (gerçek 1-döngüsü) | (H1) | `s_k/k → −0,415`, lineer; log formu yok. Ayrıca eventually periodic |
| Eventually periodic (örn. `1,2,1,3`) | (H1) | periyot ortalaması `1,75 ≠ α` → `s_k` lineer |
| `κ ≤ 1` | (H2) | `Σ j^{−κ}` **ıraksak** → Lemma A çöker → teorem sessiz kalır |
| `B = 4` zero-critical | *hiçbiri* | `α/κ ≤ log₂3 = α` ⟺ `κ ≥ 1`; (H2) zaten bunu diyor → **yeni kısıt yok, teorem boş**. §9'da doğru belirtilmiş |
| Rastgele bounded zero-critical | (H1) | rastgele yürüyüş → `s_k ~ √k`, `log₂k` değil |
| Sonlu uzun zero-sheet run'ları | *hiçbiri* | teoremle çelişmiyor; §9 doğru |

Yanlış yere düşen bir karşı-örnek bulunamadı. `[VALID]`

## Madde 9 — Literatür

Ayrı yürütüldü: `02-cp20-task6-bagimsiz-dogrulama/LITERATUR_RAPORU.md`.
Wang (Bölüm 4'ün beş kriteri de uygulanmıyor), Dubickas (lineer sınır,
farklı nesne), Chang arXiv:2603.11066 (630 sonuç, faktör karmaşıklığı
kavramı hiç yok), Tao, Siegel, Kramer, Bernstein–Lagarias tarandı.
**Eşdeğer teorem bulunamadı.** Novelty sertifikalı değil ama kalan
boşluklar düşük riskli. `[NO OVERLAP FOUND]`

## Madde 10 — Bağımsız hesaplama

Arşivin engine'lerine bakılmadan yapılanlar:

| Kontrol | Ölçek | Sonuç |
|---|---|---|
| Lemma B bölünebilirlik | 6.363.065 tekrar çifti | 0 ihlal |
| Lemma B örtüşen/ayrık ayrımı | 3.505.204 | 0 ihlal |
| Sturmian `p_g(r) = r+1` | r = 1..20 | tam |
| Controller yeniden kurulum | 100.000 sembol | **SHA eşleşti** |
| Zero-critical üst sınır | 3 kelime × 4 uzunluk | hepsi sağlandı |

`[REPRODUCED]`

---

# Çekirdek test — teoremin içeriği somut mu?

Denetim promptunda yok, kendi eklediğim test. Teorem "sonsuz realizasyon
yok" diyor; ama her **sonlu** prefix 2-adic olarak realize edilebilir.
O halde prefix uzadıkça durumlar Lemma A'nın `O(k^κ)` sınırını aşmalı.

Teklik koşulundan (`n_k` tek ⟺ `3^k n₀ + B_k ≡ 2^{A_k} mod 2^{A_k+1}`)
her `r` için gerçek realizör kuruldu ve ileri koşarak **doğrulandı**:

| r | n₀ basamak | prefix doğru | max `n_k/k^κ` |
|---|---|---|---|
| 5 | 3 | ✓ | 2,74 × 10² |
| 50 | 22 | ✓ | 4,34 × 10²¹ |
| 150 | — | ✓ | — |
| 300 | 141 | ✓ | **1,64 × 10¹⁴¹** |

2-adic tutarlılık doğrulandı (`x_r ≡ x_k mod 2^{A_k+1}`).

`n₀`'ın basamak sayısı `r` ile lineer büyüyor, `max n_k/k^κ` üstel
patlıyor. Lemma A'nın sabiti `n₀`'a bağlıdır ama `r`'ye bağlı **olamaz**
— dolayısıyla hiçbir sabit `n₀` sonsuz prefix'i taşıyamaz. **Teoremin
çelişkisi somut olarak görünür.**

---

# Kırma girişimleri — hepsi başarısız

| Saldırı | Sonuç |
|---|---|
| Örtüşen occurrence'larda Lemma B'yi bozmak | Başarısız (0/439.234) |
| `n_u = n_v` boşluğundan kaçmak | Başarısız (irrasyonellik kapatıyor) |
| Lemma C'nin `O(1)`'ini `u` veya `r`'ye bağımlı göstermek | Başarısız (`r ≤ u` altında uniform) |
| Nicelik sırasını tersine çevirmek | Başarısız (sıra doğru kurulmuş) |
| Çoklu `g`-faktörü ile üst sınırı şişirmek | Başarısız (birleşim küçülür) |
| Hipotezleri sağlayan düşük-karmaşıklıklı dizi bulmak | Başarısız |
| Karşı-örnek listesinden geçen bir örnek bulmak | Başarısız |

---

# Kapsam — teoremin İDDİA ETMEDİĞİ

§9 doğru yazılmış. Kapsam dışı: `B ≥ 4`, kritik siteli kelimeler
(`a_k = g_k`), sınırsız valuationlar, kritik-logaritmik yasayı
sağlamayan yüksek-durum kelimeleri, `κ ≤ 1`.

**Collatz çözülmedi.** Teorem, sonsuz bir sınıflar ailesinden **birini**
kapatıyor.

---

# Denetimin kendi sınırı

Bu denetim de yapay zekâ tarafından yapıldı. Arşivin koduna bakmadan,
farklı bir oturumda, sıfırdan yazılan kodla çalıştım — bu gerçek bir
bağımsızlık derecesi, ama **insan matematikçi bağımsızlığı değil**.

Ortak kör nokta ihtimali duruyor. Özellikle §5'in nicelik yapısı ve
Lemma C'nin uniformluğu, kâğıt üzerinde takip edilen ve sayısal olarak
test **edilemeyen** adımlardır — oradaki bir hata bu yöntemle
yakalanamazdı.

---

# Öneri

1. Madde 7'deki onarımı metne yaz (`−41` sınırının türetimi).
2. Controller word'ünün SHA serileştirmesini belgele (ham byte).
3. Onarım sonrası **dondurulabilir** ve downstream kullanılabilir.
4. CP20 Task 7 açılabilir.
5. Bu teorem, CP17 ile birlikte dış göze gösterilecek paketin parçası olmalı.

## Çalıştırmak için

```bash
python3 madde08_karsi_ornek_disiplini.py           # ~10 sn
python3 cekirdek_sonlu_prefix_realizorleri.py      # ~1 sn
python3 madde01_06_ortusme_ve_ust_sinir.py         # ~21 sn
python3 madde07_controller_yeniden_kurulum.py      # ~61 sn
python3 madde07b_sha_varyant_taramasi.py           # ~87 sn
```
