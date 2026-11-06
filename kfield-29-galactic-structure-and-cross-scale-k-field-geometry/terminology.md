# Terminology and symbol ledger

Local definitions govern; a matching letter from another source does not merge meanings.

| Term/symbol | Definition and type | First use |
|---|---|---|
| x, direction | directed unit sky vector; no radial distance encoded | L01 |
| {x,-x}, axis | unoriented pair; preserve original direction separately | L01 |
| ICRS | fixed celestial coordinate frame; x at RA0/Dec0, y at RA90/Dec0, z north | L01 |
| alpha, delta | right ascension and declination; declared degrees in sky examples | L01 |
| e_x,e_y,e_z | coordinate unit vectors | L01 |
| dot product a·b | sum of component products | L01 |
| norm ||x|| | sqrt(x·x), nonnegative length | L01 |
| arccos | inverse cosine returning angle 0°–180° in sky exercises | L01 |
| antipodal | opposite unit directions | L01 |
| projective view | explicitly identifies antipodal ends for a defined operation | L01 |
| normal | perpendicular vector; unit normal has length one | L02 |
| n,N,h,nu,u | response direction, sheet normal, positive spacing, odd order, n·N | L02 |
| kappa,q_resp | reciprocal-length scalar and vector of historical response | L02 |
| psi_ij | radian loop phase; psi_ac=psi_ab+psi_bc before reduction | L02 |
| F,D,G_star | dimensionless transfer, weighted response, relative response D/F | L02 |
| w_ij,R_local | absolute local reciprocal-metric entry; historical source-defined weight | L02 |
| U_D | synthetic relative response unit for classroom cards | L02 |
| q_j,Delta_j | reciprocal plane vector and spacing; q_j=n_j/Delta_j | L02 |
| phi | dimensionless plane phase in cycles, not a physical center | L02–03 |
| null/flag | undefined value plus explicit domain reason, preserving inputs | L02 |
| binary64 | source floating-point format; finite representation with retained residuals | L02 |
| A=[a b c] | ordered direct column basis, source-local length type | L03 |
| I, diag, transpose T | identity; diagonal matrix; exchange rows and columns | L03 |
| inverse A⁻¹ | reverses basis multiplication when columns are independent | L03 |
| Q_gal | reciprocal columns; Q_galᵀA_gal=I | L03 |
| R_gal_rows | G04 reciprocal row matrix A_gal⁻¹; not inverse Gram | L03 |
| k,c_k | integer center address, center A(k+phi) | L03 |
| A phi | zero-index center in reconstruction units | L03 |
| B,O_K | mature Cell3 ICRS column basis and declared physical origin | L03–04 |
| M_cell,R_cell | BᵀB in nm² and its inverse in nm⁻² | L03–04 |
| M_gal | A_galᵀA_gal in reconstruction-length units squared | L03–04 |
| determinant,V | signed volume and its absolute value; handedness uses sign | L03 |
| L | abstract synthetic length, never automatically nm or cosmic distance | L02 onward |
| z,u in ownership | z=floor(t+1/2), residual u=t-z∈[-1/2,1/2); distinct from response u | L03 |
| lambda | sum of declared address labels; half-step labels count half-steps | L04,06 |
| A2 | integer sum-zero address changes, rank two | L04 |
| root s_ab | (a-b)/2; same-sheet half-step difference | L04 |
| primitive lift | one of a/2,b/2,c/2; normal plus in-sheet slip | L04 |
| g,N,t_a | inverse-transpose sheet covector, unit normal, residual slip | L04 |
| G_phase,G_eff | reserved distinct source-defined metrics; not substituted for M | L04 |
| Q,Q_g,Q_nu elsewhere | reserved distance/integerization symbols; not Q_gal | L04 |
| q in metric exercise | dimensionless address displacement, not q_resp | L05 |
| positive definite | qᵀMq>0 for every nonzero real q | L05 |
| cross term | twice off-diagonal contribution in symmetric quadratic | L05 |
| ellipse/ellipsoid | constant positive quadratic-distance curve/surface | L05 |
| eigenvector/eigenvalue | direction preserved up to scalar multiplication / its multiplier | L05 |
| occupancy | full indexed observed count or fraction vector | L06 |
| depth | named hierarchy level; dyadic and ternary depths remain distinct | L06 |
| r=x-c | signed vector residual, retained with center for reconstruction | L06 |
| angular miss | angle between observed direction and nonzero center direction | L06 |
| radial mismatch | ||c||-1 in unit-shell coordinates, not galaxy physical distance | L06 |
| frozen/holdout | choices fixed before evaluation / population not used for those choices | L07 |
| branch | preserved alternative fit with parameters, results and history | L07 |
| control family | specified transformations used for a source comparison | L07 |
| M_bar | M/V^(2/3), dimensionless volume-normalized metric | L08 |
| U | orthogonal transformation; UᵀU=I; proper rotation also det(U)=+1 | L08 |
| K | source holonomy root tensor sum s sᵀ, distinct from distance metric M | L08 |
| hard mode/eigenframe | larger in-plane eigenvalue direction / ordered mode frame of specified tensor | L08 |
| selection/exposure | which objects or sky regions a survey could include; retain inputs | L08 |
| contrast | declared signed comparison, e.g. mean hard minus comparison fraction | L08 |

Evidence layers: source fact, derived implication, interpretation, proposed mechanism, reference mathematics and unresolved information are defined in sources.md. No statistical summary replaces a source record or residual channel. Detector parity, projective signs, chirality and family labels are not interchangeable; only response antipodal parity is calculated in this course. Dyadic refinement and ternary address recursion retain separate labels.
