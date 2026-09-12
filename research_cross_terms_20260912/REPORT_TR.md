# Çapraz terimlerden birinin tam kapanışı ve yansıma ayrıştırması

12 Eylül 2026. Önceki affine rekürsiyondaki iki çapraz terim incelendi. Üç ajan özdeşlik, karşı-aile ve bağımsız doğrudan hesap üzerinde çalıştı. Ana araştırmacı tam tamsayı korelasyonuyla daha büyük aileyi ölçtü. Bu turda bir çapraz terim tam olarak başka kanalın normuna indirgendi; toplam için tek-adımlık iki taraflı karşılaştırma kanıtlandı. Uniform W, D2 ve Collatz açık kalıyor. Dünya literatüründe öncelik iddia edilmiyor.

## Sonuç: iki bağımsız çapraz terim kalmadı

Önceki notasyonda q=2^(s-1), h0=q/2 ve Delta Z(b)=Z(b)-Z(b+h0). N0,N1,NB sırasıyla Delta A0, Delta A1, Delta B'nin yarım periyottaki kare normları olsun. Çarpımları2 katsayısı OLMADAN tanımlıyoruz:

    E=sum_(h<h0) Delta A0(h) Delta A1(3h),
    O=sum_(h<h0) Delta B(3h+2) Delta B(-3h-1).

Yeni tam özdeşlik:

    E=NB>=0.

İspat, A0,A1 otokorelasyonlarının Fourier dönüşümlerinin mutlak kare olması; B_hat(a)=f1_hat(a) conjugate(f0_hat(3a)) ve odd frekanslarda3 ile yeniden indekslemeye dayanır. Ana hesap bütün örneklerde eşitliği gözledi; iki ajan birbirinden bağımsız Fourier türetmeleriyle doğruladı. İspat genel gerçek kanal dizileri için geçerli; Collatz'a özgü sınırlı sayısal örnekten çıkarılmadı.

## Geriye kalan terim bir yansıma bileşeni

Z=Delta B ve RZ(b)=Z(1-b) olsun. R, gerçek anti-periyodik diziler üzerinde kendine eşlenik, norm koruyan ve karesi birim olan operatördür. Z_+=(Z+RZ)/2, Z_-=(Z-RZ)/2 ve yarım normları N_+,N_- ile:

    NB=N_++N_-,   O=N_+-N_-.

Parent sibling farklarının kare toplamı S için artık yalnız pozitif terimler içeren tam ifade var:

    S=N0+N1+6N_++2N_-.

Özellikle:

    S_even=N0+N1+2NB,
    S_odd=4N_+,
    S_even <= S <= N0+N1+6NB <= 2 S_even.

Son eşitsizlik NB²<=N0N1 ve2NB<=N0+N1 ile çıkar. Parent primitive dördüncü moment qS'dir. Buradaki S_even, W_flat DEĞİLDİR. Bu sonucu W/W_flat<=2 diye okumak yanlıştır.

Bir başka kesin sonuç: birleşik çapraz katkı2E+2O=4N_+ hiçbir zaman negatif değildir. Tek başına odd çapraz terim negatif olabilir, ama even terimle birlikte diyagonal toplamın altına indiremez. Bu nedenle çapraz terimleri atmak bu düzeyde bir alt sınır verir.

## Bağımsız kontroller ve gerçek engeller

Ana probe.py, t=2,...,9; bütün j; s=2,...,min(t,7) için247 durumda hem parent hem kanalları doğrudan hesapla karşılaştırdı. Genel tamsayı çapraz korelasyonunun yönü ayrıca simetrik olmayan dizilerle sınandı. E=NB, yansıma norm ayrımı ve iki-kat sınırı tam aritmetikte doğrulandı.

Bağımsız ajan t=2,...,10 için313 gerçek filtre durumunu ve11.004 parent korelasyon özdeşliğini scalar tamsayı döngüleriyle doğruladı. Ana veya önceki Kronecker kodunu kullanmadı. Özdeşlik ajanı132, adversarial ajan460 ayrı kapsamlı doğrudan örnek de kontrol etti; bu kümeler örtüşür, bağımsız benzersiz durum sayıları gibi toplanmamalıdır.

Adversarial kontrol, 'çapraz terimler küçük' veya 'uniform rho<1' varsayımlarını sınırlayan gerçek örnekler buldu:

- (t,j,s)=(5,3,4): even kanal iki normu6,6 ve iç çarpımı6; rho_even=1. İç ağırlık, sonlu kritik-orana yakın örnek.
- (11,6,4): odd iki normu384160,384160 ve iç çarpımı384160; rho_odd=1.
- (5,4,4): odd iç çarpımı-2, iki norm2; rho_odd=-1.
- (9,5,4): S=45356, S_even=23256; oran667/342 yaklaşık1,95029. Çaprazları atmak gerçek filtrede neredeyse iki kat eksik sonuç veriyor.

Bunlar bütün filtre/ölçekleri kapsayan koşulsuz strict-gap iddiasını engeller. Düşük sabit s'yi dışlayan veya büyüyen kritik aileye ek hipotez koyan bir teoremi çürütmez. Uç ağırlıklarda j=0,t kanal sıfırları nedeniyle rho tanımsız olabilir; bunlar nondegenerate eşitlik örneği diye sunulmadı.

Genel gerçek nonnegative kanallar için2 sabiti keskindir: q=4, f0=(sqrt(2),0,0,0), f1=(1,1,0,0) örneği eşitlik verir. Bu kanalların gerçek binom Collatz çifti olduğu iddia edilmiyor; gerçek ailede2'nin keskinliği açık.

## Sabit gerçek ailede kazanç

(t,j)=(60,38), s=2,4,...,16 başlangıçta sabitlendi. Tüm korelasyonlar, momentler, E ve O tamsayı olarak hesaplandı. Tabloda yeni üst sınır U_new=N0+N1+6NB; eski Cauchy üst sınırı U_old=N0+N1+2sqrt(N0N1)+4NB. Yeni oranlar tam rasyonelin ondalık gösterimi, kareköklü eski oranlar sayısal gösterimdir.

|s|odd rho=O/NB|S/S_even|U_old/S|U_new/S|
|---|---:|---:|---:|---:|
|4|-0,03005|1,36143|1,34526|1,28193|
|8|0,47849|1,54874|1,20148|1,12498|
|12|0,53407|1,58301|1,17967|1,11186|
|16|0,61797|1,62813|1,14461|1,09109|

Özdeşlik even Cauchy kaybını tam ortadan kaldırıyor. Geriye kalan U_new-S=2(NB-O)=4N_-; dolayısıyla asıl yeni ihtiyaç yansıma bileşenlerinin ağırlığını kontrol etmek. Bu tablodaki oranlar W/W_flat veya Collatz yakınsama oranı değildir. Sabit t=60 ve sonlu s taraması asimptotik sonuç vermez.

## İki-kat sınırını tekrar tekrar uygulamak ne sağlar?

Alt kanallar doğru parametrelerle (t-1,j,s-1) ve(t-1,j-1,s-1) filtreleridir. Karışık normu Cauchy ile atıp yalnız bu iki dördüncü momenti taşırsak genel bir kaba rekürsiyon elde ederiz; fakat bu bilgi kaybı, bilinen kaba eşlenik-frekans sınırından daha iyi bir sonuç sağlamaz. Ayrıntılı karşılaştırma IDENTITIES.md'de bağımsız olarak denetlenmiştir. Bu nedenle tek-adımlık2 sabitini bütün derinliklerde uniform2 diye taşımıyoruz.

## Araştırma kararı

Kabul edilen ilerleme: even çapraz terimin norm özdeşliği, yansıma öz-ayrıştırması, pozitif toplam formülü ve tek-adımlık iki-kat karşılaştırma. Açık kalan: yansıma-çift bileşenin N_+ ağırlığını veya yeterli birleşik kanal potansiyelini gerçek binom/parite yapısından kontrol etmek. Alt kanalların ortak moment bilgisini tamamen atmak yeni ilerlemeyi kaybettiriyor.

Sonraki hedef, sadece kanal normlarını değil NB ve yansıma bileşenini birlikte taşıyan bir ağırlıklı yineleme kurmak veya bu yaklaşımın büyüyen kritik ailede yetersizliğini gösteren karşı-aile bulmak. Kaynak–filtre hizalanması ve gerekli W_flat ölçeği ayrıca açık kalıyor. Hesap ve kanıt araçları geliştirildi; ana Collatz ispat engeli giderildiği iddia edilmiyor.

Yeniden üretim: probe.py; bağımsız denetim kodu INDEPENDENT.md içinde; tüm tamsayı sonuçları RESULTS.json, independent_results.json ve attack_results.json dosyalarında. Ücretli model çağrısı yapılmadı.
