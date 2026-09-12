# Integrated canonical archive overlay review — 2026-09-12

The builder now includes root `research_*` continuation directories and
`RESEARCH_INDEX_20260908.md` under `EXPLORATORY_CONTINUATION/`. It keeps
`research_manager` in its original `RESEARCH_MANAGEMENT/` location, without a
duplicate copy. Existing static historical members remain byte-for-byte identical
after decompression.

Selection uses `git ls-files -z` and fails if Git discovery fails. Files from the
two newly reviewed roots `research_integration_20260912` and
`research_w_continuation_20260912` can also enter before staging, restricted to
`.md`, `.py`, `.json`, `.jsonl`, and `.txt`. This explicit exception means the
integrator must review those two directories before a release build. Arbitrary
untracked older research files do not enter the archive.

The continuation selector excludes ZIP packages, readback-named artifacts,
compiled/cache files, private `.key` files, SQLite databases, and runtime
guards/locks. It rejects missing selected files and symlink files. Existing
canonical management/audit overlay behavior is unchanged. This file-selection
policy is not a semantic secret-content scanner; it relies on the previously
sanitized tracked snapshot and review of the two new source directories.

`EXPLORATORY_CONTINUATION/` is a dynamic prefix. Recovery rebuilds discard its old
members and insert the current selection, preventing duplication or preservation
of stale continuation files on repeated builds.

Validation: `python -X utf8 tools/test_build_current_archive.py` passed both
regression tests. The selection test covers tracked inclusion, explicit new-root
inclusion, and exclusions. The recovery test builds a small isolated fixture
twice, checks byte-identical ZIPs, verifies unchanged static binary contents, and
checks that the stale exploratory member disappears. It does not rebuild or
modify the real archive. `verify_handoff.py` already checks the whole ZIP and the
complete member-root, so no verifier implementation change is needed.

The actual canonical build verification is recorded separately in
`publication_receipts/BUILD_VERIFICATION_20260912.json`. Its GitHub size cap (100,000,000 bytes), CRC verification,
duplicate-name rejection, and full-member SHA256 root remain active. Archive
integrity establishes preservation, not correctness of every research claim.
