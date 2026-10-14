# CP20 Task 8 (E1–E7/E7R) bağımsız yenilik taraması

**Sınır:** Collatz problemi çözülmedi. Etiketler yayımlanmış öncelik, yöntem sıradanlığı ve programın kendi çürütmelerini ayırır; `NEW-CANDIDATE` yeni teorem tescili değildir. Yuan Si kaynağı Zenodo ön baskısıdır, hakemli yayın olduğu doğrulanmadı.

## Sayım

| Verdict | Adet |
|---|---:|
| KNOWN | 1 |
| SUPERSEDED | 0 |
| PARTIAL | 9 |
| STANDARD | 8 |
| NEW-CANDIDATE | 8 |
| INTERNAL | 7 |
| FLAWED | 5 |

**Toplam: 38 ayrı iddia.**

## NEW-CANDIDATE (güç sırası; ispat gücü ayrıca belirtilmiştir)

- **A01 [PROVED/FROZEN]** Kritik-log varsayımı altında N_r≈2^{αr/κ} pencerelerinde liminf h(D_1,D_2)≥α/κ. Yalnız koşullu kritik-log yörüngeler; literatürde aynı tip-özel nicel pencere teoremi saptanmadı.
- **A05 [PROVED — AUDIT EXTENSION CANDIDATE]** Her n≍2^{(α/κ)r} tam-ölçek penceresi için basınç birikim alt sınırı h(D_1,D_2)≥α/κ uzantısı V3 donmuş çekirdeğine dahil değildir. Bağımsız denetim bekleyen koşullu ek.
- **M02 [PROVED/FROZEN]** Her pozitif sonlu sözcükte negatif gölge 1≤X_k<3^k ve M_k=X_k (k≥1). Tam çift-adik/üç-adik eşitliğin literatür eşdeğeri bulunmadı; sonlu sözcük cebiri kendisi temel.
- **M03 [PROVED/FROZEN]** Kritik-log altında ρ_M(k)=max(0,ρ_r(k)−ln(3/2))+O(log k/k). Eşitlik koşullu; sayısal pozitif-alt-sınır [B-LEAD], kanıt değildir.
- **D03 [PROVED — NOT INDEPENDENTLY AUDITED]** Genel A_k/k→L tavan-limitinde r_k plateau/oran alternatifinin D0 uzantısı bağımsız denetlenmemiştir. Bağımsız denetim yok; varlığı ispat değildir.
- **D05 [PROVED/FROZEN]** Kritik-log altında liminf_k ln(1+r_k)/k=(ln 3) liminf_j t_j/t_{j+1}. D1 sınırlı alfabe/yaralanma zamanları için, Collatz çözümü değil.
- **D06 [PROVED/FROZEN]** Plato çukurunda ρ_r(t_{j+1})=(ln3)t_j/t_{j+1}−κ ln(t_j)/t_{j+1}+O(1/t_{j+1}). D05 ikinci mertebe özelleştirmesi.
- **R03 [PROVED/AUDIT PASS]** CF-left uçlarında r≥17000 için |K(k_r,l_r)−1|≤2πm_r2^(−W_r/2−4−β)+4m_r exp(−W_r²/(72αm_r))→0. Karşıteorem B3 üniform O(1/m_r) hedefine ters; mevcut Si teoreminin merkezi s≈2n bölgesi bu αn bölgesi değil.

## KNOWN / SUPERSEDED ve yakın öncüller

- **R04 KNOWN:** Si (2026, Zenodo DOI 10.5281/zenodo.20027097) doğrudan *koşullu affine Fourier* nesnesini ele alır: “by conditioning on S_n = s ... affine Fourier coefficient ... primitive ternary Bernoulli-bridge transform”. Tao (arXiv:1909.03562) önceki koşulsuz Syracuse affine modelidir. Projenin özgül modüler çarpanı Si ile aynı gözlenebilirin özel frekansıdır; sayıların tek tek hesabının aynen yayımlandığı iddia edilmiyor.
- **SUPERSEDED: 0.** İleri sürülen özgül κ-kritik pencere ve CF-left karşıteorem için doğrulanmış daha güçlü *aynı niceleyicili* yayın bulunmadı. Tao veya Si’yi bu sırf sözcük benzerliğiyle “superseded” saymak yanlış olur.
- **E11 PARTIAL:** Si’nin aynı mikrokanonik affine Fourier çerçevesi E6-N1’in model fikrini önceler; özel Hadamard/periyot özdeşliğinin özdeş yayımlanmış ifadesi doğrulanmadı.
- **R05 PARTIAL:** Si’nin tarif ettiği merkez/entropi ve h≥1 sert-frekans sonuçları αr+O(1), h=0 hedefini kapsamaz; negatif transfer programın denetiminde kanıtlandı.
- **E01 ve D01/D04 STANDARD:** sırasıyla mod-3 destek ve 2-adik lift/chunk cebiri; sırf ilgili makale olduğu için Tao/Si’ye mal edilmedi.

