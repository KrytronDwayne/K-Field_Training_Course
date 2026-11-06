# Lesson 1 — Address coordinates and physical points

**Essential question:** How can an address describe a point when the three address directions are tilted or differently scaled?

**Goals:** Convert an address to a physical point; recover an address by undoing three component equations; distinguish dimensionless coordinates from lengths.

**Bridge from course-03:** You need signed arithmetic, fractions and solving one-variable linear equations. A vector is an ordered triple; adding vectors means adding corresponding entries. We review column multiplication and inverse action here, so no remembered matrix formula is needed. A physical coordinate triple uses perpendicular reference axes; our address directions need not be perpendicular.

## C04.01-E1 — Build a point from three displacements

Imagine giving walking instructions from a chosen starting point. Each address entry tells how much of one allowed step to take. A negative entry means moving in the opposite direction. Fractions mean partial steps. The starting point matters just as much as the steps.

Our **classroom analogue, not Cell3 and not measured data**, uses an arbitrary length unit, written LU. The origin is O=(2,-1,4) LU. Its ordered step vectors are a=(1,0,0) LU, b=(1,2,0) LU and c=(0,0,-3) LU. Write these as columns of a matrix:

```text
        [1  1   0]
B =     [0  2   0] LU,       O = (2,-1,4) LU.
        [0  0  -3]
```

An address q=(q1,q2,q3) is dimensionless. Column multiplication means Bq=q1 a+q2 b+q3 c. First scale each column by its address entry, then add the results. The physical point is **x=O+Bq**, or component by component:

```text
x1 = 2 + q1 + q2
x2 = -1 + 2q2
x3 = 4 - 3q3                     (physical entries measured in LU)
```

This map is called *affine*: it combines a linear displacement rule with a fixed starting point. If x is given, first form d=x-O. Solve d2=2q2 and d3=-3q3, then d1=q1+q2. Thus q2=d2/2, q3=-d3/3 and q1=d1-d2/2. Every d gives exactly one q, so B is invertible. Its inverse means precisely this undoing operation:

```text
         [1  -1/2   0]
B^-1 =   [0   1/2   0] LU^-1,     q=B^-1(x-O).
         [0    0   -1/3]
```

Inverse length times length yields a dimensionless address. A superscript -1 on a matrix means inverse, not taking the reciprocal of every entry. Since this triangular matrix has determinant 1×2×(-3)=-6 LU³, its orientation is reversed relative to the reference axes. A negative determinant does not prevent inverse action; zero would. Determinants are a recognition bridge here, not a required new calculation method.

## C04.01-W1 — Fully worked conversion and return

Take q=(1/2,-1/2,1). The scaled columns are (1/2,0,0), (-1/2,-1,0), and (0,0,-3) LU. Their sum is (0,-1,-3) LU. Adding O gives **x=(2,-2,1) LU**.

To return, subtract O: d=(0,-1,-3) LU. Then q2=-1/2, q3=1, and q1=0-(-1/2)=1/2. Both directions recover the starting quantities. This two-way check catches an omitted origin or a mistaken sign on c.

## C04.01-P1 — Guided practice, then check

Use q=(1,0,-1). Compute Bq, then x, then recover q from x. Before reading the answer, predict whether the third physical coordinate will exceed the origin's third coordinate.

**Worked answer:** Bq=(1,0,3) LU because -1 times c points upward. Therefore x=(3,-1,7) LU. The displacement is (1,0,3); q2=0, q3=-1, q1=1. The third coordinate exceeds 4 LU.

> **Claim scope and source interface:** The numerical B and O above are synthetic teaching inputs. For actual Cell3, B denotes the mature source-locked ICRS columns [a b c], with an intentional negative determinant; the declared physical origin is O_K. The same affine identity reads q=B^-1(x-O_K). We do not substitute these toy lengths for the source's nm values. Source: S02 `/proof_contract` and `/backbone_sequence/1/definitions`; see [source register](sources.md).

## Diagnostic checks

1. **C04.01-D1:** At x=O, what is q? Why is B^-1 O not the answer?
2. At q=(0,1,0), find x. Does one step along b change only the second physical coordinate?
3. Recover q for x=(2,1,4) LU.
4. A student writes “q has units LU.” Identify the unit cancellation that corrects this statement.

**Worked answers:** (1) x-O=0, so q=0. Using O alone fails to measure displacement from O. (2) x=O+b=(3,1,4) LU; both first and second physical entries change. (3) d=(0,2,0); q2=1, q3=0, q1=-1, so q=(-1,1,0). Substitution gives (2,1,4). (4) B^-1 has units LU^-1 and x-O has LU; their product is dimensionless.

**Pacing:** 20 minutes explanation/worked example, 15 practice, 15 diagnostics and feedback, 5 transition.

**Next dependency:** [Lesson 2](lesson-02.md) separates a full address into its integer cell owner and retained local coordinate.
