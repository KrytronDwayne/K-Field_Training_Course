# Mathematical Tools: Units, Vectors, and Coordinates

Course-02 · High-school seniors · Seven lessons and a two-period capstone.

Read the lessons in order. Each includes worked answers after its diagnostic checks.

[Lesson-01](lesson-01.md) | [Lesson-02](lesson-02.md) | [Lesson-03](lesson-03.md) | [Lesson-04](lesson-04.md) | [Lesson-05](lesson-05.md) | [Lesson-06](lesson-06.md) | [Lesson-07](lesson-07.md)

Supporting materials: [Course map](course-map.md), [Terminology](terminology.md), [Teacher guide](teacher-guide.md), [Capstone and full answer key](capstone.md), [Sources](sources.md).

<!-- BEGIN: lesson-01 -->
# Lesson 01 — Units and scientific notation

**Essential question:** How can a number change while the quantity it describes stays the same?

**Goals:** Convert lengths and times with unit factors; express numbers in scientific notation; distinguish a period from a frequency and convert both correctly.

**Prerequisite bridge.** You can multiply fractions and solve a linear equation. A conversion factor is a fraction equal to one: 100 cm and 1 m name the same length. Multiplying by their ratio changes the description, not the object. Course-01's distinction between a stated input and a derived result is used here: our numbers are invented teaching inputs, and arithmetic produces the results.

## Build the idea

A quantity consists of a number and a unit. The unit says what counts as one. Length, time, and frequency are different kinds of quantities, called dimensions. We write their dimensions as L, T, and T^-1. A frequency counts repeated cycles per unit time; a cycle is a count, not a length. You may add 2 m to 30 cm after converting to a common unit, but adding 2 m to 3 s has no defined meaning here.

Our exact unit relations are 1 m = 100 cm = 1000 mm, 1 km = 1000 m, 1 min = 60 s, and 1 ms = 0.001 s. A hertz, Hz, means one cycle per second; 1 kHz = 1000 Hz. Write conversion factors so unwanted units cancel. For example, 250 cm × (1 m / 100 cm) = 2.5 m. Reversing the factor would leave cm²/m rather than the desired m.

Scientific notation writes a nonzero number as a × 10^n with 1 ≤ |a| < 10 and integer n. Positive powers count repeated factors of ten; negative powers mean reciprocals. Thus 10^-3 = 1/1000, 3200 = 3.2 × 10^3, and 0.0048 = 4.8 × 10^-3. When multiplying powers of ten, add exponents: (3 × 10^2)(2 × 10^-3) = 6 × 10^-1. Zero is simply zero. A negative value keeps its sign, as in -0.002 = -2 × 10^-3.

A period T is the time for one cycle. For evenly repeating cycles, frequency f = 1/T because one cycle divided by its duration gives cycles per second. Conversely T = 1/f. Convert the time unit before labeling the reciprocal Hz. The reciprocal of 4 ms is 0.25 per millisecond, which is 250 per second, not 0.25 Hz.

## Fully worked synthetic example

An invented scanner moves 36 mm in one repeating cycle lasting 4 ms. Express the length, period, and frequency using metres and seconds.

1. Length: 36 mm × (1 m / 1000 mm) = 0.036 m = 3.6 × 10^-2 m.
2. Period: 4 ms × (1 s / 1000 ms) = 0.004 s = 4 × 10^-3 s.
3. Frequency: f = 1/(0.004 s) = 250 s^-1 = 250 Hz = 0.25 kHz.
4. Reverse checks: 0.036 m × 1000 mm/m = 36 mm; 250 cycles/s × 0.004 s/cycle = 1. The original inputs are recovered without rounding.

The displacement per cycle alone does not specify a path or mechanism. We have calculated units and a repeat rate, not inferred how the scanner works.

> **Claim scope:** All device values in this course are synthetic. Unit definitions and the arithmetic are reference mathematics; no measurement or physical mechanism is being reported. Exact fractions are preferred. When a decimal must be displayed approximately, the rule will be nearest chosen decimal place with halfway values away from zero, and the unrounded value will remain available.

## Guided practice

Convert 7.5 cm to metres and 2 min to seconds. Write the factors before calculating: 7.5 × (1/100) m = 0.075 m; 2 × 60 s = 120 s. A 2 Hz repeat has period 1/2 s. Check each by multiplying back to its starting unit.

## Diagnostic checks

