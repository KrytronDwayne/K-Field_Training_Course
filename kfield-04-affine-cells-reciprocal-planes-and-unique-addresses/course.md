# Affine Cells, Reciprocal Planes, and Unique Addresses

Six student lessons, followed by the separately linked two-period capstone. Classroom arithmetic uses a synthetic analogue in LU; source cards preserve locked Cell3 nm values.

Supporting materials: [course map](course-map.md), [glossary](terminology.md), [teacher guide](teacher-guide.md), [capstone and answer key](capstone.md), [sources](sources.md), [canonical card](canonical-card.md).

<!-- BEGIN: lesson-01 -->
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
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 2 — Why half-open cells have one owner

**Essential question:** How can every boundary point belong to exactly one cell?

**Goals:** Read half-open intervals; assign integer owners using floor, including negative addresses; reconstruct an address from its owner and local coordinate.

**Bridge:** Lesson 1 assigns exactly one dimensionless address q to each physical point. We now organize addresses into cells. Keep B and O unchanged; this lesson changes the description of q, not the point.

## C04.02-E1 — A number-line rule with no gaps

An interval is a range of numbers. A square bracket includes its endpoint; a round bracket excludes it. Thus [-1/2,1/2) includes -1/2 and all numbers up to, but not including, 1/2. The cell centered at integer k uses [k-1/2,k+1/2). The right endpoint of one interval is the included left endpoint of the next:

| Owner k | Included range |
|---|---|
| -1 | [-3/2,-1/2) |
| 0 | [-1/2,1/2) |
| 1 | [1/2,3/2) |

The **floor** of a real number t, written floor(t), is the greatest integer less than or equal to t. It is a move toward the left on the number line, not a deletion of decimal digits: floor(-1.2)=-2, while floor(1.2)=1.

For one address entry define z=floor(q+1/2). The defining floor inequality says z≤q+1/2<z+1. Subtract z+1/2 from every part to obtain -1/2≤q-z<1/2. Set u=q-z. We have **q=z+u**, with integer owner z and retained local coordinate u in [-1/2,1/2).

Why is z unique? The intervals above touch only at an endpoint, and only the interval on its right includes that point. Every number lies in one interval, never two. In three dimensions do this independently in each entry. The notation [-1/2,1/2)^3 means all triples whose three entries lie in that interval. It is a product of three ranges, not the cube of a number.

The physical cell owned by integer triple z consists of points O+B(z+u) with u in that product. Since B has a unique inverse, different address descriptions cannot secretly represent one physical point. Therefore the address partition gives unique physical ownership too.

## C04.02-W1 — Three exact boundaries

For q=(1/2,-1/2,3/2), first add 1/2 to each entry: (1,0,2). Applying floor gives **z=(1,0,2)**. Subtract componentwise: **u=(-1/2,-1/2,-1/2)**. Every local entry is allowed because the lower endpoint is included. Adding z+u returns the original q exactly.

A local +1/2 would be excluded. It must instead be represented as -1/2 in the next positive-index cell. This is true even when the global address is negative.

## C04.02-P1 — Negative and near-boundary addresses

Find z and u for q=(-3/2,49/100,51/100). Check the range of all three local entries, then add them back.

**Worked answer:** q+(1/2,1/2,1/2)=(-1,99/100,101/100), whose floors are (-1,0,1). Subtracting gives u=(-1/2,49/100,-49/100). The second entry stays just below the upper boundary; the third moves into the neighboring cell. The sum (-1,0,1)+(-1/2,49/100,-49/100) recovers all entries of q.

> **Claim scope:** This is an exact mathematical partition convention, adopted for Cell3 in S02 `/backbone_sequence/1`. It is not a claim that a measured point has infinite precision. It is also separate from a generic nearest-integer rounding rule. If nearest-integer rounding is needed elsewhere, its half-tie rule must be declared. Here floor(q+1/2) assigns half ties toward the larger integer and gives the local interval [-1/2,1/2). A library's ties-to-even rounding may disagree and cannot replace the ownership operation.

