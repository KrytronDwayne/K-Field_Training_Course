# lesson-01: Measurements as linear channels

2 sessions of 55 minutes.

**Essential question:** How can three channels describe two unknowns without throwing away the third reading?

**Goals**

- Translate channel recipes into equations and an ordered matrix.
- Solve two normal equations by elimination.
- Reconstruct every input from represented and residual entries.

## Prerequisite bridge

You need signed arithmetic, fractions and linear equations. A tuple is an ordered list: (2,3,6) means first channel 2, second 3, third 6. Multiplying a tuple by a number multiplies every entry; adding tuples adds corresponding entries. These are the only operations needed to begin. Earlier courses motivate retained information, but all matrix operations used here are taught locally.

<a id="C21.01-E1"></a>
## Explanation — C21.01-E1

Imagine two adjustable coordinates, c1 and c2. A channel is a stated recipe for combining them. Our synthetic instrument reports c1, c2, and c1+c2. A linear recipe multiplies each coordinate by a fixed number and adds; there are no products of unknown coordinates. Arrange the recipes as rows:

```text
A_small = [1 0]     c = [c1]       A_small c = (c1,c2,c1+c2)
          [0 1]         [c2]
          [1 1]
```

A matrix is this rectangular table of coefficients. A row times a column means multiply matching entries and add. Its shape is 3 by 2: three output channels and two input coordinates. The system is overdetermined because there are more equations than unknowns. It may be exactly consistent, but it need not be. For y=(2,3,6), the first two equations demand c1=2 and c2=3, whose sum is 5 rather than 6. Keep all three readings.

Declare a decoding convention before solving. In this course the scalar field is the real numbers, written R, and the inner product is Euclidean: u dot v is the sum of pairwise products. For example (1,0,1) dot (2,3,6)=8. We choose the represented vector A_small c so that the residual r=y-A_small c is perpendicular to each column. Perpendicular here means dot product zero. This convention is a reproducible coordinate choice, not a discovery that the residual lacks information.

The transpose A_small^T is obtained by turning columns into rows. Thus A_small^T r=(r1+r3,r2+r3). Set both entries to zero. Substituting r=(2-c1,3-c2,6-c1-c2) gives 8-2c1-c2=0 and 9-c1-2c2=0. These are the normal equations. In compact notation A_small^T A_small c=A_small^T y. Multiplication here has already been defined by sums; it introduces no new physical assumption.

Solve 2c1+c2=8 and c1+2c2=9. Twice the first minus the second gives 3c1=7, so c1=7/3. Then c2=8-14/3=10/3. The represented channels are (7/3,10/3,17/3). Subtract each from y to obtain r=(-1/3,-1/3,1/3). The two perpendicularity checks are -1/3+1/3=0 and -1/3+1/3=0. Reconstruction gives (7/3-1/3,10/3-1/3,17/3+1/3)=(2,3,6).

This construction also minimizes the sum of squared residual entries, but that score is not our saved output. To see the mathematical fact without calculus, change c by h. The new residual is r-A_small h. Its squared length is r dot r minus twice r dot A_small h plus (A_small h) dot (A_small h). The middle term is zero by the perpendicularity condition, and the last term is nonnegative. This explains the convention while leaving the entire signed residual intact.

> Scope: All channel values in these exercises are synthetic and dimensionless. The Euclidean metric is declared. A different weighting would define a different decoder and must be recorded. No physical source coefficient-selection law is being inferred.

For practice y=(1,2,3), compute A_small^T y=(1+3,2+3)=(4,5). Elimination gives c=(1,2). All three residual entries are zero, so explicitly retain (0,0,0), the channel order and the matrix. A missing entry and a known zero are different records.

<a id="C21.01-W1"></a>
## Worked example — C21.01-W1

C21-DEC-EX1: y=(2,3,6) makes c1=2, c2=3, c1+c2=6 inconsistent. The normal equations are 2c1+c2=8 and c1+2c2=9. Elimination gives c=(7/3,10/3). A c=(7/3,10/3,17/3); r=(-1/3,-1/3,1/3). Reconstruct all three channels.

<a id="C21.01-P1"></a>
## Guided practice — C21.01-P1

Try the operation before reading the solution. C21-DEC-P1: y=(1,2,3) gives right side (4,5), c=(1,2), A c=y, r=(0,0,0). Write all three zero residual entries and the original A.

<a id="C21.01-D1"></a>
## Diagnostic checks — C21.01-D1

1. For y=(1,1,3), write and solve the normal equations; retain r.
2. Explain why three rows need not provide three independently adjustable coefficients.
3. Check every reconstruction entry for y=(2,3,6).
4. What extra information is lost if only the residual squared length is stored?

## Worked answers

1. The equations are 2c1+c2=4 and c1+2c2=4. Subtraction gives c1=c2; hence c=(4/3,4/3), represented=(4/3,4/3,8/3), r=(-1/3,-1/3,1/3).
2. There are only two column recipes; the third output is their sum. More readings do not create an additional coefficient direction.
3. 7/3-1/3=2; 10/3-1/3=3; 17/3+1/3=6.
4. Signs and channel positions disappear. For instance r and -r have the same squared length but reconstruct different input vectors.

**Boundary to carry forward:** C21-DEC-D1: y=(1,1,3) gives c=(4/3,4/3), r=(-1/3,-1/3,1/3). Three channels do not imply three independently recoverable coefficient coordinates; here rank is two.

**Next dependency:** [lesson-02](lesson-02.md). Use this lesson’s reconstruction and scope checks there.
