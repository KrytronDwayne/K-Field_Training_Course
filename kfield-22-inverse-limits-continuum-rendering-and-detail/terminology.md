# Terminology and notation

|Term or symbol|Meaning and local convention|Introduced|
|---|---|---|
|Z; Z/3^d Z|Integers; their residues modulo 3^d|01|
|d, N, j|Positive depth, truncation depth, digit index; dimensionless|01,04|
|u_j|Balanced digit −1,0,1, or ordered triple of these; least significant first in addresses|01|
|t_d, a_d|Signed weighted digit sum; its nonnegative residue|01|
|A_d|Three-coordinate address set (Z/3^d Z)^3, with 27^d elements|01,03|
|π_d|Coordinatewise reduction from depth d+1 to d|01|
|Compatibility|Every deeper residue reduces to its stored shallower residue|01|
|δ, k|Address distance 3^(−k) for exactly k shared low-order digits; zero for identical complete histories|02|
|A∞, Z₃³|Set of complete compatible triple histories; not a finite residue set|03|
|Inverse limit|Whole compatible ladder under reduction maps|03|
|r, S_N|In the geometric-sum derivation only: scalar ratio and finite sum r+…+r^N|04|
|Σ|Sum over the stated index range; infinite sum is a limit of partial sums|04|
|z_N, z|Dimensionless normalized rendered partial vector and its real limit|04|
|B, r_N, r|Declared length-valued matrix; rendered displacement Bz_N and limit Bz. This r is not the geometric ratio|04|
|LU|Synthetic length unit, not a measured Cell3 calibration|04|
|O_K, x|Declared physical origin and absolute position; x−O_K is displacement|04|
|Infinity norm|Largest absolute coordinate; matrix version is largest absolute row sum|04|
|Absolute tail bound|Upper bound on remaining absolute contribution, retained with exact rule or unresolved continuation|04|
|Ordered pair|History and image retained together; equal images need not mean equal histories|04|
|f_d, g₂, composition ∘|Finite-prefix functions; composition means apply the right function first|05|
|Cylinder, pullback|Histories sharing a finite prefix; observation evaluated after reduction|05|
|P₀, P₁|Four-cell global and adjacent-pair averaging, equal weights|06|
|Q₀, Q₁|P₁−P₀ and I−P₁, retained between-pair and within-pair detail|06|
|I; transpose; projector|Identity map; row/column swap; operation P satisfying P²=P|06|
|Dot product, orthogonal|Sum of coordinate products; dot product zero|06|
|Filtration|Sequence of nested coarse spaces; infinite reconstruction requires a convergence contract|06|
|E, Q|A specified block averaging and I−E; product rules require explicit extra properties|06|
|Δf|f_t−f_s, signed finite difference across two labeled endpoints|06|
|ℓ², sequence 2-norm|Real square-summable sequence space; square root of sum of squared entries|07|
|Carrier, domain, action|Ambient objects; allowed inputs for one operator; its transformation rule|07|
|D, Dom(D)|Action (Dx)_n=nx_n; domain where Σn²x_n² is finite|07|
|Convergence mode|Criterion specifying what it means to approach a limit, e.g. ℓ² norm|07|
|Unbounded|No one finite constant bounds output norm by constant × input norm on the domain|07|
|Self-adjointness|Advanced operator property involving the adjoint and its domain; recognition only|07|

Reserved wider-series notation: M_cell=BᵀB and R_cell=M_cell^−1 are the Cell3 Gram metric and its inverse, whereas G_phase is a separate phase metric. None is required in core computations here. B in the illustrative diagonal example is explicitly synthetic, not the mature ordered ICRS Cell3 basis. The latter has intentional negative determinant and half-open cells [−1/2,1/2)^3; neither its numerical constants nor ownership rule is substituted by our examples. Address reduction is not nearest-integer rounding. No half-tie convention is needed for a residue operation.

Source vocabulary and status: “reported” identifies an archival assertion; “derived” identifies the course's explicit mathematical consequence; “synthetic” identifies authored inputs; “not supplied” identifies a missing contract or body, not a refutation. Compiler M03/M07/M08 authority is not automatically mathematical-backbone authority. No parity, chirality, metric, physical velocity or energy branch is merged here.
