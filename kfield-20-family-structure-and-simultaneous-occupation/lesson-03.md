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
