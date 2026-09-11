"""
Collatz deneyi.

Kural (tamami bu):
  - Sayi ciftse: ikiye bol
  - Sayi tekse: uc ile carp, bir ekle
  - Sonuc 1 olana kadar tekrarla

Soru: her sayi eninde sonunda 1'e iner mi?
Kimse bilmiyor. Bu dosya, bilinmeyene bilgisayarla bakma denemesidir.

Bu surum 1 disinda bir donguyle karsilasirsa sessizce sonsuza girmek yerine
acik bir RuntimeError uretir.
"""

LIMIT = 1_000_000


def sonraki(n):
    return n // 2 if n % 2 == 0 else 3 * n + 1


def yolculuk(n):
    adim = 0
    zirve = n
    gorulen = set()
    while n != 1:
        if n in gorulen:
            raise RuntimeError(f"1 disinda dongu tespit edildi; tekrar eden deger: {n}")
        gorulen.add(n)
        n = sonraki(n)
        zirve = max(zirve, n)
        adim += 1
    return adim, zirve


def main():
    adim_hafiza = {1: 0}

    def adim_sayisi(n):
        yigin = []
        yigin_set = set()
        m = n
        while m not in adim_hafiza:
            if m in yigin_set:
                raise RuntimeError(f"1 disinda dongu tespit edildi; tekrar eden deger: {m}")
            yigin.append(m)
            yigin_set.add(m)
            m = sonraki(m)
        d = adim_hafiza[m]
        while yigin:
            d += 1
            adim_hafiza[yigin.pop()] = d
        return adim_hafiza[n]

    en_uzun = (0, 0)
    en_yuksek = (0, 0)
    toplam_adim = 0

    for n in range(1, LIMIT + 1):
        a = adim_sayisi(n)
        toplam_adim += a
        if a > en_uzun[0]:
            en_uzun = (a, n)

    for n in range(1, 100_001):
        _, z = yolculuk(n)
        if z > en_yuksek[0]:
            en_yuksek = (z, n)

    print(f"1'den {LIMIT:,}'e kadar TUM sayilar 1'e indi. Istisna yok.")
    print()
    print(f"En uzun yolculuk : {en_uzun[1]:,} sayisi -> {en_uzun[0]} adim")
    print(f"Ortalama yolculuk: {toplam_adim / LIMIT:.1f} adim")
    print()
    print(f"En yuksege cikan (ilk 100.000 icinde): {en_yuksek[1]:,}")
    print(f"  -> yukseldigi tepe: {en_yuksek[0]:,}")
    print(f"  -> yani basladigi yerin {en_yuksek[0] // en_yuksek[1]:,} kati kadar yukari cikti")
    print()

    a27, z27 = yolculuk(27)
    print(f"Ilginc olan: 27 gibi kucucuk bir sayi {a27} adim suruyor")
    print(f"  ve yol boyunca {z27:,}'e kadar tirmaniyor.")
    print(f"  Komsusu 26 ise sadece {yolculuk(26)[0]} adimda bitiyor.")


if __name__ == "__main__":
    main()
