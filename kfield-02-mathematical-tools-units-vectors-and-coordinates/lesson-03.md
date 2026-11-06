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
