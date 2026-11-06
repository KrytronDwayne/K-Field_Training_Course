# Complex Carriers and Gauge Symmetry

Seven student lessons. See teacher-guide.md for pacing, capstone.md for synthesis and worked answers, terminology.md for notation, and sources.md for exact provenance.

<!-- BEGIN: lesson-01 -->
# Lesson 1 — Complex numbers and phase

Essential question: How can a number record both size and a reversible turn?

Goals: Compute a conjugate and magnitude; multiply complex numbers; rotate by a quarter-turn and reverse the operation.

Prerequisite bridge: You can plot a pair of real coordinates and expand brackets. We package a pair (a,b) as a single number a+bi. No prior complex arithmetic from course-13 is needed. Use two periods: arithmetic, then rotations and recovery.

## C14.01-E1 — Two coordinates in one number

Define i by i²=−1. The complex number z=a+bi has real component a and imaginary component b, both real numbers. The imaginary component of 2−i is −1, not −i. Plot z at (a,b). Add corresponding components. Multiply by expanding brackets and replacing i² by −1. For example, (1+i)(2−i)=2−i+2i−i²=3+i.

The conjugate is z̄=a−bi: reflection across the horizontal axis. Multiplication gives z̄z=(a−bi)(a+bi)=a²+b². This is the squared modulus |z|²; |z|=√(a²+b²) is distance from the origin. A square root here is the nonnegative number with the stated square. Keep squared lengths when comparing sizes.

Multiplying by i gives i(a+bi)=−b+ai. The point (a,b) becomes (−b,a), a counterclockwise quarter-turn. Its squared length stays b²+a². Repeated multiplication cycles through 1,i,−1,−i,1. The inverse turn multiplies by −i because (−i)i=1. Size alone does not determine z: 1 and i have the same modulus but different directions. Keep both coordinates and the rotation used.

A phase is a direction on the complex unit circle. A unit phase u has |u|=1 and ūu=1, so ū reverses multiplication by u. In angle notation u=cos θ+i sin θ, also written e^(iθ). Here this is notation for a unit-circle turn, requiring no calculus. A full turn is 2π radians, or 360°. Combining turns adds angles, so phases multiply. Powers repeat a turn; negative powers reverse it. At z=0 no unique direction exists, although every phase still sends 0 to 0.

## C14.01-W1 / C14-CX-EX1 — Worked example

For z=1+i, the conjugate is 1−i and |z|²=1²+1²=2. Rotate: iz=i+i²=−1+i. Its squared modulus is (−1)²+1²=2. Reverse: (−i)(−1+i)=i−i²=1+i. Both coordinates survive. This is synthetic arithmetic, not a measurement.

## C14.01-P1 / C14-CX-P1 — Answered practice

Rotate 2−i by i, find the new conjugate and modulus, then recover the original. Answer: i(2−i)=1+2i; conjugate 1−2i; squared modulus 1+4=5; modulus √5. Reversal gives (−i)(1+2i)=2−i. Also multiply (2+i)(1−i): 2−2i+i−i²=3−i. The rotated squared modulus 5 equals the original 4+1.

> Claim scope: Complex arithmetic and rotations are mathematical operations with dimensionless coordinates here. A physical interpretation of phase needs a separately supplied model; no force or measured field is inferred.

For a later six-fold example define ζ=(1+i√3)/2. Its conjugate is (1−i√3)/2. Check ζ̄ζ=(1−i√3)(1+i√3)/4=(1−i²·3)/4=(1+3)/4=1. Thus ζ is a unit phase, with real component 1/2 and imaginary component √3/2. This exact calculation uses only (√3)²=3, not rounded coordinates.

## Diagnostics — C14.01-D1

1. For −3+2i, give both components, conjugate, and squared modulus.
2. Rotate 1−2i by i and undo it.
3. Give two different numbers with modulus 1. What information is missing from modulus alone?
4. Compute (1+i)². Does squaring preserve its modulus?

Worked answers: (1) Components −3 and 2; conjugate −3−2i; squared modulus 9+4=13. (2) i+2=2+i, then (−i)(2+i)=1−2i. (3) 1 and i; direction is missing. (4) 1+2i+i²=2i, of modulus 2, whereas |1+i|=√2. Multiplication preserves length when its multiplier has modulus 1, not in general.

Next dependency: [Lesson 2](lesson-02.md) combines complex coordinates and tests changes of the whole tuple.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 2 — Inner products and unitary changes

