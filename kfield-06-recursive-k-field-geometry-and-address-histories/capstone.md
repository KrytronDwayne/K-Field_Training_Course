# Capstone — Two trees, one complete record

Allow two 55-minute periods. Work with exact fractions and integers. All intervals and toy volumes are classroom constructions. Source object names and rules are scoped in sources.md. You may use lessons and a calculator, but explain every count. No infinite limits are required.

## Student tasks (100 points)

1. **C06-CAP-01 (12):** Starting from [0,1), draw the binary interval tree through n2=3. Output each index, half-open interval and parent. State who owns 1/2 and whether endpoint 1 is a geometric vertex.
2. **C06-CAP-02 (10):** Build the one-coordinate ternary residue tree through d3=2. Label each modulus and parent. State three-coordinate counts at d3=0,1,2 and explain why this is not binary subdivision.
3. **C06-CAP-03 (16):** For fixed outer 3B, derive cell and distinct corner counts at n2=0,1,2. Give length/area/volume factors relative to depth zero. Verify the toy total volume 162 at depth 2 using base-cell volume 6.
4. **C06-CAP-04 (10):** Encode integers 5 and 8 in three balanced digits, low-to-high. Show the repeated remainder steps and decode each word.
5. **C06-CAP-05 (10):** For both integers give depth 3,2,1 standard and balanced representatives. Check modular compatibility by differences. Explain why removing the low digit is wrong.
6. **C06-CAP-06 (14):** Record and recover binary indices 5 and 6 at depth 3 from coarse parents and bits. Recover the words for 5 and 8 from depth-2 balanced words plus high digits. Include metadata and all zero details; give two possible children if detail is omitted.
7. **C06-CAP-07 (8):** Explain what 27 window nodes, 27 Group volumes and 729 Supergroup volumes count. Derive the last number two ways.
8. **C06-CAP-08 (8):** State the domain of 3^g_rung×2^n_rung+1=10. Derive the unique solution and bound the finite search. Explain why 729 volumes and 27^2 classes are different objects.
9. **C06-CAP-09 (12):** For centered 9B, derive 6859 half-step points and 55 reachable integer-lambda sheets. Show every intermediate sheet is attained. Contrast 729 volumes and 1000 ordinary corners. Repeat half-step and sheet counts for 3B.

## Full worked answer key and rubric

### 01 — Binary tree (12)

At depth zero: index 0, [0,1), no parent. At depth 1: indices 0,1, intervals [0,1/2),[1/2,1), both parent 0. At depth 2: indices 0,1,2,3, intervals [0,1/4),[1/4,1/2),[1/2,3/4),[3/4,1), parents 0,0,1,1. At depth 3:

| j | Interval | Parent at depth 2 |
|---|---|---|
| 0 | [0,1/8) | 0 |
| 1 | [1/8,2/8) | 0 |
| 2 | [2/8,3/8) | 1 |
| 3 | [3/8,4/8) | 1 |
| 4 | [4/8,5/8) | 2 |
| 5 | [5/8,6/8) | 2 |
| 6 | [6/8,7/8) | 3 |
| 7 | [7/8,1) | 3 |

Connect each child to its listed parent to draw the tree. At depth 3 index 4 owns 1/2; at depth 2 index 2 does; at depth 1 index 1 does. Endpoint 1 is a geometric boundary vertex but not an owned point. Award 4 for complete indices/depths, 4 for intervals, 2 for parents, 2 for boundary explanation.

### 02 — Ternary tree (10)

Depth 0 has class 0 modulo 1. Its depth-1 children modulo 3 are 0,1,2. Their depth-2 children modulo 9 are respectively (0,3,6), (1,4,7), (2,5,8). Each child reduces modulo 3 to its parent. Three-coordinate counts are 1,27,729 because each coordinate has 1,3,9 choices. This refines residue information; binary subdivision halves geometric intervals. Award 4 for all edges, 2 for moduli, 2 for product counts, 2 for type distinction.

### 03 — Scale and corners (16)

