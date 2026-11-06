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
