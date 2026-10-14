# COLLATZ ARAŞTIRMA WORKFLOW — KONSORSİYUM (REV 4)

**Tarih:** 2026-09-23
**Durum:** Rev 3'ün yerine geçer. Yeni olanlar: konsorsiyum kararı, Unreal Agent, COLLAPSE kapısı, arka plan protokolü.
**Değişmez sınır:** Collatz açıktır. Hiçbir ajan çıktısı tek başına kanıt değildir. Sonlu hesap teorem değildir.

## 1. Temel ilke

Yön kararını tek bir ajan vermez; bu kural koordinatörü de kapsar. Kararı **konsorsiyum oyu ve exact test birlikte** verir.
Exact test oydan üstündür: exact olarak çürüyen bir öneri, aldığı oy ne olursa olsun elenir.

## 2. Üyeler ve roller (maliyet sırası)

| # | Üye | Rol | Kota |
|---|---|---|---|
| 1 | **ChatGPT Web** | Teorist; lemma üretimi, ispat eleştirisi, literatür | ChatGPT mesaj kotası |
| 2 | **Muse 1.3** (`xhigh`, salt-okunur) | Bağımsız teorist ve denetçi | Abonelik |
| 3 | **Unreal Agent** (`gpt-6-sol`) | Hesap üyesi; kod yazar ve çalıştırır, tarama ve karşıörnek arar | Codex kotası (ortak) |
| 4 | **Jev** | Ucuz ön-filtre; yalnız `ADVISORY` | Çok ucuz |
| 5 | **Opus** | Yalnız zorunlu son denetimde, gerekçesi yazılarak | Ücretli |
| — | **Hermes (koordinatör)** | Brifing, oy sayımı, exact yerel doğrulama, kayıt. Oyu diğer üyelerle eşit, veto hakkı yok. | — |
| — | **Kullanıcı** | İstediği zaman oy veren üye; sezgi ve yön | — |

“Alt ajan” denildiğinde varsayılan olarak ChatGPT Web kastedilir.

## 3. Checkpoint döngüsü

Sıra esnektir; gerekirse adımlar atlanabilir ya da tekrarlanabilir.

```text
[1] BEYİN FIRTINASI   Konsorsiyum Tur 1: her üye aynı brifingi alır ve birbirinden
                      bağımsız çalışır (≤3 yön + oy + "en büyük yöntem hatamız").
[2] LİTERATÜR         Hermes kaynakları kendisi doğrular; doğrulanamayan kaynak
                      "DOĞRULANMADI" etiketiyle ayrılır ve kullanılmaz.
[3] YENİ TEORİ        Tur 2: cevaplar anonimleştirilir ve çapraz eleştiriye açılır;
                      üyeler yeniden oy verir. Jev ADVISORY ön-eleme yapar.
[4] TEST              Kazanan yön için önce kill kriteri yazılır. Unreal Agent tarar;
                      Hermes aynı sonucu ayrı kodla exact olarak yeniden üretir.
[5] KANIT / ÇÜRÜTME   Kanıt girişimi (ChatGPT ve Muse) ile çürütme girişimi (Unreal)
                      ayrı yapılır; Muse ispatı satır satır denetler.
[6] KAPANIŞ           Rapor + kod + JSON + SHA-256 manifest; journal ve state;
                      commit/push; taze klon hash doğrulaması.
```

## 4. Kapılar (her fikir geçmek zorunda)

1. **COLLAPSE kapısı:** “\(D\mid B\) biliniyor olsa bile bu fikir yeni bir şey söylüyor mu?” Cevap hayırsa fikir reddedilir.
   Bu kapı fikir doğarken uygulanır; test yapıldıktan sonra değil.
2. **İşaret kapısı:** \(3n-1\) problemindeki gerçek döngüler — (1), (5,7), (17,25,37,55,41,61,91) — hiçbir teori tarafından dışlanmamalı.
3. **Ölçek kapısı:** Küçük rasyonel adaylarda elde edilen istatistik, büyük minimum rejimine (\(n_{\min}>2^{71}\)) genellenmez.
4. **Literatür kapısı:** Steiner, Simons–de Weger, Hercher ve Eliahou çizgisinde zaten yapılmış bir şey “yeni” diye sunulmaz.

## 5. Ajan protokolleri

- **Arka plan:** Uzun görevler `notify:true` ile çalışır. Hermes ön planda beklemez; sohbet URL’sini hemen kullanıcıya verir.
- **ChatGPT Web:** Her görev yeni bir `--agent` ile ve bir **rol işaretiyle** gönderilir. `poll_marker.py`, doğru rol ve doğru bitiş işaretini görmeden yanıtı kabul etmez. Chrome kapalıysa Hermes onu CDP ile yeniden açar.
- **Muse:** `--model muse-spark-1.3 --reasoning-effort xhigh --approval-mode never --disable-write --disable-web-tools`. Çağrı ve bekleme döngüsü tek bir `wsl` çağrısı içinde yapılır.
- **Unreal Agent:** `ua_run.sh <iş> <prompt>` → `ua-work/<iş>/final.txt`. Kodu ve SHA-256 değeri saklanır.
- **Bağımsızlık:** Tur 1 bitmeden hiçbir üyenin cevabı yorumlanmaz ve başka üyelere gösterilmez.

## 6. Etiketler

`[PROOF]` · `[EXACT COMPUTATION]` (sonlu) · `[CONJECTURE]` (falsifier ve kill kriteriyle) · `[HEURISTIC]` · `[ADVISORY]` (Jev veya tek ajan) · `KILL` / `PARK` / `CONDITIONAL` · `DOĞRULANMADI` (literatür)

## 7. Değişmez güvenlik kuralları

1. Üretici ile denetçi ayrı ajanlardır.
2. Ajanların verdiği sayılar yerel exact hesapla yeniden üretilmeden kabul edilmez.
3. Credential, token ve oturum sırları hiçbir rapora girmez.
4. Kullanıcıya düzenli ara durum raporu verilir; sonuçlar sade dille ve “ne kazandık / ne kaybettik” biçiminde sunulur.

## 8. Rev 3 → Rev 4 dersleri

- Tek ajanın önerisi karar gibi sunuldu → konsorsiyum oylaması getirildi.
- C1 ve carry-band rotalarına COLLAPSE kapısı geç uygulandı → kapı fikir doğarken uygulanacak.
- ChatGPT köprüsü yanlış veya eski yanıt topladı → rol ve bitiş işareti doğrulayan poller kullanılacak.
- Hesap işleri için Unreal Agent eklendi; CP26’da yerel tekrarla birebir uyum gösterdi.