Essential question: How do we verify a reversible transformation that mixes complex coordinates?

Goals: Form a conjugate transpose; multiply a 2×2 matrix by a vector and matrix; test unitarity and recover an input.

Prerequisite bridge: Lesson 1 supplies conjugation and bracket expansion. Stack two numbers into a column v=(v₁,v₂)ᵀ. T means transpose: interchange rows and columns. Use two periods, first for matrix operations and then for mixing.

## C14.02-E1 — Rules for combining coordinates

A matrix is a rectangular array. In A=[[a,b],[c,d]], each row supplies one output coordinate: Av=(av₁+bv₂,cv₁+dv₂)ᵀ. Matrix multiplication AB applies B first, then A. Each entry is a row-column sum; for example (AB)₁₂=aB₁₂+bB₂₂. Thus [[1,2],[0,1]][[1,0],[3,1]]=[[7,2],[3,1]]. Identity I₂=[[1,0],[0,1]] leaves inputs unchanged. In diag(a,d), off-diagonal entries are zero.

The dagger † means conjugate transpose: [[a,b],[c,d]]†=[[ā,c̄],[b̄,d̄]]. The complex inner product is ⟨v,w⟩=v†w=v̄₁w₁+v̄₂w₂. In particular ||v||²=⟨v,v⟩=|v₁|²+|v₂|² is squared norm. It is real and nonnegative, although a general inner product may be complex. We conjugate the first argument.

A square matrix U is unitary when U†U=I. This tests every possible input. Indeed ||Uv||²=(Uv)†Uv=v†U†Uv=v†v. The identity (Uv)†=v†U† follows by conjugating the products and interchanging rows and columns. A unitary square matrix has inverse U†, giving v=U†(Uv). Our examples also multiply in both orders to check the inverse. General matrix multiplication is order-sensitive.

## C14.02-W1 — Worked example

For U=diag(i,−i), U†=diag(−i,i). Hence U†U=diag((−i)i,i(−i))=I₂; UU† is also I₂. On (1+i,2−i), output is (−1+i,−1−2i). Squared norm before and after is 2+5=7. Applying U† gives (−i)(−1+i)=1+i and i(−1−2i)=2−i. All components return.

## C14.02-P1 — Answered practice with mixing

Let V=(1/√2)[[1,i],[i,1]]. The scalar outside multiplies every entry. Its dagger is (1/√2)[[1,−i],[−i,1]]. Multiply, retaining the scalar factor 1/2:

V†V=(1/2)[[1+(−i)i,i−i],[−i+i,(−i)i+1]]=(1/2)[[2,0],[0,2]]=I₂.

The same calculation gives VV†=I₂. On v=(1,i), output is ((1+i²)/√2,(i+i)/√2)=(0,√2 i). Squared norm is 2 before and after. Recovery gives ((−i)(√2 i)/√2,(√2 i)/√2)=(1,i). On (2,0), output is (√2,√2 i), squared norm 2+2=4. Applying V† yields ((√2+(−i)(√2 i))/√2,((−i)√2+√2 i)/√2)=(2,0). Cancellation in an output slot has not destroyed the input information.

> Claim scope: These are synthetic, dimensionless vectors. A single preserved vector length is insufficient to prove unitarity. U†U=I supplies the general check; retain the transformation to reverse it.

## Diagnostics — C14.02-D1

1. Find [[1,i],[2,−i]]†.
2. Compute ⟨(1,i),(i,1)⟩ and ||(1,i)||².
3. Why does VᵀV fail as the unitarity test? Multiply it.
4. Is diag(1,2) unitary? Give matrix and vector checks.

Worked answers: (1) [[1,2],[−i,i]]. (2) i+(−i)·1=0; the squared norm is 1+(−i)i=2. (3) Vᵀ=V, so VᵀV=(1/2)[[0,2i],[2i,0]]=[[0,i],[i,0]], not I₂. Conjugation matters. (4) Its dagger-product is diag(1,4); it changes (0,1) to (0,2), changing squared norm from 1 to 4. Invertibility alone is insufficient.

Next dependency: [Lesson 3](lesson-03.md) uses an explicitly ordered five-coordinate carrier.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
# Lesson 3 — The ordered three-plus-two carrier

Essential question: What must accompany a tuple so its meaning survives a change of order?

Goals: Write the color-first carrier; split and reconstruct it with projectors; permute coordinates and operators consistently.

