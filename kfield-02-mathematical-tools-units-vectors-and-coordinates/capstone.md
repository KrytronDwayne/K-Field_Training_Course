# Capstone — Design and verify a coordinate converter

Allow two 55-minute periods: one to design and calculate, one to test, explain, and repair. Everything below uses synthetic inputs. Your deliverable is a converter specification, a worked test record, and reconstruction evidence. No programming or physical experiment is required.

## Design brief

A fictional drawing system uses perpendicular background axes (x,y), positive x right and positive y up. Its local origin is O = (100,-20) cm. The first ordered basis arrow is b1 = (2,1) cm and the second is b2 = (1,-1) cm, each per one dimensionless local coefficient. The system receives q = (5/4,-3/4). A fictional scanner repeats once every 25 ms. A comparison model enlarges all lengths by a factor of 3, including the height of a rectangular box.

Write a specification that another student can use without guessing. You may choose your own display precision and tie rule if you state them and test both positive and negative ties; for direct comparison with the key, use nearest tenth, ties away from zero. Preserve exact inputs, displayed values, and signed residuals. Work in centimetres first, then provide requested metre conversions. Keep matrix columns in the given order even though their determinant is negative.

## Required tasks and test cases

1. **Contract and units (8 points).** State axes, ordering, types, origin, basis matrix, coefficient units, exact arithmetic policy, and rounding rule. Convert O, b1, b2 to metres, 25 ms to seconds, and the repeat frequency to Hz and kHz.
2. **Scale (4 points).** Determine how length, area, and volume change under factor 3. Apply this to a separate 2-by-3-by-4 cm box. Explain why changing cm to m is not a physical enlargement.
3. **Forward conversion and position (6 points).** Calculate v = Bq, its magnitude, and P = O+v. Give P in cm and m. Show that P and v have different meanings.
4. **Orientation and inverse (8 points).** Calculate D, physical unit-square area, and orientation. Derive or state the taught inverse with units. Recover q from your P and show both forward and reverse reconstruction. Test a second point P2 = (103,-20) cm. Give a singular alternative matrix and two inputs that it fails to distinguish.
5. **Projection (6 points).** Use the dimensionless direction d = (2,0). Calculate its magnitude, unit direction, the scalar projection of v along it, the vector projection p, and perpendicular residual r. Verify v = p+r and r·d = 0. Give cos(theta) and sin(theta) for the angle from positive x to v, then check the components by multiplying by |v|.
6. **Rounding and restoration (8 points).** Display q using your chosen rule. Preserve e = q-q_hat and calculate Be. Compute the display-only point and restore P. Explain why neither the magnitude |e| nor the display alone reconstructs q. Include one positive and one negative exact tie in your test record.

The total is 40 points. A response that gives only numerical answers is incomplete: include enough equations, units, and definitions to reproduce each step.

## Full worked answer key

### 1. Contract and units

Use ordered (x,y) background coordinates, perpendicular and equally scaled; points P and O are locations, v is a directed displacement, and q is a dimensionless coefficient pair. B = [[2,1],[1,-1]] cm means columns b1 then b2. The forward rule is P = O+Bq; the reverse rule is q = B^-1(P-O) after confirming nonzero determinant. Keep fractions internally and display tenths with ties away from zero.

O = (1,-0.2) m; b1 = (0.02,0.01) m; b2 = (0.01,-0.01) m. T = 25/1000 s = 0.025 s, so f = 1/0.025 = 40 Hz = 0.040 kHz. Multiplying 40 cycles/s by 0.025 s/cycle gives one.

### 2. Scale

The length factor is 3, area factor 9, and volume factor 27. The box becomes 6 by 9 by 12 cm. Its 2-by-3 face changes from 6 to 54 cm², and volume from 24 to 648 cm³. Conversion to metres changes the numerical descriptions of those same lengths; enlargement creates different physical lengths in the synthetic model.

### 3. Forward conversion

v = (2×5/4+1×(-3/4), 1×5/4-1×(-3/4)) cm = (7/4,2) cm. Its magnitude is sqrt((7/4)²+2²) cm = sqrt(113)/4 cm. Retain this exact square-root form. P = (100,-20)+(7/4,2) = (407/4,-18) cm = (101.75,-18) cm = (1.0175,-0.18) m. P describes a location in the background grid, whereas v is measured from O to P.

### 4. Orientation and recovery

D = 2×(-1)-1×1 = -3 cm². The unit-coordinate-square image has area 3 cm² and negative orientation. In metre units, D = -0.0003 m², giving the same physical area. B^-1 = (1/(-3)) [[-1,-1],[-1,2]] cm^-1 = [[1/3,1/3],[1/3,-2/3]] cm^-1.

