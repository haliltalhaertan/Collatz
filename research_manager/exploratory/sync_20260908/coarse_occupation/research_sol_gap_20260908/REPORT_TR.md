# Araştırma devamı — 8 Eylül 2026

## Sonuç

Belirli bir geçerli blok seçimi için, önceki C/R işaretli-blok Laplace hedefini çürüten analitik bir karşıörnek dizisi elde edildi. Tam kanıt iki yerleşik alt ajan tarafından baştan sona denetlendi; ikisi de matematiksel düzeltme istemeden kabul etti.

Seçim: B_0=2, L_R=floor((6/5) log R), başlangıçtan itibaren ayrık bloklar. Bu katsayı sembolik yararlı-blok arzı teoreminin izin verdiği aralıktadır. Gerçek erişilebilir G son-eklerinden kurulan bir dizi üzerinde, sabit c_*>0 için

E exp(-lambda N_C) >= c_* L_R/R.

L_R büyüdüğünden bu ifade hiçbir sabit C ile C/R tarafından üstten sınırlanamaz. Sonuç sonlu bir sayısal deneye veya model oybirliğine değil, belgede gösterilen sayım, ağırlık karşılaştırması ve asimptotik hata sınırlarına dayanır.

## Yeni kapanan adımlar

- Aşım miktarı toplandıktan sonra yeniden başlatılmış son-ek yasası tam olarak serbest düzgün bileşim yasasıdır. İlk-geçiş koşullandırması bu kullanım için ek bir engel değildir; aşım ayrı ayrı sabitlenirse bu ifade değişir.
- Kaba köprünün en yüksek iki seviyesi arasındaki fark için, yeterli blok uzunluğunda sabit pozitif olasılık alt sınırı kanıtlandı. İspat, bir bloktan sabit miktarda toplamı son bloğa taşıyan birebir dönüşüm kullanır.
- Bu uzunluk rejiminin, B_0=2 için izin verilen sembolik rejimle örtüştüğü kesin rasyonel eşitsizliklerle kontrol edildi.
- Tam bölünebilir blok ızgarası gerçek erişilebilir bir sonsuz son-ek dizisinde kuruldu. Başlangıç bloğu istisnası doğru biçimde korunuyor: N_C<=1.

## Ne sonuç çıkmıyor?

Bu kanıt daha küçük her blok katsayısını çürütmez; bazı daha küçük katsayının işe yaradığını da göstermez. Diğer ızgaralar ve sayım yöntemleri açık kalır. Kompleks fazlar birbirini götürebileceğinden, bu pozitif Laplace belgesinin başarısızlığı kompleks çekirdek sınırının başarısızlığı değildir. XUB ve Collatz açık kalıyor.

## İş dağılımı

Bir yerleşik alt ajan maksimum-fark alt sınırındaki birebir dönüşümü geliştirdi; diğer alt ajan gerçek ilk-geçiş yasasını ve indisleri çözdü. Ana ajan rejimlerin örtüşmesini belirleyip tüm parçaları gerçek dizi üzerinde birleştirdi. Sonrasında iki ajan da tam birleşik kanıtı bağımsız denetledi.

Sol low'a tek küçük soru verildi. Sol, seçilmiş maksimumun yanındaki bloktan toplam aktarımıyla başka bir doğru birebir dönüşüm sundu; fakat bunun ihtiyaç duyduğu koşullu olasılık alt sınırını açık bıraktı. Katkı denetlendi ve gelecekteki küçük-katsayı sorusu için kaydedildi. Tam çürütme kanıtı Sol'un çözülmemiş varsayımına dayanmıyor.

## Maliyet ve kayıtlar

Bu tur: 1 Sol low çağrısı, 42,82 saniye, 0,020004 USD. Önceki turla toplam 0,061356 USD. 2 dolarlık bütçeden 1,938644 USD kaldı. Açık OpenRouter çağrısı yok; süre kesmesi ve tekrar deneme uygulanmadı.

Tam kanıt COARSE_GRID_OBSTRUCTION_PROOF.md, bağımsız inceleme INDEPENDENT_AUDIT.md, tam rasyonel sabit kontrolleri CONSTANT_CHECKS.json, kaynak bağları SOURCE_HASHES.json ve sonraki soru NEXT_ACTION.md dosyalarındadır. Orijinal kanonik notlar ve mühürlü aşamalar değiştirilmedi.
