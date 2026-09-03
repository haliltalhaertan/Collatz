# CP20 TASK 8B3 — E7 RECOVERY V1 — ZERO-TRUST AUDIT

Audit date: 2026-09-03

## FINAL VERDICT

`[AUDIT PASS]`

## 1. Audit target and integrity

Audited package:

`CP20_TASK8B3_E7_RECOVERY_V1_STAGE1_COMPLETE_PACKAGE.zip`

Authoritative package SHA-256:

`3889a381235965d3392f944a0c0b637b7fc6493daf6d07d164b836de0f6df486`

Independently recomputed package SHA-256:

`3889a381235965d3392f944a0c0b637b7fc6493daf6d07d164b836de0f6df486`

Authoritative pre-run seal SHA-256:

`58734a03a2aa7854f9ecb9f079c6db4b3d05191c249ffa6ccd7e629c4085590c`

Independently recomputed embedded pre-run seal SHA-256:

`58734a03a2aa7854f9ecb9f079c6db4b3d05191c249ffa6ccd7e629c4085590c`

The integrity gate therefore passes byte-for-byte. The producer verifier was not treated as independent mathematical evidence. The mathematical adjudication below is based on fresh derivation from the frozen definitions and independent exact reproductions.

## 2. E7R-B1 — exact block kernels and concatenation

Status: **[PROVED] — ACCEPTED.**

Frozen definitions were checked on their stated domains. For `0<=u<=v<=r`, nonnegative endpoints `k,ell`, with `k<=ell` when `u<v` and `k=0` when `u=0`, let `m=v-u` and `Delta=ell-k`. For a weak composition `x_{u+1}+...+x_v=Delta`, define cumulative states `t_u=k` and `t_s=k+sum_{a=u+1}^s x_a`.

The complex kernel is

```text
K^(4)_{u,v}(k,ell)=sum_x product_{s=u+1}^v q_{s,t_{s-1}},
```

where `q_{1,0}=zeta_4` and later rows use the frozen finite phase law.

The positive kernel is

```text
K^+_{u,v}(k,ell)=C(ell-k+v-u-1,v-u-1)
```

for feasible `u<v`, with the frozen totalized boundary conventions.

The normalized kernel is

```text
mathcal K^(4)_{u,v}(k,ell)=K^(4)_{u,v}(k,ell)/K^+_{u,v}(k,ell)
```

on feasible positive-mass endpoints.

### General concatenation proof

For every valid split `u<w<v`, every full weak composition has a unique intermediate state

```text
j=k+sum_{a=u+1}^w x_a.
```

This gives a bijection between full compositions and triples consisting of `j`, a left composition from `k` to `j`, and a right composition from `j` to `ell`. The phase product factors exactly across the split because each row multiplier depends only on the row and the state immediately preceding that row. Therefore

```text
K^(4)_{u,v}(k,ell)=sum_{j=k}^ell K^(4)_{u,w}(k,j) K^(4)_{w,v}(j,ell).
```

Removing phases gives the positive Vandermonde identity

```text
K^+_{u,v}(k,ell)=sum_{j=k}^ell K^+_{u,w}(k,j) K^+_{w,v}(j,ell).
```

Dividing by total positive mass gives the normalized cotransition law

```text
mathcal K^(4)_{u,v}(k,ell)
= sum_j pi_{u,w,v}(j|k,ell)
  mathcal K^(4)_{u,w}(k,j)
  mathcal K^(4)_{w,v}(j,ell),
```

with

```text
pi_{u,w,v}(j|k,ell)=K^+_{u,w}(k,j)K^+_{w,v}(j,ell)/K^+_{u,v}(k,ell),
```

nonnegative and summing exactly to one.

### Independent exact reproductions

**Boundary kernel.** For `(u,v,k,ell)=(0,2,0,0)`, there is one all-zero composition, so

```text
K^(4)_{0,2}(0,0)=exp(2*pi*i/48) exp(2*pi*i/72)=exp(2*pi*i*5/144),
K^+_{0,2}(0,0)=1.
```

The normalized kernel is the same phase. This confirms that `zeta_4` appears exactly once on the left boundary.

