# 01 — Collatz Sanısı

## Kural

Bir sayı tut. Herhangi bir sayı. Sonra şunu tekrarla:

- Sayı **çiftse** → ikiye böl
- Sayı **tekse** → üçle çarp, bir ekle

Bu kadar. Tamamı bu.

## Deneyelim: 6 ile başlayalım

```
6 → çift → 3
3 → tek  → 10
10 → çift → 5
5 → tek  → 16
16 → çift → 8
8 → çift → 4
4 → çift → 2
2 → çift → 1
```

8 adımda 1'e indi. (1'e inince duruyoruz, çünkü 1'den sonra
1 → 4 → 2 → 1 → 4 → 2 → 1... diye sonsuza kadar dönüp duruyor.)

## Soru

**Her sayı eninde sonunda 1'e iner mi?**

Bu soru 1937'den beri ortada. Dünyanın en iyi matematikçileri
uğraştı. **Cevabı hâlâ bilinmiyor.** Kimse ispatlayamadı, kimse
ters bir örnek de bulamadı.

Ünlü matematikçi Paul Erdős bu problem için şöyle demiş:
*"Matematik henüz böyle problemler için hazır değil."*

## Deneyimiz

`deney.py` — 1'den 1.000.000'a kadar her sayıyı tek tek denedi.
Yaklaşık 4 saniye sürdü.

### Sonuç 1: İstisna yok

Bir milyon sayının **hepsi** 1'e indi. Tek bir tanesi bile
kaçamadı, sonsuza gitmedi, başka bir döngüye takılmadı.

> Bu bir ispat **değil**. Bir milyon sayı denemek, "bütün sayılar
> böyle" demek için yeterli değil — çünkü sayılar sonsuz.
> Bu ayrım araştırmanın kalbi: *kanıt* ile *ispat* aynı şey değil.

### Sonuç 2: Yolculuk süreleri çılgınca değişiyor

| Sayı | Kaç adımda 1'e iner |
|------|---------------------|
| 26 | 10 adım |
| **27** | **111 adım** |
| Ortalama (1 milyon sayının) | ~131 adım |
| 837.799 (rekortmen) | 524 adım |

**Buradaki tuhaflık:** 26 ve 27 yan yana iki sayı. Neredeyse aynılar.
Ama biri 10 adımda bitiyor, öbürü 111 adım sürüyor — 11 katı.

Yani bir sayının "ne kadar süreceğini" ona bakarak tahmin etmenin
bilinen bir yolu yok. Küçük sayı hızlı biter diye bir kural yok.

### Sonuç 3: Yukarı çıkıyorlar

Kural "aşağı in" demiyor. Tek sayılarda `3n+1` yapıyoruz — bu
sayıyı büyütüyor. Ne kadar büyütebiliyor?

- **27** → yola çıkarken 27, ama zirvede **9.232**'ye tırmanıyor
- **77.671** → zirvede **1.570.824.736**'ya çıkıyor
  (başladığı yerin **20.224 katı**)

Sonra yine de 1'e düşüyorlar. Her seferinde.

## Neden bu kadar zor?

Sezgi şunu söylüyor: rastgele bir sayı %50 ihtimalle çift.
Çiftse ikiye bölünüyor (yarıya iniyor), tekse üçle çarpılıp
1 ekleniyor (üçe katlanıyor) — ama sonuç mutlaka çift olduğu için
hemen ardından ikiye bölünüyor.

Yani uzun vadede sayı ortalama olarak her adımda `3/4` katına
iniyor gibi. Küçülme eğilimi var.

**Ama** bu bir *eğilim*, garanti değil. Tek bir sayının kaçıp
sonsuza gitmediğini, ya da 1'e uğramayan başka bir döngüye
takılmadığını hiçbir "eğilim" ispatlamıyor.

Bugüne kadar bilgisayarlarla ~2⁶⁸ (yaklaşık 300 milyar milyar)
sayıya kadar kontrol edildi. Hepsi 1'e indi. Yine de ispat yok.

## Hâlâ bilmediklerimiz — bizim sıradaki sorularımız

1. 27 neden bu kadar uzun sürüyor? Onun gibi "inatçı" sayıların
   ortak bir özelliği var mı?
2. Rekortmenler (524 adımlık 837.799 gibi) bir örüntü izliyor mu?
3. Kuralı değiştirsek ne olur? `3n+1` yerine `5n+1` desek?
   *(Bu soru özellikle ilginç — cevabı sürprizli.)*

## Bu araştırmadan ne öğrendik

- Bir problemin **kuralının basit olması**, cevabının kolay
  olduğu anlamına gelmiyor.
- Bilgisayar milyonlarca örnek verebilir, ama "hepsi" diyemez.
- Matematikte en değerli şey cevap değil, **doğru soru**.
