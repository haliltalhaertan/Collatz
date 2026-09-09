# Alanlar arası tarama: işe yarayan mekanizma ve aktarım engeli

8 Eylül 2026. İki alt ajanla itiraz odaklı tarama. Bu belge bir literatür elemesi ve araştırma tasarımıdır; hiçbir kaynak Collatz'a doğrudan uygulanmış veya bütün ispatıyla yeniden denetlenmiş sayılmıyor. Kaynak açıklamaları ile bizim çıkarımlarımız aşağıda ayrıdır. Yeni ücretli model çağrısı yok.

## Başlangıç hedefi

Güncel hedef göreli düzgün dağılım hatası o(1) değil, Q_(r,A)(b)<=2^((h_*+b-alpha+lambda+o(1))*r). Kritik-log sınıfına koşullu aktarımda lambda<alpha-h_*-b(1-1/kappa) yeterli. Bu yüzden her bağlantıya aynı soru soruldu: bu SAYIM hedefindeki hangi eşitsizliği sağlayacak?

## 1. İstatistiksel fizik, nadir olaylar ve optimal kontrol

Kaynak: Chetrite–Touchette, [Nonequilibrium Markov processes conditioned on large deviations](https://arxiv.org/abs/1405.5157), özellikle Doob dönüşümü ve koşullandırma bölümleri; [Variational and optimal control representations](https://arxiv.org/abs/1506.05291). Çalışmalar koşullandırılmış süreçleri değiştirilmiş süreçler ve kontrol/entropi maliyetleriyle ilişkilendiriyor. Uzun-zaman eşdeğerliği için büyük sapma ve spektral/konvekslik koşulları bulunuyor; bunları bizde kanıtlamadık.

Bizim çıkarımımız: sonsuz-zaman teoremini taşımadan, SONLU ve TAM koşullu blok yasası için geriye doğru bir başarı olasılığı/sayısı yazabiliriz. Her durum için gelecekte hedef aralığa ulaşabilecek devamların sayısını üstten sınırlayan bir F bulursak, yerel eşitsizliklerin doğrulanması başlangıçtaki Q'yu üstten sınırlar. COUNT_CERTIFICATE.md bunun açık durumunu, geçişini, terminal koşulunu ve geriye-indüksiyon kanıtını veriyor.

Bu, yeni bir anti-concentration teoremi değil. Asıl zorluk F'yi küçük bir aritmetik formülle temsil etmek. Yalnız kalan adım ve toplam kütleyi tutmak, kalıntıyı tamamen unutmak, en az bir başarılı kelime varsa tüm kelime sayısından daha iyi sınır veremiyor. Dolayısıyla bu öneri eski drift/slack-only başarısızlıklarını atlamıyor.

Öncelik: orta; gerçek sayım olayına doğrudan bağlı olduğu için küçük bir sertifika denemesi anlamlı. Büyük durum uzayını yalnız yeniden hesaplamak ilerleme sayılmamalı.

## 2. İklim modellemesi: nadir yolları hedefleyerek örneklemek

Kaynak: Wouters–Bouchet, [Rare event computation in deterministic chaotic systems using genealogical particle analysis](https://arxiv.org/html/1511.02703v2), özellikle giriş, §2.2 ve §5.2.2. Lorenz '96 modelinde seçme/çoğaltma ile nadir olay örneklemesi; zaman-bağımlı ağırlıklar; deterministik kopyaların ayrılması için küçük pertürbasyon ve bunun yanlılığının kontrolü tartışılıyor.

Bizim çıkarımımız: rastgele başlangıçların çoğunu izlemek yerine, küçük endpoint olayına katkı veren değerleme kelimelerini hedefleyebiliriz. Ancak Collatz tam sayılarına küçük gürültü eklemek aynı problemi korumaz. Örnekleme, başlangıç tam sayıları yerine sonlu pozitif bileşim uzayında yapılmalı; kalan kütleye koşullu TAM geçiş ağırlıkları korunmalı. Öneri dağılımı değişirse olabilirlik oranı ve normalizasyon tutulmalı.

Kullanım: nadir yolların hangi aritmetik özellikte toplandığını keşfetmek. İyi görünen örnekleme çıktısı üst sınır kanıtı değildir; aynı yolların tekrar tekrar çoğalması belirsizliği küçültmüş gibi gösteremez. Yakın zamanda başarısız bulunan ölçü-değiştirme karşılaştırmasını bu adla tekrar kullanmamalıyız.

Öncelik: yardımcı araç, ispatın yerine geçmez. Bu tur yeni parçacık deneyi başlatılmadı.

## 3. Bilgi kuramı ve sinyal işleme: güçlü görünen genel teoremlerin ölçeği yetmiyor

Kaynak: James R. Lee, [Covering the large spectrum and generalized Riesz products](https://arxiv.org/html/1508.07109v2), Teorem 3.3. Büyük Fourier spektrumu, entropiyle kontrol edilen sayıda karakterin işaretli toplamlarıyla örtülüyor. Bu doğrudan bir spektrum-kardinalite teoremi değil.

Bizim ölçek hesabımız: q=2^(alpha*r), kelime sayısı N=2^(h_*r+o(r)), yoğunluk f=qp. Uç destek en fazla N olduğundan Ent(f)=ln(q)-H(p)>=(alpha-h_*)r ln2+o(r). Gerekli epsilon=2^(-delta*r) için Lee sınırının en iyimser ölçeği bile r*2^(2delta*r). Bu, ihtiyaç duyduğumuz küçük istisna sayısını sağlamıyor. Döngüsel grupta bir ilkel elemanın bütün grubu üretmesi de 'az üreteç=az frekans' kestirmesini geçersiz kılıyor.

Sinyal işleme açısından temel Parseval hesabı: sum|phi|^2=q*sum p^2. Dolayısıyla #{|phi|>epsilon}<=q*sum p^2/epsilon^2. İyimser sum p^2~1/N varsayımı altında bile üst sınırın üssü alpha-h_*+2delta. Örneğin b=1.2, lambda=0 için yaklaşık .84924; önceki kappa=1.053 kalibrasyonunda izin verilen kayıp yalnız .01892 civarı. Ayrıca 1/N değeri gerçek dağılım için kanıtlanmış değil.

Öncelik: standart entropi veya ikinci moment tek başına çözüm adayı olmaktan elendi. Aritmetiğe özel, belirli frekans bölgelerine veya ağırlıklara odaklı ek kazanç gerekli. Bu, bütün bilgi kuramı yöntemlerinin imkânsızlığı iddiası değil.

## 4. Kuantum kaosu: her ölçekte boşluk fikri

Kaynak: Bourgain–Dyatlov, [Spectral gaps without the pressure condition](https://arxiv.org/html/1612.09040), §1.3, §2.2 ve fraktal belirsizlik teoremi. Düzenli fraktal kümelerin çok ölçekli geometrisi Fourier yoğunlaşmasına kısıt getiriyor; yalnız toplam küme büyüklüğü kullanılmıyor.

Bizim çıkarımımız: endpoint kümesinin ve sorunlu frekansların yalnız SAYISINI değil, hangi ölçeklerde zorunlu boşluk bıraktığını araştırmak anlamlı olabilir. Fakat sonlu destek küçüklüğü bu geometriyi vermez. '3'e bölünmeyen kalıntılar' şartı da normalize edilmiş gerçek aralıkta her ölçekte sabit göreli boşluk sağlamaz. Sürekli Fourier teoremi sonlu Z/3^r grubuna kendiliğinden taşınmaz.

Öncelik: daha uzun vadeli yapısal soru. Somut ilk sınama, gerçek endpoint tekrarından çok ölçekli boşluk çıkarılıp çıkarılamadığıdır. Henüz böyle bir özellik kanıtlanmadı; kaynak adı Collatz için bir aktarım teoremi yerine kullanılamaz.

## 5. Yazılım doğrulama: yanlış soyut yolu hedefleyerek modeli düzeltmek

Kaynak: Clarke–Grumberg–Jha–Lu–Veith, [Counterexample-Guided Abstraction Refinement](https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Counterexample-guided%20Abstraction%20Refinement.pdf), §§3–4. Soyut karşı örnek somut modelde sınanıyor; sahteyse onu yaratan bilgi kaybı gideriliyor. Sonlu modeldeki tamamlanma argümanı sınırsız tam sayılara taşınamaz.

Bizim çıkarımımız: kalıntı grafiğinde ilk kenar bir t değeriyle, ikinci kenar başka t ile mümkün olabilir; bunları birleştirmek aynı sayının yolunu vermeyebilir. Tüm modülü büyütmek yerine ortak t, eşitsizlik ve bölünebilirlik koşullarını korumak işe yarayabilir. Yeni sayım sertifikasında da kaba F'nin yerel eşitsizliğini bozan SOMUT durum, hangi kalıntı bilgisinin eksik olduğunu gösterebilir.

Sınır: sonlu uyumlu yol sonsuz karşı örnek değildir. En küçük-istisna adaylığından elenen sınıflar bütün yörünge grafiğinden silinemez. Bu yöntem gerekli bir soyutlama varsa kullanılmalı, sırf araç mevcut diye yeni grafik kurulmasına gerek yok.

Ek kaynak: Hoffmann–Aehlig–Hofmann, [Resource Aware ML](https://www.cs.cmu.edu/~janh/papers/hah12cav.pdf). Potansiyeller program maliyeti üst sınırları için kısıtlara çevriliyor. Bizde geçici büyümeye izin veren bir potansiyel için tüm seçilmiş geçişlerde Phi(x)>=1+Phi(x') ve Phi>=0, ayrıca stratejinin her durumda tanımlı olması ve başarılı çıkışlar gerekir. Sadece sırayla farklı ölçülerin azalması yeterli değil.

## 6. Karadelik benzetmesinin gerçek literatür karşılığı: delikli dinamik sistemler

Kaynak: Atnip–Froyland–Gonzalez-Tokman–Vaienti, [Thermodynamic Formalism and Perturbation Formulae for Quenched Random Open Dynamical Systems](https://arxiv.org/abs/2307.00774), 2024 sürümü; bu monografi önceki 2103.04712 çalışmasını genişletip yerine geçiyor. Bir deliğe girince izlemeyi sonlandıran sistemlerde kaçış oranı, transfer operatörü ve hayatta kalan küme birlikte inceleniyor. Bu taramada kapsam/hipotez düzeyinde okundu; monografinin tüm kanıtları denetlenmedi.

Bizim çıkarımımız: 'bilinen havzaya girmeden kalan yollar' için doğru dil bu. Fakat hayatta kalanların ölçüsünün sıfıra gitmesi, kümenin boş olması anlamına gelmez. Çok küçük hatta sıfır ölçülü bir kümede yine istisna bulunabilir. Ayrıca buradaki aralık haritaları, rastgele sürüş ve daralan potansiyel koşulları Collatz için kurulmuş değil. Yeni bir genel daralma varsayımı ekleyerek eski E7 engelini gizleyemeyiz.

Öncelik: sezgiyi doğru sorulara çevirmek için yararlı; doğrudan uygulanabilir hazır teorem saptanmadı.

## 7. Kriptografi: neden hash benzetmesini şimdilik kullanmıyoruz?

Kaynak: Tomamichel–Schaffner–Smith–Renner, [Leftover Hashing Against Quantum Side Information](https://arxiv.org/html/1002.2436v1), klasik Lemma 1. Yeterli min-entropi ve uygun rastgele seçilmiş iki-evrensel hash ailesi çıktı düzgünlüğü verir; garanti aile üzerinden ortalamalıdır.

Bizim endpoint haritamız sabit ve aritmetik. Uygun rastgele tohum/iki-evrensellik yok. Yüksek girdi entropisi, bu belirli haritanın aralıklarda yığılmadığını tek başına göstermez. Buradan elde edilecek somut ödev bir çakışma/iki-evrensellik özelliği olurdu; onu kanıtlamadan 'Collatz hash gibi karıştırıyor' demek döngüsel olur. Şimdilik öncelik verilmedi.

## Sonuç ve bir sonraki küçük adım

En uygulanabilir yeni birleşim: tam koşullu blok yasası + geriye doğru sayım üst sınırı + somut ihlalle soyutlamayı düzeltme. Bu kontrol kuramı ve yazılım doğrulamadan gelen yöntemleri asıl sayım hedefinde buluşturuyor. Fourier hattının yerini aldığı veya daha güçlü olduğu gösterilmedi.

COUNT_CERTIFICATE.md yerel kontrol koşullarını kanıtlıyor. check_count.py, 18 küçük parametre durumunda toplam 1064 kelimeyi bağımsız kapalı form hesabıyla karşılaştırdı; tüm sayımlar tam eşleşti. Bu yalnız formül/uygulama doğrulaması. Henüz sıkıştırılmış bir F, yeni üstel kazanç veya sonsuz-r sertifikası yok.

Devam için ölçüt: önerilen küçük aritmetik durum modeli, tüm yerel eşitsizlikler doğrulanırken kökteki üst sınırı toplam kelime sayısından anlamlı biçimde düşürebiliyor mu? Bunu yapamıyorsa nadir örnekler veya etkileyici grafikler üzerinden başarı ilan edilmeyecek.
