# İlerlemenin yeniden değerlendirilmesi ve on inceleme başlığı

8 Eylül 2026. Yerel araştırma notu; yeni kanonik aşama, yayın veya Collatz ispatı değildir.

## Katılımın gerçek kapsamı

Kullanıcı on ayrı ajan istedi. Yeni `review01_global` ajanı başarıyla açıldı. Sonraki yeni ajan açma ve eski ajanlara görev gönderme denemeleri `agent thread limit reached` hatası verdi. İlk yeni ajan tamamlandıktan sonra da yeni oturum açılamadı; onun kendi bağımsız alt ajan açma denemesi de aynı hatayla sonuçlandı. Mevcut yeni ajan aynı oturumda ek incelemeler yapabildi.

Dolayısıyla bu turda baş araştırmacı ve **bir yeni alt ajan** çalıştı. Aşağıdaki on başlık on ayrı ajan görüşü değildir. Eski raporlardaki ajan değerlendirmeleri tarihsel kaynak olarak okundu, yeni katılım sayılmadı. On bağımsız ajan isteği teknik olarak tamamlanamadı.

## Ortak zemin ve itiraz

Projenin kalıcı varlıkları koşullu teoremler, tam aritmetik indirgemeler, karşı örnekler ve daha hızlı tam sayım algoritmasıdır. Son turlarda yeni bir yörünge sınıfı dışlanmadı. Global kritik-log sınıfını dışlayan koşullu köprü bütün olası kaçışları veya döngüleri kapsamıyor.

İlk bağımsız değerlendirme bir sonraki turda geniş bir çift ailesinde üstel kazanç yoksa varyans hattını duraklatmayı önerdi. Baş araştırmacı iki itiraz yöneltti: bir turda tam üstel kazanç istemek ara yapısal kazanımları haksız yere dışlayabilir; pozitif çift katkılarını ayrı sınırlamak önemli işaretli iptalleri kaybedebilir. Aşağıdaki tam hesap ikinci itirazı somutlaştırdı. Varyans ancak yeterli bir yol; yalnız köken aralığına gereken sayımı tüm ötelemelere taşıdığı için zorunlu araştırma hedefi değil.

## On başlıkta karar haritası

|Başlık|Değerlendirme|Somut karar veya açık|
|---|---|---|
|1. Genel ispat kapsamı|CP17 ve koşullu sayım köprüsü tüm Collatz sonucuyla aynı şey değil.|Döngü, genel kaçış ve özel kritik-log kapsamlarını ayrı tut.|
|2. Sayımdan yörüngeye geçiş|Yeni ajan mevcut ispatta hata bulmadı; uniform sabit kütle bandı şartını doğruladı.|Global yasa yerine seyrek uygun pencere koşulu kullanılabilir; aşağıdaki önerme.|
|3. Hesaplama başarısı|Modüler aritmetik-dizi DP gerçek bir algoritmik kazanım; katsayı üst sınırı değil.|Araçtan çıkan her büyük paneli yeni matematiksel ilerleme sayma.|
|4. Marjinal sayım çıkmazı|Yükseklik/offset/marjinal sınırların belirli mimarisinde eski kappa tavanı kanıtlı.|Aynı sınırın parametrelerini tekrar optimize etmeyi bırak.|
|5. Varyans hedefi|Nicel eşik yeterli; henüz actual-prefix korelasyon tahmini yok.|Özdeşliği ispat sanma; yeni yapısal girdiyi açık adlandır.|
|6. Birleşme ve çokluk|Aynı (k,z) grubundaki başlangıçların devam göstergeleri aynı; katkı çokluğun karesiyle büyür.|Tekil başlangıç bağımsızlığı yerine gruplu işaretli toplamı incele.|
|7. İptaller|Sonlu örneklerde büyük pozitif ve negatif katkılar birbirini götürüyor.|Mutlak değerle bütün kovaryansları toplamak varsayılan yol olmasın.|
|8. Köken ve ötelemeler|Köprü tek köken sayımını ister; tüm blok varyansı daha güçlü yeterli bilgi ister.|Varyansın zorlaşması asıl hedefin yanlışlığı sayılmasın; doğrudan sayım yolu açık kalsın.|
|9. Başka momentler|22. normalize merkezî moment için altüstel bir sınır da mevcut parametrelerde yeterli olur.|Bu yalnız alternatif koşullu hedef; 22'li bağımlılıkları kontrol ettiğimiz anlamına gelmez.|
|10. Araştırmayı yönetme|Yalnız yeni gösterim ve daha fazla sonlu satır, eksik tahmini çözmez.|Sonraki çalışma gerçek çift gruplarında iptali koruyan bir yapı, yeterli bir sertifika veya somut yöntem engeli üretmeli.|

