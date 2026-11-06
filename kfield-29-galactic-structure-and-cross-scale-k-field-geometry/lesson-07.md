# Discovery and held-out comparisons

Essential question: What makes a held-out comparison a test of an already chosen geometry?

Goals: State what must be frozen; retain all signed occupancy differences and phase shifts; distinguish source control families from changes fitted after inspection.

Prerequisite bridge. Lesson 06 retained full memberships and residual channels. We now compare two populations under one preselected assignment rule. The two periods cover the discovery contract and the complete discrepancy ledger.

## C29.07-E1 — Separate choosing from checking

Discovery data may choose candidate plane normals, spacings, phases and the three-plane system. Once chosen, save them with basis order, units, source hashes, assignment algorithm and boundary convention. **Freeze** means do not alter these choices while evaluating the holdout. A holdout is a population not used to choose that fitted configuration. Reusing its answers to choose a better phase makes a new exploratory branch, which can be valuable but needs a later independent check.

G04 p3 reports 57,076 discovery positions and 57,305 holdout positions. Their sum is 114,381. It says discovery selected candidate directions, spacings, phases and triad; final assignments used actual directed vectors. G02 p8 reports three controls: full orientation rotations (600 runs), common phase translations (600), and RA/Dec coordinate permutations (300). Each changes a different part of the arrangement. An orientation rotation preserves internal angles of the cell while changing its relation to the sky; a phase translation shifts plane offsets; coordinate permutation tests the joint angular coordinate structure. Those controls are not interchangeable, and their source statistics remain attached to their original families.

A count divided by population size is a fraction. Comparing fractions is useful when populations differ in size, but retain original counts, totals and identities at their source. A signed difference is always declared in order: here **holdout minus discovery**. Correlation compresses the relation between two vectors to one number; it cannot replace the componentwise differences or explain them away.

## C29.07-W1 — Complete seven-sheet reading

G01#/observed_27_node_occupancy contains seven-element discovery, holdout and rotation-mean fraction arrays. [Source comparison ledger](source-comparison.md) displays all their entries and every holdout-minus-discovery difference. For example on sheet -3, the stored values give

`0.012634150597679085 - 0.012264349288667742 ≈ +0.000369801309011343`.

On sheet 0 the corresponding difference is approximately -0.00246333476723913. Report both directions of difference, not only enhanced sheets. The verification script computes all seven from the hashed original record, retaining decimal subtraction results without interpreting them as exact rational population ratios. Summing each source fraction vector gives approximately one; the tiny stored-precision remainder is also retained.

The source's discovery/holdout correlation is 0.9995135003207234. This is a source-reported descriptive statistic, not an independently recomputed 27-state statistic here: G01 does not contain the full 27-state vectors needed for that replay. The seven-sheet subtraction is a fresh, narrower computation. Do not label the two checks as equivalent.

## C29.07-P1 — Frozen versus refitted practice

Toy discovery occupancies (1,2,1) and holdout occupancies (0,3,1) produce (-1,1,0). Both totals are four. Retain all three bins and the memberships established in lesson 06.

Freeze synthetic A=I₂ L and phi=(1/4,1/2). For a holdout point x=(3/10,1/2)L, the old k=0 center is (1/4,1/2)L and residual is (1/20,0)L. After looking at x, someone proposes phi'=(1/3,1/2). The phase shift is phi'-phi=(1/12,0). The new k=0 center is (1/3,1/2)L and residual (-1/30,0)L. Reconstruct x from either pair: 1/4+1/20=3/10 and 1/3-1/30=3/10. The integer label happens not to change; the center and signed residual do. Keep both assignments and the branch history. An improved distance after refitting does not turn the exploratory branch into a frozen test.

> Source interpretation boundary. G01#/pure_holonomy_coordinate_tests attributes the detected structure to mixed branch-lift coordinates rather than an isolated pure sheet/A2 harmonic under its tested family. Its family statistic and interpretation remain source-reported. We retain weak pure-coordinate channels alongside mixed-coordinate results. G02 pp17–20 distinguishes these constructions; a pure-coordinate test is not a substitute for the full-state comparison.

## Diagnostics — C29.07-D1

1. Name four geometric choices to freeze before evaluating holdout.
2. A phase is changed after examining holdout. What must happen to the old result?
3. Does a high correlation justify omitting a negative sheet difference?
4. What has this course freshly verified about G01 occupancy, and what has it not replayed?

Worked answers. 1. Normals, spacings, common phase and selected triad, with assignment and conventions also saved. 2. Preserve the frozen result and add a named exploratory branch, including phase difference and both residuals. 3. No: the signed component is retained information and may locate an unresolved mechanism. 4. It checks the seven-sheet stored fractions and their differences; it does not reconstruct 27-state occupancy or independently reproduce the source correlation from catalog rows.

Next: [lesson 08](lesson-08.md) turns a cross-domain similarity into an explicit transformation and prospective prediction.
