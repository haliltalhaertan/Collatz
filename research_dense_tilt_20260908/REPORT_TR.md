# Doğrudan yoğun Laplace tahmini — 8 Eylül 2026

Bu tur ana C/R üst sınırını kanıtlamadık. Fakat fırsat sayısından gerçekleşen daralma sayısına geçişin doğru biçimini kesinleştirdik ve iki hatalı kısa yolu eledik.

Doğru dönüşüm, yolların olasılıklarını Q adı verilen açık bir geçiş yasasıyla değiştiriyor. Bu yeni yasada beyaz fırsatların doğrudan üstel ortalaması C/R ile kontrol edilirse hedefe kayıpsız geçiliyor. Q aynı uç toplamını koruyor, fakat düzgün bileşim veya döngüsel değişmezlik yasası değil. Önceki sayım sonuçları ona otomatik aktarılamaz.

Bu ayrım sadece teknik bir uyarı değil: iki bağımsız yazı-tura adımlı kesin bir karşıörnek, her fırsatta başarı şansı sabit olsa bile eski yasa altındaki fırsat ortalamasını doğrudan yerine koymanın yanlış olduğunu gösteriyor. Örnekte 11/16 büyüklüğündeki gerçek ortalama, öne sürülen 21/32 üst sınırından büyük. Bu bir çıkarım ilkesine karşıörnek; Collatz dizisine karşıörnek değil.

Eski olasılık yasasında kalmak için Holder eşitsizliği kullanılabiliyor, fakat bu yöntem kuvvet kaybediyor: C/R bilgisi doğrudan C/R sonucuna dönüşmüyor. Ayrıca yalnızca kalan uzunluğa bağlı C/(R+1) biçimindeki basit üst çözüm, gerçekten erişilebilen düşük durumlarda eşitsizliği sağlayamıyor. Sonraki deneme yükseklik ve faz bilgisini taşımak zorunda.

İki yerleşik alt ajan doğru dönüşümü ayrı ayrı türetti; ana ajan uyarlamalı fırsat karşıörneğini ve basit üst-çözüm engelini ekledi. Belgede her yasanın ve eşitsizliğin kapsamı açıkça yazıldı. Doğrudan yoğun Laplace üst sınırı, XUB ve Collatz hâlâ açık.

Yeni Sol/OpenRouter çağrısı yok; toplam harcama 0,061356 USD olarak kaldı. Bu turdaki dosyalar yereldedir, daha önce onaylanan 20 dosyalık Drive/GitHub V1 paketine dahil değildir.
