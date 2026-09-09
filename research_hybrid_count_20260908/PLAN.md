# Bounded hybrid-state check

2026-09-08. Test the proposed joint high-interval/low-residue count certificate. No canonical changes, paid calls, or broad parameter tuning.

Reuse the exact 48 parameter rows in research_compressed_count_20260908/RESULT.json: r=3..10, offsets -1,0,1, interval exponents .8,1.2. Fix high precision t=min(3,r-1). Compare low precision ell=0..min(3,r-t). Full precision t+ell=r is a calibration, not evidence of useful compression.

Record the upper count and number of memoized Bellman states, compare with the independently verified exact count and old high-only result, check monotonicity under low-digit refinement. Reproduce the r=2,A=3,L=3 spurious splice as a separate exact-precision sanity check. Stop after this panel; use algebraic analysis to decide whether fixed precision can supply the required exponent.
