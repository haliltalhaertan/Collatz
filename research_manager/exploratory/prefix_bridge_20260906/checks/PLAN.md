# Exploratory prefix bridge exact checks

Scope: new exploratory checks, not a continuation or rerun of any sealed E7/B4 source. No imports of producer code. These checks do not prove an asymptotic estimate.

Fixed cases, declared before executing the source: all positive compositions a=(1+z_1,...,1+z_r) with sum(z)=n, for r=4,...,8 and n=0,...,5, plus r=16,n=1. No adaptive additions, floating-point phase evaluations, or increased depth.

For every case compute B=sum_{j=1}^r 3^(r-j) 2^(a_1+...+a_{j-1}). Check with exact Fraction exponents:

1. CRT factorization e_(16m)(B)=e_m(uB)e_16(vB), m=3^r, u=16^-1 mod m, v=(1-16u)/m, including the integer Bezout equation.
2. B=3^(r-3) B_3 + 2^(a_1+a_2+a_3) B_tail.
3. The same concatenation identity at the level of exact rational phase exponents.
4. B mod 16 equals the first four summands modulo 16.
5. B mod 16 is constant when (r mod 4, min(a_1,4),min(a_2,4),min(a_3,4)) is held constant.
6. The correction e_16(vB) is never 1 (record violations).

Record failure witnesses, total paths, grouped residue keys, oddness, and actual residue values. Source and plan SHA-256 are emitted before the only execution. The output records UTC timing and both input hashes. This is honest local ordering provenance, not an independent external timestamp/seal or proof that a source has never previously run elsewhere.

Domain distinctions: at most 16 residue classes is not a claim of 16 exact-prefix classes. Exact positive prefixes are infinite across increasing total lengths; conditioning a tail depends on their exact sum as well as the residue class. Finite checks cannot establish uniform tail asymptotics or cancellation of aggregate coefficients.
