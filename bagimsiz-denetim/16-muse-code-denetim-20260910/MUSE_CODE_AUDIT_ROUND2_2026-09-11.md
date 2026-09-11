# MUSE CODE — BAĞIMSIZ KOD DENETİMİ (ROUND 2)

**Tarih:** 2026-09-11
**Denetçi:** Muse Code 1.1.1 (muse-spark-1.3), reviewer modu — salt-okunur
**Kapsam (round 1'den geniş):** ~40 script'in tamamının çalıştırılması (mpmath kurulu),
14 klasörde rapor-vs-script tutarsızlık avı, GOREV001 panellerinin bağımsız yeniden üretimi,
tools determinizmi, 6 klasörde derin matematik-kod uyumu.
**Bağımsızlık:** Round-1 bulguları prompt'a sokulmadı; taze md5 baseline (43 dosya) alındı.
**Salt-okunur kanıtı:** md5 öncesi/sonrası karşılaştırması — 43 dosya birebir; tek fark
denetçinin değil, round-1 doğrulama scriptinin (`verify_madde07.py`) audit klasörüne
eklenmiş olması. Muse'un scratch'i yalnız /tmp (madde07_fast.py), proje ağacı temiz.

**PROVENANCE NOTU:** Bu denetim, düzeltme-öncesi ağaçta koştu. Denetim bitiminde
uzak dala (aynı PR dalı) 12 remediation commit'i geldi (2b7d2f2..4e09d12, 2026-09-11,
araştırma yöneticisi): madde07 serileştirme düzeltmesi, handoff verifier hardening,
mpmath kaldırma, döngü tespiti, aralık-aritmetiği sertifikaları, B=4 DP düzeltmesi,
GOREV001 portable checker + regression testler. Round-2 bulgularının çoğu bu
commit'lerle kapanmış durumda.

**Karar: ŞARTLI GEÇERLİ.** Sayısal çekirdek sağlam; üç çekince sınıfı: madde07 birincil
scripti, raporun geri aldığı eski çıktıları basan scriptler, verify_handoff'un mevcut
checkout'ta FAIL vermesi. Matematiksel içeriği çürüten bulgu yok.

---

# Bağımsız Kod Denetimi — Sonuç

## Özet karar: ŞARTLI GEÇERLİ

Sayısal çekirdek sağlam: çalıştırdığım ~40 scriptin ürettiği tüm değerler rapor tablolarıyla birebir tutuyor (tek istisna aşağıda). Ancak üç sınıfta çekince var: (1) Madde 7'nin birincil scripti yazıldığı haliyle SHA kontrolünden geçemiyor; (2) birkaç script, raporun metinde düzelttiği eski/hatalı sonucu hâlâ basıyor; (3) `verify_handoff.py` mevcut checkout'ta FAIL verir. Matematiksel içeriği çürüten bir bulgu yok.

## Çalıştırma tablosu

`*` = değer doğru ama çıktıda raporun açıkladığı bir nüans var (altta).

