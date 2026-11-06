"""Authored course sections; run only to reproduce these drafts, not to overwrite audited repairs."""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parent
P=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(name,text): (ROOT/name).write_text(text.strip()+'\n',encoding='utf-8')
lessons={
1:r'''# Lesson 01 — Scalar lifts and reconstructed shape

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
''',
2:r'''# Lesson 02 — Reciprocal inversion identities

Essential question: What must be retained to reconstruct a reciprocal direction, spacing and address?

Goals: Compute a reciprocal vector and its metric length; invert a conditional Bragg relation with its allowed angles; reconstruct a signed residual without losing components.

Prerequisite bridge. Lesson 01 taught reversible summaries and positive dimensionless logarithm ratios. Here a vector is an ordered list of three signed components. Multiplying vectors in the dot product means multiplying corresponding entries and adding: (a,b,c) dot (u,v,w)=au+bv+cw. A vector's Euclidean length is the nonnegative square root of its dot product with itself. A square root undoes squaring; sqrt(13)^2=13.

Pacing: three 55-minute periods, each with 5 retrieval, 20 instruction/example, 15 practice and 15 checks. Periods cover basis/metric, Bragg/angle branches, then residual and scale reconstruction.

## C23.02-E1 — Basis, reciprocal and metric

Let LU denote an arbitrary length unit. Our synthetic basis has columns a=(2,0,0), b=(0,3,0), c=(0,0,4) LU. The matrix B=diag(2,3,4) LU is shorthand for the array with these entries on its diagonal and zeros elsewhere. Multiplication B u scales the components of a dimensionless address u separately. Its inverse B^-1 divides them by 2,3,4. A transpose B^T exchanges rows and columns; a diagonal matrix is unchanged. B^-T means the transpose of B^-1. A basis is nonsingular when it has a unique inverse; this diagonal example qualifies because none of 2,3,4 is zero.

For a physical position x with declared origin O_K, u=B^-1(x-O_K), and x=O_K+B u. Subtract the origin first. The reciprocal columns a*,b*,c* are (1/2,0,0),(0,1/3,0),(0,0,1/4) LU^-1. They extract address components: a* dot (x-O_K)=u_1. For example, O_K=(1,1,1) LU and x=(3,4,5) LU give displacement (2,3,4) LU and address (1,1,1). Using x directly would give the wrong address (3/2,4/3,5/4).

The Gram metric M_cell=B^T B records dot products of the basis columns. In this synthetic analogue M_cell=diag(4,9,16) LU^2, and R_cell=M_cell^-1=diag(1/4,1/9,1/16) LU^-2. For an integer triple h (a plane address), define q=B^-T h. Then B^T q=h and

    q dot q = h^T R_cell h.

For this diagonal example the right side is h_1^2/4+h_2^2/9+h_3^2/16. This metric expression is just the same three squares computed from the address. In general the identity follows because q^T q=h^T B^-1 B^-T h, and B^-1 B^-T=(B^T B)^-1. The diagonal calculations are the assessed operation; general matrix inversion is not required.

For nonzero q, define d=1/length(q), a positive spacing in LU, and n_hat=q/length(q), a dimensionless unit normal. Then q=n_hat/d. Keep the signs of n_hat: d alone does not retain orientation. If q=0 there is no unit direction or finite d by this rule.

The source reciprocal branch (S02 /backbone_sequence/18/branches/reciprocal_plane_inversion) also supplies 2d sin(theta)=m lambda_wave. For the positive-sine angle convention and positive integer order m and wavelength lambda_wave, solve by dividing: d=m lambda_wave/(2 sin(theta)). The source absolute-value form extends the positive spacing convention to other angle branches; the original signed equation and its orientation must still be retained. Never divide by zero. Sine is the vertical coordinate of a unit-circle direction; the provided values sin(30 degrees)=sin(150 degrees)=1/2 suffice here. Angles theta and 180 degrees-theta have the same sine but distinct directions.

Using a common positive length reference L_ref, write Gamma_B=ln(d/L_ref)+ln|sin(theta)|-ln(lambda_wave/L_ref). Combine logarithms to get ln(d|sin(theta)|/lambda_wave)=ln(m/2). Gamma_B is dimensionless. It is distinct from Gamma2, G_Gamma and any metric. If adjacent linear scales satisfy d_next=3d, then ln(d_next/L_ref)-ln(d/L_ref)=ln 3. This does not declare that every signed reciprocal scale uses the same exponent: record whether q has 3^(+g) or 3^(-g).

## C23.02-W1 — Worked reconstruction

For h=(1,1,0), q=(1/2,1/3,0) LU^-1. Its squared length is 1/4+1/9=13/36 LU^-2. Thus length(q)=sqrt(13)/6 LU^-1, d=6/sqrt(13) LU and n_hat=(3,2,0)/sqrt(13). Check n_hat dot n_hat=(9+4)/13=1; dividing n_hat by d returns q. Also B^T q=(1,1,0). The metric gives the same 13/36.

In a **separate synthetic Bragg example**, m=2, lambda_wave=2 LU and sin(theta)=1/2 give d=4 LU. Both 30 and 150 degrees satisfy this spacing, with Gamma_B=ln(2/2)=0. This d does not belong to the preceding q: each reconstruction must use its own input packet.

## C23.02-P1 — Practice and answer

First set h=(0,0,1) using the same B. Then solve a separate Bragg example with m=1, lambda_wave=3 LU, sin(theta)=1/2. Finally use h=(1,1,0), g=0 and reciprocal residual rho=(1/10,-1/5,0) LU^-1 to reconstruct q_observed=3^g B^-T h+rho.

Answers: q=(0,0,1/4) LU^-1, squared length=1/16 LU^-2, d=4 LU and n_hat=(0,0,1). The Bragg spacing is 3 LU and Gamma_B=ln(1/2). In the residual case 3^0=1, so q_observed=(1/2+1/10,1/3-1/5,0)=(3/5,2/15,0) LU^-1. Subtract the prediction to recover rho exactly. Its negative second component is information, not a rounding instruction. The observed squared length is 9/25+4/225=17/45 LU^-2, giving d_observed=sqrt(45/17) LU; its normal must be calculated from that observed vector, not borrowed from W1.

> Claim scope. B here is a synthetic positive-determinant diagonal teaching basis, not the mature locked Cell3 numerical geometry. Actual Cell3 uses ICRS columns [a b c], intentional negative determinant and half-open address cells [-1/2,1/2)^3. Its origin and metric must be retained. This lesson changes none of those constants. M_cell and R_cell are not G_phase, G_eff, distance Q, Q_g or Q_nu. Bragg numbers here are conditional teaching inputs, not measured events.

## Diagnostics and worked answers

1. **C23.02-D1:** Can positive m lambda_wave and sin(theta)=0 give finite d? Answer: no, the original left side is zero and the right side positive. The inversion excludes that input.
2. What if B=diag(2,3,0)? Answer: its third address cannot be recovered from B u; the inverse does not exist. Zero q is a separate excluded case even for nonsingular B.
3. Why retain rho as three signed entries? Answer: q_observed=prediction+rho reconstructs every component; length(rho) alone cannot recover its direction or signs.
4. If d changes from 2 LU to 6 LU, find the log difference. Answer: ln(6/L_ref)-ln(2/L_ref)=ln 3 with a common LU-valued reference. A different reference in each term would contaminate the comparison.
5. Does knowing d select 30 rather than 150 degrees in W1? Answer: no, both sines are 1/2. Store the angle branch and normal orientation as well as spacing.

Next dependency: [Lesson 03](lesson-03.md) uses the unit normal for signed motion components.
''',
3:r'''# Lesson 03 — Geometry and proposed inertial response

Essential question: Which additional inputs turn a direction-dependent motion calculation into a force prediction?

Goals: Compute signed directional velocity and acceleration; retain perpendicular components for reconstruction; identify the law and coefficient needed for a force.

Prerequisite bridge. Lesson 02 defined dot products, vector length and unit normals. Use LU for length, T for time and MU for mass. Velocity v gives change of position per time, in LU/T; acceleration a gives change of velocity per time, in LU/T^2. A negative component means motion or change opposite to the chosen positive axis, not a negative magnitude.

Pacing: one 55-minute period: 5 retrieval, 20 instruction/example, 15 practice, 15 diagnostics and repair.

## C23.03-E1 — Preserve a direction and its complement

For a dimensionless unit normal n, the scalar v_parallel=v dot n tells how much velocity points along that orientation. Multiply it by n to obtain the parallel **vector**. The perpendicular vector is v_perp=v-(v dot n)n. Their sum returns v. The dot product of the perpendicular part with n is zero because n dot n=1. This is a reversible description if both pieces are kept. The same decomposition applies to a.

Reverse the normal by replacing n with -n. The scalar projections change signs because each product changes sign. Their squares stay fixed. The parallel vector does not change: its scalar and its normal both reverse. This distinction matters when comparing signed measurements with orientation-independent costs.

Geometry tells us these projections; it does not supply a mass or a force coefficient. A constitutive equation is an additional response rule connecting specified inputs and outputs. For example, propose F_parallel=mu a_parallel with mu in MU. Then F_parallel has units MU*LU/T^2. This is a conditional model computation. The familiar constant-mass Newtonian relation between net force and acceleration is a reference-theory example of such a rule; this exercise does not derive it from the scalar lift. A full prediction of motion would also need starting position/velocity and the applicable forces or boundary conditions. Nothing in the dimensionless F of Lesson 01 makes it this F_parallel.

## C23.03-W1 — Worked signed projection

Let n=(0,0,1), v=(1,2,3) LU/T, and a=(0,0,-2) LU/T^2. Then v_parallel=1(0)+2(0)+3(1)=3 LU/T and a_parallel=-2 LU/T^2. The retained velocity complement is v_perp=(1,2,0) LU/T; 3n+v_perp=(1,2,3). The acceleration complement is zero. Reversing n gives scalar values -3 and +2, while squared values stay 9 LU^2/T^2 and 4 LU^2/T^4. No coefficient mu was supplied, so there is no numerical force prediction.

## C23.03-P1 — Practice and answer

For n=(3/5,4/5,0), v=(5,0,0) LU/T and a=(0,5,0) LU/T^2, verify the normal, calculate both projections, retain complements, and then use the explicitly proposed mu=2 MU response law above.

Answer: n dot n=9/25+16/25=1. Projections are 3 LU/T and 4 LU/T^2. Parallel velocity is (9/5,12/5,0); subtracting from v leaves (16/5,-12/5,0) LU/T. Parallel acceleration is (12/5,16/5,0), leaving (-12/5,9/5,0) LU/T^2. Adding each pair returns its input. The conditional force scalar is 2*4=8 MU*LU/T^2. Its parallel vector would be (24/5,32/5,0) in those force units. The geometry alone does not determine a perpendicular force.

> Claim scope. These are synthetic kinematic inputs and an explicitly added response law. They illustrate how to keep a mechanism's premises visible alongside M19 scalar and reciprocal branches. No observation of gravitational or inertial response is supplied here. A photon-equivalent model energy would also require its own definition; it is not measured transferred energy. Phase is not force.

## Diagnostics and worked answers

1. **C23.03-D1:** Can the dimensionless G of Lesson 01 be relabeled as a force? Answer: not without a declared conversion with units and a response law. Its scalar identity supplies neither.
2. What goes wrong if n=(0,0,2) is used as a unit normal? Answer: n dot n=4, and v dot n doubles the intended signed projection. Normalize first: n/length(n)=(0,0,1).
3. Does reversing n reverse the parallel velocity vector? Answer: no, (-v_parallel)(-n)=v_parallel n. It reverses the signed scalar label.
4. If a synthetic force reading is 9 rather than the predicted 8, what is retained? Answer: observed 9, predicted 8 and residual +1 MU*LU/T^2, together with n, mu, a and the law. Their sum reconstructs the reading; do not erase the discrepancy or call it a new measured law.

Next dependency: [Lesson 04](lesson-04.md) applies the same discipline—compute what inputs justify, then name the remaining structure—to finite cycle counts.
''',
6:r'''# Lesson 06 — Comparing mechanism classes

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
''',
7:r'''# Lesson 07 — A map of exact and open branches

Essential question: How can an atlas preserve a source's constructions and every boundary on their use?

Goals: Classify each branch by its actual evidence; attach inputs, units and boundaries to a reconstruction; assemble a proposal without promoting missing definitions into supplied facts.

Prerequisite bridge. Lessons 01–06 supplied scalar and reciprocal reconstructions, directional motion, finite counts, small maps and a frozen response comparison. An atlas is a structured index of these results and their dependencies. It makes the next needed definition, map or measurement visible.

Pacing: one 55-minute period: 5 retrieval, 20 instruction/example, 15 practice, 15 diagnostics and repair.

## C23.07-E1 — Store claims with their contracts

Use six evidence layers. A source fact says what a pinned document records. A derived implication follows by explicit calculation from stated inputs. An inferred structure proposes an interpretation of recurring relationships. A proposed mechanism adds a response rule. Reference theory supplies separately identified mathematical or physical results. An unresolved question names a missing definition, proof body, map or test. A row may have a source claim and a separate local verification column; never force them into one status.

M19 is typed D+E in S02 /backbone_sequence/18 and requires M07,M08,M10,M13,M18. This is the mathematical-backbone namespace. S03 AUD-001 (/findings/0) removes the serialized M19-to-M20 edge: M20 closes the M01–M18 core. Our sequential teaching order is not a claim that every lesson is an archival module dependency. Compiler modules with the same labels belong to a different ledger and cannot silently lend authority to backbone M19.

The atlas needs columns for claim, pointer or synthetic definition, domain/units, retained inputs/output, local verification and next obligation. Keep the supplied evidence contract: a missing body is VERIFIED_NOT_LOADED, not a manufactured proof or a new rejection of the archived claim. Similarly, a null endpoint boundary is an empty field, not permission to remove known constituent restrictions (S03 AUD-010, /findings/9). S03 AUD-011 (/findings/10) also requires a full premise contract rather than attributing all results to Cell3 alone.

## C23.07-W1 — Worked branch atlas

| Branch and provenance | Domain and retained information | Verified here | Remaining obligation |
|---|---|---|---|
| Scalar lift; S02 M19 gravity_scalar_lift | Positive area ratios, A_ref, all three signed y and inferred F,M,G | Finite forward/inverse substitution, lesson 01 | F/M/Gamma2 definition bodies and reference constants, S03 AUD-009 |
| Reciprocal inversion; S02 M19 reciprocal_plane_inversion | Nonsingular B, O_K, nonzero q; B, h, units, scale sign, orientation and rho | Synthetic metric and vector reconstruction, lesson 02 | Load locked geometry for a physical application; retain angle branches |
| Bragg inversion; same pointer | Positive m and wavelength, nonzero sine, common length reference | Conditional arithmetic and logarithm identity | Measured inputs and applicability of the response model |
| Open/periodic cycles; S02 M19 exceptional_cycle_bridge | Declared finite edge convention and all vertices/edges | Counts 28 and 55 | Explicit map selecting the named 52-cycle sector |
| Cohomology and exceptional carriers; same pointer | Source theorem contracts, not physical force units | 3^6=729 given the stated dimension 6 | Proof bodies not replayed; no inferred action from a count |
| Exceptional action extension; same pointer | Specified field, basis, operators, bracket and representation domain | Small illustrative intertwiner only, lesson 05 | Specific F4 action, E6/E7 real forms and physical cohomology coupling |
| Synthetic H1/H2; lesson 06 definitions | w,z, coefficient units, orientation, frozen calibration | Entire signed prediction/residual table | New held-orientation test and source-to-response map |

The source calls the scalar lift, reciprocal identities, counts and exceptional carriers exact. The atlas preserves that reported result while identifying precisely which finite parts this course replays. It does not turn theorem names into proof bodies. The gravity title motivates a mechanism question; no force law is smuggled into the algebra.

## C23.07-P1 — Practice and worked atlas entries

Build three rows from earlier practice: reciprocal address, mechanism comparison and extension proposal. Add the source boundary that must survive a null endpoint.

Answer row 1: use lesson 02 synthetic B=diag(2,3,4) LU, h=(1,1,0), g=0, rho=(1/10,-1/5,0) LU^-1. q_observed=(3/5,2/15,0) LU^-1 and q_observed-rho=(1/2,1/3,0). Its source pattern is S02 M19 reciprocal_plane_inversion, while these numerical inputs are synthetic. Retain B, exponent sign, h and rho; next obligation is an actual locked-basis/input packet for a physical interpretation.

Answer row 2: use lesson 06's calibration w=1,z=2 with k=2 U*T/LU and b=2 U*T^2/LU^2. Keep both held cases: (-1,-2,-2,0,2,-4) and (2,5,4,1,8,-3), ordered as w,z,H1 prediction,H1 residual,H2 prediction,H2 residual. w has LU/T and all remaining entries U. The definition is synthetic, and the next obligation is to account for residual coordinates without deleting either case.

Answer row 3: retain the frozen k and the normals (1,0,0),(-1,0,0),(0,1,0) with fixed v=(1,0,0) LU/T. Predicted responses are +2,-2,0 U. State the exact odd-reversal rule, preserve future readings and each signed residual, and identify c n_y as an explicitly proposed extension requiring separate calibration and held tests. No observed results are filled in.

Boundary answer: even if an atlas endpoint is null, the missing specific exceptional action and the missing F/M/Gamma2 definition bodies remain attached. Propagate restrictions from constituent rows; S03 AUD-010 requires this preservation.

> Claim scope. This atlas is a finite educational reconstruction and a source-status ledger. It preserves both archived claims and missing replay obligations. It supplies no invented physical data, source constants or 52-by-52 action.

## Diagnostics and worked answers

1. **C23.07-D1:** Can a source theorem card be marked freshly proved because its file hash matches? Answer: no. The hash establishes byte identity; the theorem's proof requires a separate replay. Keep both facts.
2. Is M19 a premise of M20 core closure? Answer: no under S03 AUD-001. Record M19's own requires list separately from the M01–M18 closure.
3. Does an endpoint value null override a nonempty constituent boundary? Answer: no. Propagate the constituent limitation and record the endpoint defect.
4. What makes the proposed orientation experiment falsifiable? Answer: fixed inputs and k give signed predictions before new readings. Any discrepancy is retained and localized by orientation; changing k after seeing it must be labeled a new model.

Next dependency: [Capstone](capstone.md) asks you to assemble the already practiced rows into a complete branch atlas with calculations and a test proposal.
'''
}
for n,body in lessons.items(): write(f'lesson-{n:02}.md',body)
print('Authored lessons',list(lessons))
