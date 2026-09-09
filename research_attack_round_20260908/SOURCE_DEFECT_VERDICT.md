# Merkezlenmiş kaynak kusuru: önceden sabit grid ve kapsam saldırısı

8 Eylül 2026. Tam tamsayı/rasyonel hesap; yeni büyük tarama yok.

## Önceden istenen grid

r=5..12, A=floor(log2(3)*r)+d, d=-1,0,1; m=ceil(1.2r); yalnız t=A-m>=1. Toplam22 geçerli panel; r5,A6 ve r6,A8 t=0 olduğundan atlandı. alpha tabanı bit_length(3**r)-1 ile, m ise (6r+4)//5 ile tam hesaplandı.

Her gerçek tek h<2^m için m shortcut adımı doğrudan yürütüldü; P_k(z) tam çoklukları korundu. e_k=sum_z P_k(z)^2-N_k^2/q, N_k=binom(m-1,k-1). Aynı grid üzerinde

    Dsrc=sum_k e_k pj(1-pj),
    D2=sum_k e_k pj^2

hesaplandı. Her satırda önek toplamları binom katsayılarıyla tam eşleşti; D2<=Dsrc kontrolü geçti. t>=1 iken pj<=1/2 olduğundan bu son eşitsizlik ayrıca cebirsel olarak geçerlidir.

Literal Dsrc<=B için İHLAL YOK. En büyük oran r5,A7,m6,t1'de Dsrc/B=37/60; Dsrc=37/8, B=15/2. Bütün panel ve katmanlar SOURCE_DEFECT_PROBE.json içinde. Kaynak source_defect_probe.py. Küçük gridin geçmesi asimptotik, eventual veya bütün kritik bantlarda uniform bir teorem değildir.

## Açık ölçek uyarısı: bütün parametrelerde Dsrc<=B yanlış olabilir

Kritik m≈1.2r ölçeğini terk edip m=11 sabit, t→∞ ve r=floor(t/2) seçelim. Sabit m için q sonunda bütün gerçek H^m(h) uç noktalarından büyüktür. Artık tam uç nokta çokluklarını P_k(y) yazabiliriz.

Gerçek iki başlangıç145 ve147,11 shortcut adımında aynı161 ucuna gider ve ikisinin de parite ağırlığı7'dir. Tek-sayı adımları:

    145,109,41,31,47,71,107,161   valuations(2,3,2,1,1,1,1)
    147,221,83,125,47,71,107,161  valuations(1,3,1,3,1,1,1).

Bu yüzden C=sum_(k,y)P_k(y)^2 > sum_(k,y)P_k(y)=1024; en az C>=1026.

p0=binom(t,r)/2^t olsun. Her sabit k için pj/p0=binom(t,r-k)/binom(t,r)→1; p0→0. Vandermonde ile B=sum_k N_k pj ve B/p0→1024. Ayrıca e_k→sum_y P_k(y)^2. Sonuç:

    Dsrc/B → C/1024 >1.

Dolayısıyla bu farklı ölçek ailesinde yeterince büyük t için literal Dsrc<=B başarısızdır. Bu kritik bant ve m≈1.2r hipotezine karşıörnek değildir; hipotezin bütün parametrelere genişletilmemesi gerektiğini gösterir.

D2 bu karşıailede farklı davranır: D2/B≈p0*C/1024→0. Dolayısıyla bu saldırı D2<=B'yi çürütmez ve D2'nin Dsrc'den daha az gereksiz bilgi kaybedebildiğini gösterir.

## Kanıt hedefi olarak anlamı

V<=KqDsrc veya daha güçlü V<=KqD2 aktarımı ve K=O(r) kabul edildiğinde, kritik ölçekte D<=2^o(r)B köken kayıp terimine tau+gamma0/2 üssünü verir. gamma0>=2tau olduğunda bu ideal gamma0'dan büyük değildir. b1.2 için koşul sağlanır. Bu yeterli çıkarım, Dsrc veya D2'nin gerçek büyüyen kritik panellerde sınırlandığı anlamına gelmez. Bu görev yalnız literal küçük-grid hipotezini sınadı ve koşulsuz genişletmeye engel gösterdi.
