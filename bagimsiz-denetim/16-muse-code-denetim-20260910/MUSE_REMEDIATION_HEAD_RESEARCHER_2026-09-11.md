# Muse Code Round-1 — Head-Researcher Verification and Remediation

**Date:** 2026-09-11  
**Repository:** `haliltalhaertan/Collatz`  
**PR:** `#1`, branch `external-audit/muse-code-round1-20260910`  
**Purpose:** independently verify the actionable Muse Code round-1 findings, repair confirmed reproducibility/integrity defects on the PR branch, preserve the historical audit record, and state what remains open.

## Verdict

Muse's round-1 verdict remains **CONDITIONALLY VALID**. I independently confirmed the substantive reproducibility findings listed below. None of the confirmed defects refutes the project's audited mathematical claims or proves any new Collatz theorem. The main mathematical research gap — an asymptotic upper bound on `W` or `D_2` strong enough for the current counting bridge — remains open.

## Confirmed findings and remediation

### 1. Madde 7 SHA serialization — CONFIRMED, FIXED

The reconstructed controller word is correct. For the same 100,000 symbols:

- SHA256 of ASCII digit-string serialization: `1639a9bfb801c79a86adc889e6631dbce7db7b07a8798e0542b4d50030c1ade1`
- SHA256 of canonical raw `bytes(a)`: `31d2db3d10ec0610f1c17fc86a6b485f6e8a378ed7696d5b41ad48e51980e1d2`
- archived SHA256: `31d2db3d10ec0610f1c17fc86a6b485f6e8a378ed7696d5b41ad48e51980e1d2`
- observed bounded-tracking range: `[-2, 1]`, inside the claimed `[-41,1]` range.

`madde07_controller_yeniden_kurulum.py` now verifies the canonical raw-byte hash and prints the text hash only diagnostically.

### 2. Madde 7b boundary handling — CONFIRMED, FIXED MORE STRONGLY

The previous `Decimal` boundary correction was one-sided. `q_k=floor((1053/1000) log2 m)` is now computed exactly from integers:

`q_k = ((m**1053).bit_length() - 1) // 1000`.

This removes floating/Decimal boundary ambiguity from the threshold table.

### 3. `mpmath` reproducibility dependency — CONFIRMED, FIXED

Two audited scripts were not self-contained in an environment without `mpmath`.

- `06-task6-guclendirme/dogrulama.py` now uses only stdlib `Decimal`, deterministic derivative bracketing/bisection, and a positive-curvature check.
- `09-literaturden-baglantilar/10_surekli_kesir_periyotlari.py` now uses stdlib `Decimal`.

Both rewritten scripts were executed successfully. The pressure table and the continued-fraction/shift-agreement values reproduce the previous results at the displayed precision.

### 4. Proof-critical pressure constants lacked interval certification — CONFIRMED, FIXED NUMERICALLY

A new `interval_pressure_certificate.py` uses exact `fractions.Fraction` arithmetic and rational remainder bounds for the atanh/log series. No floating-point sign decision is used in the certificate.

Certified intervals:

- `h_3 in [0.523466680692464716388106606672490983, 0.523466680692464716388106606672491091]`
- `alpha/h_3 in [3.027819265639788519869187409275958256, 3.027819265639788519869187409275958874]`
- `h_infinity in [0.569309013485800536574394779462134721, 0.569309013485800536574394779462134871]`
- `alpha/h_infinity in [2.784010903000901886208036320856840999, 2.784010903000901886208036320856841726]`

This closes the numerical-certification item only. It does **not** by itself promote the strengthened corollary's governance status; its non-numerical audit requirements remain separate.

### 5. B=4, r=640 table value — CONFIRMED, CORRECTION RECORDED

Exact DP re-computation gives

`log2(N)/640 = 0.5794355916750416...`,

so the six-decimal value is `0.579436`, not the historical document's `0.579440`.

The historical candidate document was not silently rewritten. A separate `NUMERICAL_CORRECTION_2026-09-11.md` records the correction and the new interval certificates.

### 6. `tools/verify_handoff.py` Git-context weaknesses — CONFIRMED, HARDENED

Independent synthetic-Git tests confirmed:

- a shallow clone can lack the historical `base_commit` object and previously failed even when current content was intact;
- merely checking `cat-file` does not prove that a present base commit is an ancestor of HEAD;
- a detached HEAD at the exact expected branch tip was previously rejected.

