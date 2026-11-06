# Lesson 03 — Three channels and the A2 plane

**Essential question:** What shape do unit transfers among three channels generate?

**Goals:** Draw and enumerate the six roots; compute dot products and Cartan entries; reconstruct any integer zero-sum triple using two simple roots.

**Bridge and pacing:** The two-side transfer added one unit and removed one. With three ordered channels, a transfer still has zero total change. Two 55-minute periods with 5 retrieval, 20 instruction/example, 15 practice, and 15 diagnostics each. Period A builds the plane and drawing; period B teaches dot products and reconstruction.

## C13.03-E1 — A plane inside triples

Let e₁=(1,0,0), e₂=(0,1,0), and e₃=(0,0,1). These are basis vectors: each identifies one channel. Add triples component by component and multiply them by numbers component by component. A unit transfer from channel j to channel i is e_i-e_j. It has one +1, one -1, and one zero. The six choices with i≠j form the A2 roots:

| Root | Triple |
|---|---|
| α₁=e₁-e₂ | (1,-1,0) |
| α₂=e₂-e₃ | (0,1,-1) |
| α₁+α₂=e₁-e₃ | (1,0,-1) |
| -α₁ | (-1,1,0) |
| -α₂ | (0,-1,1) |
| -(α₁+α₂) | (-1,0,1) |

Every listed sum is zero. All real triples with x+y+z=0 form a plane H. Two coordinates may be chosen freely, while z=-x-y is forced. All *integer* triples in H form the root lattice Q₂. A lattice consists of integer combinations of its generating vectors. The six roots are the shortest nonzero vectors of this lattice in the dot product below; the lattice also contains longer vectors and zero. “Root” and “root-lattice vector” are different descriptions.

For v=(x,y,z) and w=(p,q,r), define v·w=xp+yq+zr. Multiply matching coordinates, then add. The squared norm is v·v. This is the ordinary Euclidean dot product on an abstract dimensionless channel space, not the Cell3 metric M_cell. A negative dot product is allowed; a squared norm is never negative.

To draw H on paper while preserving this dot product, place α₁ at the arrow (√2,0) and α₂ at (-1/√2,√(3/2)) in ordinary horizontal/vertical drawing coordinates. A square root √a is the nonnegative number whose square is a. These arrows have squared lengths 2 and dot product -1. Plot their sum and the three negatives. The result is a six-vertex hexagon around the origin. Alternatively, plot coefficient pairs (m,n) for mα₁+nα₂ as (1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1); this is a useful coordinate chart but ordinary square-paper distances in that chart are not the root metric. Label which drawing convention you use.

The Cartan matrix is a compact table of normalized dot products. Our convention is C_ij=2(α_i·α_j)/(α_j·α_j). The denominator is the squared norm of the column root. No matrix multiplication is required to fill this table.

## C13.03-W1 — Compute and reconstruct

α₁·α₁=1²+(-1)²+0²=2. Likewise α₂·α₂=2. Their cross dot product is 1×0+(-1)×1+0×(-1)=-1. Therefore C₁₁=2×2/2=2, C₁₂=2×(-1)/2=-1, C₂₁=-1, C₂₂=2. The matrix is [[2,-1],[-1,2]].

For q=(2,-3,1), take 2α₁-α₂=(2,-2,0)+(0,-1,1)=(2,-3,1). In general mα₁+nα₂=(m,-m+n,-n). For a zero-sum q=(x,y,z), choose m=x,n=-z. The middle component becomes -x-z=y, so every integer zero-sum triple is obtained. The coefficients are unique because the first and third components determine them.

> **Source scope:** S02 /backbone_sequence/8 and /proof_nodes/63/formula (KFM-X021). The calculations establish the finite abstract root datum. They neither substitute a physical metric nor identify a detector action.

## C13.03-P1 — Build the atlas entry

Reconstruct (-1,3,-2), calculate the squared norm of α₁+α₂, calculate α₁·(α₁+α₂), and check the sums of the six roots. Fill the Cartan table yourself before looking back at the example. Draw the six roots as arrows in the length-preserving paper coordinates taught above; label each tip with its triple. Check opposite pairs and equal distances from the origin.

**Worked practice answer:** The coefficients are m=-1,n=2. Thus -α₁+2α₂=(-1,1,0)+(0,2,-2)=(-1,3,-2). Its squared norm is 1+9+4=14. The summed root is (1,0,-1), squared norm 2. Its dot product with α₁ is 1+0+0=1. Each root has one +1 and one -1, hence sum zero. The Cartan entries are 2,-1,-1,2 by the four products above. The drawing tips for α₁,α₂,α₁+α₂ are (√2,0),(-1/√2,√(3/2)),(1/√2,√(3/2)); their negatives supply the other three tips. Label these respectively (1,-1,0),(0,1,-1),(1,0,-1) and their negatives. Each tip has squared distance 2 from the origin. This is a regular hexagon. In the coefficient chart the six listed points also come in opposite pairs, but square-paper distances there are not the root metric.

## Diagnostic checks

1. **C13.03-D1:** Is (1/2,-1/2,0) in H? In Q₂? Explain.
2. **C13.03-D2:** Express (3,-1,-2) in simple roots and check every coordinate.
3. **C13.03-D3:** Is (2,-2,0) a root, a root-lattice vector, or neither? Compute its squared norm.
4. **C13.03-D4:** Calculate α₂·(α₁+α₂). Why must the Cartan diagonal equal 2 here?

**Worked answers:** 1. It sums to zero, so is in H, but has noninteger entries, so is not in Q₂. 2. 3α₁+2α₂=(3,-3,0)+(0,2,-2)=(3,-1,-2). 3. It is 2α₁ in Q₂, with squared norm 8; it is not one of the six roots. 4. 0×1+1×0+(-1)×(-1)=1. Each diagonal is twice a nonzero squared norm divided by itself.

**Next dependency:** [Lesson 04](lesson-04.md) adds fractional weights to the same plane without confusing them with roots.