Subtract O from P to obtain (7/4,2) cm. Then q1 = (1/3)(7/4)+(1/3)2 = 7/12+8/12 = 5/4. Also q2 = (1/3)(7/4)-(2/3)2 = 7/12-16/12 = -3/4. Reapplying B gives (7/4,2) cm and adding O gives P. Conversely, starting from q and applying forward then reverse returns q. The two directions test the offset as well as the matrix.

For P2, the displacement is (3,0) cm. The inverse gives q2_test = (1,1); B(1,1) = (3,0) cm and O+B(1,1) = P2. Here q2_test names the whole second test pair, not the second component of the original q.

A singular alternative is S = [[1,2],[2,4]] cm. det(S) = 0 cm² and S(2,0) = S(0,1) = (2,4) cm. Those distinct inputs establish failure of unique recovery. Merely changing a determinant sign would not create this loss.

### 5. Projection and trigonometric check

|d| = 2 and u = (1,0). The scalar projection is (v·d)/|d| = ((7/4)2+2×0)/2 = 7/4 cm. The vector projection is p = (7/4,0) cm. The retained residual is r = (0,2) cm. Their sum is v and r·d = 0.

The vector lies in the first quadrant. Its adjacent leg is 7/4 cm, opposite leg 2 cm, and hypotenuse sqrt(113)/4 cm. Thus cos(theta) = 7/sqrt(113) and sin(theta) = 8/sqrt(113). Multiplying each by sqrt(113)/4 cm gives 7/4 cm and 2 cm. Their squared ratios add to (49+64)/113 = 1. Using v·d alone would yield 7/2 cm, which is twice the scalar projection.

### 6. Rounding and restoration

Using the key's rule, q_hat = (1.3,-0.8); both entries are halfway cases, one positive and one negative. The residual is e = (1.25-1.3,-0.75-(-0.8)) = (-0.05,0.05) = (-1/20,1/20). Therefore Be = (2(-1/20)+1/20, -1/20-1/20) cm = (-1/20,-1/10) cm.

The display-only displacement is Bq_hat = (1.8,2.1) cm, giving P_hat = (101.8,-17.9) cm. Restore: P_hat+Be = (101.75,-18) cm = P. Restore coefficients: q_hat+e = (1.25,-0.75). The magnitude |e| erases component directions and signs. The display alone corresponds to many possible exact values; retaining the original or its exact residual is necessary. An alternative declared rule earns full credit if its displayed values, signed residuals, and reconstruction are internally consistent.

## Point rubric and repair criteria

| Task | Points | Observable evidence |
|---|---:|---|
| Contract and units | 8 | 4 for complete axes/type/origin/column/unit/rounding specification; 2 for spatial conversions; 2 for period and frequency conversions |
| Scale | 4 | 2 for s, s², s³; 1 for box calculations; 1 for size-versus-unit distinction |
| Forward conversion | 6 | 2 for v; 1 for exact magnitude; 2 for P in both units; 1 for point/displacement distinction |
| Orientation and inverse | 8 | 2 for determinant/area/sign; 2 for inverse with units; 2 for both reconstruction tests; 2 for singular counterexample |
| Projection | 6 | 1 for normalization; 2 for scalar/vector distinction; 1 for residual/perpendicularity; 2 for sine/cosine and component checks |
| Rounding | 8 | 2 for rule and both ties; 2 for e; 2 for Be and restored P; 2 for reconstruction explanation |

Award method credit for a later consistent calculation based on an earlier arithmetic slip, but require correction before declaring the converter verified. Missing origin subtraction, an unnormalized direction, division by zero, loss of residual components, or an undeclared order change requires repair regardless of total points. Mastery means every required operation is demonstrated correctly after feedback, not merely reaching a numerical score.

## Coverage and evidence scope

| Operation | Prior introduction | Prior practice |
|---|---|---|
| Units and frequency | Lesson 01 | Scanner example and diagnostics 1–3 |
| Scale | Lesson 02 | Box and stretched rectangle |
| Origin, displacement, magnitude | Lesson 03 | Shifted-origin example |
| Sine/cosine and projection | Lesson 04 | Axis and tilted-direction examples |
| Ordered basis conversion | Lesson 05 | Forward/substitution recovery |
| Determinant and inverse | Lesson 06 | Negative determinant and singular examples |
| Contract, rounding, residuals | Lesson 07 | Exact versus displayed reconstruction |

Inputs are invented classroom quantities. Results are derived reference mathematics. No observed physical dataset, inferred mechanism, or experimental claim is asserted. Source convention context is documented in sources.md; source labels do not certify these synthetic calculations. The exact inputs and both kinds of residual are retained in this answer record.

