# Terminology and notation

| Term/symbol | Meaning and units in this course | First taught |
|---|---|---|
| L, τ, D | Chosen length, time and detector units; D also denotes displacement in Lesson 5 only, where explicitly a vector with length units | 1, 5, 7 |
| Vector | Ordered signed components; direction is not recoverable from cost alone | 1 |
| Matrix; entry (i,j) | Table of coefficients; i is row, j column | 1, 3 |
| Transpose, superscript T | Exchange rows and columns; distinct from total duration T | 1, 3 |
| Dot product | Sum of matching products; with a unit normal it gives a signed projection | 2 |
| Unit direction/normal | Dimensionless vector with length one; normal is perpendicular to a plane | 1, 2 |
| q(z) | Scalar quadratic form zᵀGz; input and G determine units | 1 |
| G (classroom) | [[2,1],[1,2]] L⁻² unless explicitly replaced; synthetic, symmetric and positive | 1 |
| Positive form | q(z)>0 for nonzero z, q(0)=0 | 1 |
| Cross term | 2G₁₂xy for a symmetric two-coordinate form | 1 |
| Contour, semiaxis | Equal-cost curve; ellipse center-to-end length on a principal direction | 1 |
| n₊, n₋ | (1,±1)/√2, dimensionless diagonal unit directions | 1 |
| o, O_K | Declared fixed origin; x−o or x−O_K is a displacement | 2, 3 |
| p_j, d_j, n_j | Dimensionless continuous plane coordinate, positive length spacing, unit normal; j labels family | 2 |
| a, p-dot | Signed plane-rate column, τ⁻¹; not a discrete integer event counter | 2 |
| H, I | Dimensionless plane-coordinate metric and identity matrix | 2 |
| A; G_ruler | Ruler map rows n_jᵀ/d_j in L⁻¹; its pullback AᵀHA in L⁻² | 2 |
| B, u, z | Column map from dimensionless u to length z=Bu/2; synthetic B=diag(2,1)L | 3 |
| Inverse B⁻¹; T_B | Undo the invertible map; T_B=2B⁻¹ with units L⁻¹ here | 3 |
| G_phase | Distinct source phase metric; units must be taken from its declared contract, not inferred from its name | 2, 3 |
| W_qpc, W | Pullback BᵀG_phase B/4; W is its classroom analogue, dimensionless under classroom typing | 3 |
| C | Source factor matrix in W_qpc=CᵀC; not path cost J; complete locked entries not retrieved | 3 |
| M_cell, R_cell | Source Gram matrix BᵀB and its inverse; not synonyms for G_phase | 3 |
| G_eff; Q, Q_g, Q_nu | Reserved distinct source metric/distance forms, not used for calculations here | 3 |
| Δt, Δx | Positive duration and signed displacement increment | 2 |
| Σ | Sum over indexed segments | 4 |
| v | Physical velocity in L/τ | 1 |
| u-dot | Coordinate rate in τ⁻¹ | 3 |
| J | Accumulated cost ΣΔt vᵀGv, τ⁻¹ here; local QPC skill convention instead yields m²/s | 2, 4 |
| Interpolation | Rule specifying behavior between samples | 4 |
| Admissible | Allowed by the fixed route specification | 5 |
| T, v-bar, δ_i | Total positive duration; average displacement/T; signed segment deviation v_i−v-bar | 5 |
| L_b, U_b, gap | Lower bound, feasible upper bound on minimum, difference U_b−L_b; cost units | 5 |
| Absolutely continuous; square-integrable velocity | Recognition-only continuum conditions: path recovered by accumulating velocity; finite accumulated squared speed | 5 |
| Certificate; SHA-256 | Reproducible claim/input/proof record; content digest identifying bytes, not proving mathematics | 6 |
| [a,b); truncation | Interval including a and excluding b; drop digits after a specified decimal place | 6 |
| Residual | Retained original minus model/displayed value; preserves reconstruction, with signs and units | 5–7 |
| VERIFIED_NOT_LOADED | Source missing-body disposition, distinct from fresh replay | 3, 6 |
| y, k, r, e | Detector response D, sensitivity D, dimensionless driver, response residual D; r here is not Lesson 6's precision residual | 7 |
| Nonidentifiability | Different allowed choices give the same observed output | 7 |
| Transfer/coupling | Explicit relation connecting defined input to response, with calibration and units | 7 |

Local symbol reuse is announced at its lesson. Classroom examples do not change the source's three-dimensional handedness, cell ownership, metric definitions or evidence classes. Numeric costs remain accompanied by their signed generating coordinates.
