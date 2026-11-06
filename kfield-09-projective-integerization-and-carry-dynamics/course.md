# Projective Integerization and Carry Dynamics

Student course for high-school seniors. See course-map.md for pacing, terminology.md for notation, capstone.md for the synthesis assessment, and sources.md for provenance.

<!-- BEGIN: lesson-01 -->
# Lesson 01 — Nearest-integer maps need a tie rule

Essential question: How can two people turn the same number into the same nearest integer, even halfway between integers?

Goals: compute ceiling and floor for signed numbers; apply a deterministic half-tie rule; retain the signed rounding coordinate; distinguish rounding from cell ownership.

Bridge and readiness: From signed arithmetic and course 08, locate 0.5 and −0.5 on a number line. Each lies halfway between two integers. If you cannot name both neighbors, draw the interval and do that before rounding. No geometry from course 08 is needed beyond reading an ordered list of coordinates.

## C09.01-E1 — Defining the operation

An integer is a whole number, including zero and negative whole numbers. The ceiling of t, written ceil(t), is the least integer greater than or equal to t. Thus ceil(2.1)=3, ceil(−2.1)=−2, and ceil(−2)=−2. The floor floor(t) is the greatest integer less than or equal to t; floor(−2.1)=−3. Ceiling does not mean “move away from zero.”

Usually there is one nearest integer. At a half-tie there are two. Throughout this course define

**nint(t)=ceil(t−1/2): choose the lower integer at every exact half-tie.**

Subtract a half first, then take the ceiling. For t=2.4 this gives ceil(1.9)=2; for t=2.6 it gives ceil(2.1)=3. The rule is a function: each input has exactly one output. Define Q=nint(t) and the retained rounding coordinate epsilon=Q−t. This sign matters: a negative epsilon means the integer lies below the input. The original input is t=Q−epsilon.

Why is −1/2 ≤ epsilon < 1/2? If Q=ceil(t−1/2), then Q−1<t−1/2≤Q. Rearranging the right inequality gives Q−t≥−1/2; rearranging the left gives Q−t<1/2. The notation [−1/2,1/2) includes the left endpoint and excludes the right. The residual is an exact coordinate, not something to discard.

## C09.01-W1 — Worked signed ties

For t=1/2, subtracting 1/2 gives 0, so Q=0 and epsilon=0−1/2=−1/2. For t=−1/2, the ceiling input is −1, so Q=−1 and epsilon=−1−(−1/2)=−1/2. Likewise nint(3/2)=1 and nint(−3/2)=−2. These four cases all choose the lower integer. They do not alternate between lower and upper integers.

## C09.01-P1 — Guided practice and answers

Compute Q and epsilon for 49/100 and 51/100. Then add 3 to each input and repeat before reading the answers. After reading E2 below, return here and independently compute Q, epsilon, and the cell owner at both +1/2 and −1/2.

Answers: ceil(−1/100)=0, so the first pair is (0,−49/100). The second gives ceil(1/100)=1, so its pair is (1,49/100). After adding 3 the outputs are 3 and 4, while the residuals stay −49/100 and 49/100. In general, for any integer m, ceil(u+m)=ceil(u)+m because shifting every integer neighbor by m preserves their order. Therefore **nint(t+m)=nint(t)+m**. This translation rule will justify carry calculations in lesson 04, including at ties.

Signed-tie practice answers (use after E2): +1/2 gives Q=0, epsilon=−1/2, owner=1; −1/2 gives Q=−1, epsilon=−1/2, owner=0. In each case Q is the lower neighbor; the owner is the upper neighbor. Record both operations by name.

## C09.01-E2 — A different operation: cell ownership

A cell centered at integer n owns coordinates q with −1/2≤q−n<1/2. The owner is floor(q+1/2). At q=1/2 the owner is 1, with centered coordinate −1/2. The integerizer instead returns 0, with epsilon=0−1/2=−1/2. Both intervals look the same, but their subtractions run in opposite directions: q−owner versus Q−q. Never substitute one operation for the other.

