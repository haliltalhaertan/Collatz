# Drive raw-archive read-back — 2026-09-07

Destination folder: `1Tg5P5wfILAgKYg-CiUmJS60kzdRFL2AU`  
Folder URL: https://drive.google.com/drive/folders/1Tg5P5wfILAgKYg-CiUmJS60kzdRFL2AU

The connector accepted both raw ZIPs. Each stored object was fetched with complete base64 content, decoded in the verification process, SHA-256 hashed, and compared with the original local ZIP. The verifier's SHA-256 implementation was first checked against the standard `abc` test vector.

| Archive | Drive ID | Bytes | SHA-256 | Verdict |
|---|---|---:|---|---|
| `lead_parallel_20260907_RAW.zip` | `1xHk0DMQdlR61ce-uJilo6pHyn4MoNZz8` | 2,403,892 | `e7cff5854e6cda42f216c25ec9fcd70676a8d6877bab013f8899f33732ff0443` | PASS |
| `math_20260907_INTERRUPTED_RAW.zip` | `1BPHjVwTmzaw1hC4mc0uZbaUOm4Wo75pW` | 79,988 | `c1d200539009fe7c87d4ccec86071ab69d3bf9143c0721258039436e78848f03` | PASS |

These PASS verdicts establish byte persistence only. They do not promote A1, A3, A5, M1, M4, PWE, KFB, E6-N2, B4, or Collatz to a proved/accepted status. M1 and M4 remain interrupted; A1 remains unauthorized and must not be executed.
