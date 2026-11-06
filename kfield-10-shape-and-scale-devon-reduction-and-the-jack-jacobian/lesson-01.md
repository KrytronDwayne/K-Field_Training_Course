# Lesson 1 — Logarithms as ratio coordinates

Essential question: How can multiplication become addition without losing the original areas?

Goals: convert positive ratios to logarithms; reconstruct areas from logs and a reference; distinguish physical scaling from changing the reference.

Bridge: You already multiply fractions, use powers, and solve equations. A face is the parallelogram spanned by two edges. Its area scales by the product of their length factors when their included angle stays fixed. Doubling both edges therefore multiplies area by four. We use signed numbers to record decreases as well as increases.

## C10.01-E1 — A coordinate for multiplication

The exponential function exp(x), also written e^x, extends powers of the positive number e (approximately 2.71828) to real exponents. It satisfies exp(x+y)=exp(x)exp(y), exp(0)=1, and always has positive output. The natural logarithm ln is its inverse: ln(r) is the unique exponent whose exponential is r. Thus exp(ln r)=r for r>0 and ln(exp x)=x. A negative log means a positive ratio below one; it does not mean a negative area.

We can work exactly without a calculator. Write L=ln 2. Then exp(L)=2, exp(2L)=4, ln(1)=0, and ln(1/2)=-L. Since multiplication of exponentials adds exponents, ln(rs)=ln r+ln s. Division subtracts: ln(r/s)=ln r-ln s. These rules require positive r,s. We do not use ln(r+s)=ln r+ln s: for r=s=1 the left side is L and the right side is zero.

An area has units. First choose ONE positive reference area A0 in the same units as all three faces. For example A0=1 LU², where LU means a declared laboratory length unit in our synthetic examples. Define the ordered triple

    y=(ln(A_ab/A0), ln(A_ac/A0), ln(A_bc/A0)).

The subscripts name faces, and the order is always [ab,ac,bc]. Each quotient and each log is dimensionless. A triple is simply three ordered numbers; its first entry is not interchangeable with its third. Inversion is component by component: A_ab=A0 exp(y_ab), and similarly for ac and bc. Store A0 with y.

If all edge lengths are multiplied by a positive factor rho at fixed angles, all areas multiply by rho². Thus every y entry increases by 2 ln rho. If instead the physical areas stay fixed and A0 changes to k A0, every y entry decreases by ln k. These operations can look similar in coordinates, but their physical records differ.

## C10.01-W1 — Worked synthetic example

Let A/A0=(1,4,8). The logs are y=(0,2L,3L), since 4=2² and 8=2³. Double all edges: rho=2, so the new area ratios are (4,16,32). Adding 2L to every old entry gives (2,4,5)L, agreeing with those powers of two. Reconstruct the original third face: A_bc=A0 exp(3L)=8A0. Both the old and new triples remain available.

## C10.01-P1 — Practice before checking the answer

Use A/A0=(2,4,16). Find y, halve every edge, find the new areas and logs, then reconstruct all original ratios. Also change only the reference to 4A0 and explain what changed physically.

Answer: y=(1,2,4)L. Halving edges multiplies areas by 1/4, giving (1/2,1,4)A0 and logs (-1,0,2)L. Applying exp to the original entries gives (2,4,16). Changing only the reference to 4A0 gives the same numerical log triple (-1,0,2)L, but the physical areas remain (2,4,16)A0 because the reconstruction reference is now 4A0. Record which operation occurred.

> Claim scope: The log laws are mathematical identities. All numerical areas here are synthetic. S02#/backbone_sequence/6 uses dimensional-log shorthand; the common A0 makes its intended ratio coordinates explicit, following SA-10. No measurement or force law is inferred.

## Diagnostic checks — C10.01-D1

1. Can a zero area be represented by a finite real log? What about a negative area?
2. What is ln(8/4), and why?
3. If A0 is replaced by 4A0, what happens to y_ac-y_ab?
4. A report stores y but omits A0. What can and cannot be recovered?

Worked answers: (1) Neither is in the positive domain; exp never gives zero or a negative value. (2) ln 2=L, also 3L-2L=L. (3) Each entry loses 2L, so their difference is unchanged. (4) Ratios between faces follow from exp(y_i-y_j). Absolute dimensional areas require the reference.

Next: [Lesson 2](lesson-02.md) separates the common shift from differences. Pacing: 55 minutes = 5 retrieval + 20 teaching/example + 15 practice + 15 diagnostics/repair.
