# Galactic Structure and Cross-Scale K-Field Geometry

Student lessons in approved dependency order. Supporting source cards, glossary, teacher guide and capstone are separate course artifacts.

<!-- BEGIN: lesson-01 -->
# Sky positions and projective axes

Essential question: What information changes when a sky direction is treated as an axis?

Goals: Convert simple sky angles into vectors; calculate directed and axial separations; identify what each observation supplies.

Prerequisite bridge. You need signed arithmetic, coordinate graphs, and the ability to square and take a positive square root. Earlier courses 04, 06, 10, 22, 24 and 26 supply coordinate and evidence-reading experience. The operations used here are rebuilt locally. A vector is an ordered list of components: (1,0,0) means one step along the first axis and none along the others. Its length is sqrt(x²+y²+z²). A unit vector has length one.

## C29.01-E1 — An arrow and an undirected line

Imagine pointing at a galaxy from the observer. The arrow gives a direction. It does not tell you how far along that arrow the galaxy lies. All positive multiples of the arrow point the same way; dividing by its length places its tip on a sphere of radius one. Keep any supplied distance separately so that this normalization can be reversed. If distance was never supplied, mark it missing rather than inventing it.

The ICRS coordinate convention used by G03 and G04 has x toward right ascension (RA) 0°, declination (Dec) 0°; y toward RA 90°, Dec 0°; and z toward the north celestial pole. RA, denoted alpha, goes around the equator; Dec, denoted delta, measures elevation above it. On a unit circle, cosine is the horizontal coordinate and sine is the vertical coordinate. Thus the horizontal projection has length cos(delta), and the height is sin(delta):

`x = (cos(delta)cos(alpha), cos(delta)sin(alpha), sin(delta))`.

For the core calculations use sin(0°)=0, cos(0°)=1, sin(90°)=1, cos(90°)=0, sin(180°)=0 and cos(180°)=-1. The formula uses angles consistently in degrees here. Later loop phases use radians, where one full turn is 2π radians = 360°.

An **unoriented axis** is the pair {x,-x}: it records a line but not which end is positive. An intrinsic galaxy axis describes the galaxy's orientation; its sky position describes where it appears. One is not supplied by the other. A **projective view** deliberately identifies the two ends for a specified calculation. Store the original arrow or its sign alongside that view.

The dot product multiplies corresponding components and adds: x·y=x₁y₁+x₂y₂+x₃y₃. For unit vectors it equals the cosine of their directed angle. `arccos(t)` means the angle from 0° through 180° whose cosine is t. Directed separation is arccos(x·y); axial separation is arccos(|x·y|). Absolute value removes the sign only in the axial calculation. For dot products 1,0,-1 the directed angles are 0°,90°,180°.

## C29.01-W1 — Worked example

RA 0°, Dec 0° gives (1·1,1·0,0)=(1,0,0)=e_x. RA 180°, Dec 0° gives (-1,0,0)=-e_x. Both have length one. Their dot product is -1, so directed separation is 180°. The absolute dot product is 1, so axial separation is 0°. If only the axis were saved, these two different sky positions could no longer be distinguished.

> Source scope. G04 pp1,3 reports 114,381 unique directed sky positions with no radial distance inferred. Its discovery operators used antipodal completion, while final fitting and assignments used the actual directed vectors. G02 p3 explicitly distinguishes this sky-position pathway from an earlier galaxy-axis pathway. These are source-reported observational and analysis facts; our three-coordinate examples are synthetic teaching examples.

## C29.01-P1 — Guided practice and answer

Compute RA 90°, Dec 0° and compare it with e_x in both views. The vector is (0,1,0)=e_y. Its dot product with e_x is zero, so both angles are 90°. An antipodal discovery view may include -e_y, but the observation record still says e_y. Preserve the object identifier and original direction.

## Diagnostics — C29.01-D1

1. Does (1,0,0) locate a galaxy at a known physical distance?
2. For e_z and -e_z, find directed and axial angles.
3. Can sky position alone identify the galaxy's own unoriented axis?
4. What must be retained when forming a projective discovery view?

Worked answers. 1. No: it specifies an arrow on the unit sphere; a radial-distance field is missing. 2. The dot product is -1, giving 180° directed and 0° axial. 3. No: the intrinsic orientation needs its own observation. 4. Retain the original direction and identity, plus the transformation and its scope; a sign can reconstruct a representative only when the chosen representative is also fixed.

Next: [lesson 02](lesson-02.md) uses the dot product to distinguish a historical response from a reciprocal plane address.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Spherical response and phase addresses

Essential question: How can similar-looking formulas describe different operations?

