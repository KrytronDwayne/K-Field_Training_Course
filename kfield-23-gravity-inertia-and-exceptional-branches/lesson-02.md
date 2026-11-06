# Lesson 02 — Reciprocal inversion identities

Essential question: What must be retained to reconstruct a reciprocal direction, spacing and address?

Goals: Compute a reciprocal vector and its metric length; invert a conditional Bragg relation with its allowed angles; reconstruct a signed residual without losing components.

Prerequisite bridge. Lesson 01 taught reversible summaries and positive dimensionless logarithm ratios. Here a vector is an ordered list of three signed components. Multiplying vectors in the dot product means multiplying corresponding entries and adding: (a,b,c) dot (u,v,w)=au+bv+cw. A vector's Euclidean length is the nonnegative square root of its dot product with itself. A square root undoes squaring; sqrt(13)^2=13.

Pacing: three 55-minute periods, each with 5 retrieval, 20 instruction/example, 15 practice and 15 checks. Periods cover basis/metric, Bragg/angle branches, then residual and scale reconstruction.

## C23.02-E1 — Basis, reciprocal and metric

Let LU denote an arbitrary length unit. Our synthetic basis has columns a=(2,0,0), b=(0,3,0), c=(0,0,4) LU. The matrix B=diag(2,3,4) LU is shorthand for the array with these entries on its diagonal and zeros elsewhere. Multiplication B u scales the components of a dimensionless address u separately. Its inverse B^-1 divides them by 2,3,4. A transpose B^T exchanges rows and columns; a diagonal matrix is unchanged. B^-T means the transpose of B^-1. A basis is nonsingular when it has a unique inverse; this diagonal example qualifies because none of 2,3,4 is zero.

For a physical position x with declared origin O_K, u=B^-1(x-O_K), and x=O_K+B u. Subtract the origin first. The reciprocal columns a*,b*,c* are (1/2,0,0),(0,1/3,0),(0,0,1/4) LU^-1. They extract address components: a* dot (x-O_K)=u_1. For example, O_K=(1,1,1) LU and x=(3,4,5) LU give displacement (2,3,4) LU and address (1,1,1). Using x directly would give the wrong address (3/2,4/3,5/4).

The Gram metric M_cell=B^T B records dot products of the basis columns. In this synthetic analogue M_cell=diag(4,9,16) LU^2, and R_cell=M_cell^-1=diag(1/4,1/9,1/16) LU^-2. For an integer triple h (a plane address), define q=B^-T h. Then B^T q=h and

    q dot q = h^T R_cell h.

For this diagonal example the right side is h_1^2/4+h_2^2/9+h_3^2/16. This metric expression is just the same three squares computed from the address. In general the identity follows because q^T q=h^T B^-1 B^-T h, and B^-1 B^-T=(B^T B)^-1. The diagonal calculations are the assessed operation; general matrix inversion is not required.

For nonzero q, define d=1/length(q), a positive spacing in LU, and n_hat=q/length(q), a dimensionless unit normal. Then q=n_hat/d. Keep the signs of n_hat: d alone does not retain orientation. If q=0 there is no unit direction or finite d by this rule.

The source reciprocal branch (S02 /backbone_sequence/18/branches/reciprocal_plane_inversion) also supplies 2d sin(theta)=m lambda_wave. For the positive-sine angle convention and positive integer order m and wavelength lambda_wave, solve by dividing: d=m lambda_wave/(2 sin(theta)). The source absolute-value form extends the positive spacing convention to other angle branches; the original signed equation and its orientation must still be retained. Never divide by zero. Sine is the vertical coordinate of a unit-circle direction; the provided values sin(30 degrees)=sin(150 degrees)=1/2 suffice here. Angles theta and 180 degrees-theta have the same sine but distinct directions.

Using a common positive length reference L_ref, write Gamma_B=ln(d/L_ref)+ln|sin(theta)|-ln(lambda_wave/L_ref). Combine logarithms to get ln(d|sin(theta)|/lambda_wave)=ln(m/2). Gamma_B is dimensionless. It is distinct from Gamma2, G_Gamma and any metric. If adjacent linear scales satisfy d_next=3d, then ln(d_next/L_ref)-ln(d/L_ref)=ln 3. This does not declare that every signed reciprocal scale uses the same exponent: record whether q has 3^(+g) or 3^(-g).

## C23.02-W1 — Worked reconstruction

For h=(1,1,0), q=(1/2,1/3,0) LU^-1. Its squared length is 1/4+1/9=13/36 LU^-2. Thus length(q)=sqrt(13)/6 LU^-1, d=6/sqrt(13) LU and n_hat=(3,2,0)/sqrt(13). Check n_hat dot n_hat=(9+4)/13=1; dividing n_hat by d returns q. Also B^T q=(1,1,0). The metric gives the same 13/36.

In a **separate synthetic Bragg example**, m=2, lambda_wave=2 LU and sin(theta)=1/2 give d=4 LU. Both 30 and 150 degrees satisfy this spacing, with Gamma_B=ln(2/2)=0. This d does not belong to the preceding q: each reconstruction must use its own input packet.

## C23.02-P1 — Practice and answer

First set h=(0,0,1) using the same B. Then solve a separate Bragg example with m=1, lambda_wave=3 LU, sin(theta)=1/2. Finally use h=(1,1,0), g=0 and reciprocal residual rho=(1/10,-1/5,0) LU^-1 to reconstruct q_observed=3^g B^-T h+rho.

Answers: q=(0,0,1/4) LU^-1, squared length=1/16 LU^-2, d=4 LU and n_hat=(0,0,1). The Bragg spacing is 3 LU and Gamma_B=ln(1/2). In the residual case 3^0=1, so q_observed=(1/2+1/10,1/3-1/5,0)=(3/5,2/15,0) LU^-1. Subtract the prediction to recover rho exactly. Its negative second component is information, not a rounding instruction. The observed squared length is 9/25+4/225=17/45 LU^-2, giving d_observed=sqrt(45/17) LU; its normal must be calculated from that observed vector, not borrowed from W1.

> Claim scope. B here is a synthetic positive-determinant diagonal teaching basis, not the mature locked Cell3 numerical geometry. Actual Cell3 uses ICRS columns [a b c], intentional negative determinant and half-open address cells [-1/2,1/2)^3. Its origin and metric must be retained. This lesson changes none of those constants. M_cell and R_cell are not G_phase, G_eff, distance Q, Q_g or Q_nu. Bragg numbers here are conditional teaching inputs, not measured events.

## Diagnostics and worked answers

1. **C23.02-D1:** Can positive m lambda_wave and sin(theta)=0 give finite d? Answer: no, the original left side is zero and the right side positive. The inversion excludes that input.
2. What if B=diag(2,3,0)? Answer: its third address cannot be recovered from B u; the inverse does not exist. Zero q is a separate excluded case even for nonsingular B.
3. Why retain rho as three signed entries? Answer: q_observed=prediction+rho reconstructs every component; length(rho) alone cannot recover its direction or signs.
4. If d changes from 2 LU to 6 LU, find the log difference. Answer: ln(6/L_ref)-ln(2/L_ref)=ln 3 with a common LU-valued reference. A different reference in each term would contaminate the comparison.
5. Does knowing d select 30 rather than 150 degrees in W1? Answer: no, both sines are 1/2. Store the angle branch and normal orientation as well as spacing.

Next dependency: [Lesson 03](lesson-03.md) uses the unit normal for signed motion components.
