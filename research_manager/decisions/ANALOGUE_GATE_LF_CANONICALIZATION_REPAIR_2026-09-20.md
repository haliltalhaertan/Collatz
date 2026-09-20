# Analogue Gate LF Canonicalization Repair

**Date:** 2026-09-20  
**Status:** INTEGRITY REPAIR / NO SCIENTIFIC CHANGE

A fresh-clone handoff check found that the committed Git blobs for `tools/analogue_gate.py` and `tools/test_analogue_gate.py` were LF-only, while the archive build had read mixed-EOL working-tree copies. The mathematical source text was unchanged after Git clean normalization, but byte hashes differed across working trees.

Decision:

1. Materialize both files from their canonical LF Git blobs.
2. Update repository and archive member hashes to those LF bytes.
3. Rebuild the deterministic archive and require a fresh-clone `verify_handoff.py` PASS before merging.
4. No scientific claim changes. Collatz remains open.
