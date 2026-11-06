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
