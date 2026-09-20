# CURRENT HANDOFF — CHAIN-KILL INTEGRATED, 2026-09-20

**Collatz is NOT solved and nothing here bears on it.**

Current state: CP21–CP24 are merged into `main` (PRs #3, #4, #5, #6, #2 — merged 2026-09-20).
Start by reading, in this order:

1. `bagimsiz-denetim/05-cp23-chain-kill-20260914/CP23_REPORT.md` — **read this first, it invalidates the previous route**
2. `bagimsiz-denetim/06-cp24-recovery-20260914/CP24_REPORT.md` — corrections to CP21–23 numbers
3. `bagimsiz-denetim/03-cp21-source-monotonicity-20260914/CP21_REPORT.md`
4. `bagimsiz-denetim/04-cp22-adversarial-brainstorm-20260914/CP22_REPORT.md`

## The intended route is DEAD — proved

`3n+1` and `3n-1` have **identical** `Ecal` tables (50/50 `(m,r)` pairs, 30/30 defect rows, zero
differences), because `H_{3n-1}(-x) = -H_{3n+1}(x)` and the energy functional is **blind to the sign
of the affine constant**. But `3n-1` provably has nontrivial cycles (`5 -> 7 -> 10 -> 5`). Therefore
any proof of the target inequality `Ecal(m,s+1) >= Ecal(m+1,s)` applies verbatim to `3n-1`, where
cycles exist: **the inequality cannot exclude a cycle.** `5n+1` gives the same verdict.

Chain grading (CARTOGRAPH, 8 links): L2 `[FAIL]`, L4 `[NOT EVEN FORMULATED]`, L3/L5/L6
`[KNOWN BARRIER]`. The chain breaks before the barriers are even reached.

**The previous handoff's "Next" directive (preserve mixed overlap and reflection projection in a
weighted affine-channel recurrence) is WITHDRAWN.** It is not false — it looks true — but CP23 proves
it cannot do the job it was chosen for. Do not spend budget grinding it; REDIRECT ranked it **last of
12 directions, below stopping entirely**.

## Mandatory ship-gate: the analogue filter

Every existing and future claim must be tested against `3n-1` and `5n+1`. **If a claim holds there
too, it cannot be about Collatz specifically** and may not be labelled as Collatz progress. This
filter produced CP23's largest result in minutes of compute.

## What the programme owns (still valid)

- **A3+A4+counting corollary `[PROOF]`, gap closed, publishable:** same-stratum endpoint collision
  <=> `B`-congruence mod `3^k`; `B` is never `0 mod 3`; hence per stratum #distinct endpoints
  `<= 2*3^(k-1)`. Verified to `m=16`, zero failures, occupancy saturates (54/54 at `(12,4)`).
- **A6 cap stabilisation** (`2^r >= 3^k - 1`) — plausibly new.
- **Cross-term identities (2026-09-12, still valid):** even cross term `E=NB`;
  `S=N0+N1+6N_plus+2N_minus`; combined cross contribution nonnegative; `S_even <= S <= 2*S_even`.
  **`S_even` is NOT `W_flat`** — reading this as `W/W_flat <= 2` is wrong.
- **Phase-quotient computation theorem** (`research_phase_quotient_20260913`):
  `sum_d N_d = O(s^4 * 2^(3s/4))`, an asymptotically smaller exponent than direct `2^s` enumeration.
- 69-entry failure library; 221-row verified dataset.

## Corrections carried by CP24 (use these numbers)

- **221** distinct rows, not 239. CP22's 18 rows were recomputation, not new parameter coverage.
- "35 new rows" should read "35 computed rows, 16 new parameter pairs".
- The claim "none dropped below 1" is **withdrawn**: `(4,2)` has `defect/M = 9/17 < 1`.
- 11 rows of `cp21_lead_extension_m25_m26.json` were wrong (histogram truncation: coarsening needs
  `coarse[z] = sum(fine[z::N])`, not `arr[:q]`). Corrected in `cp24-recovery/corrected_extension.json`.

## Next

