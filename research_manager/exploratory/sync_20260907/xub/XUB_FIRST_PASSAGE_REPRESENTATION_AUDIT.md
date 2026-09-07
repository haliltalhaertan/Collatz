# Independent audit of the XUB first-passage representation

Date: 2026-09-07

Verdict: **`[PASS WITH REQUIRED DOMAIN/SCOPE REPAIRS]`**

## Exact checks

- The strict first-crossing threshold is generally `c_s(a)=floor(beta*s-a)+1`. For the two actual starts the threshold is nonintegral, so this equals the candidate `ceil(beta*s-a)` and the displayed G/H formulas remain correct.
- The crossing increment `Y_s=c_s-J+e`, overshoot `X_s=eta_s+e`, and independence of `eta_s` from the pre-crossing index `J` are correct.
- Geometric memorylessness supplies exactly the factor `rho^(c_s-J)`; no extra `(1-rho)` or `rho` factor is missing.
- Starting the fictitious suffix at `a'_s=eta_s+beta` produces `eta_s+e` after its first increment. Therefore the suffix length is exactly `m-s+1` and the compensating multiplier is exactly `q(a'_s)^(-1)`.
- The unnormalised uniform-composition representation with prefix sum `U_s`, suffix sum `Z_(m-s+1,n-c_s)`, and denominator `N_(m,n)` is correct under the stated killing and phase-product convention.
- The G and H_0 threshold/overshoot formulas, the common reindex `t=r+1-ell`, and

  ```text
  k=floor(beta*r)-floor(beta*t)-14
  ```

  have no detected off-by-one error.
- The exact identity

  ```text
  2^(a')=2^(t+floor(beta*t))/3^(t-1)
  ```

  is correct.
- The bound `|B_s(a)|<=P_a(tau_0=s)` is exact.

## Binding repairs

1. Use `floor(beta*s-a)+1` in any general statement; `ceil` alone mishandles an integral strict-crossing threshold.
2. State the boundary-start ratio estimate only on coupled accessible arrays where `p_l(x,b)>0`, not for arbitrary independent continuum `x,b` in compact sets.
3. The boundary-start `O(1/l)` complex ratio is a new arithmetic hypothesis, not a consequence of BLL/KUB.
4. Treat the finitely many short suffix/endpoint cases separately when using the convolution estimate.

With the repaired sufficient hypothesis,

```text
P(tau_0=s)=O(s^(-3/2)),
p_l(x,b)=O(l^(-1/2)),
p_m(a,b_r)>=c*m^(-1/2)
```

give

```text
sqrt(m)*sum_s s^(-3/2)*(m-s+1)^(-3/2)=O(1/m)
```

after the endpoint pieces are separated. Thus the proposed local boundary-start estimate really would imply XUB, but it has not been proved.

Classification:

- Exact first-passage/memoryless representation: **`[PROVED / AUDITED]`**.
- Common G/H boundary-start triangular array: **`[PROVED / AUDITED]`**.
- Boundary-start complex `O(1/l)` estimate: **`[OPEN]`**.
- XUB: **`[OPEN]`**.
- E6-N2/B4, nonzero profile, polynomial lower bound, Collatz: **`[OPEN / NOT PROVED]`**.
