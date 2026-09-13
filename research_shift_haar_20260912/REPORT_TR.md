# Shift-Haar / 2-adik kaydırma değer ayrıştırması — source-filter hizalanması için faz-duyarlı köprü

Tarih: 12 Eylül 2026  
Kanonik kaynak commit: `434d8fc55544207b35a4c4390600598dd6623d28`  
Devam edilen araştırma dalı: `research/mixed-gram-round1-20260912`  
Durum: **yeni exact özdeşlikler + exact küçük panel doğrulamaları + ayrı etiketli önceki FFT tanıları. Uniform W, D2 ve Collatz açık.**

## Basit sonuç

Önceki turda `N_B` ve yansıma-çift parça `N_+` bulundu, fakat bunları gerçek kaynak ağırlıklarıyla ölçekler boyunca nasıl taşıyacağımız açık kaldı.

Bu turda doğru ara nesne bulundu:

> Aynı iletkendeki source-filter Fourier hizalanma hatası, autocorrelation sibling-farklarının kaydırma `v2(d)` sınıflarına **tam olarak ayrılır**.

Bu ayrıştırma, Boolean Walsh değildir. Aynı cyclic Fourier iletkeni içindeki frekans lift ağacının Haar/martingale ayrıştırmasıdır; zaman-kod parite küpüne herhangi bir grup izomorfizmi varsayılmaz.

En önemli bağlantı:

- tail tarafında ilk `v2(d)=0` katmanının kare enerjisi **tam olarak `4 N_+`**;
- daha derin katmanlar, child kanalların aynı değer-enerjileri ve `N_B`'yi genişleten pozitif blok-overlap kulesi ile exact tekrar eder.

Böylece `N_+` artık yalnız yerel cross-term notasyonu değil: gerçek source-tail alignment'ın **ilk faz-duyarlı Haar increment'i**.

Ayrıca ilk `L` değer katmanının işaretli katkısını aynen tutup yalnız kalan katmanları Cauchy ile kapatan bir `U_L` sınırı elde edildi. `U_L` monoton azalır; `L=0` daha önceki merkezlenmiş concentration/Cauchy sınırıdır, bütün katmanlar tutulunca exact hizalanma elde edilir.

Bu küçük panellerde güçlü bir fark yarattı. Örneğin `r=14` için:

- `U_0/W ≈ 2.20222`,
- `U_1/W ≈ 1.52269`,
- `U_2/W ≈ 1.06313`,
- `U_3/W = 1`.

Bu sonlu sonuç asimptotik teorem değildir. Fakat fazı ilk iki lift katmanında korumanın önceki faz-kör Gram yaklaşımından neden daha etkili olduğunu somut olarak gösterir.

---

# 1. Kurulum

Tek bir `(k,s)` source-tail shell'i sabitleyelim. Yerel cyclic modül

`n = 2^s`,  `H = n/2`.

Gerçek source projeksiyonu `P(u)` ve gerçek tail aggregate filtresi `F(u)` olsun. İkisi de `Z/nZ` üzerinde gerçek dizilerdir.

Cyclic autocorrelation'ları

`C_P(d)=sum_u P(u)P(u+d)`,

`C_F(d)=sum_u F(u)F(u+d)`

ve sibling farklarını

`D_P(d)=C_P(d)-C_P(d+H)`,

`D_F(d)=C_F(d)-C_F(d+H)`,  `0<=d<H`

tanımlayalım.

`R_P=D_P(0)` ve `R_F=D_F(0)` olsun. Önceki notation'da `R_F=D(t,j,s)` tail shell budget'ıdır. Sıfır shell'de (`R_P R_F=0`) hem gerçek variance hem flat katkı sıfırdır; aşağıdaki normalize ifadeler yalnız pozitif shell'ler içindir.

Unnormalized Fourier dönüşümünde primitive odd frekanslar için

`X_a=|P_hat(a)|^2`, `Y_a=|F_hat(a)|^2`.

Flat shell katkısı

`flat = H R_P R_F / Q^2`

