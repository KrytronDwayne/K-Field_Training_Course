# Terminology and notation

| Term or symbol | Meaning and units in this course | First use |
|---|---|---|
| Quantity; dimension | Number with unit; kind such as length L or time T | L01 |
| m, cm, mm, km | Length units; 1 m = 100 cm = 1000 mm; 1 km = 1000 m | L01 |
| s, ms, min | Time units; 1000 ms = 1 s; 60 s = 1 min | L01 |
| Hz, kHz | Cycles per second; 1 kHz = 1000 Hz | L01 |
| a × 10^n | Scientific notation; nonzero coefficient satisfies 1 ≤ absolute value < 10 | L01 |
| T, f | Period and frequency, T in time and f in inverse time; f = 1/T for evenly repeated cycles | L01 |
| s as scale factor | Positive dimensionless new/old length ratio; distinguish from unit s = second by context | L02 |
| A, V | Area and volume, squared/cubed length units | L02 |
| Point, origin O | Location and chosen reference location | L03 |
| x,y; v_x,v_y | Ordered background axes; horizontal/vertical vector components | L03 |
| v, w | Directed displacement vectors, typically length units | L03 |
| Magnitude of v | Nonnegative length sqrt(v_x²+v_y²) in perpendicular equal-scale axes | L03 |
| sqrt(z) | Nonnegative square root of nonnegative z | L03 |
| u | Unit direction, v divided by its magnitude, for v nonzero; dimensionless for a length vector | L03 |
| theta, ° | Angle and degree; a full turn is 360° | L04 |
| sin, cos | Opposite/hypotenuse and adjacent/hypotenuse for acute right-triangle angles; unit-arrow coordinates extend signs | L04 |
| Scalar; dot product v·w | Single value; sum of component products with product units | L04 |
| d | Nonzero projection direction, explicitly dimensionless in teaching examples | L04 |
| s_parallel | Signed scalar projection v·u, length units for displacement v | L04 |
| p, r | Vector projection and perpendicular residual; v = p+r | L04 |
| B = [b1 b2] | Ordered synthetic column basis; [[a,b],[c,d]] displays its rows; B has length units | L05 |
| q = (q1,q2) | Dimensionless local coefficients; Bq = q1 b1+q2 b2 | L05 |
| P = O+Bq | Affine converter: background point from local coefficients | L05/L07 |
| D = det(B) | Signed determinant ad-bc; squared length units for our basis matrices | L06 |
| Singular; nonsingular | D = 0 with no unique inverse; D ≠ 0 with unique inverse | L06 |
| B^-1 | Inverse conversion, with inverse length units in our examples; not entrywise reciprocal | L06 |
| a,b,c,d in L06 | Scalar matrix entries local to the 2D derivation; not Cell3 vector names | L06 |
| X,Y | Background displacement components in inverse derivation | L06 |
| Typed; affine | Explicit kinds/units/order; linear conversion followed by an origin shift | L07 |
| q_hat, e | Displayed coefficients and signed residual e = q-q_hat; both dimensionless | L07 |
| Be | Background length residual omitted by coefficient display | L07 |
| Nearest tenth, ties away from zero | Closest multiple of 0.1; choose larger absolute value at equal distances | L07 |

Markdown note: the magnitude notation is also written as “magnitude of v” where vertical bars would interfere with a table.

## Source-local recognition labels, not assessed operations

S02 uses a 3D Cell3 basis B with ICRS columns [a b c], intentional left-handedness, and no silent column permutation or transpose. These are separate objects from our synthetic 2D B and L06 scalar entries. ICRS is the source's coordinate-frame label here; no astronomical conversion is required. O_K is the declared physical origin for later affine source identities; this course uses O. Source-local half-open cells [-1/2,1/2)^3 include each lower boundary and exclude each upper boundary, separately from classroom rounding.

S02 `/typed_conventions/metric_symbols` gives M_cell = B^T B, R_cell = M_cell^-1, and a distinct G_phase. Superscript T means transpose, exchanging rows and columns. These metric names are reserved: none is replaced by our ordinary 2D dot product without an explicit definition. Other advanced symbols and invariants in input-contract.json belong to later courses, and are not silently treated as taught prerequisites here.
