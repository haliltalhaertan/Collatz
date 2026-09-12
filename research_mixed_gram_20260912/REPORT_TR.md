# Mixed-Gram Round 1 — kapalı overlap hiyerarşisi ve faz-kör gevşetmenin sınırı

Tarih: 12 Eylül 2026  
Kaynak commit: `434d8fc55544207b35a4c4390600598dd6623d28`  
Durum: **yerel/analitik ilerleme + tam sonlu doğrulama; uniform W/D2 ve Collatz açık.**

## Basit özet

Bu turda önceki çapraz-terim sonucunu bir “operatör yinelemesi” biçimine çevirdim.
Amaç yalnız `M4` taşımak yerine komşu filtrelerin Fourier güçlerinin ne kadar
örtüştüğünü de taşımaktı.

İki şey çıktı.

1. **Gerçek bir Gram/overlap hiyerarşisi kurulabiliyor.**  
   `G_d`, aralarında `d` kadar tail-ağırlık kayması olan iki kanalın Fourier güç
   örtüşmesini ölçsün. `G_0=M4`. Bir ölçek yukarı çıkarken `G_d`, yalnız
   `G_{d-1},G_d,G_{d+1}` komşularına bağlanan kapalı bir üst-yineleme sağlıyor.
   Yani “mixed bilgiyi koruyan ama boyutu her adımda patlayan” bir durum yerine,
   fazı attığımızda mesafe ekseninde lineer genişleyen bir hiyerarşi elde ediyoruz.

2. **Bu faz-kör hiyerarşi şimdilik yeterli değil.**  
   Kritik küçük gridde 612 tam durumda yeni hiyerarşi üst sınırı, zaten bilinen
   `M4 <= M2^2/2` sınırını tek bir kez bile sıkı biçimde yenemedi; 6 durumda eşit,
   geri kalanlarda daha kötüydü. Eski scalar iterasyondan 101 durumda daha iyi
   olsa da asıl karşılaştırılması gereken bilinen trivial sınırı geçemedi.

Ayrıca “yansıma-kötü bileşeni iki ardışık ölçekte birden tam doygun olamaz”
fikri gerçek filtrede **yanlış** çıktı: `(t,j,s)=(11,6,4)` ve onun
`(10,6,3)` çocuğunda aynı anda `N_-=0`, `N_B>0`.

Bu nedenle sonraki ciddi aday, fazı mutlak değerle atmayan ve source/W_flat
ağırlıklarını daha baştan içine alan **faz-duyarlı blok Gram operatörü** olmalı.

---

## Bu turda okunan kaynaklar

Doğrudan okundu ve bu raporun temeli olarak kullanıldı:

- `START_HERE_CURRENT_HANDOFF.md`
- `research_visible_defect_20260908/kernel.md`
- `research_visible_defect_20260908/attack.md`
- `research_cross_terms_20260912/REPORT_TR.md`
- `research_cross_terms_20260912/IDENTITIES.md`
- `research_cross_terms_20260912/ATTACK.md`
- `research_cross_terms_20260912/INDEPENDENT.md`
- `research_shift_recurrence_20260912/RECURRENCE.md`
- `research_shift_recurrence_20260912/ALGORITHM.md`
- `research_w_continuation_20260912/PROPOSAL.md`
- `research_peak_peeling_20260912/ANALYTIC_REVIEW.md`

`research_concentration_audit_20260912` ve `research_galois_audit_20260912`
bu turda yeniden okunmadı; mevcut devir notundaki “uniform strict gap/Galois
tek başına yetmiyor” hükümleri yukarıdaki son cross-term raporundan devralındı.

Drive depo paketi `COLLATZ_CROSS_REPOSITORY_20260912.zip` indirildi.
Boyut ve SHA-256 yerel olarak yeniden doğrulandı:

- bytes: `32924513`
- SHA-256: `000519a99d0c04009f6cbbb50053630f37f4394f905a357e83e6d9f817da5840`

---

# 1. [KANIT] İki-lift Fourier formu

Parent derinliği `s>=2` olsun. Alt modül

`q = 2^(s-1)`

ve `r = 3^(-1) mod q` olsun. Alt seviyede

`phi_j(a) = Fourier(F_(s-1;t-1,j))(a)`.

