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
