# The Authoritative Cell3: Basis, Metric, and Scale

Six core lessons for high-school seniors. Use the [course map](course-map.md), [geometry card](geometry-card.md), [glossary](terminology.md), [teacher guide](teacher-guide.md), and [capstone with full key](capstone.md). [Sources](sources.md) and [verification record](verification.json) preserve provenance and numerical information.

<!-- BEGIN: lesson-01 -->
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
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
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
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
# Lesson 3 — Face areas and signed volume

**Essential question:** How can area and volume record orientation without becoming negative sizes?

**Goals.** Calculate three cross products; distinguish oriented area from area magnitude; evaluate a scalar triple product and its sign; retain face labels and units.

## Bridge

You can add vectors, take dot products, and compute magnitudes. Those tools measured edges. To measure a face, we need an operation whose magnitude is the parallelogram area and whose direction identifies which way the face is oriented.

## Oriented area components

For u=(u_x,u_y,u_z) and v=(v_x,v_y,v_z), define

u×v=(u_y v_z−u_z v_y, u_z v_x−u_x v_z, u_x v_y−u_y v_x).

Each component is a signed two-dimensional area: yz, zx, and xy in that order. In a two-dimensional plane the difference of the two products measures the parallelogram's signed area. Combining the three gives a vector perpendicular to both inputs. You can verify perpendicularity by dotting the displayed vector with u or v: each product cancels with its opposite. Reversing the order negates the vector. The right-hand rule selects its direction: curl from the first arrow toward the second; the thumb gives the normal direction in right-handed external axes.

The magnitude A_uv=||u×v|| is nonnegative and equals ||u||||v||sin(theta_uv), base times perpendicular height. Sine for an acute right-triangle angle is opposite/hypotenuse; for an included angle from 0 to 180 degrees it gives the nonnegative height factor. Parallel edges have zero area. A **normal** is a perpendicular direction; a unit normal is the cross vector divided by its magnitude, when the magnitude is nonzero.

For three columns, det(B)=a·(b×c), a **scalar triple product**. It is signed base area times signed perpendicular height. The unsigned volume is V=|det(B)|. A zero determinant means the edges cannot enclose three-dimensional volume; a nonzero determinant means they are independent. Negative orientation is retained, not converted into a new basis.

## Worked example — Classroom analogue, not Cell3

Use the same a,b,c as Lessons 1–2. Calculate all three labeled face vectors:

- c_ab=a×b=(0·0−0·2, 0·1−1·0, 1·2−0·1)L²=(0,0,2)L².
- c_ac=a×c=(0,3,0)L², because the middle component is 0·0−1·(−3)=3.
- c_bc=b×c=(2·(−3)−0·0, 0·0−1·(−3), 1·0−2·0)L²=(−6,3,0)L².

Their areas in **ab, ac, bc** order are 2L², 3L², sqrt(36+9)L²=3sqrt(5)L². The third area is about 6.7082L², but its exact expression remains 3sqrt(5)L². Do not reorder this list to match a different source field: the locked source also has a normalized area ray in **bc, ac, ab** order.

Now det(B_ex)=a·c_bc=(1,0,0)·(−6,3,0)L³=−6L³. The same result follows from (a×b)·c=(0,0,2)·(0,0,−3)L³. Its absolute value is 6L³. The area of ab is 2L² and the perpendicular height along c is 3L, so ordinary volume is 2·3=6L³. This independent geometric check confirms the magnitude and leaves the negative orientation intact.

The columns of a cofactor table are conventionally b×c, c×a, a×b. Notice that c×a=−c_ac. Thus naming c_ab, c_ac, c_bc as “face cofactors” does not authorize inserting them unchanged into that column order. Explicit cross-product labels prevent a sign error.

> **Claim scope.** The analogue verifies the operations exactly. Actual Cell3's source volume and areas are on the geometry card. Its negative determinant is intentional under fixed ICRS columns. No detector parity, projective identification of n with −n, or physical chirality is inferred from this arithmetic.

