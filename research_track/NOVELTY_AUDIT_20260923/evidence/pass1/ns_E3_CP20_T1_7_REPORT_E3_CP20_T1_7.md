# CP20 Task 1–7: bağımsız yenilik denetimi

**Karar:** Collatz çözülmedi. Arşivin `[PROVED]` etiketi bir **program içi ispat değerlendirmesidir**, yayınlanmış/öncelik kazanmış sonuç anlamına gelmez. Aşağıdaki kararlar, birbirinden ayrılmış **47 iddiaya** ilişkindir; tam cümleler, özgün etiketler, mutlak dosya yolları, üçer nesne/yöntem sorgusu ve açılmış kaynak alıntıları `ledger_E3_CP20_T1_7.json` içindedir. `NEW-CANDIDATE` yalnızca “aradım, eşdeğerini bulamadım” demektir.

## Sayım

| Karar | Adet |
|---|---:|
| KNOWN | 0 |
| SUPERSEDED | 2 |
| PARTIAL | 5 |
| STANDARD | 13 |
| NEW-CANDIDATE | 9 |
| INTERNAL | 14 |
| FLAWED | 4 |
| **Toplam** | **47** |

**Literatürde mutlaka kaydedilmesi gereken öncelik:** [Garcia–Tal, *A note on the generalized 3n+1 problem*, *Acta Arith.* 90 (1999), 245–250](https://doi.org/10.4064/aa-90-3-245-250), açılan **orijinal PDF** Korolar 1: “**The Banach density of the orbit O(n) under H is zero.**” Yalnızca nitel bir cümle de değildir: Teorem 1'in (6) numaralı eşitsizliği, Heppner'in `δ₁,δ₂∈(0,1)` katsayılarıyla **her değer penceresinde** `O(log X·(X^{1−δ₁}+X^{δ₂}))` sınırını verir. Buradan ıraksak bir yörüngede `Σ1/n_k<∞` dyadik toplamla çıkar; *üstelin sayısal değeri* Garcia–Tal'da verilmez. Bu 1999 yayınını, CP20'nin “occupation/pressure” yöntem kelimeleriyle yapılan önceki taramasının atlamış olması ciddi bir literatür boşluğudur. Banach yoğunluğu sıfır **tek başına** ne `κ≥κ₀` ne `κ>2.784` demektir.

[Michael John Curry, *An Explicit Windowed Sparsity Bound …*, Zenodo **sürüm** DOI 10.5281/zenodo.22087163, **kavram** DOI 10.5281/zenodo.22087162](https://zenodo.org/records/22087163) PDF'si açılıp Teorem 2.3 ve Korolar 4.3 okundu. Alıntı: “**No divergent orbit satisfies g_n ≤ B log2 n + K ... B < 1/β* = 1.0358567...**”. Burada `g_n=n log₂3−A_n=s_n+{n log₂3}`; dolayısıyla CP20'nin `s_n=κ log₂n+O(1)` varsayımına **κ<1.0358567600** için uygulanır. Bu metin *hakemli/doğrulanmış yayın değil, 2026 Zenodo ön baskı iddiasıdır*; PDF'deki parity-prefix/kaydırma ve iki-kollu sayım ile işaret ve nicelik sırasını kontrol ettim, tüm olası gizli matematik hatalarına karşı bağımsız hakemlik yapılmış gibi sunmuyorum. Garcia–Tal'ın (6)'sı Curry'nin karşılıklı toplam sonucunun tarihsel çekirdeğini zaten içerir; Curry'nin **açık** `β*=0.9653844417…` ve `1/β*` hesabını bununla özdeşleştirmiyorum.

**Kapsama hesabı:** `1.0358567600 < κ₀=1.0526808586 < 1.053 < 2.784`. Curry, T1'in `1.03585676≤κ<κ₀` parçasını, T6'nın **κ=1.053** simgesel kontrolcü dışlamasını ve T7'nin **1<κ≤2.784** sıfır-kritik tam-log bandının büyük çoğunluğunu **kapsamaz**. T1'in genel düşük-pencere önermesi Curry'nin tam-log öncülünü gerektirmez; örtüşen alt durumda Curry bağımsız ek kısıt verir. T7 ise yalnız **tek pozitif yörünge + her konumda a≠g + tam logaritmik yasa** altında konuşur. Hiçbiri genel ıraksak yörüngeleri, döngüleri veya Collatz'ı dışlamaz.

## NEW-CANDIDATE — güçlüden zayıfa

1. **T7-05:** Sıfır-kritik tam-log yörünge için, önceden `B` bildirmeden `κ≥α/h∞>2.784` ve `1<κ≤2.784` dışlaması. Garcia–Tal'ın değer penceresi ve Curry'nin 1.0358567 eşiği daha zayıftır; `B=∞`, gerçekten sınırsız-a yörüngesi **değildir**.
2. **T7-04:** Ayrıca `a≤3` iken `κ>3.027` (`h₃<0.523467`); programın kendi eski `κ≥α` sınırından güçlü.
3. **T7-02:** Her sonlu `B≥3` için tam özelleştirilmiş ağırlıklı basınç oranı `limsup log₂p_a(r)/r≤h_B`, sonuç `κ≥α/h_B`. Chernoff tekniği standart, bu koşullu dil/sabit birleşiminin yayın eşdeğeri saptanmadı.
4. **T6-04:** Pozitif tam-log yörüngede tekrarlanan valuation faktörlerini ayırıp `liminf log₂p_a(r)/r≥α/κ`. [Wang, arXiv:1809.02278](https://arxiv.org/abs/1809.02278) özetinde “**limsup b_n/n > log₂3**” rejimini dışlar; CP20 `A_n/n→log₂3` rejimindedir. Wang'ın 4.13 önek-tekerrür özel hali, denetim raporunda karşılaştırılmıştır; rastgele konumlu faktör ve üstel alt sınır ile eşdeğer değildir.
5. **T6-06:** `κ=1.053` için kanıtlanmış `p_a(r)≤43(r+1)²` bulunan özel kontrolcü, T6-04 alt sınırıyla **her κ>1** pozitif tam-log realizasyonuna aykırı. T1/T2'deki sonlu veya simgesel kontrolcü “Collatz karşıörneği” değildir.
6. **T1-05:** `κ<μ/h(μ)` koşullu yüksek-durum / negatif-gezi ikilemi, `N^{κh(μ)/μ+o(1)}` istisna sayısıyla. Tekil bütün-yörünge seyrekliğinin aynısı değil.
7. **T1-03:** İstenildiği gibi seçilen düşük-`A` kuantil altkümesinin `N^{max(ch(μ),κ−cη(μ))+o(1)}` sayımı; Terras/Everett tipik başlangıç ve Tao/Inselmann “almost all” sonuçlarıyla nesne/nicelik sırası farklı.
8. **T4-03:** Sınırlı-a küçük-3-adik-bitiş ağacının ileriye doğru sıfır-sheet dalına indirgenmesi; `Amax=3` için gerekli `0.5283208336k−O(log k)` sonek. Bir bitiş/yokluk teoremi değil; diğer T4 dosyaları mevcut değil.
9. **T1-06:** `κ>1` için sıfır-kritik 20-bloklu **simgesel** çizelge. Sonucun özgün unsuru yapılandırma; ne Curry'ye ne de tek-tamsayı pozitif yörüngesine karşıörnektir.

Bu dokuz aday için yalnız yöntem sorgusu yapılmadı: ledger'da her biri için **en az üç** “Banach density / windowed count / stopping time distribution”, “parity vector / residue class / 2^m−3^k / inverse tree density”, “valuation factor complexity / Sturmian / E-sequence”, “3-adic endpoint / cycle length” gibi **nesne sorguları** kayıtlıdır. arXiv API, OpenAlex, Crossref ve Zenodo kullanıldı; Semantic Scholar birçok sorguda **429 Too Many Requests** verdi, bunları pozitif eşdeğer bulunamadı kanıtı olarak kullanmadım. Lagarias'ın [1963–1999](https://arxiv.org/abs/math/0309224) ve [2000–2009](https://arxiv.org/abs/math/0608208) açıklamalı bibliyografyalarının **özetleri** açıldı, tam bibliyografya tarandığı iddia edilmiyor. [Tao 1909.03562](https://arxiv.org/abs/1909.03562) özetindeki “**almost all ... logarithmic density**” ve [Inselmann 2402.03276](https://arxiv.org/abs/2402.03276) özetindeki “**almost all ... natural density**” belirlenmiş tek pozitif yörüngeyi kapsamaz.

## KNOWN / SUPERSEDED ve yakınlık

- **KNOWN: 0** *ayrı CP20 nicel iddiası*: 1999'da bilinen Garcia–Tal sonucu, bu programın özgül h∞, h₃ veya faktör-entropi ifadesiyle **özdeş** değildir. Bilinen eski literatür sonucunu CP20 iddiası gibi ekleyerek yapay KNOWN sayısı artırmadım.
- **SUPERSEDED: T6-05** `p_a(r)≤(r+1)(B−1)^r` ve `B=3⇒κ≥α`: **aynı arşivin** sonradan dondurulmuş T6 güçlendirmesi/T7 V3, `h_B` ile bunu aşar (B=3: `κ>3.027`). Bu bir *dış yayın önceliği* demek değildir.
- **SUPERSEDED: T7-03** ilk `B=4` formu `κ≥2.820716194924186...`: **aynı arşivin** sonradan gelen `B≥3` V3 formunun **B=4 özel hali**. Burada `2.784` üniform sonucu tek başına `2.8207` özel eşiği kapsamaz; kapsayan sonlu-B formülüdür.
- **PARTIAL (T1-01, T3-02, T5-02, T6-01, T6-02):** eski affine silindir/CRT, basit geri-kazanım, sıfır-sheet kongruansı ve tekrar eden önek cebiriyle temas var; özgül altküme/tekrarlanan keyfi faktör biçimleri doğrudan yayın teoremi olarak **doğrulanmadı**. Özellikle Garcia–Tal (6) ve Curry'de `Σ1/n_k<∞` bilinmesi, T6 `n_k=O(k^κ)` için gerekli carry kontrolünü artık yeni bir genel ıraksaklık keşfi yapmaz. `STANDARD` olan 13 basit sayım/bölünebilme/teleskoplama iddiasına özel yayın isnat edilmedi.

## Yanlış “yeni” ifadesi, overclaim ve tamirler

- **T1 audit:** `κ₀=μ/h(μ)` hesabı CP19 Task 4 içinde zaten vardı; CP20'ye ilk kez ait denemez. İlk “her κ>1 için LEVEL-3 survivor” ifadesi **yanlış**, son audit bunu yalnız LEVEL-2 olarak düzeltti. `1.053` controller için T6/T7 sonradan daha güçlü engel kurar. Başka yerde Collatz ispatı bulundu iddiası **görülmedi**.
- **T6 V2:** “her ε>0” yerine `0<ε<α/κ` gerekir; V3 onardı. **T7 taslak:** Chernoff'da `N(S)t^(−S)≤P(t)` değil, `N(S)t^S≤P(t)`; V3 onardı. **Denetim sayısalı:** `B=4,r=640,C_D=8` altı basamak `0.579436`, tarihi `0.579440` hatalı; h₄ eşiği değişmez.
- **T4 örnek indekslemesi:** `e_k=1,a_k=2+2·3^k` ancak uygun **pozitif başlangıç indeksinden** kanonik olabilir; `k=0` için `e₀∈[0,3⁰)` olduğundan `e₀=1` yazılamaz. Bu, sınırsız-a küçük-endpoint karşıörneğinin kuyruğunu bozmaz. T2/T3 `[FAIL]` etiketleri **yöntem kaybı**dır, genel teorem çürütmesi değildir.
- **Önceki literatür haritası eksik:** Task6 literatür karşılaştırmasında Garcia–Tal 1999 ve 2026-08-24 Curry incelenmemiş; `NEW-CANDIDATE` etiketleri bu **şimdiki nesne taramasından sonra** bile geçici. Curry'nin kayıttaki “novelty” iddialarının bazı parçaları Garcia–Tal'ın nicel olmayan sabitli ama kuvvet tasarruflu (6) ispatından çıkar; yalnız Banach-density-0 cümlesinden karşılıklı toplamın yakınsaklığı çıkmaz.

## Kapsam ve erişim sınırı

Okunan birincil arşiv: CP20 **Task 1–7** içindeki başlıca theorem/findings/audit/freeze metinleri, özellikle T1 sayım ve audit; T2 ara-yol; T3 bulgular; T4 tek kalmış `FINDINGS.docx.txt`; T5 sıfır-sheet; T6 T7 altında kopyalanan **kanonik V3**; T7 kanonik basınç V3 ve rigorous-proof taslağı. `arch-era-d1.log` özetini **bulgu değil dizin** olarak kullandım. Ayrıca belirtilen bağımsız T6/T7 raporları ve `06-task6-guclendirme` sayısal düzeltmesi okundu. Dış kaynakta Garcia–Tal ve Curry **PDF**, Wang/Tao/Inselmann/Lagarias **arXiv API özetleri**, De Jesús'un Zenodo **kayıt özeti** açıldı; açılmayan hiçbir makaleye tam-metin kanıtı isnat edilmedi. T4'ün bildirilen **13 eksik çıktısı**, paket ZIP'leri, bütün ham CSV'ler/kodlar ve Task 8/Module E kapsam dışıydı; 193 arşiv dosyasının tamamı tarafımdan tek tek okunmuş gibi bir iddia yok. Kapsam bu yüzden **makul ama eksiksiz öncelik sertifikası değil**. Arşiv altına yazılmadı.

NOVELTY_SCAN_E3_CP20_T1_7_20260923_COMPLETE
