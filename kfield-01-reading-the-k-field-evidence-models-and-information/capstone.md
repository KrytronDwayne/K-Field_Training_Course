# Capstone — An annotated evidence map

## Student assignment

**Question:** What is supported at each link from a geometric identity to a reported response, and what remains open?

Use Lessons 1–5 and sources.md. Produce two address cards, a diagram or table of evidence links, and the calculations below. Label arrows with their rules, assumptions, or missing inputs. Sharing a document or label does not create a causal connection.

**Source card G:** S02, `/backbone_sequence/0/invariants`, lists `B R B^T=I`. Its definitions are G = B^T B and R = G^−1, named M_cell and R_cell here. `/proof_contract` identifies mature locked values at stored precision and the ordered, intentionally left-handed ICRS basis. `/mature_locked_cell3/direct_reciprocal_closure_max_abs` reports 2.8939781400741195e-16. Use the full file path and hash from sources.md.

**Source card W:** S06, numbered item 2, **Reported angular response**, reports 180,000 samples, 2,000 rotations, ten channels, and the recovered clock 15.0407096514 degrees/hour. It describes `SiderealReplay` with 97 finite states. Item 3 names `EarthOnlyAttribution` as an additional Earth-coupling premise. Use the full logical path and hash from sources.md. No raw reading series is supplied.

1. **Addresses and roles.** Complete both addresses with versions, locators, evidence roles, and access limits. Classify the geometric identity, reported numerical discrepancy, acquisition metadata, replay, and Earth-only attribution. Include a definition, a proposed mechanism, and an open question, clearly labeled.
2. **Geometry witness.** Use Lesson 5's synthetic scales (2,3,−4) mm and O_K = (5,0,0) mm. Send q = (2,−1,1) to physical position and back. Verify the three factors of B R B^T. Explain why this checks the synthetic example but does not freshly verify S02's locked basis. Identify origin, units, scale nonzero assumption, order, and retained sign.
3. **Residual accounting.** A separate synthetic record has t = (0,1,2) s and channel A readings x = (9,13,13) DU. Use M0 = 10 DU + (2 DU/s)t and M1 = (−1,1,−1) DU. Find every r0 and r1; reconstruct x from both layers. Explain why W's residual cannot be computed here and list needed records. Do not replace that gap with zero.
4. **Separating prediction.** For the taught rules M_A = 2u DU and M_B = (u+1) DU, compare u = 1 and u = 4. Choose the separating input, state assumptions and recording requirements, and find both signed residuals for a synthetic follow-up reading of 7 DU at that input. State what remains unresolved.
5. **Research chain.** Trace geometry → state → dynamics → instrument using Lesson 5's rule, starting q1 = 1 and taking two one-second increments. Give position and reading prediction with distinct units; retain the residual for 12 DU. Place G and W on a source research map, showing what neither card supplies for a complete physical causal chain. State the conditional role of `EarthOnlyAttribution`.

**Submission check:** Preserve every supplied residual, sign, unit, version, and missing input. Label invented values. Label every causal arrow with an explicit rule or as proposed.

---

## Teacher answer key

### 1. Addresses and roles

G uses the full S02 archival path and SHA-256 in sources.md, `/backbone_sequence/0/invariants`, plus the supplied closure and contract pointers. The identity is source-stated geometry under its basis contract. The closure discrepancy is a reported numerical witness, not an instrument residual or exact zero. Byte identity and pointers were checked; the full locked calculation and all proof bodies were not freshly verified here. M_cell = B^T B and R_cell = M_cell^−1 provide a definition entry.

W uses `applications/kfield_lucas_lab/rag_corpus/50_physical_closure.md`, SHA-256 `c2a25a583af904601968adc1d3efde825f76218c92a2f52d829afc093f52c02a`, item 2, with item 3 for the attribution condition. Counts and clock are source-reported observation metadata. The 97 states belong to a reported finite model, not another measured dataset or fresh student compiler verification. Earth-only attribution is an additional premise. A valid mechanism entry is “a proposed directional coupling produces orientation-dependent response.” A valid open question asks which channel-by-time residual structure remains after a specified response model. Neither source card supplies that raw residual.

### 2. Synthetic geometry