Goals: Evaluate a finite response card; flag undefined branches before division; compute a reciprocal address without treating phase as force.

Prerequisite bridge. Lesson 01 taught unit vectors, dot products and radians. A normal is a vector perpendicular to a plane. The dot product with a unit normal measures the signed component along it. A zero dot product means the vectors are perpendicular. This lesson takes two periods: response and address first, domain and parity second.

## C29.02-E1 — Follow the contract of each map

An input-output rule needs a domain, units and a source. G03 is a historical Cell3 spherical-response construction. It is not the galaxy cell of G04. Here is the complete response card needed for our finite exercises:

| Symbol | Meaning and rule |
|---|---|
| n, N | unit direction and unit sheet normal |
| h | positive half-step sheet spacing, units L |
| nu | odd lock order, nu=2r+1 for integer r |
| u | n·N, dimensionless |
| kappa | nu π/(h u), units 1/L, defined only if u≠0 |
| q_resp | kappa n, reciprocal-length vector |
| s_ab,s_ac,s_bc | loop displacement vectors in L, with s_ac=s_ab+s_bc |
| psi_ij | q_resp·s_ij, a dimensionless radian phase |
| F | sqrt(3+2cos(psi_ab)+2cos(psi_ac)+2cos(psi_bc))/3 |
| D | sum over ab,ac,bc of w_ij[1-cos(psi_ij)], w_ij=abs(R_local,ij) |
| G_star | D/F, defined only when F≠0 and previous fields exist |

`sum` instructs you to add the three terms. The weights are nonnegative and inherit their units from the historical local reciprocal metric. F is dimensionless, so G_star has D's units. The source calls G_star an unscaled relative response; an absolute gravity calibration is undefined. Synthetic weights in this course use a declared relative response unit U_D, not a measured force unit.

The phases must respect loop closure: psi_ac=psi_ab+psi_bc before reduction by full turns. A cosine repeats after 2π. A supplied triple cannot be treated as geometrically realized merely because its three cosines can be evaluated. For a negative square-root argument, flag an inconsistent card or precision issue; do not silently replace it with zero.

G04 p4 has a different map. Its reciprocal vector q_j=n_j/Delta_j has length inverse to its plane spacing Delta_j. Points on plane k_j satisfy `q_j·x=k_j+phi_j`, where k_j is an integer and phi_j is the phase offset measured in **cycles**, not radians. Multiply cycles by 2π to express a radian phase. At a general point, q_j·x-phi_j need not be an integer. That difference is a continuous address, with its fractional component retained. We use q_resp and q_j to avoid a collision between the two source-local uses of q.

## C29.02-W1 — Worked example

Synthetic response: n=N=e_z, h=1L, nu=1. Then u=1, kappa=π/L and q_resp=(0,0,π/L). Choose loop displacements perpendicular to e_z and obeying closure, so all loop phases are zero. Since cos(0)=1, F=sqrt(3+2+2+2)/3=1. Each term in D is w(1-1)=0, hence D=0 and G_star=0 U_D.

Separately, a synthetic reciprocal row q₁=(1,0)/L acting on x=(5/4,0)L gives q₁·x=5/4 cycles. With phi₁=1/4, the plane label is k₁=1. The L units cancel. This is an address calculation, not a response or a force.

## C29.02-P1 — Domain practice and answers

Case A: n=e_x and N=e_z. Their dot product is zero, so kappa and q_resp are undefined. Save the input vectors and a `u_zero` flag with null response fields.

Case B: consider closure-consistent loop phases (psi_ab,psi_ac,psi_bc)=(2π/3,4π/3,2π/3). Their cosines are all -1/2, giving F=sqrt(3-1-1-1)/3=0. With all three weights 1 U_D, D=3(1+1/2)=9/2 U_D. G_star is undefined, with a `transfer_zero` flag. Even if a different card gave D=0 too, 0/0 would remain undefined. The blueprint's all-2π/3 triple is repaired here because it violates loop closure; this is an algebraic domain demonstration, not a replay of G03's frozen geometry.

Case C: a separately stipulated regular transfer has D=2 U_D and F=1/2. G_star=2/(1/2)=4 U_D. Keep its synthetic label.

> Scope and precision. G03#/precision_contract specifies IEEE-754 binary64 arithmetic, phase reduction to [-π,π), null undefined values and separate flags. These classroom calculations use exact symbolic angles; a numerical residual near zero is retained separately from an exact domain statement. No historical G03 coefficient replaces the mature S02 lock.

## Antipodal parity