Parent modülündeki bir tek frekansın iki lift'i `xi=a` ve `xi=a+q` olarak
eşlenir. Parite split'ini doğrudan `x=2u+e` ile açınca

`Phi_j(xi) = phi_j(a) + sigma * eta_a * phi_(j-1)(r a)`

elde edilir; burada `sigma=+1/-1` iki lift'i ayırır ve `|eta_a|=1`.
Ayrıca

`eta_a^2 = exp(2 pi i r a / q)`.

Bunun kritik özelliği, iki liftte mixed lineer terimin işaret değiştirmesidir.

Dördüncü kuvvetleri iki lift üzerinde toplarsak

`|A+zB|^4 + |A-zB|^4
 = 2|A|^4 + 2|B|^4 + 8|A|^2|B|^2
   + 4 Re(z^2 B^2 conjugate(A)^2)`.

Dolayısıyla aşağıdaki tanımlarla:

`G_0(t,j,s) = sum_(a odd mod 2^s) |phi_j(a)|^4 = M4(t,j,s)`

`G_1(t,j,s) = sum_(a odd) |phi_j(a)|^2 |phi_(j-1)(3^-1 a)|^2`

ve phase coherence `C_1` ile

`G_0(t,j,s)
 = 2 G_0(t-1,j,s-1)
 + 2 G_0(t-1,j-1,s-1)
 + 8 G_1(t-1,j,s-1)
 + 4 C_1(t-1,j,s-1)`.

Bu, önceki

`S=N0+N1+6N_+ +2N_-`

özdeşliğinin Fourier-lift/operatör biçimidir. Ölçekler bire bir uyuşur:

`G_1 = 2^(s-2) N_B`,  
`C_1 = 2^(s-2) O`.

Bu turda yeni olan, formun `G_d` hiyerarşisine genişletilmesidir.

---

# 2. [KANIT] Mesafe-d mixed overlap hiyerarşisi

`d>=0` için

`G_d(t,j,s)
 = sum_(a odd mod 2^s)
     |phi_j(a)|^2
     |phi_(j-d)(3^(-d) a)|^2`

tanımlansın. Destek dışı `j-d` kanalı sıfırdır. `G_0=M4`.

`d>=1` iken bir üst ölçeğin aynı iki-lift ayrıştırmasında, sabit alt frekansta
dört kompleks sayı ortaya çıkar:

`A = phi_j(a)`,
`B = phi_(j-1)(r a)`,
`C = phi_(j-d)(r^d a)`,
`D = phi_(j-d-1)(r^(d+1) a)`.

İki liftte güç çarpımı

`sum_(sigma=+-1) |A+sigma u B|^2 |C+sigma v D|^2`

olur (`|u|=|v|=1`). Açılım:

`2(|A|^2+|B|^2)(|C|^2+|D|^2)
 + 8 Re(u B conjugate(A)) Re(v D conjugate(C))`.

Son terimde

`8 |A B C D|
 <= 4(|A C|^2 + |B D|^2)`

uygulanır. Frekans üzerinde toplayıp `a -> 3^-1 a` yeniden indekslemesi
yapınca kapalı hiyerarşi elde edilir:

**d>=1 için**

`G_d(t,j,s) <=
   6 G_d(t-1,j,s-1)
 + 6 G_d(t-1,j-1,s-1)
 + 2 G_(d+1)(t-1,j,s-1)
 + 2 G_(d-1)(t-1,j-1,s-1).`

`d=0` için önceki kesin formdan `|C_1|<=G_1` kullanırsak

`G_0(t,j,s) <=
   2 G_0(t-1,j,s-1)
 + 2 G_0(t-1,j-1,s-1)
 +12 G_1(t-1,j,s-1).`

Taban `s=1`'de tek primitive frekans vardır. Eğer

`delta_l = binom(t-1,l)-binom(t-1,l-1)`

ise tam olarak

`G_d(t,j,1)=delta_j^2 delta_(j-d)^2`.

Dolayısıyla faz bilgisi atıldıktan sonra bile `G_0,G_1,G_2,...` ailesi
**mesafe ekseninde komşu bir üst-yineleme olarak kapanır**. Başlangıçta `d=0`
olduğu için derinlik `s` boyunca yalnız `d<=s-1` gerekir; durum genişliği
lineerdir.

