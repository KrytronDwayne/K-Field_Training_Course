# Terminology and notation

| Term or symbol | Meaning and local contract |
|---|---|
| A_ab,A_ac,A_bc; A_ref | Positive face areas and a common positive reference area, in the same squared-length unit. |
| y_ab,y_ac,y_bc | Classroom dimensionless log ratios ln(A/A_ref), in this order. |
| ln; e^y | Natural logarithm and its inverse exponential; ln(uv)=ln u+ln v for positive inputs. |
| F,M,G=G_Gamma | Lesson 01 inferred dimensionless coordinates F=y_ac-y_bc, M=y_bc-y_ab, G=9y_ab+8y_ac-11y_bc. Archival definition bodies remain missing. M is not mass or M_cell. |
| Gamma2 | Archival gravity scalar; its definition and reference/integration constant remain VERIFIED_NOT_LOADED. |
| Gamma_B | Dimensionless conditional Bragg logarithm ln(d/L_ref)+ln(abs(sin theta))-ln(lambda_wave/L_ref). Distinct from Gamma2. |
| B; B^T; B^-T | Ordered basis matrix, transpose (swap rows and columns), inverse transpose. Synthetic B=diag(2,3,4) LU is not the locked Cell3 basis. |
| diag(a,b,c) | Matrix with those diagonal entries and zeros elsewhere. |
| O_K; x; u | Declared physical origin, physical position, dimensionless address u=B^-1(x-O_K). |
| M_cell; R_cell | Gram metric B^T B (LU^2) and inverse metric (LU^-2) in the synthetic example. |
| G_phase,G_eff,Q,Q_g,Q_nu | Distinct source objects reserved by the input contract; no identification with M_cell, R_cell or G_Gamma is made or needed here. Their formulas are not assessed. |
| h; q; d; n_hat | Integer reciprocal address, reciprocal vector (LU^-1), positive spacing 1/length(q) (LU), unit normal q/length(q). q must be nonzero. |
| dot product; length | Sum of paired component products; nonnegative square root of self dot product. |
| rho in lesson 02 | Full signed reciprocal residual vector, LU^-1; retained in q_observed=3^(signed g)B^-T h+rho. |
| g; m; lambda_wave; theta | Declared recursion depth/exponent sign; positive Bragg order; positive wavelength LU; angle with nonzero sine. |
| LU,T,MU,U | Synthetic length, time, mass and response units. U is not automatically force or energy. |
| v,a,n | Velocity LU/T, acceleration LU/T^2 and dimensionless unit normal. |
| v_parallel; v_perp | Signed projection v dot n and perpendicular vector v-(v dot n)n. |
| mu; F_parallel | Added mass coefficient MU and conditional force scalar MU*LU/T^2; distinct from lesson 01 F. |
| graph; vertex; edge | Declared points and undirected links. Boundary and edge-count conventions are part of the input. |
| spanning tree; cycle dimension | Connected no-cycle subgraph containing all vertices; independent cycle count E-V+1 for a connected finite graph. |
| V,E; P3 | Vertex and edge counts; three-vertex open path. E here is not a projection operator. |
| periodic; winding | Adds wrap links; a route around a periodic direction. A sector decomposition requires an actual map. |
| Z3; H^2 | Modulo-three labels; source cohomology classification name. Dimension-six theorem is supplied, not proved here. |
| SU(3),F4,E6,E7; Albert algebra | Source theorem/carrier names. Exceptional action and real-form selection require explicit construction. |
| action; involution | Operators preserving the stated composition rules; operation whose square is identity. |
| rho,sigma,sigma-prime in lesson 05 | Matrices for finite actions; not reciprocal residuals. Sigma-prime=-I is distinct from worked sigma=diag(-1,1). |
| I; T_map | Identity matrix; an intertwiner (written T in lesson 05), not the time unit T. |
| D; trace; canonical | Full matrix defect; sum of diagonal entries; selected by additional declared rules, not mere existence. |
| [A,B]; R(X) | Commutator AB-BA; assigned operator for a Lie generator. Not the metric R_cell. |
| w,z,k,b,r | Motion projection LU/T, response U, H1 coefficient U*T/LU, H2 coefficient U*T^2/LU^2, signed residual z-prediction in U. |
| invariant; odd/even | A property preserved under a specified transformation; response reverses/stays fixed when the input reverses. |
| calibration; held case | Inputs used to set a parameter; case excluded from that choice and predicted after freezing it. |
| VERIFIED_NOT_LOADED | Source-reported verification status with missing replay definition/body, preserved without inventing one. |
| source fact / local replay | What pinned bytes say / what calculations this course actually recomputes. A matching hash establishes byte identity, not theorem validity. |
| branch boundary | A domain restriction or unconstructed extension that must propagate even when an endpoint field is null. |

The locked Cell3 conventions remain ICRS columns [a b c], intentional negative determinant and half-open cells [-1/2,1/2)^3. Classroom examples do not replace those constants. No nearest-integer rule is used in the core exercises; cell ownership is not silently treated as rounding. No detector parity, carry parity, projective sign, chirality, family label, primitive lift or dyadic/ternary recursion is identified with another.