Reverse n while keeping N fixed. Then u changes sign and kappa changes sign. Their product q_resp=kappa n keeps its value: two sign changes cancel. Thus loop phases, F, D and G_star are even under this antipodal operation where defined. “Odd” means sign-reversing; “even” means unchanged. This response parity does not identify antipodal sky positions or any other kind of parity.

## Diagnostics — C29.02-D1

1. A reciprocal row is (0,2)/L and x=(0,3/4)L. With phi=1/2, what is k?
2. Which fields fail first when u=0?
3. Does antipodal reversal change q_resp? Show the signs.
4. What is wrong with reporting G_star in newtons from this card?

Worked answers. 1. The dot product is 3/2; subtract 1/2 to obtain k=1. 2. Division by u makes kappa undefined, so downstream q_resp and phases are unavailable; retain all inputs. 3. (-kappa)(-n)=kappa n, unchanged. 4. No force calibration or force unit has been supplied; relative response and phase do not establish a force law.

Next: [lesson 03](lesson-03.md) combines reciprocal rows into one reconstructible address system.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
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
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
# Shared grammar and distinct metrics

Essential question: Which shared constructions survive when the basis changes?

Goals: Verify root closure and orthogonality; compare two typed metrics; distinguish a common algebraic construction from a physical identification.

Prerequisite bridge. Lesson 03 taught column bases, transposes, inverses and the Gram matrix. We now subtract basis steps and ask which formulas remain true for every independent basis. The first period develops closure; the second compares source roles and units.

## C29.04-E1 — Different routes to the same sheet

An integer address (i,j,k) records steps along a,b,c. Its sum lambda=i+j+k labels a sheet. A change such as (1,-1,0) has sum zero and stays in that sheet. The set of integer changes with sum zero is called the A2 address lattice here. “Rank two” means two independent changes suffice: every (i,j,k) with sum zero equals i(1,0,-1)+j(0,1,-1). This is a concrete operational definition; no abstract algebra is needed.

In the local half-step window a primitive lift is a/2, b/2 or c/2. Here i,j,k count half-steps: the corresponding full-step address is (i,j,k)/2, and the local sheet label lambda=i+j+k is twice its full-step coordinate sum. Each primitive lift increases this local label by one. Taking one lift forward and another backward produces an in-sheet displacement, called a root or elementary holonomy displacement in G02:

`s_ab=(a-b)/2`, `s_bc=(b-c)/2`, `s_ac=(a-c)/2`.

Add the first two expressions. The -b and +b cancel, giving `(a-c)/2=s_ac`. This closure identity holds for any three vectors, not only a fitted galaxy cell. It does not force their lengths or angles to agree.

The vector `g=A⁻ᵀ(1,1,1)` uses inverse transpose: transpose the inverse, then multiply. It satisfies g·a=g·b=g·c=1 by reciprocity. Hence g·s_ab=(1-1)/2=0, and similarly for the other roots. Thus g points perpendicular to the root sheet. Dividing g by its length gives a unit normal N. With `h=1/(2||g||)`, each primitive half-step has normal component h. Its remainder t_a=a/2-hN is the in-sheet slip; recover a/2 by adding hN+t_a. No component is discarded.

## C29.04-W1 — Worked comparison

Synthetic A=diag(1,2,3)L gives a=(1,0,0)L, b=(0,2,0)L and c=(0,0,3)L. Therefore s_ab=(1/2,-1,0)L, s_bc=(0,1,-3/2)L and s_ac=(1/2,0,-3/2)L. Adding the first two gives the third component by component.

Here g=(1,1/2,1/3)/L. Its dot product with s_ab is 1/2-1/2=0; with s_bc it is 1/2-1/2=0; with s_ac it is 1/2-1/2=0. The Gram metric is diag(1,4,9)L². It describes lengths and angles that closure alone did not specify.

## C29.04-P1 — Guided practice and answer

Change to synthetic A'=diag(2,1,4)L. Compute roots and metric. The roots are (1,-1/2,0)L, (0,1/2,-2)L and (1,0,-2)L, again closing. The metric becomes diag(4,1,16)L², different from the previous metric. The new perpendicular vector is g'=(1/2,1,1/4)/L; for example g'·s'_ab=1/2-1/2=0. The two normals are not parallel because their component ratios are not all equal. Shared closure has not identified their directions.

Now classify a proposed ratio “galaxy sheet spacing divided by Cell3 spacing in nm.” The numerator is an uncalibrated unit-sphere reconstruction length, the denominator a physical length. It is not an admitted physical scale ratio. A galaxy radial calibration and a declared mapping would be needed. Dimensionless comparisons formed separately within each cell can still be meaningful.

## Source comparison card

