# CP20 TASK 8B3 — E7R-B3 V1 — CANONICAL STAGE 0 RECORD

Status: `[STAGE 0 FROZEN — AWAITING MANAGER AUTHORIZATION]`

Canonical dependency audit commit: `887aa78c6a3508b70a6277cc09705837aec79edf`

Accepted scientific dependencies only:
- E6-N1
- E7R-B1 `[PROVED][AUDITED]`
- E7R-B2 `[PROVED][AUDITED]`

Historical/lost/unaudited B3 conclusions are excluded.

Frozen theorem:
`exists A,R0<infinity such that for all r>=R0, sup_(k,ell in W_r) |mathcal K^(4)_(u_r,v_r)(k,ell)| <= A/m_r`.

Frozen geometry:
- `n_r=floor((log_2 3-1)r)-8`
- `u_r=floor(r/3)`
- `v_r=r-floor(r/3)`
- `m_r=v_r-u_r`
- `W_r=ceil(8 sqrt(r ln(r+1)))`
- feasible: integers `r>=16`, `0<=k<=ell<=n_r`
- window: `|k-u_r n_r/r|<=W_r`, `|ell-v_r n_r/r|<=W_r`

Frozen mechanisms: M1 local swap/holonomy; M2 arithmetic residue cancellation; M3 exact recursive concatenation; M4 mandatory analytic counterfamily search.

Frozen counterfamilies: left edge, right edge, diagonal/low-increment feasibility, fixed/slow increment feasibility, mod-6 residue probe, left-edge near-one row-phase alignment.

Fixed finite diagnostic r-grid: `24, 96, 384, 1536`. No adaptive extension. Complex diagnostics are binary64 `[NUM]`; geometry sanity uses Decimal at exactly 80 digits. No precision rescue.

Stage 1 has NOT been executed.

Drive persistence folder:
`https://drive.google.com/drive/folders/1QnrFYkCCqQbgd1daK9N6EAyY4s2NIJec`

## Stage-0 artifact SHA-256

- `CP20_TASK8B3_E7R_B3_V1_PRE_RUN_SEAL.md`: `5d0cf5c2a7b4e6fde40b5b8f854b1f72c01d505d643b8838b95f1e6dcda9b75c`
- `CP20_TASK8B3_E7R_B3_V1_CONFIG.json`: `832dc8a930090d166cf3fb0e5f7687ac838c8ef2fd2a281b413da1c484e2aa12`
- `CP20_TASK8B3_E7R_B3_V1_OUTPUT_SCHEMA.json`: `2df66a1b448f9eb1a8b02f081a1298dbd78a905863fe1bdce4826a5648234d7c`
- `CP20_TASK8B3_E7R_B3_V1_KERNEL_CHECKS.py`: `24e8d3d132b92672470a4a2b05450875a652ef46263e066f78c54496140cdb81`
- `CP20_TASK8B3_E7R_B3_V1_STAGE1.py`: `9e1f781fd6170d1d35a6e70842068e9fa054dd3c0233d7f9249b4a5becfce323`
- `CP20_TASK8B3_E7R_B3_V1_VERIFY.py`: `df18bd0f9a434877ec57312caa1c3d45def9f95c216e41d6bbdec4f8d3169062`
- `CP20_TASK8B3_E7R_B3_V1_PRE_RUN_SHA256SUMS.txt`: `18b82a2cc02692033014e7090b3661a221ca31f6b73a7b1a983dbcd6a55adbb4`
- `CP20_TASK8B3_E7R_B3_V1_PRE_RUN_SEAL.zip`: `acb61ef495bc164c5f55754ea355128bd8105bf7ddec9ff900c2dc16f9646eb3`

Pre-run manifest count: 6 manifested source/config/seal files.
Pre-run manifest SHA-256: `18b82a2cc02692033014e7090b3661a221ca31f6b73a7b1a983dbcd6a55adbb4`.
Deterministic pre-run ZIP member count: 7.
Pre-run ZIP SHA-256: `acb61ef495bc164c5f55754ea355128bd8105bf7ddec9ff900c2dc16f9646eb3`.

ZIP policy: sorted member names; ZIP_STORED; fixed member timestamp 1980-01-01 00:00:00; CRC PASS at seal time.

Any manifested-byte, theorem, window, geometry, diagnostic, precision, counterfamily, norm, or source change voids this record and requires a fresh seal.

Nothing in this record proves the Collatz conjecture.
