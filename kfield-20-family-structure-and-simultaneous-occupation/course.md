# Family Structure and Simultaneous Occupation

A complete topical course for high-school seniors. Seven lessons over 15 core periods, plus three capstone periods.

[Course map](course-map.md) · [Terminology](terminology.md) · [Capstone and full key](capstone.md) · [Teacher guide](teacher-guide.md) · [Sources](sources.md)

<!-- BEGIN: lesson-01 -->
# Lesson 1 — Residues modulo three

Essential question: How can one rule divide 27 coordinate labels into three equal classes?

Goals: Compute residues, including negative residues; enumerate a class without omissions; distinguish a class count from an occupation claim.

Prerequisite bridge: You already add signed integers and solve an equation such as x+3=5. Here we add one rule: numbers differing by a multiple of three receive the same label. The course follows courses 15 and 18 in the series, but all finite operations needed here are introduced locally.

## C20.01-E1 — A finite coordinate system

The residue of an integer modulo three is the unique member of {0,1,2} left after subtracting a suitable multiple of three. For example, 8=2×3+2 has residue 2. Also −1=(−1)×3+2 has residue 2. The symbol ≡ means “has the same residue as”: −1≡2 modulo 3. Use these representatives even when subtraction gives a negative number.

The source writes F₃ for these three labels with addition and multiplication reduced modulo three. X=F₃³ is the set of ordered triples (x₁,x₂,x₃). The exponent 3 means three coordinate positions here. Each position has three choices, so X contains 3×3×3=27 nodes. A node is a label, not an observed particle or a position in metres.

Define λ(x)=(x₁+x₂+x₃) mod 3. The Greek letter λ is pronounced “lambda.” Define Cᵣ to contain every node whose λ value is r, for r=0,1,2. In source notation Cᵣ=λ⁻¹(r): this means the set of inputs with output r, not division by λ. Each node belongs to exactly one class because each integer sum has exactly one residue.

To build Cᵣ, choose x₁ and x₂ freely, then solve x₃≡r−x₁−x₂. There is exactly one allowed x₃. Thus nine pairs give nine nodes per class. Use the following fixed pair order throughout the course; the table gives x₃, not the full triple.

| (x₁,x₂) | C₀: x₃ | C₁: x₃ | C₂: x₃ |
|---|---:|---:|---:|
| (0,0) | 0 | 1 | 2 |
| (0,1) | 2 | 0 | 1 |
| (0,2) | 1 | 2 | 0 |
| (1,0) | 2 | 0 | 1 |
| (1,1) | 1 | 2 | 0 |
| (1,2) | 0 | 1 | 2 |
| (2,0) | 1 | 2 | 0 |
| (2,1) | 0 | 1 | 2 |
| (2,2) | 2 | 0 | 1 |

## C20.01-W1 — Worked classification

For (2,2,2), the sum is 6=2×3+0, so λ=0. For (0,0,1), λ=1; for (0,0,2), λ=2. To find the C₀ node beginning (1,2), compute x₃≡0−1−2=−3≡0. The node (1,2,0) checks because its sum is 3. The table gives 9+9+9=27 nodes without repetition: different first pairs differ, and different classes have different residues.

## C20.01-P1 — Guided practice, with answers

Find the C₂ node beginning (2,1), then the C₁ node beginning (2,2). Enumerate C₂ using the fixed pair order.

Answers: 2−2−1=−1≡2 gives (2,1,2); 1−2−2=−3≡0 gives (2,2,0). The ordered C₂ list is (0,0,2), (0,1,1), (0,2,0), (1,0,1), (1,1,0), (1,2,2), (2,0,0), (2,1,2), (2,2,1). Its sums are 2,2,2,2,2,5,2,5,5, all residue 2.

> Claim scope: S02#/backbone_sequence/15/definitions supplies X, λ and Cᵣ. Enumeration is freshly checkable finite mathematics. The three classes are the source's family-label construction; counting them alone does not identify which physical carrier is occupied. Family labels are not detector parity, chirality, projective signs, or primitive lifts.

## Diagnostic checks

1. What is −5 modulo 3?
2. Which class contains (2,0,2)?
3. Why are there nine nodes in C₁, rather than three?
4. **C20.01-D1:** Does the existence of three classes itself establish simultaneous physical occupation?

Worked answers: (1) −5=−2×3+1, so 1. (2) The sum is 4, so C₁. (3) There are nine freely chosen first-coordinate pairs and one third coordinate for each. (4) No; the class count specifies the label space. Identifying the occupied carrier needs the source premises examined in lesson 6.

Next dependency: [Lesson 2](lesson-02.md) assigns values to these ordered nodes and retains both averages and detail.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 2 — Uniform and zero-sum sectors

Essential question: How can a class average simplify a list without losing any entry?

Goals: Normalize a class indicator; split a list into mean and detail and reconstruct it; count independent uniform and detail coordinates.

