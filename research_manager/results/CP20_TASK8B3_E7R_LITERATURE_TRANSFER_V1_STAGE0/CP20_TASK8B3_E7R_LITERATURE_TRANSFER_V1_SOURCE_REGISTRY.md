# CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1 — SOURCE REGISTRY

Status: **STAGE 0 SOURCE FREEZE**

Project base commit: `b3eaaae80a64003f4ee06a43b65fbd3680b8e22b`
Stage-0 order SHA-256: `004d22da3d279dd27c6f88a08a723956e99b3f9777eb2ecb3784644d42b1ac8f`

## Project authorities

Only the following project results are accepted dependencies:

- E6-N1 `[PROVED][AUDITED/ACCEPTED WITH SCOPE REPAIR]`
- E7R-B1 `[PROVED][AUDITED]`
- E7R-B2 `[PROVED][AUDITED]`
- B3-CT `[PROVED][AUDITED]`

The full frozen-window pointwise E7R-B3 `O(1/m_r)` route is `[FALSE][CLOSED]`.
E7R-B4/E6-N2, E7R-B5, and E7R-B6 remain `[OPEN]`.
Historical pre-recovery E7 conclusions remain `[UNVERIFIED — ARTIFACTS LOST]`.

Canonical project files are frozen by Git commit `b3eaaae80a64003f4ee06a43b65fbd3680b8e22b`. Stage 1 may use only files at that commit or separately hash-sealed files named below.

## T — Terence Tao

Title: *Almost all orbits of the Collatz map attain almost bounded values*  
arXiv: `1909.03562v7`  
Version: `v7`  
Last revised: `2026-07-16 05:37:32 UTC`  
Journal reference: Forum of Mathematics, Pi 10 (2022), e12.

Frozen local files:

- `sources/tao/tao_1909.03562v7.pdf`
  - SHA-256: `62cf49d4d8e8e681c7a4738ebaf56f3dbb7b67de95f37ccbac6e428ef3fc394e`
- `sources/tao/tao_1909.03562v7_source.tar`
  - SHA-256: `ba81acd6254838251f1ee585256a6f9f223cdc9c73bed0a3c4fd25782d0124ad`

Minimum locations to inspect in Stage 1:

- §1.2, Eq. (1.1): Syracuse step as an affine map.
- §1.2, Eqs. (1.3)–(1.7): iterated affine map and offset notation.
- Definition 1.7: geometric random variable convention.
- Eq. (1.22): Syracuse random variable on a 3-adic cyclic group.
- Proposition 1.17 / Eq. (1.28): high-frequency characteristic-function decay for the Syracuse offset.
- Eq. (1.29): reversed-offset representation used in the Fourier analysis.
- §7, Proposition 7.1 and its white-point/renewal mechanism.

Tao's results may be treated as known literature. **No mapping from Tao's observable to the project observable is accepted in Stage 0.**

## S — Yuan Si

Title: *A microcanonical phase transition for the Collatz affine random model*  
Author: Yuan Si  
Evidence class: **[LITERATURE CLAIM — UNAUDITED]**

### Zenodo frozen record

DOI: `10.5281/zenodo.20027097`  
Record: `20027097`  
Created/modified: `2026-05-04`  
Frozen file: `sources/si_zenodo/main.pdf`

- MD5 published by Zenodo: `f59b2b147590fc66d3153d34ad497390`
- SHA-256 independently frozen: `0dfad7f22df91c14c36182d7557aee537a462ef0a2a548422c366d21e2bd06c8`

### Public source repository

Repository: `SamSi0322/collatz-affine-model`  
Exact commit: `119199e7165505f9535952e272056af912ce59fb`

Frozen files:

- `sources/si_github/main.tex`
  - SHA-256: `c1ff1f11f442fed1b2f7a37be61fe0e3c0916719549018557446ca01e81e0811`
- `sources/si_github/main.pdf`
  - SHA-256: `0dfad7f22df91c14c36182d7557aee537a462ef0a2a548422c366d21e2bd06c8`

The Zenodo PDF and GitHub `main.pdf` are byte-identical at the frozen commit.

Minimum Si source labels/definitions to inspect in Stage 1:

- `eq:affine`: affine iterate `3^n 2^(-S_n)x + F_n`.
- `eq:Fn`: affine offset.
- `eq:split`: multiplicative/offset character split.
- microcanonical conditioning on `S_n=s`.
- effective ternary depth `d(xi)=n+k-v_3(xi)` and `h=k-v_3(xi)`.
- `eq:Delta`: `Delta_n=s log_3 2-n-h`.
- resonant hard frequency `xi=3^(k-h) 2^s`.
- the Bernoulli-bridge/perpetuity reduction and pair-switch variables.

Every theorem-level statement imported from Si remains `[LITERATURE CLAIM — UNAUDITED]` unless independently proved or separately audited.

## Dependency rule

No unsealed web page, cached quotation, secondary summary, or later source revision may become a Stage-1 dependency. Any source change requires a new seal.
