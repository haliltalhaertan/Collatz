# Yoğun çift sayımı — 8 Eylül 2026

Bu turda her çiftteki beyaz B=1 fırsatlarını sayan daha yoğun istatistiği inceledik. İki sonuç elde edildi:

1. Hiç beyaz B=1 fırsatı bulunmayan yolların olasılığı, yeterince büyük gerçek dizilerde en az c_eta/R. Bu, doğrudan Laplace ortalaması için 1/R'den daha küçük bir üst ölçek beklenemeyeceğini gösteriyor. İstenen C/R üst sınırıyla uyumlu; o sınır hâlâ açık.
2. Önceki 'en az A log R beyaz fırsat, başarısızlık olasılığı en fazla C/R' ara hedefi yanlış. Gerçek erişilebilir asal bir alt dizi üzerinde başarısızlık olasılığı en az c_A log R/R. Bu, sabit A'yı değiştirerek veya fırsatları daha dar bir düzenli bölgeye kısıtlayarak düzelmiyor.

İkinci sonuç, sınırdaki sabit sayıda artımı sabitleyip ortadaki köprünün döngüsel sıralama yasasını kullanıyor. Orta parça çift sayısı asal seçilince bağlar kalkıyor ve ilgili sıralama sayısı tam olarak 1,...,n üzerinde düzgün dağılıyor. İki alt ajan bu çıkarımı bağımsız kontrol etti.

Bu yüzden araştırmada doğrudan üstel ortalamayı kontrol etmekle, logaritmik sayıda fırsatı yüksek olasılıkla zorlamak arasındaki farkı korumalıyız. İlk O(log R) sayım değerinin toplam kütlesi log R/R olabilirken, üstel ağırlıklandırılmış kütlesi 1/R olabilir.

Ayrıca art arda B=1 çiftleri için bütün girişlerin siyah kalmasının tam aritmetik koşulu yazıldı ve denetlendi. Bu koşul, pozitif yakın-rezonans sorununu somutlaştırıyor; gerçekleşme sıklığını henüz kontrol etmiyor.

Bu sonuçlar kompleks çekirdek sınırını, XUB'yi veya Collatz'ı çürütmüyor. Tam kanıtlar DENSE_LOWER_TAIL_PROOF.md ve EXACT_B1_WORD_LEMMA.md içindedir.

Bu tur yeni OpenRouter isteği yok. Kümülatif harcama 0,061356 USD, kalan 1,938644 USD.

Drive/GitHub durumu: Kullanıcı önceki tamamlanmış araştırma turlarının 20 dosyalık paketinin iki hedefe de yüklenmesini açıkça onayladı. ZIP Drive'a yüklendi ve geri indirilen bütün baytları doğrulandı. Aynı 20 dosya GitHub'da codex/coarse-occupation-20260908 dalına eb4818a2dbfa946d7752783d1722b02cb8520a72 commit'iyle kaydedildi; 20/20 dosya geri okumada birebir eşleşti. Bu yeni yoğun-sayım turu, onaylanan V1 anlık görüntüsünün içinde değildir ve yereldedir. Kalıcılaştırma makbuzu research_publication_20260908/PERSISTENCE_RECEIPT.md içindedir.
