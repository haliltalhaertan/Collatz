# CP20 Task 6 — Bağımsız Literatür Kontrolü

**Tarih:** 2026-08-26
**Kapsam:** Audit prompt madde 9 (literatür örtüşmesi / novelty).
**Yöntem:** Arşivin kendi `LITERATURE_HYPOTHESIS_MAP` dosyasına *güvenilmedi*;
kaynak makaleler doğrudan indirilip ilgili teoremler tam metinden okundu ve
hipotezleri controller üzerinde sayısal olarak test edildi.

## Özet verdict

`[TASK 6 TEOREMİ İNCELENEN KAYNAKLARIN HİÇBİRİ TARAFINDAN KAPSANMIYOR]`
`[EN YÜKSEK RİSKLİ KAYNAK (arXiv:2603.11066) TARANDI — KAPSAMIYOR, bkz. §6]`
`[NOVELTY YİNE DE SERTİFİKALI DEĞİL — kalan boşluklar §7'de]`

## 1. SanMin Wang — E-sequence yaklaşımı

**Kaynak:** SanMin Wang, *An E-sequence approach to the 3x+1 problem*,
arXiv:1809.02278v4 (13 Ekim 2019); Symmetry 11 (2019) 1415.
Tam metin indirildi ve Bölüm 4 okundu.

Wang'ın notasyonu ile arşivin notasyonu eşleşmesi:
`b_n = A_k` (valuation toplamı), `x_n = n_k` (durum), `B_n = B_k`.

Wang'ın Bölüm 4'teki her Ω-ıraksaklık kriterini controller üzerinde test ettim:

| Wang sonucu | Hipotezi | Controller'daki durum | Uygulanabilir? |
|---|---|---|---|
| **Teorem 4.2** | `lim b_n/n > log₂3` | `lim = log₂3`, **aşağıdan** (ölçüldü: 1,584900 vs α=1,584963) | **Hayır** |
| **Corollary 4.7** | mekanik kelime, `θ ≥ log₂3` | controller mekanik değil (geri beslemeli) | **Hayır** |
| **Teorem 4.11** | `c>log₂3` ile sonsuz çoklukta `l>kc` uzunluğunda **1-run** | ölçülen **en uzun 1-run = 2** (300.000 sembolde) | **Hayır** |
| **Teorem 4.13** | `c>log₂3` ile sonsuz çoklukta **ilk önek tekrarı**, `b_{l+r}>lc` | aşağıda ayrıntılı — **sağlanmıyor** | **Hayır** |
| **Teorem 4.14** | mekanik kelime, `θ < log₂3` | controller mekanik değil | **Hayır** |

### Teorem 4.13 ayrıntılı testi

Audit prompt bu teoremi özellikle işaret ediyordu. Tam ifadesi (s.12):

> `(a_n)` E-sequence olsun, öyle ki (i) her `n` için `3ⁿ > 2^{b_n}`;
> (ii) bir `c > log₂3` sabiti var ve sonsuz çoklukta `(r,l)` çifti için
> `l > r`, `b_{l+r} > lc`, ve `a_{l+k} = a_k` (`1 ⩽ k ⩽ r`).
> O zaman `Ω−lim a_n = ∞`.

Hipotez (ii) **ilk öneğin** tekrarını istiyor. Controller'da ölçüm:

| önek uzunluğu r | tekrar eden l sayısı (300.000 sembolde) |
|---|---|
| 1–10 | 11.274 – 124.510 |
| 12, 15 | **4** |
| 20, 30, 50 | **0** |

Kritik nokta: `b_{l+r}/l ≈ α(1+r/l)`. Sabit bir `c > α` için **sonsuz çoklukta**
çift gerekiyor, yani `l → ∞`. Ama `l → ∞` iken `c → α` — meğerki `r`, `l` ile
**orantılı** büyüsün. Bunu doğrudan taradım:

| r ≈ β·l | denenen l | bulunan önek tekrarı |
|---|---|---|
| β = 0,10 | 39.900 | 1 |
| β = 0,25 | 39.900 | **0** |
| β = 0,50 | 39.900 | **0** |
| β = 1,00 | 39.900 | **0** |

Orantılı uzunlukta önek tekrarı yok. **Wang Teorem 4.13 uygulanamıyor.**

*Not:* Hipotez (i) de tam sağlanmıyor — `n = 1, 3, 5`'te ihlal var (başlangıç
etkisi, kaydırma ile giderilebilir). Ama asıl engel (ii).

### Wang'ın kendi açık problem beyanı

Makalenin sonuç bölümünde (s.14) Wang aynen şunu yazıyor:

> *"Another interesting problem is whether `(a_n)` with infinitely many `n`
> satisfying `b_n > n log₂3` is Ω−divergent. By virtue of Theorem 4.2, we only
> need to consider the case of `lim b_n/n = log₂3`. Theorem 4.6 answers the
> problem if [...] → ∞. **Currently, we don't know how to tackle with the other
> cases of the problem.**"*

CP20 controller **tam olarak** `lim b_n/n = log₂3` rejiminde. Yani makalenin
yazarı, Task 6'nın saldırdığı bölgenin kendi yöntemleriyle açık olduğunu
açıkça yazıyor. Bu novelty için **destekleyici** ama kanıt değil.

## 2. Dubickas — kelime karmaşıklığı alt sınırı

Bu, arşivin literatür haritasında **hiç geçmiyordu** ve gerçek bir risk adayıydı,
çünkü konusu doğrudan "Collatz kelimelerinin karmaşıklığı için alt sınır".

**Kaynak:** Dubickas [Dub09, Theorem 3], Andrieu–Eliahou–Vivion,
*A Normality Conjecture on Rational Base Number Systems*, arXiv:2510.11723
üzerinden doğrulandı (s.2, denklem 1.3).

Dubickas'ın sonucu, `p/q` rasyonel tabanındaki **minimal kelimeler** için:

```
liminf_{l→∞}  p_w(l) / l  ≥  log q / log(p/q)
```

**Neden Task 6'yı kapsamıyor — iki bağımsız sebep:**

1. **Mertebe farkı.** Dubickas'ınki **lineer** bir alt sınır (`p_w(l) ≳ c·l`).
   Task 6'nınki **üstel**: `liminf log₂p_a(r)/r ≥ α/κ ≈ 1,505`, yani
   `p_a(r) ≳ 2^{1,5r}`. Bunlar aynı büyüklük mertebesinde bile değil.
2. **Nesne farkı.** Dubickas rasyonel taban minimal kelimeleri / parite
   (mod 2) Collatz kelimeleri ile ilgileniyor. Task 6'nınki **valuation
   kelimesi** (`a_k ∈ {1,2,3}`), farklı bir kodlama.

## 3. Diğer kontrol edilen kaynaklar

| Kaynak | Neden kapsamıyor |
|---|---|
| Tao, arXiv:1909.03562 | "almost all" / logaritmik yoğunluk sonucu; tek bir **belirlenmiş deterministik** diziyi dışlamaz |
| Bernstein–Lagarias (1996) | 2-adic eşlenik zemin çalışması; Task 6 eşlenik haritayı kullanmıyor |
| Siegel, arXiv:2007.15936 | numen çerçevesi, periyodik noktalar; kritik-logaritmik deterministik diziyi çözmüyor |
| Kramer, arXiv:2607.10041 (2026) | **sonlu** exponent-code tanılaması; sonsuz faktör karmaşıklığı alt sınırı vermiyor |
| Sturmian `p_g(r)=r+1` | standart kelime kombinatoriği; Task 6'da **bilinerek** ve doğru şekilde kullanılıyor, iddia edilen yenilik bu değil |

## 4. Arşivin kendi literatür haritasının değerlendirmesi

`CP20_TASK6_LITERATURE_HYPOTHESIS_MAP.md` dosyası doğru ve dürüst:
Wang, Bernstein–Lagarias, Tao, Siegel, Kramer'i kapsıyor ve kendi ifadesiyle
*"this is not a formal novelty certification"* diyor.

