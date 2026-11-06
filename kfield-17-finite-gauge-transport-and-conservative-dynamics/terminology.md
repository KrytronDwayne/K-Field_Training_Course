# Terminology and notation

Symbols are scoped to their lessons. All toy links and states are dimensionless. LU, TU and AU denote illustrative length, time and action units, and EU=AU/TU denotes energy units. They are not experimental calibrations.

| Term/symbol | Operational meaning and units | First use |
|---|---|---|
| i; conjugate | i²=−1; conjugate of a+bi is a−bi | 01 |
| State ψ | Column of components in a declared local frame | 01 |
| Frame/site | Coordinate convention/location label; x and y are labels here | 01 |
| U_xy | Link from y to x; rightmost factor acts first | 01 |
| diag; I | Diagonal matrix; identity of the stated dimension | 01 |
| T; † | Transpose; conjugate transpose (adjoint) | 01 |
| Inverse U⁻¹ | Two-sided map undoing U | 01 |
| Unitary | U†U=UU†=I; preserves Euclidean complex norm | 01 |
| Norm squared N | ψ†ψ, sum of squared component moduli | 01 |
| G_x; prime | Frame change at x; prime means changed coordinates, not derivative | 02 |
| d_x | ψ_x−U_xyψ_y, full retained finite difference | 02 |
| Covariant | Follows its stated transformation rule, e.g. d′_x=G_xd_x | 02 |
| Invariant | Unchanged under the specified operation | 02 |
| Holonomy U_loop | Ordered net loop map with a basepoint | 03 |
| X; Z | Synthetic swap and diag(1,−1) maps | 03 |
| Conjugation | G U G⁻¹; preserves trace | 03 |
| Plaquette | Elementary closed lattice face; example loop is an algebraic analogue | 03 |
| Tr; Re | Diagonal sum; real part | 04 |
| F | I−U_loop, retained matrix comparison | 04 |
| β; S | Positive action coefficient in AU; β ReTr(I−U_loop) in AU | 04 |
| det | Determinant; diagonal product, or ad−bc for a 2 by 2 matrix | 05 |
| Lhat | Self-adjoint finite matrix in TU⁻¹ for the synthetic evolution | 05 |
| τ_C; C | Real Cayley time in TU; dimensionless rational update | 05 |
| Self-adjoint | Lhat†=Lhat, distinct from unitarity | 05 |
| M_cell; R_cell | Gram metric BᵀB in LU²; its inverse in LU⁻² | 06 |
| B | Ordered real basis columns; toy examples do not replace locked ICRS Cell3 B | 06 |
| δ; V | det(M_cell)=V² in LU⁶; positive volume in LU³ | 06 |
| G_phase; G_eff | Distinct phase/effective metrics, not substituted for M_cell | 06 |
| Bivector; wedge²R | Oriented area coordinates; map on pairs (12,13,23), LU⁻⁴ | 06 |
| Minor | Determinant of a selected submatrix | 06 |
| J | Declared example pairing [[0,0,1],[0,−1,0],[1,0,0]] | 06 |
| H_E; H_B | Dimensionless mature electric/magnetic Hodge blocks | 06 |
| Rung; compiler | Hierarchy level; specified finite model construction | 07 |
| Certificate; hash | Calculation record; byte fingerprint, not proof of its content | 07 |
| ε_E; ε_B; α | Source-reported enclosure/contraction bounds | 07 |
| Δ; H_N; τ_R; E0 | Gap in energy units; action scale; positive time scale; E0=H_N/τ_R | 07 |
| d_root; c_* | Normalized synthetic root bound; positive detail lower bound | 07 |
| min | Smaller of the supplied arguments | 07 |
| Q_L | Unnormalized ψ†Lhatψ in TU⁻¹; not distance Q, Q_g or Q_nu | 08 |
| Q_L/N | Normalized expectation for N>0 | 08 |
| r | Retained component-wise remainder ψ_new−ψ_ref | 08 |
| β_T; exp; ln | Recognition-only thermal parameter; exponential; its inverse logarithm | 08 |
| T (thermal paragraph only) | Uncomputed tail; distinct from transpose superscript T | 08 |

Source notation safeguards: O_K denotes the declared physical origin in affine identities using x−O_K; it is not used as a substitute for a site label. Cell ownership [-1/2,1/2)^3 is distinct from nearest-integer tie rules, neither of which is assessed here. Detector parity, carry parity, projective signs, chirality and family labels are not equated by our minus signs. Our two-component space is not claimed to be the source's color-first C₃ direct-sum W₂ carrier. Mathematical-backbone module names and integration compiler labels are separate namespaces.
