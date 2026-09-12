# MUSE CODE — BAĞIMSIZ KOD DENETİMİ (ROUND 1)

**Tarih:** 2026-09-10
**Denetçi:** Muse Code 1.1.1 (muse-spark-1.3), reviewer modu — salt-okunur
**Kapsam:** haliltalhaertan/Collatz çalışma kopyası (bagimsiz-denetim/, tools/) + GOREV001
**Salt-okunur kanıtı:** denetim öncesi/sonrası md5 karşılaştırması, 43/43 dosya birebir; __pycache__ bile oluşmadı.
**Doğrulama ortamı:** muse exec --prompt-file ... --trust-workspace --disable-write --disable-approval

## Doğrulayan not (Hermes, ikinci bağımsız kontrol)

Muse'un kritik bulgusu (Madde 7 serileştirme) ayrıca Hermes tarafından
`verify_madde07.py` ile birebir tekrarlandı:
- SHA256(ASCII digit-string) = 1639a9bfb801c79a86adc889e6631dbce7db7b07a8798e0542b4d50030c1ade1  (arşivle UYUŞMAZ)
- SHA256(ham bytes(a))      = 31d2db3d10ec0610f1c17fc86a6b485f6e8a378ed7696d5b41ad48e51980e1d2  (arşivle EŞLEŞİR)
- z aralığı [-2, 1] — iddia [-41, 1] içinde; yeniden kurulumun kendisi doğru.
Sonuç: raporun "EŞLEŞTİ" kararı doğru; dağıtılan script yanlış serileştirmeyi hash'liyor.
Düzeltme (tek satır): `hashlib.sha256(bytes(a))`.

**Karar: ŞARTLI GEÇERLİ.** Hiçbir bulgu ana matematik iddialarını çürütmedi.

---

# Bağımsız Kod Denetimi — Collatz Arşivi

## Özet karar: ŞARTLI GEÇERLİ

Matematiksel iddiaların tamamı bağımsız yeniden hesapla doğrulandı; incelenen kodda matematik hatası bulunamadı. Şartlar: (1) Madde 7 SHA tutarsızlığı giderilmeli, (2) iki script doğrudan çalışmıyor (`mpmath` yok), (3) GOREV001 `main` olduğu gibi çalışmıyor (`/mnt/data`), (4) basınç sabitleri hâlâ aralık aritmetiğiyle sertifikalanmalı (belgeler bunu zaten şart koşuyor, §12).

## Çalıştırma sonuçları vs beklenen

| Script | Beklenen | Gerçek | Sonuç |
|---|---|---|---|
| `deney.py` | 1M istisnasız; 524 adım | Aynı çıktı, exit 0 | GEÇTİ |
| `dogrulama.py` | h_3=0.523466681 | exit 1 (`mpmath` yok) | ÇALIŞMADI |
| `10_...periyotlari.py` | uyuşma 0.99+ | exit 1 (`mpmath` yok) | ÇALIŞMADI |
| GOREV001 panelleri | W kesirleri | Bit-bit aynı, assertler geçti | GEÇTİ |

`deney.py` gerçek çıktısı: 1–1.000.000 tamamı 1'e indi; en uzun 837.799 → 524 adım; ortalama 131,4; ilk 100.000'de zirve 77.671 → 1.570.824.736; 27 → 111 adım/9.232 zirve; 26 → 10 adım. Saf döngüyle bağımsız spot kontrol: `837799→(524, 2974984576)`, `77671→(231, 1570824736)`, `27→(111, 9232)`, `26→(10, 40)` — tamamı uyuşuyor.

Çalışmayan iki scriptin matematiği bağımsız yoldan (`scipy`+`Decimal`, `mpmath` yok, ağ yok) yeniden üretildi:

| B | h (hesap) | kappa (hesap) | Sonuç |
|---|---|---|---|
| 3 | 0.523466681 | 3.0278193 | Belgeyle aynı |
| 4 | 0.561900734 | 2.8207162 | Belgeyle aynı |
| 5,6,8,10 | 0.567913141…0.569308553 | 2.7908…2.7840 | Belgeyle aynı |
| ∞ | 0.569309013486 | 2.7840109030 | Belgeyle aynı |

DP yakınsama satırları da tuttu: B=3 r=1280 → 0.520476 / 0.532044 (belge §10 ile basamak-basamak aynı). Sürekli kesir: `cf=[1,1,1,2,2,3,1,5,2,23,…]`; q=53→0.9940, q=306→0.9971, q≥665→0.9999 — "büyük q'de 0.99+" doğrulandı.

| r | W | qD2 | Sonuç |
|---|---|---|---|
| 5 | 37/4 | 37/4 | Rapor+JSON ile aynı |
| 10 | 819/32 | 2915/32 | Rapor+JSON ile aynı |
| 12 | 2795/4 | 21195/8 | Rapor+JSON ile aynı |
| 14 | 274211/256 | 4612387/256 | Rapor+JSON ile aynı |

## Bulunan sorunlar