(`Q=2^t` full tail modulus) ve gerçek shell variance

`V = Q^(-2) sum_(a odd mod n) X_a Y_a`.

Alignment

`A=V/flat`.

---

# 2. [KANIT] Alignment'ın autocorrelation fark özdeşliği

Autocorrelation Fourier dönüşümleri `X_a` ve `Y_a`'dır. Primitive bilinear Parseval / power-of-two Ramanujan toplamı şunu verir:

`sum_(a odd) X_a Y_a
 = H sum_(d=0..H-1) D_P(d) D_F(d)`.

Ayrıca

`sum_(a odd) X_a = H R_P`,

`sum_(a odd) Y_a = H R_F`.

Dolayısıyla **tam olarak**

`A = [sum_(d<H) D_P(d)D_F(d)]/(R_P R_F)`.

`d=0` terimi zaten `R_P R_F` olduğundan

`A-1 = [sum_(1<=d<H) D_P(d)D_F(d)]/(R_P R_F)`.

Bu, source-tail spektral hizalanmayı Fourier katsayılarını tek tek hesaplamadan, tamamen tamsayı autocorrelation farklarıyla ifade eder.

---

# 3. [KANIT] Shift-valuation / lift-Haar ayrıştırması

`ell=1,...,s-1` için

`Omega_ell = { d : 1<=d<H, v2(d)=ell-1 }`.

Tanımla:

`Gamma_ell = sum_(d in Omega_ell) D_P(d)D_F(d)`,

`S_ell = sum_(d in Omega_ell) D_P(d)^2`,

`T_ell = sum_(d in Omega_ell) D_F(d)^2`.

O zaman

`A = 1 + sum_(ell=1..s-1) gamma_ell`,

`gamma_ell = Gamma_ell/(R_P R_F)`.

Ve her katmanda Cauchy:

`|gamma_ell| <= sqrt(S_ell T_ell)/(R_P R_F)`.

Bu, primitive frekans güç dağılımlarının high-bit lift ağacındaki ortonormal Haar ayrıştırmasıyla aynıdır. Eğer primitive odd frekanslar `a=1,3,...,2^s-1` diye sıralanırsa ilk Haar farkı `a` ile `a+2^(s-1)` liftlerini karşılaştırır, sonraki Haar farkları bu lift bloklarının ortalamalarını karşılaştırır. Yukarıdaki `v2(d)` formülü aynı ayrıştırmanın tamamen tamsayılı autocorrelation dualidir.

Önemli: bu **parity-word Walsh** ayrıştırması değildir. Ayrıştırılan şey cyclic Fourier frekans indeksinin 2-adik lift ağacıdır.

---

# 4. [KANIT] Signed-retention üst sınırı ve monotonluk

İlk `L` katmanın işaretini tam tutup kalanını tek Cauchy ile kapat:

`U_L = 1
       + sum_(ell<=L) gamma_ell
       + sqrt[(sum_(ell>L)S_ell)(sum_(ell>L)T_ell)]/(R_P R_F)`.

Özel durumlar:

- `U_0 = 1+sqrt((C_X-1)(C_Y-1))`: önceki merkezlenmiş concentration bound;
- `U_(s-1)=A`: exact alignment.

Ayrıca

`U_(L+1) <= U_L`.

İspat: yeni ayrılan blok için `a=S_(L+1), b=T_(L+1)`, geri kalan için `c,d` yaz. Cauchy `Gamma_(L+1)<=sqrt(ab)` verir; ayrıca

`sqrt((a+c)(b+d)) >= sqrt(ab)+sqrt(cd)`

çünkü farkın karesi `(sqrt(ad)-sqrt(bc))^2 >=0`'dır. Böylece işaretli bir katmanı exact taşımak üst sınırı kötüleştiremez.

Bu çok önemli bir farktır: peak-peeling frekansları tail büyüklüğüne göre seçerken, burada frekans seçimi yoktur; sabit aritmetik `v2(d)` katmanları kullanılır ve negatif alignment katkıları korunur.