Prerequisite bridge: Lesson 1 supplied nine ordered nodes in each Cᵣ. Now place a number at every node. A vector is this ordered list of numbers. Adding vectors means adding corresponding entries; multiplying by a number scales every entry. These are dimensionless teaching amplitudes, not measured masses or densities. Use two periods: decomposition first, normalization and coordinate counts second.

## C20.02-E1 — Values, length and reversible decomposition

Write δₓ for the list with a 1 at node x and 0 at every other node. It acts like an address marker. Any list f can be written as the sum of its values times their markers. For real lists, the inner product f·g is the sum of entrywise products. The squared norm ||f||² is f·f; the norm is its nonnegative square root. Distinct address markers have inner product 0 and are called orthogonal. Each marker has norm 1.

The class indicator is 1 on its nine nodes and 0 elsewhere. Its squared norm is nine. Multiplying it by 1/3 gives the source's normalized indicator Φᵣ=(1/3)Σₓ∈Cᵣδₓ. Here Σ means “add all the indicated terms.” Its squared norm is 9×(1/3)²=1. Different Φᵣ are orthogonal because their nonzero entries never overlap.

For values f₁,…,f₉ in a class, define the mean m=(f₁+…+f₉)/9. Define details dⱼ=fⱼ−m. Their sum is Σfⱼ−9m=0. The reconstruction rule is fⱼ=m+dⱼ for every j. The mean and the full ordered detail list are both primary coordinates of the representation; keeping only one loses information.

The constant list m on a class equals (3m)Φᵣ, because Φᵣ has entries 1/3. Its coefficient in the normalized basis is therefore 3m, not m. The inner product gives the same result: Φᵣ·f=(Σfⱼ)/3=3m. A zero-sum detail has inner product (Σdⱼ)/3=0 with Φᵣ.

The source calls the class-constant space U_λ: choose three constants, one for each class. It calls the zero-sum space on Cᵣ Wᵣ. A space is a collection of lists closed under adding and scaling. Its dimension counts independent coordinates: choices that can be varied freely. Eight detail entries can be chosen freely; the ninth is forced to be the negative sum of the first eight. Hence dim Wᵣ=8. Across X we have 3+8+8+8=27 independent coordinates. The phrase direct sum means each f has one unique decomposition into these four parts. It does not mean deleting any of them.

## C20.02-W1 — Worked decomposition

Take the synthetic list (1,2,3,4,5,6,7,8,9) on C₀ in lesson 1's order. Its sum is 45, so m=45/9=5. Subtract 5 entry by entry to obtain d=(−4,−3,−2,−1,0,1,2,3,4). Pairing opposite entries verifies Σd=0. The normalized-indicator coefficient is 3×5=15. Thus f=15Φ₀+d on C₀, with zeros outside it.

Reconstruction at the first, middle and last entries gives 5−4=1, 5+0=5 and 5+4=9; the same addition restores all nine. Independently, ||f||²=285; the uniform part contributes 9×25=225, and the detail contributes 16+9+4+1+0+1+4+9+16=60. Because the parts are orthogonal, their squared norms add: 225+60=285.

## C20.02-P1 — Guided practice, with answers

Decompose (9,0,0,0,0,0,0,0,0), retaining order and all entries. Find the coefficient of Φᵣ and reconstruct.

Answer: m=9/9=1; d=(8,−1,−1,−1,−1,−1,−1,−1,−1), whose sum is 8−8=0. The coefficient is 3. At the first node 1+8=9 and at each other node 1−1=0. The norm check is 81=9+72. If a second class is all 2 and a third all −1, their coefficients are 6 and −3, with zero detail in each; keep those zero detail lists too.

> Claim scope: S02#/backbone_sequence/15/definitions supplies Φᵣ, U_λ and Wᵣ. These examples are synthetic finite data. Their residual details are preserved information. No observation is rejected because its deviation from the mean is large. W₀,W₁,W₂ here are class-detail spaces, not the weak gauge carrier W₂ from other courses.

## Diagnostic checks

1. **C20.02-D1:** Is an indicator with amplitude 1/9 normalized?
2. A class mean is −2. What coefficient multiplies Φᵣ?
3. Eight detail entries sum to 7. What is the ninth?
4. If only the details are saved, can you recover the original list uniquely?

Worked answers: (1) No: squared norm 9/81=1/9 and norm 1/3. (2) −6, because −6/3=−2 at each node. (3) −7 to make the sum zero. (4) No: adding any common constant leaves details unchanged. Save the mean or its equivalent coefficient as well.

Next dependency: [Lesson 3](lesson-03.md) uses norms and orthogonal coordinates to check lifted and Fourier representations.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
# Lesson 3 — Lifts and Fourier-style channels

Essential question: When does a change of coordinates preserve all information?

Goals: Check a finite lift's normalization; apply and reverse a three-channel Fourier map; extract all nine Weyl coefficients of a supplied matrix; explain why a representation does not choose its input.

