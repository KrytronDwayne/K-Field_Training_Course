# Terminology and notation

| Term/symbol | Meaning and domain | Units / first use |
|---|---|---|
| ICRS | International Celestial Reference System; fixed external axes for locked Cell3 | L1 |
| x, O_K, d=x−O_K | External point, declared origin, displacement | length; L1 |
| q=(q_1,q_2,q_3) | Counts of the three direct basis columns | dimensionless; L1 |
| a,b,c; B=[a b c] | Labeled direct edges and column basis; locked B uses ICRS | nm for Cell3; L1 |
| B_ex, L | Classroom analogue basis; arbitrary length unit | L; L1–2 |
| Half-open cell | Each coordinate includes −1/2 and excludes +1/2 | dimensionless coordinates; L1 |
| \|\|v\|\| | Magnitude sqrt(v_x²+v_y²+v_z²) | units of v; L2 |
| u·v | Dot product, sum of componentwise products | product units; L2 |
| theta_ij | Included edge angle, 0–180 degrees | degrees; L2 |
| cos, arccos, sin | Projection factor; angle with that cosine; height factor | dimensionless factors; L2–3 |
| B^T | Transpose: rows and columns exchanged for calculation | units of B; L2 |
| M_cell=B^T B | Cell3 Gram metric; source-local G in M01 | nm²; L2 |
| M_ex | Gram metric of classroom analogue only | L²; L2 |
| Symmetric | Entry ij equals entry ji in the mathematical object | L2; finite stored discrepancies preserved in L6 |
| Positive definite | q^T M q>0 for every nonzero coordinate triple | invertible Euclidean basis; L2 |
| u×v, c_ab/c_ac/c_bc | Oriented area vector; labeled face crosses | length²; L3 |
| A_ab,A_ac,A_bc | Magnitudes of corresponding face crosses | length²; L3 |
| Normal / unit normal | Perpendicular vector / its magnitude-one direction | length² for a face cross; dimensionless when normalized; L3 |
| det(B), V | Signed triple product a·(b×c); unsigned absolute determinant | length³; L3 |
| I | Identity matrix, leaves triples unchanged | dimensionless; L4 |
| T^−1 | Inverse linear map where it exists | reciprocal units; L4 |
| R_cell, R_ex | Inverse of the corresponding Gram metric | nm^−2 or L^−2; L4 |
| D=B R_cell=B^−T | Reciprocal basis columns; D^T d recovers q | nm^−1; L4 |
| G_phase, G_eff | Separately typed metrics in later work; not M_cell by naming | no calculation with them here; L2/4 |
| Q,Q_g,Q_nu | Reserved distinct later distance quantities, not inverse metrics or basis maps | recognition only; L4 |
| s / t | Positive dimensionless rescale / length coordinate on a positive ray | 1 / length; L5 |
| l_a,l_b,l_c | Positive edge lengths | length; L5 |
| eta, alpha, alpha^−1 | Supplied dimensionless ratio inputs; alpha^−1 means 1/alpha | L5 |
| k_b,k_c | Supplied-angle expressions fixing l_b/l_a, l_c/l_a | dimensionless; L5 |
| A_* | Chosen positive labeled area anchor | length²; L5 |
| Positive ray | All positive multiples of one fixed ratio triple | L5 |
| Lexeme / pointer / SHA-256 | Number string / exact JSON location / file fingerprint | L6 |
| E,F | Local residual matrices MR−I and B^T B−M in L6; no relation to later projection operators | dimensionless / length² |
| ROUND_HALF_EVEN | Decimal half-tie arithmetic rule: retain even last digit | separate from cell ownership; L6 |
| Source-reported / recomputed | Archived claim / declared fresh numerical calculation | L6 |

Notation scope: early lessons use B for a generic basis and explicitly label the classroom analogue; the locked card always means actual Cell3. Bare G from the source is translated to M_cell here. The course does not equate orientation with detector parity, chirality, or a projective sign identification.
