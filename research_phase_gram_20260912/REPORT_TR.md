# Faz-duyarlı 3×3 Gram bloğu: gerçek bir iyileştirme, fakat kapanış için hâlâ eksik faz

**Tarih:** 12 Eylül 2026  
**Kaynak main:** `434d8fc55544207b35a4c4390600598dd6623d28`  
**Önceki tur:** `research_mixed_gram_20260912` / PR #2  
**Statü:** yeni yerel teoremler + tam sonlu kontroller + bir kapanış karşıörneği. Uniform `W`, `D2` ve Collatz açık.

## Basit sonuç

Önceki turda `G_d` mixed-overlap hiyerarşisini kurduk ama fazı mutlak değere çevirdiğimiz için kritik gridde bilinen `M2^2/2` sınırını yenemedik. Bu turda fazın bir kısmını gerçekten koruyan ilk küçük operatörü kurdum.

Ana nesne 3×3 bir **faz Gram matrisi**. Bu matris, üç komşu tail kanalının iki Fourier lift'i arasındaki güç farklarını birlikte taşıyor. Pozitif yarı-belirli (PSD) olduğu için 2×2 Cauchy yerine 3×3 Schur-complement sınırı kullanılabiliyor.

Bu yeni sınır:

- önceki faz-kör `G1` sınırından **teorem olarak hiçbir zaman daha kötü değil**;
- önceden sabitlenen kritik sonlu kutudaki **543/543** durumda daha sıkı çıktı;
- `t=60,j=38` ailesinde eski bound'un yaklaşık `%51`–`%77` seviyesine indi;
- fakat doğrudan `M4=G0` kapanışını çözmüyor, çünkü Gram'ın bir sonraki ölçekteki diyagonali yeni imaginary/two-step faz bilgisi istiyor.

Bu kapanış eksikliği yalnız sezgi değil: aynı mevcut büyüklükleri ve aynı real-edge Gram verisini taşıyan iki exact kompleks örnek, bir sonraki diyagonal için sırasıyla

`6 - 4 sqrt(2)` ve `6 + 4 sqrt(2)`

veriyor. Dolayısıyla yalnız real-edge Gram ile tam recurrence mümkün değil.

Tam fazı kaybetmemek için daha büyük bir quartic-character recurrence de kuruldu. O recurrence **tam olarak kapanıyor** ve 272 gerçek filtre durumunda exact `M4` ile eşleşti. Ancak naif memo state sayısı hızla büyüyor: `s=12` için 88.198 state, doğrudan residue sayısı ise 4.096. Yani tam fazı ham biçimde taşımak şu haliyle hesaplama çözümü değil.

Son olarak `W_flat` shell ağırlıklarıyla PSD Gram matrislerini toplama leması uygulandı. Bütün shell'leri veya aynı conductor'ları birlikte toplamak fayda vermedi; fakat **aynı `j` (dolayısıyla aynı `k` source stratum) içinde conductor'ları toplamak** r=10,12,14 gerçek panellerinin üçünde de pointwise 2×2 Cauchy toplamından daha sıkı çıktı. Bu henüz `W` bound'u değildir, fakat source-ağırlıklı faz bilgisini hangi eksende toplamanın doğal olduğunu gösteren ilk pozitif işarettir.

---

# 1. [KANIT] Lift-power farklarından faz Gram matrisi

Alt precision `s>=1`, `N=2^s` olsun. Tail filtrelerinin Fourier katsayılarını

`phi_l(a) = hat F_(s;t,l)(a)`

ile gösterelim. Bir üst precision `(s+1,t+1)` için aynı alt odd frekans `a`'nın iki primitive lift'i `xi_+=a`, `xi_-=a+N` olsun.

Kanal ofseti `d>=0` için parent katsayısını ortak başlangıç frekansından odd dilation ile örnekle:

`P_d^±(a) = | hat F_(s+1;t+1,j-d)( 3^{-d} xi_± ) |^2`.

Tüm tersler ilgili power-of-two modülde alınır. Şimdi gerçek sayı

`x_d(a) = [P_d^+(a)-P_d^-(a)]/4`

tanımlansın.

Önceki iki-lift formu bu farkın, komşu tail kanalları arasındaki gerçek edge coherence olduğunu söyler. Ama burada herhangi bir square-root phase seçmek gerekmiyor; `x_d` doğrudan iki gerçek güç farkıyla tanımlandı.

Her `e,f>=0` için

