# Lesson 04 — A finite gauge-invariant action

Essential question: How can a loop change its components while a quantity calculated from it stays the same?

Goals: compute a trace and an action term; verify action invariance under the taught frame changes; explain what the action does not retain.

Prerequisite bridge: lesson 03 showed U′_loop=G0 U_loop G0⁻¹. We now seek a number unchanged by this conjugation. Pacing: 5 retrieval, 20 teaching, 15 practice, 15 diagnostics; 55 minutes.

## C17.04-E1 — Trace and action

The trace Tr of a square matrix is the sum of its diagonal entries. For [[a,b],[c,d]], Tr=a+d. Re means take the real part of a complex number. For a scalar, treat it as a 1 by 1 matrix: its trace is itself, and I is the number 1. Keep this dimension distinction when computing Tr(I).

For two 2 by 2 matrices A and B, Tr(AB)=ae+bg+cf+dh using lesson 03's entries. Tr(BA)=ea+fc+gb+hd is the same sum, since individual number products commute. Therefore Tr(AB)=Tr(BA), even when AB≠BA. Put A=G and B=U G⁻¹ to obtain Tr(GUG⁻¹)=Tr(U G⁻¹G)=Tr(U). This moves a whole factor cyclically inside the trace; it does not license arbitrary reordering of matrices.

Define the single-loop action S=β ReTr(I−U_loop), with β>0. Here β has declared action units AU, so S has AU; the matrix term is dimensionless. AU is an illustrative unit of energy times time, not a measured energy transfer. For several loops, sum their terms with their own positive β_p. This has the form of the finite action in S02 M13. Since both Tr(I) and Tr(U_loop) are unchanged by conjugation, S is unchanged. That is finite gauge invariance. It is a property of relabeling local frames, not automatically a time-conservation law.

The matrix F=I−U_loop is another possible retained comparison coordinate. Given F and I, recover U_loop=I−F. Taking just its trace loses information. We therefore keep the links, U_loop, F, β, and S together.

## C17.04-W1 — Equal action, different entries

For U_loop=XZ=[[0,−1],[1,0]], F=[[1,1],[−1,1]]. Tr(F)=2. With β=3 AU, S=3·2=6 AU. Under conjugation by Z, U′=−XZ=[[0,1],[−1,0]] and F′=[[1,−1],[1,1]]. Its trace is again 2, so S′=6 AU. The off-diagonal signs changed and remain in our record. Equal traces do not say F=F′.

## C17.04-P1 — Matrix and scalar cases

1. Use the practice matrix loop ZX and β=2 AU. Find F and S before and after conjugation by Z.
2. Use scalar links (U01,U12,U20)=(i,1,i), with β=2 AU. Change frames with (G0,G1,G2)=(−1,i,1). Compute all transformed links and the action.

Worked answers: (1) F=[[1,−1],[1,1]], trace 2, action 4 AU. Conjugation gives XZ and F′=[[1,1],[−1,1]], still action 4 AU. (2) U′01=(−1)i(−i)=−1, U′12=i·1·1=i, and U′20=1·i·(−1)=−i. Their product (−1)i(−i)=−1 equals the original i·1·i. In one dimension I−U=1−(−1)=2, so the action is 4 AU in each frame. Matching this scalar action to the matrix action does not equate their state spaces or loops.

> Claim scope: The action form is source-grounded at S02 /backbone_sequence/12/definitions. Our coefficients and loops are synthetic. Gauge invariance follows from finite algebra. No archived field values, observed forces, or continuum dynamics were calculated.

## Diagnostic checks

1. **C17.04-D1:** Can a loop be reconstructed from its trace alone? Use XZ and ZX.
2. What is the action of a 2 by 2 identity loop with β=3 AU?
3. Why does Tr(I) equal 2 in the matrix example but 1 in the scalar example?
4. Is invariance under a frame change the same claim as conservation through time?

Answers: (1) No; both have trace 0 but different entries. (2) I−I is zero, so S=0 AU. (3) There are two diagonal ones versus one. (4) No. A frame change re-expresses a configuration; a time update changes the state according to another specified rule. Lesson 05 supplies such a rule.

Next dependency: [lesson 05](lesson-05.md) constructs an invertible finite time step and checks its norm.
