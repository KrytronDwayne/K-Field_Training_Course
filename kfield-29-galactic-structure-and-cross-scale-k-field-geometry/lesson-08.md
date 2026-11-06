# A cross-domain explanatory map

Essential question: What extra structure makes a recurring pattern a testable cross-domain explanation?

Goals: Derive scale-normalized metric invariance; distinguish shape from orientation; specify a frozen independent prediction with retained mismatch channels.

Prerequisite bridge. Lessons 04–05 taught roots, metrics and eigen-directions; lesson 07 taught frozen comparisons. We combine those capabilities over two periods. Eigenframe here means the ordered set of perpendicular eigen-directions of a specified symmetric matrix, with signs or projective conventions declared. We do not ask students to diagonalize a source matrix numerically.

## C29.08-E1 — Write the transformation, then identify what survives

A candidate explanation should say which objects correspond, how to transform them, what is invariant, and what new observation would distinguish it from alternatives. Shared algebra is one layer. The metric, orientation, occupancy and calibrated physical role are additional layers. A mechanism sufficient to explain recurrence across domains must account for the measured differences too.

Suppose every edge of a three-dimensional basis is multiplied by a positive scalar s. Each dot product gains s², so M becomes s²M. Volume V=|det A| gains s³ because three independent directions are scaled. Define the volume-normalized metric `M_bar=M/V^(2/3)`. The exponent 2/3 means “take a cube root, then square.” V has units L³, so V^(2/3) has units L²; M_bar is dimensionless. For positive s, `(s³V)^(2/3)=s²V^(2/3)`, so M_bar is unchanged. Store V as well as M_bar to recover M: M=V^(2/3)M_bar. A normalized view alone intentionally hides overall scale; retaining V makes the representation reversible.

A rotation U preserves dot products: its defining algebraic check is UᵀU=I. For a rotated basis UA, `(UA)ᵀ(UA)=AᵀUᵀUA=AᵀA`. Thus orientation can change while Gram stays fixed. The rotation must still be retained if reconstruction in ICRS matters. A reflection also preserves Gram but changes handedness; only det(U)=+1 is a proper rotation. Equal Gram matrices alone cannot distinguish reflection. Changes of shape generally alter the normalized metric.

## C29.08-W1 — Worked scaling and shape comparison

Synthetic A=diag(1,2,3)L has V=6L³ and M=diag(1,4,9)L². For 2A, volume is 48L³, metric diag(4,16,36)L² and every root doubles. Since 48^(2/3)=4·6^(2/3), dividing the new metric by the new volume scale yields exactly the old M_bar. This is a mathematical implication of uniform scaling, not evidence that any two physical systems are related by that scaling.

Contrast A'=diag(2,1,4)L from lesson 04. Its volume is 8L³ and metric diag(4,1,16)L². Relative to the same ordered labels, its first-to-second diagonal metric ratio is 4, whereas A's ratio is 1/4. Uniform scaling cannot explain that change. To compare actual cells one must preserve order or explicitly record and justify any permutation. A changed ratio is a retained structural difference.

## C29.08-P1 — From source hypothesis to future test

G02 p19 proposes that hard-mode-aligned states should be preferentially depleted. Its post hoc projection is the source of this hypothesis, not a performed independent test. Here “hard mode” refers to the larger nonzero eigenvalue of the holonomy root tensor K=sum s sᵀ; applying s sᵀ to v means s(s·v). The roots lie in a plane, so its normal has K N=0. The two in-plane directions receive different multipliers. This defines the source terms without conflating K with lesson 05's distance metric.

A valid prospective plan freezes the galaxy basis, phase, root-tensor eigenframe, the state set to be tested, assignment algorithm, inclusion rules and control comparison before opening a new independent catalog. Save survey selection inputs that describe which sky regions or objects could be observed. Missing selection information stays an unresolved field. If testing distance shells, require independent distances and freeze shell boundaries; do not manufacture them from a unit sphere.

For a finite **synthetic planning exercise**, suppose a frozen transformation has already assigned four equally exposed states to hard-aligned labels H1,H2 and comparison labels C1,C2. Define the contrast as mean hard occupancy fraction minus mean comparison fraction. Predict contrast <0 in the independent sample. Toy counts (1,1,3,3) total eight, fractions (1/8,1/8,3/8,3/8), giving contrast 1/8-3/8=-1/4. Counts (3,3,1,1) instead give +1/4, contradicting this directional prediction under the stated equal-exposure contract. Zero would also fail the strict “<0” rule. Neither outcome is erased. The four-state example teaches the operation; actual work retains all 27 states, controls, exposures and residuals, with a justified aligned-state mapping fixed in advance.

> Claim scope. Proposed common transport or scale-coupling mechanisms are hypotheses to compare by explanatory reach and independent predictions. The algebraic invariance above is derived; source occupancy is reported evidence; hard-mode depletion is a proposed test; physical galaxy length calibration and survey selection remain unresolved here. G02 pp19–20 also notes many possible compound ratios. A ratio chosen after seeing all candidates must retain the search family and compete prospectively, not be relabeled as an independent lock.

## Diagnostics — C29.08-D1

1. Under A→3A, how do M, V and roots change?
2. What additional value reconstructs M from M_bar?
3. Why does equal Gram not establish equal ICRS orientation or handedness?
4. For equal-exposure toy counts (2,2,2,2), does the strict depletion prediction pass?
5. What makes a new eigenframe selected after seeing the new catalog exploratory?

Worked answers. 1. M→9M, V→27V, roots→3 roots. 2. V, through M=V^(2/3)M_bar; retain the basis or orientation mapping for full vector reconstruction too. 3. Rotations preserve Gram, and reflections preserve it while reversing orientation. 4. All fractions are 1/4 and contrast is 0, so the strict negative prediction fails; retain every count. 5. The tested geometry has changed using the evaluation data, so the original frozen prediction and the new branch must both remain recorded.

Next: [capstone](capstone.md) assembles a source-traced comparison using these already practiced operations.
