# Spherical response and phase addresses

Essential question: How can similar-looking formulas describe different operations?

Goals: Evaluate a finite response card; flag undefined branches before division; compute a reciprocal address without treating phase as force.

Prerequisite bridge. Lesson 01 taught unit vectors, dot products and radians. A normal is a vector perpendicular to a plane. The dot product with a unit normal measures the signed component along it. A zero dot product means the vectors are perpendicular. This lesson takes two periods: response and address first, domain and parity second.

## C29.02-E1 — Follow the contract of each map

An input-output rule needs a domain, units and a source. G03 is a historical Cell3 spherical-response construction. It is not the galaxy cell of G04. Here is the complete response card needed for our finite exercises:

| Symbol | Meaning and rule |
|---|---|
| n, N | unit direction and unit sheet normal |
| h | positive half-step sheet spacing, units L |
| nu | odd lock order, nu=2r+1 for integer r |
| u | n·N, dimensionless |
| kappa | nu π/(h u), units 1/L, defined only if u≠0 |
| q_resp | kappa n, reciprocal-length vector |
| s_ab,s_ac,s_bc | loop displacement vectors in L, with s_ac=s_ab+s_bc |
| psi_ij | q_resp·s_ij, a dimensionless radian phase |
| F | sqrt(3+2cos(psi_ab)+2cos(psi_ac)+2cos(psi_bc))/3 |
| D | sum over ab,ac,bc of w_ij[1-cos(psi_ij)], w_ij=abs(R_local,ij) |
| G_star | D/F, defined only when F≠0 and previous fields exist |

`sum` instructs you to add the three terms. The weights are nonnegative and inherit their units from the historical local reciprocal metric. F is dimensionless, so G_star has D's units. The source calls G_star an unscaled relative response; an absolute gravity calibration is undefined. Synthetic weights in this course use a declared relative response unit U_D, not a measured force unit.

The phases must respect loop closure: psi_ac=psi_ab+psi_bc before reduction by full turns. A cosine repeats after 2π. A supplied triple cannot be treated as geometrically realized merely because its three cosines can be evaluated. For a negative square-root argument, flag an inconsistent card or precision issue; do not silently replace it with zero.

G04 p4 has a different map. Its reciprocal vector q_j=n_j/Delta_j has length inverse to its plane spacing Delta_j. Points on plane k_j satisfy `q_j·x=k_j+phi_j`, where k_j is an integer and phi_j is the phase offset measured in **cycles**, not radians. Multiply cycles by 2π to express a radian phase. At a general point, q_j·x-phi_j need not be an integer. That difference is a continuous address, with its fractional component retained. We use q_resp and q_j to avoid a collision between the two source-local uses of q.

## C29.02-W1 — Worked example

Synthetic response: n=N=e_z, h=1L, nu=1. Then u=1, kappa=π/L and q_resp=(0,0,π/L). Choose loop displacements perpendicular to e_z and obeying closure, so all loop phases are zero. Since cos(0)=1, F=sqrt(3+2+2+2)/3=1. Each term in D is w(1-1)=0, hence D=0 and G_star=0 U_D.

Separately, a synthetic reciprocal row q₁=(1,0)/L acting on x=(5/4,0)L gives q₁·x=5/4 cycles. With phi₁=1/4, the plane label is k₁=1. The L units cancel. This is an address calculation, not a response or a force.

## C29.02-P1 — Domain practice and answers

Case A: n=e_x and N=e_z. Their dot product is zero, so kappa and q_resp are undefined. Save the input vectors and a `u_zero` flag with null response fields.

Case B: consider closure-consistent loop phases (psi_ab,psi_ac,psi_bc)=(2π/3,4π/3,2π/3). Their cosines are all -1/2, giving F=sqrt(3-1-1-1)/3=0. With all three weights 1 U_D, D=3(1+1/2)=9/2 U_D. G_star is undefined, with a `transfer_zero` flag. Even if a different card gave D=0 too, 0/0 would remain undefined. The blueprint's all-2π/3 triple is repaired here because it violates loop closure; this is an algebraic domain demonstration, not a replay of G03's frozen geometry.

Case C: a separately stipulated regular transfer has D=2 U_D and F=1/2. G_star=2/(1/2)=4 U_D. Keep its synthetic label.

> Scope and precision. G03#/precision_contract specifies IEEE-754 binary64 arithmetic, phase reduction to [-π,π), null undefined values and separate flags. These classroom calculations use exact symbolic angles; a numerical residual near zero is retained separately from an exact domain statement. No historical G03 coefficient replaces the mature S02 lock.

## Antipodal parity

Reverse n while keeping N fixed. Then u changes sign and kappa changes sign. Their product q_resp=kappa n keeps its value: two sign changes cancel. Thus loop phases, F, D and G_star are even under this antipodal operation where defined. “Odd” means sign-reversing; “even” means unchanged. This response parity does not identify antipodal sky positions or any other kind of parity.

## Diagnostics — C29.02-D1

1. A reciprocal row is (0,2)/L and x=(0,3/4)L. With phi=1/2, what is k?
2. Which fields fail first when u=0?
3. Does antipodal reversal change q_resp? Show the signs.
4. What is wrong with reporting G_star in newtons from this card?

Worked answers. 1. The dot product is 3/2; subtract 1/2 to obtain k=1. 2. Division by u makes kappa undefined, so downstream q_resp and phases are unavailable; retain all inputs. 3. (-kappa)(-n)=kappa n, unchanged. 4. No force calibration or force unit has been supplied; relative response and phase do not establish a force law.

Next: [lesson 03](lesson-03.md) combines reciprocal rows into one reconstructible address system.
