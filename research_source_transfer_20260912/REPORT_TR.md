# Source transfer Round 3 — gerçek prefix histogramı için exact lift operatörü

Tarih: 12 Eylül 2026  
Kanonik başlangıç: `434d8fc55544207b35a4c4390600598dd6623d28`  
Devam dalı: `research/mixed-gram-round1-20260912`  
Durum: **exact kaynak rekürsiyonu + exact ilk signed-katman mixed-channel özdeşliği; uniform W/D2 ve Collatz açık.**

## Basit sonuç

Shift-Haar turunda kalan ilk somut hedef `Delta W_1 = q^(-2) sum_(k,s) H_s Gamma_(k,s,1)` idi. Bu turda `Gamma_1`'in source tarafının da önceki tail `N_+` yapısıyla aynı tür bir reflection-even mixed kanala sahip olduğu görüldü. Daha önemlisi, gerçek prefix endpoint histogramı `m -> m+1` geçişinde **iki komşu prefix-weight katmanından gelen exact lineer bir lift transferi** sağlıyor.

Bu, source histogramını keyfi bir pozitif dizi gibi ele almak zorunda olmadığımızı gösteriyor. Source da 2-adik lift ağacında faz-korumalı bir transfer operatörüne sahip. Henüz bu operatör için gerekli büyüyen-aile norm bound'ı kanıtlanmadı. Bu tur W exponentini kapatmıyor.

## 1. Source histogramı

`P_(m,k,s)(z)`: `1<=h<2^m`, `h` tek, ilk `m` shortcut adımında tam `k` tek parite ve `H^m(h)=z (mod 2^s)` olan başlangıçların sayısıdır. Toplam kütle `binom(m-1,k-1)`.

## 2. [KANIT] `m -> m+1` exact source transferi

Bir alt başlangıç `h<2^m` ile üst lift'i `h+2^m` ilk `m` pariteyi paylaşır. Ortak prefix weight `k` ise affine shortcut formülü

`H^m(h+2^m)=H^m(h)+3^k`

verir. `3^k` tek olduğundan iki endpoint'in pariteleri zıttır. Son shortcut adımında base weight `k` çift endpoint seçimiyle yeni weight `k`'ya, base weight `k-1` tek endpoint seçimiyle yeni weight `k`'ya gider.

`N=2^(s+1)`, `q=2^s`, `c` tek ve `r=3^(-1) mod N` olsun. Uzunluğu `N` olan dizi `P` için

`(E_c P)(z)=P(2z)+P(2z-c)`,

`(O_c P)(z)=P(r(2z-1))+P(r(2z-1)-c)`.

Bütün giriş indeksleri `mod N`. O zaman tam olarak

`P_(m+1,k,s) = E_(3^k) P_(m,k,s+1) + O_(3^(k-1)) P_(m,k-1,s+1).`

Kütle düzeyinde bu Pascal özdeşliğine iner.

## 3. [KANIT] Fourier'de exact 2x2 lift matrisi

`omega=exp(-2 pi i/N)` ve unnormalized Fourier ile, `a mod q` için:

`hat(E_c P)(a) = 1/2[(1+omega^(ac))hat P(a) +(1-omega^(ac))hat P(a+q)]`.

`hat(O_c P)(a) = omega^a/2[(1+omega^(3ac))hat P(3a) +(omega^(3ac)-1)hat P(3a+q)]`.

Frekanslar `mod N`. Bu source tarafında hangi lift fazının korunması gerektiğini açıkça gösterir; burada mutlak değer almak Round 1'deki faz-kör kaybı tekrar üretir.

## 4. [KANIT] İlk signed shift-Haar katmanı iki mixed `+` kanalın iç çarpımıdır

Uzunluğu `2q` olan gerçek dizi `x` için `x0(u)=x(2u)`, `x1(u)=x(2u+1)`,

`B_x(b)=sum_u x0(u)x1(u+b)`, `h0=q/2`, `Z_x(b)=B_x(b)-B_x(b+h0)`.

Reflection `(RZ)(h)=Z(-h-1)` ve `Z_(x,+)=(Z_x+RZ_x)/2` olsun. Autocorrelation sibling farkı `D_x(d)=C_x(d)-C_x(d+q)` için

`D_x(2h+1)=Z_x(h)+Z_x(-h-1)=2Z_(x,+)(h)`.

Dolayısıyla iki gerçek dizi `x,y` için tam olarak

`Gamma_1(x,y)=4 <Z_(x,+),Z_(y,+)>_half`,

`S_1(x)=4||Z_(x,+)||_half^2`, `T_1(y)=4||Z_(y,+)||_half^2`.

Tail filtresinde bu önceki `T_1=4N_+` sonucudur; source histogramında aynı yapının source karşılığı oluşur. Bu nedenle

`Delta W_1 = 4 q^(-2) sum_(k,s) H_s <Z_(P,+),Z_(F,+)>`.

Tek global Cauchy:

`|Delta W_1| <= 4q^(-2) sqrt[(sum H_s||Z_(P,+)||^2)(sum H_s||Z_(F,+)||^2)]`.

Tail ikinci çarpan eski `N_+` bütçesidir. Yeni açık problem source reflection-even mixed enerjisinin büyüyen kritik ailede yeterli bound'ıdır.

## 5. [TAM SONLU DOĞRULAMA]

`source_transfer_round3.py` doğrudan shortcut enumerasyonu yaptı:

- `m=1..10`, ilgili `k`, `s<=6`: **360** source-transfer eşitliği, 0 ihlal;
- arbitrary integer diziler: **250** first-level mixed-plus identity, 0 ihlal;
- Fourier formülü: direct complex DFT ile **2480 katsayı** kontrolü, maksimum fark `8.79e-13` (yalnız normalizasyon/yön kontrolü; ispat değil).

Gerçek alt ajan çalıştırılmadı; bunlar aynı asistan oturumundaki hesaplar ve cebirsel ispatlardır.

## 6. Ne sağladı, ne sağlamadı?

Yeni yapı: gerçek prefix source exact `E/O` lift transferiyle taşınabilir; source ve tail ilk signed Haar katmanı aynı reflection-even mixed kanal diline girdi; `Delta W_1` için source/tail mixed enerjilerini eşleyen aggregate hedef oluştu.

Açık kalan: source mixed-energy exponenti, signed toplamda ek cancellation, `ell=2` coupled operator, `W_flat`, uniform W/D2 ve Collatz.

## 7. Sıradaki ayırt edici hedef

`N^P_+(m,k,s)=||Z_(P,k,s,+)||^2` için kritik bandda aggregate `sum_(k,s) H_s N^P_+` büyümesini source transfer operatöründen kontrol et veya bu hedefi çürüten gerçek büyüyen aile üret. Tail karşılığı mevcut cross-term recurrence ile taşınabilir. Yetmezse `ell=1` hattını büyütmek yerine doğrudan `ell=1,2` coupled operator'a geçmek gerekir.

**Ne yeni bulundu?** Gerçek prefix source histogramının exact `m->m+1` lift transferi ve ilk signed katmanın source/tail reflection-even mixed kanal iç çarpımı olduğu.

**Ne elendi?** Source'u tamamen yapısız histogram olarak ele alma zorunluluğu; fakat otomatik contraction henüz gösterilmedi.

**Ana ispatta ne açık?** Source mixed-energy büyümesi, tail residual bütçesi, W_flat ve nihai W bound.

**Sıradaki somut adım?** `sum H_s N^P_+` için source transferinden exponent bound çıkarmaya çalışmak; ilk ayırt edici başarısızlıkta gerçek karşı-aile kaydetmek.
