# CP20_TASK8B3_E7R_LITERATURE_TRANSFER_V1 — PROJECT DEFINITIONS

Status: **FROZEN PROJECT NORMAL FORM; NO LITERATURE TRANSFER ADJUDICATED**

## Parameters

\[
\alpha=\log_2 3,\qquad \beta=\alpha-1,\qquad n_r=\lfloor\beta r\rfloor-8.
\]

Let \(Z_1,\ldots,Z_r\) be iid nonnegative geometric increments with

\[
\Pr(Z_i=j)=2^{-(j+1)},\qquad j=0,1,2,\ldots
\]

and

\[
S_s=Z_1+\cdots+Z_s.
\]

Define \(A_i:=Z_i+1\), so \(A_i\ge1\).

The canonical/unconditioned law is the iid law above.  
The microcanonical project law is the conditional law given \(S_r=n_r\).

## Exact microcanonical law

For a nonnegative vector \(z=(z_1,\ldots,z_r)\) with \(\sum_i z_i=n\),

\[
\Pr(Z_1=z_1,\ldots,Z_r=z_r)=2^{-(n+r)}.
\]

Hence, conditional on \(S_r=n\), all weak compositions of \(n\) into \(r\) parts are exactly equiprobable.

For \(1\le s\le r-1\),

\[
\Pr(S_s=j\mid S_r=n)
=
\frac{\binom{j+s-1}{s-1}\binom{n-j+r-s-1}{r-s-1}}
{\binom{n+r-1}{r-1}}.
\]

This is the accepted conditioned weak-composition bridge. No unconditioned Syracuse approximation replaces it.

## Conditioned phase observable

The accepted E6 representation uses

\[
G_{r,n}:=\mathbb E[F_{r,4}\mid S_r=n]
\]

with

\[
F_{r,4}
=
\zeta_4\prod_{s=2}^{r}p^{\rm fin}_{s,S_{s-1},4},
\qquad
\zeta_4=\exp(2\pi i/48).
\]

For \(s\ge2,j\ge0\), the analytic finite phase is

\[
p^{\rm fin}_{s,j,4}
=
\exp\!\left(2\pi i\,\frac{2^{s+j-5}}{3^s}\right).
\]

When \(s+j-5\ge0\), this may be represented by the residue
\[
2^{s+j-5}\pmod{3^s}.
\]

When \(s+j-5=-t<0\), modular inversion alone is not the analytic phase. Let
\(\rho=(2^t)^{-1}\pmod{3^s}\) and \(2^t\rho=1+h3^s\). Then the exact identity is

\[
p^{\rm fin}_{s,j,4}
=
\exp(2\pi i\rho/3^s)\exp(-2\pi i h/2^t).
\]

The negative-exponent cases for \(s\ge2,j\ge0\) are exactly
\[
(2,0),(2,1),(2,2),(3,0),(3,1),(4,0).
\]

A unified exact modulus/residue representation is
\[
M_s=2^{\max(0,5-s)}3^s,\qquad
R_{s,j}=2^{j+\max(0,s-5)}\pmod{M_s},
\]
with phase \(\exp(2\pi i R_{s,j}/M_s)\). For \(s=1,j=0\), \(M_1=48,R_{1,0}=1\), giving \(\zeta_4\).

For block rows in the later valid domain (in particular the accepted B3 block rows),
\[
q_{s,j}
=
\exp\!\left(
2\pi i\,\frac{2^{s+j-5}\bmod 3^s}{3^s}
\right).
\]

## Exact block kernel

For feasible \(0\le u\le v\le r\), endpoints \(k,\ell\), put \(m=v-u\), \(\Delta=\ell-k\).
For each weak composition
\[
x_{u+1}+\cdots+x_v=\Delta,\quad x_a\ge0,
\]
let \(t_u=k\) and \(t_s=k+\sum_{a=u+1}^{s}x_a\). Then

\[
K^{(4)}_{u,v}(k,\ell)
=
\sum_x\prod_{s=u+1}^{v}q_{s,t_{s-1}},
\]

\[
K^+_{u,v}(k,\ell)
=
\binom{\ell-k+v-u-1}{v-u-1}
\]

for feasible \(u<v\), and

\[
\mathcal K^{(4)}_{u,v}(k,\ell)
=
K^{(4)}_{u,v}(k,\ell)/K^+_{u,v}(k,\ell).
\]

The accepted boundary/totalization conventions from E7R-B1 remain in force.

## Stage-0 exact algebra verification

Define
\[
\theta_r:=\{\beta r\}.
\]

Because \(r\) is an integer and \(\alpha=\beta+1\),

\[
\{\beta r\}=\{\alpha r\}.
\]

Also
\[
\sum_{i=1}^{r}A_i=r+S_r.
\]

Under \(S_r=n_r\),

\[
\sum_{i=1}^{r}A_i
=r+n_r
=r+\lfloor(\alpha-1)r\rfloor-8
=\lfloor\alpha r\rfloor-8.
\]

Since \(\log_3 2=1/\alpha\) and
\(\lfloor\alpha r\rfloor=\alpha r-\theta_r\),

\[
(r+n_r)\log_3 2-r
=
-\frac{\theta_r+8}{\alpha}.
\]

Status of these identities: **[VERIFIED — PURE ALGEBRA FROM FROZEN DEFINITIONS]**.

Their relationship to Yuan Si's \(\Delta\) or entropy-line parameter is only:

**[CANDIDATE PARAMETER MATCH — NOT YET PROVED]**.

No M1–M8 literature mapping is adjudicated in Stage 0.
