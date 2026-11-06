# Terminology and notation

| Term/symbol | Meaning and unit/domain | First lesson |
|---|---|---|
| Channel / response identity | Named detector pathway and its wavelength-response definition | 1 |
| nm | Nanometre, 10^-9 metre; nominal wavelength is not a response curve | 1 |
| Count | Instrument output unit; not automatically energy or power | 1 |
| Gain / exposure e | Instrument setting / acquisition duration in seconds | 1 |
| Calibration | Documented input/output relation with conditions and reference | 1 |
| Sensor normal +z | Perpendicular direction in the declared toy bench frame | 1 |
| t / support | Elapsed midpoint seconds / contributing interval or sample set, explicitly stated | 1 |
| Acquisition key | Device, session, sequence and channel; timestamp accompanies it | 2 |
| Null / absent / zero | Explicit missing numeric entry / missing expected acquisition / numeric value | 2 |
| Flag / mask | Diagnostic state and reason / named view's parallel validity record | 2 |
| A, C | Spectral count and same-row Clear count (Clear is abbreviated C in formulas) | 1 |
| r=A/C | Dimensionless same-row Clear-reference ratio on its declared valid domain | 3 |
| delta | Exact ratio minus displayed ratio; signed rounding closure | 3 |
| R, s, a | Declared reversal; (x+Rx)/2 same component; (x-Rx)/2 inverted component | 4 |
| H, E, O, I | Two-position shift on four-point circle; even/odd/identity operations | 4 |
| Parity | Sign under the explicitly named operator; R parity and H parity differ | 4 |
| Dot product | Sum of matching-entry products | 4 |
| Nullspace | Inputs a comparator maps to zero | 4 |
| DFT / Fj | Four-sample discrete Fourier transform / complex coefficient at index j | 4 |
| i | Imaginary unit, i*i=-1; coefficient a+bi has two signed coordinates | 4 |
| Phase / magnitude | Cycle position encoded in complex coefficients / size without position | 4,6 |
| Aliasing | Different native indices produce identical sampled weights | 4 |
| Harmonic | Integer cycle count relative to a declared period | 4 |
| Ternary ladder | Source ladder multiplying by 3: 1,3,9,27 | 4 |
| q,k / comb | Unwrapped toy phase in cycles, integer event index / fixed event list | 5 |
| Ephemeris / sidereal | Versioned astronomical positions / relative to celestial directions | 5 |
| m,d_i | Mean over named support / signed detail x_i-m in input units | 6 |
| k in lesson 7 | Locally scoped calibration factor, output units/count; distinct from event index k | 7 |
| delta_t | Shared clock offset in seconds | 7 |
| Identifiability | Whether supplied outputs determine the requested separate inputs/parameters | 7 |
| Prospective / exploratory | Frozen before new outcome inspection / revised using inspected outcomes | 8 |

Evidence labels: synthetic input (authored); derived transform (arithmetic from named inputs); source-reported observation (archive statement); inferred structure (interpretation); proposed mechanism (candidate process); reference theory (comparison model); unresolved information (retained incomplete account). None automatically promotes another.

Avoid cross-course collisions: this course does not use Q for a projector or for distance. In T35, Q is a source-local quadrature baseline; it is not a Cell3 distance. M_cell, R_cell, G_phase and G_eff retain their packet types and are not required for the finite student arithmetic. The toy +z frame is not ICRS. The DFT index is not a backbone/compiler module label.
