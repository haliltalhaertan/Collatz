# Araştırma devamı — kısa blok sorusunun sonucu

Önceki karşıörnek yalnızca belirli bir c=6/5 blok katsayısını kapsıyordu. Bu turda sonuç güçlendirildi: başlangıçtan hizalı ayrık blok ızgarasında L_R=floor(c log R) seçimi, HER sabit c>0 için aynı engelle karşılaşıyor. Daha küçük bir sabit katsayı seçmek yardımcı C/R Laplace tahminini kurtarmıyor.

Gerçek erişilebilir G son-eklerinden kurulan bir dizide, sabit A(c,eta,lambda)>0 için

E exp(-lambda N_C)>=A L_R/R.

İspattaki yeni adım, her tekil bloğun yeterli toplamı taşıması koşulunu kaldırıyor. Bunun yerine sabit k komşu bloğun her penceresinde yeterli toplam bulunuyor; ilk k bloktan birinde uygun aktarım noktası seçiliyor. Dönüşüm birebir olmak zorunda değil: en fazla k farklı kaynak aynı sonuca gidebildiği için ağırlık kaybı sabit bir çarpanla kontrol ediliyor. Bu değişiklik önceki blok-uzunluğu kısıtını kaldırıyor.

İki yerleşik alt ajan tam birleşik kanıtı bağımsız denetledi ve matematiksel düzeltme istemeden kabul etti. Ana ajan gerçek son-ek yasasını, eşik aktarımını ve sabitlerin R'den bağımsızlığını yeniden kontrol etti. Bu sonuç model anlaşmasına dayalı bir çıkarım değil; gösterilmiş ağırlık ve olasılık eşitsizliklerine dayanıyor.

Ayrı bir sonuç, L_R=(log R)^p mertebesinde 1/2<p<1 için de engeli gösteriyor. Bunun kanıtı ayrı dosyada; L_R=O(sqrt(log R)) için başarı veya başarısızlık iddiası yapılmıyor.

Bu yardımcı sayım ailesinin başarısızlığı kompleks faz iptalinin başarısızlığı değildir. XUB ve Collatz açık. Sonraki çalışma, seçilmiş uzun blok başlangıçları yerine her çiftteki gerçek daralma fırsatlarını sayan daha sık örneklenen istatistiğe dönmek. Bunun tam sonlu özyinelemesi NEXT_ACTION.md dosyasına yazıldı; henüz gereken C/R sınırı kanıtlanmadı.

Bu tur OpenRouter/Sol'a yeni istek gönderilmedi. Yerleşik alt ajanlarla açık adım kapanınca ek çağrıya ihtiyaç kalmadı. Önceki toplam harcama 0,061356 USD olarak kaldı; 2 dolarlık bütçeden 1,938644 USD var. Açık OpenRouter çağrısı yok.

Tam kanıt ALL_LOG_COEFFICIENTS_PROOF.md, kısa-ölçek uzantısı SUBLOG_COROLLARY.md, bağımsız denetim INDEPENDENT_AUDIT.md ve sonraki adım NEXT_ACTION.md dosyalarında. Orijinal kanonik dosyalar veya mühürlü aşamalar değiştirilmedi.
