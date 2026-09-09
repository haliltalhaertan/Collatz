# Üç alt ajanla karşılıklı saldırı: ortalamayı çıkar, gereken hedefi küçült

8 Eylül 2026. Baş araştırmacı + üç mevcut alt ajan: audit_cancellation, audit_coarse_identity, review01_global. Üçü de yeni görevi kabul etti. Sonuçlar aşağıdaki dosyalara yazıldı; farklı geçişler ek bağımsız ajan sayılmadı. Ücretli çağrı, yayın veya kanonik kabul işlemi yok.

## Ana sonuç ve önceki yorumun düzeltilmesi

Önceki milyonluk pozitif/negatif kovaryans hesabı doğru, ancak buna verilen stratejik anlam fazla güçlüydü. Büyük katkıların önemli kısmı, bilinen sabit ortalamanın kovaryans içinde gereksiz taşınmasından doğuyor. Bu ortalama baştan çıkarılınca r14 örneğindeki yaklaşık1.27 milyonluk grup diyagonali yaklaşık1490'a düşüyor. Gerçek varyans yaklaşık1617. Dolayısıyla buradan zorunlu, henüz açıklanmamış dev bir çapraz-ağırlık iptali mekanizması çıkarmak gerekmez.

Baş araştırmacı bu itirazı tam hesapla getirdi. İki ajan cebiri kontrol edip kabul etti; önceki 'çift ailelerini mutlaka birlikte iptal ettirmeliyiz' yorumunu düzelttik. Ağırlık sınıfları sayısı O(r) olduğundan, bunlar arasında Cauchy kullanmanın kaybı yalnız polinomdur ve üstel sayım hedefine zarar vermeyebilir.

## 1. Sabit tabanın tam olarak çıkarılması

q=2^t; P_k(z), m adımda k tek durum görüp z mod q kalıntısına ulaşan gerçek tek başlangıçların sayısı. N_k=binom(m-1,k-1) ve j=r-k olsun. Kuyruk kabul oranı p_j=binom(t,j)/q. Geçersiz j için katkı sıfırdır.

    E_k(z)=P_k(z)-N_k/q,
    e_k=sum_z E_k(z)^2.

Her ötelemede tam olarak binom(t,j) kuyruk kalıntısı kabul edilir. Bu nedenle sabit N_k/q bileşeni yalnız N_k p_j ortalamasına katkı yapar. Kovaryans hesabında sıfır yöndür. Merkezleme gözlemi değiştirmez; açıklanmış bileşeni kaldırır.

|r|Ham grup diyagonali|Merkezlenmiş grup diyagonali|Tek tek ağırlık varyansları toplamı|Toplam varyans|
|---:|---:|---:|---:|---:|
|5|81/4|37/8|37/4|49/4|
|10|27895/4|6701/256|819/32|307/16|
|12|28179333/128|50973/128|2795/4|6395/4|
|14|650219507/512|12206397/8192|274211/256|413919/256|

Son iki örnekte ağırlıklar arası toplam çapraz katkı pozitiftir. Merkezlenmiş diyagonal de tek başına varyans değildir; aynı ağırlık içindeki kalıntı bağımlılığı devam eder.

## 2. Daha doğrudan yeterli hedef

İki gerçek önek sapması niceliği tanımlayalım:

    D_source=sum_k e_k p_j(1-p_j),
    D_2=sum_k e_k p_j^2.

t>=1 için binom kuyruk oranlarının tamamı en fazla1/2, dolayısıyla D_2<=D_source. K, katılan ağırlıkların sayısı olsun; K<=m. Ajanın Fourier hesabı ve temel konvolüsyon normu şu genel sınırları verir:

    V <= K q D_2 <= K q D_source,
    |G(0)-B| <= sqrt(K q(q-1) D_2) <= sqrt(K) q sqrt(D_2).

Bu çıkarım, ağırlıklar arası negatif korelasyon varsaymaz. Daha hassas biçimde V_k<=M_j^2 e_k/q; M_j kuyruk göstergesinin sıfır dışı en büyük Fourier katsayısıdır. Yukarıdaki D_2 sınırı yalnız M_j<=q p_j kullanır.

alpha=log2(3), tau=alpha-b, gamma0=h*+b-alpha olsun. D_2<=2^((omega+o(1))r) ise köken sayımı üssü en fazla max(gamma0,tau+omega/2). b=1.2,kappa=1.053 için yeterli koşul:

    omega < 2b/kappa-2tau ≈1.5092772778.

Özellikle D_source<=2^o(r) B gibi bir sonuç, b>=alpha-h*/3≈1.0830812047 rejiminde ideal sayım üssüne yeter. b=1.2 bu aralıktadır. Burada B'nin üssü yaklaşık1.1206813872 olduğundan bu örnek varsayım gerekenden güçlüdür.

**Kanıtlanmamış olan tam olarak gerçek büyüyen kritik panellerde D_2 veya D_source üst sınırıdır.** Yeni varyans/yörünge tahmini elde edilmedi. Sadece artık belirsiz bir 'iptal' hedefi yerine gerçek önek histogramının ağırlıklı sapmasına bağlanan yeterli, daha sade bir hedef var. Uniformluk yalnız A=floor(alpha r) değil, gereken her sabit kritik bant içindir.

## 3. Adaya saldırı: sınırlandırılmış gerçek hesap ve karşıaile

