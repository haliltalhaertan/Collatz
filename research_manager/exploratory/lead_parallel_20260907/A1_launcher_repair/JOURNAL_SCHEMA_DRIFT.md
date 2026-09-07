# RESEARCH_JOURNAL.jsonl — schema drift and hash-chain verification

File: `research_manager/RESEARCH_JOURNAL.jsonl` (21 entries, LF line endings, trailing newline present, no CRLF).
Verified at main `1a6f924`. Date: 2026-09-07.

Entries 1–19 were written by the human/manager governance process. Entries 20–21 were written mechanically by
`.github/scripts/b4_v2_canonical_integrate.py` on branch `origin/b4-v2-governance-runner-no-more-branches-20260905`
(function `journal()`, and its call site that supplies the row dictionaries).

---

## 1. Hash chain: **INTACT — 20 of 20 links verify**

Chaining convention recovered from the CI script (`journal()`, the line that builds each record):

```python
r={**r,'schema':'COLLATZ_RESEARCH_JOURNAL_V1','sequence':seq,'previous_entry_sha256':prev}
line=json.dumps(r,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
raw+=line+b'\n'; prev=hb(line); seq+=1
```

So `entry[n].previous_entry_sha256 == sha256(raw bytes of line n-1, **excluding** the trailing newline)`.
This was confirmed empirically before reading the script, by testing six candidate conventions against all 20 links:

| convention | links verified |
|---|---|
| **sha256(line bytes, no trailing newline)** | **20 / 20** |
| sha256(line bytes + `\n`) | 0 / 20 |
| sha256(re-serialised compact, sorted keys) | 12 / 20 |
| sha256(re-serialised compact, insertion order) | 12 / 20 |
| sha256(`json.dumps` defaults) | 4 / 20 |
| sha256(`json.dumps` sorted, default separators) | 4 / 20 |

The re-serialisation conventions fail on some links only because entries 1–19 were not all written with the same
`json.dumps` settings; the authoritative convention hashes the stored bytes, which is convention-independent, and it
verifies everywhere.

Per-link result (`sha256(line n)` is the value that entry `n+1` must carry):

| seq | sha256 of this line | link from previous |
|---|---|---|
| 1 | `9549132d2d5e4162bfe512f77bceb549d0473cf7c00942daf254a8159456bfad` | genesis (`previous_entry_sha256: null`) |
| 2 | `ae5dad72c9bed9b4697059ac623be265c926c4c18555a4dc58980be78096e0c4` | OK |
| 3 | `6a7e2e14f1e799346515d86ff9216133e46757d6713d0c517ae2ed92dfe65bbc` | OK |
| 4 | `0982f7f093432b0f4d63ae82b7b279c70743e37e9dccfdfa1aa40de0c00aa1c7` | OK |
| 5 | `34bbc2c3ffe96ab408c6a69c97a399ca8c44145e904cae3e3f5d377d874ef1ba` | OK |
| 6 | `99d7d8061528256a0fcff1b9072286f0a83399028869d7571b6985e6ebdf8236` | OK |
| 7 | `6ca3771cf20f1a37349fa3d236a8095c2f5a145c2d2d907bea00cc7898e1e506` | OK |
| 8 | `8c8a5e2d429d339b2c92900d77a82bb996747a98f4274d05eb21f30a469ef43c` | OK |
| 9 | `0909ce7d09a7bea9f08cda9c7e724a60110b808efa413fb9deedfd37d269eff8` | OK |
| 10 | `785ffe55b2152a6188228c31eab063c285ffd914aff67e7e2438bed64eeb7179` | OK |
| 11 | `8cae74d2a54ac60dac74c584ea1ebc59d501e64b46875ee8227b1b2d0d5f2aa6` | OK |
| 12 | `f81317fdfd090f5b9428bf7c9af850f2cf1cd63632fe52df52c63e883e502a2b` | OK |
| 13 | `b4e7cac5d31634e846f11d09341d0dc67388bbcfe72c811337b338c27712ee97` | OK |
| 14 | `38cda175e203b5bab71dea43f80dee17c48bb6a72802dae00a0cd2f41410fd14` | OK |
| 15 | `c6c6914e05f0f42925251b3be26e0e525e9f62cb04923da5b8b3cd7379446ee2` | OK |
| 16 | `f6f36c294110fe8a3002e1a974e2cecc22555cd08625a791464600571af98c44` | OK |
| 17 | `64b9a946f25326588d67d5564429a1b1bb90bf475b015b655611f51522692eef` | OK |
| 18 | `9b8765f2c147233186fc90b24404c57d6a1b82c3e01f0b2c87e0fda8d3e69ca5` | OK |
| 19 | `24321b3fa051b3a567ffbf2eb59bb383a814b9510853c9cc16a14698a4c0c67c` | OK |
| **20** | `27286f626eb3a20735dc14dd789f316161adc6a06439f8df6fb09e6dd948ca9e` | **OK** (19 → 20, across the schema change) |
| **21** | `f00f80b4b0f394b4c08711e03271e519974ef43ede4094fc82b030e3416b6f72` | **OK** (20 → 21) |

