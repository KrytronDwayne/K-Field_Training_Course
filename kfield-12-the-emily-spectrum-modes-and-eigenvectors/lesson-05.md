# Lesson 05 · Counting Emily multiplicities

**Essential question:** What exactly is being counted when the same seven numbers appear in different places?

**Goals:** Build all seven multiplicities; distinguish modes from nodes; decompose a pattern into antipodal even and odd parts; count the independent parity coordinates.

**Prerequisite bridge.** Each of the three mode choices contributes +√2,0,or −√2 to a product eigenvalue. Divide the common symbolic factor √2 out of the bookkeeping and call those contributions +1,0,−1. The sum m gives eigenvalue m√2. Two periods separate mode counting from node and function parity.

## C12.05-E1 · Count ordered choices

For two choices, sums −2,−1,0,1,2 occur 1,2,3,2,1 times: −2 uses (−1,−1), −1 uses (−1,0),(0,−1), and 0 uses (−1,1),(0,0),(1,−1). Reverse signs for positive sums. To add the third choice and get m, use earlier sums m+1, m, or m−1 according to whether the last choice is −1,0,or 1. Add those three earlier counts; outside the two-choice range use zero. This sliding addition is sometimes called convolution; only finite addition is needed here.

## C12.05-W1 · The complete Emily ledger

The table lists every ordered mode triple. A string such as `+0−` means the factor order (u+,u0,u−), not a node address. Distinct permutations give distinct patterns even when the eigenvalue agrees.

| m | Eigenvalue | All mode labels | Multiplicity |
|---|---|---|---|
| −3 | −3√2 | `−−−` | 1 |
| −2 | −2√2 | `−−0`, `−0−`, `0−−` | 3 |
| −1 | −√2 | `−00`, `0−0`, `00−`, `−−+`, `−+−`, `+−−` | 6 |
| 0 | 0 | `000`, `+0−`, `+−0`, `0+−`, `0−+`, `−+0`, `−0+` | 7 |
| 1 | √2 | `+00`, `0+0`, `00+`, `++−`, `+−+`, `−++` | 6 |
| 2 | 2√2 | `++0`, `+0+`, `0++` | 3 |
| 3 | 3√2 | `+++` | 1 |

For example, m=0 receives two-choice counts 2+3+2=7; the labels show one all-zero choice and six arrangements of +,0,−. The total 1+3+6+7+6+3+1=27 accounts for every choice. **Multiplicity** here is the number of independent modes with that eigenvalue; Lesson 04's orthogonality ensures these listed modes are independent.

Now distinguish two other countings. For *nodes* L=(i,j,k), the source sheet label is λ_sheet=i+j+k. This is not the adjacency eigenvalue λ. The node populations have the same 1,3,6,7,6,3,1 list because the same sum-counting works on coordinate choices. Define the node label χ(L)=(-1)^(i+j+k): it is +1 on even integer sums and −1 on odd sums, including negative integers. Hence there are 3+7+3=13 positive-χ nodes and 1+6+6+1=14 negative-χ nodes. These are labels of addresses, not parity of functions.

For *functions*, reflection R sends a pattern f to Rf with (Rf)(L)=f(−L); it swaps antipodal addresses. An even function satisfies Rf=f; an odd function satisfies Rf=−f. Every pattern splits reversibly as e=(f+Rf)/2 and o=(f−Rf)/2, with f=e+o. On a pair having values a,b, these parts have values ((a+b)/2,(a+b)/2) and ((a−b)/2,(b−a)/2). Their sum recovers a,b. The center is fixed, so an odd function must have center value 0.

The 26 noncentral nodes make 13 pairs. One even value per pair plus an independent center value gives 14 even coordinates. One signed odd value per pair gives 13 odd coordinates. This is the source's 14-even/13-odd *node-function* split. On one path, u+ and u− are both even under reflection, while u0 is odd. Thus a mode's eigenvalue sign is not its reflection parity.

## C12.05-P1 · Guided practice and answers

Enumerate m=1: three placements of + in (+,0,0), and three placements of − in (+,+,−), give 6. Re-add the ledger to get 27. Split f=(1,2,3): Rf=(3,2,1), e=(2,2,2), o=(−1,0,1); adding gives f. Count the Lucas pairs: (27−1)/2=13, so even dimension 13+1=14 and odd dimension 13. Recompute χ counts by even versus odd sheet sums: 13 and 14. Notice that χ-positive count 13 does not equal the even-function count 14.

> **Claim scope and source card.** S02 /backbone_sequence/7/proof/4–5 and /backbone_sequence/7/emily_spectrum support the mode ledger and function parity; /backbone_sequence/2/sheet_populations supports the separate node ledger. Thirteen antipodal pairs are pairs of addresses. Thirteen decoder channels in S02 /backbone_sequence/16 are decoder inputs; seven syndrome dimensions are retained residual coordinates there. These are different carriers. No common count supplies an operator-preserving map. The full decoder is recognition-only in this course.

## C12.05-D1 · Diagnostic checks

1. Derive the multiplicity at m=−1 using the two-choice counts.
2. Why are there 14 even function coordinates but only 13 odd ones?
3. Split (4,1,0) into even and odd path parts and reconstruct it.
4. Do seven sheet populations and seven distinct Emily eigenvalues establish an identification? Compare χ counts with function parity counts.

**Worked answers.** 1. Earlier sums 0,−1,−2 contribute 3+2+1=6. 2. Both have 13 pair coordinates; only the even part has an unrestricted center. 3. Rf=(0,1,4), e=(2,1,2), o=(2,0,−2); e+o=(4,1,0). 4. No: sheet populations count nodes, eigenvalues classify modes; a map and operators remain to be specified. χ has 13 positive and 14 negative nodes, while function parity has 14 even and 13 odd dimensions.

**Next dependency:** [Lesson 06](lesson-06.md) uses modes to reconstruct a state and explains exactly what happens to its uniform mean.