> Scope: S02 M06 supplies the integerization framework, but its half-tie behavior is ambiguous. S03 finding AUD-013 identifies that ambiguity. This explicit lower-tie convention implements course amendment SA-09; it is not attributed to the original archive. All numbers in this lesson are teaching examples, not measurements.

## Diagnostic checks

1. **C09.01-D1:** At q=−1/2 compute the cell owner and integerizer. Explain their difference.
2. **C09.01-D2:** Compute ceil(−7/4), then nint(−7/4).
3. **C09.01-D3:** A program returns 1 at t=1/2. Is it implementing our contract? State the resulting epsilon.
4. **C09.01-D4:** Verify the translation rule at t=−1/2 with m=3. Recover the original t from its pair.

Worked answers: (1) owner=floor(0)=0; nint=ceil(−1)=−1. The owner centers q−owner, while integerization retains Q−q. (2) ceil(−1.75)=−1; nint=ceil(−2.25)=−2. (3) No: epsilon=+1/2 violates the excluded upper endpoint. (4) nint(2.5)=2=−1+3. Original t=−1−(−1/2)=−1/2.

Next: [lesson 02](lesson-02.md) applies this rule separately to three scaled coordinates.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 02 — Projective rays at successive scales

Essential question: How does a fixed ratio become a sequence of integer triples?

Goals: normalize a positive ordered triple to a ray representative; compute three successive scales; round each coordinate using lesson 01; separate synthetic inputs from stored source inputs.

Bridge: Compute nint(13.5) before beginning. The answer is 13. If you obtained 14, revisit the signed half-tie examples. We now apply the same scalar operation three times, without changing it.

## C09.02-E1 — Ratios, representatives, and generations

The positive triples (6,4,3) and (12,8,6) have the same ratios. Calling them representatives of one projective ray means we identify triples related by a positive common multiplier. Divide by the first coordinate to choose a representative whose first coordinate is 1. Both examples become r=(1,2/3,1/2). Here r is an ordered triple of dimensionless ratios. Normalizing removes the common magnitude: if the original magnitude is needed, retain the first coordinate separately. Our decoder recovers r, not an unrecorded magnitude.

Call the three coordinate positions a,b,c. These are ordered slots, not three interchangeable values. A generation g is a nonnegative integer: 0,1,2,… . S02 M06 defines the scale K_g=27^g. A power means repeated multiplication; 27^0=1, 27^1=27, 27^2=27×27=729. Each next scale is 27 times the previous one. This is integerization depth, not a dyadic or ternary address depth from another course.

Multiply every coordinate of r by K_g, then apply nint to each result:

**Q_g=nint(K_g r), component by component.**

Q_g is an integer triple in count coordinates, not a metric, an energy, or the detail operator called Q in another context. The approximation to the normalized ray is Q_g/K_g; dividing every coordinate by K_g returns to ratio coordinates. The scaled input and the integer record must remain separate columns.

## C09.02-W1 — Worked synthetic ray

Use r=(1,2/3,1/2), deliberately chosen for hand calculation.

| g | K_g | Exact K_g r | Q_g |
|---|---:|---|---|
| 0 | 1 | (1,2/3,1/2) | (1,1,0) |
| 1 | 27 | (27,18,27/2) | (27,18,13) |
| 2 | 729 | (729,486,729/2) | (729,486,364) |

For the middle coordinate at g=2, 729×2/3=486 exactly. For the third, 729/2=364.5 and the lower tie gives 364. Q_2/729 is therefore (1,2/3,364/729). This last value differs from 1/2; lesson 03 will retain precisely that difference.

## C09.02-P1 — Guided practice and answers

Build the same table for a second synthetic ray r=(1,1/3,1/4). Do not round the input fractions first.

