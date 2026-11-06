# Reading the K-Field: Evidence, Models, and Information

Five lessons for high-school seniors. [Course map](course-map.md) · [Terminology](terminology.md) · [Sources](sources.md) · [Capstone and answer key](capstone.md) · [Teacher guide](teacher-guide.md)

<!-- BEGIN: lesson-01 -->
# Lesson 1 — A model as a chain of questions

**Essential question:** What kind of claim is each step of a scientific explanation making?

**Goals:** Classify claims by their roles; separate a calculation from a proposed cause; rewrite a mixed claim as an evidence chain.

**Prerequisite bridge:** You already distinguish a number supplied in a problem from a number you calculate. Here we extend that distinction to research. No earlier K-Field knowledge is assumed.

## Build the chain from first principles

Suppose a light sensor displays 12 at one orientation and 15 at another. The recorded values are observations. A sensor channel is one named stream of readings. The unit and orientation matter: a bare 12 is not a reproducible observation. Keep order, channel, acquisition time, orientation, and unit whenever available.

A model is an explicit representation connecting inputs to outputs under stated rules. It answers a chain of questions: What was recorded? What do the terms mean? What follows by calculation? What structure might organize the result? What process might produce it? What remains unresolved? These roles differ even when they occur in one sentence.

| Role | Question answered | Entirely synthetic example |
|---|---|---|
| Observation | What was recorded? | Channel A displays 12 units at position 1 and 15 at position 2. |
| Definition | What convention are we choosing? | Define change as the second reading minus the first. |
| Derived implication | What follows from inputs and rules? | The change is 15 − 12 = 3 units. |
| Inferred structure | What organizing relationship is suggested? | Response may depend on orientation. |
| Proposed mechanism | What process could produce it? | A directional coupling could change the response. |
| Established reference theory | Which established framework supplies a comparison? | A reference model could supply its own response rule; none is needed in this arithmetic example. |
| Open question | What remains to be specified or tested? | Does the change recur at the same orientations on another cycle? |

An observation can be source-reported: you read an author's account rather than the instrument records. “Source-reported observation” preserves both content and access. A definition establishes language; it does not establish that nature follows that definition. A derivation depends on inputs and rules. A mechanism needs a process, not merely a new name for the pattern.

These distinctions make new mechanisms easier to investigate. If different systems share a pattern, preserve that recurrence and ask what common structure could explain it. Also preserve differences between the systems. Shared patterns do not make their units or definitions interchangeable.

## Worked example: unpack a paragraph

**Synthetic paragraph:** “At positions 1 and 2, channel A recorded 12 and 15 display units. Let D mean the second reading minus the first. Thus D = 3 units. A directional interaction may cause the change; it should repeat when the orientation repeats.”

The first sentence is an observation within the invented scenario. The next defines D. Substitution gives D = 15 − 12 = 3: a derived implication. The directional interaction is a mechanism hypothesis. The final clause becomes a prediction only under assumptions, such as unchanged relevant conditions and the proposed dependence on orientation. Whether it repeats remains an open question until another record is available. Calling the entire paragraph “measurement” would hide its different jobs.

> **Claim scope:** All numbers in this lesson are invented. Classification neither establishes nor dismisses a physical K-Field mechanism. The record and explanation remain separately recoverable.

## Guided practice

Rewrite this synthetic note into observation, derivation, and mechanism statements: “The readings are 4 and 9, so the difference is 5; perhaps temperature caused it.” Add an open question that could distinguish temperature and orientation accounts. Record both variables rather than deleting a reading that disagrees.

## Diagnostic checks

1. Classify “Define a repeat as returning to the same marked orientation.” Why is it not a measurement?
2. A source says its sensor recorded 8 units. You have only the narrative. What label preserves your access?
3. Classify “8 − 6 = 2” and state its dependence on the inputs.
4. Rewrite “The pattern is caused by geometry” as a proposed mechanism and an open question without inventing evidence.

## Worked answers

