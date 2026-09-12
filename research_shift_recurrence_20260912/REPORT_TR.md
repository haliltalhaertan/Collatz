# Kaydırma korelasyonu: affine rekürsiyon ve tam moment hesabı

12 Eylül 2026. Önceki Galois denetiminden devam edildi. Üç alt ajan rekürsiyon, adversarial kontrol ve tam moment algoritması üzerinde çalıştı; ana araştırmacı bütün küçük kaydırmaları ve daha büyük tam ortak dağılımları hesapladı. Bu turda proje içinde kabul edilen yeni sonuç, gerçek parite-ağırlık korelasyonunun doğru ek durumlarla kapanması ve tek kaydırma için ispatlanmış hesap maliyeti azalmasıdır. Dünya literatüründe öncelik/özgünlük iddiası yapılmıyor. Uniform W, D2 ve Collatz sonuçları hâlâ açık.

## Basit anlamı

İki başlangıç arasındaki ilişkiyi yalnız 'aradaki fark' olarak izlemek yetmiyor. Tek/çift adımları farklı olduğunda biri3 ile çarpılıyor, diğeri çarpılmıyor. Aralarındaki ilişkiyi 'ikinci sayı = a × birinci sayı + b' biçiminde tutunca hesap kendi içinde kapanıyor. Aynı kalan durum birden çok kez ortaya çıktığında yeniden hesaplamak gerekmiyor.

Bu, bir kaydırmanın bütün başlangıçlar üzerindeki ortak parite dağılımını, başlangıçları ayrı ayrı dolaşmadan tam hesaplamayı sağlıyor. Bütün kaydırmaları ve bunların kareli toplamını aynı küçük maliyetle çözdüğümüz anlamına gelmiyor.

## Tam rekürsiyon

K_n(v), n kısayol adımındaki tek parite sayısı olsun. Tek a için:

    Q_n(a,b;x,y)=sum_(v mod2^n) x^K_n(v) y^K_n(av+b),
    J_n(d)=Q_n(1,d), Q_0=1.

q=2^(n-1), e in{0,1}, f=(ae+b)mod2 ile:

    a'=3^(f-e)a modq,
    b'=[3^f(ae+b)+f]/2 -2e a' modq,
    Q_n(a,b)=sum_e x^e y^f Q_(n-1)(a',b').

3^-1 modüler terstir. Bölme, çift tamsayı pay üzerinde modq indirgemesinden ÖNCE yapılır. Türetiliş RECURRENCE.md ve farklı biçimden bağımsız denetimi ADVERSARIAL.md içindedir.

Özellikle:

    J_n(2d)=J_(n-1)(d)+xy J_(n-1)(3d),
    J_n(2^ell d)=sum_(h=0..ell) binom(ell,h)(xy)^h J_(n-ell)(3^h d).

Bu hem J_n(0)=(1+xy)^n hem kardeş kaydırma J_n(2^(n-1))=(x+y)(1+xy)^(n-1) yasasını geri verir. Tek kaydırmalarda affine eğim gerekir; yalnız J ailesini kullanarak kapanış varsayımı geçersizdir.

## İspatlanmış maliyet azalması

Başlangıç eğimi1 olduğunda derinlik d'deki eğimler3^delta, |delta|<=d biçimindedir. Kalan b durumları en fazla2^(s-d), ağaç dalları en fazla2^d olduğundan:

    N_d <= min(2^d,(2d+1)2^(s-d)).

Toplayınca tek kaydırma için O(sqrt(s)2^(s/2)) farklı durum elde edilir. Polinom katsayıları ve tamsayı bit maliyeti de hesaba katılınca güvenli ifade poly(s)2^(s/2)'dir. Bu bütün tek kaydırmalar için geçerli bir üst sınırdır; deneyde seçilen iyi bir kaydırmaya dayanmıyor. Bütün kaydırmalar aynı önbelleği paylaşırsa durum sayısı en fazla6×2^s; global hesap hâlâ s bakımından üsteldir.

## Doğrulama

- Ana uygulama: s=1,...,9 için bütün kaydırmalar; toplam349.524 sıralı kalıntı çifti üzerinden doğrudan histogram karşılaştırması. Bütün katsayılar tam eşleşti.
- Rekürsiyon ajanı: ayrı uygulamayla1.066 affine polinom karşılaştırması, tam eşleşme.
- Adversarial ajan: n=1,...,6 için bütün tek a ve bütün b;2.730 affine durum, bütün katsayılar tam eşleşti. Modüler bölme ve temsilci seçimi ayrıca denetlendi.
- Daha büyük durum-sayısı deneyi ile tam polinom hesabı ayrı tutuldu. Aşağıdaki iki satır GERÇEK tam polinom hesaplarıdır; büyük ölçeklerde doğrudan yeniden sayım yapılmadı. Toplam kütle ve iki binom marjinali kontrol edildi.

