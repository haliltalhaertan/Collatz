# Source Krawtchouk Round 5 package manifest

Date: 2026-09-13
Base main: `434d8fc55544207b35a4c4390600598dd6623d28`
Research branch: `research/mixed-gram-round1-20260912`
PR: #2

Verified exact package:

- logical filename: `COLLATZ_SOURCE_KRAWTCHOUK_ROUND5_20260913.zip`
- bytes: `18760`
- ZIP members: `11`
- SHA-256: `9ef68e86e5967c3b38197d4be482ca854a6fa204e1c2dafdddafb0b9b49ca457`
- Drive file id: `1_9FSBbzxO_Qivkdy30PVCWrFmyRLt3sa`
- Drive folder: `SOURCE_KRAWTCHOUK_ROUND5_20260913`

## GitHub exact-byte representation

The GitHub connector available in the research session accepts UTF-8 repository files but has no direct local-binary upload action. An initial attempted binary blob was detected by read-back to have the wrong size and was deleted.

The exact package is therefore stored losslessly on GitHub as six verified base64 parts:

- `package_b64/part00.txt` — 5000 bytes — Git blob `4448cfd573c867bd7a67bedf0ecf563c760b6f1d`
- `package_b64/part01.txt` — 5000 bytes — Git blob `d0bde1568a7765e5866323c2e7d04fccc7bf921b`
- `package_b64/part02.txt` — 5000 bytes — Git blob `3055e251a792d16b0bf1a95cbc9dc9e4cb4640ad`
- `package_b64/part03.txt` — 5000 bytes — Git blob `25d44c52b173662e51842cbd5be74f0fba54c01f`
- `package_b64/part04.txt` — 5000 bytes — Git blob `315e5af247cd08f9742259c080e2e7eb7d5cdf68`
- `package_b64/part05.txt` — 16 bytes — Git blob `1a5eb52a119006431a6a8f6ee06509a17fb4ed1c`

These six Git blob IDs and sizes were read back from GitHub and match the locally generated exact-package chunks byte for byte.

Reconstruction from a checkout:

```bash
cat research_source_krawtchouk_20260913/package_b64/part*.txt \
  | base64 -d > COLLATZ_SOURCE_KRAWTCHOUK_ROUND5_20260913.zip
sha256sum COLLATZ_SOURCE_KRAWTCHOUK_ROUND5_20260913.zip
```

Expected SHA-256:

`9ef68e86e5967c3b38197d4be482ca854a6fa204e1c2dafdddafb0b9b49ca457`

The ZIP contains the full Round-5 report, producer code, full `RESULTS.json`, summary, provenance, checksums, same-session second implementation and its output/results, and the preserved first failed checker record.

Drive also contains all 11 constituent files individually plus the exact ZIP.

No real subagent was available; the second implementation is not represented as an independent-agent audit. No paid provider calls were made. Old B4 V1/V2 authorization was not reused. Uniform W, W_flat, D2 and Collatz remain open.