- **Orta** — `04-cp20-task6-denetim/madde07_controller_yeniden_kurulum.py:42-50` + `DENETIM_RAPORU.md:128-132`: script basamak-stringi hash'leyip `HAYIR` basıyor (yeniden çalıştırdım: hesaplanan `1639a9bf…` ≠ arşiv `31d2db3d…`); rapor ise `EŞLEŞTİ` diyor. Gerçek: üretilen dizi doğru — `bytes(a)` (ham byte) serileştirmesi arşiv hash'ini veriyor (denedim: `raw-bytes EŞLEŞTİ`, diğer 5 serileştirme yok). Yani script yanlış şeyi hash'liyor, raporun sonucu doğru ama dağıtılan scriptle tekrar üretilemiyor. `madde07b` zaten bu araştırmaydı. Düzeltme: script `hashlib.sha256(bytes(a))` kullanmalı.
- **Orta** — `drive-dl/GOREV001_independent_check.py:315,346`: `main()` çıktıyı sabit `/mnt/data/RESULTS.json` ve `/mnt/data/ACTUAL_OUTPUT.txt` yollarına yazıyor; bu dizin yoksa (bu ortam dahil) `FileNotFoundError` ile çöküyor. Panel fonksiyonlarının kendisi sorunsuz (import edip çalıştırdım, tüm iç `assert`ler geçti). Ayrıca `expected` sözlüğündeki (satır 291-296) değeler raporun kopyası olduğundan sondaki `assert` bloğu bağımsız ispat değil, regresyon kilidi — gerçek bağımsızlık içsel tam-aritmetik kontrollerden geliyor.
- **Orta** — `Collatz/tools/verify_handoff.py:99`: shallow clone'da `git cat-file -e <base_commit>^{commit}` başarısız olur → `HANDOFF VERIFICATION: FAIL`. Kod okumasıyla doğrulandı (çalıştırılmadı): `git_value` returncode≠0'da `AssertionError` yükseltiyor. Ek zayıflıklar: yalnızca nesne *varlığı* bakılıyor, `merge-base --is-ancestor` ile atalık kontrolü yok; detached HEAD'de `branch --show-current` boş döner → içerik doğru olsa da FAIL; ilk journal girdisini dış çapaya bağlayan sabitleme yok (zincir kendi içinde tutarlı). Olumlu: zip üye sayımı + alt-küme kontrolü birlikte tam-küme eşitliği veriyor; ekstra dosya kaçar notu geçersiz.
- **Uç** — `06-task6-guclendirme/dogrulama.py:18`: `findroot(diff(f), 1.4)` tek başlangıç, yakınsama/`f''>0` kontrolü yok (05/01'deki kontrol burada yok). Bu B aralığında sorun çıkarmıyor (scipy ile global minimizasyon aynı değerleri verdi), ama kırılgan.
- **Uç** — Güçlendirme belgesi §10: B=4 r=640 satırı `0,579440` yazıyor; iki ayrı hassasiyette (Decimal 60/120 basamak, g-kelimesi birebir aynı) sonuç `0.579436`. 5. basamağa kadar tutuyor; 6. basamak yazım/yuvarlama artefaktı.
- **Uç** — `01-collatz/deney.py`:显式 döngü tespiti yok; 1 dışındaki döngüde `while m not in adim_hafiza` sonsuza girerdi. Pratikte 1M tamamlandığı için sonuç geçerli; zirve taramasının yalnız ilk 100.000'de olduğu belgede açıkça yazıyor, tutarlı.
- **Uç** — `04-.../madde07b_sha_varyant_taramasi.py:19-20`: sınır-durum düzeltmesi yalnızca yukarı ayarlıyor; 150 basamakta risksiz ama tek yönlü.
- **Bilgi** — `bagimsiz-denetim` altında GOREV001 hesabını tekrarlayan dosya yok (aramada 0 eşleşme): kopya yok, bağımsızlık korunuyor; ama GOREV001 panellerinin arşiv-içi ikinci üretimi de yok.

## `verify_handoff.py` değerlendirmesi

Mantık: state/build JSON şema kontrolü → aktif aşama izin-listesi (11 aşama) → `active_integrator` kilit alanları + `cat-file` ile base commit varlığı → dal adı eşitliği → kayıtlı SHA256'larla dosya ve arşiv (boyut, üye sayısı, CRC, üye hashleri) karşılaştırması → journal hash-zinciri (şema, sıra, önceki-hash) → PASS basar; her sapmada FAIL + istisna. Güçlü yanları: salt-okunur, imza-dışı bütünlük kontrolleri tam, hata mesajı az bilgi veriyor. Zayıf noktaları yukarıda (shallow clone, atalık bakılmaması, detached HEAD, çapa yok). Shallow-clone iddiası kod satırıyla doğrulandı.

## Genel izlenim ve öneriler

Kod tabanı dürüst yazılmış: formüller belgelerle birebir (`h_B` ağırlıkları, defect destekleri, Vandermonde, parite-sayım sırası), DP ve Sturmian kontrolleri sağlam, başarısızlıklar sessiz geçilmiyor (`assert`ler yerinde). Ancak denetim klasöründeki bir doğrulama scripti yanlış hüküm basıyor (Madde 7) — raporla script çelişmemeli; öncelik bu düzeltme. Sonra: `mpmath` bağımlılığı belgelensin veya stdlib karşılığı eklensin; GOREV001 çıktı yolları parametrik olsun; `h_3`/`h_∞` için aralık-aritmetiği sertifikası tamamlansın (belgeler zaten istiyor). Hiçbir bulgu ana matematik iddiaları çürütmüyor.

Beyan: dosya yazmadım, düzenlemedim, silmedim; git ile state değiştirmedim (yalnızca okuma: `ls`, `git` yok); Python çalıştırdım (`-B` bayrağıyla, `__pycache__` bile oluşmadı); ağ kullanmadım.

SUPHRAMANETON_YAZMADI
