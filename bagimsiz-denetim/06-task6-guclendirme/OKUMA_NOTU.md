# Bu klasör ne?

Task 7 denetiminde bulduğum şeyin yazılmış hali (Bulgu C).

## Kısaca ne oldu

Task 6, B=3 için şu üst sınırı kullanıyordu:

```
p_a(r) ≤ (r+1)·2^r
```

Bu sınır sadece **alfabe kısıtını** kullanıyor — "her konumda 2 seçenek var,
r konum var". Ama teoremin zaten varsaydığı ikinci bir kısıt daha var:
`s_k = κ log₂k + O(1)`, yani sapmanın çok yavaş büyümesi.

Task 6 o ikinci kısıtı **üst sınırda kullanmıyordu.** Task 7 ise kullandı
(büyük-sapma / Chernoff cezası olarak) ve çok daha keskin bir sınır elde etti
— ama sadece B=4 için, geriye dönüp B=3'e bakmadı.

Geriye dönüp baktım.

## Sonuç

| | Task 6'nın verdiği | Güçlendirilmiş |
|---|---|---|
| B=3 eşiği | κ ≥ 1,585 | **κ ≥ 3,028** |

Dışlanan aralık `1 < κ < 1,585`'ten `1 < κ < 3,028`'e genişliyor.

## Ve daha önemlisi

Kaba sınır `B ≥ 5` için **hiçbir işe yaramıyor**. Çünkü `log₂(B−1) ≥ 2 > α`
olduğunda eşik 1'in altına düşüyor — ama teorem zaten `κ > 1` varsayıyor.
Yani kaba sınır B≥5'te boş bir ifade. B=4'te de öyle (tam olarak κ ≥ 1).

Kaba sayım **yalnızca B=3'te** bilgi taşıyordu, orada da neredeyse yarısını
kaybediyordu.

Basınç sınırı ise her B için ~2,78 üstü bir eşik veriyor — sınırsız alfabe
dahil.

## Birleşik ifade

Üç checkpoint'in (Task 6 alt sınırı + Task 7 yöntemi + bu güçlendirme)
toplamı tek bir cümle:

> Zero-critical, kritik-logaritmik bir valuation kelimesine sahip pozitif
> ordinary Syracuse yörüngesi, **alfabe kısıtı ne olursa olsun**
> `1 < κ < 2,784` aralığında var olamaz.

## Durum

`[DENETLENMEMİŞ GÜÇLENDİRME ADAYI]`

Dondurmadan önce gerekenler belgenin §12'sinde. En önemlisi: `h_3` ve
`h_∞` sabitleri **rasyonel/aralık aritmetiğiyle** yeniden üretilmeli.
Benim hesabım 80 basamak kayan nokta — kanıt değil, kontrol.

## Dosyalar

- `CP20_TASK6_STRENGTHENED_COROLLARY.md` — arşiv formatında, İngilizce,
  doğrudan Drive'a konabilir
- `dogrulama.py` — kaba/basınç karşılaştırması ve B=3 yakınsama testi