Prerequisite bridge: Lesson 2 introduced vectors, orthogonality and squared norm. We now learn matrix operations and complex numbers before using them. This lesson occupies four 55-minute periods: matrices and lifts; complex coordinates and Fourier maps; shift/phase matrices; trace extraction and repair. Do not compress the four sessions into one.

## C20.03-E1 — Session A: matrices and a fully specified lift

A matrix is a rectangular array defining a linear rule on a column vector. To compute output row j, multiply each entry in row j by the corresponding input entry and add. “Linear” means the rule respects adding inputs and scaling them. Column k is the output when the input is the address vector eₖ with a 1 in position k. The identity I leaves every entry unchanged. For matrices A and B, AB means apply B first, then A; its (j,k) entry is Σₗ AⱼₗBₗₖ. The transpose interchanges rows and columns.

A permutation matrix rearranges entries. It preserves the sum of squared entries, and reversing the permutation restores the input. For real matrices its adjoint, written †, is its transpose; session B extends this to complex entries. For a square reversible norm-preserving matrix U, U†U=UU†=I. Such a matrix is called unitary. A rectangular map V with V†V=I is an isometry: it preserves lengths and is reversible on its image, but its image need not fill the larger output space.

Here is a synthetic model with every object declared. Its source inspiration is S02#/backbone_sequence/15/all_lifts, but it is not a replay of missing source objects. Let L={(a,b,0): a,b∈{0,1,2}}, a set of nine translation labels. Define Pᵥδₓ=δₓ₊ᵥ, reducing all three coordinates modulo 3. Translation is reversible by subtracting v, so Pᵥ†Pᵥ=I₂₇. Use a separate orthogonal address |v⟩ for each translation. The notation g⊗|v⟩ means put the entire list g in the block labelled v and put zeros in other blocks. This introduces a product of address sets, explained more generally in lesson 4.

Define V f=(1/3)Σᵥ∈L Pᵥf⊗|v⟩. Thus V sends 27 input entries into nine labelled blocks of 27 entries. These 243 output slots do not represent 243 independently chosen input coordinates: the blocks are linked by their common input f. To reverse a vector of blocks gᵥ on the image of V, use V†g=(1/3)ΣᵥPᵥ†gᵥ. Substituting gᵥ=Pᵥf/3 gives V†Vf=(1/9)Σᵥf=f. Orthogonal block labels also give ||Vf||²=(1/9)Σᵥ||Pᵥf||²=9||f||²/9=||f||². These are separate reconstruction and norm checks.

### C20.03-W1 — Worked lift

For f=δ_(0,0,0), the output has amplitude 1/3 at the nine addresses ((a,b,0),(a,b,0)), one address in each v-block. Its squared norm is 9×1/9=1. Reversing each translation sends all nine entries back to the origin; the outer factor 1/3 makes their summed amplitude 9×(1/3)×(1/3)=1. The rest are zero.

### C20.03-P1 — Practice and answer

Use f=2δ_(1,0,0). In block v=(a,b,0), locate the nonzero entry, calculate its amplitude and the total squared norm, then reverse it. Answer: the address is (1+a mod 3,b,0), amplitude 2/3. Squared norm is 9×4/9=4, equal to the input norm squared. Inverse translations align all nine entries at (1,0,0), and (1/3)×9×(2/3)=2 reconstructs f.

## Session B: complex coordinates and Fourier channels

The imaginary unit i satisfies i²=−1. A complex number a+bi is a pair of real coordinates; multiply by distributing and replacing i² with −1. Its conjugate is a−bi. Their product is a²+b², the squared absolute value. For complex vectors use ⟨f,g⟩=Σⱼ conjugate(fⱼ)gⱼ and ||f||²=Σⱼ|fⱼ|². An adjoint † now means transpose and conjugate. For example, the adjoint of the column (1,i) is the row (1,−i). The same norm and orthogonality tests still work.

Set ω=(−1+i√3)/2. Squaring gives ω²=(−1−i√3)/2, so conjugate(ω)=ω². Adding gives 1+ω+ω²=0, and multiplying ω by ω² gives 1. Therefore ω³=1 and its powers repeat every three. These identities let us calculate without decimal rounding.

The three-channel Fourier matrix has entries Fⱼₖ=ω^(jk)/√3 for row and column indices j,k=0,1,2:

```
       1 [1  1   1 ]
F = ─────[1  ω   ω²]
      √3 [1  ω²  ω ]
```

Each column has squared norm (1+1+1)/3=1. The inner product of distinct columns is (1+ω+ω²)/3=0. Thus F†F=I₃, so F† reverses F. This is a change of coordinates, retaining all three channels. It does not declare the channels to be physical families.

