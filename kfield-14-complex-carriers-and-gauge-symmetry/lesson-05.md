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
