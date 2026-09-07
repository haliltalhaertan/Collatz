# XUB exact first-passage reduction

Date: 2026-09-07

Status: exact algebraic reduction; XUB itself remains **`[OPEN]`**.

Let

```text
p(y)=(1-rho)rho^y,
q(x)=exp(2*pi*i*2^x),
X_t=a+S_t-beta*t,
tau_0=inf{t>=0:X_t>0}.
```

Write the free and killed unnormalised Feynman--Kac kernels as

```text
L_l(x,b)=E_x[prod_(u=0)^(l-1)q(X_u); X_l=b],
L_l^0(x,b)=E_x[prod_(u=0)^(l-1)q(X_u); X_l=b, tau_0>l].
```

## 1. First-crossing coordinates

For a first crossing at `s>=1`, define

```text
c_s(a)=floor(beta*s-a)+1,
eta_s(a)=a+c_s(a)-beta*s,
x_J=a+J-beta*(s-1).
```

The final crossing increment has the unique form

```text
Y_s=c_s(a)-J+e, e>=0,
X_s=eta_s(a)+e.
```

This strict-crossing definition is valid even if `beta*s-a` is an integer. For the actual starts it is never an integer, so `c_s=ceil(beta*s-a)` as well and `0<eta_s(a)<1`. Crucially, `eta_s` is independent of the pre-crossing endpoint index `J`.

Put

```text
A_s(a)=sum_J rho^(-J)L_(s-1)^0(a,x_J)q(x_J),
B_s(a)=rho^(c_s(a))A_s(a),
a'_s=eta_s(a)+beta.
```

Geometric memorylessness and one fictitious first suffix step give

```text
(1-rho)sum_(e>=0)rho^e L_(m-s)(eta_s+e,b)
=q(a'_s)^(-1)L_(m-s+1)(a'_s,b).
```

Therefore the exact crossing numerator is

```text
L_m^cross(a,b)
=sum_(s=1)^m B_s(a)q(a'_s)^(-1)L_(m-s+1)(a'_s,b),
```

with inaccessible suffix kernels understood as zero, and the conditional crossing term is

```text
R_m^0(a,b)=L_m^cross(a,b)/p_m(a,b).
```

Also, directly by triangle inequality and the meaning of the geometric tail,

```text
|B_s(a)|<=P_a(tau_0=s).
```

This representation collapses the infinite overshoot sum, but it does not produce a finite-state closure: an `O(m)` first-passage sum and a dense family of boundary starts remain.

## 2. Uniform-composition form

Let `N_(m,n)=binom(n+m-1,m-1)`. Let `Z_(l,k)(x)` be the free phase sum over weak `l`-part compositions of `k`, and let `U_s(a)` be the phase sum over prefixes that remain at or below the barrier before the crossing. Then

```text
R_m^0(a,b)
=N_(m,n)^(-1)
 * sum_(s:c_s(a)<=n) U_s(a)q(a'_s)^(-1)
   Z_(m-s+1,n-c_s(a))(a'_s).
```

The extra `+1` in the suffix length is the fictitious geometric step that merges the true crossing overshoot with the remaining composition.

## 3. Actual G and H_0 indices

For `G`, `m=r` and `a_G=-4-alpha`:

```text
c_s^G=6+floor(beta*(s+1)),
eta_s^G=1-{beta*(s+1)}.
```

For `H_0`, `m=r-4` and `a_H=-5*alpha`:

```text
c_s^H=6+floor(beta*(s+5)),
eta_s^H=1-{beta*(s+5)}.
```

With `ell=m-s`, both families share

```text
a'_(r,ell)=beta+1-{beta*(r+1-ell)},
k_(r,ell)=floor(beta*r)-floor(beta*(r+1-ell))-14.
```

Only `k_(r,ell)>=0` contributes. The prefix time is `s_G=r-ell` or `s_H=r-4-ell`.

Writing `t=r+1-ell` yields the exact root-of-unity identity

```text
2^(a'_(r,ell))=2^(t+floor(beta*t))/3^(t-1),
q(a'_(r,ell))=exp(2*pi*i*2^(t+floor(beta*t))/3^(t-1)).
```

Thus the boundary starts are not arbitrary continuum interpolation points, but their ternary conductors grow and their phases form a dense high-conductor triangular family.

## 4. Remaining estimate

Since `p_m(a,b_r) asymp m^(-1/2)`, XUB is equivalent to

```text
|sum_s B_s(a)q(a'_s)^(-1)L_(m-s+1)(a'_s,b_r)|
<=C*p_m(a,b_r)/m=O(m^(-3/2)).
```

A clean sufficient—not necessary—local target is

```text
|L_l(x,b)/p_l(x,b)|<=C/l
```

uniformly on the coupled accessible boundary-start arrays (so `p_l(x,b)>0`) with `x in [beta,beta+1]` and terminal `b` in the fixed project interval. It is not a statement for arbitrary independent continuum `x,b`. Together with `P(tau_0=s)=O(s^(-3/2))`, free local-limit scale `p_l=O(l^(-1/2))`, and separate endpoint treatment, this would yield the required convolution scale. This boundary-start complex estimate is presently **`[OPEN]`**.

No nonzero coefficient, E6-N2/B4 result, polynomial lower bound, or Collatz result follows.
