"""Independent Fraction-based verification of the displayed compressed family."""
from fractions import Fraction as F
def path(a,b,steps):
    a,b=F(a),F(b)
    for _ in range(steps):
        assert a.denominator==b.denominator==1 and a%2==0
        a,b=(3*a/2,(3*b+1)/2) if b%2 else (a/2,b/2)
    return a,b
assert path(3456,20,7)==path(2592,20,5)==(243,2)
assert 3456%27==2592%27==0 and 20%27==20
assert 3456-2592==864
assert path(0,20,6)==(0,1)
print('PASS: exact shared affine endpoint, strict tail decrease, checkpoint membership, convergent base.')