Guided practice: (4, 9) is the synthetic observation; 9 − 4 = 5 is derived; temperature is a proposed cause. Ask whether the same orientation gives the same response at different recorded temperatures, documenting other relevant conditions.

1. A definition assigns the criterion for repeat. It records no actual return.
2. A source-reported observation, with raw records not retrieved.
3. A derived arithmetic implication, provided 8 and 6 are the relevant same-unit inputs in that order.
4. “A geometry-dependent coupling is a candidate mechanism. Does changing orientation while holding modeled state and instrument settings fixed produce its predicted change?” The process remains proposed until its response rule is specified and compared.

**Next dependency:** [Lesson 2](lesson-02.md) attaches claims to retrievable source addresses.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 2 — Following a claim to its source

**Essential question:** What must travel with a claim so another reader can find and assess the same statement?

**Goals:** Build a file–locator–version–evidence address; distinguish a reported measurement from a finite replay; preserve the scope of a source status.

**Prerequisite bridge:** Lesson 1 classified claim roles. Now add access: a geometric derivation in its source remains source-reported to a reader who has not checked the proof.

## Build a complete source address

A filename finds a container, not a passage. A locator selects a passage inside it. A version identifies which contents were read. SHA-256 is a content fingerprint written as 64 hexadecimal characters. It checks byte identity against a pinned version, not whether the contents are correct.

JSON is structured text with named fields and ordered lists. A JSON pointer follows slash-separated field names. List positions start at zero. Thus `/backbone_sequence/0/invariants` selects the invariants field of the first item in the backbone sequence. Markdown can instead use a heading and numbered item. Full paths and fingerprints are in [sources.md](sources.md); S02 and S06 below are short labels for those records.

An evidence address contains the source ID and exact path, version fingerprint, locator, claim, evidence class, and access limits. Keep a source's status wording separate from your verification. Reading a “closed” label is different from freshly checking every proof.

## Worked example A: a geometric identity

S02 is the mature archival JSON. At `/backbone_sequence/0/invariants`, it lists `B R B^T=I`. This is a source-stated geometric identity. Read it here as “the declared combination of coordinate rules returns the input.” A transformation is a rule taking coordinates in and giving coordinates out. Lesson 5 teaches a finite arithmetic version. Deriving the full matrix identity is outside the core assessment.

At `/proof_contract`, S02 gives authority as “mature locked values at their stored precision.” Its orientation contract uses ICRS columns [a b c] and an intentional left-handed determinant. ICRS names the spatial reference frame; [a b c] fixes three basis directions in order. Do not swap that order or borrow constants from another branch. Source-local G is called M_cell in this course; source-local R is R_cell. This explicit naming translation does not change the metric.

These source labels are recognition vocabulary here. A basis provides the ordered directions used to assign coordinates. A determinant is a signed volume factor; its sign records orientation. A metric is a rule for computing geometric lengths and angles from coordinates. You need not calculate any of these for this address card. Lesson 5 introduces a small coordinate example before asking you to calculate a return identity.

At `/mature_locked_cell3/direct_reciprocal_closure_max_abs`, S02 reports `2.8939781400741195e-16`. The notation e-16 means multiply by 10 to the power −16. This is a reported numerical closure discrepancy, not an instrument residual or exact zero. The course checked source bytes and the locator; it has not rerun the full locked-matrix calculation.

## Worked example B: measurement and replay

S06, numbered item 2, **Reported angular response**, reports 180,000 samples, 2,000 rotations, ten channels, and a recovered clock of 15.0407096514 degrees/hour. A degree measures angle; degrees/hour measures angular change per hour. These are metadata describing a record, not every reading. The acquisition schema is needed to know whether a “sample” counts a multichannel acquisition or an individual channel value.

The same item says `SiderealReplay` realizes 97 finite states. A state is a model configuration; finite means the model has a specified finite collection of configurations. Those 97 states are not 97 newly measured rotations. The source gives a supplied spectral-response-law scope and separately excludes physical K-field co-rotation from that conclusion. Item 3 makes Earth coupling conditional on `EarthOnlyAttribution`, an explicit additional attribution premise. This course does not silently supply it.

