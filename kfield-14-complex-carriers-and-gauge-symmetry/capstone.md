# Capstone — From a typed carrier to a cover kernel

Use three 55-minute periods: arithmetic and carrier (steps 1–3), determinant and kernel (4–5), action and source comparison (6–7). All examples are dimensionless and synthetic. Use the source cards in Lesson 7 and sources.md. This is an open-note assessment of taught operations, with no compiler, calculus, external research, or general group-classification proof required.

## Student tasks

1. **C14-CAP-01 (10 points).** Start with 2−i. Give its conjugate, rotate by i, compute both squared moduli and moduli, give the rotated conjugate, and recover the input. Explain why retaining only a modulus would lose information.
2. **C14-CAP-02 (15 points).** For V=(1/√2)[[1,i],[i,1]], compute V†V, apply V to (1,i), check squared norm, and invert the output. Explain why transpose alone is inadequate.
3. **C14-CAP-03 (15 points).** Convert the weak-first tuple (i,−1,2,0,1+i) to color-first using P from Lesson 3. Write both projections and reconstruct the tuple. Transform the charge matrix diag(3,3,−2,−2,−2), stating the conjugation formula. Recover the weak-first tuple.
4. **C14-CAP-04 (15 points).** Compute the determinant product for color diag(−1,−1,1) and weak diag(i,−i). Derive the central exponent for weights a,b, then test a=−2,b=3. Contrast this with diag(2,1/2): distinguish norm and top-form preservation.
5. **C14-CAP-05 (25 points).** Enumerate the toy map k mod 3 from addition modulo 6 and its kernel. Separately enumerate all six kernel triples of Φ(g₃,g₂,z)=(z⁻²g₃,z³g₂). Use ζ=1/2+i√3/2 and powers reduced modulo 6. Verify both determinants and both action blocks in every row; explain why there are no additional kernel elements. State what extra labels are required for reversible accounting.
6. **C14-CAP-06 (10 points).** Apply local phases (−1,i) to (2,i), invert, and check the norm. Name group, carrier, action, and invariant. Explain which further physical rule is absent.
7. **C14-CAP-07 (10 points).** Make two source-addressed rows: mature determinant-lock construction and integration global-form disposition. Include paths, hashes, pointers, hypotheses, full family, and distinct compiler namespace. Distinguish source-reported formal status from fresh checks. Preserve unresolved branches explicitly.

## Full worked answer key and scoring rubric

1. Conjugate 2+i. Rotated value i(2−i)=1+2i, whose conjugate is 1−2i. Squared moduli both equal 5; both moduli equal √5. Multiplying 1+2i by −i gives 2−i. Magnitude alone leaves direction unresolved. Award 2 points for conjugates, 2 for rotation, 2 for sizes, 2 for inverse, 2 for information accounting.
2. V†=(1/√2)[[1,−i],[−i,1]]. Multiplication yields (1/2)[[2,0],[0,2]]=I₂. V(1,i)=(0,√2 i); its squared norm is 2, matching 1+1. V†(0,√2 i)=(1,i). VᵀV=[[0,i],[i,0]]≠I₂, so dropping conjugation fails. Award 5 points for dagger-product with entries, 3 for action, 2 for norm, 3 for recovery, 2 for transpose distinction.
3. h=(2,0,1+i,i,−1). P_ch=(2,0,1+i,0,0) and P_wh=(0,0,0,i,−1); their sum is h. A_new=P A_old Pᵀ=diag(−2,−2,−2,3,3). Applying Pᵀ recovers (i,−1,2,0,1+i). Award 3 for permutation, 4 for both projections and sum, 5 for matrix formula and weights, 3 for inverse.
4. Color determinant (−1)(−1)·1=1; weak determinant i(−i)=1; product 1. Each diagonal entry has modulus 1, so these blocks also preserve norm. The central determinant is (z^a)³(z^b)²=z^(3a+2b); −6+6=0. diag(2,1/2) has determinant 1 but sends (1,0) to (2,0), changing squared norm 1 to 4. Award 4 for determinant product, 5 for exponent and lock, 2 for norm check of the blocks, 4 for the counterexample.
5. Toy outputs are 0,1,2,0,1,2; kernel {0,3}. The source table is below. Award 3 points for toy, 6 for six source triples, 6 for determinant/action checks, 6 for necessity and sufficiency, 4 for retained-label accounting.

