# Literatürden Bağlantılar — Saldırı Fikirleri

**Tarih:** 2026-08-26
**Amaç:** Novelty savunması değil. Literatürdeki **araçları** arşivin açık
cephesine taşımak.

**Açık cephe (CP20 dondurulduktan sonra):**
1. `κ ≥ 2,784` — yüksek exponent
2. Orta yoğunluklu kritik siteler (`ε ≈ 0,01–0,1`)
3. Kritik-log olmayan discrepancy yasaları
4. **LEVEL-3: ordinary integrality / coherence** ← asıl duvar

---

# ⭐ BAĞLANTI 1 — Hensel basamakları üzerinden LEVEL-3

## Fikrin çekirdeği

Arşiv (CP18 Task 6) şunu kurmuş: bir valuation schedule verildiğinde,
`q_r = −B_r/3^r` dizisi `Z₂`'de **tek** bir 2-adic realizer `x`'e
yakınsıyor.

LEVEL-3 sorusu: bu `x` pozitif **ordinary tam sayı** olabilir mi?

**Kritik gözlem — literatürden değil, tanımdan:**

> Bir pozitif tam sayının 2-adic Hensel açılımı **sonludur**: sonlu
> sayıda sıfır olmayan basamak, sonra sonsuza kadar sıfır.

Dolayısıyla LEVEL-3'ü kapatmak için şu **çok zayıf** ifade yeter:

```
x'in Hensel açılımında sonsuz çok sıfır olmayan basamak vardır.
```

## Neden bu önemli

CP19'un park ettiği high-half mekanizması, **hangi** bitin ne olduğunu
sınıflandırmaya çalışıyordu ve büyüyen hassasiyet gerektirdiği için
duvara çarptı (`CP19 Task 9: "requires growing state; no fixed-width
recurrence"`).

Bu formülasyon **hiçbir biti sınıflandırmıyor.** Sadece "sonsuz çoğu
sıfır değil" diyor. Bu, park edilmiş bariyerin istediğinden mertebe
olarak daha az bilgi.

## Literatürdeki araç

**Bugeaud (p-adic Mahler sınıflandırması):** cebirsel irrasyonel
`ξ ∈ Q_p` için, herhangi `δ < 1/2` ve yeterince büyük `n` için, Hensel
açılımının ilk `n` basamağı arasında **en az `(log n)^{1+δ}` tanesi
sıfır değildir.**

Kanıt aracı: **Schlickewei'nin p-adic Subspace Teoremi**.

Ve genel ilke (Adamczewski–Bugeaud hattı): *cebirsel irrasyonel p-adic
sayıların Hensel açılımı düşük karmaşıklıklı olamaz.*

## Nasıl bağlanır

Arşivin elinde artık **karmaşıklık sınırları var** (Task 6 alt, Task 7
üst). Eksik halka:

```
valuation word karmaşıklığı  ⟶  x'in Hensel açılımı karmaşıklığı
```

Bu transfer kurulabilirse, iki uçtan da saldırılabilir:

- **Üst sınır yolu:** Task 7 basıncı `p_a(r) ≤ 2^{h·r}` veriyor. Eğer
  bu, `x`'in Hensel açılımına düşük karmaşıklık olarak taşınırsa,
  Adamczewski–Bugeaud `x`'in cebirsel irrasyonel olamayacağını söyler.
  `x` rasyonel olmalı → eventually periodic → `A_k/k` rasyonel →
  `α` irrasyonelle çelişki. **Bu, Task 6 Lemma B'nin aynısı ama farklı
  yoldan** — yani tutarlılık kontrolü olarak da değerli.
- **Basamak yoğunluğu yolu:** doğrudan "sonsuz çok sıfır olmayan
  basamak" gösterilirse, `x` tam sayı olamaz. Cebirsellik gerekmez.

## Sayısal destek

`hensel_basamak_deneyi.py` — controller'ın kısmi realizörleri
`x_r = n₀ mod 2^{A_r+1}`:

