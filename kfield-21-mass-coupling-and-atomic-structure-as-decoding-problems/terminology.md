# Terminology and notation

Symbols are local to their declared object. In particular c_light is not c, V is not a geometric volume, and the decoder G is not a Cell3 metric.

| Term | Meaning and scope | First lesson |
| --- | --- | --- |
| Channel | An ordered linear recipe for coefficients; one row of A. | 01 |
| Tuple/vector | An ordered list; operations are entrywise unless a dot product is stated. | 01 |
| Matrix A_small | The 3 by 2 classroom channel table [[1,0],[0,1],[1,1]]. | 01 |
| A | The ordered 13 by 6 M17 matrix; never a chemical label within a matrix equation. | 03 |
| c, cj | Coefficient vector and its jth entry; dimensionless in exercises. | 01 |
| y | Full ordered input vector; synthetic throughout the numerical exercises. | 01 |
| r or s | Full signed channel residual y-Ac; s is used for M17 syndrome. | 01,03 |
| Transpose A^T | The matrix formed by turning columns into rows. | 01 |
| Euclidean inner product | Sum of entrywise products; declares the decoder geometry. | 01 |
| Normal residual | A^T r, a set of column-dot-product constraints; not the full r. | 01 |
| Rank | Number of independent column directions over the specified scalar field. | 02 |
| Image / kernel | Outputs a map can produce / inputs it sends to zero. | 02 |
| R / Z | Real-number field / integers. Bold or contextual R for reals is separate from projector R. | R: 01; Z: 02 |
| Syndrome | Residual coordinates retained outside the represented image under a declared decomposition. | 02 |
| Lattice / saturation | Integer column combinations / containing all integer points of its real span. | 02 |
| G=A^T A | Decoder Gram matrix only; distinct from all Cell3 and phase metrics. | 03 |
| Eigenvector / eigenvalue | A direction a linear map only scales / the scale factor. | 03 |
| Aplus | (A^T A)^(-1)A^T for this full-column-rank Euclidean decoder. | 03 |
| P / R=I-P | Represented-channel projector / complementary residual projector. | 03 |
| L_int | Derived 6 by 13 integer extractor with L_int A=I6; not source L. | 03 |
| Source L | Missing 7 by 13 syndrome matrix with LA=0; VERIFIED_NOT_LOADED. | 03 |
| W / W7 | Explicit toy four-character table / missing ordered source seven-character replay object; do not equate them. | 03 |
| Representation / intertwiner | Declared group actions / a map respecting those actions; equality of dimensions supplies neither. | 03 |
| b / b_toy | Source renderer order (1,alpha,alpha²,alpha³,a_e,eta) / separately stipulated toy values. | b: 03 (rendering 04); b_toy: 04 |
| m_e / m_ref | Source reference mass / synthetic reference mass. Neither value is inferred from a dimensionless ratio. | 04 |
| V | Nominal composition label 12C+H+14N+16O, not geometric volume or exact isotope mass. | 05 |
| C,H,N,O | Ordered nonnegative atom counts for composition endpoints. | 05 |
| U1,U2,U3,K | Stated signed composition moves; U3=U1+U2, K is independent. | 05 |
| Fiber | Inputs sharing a specified output; the map and domain must be declared. | 05 |
| Isotope / isomer | Same element with different neutron count / same molecular formula with different arrangement. | 05 |
| A+B → AB | Synthetic conserved constituent labels, distinct from matrix A. | 05 |
| u / E_unit | Stipulated synthetic mass / energy units; 1u c_light²=10 E_unit is a toy conversion. | 05 |
| Q_release / delta m | Released-energy convention / initial minus final complete-object mass. | 05 |
| c_light | Speed factor in the declared mass-energy reference relation; distinct from coefficient c. | 05 |
| Graph / spectrum | Vertices and edges with identity / eigenvalue list that need not uniquely identify the graph. | 06 |
| QPC phase tensor | Source-local requested coordinate not supplied here; recognition-only. | 06 |
| t / n / c_star | Solver step parameter / update index / exact decoder coefficient target. | 07 |
| Approximant / closure | Displayed replacement / exact original-minus-replacement difference. | 08 |
| M_cell / R_cell / G_phase | Cell3 Gram metric / its inverse / distinct phase metric; no numerical use or substitution in this course. | source contract |
| O_K / B | Declared physical origin / locked ordered source basis, unused in classroom channel arithmetic. | source contract |