## Diagnostic checks

1. **C04.02-D1:** Compare owners of 499/1000 and 1/2. Why must you not round the first before assignment?
2. Find floor(-7/5), then the owner and local coordinate of q=-7/5.
3. Is z=0,u=1/2 a valid representation of q=1/2 under this rule? Repair it.
4. Does retaining only z allow reconstruction? Give two different addresses with owner zero.

**Worked answers:** (1) floor(999/1000)=0, but floor(1)=1. Rounding erases which side of the boundary the input occupies. (2) floor(-1.4)=-2; ownership uses floor(-1.4+0.5)=floor(-0.9)=-1. Thus u=-7/5+1=-2/5. (3) No: the local upper endpoint is excluded. Use z=1,u=-1/2. (4) No. q=0 and q=1/4 both have owner zero but different u. Retaining u is essential information.

**Pacing:** 20 minutes explanation/worked example, 15 practice, 15 diagnostics and feedback, 5 transition.

**Next dependency:** [Lesson 3](lesson-03.md) constructs physical vectors that read address entries and label parallel planes.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
# Lesson 3 — Reciprocal vectors as plane counters

**Essential question:** What physical calculation reads an address coordinate without confusing it with a physical axis?

**Goals:** Verify three direct-reciprocal pairings; calculate affine plane levels; select matching canonical source fields while rejecting a superseded branch.

**Bridge:** Lessons 1–2 gave q=B^-1(x-O), with q=z+u. We keep the same synthetic B and O. A **dot product** multiplies corresponding components and adds: (r1,r2,r3) dot (s1,s2,s3)=r1s1+r2s2+r3s3. For example (1,2,0) dot (3,-1,4)=3-2+0=1. It produces a scalar, one number rather than a triple.

## C04.03-E1 — Design a vector by what it reads

We want a vector that reads q1 from the physical displacement d=q1a+q2b+q3c. It must have dot product 1 with a and 0 with b and c. Distributing the dot product then gives q1×1+q2×0+q3×0=q1. This reader is the first **reciprocal vector**. The second reads q2 with pairings (0,1,0); the third reads q3 with pairings (0,0,1). The reciprocal is not the direct vector normalized to length one.

Let h=(h1,h2,h3) be an integer triple specifying which combination h1q1+h2q2+h3q3 to read. We require g_h dot a=h1, g_h dot b=h2 and g_h dot c=h3. For our synthetic columns these conditions become:

```text
g1 = h1,      g1+2g2 = h2,      -3g3 = h3.
Therefore g_h = (h1,(h2-h1)/2,-h3/3) LU^-1.
```

Here g1,g2,g3 are components of the vector g_h, not separate plane labels. Taking a dot product with d now gives **g_h dot (x-O)=h dot q**. Both sides are dimensionless. A plane family consists of points where this level is an integer m: **g_h dot (x-O)=m**. A general point can have a noninteger level; it then lies between the integer-level planes. h must be nonzero for a plane normal and finite spacing.

The compact formula is g_h=B^-T h. The symbol T means transpose, swapping rows with columns; B^-T means transpose the inverse B^-1. Each row of B^-1 already reads one address entry. Turning these rows into columns and weighting them by h makes the required physical reader. This derives the notation from the three pairings; you do not need a general matrix-inversion algorithm.

## C04.03-W1 — Check every pairing

For h=(1,0,0), g=(1,-1/2,0) LU^-1. Pair with a=(1,0,0): 1. Pair with b=(1,2,0): 1-1=0. Pair with c=(0,0,-3): 0. At the lesson-1 point x=(2,-2,1) LU, x-O=(0,-1,-3) LU, so g dot (x-O)=0+1/2+0=1/2, correctly reading q1.

## C04.03-P1 — A second reader

Use h=(0,1,0). Find g, verify its three pairings, and evaluate the level at q=(1/2,-1/2,1).