Prerequisite bridge: Lesson 2 taught columns, matrices, and inverse changes. Five slots use the same multiplication rule. This lesson takes one period.

## C14.03-E1 — Slots have types

A carrier is a space on which transformations act. Here H=C₃⊕W₂: C₃ is a three-dimensional complex color block and W₂ a two-dimensional complex weak block. Names identify source roles, not visible paint colors or measurements. The direct sum ⊕ keeps both blocks separately identifiable. Store h=(c₁,c₂,c₃,w₁,w₂)ᵀ. Example entries are dimensionless.

P_c=diag(1,1,1,0,0) projects onto the color block in its original slots. P_w=I₅−P_c=diag(0,0,0,1,1) selects the weak block. Diagonal multiplication gives P_cP_w=0, P_c²=P_c and P_w²=P_w. Each projection loses the other block; together they reconstruct h=P_ch+P_wh. The 0 in the matrix equation means the zero matrix.

M10 displays a weak-first tuple although the governing convention and correction require color-first. Reconcile it with the actual permutation P below, whose rows select old coordinates:

```text
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
1 0 0 0 0
0 1 0 0 0
```

P(w₁,w₂,c₁,c₂,c₃)ᵀ=(c₁,c₂,c₃,w₁,w₂)ᵀ. Its inverse is Pᵀ: each slot returns, so PᵀP=PPᵀ=I₅. The zero-based output indices are [2,3,4,0,1]; counting slots from one gives [3,4,5,1,2].

Operators must move too. If old output is A_old h_old, new output is P A_old Pᵀ h_new. The rightmost factor first restores the old input order. Thus A_new=P A_old Pᵀ. The integer phase weights diag(3,3,−2,−2,−2) become Q_charge=diag(−2,−2,−2,3,3). This local symbol denotes a charge operator, not a distance metric Q. A phase z acts as diag(z⁻²,z⁻²,z⁻²,z³,z³); Lesson 4 explains the weights.

## C14.03-W1 — Worked example

The weak-first tuple (1,2,3,4,5) becomes h=(3,4,5,1,2). Its projections are (3,4,5,0,0) and (0,0,0,1,2), whose sum is h. Pᵀ restores (1,2,3,4,5). Nothing changed except each entry's slot. The charge list becomes (−2,−2,−2,3,3).

## C14.03-P1 — Answered practice

Convert (i,−1,2,0,1+i) from weak-first to color-first and retain both projections. Answer: h=(2,0,1+i,i,−1); P_ch=(2,0,1+i,0,0); P_wh=(0,0,0,i,−1). Their sum reconstructs h. Verify the charge change by applying Pᵀ to an arbitrary h, multiplying old first-two slots by 3 and old last-three by −2, then applying P. Output is (−2c₁,−2c₂,−2c₃,3w₁,3w₂), proving P A_old Pᵀ=Q_charge on every input.

> Claim scope: S02 /typed_conventions/carrier_order and /backbone_sequence/9 give the source convention and displayed M10; S03 /findings/3 (AUD-004) gives the correction. Tuple calculations are fresh finite verification. Role labels alone supply no physical interaction law.

## Diagnostics — C14.03-D1

1. Why is merely relabeling (w₁,w₂,c₁,c₂,c₃) as color-first wrong?
2. Find both projections of (1,i,−1,2,0) and reconstruct it.
3. Can P_ch alone reconstruct arbitrary h? Identify what is missing.
4. Give the formula for changing A_old to the new order. Explain the rightmost factor.

Worked answers: (1) The first two values still belong to W₂; the action and labels would disagree. (2) (1,i,−1,0,0)+(0,0,0,2,0)=h. (3) No; w₁,w₂ remain unresolved unless retained. (4) P A_old Pᵀ, where Pᵀ restores the order expected by A_old.

Next dependency: [Lesson 4](lesson-04.md) uses the block sizes three and two to calculate a determinant constraint.
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
# Lesson 4 — Determinants and the top-form lock

Essential question: What extra constraint preserves an ordered volume coefficient as well as lengths?

Goals: Compute small determinants; calculate the three-plus-two phase constraint; distinguish norm preservation from determinant preservation.

Prerequisite bridge: Lessons 2–3 taught unitary matrices and the ordered blocks C₃,W₂. Now attach one scalar to a square matrix. Use two periods: determinant intuition and calculation, then the phase constraint.

## C14.04-E1 — A scalar that records oriented scaling