1. Convert 0.003 km to metres and then millimetres.
2. Write 0.00072 s in scientific notation and milliseconds.
3. A repeat has period 20 ms. Find f in Hz and kHz.
4. Explain what is wrong with “3 m + 2 s = 5” and with “2 Hz = 2 seconds.”

## Worked answers

1. 0.003 × 1000 = 3 m; 3 × 1000 = 3000 mm. Multiplying the original by 10^6 gives the same millimetres.
2. 7.2 × 10^-4 s; multiplying seconds by 1000 ms/s gives 0.72 ms.
3. T = 0.020 s; f = 1/0.020 = 50 Hz = 0.050 kHz. The product fT is one cycle.
4. Length and time cannot be added in this model. Hz has dimension T^-1, whereas seconds have T. A 2 Hz repeat has period 0.5 s.

**Next dependency:** [Lesson 02](lesson-02.md) applies unit factors to areas and volumes, where the conversion factor must also be squared or cubed.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 02 — Ratios, powers, and scale

**Essential question:** Why does doubling every edge multiply volume by eight?

**Goals:** Calculate a dimensionless scale ratio; derive length, area, and volume scale factors; distinguish changing a physical size from changing its unit.

**Prerequisite bridge.** Lesson 01 taught unit cancellation and powers of ten. Here repeated multiplication explains why the power of a unit matters. A ratio compares two quantities by division; convert them to the same unit before dividing.

## Build the idea

Let s = new length / old length for corresponding edges of two similar shapes. Similar means the shapes have the same angles and all corresponding lengths share one positive scale factor. Equal length units cancel, so s has no unit. For a rectangle with side lengths l and w, area A = lw counts how many unit squares cover it. Scaling both lengths gives A_new = (sl)(sw) = s²A_old. For a rectangular box, V = lwh counts unit cubes; scaling all three lengths gives V_new = s³V_old. The factors are s, s², s³ for length, area, volume.

This reasoning also explains squared and cubed unit conversions. Since 1 cm = 0.01 m, one square centimetre is (0.01 m)(0.01 m) = 0.0001 m². One cubic centimetre is 0.000001 m³. Changing units leaves the object unchanged. Enlarging an object changes its physical lengths. A drawing scale compares the represented length and the drawing length; its direction must be stated.

For s = 1/2, length halves, area becomes one quarter, and volume one eighth. For different horizontal and vertical factors, there is no single uniform s: a rectangle stretched by 2 horizontally and 3 vertically gains an area factor 6. The square rule requires the same factor in both directions. We use positive size ratios here; orientation signs will have a separate role in Lesson 06.

## Fully worked synthetic example

A model box measures 2 cm by 3 cm by 4 cm. A uniformly enlarged version has first edge 6 cm. The corresponding-length ratio is s = 6/2 = 3, so its edges are 6, 9, and 12 cm.

The 2-by-3 face originally has area 6 cm². Its new area is 54 cm², calculated directly as 6 × 9 or as 3² × 6. Original volume is 2 × 3 × 4 = 24 cm³. New volume is 6 × 9 × 12 = 648 cm³, also 3³ × 24. In metres the original volume is 0.02 × 0.03 × 0.04 = 0.000024 m³; multiplying 24 cm³ by 10^-6 m³/cm³ agrees. Each route preserves dimensions.

> **Claim scope:** This is an exact synthetic geometric enlargement. The volume rule alone does not establish a mass, energy, or biological scaling law. Such a law would need its own relationship and inputs. Nothing is rounded in this example.

## Guided practice

A 10 mm square becomes a 5 mm square. First find s = 5/10 = 1/2. Its area changes from 100 mm² to 25 mm², so the area ratio is 1/4. Express 25 mm² in cm²: each millimetre is 0.1 cm, giving 25 × (0.1)² = 0.25 cm². Check with a 0.5 cm side: 0.5² = 0.25.

## Diagnostic checks

1. A cube's edge grows from 2 m to 8 m. Find the length, face-area, and volume ratios.
2. Convert 9 cm² to m² and 9 cm³ to m³.
3. A 3-by-4 cm rectangle is stretched only horizontally by 2. Find the new area and explain why multiplying by 2² would be wrong.
4. On a drawing, 2 cm represents 5 m. State the represented-to-drawn ratio with matching units, and find the represented length of a 6 cm line.

## Worked answers

