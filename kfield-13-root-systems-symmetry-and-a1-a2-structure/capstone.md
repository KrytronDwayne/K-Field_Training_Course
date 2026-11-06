# Capstone — A labeled A1/A2 transfer atlas

Create six atlas panels. Each panel must name its carrier, operation, invariant, full input/output, and any quotient or removed component. All numbers below are teaching examples. Source-grounded definitions come from S02 M09; none of these panels is an empirical measurement. Use nine core periods followed by two 55-minute capstone periods. In capstone period 1, spend 10 minutes planning, 35 on panels 1–3, and 10 checking. In period 2, spend 35 minutes on panels 4–6, 10 on reconstruction, and 10 on peer explanation and repair.

## Student tasks

1. **C13-CAP-01 — Operations.** On real triples use T(x,y,z)=(z,x,y). Build the composition table for I,T,T², identify identity and inverses, and trace (1,2,3). Verify sum and squared norm.
2. **C13-CAP-02 — Two sides.** For integer carries (-1,3), compute S,A, apply one transfer (+1,-1), and decode both records. Give the parity label plus the even displacement of A before and after. Explain why the parity alone is insufficient.
3. **C13-CAP-03 — Roots.** List all six A2 roots, draw them in either labeled chart taught in Lesson 03, compute the four Cartan entries, and reconstruct (-1,3,-2) in simple roots. Distinguish H, Q₂, and the six-root set.
4. **C13-CAP-04 — Weights.** Compute all three centered channel weights. Compute u₁+u₂ and 2u₁+u₂ with their classes and retained coefficient pairs. Explain why three channel weights do not represent three quotient classes. Give a reconstruction record for the first sum.
5. **C13-CAP-05 — Typed lift record.** For ρ=(1,0,0) and v=(-1,0,1), calculate ℓ=ρ+3v, reduce modulo 3, and recover v. Separately record family F2, ray [1:2:3] with scale 2, and the supplied detector function f(t)=t under t→-t. Explain what can and cannot be inferred across fields, and why there are 27 compatible lifts rather than 27 primitive channel types.
6. **C13-CAP-06 — An action.** Use T on H. Show its action on both simple roots and hence all six roots. Trace q=(2,-3,1), verify squared norm, and state its quotient class while retaining q. Supply the matrix of T. Verify the taught map f(v)=2v between H and H with operation T on both. State what would still be required for a physical identification on a different carrier.

## Full answer key

**Panel 1:** Use row operation after column operation:

| After | I | T | T² |
|---|---|---|---|
| I | I | T | T² |
| T | T | T² | I |
| T² | T² | I | T |

I is identity, I⁻¹=I, T⁻¹=T², (T²)⁻¹=T. All table entries lie in the set, so it is closed. The orbit is (1,2,3),(3,1,2),(2,3,1),(1,2,3); every sum is 6, every squared norm 14. Symbolically T³(x,y,z)=(x,y,z), and permutation preserves the sums of entries and their squares for all triples. Retain the original tuple and transformation exponent to reconstruct any step.

**Panel 2:** Input S=2,A=-4; output (0,2), S'=2,A'=-2. Both are even: A=0+2(-2) and A'=0+2(-1). Input halves are (2-4)/2=-1 and (2+4)/2=3; output halves are (2-2)/2=0 and (2+2)/2=2. Store S, class representative r, and k in A=r+2k. The remainder r=0 alone cannot distinguish -4 from -2. A1 difference carrier P₁=Z; allowed displacements Q₁=2Z. At fixed S=2 only even A yields integer carries. The transfer preserves S, not necessarily squared norm, and has no assigned detector parity.

**Panel 3:** Roots are ±(1,-1,0), ±(0,1,-1), ±(1,0,-1). Coefficient chart points are ±(1,0),±(0,1),±(1,1), with the warning that chart distances are not Euclidean root lengths. A metric-preserving drawing uses α₁=(√2,0), α₂=(-1/√2,√(3/2)), their sum and negatives. Both simple squared norms are 2, cross products -1, so C=[[2,-1],[-1,2]]. The vector is -α₁+2α₂=(-1,1,0)+(0,2,-2)=(-1,3,-2), norm squared 14. H contains all real zero-sum triples; Q₂ contains the integer ones; the root set contains only the six unit transfers.

