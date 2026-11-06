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