1. s = 8/2 = 4. The ratios are 4, 16, and 64; cube volumes 512/8 confirm 64.
2. 9 × (0.01)² = 0.0009 m²; 9 × (0.01)³ = 0.000009 m³. The numerical factors differ because the dimensions differ.
3. New dimensions are 6 by 4 cm, area 24 cm² rather than 12 cm². Only one factor of 2 enters the product.
4. 5 m = 500 cm, so represented/drawn = 500/2 = 250. The 6 cm line represents 1500 cm = 15 m.

**Next dependency:** [Lesson 03](lesson-03.md) applies scale factors to directed coordinate differences while separating an object’s location from its displacement.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
# Lesson 03 — Points and directed displacements

**Essential question:** What changes when we move the origin, and what remains the same?

**Goals:** Distinguish points, origins, and displacement vectors; compute and reconstruct coordinate differences; calculate vector magnitude and a unit direction.

**Prerequisite bridge.** You can read a coordinate pair and subtract signed numbers. Lesson 02 showed how multiplying every length by s changes a shape. We now apply that same multiplication to both components of an arrow.

## Build the idea

A point is a location. An origin is the location chosen as the zero of a coordinate description. Fix perpendicular horizontal x and vertical y axes, with positive x right and positive y up. A pair (x,y) gives ordered coordinates: first horizontal, then vertical. Reversing that order changes the description.

We may describe a local origin O and a point P using a shared background grid. The position vector relative to O is P - O. A displacement from P to Q is v = Q - P: subtract the starting coordinates from the ending coordinates, component by component. A vector is a directed displacement; it has length and direction and can be drawn with its tail anywhere. The point and the vector are different objects even when their pairs happen to match.

If v = (v_x,v_y) and w = (w_x,w_y), adding vectors means adding corresponding components. This represents following one arrow and then the next. Multiplying a vector by s multiplies both components. For positive s its length scales by s; multiplying by -1 reverses the direction. The notation v_x means the horizontal component of v, not multiplication by x.

The magnitude |v| is the arrow's nonnegative length. A right triangle has perpendicular legs v_x and v_y and hypotenuse |v|. The Pythagorean relationship says the hypotenuse squared equals the sum of the leg squares, so |v| = sqrt(v_x² + v_y²). Here sqrt means the nonnegative number whose square is the input. One way to see the relationship is to arrange four copies of a right triangle in a square of side a+b: removing their total area 2ab leaves the tilted hypotenuse square with area (a+b)²-2ab = a²+b².

For v ≠ (0,0), the unit direction u = v/|v| has length one. Divide each component by the same magnitude. If v has length units, those units cancel in u. The zero vector has no unique direction, so division by its zero magnitude is forbidden.

## Fully worked synthetic example

On a background grid in metres, let O = (10,-2) m, P = (13,2) m, and Q = (16,6) m.

Position relative to O: P - O = (13-10, 2-(-2)) = (3,4) m. Displacement from P to Q: v = Q - P = (3,4) m. These happen to have equal components, but they connect different endpoints. Reconstruct P as O + (3,4) m = (13,2) m and Q as P + v = (16,6) m.

Magnitude |v| = sqrt(9+16) m = 5 m. Direction u = (3/5,4/5), whose squared magnitude is 9/25+16/25 = 1. Recover the vector: (5 m)u = (3,4) m.

Choose instead O' = (11,0) m without rotating the axes. P - O' = (2,2) m and Q - O' = (5,6) m. Subtraction still gives (3,4) m. Changing origin changes positions but not this displacement. Enlarging the displacement by factor 2 gives (6,8) m with length 10 m, consistent with Lesson 02.

> **Claim scope:** These are synthetic Euclidean coordinates in perpendicular axes, not Cell3 coordinates. The Euclidean magnitude formula here must not be silently applied to coordinates in a tilted basis. No physical motion is inferred from merely labeling points.

## Guided practice

From A = (-1,2) cm to B = (2,-2) cm the displacement is (3,-4) cm. Its magnitude is 5 cm and direction (3/5,-4/5). Reverse the journey: (-3,4) cm has the same magnitude but the opposite direction. Adding either displacement to its starting point checks its endpoint.

## Diagnostic checks

1. O = (2,3) m and P = (-1,7) m. Find P - O and reconstruct P.
2. Find the magnitude and unit direction of (0,-6) cm.
3. For P = (1,2) m, Q = (4,6) m, and new origin O' = (5,-1) m, find both relative positions and their difference.
4. Can (0,0) be normalized? What does multiplying (3,4) m by -2 do to length and direction?