### Birincil kaynaklardan kontrol edilmiş kısa alıntılar

- **Atlanmaması gereken 1999 teoremi:** Garcia–Tal, *Acta Arith.* 90 (1999), 245–250, Teorem 1/Koroler 1: tam yörüngenin **değer kümesi** üst Banach yoğunluğu sıfırdır; ayrıca çakışma-denklik sınıflarının bir temsilci kümesi üst Banach yoğunluğu sıfırdır. [Yazarların PDF’si](https://www.impan.pl/shop/publication/transaction/download/product/110779?download.pdf): “A direct consequence is that any orbit O(n) under H has Banach density zero (Corollary 1).” Önceki yöntem-terimi taraması bunu atlayabilirdi. **A01’in koşullu kritik-*zaman* tip yoğunluğu veya D05’in injury oranı ile eşdeğer değildir.** Garcia–Tal teoremine bu koşullu ifadeleri kapsıyor atfı yapılmadı.

- [Tao, Almost all orbits of the Collatz map attain almost bounded values (2019/2022), arXiv:1909.03562](https://export.arxiv.org/api/query?id_list=1909.03562): “for any function f ... with lim ... f(N)=+infty ... Col_min(N) <= f(N) for almost all N ... in the sense of logarithmic density”.
- [Yuan Si, A microcanonical phase transition for the Collatz affine random model (2026), Zenodo 20027097 (preprint; hakemli yayın doğrulanmadı)](https://zenodo.org/api/records/20027097): “by conditioning on S_n = s. Under this conditioning the multiplicative phase becomes deterministic, and the affine Fourier coefficient at hard frequencies reduces to a primitive ternary Bernoulli-bridge transform”.
- [Inselmann, An approximation of the Collatz map and a lower bound for the average total stopping time (2024), arXiv:2402.03276](https://export.arxiv.org/api/query?id_list=2402.03276): “Results of Terras and Everett imply that ... almost all m ... fulfill ... simultaneously ... We extend this result to α=2(log(4/3))^{-1}”.
- [Lagarias, The 3x+1 problem: An annotated bibliography (1963--1999), arXiv:math/0309224](https://export.arxiv.org/api/query?id_list=math/0309224): “This paper is an annotated bibliography of work done on the 3x+1 problem and related problems from 1963 through 1999.”.
- [Lagarias, The 3x+1 Problem: An Annotated Bibliography, II (2000-2009), arXiv:math/0608208](https://export.arxiv.org/api/query?id_list=math/0608208): “This paper is an annotated bibliography of work done on the 3x+1 problem published from 2000 through 2009”.
- [Parity sequences of the 3x+1 map on the 2-adic integers and Euclidean embedding, arXiv:1805.00133](https://export.arxiv.org/api/query?id_list=1805.00133): “we consider the one-to-one correspondence between a 2-adic integer and its parity sequence under iteration of the so-called 3x+1 map”.

Arama: arXiv API (`id_list`, “Collatz Fourier”, “3x+1 parity”, “Collatz cycles”), OpenAlex (“Banach density/sparsity/reciprocal sum”, “windowed count/stopping time”, “inverse tree density”, “2^m-3^k/cycle”, “microcanonical Fourier”), Crossref, Semantic Scholar ve Zenodo sorguları denendi. Semantic Scholar `429` döndürdü; bu hizmette sonuç **DOĞRULANMADI**. Sorgu-iddia dökümü JSON dosyasındadır. Lagarias iki bibliyografyasının ilki PDF olarak ayrıca Garcia–Tal maddesi için açıldı, ikincisinin yalnız API özeti açıldı: kayıt eşitliklerinin kapsanmamasına ilişkin kesin negatif kanıt değillerdir.

## Yanlış “yeni” / overclaim ve doğruluk sınırları

- **En ciddi literatür boşluğu:** Önceki yöntem-sözcüğü taraması koşullu affine Fourier nesnesini kaçırmış: Si 2026 mikrokanonik Fourier gözlenebilirini açıkça tanımlıyor; E6-N1’in **tümünün** özgün mekanizma diye anlatılması fazla iddialı. R04’te tam model eşlemesi verilmiştir; E7R-LT doğru olarak doğrudan *teorem transferini* kapatır, nesne önceliğini değil.
- D1 bağımsız denetimindeki “GERÇEKTEN YENİ” D05/D06 için literatür sertifikası değil; eşdeğer yayını bulamadığımızdan `NEW-CANDIDATE` yazıldı. D0’ın 2-adik temel sonuçları da yenilik diye sunulmamalı.
- Task8A V2 tam-kutu h iddiası h(0,M₂)=−∞ karşıörneği nedeniyle V3’te düzeltildi. CP19 T4’e köprü ayrıca kurum-içi önceki sonuca dayanır; “Sturmian penalty” kesin pozitif iddiası doğru değil.
- D-T4 (w=(1), en küçük tam gerçekleştiren 3) ve D-T5 (a≡2,n₀=1 çevrimi) ilk geniş iddiaları çürütür. D1-E faz tekrarından otomatik değerleme teoremi yok.
- E0 tüm frekanslarda üstel spectral gap, mod-3 için |φ|≥1/2 yüzünden yanlıştır; düşük conductor karşıörneğini E1’in yüksek conductor açık hedefiyle karıştırmayın.
- E7 özgün B3 üniform O(1/m_r) **yanlış**: E7R-B3 CF-left pencere noktalarında |K|→1 karşıteoremi var. R03 kanıtı *B4 küresel hedefini* tek başına çürütmez veya kanıtlamaz.
- E5/E6 yalnız S1/N1 exact normal formlar; N_r=O(r^(−3/2)), E6-N2, derece-bir asimptotiği **OPEN**. E7 başlangıç seal’i PRE-RUN; E7R sonraki iyileştirmesi ayrı tarihlidir. B4 V2 yetkisi giriş-bütünlüğü hatasıyla T1 başlamadan tüketildi; B4 V2 bilimsel başarısı yok.

## Okuma kapsamı ve açık sınırlar

- Okundu: `arch-era-d2.log` (260 satır), CP20 Task8 8A V2/V3 ve sertifika özeti, 8B0/8B1/8B2 D0-D1 master/theorem, Module E E0–E7 master/theorem/seal/stratejik kayıtları; `Collatz/bagimsiz-denetim/10-task8a`, `11-surekli-kesir-denetim`, `12-d0-denetim`, `13-d1-denetim` raporları ve E7R dört bağımsız denetim raporu; E4 bağımsız denetim raporu ve E7R-LT kaynak kayıtları. JSON’da her iddia için tek tam kaynak yolu vardır.
- Açılmayanlar: 8B3 E3 yaklaşık 88 MB RAW_SERIES.json ve 14.7 MB CSV bütün olarak, paket ZIP’leri tam açılıp her iç dosya denetlenmedi, docx ikili dosyaları okunmadı (mevcut düz metin eşleri tercih edildi); tüm 319 Task8 dosyasının satır-satır dış literatür kontrolü yapılmadı. Her exact/sayısal sonuç yeniden hesaplanmadı; bağımsız denetim raporlarının açık sınırları gözetildi.
- Birincil kaynak API özetleri Tao/Inselmann/Lagarias/parity için, Zenodo doğrudan metadata/abstract Si için açıldı. Si’nin PDF’sindeki teorem koşulları projenin E7R-LT bağımsız denetiminde okunmuştur; burada PDF’nin her sayfası yeniden kontrol edilmedi. Garcia–Tal 1999 PDF’si açıldı; değer kümesinin Banach yoğunluğu teoremi doğrulandı, fakat koşullu kritik-zaman basıncı sonucunu kapsamadığı ayrımı yapıldı. Başka bir 1999 teoreminin eşdeğerliğinin bulunmaması yokluk kanıtı değildir.

NOVELTY_SCAN_E4_CP20_T8_E7_20260923_COMPLETE
