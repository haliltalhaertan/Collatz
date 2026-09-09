# Exact all-black criterion for a consecutive B=1 word

Fix 0<eta<=1/17, z>0 and L>=1. Along L consecutive pair totals B=1, the entry phases are z_i=(8/9)^i z, 0<=i<L. Black means dist(z_i,Z)<eta; white means distance at least eta.

Then all L entries are black if and only if

dist(z,9^(L-1) Z)<eta.

Proof: If every entry is black, its nearest integer m_i is unique, and

|8m_i-9m_(i+1)|<17eta<=1.

This is an integer, hence zero. Since gcd(8,9)=1, m_0=9^(L-1)h and m_i=8^i9^(L-1-i)h for an integer h. This gives |z-9^(L-1)h|<eta. Conversely, writing z=9^(L-1)h+e with |e|<eta yields integer centers 8^i9^(L-1-i)h and errors (8/9)^i e, all strictly smaller than eta.

In particular, eta<=z<=9^(L-1)-eta forces at least one white entry. The inclusive boundary and L=1 case follow from the strict definition of black. For positive z, an entirely black word therefore has either z<eta (h=0), or proximity to a positive multiple of 9^(L-1).

For the actual G first-crossing-at-one suffix, z_0=16/9, and at pair index j,

z_j=2^(4+2j+H_j)/9^(j+1),

where H_j is the preceding pair-total sum. Thus an L-long B=1 word is entirely black exactly when, for some h>=0,

|2^(4+2j+H_j)-h*9^(j+L)|<eta*9^(j+1).

The initial phase has distance 2/9 from the nearest integer and is white for our eta, so the first pair contributes a mark if it is B=1. This is one opportunity, not a growing abundance theorem. Coprimality excludes exact positive equality in the displayed integer difference but only supplies a lower bound of one; it does not exclude the growing near-resonance window. This deterministic criterion does not prove a frequency estimate or the direct dense Laplace bound.
