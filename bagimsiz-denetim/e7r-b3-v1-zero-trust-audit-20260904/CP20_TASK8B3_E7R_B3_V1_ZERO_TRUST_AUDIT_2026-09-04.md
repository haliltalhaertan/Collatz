# CP20 TASK 8B3 — E7R-B3 V1 — ZERO-TRUST COUNTERTHEOREM AUDIT

Audit date: 2026-09-04

## Final verdict

[AUDIT PASS]

## 1. Audit target and integrity

Audited package:

`CP20_TASK8B3_E7R_B3_V1_STAGE1_COMPLETE_PACKAGE.zip`

Authoritative package SHA-256:

`5172a6cadfa5d2bbce84564f19d3ba76b1338e51c7a5a96225d8c77ac4b4b186`

Independently recomputed package SHA-256:

`5172a6cadfa5d2bbce84564f19d3ba76b1338e51c7a5a96225d8c77ac4b4b186`

Authorized pre-run seal SHA-256:

`acb61ef495bc164c5f55754ea355128bd8105bf7ddec9ff900c2dc16f9646eb3`

Independently recomputed embedded seal SHA-256:

`acb61ef495bc164c5f55754ea355128bd8105bf7ddec9ff900c2dc16f9646eb3`

All entries of the Stage-1 SHA-256 manifest were independently recomputed and matched. The pre-run seal was separately unpacked, and every pre-run manifest entry also matched. The canonical Stage-1 result commit `b76e9e004cf9310ae0fc4a295b33d0d1c3836a62` was read independently from GitHub and contains the same B3-CT claim, package hash, seal hash, and mandatory-stop status.

The producer verifier was not used as independent mathematical evidence.

## 2. Frozen definitions being audited

Let

\[
\alpha=\log_2 3,\qquad \beta=\alpha-1,
\]

\[
n_r=\lfloor\beta r\rfloor-8,
\quad u_r=\lfloor r/3\rfloor,
\quad v_r=r-u_r,
\quad m_r=v_r-u_r,
\]

and

\[
W_r=\left\lceil 8\sqrt{r\ln(r+1)}\right\rceil.
\]

Write

\[
\mu_u=u_r n_r/r,\qquad \mu_v=v_r n_r/r.
\]

The frozen endpoint window is

\[
\mathcal W_r=\{(k,\ell):0\le k\le\ell\le n_r,
|k-\mu_u|\le W_r,
|\ell-\mu_v|\le W_r\}.
\]

For block rows `s>=u_r+1>=6`, the accepted finite phase is

\[
q_{s,j}=\exp\!\left(2\pi i\frac{2^{s+j-5}\bmod 3^s}{3^s}\right).
\]

For feasible endpoints the normalized block kernel is the uniform weak-composition average

\[
\mathcal K^{(4)}_{u,v}(k,\ell)
=\frac{1}{\binom{\ell-k+v-u-1}{v-u-1}}
\sum_{x_{u+1}+\cdots+x_v=\ell-k}
\prod_{s=u+1}^{v}q_{s,t_{s-1}},
\]

where `t_u=k` and `t_s=k+sum_{a=u+1}^s x_a`.

The frozen B3 theorem claimed the existence of absolute finite constants `A,R0` such that, for all sufficiently large `r`,

\[
\sup_{(k,\ell)\in\mathcal W_r}
|\mathcal K^{(4)}_{u_r,v_r}(k,\ell)|\le A/m_r.
\]

## 3. CF-left feasibility and frozen-window persistence

The unclipped CF-left endpoints are

\[
k_r=\lceil \mu_u-W_r\rceil,
\qquad
\ell_r=\lceil \mu_v-W_r\rceil.
\]

Because `W_r` is an integer,

\[
-W_r\le k_r-\mu_u<1-W_r,
\]

and similarly for `\ell_r`, hence both remain in the original frozen window whenever feasible. Also `\ell_r>=k_r` and `\ell_r<=n_r`; the only eventual clipping issue is positivity of `k_r`.

Using

\[
u_r\ge (r-2)/3,
\qquad n_r/r\ge \beta-9/r,
\]

we obtain

\[
\mu_u\ge\frac{\beta r}{3}-3-\frac{2\beta}{3}+\frac{6}{r}.
\]

Since

\[
W_r\le8\sqrt{r\ln(r+1)}+1,
\]

a sufficient lower bound for `\mu_u-W_r` is

\[
f(r)=\frac{\beta r}{3}-3-\frac{2\beta}{3}+rac{6}{r}-8\sqrt{r\ln(r+1)}-1.
\]

