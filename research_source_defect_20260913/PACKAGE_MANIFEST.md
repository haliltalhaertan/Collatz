# Source Defect Round 7 package manifest

Date: 2026-09-13
Base main: `434d8fc55544207b35a4c4390600598dd6623d28`
Research branch: `research/mixed-gram-round1-20260912`
PR: #2

## Google Drive

Folder:
`https://drive.google.com/drive/folders/1r86UtxIrBkf9DN6gVRGCfXJY9f80h1bo`

ZIP:
- file id: `1dOXw-q4l9tTavfCrPpmMVEyEmawbI7na`
- name: `COLLATZ_SOURCE_DEFECT_ROUND7_20260913.zip`
- bytes: `20035`
- members: `11`
- SHA-256: `51053b4f8441a565d3703decb228841d4cf66f4e21a458c74c6dafe74401afdd`
- raw Drive read-back: verified byte size + SHA-256; ZIP CRC/testzip PASS.

Readable report:
- file id: `1e2XzO38WcYE1oZT54JXtHmPy5VD-AEZo`
- name: `REPORT_TR.md`

Drive manifest:
- file id: `1B6dBo8Wu2ul7yZWgzEpKNKTeq_ZHqOg0`
- name: `PACKAGE_MANIFEST.md`

## GitHub exact-byte mirror

The scientific report/code/summary/provenance are stored as readable UTF-8 files.
The full exact Drive ZIP is additionally represented losslessly in
`research_source_defect_20260913/package_b64/part*.txt`.

All six part files were read back from GitHub and their Git blob SHA-1 values
match the locally generated chunks exactly:

- part00: `c6652ef4b65061b387da73be5585a5c26eb5116d` (5000 bytes)
- part01: `8b9c9291e3f4693def7b78f5625417407010e4c6` (5000 bytes)
- part02: `eb6f68e744ea003d7db57039e24a0e111d24c34a` (5000 bytes)
- part03: `6b53e2d365e9abde304a43193a52d23946d8f28c` (5000 bytes)
- part04: `16d6da3a70498ffeb23385f0be07b4da52e44bf6` (5000 bytes)
- part05: `9e777d9734eaf077f707aecc84f8a1349c3dc0e7` (1716 bytes)

Reconstruct:

```bash
cat research_source_defect_20260913/package_b64/part*.txt \
  | base64 -d > COLLATZ_SOURCE_DEFECT_ROUND7_20260913.zip
sha256sum COLLATZ_SOURCE_DEFECT_ROUND7_20260913.zip
```

Expected SHA-256:
`51053b4f8441a565d3703decb228841d4cf66f4e21a458c74c6dafe74401afdd`

Thus Drive and GitHub contain the same full Round-7 byte package, while the
main report/code remain directly readable in both workflows.