| r | bit sayısı | `1` biti | yoğunluk | son `1` bitinin yeri |
|---|---|---|---|---|
| 100 | 153 | 91 | 0,5948 | 152 |
| 400 | 626 | 324 | 0,5176 | 624 |
| 800 | 1258 | 627 | 0,4984 | 1257 |
| 1200 | 1892 | 921 | 0,4868 | 1890 |

2-adic yakınsama doğrulandı: `r` büyüdükçe düşük bitler **sabitleniyor**
(her adımda önceki `A_r+1` bit aynı kalıyor).

`1` biti yoğunluğu **~0,49'da duruyor** ve en yüksek `1` biti hep en üst
sırada. Tam sayı olsaydı bir yerden sonra tüm bitler sıfır olurdu.

> Bu bir ispat değil — sonlu kesit. Ama aranan ifadenin doğru yönde
> olduğunun göstergesi.

## Önerilen Task

**"Hensel basamak yoğunluğu ve ordinary integrality"**
Sorular: (i) `q_r = −B_r/3^r` dizisinin bit yapısı, valuation word'den
nasıl okunur? (ii) `A(W)` ve `B_W` cebirinden basamak yoğunluğu için
bir alt sınır çıkar mı? (iii) Schlickewei/Subspace teoremi bu duruma
doğrudan uygulanabilir mi, yoksa cebirsellik varsayımı engel mi?

---

# BAĞLANTI 2 — Otomatik diziler ve transandantallık

**Kaynak:** Capuano, Checcoli, Mula, Terracini, *If a machine did it, it
is probably transcendental (even p-adically)*, arXiv:2503.16330 (2025).

**Sonuç:** otomatik p-adic sayılar **transandantaldır**.

**Bağlantı:** eğer bir valuation word sonlu otomatla üretilebiliyorsa,
karşılık gelen realizer transandantal olur → tam sayı olamaz → o sınıf
LEVEL-3'te kapanır.

**Uyarı:** CP20 controller'ı bang-bang kuralla üretiliyor ama eşiği
`κ log₂ k` içeriyor — logaritmik eşik otomatik değildir. Yani controller
muhtemelen bu sınıfın dışında.

**Ama:** arşivin kapattığı/kapatmadığı diğer sınıflarda **morfik** veya
**otomatik** kelimeler olabilir. Bunlar bu araçla **tek hamlede**
kapanır. Ucuz bir tarama.

---

# BAĞLANTI 3 — Bir simetri: tekrarlar

**Adamczewski–Bugeaud kombinatoryal kriteri:** bir kelimede *yeterince
erken ve yeterince uzun tekrarlar* varsa (ω-power prefiksler), Subspace
Teoremi uygulanır ve sayı transandantal çıkar.

**Arşivin Task 6 Lemma B'si:** aynı faktör iki kez geçerse,
`2^{A(W)} | (n_v − n_u)` — yani tekrar, ordinary durumlar arasında
**devasa bir ayrışma** zorlar.

Bunlar **aynı madalyonun iki yüzü**:

| | Adamczewski–Bugeaud | Task 6 |
|---|---|---|
| Tekrar varsa | → transandantal | → üstel ayrışma |
| Kullanım | tekrarı **kullanır** | tekrarı **dışlar** |

Bu simetri şunu düşündürüyor: iki argüman birleştirilebilir. Tekrar olan
durumda A–B, olmayan durumda Task 6 çalışır — ve **her kelime ya
tekrarlıdır ya değildir**. Bir dikotomi kurulabilir.

**Önerilen Task:** *"Tekrar dikotomisi"* — tekrarlı kelimeler için
Subspace, tekrarsızlar için faktör-karmaşıklığı; ikisinin birleşimi tüm
sınıfı kapsıyor mu?

---

# BAĞLANTI 4 — Geometrik entropi köprüsü

Üç ayrı yerde **aynı geometrik yapı**:

- CP19 T4'ün `h(α) = 1,5056…` — sınırsız alfabede ortalama-kısıtlı
  **geometrik** maksimum entropi
- Tao'nun Syracuse rastgele değişkeni — **geometrik** dağılım
  (Shannon entropisi `log 4`)