The verifier now:

1. requires `merge-base --is-ancestor` whenever the historical commit object is present;
2. treats a missing historical base in a **shallow clone** as a warning only for a `RELEASED` lock;
3. still fails a `HELD` lock when its base cannot be verified;
4. checks `continuity.minimum_required_commit` similarly;
5. accepts detached HEAD only when HEAD exactly equals an available expected local/origin branch tip and emits a warning.

Synthetic regression result: `VERIFY_HANDOFF_GIT_CONTEXT_TESTS: PASS`.

### 7. GOREV001 hardcoded `/mnt/data` output — CONFIRMED, PORTABLE REFERENCE ADDED

A portable copy accepts `--output-dir` (default: current directory) and an optional `--no-reference-check`. The exact internal arithmetic checks remain the evidence; the reference table is treated only as a regression lock.

The portable run reproduced exactly:

- r=5: `W=37/4`, `qD2=37/4`
- r=10: `W=819/32`, `qD2=2915/32`
- r=12: `W=2795/4`, `qD2=21195/8`
- r=14: `W=274211/256`, `qD2=4612387/256`
- boundary m=3,k=2,t=2,j=1: `P=[1,0,1,0]`, `V=0`, `qD2=1`.

### 8. `01-collatz/deney.py` non-1 cycle handling — CONFIRMED, FIXED

Explicit cycle detection was added to both direct trajectory and cached step-count paths. The full 1..1,000,000 run still reproduces the old finite result: longest start `837799`, 524 steps; average 131.4; first-100,000 peak start `77671` reaches `1570824736`.

## Finding deliberately NOT “fixed” as if solved

Muse noted that the journal hash chain lacks an external first-entry anchor. The chain's internal integrity is verified, but a constant stored in the same Git repository is not a genuinely external anchor. I therefore did **not** fake a solution by adding a same-repository constant. If stronger tamper-evidence is desired, the root hash should be published in an independent medium (for example Drive with immutable provenance, a release attestation, or another signed/externally timestamped channel) and then verified against that source.

## Evidence hashes from the independent remediation run

- `madde07_output.txt`: `a67ad29520a75e5d9ef8d6c7676204c5f7a1c8c75b4cfcbaf00517d0d4e5c30e`
- `dogrulama_output.txt`: `6cb157fb9604de67a41643081d5fea31c874237bdda3f31ba35290acf1ea79e9`
- `10_surekli_kesir_periyotlari_output.txt`: `25feba685651b5263da9fb0d2c3d49ae85b9fbf36d2cc320bab9c4039a96dda6`
- `interval_pressure_certificate_output.txt`: `5628de1bcc9cb2f1241356973ef132fda1d893777ced17ae1efed797e62d6eb3`
- `verify_handoff_test_output.txt`: `daedbb0b7ef829c854f2bd549ecc297b80ab9c36c74a5c57a5615c7f0760e583`
- `GOREV001_independent_check_portable.py`: `f7c93daf5dd2c08f6feb14f5b2095694031c56f9d49bc50ac2a6945aa9a52899`
- portable `RESULTS.json`: `173e8ea2c930eaa9a2ae0470db866b96aeeb4b9c1b17b23afdf3094c9f59e016`
- portable `ACTUAL_OUTPUT.txt`: `8a3a588cff45fa07250190c5b3f77a6dca642be932dfdea14102db2df3316172`
- `deney_output.txt`: `bfd8bd2402cff1cf67e777e6c692f39deecb9509ef044503715e298385958f91`
- `test_verify_handoff_git_context.py`: `d47c7e012591d8cdf8e47ad79fbcd31b64d1a15aa5de7546bd360d12edf74c3c`

## Publication / merge status

These remediations belong on the existing external-audit PR branch. They should **not** be merged directly to `main` as a substitute for the repository's canonical publication cycle. `GITHUB_SYNC_POLICY.md` requires an accepted audit/manager milestone to rebuild and verify the deterministic current archive and record the resulting archive/commit hashes in the handoff. Until that cycle is performed, PR #1 should remain open.

## Scientific status after remediation

No new Collatz proof or orbit exclusion is claimed. The current quantitative research bottleneck remains the asymptotic bound on the actual filtered source quantity `W` (or helper `D_2`) strong enough to cross the already-audited sufficient exponent threshold.
