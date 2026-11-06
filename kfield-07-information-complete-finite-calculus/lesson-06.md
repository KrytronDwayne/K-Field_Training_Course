# Lesson 06 — Singular equations and retained freedom

Essential question: What information must accompany an equation that has many solutions or no exact solution?

Goals: solve a two-equation system by substitution; retain its free coordinate; compute an output compatibility coordinate and declared residual view; distinguish singular and invertible maps.

Prerequisite bridge: You can solve u+v=6 for u=6−v. Lesson 05 retained components a model did not determine. Here missing information can occur on the input side as well as the output side. All quantities in this lesson are dimensionless synthetic numbers.

## C07.06-E1 — Read a matrix as two recipes

Write an input pair as psi=(u,v). The matrix K=[[1,1],[2,2]] is shorthand for the output rule K psi=(u+v,2u+2v). Each row tells you to multiply the input coordinates by its entries and add. To solve K psi=j for an output pair j=(j_1,j_2), ask for an input producing both output numbers.

The second output is always twice the first. Consequently j_2−2j_1=0 is necessary for an exact solution. It is sufficient too: if it holds, set v=t and u=j_1−t; then both equations hold for every real t. A real number here may be positive, negative, zero or fractional. The parameter t is free because the output does not determine it.

This map is singular: different inputs can produce the same output, and some requested outputs are unreachable. Its kernel is the collection of input changes producing zero output. Changing psi by s(−1,1) leaves the sum unchanged; K(−1,1)=(0,0). Every zero-output input has that form, since u+v=0 gives u=−v. Retaining the free coordinate t distinguishes members of a solution family.

On the output side, define the compatibility coordinate c=j_2−2j_1. This is a concrete coordinate for the cokernel information: it records the obstruction left after accounting for reachable outputs. No quotient-space calculation is required. For our chosen view j_fit=(j_1,2j_1), keep output residual rho=j−j_fit=(0,c). Then j=j_fit+rho. This convention matches the first equation exactly; it is not asserted to be uniquely best. The input parameter t and output obstruction c have different roles and both must survive when relevant.

## C07.06-W1 — Worked singular solution

For j=(6,12), the equations are u+v=6 and 2u+2v=12. Divide the second by 2 to see it repeats the first. Set v=t; then psi=(6−t,t). Its output is (6−t+t,12−2t+2t)=(6,12) for all real t. The kernel direction is (−1,1), and c=12−2·6=0. If the actual illustrative input is (2,4), retaining t=4 recovers it. Choosing t=0 would select (6,0), another solution, but would not recover that illustrative state.

Contrast L=[[1,0],[0,2]], whose rule is L(u,v)=(u,2v). It sends (3,4) to (3,8), and its decoder is (j_1,j_2/2) for every real output pair. This invertible map has exactly one input per output. An inverse formula for L cannot be transferred to singular K.

> Claim scope: S02#/backbone_sequence/3/source_relation keeps K psi=j primary on singular strata and restricts inverse formulas to their invertible domain. These small matrices are synthetic analogues. Kernel, cokernel and retained parameters are explicitly distinguished; no physical field equation is being solved.

## C07.06-P1 — Practice with an incompatible request

For j=(6,13), test compatibility. Declare the first-equation-matching view, retain its residual and write the complete fitted input family. Use t=4 to give one input and check its output plus residual.

Answer: c=13−12=1, so no exact input produces j. Keep j_fit=(6,12), rho=(0,1), and psi_fit=(6−t,t) with t retained. With t=4, psi_fit=(2,4); K psi_fit=(6,12), and (6,12)+(0,1)=(6,13). The residual has not made K psi_fit=j true; it makes K psi_fit+rho=j true.

## Diagnostics

1. **C07.06-D1:** Invert L on (3,8). For singular K and output (8,16), recover the input when t=3. What is lost if t is deleted?
2. **C07.06-D2:** For K and j=(8,17), find c, j_fit, rho and the fitted input with t=3. Is it an exact solution of K psi=j?
3. **C07.06-D3:** For K and j=(0,0), list two distinct inputs and describe all of them. Does zero output imply zero input?

Worked answers: D1: L inverse gives (3,8/2)=(3,4). K gives (8−3,3)=(5,3); without t, the whole family (8−t,t) remains and the actual input is undetermined. D2: c=1, j_fit=(8,16), rho=(0,1), psi_fit=(5,3). Its output is (8,16), so it is not an exact solution for (8,17); retain the nonzero residual. D3: (0,0) and (−1,1) both work; all inputs are (−t,t). Zero output alone does not force zero input.

Next dependency: [Lesson 07](lesson-07.md) records anchors, details, model layers, free coordinates and compatibility data in a complete transformation ledger.