**Worked answer:** g=(0,1/2,0) LU^-1. Its dot products with a,b,c are 0,1,0. At x-O=(0,-1,-3), the level is -1/2, equal to q2.

## C04.03-E2 and C04.03-W2 — Read a source card without changing its branch

A source pointer names a location inside a JSON document. The slash path `/backbone_sequence/1/result` selects the second sequence entry (indexing starts at zero), then its result field. S02's M02 result lists unit normals and spacings in u,v,w order. These source axis names are separate from our local-coordinate vector u; in the table they label the three reciprocal families. A unit normal specifies direction; a spacing specifies the perpendicular separation, taught computationally in lesson 4. A nanometre, nm, is 10^-9 metre.

Read the canonical table in [canonical-card.md](canonical-card.md), reproduced from S02 `/backbone_sequence/1/result`. For u, the full source spacing is **0.32954652969544673 nm** and its matching normal is **(0.9959651903089612, -0.08360216250737743, 0.03261929056440005)**. Copy the full lexemes (the exact written decimal strings), axis order, units and pointer onto your card. This is source-reading, not hand computation of those decimals.

## C04.03-P2 — Compare provenance before arithmetic

Compare canonical u spacing with S02 `/backbone_sequence/1/reciprocal_witness/u/spacing_nm`, which reads **0.3295465297092934 nm**. Use S03 `/findings/4` to decide which is active. Then identify canonical v and w spacings from the card.

**Worked answer:** AUD-005 in S03 marks `M02.reciprocal_witness` SUPERSEDED_NUMERIC_WITNESS. The canonical active u spacing is 0.32954652969544673 nm; the other is retained solely as superseded provenance. Canonical v is 0.4515973797212846 nm and w is 0.6050977415185554 nm. The discrepancy between branches is not measured residual information and should not be renamed as such.

> **Claim scope:** The table reports archival source values at stored precision; the small synthetic pairing examples are freshly checkable mathematical derivations. The source's printed unshifted plane expression must be read with its origin convention; our affine equations always retain x-O (x-O_K for Cell3). No closure theorem or physical mechanism is inferred from reading this card. Never mix a canonical normal with a stale spacing.

## Diagnostic checks

1. **C04.03-D1:** For h=(1,1,0), find g and evaluate g dot (x-O) and g dot x at the worked point. Which equals h dot q?
2. **C04.03-D2:** A card uses the canonical u normal but spacing 0.3295465297092934 nm. Accept or reject? Name the field that repairs it.
3. Find g for h=(0,0,1), and verify its pairing with c.
4. For h=0, can the formula provide a direction for a plane normal?

**Worked answers:** (1) g=(1,0,0) LU^-1; shifted level is 0 and unshifted is 2. h dot q=1/2-1/2=0, so only the shifted expression works. (2) Reject the mixed branch. Use S02 `/backbone_sequence/1/result/reciprocal_spacings_u_v_w_nm/0` with the matching normal at `/backbone_sequence/1/result/reciprocal_normals_u_v_w/0`. (3) g=(0,0,-1/3); g dot c=1. (4) No: g=0 has no direction. The equation is all space if m=0 and no points if m≠0, not a plane family.

**Pacing:** 20 minutes dot-product bridge and worked pairing, 10 pairing practice, 10 source-card worked/practice activity, 10 diagnostics and feedback, 5 transition. The source card is supplied; students do not browse or invert locked decimal matrices.

**Next dependency:** [Lesson 4](lesson-04.md) turns these nonzero plane counters into unit normals and physical spacings.
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
# Lesson 4 — Plane normals and physical spacing

**Essential question:** How does a vector that counts plane levels determine the distance between planes?

**Goals:** Calculate a vector's magnitude and unit direction; derive consecutive-level spacing; explain how scaling or reversing a plane label changes its planes.