## Guided practice and diagnostic checks

1. Find c×a and its magnitude.
2. Check b·(b×c). What does the result say?
3. Exchange a and b. What happens to signed volume and unsigned volume?
4. Replace c by (2,0,0)L. Compute the determinant and explain the geometric failure.

## Worked answers

1. (0,−3,0)L², magnitude 3L²; reversing order changes orientation, not area.
2. (1,2,0)·(−6,3,0)L³=−6+6=0L³. The cross vector is perpendicular to b.
3. Signed volume becomes +6L³; unsigned volume remains 6L³. This is a new ordered basis.
4. b×c=(0,0,−4)L², so a·(b×c)=0L³. All three edges lie in the xy plane and cannot describe arbitrary z displacements.

**Next dependency:** [Lesson 4](lesson-04.md) uses nonzero volume to justify reversing a coordinate map and its metric.
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
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
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Lesson 5 — Scale classes and the area anchor

**Essential question:** Why can ratios determine shape while leaving one size still free?

**Goals.** Derive how lengths, areas, volume, and metrics scale; explain the positive ray of possible lengths; determine a scale from a positive area anchor; distinguish supplied ratios from a physical interpretation.

## Bridge

You have calculated edge lengths, face areas, and signed volume. Multiplying every edge by the same positive number s produces a larger or smaller version with the same angles. A positive s preserves handedness. Negative scaling would reverse orientation and is not part of the positive scale class used here.

Because a dot product multiplies two edge components, M becomes s²M. Each cross product also multiplies two components, so every face area becomes s² times its previous value. A triple product multiplies three components, so signed volume becomes s³det(B). Inverting s²M gives s^−2R: multiplying these two matrices still yields I. Edge lengths scale by s, while ratios of any two lengths or any two areas remain unchanged. A normalized direction stays the same because both vector and its magnitude gain s.

## Worked example — Classroom analogue, not Cell3

The original ab area is 2L². Choose a new supplied anchor A_ab=8L². Since 2s²L²=8L², s²=4 and the allowed positive scale is s=2. The new numerical basis is [[2,2,0],[0,4,0],[0,0,−6]]L.

Its ab/ac/bc areas are 8L²,12L²,12sqrt(5)L², its determinant is −48L³, its Gram matrix is 4M_ex, and its inverse metric is R_ex/4. The ratio A_ac/A_ab is 12/8=3/2, the same as 3/2 before scaling. Its normalized area list in bc/ac/ab order is (1,1/sqrt(5),2/(3sqrt(5))), both before and after. “Normalized” here means dividing the whole area list by A_bc; to reconstruct actual areas retain A_bc as well as the list. If we retained only ratios, absolute scale would be missing.

## The source's conditional uniqueness argument

S02 `/scale_uniqueness_theorem` supplies a fixed labeled angular frame and positive constants eta and alpha. They are inputs in this course, not quantities we derive from masses or other experiments. Their interpretation belongs to course-08. Write l_a,l_b,l_c for the three positive edge lengths, and theta_ab,theta_ac,theta_bc for the included angles. The source specifies

l_c/l_a=(eta/1000) sin(theta_ab)/sin(theta_bc)=k_c,

l_b/l_a=(alpha^−1/100) sin(theta_ac)/sin(theta_bc)=k_b.

Here alpha^−1 means 1/alpha; k_b and k_c name the resulting positive dimensionless ratios. Sines are the height factors taught in Lesson 3. Nondegenerate fixed angles and positive inputs are essential: a zero denominator is not permitted. The source angular frame must also be a realizable independent three-dimensional frame, as the locked basis supplies.

Set l_a=t. Then l_b=t k_b and l_c=t k_c, so

(l_a,l_b,l_c)=t(1,k_b,k_c), t>0.

This is a **positive ray**: one fixed ratio triple multiplied by any positive size t. Two ratios fix relative lengths, not orientation by themselves. The fixed labeled frame provides directions. With this frame and these ratios already supplied, only one continuous scale remains.