For a real 2×2 matrix [[a,b],[c,d]], its columns are the transformed unit directions. Their signed parallelogram area is ad−bc, the determinant det A. Swapping columns reverses the sign; equal columns make area zero. For complex entries use the same algebraic formula, although the result is a complex coefficient rather than ordinary real area. For example det [[1,i],[i,1]]=1−i²=2. Multiplying every entry of a 2×2 matrix by s multiplies its determinant by s², since each term has two factors. Therefore Lesson 2's V has determinant (1/√2)²·2=1.

A diagonal matrix has determinant equal to the product of its diagonal entries. For a block diagonal matrix diag(A_c,A_w), determinant equals det A_c times det A_w. These rules suffice for every required calculation. Recognition-only general rule: det(AB)=det A det B.

A top form here is an ordered alternating volume coefficient Ω. “Alternating” means exchanging two input directions reverses its sign and repeating a direction gives zero. Under a transformation A the coefficient scales by det A. We use this transformation rule as the contract; a full construction with exterior algebra belongs to the next course. Preserving Ω means keeping the coefficient itself unchanged, so det A=1, not merely |det A|=1. A phase factor can have modulus one without equaling one.

The source contract preserves the Hermitian structure of each block (the inner products from Lesson 2), the block decomposition, and the top form. Thus A_c and A_w are unitary and det A_c det A_w=1. U(n) names the group of n×n unitary matrices, while SU(n) adds determinant one. The notation S(U(3)×U(2)) means pairs of unitary blocks whose determinant product is one; it does not require each block determinant to equal one separately. The multiplication of pairs is component by component. Lesson 5 teaches the group terminology.

Suppose a unit phase z acts with integer weight a on each color slot and weight b on each weak slot. The matrix is diag(z^a I₃,z^b I₂). Its determinant is z^(3a+2b). To preserve the top form for every phase, require 3a+2b=0. If the integer exponent n were nonzero, taking an angle π/n would yield z^n=−1, so it could not equal one for every phase. Integer solutions are a=−2m,b=3m: 3a=−2b requires a even, then substituting a=−2m gives b=3m. The primitive source choice uses m=1, giving weights (−2,−2,−2,3,3); “primitive” means no common integer factor greater than one in their magnitudes. The opposite choice m=−1 reverses the phase parameter. No physical charge unit is inferred from these integers.

## C14.04-W1 — Worked example

det diag(i,−i)=i(−i)=1. Color block diag(i,−i,1) therefore has determinant 1; weak block I₂ has determinant 1, so their product is 1. Every entry has modulus one, giving unitarity too. For central weights a=−2,b=3, the determinant exponent is 3(−2)+2(3)=0, and z⁰=1 for every unit phase.

## C14.04-P1 — Answered practice

Color diag(−1,−1,1) and weak diag(i,−i) have determinants 1 and 1; they preserve both block norms and Ω. Weights a=2,b=−3 also give 6−6=0. In contrast, a=1,b=0 at z=i gives determinant i³=−i and fails the top-form condition while preserving norms. Finally diag(2,1/2) has determinant 1 but sends (1,0) to (2,0): squared norm changes from 1 to 4. Both conditions must be checked.

> Claim scope: The preserved-block/top-form contract is source-local to S02 M10, with the order correction from S03. The diagonal and integer computations are verified here. Classification of the entire connected group is source-read recognition, not an untaught proof requirement.

## Diagnostics — C14.04-D1

1. Compute det [[2,1],[3,2]].
2. Test weights a=4,b=−6 for all phases. Are they primitive?
3. Why does testing z=1 alone never establish the all-phase lock?
4. Does diag(2,1/2) satisfy both conditions? Does diag(i,1)?

Worked answers: (1) 4−3=1. (2) 12−12=0, so the lock holds; common factor 2 makes them nonprimitive. (3) 1^n=1 for any integer n, including failing weights. (4) The first has determinant 1 but fails norm preservation; the second preserves norm but has determinant i, so fails to preserve Ω.

Next dependency: [Lesson 5](lesson-05.md) expresses these block transformations through a map and calculates precisely which inputs become invisible in its output.
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Lesson 5 — Cover maps and quotient kernels

Essential question: How can different transformation labels produce exactly the same action?

Goals: Enumerate a finite map kernel; verify six source-kernel elements and exhaustiveness; retain enough labels to recover a preimage.