**Bridge:** Lesson 3 constructs g_h with g_h dot (x-O)=h dot q. Integer values m define parallel planes. We now need the physical distance between planes labeled m and m+1. All computation still uses the synthetic basis in LU, not the source's nm geometry.

## C04.04-E1 — Length, direction and projection

The magnitude of v=(v1,v2,v3), written |v|, is sqrt(v1²+v2²+v3²). The square root is the nonnegative number whose square is the input. Repeated use of the right-triangle length rule gives this formula for perpendicular physical axes. For nonzero v, divide each component by |v| to obtain a **unit vector**, of magnitude 1. Division changes length without changing direction.

For a nonzero reciprocal vector g, define n=g/|g|. Its components have no units because inverse length cancels inverse length. A displacement parallel to n is t n, where the signed number t has length units. Its projection on n is n dot (t n)=t because n dot n=1. More generally n dot d is the signed component of a displacement d along that direction. To see why this measures perpendicular separation, split d as (n dot d)n plus the remainder d-(n dot d)n. The remainder has dot product zero with n, so it lies along a level plane and adds no perpendicular displacement. For a given normal projection, adding a nonzero perpendicular-to-n remainder only increases the displacement's squared length.

A vector perpendicular to a plane is called a **normal**. Along a plane the level does not change: g dot d=0 for a displacement d within it. Therefore g, and also n, is normal to the level planes. Move by t n from one plane. The change of level is g dot (t n)=t|g|. To increase the level by exactly one, choose **t=1/|g|**. Hence consecutive integer-level spacing is **d_h=1/|g_h|**. Spacing is positive, while n carries orientation. Since |g| has inverse-length units, d_h has length units.

## C04.04-W1 — From counter to ruler

For h=(1,0,0), lesson 3 gives g=(1,-1/2,0) LU^-1. Its magnitude is sqrt(1+1/4)=sqrt(5)/2 LU^-1. Divide componentwise:

```text
n = (2,-1,0)/sqrt(5),       d_h = 2/sqrt(5) LU.
```

Check |n|²=4/5+1/5=1. The displacement to the next level is d_h n=(4/5,-2/5,0) LU. Its level increment is g dot (d_h n)=4/5+1/5=1. This checks the spacing using the original counter rather than merely repeating the magnitude calculation. The origin cancels when comparing two points, but stays explicit in each point's plane equation.

## C04.04-P1 — Two axis-aligned normals

Find g, n and spacing for h=(0,1,0) and h=(0,0,1). Verify that moving by the spacing along n increases the corresponding level by one.

**Worked answer:** The first gives g=(0,1/2,0) LU^-1, |g|=1/2 LU^-1, n=(0,1,0), spacing 2 LU. Its normal step (0,2,0) LU has dot product 1 with g. The second gives g=(0,0,-1/3) LU^-1, n=(0,0,-1), spacing 3 LU. Its step (0,0,-3) LU also raises the level by 1. A negative component in a normal is a direction, not a negative spacing.

> **Claim scope:** These are geometric derivations for nonzero h, with all integer levels m allowed. We do not impose a “primitive integer label” convention that would discard labels with a common factor. Replacing h by 2h inserts additional planes between the old integer levels. This differs from multiplying both sides of one plane equation by 2, which leaves that individual plane unchanged. Canonical Cell3 normal and spacing fields remain the source-reading values from lesson 3, with their separate nm units.

## Diagnostic checks

1. **C04.04-D1:** Replace h=(1,0,0) by (2,0,0). Find g, n and the consecutive-level spacing; explain which new planes appear.
2. Replace h=(1,0,0) by (-1,0,0). What happens to normal, spacing and the unlabeled set of planes?
3. What fails at h=0 in n=g/|g| and d_h=1/|g|?
4. For h=(0,1,0), find the physical plane with m=1. Is it x2=2 LU or x2=1 LU?

