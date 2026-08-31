# Matematiksel Araştırmalar

Bu bir ders defteri değil, bir **araştırma defteri**.

## Nasıl çalışıyoruz

Burada formül ezberlemiyoruz. Şunu yapıyoruz:

1. **Bir soru buluyoruz** — kuralı bir cümlede anlatılabilen, ama cevabı belli olmayan.
2. **Deniyoruz** — bilgisayara binlerce, milyonlarca örnek hesaplatıyoruz.
3. **Bakıyoruz** — sayılarda bir örüntü, bir tuhaflık var mı?
4. **Yazıyoruz** — ne gördüğümüzü, neyi hâlâ anlamadığımızı kaydediyoruz.

Gerçek matematikçiler de aşağı yukarı böyle çalışıyor. Fark şu ki
onlar dördüncü adımdan sonra bir de *ispat* yazmaya çalışıyor.
Biz oraya gelene kadar önce görmeyi öğreneceğiz.

## Kural

**Anlamadığın hiçbir şeyi geçme.** "Bu ne demek?" sorusu bu defterde
en değerli sorudur — çünkü bir şeyi gerçekten anlamadan onunla
araştırma yapılamaz. Aptalca soru yok.

## Araştırmalar

| # | Konu | Durum |
|---|------|-------|
| [01](01-collatz/) | Collatz sanısı — sayıların 1'e düşüşü | Giriş / açık soru |
| [02](02-cp20-task6-bagimsiz-dogrulama/) | CP20 Task 6 teorem adayı — sayısal doğrulama + literatür | Sayısal bileşenler ve novelty kontrol edildi |
| [03](03-cp17-zemin-kontrolu/) | CP17 zemin teoremi — carry özdeşlikleri ve K17 sabiti | Dışarıdan doğrulanabilir iddialar tutuyor |
| [04](04-cp20-task6-denetim/) | CP20 Task 6 — bağımsız zero-trust denetim | `PROOF VALID WITH WORDING REPAIR` |
| [05](05-cp20-task7-denetim/) | CP20 Task 7 — B=4 basınç teoremi denetimi | `PROOF VALID WITH WORDING REPAIR` (kapsam) |
| [06](06-task6-guclendirme/) | Task 6'nın B=3 sonucunun güçlendirilmesi | Denetlenmemiş aday: κ ≥ 1,585 → κ ≥ 3,028 |
| [07](07-geriye-donuk-tarama/) | Geriye dönük tarama — eski sonuçlara yeni yöntem | Frontier κ ≥ 1,053 → κ ≥ 2,784; seyrek-kritik genişletme (taslak) |
| [08](08-literatur-taramasi/) | Detaylı literatür taraması — birincil kaynaklardan | Eşdeğer teorem bulunamadı |
| [09](09-literaturden-baglantilar/) | Literatürden saldırı fikirleri — açık cepheye araç taşıma | 5 bağlantı, öncelikli: Hensel basamak yoğunluğu |
| [11](11-surekli-kesir-denetim/) | Sürekli kesir bulgusunun kendi denetimi | `[VALID AS OBSERVATION — ONE LEMMA MISSING]` |
| [12](12-d0-denetim/) | CP20 Task 8B2 D0 bağımsız denetimi | `[PROOF VALID WITH WORDING REPAIR]` |
| [13](13-d1-denetim/) | CP20 Task 8B2 D1 bağımsız denetimi | `[PROOF VALID WITH WORDING REPAIR]` + Bulgu D |

## Güncel durum

**[DURUM.md](DURUM.md)** — Drive'da dondurulan teoremler, bu reponun
katkısı, ve bağımsız denetimin bende düzelttiği üç hata.

## İki katman

Bu defterde iki farklı seviye var ve karışmamaları önemli:

- **01** — sıfırdan giriş. Collatz nedir, neden zor, elle takip edilebilir örnekler.
- **02** — Google Drive'daki CP01–CP20 araştırma arşivinin aktif cephesine
  yapılan bağımsız kontrol. Bu seviye teknik ve arşivin kendi
  denetim disiplinine tabi.

CP20 Task 6 denetimi tamamlandı (04): ana teorem geçerli, controller'ın
sınırlı-takip lemmasında bir ifade onarımı gerekiyor.

## Deneyleri çalıştırmak

```bash
python3 01-collatz/deney.py
```

Ek bir program kurmanız gerekmiyor, sadece Python yeterli.
