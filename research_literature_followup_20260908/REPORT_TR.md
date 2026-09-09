# Açığa yönelik literatür taraması

8 Eylül 2026. Birincil kaynakların seçilmiş teorem, tanım ve ispat bölümleri incelendi; bütün makaleler satır satır yeniden ispatlanmadı. Yeni ücretli çağrı, alt ajan veya uzaktan yayın yok.

## Sonuç

Hazır bir aralık-sayımı veya gerçek önek korelasyonu teoremi bulamadım. Üç kullanışlı bağlantı var: işaretleri koruyan Collatz operatörleri, Boolean küpte moment sınırları ve paradoksal blokların harmonik maliyeti. Tamamlayıcı parite simetrisi de bir kontrol aracı sağlıyor, fakat bizim aralık ve çokluk şartlarımızı otomatik korumuyor.

## Kaynaklar ve aktarım sınırları

1. **John Leventides–Costas Poulios, Koopman operators and the 3x+1-dynamical system.** [Birincil metin](https://arxiv.org/html/2010.12987). §§7–10; özellikle Teorem8.8, M_k M_k*=I; Teorem8.11 izometri; Teorem10.3 bir eşdeğerlik. İşaretli yapıyı korumak için ilgili. Norm koruma daralma değildir; ağırlık ve küçük-aralık kısıtlarımız için nicel projeksiyon tahmini hâlâ gerekli. Makalenin son eşdeğerliği hazır bir çözüm sayılmamalı.

2. **Kenneth G. Monks–Jonathan Yazinski, The autoconjugacy of the 3x+1 function (2004).** [Yazar nüshası](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf), [yayın kaydı](https://www.sciencedirect.com/science/article/pii/S0012365X03001250). Parite tamamlayıcısı Omega; eşitlik2.1. Kaynak Örnek2'de Omega(3)=-4/9 verir. Pozitif tam sayıları veya küçük gerçek aralıkları koruyan bir eşleme değildir. Sonlu uygulama kontrolü aşağıda.

3. **Naomi Kirshner–Alex Samorodnitsky, A moment ratio bound for polynomials and some extremal properties of Krawchouk polynomials and Hamming spheres (2019).** [Birincil PDF](https://arxiv.org/pdf/1909.11929). Giriş(1)–(2), Teorem1.3 ve Corollary1.4; dereceye bağlı moment sınırları ve Krawchouk yapısı. Bu teoremlerde gerekli derece veya spektral katman kontrolü bizim işaretli sayım fonksiyonumuz için kanıtlanmış değil. Güçlendirilmiş teoremi parametre şartlarını denetlemeden uygulamıyoruz; aşağıda yalnız standart hiperkontraktif sonuç kullanılıyor.

4. **Olivier Rozier–Claude Terracol, Paradoxical behavior in Collatz sequences.** [İncelenen v2](https://arxiv.org/html/2502.00948v2). Teorem3.2, sonsuz durma zamanından sonsuz paradoksal blok üretir; Corollary3.3, başlangıcı2'den büyük bu blokların sonluluğunu yeterli kılar. Corollary4.2 harmonik ortalama kısıtı verir. Ekim2026 dergi sayı tarihi günümüzden ileri olduğundan inceleme v2 önbaskısına dayanır. Bu bloklar C<1 olduğu halde T^j(n)>=n sağlar; sonluluk iddiası kanıtlanmış değildir.

5. **Tong Niu, Parity vectors and paradoxical sequences in the accelerated Collatz map (Mayıs2026).** [v1](https://arxiv.org/html/2605.13886v1). Teorem2, her sabit parite kelimesinin tek kalıntı sınıfını; Teorem4 sabit uzunluk sayımını; Teorem7 sınırlı uzunlukların yoğunluk sıfırını ele alır. N<2^k rejiminde kelime başına tavan1 kalır. Sabit K sonucu, büyüyen uzunlukta ihtiyaç duyduğumuz uniform üst sınıra dönüşmez. Diğer sayısal iddiaları yeniden doğrulamadım.

6. **Functional analysis approach to the Collatz conjecture.** [v9 metni](https://arxiv.org/html/2106.11859). §3'te kök-birlik iptaliyle integral değişmezliği; Remark2.6'da özel yörünge sabit noktaları ile diğer operatör sabit noktalarının ayrımı. Genel bir operatör sabit noktası bulmak yörünge sınıflandırmasını tamamlamıyor. Bu kaynak ana sayım açığımız için doğrudan bir sınır sağlamadı.

Ek tarama: [Angermund, 2025](https://arxiv.org/abs/2506.19115) aritmetik ilerlemelerle parite ayrışımı için ilgili bir önceki çalışma; özeti incelendi, bizim modüler durum birleştirmesiyle algoritmik eşdeğerlik veya yenilik önceliği kararı verilmedi. [Tao'nun ana sonucu](https://arxiv.org/abs/1909.03562) logaritmik yoğunluk kapsamındadır; bu taramada yeniden bir bireysel-yörünge teoremi gibi kullanılmadı.

## Kendi aktarım kontrolümüz: tamamlayıcı simetri afin değil

Q_t(x), ilk t parite bitlerini bir t-bit kelimeye çevirsin. Tam kalıntı periyodunda Q_t bijektiftir. Sonlu tamamlayıcı

    Omega_t(x)=Q_t^(-1)((2^t-1) XOR Q_t(x))

bir involüsyondur ve K_t(x)+K_t(Omega_t(x))=t. check_transfer.py bunu t=1..5 için tam kontrol etti. Mod8 tablosu:

    x:       0 1 2 3 4 5 6 7
    Omega:   7 2 1 4 3 6 5 0

Bir afin ax+c olsaydı ilk iki değer c=7,a=3 zorlayacaktı; x=2'de5 çıkardı, gerçek değer1. Dolayısıyla bu simetriyi bütün afin kuyruk ailelerine tek bir afin yeniden indisleme olarak uygulayamayız. Bu bulgu başka ağırlıklı/gruplu simetrileri dışlamaz. Ayrıca tam tamamlayıcı tek başlangıcı çift başlangıca ve sabit ağırlığı tamamlayıcı ağırlığa götürür; bizim sayılan kümemiz değişmez değildir.

## Kendi aktarım kontrolümüz: yüksek moment bedava değil

Ötelemeyi t-bit vektör olarak yazıp f(a)=G(a)/B-1 alalım. Boolean Walsh derecesi d ise standart hiperkontraktivite

    ||f||_22 <= 21^(d/2)||f||_2

verir. Önceki yeterli koşuldaki M22=E|f|^22 olduğundan

    M22 <= 21^(11d)(V/B^2)^11.

Bu, düşük derece ve L2 kontrolünü yüksek momente çevirebilecek bir kapıdır. d doğrusal büyürse katsayı üstel olabilir; yalnız d<=t kullanmak genel olarak hedefi sağlamaz. Krawchouk/Hamming yapısı parite koordinatlarında basittir; parite kodlamasının doğrusal olmayan bileşkesi dereceyi korumak zorunda değildir.

Önceki dört G panelini tamsayı Walsh dönüşümüyle inceledim. Yeni büyük yörünge taraması yok. Merkezlenmiş fonksiyon dereceleri:

|r|t|gerçek Walsh derecesi|
|---:|---:|---:|
|5|1|1|
|10|3|2|
|12|4|4|
|14|5|5|

Her panelde Walsh katman enerjileri tam olarak önceki varyansı verdi. Örneklerde tüm fonksiyonun otomatik olarak çok düşük dereceli olduğu söylenemez. Bu, büyüyen r için derece oranının alt sınırı veya yaklaşık düşük derece teoreminin çürütülmesi değildir. Yaklaştırma düşünülürse kalan kısmın gereken momentte ayrıca kontrolü gerekir. Sonlu normalize22.momentler de JSON'a kaydedildi; asimptotik kanıt sayılmadı.

## Eski CP17 ile somut birleşim: paradoksal blokların harmonik bütçesi

Bu bölüm kaynaklardaki blok fikrinden esinlenen kendi çıkarımımızdır. CP17'nin yalnız tekrarsız pozitif tek-sayı yörüngesi alanındaki kayıtlı H_N üst sınırını kullanır; bu tur bütün CP17 ispatı yeniden denetlenmedi. Notasyon ve sonuç, research_project_review_20260908/CP17_PROOF_REFERENCE.md §1'den kontrol edildi.

Tek-sayı yörüngesinde [u,v) bloğu için

    delta_(u,v)=A_v-A_u-alpha(v-u)>0,
    n_v>=n_u

olsun. Tam çarpım özdeşliği

    n_v/n_u = 2^(-delta_(u,v)) product_(u<=i<v)(1+1/(3n_i))

verir. Logaritma ve log(1+x)<=x ile

    delta_(u,v) <= (1/(3 ln2)) sum_(u<=i<v)1/n_i.

Seçilen bloklar [0,N) içinde olsun ve her indeks en fazla L_N blokta kullanılsın. Toplayınca

    sum_blocks delta_(u,v) <= L_N H_N/(3 ln2).

CP17'nin kayıtlı sonucunu uygularsak sağ taraf en fazla

    L_N (K17+o(1)) ln ln N/(3 ln2).

Özellikle ayrık ve delta>=delta0>0 olan blokların sayısı O(ln ln N). Bu dar sonuç bu alanda geçerlidir; döngülere uygulanmaz. Delta keyfi küçülebilir ve örtüşme çokluğu sınırsız olabilir. Rozier–Terracol'ün ürettiği bloklar farklı başlangıçların 2 kuvvetiyle ölçeklenmesini kullanabilir ve büyük ölçüde örtüşebilir; yukarıdaki aynı-yörünge bütçesine çokluk kontrolü olmadan aktarılamaz.

Bu nedenle asıl yeni araştırma sorusu: varsayımsal bir istisnadan, kontrol edilen örtüşme çokluğu L_N ile, toplam delta bütçesini aşan bir blok ailesi çıkarılabilir mi? Kaynaktaki sonsuzluk sonucu bunu tek başına sağlamaz. Ayrıca bizim mevcut kritik tablomuz A=floor(alpha r) kullanıyor ve delta<=0 tarafındadır; paradoksal blokla özdeş değildir. Pozitif delta için tavan ve ilgili komşu kütleler ayrı ele alınmalı. Mevcut sayım köprüsü zaten sabit kritik bandın tümünde uniformluk istiyor.

## Araştırma kararı

Ana sayım hattını yeni bir literatür başlığı uğruna terk etmiyorum. En somut seçenek, G-B'nin işaretleri korunan dyadik/Boolean katman yapısını incelemek ve kullanılabilecek derece/katman bütçesini kanıtlamaktır. Koopman izometrisini daralma sanmak veya her katmanın mutlak katkısını erken toplamak yanlış olur.

Bağımsız yan soru olarak harmonik blok bütçesi korunmalı: yalnız 'sonsuz paradoksal blok var' değil, 'ne kadar bağımsız harmonik yük taşıyorlar?' sorusu eski sonuçlarımızı yeni literatüre bağlar. Şu an iki yolda da eksik lemma açık; yeni yörünge dışlaması, yeni asimptotik sayım üst sınırı veya genel Collatz kanıtı yok.