---

# 5. [KANIT] `N_+` tam olarak ilk tail Haar enerjisidir

Cross-term notasyonunda parent derinliği `s>=2` için

`q=2^(s-1)`, `h0=q/2`,

`D_parent(d)=C_s(d)-C_s(d+q)`.

Önceki exact split:

`D_odd(h)=Delta B(3h+2)+Delta B(-3h-1)`.

Odd parent shifts `d=2h+1`, yani tam `v2(d)=0` katmanıdır. Önceki ispat

`S_odd = sum_h D_odd(h)^2 = 4 N_+`

verdi.

Dolayısıyla bu turdaki notation ile tail için

`T_1(t,j,s) = 4 N_+(t,j,s)`.

Bu, önceki yansıma-çift bileşenin gerçek `W` hizalanma problemindeki yerini tam belirler.

Fourier lift dilinde aynı ifade: `Y_+ - Y_- = 4 Re(c)` olduğu için ortonormal ilk Haar detail enerjisi `8 sum Re(c)^2 = 4(G_1+C_1)`, bu da önceki `N_+` ölçeklemesiyle aynıdır.

---

# 6. [KANIT] Daha derin tail katmanları ve pozitif blok-overlap kulesi

Parent even branch için önceki exact form:

`D_parent(2h)=Delta A0(h)+Delta A1(3h)`.

`ell>=2` için `v2(2h)=ell-1` iff `v2(h)=ell-2`. Dolayısıyla

`T_ell(t,j,s)
 = T_(ell-1)(t-1,j,s-1)
 + T_(ell-1)(t-1,j-1,s-1)
 + 2 E_(ell-2)`,

burada

`E_r = sum_(0<h<h0, v2(h)=r) Delta A0(h) Delta A1(3h)`.

Şimdi cumulative mixed overlap tanımla:

`B_r = sum_(0<=h<h0, 2^r | h) Delta A0(h) Delta A1(3h)`.

O zaman

`E_r = B_r-B_(r+1)`

(terminal `h=0` terimi iki cumulative toplamda da bulunduğu için doğru biçimde iptal olur).

En önemli Fourier blok formülü:

`B_r = [2/(q 2^r)]
       sum_(a,b odd mod q; a+3b = 0 mod q/2^r)
         |f0_hat(a)|^2 |f1_hat(b)|^2 >= 0.`

İspat: anti-periodik `Delta A0,Delta A1` Fourier'de yalnız odd frekans taşır ve dönüşümleri sırasıyla `2|f0_hat|^2`, `2|f1_hat|^2`'dir. `2^r|h` altgrubu üzerinde karakter toplamı `a+3b=0 mod q/2^r` kongruensini zorlar. Half/full normalizasyonu yukarıdaki `2/(q2^r)` katsayısını verir.

`r=0`'da kongruens tek bir partner bırakır ve önceki

`B_0=N_B`

özdeşliği geri gelir.

Dolayısıyla `N_B`, yeni bir nesne değilmiş gibi kaybolmaz: **pozitif alias-block overlap kulesinin ilk elemanıdır.**

Ancak positivity contraction değildir. Gerçek filtre karşıörneği:

`(t,j,s)=(6,3,5)` için

`(B_0,B_1,B_2,B_3)=(16,24,16,16)`.

Yani `B_(r+1)<=B_r` gibi doğal bir monotonluk iddiası yanlıştır. Bu turda 426 gerçek filtre durumunda 1.822 cumulative `B_r` değeri kontrol edildi; hepsi nonnegative, fakat birçok nonmonotone örnek var.

---

# 7. [TAM SONLU DOĞRULAMA] Exact tamsayı kontrolleri

`shift_haar_round2.py` ana hesapta:

- 426 gerçek `(t,j,s)` tail durumu;
- 1.822 cumulative blok-overlap nonnegativity kontrolü;
- 426 kez `T_1=4N_+` kontrolü;
- 1.396 valuation-recursion özdeşliği;
- bütün kontroller exact tamsayı/Fraction aritmetiğinde geçti.

