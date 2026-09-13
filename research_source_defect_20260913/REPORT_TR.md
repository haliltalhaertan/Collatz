# Source Defect Round 7 — monotonicity defectinin exact iki-terimli ayrışması

**Tarih:** 13 Eylül 2026  
**Kanonik main:** `434d8fc55544207b35a4c4390600598dd6623d28`  
**Araştırma dalı / PR:** `research/mixed-gram-round1-20260912` / PR #2  
**Statü:** **exact enerji-defect özdeşliği + generic positivity karşıörneği + tam sonlu actual-source kontrolü.** Uniform `W`, `W_flat`, `D2` ve Collatz açık.

## Basit sonuç

Round 5'te gerçek prefix source için şu güçlü desen görülmüştü:

`Ecal(m+1,s) <= Ecal(m,s+1)`.

Bu 108 exact geçişte doğruydu fakat neden doğru olduğu bilinmiyordu. Bu tur monotonicity farkını tam olarak iki ayrı mekanizmaya ayırdı:

`Ecal(m,s+1) - Ecal(m+1,s) = M_merge - L_lift.`

Burada:

- `M_merge >= 0`, komşu k-stratumlarından gelen iki source kategorisinin Pascal/binom ağırlıklı **birleştirme slack'i**;
- `L_lift`, bir source stratumunun iki Fourier lift'i arasındaki signed genişleme. Fiziksel uzayda doğrudan source autocorrelation sibling-farkının doğal affine shift `3^k`'deki değeridir ve iki işaretli olabilir.

Dolayısıyla source monotonicity problemi artık kesin olarak şu tek eşitsizliğe indirgenmiştir:

`M_merge >= L_lift.`

`L_lift <= 0` olduğu her durumda monotonicity otomatik gelir. Prescribed Round-5 gridindeki 108 exact geçişin 105'inde bu zaten oldu. Geri kalan 3 durumda merge slack pozitif lift genişlemesini bastırdı.

Fakat önemli bir sınır bulundu: nonnegative histogramlar ve doğru binom stratum kütleleri tek başına yeterli değildir. `m=3,s=2` için açık nonnegative integer histogram ailesi aynı transfer altında

`input=12`, `output=40/3`, yani `output/input=10/9>1`

veriyor. Bu nedenle monotonicity salt positivity/Jensen sonucu değildir; gerçek Collatz source'un **reachable-source** yapısı gerçekten kullanılmalıdır.

Bu tur monotonicity'yi henüz kanıtlamıyor. Fakat eksik lemmayı çok daha dar ve somut hale getiriyor.

---

## 1. Kurulum

`P_k = P_(m,k,s+1)` gerçek source histogramı olsun. Modül

`N=2^(s+1)`, `q=N/2=2^s`

ve stratum kütlesi

`n_k = binom(m-1,k-1)`.

Primitive enerji fonksiyonunu, uzunluğu `2^r` olan gerçek bir dizi `X` için

`J_r(X) = sum_(xi odd mod 2^r) |Xhat(xi)|^2`

olarak tanımla. Sibling-difference formuyla tam olarak

`J_r(X) = 2^(r-1) sum_(u<2^(r-1)) [X(u)-X(u+2^(r-1))]^2.`

Round-5 source enerjisi

`Ecal(m,r) = sum_k J_r(P_(m,k,r))/n_k`.

Round-3 source transferindeki doğal base-k kategorilerini bu kez ayrı tutuyoruz. `c_k=3^k mod N` olsun:

`E_k = E_(c_k) P_k`,

`O_k = O_(c_k) P_k`.

Her ikisi de mod `q` dizisidir. `E_k`, base weight k'dan output weight k'ya; `O_k`, base weight k'dan output weight k+1'e katkıdır. Exact source transfer:

`P'_(k) = E_k + O_(k-1)`

ve output kütlesi

`n'_k=n_k+n_(k-1)=binom(m,k-1)`.

Eksik sınır kategorileri sıfır kabul edilir.

Üç enerji tanımla:

`I = sum_k J_(s+1)(P_k)/n_k = Ecal(m,s+1)`,

`F = sum_k [J_s(E_k)+J_s(O_k)]/n_k`,

`O = sum_k J_s(E_k+O_(k-1))/(n_k+n_(k-1)) = Ecal(m+1,s)`.

`F`, son Pascal birleştirmesinden önceki iki ince kategorinin enerjisidir.

---

## 2. [KANIT] Lift genişlemesi `L = F-I` için exact source-shift formu

Bir base stratum k için `P=P_k`. Input primitive frekansını `xi` ile gösterelim. Round-5 gauge formunda output frekansı `a=3^k xi mod N` seçilince iki lift katsayısının ince-kategori toplam enerjisi

