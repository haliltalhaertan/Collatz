# CP21–CP24 bağımsız yenilik denetimi

**Hüküm:** Collatz problemi çözülmedi. Bu dosyalardaki önek-kaynağı monotonluğu ve yarıçap-2 charging hâlâ varsayımdır. «NEW-CANDIDATE» yalnızca belirtilen taramada aynı ifadeyi bulamadığım anlamına gelir; öncelik veya doğruluk sertifikası değildir. Ayrıntılı, dosya-yolu ve arama-sorgusu içeren **51 ayrı karar** `ledger_E6_CP21_24.json` dosyasındadır.

## Sayım

| Karar | Adet |
|---|---:|
| KNOWN | 3 |
| SUPERSEDED | 1 |
| PARTIAL | 1 |
| STANDARD | 19 |
| NEW-CANDIDATE | 5 |
| INTERNAL | 14 |
| FLAWED | 8 |
| **Toplam** | **51** |

`INTERNAL` bir sonlu tanığın yanlış olduğu anlamına gelmez: yalnızca programın tanımladığı eşitsizlik/hesap veya ölü ispat yolu için dışarıdan yenilik karşılaştırmasının uygun olmamasıdır. `FLAWED` kayıtlarının birçoğunu **programın CP24 düzeltmesi zaten geri çekmiştir**; güncel teoremlere yanlışlık atfetmiyorum.

## Arama ve birincil metin kapısı

Nesne sorgularını yöntem sorgularına ekledim: **“Banach density / sparsity / reciprocal sum / windowed count / stopping time distribution / Garcia Tal”**; **“parity vector / affine offset / endpoint collision / residue class / 3^k / Böhm Sontacchi / Wirsching / Rozier”**; **“cycle length / 2^m−3^k / local minima / 3x−1 / Simons de Weger / Eliahou / Steiner / Hercher”**; ayrıca **“inverse tree density / max-entry cap / source energy / Fourier monotonicity”**. arXiv API, Crossref, OpenAlex, Semantic Scholar ve Zenodo denendi; Semantic Scholar bazı sorgularda HTTP 429, OpenAlex daha sonra kota hatası verdi. Sonuçları tek başına atıf saymadım. Lagarias'ın [1963–1999](https://arxiv.org/pdf/math/0309224) ve [2000–2009](https://arxiv.org/pdf/math/0608208) bibliyografyalarının **PDF'leri okundu**: bunlar içerdiği çalışmaların *birincil metni değildir*.