`K_ef(t,j,s) = sum_(a odd mod N) x_e(a) x_f(a)`

olsun. O zaman her sonlu kanal bloğu için `K` bir Gram matrisidir:

`K = sum_a x(a) x(a)^T >= 0`.

Dolayısıyla bütün principal minor'lar nonnegative ve özellikle

`|K_01| <= sqrt(K_00 K_11)`.

Odd dilation yalnız frekansları permüte ettiği ve lift çiftinin yönünü en fazla işaret değiştirdiği için diyagonaller

`K_dd(t,j,s) = K_00(t,j-d,s)`

olur.

Bu diyagonal önceki cross-term notasyonuyla doğrudan `N_+`'dır. Parent cross parametreleri `(t+1,j,s+1)` ise

`K_00(t,j,s) = 2^(s-1) N_+`,

ve

`G_1(t,j,s) = 2^(s-1) N_B`.

Dolayısıyla

`K_00/G_1 = N_+/N_B`

(tanımlı olduğu durumda). Yeni Gram bloğu tam olarak önceki reflection-even bilgisinin komşu `j` kanalları arasındaki genişlemesidir.

---

# 2. [KANIT] Exact `G_d` lift kimliği ve `K_0d`

Önceki turdaki

`G_d(t,j,s) = sum_(a odd) |phi_j(a)|^2 |phi_(j-d)(3^{-d}a)|^2`

tanımını koruyalım. İki lift'in güçlerini

`P_d^± = p_d+p_(d+1) ± 2 x_d`

şeklinde yazınca, `d>=1` için doğrudan

`G_d(t+1,j,s+1)`
` = 2[ G_d(t,j,s) + G_(d+1)(t,j,s)`
`      + G_(d-1)(t,j-1,s) + G_d(t,j-1,s) ]`
`   + 8 K_0d(t,j,s)`

elde edilir.

Özellikle `d=1`:

`G_1(parent) = BASE + 8 K_01`,

`BASE = 2[G_1(j)+G_2(j)+G_0(j-1)+G_1(j-1)]`.

`d=0` için

`G_0(parent) = 2G_0(j)+2G_0(j-1)+4G_1(j)+8K_00(j)`.

Son formül neden asıl darboğazın sürdüğünü de gösteriyor: `M4=G0` için gereken yeni faz bilgisi bir **diyagonal** `K00`. PSD tek başına diyagonale üst sınır üretmez; yalnız `0<=K00<=G1` geri gelir. Bu nedenle yeni Gram leması `G1` propagation'ını güçlendiriyor fakat tek başına `G0` kapanışını çözmüyor.

---

# 3. [KANIT] 3×3 Schur sınırı

Üç kanal bloğunu

```
K = [[a, x, z],
     [x, b, y],
     [z, y, c]] >= 0
```

şeklinde yazalım. Burada

- `a=K00(t,j,s)`,
- `b=K00(t,j-1,s)`,
- `c=K00(t,j-2,s)`,
- `x=K01(t,j,s)`,
- `z=K02(t,j,s)`,
- `y=K01(t,j-1,s)`.

Eğer `c>0` ise Schur complement exact olarak

`(x - zy/c)^2 <= (a-z^2/c)(b-y^2/c)`

verir. Dolayısıyla

`x <= zy/c + sqrt[(a-z^2/c)(b-y^2/c)] =: U_Schur`.

`c=0` olduğunda PSD `z=y=0` zorlar ve 2×2 Cauchy'ye dönülür.

Bu, yalnız `a,b` bilgisini kullanan

`x <= sqrt(ab)`

sınırından daha sıkı veya eşittir. Ayrıca

`a<=G1(t,j,s)`, `b<=G1(t,j-1,s)`

olduğu için

`sqrt(ab) <= [G1(j)+G1(j-1)]/2`.

Böylece `d=1` için yeni phase bound, önceki Round-1 phase-blind bound'u **genel olarak domine eder**:

`U_3x3(G1 parent) <= U_2x2 <= U_phase-blind`.

Bu sıralama sonlu deneyden çıkarılmadı; PSD ve AM-GM'den kanıtlandı.

---

# 4. [TAM SONLU KONTROL] Gerçek filtrelerde Gram ve Schur

`phase_gram_round2.py` şu exact integer/Fraction kontrollerini yaptı:

- `t=5..24`, bütün `j>=2`, `s=2..min(t,8)` üzerinde **1.862** 3×3 Gram durumu;
- bütün 2×2 principal minor'lar ve 3×3 determinant nonnegative;
- ihlal: **0**;
- determinantı sıfır olan durum: **635**;
- Schur upper'ın exact tight olduğu durum: **349**.

Ayrı bir direct-DFT uygulaması ana scripti import etmeden parent Fourier lift güçlerini açık `O(N^2)` toplamlarla kurdu. `t=5..10`, `s<=5`, bütün uygun j için **156** durumda direct Gram ile integer residual Gram karşılaştırıldı:

- durum: PASS;
- max relative hata: `1.5401013797600172e-12`;
- max absolute hata: `2.3283064365386963e-08`.

Bu ikinci kontrol kayan noktalı bir normalization/implementation check'tir; ispat değildir. İlk koşu `9/2` biçimli Fraction string'ini doğrudan `float()` çevirdiği için `ValueError` ile durdu. Kod düzeltildi; yalnız başarılı ikinci koşu kontrol sonucu olarak kullanıldı.

---

# 5. [SONLU AYIRT EDİCİ TEST] Kritik kutuda gerçek kazanç

Round-1 ile aynı kritik oran kullanıldı:

- `t=8..30`,
- `j=round(t/log2(3)) +/-1`, interior'a kırpılmış,
- `s=3..min(t,10)`,
- toplam **543** durum.

Sonuç:

- 3×3 bound eski phase-blind bound'dan sıkı: **543/543**;
- 3×3 bound 2×2 `sqrt(K00 K11)` bound'dan sıkı: **530/543**.

Bu ikinci sayı sonlu tanıdır; genel theorem yalnız `U_3x3<=U_2x2<=U_old` der.

En büyük relatif kazanç örneklerinden biri `(t,j,s)=(26,15,3)`:

- gerçek `G1 = 91213299358218935463936`,
- eski phase-blind upper `=590023164170276281761792`,
- 3×3 upper **gerçeğe tam eşit**,
- `U_3x3/U_old ~= 0.15459274296`.

Kutu içindeki en zayıf relatif kazançta bile

`U_3x3/U_old ~= 0.88959267240`.

Bunlar `W` oranları değildir; tail mixed-overlap propagation bound'larıdır.

---

# 6. [SONLU TANI] Sabit `(t,j)=(60,38)` ailesi

| s | U_3x3 / eski bound | U_3x3 / gerçek G1 |
|---:|---:|---:|
| 4 | 0.51428 | 1.01625 |
| 6 | 0.59185 | 1.20344 |
| 8 | 0.77638 | 1.23147 |
| 10 | 0.76632 | 1.13773 |
| 12 | 0.77273 | 1.08937 |

Yani daha önce concentration'ın büyüdüğü gerçek ailede dahi 3×3 faz bloğu eski bound'un ciddi bir kısmını geri alıyor. Bu sonlu tablo asimptotik contraction theorem değildir.

---

# 7. [KANIT] Source/W_flat ağırlıklı Gram toplamı

Her shell/stratum için ayrı bir PSD `K_b` olsun ve `w_b>=0` herhangi nonnegative ağırlıklar olsun. O zaman

`Kbar = sum_b w_b K_b >= 0`.

Dolayısıyla aynı Schur sınırı **ağırlıklı toplamdan sonra** da geçerlidir. Bu önemli; önce her shell'de mutlak değer alıp sonra toplamak zorunlu değildir.

Mevcut W ayrışımında

`flat_(k,s) = h_s R_(k,s-1) D(t,r-k,s)/q^2`

nonnegative ve

`W_flat = sum_(k,s) flat_(k,s)`.

Bu nedenle özellikle sabit `k` (eşdeğer sabit `j=r-k`) içinde conductor `s`'leri

`w_s = flat_(k,s)`

ile Gram matrisinden önce toplamak rigoröz olarak mümkündür. Bu işlem `W`'yi otomatik sınırlandırmaz: `K01`, shell alignment `A_(k,s)` değildir. Fakat **aynı source-shell ölçüsü altında faz overlap'ını Cauchy'den önce birleştirmenin** doğru yolu budur.

## Küçük gerçek-source panelleri

Eligible `s>=2,j>=2` satırlar kullanıldı. Baseline, her satırda ayrı 2×2 Cauchy uygulayıp `flat` ile toplamaktır. Sonra 3×3 Gram'lar sabit j/k içinde önce toplandı, Schur bound en son uygulandı.

