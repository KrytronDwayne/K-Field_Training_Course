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
