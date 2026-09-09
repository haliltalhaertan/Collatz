# Görünen sapma: ince ölçek teşhisi ve kuyruk sıfırlarının tam sınıflandırması

8 Eylül 2026. Baş araştırmacı ve üç alt ajan (audit_cancellation, audit_coarse_identity, review01_global). Yeni ücretli çağrı veya yayın yok. Sabit küçük paneller dışında yörünge aralığı büyütülmedi.

## Sonuç

Bir önceki turun sorusunu somut olarak ayırdık: gerçek önek sapması hangi kalıntı hassasiyetinde oluşuyor ve kuyruk tarafından ne kadarı görülüyor? Dört panelde iki bağımsız hesap tam eşleşti. Kuyruk filtresi kaba kaynak sınırından belirgin biçimde küçük sonuç verebiliyor; fakat kalan enerji iki büyük panelde büyük ölçüde en ince kalıntı ayrımında.

Ek olarak bir genel sonlu-cebir önermesi elde edildi ve iki ajan tarafından bağımsız denetlendi: sabit ağırlıklı Collatz kuyruk göstergesinin sıfır dışı Fourier katsayıları yalnız tek bir istisnada tam sıfır olabilir. Bu, yüksek hassasiyetlerde büyük bir tam görünmezlik uzayı arama fikrini bu operatör için kapatıyor. Katsayıların ne kadar küçük olduğunu söylemiyor; yeni asimptotik sayım tahmini veya yörünge dışlaması yok. Literatürde ilk kez bulunduğu iddia edilmiyor.

## 1. Sabit deney ve bağımsız doğrulama

Önceden sabitlenen r=5,10,12,14; A=floor(alpha r), m=ceil(1.2r), t=A-m kullanıldı. Kısa t aralığı1..5. Baş araştırmacı gerçek histogramları, kalıntı sınıflarına koşullu projeksiyonları ve gerçek öteleme sayımlarını hesapladı. Bu projeksiyonlar döngüsel Fourier iletken katmanlarının enerjilerini tam rasyonel aritmetikle verir; kayan noktalı DFT kullanılmadı.

review01_global ayrı betikte doğrudan konvolüsyon, kaynak/kuyruk otokorelasyon çifti ve kardeş kutu ayrışımı kullandı. compare.py bütün G dizileriyle V,W,qD2 toplamlarını iki çıktı arasında tam eşleştirdi.

W=sum_k V_k gerçek tek-ağırlık varyansları toplamıdır. qD2, kuyruk filtresini yalnız kabul kümesi büyüklüğüyle sınırlayan daha kaba üst sınırdır. W/(qD2) bir sonlu sıkılık oranıdır; gerçek görünmez enerji oranı diye yorumlanmamalı.

|r|W|qD2|W/(qD2)|Toplam V'nin en ince katmandaki payı|
|---:|---:|---:|---:|---:|
|5|37/4|37/4|1|1|
|10|819/32|2915/32|0.280961|0.540717|
|12|2795/4|21195/8|0.263741|0.945426|
|14|274211/256|4612387/256|0.059451|0.706960|

r14'te en büyük kaynak enerjisine sahip k11 katmanında e_k=2970, gerçek V_k=6647/16, kaba sınır37125/4. Kuyruk etkisini atmak bu katmanda önemli bilgi kaybettiriyor. Fakat bu sonlu oranlardan üstel sönüm veya monoton iyileşme çıkarılamaz. Büyük iki örnekte en ince katmanın payı yaklaşık%95 ve%71; yalnız ilk birkaç kalıntı bitini kontrol etmek, bu panellerde bile kalan sapmanın tamamını açıklamıyor.

## 2. Ölçeklerle doğru eşleştirme

P_(k,s), aynı m-adımlık gerçek uç noktaları mod2^s saysın. R_(k,s-1), mod2^(s-1)'deki her kutunun iki çocuğu arasındaki farkların kareleri toplamı olsun. q=2^t üzerinde kaynak enerjisinin tam iletken2^s katkısı

    e_(k;s)=2^(s-1-t) R_(k,s-1).

Eşdeğer olarak primitive Fourier enerji toplamı2^(s-1)R_(k,s-1)'dir. Bu sınıflandırma Boolean Walsh derecesi değildir. Ham e_(k,s) modül büyürken azalabilir; 2^s e_(k,s) monotondur.

Kuyruk için tam lift formülü:

    F_(s;t,j)(u)=binom(t-s,j-K_s(u)),
    hat T_(t,j)(a*2^(t-s))=sum_(u<2^s)F_(s;t,j)(u)exp(-2pi i a u/2^s), a odd.

Kaynak ve kuyruk katsayılarının kare çarpımları o katmandaki gerçek V_k'yi verir. Odd3^k çarpanı iletkeni korur, fakat ağırlıklar arasındaki fazları değiştirir; toplam G oluşturulurken bu çarpan çıkarılmadı.

## 3. Tam Fourier sıfırları önermesi

H(x)=x/2 (çift), (3x+1)/2 (tek) ve K_t(x) ilk t adımın tek durum sayısı olsun. t>=1, q=2^t,0<=j<=t için T_(t,j)(x)=1_(K_t(x)=j). O zaman

    hat T_(t,j)(xi)=0, xi!=0 modq