| r | actual weighted H1 | pointwise 2×2 | fixed-k/j grouped 3×3 | grouped / pointwise |
|---:|---:|---:|---:|---:|
| 10 | 41.625 | 46.1103 | 43.1213 | **0.93518** |
| 12 | 913.3125 | 12449.0503 | 12145.7560 | **0.97564** |
| 14 | 111358.3359 | 314988.6345 | 284394.1285 | **0.90287** |

Üç panelde de aynı-k stratum gruplaması pointwise 2×2 toplamından daha iyi çıktı. Buna karşılık conductor'a göre gruplamak veya her şeyi tek global Gram'a koymak bu panellerde pointwise baseline'ı yenemedi. Bu, "her şeyi topla sonra Cauchy" demenin doğru olmadığına dair yararlı negatif kontroldür.

**Statü:** sonlu tanı. r=10,12,14 bir uniform theorem değildir. Ama kaynak ağırlıklarıyla faz bilgisini koruyacaksak doğal toplama ekseni olarak `V_k=sum_s V_(k,s)` ile uyumlu sabit-k grubunu işaret ediyor.

---

# 8. [KANITLANMIŞ ENGEL] Real-edge Gram tek başına bir sonraki ölçekte kapanmıyor

Bir sonraki ölçekteki edge diyagonalini düşünelim. Uygun gauge'da mevcut üç kompleks kanal `u0,u1,u2` olsun. Current real edges

`x0=Re(u1 conjugate(u0))`,
`x1=Re(u2 conjugate(u1))`

ile Gram'ın ilgili kısmı belirlenir.

Bir sonraki liftte future phase rotation'ın karesi `lambda^2=i` olabilen bir durum vardır. Parent edge diagonaline giren tek-frekans katkısı

`|P|^2+|Q|^2+2 Re(lambda^2 P Q)`

şeklindedir; burada

`P=u1 conjugate(u0)+u2 conjugate(u1)`,
`Q=|u1|^2+u2 conjugate(u0)`.

Şimdi iki veri seti al:

`A: (u0,u1,u2)=(1, exp(i*pi/4), i)`

ve kompleks eşleniği

`B: (1, exp(-i*pi/4), -i)`.

İkisinde de:

- bütün magnitudes `(1,1,1)`,
- current real edges `(sqrt(2)/2, sqrt(2)/2)`.

Yani real-edge Gram ve güç bilgisi aynıdır. Ama `lambda^2=i` için next diagonal:

`A -> 6-4 sqrt(2)`,

`B -> 6+4 sqrt(2)`.

Dolayısıyla **real-edge Gram + magnitudes tek başına kapalı bir scale state değildir.** Imaginary edge orientation veya eşdeğer complex phase bilgisi gerçekten zorunludur.

Bu, actual Collatz filtresinin bu iki toy amplitude'ı bire bir gerçekleştirdiği iddiası değildir. Genel operatör kapanışına karşı exact cebirsel bir karşıörnektir.

---

# 9. [KANIT] Tam fazı taşıyan quartic-character recurrence

Real Gram'ın neden kapanmadığını gördükten sonra fazı hiç atmayan bir state de kuruldu.

Precision `n`, modulus `N=2^n` için

`Phi_(n;t,l)(a) = hat F_(n;t,l)(a)`

olsun. Dört factor için channel offsets `d_i`, signs `eps_i in {+1,-1}` ve character twist `C` tanımla:

`Q_n(C; d,eps)`
` = sum_(xi odd mod N) exp(2pi i C xi/N)`
`   prod_(i=1..4) Phi_(n;t,j-d_i)( eps_i 3^{-d_i} xi )`.

Gerçek filtre nedeniyle conjugate factor `eps=-1` ile temsil edilebilir. Başlangıç dördüncü moment tam olarak

`M4(t,j,n)=Q_n(0; d=(0,0,0,0), eps=(+,+,-,-))`.

`n>=2` için `q=N/2`, `r=3^{-1} mod q`, `c=4r-1` al. Bir subset `S` içindeki factor'lar odd lift branch'ini seçsin. Her seçilen factor'ın offset'i bir artar. `mu_i=eps_i 3^{-d_i} mod N` olsun.

İki parent frequency lift'i toplandığında terim ancak

`C + |S| = 0 mod 2`

ise hayatta kalır. Hayatta kalan child character

`C' = [ C + c sum_(i in S) mu_i ] / 2 mod q`

ve child offsets