**Eksiği:** kelime kombinatoriği tarafındaki karmaşıklık literatürü —
özellikle Dubickas — hiç yoktu. Bu boşluk şimdi kapatıldı (§2) ve sonuç
lehte çıktı, ama boşluğun varlığı, haritanın taramasının **konu bazlı değil
Collatz bazlı** yapıldığını gösteriyor. Karşılaştırılabilir bir risk başka
bir alt alanda hâlâ olabilir.

## 5. Task 6'nın gerçekte yeni olan kısmı

İncelenen literatüre göre yeni olan, tek tek bileşenler değil — bunların
birleşimi:

- Tekrarlanan faktör → `2^{A(W)} | (n_v − n_u)` bölünebilirliği **tek başına
  yeni değil** (Wang 4.13 aynı cebiri önek için kullanıyor).
- Sturmian `p_g(r) = r+1` **standart**.
- **Yeni olan:** bu ikisinin `n_k = O(k^κ)` polinom durum sınırıyla
  birleştirilip *keyfi konumlardaki* faktörlere uygulanması ve buradan
  bir **üstel faktör-karmaşıklığı alt sınırı** çıkarılması; ardından bunun
  zero-critical dilin üst sınırıyla çelişkiye sokulması.

Wang önek kullanıyor ve ek eşitsizlikler gerektiriyor; Task 6 keyfi faktör
kullanıyor ve ek eşitsizlik gerektirmiyor. Bu gerçek bir genelleme.

## 6. En yüksek riskli kaynak — tarandı, kapsamıyor

**arXiv:2603.11066v6** — Edward Y. Chang (Stanford CS / QuadriumAI),
*Exploring Collatz Dynamics with Human–LLM Collaboration*, Şubat–Nisan 2026.
630 formal sonuç, ~10¹⁴ hesaplama, 29 paradigma. Tam metin indirildi
(13.927 satır) ve tarandı.

Bu kaynak, Task 6 ile aynı alanda, çok daha geniş kapsamlı ve **benzer
metodolojiyle** (insan–LLM işbirliği) üretildiği için en yüksek riskli
adaydı. Sonuç: **kapsamıyor.**

### Anahtar kavram taraması (tam metin)

| Task 6'nın merkezi kavramı | Chang'da geçiş sayısı |
|---|---|
| `factor complexity` | **0** |
| `subword` | **0** |
| `word complexity` | **0** |
| `repeated factor` / `repeated prefix` | **0** |
| `return word` | **0** |
| `same word occurs` / `occurs twice` | **0** |
| `logarithmic discrepancy` | **0** |
| `kappa` (κ log₂k hipotezi) | **0** |
| `polynomially bounded` / `polynomial growth` / `O(k^…)` | **0** |

Task 6'nın **hem mekanizması hem merkezi hipotezi** metinde hiç geçmiyor.

### Yakın görünen ama farklı çıkan üç nokta

**(a) "Sturmian" — 49 geçiş, farklı rol.**
Chang'ın *Sturmian-compatible* tanımı `v_d ∈ {1,2}`, yani bir **alfabe
kısıtı** (B=2). Bunu Carry Contamination Teoremi'nde (Thm 10.4) 2-adic
carry argümanı için kullanıyor. Task 6'da Sturmian, Beatty kelimesi
`g_k`'nın `p_g(r) = r+1` **faktör sayımı** için kullanılıyor. Aynı kelime,
tamamen farklı iş. Ayrıca Chang B=2 ile, Task 6 B=3 **ve** `a_k ≠ g_k`
kısıtıyla çalışıyor — farklı sınıflar.

