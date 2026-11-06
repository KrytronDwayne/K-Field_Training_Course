# Lesson 05 — Cylinder observations

Essential question: What can an observation see if it reads only a finite prefix?

Goals: Evaluate an observation through reduction; find the prefix depth it actually needs; preserve finer addresses sharing one value.

Bridge and pacing: Lesson 01 taught reduction and Lesson 04 separated histories from rendered values. One 55-minute period: retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15.

## C22.05-E1 — One observation, many histories

A function assigns an output to each allowed input. An observation f_d on depth-d residues uses just that finite address. To apply it at depth d+1, first reduce and then use f_d. The notation f_d∘π_d means exactly this two-step operation, called composition. It is also called a pullback of the observation to the finer level.

A cylinder is the collection of all complete histories sharing a chosen finite prefix. A cylinder observation is constant as you vary the unresolved tail inside that cylinder. No literal cylinder in physical space is required. If two finer inputs reduce to the same prefix, a function of that prefix must return the same output. The converse need not hold: an observation can also group several different prefixes into one output.

In three coordinates, declare whether the function reads the whole prefix triple or only one coordinate. Recording a scalar observation is not an instruction to erase the other coordinates. A useful table stores full address, prefix depth, observation rule and observation value together. This gives a reproducible coarse view while retaining fine distinctions.

## C22.05-W1 — A depth-one indicator

Define f₁(a)=1 if a mod3=1 and 0 otherwise. The outputs 0 and 1 are dimensionless labels. At depth 2, f₁(1)=f₁(4)=f₁(7)=1 because all three reduce to 1 modulo3. At depth 3 each depth-2 residue a has extensions a+9k for k=0,1,2. Since 9k is divisible by3, the output stays the same. For example the extensions of 4 are 4,13,22, all giving 1. The function reads the first prefix, even when evaluated on depth-3 inputs.

> Claim scope: S02 /backbone_sequence/17/proof/3 states finite-prefix observables and consistent pullback. The function here is an authored mathematical example, not a sensor measurement. Equal outputs identify an observation class, not an entire exact history.

## C22.05-P1 — Practice, then check

Let g₂(a)=a mod9. Evaluate it on depth-3 residues 7,16,25. Recover their balanced first three digits and identify what g₂ ignores. For triple inputs (a,b,c), keep b and c in the ledger even though g₂ reads only a.

Answer: each output is 7. The digit triples are (1,−1,1), (1,−1,−1), (1,−1,0): their signed sums are 7,−11,−2, respectively, and their mod27 residues are 7,16,25. All share their first two digits. The third digit and all later continuation are invisible to g₂. Store each separate input beside output 7; do not replace the three rows by a single unlabeled row.

## Diagnostics — C22.05-D1

1. Can an observation that reads the third balanced digit always be described as depth-one?
2. What is f₁(8) in the worked example?
3. Does equal g₂ force equal third digits?
4. Can the constant observation f(a)=0 use no digits at all?

Worked answers: (1) No: 7,16,25 have the same depth-one prefix but different third digits. A general third-digit reader needs depth 3. (2) 8 mod3=2, so f₁(8)=0. (3) No; the practice table is an explicit counterexample. (4) Yes, depth zero suffices because the output ignores every input. The input histories should still be retained if the record is to preserve them.

Next dependency: [Lesson 06](lesson-06.md) decomposes coarse and fine information into pieces that reconstruct the input exactly.