Here a spectral response law describes how a response is organized by repeating components. Co-rotation means rotating together physically. A replay can reproduce a specified response rule without by itself establishing that physical motion. “Conditional” means the conclusion requires an additional stated premise. These interpretations let you preserve the source's scope without performing spectral analysis or a formal proof.

> **Claim scope:** S06 is a retrieved source narrative. Its reported formal replay and reported measured response have different authority. No compiler was run and no raw instrument series was analyzed here. The raw measurement residual remains a retrieval gap.

## Guided practice

Make two address cards for S06 item 2: A for 180,000 samples, B for 97 replay states. Give the full path and hash using sources.md, then distinguish claim roles and access limits. Explain why dividing 180,000 by ten does not establish the acquisition count per channel without its schema.

## Diagnostic checks

1. What does zero in `/backbone_sequence/0/invariants` select?
2. Does matching SHA-256 establish a theorem? What does it establish?
3. A student writes “97 measured states establish physical co-rotation.” Identify both scope changes.
4. Make an address card for the closure discrepancy, including what has and has not been verified.

## Worked answers

Guided cards: A uses the exact S06 path and hash, item 2, reported acquisition metadata, raw samples unavailable here. B uses the same address but identifies reported finite replay states, with no fresh formal execution. The sampling distribution requires an acquisition convention; division alone cannot supply it.

1. The first list item; indexing starts at zero.
2. It checks byte identity with the pinned version. Theorem correctness needs the relevant mathematical checks.
3. Replay states were promoted to measured states, and a supplied response law was promoted to physical co-rotation beyond its stated scope.
4. S02, complete path and hash from sources.md; `/mature_locked_cell3/direct_reciprocal_closure_max_abs`; reported 2.8939781400741195 × 10^−16; archival computational witness. Byte identity and field presence were checked, but the locked calculation was not reproduced. Retain the discrepancy as reported information.

**Next dependency:** [Lesson 3](lesson-03.md) examines what reconstruction requires beyond metadata.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
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
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
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
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Lesson 5 — The K-Field research map

**Essential question:** Which rules connect a geometric description to an instrument reading?

**Goals:** Trace geometry → state → dynamics → instrument; verify a finite return identity; annotate the chain with assumptions, provenance, and retained residuals.

**Prerequisite bridge:** You can classify claims, attach source addresses, reconstruct x = M+r, and compare predictions. New coordinate notation is taught below; matrix calculation is not assumed.

## Four links answer different questions

Geometry describes locations, directions, distances, and conventions. State specifies the current configuration. Dynamics supplies a rule changing that state. An instrument rule maps state and settings to a predicted reading. Every arrow needs a rule. Geometry alone does not specify starting state, time evolution, or detector calibration.

| Link | Necessary question | Gap to flag |
|---|---|---|
| Geometry | Which coordinates, origin, unit, direction order? | Missing basis or origin |
| State | Which configuration is occupied now? | Missing initial values |
| Dynamics | How does state change per step? | Missing update or time interval |
| Instrument | What reading does the state predict? | Missing gain, offset or transfer rule |

A coordinate triple is an ordered list of three numbers. In our synthetic geometry, q = (q1,q2,q3) is a dimensionless address; subscripts select entries. The origin O_K = (5,0,0) mm marks zero address. Define position x = O_K + (2q1,3q2,−4q3) mm. Multiply entries by their respective scales and add the origin entry by entry. The negative scale reverses the third direction and must be preserved. These teaching constants are not mature Cell3 constants. Here x is position; a sensor reading will be explicitly named x_reading when both occur.

## Worked geometry and source bridge

