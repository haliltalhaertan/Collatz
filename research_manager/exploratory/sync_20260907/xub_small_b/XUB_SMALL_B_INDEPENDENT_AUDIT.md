# Independent audit of the XUB small-b reduction

Date: 2026-09-07

Verdict: `[PASS WITH MINOR DOMAIN AND WORDING REPAIRS]`.

The audit independently re-derived the pair operator, the general contraction-deficit identity, the `b=0,...,4` difference sets, the equality set, the uniform contraction estimate, the black-to-black lemma, the `9^L` divisibility conclusion, and conductor amplification. No missing factor, frequency, power of three, or direction-of-implication error was found.

Required repairs incorporated into the primary note:

1. Since `z=2^(x-beta)>0`, the equality set is `z in Z_(>0)`, not merely an unqualified integer set.
2. The black set uses strict inequalities: `dist(z,Z)<eta` and `eta<1/(9+2^(B+2))`. Equality at the threshold is not covered.
3. `E,D` in `z=2^E/3^D` are nonnegative integers. On the actual original boundary starts, `E=t+floor(beta*t)+1` and `D=t`.
4. “Positive-black run” means an eta-black run whose initial nearest integer satisfies `n_0>=1`; it does not mean merely that the pair symbols are positive.
5. The displayed distance condition is a consequence of the divisibility statement; no converse is claimed.

The exact combined lemma is:

Let `B>=0`, `L>=1`, and `0<eta<1/(9+2^(B+2))`. Suppose

`z_(j+1)=2^(b_j+2)z_j/9`, `0<=b_j<=B`,

and `z_0,...,z_L` are all eta-close to integers. If `n_j` is the unique nearest integer to `z_j`, then

`9^L divides n_0`

and

`n_L=2^(sum_j(b_j+2))n_0/9^L`.

If `n_0>=1` and `z_0=2^E/3^D`, then for `n_0=9^L h`,

`|2^E/3^(D+2L)-h|<eta/9^L`.

The audit validates only this deterministic implication. It does not establish conditioned rarity, white occupation, XUB, E6-N2/B4, or Collatz.

