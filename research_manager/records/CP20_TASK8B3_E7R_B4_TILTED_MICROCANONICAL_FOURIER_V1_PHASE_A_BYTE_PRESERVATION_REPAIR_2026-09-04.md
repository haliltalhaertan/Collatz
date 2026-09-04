# B4 Phase-A byte-preservation repair

Prior Phase-A candidate: `6e7757b316646d5eaf350c7acbaecb9c8468f1eb`.

Read-back verdict for that candidate: **FAIL — sealed `ORDER.md` EOL normalization**. Stage 1 remained NOT AUTHORIZED and no Phase-B decision was created.

Repair: add a path-specific `-text` Git attribute and re-stage the exact raw `ORDER.md` bytes independently fetched from Drive seal file `12WfXfOfCHt9XZTSqBYPDfLV7xsZ1bVIY`.

Raw Drive seal SHA-256: `ec26b5fbbd89f0a8184486c82bbb34b6a810263a8b2016a17103cf8fda6ab41c`; 16 unique members; CRC PASS.  
Raw ORDER SHA-256: `90dbb1b229a6f5d7677251ce250ef377dba36b369a566d9cc0207aff420a333a`.  
Required Git blob for raw ORDER: `a62a0781b5c78f6203401b47329a8584617e8f94`.

This repair changes no scientific content and performs no Stage-1 mathematics. Phase-B authorization remains forbidden until the repaired Phase-A commit passes canonical read-back.
