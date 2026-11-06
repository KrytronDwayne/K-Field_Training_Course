# Course map — Projective Integerization and Carry Dynamics

Six lessons, seven 55-minute core periods, followed by two capstone periods. Lesson 04 is deliberately split across two periods to teach the carry derivation before the parity-constrained side transform. The approved six-lesson dependency order is retained. All core calculations are finite and use taught arithmetic.

Entry capabilities: signed arithmetic, exact fractions, ratios, powers, linear equations, and ordered triples. Course-08 ray capability is refreshed in lesson 02 by explicit normalization; no unprovided theorem from that course is required.

## Coverage and prerequisite sequence

| Concept | Explanation | Worked example | Independently answered practice | Diagnostic | Later use | Minutes |
|---|---|---|---|---|---|---:|
| C09.01: Nearest-integer maps need a tie rule | lesson-01: C09.01-E1; E2 | C09.01-W1 | C09.01-P1 | C09.01-D1–D4 | lesson-02 | 55 |
| C09.02: Projective rays at successive scales | lesson-02: C09.02-E1; E2 | C09.02-W1 | C09.02-P1 | C09.02-D1–D4 | lesson-03 | 55 |
| C09.03: The retained rounding coordinate | lesson-03: C09.03-E1 | C09.03-W1 | C09.03-P1 | C09.03-D1–D4 | lesson-04 | 55 |
| C09.04: Carry between generations | lesson-04: C09.04-E1; E2 | C09.04-W1 | C09.04-P1 | C09.04-D1–D4 | lesson-05 | 110 |
| C09.05: Small differences at deeper levels | lesson-05: C09.05-E1; E2 | C09.05-W1 | C09.05-P1 | C09.05-D1–D4 | lesson-06 | 55 |
| C09.06: A lossless recursive compiler | lesson-06: C09.06-E1; E2 | C09.06-W1 | C09.06-P1 | C09.06-D1–D4 | capstone | 55 |

Every lesson depends on the previous lesson; lesson 01 starts from the stated entry capabilities. Unit 1 is lessons 01–03 (encode and recover); unit 2 is lesson 04 (carry and side coordinates); unit 3 is lessons 05–06 (compare and audit). At each boundary review the exact decoder and the relevant prior diagnostics before advancing.

## Capstone backward map — concrete inputs and outputs

| Step | Input → output operation | Earlier explanation | Earlier answered practice | Check |
|---|---|---|---|---|
| C09-CAP-01 | ±1/2 → integer/residual/owner triples; declare rule | C09.01-E1, 01-E2 | C09.01-P1 signed-tie return portion; 01-D1 and D4 | C09.01-D1 |
| C09-CAP-02 | T and g0..2 → exact scales and integer table | C09.02-E1 | C09.02-P1 | C09.02-D1 |
| C09-CAP-03 | scaled inputs and Q → signed residuals and reconstructed T | C09.03-E1 | C09.03-P1 | C09.03-D1 |
| C09-CAP-04 | adjacent rows → carries by both routes → S/A → integer inverse halves | C09.04-E1, 04-E2 | C09.04-P1; 04-D1/D3 for parity rejection | C09.04-D1 |
| C09-CAP-05 | T,T' through g3 → full comparison and first split; historical card → difference and provenance | C09.05-E1, 05-E2 | C09.05-P1; 05-D1 for historical reading | C09.05-D1–D4 |
| C09-CAP-06 | Q0, side modes, terminal epsilon → finite sum, backward residuals, full round trip and metadata | C09.06-E1, 06-E2 | C09.06-P1; 06-D1/D4 for metadata and scope | C09.06-D1 |

ID convention: within the backward-map shorthand, each numbered fragment such as 04-E2 expands to C09.04-E2. D1–D4 denotes the four separately numbered diagnostic items, not a generic coverage placeholder. Each item is present with an answer before the capstone. P1 prompts require an independent attempt before reading answers. For lesson 01, teach E2 before the signed-tie return portion of P1.

## Timing and teaching contract

Each 55-minute core period reserves 5 retrieval, 20 explanation/worked example, 15 guided practice, and 15 independent diagnostics/repair minutes. Lesson 04 uses this allocation twice. The teacher guide specifies its split; capstone.md specifies the two synthesis periods. Additional repair time is permitted when a prerequisite gate fails.

Core boundary: exact finite ledgers and supplied source-reading cards. Infinite-series recognition is optional; no limit proof, archive-wide proof certification, mass identification, or gauge transport is assessed. All six source-kernel operations are introduced, practiced, assessed, and reused.
