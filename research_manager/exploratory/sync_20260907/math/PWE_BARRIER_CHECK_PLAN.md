# Predeclared bounded check plan

Date: 2026-09-07

Status: exploratory numerical cross-check only. This plan was written before the
source was executed. It authorizes no sealed run, depth extension, fit, plot, or
canonical change.

The independent script will implement the row-product dynamic program directly,
without importing producer code. It will perform only these checks:

1. Compute `H_{r-4,n_r-j}(j)` for `r in {30,40,50,60}` and every
   `0 <= j <= min(n_r,L_r)`, with `delta=1/2` in the published cutoff.
   Record adjacent increases of `|H_j|`, the maximizing `j`, and the ratio to
   `|H_0|`. Purpose: test the claimed monotonic/coupling rationale, not PWE's
   eventual bounded-ratio statement.
2. Compute the full, barrier-restricted, and complementary complex expectations
   for `G_{r,n_r}` at `r in {30,60,100}` and `T in {-4,0}`, where the barrier is
   `delta_s <= T` for all rows. Compute the corresponding exact path-count
   probability. Purpose: distinguish a barrier probability from a complex
   Feynman-Kac contribution.
3. Use integer modular powers for every phase and Python binary64 complex
   arithmetic. This is `[NUM]`; no asymptotic claim follows.

No other cases may be added after output inspection.
