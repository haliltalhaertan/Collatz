# Next analytic direction

The earlier question 'could a smaller fixed positive logarithmic coefficient repair the origin-grid marked-Laplace bound?' is now answered NO by ALL_LOG_COEFFICIENTS_PROOF.md. Do not spend further calls attempting to prove that helper bound. The separately audited shorter-scale corollary extends the obstruction above sqrt(log R), but does not settle scales at or below that size.

Return to the denser pair-opportunity count from the exact pair-averaging reduction. A focused candidate is N_white, counting EVERY pair entry with pair total B=1 and dist(z,Z)>=eta, rather than only the start of selected long blocks. For 0<eta<1/2, |A_1|=|cos(pi z)|<=exp(-lambda_eta) at such an entry, lambda_eta=-log(cos(pi eta))>0. A direct Laplace estimate for this dense count would still be a sufficient bound; it has not been proved here.

The exact recursion is an available analytic starting point. Let F_(R,K)(z)=E exp(-lambda N_white) for the uniform R-part composition law, z>0. For R>=3,

F_(R,K)(z)=sum_(b=0)^K p_(R,K)(b)
 * exp[-lambda*1_{b=1 and dist(z,Z)>=eta}]
 * F_(R-2,K-b)((4/9)*2^b*z),

p_(R,K)(b)=(b+1)*binom(K-b+R-3,R-3)/binom(K+R-1,R-1).

This follows by counting b+1 splits of the first pair and all remaining compositions. F_(1,K)=1 and F_(0,0)=1. For R=2, B=K deterministically and F_(2,K)(z)=exp[-lambda*1_{K=1 and dist(z,Z)>=eta}]. No numerical recursion was run.

The next bounded analytic question is to derive a valid estimate for this recursion on the actual arrays, or an obstruction that genuinely applies to the dense statistic. Arithmetic near-integer visits remain unresolved. Do not silently assume independent conditioned increments or infer a lower-tail bound from a large mean. A tail estimate requiring at least A log R opportunities with failure probability C/R would be a stronger sufficient condition; target the Laplace expectation directly instead of assuming that stronger condition is necessary.

Research stays exploratory; the closed B4 authorization is not reopened. OpenRouter cumulative spend remains $0.061356 of $2.00, with no calls dispatched this turn and none outstanding.