Answers: the scaled triples are (1,1/3,1/4), (27,9,27/4), (729,243,729/4). Since 27/4=6.75 and 729/4=182.25, the integer triples are (1,0,0), (27,9,7), (729,243,182). The third coordinate rounds up at g=1 and down at g=2. A scale change does not preserve the direction of rounding.

## C09.02-E2 — Source-reading card

S02#/backbone_sequence/5/active_ray stores (1.0,0.7297352564331424,0.5446170214888189). Treat these finite decimal tokens as the exact inputs for a stored-input replay, not as an assertion about an infinite-precision physical ratio. Its reported first three Q triples are (1,1,1), (27,20,15), (729,532,397). For example, the middle scaled value at g=1 is 19.7028519236948448, which rounds to 20. The verification file independently replays these tokens. Do not replace either synthetic ray with these numbers mid-table.

> Scope: The generation rule and source card are source-grounded. The simple fractional rays are synthetic analogues. We are deriving integer records, not establishing a physical mechanism. No Cell3 basis, dimensional length, or mass is inferred from this table.

## Diagnostic checks

1. **C09.02-D1:** Why would using 3^g change the exercise? Identify which source-card Q triple belongs to g=1.
2. **C09.02-D2:** Normalize (8,4,2). What extra coordinate must be saved to reconstruct that original triple?
3. **C09.02-D3:** Compute the third Q coordinate for r=(1,2/3,1/2) at g=2, showing the tie step.
4. **C09.02-D4:** For the practice ray, calculate Q_1/K_1. Is the third coordinate exactly 1/4?

Worked answers: (1) At g=1 the scale would be 3 instead of 27, producing different scaled inputs. Source g=1 is (27,20,15). (2) r=(1,1/2,1/4); retain the first-coordinate scale 8 to multiply back. (3) ceil(729/2−1/2)=ceil(364)=364. (4) (1,1/3,7/27); 7/27−1/4=(28−27)/108=1/108, so it is not exact.

Next: [lesson 03](lesson-03.md) turns that difference into a decoding coordinate.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
# Lesson 03 — The retained rounding coordinate

Essential question: How can an integer approximation participate in exact recovery?

Goals: compute signed residual triples; distinguish count residuals from ratio-coordinate differences; derive and apply an exact decoder.

Bridge: Lesson 01 used epsilon=Q−t; lesson 02 supplies t=K_g r. Check that 7−27/4=1/4 before continuing. If fraction subtraction is difficult, rewrite 7 as 28/4.

## C09.03-E1 — Solving for the ray

At each generation define **epsilon_g=Q_g−K_g r**. Every coordinate lies in [−1/2,1/2). Epsilon is measured in the same integer-count coordinate units as Q: both describe the scaled dimensionless ray. It is not a length or physical measurement uncertainty. Since K_g is positive, rearranging gives K_g r=Q_g−epsilon_g and then

**r=(Q_g−epsilon_g)/K_g.**

This is an exact algebraic identity. In contrast, Q_g/K_g alone is an approximation. Subtract r from that approximation to obtain **Q_g/K_g−r=epsilon_g/K_g**. The residual divided by scale is the signed ratio-coordinate error under this declared sign convention. Increasing K reduces the maximum magnitude of that coordinate error to at most 1/(2K); it does not make the finite residual disappear.

An integer record alone cannot identify the original input. For example, 0.1 and 0.2 both round to 0, but their residuals are −0.1 and −0.2. The pair distinguishes them. Keeping only the absolute residual would also lose information: inputs 0.1 and −0.1 have the same rounded integer and residual magnitude but different signs.

## C09.03-W1 — Worked exact recovery

For the synthetic r=(1,2/3,1/2), subtract lesson 02's scaled inputs from its integer triples:

| g | Q_g | epsilon_g |
|---|---|---|
| 0 | (1,1,0) | (0,1/3,−1/2) |
| 1 | (27,18,13) | (0,0,−1/2) |
| 2 | (729,486,364) | (0,0,−1/2) |