Continuing **C20.03-W1/P1**: Fe₀=(1,1,1)/√3 and Fe₁=(1,ω,ω²)/√3. For the second output, multiplying by F† gives coordinates (1+ω+ω²)/3=0, (1+ω²ω+ωω²)/3=1, and (1+ωω+ω²ω²)/3=0. Thus it returns e₁. The first output similarly returns e₀. Keep zero channels when reconstructing.

## C20.S01-E1 — Sessions C and D: finite Weyl coordinates

A basis is a set of independent building blocks that can express every object of a given type. Independence means a sum of the blocks can equal zero only when every coefficient in that sum is zero. The image of a map is the set of outputs it can produce; its rank counts the independent coordinates of that image. In lesson 4 we test independence and rank using explicit column equations. Here the objects are 3-by-3 matrices; their nine entries require nine independent complex coordinates.

Define the shift P by Peⱼ=e_(j+1 mod 3) and the phase D by Deⱼ=ωʲeⱼ. Explicitly,

```
P = [0 0 1]     D = [1 0  0 ]
    [1 0 0]         [0 ω  0 ]
    [0 1 0]         [0 0  ω²]
```

D is diagonal: only entries with equal row and column indices can be nonzero. Check order: DPeⱼ=ω^(j+1)e_(j+1), whereas PDeⱼ=ωʲe_(j+1). Thus DP=ωPD. Order matters even though both rules are reversible. Use exactly B_ab=DᵃPᵇ with a,b=0,1,2. This B_ab is a matrix-coordinate basis, not the physical Cell3 basis B.

The trace Tr(A) is the sum of a square matrix's diagonal entries. For matrix coordinates use the inner product Tr(A†C). Computing this trace equals summing conjugate(Aⱼₖ)Cⱼₖ over all nine positions, so it is just the vector inner product applied to a matrix's entries. Here B_ab has entry ω^(aj) at position j=k+b mod 3 and zeros elsewhere. Two different b values occupy disjoint positions, giving inner product zero. For equal b, the inner product of B_ab and B_cb is Σⱼω^((c−a)j): it equals 3 if c=a, otherwise 1+ω+ω²=0. Consequently

Tr(B_ab†B_cd)=3δ_acδ_bd,

where δ_ac is 1 when a=c and 0 otherwise. This delta with two indices is an equality test; δₓ earlier was an address vector. The orthogonality proves independence: taking the inner product with any B_cd extracts three times its coefficient. Nine independent matrices fill the nine-entry space.

For a supplied Y, write Y=Σ_ab y_ab B_ab. Multiplying by B_ab† and taking trace gives y_ab=Tr(B_ab†Y)/3. A convenient entrywise version is

y_ab=(1/3)Σ_(j=0,1,2) ω^(−aj) Y_(j,j−b mod 3).

This formula is a way to express an already supplied matrix. It cannot select the physical numerical coefficients of that matrix.

### C20.S01-W1 — Worked extraction and reconstruction

Take the synthetic Y=I+2P−D²P. Its diagonal entries are all 1. In shift positions (j,k)=(0,2),(1,0),(2,1), its entries are respectively 1, 2−ω², 2−ω. Other entries vanish. For b=0, the trace sum gives y₀₀=3/3=1 and y₁₀=y₂₀=(1+ω+ω²)/3=0. For b=1, the entries are 2−ω^(2j), so

y_a1=[2Σⱼω^(−aj)−Σⱼω^((2−a)j)]/3.

For a=0, the sums are 3 and 0, giving 2. For a=1, both sums vanish, giving 0. For a=2, the sums are 0 and 3, giving −1. For b=2 every accessed entry is zero, so all three coefficients vanish. Retain the complete table (rows a, columns b):

| a\b | 0 | 1 | 2 |
|---|---:|---:|---:|
| 0 | 1 | 2 | 0 |
| 1 | 0 | 0 | 0 |
| 2 | 0 | −1 | 0 |

Reconstruction gives 1I+2P−1D²P, the original Y, including every zero coordinate.

### C20.S01-P1 — Practice and worked answer

Extract all nine coordinates of Y=2I+D−P². First write its entries. Answer: diagonal (3,2+ω,2+ω²); entries −1 at (0,1),(1,2),(2,0); all others zero. For b=0, the sum is [2Σω^(−aj)+Σω^((1−a)j)]/3, yielding (2,1,0) for a=0,1,2. For b=1 it is zero. For b=2 it is −Σω^(−aj)/3, yielding (−1,0,0). The full coefficient table is [[2,0,−1],[1,0,0],[0,0,0]]. Rebuilding 2B₀₀+B₁₀−B₀₂ reproduces all the stated entries. This computation checks each trace coefficient, including the six zeros.

> Claim scope: S02#/backbone_sequence/15 gives the lift and Weyl formulas. S03#/findings/8 (AUD-009) records missing exact lift set L and operators Pᵥ. Our nine-translation model is explicitly synthetic; we have not recovered those source objects. The Fourier and Weyl calculations verify the declared finite conventions, not a physical coefficient-selection mechanism. Norm preservation requires the stated orthogonal labels and reversible translations.