The area equation A_ab=l_a l_b sin(theta_ab) becomes A_ab=t² k_b sin(theta_ab). Supply a positive area anchor A_* for this face. Dividing and taking the positive square root gives

t=sqrt(A_*/[k_b sin(theta_ab)]).

The denominator is positive and dimensionless, so t is a length and is unique among positive choices. Other nonzero labeled face anchors work in the same way with their own factors. We can use the supplied locked A_ab=0.19486916546048413 nm² as the numerical anchor for the Cell3 card; that choice does not establish why nature would select it.

A hand-checkable ray example has k_b=2, k_c=3 and all three angles 90 degrees. With A_*=8L², t=sqrt(8/2)L=2L and lengths are (2,4,6)L. This **separate synthetic ray example** illustrates the algebra; its right angles differ from our sheared classroom analogue. It is not a replacement basis for that analogue or for Cell3.

> **Claim scope.** The scale-uniqueness argument is conditional algebra from supplied angular and ratio inputs. It does not derive the angular frame, eta, alpha, the area anchor, or their physical origin. The source's bc/ac/ab ray is a list of area ratios, not the edge-length ray (1,k_b,k_c).

## Guided practice and diagnostic checks

1. Scale the classroom analogue by s=3. Give ab area, determinant, and inverse metric factor.
2. An analogue anchor asks for A_ab=18L². Find s and the ac area.
3. Can the two supplied length ratios alone distinguish t=1L from t=10L? Explain.
4. In the right-angle ray example k_b=2,k_c=3, replace the anchor by 2L². Find lengths. Why is a zero anchor excluded?

## Worked answers

1. A_ab=9·2=18L²; det=27(−6)=−162L³; inverse metric R_ex/9.
2. 2s²=18 gives s=3, so A_ac=9·3=27L².
3. No. t cancels in both ratios. A dimensional anchor is needed.
4. t=sqrt(2/2)L=1L, so lengths (1,2,3)L. A zero anchor would force t=0 in this nondegenerate frame, collapsing the cell and violating t>0.

**Next dependency:** [Lesson 6](lesson-06.md) turns the source lock, units, and numerical checks into a reproducible geometry card.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# Lesson 6 — A reproducible Cell3 specification

**Essential question:** What must accompany a decimal matrix so another reader can reproduce its meaning and checks?

**Goals.** Read exact source-decimal strings with labels and units; distinguish a mathematical identity from a stored-precision witness; calculate and preserve a signed residual; assemble a provenance-complete geometry card.

## Bridge

You can read columns, compute a metric, check faces and volume, invert the small analogue, and fix scale from an anchor. The remaining task is to keep a numerical record reproducible. A long decimal is not self-explanatory: a row/column convention, unit, source version, and arithmetic rule can change its meaning.

## Source identity and evidence layers

A **lexeme** is the written number string, including its digits. Preserve it before numerical conversion. A **JSON pointer** gives a location within a structured source: `/mature_locked_cell3/B_nm/0/1` means first row, second entry; indices start at zero. A **SHA-256** digest is a 64-character file fingerprint used here to check file identity. It does not prove the mathematics inside the file. [sources.md](sources.md) supplies exact source paths, digests, and pointers; [geometry-card.md](geometry-card.md) supplies the compact numeric fields.

S02 is the mature lock. S03 confirms canonical values and corrects specific stale witness uses. S01 is a historical corrected-source occurrence, not the active numerical branch. Never blend a historical spacing with a mature normal because their digits look close. Preserve a displaced value under its historical provenance. That historical comparison is different from a closure residual computed from one active numerical branch.

Keep the evidence layers explicit. A source fact says what the archived record contains. A mathematical derivation follows from stated assumptions. A numerical witness checks chosen decimals with specified arithmetic. A proposed mechanism explains why a physical structure might arise. This course performs the first three; it introduces no new observed dataset or mechanism. Standard Euclidean vector geometry supplies the reference mathematics.

## Worked example — a precision check you can do by hand

