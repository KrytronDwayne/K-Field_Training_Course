# Course map — Lucas Graphs: Edges, Cycles, and Memory

Audience: high-school seniors. Entry capabilities: signed arithmetic, fractions, multiplication, coordinate tuples, and substitution into linear equations. Course 05 and course 10 are the series prerequisites; local bridges teach all graph and matrix operations required here. No calculus, group theory, spectral theorem or prior matrix course is assumed.

Dependency chain: lesson-01 → lesson-02 → lesson-03 → lesson-04 → lesson-05 → lesson-06 → capstone. The source's mathematical M08 requires M03 and M07; those source dependencies remain intact, while the finite graph definitions and proofs used for this topic are taught locally. Spectral material belongs to the next topical course and is not a hidden prerequisite.

| ID and concept | New capability | Periods | Later use |
|---|---|---:|---|
| lesson-01 / C11.01 | Build path products; count by direction | 1 | Incidence rows and columns |
| lesson-02 / C11.02 | Orient edges, multiply D, eliminate to find rank | 2 | Cycle verification and gradients |
| lesson-03 / C11.03 | Tree/chord cycle, cut gradient, orthogonality and decoder | 2 | General dimension proof |
| lesson-04 / C11.04 | Derive rank/cycle counts and reproducible Lucas tree | 1 | Periodic augmentation with same tree |
| lesson-05 / C11.05 | Wrap counts, winding/details inverse, full cycle sum | 2 | Complete state preservation |
| lesson-06 / C11.06 | Preserve general-flow remainder; scope memory claims | 1 | Capstone reconstruction |

Each period is 55 minutes, allocated 5 retrieval / 20 explanation and example / 15 guided practice / 15 diagnostics and repair. Nine core periods plus two capstone periods = 605 minutes. Original six lesson IDs are preserved; the approved two-period treatment of lessons 02, 03 and 05 prevents rank, gradients and periodic decoding from being compressed into one period each.

## Actual coverage and capstone operations

| Concept | Introduction | Worked example | Answered prior practice | Assessment | Later use |
|---|---|---|---|---|---|
| C11.01 | lesson-01: C11.01-E1 | C11.01-W1: 4/4, 6/7, 27/54 counts | C11.01-P1: square, cube, degree and rectangle drawing | C11.01-D1; C11-CAP-01 | lesson-02 |
| C11.02 | lesson-02: C11.02-E1 | C11.02-W1: triangle D, product, rank | C11.02-P1: square matrix/product/rank, reversal, transpose | C11.02-D1; C11-CAP-02 | lesson-03 |
| C11.03 | lesson-03: C11.03-E1 | C11.03-W1: triangle cycle and gradient | C11.03-P1: square tree/chord, balance, gradient, dot, decode | C11.03-D1; C11-CAP-03 | lesson-04 |
| C11.04 | lesson-04: C11.04-E1 | C11.04-W1: rectangle and Lucas dimensions | C11.04-P1: square/Lucas tree, rank, cycle basis proof | C11.04-D1; C11-CAP-04 | lesson-05 |
| C11.05 | lesson-05: C11.05-E1 | C11.05-W1: 81/55, nine-entry transform | C11.05-P1: inverse details, h_(0,9), counts, rational guard | C11.05-D1; C11-CAP-05 | lesson-06 |
| C11.06 | lesson-06: C11.06-E1 | C11.06-W1: triangle retained remainder | C11.06-P1: square inverse/divergence, update contrast | C11.06-D1; C11-CAP-06 | capstone |

Each E1, W1, P1 and D1 is an actual labeled section/item in the named lesson. The capstone supplies named inputs, outputs, full answers and point allocations; its backward map links all assessed suboperations to earlier answered practice. Four diagnostics per lesson probe more than the single indexed D1. Students work practice before reading the worked answers.

## Scope and invariants

Core source: S02#/backbone_sequence/7. All claims of physical dynamics, memory lifetime or exceptional action remain outside the proved count statements. The periodic coordinate choice retains 28 open values, 24 details and 3 windings; general flows additionally retain tree remainder. No original flow, sign or coordinate is discarded. Real/rational linear algebra is the domain of the decoder. Geometric source constants and unrelated parity/metric conventions are not imported into graph proofs.

Supporting files: terminology.md; teacher-guide.md; capstone.md; sources.md; source-provenance.json; verify_examples.py; worked-example-verification.json; independent-content-audit.json. Recovery authority is manifest.json. Final student assembly is course.md, containing the six lesson texts verbatim in the declared order and links to supporting material.
