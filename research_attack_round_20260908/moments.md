# 22. moment ve Walsh enerji yoluna karşı denetim

8 Eylül 2026. review01_global ajanının ek görevi. Yeni bağımsız ajan değil; küçük cebir ve birincil kaynak kontrolü, büyük hesap yok.

## Sonuç

22. moment koşulu doğrudur fakat genel hiperkontraktivite yeni bir Collatz tahmini üretmez. Yalnız tam derece d<=t bilgisiyle kullanılırsa mevcut varyans hedefinden belirgin biçimde daha pahalıdır. Dahası aynı ağırlıklı Walsh enerjisi elde edilebilirse, doğrudan nokta değerlendirmesi 22. moment üzerinden geçmekten daha iyi bir yeterli eşik verir.

## Notasyon ve moment koşulu

q=2^t, t=tau*r+o(r), f=G/B-1 ve ortalama(f)=0 olsun. Walsh dönüşümü normalize edilir: fhat(S)=E_a f(a) chi_S(a). E_l=sum_{|S|=l} fhat(S)^2; sum E_l=V/B^2.

b=1.2, kappa=1.053 için tau=0.3849625007211561, gamma0=1.1206813872251445 ve izinli kayıp lambda=b/kappa-gamma0=0.01891975237599524.

M_p=E|f|^p ise |f(0)|<=(q M_p)^(1/p). Dolayısıyla M_p<=2^((mu+o(1))*r) ve (tau+mu)/p<lambda yeterlidir. p=22 için yalnız mu=0 değil, mu<22lambda-tau yaklaşık 0.03127205 de yeterlidir. Bu bir koşullu yeterlilik hesabıdır; gerçek M22 için sınır kanıtlanmadı.

## Hiperkontraktivitenin tam maliyeti

W21=sum_{l>=1}21^l E_l tanımlansın. Standart Boolean hiperkontraktivitesi, ghat(S)=21^(|S|/2) fhat(S) seçilerek

    ||f||22^2 <= W21,  M22 <= W21^11