At g=1, the third coordinate is recovered as (13−(−1/2))/27=(27/2)/27=1/2. The first coordinate is (27−0)/27=1, and the second is (18−0)/27=2/3. At g=0 the middle coordinate is 1−1/3=2/3; even the coarsest level retains the exact ray when its residual is present.

## C09.03-P1 — Guided practice and answers

Complete the residual column and recover every coordinate for the practice ray (1,1/3,1/4) using its three lesson 02 rows.

Answers: epsilon_0=(0,−1/3,−1/4), epsilon_1=(0,0,1/4), epsilon_2=(0,0,−1/4). At g=0 subtraction gives (1,1/3,1/4). At g=1 the third decoder is (7−1/4)/27=(27/4)/27=1/4. At g=2 it is (182+1/4)/729=(729/4)/729=1/4. The first and middle decoders are respectively K/K=1 and (K/3)/K=1/3 for g=1,2. The changing sign is essential information.

> Scope: These are exact identities on deliberately synthetic rational inputs. The retained residual does not by itself name a physical cause. For a stored decimal source input, the same identity recovers that stored input; it does not restore digits that were never supplied.

## Diagnostic checks

1. **C09.03-D1:** Someone uses (Q+epsilon)/K for the worked example's third coordinate at g=1. Calculate their result and explain the correction.
2. **C09.03-D2:** For the practice ray at g=1, state the third residual and the third ratio-coordinate error, with their different coordinate units.
3. **C09.03-D3:** Can Q=0 and |epsilon|=1/10 identify an input uniquely? Give the possible inputs.
4. **C09.03-D4:** Which metadata are needed to decode a triple reliably?

Worked answers: (1) The wrong numerator is 13−1/2=12.5, so the result is 25/54 rather than 1/2. Subtract epsilon because epsilon=Q−Kr. (2) The count residual is 1/4; the ratio-coordinate error is (1/4)/27=1/108. (3) No: epsilon=−1/10 yields input +1/10; epsilon=+1/10 yields −1/10. (4) Keep all signed coordinates, their order, ray/branch identity, generation, scale rule, tie rule, and residual sign definition. Never pair Q from one branch with epsilon from another.

Next: [lesson 04](lesson-04.md) relates the complete pairs at consecutive generations.
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
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
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Lesson 05 — Small differences at deeper levels

Essential question: When can two different rays have identical integer records, and where is their difference stored?

Goals: compare two exact inputs over stated generations; identify the first integer difference within that range; preserve earlier residual differences; interpret a historical replay without merging source branches.

Bridge: An integer and residual recover the ray together. Before proceeding, explain how inputs 0.1 and 0.2 can have the same integer 0 but different residuals. A generation table now lets us follow this distinction across scales.

## C09.05-E1 — Scaling a difference

Let two inputs in the same coordinate differ by delta, a signed amount. Their scaled difference at generation g is K_g delta. This does not tell us the rounded difference alone: the positions relative to half-integers also matter. Compare every earlier generation before declaring the first differing generation. “First” always refers to the specified starting level, inputs, and tie rule.

If Q'_g=Q_g but r'=r+delta, then epsilon'_g=Q_g−K_g(r+delta)=epsilon_g−K_g delta. Thus **epsilon'_g−epsilon_g=−K_g delta** while the integer records agree. There is no loss of the distinction in the complete pair. Once the integers differ, the general relation is epsilon'_g−epsilon_g=(Q'_g−Q_g)−K_g delta.

For two distinct exact scalar inputs, a sufficiently large scale will separate the integers: inputs that round to one integer lie in an interval of width 1, so a scaled separation greater than 1 cannot fit there. Since repeated multiplication by 27 can exceed any fixed positive bound, nonzero differences eventually separate. This gives a sufficient bound, not a universal predetermined first generation. Our assessments use explicit finite tables.

