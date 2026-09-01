# Collatz Research Archive

Bu depo iki ayrı katman taşıyor. Karışmamaları önemli.

| Katman | Yer | Ne |
|---|---|---|
| **Arşiv** | `Collatz Problemi — Araştırma Arşivi-*.zip` | Google Drive'daki kanonik araştırma arşivinin aynası (CP01–CP20, 718 girdi) |
| **Bağımsız denetim** | [`bagimsiz-denetim/`](bagimsiz-denetim/) | Arşivin aktif cephesine yapılan zero-trust doğrulama katmanı |

---

## Katman 1 — Arşiv

Kullanıcının kanonik Google Drive Collatz araştırma arşivinin aynası.

Drive kök klasörü: `1mRJGjUsali3eOYtRyMnvO19afK_M4SY5`

Checkpoint'ler, promptlar, denetimler, hesaplama artefaktları, manifestolar
ve kurtarılan arşivler burada korunuyor. Baş araştırmacı programı bu katman
üzerinden yürütüyor.

### Güncel senkronize arşiv

- Arşiv: [`Collatz_Research_Archive_CURRENT.zip`](./Collatz_Research_Archive_CURRENT.zip)
- SHA-256: `0dc2284a1d0113bd79fd462db10ee7b0278d9be8c38a42fd8563c389bb7c5902`
- Üye sayısı: 834
- Açılmış araştırma verisi: 165.110.971 bayt
- ZIP boyutu: 84.163.627 bayt
- Derleme kaydı: [`CURRENT_ARCHIVE_BUILD.json`](./CURRENT_ARCHIVE_BUILD.json)

Güncel paket; tam çıkarılmış araştırma ağacını, E3–E6 artefakt ve verilerini,
bağımsız E4 denetim çıktılarını, araştırma yöneticisi prompt/kararlarını ve
deterministik paketleme aracını içeriyor. Geçici doğrulama ağaçları ile aynı
hash'li girdilerin izole audit kopyaları pakete tekrar eklenmedi.

### Aktif araştırma durumu

- E4: belge/kapsam onarımlarıyla bağımsız denetimden geçti.
- E5: E5-S1 tam conditioned-geometric bridge kabul edildi; E5-S2–E5-S5 açık.
- E6: Stage 1 sonuç paketi yalnızca
  `83a26e81fc8a96479a6b76fdd33f962a047885115f00ec6a892248a0c07b6c57`
  seal ZIP hash'i altında döndü. Complete-package SHA-256
  `9511dc8c9bbd0485f159bbfdf2b5f1f784813af156db5085d90e4faccf1be849`;
  E6-N1, kapsam onarımlarıyla yönetici denetiminden geçti; E6-N2–E6-N5 açık.
- E7: pre-run seal doğrulandı. Seal ZIP SHA-256
  `0eb3b2d1487ec1d8dfcf0fc200b1082a8e61b7df2e52f9b6f8f1b943f2ad77f0`;
  açık dış yönetici onayı bekleniyor. Stage 1 yetkili değil.

### Kesintisiz devir ve kurtarma

Yeni bir LLM veya araştırmacı önce [`START_HERE_CURRENT_HANDOFF.md`](./START_HERE_CURRENT_HANDOFF.md)
dosyasını okumalıdır. Canlı durumun makine-okunur tek kaynağı
[`CURRENT_RESEARCH_STATE.json`](./CURRENT_RESEARCH_STATE.json), olay geçmişi
ise hash-zincirli [`research_manager/RESEARCH_JOURNAL.jsonl`](./research_manager/RESEARCH_JOURNAL.jsonl)
dosyasıdır.

Devam etmeden önce şu kontrol geçmelidir:

```bash
python tools/verify_handoff.py
```

Arşiv ağacı yerelde yoksa, hash'i doğrulanmış güncel paket üzerine yazmadan
`_restored_current/` altına şu araçla geri yüklenebilir:

```bash
python tools/extract_current_archive.py
```

Her kabul edilmiş bilimsel ilerleme; karar, günlük, canlı durum, güncel arşiv,
doğrulama ve GitHub push işlemlerinin tek bir yayın çevrimi olarak
tamamlanmasını gerektirir.

## Katman 2 — Bağımsız denetim

Kaynak: `haliltalhaertan/math` deposu, dal
`claude/matematiksel-arastirmalar-rrzrbc`. Tüm içerik
[`bagimsiz-denetim/`](bagimsiz-denetim/) altına aktarıldı; commit geçmişi
[`bagimsiz-denetim/GECMIS.md`](bagimsiz-denetim/GECMIS.md) içinde.

Bu katmanın kuralı: **arşivin motorlarına bakılmaz.** Her dizi tanımlardan
sıfırdan kurulur, sonuçlar ancak ondan sonra karşılaştırılır. Protokolün
tamamı [`bagimsiz-denetim/DENETCI_PROMPTU.md`](bagimsiz-denetim/DENETCI_PROMPTU.md)
dosyasında — başka bir modele tek seferde yapıştırılabilir.

### Denetim sonuçları

| Klasör | Konu | Sonuç |
|---|---|---|
| `04-cp20-task6-denetim` | CP20 Task 6 | `[PROOF VALID WITH WORDING REPAIR]` |
| `05-cp20-task7-denetim` | CP20 Task 7 | `[PROOF VALID WITH WORDING REPAIR]` (kapsam) |
| `11-surekli-kesir-denetim` | Sürekli kesir bulgusu | `[VALID AS OBSERVATION — ONE LEMMA MISSING]` |
| `12-d0-denetim` | CP20 Task 8B2 D0 | `[PROOF VALID WITH WORDING REPAIR]` |
| `13-d1-denetim` | CP20 Task 8B2 D1 | `[PROOF VALID WITH WORDING REPAIR]` + Bulgu D |

### Bu katmanın arşive geri verdikleri

- **Task 6'nın B=3 güçlendirmesi** (`06-task6-guclendirme`) — `κ ≥ 1.585`
  sınırını `κ ≥ 3.028`'e çıkarıyor. Drive'da `STRENGTHENED_COROLLARY_V3`
  olarak donduruldu.
- **Sürekli kesir etkin sınırı** (`09-literaturden-baglantilar`) —
  `log₂ n₀ ≳ α·q_n`. Drive'da karşılığı yok.
- **Bulgu D** (`13-d1-denetim`) — `c_k := (3^k r_k + B_k)/2^{A_k}` ile
  injury-free adımın tam karakterizasyonu: bir plato, sıradan bir tam
  sayının gerçek Syracuse yörünge parçası. Sonucu: sonsuz plato ⟺ LEVEL-3
  problemi.

### Denetimin bende düzelttiği hatalar

Bu katman kendi hatalarını da kayda geçiriyor; hepsi ilgili raporlarda ⛔
bloklarıyla duruyor ve `DENETCI_PROMPTU.md` §5'te hata ailesi olarak
soyutlandı. Ayrıntı için [`bagimsiz-denetim/DURUM.md`](bagimsiz-denetim/DURUM.md).

---

## İlk kez bakıyorsanız

`bagimsiz-denetim/01-collatz/` sıfırdan giriş — problemin ne olduğu, neden
zor olduğu, elle takip edilebilir örnekler. Matematik bilgisi gerektirmiyor.

```bash
python3 bagimsiz-denetim/01-collatz/deney.py
```

---

Bu depodaki mevcut çalışmalar Collatz varsayımını kanıtlamamaktadır.
