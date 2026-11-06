# Lesson 06 — Metric and Hodge factors

Essential question: How do coordinate weights and volume normalization combine without confusing units or source branches?

Goals: compute a weighted squared length; construct the two normalized diagonal Hodge blocks; check determinants, duality and units; distinguish mature and historical exponents.

Prerequisite bridge: the earlier norm added squared components with equal weights. A physical basis may give different lengths to coordinate steps. We begin with two coordinates before the source's three-dimensional structure. Three 55-minute periods: A weighted lengths and determinants; B area coordinates and blocks; C normalization proof, practice and historical comparison. Each period allocates 5 retrieval, 20 teaching, 15 practice, 15 diagnostic/repair minutes.

## C17.06-E1 — Start with a ruler, then area pairs

A metric supplies the rule for squared length in coordinates. For the positive diagonal metric diag(1,4) LU², a dimensionless coordinate vector (u,v) has squared physical length u²+4v² LU². LU is a chosen length unit. Thus (1,1) has squared length 5 LU², not 2 LU². The metric encodes that a unit step in the second coordinate has physical length 2 LU. Retain both the vector and metric: its length alone cannot reconstruct either.

For a real three-column basis B, the Gram metric M_cell=BᵀB lists all pairwise dot products of basis columns. The dot product of real columns is the sum of component products. The superscript T means transpose without complex conjugation, since B is real. R_cell=M_cell⁻¹ is the inverse metric, with reciprocal units. We abbreviate these as M and R only within this lesson. They are not the distinct phase metric G_phase or any effective metric G_eff. The toy diagonal M below is not a replacement for the mature locked Cell3 basis, its ICRS columns, or its intentional negative determinant.

For diagonal M=diag(m₁,m₂,m₃), det(M)=m₁m₂m₃. Denote this positive determinant by δ. If V is the positive cell volume, δ=V²; a volume sign from basis handedness is not recovered from δ. The inverse is R=diag(1/m₁,1/m₂,1/m₃). In three dimensions a uniform scalar factor k multiplying a whole matrix multiplies its determinant by k³: each of three independent coordinate directions contributes one factor.

Area components need two directions. A bivector is an oriented area coordinate; use the explicit order (12,13,23). For a diagonal map R=diag(r₁,r₂,r₃), an area in directions 1 and 2 gains factor r₁r₂, so the induced area map is wedge²R=diag(r₁r₂,r₁r₃,r₂r₃). Read “wedge squared” as the action on coordinate pairs, not entry-by-entry squaring. More generally its entry for row pair (i,j) and column pair (k,l) is the 2 by 2 minor R_ik R_jl−R_il R_jk. A minor is the determinant of the selected two-row/two-column table; this formula defines the needed operation. Only diagonal examples are required here.

The source's Hodge factors weight electric and magnetic two-form components. A two-form assigns an oriented area a number; for this course the blocks are explicit metric-derived matrices, without requiring calculus on forms. The mature formulas are H_E=δ^(1/3)R and H_B=δ^(2/3)wedge²R. A power 1/3 means cube root; a power 2/3 means square that cube root. Since M has LU², δ has LU⁶, R has LU⁻², and wedge²R has LU⁻⁴, both blocks are dimensionless.

Declare the example's pairing matrix J=[[0,0,1],[0,−1,0],[1,0,0]]. It exchanges components 1 and 3 and reverses component 2; Jᵀ=J and J²=I. For a diagonal D=diag(a,b,c), J D Jᵀ=diag(c,b,a), because the middle sign occurs twice. This convention is supplied for our teaching example. We do not silently substitute it for the archival J whose basis convention is a retrieval issue in S03 AUD-009.

## C17.06-W1 — Construct and check both blocks

Take synthetic M=diag(1,4,16) LU². Then δ=1·4·16=64 LU⁶ and V=8 LU³. R=diag(1,1/4,1/16) LU⁻². The three area factors are (1/4,1/16,1/64) LU⁻⁴. The cube root of δ is 4 LU²; δ^(2/3)=16 LU⁴. Hence

    H_E = diag(4,1,1/4)
    H_B = 16 diag(1/4,1/16,1/64) = diag(4,1,1/4).

Their determinants are 4·1·(1/4)=1. Although the blocks happen to match in this example, their coordinate roles differ. The duality check gives J H_B Jᵀ=diag(1/4,1,4)=H_E⁻¹. It involves the declared pairing of vector and area coordinates, not an untyped equality of physical fields.

Why these exponents? The determinant of R is δ⁻¹. The area determinant is (r₁r₂)(r₁r₃)(r₂r₃)=(r₁r₂r₃)²=δ⁻². Thus det(δ^a R)=δ^(3a−1) and det(δ^b wedge²R)=δ^(3b−2). Requiring these to equal 1 for EVERY positive δ forces 3a−1=0 and 3b−2=0, or a=1/3 and b=2/3. Checking δ=1 alone cannot choose exponents. This diagonal derivation explains the normalization; S02's normalization theorem states the corresponding three-dimensional identities more generally.

## C17.06-P1 — Swap the first two weights

Use M=diag(4,1,16) LU². Find R, δ, the area factors, both blocks, their determinants and J H_B Jᵀ. Then scale all entries of M by 4 and check whether the normalized blocks change. As a two-dimensional warm-up, find the squared length of (1,2) in diag(4,1) LU².

Worked answer: the warm-up gives 4·1²+1·2²=8 LU². In three dimensions δ=64 LU⁶ and R=diag(1/4,1,1/16) LU⁻². The area factors are (1/4,1/64,1/16) LU⁻⁴. H_E=diag(1,4,1/4), H_B=diag(4,1/4,1); each determinant is 1. Pairing gives diag(1,1/4,4)=H_E⁻¹. Under M→4M, δ→64δ, R→R/4 and wedge²R→wedge²R/16. The normalization factors gain 4 and 16, respectively, cancelling those changes. Both blocks stay the same. Keep the scale and M as well: normalized blocks alone discard absolute scale.

> Claim scope: Mature formulas: S02 /hodge_normalization_theorem and /backbone_sequence/12; independent archival correction: S04 /hodge_correction_proof. Historical S01 /backbone_sequence/12/definitions instead uses exponents 2/3 and 4/3. Those are not used in the mature branch. Our matrices and J are synthetic and declared, not recovered Cell3 numerical data.

## Diagnostic checks

1. **C17.06-D1:** Determine the units of each mature block and show how the historical exponents fail at numerical δ=64 in fixed LU units.
2. Why does a δ=1 test fail to distinguish the exponent choices?
3. Is wedge²diag(1,1/4,1/16) equal to diag(1,1/16,1/256)?
4. What information must accompany a normalized block to preserve the original scale and state?

Answers: (1) LU²·LU⁻²=1 and LU⁴·LU⁻⁴=1. Historical determinants are δ^(3·2/3−1)=64 and δ^(3·4/3−2)=64²=4096, not 1; their blocks also carry LU² and LU⁴ rather than dimensionless units. (2) Every power of 1 is 1. (3) No; it is diag(1/4,1/16,1/64), using pair products. (4) Retain M or its declared scale with the normalization parameters, the basis convention and the full coordinate state. A scalar length is not a replacement for these.

Next dependency: [lesson 07](lesson-07.md) reads certificate coefficients only within their declared normalization and domain.