- CP17'nin rate fonksiyonu — freeze notunda `η(μ) = I_CP17(μ)/ln 2`
  özdeşliği **zaten kayıtlı**

Arşiv Tao'yu "almost all sonucu, deterministik dizi dışlamaz" diye
reddetmişti. Doğru bir ret — ama **yöntemini** değil, sonucunu reddetti.

Tao'nun 3-adic Fourier makinesi bir *dağılım* aracı. Arşivin ihtiyacı
olan şey tek bir deterministik dizi. Ama ikisi aynı geometrik ölçüde
buluşuyorsa, Tao'nun tekniklerinden hangilerinin deterministik versiyonu
olduğu ayrı bir sorudur.

**Önerilen Task:** *"CP17 rate fonksiyonu ile Syracuse rastgele
değişkeni arasındaki özdeşliğin kapsamı"* — bu bir tesadüf mü, yoksa
CP17 zaten Tao'nun ölçüsünün deterministik bir kesiti mi?

---

# BAĞLANTI 5 — Sturmian serilerin transandantallığı

**Kaynak:** Florian Luca, *On the transcendence of a series related to
Sturmian words*.

Arşivin `g_k` kelimesi Sturmian. Sturmian yapıdan üretilen serilerin
transandantallığı üzerine literatür var ve doğrudan
`Σ 2^{D_k}` / `X_N` tipi nesnelere benziyor (CP17'nin carry serisi!).

CP17 zaten `X_N = Σ_{k<N} 2^{D_k}` ve `U_N = 1 + X_N/(3n₀)` kuruyor.
`D_k = −s_k − {αk}` içinde `{αk}` Sturmian yapının ta kendisi.

**Önerilen Task:** `X_∞ = Σ 2^{D_k}` transandantal mı? Eğer öyleyse ve
ordinary realization `X_∞`'un cebirsel olmasını gerektiriyorsa, çelişki.

---

# Öncelik önerisi

| # | Bağlantı | Neden | Maliyet |
|---|---|---|---|
| 1 | **Hensel basamak yoğunluğu** | LEVEL-3'e doğrudan, park edilmiş bariyerden daha az istiyor | Orta |
| 2 | Tekrar dikotomisi | Task 6 zaten yarısını yapmış | Düşük |
| 3 | Otomatik dizi taraması | Ucuz, bazı sınıfları tek hamlede kapatabilir | Çok düşük |
| 4 | Geometrik entropi köprüsü | Yapısal anlayış, doğrudan sonuç değil | Orta |
| 5 | `X_∞` transandantallığı | CP17 nesnesi hazır | Orta |

**Bence 3 → 2 → 1 sırası.** Üçüncüsü bir günlük iş ve bazı açık
sınıfları eleyebilir; ikincisi arşivin elindeki lemmayı ikiye katlar;
birincisi asıl duvara saldırı.

---

# Dürüstlük kaydı

Bunların hiçbiri teorem değil. Beşi de "bu araç buraya taşınabilir mi?"
sorusudur, ve taşınabilirliğin kendisi ispatlanmadı. Özellikle
Bağlantı 1'in eksik halkası (valuation word karmaşıklığı → Hensel
karmaşıklığı transferi) hiç önemsiz değil; oradaki bir kopukluk bütün
fikri boşa çıkarır.

Sayısal destek yalnızca Bağlantı 1 için var ve sonlu kesittir.

## Kaynaklar

- [Capuano, Checcoli, Mula, Terracini — If a machine did it, it is probably transcendental (even p-adically), arXiv:2503.16330](https://arxiv.org/abs/2503.16330)
- [Adamczewski & Bugeaud — On the complexity of algebraic numbers I](https://adamczewski.perso.math.cnrs.fr/ComplexityI.pdf)
- [Bugeaud & Kekeç — On Mahler's classification of p-adic numbers](https://irma.math.unistra.fr/~bugeaud/travaux/BuKe1.pdf)
- [Bilu — The many faces of the Subspace Theorem, arXiv:0907.2098](https://arxiv.org/abs/0907.2098)
- [Tao — Almost all orbits of the Collatz map, arXiv:1909.03562](https://arxiv.org/abs/1909.03562)
