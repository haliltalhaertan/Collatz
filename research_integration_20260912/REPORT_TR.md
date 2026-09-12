# Birleştirme ve araştırma turu — 12 Eylül 2026

Tam araştırma snapshot'ı b49f630 ile Muse dış-denetim dalı dc43110, geçmişi koruyan c10ac750 birleştirme commit'inde çatışmasız birleşti. Yeni kanonik arşiv eski statik üyeleri korur; kökteki araştırma raporlarını EXPLORATORY_CONTINUATION altında ekler. Özel anahtarlar ve geçici dosyalar araştırma arşivine alınmaz. Yayın sonrası kimlikler ve geri okuma kayıtları publication_receipts altında tutulur.

Bağımsız yeniden çalıştırmada ham-bayt controller SHA, rasyonel basınç sertifikaları, Git bağlamı denetimi, gerçek GOREV001 panelleri ve döngü tespiti kontrolleri geçti. Bu denetim tüm tarihsel matematik iddialarının yeniden ispatı değildir.

Ek inceleme iki yorum sorununu düzeltti: sonlu drift ölçümü artık H1'in asimptotik ihlali sayılmıyor; sonlu kuyruk gözlemi limit kanıtı diye sunulmuyor. Üstelik kappa=0.5 greedy controller yeniden çalıştırıldığında N=60000'de s_N=6 bulundu; eski 'gözle görülür lineer drift' ifadesi geri çekildi. Print/docstring dışındaki hesap AST'si aynı kaldı. Bütün kanıtlar AUDIT_REVIEW.md ve AUDIT_CHECKS.json içinde.

Araştırma devamında kuyruk filtre enerjisinin iletken katmanlarına dağılımı için tam binom formülü ve en ince katmanın toplam enerjinin yarısını taşıdığı özdeşlik kaydedildi. Gerçek kaynak ile filtreyi ortalama eşleştirmenin üst sınır olacağı varsayımı gerçek küçük panellerde yanlış çıktı. Baş araştırmacının ayrı tam otokorelasyon hesabı 64 katman sonucunu doğruladı. Ayrıntı: ../research_w_continuation_20260912/REPORT_TR.md.

Collatz ve gereken W/D2 asimptotik sınırları açık. Yeni ücretli model çağrısı, tüketilmiş B4 programı çalıştırması veya yeniden mühürleme yapılmadı. Bir sonraki açık soru, gerçek kaynak-filtre eşleşmesinin ağırlıklı ortalamasını büyüyen kritik ölçekte kontrol etmek.
