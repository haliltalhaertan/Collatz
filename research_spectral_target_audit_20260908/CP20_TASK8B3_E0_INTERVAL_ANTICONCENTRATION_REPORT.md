# CP20 TASK 8B3 E0 — INTERVAL ANTI-CONCENTRATION REPORT

**Status:** `[OPEN — FINITE EXACT EVIDENCE SUPPORTS UNIFORM-LIKE OCCUPANCY]`

For \(Q_{r,A}(\beta)=\#\{w:0\le M_r(w)<2^{\beta r}\}\), compare with \(|W_{r,A}|2^{(\beta-\alpha)r}\) and
\[
D_r(\beta)=\frac1r\log_2\frac{Q}{|W|2^{(\beta-\alpha)r}}.
\]
All feasible \(|d|\le5\) were exhausted through r=10, the full band at r=12, and critical d=0 through r=14.

At d=0:
- r=12, beta=1.2: ratio 0.988, D=-0.00145;
- r=12, beta=1.45: ratio 1.002, D=0.000236;
- r=14, beta=1.2: ratio 1.005, D=0.000518;
- r=14, beta=1.45: ratio 1.0022, D=0.000227.

No finite evidence of exponential Archimedean clustering was found. The low-conductor obstruction therefore does not close this route.

Next target after audit: a uniform critical-band bound
\[
Q_{r,A}(\beta)\le2^{(h_*+\beta-\alpha+o(1))r}
\]
for a beta range sufficient for Task 6, with fixed-conductor periodic bias handled separately.