## Worked answers

1. P - O = (-3,4) m. Adding (2,3)+(-3,4) gives (-1,7) m.
2. sqrt(0+36) = 6 cm; direction (0,-1), with length one.
3. P - O' = (-4,3) m and Q - O' = (-1,7) m; their difference is (3,4) m, also Q - P.
4. No: its magnitude is zero. The new vector (-6,-8) m is twice as long, 10 m, and points opposite to (3,4) m.

**Next dependency:** [Lesson 04](lesson-04.md) uses unit directions to measure the part of a vector along a chosen line.
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
# Lesson 04 — Angles and projections

**Essential question:** How much of an arrow points along a chosen direction?

**Goals:** Use sine and cosine as right-triangle ratios; calculate a dot product and normalize a non-unit direction; distinguish scalar and vector projection and reconstruct the retained perpendicular part.

**Prerequisite bridge.** Lesson 03 taught magnitude and unit direction. A direction of length one lets us measure how far a vector reaches along a line without accidentally multiplying by the length of the direction arrow.

## Build the idea

An angle measures a turn. A full turn is 360 degrees (360°); a right angle is 90°. In a right triangle, the hypotenuse is opposite the right angle. Relative to an acute angle theta, the leg touching that angle is adjacent and the other leg is opposite. Define cos(theta) = adjacent/hypotenuse and sin(theta) = opposite/hypotenuse. Similar triangles preserve these ratios. Thus a vector of length L making an acute angle theta above positive x has components (L cos(theta), L sin(theta)). In a 3-4-5 triangle, an angle with adjacent leg 3 and opposite leg 4 has cosine 3/5 and sine 4/5.

For larger angles, define cosine and sine as the x and y coordinates of a unit arrow measured counterclockwise from positive x. This extends the right-triangle definitions while preserving signs. At 0°, (cos,sin) = (1,0); at 90°, (0,1); at 180°, (-1,0). Therefore a projection may be negative: it points against the chosen positive direction. These exact values and the 3-4-5 ratios are introductory examples. Other right triangles use the same definitions, including exact square-root lengths in the capstone; no table lookup or inverse trigonometric function is required.

The dot product of v = (v_x,v_y) and w = (w_x,w_y) is the scalar v·w = v_x w_x + v_y w_y. A scalar is one number with its unit, rather than a directed pair. In perpendicular equal-scale axes this product also equals |v||w|cos(theta), where theta is the angle between the arrows. To understand its directional meaning, take a unit arrow u. The horizontal piece (v_x,0) contributes v_x u_x along u, and the vertical piece (0,v_y) contributes v_y u_y. Adding these contributions gives v·u, the signed length along u. This is the scalar projection s_parallel.

For a nonzero direction d, normalize first: u = d/|d|. Then

- scalar projection: s_parallel = v·u = (v·d)/|d|;
- vector projection: p = s_parallel u = [(v·d)/(d·d)]d;
- residual vector: r = v - p, so v = p + r.

The scalar tells signed distance; the vector tells the actual arrow along the line. The residual is the perpendicular part and must be retained to reconstruct v. Indeed r·u = v·u - s_parallel(u·u) = s_parallel - s_parallel = 0. A zero dot product with a nonzero direction means perpendicular. If d has length units, v·d has squared length units and the formula still gives p in length units. If d is dimensionless, the same formula is valid with the corresponding unit cancellation. Never project onto d = 0.

## Fully worked synthetic example

Let v = (4,3) m and let the dimensionless direction be d = (2,0). Its magnitude is 2, so u = (1,0). The scalar projection is (4×2+3×0)/2 = 4 m. The vector projection is (4 m)(1,0) = (4,0) m. The retained residual is (0,3) m. Check v = (4,0)+(0,3) = (4,3) m and r·u = 0.

The original vector has length 5 m. Relative to positive x, cos(theta) = 4/5 and sin(theta) = 3/5. Thus the same parallel distance is 5×4/5 = 4 m and the vertical distance is 5×3/5 = 3 m. Merely using v·d = 8 m would double the scalar projection because d is not unit length.

## Guided practice: a tilted direction

Let v = (5,0) m and d = (3,4), dimensionless. Then |d| = 5, u = (3/5,4/5), and s_parallel = (15+0)/5 = 3 m. The projection is p = (9/5,12/5) m and r = (16/5,-12/5) m. Check reconstruction: (25/5,0) = (5,0) m. Check perpendicularity: r·d = (48/5-48/5) m = 0. Both components of r matter even though r is perpendicular to d.

