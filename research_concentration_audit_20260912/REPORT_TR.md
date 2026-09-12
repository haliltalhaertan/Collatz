# Sunulan kaynak yoğunlaşması iddiasının denetimi

12 Eylül 2026. Bu bir öneri denetimidir. Mevcut r=5..20 verileri kullanıldı; yeni büyük panel veya ücretli çağrı yapılmadı. Önceki W, D2 ve Collatz açık durumu değişmedi.

## Kabul edilen kısım ve daha güçlü eşitsizlik

Bir iletkendeki h frekansta x_a=|P_hat(a)|^2/sum|P_hat|^2 ve y_a=|F_hat(a)|^2/sum|F_hat|^2 olsun. Sıfır toplamlı katmanlarda bu oranlar tanımsızdır ve varyans katkısı sıfırdır. Diğerlerinde sum x=sum y=1, A=h sum xy, C_X=h sum x^2 ve C_Y=h sum y^2.

Sunulan |A-1|<=sqrt(C_X(C_Y-1)) doğrudur. Her iki dağılımı da merkezleyince daha güçlü biçim elde edilir:

    A-1 = h sum_a (x_a-1/h)(y_a-1/h)
    |A-1| <= sqrt((C_X-1)(C_Y-1)).

İspat Cauchy–Schwarz ve sum(x-1/h)^2=(C_X-1)/h özdeşliğidir. Bu standart sonlu vektör eşitsizliği, yeni Collatz kontrolü değildir. Düzlüğün iki taraflı sapmasını ve aralarındaki korelasyonu ayırdığı için yararlı bir tanıdır. C_X veya C_Y tek başına A'yı belirlemez.

## Gerçek ihlal katmanının yeniden hesabı

r=12,m=15,t=s=4,k=10,j=2 için gerçek kaynak histogramı check_claim.py içinde verilmiştir. Tamsayı otokorelasyonlarından primitive ikinci/dördüncü momentleri tam hesapladık:

- Kaynak: sum|P_hat|^2=10352, sum|P_hat|^4=35956960, C_X=1123655/418609=2,684259057975...
- Filtre: sum|F_hat|^2=48, sum|F_hat|^4=432, C_Y=3/2.
- A=1,902112313241...; |A-1|=0,902112313241...
- Sunulan üst sınır yaklaşık1,15850; merkezlenmiş üst sınır yaklaşık0,917676.
- {3,13} çiftinin kaynak enerjisi payı %81,03946; filtre enerjisi payı %55,37213. Bu yüzdeler FFT tanılarıdır.

Dolayısıyla önerideki yaklaşık2,67 yerine gerçek histogramdan2,684259 çıkıyor. %81 kaynak yoğunlaşması doğrudur. Ancak bunun tamamını yalnız kaynağa bağlamak doğru değildir: filtre de aynı çifte düz dağılımın %25'i yerine %55,37 pay verir. Merkezlenmiş kaynak–filtre korelasyonu yaklaşık0,983'tür. Yoğunlaşmaların aynı yerde olması belirleyicidir. Sadece varyansın çift payı ve filtrenin çift payı, A bilinmeden kaynak payını tekil biçimde belirlemez; burada doğrudan kaynak verisiyle doğruladık.

## Aşırı sonuçlar ve eksik varsayımlar

1. C_Y/h'nin küçülmesi uniform C_Y sınırı değildir. Sunulan tablodaki C_Y=136, düz dağılımın dördüncü-moment ölçütünde136 katıdır; yaklaşık h/136 etkin frekansa karşılık gelir. En büyük tek frekans payının küçülmesi, Fourier enerjisinin uniform dağıldığı anlamına gelmez. Tablo tüm (t,j) seçimlerini ve yeniden üretim kodunu vermediğinden büyük-s sayıları bu denetimde doğrulanmış sayılmaz. Kendi tablosundaki s=6 değeri0,51 de 's<=6 için yarımın altında' cümlesiyle çelişir.

