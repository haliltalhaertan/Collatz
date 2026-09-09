# Collatz llm-lab gerçek pilot V2 — 7 Eylül 2026

**Sonuç: PARTIAL. Bir incelenebilir nihai cevap elde edildi; XUB-MARKED-OCC OPEN. Sağlayıcı kayıtlarıyla uzlaştırılmış toplam ücret: $0.081616.**

Bu, yeni kullanıcı talimatıyla yeni sözleşme altında yapılan testtir. V1 yeniden başlatılmadı. Ana Collatz kopyası salt okunur girdi olarak kullanıldı; canonical bilimsel durum, B4/E7 mühürleri ve Git dalları değiştirilmedi. Drive aktarımı ve GitHub push yapılmadı.

## Sonuçlar

| Hat | Yerel sonuç | Süre | Nihai cevap | Ücret |
|---|---|---:|---|---:|
| Sol | COMPLETED; claim OPEN | 148.049 sn | Var | $0.028816 |
| Qwen | TIMEOUT | 600.557 sn | Yerel kayıtta yok | Sonradan provider GET: $0.052800 |
| Grok | BLOCKED_DEPENDENCY | Çağrı yok | Yok | $0 |

Toplam koşum yaklaşık 601 saniye sürdü. Gerçek model çağrısı 2, yeniden deneme 0. Sözleşme tavanı 3 çağrı ve $0.75 idi.

Sol: 4639 giriş, 1722 completion, bunun içinde raporlanan 620 reasoning tokenı. İlk testin 5000 completion / 5000 reasoning / boş nihai cevap sonucundan farklı olarak bu testte açık bir matematiksel değerlendirme alındı. Bu tek karşılaştırma bir model kalite veya hız benchmarkı değildir; ayarlar ve istem değişmiştir.

## Maliyet ve timeout bulgusu

Koordinatör kapanışta doğru biçimde provider_cost_complete=false bildirdi. Yerel kesin ücret $0.028816; çözümlenmemiş Qwen rezervasyonuyla fiyat tavanlarına bağlı aralık $0.028816–$0.135422 idi.

Generation ID ilk akış sırasında kaydedildi. Koşumdan sonra mevcut Qwen generation kaydına tek bir salt okunur GET yapıldı; yeni model çağrısı yapılmadı. Sağlayıcı total_cost=$0.052800 bildirdi. Böylece toplam:

`$0.028816 + $0.052800 = $0.081616`.

Bu, sağlayıcının kullanım kaydından alınan tutardır. Eski koşum paketi değiştirilmedi; uzlaştırma ayrı PROVIDER_COST_READBACK.json dosyasında tutuluyor.

**Yeni açık mühendislik bulgusu:** Qwen sağlayıcı kaydı finish_reason=stop, cancelled=false bildirirken yerel llm-lab 600 saniyede final metni alamadan timeout oldu. Sağlayıcı tamamlanması ile yerel akış tüketimi arasında uyuşmazlık var. Salt modelin yavaş olduğunu veya süreyi artırmanın çözeceğini söylemek için yeterli kanıt yok.

İncelenecek aday: directed_engine callback'i her parçada büyüyen PARTIAL.json dosyasını yeniden yazıyor ve TRACE.jsonl dosyasına ekleme yapıyor. Bu davranış kaynakta görüldü; darboğazın kesin nedeni olduğu henüz ölçülmedi. Önce kayıt/akış performansını çevrimdışı tekrar üretmek uygun sonraki mühendislik işidir.

Model provenansı ayrıca korunmalıdır: istek ve stream qwen/qwen3.8-max-0902, son generation metadata qwen/qwen3.8-max-20260902 diyor. Bu kayıtta doğrulanmış alias veya model değişimi hükmü verilmedi.

## Bilimsel değerlendirme

Sol tam iddiayı kanıtlamadı veya erişilebilir karşıörnek kurmadı. Kesin weak-composition sayım kimliğini ve düşük duruma girişin nadir olmadığını açıklayıp, rezonans dışlaması kaldırılmış daha zayıf bir gerekli occupation tahminini ayırdı.

N0 yararlı ve düşük olmayan blokların sayısı, NC bunlara ek olarak rezonanssız olanların sayısı olsun. NC <= N0 olduğundan exp(-lambda N0) <= exp(-lambda NC). Dolayısıyla N0 için C/R Laplace sınırı, asıl hedefin gerekli daha zayıf sonucudur. Bu eşitsizlik yönü ve gösterilen temel sayım türetimleri baş araştırmacı tarafından kontrol edildi. N0 tahmini kanıtlanmış değildir; çözülmesi de rezonans dışlamasını kendiliğinden çözmez. Önceden verilmiş engellerin yeniden açıklanması yeni bir XUB ispatı değildir.

Grok çalışmadığı için modelden bağımlı hakem incelemesi alınmadı. XUB, E6-N2/B4 ve Collatz durumu değişmedi.

## Hazırlık ve doğrulama

- Gerçek pilot düzeltmelerine yönelik 40 çevrimdışı test bu görevde yeniden geçti. İlk test girişimindeki 7 geçici dizin fixture hatası, açık yeni workspace geçici diziniyle giderildi; son tam sonuç 40 passed.
- Dört bilimsel girdi: SHA256 4/4 PASS.
- Yeni sözleşme SHA256: f76c2a284286815f5cb21e53d1be06caa0c61bb85bde0d4674b84b6612e3e56e.
- Güncel model kataloğunda low effort doğrulandı. Üç model için sayısal cap desteği ilan edilmediği için effort=low seçildi; zorunlu nihai cevap garantisi ileri sürülmedi.
- Completion tavanları Sol/Qwen/Grok: 12000/12000/8000. Hat başına 600 sn, toplam 1200 sn, 2 eşzamanlı üretici.
- llm-lab package verifier: ok=true.
- Bağımsız ZIP CRC kontrolü: PASS; 34 üye, 111966 bayt.
- ZIP SHA256: 4b313c8486836941994a406588591617ef7d327b3eea99f56d8497c22eb7d012.

Kaynak reasoning denetimi: https://openrouter.ai/docs/guides/best-practices/reasoning-tokens . Model kataloğunun kullanılan anlık görüntüsü MODEL_CATALOG_SNAPSHOT.json dosyasında.

## Kullanım kararı

Sol ile dar, açık sonuç isteyen araştırma görevleri bu testte kullanılabilir çıktı verdi. Maliyet belirsizliği ve çağrı kimliği düzeltmeleri gerçek koşumda işe yaradı. Bununla birlikte Qwen akış uyuşmazlığı giderilmeden aynı bağımlı üçlü düzeni hızlı ve güvenilir kabul etmiyorum. Beş yolu birden çalıştırmaya geçmeden önce bu darboğazı teşhis etmek gerekir; sözleşme şeması ayrıca en fazla dört eşzamanlı worker kabul ediyor, dolayısıyla beş görev en az iki dalgada yürütülür.
