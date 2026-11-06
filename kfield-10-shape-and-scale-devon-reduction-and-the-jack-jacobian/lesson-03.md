# Lesson 3 — Linear response and small changes

Essential question: When does reversing a coefficient map differ from reversing a finite physical change?

Goals: apply and invert a two-variable matrix; identify a tangent coefficient; calculate and preserve a finite remainder.

Bridge: A dot product multiplies corresponding entries and adds. A matrix is a rectangular table whose rows do that calculation to an input column. We will start with two inputs before the three-input Jack map.

## C10.03-E1 — Exact linear maps and local predictions

Let H have rows (1,1) and (1,-1). Applied to input (p,q), its output is (h,k)=(p+q,p-q). Add the two output equations: h+k=2p. Subtract them: h-k=2q. Hence p=(h+k)/2, q=(h-k)/2; the inverse table is H/2. An inverse is a rule that restores every permitted input, not just a remembered example. Substitution gives ((p+q)+(p-q))/2=p and ((p+q)-(p-q))/2=q.

This linear map is exact for any real p,q. A *Jacobian* is a table of such response coefficients at a stated starting point for a possibly nonlinear map. To understand 'local', use a dimensionless change parameter t, initially zero. If f(t)=f(0)+ct+R(t), and R(t)/t approaches zero as nonzero t approaches zero, c is the derivative or tangent coefficient at zero. The predicted change is ct. This definition compares the remainder with the change parameter; it does not authorize throwing R away. Here our polynomial examples let us check it by division.

For example, (1+t)(1+2t)=1+3t+2t². The change from its initial value 1 is 3t+2t². Its tangent part is 3t because (2t²)/t=2t approaches zero. At any specified nonzero t, retain the exact remainder 2t². The exact output is recovered as baseline + tangent prediction + remainder. This is a finite synthetic product model, not a measured cell response.

For a positive length l(t)=l0(1+ct), the exact log change is ln(l(t)/l0)=ln(1+ct). Its tangent is ct at t=0 (the local log rule ln(1+h)/h approaches 1). This is a supplied elementary log property; a general calculus proof is not needed for the computations. The symbol dln l denotes this first-order change, not the exact percentage or the finite log. Keep ln(1+ct)-ct when comparing them. For a log-defined path l(t)=l0 exp(ct), the log change is exactly ct, a different path that must be declared.

## C10.03-W1 — Worked synthetic examples

Input (2t,t) goes through H to (3t,t). Applying H/2 returns ((3t+t)/2,(3t-t)/2)=(2t,t). This reversal has zero residual for every t.

Separately, at t=1/10 the product (1+t)(1+2t)=1.1 times 1.2=1.32. Change=0.32, tangent=0.30, remainder=0.02. Reconstruct 1+0.30+0.02=1.32. Halving t to 0.05 gives remainder 2(0.05)²=0.005; it becomes smaller but remains part of the record.

## C10.03-P1 — Practice

Apply H to (t,-2t) and invert. For the separate square model (1+t)², find exact change, tangent, remainder at t=0.1, and the exact log change. Find the log remainder for a single 10% increase and retain its sign.

Answer: H(t,-2t)=(-t,3t); inverse gives ((-t+3t)/2,(-t-3t)/2)=(t,-2t). Expansion gives 1+2t+t²: change 0.21, tangent 0.20, remainder 0.01. The exact square log change is 2ln(1.1), approximately 0.19062036, not 0.20. For a single increase it is ln(1.1), approximately 0.09531018; subtracting 0.1 gives approximately -0.00468982. These decimals are calculator approximations; the exact logarithmic expressions retain all information.

> Claim scope: H and the product/square are declared classroom models. They explain what 'tangent' means before the source map. A small finite remainder is preserved, not erased by a tolerance or a label.

## Diagnostic checks — C10.03-D1

1. Is ln(1.1)=0.1? 2. If H has input (3,2), recover it from its output. 3. In the product example, what is R(t)/t? 4. Does zero linear inverse residual imply zero nonlinear remainder?

Worked answers: (1) No; the retained difference is ln(1.1)-0.1. (2) Output (5,1); ((5+1)/2,(5-1)/2)=(3,2). (3) 2t for t nonzero; it approaches zero. (4) No. The inverse tests a coefficient map, while the remainder tests a finite approximation; they answer different questions.

Next: [Lesson 4](lesson-04.md) names the source inputs and outputs before using a Jacobian. Two periods, each 5 retrieval + 20 teaching/example + 15 practice + 15 checks: first exact two-variable maps, then local versus finite changes.