Independent high-precision evaluation gives

\[
f(17000)=54.90439255695679\ldots>0.
\]

A derivative lower bound at `r=17000` is

\[
0.0894081320325768\ldots>0,
\]

and remains positive thereafter. Thus clipping is inactive for every `r>=17000`.

A separate 100-digit/140-digit cross-precision scan over `16<=r<17000` found no geometry disagreements. The last clipped value is `r=16376`; at `r=16377`,

\[
(n,u,v,m,W,k,\ell)=(9571,5459,10918,5459,3190,1,3191).
\]

No later clipping occurs before the analytic tail takes over. The load-bearing proof uses only the conservative explicit threshold `r>=17000`.

## 4. Exact uniform weak-composition block bridge

Put `\Delta=\ell_r-k_r`. On fixed endpoints, every nonnegative increment vector

\[
x_{u+1}+\cdots+x_v=\Delta
\]

has the same conditional weight, so the normalized kernel is exactly the uniform average over weak compositions of `\Delta` into `m=m_r` parts.

Write

\[
k_r=\frac{u n_r}{r}-W+\varepsilon_u,
\qquad
\ell_r=\frac{v n_r}{r}-W+\varepsilon_v,
\qquad0\le\varepsilon_u,\varepsilon_v<1.
\]

Then

\[
\Delta=\frac{m n_r}{r}+\varepsilon_v-\varepsilon_u.
\]

For the partial block sum `X_a`, the deterministic linear interpolation is

\[
L_a=k_r+\frac{a\Delta}{m}
=\frac{(u+a)n_r}{r}-W+(1-a/m)\varepsilon_u+(a/m)\varepsilon_v,
\]

hence

\[
L_a\le\beta(u+a)-W+1.
\]

## 5. Stars-and-bars, Doob and Azuma constants

A uniform weak composition corresponds bijectively to `\Delta` stars and `m-1` bars. Let

\[
N=\Delta+m-1,\qquad K=m-1.
\]

The bar positions are a uniformly random `K`-subset of `{1,...,N}`. If `B_a` is the `a`-th bar, then `B_a=X_a+a` exactly.

For fixed prefix length `x`, let `H_x` count bars in the first `x` positions. Then

\[
\mathbb EH_x=xK/N.
\]

The Doob martingale obtained by exposing positions sequentially has exact step bound

\[
|M_i-M_{i-1}|\le1,
\]

because its two possible next values differ by

\[
1-\frac{x-i}{N-i}=\frac{N-x}{N-i}\le1.
\]

Therefore Azuma-Hoeffding yields each one-sided tail `exp(-t^2/(2x))`.

For `1<=a<=m-1`, put `y_a=a+a\Delta/m`. The positive and negative excursion conversions give respectively deviations larger than `(H-1)K/N` and `HK/N`.

For the unclipped CF-left family,

\[
N=\Delta+m-1<m\left(1+\frac{n_r}{r}\right)<\alpha m.
\]

Thus

\[
K/N>\frac{m-1}{\alpha m}>1/2
\]

for `m>=5`. Taking `H=W/2` and using `H>=3`, the weaker common deviation `>H/3` is valid in both directions. Therefore

\[
\Pr\left(\left|X_a-a\Delta/m\right|>W/2\right)
\le2\exp\left(-\frac{W^2}{72N}\right).
\]

Union bounding the interior times and using `N<\alpha m` yields exactly

\[
P_r^{\rm bad}\le2m_r\exp\left(-\frac{W_r^2}{72\alpha m_r}\right).
\]

Since `W_r^2>=64r\ln(r+1)` and `m_r<=(r+4)/3`,

\[
P_r^{\rm bad}\le2m_r(r+1)^{-c_r},
\qquad
c_r=\frac{8}{3\alpha}\frac{r}{r+4}.
\]

The limiting exponent is

\[
\frac{8}{3\log_2 3}=1.6824793428572198\ldots>1,
\]

so `P_r^{bad}=o(1)`.

## 6. Good-event phase alignment and no modular wrap

On the good bridge event,

\[
|X_a-a\Delta/m|\le W/2.
\]

At row `s=u+a+1`, the preceding state `j=k_r+X_a` obeys

\[
j\le L_a+W/2\le\beta(s-1)-W/2+1.
\]

The exact no-wrap threshold is

\[
2^{s+j-5}<3^s\iff j<\beta s+5.
\]

The good-event estimate gives the stronger uniform margin

\[
(\beta s+5)-j\ge W/2+4+\beta.
\]