## Yeni sınırlı hesap: küçük varyans bağımsızlığın kanıtı değil

Önceki notasyonda q=2^t, P_k(z) gerçek tek başlangıç öneklerinin çokluğudur. Her (k,z) grubu için

    I_(k,z)(a)=T_(r-k)(3^k a+z),  p_(k,z)=binom(t,r-k)/q,
    G(a)=sum_(k,z) P_k(z) I_(k,z)(a).

Yalnız geçerli 0<=r-k<=t grupları tutulur. Tam varyans ayrışımı:

    V = D_group + C_positive + C_negative,
    D_group = sum_(k,z) P_k(z)^2 p_(k,z)(1-p_(k,z)).

C_positive ve C_negative farklı (k,z) gruplarının işaretli kovaryanslarının sırasız çiftler üzerinde iki kat toplamıdır. (k,z) sınıfları aynı göstergeye sahip bütün grupları mutlaka birleştiren maksimal sınıflar değildir.

Önceden sabitlenen r=5,10,12,14 için kod, bütün gerçek önekleri ve bütün q ötelemeyi tam tamsayı hesabıyla kullandı. Önceki G dizileri yeniden elde edildi; toplam, ortalama ve kovaryans özdeşliği tam eşleşti.

|r|Grup içi katkı D_group|Pozitif gruplar arası katkı|Negatif gruplar arası katkı|Kalan V|
|---:|---:|---:|---:|---:|
|5|81/4|14|-22|49/4|
|10|27895/4|740027/32|-962573/32|307/16|
|12|28179333/128|169538581/128|-98756637/64|6395/4|
|14|650219507/512|6195685367/512|-1711269259/128|413919/256|

Örneğin r=14'te bütün katkıları payda512 ile yazınca

    V=(650219507+6195685367-6845077036)/512=827838/512.

Bu, yaklaşık 1.27 milyon grup içi katkı ve 12.10 milyon pozitif çapraz katkının yaklaşık -13.37 milyon negatif çapraz katkıyla iptal edilerek yaklaşık1616.87 varyans bıraktığı sonlu bir örnektir. İşaretleri atmak bu örnekte güçlü bilgi kaybıdır. Asimptotik iptal, optimal gruplama veya zorunlu genel alt sınır kanıtlanmadı. Sonuç gruplama seçimine bağlı teşhistir; bütün katkıların her ölçekte bu boyutlarda kalacağı iddia edilmez.

## Global yasa yerine uygun pencereler: koşullu köprü

Yeni ajanın önerisi, baş araştırmacının cebirsel kontrolü: tekrarsız bir pozitif tek-sayı yörüngesi olsun. Sabit 0<b<alpha ve kappa>0 için, sonsuz N_j boyunca

    r_j=ceil((kappa/b+delta)log_2 N_j)

seçilsin. delta>0 ve gamma<1/(kappa/b+delta) olsun. Her [N_j,2N_j] penceresinde en az cN_j başlangıç u için aynı anda

    n_(u+r_j)<=N_j^(kappa+epsilon_j), epsilon_j -> 0,
    |s_(u+r_j)-s_u|<=C

sağlansın; c>0 ve C sabit olsun. İlgili her sabit kritik kütle bandında uniform Q_(r,A)(b)<=2^((gamma+o(1))r) bu yörüngeyi dışlar.