This is a **synthetic rounding example**, not a Cell3 measurement. An exact multiplier is 1/3. Suppose a display stores 0.333. A closure check gives 3·0.333−1=−0.001. Keep the sign and value r=−0.001. The computed product is reconstructed as 1+r=0.999. Do not replace the stored 0.333 by a different constant merely to make the check return zero.

For a matrix check define E=M_stored R_stored−I entry by entry. For a basis/metric comparison define F=B_stored^T B_stored−M_stored. The reference identities are exact when R is the exact inverse and M is the exact Gram matrix. Independently rounded stored arrays need not satisfy them digit for digit. Record **all nine entries** of E and F with their units, not just the largest absolute entry. Reconstruction is M_stored R_stored=I+E and B_stored^T B_stored=M_stored+F. Retaining the source path/hash and arithmetic recipe makes the inputs replayable without copying an archive.

For this course, the attached verification script reads number strings directly, uses Python Decimal with 60 significant digits and ROUND_HALF_EVEN, and preserves complete residual matrices in [verification.json](verification.json). Decimal rounding at a half-tie chooses the even final retained digit: to one decimal place, 1.25 becomes 1.2 and 1.35 becomes 1.4. This is an arithmetic precision rule; it is separate from the half-open spatial cell ownership in Lesson 1. No nearest-integer spatial rounding is used here. No residual is removed because it is small.

## Reading the checked card

The card labels the actual B in nm and M_cell in nm²; R_cell has nm^−2. It quotes source decimals without symmetrizing them. For example, stored R_12 is 0.0015348024281924184 while R_21 is 0.0015348024281924234. Their difference is −0.0000000000000000050 nm^−2, or −5.0×10^−18 nm^−2. The exact inverse metric is symmetric, but these two stored approximations differ. Both strings remain on the card; the difference remains in the verification record.

The source-reported `direct_reciprocal_closure_max_abs` is 2.8939781400741195e−16. The notation e−16 means multiply by 10^−16. This scalar is not our newly recomputed matrix residual, and its label does not specify enough arithmetic to reproduce that source calculation exactly. We retain it as source-reported. Our verification script separately declares its inputs, operations, and precision. A hash match confirms that we checked the intended file, not that its reported witness has been freshly reproduced.

For a short reading exercise, `/mature_locked_cell3/B_nm/0/1` gives 0.0353307758438284 nm, the x component of **b**. `/mature_locked_cell3/face_areas_nm2/ab` gives 0.19486916546048413 nm². A normalized area ray lists bc/ac/ab and begins with 1.0; the face-area table lists ab/ac/bc. Write these labels before doing arithmetic.

> **Claim scope.** The card is a source-grounded specification plus declared numerical verification. It neither replaces canonical source decimals with higher-precision recomputations nor interprets closure differences as measured physical changes. Unresolved arithmetic provenance of a source-reported scalar stays explicitly unresolved.

## Guided practice and diagnostic checks

1. Read B's third column from the card. Give units and axis convention.
2. A student replaces both unequal reciprocal-metric entries by their average. What information has changed?
3. In the synthetic rounding example, store 0.3333 instead. Find the signed residual and reconstruct the product.
4. Name the minimum records needed to distinguish a source-reported closure scalar from a new verification.

## Worked answers

1. c=(−0.0101293176267288,−0.3897877023662599,−0.6897344083672676) nm in the fixed ICRS axes.
2. Both source lexemes have changed and their antisymmetric difference has been lost unless separately retained. The locked card must preserve the originals.
3. 3·0.3333−1=−0.0001; 1+(−0.0001)=0.9999. Smaller magnitude does not authorize deleting the residual.
4. Source ID, full-file hash, exact pointer, original scalar string and reported status; for the new check, input fields, formula, units, arithmetic precision, rounding mode, and every signed residual component.

**Next dependency:** [Capstone](capstone.md) combines your classroom calculation sheet with a separately labeled locked Cell3 geometry card.
<!-- END: lesson-06 -->

