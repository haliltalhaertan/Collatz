# Gerçek döngüsel spektrumda tepe ayırma — 12 Eylül 2026

Bu tur, önceki gerçek kaynak–filtre örtüşmesi bulgusunu daha büyük sonlu panellere taşıdı. Birkaç büyük frekansı ayıran geçerli bir üst sınır elde edildi; fakat küçük bir katmanda gözlenen tek frekans çifti hâkimiyeti büyük panellerde aynı güçte sürmedi. W, D2 ve Collatz açık. Bu çalışma asimptotik bir teorem veya Collatz kanıtı değildir.

## Önceden sabitlenen deney ve doğrulama

PLAN.json hesap öncesinde r=5,...,20, A=floor(log2(3^r)), m=ceil(6r/5), t=A-m ve her (k,s) katmanında L=1,2,4 eşlenik frekans çifti seçimini sabitledi. Başlangıçlar 1<=h<2^m aralığındaki tüm tek sayılardır; örnekleme yapılmadı. Toplam 16.510.880 panel-başlangıç değerlendirmesi yapıldı. Aynı başlangıç farklı panellerde tekrar bulunabildiği için bu sayı farklı tamsayıların sayısı değildir.

probe.py gerçek uç noktaları ve tek-adım sayılarını üretir. Histogram popülasyonlarını binom sayılarıyla, her k için doğrudan çeviri varyansını tam rasyonel iletken toplamıyla, ilk iki hassasiyette gerçek varyansı düz modelle karşılaştırır. W ve W_flat tam rasyoneldir. Frekans sıraları, paylar ve U_L sayıları FFT temelli sayısal tanılardır; aralık aritmetiğiyle sertifikalanmadı.

İlk hesapta tam eşit tepe değerlerini kayan nokta gürültüsü farklı sıralayabildi. Nihai probe, Z[zeta_(2^s)] içinde Phi=X^(2^(s-1))+1 indirgemesiyle tam eşitlik gruplarını bulur ve grup içinde küçük frekans temsilcisini seçer. Farklı grupların sırası hâlâ sayısal olup açık fark kontrolü yapılır. RESULTS.json bu düzeltilmiş çalışmadır. Kaynağa bakıp daha fazla katkı taşıyan çifti seçmek ayrı bir kaynak-uyarlamalı tanıdır; filtreye göre önceden seçimin başarısı gibi sunulmaz.

Bağımsız denetçi NumPy, FFT ve probe fonksiyonları olmadan scalar tamsayı yörüngeleri ve doğrudan çevirilerle r=12 ve r=20'yi yeniden hesapladı. W_flat için binom formülünü kopyalamadan gerçek filtre fark normlarını kullandı. Bütün katkı veren k katmanları ve toplamlar tam eşleşti:

| r | Başlangıç | W | W_flat |
|---|---:|---:|---:|
| 12 | 16.384 | 2795/4 | 7987/16 |
| 20 | 8.388.608 | 1056368259/4096 | 824144183/4096 |

## Tepe ayırma ne kadar işe yaradı?

L her (k,s) katmanında seçilen çift sayısıdır; bütün panelde tek bir çift anlamına gelmez. Aşağıdaki payların paydası özgün W'dir. Tam boşalan küçük katmanların 1e-16 mertebesindeki sayısal yuvarlama kalıntıları gerçek negatif varyans değildir.

| r | W/W_flat | Filtreye göre ilk çiftin payı | İlk 4 çiftin payı | Kaynağa da bakarak seçilen ilk çiftin payı |
|---|---:|---:|---:|---:|
| 12 | 1,39977 | %75,76 | %100 | %83,62 |
| 14 | 0,73268 | %28,57 | %85,43 | %50,76 |
| 18 | 1,01805 | %41,98 | %75,36 | %56,94 |
| 19 | 1,00343 | %28,03 | %59,07 | %51,44 |
| 20 | 1,28178 | %26,80 | %67,56 | %62,39 |

Önceki r=12,k=10,s=4 katmanındaki %94,37 tek-çift payı doğrudur; yalnız o katmanın payıdır. Tüm W için aynı yüzdeyi kullanmak yanlıştır. Büyüyen panellerde filtre tepesi ile gerçek kaynak enerjisinin birlikte nerede bulunduğu belirleyicidir.

Sabitlenen 16 panelde en büyük W/W_flat tam 11180/7987, yaklaşık 1,39977 çıktı. Bu gözlem uniform C varlığını kanıtlamaz, yokluğunu da göstermez. Bir çift çıkarıldıktan sonra kalan W'nin özgün W_flat'e oranı bu panellerde 1'in altında kaldı; bunun genel geçerli olduğunu kanıtlamadık.

## Geçerli analitik ilerleme

