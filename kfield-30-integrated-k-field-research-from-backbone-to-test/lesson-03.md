# Lesson 3 — Interferometers and identifiable coupling

Essential question: Which hidden quantities can a measured response recover?

Goals: Multiply a small measurement table by a parameter pair; exhibit an invisible change; recover parameters from sum and difference; explain why a physical transfer calibration is necessary.

Prerequisite bridge: You can solve two linear equations and reconstruct a mean/detail pair. An **inverse problem** starts from outputs and asks which inputs produced them. **Identifiable** means unique within the declared candidate domain and measurement model. We first use dimensionless synthetic channels so that instrument units cannot be hidden inside convenient arithmetic.

## C30.03-E1 — Reading a matrix as instructions

Write theta=(theta1,theta2) for two unknown response contributions. A matrix is a rectangular table. In y=H theta, each row of H gives multipliers: multiply each row entry by the corresponding theta entry, then add. For H=[[1,1],[2,2]], the outputs are y1=theta1+theta2 and y2=2theta1+2theta2. The second channel is twice the first, so it provides a repeat of the same combination rather than a new equation.

**Rank** counts independent combinations measured. Here rank is 1 because the second row is a multiple of the first. A **null direction** is a parameter change giving zero output change. Adding t to theta1 and subtracting t from theta2 changes neither sum. The direction (1,−1) is invisible for every real t. A set of inputs sharing one output is an equal-output family. Recognizing such a family tells you which measurement to add.

An interferometer compares wave paths through their relative phase. Phase labels position within a repeating cycle; a detector converts the comparison into recorded values through a transfer relation. A beat frequency describes cycles per second, not joules per second. This course uses a linear sum/difference response as a proposed local instrument model, not as a universal law for every interferometer. Before applying it to real channels, the apparatus must demonstrably implement the row coefficients, signs, units and operating range.

## C30.03-W1 — Same outputs, different states

For thetaA=(2,1), H thetaA=(2+1,4+2)=(3,6). For thetaB=(1,2), H thetaB=(1+2,2+4)=(3,6). Their difference is (1,−1), the invisible direction. One cannot choose between them from these two channels.

Add a third row (1,−1). It predicts +1 for A and −1 for B. Let s=theta1+theta2 and d=theta1−theta2. Adding the equations gives s+d=2theta1; subtracting gives s−d=2theta2. Therefore theta=((s+d)/2,(s−d)/2). The two rows (1,1) and (1,−1) are independent: no single multiplier turns the first into the second. Their rank is 2.

The physical-closure source T50 describes a related transfer obstruction: a scalar response can retain distinct gain/responsivity factorizations. In a dimensionless toy transfer with product gR=6, (g,R)=(2,3) and (1,6) give the same product. Exact wavelength geometry does not by itself choose either factor. A known reference that measures g separately can resolve this ambiguity within that product model.

## C30.03-P1 — Practice, then substitution

Recover theta for s=5,d=−1. Check all three original/added row outputs. Then describe what is missing when only gR=6 is recorded.

Answer: theta1=(5−1)/2=2 and theta2=(5+1)/2=3. The original channels are 5 and 10, and the new difference is −1. Product 6 alone cannot select a factorization; obtain a separate calibrated reference or retain the entire equal-product family. Do not discard the doubled channel: its disagreement with twice the first may reveal an unmodeled response.

> Claim scope: All numbers in the inverse examples are synthetic. T30 says detection needs a real blinded registered endpoint; extraction needs net-power accounting for a defined control volume; induction needs controlled reversing force/impulse evidence. Here an endpoint is a predeclared reported response, and a control volume is the bounded region whose energy flows are accounted for. Our rank calculation establishes none of those empirical outcomes.

## C30.03-D1 — Diagnostics and worked answers

1. Find another state giving (3,6). **Answer:** (0,3), because its sum is 3; there are infinitely many real examples.
2. Would row (3,3) resolve the ambiguity? **Answer:** No; it is three times (1,1), still blind to (1,−1).
3. For s=4,d=2, recover and check theta. **Answer:** (3,1), whose sum is 4 and difference is 2.
4. Why is adding row (1,−1) on paper insufficient for a detector claim? **Answer:** The apparatus must measure that combination with known transfer, orientation and calibration; an algebraic row does not construct an instrument.

Next dependency: [Lesson 4](lesson-04.md) chooses new measurements by their distinct predicted outputs.
