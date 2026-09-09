# CP20 TASK 8B3 — E0 EXACT RECURSION V2

Define `M_r := 2^(-A_r) B_r mod 3^r`. If `m=a_(r-1)`, then

`B_r = 3 B_(r-1) + 2^(A_r-m)`,

hence

`M_r = 2^(-m)(3 M_(r-1)+1) (mod 3^r)`.

For `r>=2`, under uniform `W_(r,A)`,

`p_(r,A)(m)=C(A-m-1,r-2)/C(A-1,r-1)`.

Thus the conditioned Fourier recursion is

`phi_(r,A)(xi) = sum_m p_(r,A)(m) e_(3^r)(xi 2^(-m)) phi_(r-1,A-m)(xi 2^(-m) mod 3^(r-1))`.

For `r=1`, `W_(1,A)={{(A)}}` and the last-part composition formula is not used.