Source tarafında `r=5,10,12,14` gerçek prefix histogramları baştan oluşturuldu. Fourier/FFT kullanılmadan autocorrelation farklarından hem gerçek alignment hem `U_L` sınırları hesaplandı.

| r | W/W_flat | U0/W | U1/W | U2/W | U3/W |
|---:|---:|---:|---:|---:|---:|
|5|1|1|1|1|1|
|10|819/779 ≈1.05135|1|1|1|1|
|12|11180/7987 ≈1.39977|1.11427|1.06655|1|1|
|14|274211/374259 ≈0.73268|2.20222|1.52269|1.06313|1|

Buradaki `U_L/W` ondalıkları exact integer/rational girdilerdeki karekök üst sınırlarının Decimal gösterimidir. `W`, `W_flat`, signed katman katkıları ve recurrence kontrolleri exact'tir.

Exact aggregate signed katkılar / W:

- `r=10`: level 1 = `40/819`, level 2 = 0.
- `r=12`: level 1 = `2329/11180`, level 2 = `216/2795`, level 3 = 0.
- `r=14`: level 1 = `-47360/274211`, level 2 = `-1024/6377`, level 3 = `-8656/274211`, level 4 = 0.

Bu r14 örneği neden global absolute-value/Cauchy bound'ın pahalı olduğunu çok açık gösteriyor: üç gerçek lift katmanının hepsi toplamda negatif katkı yapıyor.

---

# 8. [SAYISAL TANI — YENİ HESAP DEĞİL] Daha büyük eski FFT panelleri

`r=18,19,20` için yeni prefix enumeration/FFT yapılmadı. Önceki `research_peak_peeling_20260912/RESULTS.json` içinde zaten yayınlanmış source/tail conjugate-pair FFT büyüklükleri yeniden gruplanarak bu yeni `U_L` tanısı hesaplandı. Bu nedenle aşağıdaki satırlar **interval/exact sertifika değildir**; mevcut floating diagnostic'in yeni bir post-processing'idir.

| r | U0/W | U1/W | U2/W | U3/W |
|---:|---:|---:|---:|---:|
|18|1.71236|1.40876|1.19144|1.05026|
|19|2.53836|1.68684|1.40653|1.27365|
|20|2.31925|1.54595|1.27660|1.19120|

Önceki tail-selected peak peeling'in `L=4` tanısı:

- r18: yaklaşık 1.29182 W,
- r19: yaklaşık 1.81589 W,
- r20: yaklaşık 1.60355 W.

Dolayısıyla bu mevcut sonlu tanılarda **iki signed lift katmanı** (`U_2`) dört tail-peak peeling'den daha sıkı çıkıyor; r20'de tek signed katman (`U_1≈1.546`) bile eski dört-peak tanısından biraz daha iyi. Bu önemli bir yön sinyalidir, fakat FFT kaynaklı sayılar nedeniyle kanıt değildir ve büyüyen aile için trend ilan edilemez.

r20'de aggregate signed lift katkıları / W yaklaşık:

- level1: -0.00327,
- level2: +0.09408,
- level3: +0.06970,
- level4: +0.04661,
- level5: +0.01271.

Yani yalnız `N_+`/ilk level'i kontrol etmek yetmez; zararlı pozitif alignment orta lift ölçeklerine taşınabiliyor. Yeni recurrence'ın `B_r` kulesine ihtiyaç duymasının sayısal karşılığı budur.

---

# 9. [AYRI UYGULAMA KONTROLÜ — BAĞIMSIZ AJAN DEĞİL]

`independent_check.py`, ana kodun helper'larını import etmeden:

- 79 deterministik arbitrary nonnegative vector çifti için direct complex DFT alignment ile integer autocorrelation formülünü karşılaştırdı;
- maksimum numerical fark yaklaşık `1.05e-14`;
- 124 gerçek küçük tail filtresinde cumulative `B_r` Fourier block formülünü doğrudan DFT ile kontrol etti;
- 415 cumulative seviye karşılaştırması geçti.