Bu, yalnız `G_0=M4` taşıyan scalar yinelemeden daha fazla bilgiyi korur.

---

# 3. [TAM SONLU DOĞRULAMA] Formüllerin uygulama kontrolü

`weighted_gram_round1.py`:

- operator biçimindeki tam `G_0` özdeşliğini **310** gerçek filtre durumunda
  tam tamsayı olarak kontrol etti;
- `d=1,...,4` için yeni hiyerarşi eşitsizliğini **736** gerçek filtre/durumda
  kontrol etti;
- ihlal: **0**;
- eşitlik örnekleri: **12**.

Bu hesaplar ispat değildir; yukarıdaki cebir ispatın kendisidir. Sonlu kontrol
normalizasyon, `3^-d` yönü ve indeks kaymalarını sınamak için yapıldı.

---

# 4. [ELENDİ — SONLU AYIRT EDİCİ TEST] Faz-kör hiyerarşi kritik bölgede yeterli görünmüyor

Hiyerarşi eşitsizliklerini tabandan yukarı dinamik programla uygulayıp
`U_H(t,j,s)` üst sınırı üretildi.

Önceden sabitlenen ayırt edici grid:

- `t=8,...,30`,
- `j = round(t/log2(3)) + {-1,0,1}` (iç destekle kırpıldı),
- `s=2,...,min(t,10)`,
- toplam **612** gerçek filtre,
- rastgele örnekleme yok.

Sonuç:

- `U_H < M2^2/2`: **0** durum,
- `U_H = M2^2/2`: **6** durum,
- `U_H`, eski scalar `U_iter`'dan daha iyi: **101** durum.

Yani mixed mesafe bilgisini taşımak eski scalar kaybının bir kısmını geri
alıyor, fakat bu kritik sonlu testte zaten bilinen conjugate-pair sınırını
geçemiyor.

**Statü:** Bu bir asimptotik imkânsızlık teoremi değildir. Fakat önerilen
“fazı at, yalnız güç-overlap hiyerarşisini taşı” yaklaşımı ilk ayırt edici
testini geçemedi. Aynı biçimde daha büyük sayı taramak şu aşamada değerli
değil.

---

# 5. [KANITLANMIŞ KARŞI-ÖRNEK] İki ölçeklik zorunlu reflection-dissipation yanlış

Bir başka doğal fikir şuydu:

> Her parent-child çiftinde en az bir ölçekte `N_-/N_B` pozitif bir uniform
> miktar olsun; böylece iki ölçeklik blokta worst-case `N_+=N_B` doygunluğu
> kırılsın.

Gerçek filtre bunu doğrudan çürütüyor.

### Parent `(t,j,s)=(11,6,4)`

`N0=653072`  
`N1=230496`  
`NB=384160`  
`N_+=384160`  
`N_-=0`

### `j` değişmeyen çocuk `(10,6,3)`

`N0=153664`  
`N1=38416`  
`NB=76832`  
`N_+=76832`  
`N_-=0`

Yani iki ardışık ölçekte de mixed kanal tamamen reflection-even.
Bir sonraki `(9,6,2)` seviyesinde ise `N_+=0`, `N_-=NB`; fakat bu,
**iki-ölçek uniform gap** iddiasını kurtarmaz.

Dolayısıyla “her iki adımda bir otomatik yansıma kaybı” leması yanlış.

---

# 6. [SONLU TANI] Source/W_flat ağırlıkları faz bilgisini yine de değerli kılabilir

Eski gerçek-source panellerinde, yalnız `s>=2` katmanlarını ve `W_flat`
katman ağırlıklarını kullanarak

`sum flat_(k,s) * (N_-/NB) / sum flat_(k,s)`

tanısı hesaplandı:

- `r=10`: `23/37 ≈ 0.62162`
- `r=12`: `9886/13323 ≈ 0.74203`
- `r=14`: `6391859/10726947 ≈ 0.59587`

Fakat sıfır-defisit katmanları da gerçekten var (`r=10` ve `r=14`
panellerinde örnek var). Bu üç sayı **teorem değildir** ve bir trend iddiası
değildir. Yalnızca şu araştırma kararını destekliyor:

