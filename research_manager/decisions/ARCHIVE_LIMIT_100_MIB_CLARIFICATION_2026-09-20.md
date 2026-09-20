# Archive Limit Unit Clarification — 100 MiB

**Date:** 2026-09-20  
**Status:** GOVERNANCE REPAIR / NO SCIENTIFIC CHANGE

The archive builder used `100_000_000` bytes as GitHub's single-object hard limit. GitHub's current documentation states that files larger than **100 MiB** are blocked. The binary threshold is therefore `100 * 1024 * 1024 = 104_857_600` bytes.

Reference: https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github

The rebuilt archive is `101_923_222` bytes: below 100 MiB, but with only `2_934_378` bytes of remaining headroom.

Decision:

1. Correct the builder and state metadata to the documented 100 MiB threshold.
2. Keep fail-closed behavior at the threshold.
3. Record a mandatory next-growth rule: before a future build reaches the threshold, migrate to hash-manifested split volumes, a base+overlay layout, Git LFS, or a GitHub Release/Drive artifact. Do not silently omit or delete historical members for headroom.
4. This is packaging governance only. It changes no mathematical status and does not prove Collatz.