| script | beklenen | gerçek | sonuç |
|---|---|---|---|
| 01 deney.py | 837799/524, 27/111, ort~131 | aynı | GEÇTİ |
| 02-01 lemma_b | 6.363.065 çift, 0 ihlal | aynı | GEÇTİ |
| 02-02 sturmian | p=r+1, aralık 4,3040 | aynı | GEÇTİ |
| 02-03 wang413 | uygulanamaz | aynı | GEÇTİ |
| 02-04 wang411 | uygulanamaz, run=2 | aynı | GEÇTİ |
| 03 carry | 56.246/54.621, 0 ihlal | aynı | GEÇTİ |
| 04 çekirdek_realizör | r300: 141 bas., 1,64e141 | aynı | GEÇTİ |
| 04 madde01_06 | 439.234/3.065.970, 0 | aynı | GEÇTİ |
| 04 madde07 | SHA eşleşti | ASCII ile HAYIR | KALDI |
| 04 madde07b | A/C ham-byte eşleşir | aynı | GEÇTİ |
| 04 madde08 | bloklama tablosu | (c),(e) notu | GEÇTİ* |
| 05-01 h4 | 50 basamak birebir | aynı | GEÇTİ |
| 05-02 dp | 0,68459/0,60004/0,57944 | aynı | GEÇTİ |
| 05-03 kapsam | B=3..16 tablosu | aynı | GEÇTİ |
| 05-04 sonsuz | κ*=2,7840109030 | aynı | GEÇTİ |
| 05-05 parikh | 240.000 çift, 0 ihlal | aynı | GEÇTİ |
| 06 doğrulama | h3=0,523466681 | aynı | GEÇTİ |
| 07 güçlendirme | 06 ile aynı tablo | aynı | GEÇTİ |
| 07 seyrek | eps tablosu | son satır eski | GEÇTİ* |
| 09-10 sürek.kesir | [1;1,1,2,2,3,1,5,2,23..] | aynı | GEÇTİ |
| 09-11 periyot | 969/671/9.967 blok | aynı | GEÇTİ |
| 09-12 etkin_n0 | 107/1520/1050/15780 | aynı | GEÇTİ |
| 09-13 sabit | yalnız K11/K17 bağı | aynı | GEÇTİ |
| 09 hensel | yoğunluk ~0,49, bitler donar | aynı | GEÇTİ |
| 10-01 yüzey | ρ_min 0,3514/0,0976/0,0354 | aynı | GEÇTİ* |
| 10-02 köprü | fark 0,0017 | aynı | GEÇTİ* |
| 11-01 konverjant | S1/S2 tabloları | aynı | GEÇTİ |
| 11-02 konum | 1050/24714/50495/125729 | aynı | GEÇTİ |
| 12-01 çekirdek | 52.190/6.430 test, 0 | aynı | GEÇTİ |
| 12-02 lift | VALID | KARŞI-ÖRNEK basar | GEÇTİ* |
| 12-03 karşıörnek | geçici-plato teşhisi | aynı | GEÇTİ |
| 13-01 A_B_C | 9.688/5.999/1.480, 0 | son satır TUTARSIZ | GEÇTİ* |
| 13-02 liminf | düzeltme analizi | False basar | GEÇTİ* |
| 13-03 kuyruk | kuyruk farkı→0 | aynı | GEÇTİ |
| 13-04 mad11_16_20 | r=1/R=3 örneği | aynı | GEÇTİ |
| 13-05 sentinel | k≥1: 5.188 test, 0 | aynı | GEÇTİ |
| 13-06 2.mertebe | kalan O(1/t) | aynı | GEÇTİ |
| 13-07 plato_c_k | 3 iddia, 0 ihlal | aynı | GEÇTİ |
| 13-08 rijitlik | 5.238 adım, 0 ihlal | aynı | GEÇTİ |
| 13-09 bedel | 120 kelime, 0 fark | aynı | GEÇTİ |
| GOREV001 panel | W/qD2, 4 panel | 4/4 tam eşleşti | GEÇTİ |

GOREV001 ayrıntısı: r=5 W=37/4, r=10 W=819/32, r=12 W=2795/4, r=14 W=274211/256; qD2=37/4, 2915/32, 21195/8, 4612387/256 — dördü de kesir-kesir eşleşti. V ve ince-katman payları da raporla tutuyor. `__main__` çalıştırılmadı, yalnız `panel`/`boundary_example` import edildi. Sınır örneği (P=(1,0,1,0), e=1, V=0, qD2=1) doğrulandı.

## Bulunan sorunlar (yeni bulgular önde)