Prerequisite bridge: We know multiplication, inverses, unit phases, determinant products, and the color-first order. Three periods cover a finite additive map, the source cover, then its full kernel and information accounting.

## C14.05-E1 — Composition, identity, and a map

A group is a set with a composition rule that stays in the set, is associative, has an identity, and gives each element an inverse. Associative means brackets may change without changing the result, as (ab)c=a(bc). It does not mean ab=ba. Reversible transformations form examples under composition. U(1) is the unit phases under multiplication; identity is 1 and inverse is conjugation. SU(3) and SU(2) have the definitions from Lesson 4 and use matrix multiplication.

First use a small additive group. In addition modulo 6, keep the remainder after division by 6: 4+5 becomes 3. Representatives are 0,1,2,3,4,5. Identity is 0; for example 2's inverse is 4. A map f(k)=k mod 3 sends these inputs to 0,1,2,0,1,2. It preserves composition: removing any multiple of 6 also removes a multiple of 3, so f(a+b mod 6)=f(a)+f(b) mod 3. For instance 4+5 mod 6=3 maps to 0, while f(4)+f(5)=1+2 mod 3=0.

The kernel of a composition-preserving map consists of inputs sent to the target identity. Here ker f={0,3}. Inputs differing by a kernel element have the same output: pairs {0,3},{1,4},{2,5}. A quotient groups such indistinguishable labels into classes. To recover k from remainder r=k mod 3, retain an extra label t=0 or 1 with k=r+3t. The remainder alone cannot reconstruct the input. A kernel is not a list of discarded errors; it identifies a precise ambiguity in the map.

## From a toy map to the source cover

For the source map use a triple (g₃,g₂,z) in SU(3)×SU(2)×U(1). The × means all combinations of one element from each factor, with componentwise multiplication. Define

Φ(g₃,g₂,z)=(z⁻²g₃,z³g₂).

The output is a color-first pair of blocks acting on H=C₃⊕W₂. Both blocks are unitary. Their determinants are z⁻⁶ and z⁶ because det g₃=det g₂=1. Their product is 1, placing the output in S(U(3)×U(2)). Scalar matrices commute with every matrix of the same size, so Φ preserves multiplication: (zz′)⁻²g₃g₃′=(z⁻²g₃)(z′⁻²g₃′), and similarly for the weak block. Such commuting elements are called central. The source calls this a cover and identifies its image with the full determinant-locked group. General surjectivity and topology are recognition-only here; the finite kernel is core work.

To get the identity output, solve z⁻²g₃=I₃ and z³g₂=I₂. These force g₃=z²I₃ and g₂=z⁻³I₂. The SU(3) determinant condition forces z⁶=1. The SU(2) condition gives z⁻⁶=1, the same restriction. Conversely, any unit phase with z⁶=1 and those scalar matrices satisfies every condition. This proves necessity and sufficiency, leaving no additional matrix choices hidden in the kernel.

Write ζ=cos(π/3)+i sin(π/3)=1/2+i√3/2. It is a turn of 60°. Six repeats give one full turn: ζ⁶=1; ζ³=−1. The six solutions of z⁶=1 are ζ^k for k=0,…,5. To see exhaustiveness on the unit circle, six times the angle must be an integer number of full turns. Within one turn the possible angles are exactly 0°,60°,120°,180°,240°,300°. Reduce exponents modulo 6; negative powers reverse the turn. Thus the kernel triples are (ζ^(2k)I₃,ζ^(−3k)I₂,ζ^k).

We can verify the key powers without a trigonometric table: ζ²=(1+2i√3−3)/4=−1/2+i√3/2. Then ζ³=[(−1+i√3)(1+i√3)]/4=(−1−3)/4=−1, with imaginary terms cancelling. Squaring ζ³ gives ζ⁶=1. The six successive powers have coordinates (1,0), (1/2,√3/2), (−1/2,√3/2), (−1,0), (−1/2,−√3/2), (1/2,−√3/2), confirming their distinctness exactly.

## C14.05-W1 — Worked example

The toy map above has output list (0,1,2,0,1,2) and kernel {0,3}. It is an analogy, not the source quotient. For the source choose k=1: z=ζ, g₃=ζ²I₃, g₂=−I₂. Their determinants are (ζ²)³=ζ⁶=1 and (−1)²=1. The color output scalar is ζ⁻²ζ²=1. The weak output scalar is ζ³(−1)=(−1)(−1)=1. This nonidentity input triple acts as identity on H.

