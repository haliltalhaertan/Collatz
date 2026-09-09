# Stratifying all prefix weights: exact moment bound and surviving ceiling

2026-09-08. Independent proposal, then adversarial rejection as a route past the current exponent ceiling. No paid calls. This keeps all prefix-weight strata; it does not assume independent continuation bits.

## Finite inequality

Consider odd 1<=x<2^m whose first m shortcut parity bits have weight k, and following t bits weight j. Write

    2^m y=3^k x+C, y=H^m(x), E=C/2^m.

For a parity word p of fixed weight k,

    E=sum_(i=0..m-1) p_i 2^(i-m) 3^(k-S_(i+1)).

Under uniform counting on ALL binary m-bit words of weight k, set p=k/m and

    q_theta=2^(-theta)*(1-p+p*3^theta), 0<theta<=1.

Fractional-power subadditivity, dropping the indicator p_i, and the sampling-without-replacement product-mean inequality give

    average E^theta <=2^(-theta)*sum_(h=0..m-1)q_theta^h = M_(m,k,theta).

For the product-mean inequality, assign k coordinates the value3^theta and the rest1. The average product of any h distinct coordinates is at most the h-th power of their arithmetic mean. This is the elementary symmetric mean inequality. It is used inside the already exposed m-bit block only.

Do NOT silently use this as a conditional moment on odd-start words: those fix the first bit to1. Instead the number of bad odd words is bounded by the number of bad words in the larger full weight class. Thus for any W>0,

    bad_count(E>W)<=binom(m,k)*M_(m,k,theta)*W^(-theta).

When E<=W, the affine relation puts all possible starts for a fixed y in an interval of length at most2^m W/3^k. There are binom(t,j) admissible endpoint residue classes modulo2^t and at most ceil(3^k/2^t) representatives per class, since1<=y<3^k. Therefore

    N_(m,t,k,j) <= min{binom(m-1,k-1),
       binom(m,k)*M_(m,k,theta)*W^(-theta)
       +binom(t,j)*ceil(3^k/2^t)*(ceil(2^m W/3^k)+1)}.

This inequality recovers the outlier strata rather than declaring every prefix outside a narrow window exceptional. It also respects mergers: the interval factor counts possibly multiple original starts per y.

## Exponent form

Put alpha=log_2(3), m=br+o(r), t=(alpha-b)r+o(r), k=sr+o(r), j=(1-s)r+o(r), W=2^(ur). The bad-offset term has exponent

    B_bad=b H_2(s/b)-theta*u+b*max(log_2 q_theta,0).

The good-offset term has exponent

    B_good=max(b-alpha*s+u,0)+max(alpha*s-(alpha-b),0)
           +(alpha-b)H_2((1-s)/(alpha-b)).

The finite sum in M contributes at most a polynomial factor even when q_theta=1. Taking the smaller of the prefix count and the sum bound yields exponent

    min{bH_2(s/b), max(B_bad,B_good)},

which may then be optimized over u and theta and maximized over feasible s. Endpoint weight strata can be handled separately; the following obstruction is at an interior stratum.

## The principal's fatal ceiling witness

Let s=b/alpha and H=H_2(1/alpha)=h_*/alpha. This is a feasible stratum. Even an oracle removing every bad-offset point and granting u<=0 leaves

    B_good >= (alpha-b)H+max(2b-alpha,0).

Its excess over the prefix exponent bH is

    (alpha-2b)H,          b<=alpha/2,
    (2b-alpha)(1-H),      b>=alpha/2,

both nonnegative. Allowing exponentially small offsets (u<0) does not change the conclusion: at this stratum b-alpha*s=0, and the interval-count factor is bounded below by one in the certificate.

Thus this stratified moment-plus-endpoint-cardinality bound still has optimized global envelope at least b*h_*/alpha. It cannot raise the orbit bridge ceiling beyond alpha/h_*. This is a limitation of this count certificate, not a lower bound for the true Collatz count.

The missing information is now particularly explicit. At the critical stratum, the prefix image is sparse inside an endpoint range of comparable exponential size. The tail condition is another sparse subset of that range. Counting either subset alone, even with a perfect bound on affine offsets, does not control their intersection better than the smaller marginal. A useful next estimate must quantify which tail residue classes the actual fixed-weight prefix image occupies; another global height or offset estimate does not supply that information.

## Adversarial checks

The attack agent independently accepted the hypergeometric moment argument and flagged the odd-start conditioning distinction, which is explicitly corrected above using binom(m,k). The principal independently supplied the ceiling witness and challenged whether negative u evades it; it does not. No numerical experiment or claimed new orbit exclusion is needed for the all-parameter ceiling calculation.