**Worked answers:** (1) g=(2,-1,0) LU^-1, |g|=sqrt(5) LU^-1, n=(2,-1,0)/sqrt(5), spacing 1/sqrt(5) LU. Odd new integer levels occur halfway between old planes because the new equation is 2q1=m. (2) g and n reverse, spacing stays 2/sqrt(5) LU; the plane set is the same with m labels reversed. (3) Both divide by zero; no unit direction or finite spacing exists. (4) (x2-(-1))/2=1 in LU components, so x2=1 LU. The origin shift matters.

**Pacing:** 20 minutes explanation/worked example, 15 practice, 15 diagnostics and feedback, 5 transition.

**Next dependency:** [Lesson 5](lesson-05.md) explains why lengths and angles must use the physical geometry rather than the appearance of addresses.
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Lesson 5 — Metric angles versus address angles

**Essential question:** Why can two perpendicular address axes represent physical directions that are not perpendicular?

**Goals:** Compare address and physical dot products; build a Gram matrix from step-vector pairings; retain cross terms when computing a squared physical length.

**Bridge:** Lesson 1 converts an address displacement v into physical displacement Bv. Lesson 3 taught dot products, and lesson 4 taught magnitude and unit directions. Here v and w are changes of address, not physical points; origin subtraction has already occurred when comparing two points.

## C04.05-E1 — Let the step vectors carry the geometry

The address e1=(1,0,0) means one a step. The address e2=(0,1,0) means one b step. Their ordinary address dot product is zero. But the actual steps are a=(1,0,0) LU and b=(1,2,0) LU. They both have a positive first physical component. The coordinate labels alone have hidden this overlap.

For two nonzero physical vectors p and s, their direction comparison is (p dot s)/(|p||s|). This equals the cosine of their angle: a number equal to 0 for a right angle, 1 for the same direction, and -1 for opposite directions. You only need the zero test for perpendicularity; calculating an inverse cosine in degrees is optional. The dot product formula is consistent with projection: p dot (s/|s|) is the signed length of p along s's unit direction, then dividing by |p| compares directions without lengths.

To avoid expanding every physical vector repeatedly, make a table of the direct step dot products. This is the **Gram metric** M_cell=B^T B. Transpose T swaps rows and columns, as in lesson 3. Entry ij is the dot product of column i with column j:

```text
             a     b     c
M_cell =   [ 1     1     0 ]
           [ 1     5     0 ] LU^2.
           [ 0     0     9 ]
```

The two off-diagonal 1 entries both matter. For address displacements v and w, the physical dot product is **(Bv) dot (Bw)=v^T M_cell w**. To compute the right side, multiply M_cell by w row by row, then dot with v. This formula follows by distributing (v1a+v2b+v3c) dot (w1a+w2b+w3c): each vi wj is multiplied by the corresponding step pairing.

For one displacement q, its squared physical length is q^T M_cell q=q1²+2q1q2+5q2²+9q3² LU². The cross term 2q1q2 combines q1q2(a dot b) and q2q1(b dot a). Their signs follow the inputs; they are never deleted because they complicate the calculation.

## C04.05-W1 — An address right angle is not a physical right angle

e1 dot e2=0. Their physical images are a and b, so a dot b=1 LU², |a|=1 LU, and |b|=sqrt(5) LU. Thus cos(angle)=1/sqrt(5), not zero. The directions are not perpendicular. The Gram method gives the same answer: M_cell e2=(1,5,0) LU², and e1 dot this triple is 1 LU².

## C04.05-P1 — Test the third direction two ways

Check whether a and c are perpendicular, then b and c, using physical components and Gram entries. Calculate the cosine for each pair. Also compute the physical squared length of address displacement (1,-1,0).

**Worked answer:** a dot c=1×0+0×0+0×(-3)=0; b dot c=1×0+2×0+0×(-3)=0, so both are perpendicular pairs. M13=M31=M23=M32=0 confirms them. Their magnitudes are |a|=1, |b|=sqrt(5), |c|=3 LU, so the cosines are 0/(1×3)=0 and 0/(sqrt(5)×3)=0. For (1,-1,0), Bq=(0,-2,0) LU gives length squared 4 LU². The Gram expression gives 1-2+5=4 LU², including the negative cross term.