## Diagnostic checks

1. **C20.03-D1:** If there are 27 orthogonal unitary translation blocks and the factor remains 1/3, what is the squared-norm factor?
2. What factor normalizes 27 such blocks?
3. Why does F†Fe₁=e₁ rather than erase a channel?
4. **C20.S01-D1:** Does a Weyl basis select a physical Y, and can DᵃPᵇ be silently replaced by PᵇDᵃ?
5. What is the rank of the lift image, given V†V=I₂₇, and why is it not 243?

Worked answers: (1) 27/9=3, so the same formula is not an isometry. (2) 1/√27 since 27 times its square is 1. (3) The columns are orthonormal and all coordinates are retained; the inverse sums produce (0,1,0). (4) No to both: coefficients are input, and reordering contributes phases because DP=ωPD. (5) 27. If a sum of lifted address vectors were zero, applying V† would give the same sum of input address vectors, forcing all coefficients to zero. Those 27 outputs span the image; the additional slots are not free choices.

Next dependency: [Lesson 4](lesson-04.md) uses explicit equations to distinguish image rank, ambient dimension and product-label count.
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
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
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Lesson 5 — The rank-48 projector

Essential question: What precisely is counted by the source's number 48?

Goals: Derive rank 48 from an independent image basis; describe the equal restriction to each family; test zero and higher-rank history alternatives.

Prerequisite bridge: Lesson 4 distinguished carrier dimension and image rank and proved finite rank multiplication for product maps. We now apply that proof to source-typed factors, not to a numerical coincidence. Use two periods: factor accounting and history alternatives.

## C20.05-E1 — The declared factors

S02#/backbone_sequence/15/family_projector states Qₙ=I₁₆⊗I₃⊗qₙ. Read the factors in order: internal carrier, family-label carrier, history carrier. The identity I₁₆ preserves 16 independent internal coordinates; I₃ preserves all three family coordinates. The history projector qₙ selects one independent history direction. The subscript n labels which history projection is used; it is not a family label.

For the rank calculation assume qₙ is nonzero, self-adjoint (qₙ†=qₙ), idempotent (qₙ²=qₙ), and rank one. Choose a normalized history vector hₙ spanning its image. Then qₙhₙ=hₙ. No total history dimension has been supplied in this calculation. If that dimension is a finite H, the full carrier dimension is 16×3×H; its selected image still has rank 48. If the history space is infinite, the image count below remains finite under the rank-one assumption. No infinite-dimensional calculation is required of students.

| Factor | Type and basis addresses | Ambient dimension | Image rank |
|---|---|---:|---:|
| I₁₆ | internal eᵢ, i=1,…,16 | 16 | 16 |
| I₃ | family fᵣ, r=0,1,2 | 3 | 3 |
| qₙ | history, image spanned by hₙ | H if finite; not fixed here | 1, assumed nonzero |
| Qₙ | ordered product (i,r,history) | 48H if finite | 48 |

These are dimensionless counts, not masses or physical volumes. S02#/proof_nodes/81 names the internal identity I_(Lambda_even). This course takes its declared dimension 16 as a source premise; it does not silently infer that dimension from the 27 lambda nodes. The internal carrier and the lambda function are separately typed objects.

## C20.05-W1 — The image basis and uniform restriction

Every image output is a sum of vectors eᵢ⊗fᵣ⊗hₙ. There are 16×3×1=48. They are independent: projecting onto any internal-family address reads exactly its coefficient of hₙ, so a zero sum forces each coefficient to vanish. This proves rank 48 under the declared assumptions. Qₙ²=I₁₆²⊗I₃²⊗qₙ²=Qₙ and Qₙ†=Qₙ follow factor by factor.

Fix a family r. The restriction still permits 16 internal choices and one history direction. Its rank is 16, while its history occupancy count is one. Across families those history counts form (1,1,1). It would be incorrect to call each entire family restriction rank one, or to call (1,1,1) a measured density. The same history projector acts for every r because the middle factor is I₃.

The source also states QₙQₘ=0 for n≠m and common history transport. Orthogonality between different n additionally requires qₙqₘ=0; rank one alone does not imply it. For example two identical rank-one q factors would have nonzero product. We preserve the source's assertion and its necessary condition without claiming a fresh replay of the transported history construction.

## C20.05-P1 — Practice and worked answers

For an explicitly finite teaching history carrier with addresses h₀,h₁,h₂, set q₀=diag(1,0,0), q₁=diag(0,1,0), q₂=diag(0,0,1). For this teaching example only, set q₃=0: there is no fourth history address. Find the rank of I₂⊗I₃⊗q₁, then I₂⊗I₃⊗q₃. What would a rank-two history projector do in the source-sized product?

