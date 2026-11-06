# Lesson 2 — Lengths and angles from a Gram matrix

**Essential question:** How does one table retain both edge lengths and their interactions?

**Goals.** Compute all nine Gram entries; use transpose and row-column multiplication; calculate a squared length with cross terms; infer whether two edges are perpendicular.

## Bridge

Lesson 1 supplied Bq as a sum of columns. We now measure that sum. The magnitude (length) of v=(v_x,v_y,v_z) is ||v||=sqrt(v_x²+v_y²+v_z²). A square root means the nonnegative number whose square is the stated value. These are the three-dimensional Pythagorean rules for the fixed perpendicular external axes.

## Dot products and matrix products

The **dot product** u·v=u_x v_x+u_y v_y+u_z v_z is a scalar. Dotting a vector with itself gives its squared length. For nonzero vectors, u·v=||u||||v||cos(theta), where theta is their included angle between 0 and 180 degrees. Cosine is the adjacent/hypotenuse ratio for an acute right-triangle angle and extends to signed projections for larger angles. Zero dot product means a 90-degree angle; a positive dot product means an acute angle. A calculator's arccos (inverse cosine) returns the angle with a specified cosine; use degree mode here. We will not require a trigonometry proof.

The **transpose** B^T swaps rows and columns, without moving the geometric vectors. The entry in row i, column j of a product UV is the dot product of row i of U with column j of V. For example, [1,0,0] dotted with [1,2,0] gives 1. Transposing a table for calculation is different from declaring that its old rows were the physical edges.

The Gram metric is M_cell=B^T B for actual Cell3. For our classroom analogue write M_ex=B_ex^T B_ex. Entry ij is edge i·edge j. The table is symmetric because u·v=v·u. Diagonal entries give squared edge lengths. Off-diagonal entries store the non-perpendicular interactions. A metric here is a rule for calculating squared length from coordinates; it is not a force or a phase field.

## Worked example — Classroom analogue, not Cell3

Suppress L only while multiplying the numbers. From a=(1,0,0), b=(1,2,0), c=(0,0,−3):

| Dot product | Calculation | Result in L² |
|---|---|---:|
| a·a | 1²+0²+0² | 1 |
| a·b | 1·1+0·2+0·0 | 1 |
| a·c | 1·0+0·0+0·(−3) | 0 |
| b·a | 1·1+2·0+0·0 | 1 |
| b·b | 1²+2²+0² | 5 |
| b·c | 1·0+2·0+0·(−3) | 0 |
| c·a | 0·1+0·0+(−3)·0 | 0 |
| c·b | 0·1+0·2+(−3)·0 | 0 |
| c·c | 0²+0²+(−3)² | 9 |

Therefore M_ex/L²=[[1,1,0],[1,5,0],[0,0,9]]. The edge lengths are L, sqrt(5)L, 3L. For a and b, cos(theta_ab)=1/sqrt(5), so the angle is approximately 63.435 degrees. The decimal angle is a calculator illustration, not a source constant. Both other angles are 90 degrees.

For q=(1,1,0), first compute M_ex q=(2,6,0)L²; then q^T M_ex q=(1,1,0)·(2,6,0)L²=8L². Independently B_ex q=a+b=(2,2,0)L has squared length 4+4=8L². Ignoring off-diagonal terms would give 1+5=6L², a different answer.

More generally, for symmetric M,

q^T M q=M_11 q_1²+M_22 q_2²+M_33 q_3²+2M_12 q_1 q_2+2M_13 q_1 q_3+2M_23 q_2 q_3.

The factor 2 collects both ij and ji entries. Negative cross terms in a particular displacement do not imply negative squared length. For an independent basis, every nonzero q gives positive squared length: this is what **positive definite** means. In source-local notation a letter x may denote the coordinate argument in x^T M_cell x; in this course q is that argument, while x denotes an external point.

> **Claim scope.** These are Euclidean geometry identities applied to the supplied basis. The source sometimes writes G for this Gram matrix; this course writes M_cell to avoid confusing it with G_phase or G_eff. Neither distinct metric is substituted here. See S02 `/backbone_sequence/0` and `/typed_conventions`.

## Guided practice and diagnostic checks

1. Transpose [[1,1,0],[0,2,0],[0,0,−3]].
2. Find squared length for q=(1,−1,0) both ways. Identify the cross contribution.
3. What are M_ex,23 and the angle between b and c?
4. Does a negative determinant force a negative Gram diagonal? Explain using the example.

## Worked answers

1. [[1,0,0],[1,2,0],[0,0,−3]].
2. B_ex q=(0,−2,0)L gives 4L². The metric gives 1+5+2(1)(1)(−1)=4L². Cross contribution: −2L².
3. b·c=0L²; both edges are nonzero, so their angle is 90 degrees.
4. No. The diagonal is 1,5,9 times L². Orientation and squared length carry different information.

**Next dependency:** [Lesson 3](lesson-03.md) uses these lengths to distinguish oriented face vectors from positive face areas.
