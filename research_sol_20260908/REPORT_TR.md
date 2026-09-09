# Araştırma turu — 8 Eylül 2026

Sol low ile üç küçük analitik soru, ardından bir yerleşik alt ajanla bağımsız matematik denetimi tamamlandı. OpenRouter çağrıları toplam 107,60 saniyede sonuçlandı. Süre kesmesi ve tekrar deneme uygulanmadı.

## Bütçe

Bu devam turu için kullanıcı üst sınırı: 2,00 USD. Üç çağrının sözleşme üst sınırı: 0,24 USD. Sağlayıcının eksiksiz bildirdiği gerçek toplam: 0,041352 USD. Kalan bütçe: 1,958648 USD. Açık OpenRouter çağrısı yok. Eski dört eşzamanlı istek sınırı bu tur için bir kullanıcı kısıtı sayılmıyor; ihtiyaç üç çağrı olduğundan üçü paralel çalıştırıldı.

## Matematiksel ilerleme

1. Önceki keşif notlarındaki eşdeğerlik iddiasına düzeltme kaydı oluşturuldu. İşaretli blok sayısının Laplace üst sınırı, kompleks çekirdek üst sınırı için yeterlidir. Ters yön gösterilmemiştir ve genel durumda faz iptali nedeniyle yanlıştır. Blok sayımı yaklaşımının çürütülmesi bütün kompleks çekirdek yolunun çürütülmesi değildir.
2. Kaba ızgarada, uçları birleştiren doğruya göre merkezlenmiş köprünün çevrimsel sıralama özdeşliği doğrudan kanıtlandı. Eşitlikler yoksa Laplace ortalaması tam bir geometrik toplamın n'ye bölümüdür; sınırlı gcd ile de 1/n mertebesi korunur. n=R/(2L), L yaklaşık log R olduğundan bu istatistiğin doğal ölçeği log R/R olur. Bu sonuç gerçek düşük-durum istatistiğine henüz aktarılmadı.
3. Gerçek affine eşiğe aktarım için daha küçük bir açık soru elde edildi. Tam bölünebilir R=2Ln durumunda, kaba köprünün en yüksek ve ikinci en yüksek seviyesi arasındaki fark Delta olsun. Sabit uygun B için, uç-nokta koşullu ve çevrimsel değişmez yasa altında, işaretli blok sayısı N_C şu alt sınırı sağlar:

   E exp(-lambda N_C) >= exp(-lambda) P(Delta>B)/n.

   Bunun sonlu çevrimsel sayım kanıtı denetlendi. Gerçek erişilebilir bir alt dizide P(Delta>B)'nin pozitif bir sabitten aşağı düşmediğini göstermek ve gereken ilk-geçiş koşullu yasaya aktarımı doğrulamak hâlâ açık. Bunlar gerçekleşirse log R/R engeli, mevcut 1/R işaretli-blok hedefini çürütebilir. Şu anda böyle bir çürütme iddiası yok.

## Denetim ve sınırlar

Sol'un grid yanıtındaki başlangıç bloğunu atlayan indeks hatası düzeltildi: olay N_C=0 değil N_C<=1 verir. Son nokta, tam bir bloğun başlangıcı olmadığı için düşük olma olayına gereksiz yere eklenmemelidir. İki yanıtta şemanın kabul etmediği iddia durum etiketi vardı; sistem bunları OPEN tuttu. Matematiksel değerlendirme, paket bütünlüğü kontrolünden ayrıca yapıldı.

Paketin 36 üyesi ve SHA-256 bütünlüğü doğrulandı: 005672e7d32677a1d89bc07f8e072b76040e9f53eb2cd757b38e4491eb03dbb8. Bu kontrol matematiksel doğruluk sertifikası değildir.

Tam argümanlar ve varsayımlar PRINCIPAL_ANALYSIS.md içindedir. Kanonik notlar değiştirilmedi, mühürlü B4 aşaması çalıştırılmadı. XUB ve Collatz açık kalıyor.

Bir sonraki küçük araştırma işi: yeni maksimum-fark olasılığı sorusunu, erişilebilir dizi ve koşullu yasa kısıtlarıyla incelemek. Bütçenin tamamını harcamak bir hedef değildir.