`|S_0|^2+|S_1|^2`
` = |X_+|^2+|X_-|^2`
`   + cos(2 pi a/N)(|X_+|^2-|X_-|^2)`

olur.

`a=3^k xi` ile primitive frekanslar yeniden indekslenince

`J_s(E_k)+J_s(O_k)-J_(s+1)(P_k)`
` = sum_(xi odd mod N) cos(2 pi 3^k xi/N) |P_hat_k(xi)|^2.`

Şimdi `C_k(d)=sum_z P_k(z)P_k(z+d)` cyclic autocorrelation olsun. Odd-character Ramanujan toplamı yalnız `d=c_k` ve `d=c_k+q` sibling shiftlerini bırakır. Böylece tam olarak

`J_s(E_k)+J_s(O_k)-J_(s+1)(P_k)`
` = q [ C_k(c_k) - C_k(c_k+q) ].`

Sonuç:

`L_lift := F-I`
` = q sum_k [ C_k(3^k)-C_k(3^k+q) ] / n_k.`

Bu ifade tam sayısal Fourier yaklaşımı değildir; exact cyclic identity'dir. Shift `3^k`, source transferindeki iki m-step lift endpoint'inin exact farkıdır.

Ayrıca Shift-Haar diliyle `C_k(d)-C_k(d+q)` source autocorrelation sibling-difference profilidir. Yani lift genişlemesi, bu profilin tam olarak arithmetic shift `3^k` üzerindeki signed örneklemesidir.

`L_lift` pozitif, sıfır veya negatif olabilir.

---

## 3. [KANIT] Pascal birleşme slack'i `M = F-O` exact kare normudur

Sabit output k için iki kategori

`A=E_k`, kütle `a=n_k`,

`B=O_(k-1)`, kütle `b=n_(k-1)`

olsun. `J_s` bir Hilbert normunun karesidir. Her `a,b>0` için elementary weighted parallelogram identity:

`J_s(A)/a + J_s(B)/b - J_s(A+B)/(a+b)`
` = J_s(b A-a B) / [a b (a+b)].`

Dolayısıyla

`M_merge := F-O`
` = sum_(k=2..m)`
`   J_s( n_(k-1) E_k - n_k O_(k-1) )`
`   / [ n_k n_(k-1) (n_k+n_(k-1)) ]`
` >= 0.`

Sınır k=1,m+1 kategorilerinde yalnız tek giriş vardır; slack sıfırdır.

Bu, generic Cauchy değil, exact kayıp miktarıdır.

---

## 4. [ANA ÖZDEŞLİK] Monotonicity defecti

Tanımlardan

`I-O = (F-O)-(F-I)`

olduğundan yukarıdaki iki theorem ile

`Ecal(m,s+1)-Ecal(m+1,s)`
` = M_merge - L_lift.`

Dolayısıyla tam eşdeğerlik:

`Ecal(m+1,s) <= Ecal(m,s+1)`

**ancak ve ancak**

`M_merge >= L_lift`.

Özellikle `L_lift<=0` ise monotonicity otomatik olarak doğrudur, çünkü `M_merge>=0`.

Bu reduction Round-5'in singular-value analizini ortadan kaldırmaz; onun fiziksel-source karşılığıdır. Generic operator expansion tam olarak `L_lift>0` yönüdür; Pascal mixing'in actual geri kazanımı ise `M_merge` ile ölçülür.

---

## 5. [KARŞI-ÖRNEK] Positivity + doğru binom kütleleri yeterli değil

`m=3`, `s=2`, input modülü `N=8` olsun. Kütleler `(n_1,n_2,n_3)=(1,2,1)`.

Şu nonnegative integer histogramları al:

`P_1=(0,0,1,0,0,0,0,0)`,

`P_2=(1,0,0,0,0,0,0,1)`,

`P_3=(0,0,0,0,1,0,0,0)`.

Toplamları tam olarak `(1,2,1)`'dir. Aynı exact `E_(3^k),O_(3^k)` source-transfer operatörünü uygula.

Exact sonuç:

`I=12`,

`F=14`,

`L_lift=2`,

`M_merge=2/3`,

`O=40/3`.

Dolayısıyla

`I-O=-4/3`,

`O/I=10/9>1`.

Bu, bütün nonnegative histogramlar veya yalnız doğru stratum kütleleri üzerinden monotonicity ispatlamaya çalışan bir yaklaşımı çürütür. Actual Collatz source'un erişilebilirlik/affine-parity yapısı zorunludur.

---

## 6. [TAM SONLU DOĞRULAMA] Actual source

Ana `source_defect_round7.py`, source histogramlarını odd başlangıçlardan doğrudan yeniden kurdu; FFT veya floating arithmetic kullanmadı.

### Prescribed Round-5 grid

