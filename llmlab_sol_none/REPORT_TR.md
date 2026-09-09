# GPT-5.6 Sol none: tek çağrılık deneme

8 Eylül 2026. Aynı dört araştırma girdisi ve Astra low ile aynı bilimsel rol/amaç; model kimliği, çalışma kimliği ve ayarları farklı. Süre kesicisi yok, 8000 çıkış tokenı, 0,13 dolar bütçe tavanı ve sağlayıcı fiyat filtresi. Tek çağrı, sıfır tekrar.

COMPLETED: 14,5988 saniye. 4694 giriş, 828 çıkış, 0 düşünme tokenı. Sağlayıcı ücreti 0,0200135 dolar. Bilimsel durum COMPLETED_WITH_OPEN_CLAIMS.

Araştırmacı kontrolü:

1. Tek blok sayımı, uniform endpoint-koşullu zayıf bileşim yasası altında doğru; ek ilk-geçiş koşullarının bu yasayı koruduğu ayrıca gerekçelendirilmelidir.
2. Gerekli koşul doğru: E exp(-lambda N)<=C/R ise P(N<=n)<=C exp(lambda n)/R. Olay üzerinde exp(-lambda N)>=exp(-lambda n) kullanılarak doğrudan çıkar.
3. Önerilen P(N<=n)<=C_0 exp(lambda n/2)/R sınırı (n<=ceil(2 log R/lambda)) yeterlidir: exp(-lambda n) ile ağırlıklandırılan sonlu toplam geometrik bir seriyle O(1/R), eşik üstü katkı ise O(R^-2) olur. Ancak bu, asıl hedeften daha güçlüdür. Soyut mantıksal örnek: N=ceil(log R/lambda) deterministik olsun. Laplace hedefi sağlanır; n=N için önerilen sağ taraf O(R^-1/2) iken sol taraf 1'dir. Bu örnek koşulların mantıksal ilişkisini test eder; erişilebilir bir Collatz karşıörneği değildir. Yanıttaki 'daha dar' gerekçesi daha kolay bir alt problem elde edildiğini göstermez. Kullanılmayan a>0 sabiti de formülün düzenlenmediğini gösterir.

Yeni ispat veya gerçek erişilebilir karşıörnek yok. Astra low önceki çağrıda 41,7355 saniye ve 0,11543 dolar idi. Bu Sol çağrısı yaklaşık 2,86 kat daha hızlı ve 5,77 kat daha ucuz; tek örnek ve farklı düşünme ayarları genel model sıralaması değildir. Astra gerekli-yeterli ayrımını daha temiz kurmuştu.

Paket bütünlüğü ve ZIP CRC geçti, 26 dosya. SHA256 a479d6d77ecccee65dca7a73f3a326901c12200e7f05a9dd89a229c477235589. Paket kontrolü matematiksel doğruluk sertifikası değildir. low ayarı ayrıca çalıştırılmadı; yeni ücretli çağrı yok.
