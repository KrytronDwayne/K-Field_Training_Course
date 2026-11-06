# Lesson 06 — From a geometric pattern to an action

**Essential question:** What additional evidence turns a matching pattern into a specified action?

**Goals:** Verify the cyclic action on H and its roots; read its permutation matrix; test whether a supplied map respects two actions.

**Bridge and pacing:** Lesson 01 taught cycles; Lessons 03–05 supplied the root plane and distinct carriers. We can now say exactly where a symmetry acts. One 55-minute period: retrieval 5, instruction/example 20, practice 15, diagnostic repair 15 minutes.

## C13.06-E1 — Specify the carrier, operation, and map

Use H={(x,y,z):x+y+z=0} as the carrier and T(x,y,z)=(z,x,y) as the operation. An action assigns each operation a transformation of the carrier, consistently with composition and identity. The three-operation table of Lesson 01 supplies this consistency: I acts as identity and three applications of T return every input.

A matrix is a rectangular table of numbers encoding a linear rule. For column triples the matrix of T has rows (0,0,1),(1,0,0),(0,1,0). To apply a matrix, take the dot product of each row with the input column. The first output is 0x+0y+1z=z, the second x, the third y. The identity matrix has rows (1,0,0),(0,1,0),(0,0,1). Matrix composition means performing the corresponding rules in succession. A transpose swaps rows and columns; here Tᵀ sends (x,y,z) to (y,z,x), so it is T² and TᵀT=I.

For any v=(x,y,z), w=(p,q,r), Tv·Tw=zr+xp+yq=v·w. This proves preservation of all dot products, not only the norm of one example. Also the sum of Tv is z+x+y, so H is preserved. An invariant subset is a set whose members remain inside it under the operation; we will verify the root set has this property.

Suppose a second carrier Y has an operation U. A proposed identification f:H→Y must specify an actual rule, not just claim that both diagrams have six points. The condition f(Tv)=U(f(v)) says that transform-then-map equals map-then-transform. Such a map is called an intertwiner. If claiming a full identification of carriers, also show f is one-to-one and onto, or specify the intended restricted part. “One-to-one” means distinct inputs never share an output; “onto” means every intended target is reached.

For a finite taught example, use Y=H, f(v)=2v and U=T. Then f(Tv)=2Tv=T(2v)=U(f(v)) because T only moves coordinates. The inverse f⁻¹(w)=w/2 proves a full carrier identification on H. However f doubles lengths, so it does not identify the metric without a scale conversion. On Q₂, the same map is not onto Q₂: α₁/2 is not integral. Claims must state which carrier and structure they concern.

## C13.06-W1 — Trace the roots

Tα₁=T(1,-1,0)=(0,1,-1)=α₂. Tα₂=T(0,1,-1)=(-1,0,1)=-(α₁+α₂). Applying T again to that third root gives (1,-1,0)=α₁. The negatives form the other cycle because T(-v)=-T(v). Thus all six roots are permuted. T³=I and TᵀT=I certify the cycle and metric preservation on the stated carrier.

> **Scope:** This finite action is derived and explicitly verified. S02 /backbone_sequence/8 supplies the root datum, not an empirical detector intertwiner. A physical assignment needs its own target carrier, mapping, operations, and invariants. The missing physical identification remains an unresolved question, not a hidden premise.

## C13.06-P1 — A vector orbit and a map test

Apply T three times to q=(2,-3,1). Write the three matrix rows of T and multiply them by the column q. Express the first result using simple roots, check squared norm at each step, and test f(Tq)=T(f(q)) for f(v)=2v. Retain q alongside its weight quotient label.

**Worked practice answer:** q → (1,2,-3) → (-3,1,2) → q. The matrix rows (0,0,1),(1,0,0),(0,1,0) have dot products 1,2,-3 with q, giving the same first output. The first image equals α₁+3α₂=(1,-1,0)+(0,3,-3)=(1,2,-3). All squared norms equal 14 because the squared entries 4,9,1 are rearranged. The left map path gives 2(1,2,-3)=(2,4,-6); the right path gives T(4,-6,2)=(2,4,-6). Every orbit vector is integral and zero-sum, hence class 0 in P₂/Q₂. Store q and the operation exponent: class 0 alone does not reconstruct the orbit point.

## Diagnostic checks

1. **C13.06-D1:** A different device diagram resembles A2. What must be supplied to claim that its operation is the action just studied?
2. **C13.06-D2:** Use the matrix rows to evaluate T(-1,3,-2), then check sum and squared norm.
3. **C13.06-D3:** Let Y=H, U=I, and f(v)=v. Does f intertwine T with U? Test α₁.
4. **C13.06-D4:** Does f(v)=2v identify the six-root set with itself? Explain the difference from identifying H with H.

**Worked answers:** 1. A target carrier, target operation U, explicit map f, and a check f(Tv)=U(f(v)), with any metric conversion and reconstruction rule. Numerical resemblance alone supplies none of these. 2. (-2,-1,3), sum 0, squared norm 4+1+9=14. 3. No: f(Tα₁)=α₂ but U(f(α₁))=α₁. 4. No: 2α₁ is not a root. On real H division by 2 is available, so f is bijective there; the claim changes when the carrier changes.

**Next dependency:** [Capstone](capstone.md) combines the six lessons into a transfer atlas. No additional mathematics is required.
