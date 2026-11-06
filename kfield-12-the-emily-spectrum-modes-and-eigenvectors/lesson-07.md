# Lesson 07 · Spectral resemblance and typed identity

**Essential question:** What must a map preserve before two spectral descriptions can be identified?

**Goals:** Name the input and output spaces and operators; test an invertible map by two calculation routes; distinguish count agreement from an operator-preserving identification.

**Prerequisite bridge.** Lessons 01–06 taught matrix action, linearity, modes, and reversible coordinates. We now compare two systems using an explicit map T. A **domain** is the set of allowed inputs; a **codomain** is the declared output set. A **carrier** names the kind of object: node functions, node labels, or decoder channels, for example.

## C12.07-E1 · Compare two routes

Suppose A_X acts on states in X, B_Y acts on states in Y, and T sends X states to Y states. To preserve the action, both routes must agree for every state x:

B_Y(Tx)=T(A_X x), abbreviated B_Y T=T A_X.

Read composition right to left: first T, then B_Y on the left; first A_X, then T on the right. Such a map is called an **intertwiner**. For an identification of whole state spaces, also require T to be invertible: another rule recovers every original x. Counts or matching spectra alone do not verify a proposed T.

How can a finite check establish “every x”? For two-coordinate states, write x=a(1,0)+b(0,1). If both routes agree on (1,0) and (0,1), linearity makes them agree on every such combination. The two resulting columns form the matrix of the composite action. This teaches the needed matrix product without a new general algorithm.

The local name B_Y is an operator in this lesson, not the source-locked geometric basis B of Cell3. No metric or physical unit is being transferred here.

## C12.07-W1 · A genuine swap identification

Let X and Y each be ordered pairs of real numbers. Define A_X(a,b)=(a,2b), B_Y(p,q)=(2p,q), and T(a,b)=(b,a). In matrix shorthand A_X=diag(1,2), B_Y=diag(2,1), T=[[0,1],[1,0]]. “diag” means the listed numbers sit on the main diagonal and other entries are zero.

Route one gives B_Y T(a,b)=B_Y(b,a)=(2b,a). Route two gives T A_X(a,b)=T(a,2b)=(2b,a). Both are the matrix [[0,2],[1,0]] applied to (a,b). Since swapping twice restores (a,b), T is invertible. For x=(3,4), Tx=(4,3), both routes give (8,3), and T(Tx)=(3,4).

This also transports eigenvectors: if A_X v=λv, then B_Y(Tv)=T(λv)=λTv. Invertibility keeps Tv nonzero. The equation, not the matching number of entries, supplies the connection.

## C12.07-P1 · Guided practice and answers

Propose instead T=I, the identity map I(a,b)=(a,b). The routes give (2a,b) and (a,2b). Their difference is (a,−b), the matrix diag(1,−1) applied to the input. On (1,0) the routes differ, so this proposed map fails even though A_X and B_Y each have eigenvalues 1 and 2. The successful swap still exists; failure of one map does not refute all possible maps.

For the successful T, x=(1,−2) maps to (−2,1), then swaps back exactly. Both routes yield (−4,1). Now compare adjacency modes with node sheets: naming seven groups on each side does not specify an operator on sheet data, a domain of states there, or an invertible T to adjacency modes. Record these as missing specifications, not as an identification.

Reflection R on the Lucas graph does commute with adjacency. To see this, reflecting each neighbor of L gives exactly a neighbor of −L, because open coordinate steps reflect to open coordinate steps. Thus summing reflected input neighbors and reflecting the neighbor-sum output agree: A_L R=R A_L. Consequently an even input has even output and an odd input has odd output. This preserves the full 14-even/13-odd sectors. It does not additionally preserve the constant line, as Lesson 06 showed. Practice this distinction on the path: for f=(1,2,3), ARf=A(3,2,1)=(2,4,2)=RAf.

> **Claim scope.** Source carriers remain separate: 27 Emily modes in seven eigenvalue groups; 27 node addresses in seven sheet populations; 13 antipodal address pairs; 13 decoder channels; and a seven-dimensional decoder syndrome (S02 /backbone_sequence/7, /2/sheet_populations, /16). In M17 the 13-by-6 matrix has rank 6, independently checked in the teacher verification, leaving seven residual coordinates. Its full decoder is recognition-only here. Backbone M08 is not automatically compiler module M08. S03 /findings/1 reports missing formula-DAG expansions; this finite course does not certify global source closure or rerun formal integration proofs.

## C12.07-D1 · Diagnostic checks

1. Calculate both swap routes on (2,5) and give the inverse of T.
2. Give one input refuting T=I for the same A_X,B_Y.
3. What three specifications are absent from a bare assertion that sheet populations “are” Emily modes?
4. Does reflection symmetry justify dropping a uniform Emily mode? Explain using two separately tested properties.

**Worked answers.** 1. Both give (10,2); the inverse is the same swap. 2. (1,0): B_Y I gives (2,0), while I A_X gives (1,0). 3. Explicit carriers/state spaces, the operators on both sides, and an invertible map satisfying the two-route equation. 4. No. Reflection commutes with adjacency and preserves even/odd sectors. The constant line is not invariant because its adjacency output is the nonconstant degree vector. These are different claims.

**Next dependency:** [Capstone](capstone.md) combines the ledger, exact reconstruction, retained residuals, and map tests.
