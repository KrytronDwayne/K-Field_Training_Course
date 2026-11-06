# Lesson 4 — Direct and inverse metrics

**Essential question:** When can a metric be reversed, and what does the reversal act on?

**Goals.** Verify an inverse by multiplication; use the analogue's block structure for hand inversion; check B_ex R_ex B_ex^T=I; distinguish inverse metric from reciprocal basis and coordinate recovery.

## Bridge

Lesson 2 taught row-column multiplication; Lesson 3 taught the nonzero-volume test. Now we reverse operations. Dividing by 2 reverses multiplying by 2. A matrix inverse reverses a matrix map, provided the map has not collapsed distinct inputs together.

The **identity matrix** I=[[1,0,0],[0,1,0],[0,0,1]] leaves each triple unchanged. An inverse T^−1 satisfies TT^−1=T^−1T=I. A square basis has an inverse exactly when its determinant is nonzero. The planar counterexample in Lesson 3 has no inverse: it cannot reconstruct an arbitrary z component.

M_cell=B^T B acts on cell-coordinate triples in a length calculation. R_cell=M_cell^−1 is the inverse metric. For the classroom analogue we use M_ex and R_ex instead. If B has length units, M has length² and R has length^−2. Neither R by itself nor M by itself converts an external position into cell coordinates. That conversion is q=B^−1(x−O_K).

## Worked example — Classroom analogue, not Cell3

The third coordinate of M_ex is independent of the first two. Its inverse factor is 1/9. To invert the top-left block, solve

u+v=s,   u+5v=t.

Subtract the first equation from the second: 4v=t−s, so v=−s/4+t/4. Then u=s−v=5s/4−t/4. These coefficients are the rows of the inverse block. Therefore

R_ex=L^−2 [[5/4,−1/4,0],[−1/4,1/4,0],[0,0,1/9]].

Verify every entry of M_ex R_ex. The upper block is

```
1(5/4)+1(-1/4)=1      1(-1/4)+1(1/4)=0
1(5/4)+5(-1/4)=0      1(-1/4)+5(1/4)=1
```

The third diagonal entry is 9(1/9)=1. All entries coupling the third coordinate to the others are zero. Units L²L^−2 cancel. The reverse product is also I: its upper block entries are 5/4−1/4=1, 5/4−5/4=0, −1/4+1/4=0, −1/4+5/4=1, with third diagonal 1.

Next, multiply B_ex R_ex. Its numerical rows are [1,0,0], [−1/2,1/2,0], [0,0,−1/3], with units L^−1. Multiply by B_ex^T=L[[1,0,0],[1,2,0],[0,0,−3]]. The first row gives [1,0,0]; the second gives [−1/2+1/2,1,0]=[0,1,0]; the third gives [0,0,1]. Thus B_ex R_ex B_ex^T=I exactly.

This second identity acts on external Cartesian vectors. Its units are L·L^−2·L=1. For any invertible square B, the reverse of B^T B is B^−1(B^T)^−1: undo the last operation first. Multiplying B on the left and B^T on the right cancels the reverse operations, leaving I. This is ordinary Euclidean geometry for an invertible basis; it does not assert that every separately defined phase metric equals I.

## Reciprocal basis and reconstruction

The columns of D=B R=(B^−1)^T form the **reciprocal basis**. A reciprocal column dotted with the corresponding direct edge gives 1 and with the other two gives 0. In our example d_1=(1,−1/2,0)/L, d_2=(0,1/2,0)/L, d_3=(0,0,−1/3)/L. For example d_1·b=1−1=0 and d_2·b=1. Thus q=D^T(x−O_K). This agrees with B^−1(x−O_K).

For displacement d=(3,2,−3)L, these three dot products give q=(2,1,1). Reconstruct B_ex q=2a+b+c=(3,2,−3)L. The residual d−B_ex q=(0,0,0)L is retained even when zero. The reciprocal basis has L^−1 units; its Gram matrix D^T D=R has L^−2 units. They are different objects.

> **Claim scope.** Exact fractions establish the analogue identities. Stored Cell3 decimals yield finite-precision checks in Lesson 6. R_cell, reciprocal basis D, G_phase, G_eff, and later distance quantities Q, Q_g, Q_nu are separately typed objects. This course neither defines those later distance functions nor substitutes them for M_cell.

## Guided practice and diagnostic checks

1. Compute entry (2,1) of M_ex R_ex, showing units.
2. Verify the (2,1) entry of B_ex R_ex B_ex^T from the intermediate matrix above.
3. Recover q from d=(1,4,−6)L, then reconstruct d.
4. Why is the zero-volume example outside the inverse identity's domain? What units distinguish D from R_ex?

## Worked answers

1. [1(5/4)+5(−1/4)]L²L^−2=0.
2. (−1/2,1/2,0)·(1,1,0)=0, with reciprocal-length times length canceling.
3. q=(1−4/2,4/2,(−6)/(−3))=(−1,2,2). −a+2b+2c=(1,4,−6)L, residual zero.
4. Independent inputs collapse onto one plane, so no unique inverse exists. D has L^−1 units and R_ex has L^−2 units.

**Next dependency:** [Lesson 5](lesson-05.md) asks what remains unchanged when all edges are scaled together.
