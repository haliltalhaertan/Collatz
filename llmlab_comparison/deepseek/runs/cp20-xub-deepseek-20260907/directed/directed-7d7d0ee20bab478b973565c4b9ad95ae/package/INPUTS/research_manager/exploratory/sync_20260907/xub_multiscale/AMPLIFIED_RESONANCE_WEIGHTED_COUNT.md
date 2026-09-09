# Exact weighted count for amplified positive resonances

Date: 2026-09-07

Status: `[EXACT REDUCTION / ARITHMETIC BOUND OPEN]`.

Fix a bounded-positive word length `L`, alphabet `{1,...,B_0}`, and interior start `j`. Let `H_j=B_1+...+B_j`, and define

`U_(B_0)(z)=sum_(b=1)^(B_0)(b+1)z^b`,

`a_(L,w)=[z^w]U_(B_0)(z)^L`.

For the actual boundary index `tau`,

`E_j=tau+floor(beta*tau)+1+2j+H_j`, `D_j=tau+2j`.

Let `R_(j,L)(h)` be the indicator that

`dist(2^(tau+floor(beta*tau)+1+2j+h)/3^(tau+2j+2L),Z) < eta/9^L`

with positive nearest integer. For `j>=1` and `R-2j-2L>=1`, exact uniform-composition counting gives

`P(G_(j,L) intersect R_(j,L) | S_R=K)`

`= binom(K+R-1,R-1)^(-1)`

`  * sum_(h,w) R_(j,L)(h) binom(h+2j-1,2j-1) a_(L,w)`

`    * binom(K-h-w+R-2j-2L-1,R-2j-2L-1)`,

where `h>=0`, `L<=w<=B_0 L`, and `h+w<=K`. Boundary cases use the standard zero-component convention.

This formula retains the actual prefix weight, word split multiplicities, endpoint conditioning, and growing ternary conductor. It uses no independence approximation.

The resonance is equivalent to a run of `Theta(L)` equal binary digits in a selected short shift of `1/3^(D_j+2L)`. Full-orbit multiplicative order and LTE do not bound this weighted short-orbit occupation.

Moreover, a per-start atom estimate followed by a union bound cannot reach the target in the useful-word regime. If useful-word probability is `R^(-a+o(1))`, abundance requires `a<1`; multiplying `O(R)` starts by a typical `O(R^(-1/2))` prefix atom gives `R^(1/2-a)`, not `O(1/R)`.

The correct target is therefore a global lower-tail or exponential-moment estimate for the number of non-low, nonresonant useful blocks, allowing some resonant blocks rather than requiring none.