Bu ikinci uygulama aynı asistan oturumunda yazıldı. **Bağımsız alt ajan/hakem denetimi değildir.** Genel doğruluk finite testten değil yukarıdaki cebirsel ispatlardan gelir.

---

# 10. Ne elendi, ne kaldı?

## Elenen / yanlış olan basit fikirler

1. `E=N_B` özdeşliğini her `v2(h)` sınıfında ayrı ayrı aynen kullanmak yanlış. Global Fourier diagonalization, shift-valuation'a naif biçimde lokalize olmaz.
2. `B_r` pozitif olduğuna göre `B_r` monoton azalır fikri yanlış; `(6,3,5)` somut karşıörnek.
3. Yalnız ilk reflection gap (`N_-` veya `N_+`) ile bütün hizalanmayı kontrol etmek yetersiz; orta lift katmanları gerçek panellerde önemli.

## Yeni gerçek yapı

- `N_+` = ilk tail shift-Haar enerjisi /4.
- `N_B=B_0`; daha derin even-branch kontrolü `B_1,B_2,...` pozitif alias-block overlap kulesine uzanıyor.
- Source-tail alignment hatası exact signed `v2(d)` katmanlarının toplamı.
- İlk birkaç signed katmanı exact taşımak, kalanını Cauchy ile kapatmaktan matematiksel olarak güvenli ve monoton iyileşen bir üst sınır doğuyor.

---

# 11. Ana ispat açısından durum ve sıradaki hedef

Bu tur `W` için asimptotik üst sınır kanıtlamadı. `W_flat`'in gerekli exponent kontrolü ayrıca açık. `D2` ve Collatz da açık.

Ama bir sonraki hedef artık çok daha spesifik:

> **Büyüyen kritik ailede yalnız ilk 1–2 shift-valuation katmanının source-weighted signed toplamını ve kalan tail/source enerji bütçesini kontrol et.**

Özellikle

`sum_(k,s) flat_(k,s) Gamma_1/(R_P R_F)`

ve ardından `Gamma_2` için aritmetik bir üst sınır aranmalı. Tail tarafında `T_1=4N_+` exact; `T_2,T_3,...` için child valuation energies + `B_r-B_(r+1)` recurrence'ı var. Source tarafında aynı `S_ell` tamsayı autocorrelation fark enerjileri doğrudan tanımlı.

Bu hedef, tüm frekans spektrumunu uniform düzleştirmekten veya bütün peakleri sınırlamaktan daha zayıftır: yalnız gerçek `W_flat` ağırlıkları altında ilk birkaç signed lift katmanı ve residual enerji istenir.

## [KANIT] Aggregate weighted form: shell normalizasyonları iptal oluyor

Bir shell `b=(k,s)` için `H_b=2^(s-1)`, source/tail sibling normları `R_{P,b},R_{F,b}` ve

`flat_b = H_b R_{P,b} R_{F,b}/q^2`

olsun. Yukarıdaki normalize signed katman

`gamma_{b,ell}=Gamma_{b,ell}/(R_{P,b}R_{F,b})`

ile çarpınca paydalar tamamen yok olur:

`flat_b * gamma_{b,ell} = H_b Gamma_{b,ell}/q^2.`

Dolayısıyla ilk `L` signed katmanın **aggregate gerçek katkısı** tam olarak

`Delta W_ell = q^(-2) sum_b H_b Gamma_{b,ell}`

ve

`W = W_flat + sum_ell Delta W_ell`

şeklindedir (sonlu panelde bütün katmanlar dahil edildiğinde). Burada hiçbir `R_P R_F` bölmesi kalmaz; sıfır shell'ler ayrıca ele alınmak zorunda değildir. Bu, source-ağırlıklı formun normalize shell oranlarından daha doğal halidir.

İlk `L` katmanı exact tutup residualı shell-bazında Cauchy ile kapatınca

