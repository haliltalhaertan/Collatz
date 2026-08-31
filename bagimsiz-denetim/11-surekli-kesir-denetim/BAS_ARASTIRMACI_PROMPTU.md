# Baş araştırmacıya gönderilecek — tek parça

Aşağıdaki bloğu olduğu gibi kopyalayabilirsiniz.

---

````markdown
# Yeni bulgu adayı: Konverjant-tetiklemeli etkin n₀ sınırı

**Durum:** `[VALID AS OBSERVATION — ONE LOAD-BEARING LEMMA MISSING]`
Kendi denetimimden geçti, bağımsız denetimden geçmedi. Drive'da karşılığı yok.

## Kısaca

`α = log₂3`'ün sürekli kesirindeki büyük kısmi bölümler, kritik-log
kontrollü zero-critical kelimelerde **uzun faktör tekrarları** üretiyor.
Task 6 Lemma B buraya uygulanınca `n₀` üzerinde **etkin alt sınır**
çıkıyor.

```
α = [1; 1,1,2,2,3,1,5,2,23,2,2,1,1,55,…]
```

## Ölçüm

Her konverjant `q_n` için, controller kelimesinde `q_n`-kaydırma altında
en uzun ortak blok:

| `q_n` | `u` | `r` | `A(W)` | **`log₂n₀ ≥`** |
|---|---|---|---|---|
| 665 | 730 | 671 | 1.062 | 1.050 |
| 15.601 | 124.297 | 15.605 | 24.732 | 24.714 |
| 31.867 | 40.572 | 31.871 | 50.513 | 50.495 |
| 79.335 | 190.874 | 79.339 | 125.748 | **125.729** |

Test edilen 10 konverjantın **hepsinde** uzun blok var; `r/q` oranı
büyük `q` için tam **1,000**.

## Ortaya çıkan yasa

```
log₂ n₀  ≳  α · q_n
```

Oran ölçüldü: 1,5789 → 1,5841 → 1,5846 → **1,5848**  (α = 1,5850).

`α` irrasyonel → sonsuz konverjant → sınır **sınırsız**. Sabit bir `n₀`
hepsini karşılayamaz.

## Neden Task 6'dan fazla

| Task 6 | Bu |
|---|---|
| tekrarların olmaması gerektiğini kanıtlıyor | tekrarların **nerede** olduğunu söylüyor |
| asimptotik (`yeterince büyük r`) | **etkin**, `q_n`'de somut sayı |
| `u ~ 2^{1,5r}` rejimi | `u ~ r` rejimi — **farklı ölçek** |

## Kırma girişimleri (hepsi başarısız)

- **`κ`'ya bağlı mı?** Hayır. `κ = 1,053 / 1,2 / 1,5 / 2,0` — hepsinde
  aynı blok uzunlukları (671, 15.605/15.607).
- **Tesadüf mü?** Hayır. Rastgele zero-critical kelimede blok yalnızca
  **20**, controller'da **15.605**.
- **Lemma C'ye bağımlı mı?** (bazı bloklarda `r > u`) Hayır — argüman
  yalnızca Lemma B (tekrar) + Lemma A (`n_k ≤ C(n₀)k^κ`) kullanıyor,
  `A(W)` doğrudan toplanıyor.
- **`n_u = n_v` boşluğu?** Yok — periyodiklik → `A_k/k` rasyonel,
  kritik-log yasası irrasyonel veriyor.

## ⛔ EKSİK LEMMA (teorem olmasının önündeki tek engel)

> **(L)** Her konverjant `q_n` için, kritik-log kontrollü zero-critical
> bir kelimede uzunluğu `≥ c·q_n` (`c>0` sabit) olan bir `q_n`-tekrar
> bloğu vardır.

10 konverjantta gözlendi (`c ≈ 1`), **ispatlanmadı**.

Malzeme mevcut görünüyor:
1. `g` Sturmian → kısmi bölüm `a_{n+1}`, `q_n` periyodunun `a_{n+1}` kez
   tekrarı (klasik)
2. `a_k = g_k − d_k`, `d_k ∈ {+1,−1}` (kritik-log kontrolü altında)
3. `s_k` logaritmik → `d` örüntüsü uzun aralıklarda `g`'ye kilitleniyor

**Hassas adım (3):** `d_k`'nın tekrar örüntüsünü `s_k`'nın logaritmik
yavaşlığından türetmek. Yapılmadı.

## Diğer açık noktalar

- Küçük `q` (5, 12, 41, 53): Lemma A'nın asimptotik rejimi şüpheli;
  o satırlar gösterge, kanıt değil
- `C(n₀)` sabiti tam izlenmedi (`n_k ≤ 2^{C+1}(n₀+c)k^κ`); mertebeyi
  değil, kesin sabiti etkiler
- `q = 111.202`'de `r/q = 0,314` — `N = 400.000` penceresi yetersiz
  olabilir, daha uzun tarama gerekli

## Senin listenle bağlantısı

4. maddene (**Crandall/Steiner/Simons–de Weger, `log₂3` continued
fractions + linear forms in logarithms, yüksek-κ**) doğrudan oturuyor.
Sen "Task 6'nın repeated-factor spacing theorem'i yeterince iyi
near-return durumları üretirse Baker/Rhin tipi saldırı mümkün olabilir"
demiştin — **bu bulgu tam olarak o near-return durumlarını üretiyor ve
nerede olduklarını söylüyor.**

Ve yüksek-κ rejimi (`κ ≥ 2,784`) frontier'ın açık kalan asıl parçası.

## Önerim

Eksik lemma (L) küçük ve kendi başına bir Task'a değmeyebilir. İki
seçenek:

- **A)** Task 8B2'ye (return word / 2-adic rate stabilization) ek modül
  olarak iliştir — return word yapısı zaten aynı kombinatoriği kullanıyor
- **B)** Ayrı kısa bir Task 8C: "konverjant-tetiklemeli etkin sınırlar",
  tek hedefi (L)'yi ispatlamak ve etkin sabiti izlemek

Bence **A**, çünkü B2 zaten o kombinatorik alanda çalışıyor.

## Dürüstlük kaydı

Bu denetimi bulgunun sahibi yaptı. Bugün Drive'daki bağımsız denetim
beni üç ayrı yerde düzeltti (Chernoff işareti, "Sturmian faz maliyeti"
artefaktı, CP19 T5 survivor'ı hakkındaki yanlış sonucum). Burada da
aynısının olması muhtemel — özellikle (L)'nin "ispatlanabilir görünmesi"
benim değerlendirmem.

Kod ve tam denetim raporu:
https://github.com/haliltalhaertan/math → `11-surekli-kesir-denetim/`
````
