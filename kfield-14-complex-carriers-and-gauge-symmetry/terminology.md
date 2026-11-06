# Terminology and notation

All numerical examples are dimensionless. Source coordinates and physical units are not inferred from these symbols.

| Symbol or term | Meaning and guard | First use |
|---|---|---|
| i | Imaginary unit; i²=−1. | 1 |
| z=a+bi | Complex number with real components a,b. | 1 |
| z̄ | Conjugate a−bi; reverses a unit phase. | 1 |
| \|z\|², \|z\| | a²+b² and its nonnegative square root. | 1 |
| phase, θ | Unit-circle direction; a full turn is 2π radians. e^(iθ) denotes cos θ+i sin θ here. | 1 |
| ζ | (1+i√3)/2; primitive sixth root used in the finite kernel. | 1,5 |
| T, † | Transpose; conjugate transpose. Do not interchange them on complex matrices. | 2 |
| I_n, diag | n×n identity; diagonal or block-diagonal matrix as specified. | 2–4 |
| ⟨v,w⟩, \|\|v\|\|² | v†w, conjugate-linear in first argument; squared norm v†v. | 2 |
| unitary | Square U satisfying U†U=I, inverse U†. | 2 |
| carrier H | Space acted on; here C₃⊕W₂ in color-first order. | 3 |
| ⊕, C₃, W₂ | Direct sum of separately typed complex color and weak blocks of dimensions 3 and 2. | 3 |
| P_c,P_w | Complementary projectors retaining both components for reconstruction. | 3 |
| P | Specified 5×5 weak-first-to-color-first permutation; inverse Pᵀ. | 3 |
| Q_charge | Dimensionless integer phase-weight operator diag(−2,−2,−2,3,3); not a distance Q. | 3 |
| det | Determinant; ad−bc for 2×2, product for diagonal entries or block determinants. | 4 |
| Ω, top form | Ordered alternating volume coefficient transforming by det A. | 4 |
| a,b (weights) | Integers multiplying phase exponents in color and weak blocks, respectively; local meanings differ from Lesson 1 components. | 4 |
| U(n),SU(n) | Unitary matrices; unitary matrices with determinant one. | 4 |
| S(U(3)×U(2)) | Color-first unitary block pairs with determinant product one. | 4 |
| group | Set with closed associative composition, identity and inverses. | 5 |
| × | Cartesian product of group choices; componentwise composition. | 5 |
| mod n | Remainder representative in 0,…,n−1; addition understood modulo n. | 5 |
| kernel | Inputs a composition-preserving map sends to target identity. | 5 |
| quotient | Classes of labels indistinguishable under the stated map or subgroup identification. | 5 |
| central | Commuting with all elements in the group; scalar matrices here. | 5 |
| Φ | Source cover map (g₃,g₂,z)↦(z⁻²g₃,z³g₂). | 5 |
| Zn or ℤ_n | Cyclic group/subgroup of order n; Z1 trivial. Physical candidate usage is source-scoped. | 5,7 |
| ρ, action | Specified map from group choices to transformations of a carrier. | 6 |
| local/global | Independent phase per node / one phase shared by nodes in the toy model. | 6 |
| SHA-256, JSON pointer | Byte digest; address to a field or array entry, using zero-based array indices. | 7 |
| namespace | Collection defining a label; compiler M03 is not automatically backbone M03. | 7 |

Reserved series notation: M_cell is the Cell3 Gram metric, R_cell its inverse, G_phase a distinct phase metric, O_K the declared physical origin, and B a source-local ordered basis. None is silently reused for a gauge matrix here. Any future link to geometry must restore its source units, ordering and origin contract.

Evidence vocabulary: source fact (what is recorded); derived implication (explicit consequence); interpretation (assigned meaning); proposed mechanism (candidate process); reference theory (comparison definitions); unresolved question (information still required). No empirical dataset is generated in this course.
