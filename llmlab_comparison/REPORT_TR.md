# DeepSeek ve GLM Flash denemesi

7 Eylül 2026. Sıra: DeepSeek V4 Pro 0813, ardından GLM 5.3 Flash. Her model için Luna'daki aynı dört araştırma girdisi ve beş yaklaşım planlandı. high düşünme ayarı, 8000 çıkış tokenı, sıfır tekrar çağrı kullanıldı. İki tur da beşinci çağrı başlatılmadan araştırmacı tarafından kontrollü durduruldu; tamamlanmış beş-yaklaşımlı kalite karşılaştırması değildir.

| Model | Çağrı | Yerelde nihai yanıt | Süre | Maliyet durumu |
|---|---:|---:|---:|---|
| Luna (önceki tur) | 5 | 5 | 452 sn | 0,03410785 dolar, tamamı biliniyor |
| DeepSeek V4 Pro 0813 | 4 | 0 | 589 sn | Bilinen sağlayıcı alt toplamı 0,07977605 dolar; tam ücret çözümlenmedi |
| GLM 5.3 Flash | 4 | 0 | 484 sn | Ücret kayıtları GET 404; sıfır maliyet denemez |

DeepSeek'te kullanıcının paylaştığı Activity görüntüsü sağlayıcının üretim kayıtlarıyla eşleşti. Phala 8000 tokenın tamamını düşünmeye harcayıp length ile kesildi (0,04182115 dolar). CoreWeave 8000 tokenın 5388'ini düşünmeye harcayıp length ile kesildi (0,0379549 dolar); buna rağmen uygulama durdurulana kadar nihai metni almamıştı. StreamLake kaydı 2608 düşünme tokenı, sıfır ücret ve boş finish_reason gösteriyor. Çevrim hattının kaydı bulunamadı. Son iki kayıt nedeniyle toplam ücret kesin değil.

Bu bulgular hem düşünme bütçesinin tükenmesini hem sağlayıcı ile yerel akış durumunun ayrışmasını gösteriyor. İkisini 'model yavaş' diye birleştirmek doğru değil. GLM'de de yerel akış vardı fakat durdurma öncesi nihai metin yoktu; sağlayıcı bitiş kayıtları henüz alınamadığından aynı teşhis GLM için kesinleştirilemez.

Bir fiyat kontrolü açığı da görüldü: katalogda listelenen ucuz fiyat, otomatik seçilen her sağlayıcının fiyatı değil. DeepSeek/Phala çağrısının gerçek ücreti, ilan ettiğimiz 0,04 dolarlık çağrı tavanını aştı. Yerel bütçe rezervasyonları bu durumda güvenilir fatura üst sınırı sayılmaz. Bu benim başlangıçtaki tavan ifademin de fiilen garanti edilmediğini gösteriyor.

GLM'ye geçmeden önce otomatik başlangıç tutuldu. Üretim kaynaklarına dokunmadan ayrı bir sağlayıcı adaptörü kopyasına OpenRouter provider.max_price filtresi eklendi: prompt 0.075, completion 0.25 USD/milyon token ve sort=price. Yeni sözleşme ve adaptör hashleri glm_capped/BINDING.json içinde. GLM turu bu ayrı ayarla başladı; bu, Luna ve DeepSeek ile kıyasın açık bir teknik farkıdır. GLM için 0,025 dolarlık plan korundu; kesin fatura henüz yok.

İki turun da sonuç paketleri oluşturuldu ve bütünlük/ZIP CRC kontrolleri geçti. Bu kontrol fiyat tahminlerini veya matematiksel doğruluğu onaylamaz. Hiçbir gizli düşünme metni bilimsel kanıt olarak kullanılmadı. XUB ve Collatz açık kaldı.

Önerilen sonraki iş: ücretli model karşılaştırmasını büyütmeden akış okuma/kaydetme yolunu ölçmek, sağlayıcı fiyat filtresini uygulamanın sözleşmesine taşımak ve düşünme/nihai cevap bütçesini ayrı gözlemlemek. directed_engine.py her parçada büyüyen PARTIAL.json dosyasının tamamını yazıyor ve TRACE ekliyor; olası darboğaz, henüz ölçülmüş kök neden değil. Bu turda üretim uygulamasına kalıcı düzeltme yapılmadı.

Dosyalar: DEEPSEEK_REVIEW.md, deepseek/PROVIDER_RECEIPTS.json, deepseek/PUBLIC_REVIEW.json, glm_capped/PROVIDER_RECEIPTS.json, glm_capped/PUBLIC_REVIEW.json. Her iki süreç kapandı; bu test için yeni çağrı planlanmadı.
