# Sol low: Collatz mini benchmark v1

8 Eylül 2026. Sonuç: 8/8 tam doğru, 16/16 puan. Sekiz bağımsız çağrı, en fazla dört eşzamanlı istek. Toplam 61,39 saniye, sağlayıcının bildirdiği tamamlanmış maliyet 0,030242 dolar. Soru başına ortalama maliyet 0,00378025 dolar; medyan çağrı süresi 22,95 saniye. Tekrar çağrı, zaman aşımı veya başarısız yanıt yok.

| Soru | Konu | Puan |
|---|---|---:|
| b1 | 6'dan başlayan standart yörünge ve adım sayısı | 2/2 |
| b2 | 7'den başlayan tek-sayı dönüşümü ve v2 üsleri | 2/2 |
| b3 | OEE dal sözcüğünün formülü ve modüler geçerliliği | 2/2 |
| b4 | İki tek-adımlı döngü için cebirsel imkânsızlık | 2/2 |
| b5 | Ortalama çarpan / log sürüklenme ve sezgisel model sınırı | 2/2 |
| b6 | Sonlu doğrulamadan evrensel ispat çıkarma hatası | 2/2 |
| b7 | Büyük ortalamanın Laplace üst sınırına yetmemesi | 2/2 |
| b8 | Daha küçük sayıya iniş varsayımından güçlü tümevarım | 2/2 |

Yöntem: Sorular, beklenen cevaplar ve 0–2 puan kuralı ilk model çağrısından önce kaydedildi; SHA256 hashleri son değerlendirmede tekrar doğrulandı. Cevap anahtarı model girdilerine dahil edilmedi. Ana uygulamanın görünürlük üretimi her çağrıda ilgili soruyu lane rolü olarak sundu. Model araç veya hesap makinesi kullanmadı. Cevaplar araştırmacı tarafından okunup anahtarla karşılaştırıldı; grade.py bu insan/araştırmacı değerlendirmesini kaydeder, bağımsız otomatik matematik doğrulayıcısı değildir. Modelin kendi claim_status etiketi puan olarak kullanılmadı.

Olumlu gözlem: Temel aritmetik ve cebir doğru. Heuristik rastgele yürüyüş ile deterministik tüm-yörünge iddiası, sonlu kontrol ile evrensel ispat, koşullu tümevarım ile varsayımın ispatı doğru ayrıldı. b7'de beklenti R/2 iken Laplace beklentisinin en az 1/2 olduğunu doğru gösterdi.

Sınırlar: Bu küçük, elle hazırlanmış temel/orta düzey denemedir. Soruların çoğu standart ve öğreticidir; eğitim verisi sızıntısına karşı özel bir koruma veya yenilik iddiası yok. Bazı soruların yazımı hangi mantıksal ayrımın beklendiğini belirgin biçimde işaret ediyor. Model/ayar başına tek örnek, kör olmayan değerlendirici ve sekiz soru ile genel başarı oranı tahmin edilemez. Tam puan, setin Sol low için yeterince zor olmadığını düşündürüyor; açık Collatz araştırmasını çözebildiğini göstermez. Daha zor benchmark ayrı sürüm, ayrı önceden dondurulmuş anahtar ve bütçe gerektirir; bu turda ek çağrı yapılmadı.

Bilimsel durum: Collatz'ın ispatı elde edilmedi. Paket bütünlüğü ve ZIP CRC geçti; 71 dosya; SHA256 2da306a389532e4646ddaec23df3cea8f5d8e291b03bdb76dad90898e180ea4d. Çalışma tamamlandı, aktif model çağrısı yok.
