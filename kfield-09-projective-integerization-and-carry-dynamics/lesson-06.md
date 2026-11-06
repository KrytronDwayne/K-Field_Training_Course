# Lesson 06 — A lossless recursive compiler

Essential question: What must a finite carry ledger retain to reconstruct its exact ray?

Goals: expand a two-generation recurrence; decode a finite ledger with its terminal residual; reverse side modes and carry updates; audit metadata and numerical consistency.

Bridge: From lesson 04, Q_1=27Q_0+C_1 and Q_2=27Q_1+C_2. From lesson 03, r=(Q_2−epsilon_2)/729. We will substitute the first identities into the last, using only multiplication, addition, and fractions.

## C09.06-E1 — Expanding without losing the endpoint

Replace Q_1 inside the equation for Q_2:

Q_2=27(27Q_0+C_1)+C_2=729Q_0+27C_1+C_2.

Subtract epsilon_2 and divide each term by 729 to obtain

**r=Q_0+C_1/27+C_2/729−epsilon_2/729.**

The last residual is called terminal because it belongs to the last included generation. It is still part of the exact decoder. A “compiler” here means a deterministic conversion into a structured ledger; no computer programming knowledge is required. The ledger is lossless for its exact supplied ray only if it retains that terminal residual and the decoding metadata.

For a finite terminal generation g, the same repeated substitution gives r=Q_0+sum_(j=1..g)(C_j/27^j)−epsilon_g/27^g. The sum notation says “add one term for each integer j from 1 through g.” At g=2 it is exactly the expanded formula above. The archive also writes an infinite carry series. Recognizing that notation is optional; proving a limit is outside this finite course.

## C09.06-W1 — Worked finite reconstruction

For synthetic r=(1,2/3,1/2), retain Q_0=(1,1,0), C_1=(0,−9,13), C_2=(0,0,13), epsilon_2=(0,0,−1/2).

The integer expansion gives Q_2=(729,729−243,351+13)=(729,486,364). Coordinatewise decoding gives a=1, b=1−9/27=2/3, and c=13/27+13/729+1/1458. To verify c, use denominator 1458: (702+26+1)/1458=729/1458=1/2. Omitting the terminal term would give 364/729, short by 1/1458.

To recover earlier residuals from the terminal record, reverse the update: **epsilon_(j−1)=(epsilon_j−C_j)/27**. First epsilon_1=((0,0,−1/2)−(0,0,13))/27=(0,0,−1/2). Then epsilon_0=((0,0,−1/2)−(0,−9,13))/27=(0,1/3,−1/2). This backward route recovers the same full signed residual history as direct subtraction from the input.

## C09.06-P1 — Guided audit and answers

For the synthetic practice ray, retain Q_0=(1,0,0), C_a=0 at both steps, side modes (S_1,A_1)=(16,2), (S_2,A_2)=(−7,7), and epsilon_2=(0,0,−1/4). Decode the carries, reconstruct every Q and epsilon, and recover r without first using its known value.

Answers: Inverse halves give C_1=(0,9,7), C_2=(0,0,−7). Forward Q updates give Q_1=(27,9,7), Q_2=(729,243,182). Backward residual updates give epsilon_1=(0,0,(−1/4+7)/27)=(0,0,1/4) and epsilon_0=(0,−1/3,(1/4−7)/27)=(0,−1/3,−1/4). All coordinates satisfy the interval. The decoder gives a=1, b=9/27=1/3, c=7/27−7/729+1/2916=(756−28+1)/2916=729/2916=1/4. Directly rebuilding from this recovered ray reproduces every row.

## C09.06-E2 — An audit procedure you can execute

First label the branch, input precision, coordinate order, rule, scale, and residual sign. Check each residual coordinate against [−1/2,1/2). Decode each side pair with inverse halves and confirm equal parity; preserve C_a. Rebuild Q forward and epsilon backward. Then decode r independently at every generation and require exact agreement. Finally round the recovered K_g r afresh and compare the results with Q_g. A table with internally consistent recurrence but a wrong rounding rule can fail this last test. Record a disagreement and its corrected version, rather than silently deleting it.

> Scope: These finite algebraic tests establish a reversible representation of the supplied ray. They do not recover an unrecorded normalization magnitude, source digits, or physical variables outside the encoding contract. Every removed component needed for the stated inverse is retained.

## Diagnostic checks

1. **C09.06-D1:** State the steps that reverse side modes and recover the full ray, including required metadata.
2. **C09.06-D2:** What exact correction is lost if epsilon_2 is omitted from P1?
3. **C09.06-D3:** A table updates Q correctly but has epsilon_1=(0,0,−1/4) in P1. Verify or refute that entry.
4. **C09.06-D4:** Is the finite identity an infinite-series proof? Can it recover the original (8,4,2) from its normalized ray without a stored magnitude?

Worked answers: (1) Keep branch, a/b/c order, K_g=27^g, lower-tie rule, epsilon=Q−Kr, generation, and coordinate units. Invert S,A, retain C_a, build Q forward and epsilon backward, and check r=(Q−epsilon)/K at every row. (2) The third correction +1/2916; other corrections are zero. (3) Direct subtraction is 7−27/4=+1/4, so the proposed negative sign is wrong. The backward terminal route also yields +1/4. (4) No to both. The finite terminal term is retained; normalized ratios do not contain the discarded magnitude 8.

Next: [capstone](capstone.md) asks you to create and audit the complete finite ledger.