review01_global, hesap öncesi verilen r5..12, A=floor(alpha r)+d, d=-1,0,1, m=ceil(1.2r), t>=1 gridini tam aritmetikle taradı. 22 geçerli panel; t=0 olan2 panel dışarıda. D_source<=B için ihlal yok. En büyük oran37/60: r5,A7,m6,t1. D_2 de kaydedildi ve her panelde D_2<=D_source kontrol edildi.

Bu geçiş, sonunda veya bütün r için eşitsizlik kanıtı değildir. Sabit1 katsayısı hedef olarak dondurulmuş bir teorem sayılmamalı.

Ajan, kritik ölçek kısıtını kaldıran bir karşıaile de verdi: m=11 sabit, t büyür, r≈t/2. Aynı (k,y) son durumuna birleşen başlangıçlar, D_source/B oranının limitini1'den büyük yapar. Baş araştırmacı H^11(145)=H^11(147)=161 ve ikisinin de k=7 olduğunu bağımsız kontrol etti. Bu aile m≈1.2r değildir; kritik varsayımı çürütmez, koşulsuz bütün-parametre yorumunu engeller. Ayrıntılar SOURCE_DEFECT_VERDICT.md'de.

## 4. Diğer iki ajanın itirazları

**Dyadik iptal:** audit_cancellation gerçek ötelemeleri eşleştirerek

    P_t(a;z)+P_t(a+2^(t-1);z)=(1+z)P_(t-1)(a;z)

özdeşliğini kanıtladı. Fark ise (1-z) çarpanı ve gerçek son parite işaretlerini taşıyan bir polinomdur. Ortalama Pascal kuralıyla sadeleşir, farkın kare enerjisi pozitif kalır. Bu enerji atılamaz. Ajan sabit küçük gridde699 katsayı eşitliğini ve ilgili rasyonel varyans ayrışımlarını kontrol etti. Bu, bilinen tam ortalamayı genişleten denetlenebilir bir ayrışım; kendi başına daralma değil.

**22. moment:** review01_global, normalize Walsh katman enerjileri E_l için W_w=sum_(l>=1) w^l E_l yazdı. Doğrudan Cauchy:

    |G(0)/B-1|^2 <= W_w[(1+1/w)^t-1].

Aynı W_21 bilgisiyle doğrudan köken kontrolü, 22.moment+hiperkontraktivite üzerinden geçmekten daha iyi: izinli enerji üssü yaklaşık0.01200305608; dolaylı yol yaklaşık0.002842913777 ister. Bu karşılaştırmada yüksek moment ara adımını bırakıyoruz. Gerçek W_w tahmini yine açık.

**Harmonik bütçe:** audit_coarse_identity bütçeyi doğruladı ve kesirli aralık paketlemesine genişletti. Aynı indeksin toplam kullanım ağırlığı en fazla1 ise sum theta_I delta_I<=H_N/(3ln2). Sonlu aralık ailelerinde kesirli optimum ile ayrık aralık optimumu aynı; ağırlıklandırma yoktan kazanç üretmiyor. İç içelik, seyrek geliş ve küçülen delta, sonsuz bloktan çelişki çıkarılmasını ayrı ayrı engelliyor. Sabit uzunlukta paradoksal blokların geç dönemde yokluğu zaten tekrarsızlıkla çıkar; yararlı yeni lemma büyüyen uzunlukları ele almak zorunda.

## Karar

Ana sıradaki soru, gerçek kritik önek histogramında D_2'nin üstel büyümesine bir üst sınır bulunup bulunamayacağı. Sadece sonlu tabloyu büyütmek yeterli değil. Önce aynı histogramın tam geçişlerinden bir eşitsizlik, ya da varsayıma kritik rejimde karşıaile aranmalı. Sıfır dışı kuyruk Fourier katsayılarına ek küçülme kanıtı olmadan da yeterlilik hesabı çalışıyor; bu nedenle bütün ham çift kovaryanslarını ayrı ayrı çözmeyi ön koşul yapmıyoruz.

Harmonik yol yan açık olarak tutuluyor. Yeni bir asimptotik sapma tahmini, yeni yörünge dışlaması veya Collatz çözümü yok. Bu turun kazanımı, yanlış stratejik çıkarımın düzeltilmesi, iki pahalı/geçersiz aktarımın elenmesi ve eksik gerçek niceliğin daha kesin belirlenmesidir.

## Kanıt izi

- cancellation.md: gerçek dyadik eşleştirme, varyans, kaynak sapması üst sınırları.
- moments.md: yüksek moment eleştirisi, doğrudan ağırlıklı Walsh sertifikası, sentetik karşımodel.
- harmonic.md: tek-yörünge bütçesi, paketleme ve başarısız çıkarım örnekleri.
- cross_audit.md: ayrı ajanın merkezleme ve Walsh eşik denetimi.
- check_centered_prefix.py / CENTERED_PREFIX.json: baş araştırmacının dört tam paneli.
- source_defect_probe.py / SOURCE_DEFECT_PROBE.json: önceden belirlenmiş22 geçerli panel.
- check_dyadic.py / DYADIC_CHECK.json: ajanın sabit küçük eşleştirme denetimi.

Eski CP17 sonucu kayıtlı hipotezleriyle kullanıldı; bütün arşiv yeniden denetlenmedi. Bu klasörün belgeleri yerel keşif notlarıdır.
