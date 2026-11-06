# Lesson 06 — Comparing mechanism classes

Essential question: How can two mechanisms share one calibration yet make different testable predictions?

Goals: Freeze response coefficients with their units; compare signed predictions and residuals; formulate a falsifiable extension with explicit missing bridges.

Prerequisite bridge. Lesson 03 supplied w=v dot n, and Lesson 05 showed that a proposed map must preserve its stated operations. Now compare response rules by what they predict under reversal and scaling. All numbers below are synthetic teaching cases; U is a declared response unit, not an identified physical energy or force.

Pacing: two 55-minute periods, each with 5 retrieval, 20 instruction/example, 15 practice, 15 diagnostics. Period 1 calibrates and freezes inputs; period 2 uses held cases, residual reconstruction and a proposal.

## C23.06-E1 — A sufficient mechanism has a stated scope

A mechanism class is a family of rules specifying how inputs produce outputs. Sufficiency always names a target: reproducing these finite response cases is a smaller task than explaining gravity, binding and exceptional actions together. Compare rules on the same input ledger. State independent inputs, units, fitted parameters, invariant patterns and predictions for cases not used to choose parameters.

Consider H1: z=k w and H2: z=b w^2, where w has units LU/T. To produce z in U, k must have units U*T/LU, while b must have U*T^2/LU^2. In H1, reversing w reverses z (an odd response). In H2, reversing w leaves z fixed (an even response). Doubling w doubles H1's response and quadruples H2's. These are consequences of the formulas, not additional observations.

Calibration means using one declared case to determine a parameter. A held case is one not used for that choice. Freeze the parameter before predicting held cases. For each case compute r=z_input-z_prediction, and keep the ordered tuple (w,z_input,z_prediction,r), with units and orientation. Reconstruction is z_input=z_prediction+r. A residual is the next unresolved coordinate of the response description; replacing it by a single score destroys the signed case structure.

## C23.06-W1 — Worked calibration and discrimination

Use synthetic calibration w=1 LU/T and z=2 U. H1 requires k=z/w=2 U*T/LU. H2 requires b=z/w^2=2 U*T^2/LU^2. Freeze both. For w=-1 LU/T, H1 predicts -2 U and H2 +2 U. For w=2 LU/T, H1 predicts 4 U and H2 8 U. Both exactly match the calibration but the reversal and doubling predictions differ. Equal performance on one case does not supply the missing rule between cases.

## C23.06-P1 — Practice and full answer

The synthetic held input list is w=(-1,2) LU/T with z=(-2,5) U. Build both residual lists without changing k or b. Then specify a new orientation test for H1.

| w (LU/T) | Input z (U) | H1 prediction (U) | H1 residual (U) | H2 prediction (U) | H2 residual (U) |
|---:|---:|---:|---:|---:|---:|
| -1 | -2 | -2 | 0 | 2 | -4 |
| 2 | 5 | 4 | 1 | 8 | -3 |

For instance, the last H2 residual is 5-8=-3 U; reconstruction is 8+(-3)=5 U. Neither bare rule exactly reproduces the full held list. H1 plus its residual field reproduces it, as does H2 plus its different residual field. Those decompositions preserve information but do not yet explain the residuals.

A falsifiable extension proposal is: keep k=2 fixed and predict z=2(v dot n) in new, explicitly recorded orientations, with odd reversal under n to -n. Hold v=(1,0,0) LU/T fixed; use n=(1,0,0), (-1,0,0), (0,1,0). The predictions are +2,-2,0 U. These normals are unit length and give w=+1,-1,0. Record every returned z with orientation and a common protocol; any nonzero residual contradicts exact agreement for that case under the stated exact-input model. In a measured application, also preserve instrument resolution and input variation rather than erasing them. No new readings are claimed here.

One specified extension to investigate after a failed orientation test is z=k w+c n_y, where n_y is the normal's second coordinate and c has units U. This is a proposal, not a fitted conclusion: collect a separate calibration to set c, freeze it, then test additional orientations. It remains odd under simultaneous normal reversal and predicts +c U at n=(0,1,0) when c is expressed numerically in U. Retain the old predictions and residuals as well as the extension's. A different possible extension may depend on speed or history; distinguish it rather than silently adding freedom after each held case.

> Claim scope. These rules are sufficient algorithms for conditional predictions from w and fixed coefficients. Neither is an established source force law or a complete explanation of mass reconstruction, binding, or a cycle-sector action. Their comparison exposes necessary inputs and discriminating invariants; unifying those other domains requires explicit shared variables and maps.

## Diagnostics and worked answers

1. **C23.06-D1:** Why not choose k=5/2 on the w=2 held case and call it a successful prediction? Answer: that uses the held output to fit k, changing the model after its prediction. It can be a new calibration, explicitly labeled, but is not the original forward test.
2. What survives reversing w under H2? Answer: w^2 and predicted z survive. The sign of w must nevertheless remain in the input ledger.
3. Can the H1 residual +1 at w=2 be deleted because one case fits exactly? Answer: no. Preserve both cases; the +1 is unresolved structure and is needed to reconstruct 5 from 4.
4. What would connect H1 to the scalar lift? Answer: a specified map from source-defined scalar variables and typed physical inputs to k or z, plus its domain and independent predictions. Matching names or fitted numbers does not provide it.

Next dependency: [Lesson 07](lesson-07.md) combines these conditional mechanisms with exact identities and open branches in one atlas.
