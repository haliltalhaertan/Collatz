# CP24 — Kurtarma, hesap düzeltmesi ve kapsam denetimi

**Collatz çözülmedi.** Bu paket CP24'ün yarım işlerini denetlenebilir bir kapanışa taşır; yeni bir evrensel yörünge/döngü dışlama teoremi ilan etmez. Önceki CP21–23 raporlarının aşağıda belirtilen sayı ve yorumlarını düzeltir. Orijinal dosyalar korunur.

## 1. En önemli sonuç: liderin eski hesap kodunda gerçek hata

`cp21_lead_extension_m25_m26.json` içindeki **11 satır hatalıdır**. İlk denetim, hepsinde `sum(merge_terms) != merge` olduğunu yakaladı. Bu bir yuvarlama farkı değildir.

Kök neden eski sohbetin **20260914_102430_a9543e / mesaj 7451** içindeki `row()` fonksiyonudur:

```python
P = P[:N]
arr = arr[:q]
Pf = hin.get(k, ... )[:N]
```

Histogramlar mod 128'de tutuluyordu. Daha küçük modüle geçiş, dizinin başını kesmek değildir; aynı kalıntıya düşen kutular **toplanmalıdır**:

```python
coarse[z] = sum(fine[z::N])
```

Kesme işlemi kütleyi kaybettirirken paydada tam binom kütlesi kalıyordu. En yüksek girdi çözünürlüğünde bazı terimler tesadüfen doğruydu; çıktı histogramı yine kesiliyordu.

**Kök neden doğrulaması:** `regression_truncation.py`, aynı kesme hatasını yeni histogramlara bilerek uygulayıp 11 eski satırın bütün ana alanlarını (`input,fine,output,lift,merge,defect,lift_terms,merge_terms`) birebir yeniden üretti. Hatanın yalnız int64 taşması olduğu alternatif açıklama veriyi yeniden üretemedi. Orijinal hesap zaten enerji tarafında Python tamsayıları kullanıyordu.

**Düzeltme:** `recompute_extension.py`, m=25,26,27 yörüngelerini yeniden sayar; int64 yalnız sınırı önceden denetlenmiş yörünge/sayım kısmındadır. Enerji ve kareler Python'un sınırsız tamsayı/Fraction aritmetiğindedir. Her stratumun kütlesi binom katsayısına eşit olmalıdır. Transferden üretilen sonraki histogram ayrıca doğrudan sonraki-seviye yörünge sayımıyla **kutusu kutusuna** karşılaştırıldı.

Çıktı: `cp24-recovery/corrected_extension.json`. Eski dosya değiştirilmedi; paket içinde karşılaştırma amacıyla bulunur. Bu düzeltme liderin önceki hatasını giderir, Muse'a mal edilmez.

## 2. Sayım kapsamı ve eşitsizlikler

| Veri | Dosyada satır | Birleşime yeni katkı |
|---|---:|---:|
| Round 8 arşiv tablosu | 210 | 210 |
| Yeniden üretilmiş CP21 uzatması | 11 | 11 |
| CP22 ATTACK sıcak bölge tablosu | 18 | 0 |
| **Tekilleştirilmiş toplam** | | **221** |

Dolayısıyla önceki **239 farklı satır** ifadesi doğru değildir. CP22'nin 18 satırı yeniden hesaplama/çapraz kontrol sağlamıştır, yeni parametre kapsamı değil.

`lead_verify.py` bu 221 satırın tüm `[a,b]` aralıklarını kesirlerle yeniden değerlendirdi:

- **33.540 aralık**, **18.259 pozitif talepli aralık**, yarıçap-2 ihlali **0**.
- Kalan aralıklar sıfır taleplidir; bunları aynı güçte kanıt saymıyoruz.
- En dar oran hâlâ `29517649/28111980`, `(m,s)=(20,3)`, `[14,16]`.
- İlk 210 satır bu turda baştan yörünge taramasıyla üretilmedi; arşiv terimlerinin özdeşlikleri ve aralıkları kontrol edildi. Yeni 11 satır sıfırdan üretildi.
- Hedef `M_merge >= L_lift` ve yarıçap-2 **genel olarak hâlâ conjecture**. Sonlu hesap ispat değildir.

Frekans tablolarında 41 eski + 35 sonraki satırın **19'u ortak**, birleşim **57 farklı `(m,s)`**. Bu tur yalnız kapsamı ve ortak toplam defect değerlerini doğruladı; bütün siklotomik işaret sertifikalarını yeniden çalıştırmadı. “35 yeni satır” yerine “35 hesaplanmış satır, 16 yeni parametre çifti” denmelidir.

Önceki `defect/M` yorumunda da hata vardı: `(4,2)` için `defect/M=9/17<1`. Pozitif toplam lift bulunan satırlar `(4,2),(8,2),(10,2),(10,9),(11,9)`; tamamının oranı `margin_audit.json` içindedir. “Hiçbirinde 1'in altına inmedi” ifadesi geri çekilir.

CP22 yapay tanığının kütle, tavan, destek ve tamsayılık koşulları da gerçek `(20,3)` histogramı sıfırdan sayılarak yeniden doğrulandı. Bu tanık belirli kaba koşulların yetersizliğini gösterir; gerçek Collatz kaynağında karşıörnek değildir. Bu tur tanığın 91 ihlal sayısını ayrıca yeniden saymadığımız için onu yeni doğrulama toplamına katmıyoruz.

## 3. Simetrinin doğru kapsamı

Tanım: `H_b(x)=(3x+b)/2` tek x için, `x/2` çift x için; `b=±1`.
`w`, m adımın pariteleri; `k=|w|`; **işaretsiz** `B_w` için

`2^m H_b^m(h)=3^k h+b B_w`.

### [PROOF — elle denetlenmiş, Lean değil] Yansıma

m≥1 ve tek `1≤h<2^m` için `H_+` başlangıcı h ile `H_-` başlangıcı `2^m-h` aynı kelimeyi üretir; işaretsiz B aynıdır ve uç noktalar toplamı `3^k` olur.

Gerekçe: `H_-(-x)=-H_+(x)` her tamsayıda doğrudur. Aynı mod `2^m` kalıntısındaki başlangıçlar ilk m paritede aynıdır; her adımda farkın 2-adik bölünebilirliği yalnız bir basamak azalır. `2^m-h≡-h` olduğundan kelimeler eşleşir. İki afin özdeşlik toplanınca uç nokta formülü gelir.

Dolayısıyla histogramlar `P^-(z)=P^+(3^k-z)` ile eşleşir. Tamamlayıcı kutu çiftlerinin **fark kareleri** yer değiştirir; `J_r` ve Ecal tüm geçerli m,r için aynıdır. Bağımsız lider kontrolü m=1..14'te **16.383 eşleştirme**, sıfır hata.

**Sınır:** Sadece bu yansımaya göre değişmez gözlenebilirler ve onlara dayanan, iki haritada da aynı biçimde geçerli hipotezler ayıramaz. Başlangıç etiketi, işaret, büyüklük veya haritaya özgü ek koşullar dahil edilince aynı hüküm otomatik geçmez. Bir ortak lemma hâlâ yardımcı olabilir. “Hiçbir modüler/kombinatoryal yöntem işe yaramaz” sonucu çıkarılamaz.

### Muse raporuna lider düzeltmeleri

Muse raporu özgün biçimiyle `muse_AUDIT.md` olarak korunmuştur; aşağıdaki düzeltmeler önceliklidir:

1. Yansımanın “hiç sabit başlangıcı yok” yan cümlesi m=1,h=1'de yanlış; m≥2 için doğrudur. Ana yansıma özdeşliğini bozmaz.
2. Yansıma altında işaretli farkların kendisinin çokluğu değil **karelerinin** çokluğu korunur. `B_w` işaretsiz, `bB_w` işaretli ofsettir; iki konvansiyon karıştırılmamalıdır.
3. “negated-B multisets” tek başına iki haritada aynı veri değildir. Geçerli sınıfın tanımı yansımaya/işaret değişimine değişmez fonksiyoneller olmalıdır.
4. `H_+` için 1 sabit nokta değildir: trivial döngü `1→2→1`; yalnız `H_+^m` için çift m'de sabittir.
5. `muse_checks.py` içindeki `check(..., True)` satırları gerçek test değildir; kullanılmayan `B5` placeholder ifadesi de kanıt değildir. F5 kapalı yörüngesi gerçek hesapla denetlenmiştir. `ALL_OK`, rapordaki her cümlenin doğrulandığı anlamına gelmez.
6. “Karışma yalnız normalize enerji demektir” de fazla geniştir. Aşağıdaki nicelik belirli ağırlıklı üst-bit dengesizliğidir; tam dağılım karışması/yörünge kontrolü için ek tanım ve köprü gerekir.

## 4. Döngü öz-tutarlılığı: yalnız hesap değil, kısa türetme

### [PROOF — elle denetlenmiş, Lean değil]

`w_0=1`, `D=2^m-3^k`, `x=bB_w/D`. x tamsayıysa, **her iki işarette**, x gerçek w kelimesini üretir ve `H_b^m(x)=x`. Pozitif döngü istiyorsak ayrıca x>0 gerekir; asıl periyot m'yi böler.

Önce kelime-kalıntı bijeksiyonu: m=1 tabanı doğrudur. Bir uzunluk-m kelimenin başlangıçları h ve h+2^m aynı ilk m pariteye sahiptir; m'inci uçları `3^k` kadar farklı, dolayısıyla bir sonraki pariteleri terstir. Böylece iki uzantının ikisi de birer kez gerçeklenir.

w'yi üreten h temsilcisi ve e ucu için `2^m e=3^k h+bB_w`. Aday denkleminden çıkarınca

`2^m(e-x)=3^k(h-x)`.

3 tek olduğundan `x≡h (mod 2^m)`; x aynı w'yi üretir. Afin denklemden de m'inci ucu x olur. Pozitiflik, B_w>0 nedeniyle + haritada D>0, − haritada D<0 demektir.

Bu nedenle **bölünebilirlikten sonra parite öz-tutarlılığını kontrol etmek yeni bir matematiksel eleme sağlamaz**; programlama hatalarını yakalayan bir kontrol olarak yine yararlıdır. Bu eleme yoluna daha fazla araştırma bütçesi ayrılmadı. Sonuç için özgünlük iddiası yoktur.

Liderin sonlu kontrolü m≤14: + haritada 7, − haritada 29 pozitif kelime-adayı; hepsi öz-tutarlı. Bunlar **farklı ilkel döngü sayıları değildir**; tekrarlar/rotasyonlar içerir. Muse ayrıca m≤8'de pozitif ve negatif tamsayı adaylarını soyut kelimelerden test etti.

## 5. Normalize enerji: önceki sönüm yorumunu geri çekiyoruz

`p_k=P_k/n_k`, `pi_k=n_k/2^(m-1)`. J ikinci dereceden homojen olduğu için

`sum_k pi_k J_r(p_k) = Ecal(m,r)/2^(m-1)`.

Bu cebirsel özdeşlik, J tanımından doğrudan gelir. Normalize edilmemiş enerjinin artması normalize niceliğin azalamayacağını göstermez. Örneğin r=2'de:

| m | Ecal | Normalize nicelik |
|---|---:|---:|
| 4 | 8 | 1 |
| 12 | 498/35 | 249/35840 |

