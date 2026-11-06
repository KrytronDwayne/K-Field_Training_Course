# Lesson 02 — Shift operators and endpoint defects

**Essential question:** What information does a finite shift lose at its two ends?

**Goals:** Apply prefix/removal maps; multiply a small matrix by a vector; compute root and terminal defects; distinguish finite, rectangular and infinite domains.

**Bridge:** Lesson 01 gave unit vectors and conditional prefix removal. We now use a simpler single chain of three positions, called 0,1,2. This radial *toy* tracks position along a chain, not all branches of the binary tree and not the source radial T_0.

**Pacing:** Two 55-minute periods. Each has retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15 minutes. Period A covers prefixing and matrix action; B covers endpoint defects and domain comparisons.

## C18.02-E1 — Maps, matrices and removal

A linear map acts on each unit vector and then adds the results with the original coefficients. On the full binary tree write L_a e_w=e_aw. Removal L_a† e_aw=e_w and L_a† e_bw=0; at the root L_a† e_Ω=0 because there is no first letter to remove. The dagger denotes the adjoint; for our real coordinate matrices it is the transpose, obtained by exchanging rows and columns. On all finite binary words, L_a†L_a=I: prefix then remove restores the input. I means the identity map, which changes nothing. Distinct prefixes have disjoint output labels, so L_a†L_b=0. Neither prefix reaches the empty word. Their combined ranges cover every nonempty word. These facts explain the analogous source relations without replacing B_8 by two letters.

For the three-state chain define S e_0=e_1, S e_1=e_2, S e_2=0. Terminal output is explicitly discarded by this map. In order (e_0,e_1,e_2),

```text
      [0 0 0]            [0 1 0]
S  =  [1 0 0]     S† =  [0 0 1]
      [0 1 0]            [0 0 0]
```

Column j records the output of input e_j. To multiply a matrix by a vector, multiply each row by the vector's entries and add. Thus S(x,y,z)=(0,x,y), while S†(x,y,z)=(y,z,0). To compose maps, apply the rightmost map first. S†S therefore means shift first, then remove.

## C18.02-W1 — Two different products

Apply S†S to (x,y,z): S gives (0,x,y), then S† gives (x,y,0). Hence S†S=diag(1,1,0). Here diag lists diagonal entries, all other entries being zero. Conversely S† first gives (y,z,0), then S gives (0,y,z), so SS†=diag(0,1,1). These products differ because they test different ends. A matrix product can always be verified on the unit inputs e_0,e_1,e_2; linearity then covers every vector.

## C18.02-P1 — Preserve the removed coefficient

Find Sf and S†Sf for f=(2,3,4). Recover f by adding a retained vector. Then use T(a,b)=(0,a,b) from two-coordinate inputs to three-coordinate outputs on (2,3).

**Worked answer:** Sf=(0,2,3), S†Sf=(2,3,0); store terminal vector (0,0,4), so f=(2,3,0)+(0,0,4). T(2,3)=(0,2,3), and T†(x,y,z)=(y,z). Thus T†T(2,3)=(2,3). The sum of squared input entries is 4+9=13, equal to the output sum 0+4+9. The terminal coordinate is absent from T's input domain; it has not been erased.

## C18.S01-E1 — Defects, ranks and index

The terminal defect is I−S†S. It keeps input information destroyed by S. The root defect is I−SS†. It keeps output information that cannot be reached by S. A map's rank counts independent output directions. Its kernel consists of inputs sent to zero; its kernel dimension counts independent lost input directions. Here the cokernel dimension counts independent missing output directions, equivalently the dimension of ker S†. Define index as dim ker S−dim ker S†. These are counts, with no physical units.

## C18.S01-W1 — Square versus rectangular

Subtracting the preceding diagonals gives I−S†S=diag(0,0,1) and I−SS†=diag(1,0,0). Each rank is 1. The kernel of S is all multiples of e_2; the kernel of S† is all multiples of e_0. The finite square index is 1−1=0.

For T from two to three coordinates, T†T=I_2, where the subscript states the number of slots. TT†=diag(0,1,1). Its input defect is zero, its output defect has rank 1, and its index is 0−1=−1. This rectangular count is consistent with its different domain and codomain dimensions. It is not a square truncation.

## C18.S01-P1 — A second endpoint ledger

Repeat the loss/reconstruction calculation for f=(1,−2,5). Compare T(1,−2).

**Worked answer:** Sf=(0,1,−2); S†Sf=(1,−2,0). Retain (0,0,5) and add it to recover f. T(1,−2)=(0,1,−2) has squared norm 5, as does its input. In contrast f has squared norm 30 and Sf has 5; the retained terminal vector contributes the other 25.

> **Claim scope:** A separate infinite unilateral shift U on l²(N_0) sends (x_0,x_1,…) to (0,x_0,x_1,…). N_0 means 0,1,2,…; square summability makes the norm finite. There is no last slot. U†U=I, ker U has dimension 0, ker U† is the root direction, and index is −1. This explanation concerns this explicitly defined U. M14's radial T_0 is a source-reported operator with a replay-definition gap under AUD-009. Neither our S nor an assertion of equal index supplies that missing definition.

## Diagnostic checks

1. **C18.02-D1:** Why cannot S†S=I and infinite index −1 both be assigned to this square S?
2. **C18.S01-D1:** Count both defect ranks and the index for S. What changes for U?
3. Evaluate L_a†e_ab, L_a†e_ba and L_b†L_a e_b on the full toy word space.
4. Find the missing information after S acts on (0,0,7). Can S† alone recover it?

**Worked answers:** (1) e_2 is killed, so S†S e_2=0 rather than e_2. Its lost and missing directions each number one. (2) Terminal rank 1, root rank 1, index 0; U has terminal defect zero, root rank 1, index −1. For any finite square n-by-n matrix, kernel and cokernel dimensions both equal n−rank. (3) e_b, zero vector, zero vector: the first letter determines removal. (4) The output is zero; store 7e_2. S† applied to zero cannot recover 7.

**Next dependency:** [Lesson 03](lesson-03.md) asks which of these maps preserves length and which can reverse every possible output.
