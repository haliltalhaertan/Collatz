# Collatz projesi: bütünsel değerlendirme ve yön seçimi

8 Eylül 2026. Bu belge bir araştırma değerlendirmesidir; yeni bir kanonik bilimsel aşama veya bütün teoremlerin yeniden denetimi değildir.

## Sonuç

Proje boşa gitmiş değil. En güçlü varlıkları, belirli varsayımlar altındaki denetlenmiş eşitsizlikler, tam aritmetik özdeşlikler ve hangi kestirmelerin çalışmadığını gösteren karşı örnekler. Fakat bütün çalışmalar tek bir tamamlanmak üzere olan ispat zinciri oluşturmuyor. Son konuşmalarda özellikle analitik yardımcı hedef ile Collatz sonucunun arasındaki mesafeyi yeterince görünür tutmadık.

Sonlu birleşme kuralı aramasını ana yol olarak büyütmeyi önermiyorum. Analitik tarafta da yalnızca mevcut C/R yardımcı sınırına devam etmek otomatik tercih olmamalı. Önce asıl aralık-sayımı hedefinde hangi Fourier katkılarını gerçekten kontrol etmek gerektiğini yazmak daha yüksek bilgi değerine sahip görünüyor.

## İncelemenin kapsamı

- Yerel HEAD:2461573739147763eb011faf03c344370a184d69; ayrık çalışma kopyası.
- Güncel arşiv ZIP envanteri:1008 üye.50 seçilmiş kaynak, dosya kimliği ve hash ile metin erişimine hazırlandı; aralarında kopyalar ve eksik kaynak kayıtları var. Bu sayı50 bağımsız teoremin yeniden ispatlandığı anlamına gelmiyor.
- CP02–CP13 sonuç bölümleri ve başarısız yöntemler; CP17 asıl teorem alanı ve son bağımsız denetim; CP18–CP20 ana kontrol belgeleri; D/E modülleri; güncel yönetici kararları ve kapalı B4 durumu incelendi.
- 8 Eylül analitik, birleşme, değiştirilmiş haritalar ve literatür klasörleri; ilgili ispat metinleri ve araştırma kodları incelendi.
- İki alt ajan analitik ve deterministik/erken-tarih hatlarını bağımsız okudu. Asıl araştırmacı arşiv, teorem alanları, yönetici durumu ve birleşik çıkarımları karşılaştırdı.
- Bütün1008 üyenin satır satır okunması, bütün ispatların sıfırdan doğrulanması veya eski araştırma deneylerinin yeniden çalıştırılması yapılmadı. Yeni ücretli model çağrısı yok.

## Araştırma tarihinin matematiksel anlamı

| Dönem | Kalıcı kazanım | Sınır |
|---|---|---|
| CP02–CP08 | Kritik büyüme, slack, sonlu valuation dizileri ve en küçük gerçekleştiricilerin tam ilişkileri; birçok doğal yerel yaklaşımın sınırı | Modüler ve gerçek koordinatlar bazen aynı bilgiyi yeniden ifade ediyor; sonlu uyumluluk sonsuz pozitif gerçekleştirici sağlamıyor |
| CP09–CP13 | Ters geçmişleri aritmetik son sınıflara göre ağırlıklı sayma; harmonik seyrekliğin ve katsayısının iyileştirilmesi | Örtüşen yolların kayıpları bağımsız çarpılamıyor; yalnız collision/yerel filtre yeterli değil |
| CP17 | Pozitif, tekrarsız, tek-sayı Syracuse yörüngesinde H_N/log log N için K17<2.742882<3; s_k-log_2 k değerinin limsup'u sonsuz | Bütün kaçışı veya başka döngüleri dışlamaz; s_k/log_2 k oranı için1'den büyük alt sınır değildir |
| CP18–CP20 | Belirli sembolik kaçış ailelerine karşı basınç, kelime karmaşıklığı, kalıntı stabilizasyonu ve tekrar-aralığı kısıtları | Global kritik-log yasası gibi güçlü varsayımlar bütün olası istisnalara otomatik uygulanmaz |
| E0–E7R | Tam koşullu dağılım/Fourier normal biçimleri, bazı yanlış daralma iddialarının çürütülmesi | Koşullu kompleks üst sınır, sıfırdan farklı profil ve gerekli aktarım teoremleri ayrı ayrı açık |
| 8 Eylül analitik | Belirli düşük-gezi olasılığının Theta(1/R) ölçeği, sabit yükseklik bandında daralma ve rezonans ayrıştırması | Bütün aritmetik fazların toplam katkısı kontrol edilmedi; pozitif üst zarf kompleks ifadeye eşdeğer değil |
| 8 Eylül birleşme | Sonsuz aileler için denetlenebilir küçük-kontrol-hedefi sertifikaları |55.210 eleme yalnız en küçük kontrol-istisnası adayları içindir; kalanları tüketen genel mekanizma yok |