> **Claim scope and names:** M_cell here is the Gram construction evaluated on the explicitly synthetic B; its displayed numbers are not Cell3 constants. In the actual source, M_cell uses the locked Cell3 B in nm and has nm² units. The reciprocal Gram metric is R_cell=M_cell^-1, with inverse-square-length units. An inverse metric is not the reciprocal basis B^-T: it is a different matrix acting on different quantities. G_phase and G_eff are separate phase/effective metrics; distance Q, Q_g and Q_nu are separately typed source quantities. None is substituted for this physical Gram form. No assessment requires their advanced theory.

## C04.05-P2 — Practice a nonzero physical cosine

Compare address displacements v=e1 and w=(1,1,0). Find their physical dot product, magnitudes and cosine. Explain why both vectors must be converted before using the physical angle formula.

**Worked answer:** Bv=(1,0,0) LU and Bw=(2,2,0) LU. Their dot product is 2 LU² and their magnitudes are 1 LU and sqrt(8)=2sqrt(2) LU. Therefore the physical cosine is 2/(1×2sqrt(2))=1/sqrt(2). The address dot product and address lengths would describe the address graph, not the physical geometry carried by B.

## Diagnostic checks

1. **C04.05-D1:** For q=(1,1,0), calculate |Bq|² directly and through the Gram expression. Why is 1+5=6 incomplete?
2. Does a negative third column make the squared length of c negative?
3. Compute the physical dot product of address displacements v=(1,-1,0) and w=(1,0,0).
4. What units must v^T M_cell w have when v and w are dimensionless?

**Worked answers:** (1) Bq=(2,2,0) LU, giving 4+4=8 LU². The Gram expression is 1+2+5=8. The value 6 omits both cross terms. (2) No: c dot c=9 LU²; orientation and squared length are different properties. (3) Bv=(0,-2,0), Bw=(1,0,0), dot product 0. Using M_cell w=(1,1,0), v dot it is 1-1=0. These physical directions are perpendicular even though v dot w=1. (4) LU², inherited from the metric.

**Pacing:** 20 minutes explanation/worked example, 15 practice, 15 diagnostics and feedback, 5 transition.

**Next dependency:** [Lesson 6](lesson-06.md) combines physical geometry, exact ownership and retained display residuals in a reconstruction ledger.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# Lesson 6 — Reconstruction and boundary checks

**Essential question:** What must an atlas retain so that its labels and rounded displays can always be checked against the original point?

**Goals:** Build a typed reconstruction ledger; verify both affine and owner/local reconstruction; restore exact addresses from displays and retained residuals before testing boundaries.

**Bridge:** Lessons 1–5 supply q=B^-1(x-O), z=floor(q+1/2), u=q-z, and the affine plane and metric checks. We now put these together. A ledger is a table of related values with declared meanings and units. It is useful only if readers can reconstruct rather than guess the input.

## C04.06-E1 — Keep the information needed to reverse each step

For each synthetic point retain the input address q or exact physical point x, the common B and O, owner z and local coordinate u. If a shortened display q_disp is shown, also retain **r=q-q_disp**, called the display residual. It is a signed triple, not merely a size or a score. Reconstruct with **q=q_disp+r**, then x=O+Bq. Retain all three entries even when one is zero.

| Field | Meaning | Units | Reconstruction role |
|---|---|---|---|
| B,O | Ordered step matrix and origin | LU, LU | Define the affine map |
| q | Full address | dimensionless | x=O+Bq |
| z | Integer cell owner | dimensionless | q=z+u |
| u | Local address in [-1/2,1/2)^3 | dimensionless | Retains position inside cell |
| q_disp,r | Display and signed display residual | dimensionless | q=q_disp+r |
| x | Physical point | LU | q=B^-1(x-O) |