## C14.05-P1 — Answered practice

For k=2, z=ζ², g₃=ζ⁴I₃ and g₂=I₂. Color action ζ⁻⁴ζ⁴=1 and weak action ζ⁶=1; determinants are ζ¹²=1 and 1. For k=3, z=−1, g₃=I₃,g₂=−I₂; again both actions and determinants equal 1. Complete the table before uncovering its entries:

| k | z | scalar in g₃ | scalar in g₂ | det g₃ | det g₂ | two output scalars |
|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 1 | 1 | 1,1 |
| 1 | ζ | ζ² | ζ³ | 1 | 1 | 1,1 |
| 2 | ζ² | ζ⁴ | 1 | 1 | 1 | 1,1 |
| 3 | ζ³ | 1 | ζ³ | 1 | 1 | 1,1 |
| 4 | ζ⁴ | ζ² | 1 | 1 | 1 | 1,1 |
| 5 | ζ⁵ | ζ⁴ | ζ³ | 1 | 1 | 1,1 |

Each g₃ exponent triples to a multiple of 6; each g₂ exponent doubles to a multiple of 6. Adding the output exponents (−2k+2k) and (3k−3k) gives zero. All six triples are distinct because z differs. Repeating the k=1 triple generates all six, returning after six products; hence this kernel is cyclic of order six, denoted Z6 or ℤ₆. Retain k to distinguish these six inputs when output is identity. For a general output, retain a chosen representative preimage plus which kernel element multiplies it; quotient output alone forgets that label.

Additional answered toy practice, C14-KER-D1 bridge: k mod 2 maps 0,…,5 to (0,1,0,1,0,1); its kernel is {0,2,4}. For recovery store r∈{0,1} and t∈{0,1,2}, then k=r+2t.

> Claim scope: S02 /backbone_sequence/9 states the quotient (SU(3)×SU(2)×U(1))/Z6 under the preserved-block/top-form contract. We have verified the displayed map's exact kernel. This is not a selection of a unique physical global form; Lesson 7 preserves the integration's wider family. No source data or residual component has been discarded.

## Diagnostics — C14.05-D1

1. Independently list the kernel of k mod 2 on addition modulo 6 (C14-KER-D1).
2. For k=5 verify the two source output scalars using reduced exponents.
3. Why can there be no seventh kernel element of the displayed Φ?
4. What labels must accompany quotient outputs for reconstruction? Explain separately for the mod-3 toy and the source kernel.

Worked answers: (1) Inputs 0,2,4 map to identity 0. (2) z=ζ⁵,g₃=ζ⁴I₃,g₂=ζ³I₂: color exponent −10+4=−6 and weak exponent 15+3=18 both yield 1. (3) Identity output fixes both matrices in terms of z, and det g₃=1 forces one of the six unit-circle roots. (4) For the toy keep r and t, k=r+3t; for the source keep a representative preimage and a kernel label k modulo 6. Neither image determines its original input alone.

Next dependency: [Lesson 6](lesson-06.md) distinguishes these transformation labels from a supplied action and its possible physical role.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# Lesson 6 — Local symmetry and physical role

Essential question: What must be supplied before an abstract symmetry becomes a rule acting on specified objects?

Goals: Name a group, carrier, and action separately; apply and invert two local phases; distinguish an invariant from an evolution rule.

Prerequisite bridge: Lesson 5 defined groups and maps, while Lesson 2 taught matrix actions and inverses. Now we distinguish the labels being composed from the objects they transform. One period is allocated.

## C14.06-E1 — A group needs an action

An abstract group specifies elements and composition. An action additionally tells how each element transforms each carrier element. Write ρ(g)v for this rule. It must satisfy ρ(identity)v=v and ρ(gh)v=ρ(g)(ρ(h)v). These equations say the action respects composition. The same group may have different actions. For U(1) on a single complex coordinate, ρ₁(z)v=zv and ρ₂(z)v=z²v both satisfy these equations. But i sends 1 to i in the first and to −1 in the second. In the second action −1 acts as identity, while in the first it does not. A group name alone therefore does not determine the action or its invisible elements.

A global phase on two nodes uses the same phase at both positions: (v₁,v₂)↦(zv₁,zv₂). A local choice allows independent phases z₁,z₂, so (v₁,v₂)↦(z₁v₁,z₂v₂). Here a node is just a labeled position in a toy model, not a detector observation. The local group is U(1)×U(1), with carrier ℂ² and action ρ(z₁,z₂)=diag(z₁,z₂). Composing two choices multiplies phases node by node. The inverse conjugates each phase. Squared norm |v₁|²+|v₂|² is preserved, as is each individual squared modulus.