**Panel 4:** u₁=(2,-1,-1)/3, u₂=(-1,2,-1)/3, u₃=(-1,-1,2)/3. Each is e_i-(1,1,1)/3; retaining the subtracted mean allows recovery. Their sum is zero. u₁+u₂=(1,1,-2)/3 has coefficients (1,1), label 2. 2u₁+u₂=(1,0,-1)=α₁+α₂ has coefficients (2,1), label 0. The channel weights have coefficient sums 1,1,-2, all congruent to 1. Class representatives are 0,u₁,2u₁ instead. For the first sum, retain representative 2u₁ and displacement -α₁. The label alone loses that displacement.

**Panel 5:** ℓ=(-2,0,3), whose residues are (1,0,0); (-2)-1=-3, 0-0=0, and 3-0=3 are divisible by 3. The recovered digit (ℓ-ρ)/3 is (-1,0,1). Retain ρ and v. Three independent digit choices per position give 27 lifts at n=1, distinguished modulo 9; this is a count of addresses, not formal basis channels. Primitive channels are modeled by e₁,e₂,e₃; centered weights by u₁,u₂,u₃. The supplied family tag is F2. The scaled ray is (2,4,6); retain both representative and scale. The supplied detector function is odd, since f(-t)=-f(t), but its values require f and t. The carry quotient and weight quotient determine none of these independently supplied tags or physical roles. General digits can have nonzero sum.

**Panel 6:** Tα₁=α₂; Tα₂=-(α₁+α₂); T[-(α₁+α₂)]=α₁. Negatives form the other three-cycle. T has rows (0,0,1),(1,0,0),(0,1,0). Its transpose is its inverse, so TᵀT=I. More directly, Tv·Tw=v·w by rearranging products, and the zero-sum condition remains true. The orbit is (2,-3,1),(1,2,-3),(-3,1,2),(2,-3,1), with squared norm 14 and label 0 throughout. Keep the full vector and step exponent. For f(v)=2v on H, both composition paths give 2Tv. At q, both give (2,4,-6). The inverse map is division by 2, but lengths scale by 2 and it does not map the six roots onto themselves. A device identification still requires its own carrier Y, operation U, explicit map f, and verification of f(Tv)=U(f(v)), with scope, invariants and reconstruction specified. The finite action alone supplies no physical assignment.

## Rubric — 60 points

| Panel | Calculation and operation | Invariant/scope | Information preservation | Total |
|---|---|---|---|---|
| 1 | Table 3, orbit 2 | Identity/inverses 2, sum/norm 2 | Original and exponent 1 | 10 |
| 2 | S/A and inverse 4 | Transfer and class 3 | S,r,k record and limitation 3 | 10 |
| 3 | Six roots/drawing 3, Cartan 2, reconstruction 2 | Plane/lattice/root distinction 3 | Included in reconstruction | 10 |
| 4 | Weights and sums 4 | Class criterion/channel distinction 3 | Coefficients/displacement/mean 3 | 10 |
| 5 | Lift/reduction/decoding/count 4 | Role separation 3 | Digit, scale, function retained 3 | 10 |
| 6 | Root action/orbit/matrix 4 | Map and invariant checks 4 | Original vector and physical boundary 2 | 10 |

Award partial credit for a correct method with a local arithmetic slip. Require repair of any conflation of carriers, loss of a reconstruction component, or unsupported physical identification before mastery sign-off, regardless of point total. No advanced compiler, Lie-theory proof, or experimental inference is needed.

## Backward teaching map

| Capstone step | Earlier explanation | Worked example | Independently answered practice | Diagnostic |
|---|---|---|---|---|
| C13-CAP-01 | C13.01-E1 | C13.01-W1 | C13.01-P1 | C13.01-D1 |
| C13-CAP-02 | C13.02-E1 | C13.02-W1 | C13.02-P1 | C13.02-D1 |
| C13-CAP-03 | C13.03-E1 | C13.03-W1 | C13.03-P1 | C13.03-D1 |
| C13-CAP-04 | C13.04-E1 | C13.04-W1 | C13.04-P1 | C13.04-D1 |
| C13-CAP-05 | C13.05-E1 | C13.05-W1 | C13.05-P1 | C13.05-D1 |
| C13-CAP-06 | C13.06-E1 | C13.06-W1 | C13.06-P1 | C13.06-D1 |