| k | z | g₃ | g₂ | determinant exponents (mod 6) | action exponents (mod 6) |
|---|---|---|---|---|---|
| 0 | 1 | I₃ | I₂ | 0,0 | 0,0 |
| 1 | ζ | ζ²I₃ | ζ³I₂ | 0,0 | 0,0 |
| 2 | ζ² | ζ⁴I₃ | I₂ | 0,0 | 0,0 |
| 3 | ζ³ | I₃ | ζ³I₂ | 0,0 | 0,0 |
| 4 | ζ⁴ | ζ²I₃ | I₂ | 0,0 | 0,0 |
| 5 | ζ⁵ | ζ⁴I₃ | ζ³I₂ | 0,0 | 0,0 |

For every row the determinant exponents are 3(2k) and 2(−3k), multiples of 6. Action exponents are −2k+2k=0 and 3k−3k=0. Identity output forces g₃=z²I₃ and g₂=z⁻³I₂; determinant one forces z⁶=1. Exactly six unit-circle roots exist, and all six listed rows work, proving exhaustion. Retain r and t in k=r+3t for the toy. For a source quotient retain a chosen preimage representative plus a kernel member label; on the identity image, retain k itself. The toy kernel is not substituted for the source kernel.

6. Output (−2,−1); inverse diag(−1,−i) returns (2,i). Squared norm before and after is 5. Group U(1)×U(1), carrier ℂ² in node order 1,2, action diag(z₁,z₂), invariant sum of squared moduli. No coupling or time-evolution equation has been supplied. Award 2 each for action, inverse, norm, group/carrier/action record, and missing physical rule.
7. A full answer may reproduce the two-row Lesson 7 table. Mature row: S02 path and digest from the source card, /backbone_sequence/9, preserved Hermitian blocks and top form, explicit color-first correction S03 /findings/3, source-reported Z6 quotient with freshly verified finite kernel. Integration row: I01 logical path and retrieved alias, digest 3800c854da827a64e72507722904bcafab07a31e88f2bc73920a8e7f62f62c1c, /hazards/3 and /open_obligations/1–2; Z1,Z2,Z3,Z6 remain admitted, physical member unresolved. Attach I02 path and digest from Lesson 7 with /direct_authority_modules: compiler M03,M07,M08 only, not backbone labels. The named Agda certificate was not rerun. Award 2 for exact addresses/digests, 2 for mature hypotheses/quotient and correction, 2 for full integration family and unresolved status, 2 for compiler namespace, 2 for fresh-versus-reported boundary.

Total: 100 points. Use the item-level rubric for feedback; a score is descriptive, not permission to erase incorrect or incomplete work. Preserve the original response, corrected response, and remaining question. A learner who mixes block order, substitutes the toy kernel, or collapses the global-form family revisits the corresponding practice even if the total score is high.

## Backward dependency map

| Step | Prior introduction | Prior worked example | Prior answered practice | Diagnostic |
|---|---|---|---|---|
| C14-CAP-01 | C14.01-E1 | C14.01-W1 | C14.01-P1 | C14.01-D1 |
| C14-CAP-02 | C14.02-E1 | C14.02-W1 | C14.02-P1 | C14.02-D1 |
| C14-CAP-03 | C14.03-E1 | C14.03-W1 | C14.03-P1 | C14.03-D1 |
| C14-CAP-04 | C14.04-E1 | C14.04-W1 | C14.04-P1 | C14.04-D1 |
| C14-CAP-05 | C14.05-E1 | C14.05-W1 | C14.05-P1 | C14.05-D1 |
| C14-CAP-06 | C14.06-E1 | C14.06-W1 | C14.06-P1 | C14.06-D1 |
| C14-CAP-07 | C14.07-E1 | C14.07-W1 | C14.07-P1 | C14.07-D1 |
