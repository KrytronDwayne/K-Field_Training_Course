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


