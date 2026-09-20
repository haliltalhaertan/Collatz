# Phase Quotient Round 6 — tam faz recurrence için exact quotient ve sub-enumeration state bound

**Tarih:** 13 Eylül 2026  
**Kanonik main:** `434d8fc55544207b35a4c4390600598dd6623d28`  
**Araştırma dalı:** `research/mixed-gram-round1-20260912` / PR #2  
**Statü:** **yeni exact simetriler + exact state-count teoremi + tam sonlu kontroller. Uniform W, D2 ve Collatz açık.**

**Sıralama notu:** Çalışma sırasında aynı PR dalına bağımsız bir source Krawtchouk/Jacobi çalışması önce entegre edilerek Round 5 oldu. Bu phase-quotient turu ilk hazırlıkta çalışma etiketi olarak Round 5 diye adlandırılmıştı; proje sıralamasında **Round 6** olarak yeniden etiketlendi. Matematiksel içerik bu yeniden numaralandırma nedeniyle değişmedi.

## Basit sonuç

Round 4'te tam fazı koruyan quartic-character recurrence kurulmuş, fakat naif memo state sayısı s=12'de 88.198'e çıkarak doğrudan 4.096 residue enumerasyonundan kötü görünmüştü. Bu tur bu finite gözlemin asimptotik yorumunu düzeltiyor.

İki sonuç var:

1. Planlanan "yakın komşu kompleks coherence + tek iki-adım coherence" tipi **sabit bant genişlikli lineer state**, generic lift cebriyle exact kapanmıyor. Bir separation-r coherence bir sonraki liftte separation r+1 terimi üretir. Actual tail ailesine özgü ek bir özdeşlik bunu değiştirebilir; böyle bir özdeşlik bu turda bulunmadı.

2. Buna karşılık tam quartic-character recurrence'ın kendisi düşündüğümüzden daha düzenli. Üç exact simetriyle quotient edilebiliyor. Daha önemlisi, quotient kullanılmasa bile kökten derinlik d'deki state sayısı

`N_d <= min(8^d, binom(d+2,2)^2 * 2^(s-d))`

ile sınırlı. Derinlikler üzerinde toplayınca

`sum_d N_d = O(s^4 * 2^(3s/4))`.

Dolayısıyla bir tek tail primitive dördüncü momentini tam fazı koruyarak hesaplamak, state sayısı bakımından doğrudan `2^s` residue enumerasyonundan **asimptotik olarak daha küçük üstel üsse** sahiptir. Bu bir hesaplama teoremidir; tail momentin küçük olduğunu, W'nin bounded olduğunu veya Collatz'ı kanıtlamaz.

Round 4'ün "ham tam-faz state'i şu finite aralıkta hesap avantajı sağlamıyor" gözlemi hâlâ doğrudur. Yanlış olacak genişletme, bundan "tam faz recurrence asimptotik olarak da 2^s enumerasyondan iyi olamaz" sonucunu çıkarmaktır. Bu tur o genişletmeyi reddediyor.

---

## 1. Quartic-character state

Round 4'teki state'i koruyoruz. `N=2^n` ve primitive odd `xi mod N` için

`Q_(t,j,n)(C; P)`

şu toplamı temsil eder:

`sum_(xi odd mod 2^n) exp(2 pi i C xi / 2^n) * prod_i phi_(j-d_i)(eps_i 3^(-d_i) xi)`.

Burada `P={(d_i,eps_i)}_(i=1..4)`, `eps_i in {+1,-1}`; M4 kökü

`P0={(0,+),(0,+),(0,-),(0,-)}`, `C=0`.

Exact recurrence'te her adım dört faktörden bir alt kümesini `d_i -> d_i+1` yapar. Primitive parity şartı nedeniyle 16 maskenin tam 8'i geçerlidir. Faz karakteri de Round 4'te verilen

`C' = [C + c * sum_(i in mask) eps_i 3^(-d_i)] / 2 mod 2^(n-1)`

kuralıyla taşınır (`c=4*3^(-1)-1` ilgili modülde).

---

## 2. [KANIT] Üç exact quotient simetrisi

### A. Ortak kanal-ofset kaydırması

Her `h <= min_i d_i` için

`Q(t,j,n,C; {(d_i,eps_i)})`
` = Q(t,j-h,n, 3^h C; {(d_i-h,eps_i)})`.

İspat: primitive frekans toplamında `xi=3^h eta` değişken dönüşümü yapılır. 3 tek olduğundan odd frekansları permüte eder; channel indisi

`j-d_i = (j-h)-(d_i-h)`

