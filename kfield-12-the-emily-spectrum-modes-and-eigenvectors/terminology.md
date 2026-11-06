# Terminology and notation

All exercise patterns and adjacency eigenvalues are dimensionless. A physical application must separately declare measurement units and its operator. Horizontal tuples are treated as columns when a matrix acts.

| Term/symbol | Exact course meaning | Introduced |
|---|---|---|
| Node / edge / open path P3 | Address / connection / three addresses −1—0—1 with no endpoint wrap | 01 |
| Pattern or state f | Ordered values at nodes; not an edge flow | 01 |
| Matrix row action | Sum of each row entry times the corresponding input entry | 01 |
| A | P3 adjacency; A(a,b,c)=(b,a+c,b), node order (−1,0,1) | 01 |
| D | Incidence: edge flows to signed node divergence; not A | 01 |
| Degree | Number of neighbors | 01 |
| Graph Laplacian | Degree times own value minus neighbor sum; contrast only | 01 |
| Eigenpair (λ,v) | Nonzero v with Av=λv component by component | 02 |
| S | Two-node adjacency S(a,b)=(b,a) | 02 |
| √q | Positive square root for q>0; √2 squared is 2 | 02 |
| Linearity | A(tv)=tAv and A(v+w)=Av+Aw | 02 |
| Spectrum / multiplicity | Eigenvalues / number of independent modes at an eigenvalue | 03, 05 |
| x·y; norm | Sum of matching-entry products; √(x·x) | 03 |
| Normalize | Divide a nonzero vector by its norm | 03 |
| Orthogonal / orthonormal | Zero mutual dot product / also unit lengths | 03 |
| r | Temporary shorthand √2, never a discarded residual | 03, 06 |
| v+,v0,v− | Unnormalized path patterns (1,√2,1),(1,0,−1),(1,−√2,1) | 03 |
| u+,u0,u− | Those patterns divided by 2,√2,2; fixed order (+,0,−) | 03 |
| L=(i,j,k); lexicographic | Triple address; i slowest, k fastest | 04 |
| G_L; A_L | Open Cartesian product P3×P3×P3; its neighbor-sum adjacency | 04 |
| Product mode U | U(i,j,k)=a(i)b(j)c(k) for three chosen path modes | 04 |
| α,β,γ | Local factor eigenvalues, unrelated to source physical constants | 04 |
| m | Integer coefficient of √2 in an Emily eigenvalue | 05 |
| λ_sheet | Source-local sheet label i+j+k; separated from eigenvalue λ | 05 |
| χ(L) | Node label (−1)^(i+j+k); not function reflection parity | 05 |
| R; antipodal | Reflection (Rf)(L)=f(−L); paired opposite addresses | 05 |
| e,o | Even (f+Rf)/2 and odd (f−Rf)/2 parts | 05 |
| Independent coordinate / dimension | A freely chosen scalar value / number of such choices | 05 |
| c_j | Mode coefficient u_j·f, with j a mode label | 06 |
| Basis | Independent patterns giving unique reconstruction of every state | 06 |
| Residual | Full signed difference f minus the retained modeled pattern | 06 |
| μ; d; **1** | Mean; centered detail f−μ**1**; all-ones pattern | 06 (ones in 01) |
| Invariant | An operation sends every pattern in a set back into that set | 06 |
| Quotient by constants | Regard states differing by a constant as equivalent; open adjacency does not descend to this quotient | 06 |
| X,Y; domain/codomain | Declared input/output state spaces | 07 |
| Carrier | Kind of object and its labeling, not just a count | 07 |
| A_X,B_Y,T,I | Two local operators, proposed map, identity map | 07 |
| diag(a,b) | Matrix with a,b on its diagonal, zeros elsewhere | 07 |
| Invertible / intertwiner | Has a recovery map / satisfies B_Y T=T A_X | 07 |
| Decoder channel / syndrome | Source M17 input / retained residual coordinate; recognition-only | 05, 07 |

Reserved source notation is kept separate: B is the source-locked ordered Cell3 basis, M_cell=BᵀB its Gram metric, R_cell its inverse, G_phase a distinct phase metric, and O_K a declared physical origin. None is needed in core computations. No source geometric basis is renamed to the classroom operator B_Y. No parity here is identified with detector parity, A1 carry parity, projective signs, chirality, or family labels.