“Local” tells where a transformation may vary. It does not say how values evolve with time or how nodes interact. An evolution rule would tell how a state changes between times; a coupling rule would relate different nodes. Neither follows from the norm calculation alone. A physical-role record must say what the coordinates represent, how the action is used, and what observational or dynamical rule connects them to a system. In a gauge interpretation, transformations may relate descriptions of one physical state; that interpretation is an additional contract, not a conclusion from matrix size.

## C14.06-W1 — Worked example

Choose carrier (v₁,v₂)=(1,1) and local phases (i,−i). The matrix diag(i,−i) gives (i,−i), squared norm 1+1=2. The inverse diag(−i,i) gives ((−i)i,i(−i))=(1,1). Choosing the global phase i instead gives (i,i). Both preserve norm but are different transformations of this input. The record must retain the two node labels and their two phase choices.

## C14.06-P1 — Answered practice

On (2,i), apply phases (−1,i). Output is (−2,−1), with squared norm 4+1=5 matching the input. Inverse phases (−1,−i) return (2,i). Record: group U(1)×U(1); carrier ℂ² with node order 1,2; action diag(z₁,z₂); invariant squared norm; inverse diag(z̄₁,z̄₂). The amplitudes and phase parameters suffice to replay either direction. For the single-node actions above, z=−1 sends v=2 to −2 under ρ₁ and to 2 under ρ₂, an explicit distinction even though the abstract group is the same.

> Claim scope: These node calculations are synthetic mathematical models. The source's typed-role rule (S02 /typed_conventions/logic) forbids identifying physical roles merely from an abstract group isomorphism. We assert no measured field, force, coupling, or time-evolution law from these examples.

## Diagnostics — C14.06-D1

1. Apply local phases (i,1) to (1,2) and invert.
2. Are ρ₁ and ρ₂ above the same action? Demonstrate with z=i,v=1.
3. Does preserved norm tell us how one node affects another? What extra rule is needed?
4. If only total norm 5 is saved from the practice example, can the amplitudes and phases be recovered?

Worked answers: (1) Output (i,2); inverse phases (−i,1) restore (1,2); norm stays 5. (2) No: outputs i and −1 differ. (3) No; a coupling or evolution rule must specify the relationship. (4) No: (√5,0), (2,i), and many other states share that norm. Retain the complex amplitudes, node ordering, and phase choices instead of replacing them by the scalar norm.

Next dependency: [Lesson 7](lesson-07.md) applies the same distinction between a mathematical construction and a wider physical-role claim when reading sources.
<!-- END: lesson-06 -->

<!-- BEGIN: lesson-07 -->
# Lesson 7 — Reconciling source branches

Essential question: How can we preserve two differently scoped source conclusions without silently replacing either one?

Goals: Build a source-addressed comparison; distinguish a checked finite calculation from reported proof status; preserve the physical global-form family and module namespaces.

Prerequisite bridge: Lesson 5 verified a specific kernel; Lesson 6 separated group, action, and physical role. We now read source claims with the same attention to their input contract. One period is allocated. All needed source cards are supplied here and in [sources.md](sources.md); no browsing or compiler work is a student prerequisite.

## C14.07-E1 — Reading an authority scope

A source address combines a file path with a pointer inside the file. For JSON, /backbone_sequence/9 means entry 9 of that array, counting from zero. A SHA-256 digest identifies particular bytes; matching it establishes byte identity, not mathematical truth. A namespace says which collection a label belongs to. “M03” in a compiler adjudication and “M03” in a mathematical backbone may designate entirely different things.

Use six evidence categories. A source fact says what a document records. A derived implication follows by explicit operations, such as our six-element kernel. An interpretation assigns a meaning or role to structure. A proposed mechanism adds a process explaining observations. Reference theory supplies established mathematical definitions used for comparison. An unresolved question names information not supplied by the current contract. This course contains source facts and mathematical derivations, not new empirical observations or an experimentally verified mechanism.