Gerekçe: yükseklik koşulu uç noktayı 2^(br_j)<3^r_j altında tutar; slack farkı A_(u+r_j)-A_u=alpha r_j+O(1) verir. Gerçek uç nokta kanonik kalıntıya eşittir. Tekrarsızlık en az cN_j ayrı kelime verir; sabit sayıda kütle sınıfının üst sınırı bunları taşıyamaz. Global kritik-log yasası gerekmiyor, fakat bu pencere koşulunun her kaçan yörüngede zorunlu olduğu da kanıtlanmış değil. Bu nedenle genel Collatz sonucuna geçilmedi.

## Alternatif moment hedefi: yeterli, henüz kanıtlanmamış

M_p=q^(-1)sum_a |G(a)/B-1|^p tanımlansın. Her p>=1 için

    G(0)<=B[1+(q M_p)^(1/p)].

Bu, köken teriminin toplamdan büyük olamamasıdır. q=2^(tau r+o(r)) ve B=2^(gamma0 r+o(r)) olduğunda M_p<=2^o(r), köken üssünü en fazla gamma0+tau/p yapar. b=1.2, kappa=1.053 için

    gamma0≈1.120681387225,
    tau≈0.384962500721,
    gamma0+tau/22≈1.138179682712 < b/kappa≈1.139601139601.

Dolayısıyla 22. moment için normalize altüstel üst sınır yeterlidir. Bu, varyansın tek seçenek olmadığını gösterir. Ancak yüksek moment çoklu bağımlılıkları gerektirebilir; mevcut ikinci moment açığını çözmeden daha yüksek momente geçmenin kolay olduğu iddia edilmez. Yeni bir gerçekleşmiş üs kazanımı değil, beyin fırtınasında karşılaştırılabilir açık hipotezdir.

## Sonraki çalışma için öneri

Ana aday: gruplu devam göstergelerindeki iptallerin tam, işareti koruyan bir yapısını bulmak. Örneğin kabul vektörleri arasında tam tamamlayıcılık veya ağırlıklı örtme özdeşliği olup olmadığı sınanabilir. Bu soru henüz cevaplanmadı. Başarı yalnız yeni bir eşitlik yazmak değil; kontrol edilmemiş terimleri veya yeterli üst sınırın üssünü gerçekten azaltmaktır. Tek turda tam hedefi kapatmak zorunlu değil; yeni sınıflama daha önceki karşı örneği aşan kanıtlanmış bir ara kazanç üretmelidir.

Yan aday: uygun pencere koşulunu mevcut yörünge kısıtlarından türetmenin mümkün olup olmadığını sorgulamak. Bu hem kapsam açısından değerli hem de bağımsız bir zor problemdir. CP17 limsup bilgisi tek başına gerekli pozitif oranlı uygun blokları sağlamaz.

Bu tur ücretli OpenRouter çağrısı, Drive/GitHub yüklemesi veya kanonik dosya değişikliği yapılmadı. Kaynak kapsamı seçilmiş yerel proje raporları ve DP kodudur; bütün arşivin sıfırdan yeniden denetimi veya yeni literatür taraması değildir.

## Sonraki turun yorum düzeltmesi

research_attack_round_20260908/REPORT_TR.md'deki üç-alt-ajan denetimi ham milyonluk kovaryans iptalinin büyük kısmını tam sabit önek ortalamasının sıfır yönüyle açıkladı. Bu belgedeki sayılar doğrudur; ancak bunlardan derin çapraz-ağırlık iptalinin zorunlu ana mekanizma olduğu sonucu çıkarılmamalıdır. P_k-N_k/q merkezlemesi r14 grup diyagonalini yaklaşık1.27 milyondan1490'a indirir. Ağırlık sınıfları arasında Cauchy'nin O(r) kaybı üstel hedef için kabul edilebilir. Sonraki hedef gerçek merkezlenmiş önek histogramının ağırlıklı sapmasıdır; asimptotik üst sınırı hâlâ açıktır.