## C09.05-W1 — Worked synthetic comparison

Compare R=(1,2/3,1/2) with R'=(1,2/3+1/1000,1/2). Only b changes; keep a and c exactly as in lesson 03.

| g | Scaled b of R' | Q_b of R / R' | epsilon_b of R / R' |
|---|---|---|---|
| 0 | 2003/3000 | 1 / 1 | 1/3 / 997/3000 |
| 1 | 18027/1000 | 18 / 18 | 0 / −27/1000 |
| 2 | 486729/1000 | 486 / 487 | 0 / 271/1000 |

At g=2 the changed input is 486.729, which rounds to 487. Its residual is 487−486.729=0.271. The first integer difference is g=2; already at g=0 the residual difference is −1/1000. For both rays the other signed residuals at g=0,1,2 are epsilon_a=0 and epsilon_c=−1/2. These statements specify all three residual coordinates, not just the differing coordinate.

## C09.05-P1 — Guided comparison and answers

Compare T=(1,1/3,1/4) with T'=(1,1/3+1/10000,1/4) through g=3. Find every b integer and signed residual. Retain the common a,c residuals too.

Answers:

| g | K_g | Q_b of T / T' | epsilon_b of T / T' | common (epsilon_a,epsilon_c) |
|---|---:|---|---|---|
| 0 | 1 | 0 / 0 | −1/3 / −10003/30000 | (0,−1/4) |
| 1 | 27 | 9 / 9 | 0 / −27/10000 | (0,1/4) |
| 2 | 729 | 243 / 243 | 0 / −729/10000 | (0,−1/4) |
| 3 | 19683 | 6561 / 6563 | 0 / 317/10000 | (0,1/4) |

At g=3 the perturbed scaled b is 6561+19683/10000=6562.9683. Round to 6563 and subtract to obtain 0.0317. The a coordinates of Q are K_g; the c coordinates are 0,7,182,4921 for both rays. Integers first differ at g=3; residuals differ from g=0. Subtracting signed residuals verifies −K_g/10000 before the split and 2−19683/10000 afterward.

## C09.05-E2 — Historical source-reading card

S01#/backbone_sequence/4/projective_rays preserves two different decimal-string rays, named master_geometry and locked_mass_bridge. S01 M06 reports agreement through g=7 and master-minus-locked=(0,8,7) at g=8. A fresh exact rational replay of those stored strings gives the same result; the complete compact replay and signed residual differences are in worked-example-verification.json. At g=8 the locked Q is (282429536481,206098790228,153815932939); the master Q is (282429536481,206098790236,153815932946). Subtract the triples to check the reported difference yourself.

> Scope: This card is a historical finite-input replay, not a replacement for S02's active ray. The fresh check concerns supplied decimal strings, not unreported infinite digits. It neither promotes the source's broader proof status nor identifies a physical mechanism. Source branches remain separate even where their integers agree.

## Diagnostic checks

1. **C09.05-D1:** From the historical card, compute the g=8 difference. Does agreement through g=7 make the source rays identical?
2. **C09.05-D2:** In W1, calculate epsilon'_b−epsilon_b at g=1 and g=2 using the general relation.
3. **C09.05-D3:** Does every distinct pair first differ at g=2? Use the two synthetic comparisons.
4. **C09.05-D4:** Why must a table keep exact input identity and the residual even before its integer split?

Worked answers: (1) Difference=(0,8,7). No; distinct residuals preserve the differences before integer separation. (2) At g=1 it is 0−27/1000=−27/1000; at g=2 it is 1−729/1000=271/1000. (3) No: W1 splits at 2; P1 splits at 3. (4) Shared integers do not identify a ray; the branch and signed residual identify which input can be recovered.

Next: [lesson 06](lesson-06.md) packages the finite history into a reversible ledger.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
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
<!-- END: lesson-06 -->
