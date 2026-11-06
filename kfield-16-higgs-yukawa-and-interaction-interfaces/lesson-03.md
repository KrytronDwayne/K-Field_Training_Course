# Lesson 3 — The Higgs doublet interface

Essential question: Which component of the supplied doublet can carry a vacuum without changing electric charge?

Goals: calculate the two component charges; apply a diagonal operator to a vector; test a proposed vacuum and calculate its squared length.

Bridge: H in lessons 1–2 had two available weak basis directions, w1 and w2, and degree (0,1). We now attach coefficients to those directions. One 55-minute period: 5 retrieval, 20 teaching/example, 15 practice, 15 diagnostics/repair.

## C16.03-E1 — A doublet has two components

A doublet is an ordered pair of components. Write H=(H_plus,H_zero) in the basis (w1,w2). The subscripts anticipate the charges we will calculate, not assumed measurements. A diagonal operator diag(a,b) multiplies the first component by a and the second by b: diag(a,b)(x,y)=(ax,by). The identity I=diag(1,1) leaves the pair unchanged. Adding two diagonal operators adds their corresponding entries.

For this supplied Higgs carrier, define T3=diag(1/2,−1/2), and Y_h=I/2=diag(1/2,1/2). The electric-charge operator is Q_electric=T3+Y_h=diag(1,0). Thus the upper component has electric charge +1 and the lower component charge 0. Both have the same hypercharge +1/2. T3 distinguishes the two weak positions; hypercharge alone does not.

The source vacuum is H_vac=(0,v/√2), with v a supplied nonnegative magnitude. √2 is the positive number whose square is 2; v/√2=v√2/2. In the compiler mass convention used here, v and H_vac carry a mass unit μ. μ denotes an arbitrary teaching unit, not a measured energy scale. The squared length of a real pair is x²+y², with unit μ² if x,y have unit μ. Our real vacuum examples need no complex-length formula.

An unbroken charge generator annihilates the vacuum: Q_electric H_vac=(0,0). “Annihilates” means returns the zero vector, not that the vacuum itself vanishes. The lower component has multiplier zero, so every value of v in this supplied direction meets this test. At a nonzero upper component, the multiplier is 1 and the test fails. The source's continuous symmetry statement uses this generator test; we do not need calculus to evaluate it. This checks the displayed electric generator, not a count of every symmetry at v=0.

## C16.03-W1 — Evaluate a neutral direction

Take synthetic v=2 μ. Then v/√2=√2 μ, so H_vac=(0,√2) μ. Its squared length is 0²+(√2)²=2 μ². Applying Q_electric gives (1×0,0×√2) μ=(0,0). Notice the vacuum is nonzero while the operator output is zero. The charge test selects a direction, but it has not selected the magnitude 2.

## C16.03-P1 — Practice

For synthetic v=4 μ, find the vacuum, its squared length, and its Q_electric output. Compare the test vector (1,0) μ.

Worked answer: 4/√2=2√2, so H_vac=(0,2√2) μ. Squaring gives 4×2=8 μ². The charge output is (0,0). For (1,0) μ the output is (1,0) μ, nonzero, so a vacuum placed solely there with nonzero magnitude would not preserve this generator.

> Claim scope: S02 /backbone_sequence/11 and /proof_nodes/80 supply the doublet, neutral direction, and parameter v. Numerical choices above are synthetic. The potential is a function used to specify which field configurations are energetically favored; its coefficients and vacuum stability are not determined by this charge test. No potential minimization is assessed.

## Diagnostics and worked answers

1. **C16.03-D1:** Does neutrality determine v, potential coefficients, stability, or rate? Answer: none of them; Q_electric(0,v/√2)=0 for every v, so the equation cannot choose a particular magnitude or evolution.
2. **C16.03-D2:** Why is the upper charge 1 rather than 1/2? Answer: add its T3 and Y_h contributions: 1/2+1/2=1.
3. **C16.03-D3:** At v=0, what is the tested vacuum? Answer: (0,0), squared length 0; Q_electric annihilates it too. This does not establish that only one generator is unbroken there.
4. **C16.03-D4:** What is the squared length for v=6 μ? Answer: v²/2=36/2=18 μ²; the general formula comes from squaring the lower component.

Next dependency: [Lesson 4](lesson-04.md) uses the same supplied v in mass formulas.