2. 'Hiçbir iletkende sıfır çarpan yok' genellemesi yanlıştır. kernel.md/attack.md'deki tam sınıflamaya göre s=1, t çift, j=t/2 için çarpan sıfırdır; t=4,j=2 somut örnektir. s>=2 ve0<=j<=t için sıfır olmaması zaten kanıtlıdır. Sıfır olmamak uniform alt sınır değildir.

3. C_X filtre t,j'den bağımsız bir kaynak niceliğidir, fakat m,k,s'ye bağlıdır. İlgili büyüyen kaynak ailelerinin tamamında kontrol gerekir. Ayrıca C_Y-1 büyüyorsa tek başına sabit C_X bile uniform A vermez. W_flat'in gerekli ölçeği de ayrıca açık kalır.

4. Bir binom-parite kaynak modeliyle uyuşmazlık yalnız o modeli çürütür. Bundan bütün kombinatoryal açıklamaların elendiği veya yeni aritmetik mekanizmanın belirlendiği çıkmaz.

5. Primitive dördüncü moment, tam frekanslı ham histogram toplamsal enerjisiyle özdeş değildir. Q_s(u)=(P_s(u)-P_s(u+2^(s-1)))/2 primitive projeksiyonudur. Q'nun Fourier dönüşümü odd frekanslarda P_hat, even frekanslarda sıfırdır; Q genelde işaretlidir. Parseval, primitive dördüncü momenti Q'nun ağırlıklı otokorelasyon enerjisine bağlar. Bu, toplamsal kombinatorik için somut bir nesnedir; pozitif küme enerjisi veya Gowers eşdağılım teoremlerinin doğrudan uygulanabileceği ayrıca gösterilmelidir.

6. 3^k dilatasyonu frekansları zaten yeniden indeksler ve C_X'i değiştirmez. Yeni bir izleme testi, bu bilinen koordinat permütasyonunu farklı k kaynakları arasındaki yeni bir ilişkiden ayırmalıdır. Düzenli desen tek başına türetilebilirlik, düzensiz desen yapısızlık kanıtı değildir.

## Mevcut bütün panellerde C_X ölçümü

Her pozitif kaynak/filtre enerjili (k,s) katmanında merkezlenmiş eşitsizlik sayısal toleransla sağlandı. Maksimumlar:

| r | En büyük C_X | (k,s) | Merkezlenmiş eşitsizlikten toplam üst sınır / gerçek W |
|---|---:|---|---:|
| 12 | 2,7511 | (8,4) | 1,1143 |
| 18 | 3,2079 | (16,6) | 1,7124 |
| 19 | 6,7426 | (18,6) | 2,5384 |
| 20 | 9,5554 | (18,7) | 2,3192 |

r20'de en büyük C_X'in bulunduğu katmanda A yalnız0,81776: büyük kaynak yoğunlaşması tek başına büyük hizalanma demek değildir. Bu sonlu büyüme uniform sabiti çürütmez; küçük bir sabitin zaten elde olduğu yorumunu da desteklemez. Önceki dört-çift ayırma üst sınırı r20'de W'nin yaklaşık1,6036 katıydı; yeni merkezlenmiş moment üst sınırı2,3192 katıyla bu panelde daha gevşektir. Momentler yine de ispat açısından ayrı çalışılabilen bir hedef verebilir.

## Araştırma kararı

Kaynak dördüncü-moment ölçümünü ve merkezlenmiş eşitsizliği yararlı ek tanı olarak kabul ediyoruz. 'Filtre sorunu çözüldü, iş yalnız C_X'e kaldı' sonucunu kabul etmiyoruz. Uygun devam, toplam W_flat ağırlıklarıyla (C_X-1)(C_Y-1) katkısını incelemek ve bunu gerçek ortak yoğunlaşma / önceki tepe ayırma sınırıyla karşılaştırmaktır. İhtiyaç duyulan uniform aritmetik tahmin hâlâ açıktır.

Kaynaklar: research_visible_defect_20260908/kernel.md ve attack.md; research_peak_peeling_20260912/RESULTS.json ve ANALYTIC_REVIEW.md. check_claim.py ve RESULTS.json yeniden üretim kaydıdır. Bu ek denetim, önceki araştırma sonucunu veya tarihsel kapalı yürütme izinlerini değiştirmez.