CP14 yalnız yeniden oluşturulmuş özet olarak tutuluyor. CP15 kurtarma DOCX'inin document.xml içinde metin yok. CP01/CP05 kaynak boşlukları mevcut. Bu boşluklar uydurularak doldurulmadı. CP17 asıl bağımsız paket, erken özet boşluklarından ayrı olarak mevcut.

## Üç ayrı matematiksel açık

### 1. Sonlu uyumluluktan tek bir gerçek başlangıca geçiş

Her100,1000 veya milyon adımlık istenen davranış için ayrı bir başlangıç bulmak, bir başlangıcın bütün sonsuz davranışı taşıdığını göstermez. İç içe kalan sınıfları2-adik bir nesne tanımlayabilir; bunun sıradan pozitif tam sayı olması ayrıca kanıtlanmalı. CP18'in uyarısı budur.

Bu, sonlu ispatların imkânsız olduğu anlamına gelmez. Bütün başlangıçlara uygulanabilir ve sonsuz ilerlemeyi yasaklayan bir kural sistemi gerçekten çözüm sağlayabilir. Eksik olan yalnız örnek sayısı değil, bütün kapsamı bağlayan koşuldur.

### 2. Marjinal sayım bilgisinden yollar arası bağımlılığa geçiş

CP20'nin basınç koşulları bazı sembollerin sayısını kontrol ediyor. D1-E ise farklı konumlardaki sembollerin birbirine eşit olup olmadığını gerektiriyor. Aynı sembol sayısına sahip dizilerin tekrar yapıları çok farklı olabilir. Bu iki bilgi arasında ispatlanmış yeterli bir köprü yok.

Eski, hâlâ anlamlı soru: uzun bir platoda bütün tehlikeli tekrarları bozmanın eşzamanlı maliyeti nedir? Tek bir tekrarı bozmak için bir değişiklik yetebilir; birçok örtüşen tekrarı birlikte bozmak için ne gerektiği açık. Bu, genel 'Sturmian tekrarlarını kullanalım' fikrinden daha somut, fakat kendiliğinden umut vadeden bir çözüm değildir.

### 3. Tek tek Fourier katsayılarından asıl aralık ölçümüne geçiş

E1, bütün ilgili frekanslarda güçlü üstel küçülmeyi yeterli bir kestirme olarak seçmişti. E2, bazı frekanslar polinom ölçeğinde kalıyor göründüğü için bu kestirmeyi çürütecek alt sınıra yöneldi. E3–E6'daki profil ve C/R işleri bunun ara parçalarıdır.

Dolayısıyla bu yan programın başarıya ulaşması öncelikle belirli bir yöntemin sınırını kanıtlar; Collatz'ı kanıtlamaz. Böyle bir sonuç bağımsız araştırma değeri taşıyabilir, ancak hedefi açıkça belirtilmeli.

## Bu incelemeden çıkan somut yön

WEIGHTED_SPECTRAL_BUDGET.md asıl aralık sorusunun tam Fourier toplamını yazar. Bir katsayının büyüklüğüne, aralığın o frekanstaki ağırlığı da çarpılır.

Özel kayıtlı frekans için xi_r/3^r=2^(-12-{alpha r}). Bu oran sıfıra yaklaşmadığından, aralık Fourier ağırlığı4096 ile sınırlıdır. Katsayı hakkında yalnız|phi|<=1 kullanılsa bile bu tek terimin uniform aralık kütlesine göre katkısı4096/L'den büyük değildir. Eşlenik frekansla birlikte8192/L sınırı gelir.

Bu genel bir anti-concentration sonucu değil: diğer frekansların sayısı, konumu ve toplam ağırlığı açık. Fakat L büyüyen aralıklar için projeyi yönlendiren özel sorunlu frekansın, asıl aralık hedefini tek başına engellemediğini tam olarak gösterir. Bu tek frekansı anlamak için zor bir polinom asimptotiğini tamamlamak zorunda olmayabiliriz. Ayrı alt ajan kontrolü4096/L ve eşlenik çift için8192/L hesabını bu dar kapsamıyla doğruladı; tüm spektruma ilişkin sonuç çıkarılmadı.

