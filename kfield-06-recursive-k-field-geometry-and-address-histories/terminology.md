# Terminology and notation

| Term or symbol | Meaning and convention | First taught |
|---|---|---|
| recursion | repeated stated operation on its output | 01 |
| root, child, parent | start; generated object; generating object | 01 |
| depth | number of rule applications, typed by system | 01 |
| [a,b) | includes a, excludes b | 01 |
| floor(t) | greatest integer at or below t | 01 |
| n2 | dyadic subdivision depth, nonnegative integer | 01 |
| j,k,b | binary child index, parent index, retained bit; j=2k+b | 01,06 |
| node | sampled point | 01 |
| volume/cell | complete region; count is dimensionless, volume magnitude has cubic length units | 01 |
| boundary vertex/corner | geometric endpoint/corner, whether owned or excluded | 01 |
| incidence | pairing of a cell with a corner; shared corners produce multiple incidences | 01 |
| B | three ordered edge columns; physical Cell3 and classroom analogue separately typed | 01,03 |
| Lucas window | 27 half-step nodes from three choices per axis | 01 |
| Lucas Group | 27 complete Cell3 volumes, outer basis 3B | 01 |
| 9B Supergroup | 729 complete Cell3 volumes, equivalently 27 Groups | 01 |
| modulo m | integer remainder class for positive integer m | 02 |
| standard representative | remainder in 0 through m−1 | 02 |
| congruent | difference divisible by the specified modulus | 02 |
| d3, A_d | ternary address depth; set of three residue coordinates modulo 3^d | 02 |
| Z | integers; Z/3^d Z denotes residue classes | 02 |
| cardinality | number of objects, not identity of their types | 01–02 |
| g_rung,n_rung | nonnegative integer exponents used only in the rung equation | 02 |
| scale factor s | factor on lengths; areas use s^2, volumes s^3 | 03 |
| B_(p,n) | source scaled-basis family 3^p 2^(−n)B, not automatically a fixed outer boundary | 03 |
| lambda | sum i+j+k of integer half-step labels in lesson03 | 03 |
| sheet | sampled points with the same lambda value | 03 |
| balanced ternary | digits −1,0,+1 with place values 1,3,9,... | 04 |
| epsilon0,... | signed digits, stored least significant first | 04 |
| representative | integer rendering of a modular class; balanced and standard forms can differ | 04 |
| compatible history | successive addresses obey their declared parent map | 05 |
| bonding map | source ternary parent operation: reduction modulo the parent's modulus | 05 |
| coarse record | lower-depth description with several possible finer continuations | 06 |
| detail/residual coordinate | retained bit/digit removed by coarse description, including zero | 06 |
| invertible/lossless record | output plus metadata determines the complete original finite input | 06 |
| r,e,t | balanced low-word integer, removed high digit, reconstructed integer | 06 |

Depth and order are always stored. Binary root-outward bits and ternary low-to-high digits are explicitly different orders. Lambda labels depend on the declared half-step grid. No use of nearest-integer rounding occurs; floor-based interval ownership is not a nearest-integer tie convention.

The broader packet reserves M_cell for the Cell3 Gram metric, R_cell for its inverse, G_phase for a separate phase metric, and O_K for a physical origin. They are not new required operations in this course. If an affine physical formula is added later, it must use x−O_K or p−O_K where needed. No symbol in this glossary silently identifies a physical basis with the classroom analogue.