**Modular-inverse checkpoint.** For `(s,j)=(2,0)`, the exponent is `-3`; use `8^{-1} mod 9 = 8`. Because `8*8=1+7*9`, the correction gives

```text
8/9 - 7/8 = 1/72 mod 1,
```

which equals the analytic finite phase exactly.

**Central kernel checkpoint.** For `(r,u,v,k,ell)=(24,8,16,2,4)`,

```text
K^+_{8,16}(2,4)=C(9,7)=36.
```

Independent enumeration produced exactly 36 phase terms over denominator `3^16=43046721`; hence the central complex kernel and its normalization were independently reconstructed from the frozen definition.

**Nontrivial complex concatenation checkpoint.** For `(u,w,v,k,ell)=(2,4,6,1,4)`, the full complex kernel has 20 exact phase terms over denominator `1458`. Independent left/right enumeration by intermediate states `j=1,2,3,4` produced groups of sizes `4,6,6,4`, whose exact multiset union equals the full 20-term kernel. Thus the complex concatenation identity holds exactly in this nontrivial case.

**Positive/normalized concatenation at the same checkpoint.**

```text
K^+_{2,6}(1,4)=C(6,3)=20=4+6+6+4.
```

The exact cotransition weights are

```text
(1/5, 3/10, 3/10, 1/5),
```

which sum exactly to one. Therefore both the positive and normalized concatenation laws are independently reproduced.

**Conclusion for B1:** E7R-B1 survives zero-trust audit on its complete frozen domain. Finite checks are corroborative only; the theorem is established by the general composition-splitting bijection.

## 3. E7R-B2 — conditioned excursion tail

Status: **[PROVED] — ACCEPTED.**

Let

```text
alpha=log_2(3),
beta=alpha-1,
n_r=floor(beta*r)-8,
W_r=ceil(8*sqrt(r*ln(r+1))).
```

Define

```text
Bad_r={ max_{0<=s<=r} |S_s - s*n_r/r| > W_r }.
```

### 3.1 Conditioned weak-composition bridge

For iid nonnegative geometric increments `Z_1,...,Z_r`, the joint probability of a vector `z` with total `n` depends only on `n`. Therefore conditioning on `S_r=n` makes `(Z_1,...,Z_r)` uniform over all weak compositions of `n` into `r` parts. This is exact and uses no unconditioned approximation.

The resulting one-time bridge law is

```text
P(S_s=j | S_r=n)
= [C(j+s-1,s-1) C(n-j+r-s-1,r-s-1)] / C(n+r-1,r-1),
```

for `1<=s<=r-1` and `0<=j<=n`.

### 3.2 Stars-and-bars and fixed-size subset

Encode a weak composition by `n` stars and `r-1` bars. Let

```text
N=n+r-1,
K=r-1.
```

Uniform compositions correspond bijectively to uniformly random `K`-subsets of `{1,...,N}`, namely the bar positions. If `B_s` is the position of the `s`-th bar, then exactly

```text
B_s=S_s+s.
```

### 3.3 Hypergeometric prefix process and Doob martingale

For fixed `x`, let `H_x` be the number of bars among positions `1,...,x`. Then

```text
E[H_x]=xK/N.
```

Expose positions sequentially and define

```text
M_i=E[H_x | first i positions exposed], 0<=i<=x.
```

This is a Doob martingale. After `i-1` exposures, the two possible values of `M_i` according as position `i` is a bar or a star differ by

```text
1-(x-i)/(N-i)=(N-x)/(N-i)<=1.
```

Since `M_{i-1}` is a convex combination of these values,

```text
|M_i-M_{i-1}|<=1.
```

This is the exact bounded-increment constant used in the audit.

Azuma-Hoeffding therefore gives

```text
P(H_x-EH_x >= t) <= exp(-t^2/(2x)),
P(H_x-EH_x <= -t) <= exp(-t^2/(2x)).
```

### 3.4 Positive excursions

For `1<=s<=r-1`, set

```text
y_s=s+s*n/r=s(N+1)/r.
```

If `S_s-s*n/r > W`, then `B_s>y_s+W`. Let `x_+=floor(y_s+W)`. If `x_+>=N` the event is impossible; otherwise it implies `H_{x_+}<=s-1`.

Using `x_+>=y_s+W-1` and