`d_i' = d_i + 1_(i in S)`

olur. Dolayısıyla exact recurrence:

`Q_n(C;d,eps)`
` = 2 sum_(S: C+|S| even) Q_(n-1)(C'; d',eps)`.

Taban `n=1`:

`Q_1 = (-1)^C prod_i [binom(t-1,j-d_i)-binom(t-1,j-d_i-1)]`.

Bu recurrence hiçbir Cauchy veya phase drop kullanmıyor; tam quartic phase bilgisini koruyor.

`phase_gram_round2.py`, `t=2..9`, bütün j, `s<=6` için **272** `M4` durumunda bu recurrence'ı repository exact moment hesabıyla karşılaştırdı; hepsi tam eşleşti.

---

# 10. [NEGATİF HESAP SONUCU] Tam faz recurrence şu haliyle hesap avantajı değil

Naif memo state `(C;d_i,eps_i)` kullanıldığında, sabit bir root `M4` hesabı için gözlenen state sayıları:

| s | phase state | doğrudan residue 2^s |
|---:|---:|---:|
| 4 | 120 | 16 |
| 6 | 1.116 | 64 |
| 8 | 6.180 | 256 |
| 10 | 25.430 | 1.024 |
| 12 | 88.198 | 4.096 |

Bu tablo bir asimptotik alt sınır değildir; daha iyi simetri quotient'ları bulunabilir. Fakat **naif "fazı tamamen sakla" çözümü daha s=12'de doğrudan residue enumeration'dan çok daha büyük state uzayı üretmektedir.** Dolayısıyla bu state'i olduğu gibi büyütmek araştırma hedefi olmayacak.

---

# 11. Araştırma kararı

Bu turda iki uç arasında gerçek bir ayrım oluştu:

1. **Fazı tamamen atmak:** Round-1'de kanıtlandı; scalar/truncated hierarchy mevcut trivial bound'u yenmiyor.
2. **Fazın tamamını taşımak:** Bu turda exact recurrence kuruldu; ama naif state uzayı pratik olarak fazla büyük.
3. **Orta yol — 3×3 faz Gram:** Bu turdaki pozitif sonuç. `G1` bound'unu rigoröz biçimde güçlendiriyor ve aynı source stratum içinde `W_flat` ağırlıklı gruplamada finite gerçek kazanç gösteriyor; fakat bir sonraki Gram diyagonaline geçmek için imaginary/two-step phase eksik.

Dolayısıyla sıradaki en değerli soru artık çok dar:

> **Tam quartic-character state'in hangi küçük quotient'u, 3×3 real Gram'a eksik olan imaginary/two-step faz bilgisini eklerken state uzayını patlatmadan kapanabilir?**

İlk aday, bütün character `C`'leri değil yalnız Gram geçişinde görünen **iki quadrature (Re/Im) edge coherence + bir two-step coherence** taşımaktır. Bu aday önce cebirsel kapanış testine sokulmalı; kapanmıyorsa daha büyük tarama yapılmamalıdır.

Source tarafında ise ayrı ama bağlantılı hedef:

> Aynı `k` stratumunda `flat_(k,s)` ağırlıklarıyla conductor'ları toplamadan önce phase Gram'ı koruyan bir inequality, shell alignment `A_(k,s)` veya doğrudan `V_k` için gerçekten kullanılabilir mi?

Bu iki bridge kurulmadan `W` üssünde ilerleme iddia edilmiyor.

---

# 12. Dört kısa cevap

**Ne yeni bulundu?**  
PSD 3×3 phase Gram ve Schur bound; phase-blind `G1` bound'unu genel olarak domine ediyor. Tam faz quartic-character recurrence da exact olarak kapandı.

**Ne elendi?**  
Real-edge Gram'ın tek başına scale closure yaptığı fikir exact `6±4sqrt(2)` karşıörneğiyle elendi. Tam fazı naif state olarak taşımak da finite state-count açısından kötü çıktı.

**Ana ispat açısından ne açık?**  
`W`, `W_flat` büyümesi, source/filter alignment ve `D2` asimptotik bound'ları hâlâ açık; Collatz kanıtlanmadı.

**Sıradaki somut adım?**  
`Re/Im edge + two-step coherence` minimal complex Gram state'inin bir scale altında gerçekten kapanıp kapanmadığını sembolik olarak test etmek; paralelde aynı-k `W_flat` weighted Gram'ın `V_k` ile exact bridge'ini aramak.