**No broken link.** The schema drift did not damage the chain: the CI script read the last stored line and hashed its
raw bytes, so it chained correctly even while changing the record shape. `sequence` is dense and monotone 1…21.
The next appended entry must carry `previous_entry_sha256 = f00f80b4b0f394b4c08711e03271e519974ef43ede4094fc82b030e3416b6f72`.

## 2. Field-by-field differences

All 19 early entries share one key set; entries 20 and 21 differ from each other as well as from the early ones.

| field | entries 1–19 | entry 20 | entry 21 | note |
|---|---|---|---|---|
| `schema` | `COLLATZ_RESEARCH_JOURNAL_V1` | `COLLATZ_RESEARCH_JOURNAL_V1` | `COLLATZ_RESEARCH_JOURNAL_V1` | **identical label, incompatible shape** — the drift is invisible to any consumer that dispatches on `schema` |
| `sequence` | present | present | present | unchanged |
| `previous_entry_sha256` | present | present | present | unchanged |
| `event` | present | present | present | unchanged |
| `timestamp` | **present** — local ISO-8601 with offset, second precision (e.g. `2026-09-04T12:52:47+03:00`) | absent | absent | **renamed** |
| `timestamp_utc` | absent | **present** — UTC with microseconds (`2026-09-04T21:21:12.131508+00:00`) | **present** (`…131514+00:00`) | **renamed**; also a precision and timezone-convention change |
| `active_task` | **present** — task identifier string | absent | absent | **renamed** |
| `task` | absent | **present** — same semantics, same value space | **present** | **renamed** |
| `active_stage` | **present** — governance stage string | absent | **absent**; entry 21 instead carries `stage` | **renamed in 21, dropped in 20** |
| `stage` | absent | **absent** | **present** (`STAGE_1_AUTHORIZED_NOT_EXECUTED`) | inconsistent even between the two new entries |
| `evidence` | **present** — nested object holding all run facts | absent | absent | **dropped**; its contents were flattened to top level |
| `next_action` | **present** — free-text instruction | absent | absent | **dropped entirely** |
| `readback` | absent | present (`PASS`) | present (`PASS`) | new, formerly inside `evidence` |
| `seal_sha256` | absent | present | present | new, formerly inside `evidence` (as `old_seal_sha256`) |
| `phase_a_commit_sha` | absent | present | present | new |
| `authorization_commit_sha` | absent | **absent** | present | new, present in 21 only |
| `contract_sha256` | absent | **absent** | present | new, present in 21 only |
| `scientific_diff` | absent | present (`NO SCIENTIFIC CHANGE`) | **absent** | new, present in 20 only |
| `stage1_executed` | absent | present (`false`) | present (`false`) | new |
| `T1_T8_executed` | absent | present (`false`) | present (`false`) | new; note the non-snake-case `T1_T8` key style |

Summary of the sets:

* present in **every** entry 1–19: `active_stage`, `active_task`, `event`, `evidence`, `next_action`,
  `previous_entry_sha256`, `schema`, `sequence`, `timestamp`
* present in **both** 20 and 21: `T1_T8_executed`, `event`, `phase_a_commit_sha`, `previous_entry_sha256`, `readback`,
  `schema`, `seal_sha256`, `sequence`, `stage1_executed`, `task`, `timestamp_utc`
* fields common to the whole file: only `event`, `previous_entry_sha256`, `schema`, `sequence`

Three renames (`timestamp`→`timestamp_utc`, `active_task`→`task`, `active_stage`→`stage`), two hard drops (`evidence`,
`next_action`), eleven additions, and no version bump on `schema`. Entries 20 and 21 are additionally not schema-uniform
with each other (`stage`, `authorization_commit_sha`, `contract_sha256`, `scientific_diff` appear in one but not the
other), so "entries 20–21 use a V2 shape" is itself an approximation.

