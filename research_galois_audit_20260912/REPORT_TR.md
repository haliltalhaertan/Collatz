# Galois, dördüncü moment ve işaret açıklamasının denetimi

12 Eylül 2026. Sunulan Claude metninin sınırlı denetimi. Önceki gerçek panel verileri kullanıldı; yeni ücretli çağrı veya kapalı yürütme yapılmadı. W, D2 ve Collatz açık.

## Doğru cebir ve alan konvansiyonu

n=2^s, H=h_s=n/2, K=Q(zeta_n), F tamsayı değerli gerçek filtre ve beta=F_hat(1) conjugate(F_hat(1)) olsun. beta cebirsel tamsayıdır; sigma_a(beta)=|F_hat(a)|^2. Burada odd a ile gezilen çokluk, K'nin bütün gömmelerini içerir. beta gerçeldir; a ve -a aynı değeri verir, minimal alanı daha da küçük olabilir. Bu yüzden 'tam Galois yörüngesi' ifadesi farklı köklerin listesinden ziyade tekrarlı gömme çokluğu olarak okunmalıdır.

Tr_K(beta), Tr_K(beta^2) ve N_K(beta) tamsayıdır. Tr_K konvansiyonuyla C_Y=H Tr_K(beta^2)/Tr_K(beta)^2 doğrudur. Minimal alanın izini kullanırsak H yerine o alanın derecesi gerekir. C_Y-1'in değişim katsayısının karesi olması, önceki normalize dördüncü-moment ölçütünün aynı ifadesidir; ek bir uniform sınır sağlamaz. s>=2 için gerçek Collatz filtresinin sıfır sınıflaması beta'nın toplam pozitif olduğunu verir.

## Otokorelasyon özdeşliği doğru; önceki kodda zaten var

C(u)=sum_v F(v)F(v+u), döngüsel indeksleme ile:

    Tr_K(beta^2)=H sum_(0<=u<H) [C(u)-C(u+H)]^2.

Bu, otokorelasyonun Fourier dönüşümünün |F_hat|^2 olması ve primitive Parseval özdeşliğidir. Önceki research_concentration_audit_20260912/check_claim.py içindeki moments(v) fonksiyonu aynı hesabı H sum_(u<n)[C(u)^2-C(u)C(u+H)] olarak yaptı. İki yazım cebirsel olarak aynıdır. Nitekim önceki hedefte Tr(beta)=48 ve Tr(beta^2)=432 tam tamsayı olarak kaydedildi.

Bu denetimde ayrıca belirtilen18 (t,j,s) durumunu tekrar hesapladık. Bir yolda otokorelasyon fark kareleri, diğer yolda beta'nın Z[X]/(X^H+1) içindeki karesinin sabit katsayısının H katı kullanıldı;18/18 tam eşleşti. Bu bir genel özdeşliktir, doğruluğu18 örnekle sınırlı değildir. Claude'un norm testlerini yeniden çalıştırmadık; tamsayılık alan teorisinden gelir.

Eksik yeni adım, bütün kaydırmaların ortak parite-ağırlık dağılımını verimli ve uniform kontrol eden bir bağıntıdır. K_s'nin tek-nokta dağılımının binom olması, (K_s(v),K_s(v+u)) ortak dağılımını belirlemez. D ispatının tek kardeş kaydırmasına dayanması bu adımı otomatik taşımaz. Ayrıca tam kapalı form elde etmek, büyüyen s'de gereken büyüklük sınırını kanıtlamaktan ayrıdır.

## Galois yapısı tek başına düzlüğü garanti etmez

Somut karşı-aile: n=2H=2^s için F_block(u)=1_{0<=u<H} ve beta=|sum_(u=0..H-1) zeta_n^u|^2. Her odd a gömmesinde geometrik toplam 2/(1-zeta_n^a) olduğundan bütün eşlenikleri pozitiftir. beta cebirsel tamsayıdır, aynı siklotomik alan ve Galois yapısı geçerlidir.

Bu filtrede C(u)-C(u+H)=H-2u,0<=u<H. Dolayısıyla:

    Tr_K(beta)=H^2,
    Tr_K(beta^2)=H^2(H^2+2)/3,
    C_Y=(H^2+2)/(3H) ~ H/3.

Böylece toplam pozitiflik, norm/iz tamsayılığı ve Galois yörünge yapısı tek başına uniform C_Y vermez. Bu blok filtresi gerçek Collatz parite-ağırlık filtresi DEĞİLDİR; gerçek Collatz C_Y sınırını çürütmez. Hangi ilave yapıyı kullanmamız gerektiğini gösterir.

