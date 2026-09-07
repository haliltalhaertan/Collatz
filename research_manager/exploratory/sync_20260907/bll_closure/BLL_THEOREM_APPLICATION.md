# BLL closure by a shifted-lattice killed local-limit theorem

Date: 2026-09-07

Classification: **`[PROVED BY VERIFIED THEOREM APPLICATION]`** for the two actual fixed-start arrays only.

This note closes the positive killed-kernel estimate left open by `../kfb_audit/KFB_FEASIBILITY_AUDIT.md`. It does not prove the crossing estimate, the full PWE window, E6-N2/B4, a nonzero profile, a polynomial lower bound, or Collatz.

## 1. Project process and reflection

Let

```text
alpha = log_2(3), beta = alpha-1, rho = beta/alpha,
P(Y=k)=(1-rho)rho^k, k>=0,
X_t=a+sum_(i=1)^t (Y_i-beta),
tau_0=inf{t>=0:X_t>0}.
```

Reflect the walk: `R_t=-X_t`. Its iid increment is

```text
eta=beta-Y.
```

It has mean zero, variance `alpha*beta>0`, exponential moments near zero, and support

```text
{beta,beta-1,beta-2,...} subset beta+Z.
```

Because two support points differ by one, the maximal shifted-lattice parameters are exactly `(h,c)=(1,beta)`. The walk is in the normal domain of attraction with norming

```text
a_m=sqrt(alpha*beta*m).
```

Moreover, `tau_0>m` is precisely `R_t>=0` through the bridge. Since the actual terminal point is strictly positive after reflection, the project killed mass equals the weak nonnegative kernel `q_m^+`, not the strict-positive kernel.

## 2. Exact admissible endpoint match

Both families have

```text
b_r=-13-beta-theta_r, theta_r={beta*r},
y_r=-b_r=13+beta+theta_r in [13+beta,14+beta).
```

For `G`:

```text
m=r, x_G=-a_G=4+alpha,
y_r-x_G=8+theta_r=m*beta-n_r in m*beta+Z.
```

For `H_0`:

```text
m=r-4, x_H=-a_H=5*alpha,
y_r-x_H=12-4*alpha+theta_r=m*beta-n_r in m*beta+Z.
```

Thus the endpoints are exactly accessible in the moving coset `m*c+h*Z`. The irrationality of `beta` is not an obstruction: the cited theorem explicitly permits nonzero shifted-lattice parameter `c`. Starts are fixed and the targets remain in a fixed compact positive interval, so both are `o(a_m)` uniformly over the admissible triangular arrays.

## 3. Published theorem and BLL

Caravenna and Chaumont, *An invariance principle for random walk bridges conditioned to stay positive*, Electronic Journal of Probability 18 (2013), paper 60, Proposition 4.1, equation (4.5), treats the general maximal `(h,c)`-lattice case and gives, uniformly for accessible `x,y=o(a_m)`,

```text
q_m^+(x,y)
 = h(1-zeta)g(0)/(m*a_m) * V^-(x)V^+(y) * (1+o(1)).
```

Primary source: <https://doi.org/10.1214/EJP.v18-2362>  
Author-hosted PDF: <https://chaumont.pages.math.cnrs.fr/rpdfiles/carcha2.pdf>  
Preprint record: <https://arxiv.org/abs/1204.6148>

The renewal factors are finite at each fixed start and bounded on the compact terminal interval. Hence, uniformly on the two actual accessible arrays,

```text
p_m^0(a,b_r)=q_m^+(-a,-b_r)=O(1/(m*a_m))=O(m^(-3/2)).   (BLL)
```

The assertion is asymptotic. Any finite set of smaller admissible indices can be absorbed into the constant. `r=14,15` are accessible but degenerate (`n_r=0`); the first nondegenerate range begins at `r=16`.

## 4. Consequence for the complex killed bridge

The free endpoint mass is uniformly `p_m(a,b_r)>=c*m^(-1/2)` by the lattice local limit theorem, equivalently by the exact negative-binomial mass plus Stirling. The exact unit-modulus domination already proved in the project is

```text
|L_m^0(a,b_r)| <= p_m^0(a,b_r).
```

Therefore

```text
|K_m^0(a,b_r)|
 = |L_m^0(a,b_r)|/p_m(a,b_r)
 <= C*m^(-3/2)/(c*m^(-1/2))
 = O(m^(-1)).                                             (KUB)
```

Since `m=r` or `m=r-4`, this is also `O(1/r)` for the two fixed-start families.

## 5. Exact scope

- BLL: **`[PROVED BY VERIFIED THEOREM APPLICATION]`**.
- KUB for the two fixed starts and barrier zero: **`[PROVED]`**.
- Uniformity means accessible points satisfying `y-x in m*beta+Z`; it is not a continuum-theta assertion.
- The result does not cover the growing `j` starts in the full PWE window.
- It supplies only an upper bound for the killed part, not a complex coefficient or nonvanishing statement.
- The crossing contribution XUB remains **`[OPEN]`** and is now the first gap in this particular splitting route.