- pointwise reflection gap istemek fazla güçlü;
- **source-ağırlıklı ortalama phase/reflection kontrolü** hâlâ makul bir
  sonraki hedef.

---

# 7. Neden yalnız `N_B` ve `N_+` ile tam kapanış beklenmemeli?

`G_1`'i bir ölçek daha yukarı taşırken yalnız adjacent overlap çıkmıyor.
Açılımda `j` ile `j-2` arasındaki

`G_2`

ve faz-duyarlı dört-kanal terimleri ortaya çıkıyor. Yani `(M4,N_B,N_+)`
üçlüsü tam bir Markov durumu değildir.

Yukarıdaki `G_d` hiyerarşisi, fazı mutlak değerle yok ettiğimizde bu genişlemeyi
kontrollü biçimde kapatıyor; ama kritik testte tam da bu faz kaybı fazla pahalı
çıktı.

Bu nedenle bir sonraki durum değişkeni yalnız başka bir scalar norm olmamalı.

---

# 8. [YENİ OPERATÖR FORMÜLASYONU / SONRAKİ HEDEF]

Alt frekansta kanal amplitüdlerini

`v_d(a)=phi_(j-d)(3^(-d)a)`

olarak dizelim. Bir ölçek lift'inde

`v'_d(sigma)=v_d + sigma eta_d v_(d+1)`.

`p_d=|v_d|^2` ve

`c_d=eta_d v_(d+1) conjugate(v_d)`

yazılırsa

`p'_d(sigma)=p_d+p_(d+1)+2 sigma Re(c_d)`.

İki lift üzerinde çarpımın ortalaması TAM olarak

`(1/2) sum_sigma p'_e(sigma)p'_f(sigma)
 = (p_e+p_(e+1))(p_f+p_(f+1))
   + 4 Re(c_e) Re(c_f).`

Bu formül yeni hiyerarşide kaybettiğimiz bilginin tam yerini gösterir:
**edge-coherence kovaryansları** `Re(c_e)Re(c_f)`.

Bundan sonraki en değerli küçük hedef:

> İki ölçeklik bir blok için `d=0,1,2` amplitüdlerini ve edge-coherence
> Gram matrisini TAM taşı; source/W_flat ağırlıklarını en baştan uygula.
> Sonra bu phase-sensitive blok operatörünün bilinen `M2^2/2` sınırından
> gerçekten küçük bir ağırlıklı üst sınır verip vermediğini sınayan tek bir
> kesin eşitsizlik kur.

Bu test iki sonuçtan birini vermeli:

1. **Kazanç:** source-ağırlıklı blok operatörü trivial sınırı gerçekten
   aşağı çeker; o zaman asimptotik operatör normu hedeflenir.
2. **Engel:** actual source ağırlıklarıyla da blok sabiti trivial sınıra
   doyar/yaklaşır; o zaman cross-term hiyerarşisini büyütmek bırakılır.

Yeni büyük `t,s` taraması bu lemmadan önce yapılmamalı.

---

# 9. Ana ispat açısından durum

**Yeni bulunan:**  
Mixed overlap için mesafe-`d` Gram hiyerarşisi ve kapalı faz-kör üst-yineleme.

**Çürütülen/elendi:**  
- iki ardışık ölçekte zorunlu `N_-` kaybı;
- fazı tamamen atan Gram hiyerarşisinin, seçilen kritik sonlu testte mevcut
  trivial sınırı geçeceği umudu.

**Açık:**  
- source-ağırlıklı phase-sensitive blok eşitsizliği;
- büyüyen kritik ailede `W` üst sınırı;
- `W_flat` için gereken asimptotik bütçe;
- `D2` hedefi;
- Collatz.

Bu tur hiçbir genel Collatz sonucu veya yüzde ilerleme iddiası üretmez.

## Yayın notu

GitHub dalındaki `RESULTS_SUMMARY.json` kompakt sonucu taşır. Bütün ayrıntılı satır tablosu `RESULTS.json`, kod, provenance ve gerçek çalıştırma çıktısıyla birlikte Drive'daki `COLLATZ_MIXED_GRAM_ROUND1_20260912.zip` paketinde saklanır.
