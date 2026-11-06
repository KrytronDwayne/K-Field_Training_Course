# Lesson 6: Sensitivity and retained numerical closure

Essential question: How can we change one input and preserve every resulting difference?

Goals

- Reevaluate all outputs after a finite input change.
- Retain signed changes and reconstruct every new output.
- Distinguish finite sensitivity from arithmetic closure.

Pacing: 55 minutes — retrieval 5; explanation and worked example 20; guided practice 15; diagnostics and repair 15.

Prerequisite bridge

Lesson 3 supplies all output formulas; lesson 4 supplies signed differences and reconstruction. A finite change compares two complete input triples. We need no derivative or limit. Subtract fractions using a common denominator: 1/2−1/3=3/6−2/6=1/6.

## C08.06-E1 — Two different kinds of difference

Sensitivity here means how the output changes when a specified input changes and the other inputs remain fixed. Keep the original triple, the input-change vector, the full new outputs, and the signed output differences. An input-change vector is simply the ordered list of new-minus-old changes. Zeros matter because they tell us what stayed fixed.

For any quantity y, write Δy=y_new−y_old; Δ is just a label meaning change. The reconstruction rule is y_new=y_old+Δy. This preserves the full finite difference even if a short decimal display hides it. Separately calculate closure c=eta×alpha−10 A_ac/A_ab using the same complete input triple. Sensitivity can be nonzero while c stays zero. One compares two input states; the other compares two algebraic paths within one state.

## C08.06-W1 — Change the ab area

Baseline areas are (12,8,6) U². Change only ab by +1/10 U², so the new triple is (12,8,61/10) U² and the input change is (0,0,1/10) U². Normalize: (1,8/12,(61/10)/12)=(1,2/3,61/120). Evaluate eta=1000×12/(61/10)=120000/61; alpha_inverse=150; alpha=1/150. The product path gives (120000/61)/150=800/61. The direct path gives 10×8/(61/10)=800/61. Closure is zero.

| Output | Old | New | Signed new − old |
|---|---|---|---|
| r_bc | 1 | 1 | 0 |
| r_ac | 2/3 | 2/3 | 0 |
| r_ab | 1/2 | 61/120 | 1/120 |
| eta | 2000 | 120000/61 | −2000/61 |
| alpha_inverse | 150 | 150 | 0 |
| alpha | 1/150 | 1/150 | 0 |
| eta_alpha | 40/3 | 800/61 | −40/183 |

For eta, subtract 2000=122000/61 to obtain −2000/61. For the product, use denominator 183: 800/61−40/3=(2400−2440)/183=−40/183. Reconstruction returns eta=2000−2000/61=120000/61 and product=40/3−40/183=800/61. For the ray’s third component, 1/2+1/120=61/120. Adding zero returns every unchanged entry. All outputs are dimensionless; only the supplied area changes carry U².

> Claim scope: These are supplied synthetic area states, not a measured trajectory or an experiment on Cell3. Exact finite sensitivity and exact arithmetic closure are taught core operations. No approximation is needed, and no difference is discarded.

Guided practice — C08.06-P1

Return to the baseline and instead change only ac from 8 to 81/10 U². Compute every output, difference, and both product paths. **Answer:** input change (0,1/10,0) U²; new ray (1,27/40,1/2). Eta=2000; alpha_inverse=1200/(81/10)=4000/27; alpha=27/4000. Product=2000×27/4000=27/2, also 10×(81/10)/6=27/2. Ray differences are (0,1/120,0); remaining differences in eta, alpha_inverse, alpha, eta_alpha order are 0,−50/27,1/12000,1/6. For example 4000/27−150=(4000−4050)/27=−50/27 and 27/4000−1/150=(81−80)/12000=1/12000. Reconstruct each by adding: 2/3+1/120=27/40; 150−50/27=4000/27; 1/150+1/12000=27/4000; 40/3+1/6=27/2. Unchanged components reconstruct by adding zero.

Diagnostic checks

1. **C08.06-D1** For W1 give the product-path value, direct-path value, closure, and product sensitivity.

2. **C08.06-D2** Why is retaining only the largest output change insufficient?

3. **C08.06-D3** In P1, reconstruct alpha_inverse from its baseline and signed difference.

4. **C08.06-D4** A student calls the W1 product difference −40/183 an algebraic failure. Correct this.

Worked diagnostic answers

1. The two paths are both 800/61; closure is 0; sensitivity relative to baseline is −40/183. They compare different things.

2. It loses the other components, signs, and unchanged coordinates, preventing complete reconstruction. Keep all seven entries and the input change.

3. 150+(−50/27)=(4050−50)/27=4000/27.

4. −40/183 compares the product at two different input triples. Within the new triple both algebraic paths agree exactly, so there is no closure failure.

Next dependency: [capstone](capstone.md). Carry the labeled input triple, divisor, source role, and retained differences forward.
