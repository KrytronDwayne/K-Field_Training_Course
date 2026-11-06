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