- **orta** — `04-cp20-task6-denetim/madde07_controller_yeniden_kurulum.py:41-51`: script ASCII digit-string hashliyor (`1639a9bf…`), arşiv değeriyle (`31d2db…`) eşleşmiyor; yazıldığı haliyle `HAYIR` basar. Eşleşme yalnız ham-byte serileştirmede var (orijinal `madde07b` koşuldu: A/C `raw-bytes` eşleşti, ASCII hiçbir varyantta eşleşmedi; hızlı tam-sayı eşdeğeri de aynı sonucu verdi; z∈[−2,1] doğrulandı). Rapor `DENETIM_RAPORU.md:129-135` "EŞLEŞTİ" gösteriyor ama parantez notu ham-byte olduğunu söylüyor — birincil script bu serileştirmeyi uygulamuyor. Ayrıca A ile C varyantı aynı hashi veriyor; hash kuralı tekilleştirmiyor.
- **orta** — `07-geriye-donuk-tarama/seyrek_kritik_genisletme.py:67-68`: `SURVIVOR DISLANIR` basıyor; `RAPOR.md:258-282` bu sonucu açıkça geri alıyor (hypothesis mismatch). Kod güncel değil.
- **orta** — `10-task8a/01_basinc_yuzeyi.py:52-59`, `02_cp19t4_koprusu.py:32-35`: iki script de geri alınan ara sayıları basıyor (grid max h=1,50545 / ince-arama 1,50398, "eşit mi False"); `HESAP_SONUCLARI.md:118-134` düzeltmesi (eksik kısıt `ρ1−ρ2 ≥ 3−2α`) koda yansımamış. Ek: `01` satır 48'de uç noktada anlamsız `h=-2,39e+40` basılıyor; `§2` asimetri tablosundaki üç satır scriptin bastığı ızgarada yok (kapsam farkı, uç).
- **uç** — `12-d0-denetim/02_onebit_lift_ve_kirma.py:51-54`: Madde 9 için `KARSI-ORNEK` (46/78) basıyor; rapor `DENETIM_RAPORU.md:78-94` bunu kriter hatası (geçici plato) diye açıklayıp cebirle VALID hükmediyor. Scripti çalıştıran aksi izlenim edinir.
- **uç** — `13-d1-denetim/01_cekirdek_A_B_C.py:105` `TUTARSIZ` ve `02_madde10_liminf.py:80` `UYUMLU: False` basıyor; ikisi de raporda belgelenmiş hatalı ilk-testler, doğrusu `03_madde10_kuyruk.py` (kuyruk farkı→0, koşuldu, tutuyor).
- **uç** — `04-cp20-task6-denetim/madde08_karsi_ornek_disiplini.py:63-71,80-86`: (c) κ=0,5 adayı H1'e de uymuyor (rapor yalnız H2 diyor); (e) için ölçülen |s|=37289, √N=245 iken "s~√k" yazılmış — gerçek lineer kayma (s/k=−0,62). Bloklama hükmü (H1) doğru, gerekçe cümlesi yanlış.
- **uç** — bakım notları: `06/dogrulama.py` ile `07/guclendirme_dogrulama.py` bit-bit aynı dosya; `04` raporun çekirdek tablosundaki r=150 satırının scriptte karşılığı yok; `09-10` (N=200k) ile `09-11` (N=60k) q=665 uyuşmasında 5. basamakta ayrışıyor (0,999880 vs 0,999899) — rapor değerleri N=60k koşusuna ait, tablolarda N belirtilmeli.

## verify_handoff.py değerlendirmesi

Mantık özeti: state/build şema ve stage allowlist → lock alanları + base_commit varlığı → branch eşitliği → 85 dosya hash'i → arşiv hash/boyut/üye-sayısı + CRC + listelenen üyelerin hash'i → journal hash-zinciri. Kod okundu, çalıştırılmadı.

- Salt-okunur sondaj: repo **shallow** (`is-shallow=true`), dal `external-audit/muse-code-round1-20260910` ≠ state `main` → verifier **şu an FAIL verir** (branch mismatch). Ağaç temiz.
- Zayıf noktalar: shallow durumu hiç sorgulanmıyor (sınırdaki base_commit varsa sığ klon geçer); detached HEAD asla geçemez ama hata mesajı yanıltıcı (`branch mismatch:` boş); state yalnız 81/1008 arşiv üyesini hash'liyor (geri kalan yalnız sayı+CRC ile); working-tree temizliği ve HEAD==base_commit kontrolü yok; journal zincirinin güven çapası yok.
- `build_current_archive.py`: zip baytları deterministik (sabit tarih 1980-01-01, sabit izin, level 9, sıralı kayıt) — ancak `built_utc` kaydı asla bayt-üretilebilir değil ve build, repo'ya yazıyor. `extract_current_archive.py`: zip-slip koruması doğru (`safe_target`), fakat hedef repo-altı zorunlu (untracked kirlilik) ve üye listesi build kaydına karşı doğrulanmıyor (yalnız bütün-hash).

## Genel izlenim ve öneriler

Raporların dürüstlük standardı yüksek: kendi hatalarını (Chernoff işareti, faz-maliyeti artefaktı, T5 survivor, T3 FAIL ifadesi, Madde 9/10 test hataları) metinde açıkça işaretlemişler. Matematik-kod uyumu incelenen altı klasörde de iyi; ikinci-mertede terimler, plato rijitliği, sentinel açıklaması bağımsız koşularla tuttu. Öncelik: (1) madde07 birincil scriptini ham-byte'a çevirip "EŞLEŞTİ" iddiasını kodla da kapatmak; (2) geri alınan çıktıları basan üç scripti düzeltmek ya da başlığına UYARI koymak; (3) handoff branch/shallow durumunu netleştirip 81/1008 üye kapsamasını genişletmek. Collatz'ın kendisiyle ilgili hiçbir iddia bu sette ispat düzeyinde değil — raporlar da bunu söylüyor.

SUPHRAMANETON_YAZMADI
