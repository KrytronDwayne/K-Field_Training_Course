# Terminology and notation

All triples retain their ordered components. The course uses a synthetic analogue in LU; real Cell3 source cards retain nm and ICRS component order. Never mix these geometries.

| Term/symbol | Operational meaning | Units and scope | First teaching |
|---|---|---|---|
| LU | Arbitrary classroom length unit | Synthetic length only | Lesson 1 |
| x | Physical point coordinate triple | LU in analogue | Lesson 1 |
| O; O_K | Declared physical origin; O_K denotes the Cell3 origin | Length | Lesson 1 |
| a,b,c | Ordered direct steps; columns of B | Length | Lesson 1 |
| B | Maps address displacement to physical displacement by scaling and summing columns | Length | Lesson 1 |
| q | Full affine address B^-1(x-O) | Dimensionless | Lesson 1 |
| d | Displacement x-O in lesson 1; do not confuse with subscripted d_h | Length | Lesson 1 |
| Inverse B^-1 | Operation undoing B; not entrywise reciprocal | Inverse length | Lesson 1 |
| Affine | Linear displacement rule plus a fixed origin | x=O+Bq | Lesson 1 |
| Determinant | Orientation/volume-scale quantity; nonzero here permits unique inverse | Length cubed; recognition bridge | Lesson 1 |
| [-1/2,1/2) | Lower endpoint included; upper endpoint excluded | Address interval | Lesson 2 |
| Floor(t) | Greatest integer no larger than t | Input's numerical integer part toward negative infinity | Lesson 2 |
| z | Integer cell owner floor(q+1/2), componentwise | Dimensionless integer triple | Lesson 2 |
| u | Local address q-z, every entry in [-1/2,1/2) | Dimensionless; retained | Lesson 2 |
| Dot product | Sum of componentwise products | Product of operand units | Lesson 3 |
| h | Integer plane-family label, nonzero for normal/spacing | Dimensionless | Lesson 3 |
| g_h | Reciprocal plane counter B^-T h | Inverse length | Lesson 3 |
| T, B^-T | Transpose; transpose of inverse | Swaps rows and columns | Lesson 3 |
| m | Integer plane level in g_h dot (x-O)=m | Dimensionless integer | Lesson 3 |
| Source pointer | Slash-delimited JSON location; array index starts at zero | Provenance | Lesson 3 |
| Lexeme | Exact written decimal string | Preserve stored precision | Lesson 3 |
| u,v,w on source card | Names of ordered reciprocal families | Labels, not the local vector u | Lesson 3 |
| nm | Nanometre, 10^-9 metre | Locked source length unit | Lesson 3 |
| \|v\| | Magnitude sqrt(v1²+v2²+v3²) | Same units as v | Lesson 4 |
| n | Unit normal g_h/magnitude(g_h) | Dimensionless; oriented | Lesson 4 |
| d_h | Consecutive integer-level spacing 1/magnitude(g_h) | Positive length | Lesson 4 |
| Projection | Signed component n dot d along unit n | Length for physical d | Lesson 4 |
| e1,e2 | Address triples (1,0,0),(0,1,0) | Dimensionless | Lesson 5 |
| M_cell | Gram metric B^T B, containing direct-step pairings | Length squared | Lesson 5 |
| R_cell | Inverse Gram metric M_cell^-1 | Inverse length squared; recognition only | Lesson 5 |
| G_phase,G_eff,Q,Q_g,Q_nu | Separately typed source quantities, not synonyms for M_cell or B^-T | Reserved; not computed here | Lesson 5 scope |
| Cross terms | Off-diagonal contributions, e.g. 2q1q2 in this analogue | Contribute to squared physical length | Lesson 5 |
| Cosine | Normalized physical dot product | Dimensionless | Lesson 5 |
| q_disp | Shortened displayed address | Dimensionless | Lesson 6 |
| r | Signed display residual q-q_disp | Dimensionless; keep each component | Lesson 6 |
| Reconstruction difference | Reconstructed minus original point | Length; retain zero or nonzero triple | Lesson 6 |

The source-card u label, local vector u, physical displacement d and spacing d_h are always distinguished by context or subscript. Source-version displacement is provenance, not the display residual r or an observed measurement channel.