There are m=3×2^n2 cells and m+1 vertices per axis, hence cells m^3 and corners (m+1)^3. Depths 0,1,2 give cells 27,216,1728 and vertices 64,343,2197. Length factors are 1,1/2,1/4; area factors 1,1/4,1/16; volume factors 1,1/8,1/64. The outer boundary remains fixed. At depth 2 the toy subcell volume is 6/64=3/32; multiplying 1728 gives 162 cubic units. Eight corners per cell counts incidences and repeats shared corners. Award 4 for derivation, 4 for count table, 4 for factors, 2 for volume, 2 for shared-boundary explanation.

### 04 — Balanced words (10)

For 5: choose −1, quotient (5+1)/3=2; choose −1, quotient (2+1)/3=1; choose +1, quotient 0. Word (−1,−1,1) decodes −1−3+9=5. For 8: choose −1, quotient 3; choose 0, quotient 1; choose +1, quotient 0. Word (−1,0,1) decodes −1+0+9=8. Both records have d3=3, low-to-high order. Award 3 per encoding process, 1 per decoding, 2 for depth/order.

### 05 — Histories (10)

For 5, standard representatives are 5,5,2 under moduli 27,9,3. Balanced representatives are 5,−4,−1; differences 9 and −3 are divisible by parent moduli 9 and 3. For 8, standard representatives are 8,8,2, balanced 8,−1,−1; differences 9 and 0 pass. Removing the highest digit leaves the low places; removing the lowest from (−1,0,1) and shifting instead gives (0,1)=3, which is the wrong mod-9 parent. Award 4 for histories, 4 for divisibility checks, 2 for digit-removal explanation.

### 06 — Recovery (14)

Binary records at child depth 3: (k,b)=(2,1) recovers j=2×2+1=5; (3,0) recovers 6. Record type=binary interval. Ternary records at d3=3: low word (−1,−1), r=−4, high digit +1 reconstructs 5=−4+9; low word (−1,0), r=−1, high digit +1 reconstructs 8=−1+9. Record balanced representation, depth, low-to-high order, rule t=r+9e and the full low word, including its zero. Without bit, binary parent 2 permits 4 or 5. Without high digit, ternary parent −1 permits −10,−1 or 8 at depth 3. Award 4 for binary, 4 for ternary, 4 for metadata/zeros/rules, 2 for alternatives. A record that cannot recover the original word cannot earn full recovery credit even if its scalar result is right.

### 07 — Typed objects (8)

The window samples three half-step positions per axis: 27 points. The Group contains three complete cells per axis: 27 regions. The Supergroup has nine per axis: 9^3=729 regions, also 27 Groups×27 cells. Counts are dimensionless; a cell volume measured numerically needs cubic length units. Award 2 each for the three object distinctions and 2 for the two Supergroup derivations.

### 08 — Rung (8)

Both exponents are nonnegative integers. Subtract 1: product=9. Since 9 is odd, n_rung=0; then 3^g_rung=9 gives g_rung=2. Finite bounds g≤2,n≤3 follow from 3^3>9 and 2^4>9, as all other factors are at least 1. Only table pair (2,0) has product 9. The value 729 labels volumes in one setting and residue triples in the other. Award 2 domain, 3 argument, 2 bounds, 1 type distinction.

### 09 — Half-step geometry (12)

Labels −9..9 represent coordinates i/2, giving 19 positions per axis and 19^3=6859 points. Lambda=i+j+k ranges −27..27, so 55 candidate sheets. For t≥0 use (t,0,0) up to 9, (9,t−9,0) up to 18, (9,9,t−18) up to 27. Negate for negative targets, proving all 55 occur. Ordinary cell corners give (9+1)^3=1000; complete volumes give 9^3=729. For 3B, labels −3..3 give 7^3=343 points and sums −9..9 give 19 sheets. Award 3 point count, 2 sheet count, 3 reachability proof, 2 grid distinctions, 2 smaller case.

## Residual accounting and source scope

These finite records preserve all removed bits/digits with their signs, zeros, ordering and depths. A coarse-only answer must state its missing possibilities. S02 M03 defines source objects and the two recursion rules; our arithmetic establishes the finite answers above. The synthetic interval and volume examples are not measurements. Infinite histories and physical mechanisms are outside the assessed operations.
