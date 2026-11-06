# Lesson 3 — Patterns and retained information

**Essential question:** How can a model simplify a record without losing it?

**Goals:** Calculate every signed residual; reconstruct original readings; preserve a second residual layer and replay metadata.

**Prerequisite bridge:** Lesson 2 showed why metadata and source status cannot substitute for raw readings. Here a fully specified synthetic record makes every arithmetic step checkable.

## Keep the model and remaining information

Let x mean a reading and M the model value at the same row. Define residual r = x − M. Rearranging gives x = M + r. This exact bookkeeping identity does not depend on the model being physically correct. The residual carries what the model does not encode. Its sign locates x above or below M. Its unit matches x and M because subtraction requires compatible units.

A summary cannot generally replace the sequence. Residual lists (1, −1) and (−1, 1) both sum to zero but encode different orderings. Reconstruction needs each signed value, index, channel, time, orientation when supplied, and the model rule. Disagreement identifies where to seek a missing coordinate or mechanism.

## Worked example: two retained layers

The whole table is invented. Let t be elapsed time in seconds. Channel A readings use display units, DU: a synthetic unit with no energy calibration. Set M0 = 10 DU + (2 DU/s)t. A rate times seconds gives DU, making the addition valid.

| Row | t (s) | Channel | x (DU) | M0 (DU) | r0 = x − M0 (DU) | M1 (DU) | r1 = r0 − M1 (DU) |
|---|---:|---|---:|---:|---:|---:|---:|
| 1 | 0 | A | 11 | 10 | 1 | 1 | 0 |
| 2 | 1 | A | 11 | 12 | −1 | −1 | 0 |
| 3 | 2 | A | 16 | 14 | 2 | 1 | 1 |
| 4 | 3 | A | 15 | 16 | −1 | −1 | 0 |

M1 is the proposed alternating sequence (1, −1, 1, −1) DU in this row order. At row 3, M0 = 10 + 2×2 = 14 DU; r0 = 16−14 = 2 DU; r1 = 2−1 = 1 DU. Reconstruct x = M0 + M1 + r1 = 14+1+1 = 16 DU. Row 4 gives 16+(−1)+0 = 15 DU. All reconstructed readings are (11, 11, 16, 15), exactly the input.

The layered equations are x = M0 + r0 and r0 = M1 + r1. Substitution yields x = M0 + M1 + r1. Preserve both residual layers and their rules. A repeated component has been decoded in an invented table; no physical cause has been identified. Row 3's remaining 1 DU is a primary coordinate for the next inquiry.

> **Claim scope:** This is exact arithmetic on synthetic data. S06 supplies metadata and a response narrative, not indexed readings and an aligned model. Its raw residual cannot be reconstructed here. Never fill that gap with this table or zeros.

## Guided practice: reverse a changed view

Subtract 10 DU from every reading: y = (1, 1, 6, 5) DU. Store that baseline and recover x = y + 10 DU at each row. If only the average y were saved, (1+1+6+5)/4 = 13/4 DU, many sequences could share that average. Row-by-row reconstruction would fail. Preserve the original or all removed details and their reconstruction rule when averaging, smoothing, or changing coordinates.

## Diagnostic checks

1. Calculate all values of M0+r0. What does equality with x establish?
2. Replace the second residual −1 with +1. What false reading is reconstructed?
3. For a new synthetic row, x = 21 DU, M0 = 18 DU, M1 = 2 DU. Find r0 and r1 and reconstruct x.
4. What is missing for S06 residual reconstruction? Can its clock rate replace those values?

## Worked answers

1. (10+1, 12−1, 14+2, 16−1) = (11,11,16,15) DU. This verifies lossless bookkeeping for the rows; it does not select a cause.
2. 12+1 = 13 DU instead of 11 DU. Losing the sign changes reconstruction by 2 DU.
3. r0 = 21−18 = 3 DU; r1 = 3−2 = 1 DU; 18+2+1 = 21 DU.
4. Indexed readings with channel, time, orientation and calibration conventions, plus aligned model values or replayable parameters are needed. Angular rate does not specify the amplitude sequence or residual.

**Next dependency:** [Lesson 4](lesson-04.md) uses retained differences to separate candidate predictions.