olarak korunur ve karakter `C -> 3^h C` olur.

Bu nedenle uygulamada her state `min d_i=0` olacak şekilde normalize edilebilir.

### B. Primitive half-character anti-periyodisitesi

Odd `xi` üzerinde

`exp(2 pi i (C+2^(n-1))xi/2^n) = - exp(2 pi i C xi/2^n)`.

Dolayısıyla

`Q(C+2^(n-1);P) = -Q(C;P)`.

Faz karakteri yarım residue aralığına indirilebilir; yalnız bir dış işaret saklanır.

### C. İşaret/conjugation simetrisi

`xi -> -xi` primitive frekansları permüte ettiği için

`Q(C; {(d_i,eps_i)}) = Q(-C; {(d_i,-eps_i)})`.

Bu üç simetri birlikte exact quotient canonicalization verir. Hiçbiri sayısal varsayım değildir.

---

## 3. [KANIT] `O(s^4 2^(3s/4))` state bound

Bu bound için quotient simetrilerine bile ihtiyaç yok; onlar yalnız sabitleri iyileştirir.

Kökten `d` recurrence adımı sonra kalan precision `n=s-d` olsun.

1. Her adımda parity şartını geçen **8** maske vardır. Dolayısıyla ağaçtan gelen kaba state sayısı `<=8^d`.

2. M4 kökünde iki `eps=+1` ve iki `eps=-1` faktör vardır; işaretler recurrence boyunca değişmez. Her offset `d_i` yalnız 0,...,d aralığındadır. İki pozitif faktörün unordered offset multiseti için `binom(d+2,2)`, iki negatif için aynı sayıda seçenek vardır. Bu yüzden offset-pattern sayısı en fazla

`binom(d+2,2)^2`.

3. Faz karakteri `C mod 2^(s-d)` olduğundan en fazla `2^(s-d)` değeri vardır.

Böylece her derinlikte

`N_d <= min(8^d, binom(d+2,2)^2 2^(s-d))`.

`D=floor(s/4)` seçelim. `d<=D` için ağaç bound'unu,
`d>D` için pattern+phase bound'unu kullanırsak

`sum_(d<=D) 8^d = O(2^(3s/4))`,

ve

`sum_(d>D) binom(d+2,2)^2 2^(s-d)`
` <= O(s^4) * 2^(s-D)`
` = O(s^4 2^(3s/4))`.

Sonuç:

`TOTAL_STATES = O(s^4 2^(3s/4)).`

Her state sabit sayıda child üretir. Binom ve state değerlerinin bit uzunlukları `poly(t,s)` ile sınırlanır; bu nedenle bit-aritmetiği ek bir polynomial faktör getirir. Burada iddia edilen esas kazanım residue exponentinin `1`'den `3/4`'e düşmesidir.

Bu theorem **bir M4 hesabı içindir**. Bütün W, bütün source strata veya bir orbit theorem değildir.

---

## 4. [YAPISAL ENGEL] Sabit separation-band state generic olarak lineer kapanmıyor

Bir tek liftte fazlar uygun gauge ile

`u'_d(sigma)=u_d + sigma u_(d+1)`, `sigma=+/-1`

biçimine getirilebilir. Separation-r complex coherence

`h_d^(r)=u_(d+r) conjugate(u_d)`

olsun. Doğrudan açılım

`h'_d^(r)`
` = h_d^(r) + h_(d+1)^(r)`
`   + sigma [ h_d^(r+1) + h_(d+1)^(r-1) ]`

verir.

Dolayısıyla bir state listesi yalnız separation `<=L` alanlarını lineer biçimde tutuyorsa, `r=L` update'inde `L+1` alanı çıkar. "Re/Im nearest-neighbor + yalnız tek two-step coherence" önerisi bu generic lift cebriyle exact finite-band closure sağlamaz.

Bu, actual Collatz tail katsayılarının ek nonlinear ilişkiler taşıyamayacağını kanıtlamaz. Yalnız generic lift özdeşliklerinin tek başına böyle bir kapanış vermediğini gösterir. Tam faz Q recurrence tam da bu genişleyen offset desenlerini saklar.

---

## 5. [TAM SONLU DOĞRULAMA]

### Küçük exact grid

Ayrı `phase_quotient_core.py` uygulaması:

- historical raw recurrence,
- quotient recurrence,
- doğrudan residue/filter autocorrelation M4

hesaplarını karşılaştırdı.

`t=2..8`, `s<=5`, bütün `j=0..t`: **188** root durumda

`raw Q4 = quotient Q4 = direct M4`