| s | Seçilen kaydırma | Doğrudan dolaşılacak kalıntı | Kullanılan farklı alt durum | Tam ortak polinom süresi |
|---|---:|---:|---:|---:|
|20|349.525|1.048.576|3.115|0,126 sn|
|24|5.592.405|16.777.216|10.905|0,643 sn|

Bunlar bu bilgisayardaki tek çalıştırma süreleridir; kontrollü donanım benchmarkı değildir. s28'de35.952 durum sayıldı, ama orada tam polinom hesaplanmadı. PLAN.json başlangıç denemesini; FULL_JOINT_RESULTS.json sonradan seçilmiş büyük tam hesapları açıkça ayırır.

## Tam dördüncü moment için ikinci araç

Filtre F değerlerini yeterince büyük tabanda bir tamsayının basamaklarına yerleştiriyoruz. Ters sıradaki aynı vektörle tamsayı çarpımı bütün doğrusal korelasyon katsayılarını verir. Her katsayı sum F^2 ile sınırlı olduğundan bundan büyük taban seçmek basamak taşmasını kesin olarak önler. Döngüsel birleştirme sonrası C(d) tam elde edilir.

Bu, kayan nokta FFT'si kullanmadan tam sonuç üretir. Ayrı ajan28 gerçek filtre durumunda bütün korelasyon katsayılarını doğrudan çift döngüyle karşılaştırdı;28/28 eşleşti. Altı sınır durumu da geçti. Adversarial ajan taşıma sınırını, byte temsilini, döngüsel birleştirmeyi ve moment normalizasyonunu ayrıca denetledi. CPython çarpımına O(n log n) garantisi atfetmiyoruz; 2^s filtre girdisi hâlâ gereklidir.

Gerçek (t,j)=(60,38) ailesinde:

| s | Tam rasyonel C_Y'nin ondalık gösterimi | Tam korelasyon hesabı |
|---|---:|---:|
|8|2,53863|0,00061 sn|
|10|4,64223|0,00408 sn|
|12|9,35757|0,02948 sn|
|14|20,20743|0,19187 sn|
|16|45,90420|1,67338 sn|
|18|109,56436|15,67177 sn|

s16 ve18 ilk deneyin ardından istenen ve ayrıca etiketlenen uzatmadır. Filtre üretimi ve moment toplaması tabloda verilen korelasyon süresine dahil değildir; ayrı süreler algorithm_results.json içindedir. Son satırda bunlar yaklaşık0,425 ve0,028 saniyedir.

Dolayısıyla bu somut ailede 'filtre hemen hemen düzdür' varsayımıyla ilerlemiyoruz. Artış tam rasyonel hesapla görülüyor. Ancak t=60 sabit ve s sınırlı: buradan asimptotik sınırsızlık veya bütün ağırlıklı toplamın başarısızlığı çıkarılamaz.

## Açık kalan matematik ve sonraki karar

Rekürsiyon gerçek C(d)'yi J_s(d) katsayılarının binom ağırlıklı toplamı olarak verir. Dördüncü momentte ise [C(d)-C(d+2^(s-1))]^2 vardır. Karesini almak farklı dalları birbirine bağlar. Pozitif polinom katsayıları veya az durum sayısı bu çapraz terimleri tek başına sınırlamaz.

Sonraki matematik hedefi, bu affine rekürsiyon üzerinde işaretli kardeş farklarını birlikte taşıyan bir ağırlıklı eşitsizlik kurmak; gerekirse gerekli daha yüksek ortak durumun gerçekten kapandığını göstermek. Bütün kaydırmalar için kısa scalar moment rekürsiyonu, uniform C_Y ve gerçek kaynak–filtre hizalanma sınırı henüz elde edilmedi. Önceki tepe ayırma yöntemi ve W_flat ağırlıklı analiz korunuyor. Kesin hesap aracı, aday eşitsizlikleri çabuk ve yuvarlama şüphesi olmadan sınamaya hazır.

Yeniden üretim: joint_probe.py, full_joint_followup.py, exact_moment.py. Son uzatma için ALGORITHM.md'deki çağrı kullanılır. Ham veriler ve bağımsız denetimler bu klasördedir. Ücretli sağlayıcı çağrısı yapılmadı.