## 3. Consequences

The renames are the operationally dangerous part. A reader that resolves the current stage by
`entry['active_stage']` — the pattern established by entries 1–19, and the same pattern the Stage-1 launcher's canonical
state check was repaired to distrust (`…_CANONICAL_STATE_PATH_REPAIR_RECORD.json`) — raises `KeyError` on entry 20 or,
worse, falls back to entry 19 and reports the stage as `STAGE_0_REPAIR_READY_NOT_DISPATCHED` when the true stage is
`STAGE_1_AUTHORIZED_NOT_EXECUTED`. `next_action` — the field that told the next session what it was allowed to do — has
no successor at all in the new shape. This is the same class of defect as the launcher's frozen-dependency semantics:
two writers holding incompatible ideas of one contract, with no mechanical check that they agree.

Note also that `schema` was left at `COLLATZ_RESEARCH_JOURNAL_V1` (hard-coded in `journal()`), so nothing in the file
signals the change.

## 4. Proposed fix: a new sequence-22 CORRECTION entry — no rewriting

**Earlier lines must not be rewritten.** Any edit to lines 1–21 invalidates every subsequent
`previous_entry_sha256` and destroys the only tamper-evidence the journal has. The chain is currently intact (§1) and
that property is worth more than field uniformity.

Append one entry, sequence 22, that (i) declares the drift, (ii) supplies canonical aliases for entries 20 and 21 so an
automated reader can normalise them without touching them, and (iii) fixes the canonical field names going forward:

```json
{"canonical_aliases":{"active_stage":"stage","active_task":"task","timestamp":"timestamp_utc"},"corrected_entries":[20,21],"correction_scope":"FIELD_NAMING_ONLY_NO_CONTENT_CHANGE","earlier_entries_rewritten":false,"event":"JOURNAL_SCHEMA_DRIFT_CORRECTION","normalized_entry_20":{"active_stage":"STAGE_0_REPAIR_ACCEPTED_AWAITING_AUTHORIZATION","active_task":"CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2","next_action":"Create Phase B Stage-1 authorization only after exact Phase-A read-back PASS; do not execute Stage 1 or T1-T8.","timestamp":"2026-09-04T21:21:12.131508+00:00"},"normalized_entry_21":{"active_stage":"STAGE_1_AUTHORIZED_NOT_EXECUTED","active_task":"CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2","next_action":"Execute B4 V2 Stage 1 exactly once under a fresh once-only authorization; not authorized by this entry.","timestamp":"2026-09-04T21:21:12.131514+00:00"},"previous_entry_sha256":"f00f80b4b0f394b4c08711e03271e519974ef43ede4094fc82b030e3416b6f72","required_fields_going_forward":["active_stage","active_task","event","evidence","next_action","previous_entry_sha256","schema","sequence","timestamp"],"schema":"COLLATZ_RESEARCH_JOURNAL_V1","sequence":22,"stage1_executed":false,"T1_T8_executed":false,"writer":".github/scripts/b4_v2_canonical_integrate.py (entries 20-21); correction written by the governance process"}
```

Rules for appending it:

1. Serialise with the file's own convention — `json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',',':'))`
   — write the bytes, then a single `\n`. Do not pretty-print.
2. `previous_entry_sha256` is `f00f80b4b0f394b4c08711e03271e519974ef43ede4094fc82b030e3416b6f72`
   (= `sha256` of line 21's bytes without its newline), which is fixed and given above.
3. The `normalized_entry_20` / `normalized_entry_21` objects are **derived views**, not replacements. Entries 20 and 21
   stay byte-identical on disk; their `active_stage` values above are read from
   `CURRENT_RESEARCH_STATE.json` at `34ac0db` and `f8d778a` respectively, which is where the CI script wrote them.
4. Also repair the producer: `.github/scripts/b4_v2_canonical_integrate.py` should emit
   `active_task`/`active_stage`/`timestamp`/`evidence`/`next_action`, or bump `schema` to a genuinely new label. Leaving
   `COLLATZ_RESEARCH_JOURNAL_V1` on a different shape is the part that makes the drift undetectable.
5. Re-verify the chain after appending: all 21 links must still verify and the new link 21 → 22 must verify.

---

Nothing in this document authorizes a B4 V2 Stage-1 run, and the proposed sequence-22 entry explicitly does not grant
one. The V2 once-only authorization was consumed on 2026-09-05; a new once-only authorization requires an explicit
manager transaction.