verir. Bunun için f=T_(1/sqrt(21)) g kullanılır. Kaynak: [Kirshner-Samorodnitsky birincil metni](https://arxiv.org/pdf/1909.11929), girişte standart hiperkontraktif sınır ve onu iyileştiren teorem ayrı belirtilir. Burada daha güçlü teorem uygulanmıyor.

W21<=2^((epsilon+o(1))*r) varsa moment yolu epsilon<2lambda-tau/11=0.00284291377734 ister. Genel p>=2 için W_(p-1) enerji bütçesinin üssü epsilon<2lambda-2tau/p olmalıdır.

Sadece derece d<=delta*r+o(r) ve V/B^2<=2^((-beta+o(1))*r) biliniyorsa W21<=21^d V/B^2. Yeterli koşul:

    beta > delta*log2(21)+tau/11-2lambda.

Tam derece sınırı delta=tau ile beta>1.68803458526 gerekir. Doğrudan varyans yolunun istediği beta>tau-2lambda=0.347122995969 idi. Dolayısıyla yalnız d<=t kullanımı burada daha zayıftır.

22. moment üzerinden bu kaba derece aktarımının doğrudan varyans eşiğinden daha iyi olması için delta<0.0796768257074 gerekir; bu yaklaşık t'nin yüzde20.7'sidir. Bu yeterli/karşılaştırmalı mimari eşiğidir, bütün olası moment yöntemlerine engel teoremi değildir. Sonlu tam-derece gözlemleri asimptotik etkili düşük dereceyi tek başına çürütmez.

## Daha iyi alternatif: aynı enerjiyle doğrudan köken kontrolü

Her w>0 için Cauchy-Schwarz doğrudan

    |f(0)|^2 <= [sum_{S!=empty} w^|S| fhat(S)^2]
                  * [(1+1/w)^t-1]

verir. Walsh karakterlerinin kökende hepsi1'dir. Dolayısıyla W_w enerjisinin üssü epsilon ise

    epsilon + tau*log2(1+1/w) < 2lambda

yeterlidir. Özellikle w=21 için epsilon<0.0120030560804 yeterli: aynı W21'i kullanan moment yolunun 0.00284291377734 eşiğinden daha gevşek. Bu karşılaştırmada yüksek moment gereksiz ara adımdır. w=1, doğrudan varyans eşiğini yeniden verir.

Bu yeni gerçek enerji üst sınırı değildir. Kullanışlı çıktı, bir spektral katman teorisi bulunursa tam olarak hangi ağırlıklı bütçenin yeterli olacağını söyleyen sertifikadır. Tek bir derece sınırı yerine farklı katmanların büyüklükleri korunur.

## Tam ortalamayı ve sonlu gözlemleri koruyan karşımodel

Bu model gerçek Collatz sayımları olarak ileri sürülmez. Amaç ortalama, kapasite, sonlu küçük momentler ve tam-derece gözlemlerinden asimptotik sonuç çıkmadığını göstermektir.

Her büyük kritik r için gerçek toplam T=binom(A-1,r-1), B=T/q, L=floor(B) olsun. e_a in {0,1} değerlerini sum e_a=T-qL olacak şekilde seçelim. sigma=1/16 ve

    K=floor(B*2^(sigma*r)/q),
    G(0)=L+e_0+(q-1)K,
    G(a)=L+e_a-K  (a!=0)

tanımlayalım. Toplam tam olarak T'dir. sigma<tau olduğundan diğer sayımlar sonunda pozitiftir. gamma0+sigma<b olduğundan G(0) da sonunda gerçek blok kapasitesi 2^(m-1)'in altındadır.

K üstel büyür. Bütün boş olmayan Walsh katsayılarında spike katkısı K/B iken yuvarlama hatası en fazla1/B olduğundan, yeterince büyük r'de bütün bu katsayılar sıfırdan farklıdır; derece tam t'dir. Buna rağmen

    G(0)/B = 2^((sigma+o(1))*r),
    V/B^2 = 2^((2sigma-tau+o(1))*r),
    M22 = 2^((22sigma-tau+o(1))*r).

Normalize varyans üstel olarak sıfıra gider, ancak sigma>lambda olduğundan köken hedefi başarısızdır; 22sigma-tau>0 olduğundan M22 altüstel değildir. İstenen herhangi bir sonlu r listesinde gerçek paneller aynen bırakılıp model yalnız daha büyük r'de başlatılabilir. Dolayısıyla mevcut sonlu moment/katman ölçümleri bu davranışı mantıken dışlamaz.

## Önerilen karar

22. moment fikrini ispatlanmış ilerleme veya varyansı aşan genel araç olarak sunmayalım. Sonraki anlamlı hedef, gerçek Collatz sayımlarında W_w için yukarıdaki doğrudan yeterli enerji bütçesini sağlayan bir yapısal sınırdır. Bütün dereceleri tek en-yüksek dereceye indirgemek hem mevcut tam-derece gözlemlerine hem de iptal teşhisine göre pahalıdır. Kökendeki işaretli Walsh toplamını doğrudan kontrol etmek daha da zayıf bir hedef olabilir; enerji sertifikası gerekli koşul değildir.

Baş araştırmacının yeni merkezleme teşhisi önceki strateji yorumuma ayrıca itiraz getiriyor: P_k(z) önce N_k/q ile merkezlenince sabit taban katkıları kaybolabilir. k-katmanları arasında Cauchy-Schwarz yalnız O(r) kayıp verdiğinden, hedef yalnız üstel oran ise k-katmanları arası negatif iptali korumak zorunlu değildir. Önceki milyonluk ham kovaryans ayrışımından 'her başarılı ispat çapraz-k iptalini korumalı' sonucu çıkmaz. Buradaki Walsh-ağırlıklı enerji bütçeleri bu stratejik iddiaya dayanmıyor. Yeni merkezleme betiği bu görevde ayrıca yeniden denetlenmedi.
