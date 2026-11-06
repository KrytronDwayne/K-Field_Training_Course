# Terminology and notation

| Term/symbol | Operational meaning and units | Introduced |
|---|---|---|
| x(t), x_n | continuous-time expression or ordered sample, declared signal units | 1,4 |
| A,b | nonnegative amplitude and retained baseline, same units as signal | 1 |
| t,T,Δt | time, repetition period, sample spacing; seconds unless toy units stated | 1,4 |
| f,ω | cycles/s (Hz), radians/s; ω=2πf | 1 |
| φ,θ | phase offset; θ locally denotes geometric/source angle; state radians or degrees | 1,5 |
| radian | angle with arc length/radius one; full turn 2π | 1 |
| sine/cosine | vertical/horizontal unit-circle coordinate | 1 |
| AC,DC | varying departure and constant baseline; retain both | 1 |
| quadrature | quarter-turn phase displacement; source quadrature baseline Q has its separate four-angle definition | 1,5 |
| superposition | addition at corresponding coordinates with common units | 2 |
| signed factor/envelope | multiplying amplitude with sign / its nonnegative absolute bound | 2 |
| beat frequency | absolute-envelope peak rate for the stated two-tone convention | 2 |
| carrier | average-frequency factor in the taught two-tone identity | 2 |
| n,v,O,d | unit normal, velocity, origin, perpendicular positive ruler spacing | 3 |
| dot product | sum of matching-coordinate products | 3 |
| q,qdot,k | local spatial phase in cycles, signed cycles/s, integer harmonic index | 3 |
| λ | wavelength, length; not silently identified with geometric d | 3,6 |
| i | imaginary unit, i²=−1; powers repeat every four | 4 |
| a+bi | complex coordinates (a,b), including sign and phase | 4 |
| conjugate | a−bi; reflection of imaginary coordinate | 4 |
| exp(iθ) | cos θ+i sin θ in this course | 4 |
| Σ | finite sum over the stated index range | 4 |
| X_k | unnormalized DFT coefficient; same declared units as samples | 4 |
| DFT/inverse | minus-sign forward; plus-sign inverse divided by four | 4 |
| DC bin/Nyquist bin | constant bin 0 / alternating bin 2 for four samples | 4 |
| aliasing/modulo | distinct continuous frequencies share sampled values / wrap indices | 4 |
| R,Z | reference and comparison complex coefficients; ratio requires R≠0 | 5 |
| C₀,C₉₀,C₁₈₀,C₂₇₀ | source-angle ordered counts; retain origin α | 5 |
| M,Q,D₀,D₉₀ | two pair means and signed half-differences, counts | 5 |
| contrast_counts | M−Q, counts; called G by T35 | 5 |
| fractional_gain g | (M−Q)/Q, dimensionless; called G by spectral JSON formula | 5 |
| ρ,P | kinematic ratio and g/ρ, dimensionless; retain denominator domains | 5 |
| c | speed in consistent units; actual light speed only in physical source formula, toy c explicitly labeled | 5,6 |
| H,I,E,O | half-turn, identity, even projection, odd projection; O as operator differs from spatial origin O by context | 5 |
| nullspace | inputs mapped to zero by a stated operation; not erased measured inputs | 5 |
| parity | in this course, response to a half-turn; not carry parity/chirality | 5 |
| W_band,τ | band power, exposure duration; energy/time and time | 6 |
| E_eq,E_photon,N_eq | model energy equivalent, reference hc/λ, ratio of the two | 6 |
| h | Planck constant in physical reference; toy h explicitly labeled | 6 |
| interval [a,b] | ordered endpoints of stated bounds; no automatic probabilistic interpretation | 6 |
| calibration/responsivity | mapping from counts to physical input / output per input factor | 6 |
| transfer/down-conversion | mapping of time-dependent input to output / process producing lower-frequency response | 6 |
| qF | source phase-cost scalar nᵀG_phase n; not q cycles, joules, g or P | 7 |
| matrix,transpose | table acting by row dot products; column/row interchange | 7 |
| covariance | joint variation information; retain shared-input structure | 7 |
| JSON pointer/SHA-256 | source location / byte identity digest, not physical validation | 7 |
| m,r | represented component and full residual x−m, same units/order as x | 8 |
| linearity | weighted sums distribute across addition | 8 |
| closure residual | original minus reconstructed, or explicitly named recomputed-minus-reported value | 7,8 |

## Protected source-local symbols and branches

B is the ordered source-locked Cell3 basis, ICRS columns [a b c], intentional negative determinant. The half-open cell is [−1/2,1/2)³; cell ownership is separate from nearest-integer tie conventions. Use x−O_K for affine reciprocal identities. M_cell=BᵀB is its Gram metric, R_cell=M_cell⁻¹ its inverse; G_phase, G_eff, reciprocal bases, geometric distance Q, Q_g and Q_nu keep their source-local meanings. The count baseline Q in this course is explicitly local.

Gauge carriers are color-first C_3 direct-sum W_2; a weak-first ordering needs an explicit permutation. Detector parity, A1 carry parity, projective signs, chirality, family labels and primitive lifts are distinct. The dyadic and ternary recursions are distinct, as are ternary and Fibonacci-cutoff branches. This course does not derive or modify those broader structures.

No detailed-product proof, M19 extension, M20 closure, compiler-label authority or global-group uniqueness is inferred from these finite exercises. Keep the runtime source guards: hypotheses on E matter for detail products; M19 is not a premise of M20 core; accepted compiler M03/M07/M08 authority is distinct from mathematical backbone labels; admitted Z1,Z2,Z3,Z6 family and source-local uniqueness contracts remain separate. Matching dimensions or graph labels supplies neither an intertwiner nor a missing proof body. Cell3 and galaxy-derived cells have separate units, metrics and scales.