Önemli yakalama: [Garcia–Tal 1999'un **orijinal, altı sayfalık makalesini açtım**](https://www.impan.pl/shop/publication/transaction/download/product/110779?download.pdf), *A note on the generalized 3n+1 problem*, Theorem 1: **“The Banach density of P is zero”**; Corollary 1: **“The Banach density of the orbit O(n) under H is zero.”** `P`, aynı sayıda iterasyondan sonra birleşme bağıntısının sınıf temsilcileridir. Dolayısıyla *olası diverjan Collatz yörüngesi bile* Banach-yoğunluğu sıfır olan bir kümededir. Bu, sırf “neredeyse hepsi iner” sezgisinden güçlü bir **mevcut seyrek-yörünge teoremidir**; fakat CP21'in belirli `Ecal` veya charging eşitsizliğini **kanıtlamaz**. Makalenin girişindeki Lagarias 1985'e atfedilen `O(x^(1−η))` kaçak-girdi sınırı ayrıca **ikincil aktarım** olarak işaretlendi; Lagarias 1985 birincil metni açılmadı.

Diğer açılan birincil metinler: [Bernstein–Lagarias 1996](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/3x-1-conjugacy-map/6975BB4A8C46CF6842217043AAF9EC13) özeti, **“The map Φ mod 2^n induces a permutation Φ_n on Z/2^n Z”**; [Rozier–Terracol 2026](https://arxiv.org/pdf/2502.00948v5) girişinde **“T^j(n) = (3^q/2^j)n + E_j(n)”**, `E_j` parite kelimesine bağlı; [Simons–de Weger 2005'in orijinal PDF'i](https://www.impan.pl/shop/publication/transaction/download/product/82263?download.pdf), **“Corollary 2. K > 2.2564 · 10^8”** (nontrivial pozitif çevrimde tek adım sayısı). Karşılaştırma için [Tao](https://arxiv.org/pdf/1909.03562) özeti **“Col_min(N) ≤ f(N) for almost all N ... (in the sense of logarithmic density)”** ve [Inselmann](https://arxiv.org/pdf/2402.03276) özeti **“extend this result to α=2(log(4/3))^−1 ... maximally possible value”**: bunlar tipik-yörünge sonuçlarıdır, her yörünge değil. **Böhm–Sontacchi 1978, Lagarias 1985 ve Wirsching 1998'in birincil kitap/makale metinlerini açamadım: ilgili doğrudan içerik atfı DOĞRULANMADI.** Bibliyografik özetleri onların yerine ispat diye sunmuyorum.

## NEW-CANDIDATE: en kuvvetli/ilginç olandan daha dar olana

1. **E21-20, radius-2 charging.** Gerçek histogram için tüm `[a,b]` aralıklarında `Σ max(L_k,0) ≤ Σ M_j` (indis aralığı ledger'da). CP24'te 221 **farklı** `(m,s)` satırı, 33.540 aralık, bunların 18.259'u pozitif talepli, sıfır ihlal; **genel kanıt yok**. Nesne odaklı `windowed count`, `inverse tree density`, `source energy` taramasında eşdeğeri bulunmadı. (20,3)[14,16] oranı yalnız `29517649/28111980`; yakınlık ispat değil.
2. **E21-04, tek frekanslı defect ≥ 0.** Doğru ortak indis tek `a mod 2^s`; 41+35 tablo **76 benzersiz değil, 57 benzersiz** çift (19 tekrar). CP24 bütün siklotomik işaret belgelerini yeniden çalıştırmadı. `parity vector / Fourier source monotonicity / residue class` sorguları eşdeğer bir yayın vermedi.
3. **E21-02, kaynak monotonluğu `M_merge≥L_lift`.** 221 sonlu satırda geçiyor, evrensel teorem değil. Tao/Inselmann'ın neredeyse-hepsi sonuçları ve Garcia–Tal'ın yörünge seyreklik teoremi **farklı nesneler**; biri diğerine bu dosyalarda indirgenmiyor. `source energy / windowed count / Banach density` tarandı.
4. **E23-04, `3n±1` için özel `Ecal` tablosunun işaret körlüğü.** Genel işaret-eşlenikliği basit cebir; özel `P^-_{m,k,r}(z)=P^+_{m,k,r}(3^k−z)` ve `Ecal^-=Ecal^+` programın tanımladığı fonksiyonelin kendi lemasıdır. `3x−1 cycles / parity vector / affine offset / source energy` sorgularında bu **özdeşlik aynen** bulunamadı; yenilik payı son derece dar.
5. **E21-11, T4 maksimum-yığın üst sınırı.** Tam ifade `M(m,k)≤⌊2^(m−k)(3^(k−1)−2^(k−1))/3^k⌋+1`. `max entry cap / parity vector endpoint multiplicity / B-spread` taramasında bu **özel formül** yok; klasik afin ifadeden gelen kaba sınır olduğundan düşük öncelikli aday. Kaynakların yalnız ilgili özetleri açılabildiğinden mutlak yenilik çıkarılmamalı.

## KNOWN / SUPERSEDED / PARTIAL ve «yeni» sanılmaması gereken özdeşlikler

- **KNOWN E23-01:** `2^mH^m(h)=3^k h+B_w` afin kelime ifadesini Rozier–Terracol'un açılan birincil girişindeki `3^k/2^m` katsayısı ve pariteye bağlı kalan **kapsar**. **KNOWN E23-09:** pozitif çevrimde `x=B_w/(2^m−3^k)` klasik afin çevrim denklemidir; Simons–de Weger'ın çevrim araştırması ile [Lagarias'ın](https://arxiv.org/pdf/math/0309224) Böhm–Sontacchi kaydı karşılaştırıldı. **KNOWN E23-07:** Garcia–Tal 1999'un daha güçlü Banach-yoğunluk-sıfır yörünge sonucu, CP23'ün “ortalama bilgi tek kaçak yörüngeyi elemez” uyarısı için doğrudan ilgili; CP21 monotonluk ile karıştırılmamalı. **STANDARD E24-04:** integral `bB_w/D` adayının ayrıca parity-word öz-tutarlılığı sınanmasının zorunlu olmaması, klasik mod-`2^m` bijeksiyon + afin denklemle elde edilir; bire bir aynı cümleyi eski basılı metinde görmedim, bu karar bağımsız tarihsel öncelik ilanı değildir.
- **SUPERSEDED E24-09:** `m≤14` pozitif `3n+1` döngü yok sonlu kontrolünün *döngü-dışlama gücü* Simons–de Weger 2005'in `K>2.2564·10^8` yayımlı alt sınırınca aşılmıştır. Bu hüküm CP24'ün `3n−1` için 29 adayını veya sayısal ham dosyasını kapsamaz; yalnız pozitif `3n+1` dışlaması.
- **PARTIAL E24-06:** `H^m(h)<h ⇔ (2^m−3^k)h>B_w` standart afin kriterdir; `m=8` için 94/128, `m=16` için 27.823/32.768 programın **küçük son-nokta kalibrasyonlarıdır**. Rozier–Terracol birincil metni parite katsayısı `<1` olmasına rağmen iniş olmama örnekleri ve kalan-terimi doğrudan inceler. Son-nokta inişi ile bir-zamanlı stopping time aynı şey değil.
- **STANDARD, bağımsız yayın önceliği iddiası yok:** T2 `1≤e_w≤3^k−1`; T7 `e_w=e_w′ ⇔ B_w≡B_w′ (mod 3^k)` (çünkü `3^k |(e−e′)` ve farkın mutlak değeri `<3^k`); A4 `B_w ≢0 (mod 3)` (ilk tek-adım terimi kalır); bundan `#farklı uç=#dolu B-sınıfı≤2·3^(k−1)`; cap'in `2^r≥3^k−1` sonrasında sabitlenmesi; parity-word/kalıntı bijeksiyonu; `H_-(−x)=−H_+(x)`. **CP23'ün “A3+A4 publishable/plausibly new” yargısı literatür taraması değildir:** basit afin+aralık+bölünebilirlik çıkarımına bağımsız yenilik ödülü vermiyorum. T4'ün *özgül sınırı* içinse ayrı NEW-CANDIDATE kararı var.

## Hatalı «yeni», aşırı yorum ve son düzeltmeler

- **T7r `[PROOF]` yanlıştı (E21-13):** `(m,k,r)=(4,2,1),h=1,13` için önerilen `t` var ama uçlar `1,8` mod 2 eşit değil. İleri yön gerekli koşul olarak kalır. **T6 ve T4'ü bundan ötürü otomatik çürütmüyorum.** CP21'de R3'ün q-uzunluklu doğal okuması da `(4,2),k=3` ile yanlış; CP22 tam anti-periyodik `N` sürümünü ve R1'in iki farklı çarpanını açıkladı (E21-06–07).
- **Eski CP21 m=25/26 sonuçları yanlış (E21-18):** `fine[:N]` kesimi katlamanın (`coarse[z]=Σ fine[z+jN]`) yerini tutmaz; CP24 11 satırı baştan saydı. CP22'nin 18 sıcak-bölge satırı yeni parametre değildi: **210+11=221**, 239 değil. Frekans tablolarında 76 değil **57** farklı parametre. `defect/M>1` genellemesi de `(4,2)` için `9/17` ile yanlış.
- **CP23 L2 “sabit r'de enerji sönmez” hükmü kanıt değildi:** sonlu `m≤12` ham artışından limit çıkmaz; normalize enerji `Ecal/2^(m−1)` olur (örnek `r=2`: `m=4` için 1, `m=12` için `249/35840`). CP24 geri çekti. Sabit `m+r` diyagonali **sonludur**; CP23'ün o diyagonal boyunca sonsuz monoton dizi limiti yorumu da yanlış.
- **İşaret-körlüğünün sınırı:** `3n−1` döngüsü `5→7→10→5` ve aynı `Ecal` tabloları, *yalnız bu değişmeze dayanan* Collatz'a giden zinciri öldürür; **her** modüler/kombinatoryal yöntemin işe yaramayacağını göstermez. Yansımanın m=1,h=1 sabit örneği vardır; değişmez olan farklar değil **fark kareleridir**. CP24 bunu kaydetmiştir. `x=bB_w/D` integral ise gerçek kelimeyi kendiliğinden izler; ayrı parity kontrolü yeni eleme değildir.
- Mutlak cap sınırının olmadığı sonucu doğru fakat CP21'deki tek `M(20,6)=39` örneği **tek başına bunu ispatlamaz**. Onarım: sabit `k=2` için `n_2=m−1` başlangıç, en çok `2·3=6` farklı tam uç; güvercin yuvası ile `cap≥⌈(m−1)/6⌉` yeterlidir. Sayısal deney ile nicelenmiş ispat arasındaki fark önemlidir.

## Kapsam / okuma sınırlaması

Okundu: dört ana `CP21_REPORT.md`–`CP24_REPORT.md`; CP21 `02-cap-bound/REPORT.md`, `03-induction/REPORT.md`, CP23 `03-salvage/salvage_report.md`, CP24 dış görüş ve doğrulama açıklamaları; belirtilen `cp21-bridge.log`, `cp21-audit.log`, `cp21-prove.log`, `CP21_LITERATURE_SWEEP.md`, `r8-*.log`, `induction/REPORT.md` ve ilgili sonlu tanık/kod yol ve sayıları; örneklenen JSON'lar. **15 MB'lık `flank_Btrend.json` bütünüyle okunmadı;** aynı içeriğin kopyaları, tüm Muse oturumları, tüm kodların yürütme izleri, 210 eski histogramın baştan sayımı ve 57 frekans satırının işaret sertifikaları bu bağımsız yenilik taramasında yeniden çalıştırılmadı. Dolayısıyla dosya-içi sonlu aritmetik rapor edildiğinde “programın raporladığı/CP24'ün kontrol ettiği” olarak okunmalı. Birincil metin erişimi açılmayan Böhm–Sontacchi 1978, Lagarias 1985 ve Wirsching 1998 için kesin bire bir tarihsel yenilik hükmü **DOĞRULANMADI**; `STANDARD` verilen basit özdeşlikler tarihsel ilk yayın iddiası değil, verilen bağıntılardan doğrudan kısa ispat kararıdır. Hiçbir dosya `/mnt/c` altında değiştirilmedi; çıktı yalnız çalışma dizinine yazıldı.

NOVELTY_SCAN_E6_CP21_24_20260923_COMPLETE
