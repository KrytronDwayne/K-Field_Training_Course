# Terminology and notation

| Symbol or term | Meaning, units and scope | Introduced |
|---|---|---|
| LU, LU² | Declared synthetic length unit and its area unit | 1 |
| A_ab,A_ac,A_bc | Positive face areas, always [ab,ac,bc] in log triples | 1 |
| A0 | ONE common positive reference area, same units as faces | 1 |
| exp, ln, L | Exponential, inverse natural log on positive numbers, L=ln2 | 1 |
| rho | Positive common edge multiplier; areas multiply by rho² | 1 |
| y | Dimensionless ordered log-area triple ln(A_i/A0) | 1 |
| m,z | Mean log and zero-sum shape; y=m1+z | 2 |
| dot product | Multiply corresponding entries and add | 2 |
| orthonormal | Mutually perpendicular, each squared length one | 2 |
| e_s,e_u,e_v | Source unit directions (1,1,1)/sqrt3,(-1,1,0)/sqrt2,(-1,-1,2)/sqrt6 | 2 |
| s,u,v | Dot projections; s=sqrt3 m; u,v area-shape coordinates | 2 |
| A2 shape fiber | Source name for the two-dimensional area-shape component; not arbitrary shear | 2 |
| I, T, P_H | Identity matrix, transpose, mean-removal I-11^T/3 | 2 |
| H | Classroom matrix rows (1,1),(1,-1); inverse H/2 | 3 |
| t_change | Dimensionless small-change parameter; written t in Lessons 3,4,6 | 3 |
| tangent, derivative | Coefficient c in f(t)=f(0)+ct+R(t), R(t)/t approaching zero | 3 |
| Jacobian | Table of local first-order response coefficients at a specified point/domain | 3 |
| remainder | Exact finite change minus tangent prediction, retained with sign | 3 |
| l_a,l_b,l_c | Positive edge lengths; vertical bars around a vector denote its length | 4 |
| theta_ij, sin(theta_ij) | Included angle and height/edge factor, supplied in exercises | 4 |
| eta, alpha_inverse, alpha | 1000 A_bc/A_ab, 100 A_bc/A_ac, reciprocal of alpha_inverse | 4 |
| x_a,x_b,x_c | Dimensionless tangent log-length changes | 4 |
| dE,dA,dG | Ordered dln eta,dln alpha,dln Gamma2; dA is not area | 4 |
| Gamma2 | Source scalar-lift coordinate; no force dynamics claimed | 4 |
| J | Fixed-angle Jack matrix with determinant 12 | 4 |
| determinant | Scalar square-matrix invertibility test; formulas taught for required cases | 4 |
| B=[a b c] | Ordered basis columns; retain frame/orientation; synthetic B differs from locked Cell3 | 5 |
| M_cell | B^T B, direct/Gram metric, units LU² in examples | 5 |
| cof(M_cell) | Metric cofactor matrix, LU⁴; not cofactors of B | 5 |
| R_cell | M_cell inverse, LU^-2; not G_phase | 5 |
| G_phase | Distinct source phase metric; recognition only, not computed here | 5 |
| C_b,C_c; S,A_branch | Integer side carries and sum/difference modes; same-parity S,A_branch | 5 |
| t_length,k_b,k_c | Positive scale length and edge ratios, lengths=t_length(1,k_b,k_c) | 5 |
| typed Devon object | Geometry, scale, shape, scalar and branch components with types and return maps | 5 |
| inverse residual | Recovered minus supplied input; distinct from approximation remainder | 6 |

The source uses A for the antisymmetric branch mode; this course writes A_branch to avoid collision. The symbol t in the anchor subsection is a length; t in tangent examples is dimensionless. The capstone spells out t_length and t_change. No nearest-integer rounding, cell ownership, parity fusion or scalar-to-force conversion is performed in this course.