**(b) Corollary 10.5 — `|C_D| = 2·3^{D−1}` sayımı.**
Bu bir üstel sayım ve ilk bakışta karmaşıklık sınırına benziyor. Ama
saydığı şey **dil/silindir düzeyinde uyumlu kelimelerin toplam sayısı**
(tüm başlangıç değerleri üzerinden). Task 6 ise **tek bir sonsuz
yörüngenin** valuation kelimesinin faktör karmaşıklığını alttan
sınırlıyor. Bunlar farklı nicelikler: biri dilin büyüklüğü, diğeri tek
bir kelimenin iç çeşitliliği.

**(c) "discrepancy" — 35 geçiş, isim çakışması.**
Chang'da `δ_K(n₀)` = residue dağılımının düzgünlükten **toplam varyasyon
sapması**. Task 6'da discrepancy = `s_k = ⌊αk⌋ − A_k`, yani valuation
toplamının `αk`'dan **aritmetik sapması**. Alakasız iki kavram.

### Chang'da Task 6'yı destekleyen bir yan bulgu

**Result 300:** *"divergent orbits require `q_L ∼ m·2^{(α−β)L}`; all tested
orbits have `S_L/L → α` rather than `β < α`."*

Bu, CP20 controller'ının bulunduğu rejimin (`A_k/k → α`, aşağıdan)
ampirik olarak gerçekten kritik rejim olduğunu destekliyor. Chang bunu
teorem olarak değil gözlem olarak veriyor.

### Chang'ın kendi formal dil sonucu farklı düzeyde

**Result 299:** `L_div` bağlamdan bağımsız (context-free) **değildir**.
Bu bir **dil sınıfı** sonucu (pumping lemma ile). Task 6'nınki ise
**nicel bir entropi alt sınırı** (`liminf log₂p_a(r)/r ≥ α/κ`). Dil
sınıfı ifadeleri nicel karmaşıklık sınırı vermez; farklı düzeyler.

## 7. Sonuç ve kalan boşluklar

Novelty **çürütülmedi**. Destekleyici kanıt güçlendi:

1. Wang'ın Bölüm 4'teki beş kriterinin hiçbiri controller'a uygulanmıyor
   (hipotezleri sayısal olarak test edildi).
2. Wang'ın kendisi `lim bₙ/n = log₂3` rejimini açık ilan ediyor —
   controller tam bu rejimde.
3. Dubickas'ın alt sınırı farklı mertebede (lineer) ve farklı nesne için.
4. Chang'ın 630 sonucu içinde faktör karmaşıklığı kavramı hiç geçmiyor.

**Yine de sertifikalanmadı.** Taranmayanlar:

- Eliahou–Verger-Gaugry'nin Collatz kelimeleri üzerine çalışmaları
- Return-word ve rekürans literatürü (kelime kombinatoriği tarafı)
- 2019–2026 arası Collatz sembolik dinamik makalelerinin tam taraması
- Dubickas'ın orijinal 2009 makalesi (yalnızca ikincil kaynaktan okundu)

Bu boşluklar artık **düşük riskli**: taranan üç ana kaynak da aynı sebeple
kapsamıyor — faktör karmaşıklığı üzerinden bir alt sınır kurma fikri
literatürde bu bağlamda görünmüyor.

**Tavsiye:** novelty artık denetimi bloke edecek kadar riskli değil.
Denetim önceliği literatürden zemine (CP17) kaymalıdır.

## Kaynaklar

- [Wang, An E-sequence approach to the 3x+1 problem (arXiv:1809.02278)](https://arxiv.org/pdf/1809.02278)
- [Andrieu–Eliahou–Vivion, A Normality Conjecture on Rational Base Number Systems (arXiv:2510.11723)](https://arxiv.org/pdf/2510.11723)
- [Tao, Almost all orbits of the Collatz map attain almost bounded values (arXiv:1909.03562)](https://arxiv.org/pdf/1909.03562)
- [Chang, Exploring Collatz Dynamics with Human–LLM Collaboration (arXiv:2603.11066)](https://arxiv.org/abs/2603.11066)
- [Kramer, Adaptive Search in Collatz Exponent-Code Space (arXiv:2607.10041)](https://arxiv.org/html/2607.10041v1)