> **Claim scope:** Projection is a derived geometric transform, not a physical removal of a component or an explanation of a force. We retain p and r together. Sine, cosine, and dot products here use the perpendicular background axes; tilted coordinate pairs require additional care in Lesson 05.

## Diagnostic checks

In these checks every direction d is dimensionless.

1. A right triangle has adjacent leg 4, opposite leg 3, and hypotenuse 5. Give cosine and sine, and the components of a 10 m vector at that angle.
2. Project v = (-2,5) m onto d = (0,3). Give scalar projection, vector projection, residual, and a reconstruction check.
3. For v = (3,4) m and d = (3,4), compute |d|, the scalar projection, and the vector projection. Explain why v·d alone is not the scalar projection.
4. What happens for v = (-4,0) m along d = (1,0)? What happens if d = (0,0)?

## Worked answers

1. Cosine = 4/5, sine = 3/5; components (8,6) m, whose magnitude is sqrt(64+36) = 10 m.
2. |d| = 3, u = (0,1), s_parallel = 5 m, p = (0,5) m, r = (-2,0) m. Their sum is (-2,5) m and r·u = 0.
3. |d| = 5; v·d = 25 m, scalar projection = 25/5 = 5 m; vector projection = 5(3/5,4/5) = (3,4) m. The extra factor |d| must be removed.
4. Scalar projection is -4 m, vector projection (-4,0) m, and residual zero. The zero direction cannot be normalized, so its projection is undefined.

**Next dependency:** [Lesson 05](lesson-05.md) builds a displacement from two ordered direction columns. Those coordinate coefficients are generally different from projections.
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Lesson 05 — Matrices as coordinate machines

**Essential question:** How can two ordered arrows encode and recover a displacement?

**Goals:** Interpret a two-column matrix as an ordered combination of arrows; calculate a forward coordinate conversion; recover inputs by solving two equations and verify both directions.

**Prerequisite bridge.** Lessons 03–04 taught vector addition, multiplication by a scalar, and projection. Those operations let us combine two arrows. Solving a pair of linear equations means finding numbers that satisfy both equations at once; substitution will be shown before any inverse formula is used.

## Build the idea

Choose two ordered arrows b1 and b2 that do not lie along the same line. They form a basis for the plane: every displacement can be made in exactly one way by combining them. A coordinate column q = (q1,q2) means “q1 copies of b1, plus q2 copies of b2.” Here q is dimensionless and each basis column is a length vector in metres. Thus the output is a displacement in metres.

A matrix is a rectangular arrangement of numbers. Write our synthetic basis as B = [b1 b2], with the arrows as columns, not rows. We show it compactly as B = [[2,1],[0,1]] m, meaning first row (2,1), second row (0,1). Its columns are b1 = (2,0) m and b2 = (1,1) m. Multiplication Bq means q1 b1 + q2 b2, so its components are (2q1+q2, q2) m. Reading columns as rows would change that operation.

B converts local coefficients into a background displacement, not directly into a point. With origin O, the point is P = O + Bq. To recover q from P, first subtract O. Keeping the origin separate avoids treating coordinates as displacements from the wrong location.

Coordinates in a tilted basis are not ordinary perpendicular-axis projections. For example b2 has background components (1,1) m but local coefficients (0,1). Its length is sqrt(2) m; taking the square root of 0²+1² would not give that physical length. To find lengths in this course, first convert to the perpendicular background axes and then use Lesson 03.

## Fully worked synthetic example

Take B = [[2,1],[0,1]] m and input q = (3,-2). Forward conversion gives 3(2,0) m - 2(1,1) m = (4,-2) m. Let O = (10,5) m. Then P = (14,3) m.

Now recover the input without assuming an inverse formula. Subtract the origin: P - O = (4,-2) m. Equating components gives 2q1+q2 = 4 and q2 = -2 after cancelling metres. Substitute the second equation into the first: 2q1-2 = 4, so 2q1 = 6 and q1 = 3. We have recovered (3,-2). Substituting back gives (4,-2) m again; adding O recovers (14,3) m. These are the reverse and forward checks.

The physical length of Bq is sqrt(4²+(-2)²) m = sqrt(20) m. Keep this exact form. The coefficient length sqrt(3²+(-2)²) is not the physical length because this basis is tilted and differently scaled.