Bu nedenle en mantıklı yeni hedef adayı: gerekli kütle/aralık aralığında, istisnai frekansların toplam ağırlığını ve geri kalan frekansların katkısını birlikte sınırlamak. 'Ortalama küçülme' gibi belirsiz bir hedef yerine açık bir toplam ve açık bir hata bütçesi kullanılmalı. Şimdilik bunların ikisi de kanıtlanmış değil.

## Öncelik sırası ve durma ölçütleri

1. **Asıl ölçüme dön:** Fourier ağırlıklı toplamda yeterli olacak kesin bütçeyi E1'in ilgili sonucuna bağla. Sabit sorunlu frekansların ucuz kontrolünü, geri kalan açık spektrumdan ayır. Yeni fikir bu toplamın bağımlılıklarını açıklamıyorsa büyük frekans taraması başlatma.
2. **Bağımsız yan-teorem hedefini adlandır:** Rezonans karşıteoremi isteniyorsa, bir sonsuz alt-dizide polinom alt sınır yeterli olabilir; bütün profili kanıtlamak daha güçlü bir hedeftir. Pozitif hayatta-kalma alt sınırını kompleks alt sınır yerine kullanma.
3. **Eski ispat varlıklarını koru:** CP17 ve Task6/7 gibi sonuçları doğru hipotezleriyle tek bir okunabilir teorem/bağımlılık dizisinde tut. 'Yeni proje hesabı' ile literatürde yenilik iddiasını ayır. Bu inceleme yenilik önceliğini belirlemiyor.
4. **Birleşmeyi sınırlı yan hat tut:** Aynı kontrol kümesi/global minimum deneyi iptal edilmeli; tamamen triviyal sonuç verir. Birleşmede devam ancak belirli kalan aileye tümüyle uygulanan yeni bir mekanizma veya sınırlı bir şablon için gerçek engel teoremi vaat ediyorsa anlamlıdır.
5. **Eski başarısız fikirleri isim değiştirerek tekrar etme:** Asallık, daha çok yerel modül, bağımsız sayılan örtüşen bloklar, yalnız slack'e dayalı potansiyel ve mekanik kelime ekstremalliği geçmişte sınandı. Yeni öneri önce hangi eski karşı örneği hangi ek bilgiyle aştığını söylemeli.

## Denetimde saptanan düzeltmeler

FINDINGS.md ayrıntıları içeriyor. En önemlileri:

- Son sohbet önerim olan aynı-S/global-minimum karşılaştırması geçersiz araştırma tasarımıdır; mevcut sertifikaları bozmaz.
- Eski ek D1 denetiminde zayıf bölünebilirlik ile tam valuation gerçekleştirme karışmış. w=(1) için r1=1 ama en küçük tam gerçekleştirici3'tür. İncelenen sonraki özetlerde ana sonuçlara yayılmış bir hata saptanmadı.
- Aynı ek koddaki [1,1,2] örneklemesinin ortalaması4/3; log_2 3 değildir. O tipiklik yorumu kullanılmamalı.
- CP17 özetindeki teorem, asıl dosyanın pozitif/tekrarsız/tek-yörünge alanıyla okunmalı. Döngüler hakkında teorem değildir.

## Arşiv ve çalışma durumu

Arşiv hash/boyut/CRC/1008 üye sayısı,85 depo dosyası ve22 kayıtlık günlük zinciri doğrulandı. Kanonik devir doğrulayıcısı bu ayrık çalışma kopyasında dal kontrolünde duruyor; PASS denmedi. Ek olarak durum dosyasındaki81 arşiv yolunda karakter kodlama bozulması bulundu. Yalnız teşhis amacıyla çözümlenen81 yolun tamamında içerik hash'i eşleşiyor. Dosyalar kayıp değil; yol metaverisi hatalı. Onarım yapılmadı.

B4 V2'nin kapanışı matematik başlamadan oluşmuş girdi-bütünlüğü hatasıdır. Matematiksel yaklaşımın çürütülmesi değildir. Bu inceleme hiçbir kapalı aşamayı çalıştırmadı veya yeniden açmadı.

Yeni inceleme dosyaları yereldir. Drive/GitHub'a yükleme veya yeni kanonik kabul işlemi yapılmadı.
