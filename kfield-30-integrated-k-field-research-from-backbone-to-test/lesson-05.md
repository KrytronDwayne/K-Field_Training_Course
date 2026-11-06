# Lesson 5 — Preregistering a complete protocol

Essential question: What must be fixed before an experiment so that every outcome remains interpretable?

Goals: Write a prospective protocol with named fields; preserve all result branches; distinguish missing metadata from zero readings; define a reversible transform and stopping rule.

Prerequisite bridge: Lesson 4 froze competing predictions. A **protocol** is an executable instruction set for collecting and interpreting outputs. **Preregistration** means fixing a version before seeing the check outcomes. It prevents the original question from vanishing when an unexpected result motivates a new one.

## C30.05-E1 — Freeze the whole path

A usable protocol records the question, candidates and parameter values; source paths/hashes and domains; geometry/frame, site and orientation; device/channel identities; timing and exposure; calibration reference, version, units and uncertainty; training versus independent check roles; transformations and reconstructions; comparison branches; raw-data destination and metadata; stopping/interruption rules; and responsible operator and reviewer.

UTC is a common time standard. A midpoint timestamp identifies the middle of an exposure, not necessarily its start. Exposure duration states the interval over which the instrument collects a value. A blinded operator label conceals the candidate interpretation while preserving a separate recoverable label mapping. Training data may set parameters; check data evaluates the frozen version. A new version needs a new check allocation.

Non-destructive transformation means retaining enough to reconstruct the input. If a known offset b is subtracted, y_corrected=y_raw−b, retain b so y_raw=y_corrected+b. If invalid acquisition is independently identified, retain the affected raw row and its fault reason in parallel. A missing value cannot be converted to the numeric value zero.

## C30.05-W1 — Fully specified synthetic rehearsal v1

This is an arithmetic rehearsal, not an instrument run. The model fixes thetaA=(2,1), and two ordered operators: sum then difference. Prediction p=(3,1). Input rows are labeled S,D; all values are dimensionless. Transformation is identity; residual is r=y−p; reconstruction is y=p+r. Stop after both rows are supplied, or record interruption with whichever rows are present. Never impute an unprovided row. Candidate B stays (1,2), prediction (3,−1). Compare exact synthetic equality to each vector, retaining mismatch-to-both and absent/invalid cases.

The authored rehearsal inputs, revealed for the next lesson, are (3,0). This makes the exercise repeatable while preserving the original frozen prediction. A genuine future run must first replace every missing apparatus field below with verified information and freeze the new version. No device readings have been supplied here.

## C30.05-P1 — Draft a planned real protocol

Copy and complete this table. Its answer illustrates honest completion of a plan when instrument access is unavailable; a missing field is a gate on execution, not a fabricated value.

| Field | Planned value or unresolved entry | Owner / return address |
|---|---|---|
| Question and model | A versus B from Lesson 4; sum/difference predictions frozen | analyst / this lesson W1 |
| Source version | S02 mature geometry; S03 corrections; T30 capability boundary | analyst / sources.md |
| Raw destination | remain in instrument's original acquisition store; actual absolute location missing | operator / protocol field `raw_destination` |
| Instrument and channel IDs | missing; must demonstrate physical sum and difference response | operator / `device_channels` |
| Geometry/site/orientation | frozen convention needed; ICRS columns [a b c], intentional handedness; actual site/orientation missing | operator / `geometry_site_orientation` |
| Time and exposure | UTC midpoint convention selected; actual epoch and duration missing | operator / `timing` |
| Transfer/calibration | reference identity, version, operating range and units missing | calibration lead / `calibration` |
| Uncertainty | instrument-specific bounds and dependencies missing; toy 1/4 bound not adopted | calibration lead / `uncertainty` |
| Blinding | labels S,D hidden by custodian's retained mapping; real mapping not yet assigned | custodian / `label_map` |
| Training/check allocation | calibration/training records separate; future acquisition is check only | analyst / `roles` |
| Transform and outputs | preserve raw row, any offset/gain, transformed value, prediction, signed residual, reconstruction | analyst / `transform_v1` |
| Stop and exceptions | stop after two valid planned operator records, or log interruption; retain all attempted/faulted rows | operator / `stop_rule` |
| Comparison | A-compatible, B-compatible, unresolved overlap, mismatch to both, invalid/incomplete; retain raw values in every branch | analyst / `comparison` |
| Independent review | reviewer identity missing; must independently replay versioned analysis | research lead / `reviewer` |
| Execution state | planned; not ready for acquisition until required metadata and transfer are pinned | research lead / `execution` |

Answer: The table is a complete field inventory and an explicitly gated draft. It is not an executed experiment or a ready-to-run instrument contract. Recording the actual raw destination in place means pointing to the acquisition store rather than copying source data into this course. A calibration change creates a new version and retains the previous one.

> Claim scope: This course can finish the research portfolio while the empirical protocol remains planned. Detection, extraction and induction branches require different evidence (T30). Signed source events are kept by immutable reference, not reinterpreted as fourteen independent plane costs: the supplied bundle has three distinct plane-family cost levels.

## C30.05-D1 — Diagnostics and worked answers

1. A difference row never arrives. Is its residual −1? **Answer:** No; its value and residual are undefined/missing. −1 would follow from an actual numeric zero reading, a different case.
2. Subtract offset 2 from raw value 7. What is retained? **Answer:** Corrected value 5, offset 2, row identity and raw pointer; 5+2 reconstructs 7.
3. Can the toy uncertainty bound become an instrument bound? **Answer:** Only with a relevant calibration witness; an authored teaching number supplies none.
4. What happens after calibration changes mid-run? **Answer:** Record timing, old/new versions and all rows; mark the departure, preserve the frozen comparison, and define a new protocol/check scope.

Next dependency: [Lesson 6](lesson-06.md) interprets completed, discrepant and interrupted outcomes without erasure.
