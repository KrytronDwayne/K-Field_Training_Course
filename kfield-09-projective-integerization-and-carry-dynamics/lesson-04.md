# Lesson 04 — Carry between generations

Essential question: What information must be added when one integer record is enlarged to the next scale?

Goals: derive the two carry recurrences; compute a carry by two independent routes; encode and decode the two side carries; test the integer parity condition.

Bridge: Lesson 03 gives Q_g=K_g r+epsilon_g, and lesson 02 gives K_g=27K_(g−1). Check that multiplying an entire triple by 27 multiplies each coordinate. This lesson takes two periods: carry derivation first, reversible side coordinates second.

## C09.04-E1 — Subtracting two descriptions

Suppose we already have Q_(g−1). Multiplying it by 27 produces an integer triple at the new scale, but its rounding history may differ from rounding the new input directly. Define the correction, or carry, by **C_g=Q_g−27Q_(g−1)** for g≥1. There is no C_0 in this ledger.

Write both descriptions at the same scale:

Q_g=K_g r+epsilon_g,

27Q_(g−1)=K_g r+27epsilon_(g−1).

Subtract the second equation from the first. The identical K_g r terms cancel, giving **C_g=epsilon_g−27epsilon_(g−1)**. Rearranging produces two update rules:

**Q_g=27Q_(g−1)+C_g** and **epsilon_g=27epsilon_(g−1)+C_g**.

The same carry updates both coordinates of the encoding. Why can it be computed from the earlier residual alone? The scaled input is K_g r=27Q_(g−1)−27epsilon_(g−1). The first term is an integer triple. Lesson 01's integer-translation rule allows it to pass through nint, so Q_g=27Q_(g−1)+nint(−27epsilon_(g−1)). Thus **C_g=nint(−27epsilon_(g−1))**. This derivation depends on the declared tie rule, not an unstated library rounding function.

## C09.04-W1 — Worked carry and reverse check

For r=(1,2/3,1/2), Q_0=(1,1,0), Q_1=(27,18,13), Q_2=(729,486,364). Integer subtraction gives C_1=(0,18−27,13−0)=(0,−9,13) and C_2=(0,486−486,364−351)=(0,0,13).

Independently, epsilon_0=(0,1/3,−1/2). Multiply by −27 to get (0,−9,13.5); rounding gives (0,−9,13), agreeing with C_1. Updating epsilon produces (0,9,−13.5)+(0,−9,13)=(0,0,−1/2). Repeat from this epsilon_1: nint(0,0,13.5)=(0,0,13)=C_2. Every residual remains in the declared interval.

## C09.04-E2 — Side sums, differences, and parity

The b and c entries are called side carries. Introduce two new coordinates **S=C_b+C_c** and **A=C_b−C_c**. S records their sum and A their signed difference. Adding these equations gives S+A=2C_b; subtracting gives S−A=2C_c. Therefore **C_b=(S+A)/2** and **C_c=(S−A)/2**. Keep C_a separately.

Integers are even if divisible by 2, odd otherwise. Both S+A and S−A must be even for integer inverse halves. This happens exactly when S and A are both even or both odd, called the same parity. The notation S congruent A modulo 2 says they have the same remainder after division by 2. The allowed integer pairs form the set sometimes called the side-mode lattice; no lattice theory is needed to test membership.

For worked C_1, S=−9+13=4 and A=−9−13=−22. Inverse halves give (4−22)/2=−9 and (4+22)/2=13. Both modes are even. Parity here is an arithmetic condition, distinct from detector polarity, projective sign, chirality, or a family label.

## C09.04-P1 — Guided practice and answers

For r=(1,1/3,1/4), compute C_1,C_2 by integer subtraction and residual rounding. Then compute and invert S,A for both generations.

Answers: Q rows from lesson 02 give C_1=(0,9,7), C_2=(0,0,−7). Residual route: −27epsilon_0=(0,9,27/4), which rounds to (0,9,7); −27epsilon_1=(0,0,−27/4), which rounds to (0,0,−7). Modes are (S_1,A_1)=(16,2) and (S_2,A_2)=(−7,7). The inverse halves are (18/2,14/2)=(9,7), then (0/2,−14/2)=(0,−7). Updating epsilon_1 yields (0,0,27/4−7)=(0,0,−1/4)=epsilon_2.

> Scope: S02 M06 provides the recurrence and side-mode definitions. The finite derivation here verifies those operations under SA-09's explicit rule. Its reported g=3 witness C=(0,−1,1) has S=0,A=−2; interpreting that pair requires only this arithmetic, not a physical identification.

## Diagnostic checks

1. **C09.04-D1:** Can S=1,A=0 represent integer side carries? Decode the source witness S=0,A=−2.
2. **C09.04-D2:** At epsilon_(g−1)=−1/2 for one coordinate, compute C_g and epsilon_g.
3. **C09.04-D3:** Prove in words why equal parity is sufficient for integer inverse halves, and why it is necessary.
4. **C09.04-D4:** In the practice example, a learner writes C_2=(0,0,+7). Which integer update exposes the error?

Worked answers: (1) No: the halves are 1/2 and 1/2. The source pair decodes to −1 and +1. (2) C=nint(13.5)=13; epsilon=−13.5+13=−1/2. (3) Even±even and odd±odd are even, so the halves are integers. Conversely S+A=2C_b and S−A=2C_c are even for integer carries, which rules out opposite parity. (4) The third Q_2 would be 27×7+7=196; direct rounding gives 182. The correct carry is −7.

Next: [lesson 05](lesson-05.md) compares when two ray records first differ.
