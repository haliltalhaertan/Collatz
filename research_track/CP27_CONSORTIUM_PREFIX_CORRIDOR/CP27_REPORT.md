# CP27 — Konsorsiyum: iç rezonans / bütün-prefix koridoru

Tarih: 2026-09-23. Durum: **KAPANDI**. Collatz **AÇIK**. Sonlu hesaplar teorem değildir.
Yöntem: Workflow Rev4 (WORKFLOW_ROLES_REV4.md). Üyeler: ChatGPT Web, Muse 1.3 (xhigh, salt-okunur), Unreal Agent (gpt-6-sol); koordinatör Hermes (eşit oy, veto yok).

## Tur 1 (bağımsız)
Üç üye de koordinatörün CP27 önerisine (Aday B'yi n_min≥2^71 altında test) DEĞİŞTİR dedi.
Ortak teşhis: en büyük yöntem hatası küçük-ölçek rasyonel istatistiği büyük n_min rejimine genellemek + COLLAPSE kapısını geç uygulamak.
Koordinatör exact doğrulamaları (evidence/r1_coordinator_checks.json):
- Unreal Z-A no-go [PROOF, exact örnek]: k=256, n_min=326>X=128, ilk alt geçiş tam döngüde. "n_min≥X ⇒ erken geçiş" rasyonel düzeyde yanlış.
- Unreal Z-B eleği: X=2^71'de ilk izinli geçiş t=72.057.431.991 (brute force t≤200000: 0; yarı-yakınsak taraması). Klasik döngü uzunluğu sınırıyla aynı sayı.

## Tur 2 (anonim çapraz eleştiri)
- Aday B: 3/3 PARK.
- X-B determinant: 3/3 "h_t=0'a zorlamıyor" (H_X≈1,63665·10^21; bilinen sınırlar alt sınır, gereken üst sınır).
- Brifingde koordinatörün tek-adım / blok sayısı notasyon karışıklığı ChatGPT tarafından yakalandı.
- Unreal Z-B formülünde t=1 istisnası; Muse Y-1'de koşulsuz adım hatası bulundu.
- Konsorsiyum seçimi: X-A ALL_PREFIX_CORRIDOR (üç üyenin ilk ikisinde).

## X-A testi ve denetim
Koridor lemması [PROOF]: n_j≥X, Δ_t>0 ⇒ Δ_t < t·ln(1+1/X).
LEMMA V (koordinatör; 3/3 üye (i),(ii) DOĞRU, rotasyon boşluğu YOK):
q≤K/2 ise dengeli bloklar s_j∈{⌊K/q⌋,⌈K/q⌉}, e_j=⌊s_j log2 3⌋ ile bütün proper blok-prefixlerde Δ_t<0; koridor boş; blok 0 kendiliğinden strict global minimum. Exact: 15/15 (cp27_xa_construct.py).
Kapsam çekincesi (ChatGPT, Unreal): (iii) (K,M,q) düzeyinde varlıksaldır; inşa edilen kelimenin integral olduğu gösterilmedi.
Dar rejim (ChatGPT/Unreal bağımsız, koordinatör sayısal doğrulama):
- q−1 ≤ β(K−1) (β=log2 3−1) ise koridor yine boş yapılabilir (inşa).
- q−1 > β(K−1) şeridinde zorunlu Δ_{q−1} ≥ [q−1−β(K−1)]ln2 > 0. q=92..120'de minimum (q,K)=(118,201): 317ln2−200ln3≈0,0051985 ≫ koridor ≤119 ln(1+2^-71)≈5,04·10^-20. Şerit kesin elenir.
- Ancak global koşul n_min≥X ile zaten 0<M ln2−K ln3 ≤ K ln(1+1/(3X)); K<240'ta sol taraf ≥0,0051985 > sağ taraf 3,39·10^-20 → dar rejim global koşulla zaten boş (Unreal). Koridorun ek elemesi yok.
Literatür: q/K>1/2'yi genel dışlayan sonuç DOĞRULANMADI (üç üye). Simons–de Weger v1.44 (91≤m≤515619 için K>7,53·10^11) eşlemesi ChatGPT'ce önerildi, DOĞRULANMADI.

## Kararlar
| Konu | Karar |
|---|---|
| Aday B (ilk geçiş iç rezonansı) | PARK (3/3) |
| X-B determinant | KILL (zorlama yok) |
| X-A ana rejim q≤K/2 | KILL/PARK — Lemma V boşluk lemması olarak saklanır |
| X-A dar rejim | PARK — gerçek ama global X koşulu zaten eler |
| Z-A, Z-B | Guardrail/no-go olarak saklanır |

## Süreç notları
- ChatGPT Tur 2 cevabı arka plan sekmesinde kısmi render edildi (DOM 126 karakter, sunucuda tam). poll_marker.py'ye otomatik reload eklendi; X-A turunda 1 reload ile çalıştı.
- Koordinatör gereksiz bir yeniden gönderim yaptı (1 mesaj kotası israfı).

## Sonraki adım önerisi (konsorsiyuma sunulacak)
Minimum/prefix/koridor ailesi CP26–CP27'de klasik Diophantine sınıra indirgendi. Yeni yön konsorsiyum Tur 1 ile seçilmeli; önerilen kapı: "Hercher/Simons–de Weger'in zaten kullandığı ürün+CF iskeletine indirgenmiyor mu?"
