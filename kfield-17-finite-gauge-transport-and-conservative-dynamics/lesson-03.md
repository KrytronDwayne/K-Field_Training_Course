# Lesson 03 — Loops and holonomy

Essential question: What remains after transport around a closed path?

Goals: multiply two small matrices in order; state a loop's basepoint and path; verify its conjugation rule under a frame change.

Prerequisite bridge: lesson 02 cancelled adjacent inverse frame maps on one link. We will cancel them on a chain. Two periods of 55 minutes: period A teaches matrix multiplication and ordered paths; period B teaches frame cancellation and checks. Each uses 5 retrieval, 20 teaching, 15 practice, 15 diagnostics/repair.

## C17.03-E1 — From successive maps to a loop

If A acts after B, the composite map is AB. To find AB, apply A to each column of B. Equivalently, multiply rows of A by columns of B. For A=[[a,b],[c,d]] and B=[[e,f],[g,h]], this gives [[ae+bg,af+bh],[ce+dg,cf+dh]]. The upper-right entry uses the first row of A and second column of B. This rule comes from applying the maps to (u,v) and collecting its coefficients. Matrix multiplication is associative: (AB)C=A(BC), because both describe the same successive actions. It need not be commutative: AB may differ from BA.

A loop starts and ends at one site, the basepoint. With our subscript convention, U_loop=U01 U12 U20 acts on site 0 by the path 0→2→1→0. Do not read it as 0→1→2→0. The rightmost map U20 acts first. The result is called holonomy, the net transport around the loop. It can differ from I even though the endpoint is the starting point.

The loop in new coordinates is

    (G0 U01 G1⁻¹)(G1 U12 G2⁻¹)(G2 U20 G0⁻¹)
    = G0 (U01 U12 U20) G0⁻¹.

The G1 and G2 factors cancel with their adjacent inverses. The operation G0 U_loop G0⁻¹ is called conjugation. It changes the description at the basepoint. A change of basepoint requires transport of the loop description as well; a bare list of matrix entries without a basepoint is incomplete.

## C17.03-W1 — Order matters

Define X=[[0,1],[1,0]], Z=diag(1,−1), and I=diag(1,1). X swaps two components, while Z reverses the second one's sign. Choose U01=X, U12=Z, U20=I. Then

    XZ = [[0·1+1·0, 0·0+1·(−1)],
          [1·1+0·0, 1·0+0·(−1)]] = [[0,−1],[1,0]].

The loop sends (1,0) first to itself under I, then itself under Z, then (0,1) under X. Reversing just the X and Z order gives ZX=[[0,1],[−1,0]], which sends (1,0) to (0,−1). Thus ZX=−XZ. All three links are unitary: X and Z are real symmetric, and each squares to I.

With G0=Z the worked loop becomes Z(XZ)Z=ZX=−XZ. This is conjugation, not a claim that the underlying path has reversed. Reversing a path instead uses the inverse links in reversed order; for a unitary loop its reverse is U_loop†.

## C17.03-P1 — Exchange the assigned links

Set U01=Z, U12=X, U20=I. Compute the loop, apply it to (1,0), and conjugate it by Z. Compare with the worked example. Also compute the scalar loop U01=i, U12=1, U20=i.

Worked answer: the new matrix loop is ZX=[[0,1],[−1,0]], giving (0,−1). Z(ZX)Z=XZ=−ZX, giving (0,1) if applied to the same numerical column. For a full frame comparison the input column must also transform. The scalar loop is i·1·i=−1. Scalar numbers commute; these scalar links provide no justification for exchanging matrix factors.

> Claim scope: These are synthetic ordered finite loops. They illustrate S02 M13's ordered plaquette products. A plaquette is an elementary closed face in a lattice model; our three-edge example teaches the algebra without claiming it is the archived native lattice. Keep links, path, basepoint, and loop; the loop alone cannot reconstruct every individual link.

## Diagnostic checks

1. **C17.03-D1:** Does i·1·i=−1 allow reordering all gauge links?
2. Write the input and output sites of U12 and explain why it follows U20 in our loop.
3. Find X² and Z². What are X⁻¹ and Z⁻¹?
4. Why are intermediate frame factors cancelled but not the two G0 factors across the loop?

Answers: (1) No; XZ and ZX above give a counterexample. (2) U12 maps 2 to 1, so its input matches U20's output 2. (3) Both squares are I, so each is its own inverse. (4) G0 and G0⁻¹ enclose U_loop and are not adjacent. Removing them would assume an unjustified reordering.

Next dependency: [lesson 04](lesson-04.md) extracts an invariant number while retaining the full loop.