ancak ve ancak t çift, j=t/2 ve xi=q/2 olduğunda geçerlidir. Yani tek olası sıfırın iletkeni2'dir; iletken4 ve üzerinde bütün katsayılar sıfırdan farklıdır.

### Kısa ispat

xi'nin iletkeni2^s olsun. Yukarıdaki F(u) katsayıları rasyonel tamsayılardır. Primitive2^s kökünde sıfırlanma, polinomun x^(2^(s-1))+1 ile bölünmesini zorlar; bu da katsayıların ilk ve ikinci yarısının aynı olmasıdır. Buradaki siklotomik polinomun indirgenmezliği standarttır; x yerine x+1 koyunca2 için Eisenstein ölçütüyle de görülebilir.

u ve u+2^(s-1) ilk s-1 pariteyi paylaşır, son pariteleri terstir. İlk s-1 paritenin her h=0,...,s-1 ağırlığı gerçekleşir. Dolayısıyla n=t-s için

    binom(n,j)=binom(n,j-1)=...=binom(n,j-s)

gerekir. Aralık [j-s,j],0<=j<=n+s nedeniyle binom satırının pozitif desteğiyle kesişir. Ortak değer sıfır olamaz. Pozitif binom satırında en fazla iki ardışık katsayı eşit olabilir; s>=2 bu yüzden imkânsızdır. s=1 için eşitlik yalnız t=2j durumunda olur. Destek dışındaki katsayılar0 alınır; n=0,1 kenar durumları da kapsanır.

### Operatör sonucu

Kuyrukla döngüsel konvolüsyon normalde q ranklıdır. Orta-ağırlık istisnasında rank q-1 ve çekirdek tam olarak span{(-1)^z}'dir. Gerçek veya kompleks histogramlar için ve odd3^k yeniden indislemesinden sonra aynı sonuç geçerli. Bu yalnız tek kuyruk/katman operatörüdür; farklı k katkılarının birbirini iptal etmesini dışlamaz.

Bu sınıflandırma sayısal bir örüntüye dayanmaz. Baş araştırmacı ayrıca t1..10, tüm geçerli j,s üzerinde440 iletken durumunu tam katsayı testiyle kontrol etti: binom lift sayımları doğrudan kuyruk kalıntı sayımlarıyla eşleşti; öngörülen5 sıfır durumu dışında sıfır yok. Kontrol ispatın yerine geçmez.

## 4. Stratejik anlamı ve sınır

Önceki m3,k2,t2,j1 oyuncak örneğinin tam görünmezliği gerçektir, fakat yalnız istisnai parite yönüdür. Onu yüksek hassasiyetlere yayılan büyük bir görünmezlik mekanizması gibi düşünemeyiz.

Diğer katsayılar sıfırdan farklı olsa bile çok küçük olabilir. Ters operatörün normu büyüyebilir. Dolayısıyla bu önerme güçlü sayım sönümünü çürütmez ve histogramın görünen enerjisine uniform bir alt sınır vermez. Sayısal küçülmenin olası açıklaması, yüksek iletkenlerdeki nicel zayıflama ve kaynağın oralardaki dağılımıdır; bu açıklama henüz kanıtlanmış değildir.

Sonraki matematiksel soru: kritik ağırlıklarda, özellikle s/t'nin küçük olmadığı katmanlarda, gerçek kaynak enerjisi ile kuyruk katsayılarının çarpımını nasıl sınırlayabiliriz? W=sum V_k için önceki yeterli üs yaklaşık1.89423978 hâlâ açık. Sadece düşük iletken formülünü yeniden hesaplamak, bütün yüksek katman toplamını çözmez.

## 5. Ajanın karşı itirazı: birleşme ayrımı

audit_coarse_identity, tam uç nokta çarpışmalarını C_exact ve farklı uç noktalar arasında v2(|y-y'|)=d çakışmalarını A_d ile ayırdı. Ham çakışma C_s=C_exact+sum_(d>=s)A_d; fakat kardeş fark enerjisi R_(s-1)=C_exact+sum_(d>=s)A_d-A_(s-1). Merkezlenmiş enerjide bu parçalar ayrı ayrı pozitif bir 'birleşme enerjisi' ve 'kalıntı enerjisi' oluşturmaz. İşaret ve taban düzeltmesi korunmalıdır.

## Dosyalar

- diagnostic.py / DIAGNOSTIC.json: baş araştırmacının tam katman projeksiyon hesabı.
- independent_check.py / INDEPENDENT_CHECK.json: ayrı ajanın konvolüsyon ve otokorelasyon denetimi.
- compare.py / COMPARISON.json: bağımsız çıktıları tam eşleştirme.
- check_zeros.py / ZERO_CHECK.json:440 sonlu sıfır sınıflandırması kontrolü.
- kernel.md: kaynak/kuyruk iletken özdeşlikleri.
- ZERO_CLASSIFICATION.md: ilk ajanın bağımsız ispatı ve rank sonucu.
- attack.md: ikinci ajanın kapsam itirazları ve bağımsız sıfır ispatı.

Eski kayıtlar tarihsel kapsamlarıyla kullanıldı; kanonik arşiv ve önceki deney sonuçları değiştirilmedi. Bu turun sonlu-cebir önermesi, Collatz yakınsama teoremi değildir.