Answers: The first has dimension 2×3×3=18 and rank 2×3×1=6. Its image basis is (i,r,h₁), so each family has two internal image states and one history direction. The second is the zero map with rank 0; it does not satisfy the nonzero rank-one premise. A rank-two history factor yields 16×3×2=96, provided the history space has at least two independent directions. These alternatives show why the assumptions are essential. They do not modify the source's qₙ definition.

> Claim scope: The factorization and occupation wording come from S02#/backbone_sequence/15, S02#/proof_nodes/78 (F038), and S02#/proof_nodes/81 (X033). Conditional rank arithmetic is freshly derived here. F038 reports exact simultaneous occupation for a common history projector; its D10 shared guard says “No physical occupation conclusion.” S03#/findings/6 (AUD-007) directs recovery of the selection proof and conditional removal of the obsolete guard. Keep all these records together. The mathematical image construction and its identification as the physical occupied carrier have distinct premises; lesson 6 addresses the latter.

## Diagnostic checks

1. **C20.05-D1:** Which factor gives uniform treatment of the family labels, and what further identification is needed for a physical occupation conclusion?
2. Does “rank one” by itself imply orthogonality of qₙ and qₘ?
3. If H=4, what are the source-sized product's ambient dimension and selected rank?
4. What data must be retained when applying Qₙ to an arbitrary finite input x?

Worked answers: (1) I₃; one must connect the actual physical-state carrier to the declared image with the required selection premises. (2) No: equal rank-one projectors are a counterexample; qₙqₘ=0 must be supplied or proved. (3) Ambient dimension 192; rank 48. (4) Keep Qₙx and (I−Qₙ)x, with their address convention and reconstruction x=Qₙx+(I−Qₙ)x. Uniform rank is not permission to discard the complement.

Next dependency: [Lesson 6](lesson-06.md) traces the source's occupation conclusion and its correction record.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# Lesson 6 — Selection, state, and source status

Essential question: Which premise connects a mathematical projector to an occupied physical carrier?

Goals: Classify source claims and fresh checks; preserve the occupation claim, conflicting guard and correction together; state the unfilled premise without inventing a proof or downgrading a source status.

Prerequisite bridge: Lesson 5 constructed a rank-48 image. You can check its arithmetic from explicit factors. Now we ask a different question: what identifies the physical states with that image? No new matrix calculation is needed; this is careful dependency reading.

## C20.06-E1 — Construction, selection and state

A mathematical carrier is a space in which states can be represented. A state is a particular assignment of coordinates in that space, subject to any declared constraints. A projector determines an image, but the equation x=Qₙx is an additional condition on x. To see the difference, take lesson 4's projector R. It is a valid rank-2 projector on three coordinates. The vector (1,1,0) is in its image; (1,−1,0) is not, since R sends it to zero. The existence of R does not choose which vector is physically present.

For the source construction, a physical-carrier identification would connect the source's definition of physical states to ran(Qₙ), the range or image of Qₙ. The necessary dependency path must actually be supplied. Agreement of dimensions does not construct a map preserving the relevant operations. Such a map, when it exists, is called an intertwiner; this is a recognition-only term here, not an unassigned proof exercise.

We distinguish six kinds of statement. A source fact reports what a document contains. A derived implication follows from explicit premises, such as rank multiplication. An interpretation gives meaning to the derived object. A proposed mechanism explains how states would be selected or evolve. An empirical observation reports an actual measurement. An unresolved question records what the retrieved material does not settle. This course contains finite derived checks and source facts; it supplies no new empirical occupation measurement. Familiar matrix algebra is reference mathematics used to check the finite claims.

## C20.06-W1 — Worked source-reading card

Read these records as a group, retaining their locators. A JSON pointer after # gives the exact path in the source document; array indices begin at zero.

| Record and pointer | What it supplies | How this course uses it |
|---|---|---|
| M16, S02#/backbone_sequence/15 | Qₙ=I₁₆⊗I₃⊗qₙ, rank 48, occupation (1,1,1) | Source construction and stated occupation theorem |
| F038, S02#/proof_nodes/78/formula | Status `exact_simultaneous_family_occupation`; scope common history projector | Preserve the source claim at its stated scope |
| X033, S02#/proof_nodes/81/formula | Status `exact_rank_48_family_projector` | Check conditional finite rank independently |
| D10, S02#/proof_nodes/78/shared_proof_steps/0/guard | “No physical occupation conclusion.” | Preserve the conflicting guard |
| AUD-007, S03#/findings/6 | Recover the selection proof linking the physical carrier to ran(Qₙ); remove obsolete guard if discharged | Retain the correction and its conditional acceptance test |

F038 lists KFM-F033, KFM-F037 and KFM-X032 as dependencies. Its shared D10 step lists KFM-F033, KFM-F037 and KFM-X031 as inputs and F038, X032, X033 as outputs. These are exact source records, not a reconstructed selection proof. We do not silently identify X031 and X032 or fill the missing path with rank arithmetic.

