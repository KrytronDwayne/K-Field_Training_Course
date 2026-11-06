# Course map — Shape and Scale: Devon Reduction and the Jack Jacobian

Audience: high-school seniors. Entry capabilities: signed arithmetic, fractions, ratios, powers, linear equations and coordinate graphs; courses 03,08,09 provide series context. This course reteaches every additional operation used in its assessments.

Dependency chain: lesson-01 → lesson-02 → lesson-03 → lesson-04 → lesson-05 → lesson-06 → capstone. Unit boundaries follow lessons 2,4,6.

| Lesson | Concept / operational outcome | Periods |
|---|---|---|
| [lesson-01](lesson-01.md) | Logarithms as ratio coordinates: Convert multiplicative changes into additive log changes | 1 |
| [lesson-02](lesson-02.md) | One scale coordinate and two shape coordinates: Separate common scaling from scale-free shape | 2 |
| [lesson-03](lesson-03.md) | Linear response and small changes: Use a two-variable sensitivity matrix before the source Jacobian | 2 |
| [lesson-04](lesson-04.md) | The Jack map and its inverse: Reconstruct allowed input changes from the source-defined outputs | 2 |
| [lesson-05](lesson-05.md) | The typed Devon object: Keep geometry, scalar lifts, and branch coordinates separately identified | 3 |
| [lesson-06](lesson-06.md) | Limits and reconstruction tests: Check invertibility, units, and source-defined approximation domains | 1 |

11 core periods plus 2 capstone periods, each 55 minutes. Lesson 5 gained one period for prerequisite closure; IDs remain stable. All core periods allocate 5 retrieval, 20 teaching, 15 practice and 15 checks/repair minutes.

## Actual content and E05 backward map

| Concept | Explanation / example | Independently answered practice / diagnostic | Later assessment |
|---|---|---|
| C10.01 | lesson-01.md: C10.01-E1, C10.01-W1 | C10.01-P1, C10.01-D1 | capstone.md: C10-CAP-01 |
| C10.02 | lesson-02.md: C10.02-E1, C10.02-W1 | C10.02-P1, C10.02-D1 | capstone.md: C10-CAP-02 |
| C10.03 | lesson-03.md: C10.03-E1, C10.03-W1 | C10.03-P1, C10.03-D1 | capstone.md: C10-CAP-03 |
| C10.04 | lesson-04.md: C10.04-E1, C10.04-W1 | C10.04-P1, C10.04-D1 | capstone.md: C10-CAP-04 |
| C10.05 | lesson-05.md: C10.05-E1, C10.05-W1 | C10.05-P1, C10.05-D1 | capstone.md: C10-CAP-05 |
| C10.06 | lesson-06.md: C10.06-E1, C10.06-W1 | C10.06-P1, C10.06-D1 | capstone.md: C10-CAP-06 |
| C10.05-anchor | lesson-05.md: C10.05-E2, C10.05-W2 | C10.05-P2, C10.05-D2 | capstone.md: C10-CAP-05 |

Each identifier above appears in actual student-facing content. The capstone uses named separate records, not an implicit single dataset. The concrete operations and supplied inputs/outputs are as follows:

- **C10-CAP-01**: Declare positive areas and common A0; convert supplied area ratios(2,4,16) to logs and invert after a common scale change. Prior explanation C10.01-E1 and answered practice C10.01-P1.
- **C10-CAP-02**: Project into s,u,v and into mean+zero-sum shape; reconstruct all log areas, areas and the retained scale. Prior explanation C10.02-E1 and answered practice C10.02-P1.
- **C10-CAP-03**: Apply and invert H to(1,-2)t; compare exact square output at t=1/10 with its linear term and retain signed remainder .01. Prior explanation C10.03-E1 and answered practice C10.03-P1.
- **C10-CAP-04**: Apply J to(2,-1,1)t and reverse(-1,3,33)t; state orders, units, determinant and fixed-angle domain. Prior explanation C10.04-E1 and answered practice C10.04-P1.
- **C10-CAP-05**: Build typed metric/cofactor/reciprocal/scale/shape/scalar/branch entries; decode taught branch pair and recover positive scale from an area anchor using supplied fixed angles. Prior explanation C10.05-E1 and answered practice C10.05-P1. Anchor additionally uses C10.05-E2 and C10.05-P2.
- **C10-CAP-06**: Audit zero linear inverse residual versus nonzero finite approximation remainder; verify full area reconstruction and preserve domain, branch, reference area and source metadata. Prior explanation C10.06-E1 and answered practice C10.06-P1.

Preserved invariants: positive dimensionless log ratios; retained scale and signed remainders; fixed-angle Jack domain; separate geometry/scalar/branch types; source formulas versus fresh finite checks; no scalar-to-force or arbitrary-shear promotion. Markdown delivery adds no new teaching in assembly. See sources.md for exact provenance and limitations.