| Contract | Galaxy cell | Mature Cell3 |
|---|---|---|
| Basis | A_gal, G01, ICRS columns | B, S02#/mature_locked_cell3, ICRS columns |
| Length type | unit-sphere reconstruction | nm in the locked record |
| Handedness | positive determinant | intentional negative determinant |
| Origin use | c_k=A_gal(k+phi) | x-O_K in affine addresses |
| Direct metric | M_gal=A_galᵀA_gal | M_cell=BᵀB |
| Inverse metric | M_gal⁻¹ | R_cell=M_cell⁻¹ |
| Normal | derived from A_gal | separately derived from B |

> Evidence scope. G02 pp3–5,17,20 and G01#/comparison_to_authoritative_K_field report shared algebra but distinct metric anisotropy and ICRS orientation. The historical normal-angle comparison is source-reported, not a fresh mature-lock replay. Our two diagonal bases establish the general logical distinction exactly. A common formula is useful explanatory structure; an additional physical correspondence needs its own transformation and prediction.

The symbols G_phase and G_eff from neighboring work have different source-defined roles; neither is silently substituted for M_cell. Similarly Q_gal is a reciprocal basis here, not a distance quadratic form called Q elsewhere, and not the indexed integerization Q_g or Q_nu. Label both symbol and source before combining equations.

## Diagnostics — C29.04-D1

1. Why does s_ab+s_bc=s_ac survive a change of basis?
2. Does equality of sheet counts fix a normal in ICRS?
3. What is the reconstruction rule for a/2 after separating its normal component?
4. What must be supplied before an orientation comparison becomes a physical scale comparison?

Worked answers. 1. The b terms cancel algebraically for all vectors. 2. No: the normal depends on the actual inverse transpose, as the two diagonal examples show. 3. a/2=hN+t_a; store both parts. 4. A calibrated length relationship and explicit mapping, preserving the different origins, orientations and units. An angle alone supplies no physical distance.

Next: [lesson 05](lesson-05.md) calculates how a metric changes address differences into geometric distance.
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Distance metrics and ellipsoids

Essential question: Why can rounding an address miss the closest center?

Goals: Calculate distance using a positive quadratic metric; verify an inverse; compare candidate centers in a skew cell; explain ellipse directions without advanced linear algebra.

Prerequisite bridge. Lesson 03 defined M=AᵀA and lesson 04 showed that bases can share closure while differing in metric. A three-period sequence now teaches the quadratic calculation, skew assignment, and geometric interpretation. All numbers below are synthetic, not galaxy measurements.

## C29.05-E1 — Derive the quadratic rule

An address displacement q=(q₁,q₂) is dimensionless. Its geometric displacement is Aq=q₁a+q₂b. The squared Euclidean length is its dot product with itself. Expanding gives

`distance² = q₁²(a·a) + 2q₁q₂(a·b) + q₂²(b·b) = qᵀ M q`.

The off-diagonal entry appears twice, producing the **cross term**. It records the fact that basis steps need not be perpendicular. The final distance is the nonnegative square root. Keep the displacement vector as well: a length alone cannot reconstruct its direction or signs.

Use `M=[[2,1],[1,2]]L²`. For q=(x,y), distance²=(2x²+2xy+2y²)L². Rewrite it as `((x+y)²+x²+y²)L²`. This is positive for every nonzero (x,y), and zero only at (0,0). Such a symmetric matrix is called positive definite. For a symmetric 2×2 matrix [[a,b],[b,c]], a>0 and determinant ac-b²>0 are an equivalent check: completing the square gives a(x+(b/a)y)²+((ac-b²)/a)y². This explains why the test works rather than simply naming a rule.

## C29.05-W1 — Metric and inverse worked example

The leading diagonal entry is 2 and the determinant is 2·2-1·1=3, both positive. The inverse is `(1/3)[[2,-1],[-1,2]]L⁻²`. Verify by multiplication: the first product row is ((4-1)/3,(-2+2)/3)=(1,0); the second is ((2-2)/3,(-1+4)/3)=(0,1). Units cancel to give I.

For q=(1,-1), Mq=(1,-1)L². Dot with q to get 1+1=2L², so distance=sqrt(2)L. Expansion independently gives 2-2+2=2L². The cross term is negative here, but the whole squared distance remains positive. Changing the sign of one coordinate changes the geometry of the displacement.

## C29.05-P1 — Two guided exercises

First take q=(1,1). Mq=(3,3)L², so qᵀMq=6L² and distance=sqrt(6)L. Direct expansion gives 2+2+2=6L². Keep the original q alongside that distance.

