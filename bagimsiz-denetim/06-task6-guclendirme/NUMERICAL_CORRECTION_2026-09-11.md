# Numerical correction and certificate note — 2026-09-11

Independent re-computation after the Muse Code round-1 audit confirmed one non-material table typo in `CP20_TASK6_STRENGTHENED_COROLLARY.md` §10.

For `B=4`, `r=640`, `C_D=8`, the exact DP count gives

`log2(N)/r = 0.5794355916750416...`

so the six-decimal display is **0.579436**, not `0.579440`.

This does not change the stated pressure constant `h_4=0.561900734...`, the asymptotic argument, or any threshold. The historical candidate document is preserved unchanged; this note is the correction record.

The previously open proof-critical numerical requirement for `h_3` and `h_infinity` now has a standard-library rational interval checker in `interval_pressure_certificate.py`. Its verified output is:

- `h_3 in [0.523466680692464716388106606672490983, 0.523466680692464716388106606672491091]`
- `alpha/h_3 in [3.027819265639788519869187409275958256, 3.027819265639788519869187409275958874]`
- `h_infinity in [0.569309013485800536574394779462134721, 0.569309013485800536574394779462134871]`
- `alpha/h_infinity in [2.784010903000901886208036320856840999, 2.784010903000901886208036320856841726]`

The checker uses exact `fractions.Fraction` arithmetic plus a rational atanh-series remainder bound for logarithms; floating point is not used for proof-critical sign decisions.

This note does **not** by itself promote the strengthened corollary to a new canonical status; non-numerical audit/governance requirements remain separate.