No technical target is dispatched by this handoff. The adopted direction (CP23 section 5) is:
write up the negative result as the deliverable, seek outside review and formal verification, and
optionally run ONE timeboxed sign-sensitive cycle bet with pre-registered kill conditions.
Uniform `W`, `D2` and Collatz remain **OPEN**.

All `[PROOF]` labels in this programme mean "hand-checked, not Lean". There has been **zero human
review and zero formal verification** — this is the largest near-term risk.

Publication: `CURRENT_ARCHIVE_BUILD.json`, `CURRENT_ARCHIVE_MEMBER_ROOT.json`, `publication_receipts/`. The deterministic ZIP preserves historical members and includes this reviewed continuation. External receipts remain outside it to avoid recursive hashes.

The following B4 V2 closure is historical governance, not live authorization.

## Historical B4 V2 closure

Canonical task: `CP20_TASK8B3_E7R_B4_TILTED_MICROCANONICAL_FOURIER_V2`  
Active stage: `STAGE_1_INPUT_INTEGRITY_FAILURE_AUTHORIZATION_CONSUMED_CLOSED`

## Forensic identity only — not live authorization

- Phase A / canonical Stage-0 base: `34ac0dbeb8c0ae2fddab706680f1682412b00786`
- Phase B / historical authorization commit: `f8d778a2113922e3bbb14c86ee2fa5359cee28ea`
- Consumed seal SHA-256: `11456b7d6f673e5cab6079850731cbda70373b77e4e0f532089d6783fd16c78e`
- Contract SHA-256: `7f2531743db7c2987d6efa785784852bc6fe066ccc23cfc607296de96f3eb403`
- Manifest SHA-256: `7f48807db5733c85759324d4f94e357aa6941de0ecd911b4180f5bc2101d6dcb`

The once-only authorization was consumed by a real invocation on 2026-09-05. It cannot be invoked, reused, or re-authorized.

## Exact execution trace

- Real sealed entrypoint invoked: **YES**
- Failure: `frozen dependency blob mismatch at Phase A: CURRENT_RESEARCH_STATE.json`
- RUN_WITNESS created: **NO**
- PRE_T1_GATE reached: **NO**
- T1 START reached: **NO**
- T1–T8 mathematics executed: **NO**
- Authorization consumed: **YES**
- Scientific change: **NO SCIENTIFIC CHANGE**

Producer evidence head: `04a66e41864d1d530ead63b1faeaf122048e3069`  
Failure JSON SHA-256: `1997355b8cc2c505df44175b2467598b0e96ded41ab0e45bf9c4d5b6e06ec30a`  
Failure stdout SHA-256: `fad5d23d92ba219aeb6057aaa6c70ed798d79b1229f9a31a261cbcbb1f9d5f34`

Independent audit head: `8fb8d68d3c131d6e11721fd629f1ea879102aedc`  
Audit verdict: `[AUDIT FAIL — DO NOT EXECUTE B4 V2 STAGE1]`  
Audit report SHA-256: `81f8908bc15b2b03c9db4f214831b7c73a1116a3b6d50e003597a3e0575ad0c7`  
Audit JSON SHA-256: `efda35345d58ee1a0109dbb47b25ef4001c894d449c536ce62ac4ac56117bd1e`  
Audit manifest SHA-256: `0ccdbad263ac7960fa6052cfba9f108abe466279117c3577c025faa322fd61a5`

## Scientific status

- B4-N1…B4-N7: `NOT ESTABLISHED`
- B4-CT: `NOT ESTABLISHED`
- E6-N2: `[OPEN]`
- Collatz: **not proved**

## Mandatory stop

**DO NOT EXECUTE OR REUSE THE B4 V2 TUPLE.** No Stage-1 execution is authorized. No V3 task, seal, authorization, or dispatch exists.

Exact next action: await a separate explicit manager transaction, if desired, to design and independently audit a new repair/reseal. This handoff dispatches nothing.

Invalid V1 T1–T8 drafts remain `[INVALID / NON-CANONICAL / DO NOT USE]`.
