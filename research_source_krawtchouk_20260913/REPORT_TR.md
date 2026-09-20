# Source Krawtchouk Round 5 — k-stratum gauge, exact singular spectrum ve yeni darboğaz

**Tarih:** 13 Eylül 2026  
**Başlangıç GitHub main:** `434d8fc55544207b35a4c4390600598dd6623d28`  
**Devam dalı / PR:** `research/mixed-gram-round1-20260912` / PR #2  
**Statü:** exact source-transfer operatör teoremi + exact Krawtchouk spektrumu + sonlu gerçek-source tanısı. Uniform `W`, `W_flat`, `D2` ve Collatz açık.

## Basit sonuç

Round 3'te bulunan gerçek source transferindeki `3^k` fazları ilk bakışta k-stratumlarını birbirinden farklı gösteriyordu. Bu turda bu fazların **tam bir k-gauge ile yok edilebildiği** görüldü. Gauge sonrasında source transferi, k-indeksinde iki sabit Pascal/Krawtchouk operatörünün toplamına dönüşüyor.

Binom stratum kütleleri `N_(m,k)=binom(m-1,k-1)` ile normalize edildiğinde operatörün singular spektrumu kapalı formda hesaplanabiliyor. Sabit primitive frekans için squared singular değerler tam olarak

`1 + cos(phi) * (1 - 2 ell/m)`, `ell=0,...,m`.

Dolayısıyla squared operator normu

`1 + |cos(phi)|`.

Bu önceki kaba source normundan daha yapısal ve daha keskin bir sonuçtur. Fakat precision büyürken en kötü primitive frekansta bu değer `2`'ye yaklaşır. Ardışık adımlarda `2`'den elde edilen küçük strict gap'lerin ürünü yalnız pozitif bir sabit kazanç verir; **üstel kazanç vermez**. Bu nedenle yalnız worst-case source operator normunu yinelemek, aradığımız asimptotik `W` üssünü kapatacak mekanizma değildir.

Buna karşılık gerçek source üzerinde güçlü ve henüz kanıtlanmamış bir desen çıktı. Aşağıda tanımlanan binom-normalize primitive enerji için

`Ecal_(m+1,s) <= Ecal_(m,s+1)`

prescribed 108 exact geçişin hiçbirinde ihlal edilmedi. Bu genel operatör normundan çok daha güçlüdür ve generic girişler için doğru değildir. Dolayısıyla sonraki hedef artık nettir: **actual Collatz source'un neden genişleyen Krawtchouk singular modlarına az projekte olduğunu kanıtla veya gerçek bir karşı-aile bul.**

---

## 1. Kurulum

Round 3 notation'ını kullanıyoruz. `P_(m,k,s)(z)` gerçek prefix endpoint histogramı; toplam kütlesi

`N_(m,k)=binom(m-1,k-1)`.

Bir source adımında output precision `s`, input precision `s+1` olsun:

`N=2^(s+1)`, `q=N/2`, `omega=exp(-2 pi i/N)`.

Fix bir odd `a mod q`. `rho_k=3^(-k) mod N` ve tercih edilen lift

`xi_k = rho_k a mod N`

olsun. Tanımla

`X_(k,+)=hat P_(m,k,s+1)(xi_k)`,

`X_(k,-)=hat P_(m,k,s+1)(xi_k+q)`,

`Y_k=hat P_(m+1,k,s)(xi_k mod q)`.

Eksik k-stratumları sıfır kabul edilir.

---

## 2. [KANIT] `3^k` fazlarını kaldıran exact k-gauge

Round-3 `E_c/O_c` Fourier transferine `c=3^k` ve `c=3^(k-1)` koy. Tercih edilen lift `xi_k` seçimi sayesinde

`A_a=(1+omega^a)/2`,  `B_a=(1-omega^a)/2`

k'dan bağımsızdır. Output temsilcisinin hangi lift olduğu yalnız bir unit phase üretir. Tam form:

`Y_k = A_a X_(k,+) + B_a X_(k,-)`
`      + gamma_k [ A_a X_(k-1,+) - B_a X_(k-1,-) ]`,

burada

`gamma_k = omega^(xi_k)`,  `|gamma_k|=1`.

Şimdi `delta_0=1`, `delta_k=gamma_k delta_(k-1)` seç ve

`x_(k,+)=delta_k^(-1) X_(k,+)`,
`x_(k,-)=delta_k^(-1) X_(k,-)`,
`y_k=delta_k^(-1)Y_k`

tanımla. O zaman bütün k-bağımlı fazlar kaybolur:

`y_k = A_a (x_(k,+)+x_(k-1,+))`
`    + B_a (x_(k,-)-x_(k-1,-)).`

Bu exact identity source transferini k-yönünde sabit bir convolution/incident operator haline getirir. Bu sonuç cyclic Fourier karakterlerini Boolean Walsh karakterleriyle eşlemiyor; Krawtchouk yapısı aşağıda **k-stratum/Hamming-weight yönünde** çıkıyor.

---

## 3. [KANIT] Binom-normalize transfer ve Krawtchouk/Jacobi matrisi

Input stratum kütlesi `n_k=binom(m-1,k-1)`, output kütlesi

`n'_k=binom(m,k-1)=n_k+n_(k-1)`.

Normalize et:

`u_(k,+)=x_(k,+)/sqrt(n_k)`,
`u_(k,-)=x_(k,-)/sqrt(n_k)`,
`v_k=y_k/sqrt(n'_k)`.

O zaman

`v_k = A_a [ sqrt(alpha_k) u_(k,+) + sqrt(beta_k) u_(k-1,+) ]`
`    + B_a [ sqrt(alpha_k) u_(k,-) - sqrt(beta_k) u_(k-1,-) ]`,

`alpha_k=(m-k+1)/m`, `beta_k=(k-1)/m`.

`M_+` bu Pascal incidence matrisinin `+`, `M_-` ise alt köşegeni işaret değiştirmiş sürümü olsun. Transfer

`T_a=[A_a M_+, B_a M_-]`.

Doğrudan matris çarpımı

`M_+ M_+^* = I + J_m`,
`M_- M_-^* = I - J_m`

verir. `J_m` yalnız komşu k-katmanlarını bağlayan simetrik Jacobi matrisidir:

`(J_m)_(r,r+1)=sqrt((r+1)(m-r))/m`, `r=0,...,m-1`.

Ayrıca

`|A_a|^2-|B_a|^2=cos(phi)`, `phi=2 pi a/N`.

Dolayısıyla

`T_a T_a^* = I + cos(phi) J_m`.

### Krawtchouk özdeğerleri

Krawtchouk polinomları

`K_ell(r)=sum_h (-1)^h binom(r,h) binom(m-r,ell-h)`

şu elementary recurrence'i sağlar:

`(m-r)K_ell(r+1)+r K_ell(r-1)=(m-2ell)K_ell(r)`.

Normalize layer vektöründe bu tam olarak `J_m` özdeğer denklemi olur. Bu nedenle

`spec(J_m)={1-2ell/m : ell=0,...,m}`.

Sonuç olarak squared singular değerler

`lambda_ell(a)=1+cos(phi)(1-2ell/m)`

ve tam operator normu

`||T_a||^2 = 1+|cos(phi)|`.

Bu Krawtchouk kullanımı, cyclic Fourier katsayılarını Walsh katsayıları sanmak değildir. Krawtchouk burada prefix-weight `k` yönündeki Pascal operatorunu diagonalize eder.

---

## 4. [KANIT] Binom-ağırlıklı primitive source energy bound

Tanımla

`Ecal_(m,s) = sum_k [1/N_(m,k)] sum_(xi odd mod 2^s) |hat P_(m,k,s)(xi)|^2.`

Odd dilation `xi -> 3^(-k)xi` her k için primitive frekansları permüte eder. Bir `a mod 2^s` için iki input lifti birlikte bütün odd input frekanslarını verir. Yukarıdaki operator normunu bütün odd `a`'lar üzerinde uygularsak

`Ecal_(m+1,s) <= rho_s Ecal_(m,s+1)`,

burada exact worst-frequency factor

`rho_s = 1 + cos(pi/2^s)`
`      = 2 cos^2(pi/2^(s+1)) < 2.`

Bu uniform, rigorous bir source-energy inequality'dir.

---

## 5. [KANITLANMIŞ ENGEL] Bu strict gap üstel kazanç üretmiyor

L ardışık precision adımında worst-case factor ürünü

`Prod_(r=0..L-1) rho_(s+r)`
` = 2^L Prod_(n=s+1..s+L) cos^2(pi/2^n)`
` = 2^(-L) [ sin(pi/2^s) / sin(pi/2^(s+L)) ]^2.`

`2^L`'ye oranı

`[ sin(pi/2^s) / (2^L sin(pi/2^(s+L))) ]^2`

ve `L->infinity` limitinde

`[ 2^s sin(pi/2^s) / pi ]^2 > 0`.