tam tamsayı eşitliğiyle geçti.

### Simetri çapraz kontrolü

Ayrı `independent_symmetry_check.py`, ana quotient fonksiyonunu import etmeden 80 deterministik rastgele küçük state üzerinde üç simetriyi doğrudan raw recurrence ile kontrol etti:

- common shift: 80/80,
- half-character sign: 80/80,
- sign/conjugation: 80/80.

Bu aynı sohbet içindeki ikinci uygulamadır; bağımsız ajan denetimi değildir.

### Seçilmiş quotient state sayıları

| s | quotient states | direct residues | oran |
|---:|---:|---:|---:|
| 4 | 57 | 16 | 3.5625 |
| 8 | 2,008 | 256 | 7.84375 |
| 12 | 27,120 | 4,096 | 6.62109 |
| 16 | 243,027 | 65,536 | 3.7083 |
| 17 | 405,740 | 131,072 | 3.09555 |
| 18 | 673,616 | 262,144 | 2.5694 |

Bunlar runtime theorem değildir; finite uygulama sayılarıdır. Görülen oranın s=8 sonrası düşmesi theorem'in yönüyle uyumludur, fakat crossover tarihi/s değeri kanıtlanmış değildir.

Round 4'ün unquotiented s=12 sayısı 88.198 idi; yeni canonical quotient aynı kök hesabında 27.120 state kullanıyor.

### Eski gerçek aileyi yeniden üretme

`(t,j,s)=(60,38,16)` için quotient recurrence:

- states: `243027`,
- `C_Y = 45.904196998361...`

verdi. Bu, daha önce certified integer correlation ile elde edilen değeri yeniden üretir. Burada yeni sonuç sayı değil; tam-faz recurrence'ın quotient edilmiş implementasyon kontrolüdür.

---

## 6. Başarısız/yarım koşular

Şeffaf provenance:

- İlk monolitik script; s=20 uzatması dahil fazla geniş kapsamla çalıştırıldı ve 180 s sınırında timeout oldu. Bilimsel sonuç olarak kullanılmadı.
- Kapsam daraltılmış ikinci monolitik koşu da toplu state sondajları nedeniyle timeout oldu. Kullanılmadı.
- Multi-s extended probe, s=17 satırını yazdıktan sonra sonraki büyük case'de timeout oldu. s=17 daha sonra **tek başına yeniden çalıştırıldı ve PASS** alınarak ancak o zaman tabloya kabul edildi.
- s=19 tek-case koşusu 120 s sınırını aştı; s=19 için sonuç raporlanmıyor.

Başarısız koşuların varlığı başarı gibi sunulmuyor.

---

## 7. Araştırma kararı

### Ne yeni bulundu?

- Tam phase recurrence için üç exact quotient simetrisi.
- Bir M4 kökü için `O(s^4 2^(3s/4))` rigoröz state-count bound.
- Round 4'ün finite state-explosion gözleminin asimptotik olarak tam resmi vermediği düzeltmesi.

### Ne elendi?

Generic lift cebrine dayanarak yalnız sabit separation bantlı küçük complex coherence listesinin exact **lineer** kapanacağı beklentisi. Daha geniş phase state veya actual-family'e özgü yeni bir ilişki gerekiyor.

### Ana ispat açısından ne açık?

Her şeyin kritik kısmı hâlâ açık:

- actual source reflection/mixed enerji büyümesi,
- W_flat gerekli exponenti,
- source-tail alignment,
- uniform W veya D2 bound,
- Collatz.

Yeni theorem hesaplamayı sıkıştırıyor; asimptotik küçüklük teoremi vermiyor.

### Sıradaki en değerli adım

Tam `C` faz karakterini tek tek taşımak yerine, quotient state'leri daha kaba ama rigoröz bir **weighted Lyapunov/majorant sınıfına** projekte etmek. İlk aday state özeti:

- offset multiset şekli,
- `v2(C)` ve küçük-residue sınıfı,
- channel support distance.

Amaç exact değeri yeniden üretmek değil; root M4 için bir üst operatör normu elde etmek. İlk önce şu falsification testi yapılmalı: aynı coarse state'e düşen exact state'lerin child majorant ihtiyaçları uniform bir sabitle kontrol edilebiliyor mu? Edilemiyorsa bu compression hattı büyütülmeden bırakılmalı.

Ayrıca bu tail-only hat, source-transfer Round 3'ün gerçek `sum H_s N_+^P` hedefinin yerine geçmez; ikisi ancak rigoröz bir weighted source-tail eşitsizliğinde birleşirse W'ye katkı verir.