Next use the skew basis a=(1,0)L, b=(0.9,0.1)L, phase phi=0, and continuous address q=(0.49,0.49). Reconstruct x=0.49a+0.49b=(0.931,0.049)L. Independent coordinate rounding assigns integer label (0,0). Distance squared to its center is 0.931²+0.049²=0.866761+0.002401=0.869162L².

The center at b has label (0,1). Its residual is x-b=(0.031,-0.051)L and squared distance is 0.000961+0.002601=0.003562L². This one comparison disproves “rounding always finds the closest center.” It does not prove b is globally closest among all integer labels. In fact that claim is not needed. A global nearest-center certificate would need a bounded search with a proof that omitted candidates cannot improve the distance. G04 p4 specifies a local closest-vector calculation around a rounded estimate; an estimate is not itself the final answer.

## Ellipse bridge

For distance L, the address points satisfy 2x²+2xy+2y²=1. Define coordinates along diagonal directions: u=(x+y)/sqrt(2), v=(x-y)/sqrt(2). This is reversible: x=(u+v)/sqrt(2), y=(u-v)/sqrt(2). Substitution gives `3u²+v²=1`. At v=0, u=±1/sqrt(3); at u=0, v=±1. Thus the unit-distance curve is an ellipse with semiaxes 1/sqrt(3) and 1 in dimensionless address coordinates. In three dimensions the analogous surface is an ellipsoid.

The direction (1,1)/sqrt(2) is multiplied by 3 under the numerical matrix M/L²; (1,-1)/sqrt(2) is multiplied by 1. A direction preserved by a matrix up to multiplication is an eigenvector; the multiplier is its eigenvalue. Here the values 3 and 1 are derived by direct substitution. No general eigenvalue algorithm is required for core work. A “hard” direction can mean the larger quadratic penalty under a specified matrix; always name that matrix, since G02's hard holonomy mode uses a different root tensor.

> Scope. These are intrinsic distances in a declared metric, not a decoder for physical galaxy distances. G02 p4 and G04 p4 supply the metric/address framework. The separately listed hidden-distance and ellipsoid graph documents are extension routes, not premises of the classroom calculation. Source-specific distance claims would need their own retrieved calibration.

## Diagnostics — C29.05-D1

1. Is diag(1,-1)L² a positive distance metric?
2. For q=(2,0), find squared distance and distance under M.
3. Why is 2xy necessary in the quadratic expansion?
4. What does the skew counterexample prove, and what does it leave unresolved?
5. At u=0, which v values are on the unit-distance ellipse?

Worked answers. 1. No: q=(0,1) gives -1L², impossible as a squared real distance. 2. 2·4=8L², distance=sqrt(8)L=2sqrt(2)L. 3. The terms q₁a·q₂b and q₂b·q₁a are equal and both occur. 4. Independent rounding is not always nearest; the globally nearest label remains unproved by this two-center comparison. 5. v²=1, so v=±1. Their signs distinguish two locations.

Next: [lesson 06](lesson-06.md) retains assignments and residual vectors while counting local states.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# Recursive occupancy and retained residuals

Essential question: How can a count summary preserve sparse structure and reconstruction?

Goals: Enumerate the 27 local states and seven sheets; track parent-child counts and identities; compute distinct vector, angular and radial residuals.

Prerequisite bridge. Lessons 03–05 taught addresses, sheets, centers and metric distances. Now counts summarize assignments, while a parallel identity-and-residual ledger keeps the information needed to reconstruct individual observations. Use one period for states and one for multilevel residual accounting.

## C29.06-E1 — Availability is not occupancy

Let each local label i,j,k take -1,0,1. There are three choices independently for each coordinate, so 3·3·3=27 **available** labels. In the half-step window, the position is A(i,j,k)/2, or O_K+B(i,j,k)/2 for Cell3. The sheet label is lambda=i+j+k. Its possible values are -3,-2,-1,0,1,2,3.

**Occupancy** counts how many observed objects are assigned to each state. It needs an assignment rule and actual observations. A geometric count of available states does not determine their observed occupancy. Nor does a list of seven sheet totals uniquely determine the 27 state counts: several states share a sheet. Keep the full state vector or its immutable source reference in addition to the sheet summary.

## C29.06-W1 — Enumerating a complete window

For lambda=-3 there is only (-1,-1,-1). For -2 there are three permutations of (-1,-1,0). For -1 there are three permutations of (-1,0,0) and three of (-1,-1,1), giving six. For 0 there are (0,0,0) and six permutations of (-1,0,1), giving seven. Changing all signs supplies the positive sheets. The complete table is:

| Sheet | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|
| Available states | 1 | 3 | 6 | 7 | 6 | 3 | 1 |