Yani her tek adımda `rho_s<2` olsa da fark precision büyüdükçe kapanır. Tek başına bu operator normunu yinelemek, `2^L` baseline'a göre **yalnız sabit çarpan** kazanç sağlar; exponential margin sağlamaz.

Bu bir source-transfer yolunun tamamının imkansızlığı değildir. Yalnız worst-case k/frequency operator normunu her adımda bağımsız uygulayan relaxation'ın engelidir.

---

## 6. [KANIT] En kötü singular modun yapısı

`cos(phi)>0` için en büyük eigenvalue `J_m`'in `ell=0` modundadır. Sol eigenvector katmanlarda

`v_0(r) proportional sqrt(binomial(m,r))`.

Elementary binomial identity ile

`M_-^* v_0 = 0`,

`M_+^* v_0` ise input `ell=0` Krawtchouk modudur. Dolayısıyla en kötü genişleyen source modu:

- yalnız `+` lift kanalında;
- gauge sonrası `X_(k,+)/N_(m,k)` k boyunca sabit olan degree-0 moddur.

`cos(phi)<0` tarafında simetrik olarak yüksek Krawtchouk derece / `-` lift modu extremaldir.

Bu, sonraki hedefi soyut bir “daha iyi norm bul” sorusundan çıkarıp şuna indirger:

> Actual Collatz source, W-kritik bandda bu extremal Krawtchouk/lift modlarına ne kadar projekte olabilir?

Bu projection küçükse generic operator normu gereksiz derecede kötümserdir.

---

## 7. [TAM / SAYISAL SONLU KONTROL]

`source_krawtchouk_round5.py` standard library ile çalıştırıldı.

### Fourier gauge formülü

Doğrudan source histogramı + açık kompleks DFT ile

- `m<=7`, `s<=4`, bütün geçerli k ve odd a;
- **429** coefficient karşılaştırması;
- maksimum mutlak hata `8.659170228218011e-14`.

Bu floating check yalnız phase/index yönünü sınar; ispat §2'dir.

### Krawtchouk recurrence

`m<=30` için bütün `(m,ell,r)` üzerinde **10.415** integer recurrence kontrolü; ihlal yok.

### Gerçek source'da daha güçlü desen

Prescribed exact grid:

- `m=2,...,18`,
- `s=1,...,min(8,m-1)`,
- **108** source geçişi.

Bütün `Ecal` değerleri exact integer/Fraction hesaplandı. Gözlenen:

`Ecal_(m+1,s) / Ecal_(m,s+1) <= 1`

108/108 durumda; `>1` örnek **0**, equality yalnız `(m,s)=(2,1)`.

Bu **teorem değildir**. Generic operator normu `1+|cos(phi)|>1` olabildiği için bu güçlenme yalnız positivity veya binom mass bilgisinden otomatik çıkmaz. Gerçek prefix source'un reachable altuzayına özgü ek yapı gerekiyorsa, işte bulunması gereken yapı budur.

---

## 8. Araştırma kararı

### Yeni bulunan

1. Exact `3^k` source fazları k-gauge ile tamamen kaldırıldı.
2. Binom-normalize source transfer Krawtchouk/Jacobi operatoruna tam indirgendı.
3. Tek-frekans singular spektrum ve norm kapalı formda bulundu.
4. Worst-case norm iteration'ın exponential kazanç veremeyeceği exact trigonometrik ürünle kanıtlandı.
5. Gerçek source'da generic bound'dan çok daha güçlü bir monotonicity adayı 108 exact durumda hayatta kaldı.

### Elenen

“Her adımda `rho_s<2`, o halde birikince üstel kazanç gelir” fikri yanlıştır. Strict gap precision ile sıfıra gider ve ürün yalnız sabit-factor avantaj verir.

### Ana ispatSında açız

- `Ecal_(m+1,s)<=Ecal_(m,s+1)` gerçek-source monotonicity'si genel mi?
- Değilse kritik bandda yeterli quantitative projection gap var mı?
- Bu source projection bilgisi Round-4 fixed-k phase Gram ve Shift-Haar `Delta W_ell` ile nasıl birleştirilir?
- `W_flat`, `W`, `D2` asimptotik exponents hâlâ açık.

### Sıradaki en değerli somut adım

Yeni ana lemma adayı:

> Actual source'un binom-normalize, gauge edilmiş Fourier vektörünün extremal `ell=0` / `ell=m` Krawtchouk singular modlarına projeksiyon'ını kritik `(m,k,s)` bandında quantitative olarak sınırla.

İlk saldırı iki parçalı olmalı:

1. `Ecal` monotonicity'yi pair-count / conditional-expectation dilinde ispatlamaya çalış;