The mature source claims a connected determinant-locked group and a Z6 quotient. Its hypotheses preserve the Hermitian color and weak blocks and the top form. The integration asks a further physical global-form question and retains four admitted possibilities, Z1,Z2,Z3,Z6. Here Zn denotes a cyclic central subgroup of order n used in a candidate quotient; Z1 is the trivial subgroup. The numeral 6 in one explicit kernel does not answer every physical choice among these groups. Our comparison must retain both the construction and the unresolved physical family.

## C14.07-W1 — Worked source comparison

| Record | Exact address and identity | Claim and authority scope |
|---|---|---|
| Mature construction, S02 | Z:/Archive_20260911/Aug14_Sept1/K-Field_Mathematical_Essence_Mature_Complete_Proof_1788234894.json; /backbone_sequence/9; SHA-256 6f3e555ed161ef3311b31dcf64c003f4f8ec493f56d22356cf8d162467c1a2f3 | M10 reports S(U(2)×U(3)) and (SU(3)×SU(2)×U(1))/Z6 under the block/top-form contract. Use the explicit Lesson 3 permutation for its weak-first display. The carrier action and our kernel work use color-first S(U(3)×U(2)). |
| Accepted integration, I01 with I02 | Logical path applications/kfield_standard_model/collaborator_record/project_record.json, retrieved alias kfield_standard_model/project_record.json; /hazards/3 and /open_obligations/1–2; SHA-256 3800c854da827a64e72507722904bcafab07a31e88f2bc73920a8e7f62f62c1c | Retains physical global forms Z1,Z2,Z3,Z6. A unique physical member remains unresolved. I02's compiler adjudication grants direct authority only to compiler M03,M07,M08; the other 17 are conditional or unresolved. These labels are not mathematical-backbone labels. |

I02 is kfield_standard_model/evidence/p12_standard_model_compiler_adjudication_report.json, SHA-256 a3dfca0e55e525c6522c3088b95e5bcc048c141fce340bfe980fcfc14123220a, pointers /direct_authority_modules, /agda/certificate, /known_science_replay. Its reported certificate is KField.StandardModelCompilerAdjudication.p12-standard-model-compiler-adjudication. It was not freshly typechecked in this course. Current source-attributed RAG excerpts cover lines 1–101 for I02 and lines 1–142 for I01; their digests are reported by the retrieval service, not independently recomputed from local integration bytes.

S02 /branch_proofs/6 reports status closed_exact_gauge_matter_theorem for a wider branch. This is a source-reported endpoint, not a fresh proof of every branch statement here. Our verified content is the arithmetic, ordering, and finite kernel shown in the lessons. Full proof bodies and the physical discriminator remain outside this course's fresh verification. Keeping that boundary preserves information rather than deleting a source branch.

## C14.07-P1 — Answered practice

Classify three statements before reading the answer. “The displayed Φ has exactly six kernel elements” is a finite algebraic implication under its specified domain, freshly checked in Lesson 5. “Physical Z6 is uniquely selected” is not the integration's disposition; its unresolved family must remain. “A Safe Agda certificate is named in I02” is a retrieved source fact about formal adjudication, not a fresh compiler execution or source-author authentication.

To reconstruct the comparison, write two rows using the addresses above. In the mature row record preserved blocks/top form, the color-first correction, and the source's quotient. In the integration row record all four forms, unresolved physical selection, I01 pointer, and I02's distinct compiler namespace. Copying an identity digest is appropriate; inventing a stronger status is not.

> Claim scope: A fresh file hash check was performed on S01–S05. The integration statements were freshly retrieved as source-attributed excerpts from the pinned generation. No compiler rerun, general group-classification proof, or independent physical selection is claimed. Source-local closure and integration non-selection remain separate records.

## Diagnostics — C14.07-D1

1. Does our six-row table settle I01's physical global-form question? Explain the contract boundary.
2. What prevents compiler M03's direct authority from transferring to backbone M03?
3. What does a matching source hash establish, and what does it not establish?
4. Write one sentence retaining both the mature quotient and integration family without contradiction.

Worked answers: (1) No; the table verifies the kernel of the displayed action, whereas I01 asks which physical global form is independently selected. (2) They are different namespaces and contracts; a shared number supplies no connecting proof. (3) It establishes identical bytes, not correctness, authorship, or a fresh typecheck. (4) Under its preserved-block/top-form contract M10 reports a Z6 quotient, while the integration retains Z1,Z2,Z3,Z6 with physical selection unresolved.

Next dependency: [Capstone](capstone.md) traces the whole carrier-to-cover calculation and builds a source comparison using these cards.
<!-- END: lesson-07 -->
