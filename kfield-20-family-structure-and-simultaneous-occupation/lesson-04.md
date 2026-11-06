# Lesson 4 — Tensor products and rank multiplication

Essential question: Why can a space have many coordinate slots but a projector have a smaller rank?

Goals: Test column independence by equations; check a projector and retain its complement; count product addresses and an independent image basis.

Prerequisite bridge: Lesson 3 taught matrix multiplication, identity, adjoint and independent coordinates. We now distinguish a rule's possible outputs from all the slots in which those outputs are written. Spend one period on rank and one on product carriers.

## C20.04-E1 — Independence, image and projectors

The image of a linear map is the set of outputs it can produce. Its rank is the dimension of that image: the number of independent output coordinates. To test vectors c₁ and c₂ for independence, solve αc₁+βc₂=0. If the only solution is α=β=0, they are independent. If they coincide, α=1, β=−1 is a nonzero solution, so they are dependent. A matrix's columns generate its image because an input (x₁,x₂,…) produces x₁c₁+x₂c₂+…. Thus rank is the number of independent columns needed to generate all columns, not the number of written columns.

A projector R satisfies R²=R: applying it twice changes nothing after the first application. An orthogonal projector also satisfies R†=R. It splits an input x into Rx and its retained complement (I−R)x. Their sum is x. Idempotence gives R(I−R)x=0. We use R locally to avoid confusing this projector with the shift P of lesson 3; the packet's example named P is exactly this R.

## C20.04-W1 / C20-RANK-EX1 — Worked rank-2 projector

Let

```
R = [1/2 1/2 0]
    [1/2 1/2 0]
    [ 0   0  1].
```

It maps (a,b,c) to ((a+b)/2,(a+b)/2,c). Applying this rule again keeps the equal first two entries and the third entry, proving R²=R for every input. Direct multiplication gives first block entries 1/4+1/4=1/2 and last diagonal entry 1, the same R. Its transpose is R, so it is orthogonal.

The first two columns equal c₁=(1/2,1/2,0); the third is c₃=(0,0,1). Solve αc₁+βc₃=(α/2,α/2,β)=0. It forces α=β=0, so the image has rank 2 in an ambient dimension of 3. The image consists of all (t,t,c), two free choices.

For x=(2,0,3), Rx=(1,1,3) and (I−R)x=(1,−1,0). Adding them restores (2,0,3). Their inner product is 1−1+0=0. The squared-norm check is 13=11+2. The complement contains the first-coordinate difference, which must not be discarded.

## Product carriers: independent labels before rank multiplication

A carrier here is the vector space in which a rule acts. A product carrier A⊗B has one independent address for each pair of basis addresses, written eᵢ⊗fⱼ. For a two-label and a three-label carrier:

| first label | family 0 | family 1 | family 2 |
|---|---|---|---|
| a | (a,0) | (a,1) | (a,2) |
| b | (b,0) | (b,1) | (b,2) |

This table has six distinct addresses. Under the declared product-basis construction, a list on these addresses has dimension 6. A tensor product of maps acts separately: (A⊗B)(u⊗v)=Au⊗Bv and extends by adding such outputs. If the first image has r independent basis vectors and the second s, their rs paired image vectors form a basis: every output expands in them, and reading a coefficient at each independent pair forces a zero combination to have every coefficient zero. This proves rank multiplication for these finite product maps. A label table alone, without a specified map, establishes no projector rank.

## C20.04-P1 / C20-RANK-P1 — Practice and worked answers

Apply R to (4,2,−1), retain the complement, and check reconstruction. Then count the dimension and rank of I₂⊗I₃⊗diag(1,0). The notation diag(1,0) means the 2-by-2 diagonal matrix with those entries.

Answer: R(4,2,−1)=(3,3,−1). Subtraction gives (1,−1,0), and addition restores the input. The tensor carrier has 2×3×2=12 addresses. Only the history address with diagonal entry 1 survives. Six basis vectors (i,r,0), with i=a,b and r=0,1,2, span the image and are independent because each has its own nonzero coordinate. Rank is 2×3×1=6. The six (i,r,1) input coordinates form the retained complement; save them alongside the projected part.

> Claim scope: This finite rank bridge implements EA-20-E07-3. Its matrices are supplied teaching examples. The product rule prepares S02#/backbone_sequence/15/family_projector. The six labels in the table are not six measured objects. Ambient dimension, label count and image rank coincide only under additional specified conditions.

## Diagnostic checks

1. **C20.04-D1 / C20-RANK-D1:** What is the rank of diag(1,0,0)?
2. Why are the equal first two columns of R not independent?
3. What is the rank of I₂⊗I₃⊗I₂?
4. What information does (I−R)x retain?

Worked answers: (1) One: only (1,0,0) is an independent nonzero image direction. Ambient dimension is three. (2) 1c₁−1c₂=0 uses nonzero coefficients. (3) 12, since every product address survives. (4) Half the signed first-entry difference in opposite coordinates: ((a−b)/2,(b−a)/2,0). Together with the image it reconstructs the input exactly.

Next dependency: [Lesson 5](lesson-05.md) applies this reasoning to the source's declared internal, family and history factors.
