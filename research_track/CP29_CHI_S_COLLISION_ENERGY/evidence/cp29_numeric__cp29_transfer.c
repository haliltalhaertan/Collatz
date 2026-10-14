
#include <stdint.h>
#include <math.h>
// q is read-only qZ, x receives qX. 4^k visits all Z=1 mod3 exactly once.
void transfer(int64_t modulus, const double* prev, double* q, double* x) {
 int64_t L=modulus/3, phi=2*L, pow4=1;
 for(int64_t k=0;k<L;k++) {
    q[2*k]=prev[(pow4-1)/3]; q[2*k+1]=0.0;
    pow4=(4*pow4)%modulus;
 }
 double weight=.5, initial=0.;
 for(int64_t k=0;k<L && weight>0.;k++) {
    initial+=weight*q[2*k]; weight*=.25;
 }
 if(phi<1075) initial /= (1. - exp2(-(double)phi));
 x[phi-1]=initial;
 for(int64_t k=phi-2;k>=0;k--) x[k]=.5*(x[k+1]+q[k+1]);
}
void collect(int64_t modulus, const double* x, double* p, double* diagnostics) {
 int64_t L=modulus/3, phi=2*L, pow2=1;
 double mass=0., square=0., maxval=0., negmass=0.;
 for(int64_t k=0;k<phi;k++) {
    double v=x[k];
    if(v<0.) negmass-=v;
    mass+=v; square+=v*v;
    if(v>maxval) maxval=v;
    if(p) p[pow2]=v;
    pow2=(2*pow2)%modulus;
 }
 diagnostics[0]=mass; diagnostics[1]=modulus*square;
 diagnostics[2]=modulus*maxval; diagnostics[3]=negmass;
}