## Literatürün doğru yönü

[Orloski–Sardari–Smith, New Lower Bounds for the Schur-Siegel-Smyth Trace Problem](https://arxiv.org/abs/2401.03252), en küçük limit iz/derece oranı için1,80203 alt sınır verir. Dolayısıyla metindeki yaklaşık1,78 ifadesi güncel sonuçları tam yansıtmıyor. Bu alt sınır, bizim normalize ikinci momentimize gereken üst sınır değildir.

Metindeki [The absolute S_k-measure...](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/abs/absolute-boldsymbol-skmeasure-of-totally-positive-algebraic-integers/DC19D18900B980F9D954E27C4E597B14) bağlantısı Wang–Pang–Wu çalışmasına gider; özet k=2,...,15 ve sonra gerçek k>2 için moment ALT sınırlarını açıkça belirtir. Bu eser, ihtiyaç duyulan uniform S_2/d <= C(S_1/d)^2 üst karşılaştırmasını kendi başına sağlamaz. Yöntem uyarlanamaz demiyoruz; uygulanacak somut teorem ve ek hipotezler gösterilmedi.

[Flammang, To answer a question of Professor Georges Rhin](https://arxiv.org/abs/2401.12951), R adlı başka bir ölçütün alt sınırlarını araştırır. [Cherubini–Yatsyna, Potential energy of totally positive algebraic integers](https://arxiv.org/abs/2202.05235), potansiyel enerji, kuvvet toplamları ve diskriminant içeren eşitsizlikler sunar. Bu denetim ikinci eserin yalnız özetini kontrol etti; bütün teoremlerini dışlayan bir literatür sonucu iddia etmiyoruz. Galois gömme listesindeki tekrarlar nedeniyle diskriminant koşullarında minimal polinom/farklı kök ayrımı da gereklidir.

## 2,32 ve1,60 farkının kaynağı: işaret açıklaması yeterli değil

f_b=V_flat,b, a_b=A_b-1, B_b=sqrt((C_X,b-1)(C_Y,b-1)) olsun. Cauchy üst sınırı U=sum f_b(1+B_b), gerçek W=sum f_b(1+a_b). Tam ayrım:

    U-W = sum_b f_b(B_b-|a_b|)
          + 2 sum_(a_b<0) f_b|a_b|.

Birinci terim hizalanmanın büyüklüğünü Cauchy ile üstten sınırlama kaybı; ikinci terim işaretin atılma kaybıdır. İkinci terim mevcut V ve V_flat rasyonellerinden tam hesaplandı; birinci terim FFT moment tanılarını miras alır.

| r | U/W | İşaret kaybı / W | Büyüklük sınırının kaybı / W | Fazlalığın işaretten gelen payı |
|---|---:|---:|---:|---:|
|12|1,11427|0,08909|0,02518|%77,96|
|18|1,71236|0,14663|0,56573|%20,58|
|19|2,53836|0,27413|1,26422|%17,82|
|20|2,31925|0,15681|1,16244|%11,89|

r20'de işaretlerin atılmasından gelen fazlalığı tam geri kazansak U/W yaklaşık2,16244 olur; önceki dört-çift ayırma1,60355'ten hâlâ büyüktür. Bu karşılaştırma Claude'un farkı tam olarak işaret iptaline bağlayan açıklamasını bu panelde reddeder. r12'de işaret önemliydi; bütün paneller için tek açıklama yapılamaz.

rho=a_b/B_b ancak B_b>0 iken tanımlıdır; B_b=0 ise a_b=0, rho oranı0/0'dır. C_Y'nin bilinmesi tek başına rho'yu vermez: gerçek A ve C_X gerekir. Mevcut bütün sonlu verileri kullanınca rho'nun hesaplanması, çözülmesi gereken asimptotik tahmini sağlamaz. Ayrıca |rho|<1 büyüklük kaybı, rho'nun negatif olup olmamasından ayrıdır.

## Karar

Galois ve otokorelasyon dili matematiksel olarak doğru ve faydalı. 'Yeni indirgeme' önceki dördüncü-moment koduyla aynı; yeni emek, gerçek parite kodlamasının kaydırma korelasyonlarını uniform sınırlamaya gitmeli. İz-alt-sınırı literatürünü doğrudan ana rotaya taşımak için gerekçe yok. Önce ortak parite-ağırlık dağılımına daha ucuz bir rekürsiyon ya da istenen normalize moment üst sınırı sağlayan somut lemma aranmalı. Mevcut tepe ayırma ve ağırlıklı ortak yoğunlaşma hedefleri açık kalıyor.
