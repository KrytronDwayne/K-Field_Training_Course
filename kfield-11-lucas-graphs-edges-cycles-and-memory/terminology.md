# Terminology and notation

All classroom coordinates are dimensionless. Lists carry declared ordering and object type. A scalar is one number; a vector is an ordered list of numbers. “Space” here means a collection closed under scaling and addition, not necessarily physical space.

| Term or symbol | Operational meaning | Introduced |
|---|---|---|
| Vertex/node; edge | Labeled location; allowed connection between two locations | 01 |
| Adjacent; degree | Joined by an edge; number of incident edges | 01 |
| Walk; path; connected | Adjacent-vertex sequence; no repeated vertices; a path between every pair | 01 |
| P2, P3; □ | Two/three-node path graph; Cartesian-product adjacency rule | 01 |
| G_L | Open P3 □ P3 □ P3 Lucas graph | 01 |
| V, E in formulas | Counts of vertices and edges, respectively | 01 |
| Open boundary | No endpoint wrap connection | 01 |
| Axis 0,1,2 | Tuple positions x0,x1,x2, not physical units | 01 |
| Orientation; tail/head | Reference arrow; its starting/ending node | 02 |
| f, f_e | Edge field and its coordinate on ordered oriented edge e | 02 |
| D | Incidence matrix, −1 at tail and +1 at head | 02 |
| Df | Node divergence, arrivals minus departures | 02 |
| φ; Dᵀφ | Node potential; its head-minus-tail edge differences | 02 |
| Transpose ᵀ | Swap rows and columns | 02 |
| Rank; independent columns | Number of independent generating columns; zero combination has only zero coefficients | 02 |
| Elimination | Solve a row equation and substitute into the remaining equations | 02 |
| Simple cycle; circulation | Closed nonrepeating route; edge field with Df=0 | 03 |
| Cycle space | All real circulations on the declared graph | 03 |
| Tree; spanning tree | Connected graph without cycles; such a subgraph using all vertices | 03 |
| Leaf; chord | Node with one tree edge; graph edge outside chosen tree | 03 |
| Fundamental cycle c | +1 chord plus signed head-to-tail tree return path | 03 |
| Cut; cut space | Separation of node sets; span of signed indicator gradients, all Dᵀφ | 03 |
| Dot product; orthogonal | Sum of entrywise products; zero dot product | 03 |
| Coefficient; decoder | Scalar multiplier of a basis element; rule reconstructing the full state | 03 |
| Dimension; basis | Number of independent coordinates; independent generating list | 04 |
| Lexicographic order | Compare first tuple coordinate, then second, then third | 04 |
| Root; parent | Distinguished (0,0,0); decrement first nonzero coordinate | 04 |
| q_i; c_i | Open chord coefficient and its ordered fundamental cycle | 05 |
| Wrap edge; h_(a,j) | Axis endpoint 2→0 edge; its fundamental cycle for axis a and line j | 05 |
| w_(a,j) | Coefficient at a wrap chord, not a node value | 05 |
| W_a, μ_a, d_(a,j) | Sum of nine wrap coefficients, its mean W_a/9, and deviations from that mean | 05 |
| Σ | Sum over the stated index range | 05 |
| Winding | Net signed seam crossing, extended linearly to weighted circulations | 05 |
| s; r | Cycle sum from chord readings; retained tree remainder f−s | 06 |
| Memory; dynamics | Specified retained state with decoder; rule for change through time | 06 |

Notation safeguards: D is not the source's B. M_cell, R_cell, G_phase and O_K remain separately typed source geometry symbols and do not enter the finite graph calculations. The cut space and our chosen tree-remainder space both have dimension V−1 but are not identified. A coefficient's sign depends on the declared cycle orientation. The mean/detail representation is real/rational; integer inputs impose reconstruction compatibility, not arbitrary integer coordinate freedom.
