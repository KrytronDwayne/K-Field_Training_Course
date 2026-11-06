# Lesson 6 — Independent replication and negative outcomes

Essential question: How can an unexpected outcome identify the next useful measurement?

Goals: Compute and reconstruct signed residuals; distinguish replay from replication; preserve negative and invalid outcomes; propose a measurement separating model change from transfer change.

Prerequisite bridge: The protocol fixes prediction p and comparison rules before check data. A residual r is the componentwise difference y−p. Componentwise means subtract matching channels in their original order. It remains a primary coordinate of the result, not a reason to remove the row.

## C30.06-E1 — Keep both the model and the discrepancy

Replay uses the same inputs to check a computation. Independent replication obtains a new acquisition under a documented protocol with independently inspectable calibration and analysis. A second computer reading the same file is useful replay, but not a new physical observation. Independence is described by records: which apparatus, reference, operator, timing and processing are shared, and which are independently established? It is not asserted merely by changing a filename.

A zero response is a number. A negative response is a signed number. A failed acquisition is a record with a fault state. An interruption is an incomplete execution record. Preserve each according to its type. Compare residual patterns across channel, time, orientation and calibration state as possible missing coordinates. A new explanatory model can decode part of r, but the original p and r must still reconstruct the original y.

## C30.06-W1 — Rehearsal outcome

The authored, dimensionless rehearsal values from Lesson 5 are y=(3,0), with frozen A prediction p=(3,1). Thus r=(3−3,0−1)=(0,−1). Reconstruction gives p+r=(3+0,1−1)=(3,0), exactly the original pair. The sum agrees with A while the difference does not. For B, pB=(3,−1), so rB=(0,+1). Retain both signed residual vectors; neither candidate exactly matches the synthetic pair.

This pattern suggests at least two next branches. The underlying contributions might now be equal, giving a zero difference, or the difference-channel transfer might be failing or differently scaled. A known nonzero difference reference would test that transfer separately. Merely reusing the sum cannot separate those explanations. The instrument-specific known reference and its uncertainty remain to be specified before an empirical test.

## C30.06-P1 — Conditional future replication

If a future independent reading were (4,1), what residual would the frozen A prediction give? State what is retained and propose a separate calibration check.

Answer: r=(4−3,1−1)=(1,0). Reconstruction gives (3,1)+(1,0)=(4,1). This is a conditional example, not an observation. The sum changed while the difference did not. A separate known sum reference could test whether sum-channel gain changed; an independently calibrated contribution measurement could instead test a changed parameter sum. Keep both branches, the original prediction, the future acquisition identity, and the complete residual. For B the conditional residual is (1,2), also retained.

One informative next measurement has an input known independently of the unknown mechanism. In the toy product gR=6, if a known reference established g=2, then R=6/2=3 within that product model. The reference does the identifying work; the old product reading alone does not. In reality reference bounds and transfer conditions propagate into R's admissible range.

> Claim scope: This lesson performs synthetic arithmetic only. Agreement, disagreement and recurrence are all retained information. An unexplained residual motivates a mechanism test; it does not specify a unique mechanism without the additional distinguishing measurements.

## C30.06-D1 — Diagnostics and worked answers

1. For p=(3,1),y=(2,−1), find r and reconstruct. **Answer:** r=(−1,−2); (3−1,1−2)=(2,−1).
2. Is rerunning the same file on another computer independent physical replication? **Answer:** It is independent computational replay; a new acquisition is needed for physical replication.
3. May a negative result be removed from a summary table? **Answer:** Preserve its signed values and metadata; summaries may index it but cannot replace its residual record.
4. If a sensor saturates, why not set its reading to zero? **Answer:** Saturation is a fault/limit state, not a zero value. Retain the original recorded value, flag, range and reason, and keep any corrected view separately.

Next dependency: [Lesson 7](lesson-07.md) packages these records so another researcher can recover every distinction.
