# Lesson 01 — Scalar lifts and reconstructed shape

Essential question: How can three scalar summaries recover three face-area coordinates without creating a fourth independent shape variable?

Goals: Compute the forward scalar map; recover its three inputs; distinguish an inferred coordinate formula from a missing archival definition.

Prerequisite bridge. You need signed arithmetic, substitution into linear equations, and ratios. The earlier courses provide geometric motivation, but all operations assessed here are taught below. A face area is a positive number with units of length squared. Three differently oriented faces carry labels ab, ac, bc; these are labels, not multiplications in the subscript.

Pacing: two 55-minute periods. Period 1 covers ratios, logarithms and the forward map; period 2 covers recovery and source status. In each: 5 minutes retrieval, 20 explanation/example, 15 practice, 15 diagnostics and repair.

## C23.01-E1 — Teach the coordinates before the lift

A ratio compares quantities of the same kind. Choose a positive reference area A_ref in the same units as every area. Then A_ab/A_ref is dimensionless: changing both from square metres to square centimetres does not change the ratio. Define the classroom coordinate y_ab=ln(A_ab/A_ref), and similarly y_ac and y_bc. The natural logarithm ln reverses the exponential e^y: ln(e^y)=y. Thus y=0 means area A_ref, y=1 means e times A_ref, and a negative y means a smaller positive area. No logarithm of a zero or negative area is allowed. We use given y values, so numerical logarithm tables are unnecessary.

Two useful rules are ln(uv)=ln u+ln v and ln(u/v)=ln u-ln v for positive u,v. They say that multiplication of areas by the same positive factor changes every y by the same additive amount t. Recovery of the areas is A_ab=A_ref e^(y_ab), and likewise for the other faces. Keep A_ref: without it the absolute areas are not recoverable.

S02, /backbone_sequence/18/branches/gravity_scalar_lift, supplies G_Gamma=9y_ab+8y_ac-11y_bc and three inverse equations. In this lesson abbreviate G_Gamma as G; it is a dimensionless scalar, not a metric or a force. The inverse equations are

    y_ab=(G-8F+3M)/6
    y_ac=(G-2F+9M)/6
    y_bc=(G-8F+9M)/6.

Subtract the third equation from the second: y_ac-y_bc=6F/6=F. Subtract the first from the third: y_bc-y_ab=6M/6=M. These two formulas are algebraically inferred coordinates. They are not recovered archival definition bodies for F and M. Here M is a dimensionless scalar; later M_cell is a matrix and mass is written mu.

Why does the inverse work? Put u=y_ab, v=y_ac, w=y_bc. Substituting G=9u+8v-11w, F=v-w, M=w-u into the first numerator gives 9u+8v-11w-8v+8w+3w-3u=6u. The other numerators reduce to 6v and 6w. Division by 6 therefore recovers each coordinate for every real u,v,w. A determinant, a test number for whether a square linear map is reversible, is +6 for the forward map ordered (F,M,G); the substitution proof already establishes reversibility without requiring determinant computation.

The source also writes d ln Gamma2=9 d ln A_ab+8 d ln A_ac-11 d ln A_bc. Here d indicates an infinitesimal change; calculus is recognition only. A change equation does not supply a starting value. For this classroom convention, a corresponding finite relation would have ln(Gamma2/Gamma_ref)=G+C with an explicitly supplied reference and constant C. The course does not assign their archival values. S03 /findings/8 (AUD-009) identifies the F, M and Gamma2 bodies as missing replay objects with status VERIFIED_NOT_LOADED.

## C23.01-W1 — Worked reconstruction

Use the synthetic ordered triple (y_ab,y_ac,y_bc)=(0,2,3). Compute F=2-3=-1, M=3-0=3 and G=9(0)+8(2)-11(3)=-17. Recover y_ab=(-17+8+9)/6=0, y_ac=(-17+2+27)/6=2 and y_bc=(-17+8+27)/6=3. All three signed coordinates return exactly. If the original areas are needed, return (A_ref,A_ref e^2,A_ref e^3), retaining the reference.

There were three inputs and there are three independent summaries (F,M,G). Appending G to F and M completes this coordinate description; it does not create a fourth independent input.

## C23.01-P1 — Practice, then check

Take y=(1,0,2). Find F,M,G, recover y, and determine what happens when every y increases by t. Work before reading the answer.

Answer: F=-2, M=1, G=9-22=-13. Recovery gives (-13+16+3)/6=1, (-13+4+9)/6=0, (-13+16+9)/6=2. In each difference the two copies of t cancel, so F and M stay fixed. G changes by (9+8-11)t=6t. This is scale sensitivity. Save t as well as the original reference when changing conventions.

> Claim scope. The five source formulas are archival source facts. Their finite algebra is freshly checkable under our declared logarithm convention. The original F/M/Gamma2 definitions and integration constants remain VERIFIED_NOT_LOADED. Neither this calculation nor its scalar title supplies a force law or a measured gravitational response.

## Diagnostics and worked answers

1. **C23.01-D1:** Why is ln(5 square metres) incomplete here? Answer: its input carries units; choose A_ref and take ln(A/A_ref). With A_ref=5 square metres the coordinate is ln 1=0.
2. If y=(t,t,t), what are F,M,G? Answer: F=M=0 and G=6t. Shape differences vanish while common scale remains.
3. Does the source differential equation fix Gamma2 absolutely? Answer: no; a reference value or integration constant and the definition body are needed. Do not replace them with an invented value.
4. Is G an extra independent shape coordinate after all three y values are supplied? Answer: no; its value follows by substitution. The inverse shows exactly which information the three summaries retain.

Next dependency: [Lesson 02](lesson-02.md) carries this habit of reversible, domain-declared reconstruction into reciprocal geometry.