For exact fractions, compare boundaries without rounding. For example 499/1000<1/2 because multiplying both sides by positive 2000 gives 998<1000. Multiplying by a positive denominator preserves the inequality. If an input interval rather than an exact point crosses a boundary, record the possible owners and retain that interval; do not pretend the display determines a unique true owner. Our assessed examples supply exact fractions so the rule is unambiguous.

Source values and display values are separate fields. Keep the locked decimal lexeme on a source card even if a shorter number is shown beside it. A source-version replacement is recorded in the provenance ledger, not relabeled as this pointwise display residual. These distinctions keep mathematical reconstruction and historical source comparison separate.

## C04.06-W1 — A complete boundary row

Start with q=(1/2,-1/2,3/2). The affine map gives x1=2+1/2-1/2=2, x2=-1+2(-1/2)=-2, and x3=4-3(3/2)=-1/2. Thus **x=(2,-2,-1/2) LU**. Lesson 2's rule gives z=(1,0,2), u=(-1/2,-1/2,-1/2).

Reconstruct using the two retained parts: z+u=(1/2,-1/2,3/2), B(z+u)=(0,-1,-9/2) LU, and O+B(z+u)=(2,-2,-1/2) LU. The physical reconstruction difference is exactly (0,0,0) LU. Recovering the address from x-O also gives q1=0-(-1)/2=1/2, q2=-1/2, q3=-(-9/2)/3=3/2. Every direction agrees.

## C04.06-P1 — Fractions on opposite sides of a boundary

Use q=(-3/2,49/100,51/100). Compute x and reconstruct it using z and u from lesson 2. Keep all fractions.

**Worked answer:** x1=2-3/2+49/100=99/100; x2=-1+98/100=-1/50; x3=4-153/100=247/100, in LU. With z=(-1,0,1) and u=(-1/2,49/100,-49/100), their sum is the exact original q; substitution gives the same x. Independently, d=x-O=(-101/100,49/50,-153/100) LU. Then q2=49/100, q3=51/100, q1=-101/100-49/100=-3/2.

**Additional display practice, C04.06-P2:** Display q=(499/1000,0,0) as q_disp=(1/2,0,0). Find r and the corrected physical point before assigning the owner.

**Worked answer:** r=(-1/1000,0,0). The displayed point is (5/2,-1,4) LU; its correction Br=(-1/1000,0,0) LU gives x=(2499/1000,-1,4) LU. Restore q_disp+r first: its owner is (0,0,0), and its local coordinate is q itself.

> **Claim scope:** Every example here is synthetic and exact. A zero reconstruction difference checks the stated operations; it is not experimental evidence for a mechanism. A nonzero difference would be retained with its components and investigated. A shortened display is useful only with the removed information and a reconstruction rule. Local coordinate u and display residual r have different roles and must both be named.

## Diagnostic checks

1. **C04.06-D1:** For the display-practice point, what wrong owner would assignment from q_disp alone give, and how does r repair it?
2. A ledger retains z but deletes u after calling it “small.” Which reconstruction fails?
3. Restore q from q_disp=(-3/2,1/2,1/2) and r=(0,-1/100,1/100), then assign z.
4. Can you replace r=(-1/1000,0,0) with its positive magnitude and still reconstruct uniquely?

**Worked answers:** (1) Display-only ownership is (1,0,0), but q_disp+r=(499/1000,0,0) gives (0,0,0). (2) q=z+u and therefore x=O+B(z+u) cannot be reconstructed; z specifies a cell, not its point. (3) q=(-3/2,49/100,51/100), so z=(-1,0,1). (4) No: a magnitude loses the sign and which coordinate changed. Many residual triples have that magnitude.

**Pacing:** 20 minutes explanation/worked example, 15 reconstruction/display practice, 15 diagnostics and feedback, 5 transition.

**Next dependency:** The [capstone](capstone.md) builds a three-point cell-address atlas using only the operations introduced and practiced in these six lessons.
<!-- END: lesson-06 -->