For q = (1,−1,2), displacement x−O_K = (2,−3,−8) mm and position x = (7,−3,−8) mm. Reverse by subtracting the origin and dividing entries by their scales: ((7−5)/2,−3/3,−8/(−4)) = (1,−1,2). The mm units cancel. Omitting the origin would give 7/2 rather than 1 in the first entry. Reversal needs nonzero scales: a zero first scale sends q1 = 1 and q1 = 2 to the same first displacement, so neither can be recovered uniquely.

For source reading, a matrix is a table specifying a linear coordinate rule. B denotes the ordered basis rule. B^T is its transposed table, exchanging rows and columns. Matrix multiplication composes the rules, applying the rightmost first. I is the identity rule returning its input unchanged; an inverse undoes a rule. S02 writes G = B^T B and R = G^−1, named M_cell and R_cell here. Its `B R B^T=I` is a return identity. Invertibility is a hypothesis, not established by writing the symbol for an inverse.

The synthetic B is diagonal: each output uses only its corresponding input. Transposing such a table leaves it unchanged. Its scales are (2,3,−4) mm, M_cell scales (4,9,16) mm², and R_cell scales (1/4,1/9,1/16) mm^−2. The composite B R B^T multiplies each coordinate by 2×(1/4)×2 = 1, 3×(1/9)×3 = 1, or (−4)×(1/16)×(−4) = 1. Units cancel too. It therefore returns every triple. This checks the synthetic identity; S02's non-diagonal locked basis remains a separately addressed source claim.

## Worked complete chain

Use state q = (q1,0,0), initially q1 = 1. One dynamics step lasts 1 s and adds 1 to q1. After two steps q1 = 3. Assume instrument rule M = 5 DU + (2 DU)q1 with fixed gain and offset; an offset is the added baseline. It predicts 11 DU. For synthetic x_reading = 12 DU, retain r = 12−11 = 1 DU and recover 12 = 11+1. Geometry gives first position 5+2×3 = 11 mm. Coincidence with the number 11 DU does not equate position and instrument reading: their units and rules differ.

In source work, S02 supplies a geometric contract and S06 a reported response and replay description. The conditional Earth-coupling link names `EarthOnlyAttribution`. Show that premise and the absent raw residual explicitly instead of drawing an unsupported causal arrow between files.

> **Claim scope:** Both worked chains are synthetic. Mature S02 uses ordered ICRS columns [a b c], intentional negative determinant, and stored precision. Its closure discrepancy remains reported information. No force, transferred energy, or instrument law is derived from geometry alone here.

## Guided practice

Send q = (−1,2,0) through the geometry and reverse it. In the dynamics example, start q1 = 0 and take three steps. Predict M and retain the residual for a synthetic 10 DU reading. Label geometry, initial state, dynamics, and instrument rule separately.

## Diagnostic checks

1. Why subtract O_K before reversing the coordinate rule?
2. Recompute the three return factors. Why is the third positive?
3. Start q1 = 2, take one step, and use the same instrument rule. Find M and r for x_reading = 9 DU.
4. Map S02 and S06: name a source contract, reported measurement, formal-model report, and unresolved input.

## Worked answers

Guided practice: displacement (−2,6,0) mm gives x = (3,6,0) mm. Reversal ((3−5)/2,6/3,0/(−4)) gives (−1,2,0). Dynamics ends q1 = 3, M = 11 DU, r = 10−11 = −1 DU. Coordinate scales/origin define geometry; zero is initial state; adding one per second is dynamics; 5+2q1 DU is the instrument rule.

1. B acts on displacement from the origin. Reversing absolute position changes the address.
2. The products are 1,1,1. Two negative factors yield a positive product; neither direction sign is dropped.
3. q1 becomes 3, M = 11 DU, r = 9−11 = −2 DU; 11−2 = 9 DU reconstructs the reading.
4. S02's ordered locked basis and precision are a contract. S06's angular clock is reported measurement metadata; its 97-state replay is a formal-model report. Raw residuals are unavailable; Earth-only attribution is an additional conditional input.

**Next dependency:** [Capstone](capstone.md) builds and defends the complete evidence map.
<!-- END: lesson-05 -->

