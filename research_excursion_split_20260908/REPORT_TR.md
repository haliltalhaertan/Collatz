# Literatürden somut uygulama — 8 Eylül 2026

Bu tur literatürdeki yerel limit teoremini gerçek koşullu diziye uyguladık. Daha önce yalnızca c/R alt sınırı verdiğimiz belirli daralmasız yol ailesinin toplam katkısının aynı zamanda C/R ile üstten sınırlı olduğunu gösterdik. Böylece bu ailenin tam ölçeği Theta(1/R) oldu.

Aile açıkça sınırlıdır: sabit sayıda başlangıç sıfırı, sabit son çift toplamı, varsa sıfır son tekli ve aradaki bütün yolun düşük bölgede kalması. Tüm daralmasız yollar için üst sınır kanıtlanmadı. Kaynak teoremin sıfır ortalama, sonlu varyans, kaydırılmış kafes ve uç nokta varsayımları ayrı ayrı kontrol edildi; Brownian yaklaşımından doğrudan sonuç çıkarılmadı.

İkinci sonuç, sınırlı yükseklik aralığına ilişkindir. B=1 çiftlerinden oluşan yeterince uzun sabit bir dizi, bu aralıktaki her başlangıçtan en az bir beyaz noktayı zorunlu kılıyor. Blok başlangıçları bu aralıkta kalan yolların ağırlıklı katkısı üstel azalıyor. Koşullu bileşim yasasına geçerken yalnızca bir kez sqrt(R) maliyeti ödeniyor. Aralıktan çıkan yolların az olduğu iddia edilmiyor.

Üçüncü çıktı, pozitif tam sayı yakınlıklarının etkisini ayıran kesin bir çekirdek açılımı. Karşılaştırma çekirdeği ile gerçek çekirdek arasındaki farkın bütün zamanlar boyunca birikimini kontrol etmek gerekiyor. Tek adımlık küçük olasılık yeterli değil. Gerekli ağırlıklı eşitsizlik yazıldı fakat doğrulanmış değil.

Sonraki hedef: birden çok düşük bölge gezintisi ve sınırsız pozitif rezonansların toplam katkısı. Bunları birleştiren genel C/R üst sınırı, XUB ve Collatz açık. Bu tur iki yerleşik alt ajan kullanıldı; yeni Sol/OpenRouter çağrısı yok. Birikimli harcama 0,061356 USD, kalan bütçe 1,938644 USD. Dosyalar yereldir; önceki V1 yayınının parçası değildir.