```text
y_s K/N - s = -s n/(rN),
```

we obtain

```text
E H_{x_+}-(s-1) > (W-1)K/N.
```

For `r>=16` and `n=n_r`,

```text
n_r<=beta*r-8,
N=n_r+r-1 < alpha*r,
K/N=(r-1)/N > (r-1)/(alpha*r) > 1/2.
```

Also `W>=3`. Therefore the required downward deviation is `>W/3`, yielding

```text
P(S_s-s*n/r > W | S_r=n)
<= exp(-W^2/(18N)).
```

### 3.5 Negative excursions

If `s*n/r-S_s > W`, then `B_s<y_s-W`. Put

```text
x_-=ceil(y_s-W)-1.
```

If `x_-<1` the event is impossible; otherwise the event implies `H_{x_-}>=s`. Exact algebra gives

```text
s-EH_{x_-}
> s n/(rN)+W K/N
>= W K/N
> W/2.
```

Thus the negative side is stronger; using the same weaker common constant gives

```text
P(s*n/r-S_s > W | S_r=n)
<= exp(-W^2/(18N)).
```

### 3.6 Boundary times and union bound

At `s=0` and `s=r`, the centered displacement is exactly zero. Therefore only the `r-1` interior times contribute. Union-bounding both signs gives

```text
P(Bad_r | S_r=n)
<= 2(r-1) exp(-W^2/(18N)).
```

### 3.7 Frozen scale and exponent

With

```text
W_r=ceil(8*sqrt(r*ln(r+1))),
```

we have

```text
W_r^2 >= 64 r ln(r+1).
```

Since `N<alpha*r`,

```text
W_r^2/(18N)
> [32/(9 alpha)] ln(r+1).
```

The independently recomputed exponent is

```text
32/(9*log_2 3)=2.243305790476293...
```

which is strictly greater than `2`. Therefore

```text
P(Bad_r | S_r=n_r)
<= 2(r-1)(r+1)^(-32/(9 alpha)).
```

Multiplying by `r` gives an upper bound of order `r^(2-c)`, where

```text
c=32/(9 alpha)>2.
```

Hence

```text
r P(Bad_r | S_r=n_r) -> 0,
```

so

```text
P(Bad_r | S_r=n_r)=o(1/r).
```

### 3.8 Floor effects, domain and uniformity

The proof uses the exact integer `n_r` and only the valid inequality `n_r<=beta*r-8`. No replacement of `floor(beta*r)` by `beta*r` is needed.

Domain:

- `r=12,13`: `n_r<0`, so conditioning is impossible.
- `r=14,15`: `n_r=0`, feasible but degenerate.
- `r>=16`: first nondegenerate regime; the quantitative theorem applies directly.

All constants are independent of `r`. The estimate is therefore uniform along the entire frozen integer sequence `r>=16`.

## 4. Exact accepted theorem

**E7R-B2 [PROVED].** Let

```text
alpha=log_2 3,
n_r=floor((alpha-1)r)-8,
W_r=ceil(8*sqrt(r*ln(r+1))),
Bad_r={max_{0<=s<=r}|S_s-s*n_r/r|>W_r}.
```

Then for every integer `r>=16`, under the frozen conditioned iid-geometric bridge,

```text
P(Bad_r | S_r=n_r)
<= 2(r-1) exp[-W_r^2/(18(n_r+r-1))]
<= 2(r-1)(r+1)^(-32/(9 log_2 3)).
```

Consequently

```text
P(Bad_r | S_r=n_r)=o(1/r).
```

## 5. Scope and downstream status

- E7R-B1 is accepted as **[PROVED]**.
- E7R-B2 is accepted as **[PROVED]**.
- B1 quantitative holonomy remains **[OPEN]**.
- B2 arithmetic mixing remains **[OPEN]**.
- B3 frozen pointwise contraction remains **[OPEN]**.
- Therefore E7R-B4 / E6-N2 is **not proved**.
- E7R-B5 and E7R-B6 remain open.

This audit authorizes acceptance of E7R-B1 and E7R-B2 only. It does not begin B3, weighted-operator work, or E8.

Nothing in this audit proves the Collatz conjecture.

## FINAL ADJUDICATION

`[AUDIT PASS]`