> **Claim scope and source connection:** B in this lesson is an explicitly synthetic two-dimensional column basis. It is not the source-locked three-dimensional Cell3 B. S02, `/typed_conventions/basis`, requires ordered ICRS columns [a b c] and intentional left-handedness, with no silent transpose or axis permutation. Those are context labels here, not additional calculations. The practical lesson is to declare and preserve the column order.

## Guided practice

Using the same B, convert q = (-1,3): -1(2,0)+3(1,1) = (1,3) m. Recover from x = (1,3) m: q2 = 3, then 2q1+3 = 1, so q1 = -1. If the origin is (-2,1) m, the corresponding point is (-1,4) m. Subtracting the origin returns (1,3) m.

## Diagnostic checks

1. Give the two columns of B = [[2,1],[0,1]] m and compute B(2,1).
2. Recover q from Bq = (7,3) m by substitution. Check forward.
3. With O = (5,-1) m and P = (8,1) m, recover q for this B and reconstruct P.
4. If you swap the two basis columns, what input order must accompany the swap to keep B(3,-2) unchanged? Is q1 a scalar projection onto b1?

## Worked answers

1. b1 = (2,0) m, b2 = (1,1) m; 2b1+b2 = (5,1) m.
2. q2 = 3; 2q1+3 = 7 gives q1 = 2. B(2,3) = (7,3) m.
3. P-O = (3,2) m. q2 = 2 and 2q1+2 = 3, hence q1 = 1/2. O+B(1/2,2) = (5,-1)+(3,2) = (8,1) m.
4. Swap to input (-2,3), so the same arrow weights stay attached to the same arrows. In general q1 is a basis coefficient, not a projection: the other tilted column also contributes horizontally.

**Next dependency:** [Lesson 06](lesson-06.md) explains precisely when recovery is possible, how orientation is recorded, and how an inverse formula follows from two equations.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# Lesson 06 — Area, orientation, and determinants

**Essential question:** How can one signed number tell whether a coordinate converter preserves a whole plane?

**Goals:** Compute and interpret a two-dimensional determinant; recognize a singular converter and explain its lost information; derive and apply an inverse only when its determinant is nonzero.

**Prerequisite bridge.** Lesson 05 recovered coordinates by solving two equations. That worked because the two basis arrows span a plane. We now test this condition before dividing by anything, and connect it to Lesson 02's area scale factors.

## Build the idea

For B = [[a,b],[c,d]], its ordered columns are (a,c) and (b,d). Define the determinant D = ad - bc. Here a,b,c,d are local scalar entry names; they are not the three named Cell3 vectors. When the entries have metres as units, D has square metres as units. The parallelogram formed by the two arrows has area |D|. Area is nonnegative; the determinant also retains orientation.

Why this formula? The signed area contributed by the horizontal part a of the first arrow and the vertical part d of the second is ad. The vertical part c of the first and horizontal part b of the second contributes the opposite orientation, so it subtracts bc. Equivalently, for a nonvertical first arrow, shear vertically by subtracting (c/a) times each x component from its y component. This moves every vertical slice up or down without changing its height or area. The first arrow becomes (a,0), and the second becomes (b,d-cb/a). Base times signed height is a(d-cb/a) = ad-bc. The case a = 0 can be handled by exchanging axes and tracking the sign; the same expression results. This explains both the magnitude and the sign rather than assigning a negative ordinary area.

Relative to positive x right and positive y up, D > 0 means the shorter turn from the first column to the second is counterclockwise, and D < 0 means clockwise. Swapping columns reverses D because bc-ad = -(ad-bc). Uniformly multiplying both columns by a positive factor s multiplies D by s², matching Lesson 02. With a dimensionless matrix, |D| is an area multiplier; with columns in metres per dimensionless coordinate unit, |D| is the physical area of one coordinate-unit square.

D = 0 means the columns lie on the same line, or one is zero. Such a matrix is **singular**: different inputs can have the same output, so a unique inverse does not exist. **Nonsingular** means D ≠ 0; then each displacement has exactly one input.

To derive recovery, write X = aq1+bq2 and Y = cq1+dq2. Multiply the first equation by d and the second by b and subtract: dX-bY = (ad-bc)q1. Similarly, subtract c times the first equation from a times the second: aY-cX = (ad-bc)q2. If D ≠ 0, divide:

q1 = (dX-bY)/D, and q2 = (-cX+aY)/D.

These two rules form the inverse matrix B^-1 = (1/D)[[d,-b],[-c,a]]. The notation -1 here means undoing the matrix operation, not taking the reciprocal of each entry. For B in metres and input displacements in metres, B^-1 has units m^-1 and the recovered q is dimensionless. This derivation also proves uniqueness: every solution must have these same two values.

## Fully worked synthetic example

Let B = [[1,2],[2,0]] m. Its columns are (1,2) m and (2,0) m. D = (1×0-2×2) m² = -4 m². The parallelogram area is 4 m² and the orientation is negative; the sign is intentional, not a calculation fault.

For q = (2,-1), Bq = (0,4) m. Recover q using X = 0 m and Y = 4 m:

q1 = (0×0-2×4)/(-4) = 2; q2 = (-2×0+1×4)/(-4) = -1, with squared metre units cancelling in each ratio. Thus B^-1 = [[0,1/2],[1/2,-1/4]] m^-1. Check the reverse and forward paths: B^-1(0,4) m = (2,-1), and B(2,-1) = (0,4) m.

## Singular counterexample and guided practice

Let S = [[1,2],[2,4]] m. Its second column is twice its first and det(S) = 4-4 = 0 m². Both inputs (2,0) and (0,1) give (2,4) m. More generally (q1,q2) and (q1+2t,q2-t) give the same output for any scalar t. If the input is discarded, the output alone cannot recover which value of t occurred. Keep the input or this additional coordinate; do not claim that this transformation is reversible by itself. The displacement (1,0) m cannot be an output because every output satisfies Y = 2X.

> **Claim scope:** Negative determinant, singularity, and projection residuals are distinct concepts. A negative determinant does not imply lost information; zero determinant does. S02's intentional left-handed Cell3 convention is not “repaired” by changing a sign. Our example is two-dimensional and synthetic, not a fresh calculation of Cell3 geometry.

## Diagnostic checks

1. Find determinant, area, and orientation of [[2,1],[0,1]] m.
2. Swap the columns of [[1,2],[2,0]] m. What changes and what stays the same?
3. Use the inverse of the worked example to recover q for (6,4) m; then check forward.
4. Explain why [[1,3],[2,6]] m is singular and give two distinct inputs with the same output.

## Worked answers

1. D = 2×1-1×0 = 2 m²; area 2 m² and positive orientation.
2. The matrix becomes [[2,1],[0,2]] m. D becomes +4 m²; the physical parallelogram and its area stay the same, but the column order and orientation change.
3. q1 = 0×6+(1/2)×4 = 2; q2 = (1/2)×6-(1/4)×4 = 2. B(2,2) = (2+4,4) m = (6,4) m.
4. D = 6-6 = 0 m² and column 2 is three times column 1. Inputs (3,0) and (0,1) both give (3,6) m, so no unique inverse is possible.

**Next dependency:** [Lesson 07](lesson-07.md) combines origin, column order, units, inverse, and retained rounding residuals into a complete calculation contract.
<!-- END: lesson-06 -->

<!-- BEGIN: lesson-07 -->
# Lesson 07 — From a drawing to a typed calculation

**Essential question:** What must another person know to reproduce and reverse your coordinate calculation?

**Goals:** Write an unambiguous coordinate contract; perform and check an affine forward/reverse conversion; declare a rounding tie rule and preserve its residual for exact reconstruction.

**Prerequisite bridge.** You can convert units, subtract an origin, multiply ordered columns, test a determinant, and recover coefficients. A drawing suggests these objects but does not specify them completely. This lesson makes every choice explicit.

## Build the idea

A **typed calculation** identifies the kind, units, and ordering of each input and output. Before calculating, state: the background axes and their order; which pairs are points versus displacements; the origin; the matrix's columns and units; the coordinate coefficient units; and the exact-versus-displayed convention. An **affine** converter combines a linear basis conversion with an origin shift: P = O + Bq. Its reverse is q = B^-1(P-O) when det(B) ≠ 0. Subtract O before the inverse; adding O is not part of multiplication by B.

A drawing should label positive axes, origin, units, and the two arrows in column order. In a typed input record, “B = [[1,2],[2,0]] m” means rows are written in the outer brackets and columns are the basis arrows (1,2) m and (2,0) m. State this even if the drawing looks obvious. Preserve the sign of the determinant. A reflection or column swap changes the contract.