- `m=2,...,18`,
- `s=1,...,min(8,m-1)`,
- **108** exact geçiş.

Her satırda üç exact identity bağımsız alanlardan karşılaştırıldı:

1. `L=F-I` ile autocorrelation shift formu aynı;
2. `M=F-O` ile weighted category-square formu aynı;
3. `I-O=M-L`.

108/108 PASS.

Bu 108 satırda:

- `L_lift>0`: yalnız **3** durum;
- `L_lift<=0`: **105** durum;
- actual monotonicity ihlali: **0**.

Pozitif-lift durumları:

- `(m,s)=(4,2)`: `L=8/3`, `M=17/3`, `M/L=17/8`;
- `(8,2)`: `L=16/7`, `M=223/15`, `M/L=1561/240`;
- `(10,2)`: `L=40/63`, `M=2804/315`, `M/L=701/50`.

### Post-hoc stres uzatması

İlk theorem/identity kontrollerinden sonra ayrıca:

- `m=10,...,18`, yeni `s=9,10` satırları;
- `m=19,20,21`, `s=1,...,10`

olmak üzere **47** ek exact geçiş çalıştırıldı. Bunlar prescribed grid değildir.

İki yeni pozitif-lift durumu bulundu:

- `(10,9)`: `L=256/21`, `M=40256/15`, `M/L=4403/20`;
- `(11,9)`: `L=6016/105`, `M=11518208/3465`, `M/L=89986/1551`.

Bu iki örnek özellikle önemli: “`s>=3` olduğunda `L_lift<=0`” gibi cazip bir genel işaret leması **yanlıştır**.

Toplam 155 actual-source geçişte monotonicity ihlali görülmedi. Pozitif `L` olan beş satır içinde en küçük `M/L` hâlâ `17/8` ile `(4,2)` idi. Bunlar sonlu tanıdır; uniform `M>=cL` teoremi değildir.

---

## 7. [AYRI UYGULAMA KONTROLÜ]

`independent_defect_check.py`, producer `E/O` transfer kodunu import etmedi. Her base odd başlangıç `h<2^m` için hem `h` hem `h+2^m` lift'ini doğrudan m shortcut adım yürüttü; iki m-step endpoint farkının `3^k` olduğunu kontrol etti ve son shortcut paritesine göre `E/O` kategorilerini doğrudan saydı.

Scope:

- `m=2,...,12`,
- `s<=6`,
- **51** exact durum.

Üç defect identity 51/51 geçti.

Bu aynı sohbet içindeki ikinci implementasyondur; bağımsız ajan denetimi değildir.

---

## 8. Araştırma kararı

### Ne yeni bulundu?

- Source monotonicity farkının exact iki-terimli ayrışması:
  `defect = M_merge - L_lift`.
- `L_lift` için doğrudan arithmetic autocorrelation shift `3^k` formu.
- `M_merge` için exact weighted square-norm formu.
- Böylece Round-5 gözlemi tek somut eşitsizliğe indirildi.

### Ne elendi?

1. “Fine categories ayrı ayrı kontraktiftir” fikri yanlış; actual source'da bile `F>I` örnekleri var.
2. “Positivity + doğru binom masses monotonicity'yi sağlar” yanlış; açık `10/9` nonnegative counterexample var.
3. “Yüksek precision'da lift terminin işareti otomatik nonpositive olur” yanlış; `(10,9)` ve `(11,9)` actual source karşıörnekleri var.

### Ana ispat açısından ne açık?

Asıl yeni lemma artık:

`M_merge >= L_lift`

actual Collatz source için neden doğru olsun?

Bunu kanıtlamak için generic Hilbert normları yetmez; actual source reachability kullanılmalıdır. Uniform `W`, `W_flat`, `D2` ve Collatz hâlâ açıktır.

### Sıradaki en değerli somut adım

`L_lift` ve `M_merge`'i bir önceki source-transfer seviyesinin ortak parity-word / endpoint-pair sayımlarıyla açmak.

Özellikle:

- `L_lift`, aynı k-stratum içindeki `3^k`-ayrılmış endpoint pairlerini sayıyor;
- `M_merge`, komşu k-stratumlardan gelen even/odd son-adım kategorileri arasındaki weighted mismatch normu.

Bir sonraki lemma adayı, her pozitif lift-alias katkısını komşu-k merge mismatch'e **enjeksiyon/charging** ile bağlamak. İlk test pointwise k eşitsizliği değil, toplam-k weighted charging olmalı; mevcut component tabloları slack'in k'lar arasında yeniden dağıldığını gösteriyor.

Bu charging başarısızsa sonraki adım, reachable-source uzayında Krawtchouk singular-mode projection'ını doğrudan `M-L` defectiyle ilişkilendirmektir.
