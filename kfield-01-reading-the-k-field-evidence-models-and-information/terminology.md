# Terminology and notation

| Term or symbol | Meaning and scope | First taught |
|---|---|---|
| Observation | Recorded value with acquisition context; source-reported when accessed through a narrative | 1 |
| Definition | Assigned meaning or convention | 1 |
| Derived implication | Consequence of stated inputs and rules | 1 |
| Inferred structure | Organizing relationship suggested by records | 1 |
| Mechanism | Proposed process producing a response | 1 |
| Reference theory | Established framework explicitly used for comparison; not required for the arithmetic here | 1 |
| Open question | Named missing input, test, or explanation | 1 |
| Model | Rule-based representation connecting inputs and outputs under assumptions | 1 |
| Channel | Named stream of instrument readings | 1 |
| Locator | Address inside a source, such as a JSON pointer or numbered item | 2 |
| SHA-256 | 64-character content fingerprint; version identity, not proof authority | 2 |
| JSON pointer | Slash-separated field/list address; list indices begin at zero | 2 |
| Metadata | Description of a record, not the complete readings | 2 |
| Finite replay/state | Model execution on a finite collection of configurations | 2 |
| EarthOnlyAttribution | S06's additional Earth-only attribution premise; not established by a state count | 2 |
| ICRS | Named spatial reference frame in S02's contract | 2 |
| Basis; determinant; metric | Ordered coordinate directions; signed volume factor; geometric length/angle rule | 2 |
| Spectral response; co-rotation | Response organized by repeating components; physical rotation together | 2 |
| x, M, r | Reading, modeled value, signed residual: x = M+r; compatible units | 3 |
| M0, r0, M1, r1 | First model/residual and second component/residual; x = M0+M1+r1 | 3 |
| DU; s; mm | Synthetic display unit; second; millimeter. DU has no energy calibration | 3, 5 |
| t | Elapsed time in seconds in Lesson 3 | 3 |
| u | Dimensionless experimental control in Lesson 4 | 4 |
| Gain; offset | Multiplicative response factor; added baseline | 4, 5 |
| Discriminating prediction | Candidate rules give different outputs at the same specified input | 4 |
| Falsifiable | A stated possible result conflicts with a rule under its assumptions | 4 |
| Geometry/state/dynamics/instrument | Coordinate structure/current configuration/change rule/reading rule | 5 |
| q = (q1,q2,q3) | Ordered dimensionless coordinate address in Lesson 5 | 5 |
| x, O_K | In Lesson 5 geometry: physical position and declared origin, in mm for the synthetic example | 5 |
| x_reading | Explicit reading label when position x also appears | 5 |
| B, B^T, I | Ordered basis rule, its transpose, identity rule | 5 |
| M_cell = B^T B | Cell3 Gram metric; source-local G in S02. Synthetic diagonal entries have mm² | 5 |
| R_cell = M_cell^−1 | Inverse Cell3 metric; source-local R in S02. Synthetic entries have mm^−2 | 5 |

Notation is local where stated: position x is a triple; reading x is a scalar in DU. Lessons and capstone flag that distinction. G_phase is a distinct reserved phase metric in the author contract and is never substituted for M_cell. Detector parity, carry parity, chirality, and family labels are outside the finite exercises. Equal numerical values do not equate differently typed quantities.
