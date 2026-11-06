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