For classroom decimal display we use **nearest tenth, ties away from zero**: choose the closest multiple of 0.1, and at an exact halfway value choose the one with larger absolute value. Thus 1.25 becomes 1.3; -1.25 becomes -1.3; 1.24 becomes 1.2. Apply this separately to each component. Keep exact rational values through the calculation. If q_hat is the displayed pair, define the rounding residual e = q - q_hat. Then q = q_hat + e and P = O + Bq_hat + Be. Multiplying the residual by B expresses the omitted display component in background length units.

Under this tie rule, a scalar tenth-rounding residual lies in [-0.05,0.05]. At a positive half-tie it is -0.05, and at a negative half-tie it is +0.05. This closed bound is not a cell-ownership interval. In particular this classroom operation does not define the source's nearest-integer convention or the half-open Cell3 ownership rule. Retain the exact input and signed residual, not only the bound.

## Fully worked synthetic example

Contract: perpendicular background axes ordered (x,y), x right and y up; all points and displacements in metres; origin O = (10,-1) m; B = [[1,2],[2,0]] m with columns as written; coefficients q dimensionless; exact arithmetic internally, nearest tenth with ties away from zero only for display.

Let q = (5/4,-3/4) = (1.25,-0.75). Forward: Bq = (5/4-6/4, 10/4) m = (-1/4,5/2) m. Add O: P = (39/4,3/2) m = (9.75,1.5) m. The determinant remains -4 m². Reverse: P-O = (-1/4,5/2) m; q1 = (1/2)(5/2) = 5/4, and q2 = (1/2)(-1/4)-(1/4)(5/2) = -1/8-5/8 = -3/4.

Display q_hat = (1.3,-0.8). The signed residual is e = (-0.05,0.05) = (-1/20,1/20). Its background image is Be = (1/20,-1/10) m = (0.05,-0.1) m. The display-only point is O+Bq_hat = (9.7,1.6) m. Restoring the residual gives (9.7,1.6)+(0.05,-0.1) = (9.75,1.5) m, exactly the original point. Rounding changed the displayed coordinate but did not authorize erasing the omitted information.

> **Claim scope:** This complete converter is an exact synthetic classroom model. In source context, S02 `/typed_conventions/metric_symbols` distinguishes M_cell = B^T B, R_cell = M_cell^-1, and G_phase. These names are recognition-only here: T means transpose (exchange rows and columns), M_cell names a length-metric construction, R_cell its inverse, and G_phase a distinct phase metric. No metric calculation or physical identification using them is required in this course. Source B must be bound to its own definition; our example does not replace it. Other advanced invariant names remain in the input contract for later courses.

## Guided practice

For the same O and B, let P = (11,2) m. Subtract O to get (1,3) m. Recover q = (3/2, 1/2-3/4) = (1.5,-0.25). Nearest-tenth display gives (1.5,-0.3), residual (0,0.05), and background residual (0.1,0) m. The display-only point (10.9,2) m plus (0.1,0) m recovers P. A value already at a tenth, such as 1.5, has zero rounding residual.

## Diagnostic checks

1. List the missing information in “multiply the coordinates by the matrix and round.”
2. Under the stated rule, round 2.25, -2.25, and 2.24 to tenths and retain each residual.
3. For the worked-example O and B, recover q from P = (12,3) m and reconstruct P. State units at every stage.
4. In the worked example, reconstruct q and P from q_hat and e. What is wrong with reporting only the magnitude of e?

## Worked answers

1. It does not identify axes/order, whether coordinates are points or displacements, origin, matrix entries/column order, units, rounding precision/tie rule, or preserved exact values and residuals. Any of these can change the result or prevent reconstruction.
2. Displays: 2.3, -2.3, 2.2. Residuals exact-minus-display: -0.05, +0.05, +0.04. Adding each residual restores the original.
3. P-O = (2,4) m. B^-1 has units m^-1; q = (2, 1-1) = (2,0), dimensionless. Bq = (2,4) m; O+Bq = (12,3) m.
4. q = (1.3,-0.8)+(-0.05,0.05) = (1.25,-0.75). P = (9.7,1.6)+(0.05,-0.1) = (9.75,1.5) m. A magnitude keeps only size and loses signs and direction, so it cannot reconstruct either component.

**Next dependency:** The [capstone](capstone.md) asks you to write and test your own converter specification using this complete sequence, including projection and residual accounting.
<!-- END: lesson-07 -->
