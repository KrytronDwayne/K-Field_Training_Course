# Lesson 3 — Charge as an additive rule

Essential question: How can five basis weights determine every charge in a sixteen-state census?

Goals: compute q and Y from a bidegree; distinguish individual charge from weighted contribution; evaluate the supplied descent remainder test.

Prerequisite bridge: Lesson 2 supplies six bidegrees and their multiplicities. Signed multiplication and fractions now attach numbers to those states.

Pacing: two 55-minute periods, each 5 retrieval + 20 teaching/example + 15 practice + 15 checks/repair. Period 1 assigns charges; period 2 teaches remainders and descent.

## C15.03-E1 — Add labels' weights

Assign the same weight a to each color label and b to each weak label. A central phase is a common rotation applied to all labels of a block. We need only its exponent rule: multiplying two phase factors adds their exponents. Consequently a wedge with r colors and s weak labels has total weight q=ar+bs. The empty product has q=0. These weights and all charges here are dimensionless; they are not measured electric charges in coulombs.

For the source's primitive convention set a=−2 and b=3. Lesson 5 will derive the allowed ratio and explain “primitive.” Define hypercharge Y=q/6. Y is the source hypercharge label, not electric charge. Each basis state in one bidegree has the same q, but a row with multiplicity m contains m distinct components. Its linear contribution is mq; its cubic contribution is m(q³). Cube each component's charge before adding. Cubing mq would introduce terms between components and answer another question.

The source also supplies a descent test: q+2t+3p must leave remainder zero on division by 6. Here triality t is the remainder of r upon division by 3 (0,1,2); weak parity p is the remainder of s upon division by 2 (0,1). “x=0 mod 6” means x is an integer multiple of 6, including zero and negative multiples. Descent means the representation can respect the source's stated identification of symmetry transformations. Evaluating this finite test does not require deriving that global symmetry construction.

## C15.03-W1 — Worked examples

Q has (r,s)=(1,1), so q=−2+3=1, Y=1/6, and m=3×2=6. With t=1,p=1, its descent integer is 1+2+3=6, remainder 0. The u^c row has (2,0), q=−4, Y=−4/6=−2/3,m=3. Its t=2,p=0 give −4+4=0. Its linear contribution is 3(−4)=−12; its cubic contribution is 3(−4)³=3(−64)=−192, not (−12)³.

## C15.03-P1 — Complete the other rows

Calculate m,q,Y,t,p and the descent integer for nu^c,e^c,d^c,L. Then use Lesson 2's explicit basis lists to assign those values to every component, keeping the row multiplicities visible.

|Sector|(r,s)|m|q|Y|t|p|q+2t+3p|remainder mod 6|
|---|---|---:|---:|---|---:|---:|---:|---:|
|nu^c|(0,0)|1|0|0|0|0|0|0|
|e^c|(0,2)|1|6|1|0|0|6|0|
|Q|(1,1)|6|1|1/6|1|1|6|0|
|u^c|(2,0)|3|−4|−2/3|2|0|0|0|
|d^c|(2,2)|3|2|1/3|2|0|6|0|
|L|(3,1)|2|−3|−1/2|0|1|0|0|

Worked route: d^c uses q=−2(2)+3(2)=2 and m=3×1=3; L uses q=−2(3)+3(1)=−3 and m=1×2=2. For e^c, s=2 has remainder zero, not two. For L, r=3 has triality zero. All three d^c components have q=2 individually; both L components have q=−3 individually.

## Diagnostic checks

1. **C15.03-D1:** For m=3,q=−4, give linear and cubic contributions and explain the order of operations.
2. For (3,1), why is t=0 rather than 3?
3. Change the synthetic weights to (a,b)=(1,0). What is Q's q and what is d^c's q?
4. Does reversing the coefficient sign of a wedge reverse its charge?

Worked answers: (1) −12 and −192; compute each component's power first, then multiply by m. (2) Dividing 3 by 3 leaves zero. (3) q=r, giving 1 and 2. (4) No. A coefficient sign changes the state expression's coefficient, not which basis labels determine the charge. Reversing all basis weights would reverse charges.

> Claim scope: The additive rule, primitive convention and congruence are source inputs replayed as arithmetic. Sources: S02 /backbone_sequence/10, KFM-F033 /proof_nodes/74/formula and KFM-X026 /proof_nodes/75/formula. Nonzero remainders in alternative trials must be retained, not silently repaired.

Next dependency: [Lesson 4](lesson-04.md) adds the components with several distinct test weights.