Displacement = (2×2,3×(−1),(−4)×1) = (4,−3,−4) mm. Position = (9,−3,−4) mm. Subtract O_K then divide by scales: ((9−5)/2,−3/3,−4/(−4)) = (2,−1,1). Return factors are 2×(1/4)×2 = 1; 3×(1/9)×3 = 1; (−4)×(1/16)×(−4) = 1. The composition returns every triple. The origin is explicit, q is dimensionless, position uses mm, scales are nonzero, and order preserves the third direction's sign. S02 has a different non-diagonal locked basis and separate provenance. A checked analogue is not a recheck of its entries.

### 3. Retained residual ledger

| t (s) | Channel | x (DU) | M0 (DU) | r0 (DU) | M1 (DU) | r1 (DU) | M0+M1+r1 (DU) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0 | A | 9 | 10 | −1 | −1 | 0 | 9 |
| 1 | A | 13 | 12 | 1 | 1 | 0 | 13 |
| 2 | A | 13 | 14 | −1 | −1 | 0 | 13 |

At each row r0 = x−M0 and r1 = r0−M1. M0+r0 and M0+M1+r1 both reproduce (9,13,13) DU. Here r1 happens to be zero for every supplied synthetic row, and those zeros are retained. W's metadata do not specify raw readings or an aligned model. Needed: indexed readings, timestamps, channel identities, orientation and calibration conventions, and model values or replayable parameters. Preserve all samples and acquisition states. The acquisition schema cannot be deduced solely from total counts.

### 4. Prediction

At u = 1, both give 2 DU. At u = 4, A = 8 DU and B = 5 DU, a 3 DU separation. Choose 4 under fixed calibration, gain, settings, and modeled conditions. Record planned inputs, both predictions, times, readings, channel identities, settings, and changes. For x = 7 DU, r_A = 7−8 = −1 DU and r_B = 7−5 = +2 DU. Neither exact rule reproduces this row. Missing response structure or failed assumptions remain unresolved; preserve both differences.

### 5. Annotated chain

Synthetic geometry: ordered scales and origin → state (1,0,0) → dynamics adds (1,0,0) per 1 s twice → state (3,0,0) → instrument M = 5 DU + (2 DU)×3 = 11 DU → supplied synthetic observation 12 DU → residual +1 DU. Geometry gives position (11,0,0) mm, different in kind from 11 DU. Reconstruction gives 11+1 = 12 DU.

G supplies a geometric identity and contract; W supplies a reported response and separate replay. The cards do not supply a complete occupied physical state, a justified causal dynamics rule linking that state to the observation, a fully calibrated instrument transfer, or the raw residual. Mark those as required inputs. Earth coupling additionally requires `EarthOnlyAttribution`; the clock and replay alone do not satisfy it. Proposed mechanisms can connect the links if their status, assumptions, and discriminating predictions remain explicit.

## Point rubric — 40 points

| Item | Points | Award evidence |
|---|---:|---|
| 1. Addresses and roles | 10 | 2 exact paths; 2 complete hashes; 2 locators; 2 identity/measurement/replay scope; 2 labeled definition, mechanism and open question |
| 2. Geometry | 8 | 2 forward displacement/position; 2 reverse reconstruction; 2 identity factors; 2 origin, units, order, nonzero scales, sign and synthetic scope |
| 3. Residuals | 8 | 2 complete r0; 2 complete r1 and reconstruction; 2 row/channel/time/unit retention; 2 honest W retrieval gap and required records |
| 4. Prediction | 6 | 2 both-input predictions and choice; 2 both signed residuals; 2 assumptions, recording plan and unresolved structure |
| 5. Research chain | 8 | 2 state/update; 2 instrument and residual; 2 position/reading units; 2 source-link gaps and conditional attribution |

Use half points within compound criteria when partly correct. A passing total is a local teaching decision. Source promotion, invented raw values, lost residuals, or an unrecoverable coordinate rule must be corrected before the learning outcomes are met. Alternative mechanisms and questions earn full credit when explicitly proposed, internally consistent, and attached to a discriminating test.

## Prior-practice map

Item 1: Lessons 1–2 paragraph and source cards. Item 2: Lesson 5 forward/reverse coordinates and return products. Item 3: Lesson 3 two-layer reconstruction. Item 4: Lesson 4 A/B and C/D comparisons. Item 5: Lesson 5 full chain, using Lessons 1–4. No new operation appears only in the assessment.