AUD-007 says that when the body cannot be loaded, M16 should retain the source-local disposition `VERIFIED_NOT_LOADED` without automatically downgrading the mature `VERIFIED_FROZEN` gate. Those capitalized words are quoted source-local statuses. They are not new certificates issued by this course. In our retrieval, the connecting physical-carrier selection proof is not loaded. We preserve the source occupation claim and guard conflict and do not decide by arithmetic alone which record is obsolete.

## C20.06-P1 — Practice with worked classification

Classify these four statements: (a) 16×3×1=48; (b) F038 reports occupation (1,1,1); (c) D10 carries its physical-occupation guard; (d) a proof connects the physical-state definition to ran(Qₙ) in this course.

Answer: (a) is a freshly checked conditional mathematical implication, with rank-one and product-carrier premises. (b) is an accurately retained source claim. (c) is a source fact recording the conflicting guard. (d) is not supplied: its body remains a retrieval gap. Replacing (d) with “rank 48” would not answer the carrier-selection question. Conversely the retrieval gap does not erase (b) or license changing the source's mature status.

> Claim scope: This lesson reports an actual documentary conflict and its explicit correction record, not a general objection to novel physical inference. Mathematical checks, reported occupation, source status and proof-body retrieval are distinct. A separate integration report uses compiler-module labels; those labels are not automatically the mathematical-backbone labels M01–M20. Its direct-authority modules M03, M07 and M08 do not turn backbone M16 into a newly checked physical-selection proof. See sources.md for the retrieved integration record and generation.

## Diagnostic checks

1. **C20.06-D1:** Does a source's `VERIFIED_FROZEN` label mean the course has replayed its proof?
2. What would allow the AUD-007 acceptance test to be met?
3. Is the source claim deleted when its selection proof is not loaded?
4. Is equal rank enough to identify two physical representations?

Worked answers: (1) No. A reported status and a fresh replay are different evidence records. (2) An explicit dependency path from the physical-state definition to Qₙ and occupation (1,1,1), with the contradictory guard resolved under that proof. (3) No. Retain claim, guard, correction and retrieval state together, with no automatic downgrade. (4) No. Rank counts dimensions; it does not give an operation-preserving identification or select physical states.

Next dependency: [Lesson 7](lesson-07.md) distinguishes family labels from numerical properties and teaches reversible elimination of coupled coordinates.
<!-- END: lesson-06 -->

<!-- BEGIN: lesson-07 -->
# Lesson 7 — Family labels and numerical properties

Essential question: Which numerical information is still needed after the family carrier is specified?

Goals: Distinguish a family-label construction from supplied numerical coefficients; solve and reconstruct a two-block scalar system; preserve singular branches and all eliminated coordinates.

Prerequisite bridge: Lessons 3–6 taught coordinates, matrix operations, rank and source status. Here we use ordinary substitution to learn the source's Schur interface. Use three periods: numerical-input scope; elimination and reconstruction; singular cases and synthesis.

## C20.07-E1 — Labels are addresses, not numerical properties

The label r=0,1,2 tells us where a family coordinate belongs. It does not give that family's mass, a matrix entry coupling it to another family, or an experimentally determined mixing value. Mixing here means that a chosen coordinate state can have components along more than one family address. A matrix describes such relations once its entries and interpretation are supplied. A Yukawa matrix is a matrix of coupling coefficients used in the reference particle-theory language; no numerical physical Yukawa matrix is derived by our finite basis calculation.

The source's Weyl formula represents a given 3-by-3 Y by nine coefficients. For example both Y=I and Y=2I have the same three row labels and the same Weyl basis, but their y₀₀ values differ. Thus carrier labels and a basis cannot by themselves select numerical coefficients. Physical masses require additional physical relations and inputs beyond merely writing Y. This course assigns no mass unit to its dimensionless synthetic entries.

| Quantity | What is supplied here | What remains outside this check |
|---|---|---|
| Family addresses | Three λ classes, dimension 3 | Physical-carrier selection proof body |
| Projector count | Conditional rank 48 and source occupation record | New measured population or density |
| Weyl coordinates | All nine coefficients for explicitly supplied synthetic Y | Selected physical Y and its numerical coefficients |
| Masses and mixing values | No numerical physical values in the M16 material used here | Numerical physical inputs or derivation tying them to states |
| Block-system solution | Exact values for supplied synthetic K and s | Identification of that K,s as a physical experiment |

This is a scope statement about the retrieved M16 material, not a claim that no other archive document contains numerical properties.

## C20.S02-E1 — Schur elimination from substitution

Write two coupled equations Au+Bw=s_U and Cu+Ew=s_W. In the core examples A,B,C,E are ordinary numbers, u,w are unknown numbers and s_U,s_W are supplied numbers. The matrix K=[[A,B],[C,E]] records the two equations. These block letters are local to this lesson: B is not Cell3's basis or a Weyl B_ab, E is not the class-mean map, and C is not a lambda class. All values in the examples are dimensionless.

