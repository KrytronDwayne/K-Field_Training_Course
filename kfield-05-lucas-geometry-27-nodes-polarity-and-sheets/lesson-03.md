# Lesson 3 — Lambda sheets and population counts

**Essential question:** Why do 27 nodes occupy seven sheet levels?

**Goals:** Compute an integer sheet label; enumerate and reconcile seven populations; verify the affine sheet identity with its origin subtraction.

**Prerequisite bridge:** Lesson 2 taught p−O and the half-address q. We only need signed addition to label sheets; we introduce a dot product before using it to check a physical plane. Budget: explanation/work 20 minutes, practice 15, checks/feedback 15, transition 5.

## C05.03-E1 — Equal sums define a sheet

Define λ(L)=L₁+L₂+L₃, pronounced lambda. Each entry lies between −1 and 1, so λ is an integer between −3 and 3. A sheet groups all window nodes having the same λ. The full plane containing that group extends beyond the finite nodes; its population here counts only nodes in the window.

To count carefully, list the ways to achieve each sum. A permutation is a rearrangement of entries. Repeated entries give fewer different rearrangements: (1,1,0) has only three, since swapping the two 1s changes nothing. Negation changes every sign. It carries a node with sum λ to a node with sum −λ and has an inverse, namely negation again. Thus opposite sheet populations must match.

## C05.03-W1 — Worked seven-sheet count

|λ|How the rows are obtained|Population|
|---|---|---|
|−3|(−1,−1,−1)|1|
|−2|three rearrangements of (−1,−1,0)|3|
|−1|three of (−1,0,0), three of (−1,−1,1)|6|
|0|center and six rearrangements of (1,0,−1)|7|
|1|three of (1,0,0), three of (1,1,−1)|6|
|2|three rearrangements of (1,1,0)|3|
|3|(1,1,1)|1|

For λ=0 the complete list is (0,0,0),(1,0,−1),(1,−1,0),(0,1,−1),(0,−1,1),(−1,1,0),(−1,0,1). The six noncentral rows have three distinct entries, so choose the 1's position in 3 ways and the −1's position in 2 remaining ways: 3×2=6. The sum 1+3+6+7+6+3+1=27 accounts for every row.

## C05.03-E2 — Checking the physical sheet

The dot product g·d multiplies corresponding components and adds: gₓdₓ+gᵧdᵧ+g_zd_z. If g has unit 1/U and d has unit U, the result is dimensionless. For the classroom basis choose g_λ=(1,0,−1/3)/U. Its dot product with each basis column is 1: with a it is 1; with b it is 1+0=1; with c it is (−1/3)(−3)=1. Consequently, for d=q₁a+q₂b+q₃c,

g_λ·(p−O)=q₁+q₂+q₃=λ/2.

The same linear expression having a fixed value describes a plane: changing a point while keeping that expression fixed keeps it in the same plane. In source notation g_λ=B⁻ᵀ(1,1,1)ᵀ is the vector whose dot product with each basis column is 1. The superscript is recognition-only here; students can verify the three dot products without calculating an inverse transpose.

For W1's physical check use L=(1,−1,1), p−O=(0,−1,−3/2) U. Then g_λ·(p−O)=0+0+(−1/3)(−3/2)=1/2=λ/2. Using p itself would give 2−(5/2)/3=7/6, which is not 1/2. The omitted origin term is g_λ·O=2−4/3=2/3; indeed 7/6−2/3=1/2.

## C05.03-P1 — Guided practice, with answer

List λ=2 and λ=1, then verify the physical identity for (0,1,−1). Answer: λ=2 consists of (1,1,0),(1,0,1),(0,1,1). λ=1 consists of (1,0,0),(0,1,0),(0,0,1),(1,1,−1),(1,−1,1),(−1,1,1). For (0,1,−1), p−O=(1/2,1,3/2) U, so g_λ·(p−O)=1/2−1/2=0=λ/2. Two different points can therefore share one sheet label.

> **Claim scope:** S02 /backbone_sequence/2/sheet_populations reports the seven populations; explicit enumeration independently verifies them. Its /proof/0 prints an identity without origin subtraction. Approved amendment SA-05 restores the affine expression g_λ·(p−O_K)=λ/2, consistent with the source node definition. This course uses that correction throughout. No sheet count is being interpreted as an observed particle population or mechanism.

## Diagnostic checks

1. **C05.03-D1:** Verify total 27, explain mirrored populations, and check g_λ·(p−O)=λ/2 for L=(1,−1,1).
2. **C05.03-D3:** Can λ=4 occur? Can two different addresses have λ=0?
3. **C05.03-D4:** A student says λ=0 has six nodes. What was omitted?
4. **C05.03-D5:** Check λ and the physical identity for L=(1,1,0).

**Worked answers:** 1. The table sums to 27; negation is a reversible pairing of opposite sheets; the dot product is 1/2 as worked above. 2. No, three entries at most 1 sum to at most 3. Yes: the center and (1,0,−1) both have sum zero. 3. The center, which adds one to the six rearrangements. 4. λ=2; q=(1/2,1/2,0), p−O=(1,1,0) U, and the dot product is 1=2/2.

**Next dependency:** [Lesson 4](lesson-04.md) derives two different class labels from λ without replacing λ.
