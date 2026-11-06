# The galaxy-derived cell

Essential question: How does a phase address become a geometric center?

Goals: Multiply a column basis by an address; recover an address using reciprocal rows; distinguish phase, origin, basis and inverse metric units.

Prerequisite bridge. Lesson 02 supplied one reciprocal row. Now put several rows together so that one point has several simultaneous addresses. Two periods separate reconstruction from types and boundary rules.

## C29.03-E1 — A matrix is an organized set of operations

For a two-dimensional example, let columns a and b be two independent step vectors. The matrix A=[a b] acts by `A(t₁,t₂)=t₁a+t₂b`. In three dimensions add t₃c. This definition teaches matrix-vector multiplication without a new rule to memorize. An inverse A⁻¹ reverses the operation: A⁻¹(At)=t. It exists only when the columns give independent directions. The identity matrix I leaves a vector unchanged. `diag(2,3)` has diagonal entries 2,3 and zeros elsewhere.

A transpose, superscript T, exchanges rows and columns. G01 stores reciprocal **columns** in Q_gal, so the reading rows are Q_galᵀ. Their defining relation is Q_galᵀ A_gal=I. G04 calls that row matrix R; here call it R_gal_rows to distinguish it from an inverse Gram metric. Its rows recover the amount of each basis step. Dotting reciprocal column j into direct column i gives 1 when i=j and 0 otherwise.

For phase offset phi and integer label k, the center is `c_k=A(k+phi)`. Phi is an address offset, dimensionless. The zero-index center is A phi in reconstruction-length units. The coordinate origin x=0, the zero-index center A phi, and phi are three different objects. For general x, t=A⁻¹x-phi is the continuous address relative to the center lattice. Retain t and any residual used in assigning an integer center.

Units provide a quick check. If A is in L, A⁻¹ and Q are in 1/L, while addresses and phi are dimensionless. The Gram matrix M=AᵀA contains dot products of basis columns and has units L². Its inverse M⁻¹ has units 1/L². An inverse basis and an inverse metric cannot be substituted for one another.

## C29.03-W1 — Phase-center worked example

Take synthetic A=I₂ L, phi=(1/4,1/2), k=(1,-1). First add addresses: k+phi=(5/4,-1/2). Multiplication by A gives c_k=(5/4,-1/2)L. Set k=0 instead and the center is A phi=(1/4,1/2)L. Recover the label by A⁻¹c_k-phi=(5/4,-1/2)-(1/4,1/2)=(1,-1). Nothing was lost.

## C29.03-P1 — Guided practice and answer

Use A=diag(2,3)L with the same k and phi. Its columns are (2,0)L and (0,3)L, so c_k=(2·5/4,3·(-1/2))L=(5/2,-3/2)L. The zero-index center is (1/2,3/2)L. Reciprocal rows are (1/2,0)/L and (0,1/3)/L. They recover (5/4,-1/2). Subtract phi to recover k. Dot products of columns give M=diag(4,9)L²; M⁻¹=diag(1/4,1/9)L⁻². Notice the reciprocal row entries were not squared until forming the inverse metric.

## Source card: orientation and precision

G01#/ordered_direct_basis_A and /reciprocal_basis_Q are the frozen galaxy matrices; their exact entries remain at their original hashed path in [sources](sources.md). Columns, not rows, are the primitive vectors. G01#/joint_phase_origin is approximately (0.47,0.45,0.568033984452736), a phase address. This displayed rounding is for reading only; the verification script loads full stored values. The galaxy determinant is positive, approximately 0.006245061651 in cubed reconstruction units. S02#/mature_locked_cell3/det_B_nm3 is -0.11791489191174465 nm³.

A determinant measures signed volume. For a 2×2 array [[a,b],[c,d]], it is ad-bc; for a diagonal 3×3 array it is the product of the diagonal entries. A positive versus negative sign specifies the orientation of the ordered basis relative to the fixed coordinate frame. Volume is the absolute determinant. Reflecting or swapping columns can change this sign; do not do so silently to “match” the sources. The ICRS frame is shared, while basis handedness differs.

> Claim scope. The galaxy lengths are unit-sphere reconstruction lengths, with no supplied radial calibration (G02 p4; G04 pp3–4). L in our examples is an abstract teaching length, not a parsec or a nanometer. Algebraic QᵀA=I is exact by definition; recomputation from stored decimal matrices has a closure residual that must be recorded rather than erased.

## Ownership is a separate convention

For the mature Cell3 address t=B⁻¹(x-O_K), subtract the declared physical origin O_K first. Half-open ownership takes z=floor(t+1/2) componentwise and u=t-z in [-1/2,1/2). Floor means the greatest integer no larger than the argument. At t=1/2, z=1 and u=-1/2; at t=-1/2, z=0 and u=-1/2. This explicitly assigns a shared wall to one cell. The corresponding nearest-integer half-tie goes toward the larger integer for this coordinate rule. Other residual sign conventions need their own intervals. This ownership partition does not certify the physically closest center in a skew cell; lesson 05 will test that distinction.

## Diagnostics — C29.03-D1

1. With A=diag(2,3)L, what are the units of phi and A phi?
2. Multiply the first reciprocal row by each direct column.
3. Is M⁻¹=A⁻¹ in the practice example?
4. For t=-3/2, find z and u under the declared ownership rule.

Worked answers. 1. Phi is dimensionless; A phi has units L. 2. (1/2,0)·(2,0)=1 and (1/2,0)·(0,3)=0. 3. No: diag(1/4,1/9)L⁻² differs from diag(1/2,1/3)L⁻¹. 4. z=floor(-1)=-1 and u=-3/2-(-1)=-1/2, retaining t=z+u.

Next: [lesson 04](lesson-04.md) compares what follows from any independent basis and what remains source-specific.