The sum is 27. By a different classification there is one body center, six face centers, twelve edge centers and eight corners, again totaling 27. Zero nonzero components means body center; one means face center; two means edge center; three means corner. All labels remain available, including unoccupied ones.

For a small synthetic hierarchy, parent P contains objects a,b,c,d. At depth one, P-left has {a}, P-middle has {b,c}, P-right has {d}. Counts (1,2,1) total four. At depth two, divide P-middle into M-left={b}, M-right={c}. Save the path P/Middle/Left for b and P/Middle/Right for c. The middle count reconstructs as 1+1=2, and the parent as 1+(1+1)+1=4. A table of totals alone cannot recover object identity; retaining membership makes the view reversible.

This toy mixed three-child/two-child tree demonstrates accounting, not a source recursion. The Cell3 dyadic spatial refinement and ternary address recursion are separately typed (S02#/backbone_sequence M03). A dyadic split halves each of three directions, producing eight spatial children; three choices per address coordinate produce 27 address children. “Depth two” is ambiguous unless the recursion is named. Do not equate those systems with our toy tree or with detector parity.

## C29.06-P1 — Guided practice and answer

An independent toy parent has objects e,f,g,h and child memberships {},{e,f,g},{h}, giving (0,3,1). It too totals four. Subtract discovery (1,2,1) componentwise to get (-1,1,0). The zero first occupancy and the zero third difference carry different information; both remain in the ledger.

Now let a synthetic observed unit direction be x=(1,0,0) and candidate center c=(4/5,0,0). The **vector residual** r=x-c=(1/5,0,0). Its Euclidean length is 1/5. The **angular miss** is arccos((x·c)/(||x||||c||))=arccos(1)=0°. The **radial mismatch**, defined here as ||c||-1, is -1/5. These are reconstruction-coordinate quantities. Zero angular miss does not mean zero vector residual: x=c+r still needs r. A radial mismatch from the unit shell is not the galaxy's physical radial distance.

At c=0 the vector residual x still exists and radial mismatch is -1, but angular miss is undefined because a zero vector has no direction. Store null with a `zero_center_direction` flag. Do not delete the observation or substitute a zero angle.

> Source scope. G01#/galaxy_cell_geometry gives the same combinatorial sheet populations; /observed_27_node_occupancy reports observational summaries separately. G04 p4 retains vector, Euclidean, angular and radial residual channels. The small memberships above are synthetic, not copied catalog rows. Source rows and unexported state arrays stay in place and are referenced by provenance.

## Diagnostics — C29.06-D1

1. How many labels lie on lambda=0, and why?
2. Does a zero observed count remove a possible state?
3. Which fields reconstruct x from a center assignment?
4. For x=e_x and c=0, list the available residuals and the undefined one.

Worked answers. 1. Seven: the origin plus the six orders of (-1,0,1). 2. No: retain its label and zero count. 3. Keep c or its address+basis+phase, and the full signed r; then x=c+r. Membership and source identity must also survive. 4. r=e_x, length 1, radial mismatch -1; angular miss is null with the zero-center flag.

Next: [lesson 07](lesson-07.md) freezes assignments before comparing independent populations.
<!-- END: lesson-06 -->

<!-- BEGIN: lesson-07 -->
# Discovery and held-out comparisons

Essential question: What makes a held-out comparison a test of an already chosen geometry?

Goals: State what must be frozen; retain all signed occupancy differences and phase shifts; distinguish source control families from changes fitted after inspection.

Prerequisite bridge. Lesson 06 retained full memberships and residual channels. We now compare two populations under one preselected assignment rule. The two periods cover the discovery contract and the complete discrepancy ledger.

## C29.07-E1 — Separate choosing from checking

Discovery data may choose candidate plane normals, spacings, phases and the three-plane system. Once chosen, save them with basis order, units, source hashes, assignment algorithm and boundary convention. **Freeze** means do not alter these choices while evaluating the holdout. A holdout is a population not used to choose that fitted configuration. Reusing its answers to choose a better phase makes a new exploratory branch, which can be valuable but needs a later independent check.

G04 p3 reports 57,076 discovery positions and 57,305 holdout positions. Their sum is 114,381. It says discovery selected candidate directions, spacings, phases and triad; final assignments used actual directed vectors. G02 p8 reports three controls: full orientation rotations (600 runs), common phase translations (600), and RA/Dec coordinate permutations (300). Each changes a different part of the arrangement. An orientation rotation preserves internal angles of the cell while changing its relation to the sky; a phase translation shifts plane offsets; coordinate permutation tests the joint angular coordinate structure. Those controls are not interchangeable, and their source statistics remain attached to their original families.

A count divided by population size is a fraction. Comparing fractions is useful when populations differ in size, but retain original counts, totals and identities at their source. A signed difference is always declared in order: here **holdout minus discovery**. Correlation compresses the relation between two vectors to one number; it cannot replace the componentwise differences or explain them away.

## C29.07-W1 — Complete seven-sheet reading

G01#/observed_27_node_occupancy contains seven-element discovery, holdout and rotation-mean fraction arrays. [Source comparison ledger](source-comparison.md) displays all their entries and every holdout-minus-discovery difference. For example on sheet -3, the stored values give

`0.012634150597679085 - 0.012264349288667742 ≈ +0.000369801309011343`.

On sheet 0 the corresponding difference is approximately -0.00246333476723913. Report both directions of difference, not only enhanced sheets. The verification script computes all seven from the hashed original record, retaining decimal subtraction results without interpreting them as exact rational population ratios. Summing each source fraction vector gives approximately one; the tiny stored-precision remainder is also retained.

The source's discovery/holdout correlation is 0.9995135003207234. This is a source-reported descriptive statistic, not an independently recomputed 27-state statistic here: G01 does not contain the full 27-state vectors needed for that replay. The seven-sheet subtraction is a fresh, narrower computation. Do not label the two checks as equivalent.

## C29.07-P1 — Frozen versus refitted practice

Toy discovery occupancies (1,2,1) and holdout occupancies (0,3,1) produce (-1,1,0). Both totals are four. Retain all three bins and the memberships established in lesson 06.

Freeze synthetic A=I₂ L and phi=(1/4,1/2). For a holdout point x=(3/10,1/2)L, the old k=0 center is (1/4,1/2)L and residual is (1/20,0)L. After looking at x, someone proposes phi'=(1/3,1/2). The phase shift is phi'-phi=(1/12,0). The new k=0 center is (1/3,1/2)L and residual (-1/30,0)L. Reconstruct x from either pair: 1/4+1/20=3/10 and 1/3-1/30=3/10. The integer label happens not to change; the center and signed residual do. Keep both assignments and the branch history. An improved distance after refitting does not turn the exploratory branch into a frozen test.

> Source interpretation boundary. G01#/pure_holonomy_coordinate_tests attributes the detected structure to mixed branch-lift coordinates rather than an isolated pure sheet/A2 harmonic under its tested family. Its family statistic and interpretation remain source-reported. We retain weak pure-coordinate channels alongside mixed-coordinate results. G02 pp17–20 distinguishes these constructions; a pure-coordinate test is not a substitute for the full-state comparison.

## Diagnostics — C29.07-D1

1. Name four geometric choices to freeze before evaluating holdout.
2. A phase is changed after examining holdout. What must happen to the old result?
3. Does a high correlation justify omitting a negative sheet difference?
4. What has this course freshly verified about G01 occupancy, and what has it not replayed?

Worked answers. 1. Normals, spacings, common phase and selected triad, with assignment and conventions also saved. 2. Preserve the frozen result and add a named exploratory branch, including phase difference and both residuals. 3. No: the signed component is retained information and may locate an unresolved mechanism. 4. It checks the seven-sheet stored fractions and their differences; it does not reconstruct 27-state occupancy or independently reproduce the source correlation from catalog rows.

Next: [lesson 08](lesson-08.md) turns a cross-domain similarity into an explicit transformation and prospective prediction.
<!-- END: lesson-07 -->

<!-- BEGIN: lesson-08 -->
# A cross-domain explanatory map

Essential question: What extra structure makes a recurring pattern a testable cross-domain explanation?

Goals: Derive scale-normalized metric invariance; distinguish shape from orientation; specify a frozen independent prediction with retained mismatch channels.

Prerequisite bridge. Lessons 04–05 taught roots, metrics and eigen-directions; lesson 07 taught frozen comparisons. We combine those capabilities over two periods. Eigenframe here means the ordered set of perpendicular eigen-directions of a specified symmetric matrix, with signs or projective conventions declared. We do not ask students to diagonalize a source matrix numerically.

## C29.08-E1 — Write the transformation, then identify what survives

A candidate explanation should say which objects correspond, how to transform them, what is invariant, and what new observation would distinguish it from alternatives. Shared algebra is one layer. The metric, orientation, occupancy and calibrated physical role are additional layers. A mechanism sufficient to explain recurrence across domains must account for the measured differences too.

Suppose every edge of a three-dimensional basis is multiplied by a positive scalar s. Each dot product gains s², so M becomes s²M. Volume V=|det A| gains s³ because three independent directions are scaled. Define the volume-normalized metric `M_bar=M/V^(2/3)`. The exponent 2/3 means “take a cube root, then square.” V has units L³, so V^(2/3) has units L²; M_bar is dimensionless. For positive s, `(s³V)^(2/3)=s²V^(2/3)`, so M_bar is unchanged. Store V as well as M_bar to recover M: M=V^(2/3)M_bar. A normalized view alone intentionally hides overall scale; retaining V makes the representation reversible.

A rotation U preserves dot products: its defining algebraic check is UᵀU=I. For a rotated basis UA, `(UA)ᵀ(UA)=AᵀUᵀUA=AᵀA`. Thus orientation can change while Gram stays fixed. The rotation must still be retained if reconstruction in ICRS matters. A reflection also preserves Gram but changes handedness; only det(U)=+1 is a proper rotation. Equal Gram matrices alone cannot distinguish reflection. Changes of shape generally alter the normalized metric.

## C29.08-W1 — Worked scaling and shape comparison

Synthetic A=diag(1,2,3)L has V=6L³ and M=diag(1,4,9)L². For 2A, volume is 48L³, metric diag(4,16,36)L² and every root doubles. Since 48^(2/3)=4·6^(2/3), dividing the new metric by the new volume scale yields exactly the old M_bar. This is a mathematical implication of uniform scaling, not evidence that any two physical systems are related by that scaling.

Contrast A'=diag(2,1,4)L from lesson 04. Its volume is 8L³ and metric diag(4,1,16)L². Relative to the same ordered labels, its first-to-second diagonal metric ratio is 4, whereas A's ratio is 1/4. Uniform scaling cannot explain that change. To compare actual cells one must preserve order or explicitly record and justify any permutation. A changed ratio is a retained structural difference.

## C29.08-P1 — From source hypothesis to future test

G02 p19 proposes that hard-mode-aligned states should be preferentially depleted. Its post hoc projection is the source of this hypothesis, not a performed independent test. Here “hard mode” refers to the larger nonzero eigenvalue of the holonomy root tensor K=sum s sᵀ; applying s sᵀ to v means s(s·v). The roots lie in a plane, so its normal has K N=0. The two in-plane directions receive different multipliers. This defines the source terms without conflating K with lesson 05's distance metric.

A valid prospective plan freezes the galaxy basis, phase, root-tensor eigenframe, the state set to be tested, assignment algorithm, inclusion rules and control comparison before opening a new independent catalog. Save survey selection inputs that describe which sky regions or objects could be observed. Missing selection information stays an unresolved field. If testing distance shells, require independent distances and freeze shell boundaries; do not manufacture them from a unit sphere.

For a finite **synthetic planning exercise**, suppose a frozen transformation has already assigned four equally exposed states to hard-aligned labels H1,H2 and comparison labels C1,C2. Define the contrast as mean hard occupancy fraction minus mean comparison fraction. Predict contrast <0 in the independent sample. Toy counts (1,1,3,3) total eight, fractions (1/8,1/8,3/8,3/8), giving contrast 1/8-3/8=-1/4. Counts (3,3,1,1) instead give +1/4, contradicting this directional prediction under the stated equal-exposure contract. Zero would also fail the strict “<0” rule. Neither outcome is erased. The four-state example teaches the operation; actual work retains all 27 states, controls, exposures and residuals, with a justified aligned-state mapping fixed in advance.

> Claim scope. Proposed common transport or scale-coupling mechanisms are hypotheses to compare by explanatory reach and independent predictions. The algebraic invariance above is derived; source occupancy is reported evidence; hard-mode depletion is a proposed test; physical galaxy length calibration and survey selection remain unresolved here. G02 pp19–20 also notes many possible compound ratios. A ratio chosen after seeing all candidates must retain the search family and compete prospectively, not be relabeled as an independent lock.

## Diagnostics — C29.08-D1

1. Under A→3A, how do M, V and roots change?
2. What additional value reconstructs M from M_bar?
3. Why does equal Gram not establish equal ICRS orientation or handedness?
4. For equal-exposure toy counts (2,2,2,2), does the strict depletion prediction pass?
5. What makes a new eigenframe selected after seeing the new catalog exploratory?

Worked answers. 1. M→9M, V→27V, roots→3 roots. 2. V, through M=V^(2/3)M_bar; retain the basis or orientation mapping for full vector reconstruction too. 3. Rotations preserve Gram, and reflections preserve it while reversing orientation. 4. All fractions are 1/4 and contrast is 0, so the strict negative prediction fails; retain every count. 5. The tested geometry has changed using the evaluation data, so the original frozen prediction and the new branch must both remain recorded.

Next: [capstone](capstone.md) assembles a source-traced comparison using these already practiced operations.
<!-- END: lesson-08 -->
