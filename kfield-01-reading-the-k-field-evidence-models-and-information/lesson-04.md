# Lesson 4 — Assumptions and falsifiable predictions

**Essential question:** How can a new input make two explanations give different answers?

**Goals:** State a model's assumptions; derive competing predictions; design a discriminating comparison retaining every result and residual.

**Prerequisite bridge:** Lesson 3 separated x, a model, and its residual. Now compare two models under the same declared conditions. An explanation's performance never licenses erasing disagreeing readings.

## Give each assumption a visible job

An assumption is a condition used by an argument. If a prediction uses constant gain, list constant gain. Gain is the multiplier connecting an input state to an instrument response. If it uses constant temperature, record that requirement too. An assumption can be well motivated; writing it makes its role inspectable.

A prediction is an output calculated before inspecting the proposed comparison's outcome. A discriminating prediction gives different outputs from candidate rules at the same specified input. Falsifiable means a stated possible result conflicts with the proposed rule under its assumptions. If assumptions fail, preserve their failure alongside the reading; do not silently rewrite the original prediction.

## Worked example: agreement and separation

Let u be a synthetic dimensionless control, a number with no physical unit. Responses use DU. Model A predicts M_A = 2u DU. Model B predicts M_B = (u+1) DU. These are invented response rules, not measured K-Field laws. Both assume the same control calibration, stable instrument settings, and no omitted changing input during comparison.

At u = 1, A gives 2×1 = 2 DU; B gives 1+1 = 2 DU. A reading of 2 DU there would not distinguish them. At u = 3, A predicts 6 DU and B predicts 4 DU. Their difference is 2 DU. Choosing u = 3 creates separation that u = 1 cannot provide.

Suppose a synthetic follow-up gives x = 5 DU at u = 3. Preserve r_A = 5−6 = −1 DU and r_B = 5−4 = +1 DU. Neither exact rule produces 5 under the stated conditions. Equal residual magnitudes do not identify a cause. They locate missing structure to investigate: an untracked input, a changed gain, or another response component. Averaging the predictions afterward does not make either original rule succeed.

A comparison record needs planned inputs, time, channel, calibration, settings, both predictions, readings, signed residuals, and observed departures from assumptions. Repeat or reorder inputs to expose time dependence, retaining every pass. No actual experiment is performed in this course.

## Compare mechanism classes

A mechanism class is a family of processes with a shared proposed way of producing an output. An orientation-only account predicts repeatability when orientation repeats under unchanged relevant conditions. A memory-dependent account may predict dependence on earlier states. Ask where their predictions separate and retain the relevant history. Across systems, compare explanatory reach, added parameters, compatible units, and internal consistency. Recurrence is an explanatory target; differences and residuals help specify it.

> **Claim scope:** Conflict with an exact prediction concerns a rule plus its assumptions. Residual structure remains information. In S06, `EarthOnlyAttribution` is an additional premise for Earth coupling; the reported angular clock alone does not supply it.

## Guided practice

Models C and D give M_C = (u+2) DU and M_D = 2u DU. Compute both at u = 2 and u = 4. Choose the more discriminating input. State a condition to keep fixed and metadata that would check it.

## Diagnostic checks

1. Solve 2u = u+1 for A and B. Why is this input unhelpful for separation?
2. At u = 0, predict A and B. For synthetic x = 1 DU, retain both residuals.
3. If gain changes between runs, what should be recorded before attributing a response change to u?
4. Why does S06's 97-state replay not by itself discharge `EarthOnlyAttribution`?

## Worked answers

Guided practice: at 2, C = 4 and D = 4 DU; at 4, C = 6 and D = 8 DU. Choose 4 for a 2 DU separation. Keep gain fixed and record the gain setting and calibration version for each run.

1. Subtract u: u = 1. Both then predict 2 DU.
2. A = 0 DU; B = 1 DU. r_A = 1−0 = 1 DU; r_B = 1−1 = 0 DU. B reproduces this row; the other residual remains available.
3. Both gain settings, times, control values, readings, and model rules. Recalculate predictions with the change explicitly represented, retaining original readings and residuals.
4. A finite replay implements a state rule. Earth-only causal attribution is a separate named premise, not a consequence of counting model states.

**Next dependency:** [Lesson 5](lesson-05.md) joins these operations into a geometry-to-instrument map.