Bir katmanda çiftlerin filtre çarpanlarını y_1>=...>=y_n, o çiftlerdeki toplam kaynak Fourier enerjisini e_i, S=sum e_i yazalım. ell=min(L,n) ve y_(n+1)=0 ile:

    V = q^-2 sum_i y_i e_i
      <= U_L = q^-2 [sum_(i<=ell) y_i e_i
                       + y_(ell+1) (S-sum_(i<=ell) e_i)].

Bu, her kalan çarpanın y_(ell+1)'den küçük veya eşit olmasından çıkan tam bir eşitsizliktir. U_L, L arttıkça azalır. İspatı ANALYTIC_REVIEW.md'dedir. Toplam üst sınır katman U_L'lerinin toplamıdır. Formülün geçerliliği tamdır; aşağıdaki FFT ile değerlendirilmiş sayılar sayısal tanıdır.

| r | Tepe ayırmadan üst sınır / W | 1 çift ayırınca | 4 çift ayırınca |
|---|---:|---:|---:|
| 12 | 1,309 | 1,087 | 1,000 |
| 14 | 3,509 | 1,628 | 1,153 |
| 19 | 4,266 | 2,714 | 1,816 |
| 20 | 3,341 | 2,341 | 1,604 |

Yani yöntem aynı panelde kaba üst sınırı belirgin iyileştiriyor. Ama sabit dört çiftle uniform sabit elde edildiği sonucu çıkmıyor. Ayrıca tepeleri bulmak tüm frekansları incelemeyi gerektirebilir; henüz asimptotik olarak ucuz bir algoritma elde etmedik.

Kalan filtre çarpanlarının hepsinin D altında olduğu yeter koşulu, sayısal olarak mevcut t=7 filtrelerde bile sağlanmıyor: L=1,2,4 için en büyük kalan y/D sırasıyla yaklaşık 3,703; 2,973; 2,383. Bu teşhis FFT temellidir. Dolayısıyla yalnız filtre büyüklüğünü sınırlamak yerine o frekanslarda ne kadar kaynak enerjisi bulunduğunu kontrol etmek gerekiyor.

## Bir sonraki somut hedef

Sabit sayıda tepenin her şeyi taşımasını varsaymak yerine, büyük filtre değerlerine düşen toplam kaynak enerjisini ölçeğe göre kontrol etmek daha uygun hedef. Bu turdan sonra, keşif amaçlı evaluate_bounds.py ile bu yöndeki daha güçlü katman-başına kuyruk koşulunu da ölçtük; bunlar önceden sabitlenen deneyin ayrı, sonradan seçilen tanılarıdır. 1/u^2 kuyruk zarfı için gereken katman-başına sayısal C, r=12'de yaklaşık 3,98 iken r=20'de 20,04 oldu. Bunu sabit C lehine kanıt olarak okumuyoruz.

Katmanları kendi W_flat ağırlıklarıyla birlikte ele almak daha az talepkâr bir yeter koşul verir. z_i=y_i/D ve kaynak kütlesi e_i/S ile, bu ağırlıklı dağılımın u üzerindeki kuyruk kütlesi M(u) olsun. Tam katman-keki özdeşliği W/W_flat = integral_0^infinity M(u) du'dur. Eğer u>=1 için uniform M(u)<=C/u^(1+epsilon) kanıtlanabilirse, W<=(1+C/epsilon)W_flat çıkar. Bu bir koşullu indirgemedir; gerekli aritmetik kuyruk sınırı henüz kanıtlanmadı. Öncelik, küçük toplam ağırlıklı kötü katmanların etkisini ayırıp gerçek kaynak–filtre ortak yoğunlaşmasına bir sınır bulmaktır.

Walsh/Krawtchouk katsayılarıyla döngüsel Fourier katsayıları arasındaki doğrudan aktarım da ANALYTIC_REVIEW.md'de somut t=4,j=2 örneğiyle denetlendi: parite kodlamasının bijektif olması, XOR ile döngüsel toplamı aynı yapmaz. Doğru toplam enerji kimliği tek tek frekanslara ilişkin iddiayı doğrulamaya yetmez.

## Yeniden üretim ve sınırlar

Python + NumPy ile probe.py; ardından evaluate_bounds.py çalıştırılır. PLAN.json, RESULTS.json, BOUND_RESULTS.json, INDEPENDENT_RESULTS.json ve iki denetim metni birlikte okunmalıdır. Ana toplamların sonlu doğrulaması, frekans paylarının sayısal tanısı ve koşullu analitik öneri birbirinden ayrıdır. Yeni ücretli sağlayıcı çağrısı yapılmadı. Önceki kapalı B4 yürütmeleri çalıştırılmadı.