Thus no modular wrap occurs on any good bridge path. Consequently

\[
q_{s,j}=\exp\left(2\pi i\,2^{j-\beta s-5}\right),
\]

and

\[
|q_{s,j}-1|\le2\pi\,2^{-W/2-4-\beta}
=2\pi\,2^{-W/2-4-(\alpha-1)}.
\]

## 7. Telescoping and averaging

For unit-modulus factors,

\[
\left|\prod_{i=1}^m z_i-1\right|\le\sum_{i=1}^m|z_i-1|.
\]

Hence every good path satisfies

\[
\left|\prod_{s=u+1}^{v}q_{s,t_{s-1}}-1\right|
\le2\pi m_r2^{-W_r/2-4-\beta}.
\]

Let `F_r` be the phase product under the exact uniform block bridge. On the bad event `|F_r-1|<=2`. Therefore

\[
|\mathcal K^{(4)}_{u_r,v_r}(k_r,\ell_r)-1|
\le2\pi m_r2^{-W_r/2-4-\beta}+2P_r^{\rm bad}.
\]

Both terms tend to zero, so

\[
\mathcal K^{(4)}_{u_r,v_r}(k_r,\ell_r)\to1.
\]

No independence assumption between row phases is used.

## 8. Independent reproductions without producer imports

At `r=16377`, independent high-precision geometry gives

\[
(n,u,v,m,W,k,\ell)=(9571,5459,10918,5459,3190,1,3191),
\]

with endpoint center distances `-3189.333333...` and `-3189.666666...`, both within the original `W=3190` window.

For an exact kernel/phase checkpoint, at sealed `r=24` left-window endpoint `(u,v,k,\ell)=(8,16,0,0)`, there is exactly one all-zero weak composition. For `s=9,...,16`, no modular wrap occurs at `j=0`, and

\[
\sum_{s=9}^{16}\frac{2^{s-5}}{3^s}=\frac{100880}{43046721}.
\]

Therefore

\[
\mathcal K^{(4)}_{8,16}(0,0)
=\exp\left(2\pi i\frac{100880}{43046721}\right).
\]

Its binary64 evaluation from this exact fraction is

`0.9998915943568581 + 0.01472411404805949 i`.

## 9. Logical consequence for frozen B3

The CF-left pair lies in the full frozen pointwise window for all sufficiently large `r`, and its normalized kernel converges to `1`. Thus for any finite `A`, eventually `|\mathcal K|>1/2` while `m_r>2A`, contradicting `|\mathcal K|<=A/m_r`.

## 10. Exact accepted countertheorem

B3-CT is accepted as an audited countertheorem. Define

\[
\alpha=\log_2 3,\quad\beta=\alpha-1,\quad n_r=\lfloor\beta r\rfloor-8,
\]

\[
u_r=\lfloor r/3\rfloor,\quad v_r=r-u_r,\quad m_r=v_r-u_r,
\]

\[
W_r=\left\lceil8\sqrt{r\ln(r+1)}\right\rceil.
\]

For every integer `r>=17000`, let

\[
k_r=\left\lceil u_r n_r/r-W_r\right\rceil,
\qquad
\ell_r=\left\lceil v_r n_r/r-W_r\right\rceil.
\]

Then `(k_r,\ell_r)` is feasible and belongs to the original frozen endpoint window `\mathcal W_r`, and

\[
\mathcal K^{(4)}_{u_r,v_r}(k_r,\ell_r)\to1.
\]

Consequently

\[
\sup_{(k,\ell)\in\mathcal W_r}
|\mathcal K^{(4)}_{u_r,v_r}(k,\ell)|\not=O(1/m_r).
\]

The threshold `17000` is a conservative explicit proof threshold. Independent finite reproduction identifies `16377` as the first permanently-unclipped integer, but minimality is not needed.

## 11. Scope and remaining open work

This refutes exactly the full frozen pointwise E7R-B3 `O(1/m_r)` statement and any claimed full-window uniform contraction bounded away from `1`.

It does not establish or refute a smaller subwindow excluding CF-left, averaged/weighted/L2/operator norms, modified endpoint windows/geometries, all possible global cancellation mechanisms, or E7R-B4/E6-N2 by another route. E7R-B1 and E7R-B2 remain the previously accepted audited results. E7R-B4/E6-N2, E7R-B5, E7R-B6, weighted/operator alternatives, and any redesigned B3 statement remain open unless separately proved and audited.

No weighted-operator work or E8 work was begun.

Nothing in this audit proves the Collatz conjecture.
