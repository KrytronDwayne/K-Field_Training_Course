# Signed event evidence

**Essential question:** How do we keep fourteen responses while recognizing that they use only three cost inputs?

**Goals:** Read a signed event with provenance; distinguish count contrast, fractional response and plane cost; count independent cost levels without deleting response rows.

**Prerequisite bridge.** Lessons 5–6 supplied four-angle reconstruction, g, ρ, P and model energy. We now read reported source records. A JSON pointer such as /events/3 selects the fourth array entry because indices start at zero. A SHA-256 digest identifies file bytes; matching it establishes byte identity, not the truth of a physical claim.

## C26.07-E1 — Read the source card first

The 2026-08-26 bundle contains two works, each represented as JSON, PDF and abstract. These six files are not six independent studies. The computational representations are the two JSON works. T35 assigns the observations the class **reported_exploratory_to_be_verified**. Read [sources](sources.md) for whole-object digests and exact paths. The source entries below retain their original order; adjacent paired rows share an event context.

A matrix is a rectangular table of numbers. Multiplying a matrix by a vector takes a dot product for each row. A superscript T means turn a column into a row. Thus qF=nᵀ G_phase n means first calculate G_phase n, then dot it with n. The source's symmetric phase metric has rows (2.9764106378,1.2431507795,−2.0803600354), (1.2431507795,2.5922286635,−2.3178839937), (−2.0803600354,−2.3178839937,6.7735709133). Its qF values are source phase-cost scalars, not joules or detector counts. Here we read the reported family values rather than claim an independently certified locked-geometry replay.

For intuition only, take synthetic matrix diag(2,3,4), meaning rows (2,0,0),(0,3,0),(0,0,4), and n=(1,0,0). Matrix multiplication gives (2,0,0); dotting with n gives qF=2. Reversing n gives the same cost because both factors change sign. A signed channel contrast need not stay unchanged. Therefore a projective cost and signed gain have different roles even when their numbers happen to match.

The source assigns w cost 1.777875828850227, v cost 5.949871981229392 and lambda cost 5.7964545517567245. There are four w rows, four v rows and six lambda rows. Fourteen response rows therefore use three independent plane-cost levels, not fourteen. “Independent levels” here counts distinct inputs; it does not assert statistical independence among families. Keep every response and any shared calibration/covariance information. Covariance records how coordinates vary together; shared inputs do not become new measurements merely by appearing in more rows.

## All-row reference ledger

Each index below references spectral-work /events/index and energy-work /all_event_channel_modulations/index. Full timestamps, signed velocities, gains, uncertainties and context stay in those immutable objects. The compact verification file retains row-by-row reconstruction and response closure. No raw acquisition is copied.

| Index | Event ID (pair:channel nm:family) | gain sign | source energy |
|---:|---|:---:|---|
| 0 | 415-515:415:w | + | null |
| 1 | 415-515:515:w | + | supplied |
| 2 | 445-555:445:v | + | supplied |
| 3 | 445-555:555:v | − | null |
| 4 | 480-630:480:lambda | − | null |
| 5 | 480-630:630:lambda | + | supplied |
| 6 | 515-680:515:lambda | − | null |
| 7 | 515-680:680:lambda | − | null |
| 8 | 630-910:630:w | + | supplied |
| 9 | 630-910:910:w | + | null |
| 10 | 415-590:415:lambda | − | null |
| 11 | 415-590:590:lambda | + | null |
| 12 | 515-590:515:v | − | null |
| 13 | 515-590:590:v | + | supplied |

The energy source names the lambda family “lambda-sheet”; the join above explicitly maps lambda-sheet to lambda. The table contains eight positive and six negative gains. Exactly five rows have energy intervals. Three positive rows have null energy fields, so “positive” and “energy selected” are not synonyms.

## C26.07-W1 — A negative row remains evidence

Read /events/3, 445-555:555:v. It shares the pair and timestamp 2026-08-25T16:51:46.693615Z with positive /events/2 at 445 nm. Row 3 has g=−0.0003402658026657847 and ρ=0.0006982587209209132. Dividing gives P approximately −0.4873061982197916. Since ρ is positive, the negative sign comes from g and remains in P. Its plane cost is the same v-family cost as its positive partner; its energy field is null. Shared cost does not imply equal or same-sign responses.

## C26.07-P1 — Worked source-card practice

For /events/0, 415-515:415:w, g=0.0005055808785109474 and ρ=0.0000574509228616101. Calculate P and interpret its energy field. **Answer:** P=g/ρ≈8.800222056115778; energy is null, not zero.

The linked energy-work /all_event_channel_modulations/0 reports four counts in angle order:
(1485.2562384582884,1483.8843576874326,1483.1281192291442,1483).
Their means are M≈1484.1921788437162 and Q≈1483.4421788437162, giving contrast 0.75 count. The half-differences are D₀≈1.064059614572102 and D₉₀≈0.4421788437163059. Adding and subtracting these reconstructs the input counts to binary64 rounding. The signed reconstruction residuals input-minus-reconstruction are (0,2.2737367544323206e−13,2.2737367544323206e−13,0) counts in this replay; they are saved, not silently rounded away. Binary64 is finite computer arithmetic and this check is not an exact interval certificate.

## C26.07-D1 — Diagnostic checks and answers

1. Count cost levels and rows. **Answer:** Three levels; fourteen response rows. Keep the within-family differences.
2. Is a negative gain an invalid observation? **Answer:** Not from its sign. It is a signed contrast relative to the quadrature baseline and stays alongside its partner.
3. How many independent studies do the six representations supply? **Answer:** Two works, not six studies. Their representations are linked evidence.
4. Does a sub-degree interpolated match establish sub-degree acquisition precision? **Answer:** No. The source acquisition grid is 4 degrees; interpolation and mechanical uncertainty remain separately required.
5. What provenance conditions remain? **Answer:** The bundle reports a declared energy revision f98c… versus packaged 9120… and a quadratic PDF digest/size mismatch. Preserve both references and conditions; do not silently merge revisions.

> **Evidence layers:** Counts and signed rows are source-reported observations; g and P are derived coordinates; qF is a model cost. A proposed beat pathway is a mechanism hypothesis. The source reports 65,880 processed rows, including 65,845 healthy and 35 diagnostic rows; the latter remain with masks and reasons in any production replay. We have replayed the compact reported-event arithmetic, not recovered raw acquisition, calibrated transfer or freshly compiled source proofs. The physical CMB authority 369812.50200040644 m/s is distinct from the experiment-local velocity.

**Next dependency:** [Lesson 8](lesson-08.md) carries the complete residual into the next comparison.
