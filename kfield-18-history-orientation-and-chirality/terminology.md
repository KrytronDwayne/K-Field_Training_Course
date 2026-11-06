# Terminology and notation

All finite teaching vectors and matrix entries are dimensionless. Source objects retain their source-local types. Similar notation is not permission to merge objects.

| Term/symbol | Meaning in this course | First taught |
|---|---|---|
| word, prefix | Ordered finite letters; prefix adds on the left | 01 |
| Ω | Empty-word label, distinct from zero vector | 01 |
| e_w, e_j | Unit coordinate vector at a word or numbered chain slot | 01–02 |
| amplitude/coefficient ledger | Complete ordered list of signed/complex entries, including zeros | 01 |
| orthogonal vectors | Dot product zero; complex version uses conjugates | 01, 07 |
| linear map | Apply to unit coordinates, multiply by coefficients and add | 02 |
| S (history) | Three-state square shift, S(x,y,z)=(0,x,y) | 02 |
| T | Rectangular isometry T(a,b)=(0,a,b) | 02 |
| U | Explicit infinite unilateral shift on l²(N_0) | 02 |
| L_a, L_b | Full binary toy prefix operators; not source B_8 labels | 02 |
| † | Adjoint: transpose for real matrices; conjugate transpose for complex matrices | 02, 07 |
| I_n, diag | Identity on n slots; matrix with given diagonal and zero elsewhere | 02 |
| rank | Number of independent output directions | 02 |
| kernel | Inputs mapped to zero | 02 |
| cokernel dimension | Number of missing output directions; equals dim ker of adjoint in these examples | 02 |
| index | dim kernel minus dim cokernel | 02 |
| input/terminal defect | I−S†S for finite S; retains destroyed terminal input | 02 |
| output/root defect | I−SS† for finite S; selects unreachable root output | 02 |
| \|\|v\|\|² | Sum of squared entries (squared magnitudes if complex) | 03 |
| isometry | Linear map preserving every input norm | 03 |
| injective, surjective, bijective | Distinct inputs stay distinct; onto codomain; both properties | 03 |
| image, complement | Reached subspace; retained perpendicular part in our orthogonal decompositions | 03 |
| projector, idempotent | P²=P; an orthogonal projector also satisfies P†=P | 04 |
| P_0, q_n | Root selection and shifted selections in finite chain | 04 |
| B (spatial) | Ordered basis columns; diagonal examples are synthetic | 05 |
| determinant | Signed volume scaling; diagonal determinant is entry product | 05 |
| coframe, covector | Ordered coordinate readers; a reader is a linear scalar-valued map | 05 |
| τ, θ¹,θ²,θ³ | Declared time reader and ordered spatial readers | 05 |
| handedness | Sign of spatial basis orientation relative to fixed reference | 05 |
| grading G | G²=I; generic two-state toy diag(1,−1) | 06 |
| P_plus, P_minus | (I±G)/2; generic grade selectors | 06 |
| P_L, P_R | L/R factor selectors; source convention uses ∓γ_5 | 06–07 |
| exterior parity | Even/odd number of basis labels in an exterior product; separate internal factor | 07 |
| ⊗ | Pair independent factor labels and act on each factor | 06 |
| Π | Toy correlation selector diag(1,0,0,1) | 06 |
| Π_phys | Source M14 correlation; not identified with toy's physical realization | 07 |
| anticommutator | AB+BA; vanishes for G and swap X | 06 |
| ell, m, j | Angular block label, cutoff, spin-regrouped label | 06 |
| H_ell, direct sum | Angular carrier; blocks placed beside each other so dimensions add | 06 |
| C₂ | Source-supplied angular invariant with eigenvalue ell(ell+1) | 06 |
| Hamiltonian | Operator specifying energy; not determined by a dimension count | 06 |
| F_hist, B_8* | Source l² word carrier and all finite words over source alphabet | 01, 07 |
| l², N_0 | Square-summable coefficient lists; indices 0,1,2,… | 01–02 |
| W, P_Π, T_0 | Source M14 isometry, defect projection and radial operator; retain source scope | 04, 07 |
| γ_μ, γ_5 | Source Clifford matrices and oriented product grading | 07 |
| signature | Pattern of positive/negative metric directions | 07 |
| intertwiner | Map preserving the relevant actions between carriers; not supplied by equal dimensions | 07 |
| i, conjugate | i²=−1; conjugate of a+bi is a−bi | 07 |
| [A,B] | AB−BA, the commutator | 07 |
| pointwise algebra | Maps multiply each slot separately; a common diagonal representation | 07 |
| CP | Source charge-conjugation/parity branch; algebraic scope kept explicit | 07 |
| A_0, S (CP witness) | Positive diagonal input and its square root, distinct from history S | 07 |
| ω, D, Y_u, Y_d | Cubic phase, diagonal phase map and supplied witness matrices | 07 |
| VERIFIED_NOT_LOADED | Source missing-replay-body disposition; not fresh proof by this course | 07 |

Reserved series notation: M_cell=BᵀB, R_cell=M_cell^−1, G_phase (phase metric), G_eff (effective metric) and O_K (physical origin) keep distinct meanings. The generic grade G is not any of those metrics. Source reciprocal/affine formulas require x−O_K; no affine identity is computed here. Source color-first C_3 direct-sum W_2 is an internal carrier convention, not a swap of spacetime labels. Detector parity, A1 carry parity, projective sign, family labels, primitive lifts, chirality and dyadic/ternary recursion labels remain separately typed.
