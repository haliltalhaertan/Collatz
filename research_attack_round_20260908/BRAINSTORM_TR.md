# Bulgulardan beyin fırtınası: bütün sapmalar önemli değil

8 Eylül 2026. Baş araştırmacı ve aynı üç alt ajan. Büyük deney yapılmadı. Bir oyuncak gerçek örnek baş araştırmacı tarafından doğrudan yeniden hesaplandı. Bu not yeni asimptotik sonuç iddiası değildir.

## 1. En önemli itiraz: D2 gereğinden güçlü olabilir

Kuyruk göstergesi T_j için sıfır dışı bazı frekanslar tam olarak görünmezdir. Özellikle q=2^t ve t çiftken j=t/2 için

    hat T_j(q/2)=binom(t-1,j)-binom(t-1,j-1)=0.

Dolayısıyla önek sapmasının (-1)^z bileşeni bu kuyruğu etkilemez. Bu, D2'nin sıfırlanan bileşenleri de cezalandırdığını gösterir; D2 yeterlidir fakat gerekli değildir.

### Gerçek küçük örnek ve yakalanan hata

Ajan önce m3,k2,q4 histogramını yanlışlıkla (1,0,2,0) verdi. Baş araştırmacı doğrudan dört başlangıcı hesapladı:

    h, K3(h), H3(h): (1,2,2), (3,2,4), (5,1,2), (7,3,26).

Doğru k2 histogramı P=(1,0,1,0), N=2. Merkezlenmiş vektör E=(1/2,-1/2,1/2,-1/2), e=1. t2,j1 kuyruk göstergesi (0,1,1,0). Her ötelemede T(a)+T(a+2)=1; 3^k=9 mod4=1. Katman sayımı sabit1, varyansı0; buna karşılık D2,k=1/4 ve qD2,k=1. Yanlış ilk histogram ve ona bağlı11/4,1/4 varyans değerleri kullanılmamalı.

Bu örnek kritik baskın katmanlara ilişkin bir asimptotik karşıörnek değildir. Tek mesajı, histogramın düzensizliğinin tamamını gidermenin zorunlu olmadığıdır.

## 2. Daha seçici hedef

W=sum_k V_k, her katmanın gerçek kuyrukla eşleşme varyansı olsun. Tam olarak

    W=sum_k q^(-2)sum_(xi!=0)|hat E_k(xi)|^2 |hat T_(r-k)(xi)|^2.

V<=K W ve |G(0)-B|<=sqrt(KqW) yeterlidir. Bu hedef gerçek kuyruk filtresinin sıfırlarını korur; W<=qD2 kestirmesi bunları kaybedebilir. Fakat W için yeni bir üst sınır yok. Daha seçici hedef yazmak tek başına ilerleme değildir. İncelenecek yapı, gerçek önek sapmasının kuyruk filtresinde ne kadar görünür olduğudur.

## 3. Birleşmenin iki farklı anlamını ayır

Sabit m,k için tam uç noktaya ulaşan başlangıç çokluğu M_y olsun. C_k=sum_y M_y^2, R_k=sum_(y!=y', y=y' modq) M_y M_y'. O zaman

    e_k=C_k+R_k-N_k^2/q.

Gerçek birleşme ile yalnız aynı kalıntıya düşme farklı mekanizmalardır. Eski birleşme sertifikaları ilk grubu açıklamaya yardımcı olabilir; ama birleşme C_k'yi büyütür. Farklı zaman/ağırlıktaki birleşmeler bu sabit m,k fiberlerine otomatik aktarılamaz. Çoklukları bir saymak hedefi değiştirir. Tek-yörünge harmonik bütçesi de birçok farklı başlangıçtan oluşan bu tabloya doğrudan uygulanamaz.

## 4. Dar ve karar verdirici sonraki inceleme

Önek histogramını mod2^s hassasiyetlerinde açalım. R_(k,s)=sum_(z<2^s)[P_(k,s+1)(z)-P_(k,s+1)(z+2^s)]^2 için tam olarak

    e_(k,s+1)=e_(k,s)/2+R_(k,s)/2,
    e_(k,t)=sum_(s=0..t-1)2^(s-t)R_(k,s).

Bu ayrışım henüz yeni bir sınır değil. Ama küçük mevcut örneklerde sapmanın hangi hassasiyette doğduğunu ayırmak ve aynı sapmanın gerçek kuyruk tarafından görülüp görülmediğini kontrol etmek, yalnız toplamD2 veya yeni büyük birr satırı üretmekten daha açıklayıcı olabilir. D2 büyük fakat W küçükse görünmezlik/filtreleme; ikisi de büyükse başka bir yol gerekir. Sonlu gözlem yalnız aday mekanizmayı seçer.

## 5. Doğrudan köken hedefi açık kalsın

J_k=sum_(z:K_t(z)=r-k)[P_k(z)-N_k/q] için G(0)-B=sum_k J_k. Yalnız pozitif J_k toplamını sınırlamak da yeterli olabilir. Bu hedef başka ötelemelerdeki düzensizliği önemsemez. Fakat kabul kümesiyle gerçek önek görüntüsünün kesişimini kontrol edecek yeni bir sertifika yoksa, eski join açığının adını değiştirmiş oluruz.

## Araştırma tercihi

Şimdilik 'kutular düzleşir' varsayımına bağlanmayalım. En dar soru: büyümeyi sürdürebilen kuyrukların gördüğü sapma hangi gerçek mekanizmadan geliyor? Küçük örneklerde çokluk, kalıntı hassasiyeti ve kuyruk filtresini birlikte ayırmak bir sonraki teşhise uygun. Yeni normlar yazmakla yetinmemek ve kritik rejimdeki baskın katmanlar için bir yapısal lemma veya karşıaile istemek konusunda üç ajanla aynı sonuca vardık.