`W <= W_flat
      + q^(-2) sum_(ell<=L) sum_b H_b Gamma_(b,ell)
      + q^(-2) sum_b H_b sqrt(S_(b,>L) T_(b,>L)).`

Son terime shell'ler arasında bir kez daha Cauchy uygulanırsa **tek bir global residual bound** elde edilir:

`W <= W_flat
      + q^(-2) sum_(ell<=L) sum_b H_b Gamma_(b,ell)
      + q^(-2) sqrt( S^agg_(>L) T^agg_(>L) ),`

`S^agg_(>L)=sum_b H_b S_(b,>L)`,
`T^agg_(>L)=sum_b H_b T_(b,>L)`.

Bu eşitsizlik shell shell worst-case oran istemez. Özellikle `ell=1` tail bütçesinde `T_1=4N_+` olduğundan

`T^agg_1 = 4 sum_b H_b N_{+,b}`

exact'tir. Böylece önceki `N_+` yansıma bileşeni ilk kez doğrudan gerçek `W`-ağırlıklı aggregate eşitsizliğe bağlanır.

Bu henüz asimptotik bir bound değildir; yeni açık girdiler `sum_b H_b Gamma_(b,1)`, gerekirse `ell=2`, ve aggregate residual source/tail bütçeleridir. Fakat hedef artık pointwise strict-gap veya her shell için uniform alignment istemekten daha zayıf ve doğrudan `W` ile normalize edilmiştir.

`aggregate_check.py` bu yeniden yazımı mevcut exact source panellerinde tam kesirlerle doğruladı. Shell'ler arasında ikinci Cauchy de uygulanmış global residual bound için:

| r | L=0 upper/W | L=1 upper/W | L=2 upper/W | L=3 upper/W |
|---:|---:|---:|---:|---:|
|5|1|—|—|—|
|10|1.12314|1|1|—|
|12|1.29997|1.13804|1|1|
|14|2.53659|1.57439|1.09316|1|

Bunlar sonlu exact girdilerden elde edilen sertifikalı cebirsel üst sınırlardır; büyüyen aile için sabit-factor veya exponent teoremi değildir. Global Cauchy shell-bazlı `U_L`'den doğal olarak daha gevşek olabilir, fakat yalnız iki aggregate residual bütçesi gerektirdiği için asimptotik hedef açısından daha uygundur.

Ayırt edici sonraki lemma:

1. `ell=1` için gerçek prefix source `D_P(d)` yapısını kullanarak aggregate signed `Gamma_1`'ı bound et;
2. başarırsa `ell=2` için `B_0-B_1` tail recurrence ile eşleştir;
3. bu iki katmanla elde edilen aggregate üst sınırın gerekli W exponentine taşınıp taşınamayacağını kontrol et;
4. finite panel başarısını asimptotik kanıt yerine koyma.

Bu rota başarısız olursa, karşıörnek artık genel “phase matters” seviyesinde değil, doğrudan source-weighted `Gamma_1/Gamma_2` büyüyen ailesinde aranabilir.

---

## Dört kısa cevap

**Ne yeni bulundu?**  
Source-filter hizalanmasının exact 2-adik shift-Haar ayrıştırması, monoton signed-retention bound `U_L`, `T_1=4N_+` bağlantısı ve `N_B`'yi genişleten pozitif `B_r` blok-overlap kulesi.

**Ne çürütüldü/elendi?**  
`E=N_B`'nin valuation sınıflarında ayrı ayrı kapanacağı ve pozitif `B_r` kulesinin otomatik monoton contraction vereceği fikirleri.

**Ana ispat açısından ne açık?**  
İlk birkaç signed source-tail katmanının büyüyen kritik ailede uniform/ağırlıklı kontrolü; residual enerji; W_flat exponenti; W, D2 ve Collatz.

**Sıradaki en değerli somut adım?**  
`ell=1` aggregate signed term için gerçek prefix histogramının aritmetik yapısını kullanan bir lemma; sonra `ell=2` ile birlikte iki-katmanlı asymptotic weighted bound.