Bu iki değer bir limit teoremi değildir. Önceki sonlu enerji dizisinden “asimptotik sönüm yok” çıkarımı geri çekilir. Sabit m+r diyagonali sonludur; tek başına sonsuz-dizi yakınsaması vermez. Enerji monotonluğu, normalize denge, tam dağılım karışması ve tek-yörünge inişi ayrı hedeflerdir.

## 6. Küçük yeni kalibrasyon ve literatür kapısı

Muse'un önerdiği sınırlı kalibrasyon da bitirildi: sabit m sonunda `H_+^m(h)<h` sayısı, (a) doğrudan yörüngeler ve (b) soyut kelimelerden modüler tersle h üretip `Dh>B_w` sınaması ile **başlangıç başına** karşılaştırıldı.

- m=8: 94/128 iniş; D>0 olduğu halde son noktada inmeyen başlangıçlar `1,7,9,19,25`.
- m=16: 27.823/32.768 iniş; D>0 olduğu halde inmeyen tek başlangıç 1.

Bu sonlu pencere ve son-nokta ölçüsüdür; “bir zamanda ilk iniş” ya da yoğunluk-1 teoremi değildir. Kullanılan tam koşul D>0 değil, **Dh>B_w**'dir.

Rozier–Terracol'un erişilen giriş bölümü de afin yinelemeyi katsayı ve pozitif kalan olarak ayırıyor ve katsayının tek başına büyüme/iniş davranışını ne ölçüde belirlediğini araştırıyor.[1] Dolayısıyla bu kalibrasyonu yeni buluş diye sunmuyoruz. Bu tur erişilen metin giriş/özetle sınırlı; tüm makalenin ispatı veya yenilik taraması onaylanmış değildir. OUTSIDE'ın web'siz prior-art hükümleri yargı olarak kalır.

**Sonraki araştırma kararı:** yeni büyük tarama değil; işaret/büyüklük duyarlı `Dh>B_w` koşulunun hangi gerçek hipotez altında tüm başlangıçlara uzatılabileceğini, mevcut literatürün kalan-terim sonuçlarıyla kıyaslayan tek, sınırlı hedef. Kabul şartı, sadece aynı koşulu yeniden söylemeyen bir sınır ve Collatz'a açık çıkarım; aksi halde yalnız kalibrasyon olarak kapatılacak. Bu paket böyle bir sınır elde ettiğini iddia etmez.

## 7. Ajan durumu ve yeniden üretim

Yeni Muse kapsam denetimi tamamlandı: gerçek rapor + kontrol kodu + sonuç JSON'u var; girdilerinin SHA256'ları önce/sonra aynı. Lider `muse_checks.py`yi ayrıca çalıştırdı: `ALL_OK`. Üç eski yarım oturumu “üç tamamlanmış bağımsız rapor” diye saymıyoruz. Bu turun matematiksel yorumları insan veya Lean kernel denetiminden geçmedi.

Paket kökünden:

```bash
python cp24-recovery/recompute_extension.py
python cp24-recovery/regression_truncation.py
python cp24-recovery/lead_verify.py
python cp24-recovery/calibration.py
python cp24-recovery/muse_checks.py
```

Gereksinim: Python 3.11+, numpy; diğer modüller standart kütüphane. Çalışma dizininden bağımsız yollar `__file__` üzerinden kurulur. `original/` eski ham Muse malzemesidir, otomatik çalıştırılmaz; bazı eski scriptler mutlak yollar veya bitmemiş iddialar içerir.

**Kapanış:** CP24 kurtarma/denetim tamam. Gerçek bir kod hatası düzeltildi, aşırı güçlü yorumlar daraltıldı, bir gereksiz eleme yolu analitik olarak kapatıldı. Collatz'a yeni genel çözüm köprüsü henüz yok.

## Sources

[1] https://arxiv.org/html/2502.00948v5 — Rozier and Terracol: Paradoxical behavior in Collatz sequences
