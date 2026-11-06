# Lesson 1 — An ordered cell in three dimensions

**Essential question:** How can three ordered arrows describe a cell without changing the external axes?

**Goals.** Read three columns as three labeled edges; map a coordinate triple to an external displacement; distinguish handedness from length and cell ownership.

## Bridge from course-02

In two dimensions, a coordinate pair tells how much of each basis arrow to add. A third component adds a third arrow by the same rule. You need signed addition, multiplication, and the distinction between a point and a displacement. This lesson supplies the three-dimensional bridge, so no previous matrix course is needed.

A vector is an ordered list of components along named axes. Write a=(a_x,a_y,a_z). Multiplying a by 2 doubles every component; adding vectors adds corresponding components. A point x has a location; x−O_K is the displacement from a declared origin O_K. Changing the origin changes this displacement, not the rule for adding vectors.

## Three columns, one mapping

A basis B=[a b c] is a rectangular table whose **columns** are the three edge vectors. Rows collect the x, y, and z components. A coordinate triple q=(q_1,q_2,q_3) tells how many copies of each edge to use:

x−O_K=Bq=q_1 a+q_2 b+q_3 c.

The q components are dimensionless counts when the edges carry length units. Independent edges reach all three spatial directions; coplanar edges do not form a three-dimensional basis. We will test independence with volume in Lesson 3.

For Cell3 the named external convention is **ICRS**, the International Celestial Reference System. Here we only need its role as a fixed set of external axes. Reading columns in ICRS does not permit exchanging axes or reflecting them. The column labels a, b, c are also fixed. A labeled cell and an unlabeled shape are different specifications.

## Worked example — Classroom analogue, not Cell3

Let L mean one arbitrary length unit. The numerical rows of B/L are

```
1   1   0
0   2   0
0   0  -3
```

Thus a=(1,0,0)L, b=(1,2,0)L, c=(0,0,−3)L. For q=(1,−1,2), add a−b+2c=(0,−2,−6)L. With O_K=(4,1,2)L, the point is x=(4,−1,−4)L. Subtracting the origin returns (0,−2,−6)L. Conversely, the second external component gives q_2=−2/2=−1; the first gives q_1=0−q_2=1; the third gives q_3=(−6)/(−3)=2. Nothing was lost.

In the xy view, a points right and b points right and up. The third edge points along negative z. This ordered arrangement has negative signed volume, called left-handed relative to the fixed axes. Lesson 3 calculates the sign. A negative sign is an orientation record, not a negative amount of space. Flipping c would change the cell specification.

## Reading the actual lock

The complete source-decimal card is in [geometry-card.md](geometry-card.md). Its first column, not its first row, is a=(0.3275012420558906, −0.0548970078840064, −0.0374875028947299) nm. A nanometre, nm, is 10^−9 metre. The source's determinant is −0.11791489191174465 nm³; its negative sign is intentional. Do not “repair” it.

For a centered cell, each coordinate belongs to [−1/2,1/2): the left endpoint is included and the right endpoint is excluded. All three coordinates must meet this condition. This assigns shared boundaries once. It is not an instruction to round a measured value or discard a residual. For translated cells, retain both the cell's integer address and its within-cell coordinates so reconstruction remains possible.

> **Claim scope.** The small integer basis is invented for teaching. Cell3 decimals and conventions are source facts from S02 `/mature_locked_cell3` and `/typed_conventions`, confirmed by S03 `/canonical_locked_values`. Their physical interpretation is not established by the classroom example. No empirical observations are introduced here.

## Guided practice and diagnostic checks

1. Write the analogue's second column. Why is (0,2,0)L not that column?
2. Find Bq for q=(−1,2,0). Recover q from your answer.
3. Is (−1/2,0,1/2) in the centered half-open coordinate cell? Explain each boundary.
4. A reader flips the third column to make the determinant positive. Has the locked specification been preserved?

## Worked answers

1. b=(1,2,0)L; (0,2,0)L is a row of the numerical table, not the second edge.
2. −a+2b=(1,4,0)L. Recover q_2=4/2=2, q_1=1−2=−1, q_3=0.
3. No. −1/2 is included but +1/2 is excluded. No component is removed; another translated cell owns that boundary.
4. No. Orientation and the third labeled vector have changed even if some lengths stay the same.

**Next dependency:** [Lesson 2](lesson-02.md) measures lengths and angles from the columns you can now read.