If E≠0, solve the second equation for w=(s_W−Cu)/E. Substitute into the first:

Au+B(s_W−Cu)/E=s_U,

so (A−BC/E)u=s_U−Bs_W/E. Name the reduced coefficient S=A−BC/E the Schur complement and the reduced source r=s_U−Bs_W/E. If S≠0 as well, u=r/S, then reconstruct w from the saved formula. Each inverse has its own condition: E≠0 permits elimination; S≠0 permits unique solution of the reduced equation.

For a 2-by-2 matrix, define its determinant det K=AE−BC. It is nonzero exactly when the two equations have a unique solution for every supplied right-hand side. When E≠0, ES=E(A−BC/E)=AE−BC, giving the source identity det K=(det E)(det S) in this scalar example. For larger blocks the inverses are matrix inverses, and factor order must be retained: S=A−BE⁻¹C and r=s_U−BE⁻¹s_W. That larger-block notation is recognition-only; the core tasks need only the substitution just taught.

## C20.07-W1 / C20.S02-W1 — Worked reconstruction

Use K=[[2,1],[1,3]] and s=(5,7). The equations are 2u+w=5 and u+3w=7. E=3 is nonzero, so w=(7−u)/3. Substitution gives 2u+(7−u)/3=5. Multiply by 3: 6u+7−u=15, hence 5u=8 and u=8/5.

In Schur notation S=2−1/3=5/3 and r=5−7/3=8/3. Then r/S=(8/3)/(5/3)=8/5, agreeing with direct substitution. Reconstruct w=(7−8/5)/3=(27/5)/3=9/5. Check BOTH original equations: 16/5+9/5=5 and 8/5+27/5=7. The determinant check is 2×3−1×1=5=3×(5/3). Saving only u would discard w; retain K, s, u and w, and the two residuals Au+Bw−s_U and Cu+Ew−s_W, both zero here.

## C20.07-P1 / C20.S02-P1 — Guided practice and worked answers

Use K=[[3,1],[2,2]], s=(7,8). Then solve the separate E=0 example K=[[1,1],[1,0]], s=(3,1) directly from its original equations.

First answer: E=2; S=3−(1×2)/2=2; r=7−8/2=3. Thus u=3/2 and w=(8−2×3/2)/2=5/2. Original equations give 3×3/2+5/2=14/2=7 and 2×3/2+2×5/2=3+5=8. The determinant is 6−2=4=2×2. Both equation residuals are zero and both unknowns are retained.

Second answer: the equations are u+w=3 and u=1. Thus u=1,w=2. E=0 makes the E-inverse formula unavailable, but det K=−1≠0. Therefore the full system is uniquely solvable. A singular chosen block is not automatically a singular full matrix.

## Keeping every singular branch

If E≠0 but S=0, the reduced equation is 0u=r. If r≠0 it is inconsistent; retain that incompatibility rather than produce a number. If r=0, u remains free, and each allowed u has w=(s_W−Cu)/E. For example K=[[1,1],[1,1]], s=(2,2) gives E=1, S=0, r=0. Every pair (t,2−t) solves both equations. Changing s to (2,3) gives r=−1 and incompatible equations u+w=2 and u+w=3. A zero inverse must never be inserted to “solve” either branch. With E=0, return to the original equations as in the practice example; they may have one solution, many, or none.

> Claim scope: S02#/backbone_sequence/15/schur_interface supplies the block formulas, and /weyl_basis supplies coordinate extraction. Our scalar examples are synthetic and freshly checked. The source occupation claim and AUD-007 conflict remain as in lesson 6. Neither choosing a basis nor eliminating a variable selects physical masses, mixing coordinates or the occupied carrier. Reconstructing w and retaining compatibility conditions preserves information through the calculation.

## Diagnostic checks

1. **C20.07-D1:** Which physical masses or mixing numbers were supplied by the three-label count?
2. **C20.S02-D1:** May you use E⁻¹ when E=0? Does E≠0 guarantee S⁻¹ exists?
3. What is lost if only u is retained after solving the worked example?
4. For K=[[1,1],[1,1]], compare right-hand sides (2,2) and (2,3).

Worked answers: (1) None; three labels and a coordinate basis do not choose numerical physical inputs. (2) No and no. E and S each require their own nonzero test in scalar examples. (3) The second state coordinate w=9/5 and the immediate ability to check the full state; save the reconstruction inputs and w explicitly. (4) The first gives all (t,2−t), with t retained as free information. The second is incompatible because one sum cannot equal both 2 and 3. Keep that incompatible branch as a reported result.

Next dependency: [Capstone](capstone.md) combines class counts, retained detail, finite lifts, trace coordinates, typed projector accounting and source-status tracing.
<!-- END: lesson-07 -->

