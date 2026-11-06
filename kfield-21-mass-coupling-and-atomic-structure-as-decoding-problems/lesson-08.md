# lesson-08: A reproducible decoding report

1 sessions of 55 minutes.

**Essential question:** What must a report contain so another reader can reconstruct every result?

**Goals**

- Assemble a ledger separating input, definition, derivation and source status.
- Retain approximation differences independently of channel residuals.
- Reconstruct a report and identify unresolved source obligations.

## Prerequisite bridge

The previous lessons provided all required computations. This final lesson introduces no new physical model. It joins the channel, source, composition, endpoint and history ledgers into a report that a classmate can check.

<a id="C21.08-E1"></a>
## Explanation — C21.08-E1

A reproducible report tells the reader what was supplied, which operation was applied and what remains unresolved. A measured value comes from an actual observation with acquisition provenance. No new empirical measurement is supplied here: y is synthetic. A source coefficient or witness is a number stated by a document and must retain its source and precision. A derived coefficient is the result of a declared calculation. An approximant is a convenient replacement accompanied by its exact difference. A model output is conditional on model inputs and conventions.

For the worked packet, record y=(2,3,6), channel order 1,2,3, the three rows of A_small, field R, Euclidean inner product and dimensionless units. Derived c=(7/3,10/3); represented=(7/3,10/3,17/3); retained r=(-1/3,-1/3,1/3). The normal check is (0,0), but it is not a substitute for r. Reconstruct each entry before making an interpretation.

Suppose you display c1 as 2.33. This is exactly 233/100 as a decimal approximant. The rounding closure is 7/3-233/100=(700-699)/300=1/300. Store that separately. If both coefficients are displayed as (2.33,3.33), the exact-minus-displayed vector is delta c=(1/300,1/300), whose represented-channel difference is A_small delta c=(1/300,1/300,1/150). Then y=A_small c_display+r+A_small delta c. Rounding information and the original syndrome account for different differences.

The source ledger should identify S02 M17’s matrix and stored renderer witnesses, the missing source L and W7, and S05 R029–R032’s application statuses. A source label such as exact_representation_theory remains an attributed status when the action matrices required for fresh replay are absent. The course has independently recomputed the finite examples; it has not loaded every physical definition body.

For the practice packet y=(1,2,3), report c=(1,2), represented=(1,2,3), r=(0,0,0). Add the negative-Q endpoint record from lesson 5 with its neutral complete-object convention, initial 5u, final 5.05u, delta m=-0.05u, stipulated conversion 10 E_unit/u and Q=-0.5 E_unit. Attach the R029 row showing unsupplied atomic coordinates. These separate records do not turn the synthetic channel into an isotope measurement.

> Report scope: Retain observations if any are later supplied, derived transforms, proposed mechanisms, established reference relations and unresolved inputs in separate fields. No outlier deletion, significance-based erasure or replacement of residual fields by scores is part of this course. Preserve source-local definitions and branches rather than harmonizing away their differences.

Before submitting, give a partner only the inputs and rules. Ask them to recompute a row, a signed residual and an endpoint difference. If the result requires guessing a unit, coefficient selection or source status, repair the earliest missing field. A compact report is successful when it is reconstructable, not when it hides the most information.

<a id="C21.08-W1"></a>
## Worked example — C21.08-W1

For the lesson01 packet, put synthetic y in the input field, A in the definition field, 7/3 and 10/3 in exact derived coefficients, and r=(-1/3,-1/3,1/3) in retained information. If displaying 2.33 for 7/3, record exact approximation closure 7/3-233/100=1/300 separately from the channel residual.

<a id="C21.08-P1"></a>
## Guided practice — C21.08-P1

Try the operation before reading the solution. Assemble the practice packet y=(1,2,3), c=(1,2), r=(0,0,0), plus the negative-Q endpoint ledger from lesson05 and the R029/R031/R032 source row. An auditor can reconstruct all channels and energy bookkeeping while seeing which atomic coordinates remain unprovided.

<a id="C21.08-D1"></a>
## Diagnostic checks — C21.08-D1

1. Classify y=(2,3,6), source alpha, 7/3, 2.33 and the toy rendered mass.
2. Compute the approximation closure for 7/3 displayed as 2.33.
3. What is missing from a report containing only c and a residual squared length?
4. What must remain unresolved in the source-traced atomic row?

## Worked answers

1. Synthetic input; source witness; exact derived coefficient; decimal approximant; conditional synthetic model output. None is a newly measured physical value.
2. 7/3-233/100=1/300; retain it separately from r1=-1/3.
3. The signed channel residual and its order/basis, plus any omitted input and decoder conventions. A scalar score cannot reconstruct y.
4. The unsupplied Cell3 address, typed additional fibers, isotope mass, graph data, charge/parity, binding residual, phase tensor and occupied-state rule; source L/W7 replay remains unloaded.

**Boundary to carry forward:** Do not relabel synthetic y as measured data, source alpha as an exact rational constant of nature, solver c as a selected occupied state, or a syndrome score as the complete syndrome. Each is a different report field.

**Next dependency:** [capstone](capstone.md). Use this lesson’s reconstruction and scope checks there.
