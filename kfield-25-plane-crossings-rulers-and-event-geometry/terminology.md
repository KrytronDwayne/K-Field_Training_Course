# Terminology and notation

Read the entries in lesson order. Symbols refer to the synthetic Cartesian model unless explicitly labeled source-only. A numerical time such as “t in seconds” is shorthand for t/(1 s); equations retaining unit-bearing coefficients avoid this shorthand.

| Term/symbol | Meaning and units | First use |
|---|---|---|
| x(t), o | Full position and declared origin; m | L1 |
| n | Oriented unit normal; dimensionless components | L1 |
| n·w | Dot product: sum of matching component products | L1 |
| d>0 | Perpendicular spacing of one plane family; m | L1 |
| k | Integer sheet index, signed and dimensionless | L1 |
| s_k | Signed perpendicular distance to sheet k; m | L1 |
| q | n·(x−o)/d; unwrapped dimensionless sheet coordinate/cycles | L1 |
| Family | One declared n,o,d contract; not a physical family label | L1 |
| Normalization | Divide a nonzero vector by its length | L1 |
| Δ | Finite final-minus-initial change | L2 |
| v | Velocity, Δx/Δt for linear motion; m/s | L2 |
| n·v | Signed projected velocity; m/s | L2 |
| r, q̇ | Signed rate of q; s⁻¹; equal for constant-rate paths | L2 |
| Dot above a symbol | Instantaneous time rate; full derivative is recognition-only | L2 |
| Absolute value of r | Rate magnitude retaining no direction alone | L2 |
| T, f | Traversal period in s and unsigned frequency 1/T in Hz | L3 |
| π, rad | Circle constant and angle unit; full turn 2π rad | L3 |
| φ | Unwrapped phase 2πq; rad | L3 |
| 1/d | Spatial interval frequency; m⁻¹, distinct from Hz | L3 |
| λ, P, u | Wavelength (m), oscillator period (s), declared propagation speed (m/s) | L4 |
| f_diff | Absolute difference of f_1 and f_2 in Hz | L4 |
| Baseband | Lower-frequency output of a specified detector chain | L4 |
| THz | 10¹² hertz | L4 |
| Root, t* | A time at which selected signed distance equals zero | L5 |
| Bracket [a,b] | Closed interval with retained endpoint values and assumptions | L5 |
| Continuous | No jump on the stated interval; required for sign-change existence argument | L5 |
| Transverse passage | Crossing with nonzero normal rate at the event | L5/L7 |
| Contact | Here, a tangent zero returning to the same side | L5 |
| Bisection | Halving a bracket and evaluating its midpoint | L5 |
| Localization | Interval or singleton locating a root under a specified model | L5 |
| Measurement bound | Supplied range of possible measurement values; not a model residual | L5 |
| Gap | Interval lacking enough path information to assign its events | L5 |
| RA, LST | Right ascension and local sidereal time in compatible angular units | L6 |
| H | Unwrapped hour angle LST−RA, positive westward in this convention | L6 |
| Angular hour | 1/24 turn, distinct from elapsed clock hour | L6 |
| mod 2π, j | Equality up to whole turns; j is an integer branch label | L6 |
| Meridian events | H=2πj upper; H=(2j+1)π lower | L6 |
| Quadrature | H=±π/2 modulo 2π relative to meridian here | L6 |
| u(t) in L6 only | Unit sightline, dimensionless; distinct from propagation speed u in L4 | L6 |
| Event provenance | Source/card ID, clock, geometry, model and supporting records | L7 |
| p | Declared family polarity tag ±1, independent of travel direction | L7 |
| y, m, e | Original coordinate, model and residual, with y=m+e | L7 |
| E0, E_H | Named synthetic starts for seconds and hours; not actual UTC epochs | L7/capstone |

## Source-only symbols and scope guards

The input contract reserves B for the source-locked Cell3 basis with ICRS columns [a b c]; its intentional negative determinant must not be “fixed.” Family B in our ledger is only a family name. In the source, M_cell=BᵀB is the cell Gram metric, R_cell=M_cell⁻¹ its inverse; G_phase is a distinct phase metric. Matrix transpose (ᵀ) swaps rows and columns and matrix inverse reverses an invertible linear map; no matrix operation is assessed in this course. O_K is the source physical origin; reciprocal identities use x−O_K.

The source half-open cell interval includes −1/2 and excludes +1/2 on each coordinate. It is not a nearest-sheet rule. No nearest-integer rounding or tie convention is used in the event computations. G_eff, distance Q, Q_g and Q_nu, carrier order, chirality, parity, lifts and recursion systems remain source-local and are not equated to q, p or sheet index. Their advanced theories are outside this topical course, not hidden prerequisites.

## Evidence vocabulary

**Source fact:** what a pinned artifact actually states, with digest and pointer. **Observation:** a supplied measurement with its metadata; none is invented in this course. **Derived implication:** a result from declared inputs and operations. **Interpretation/inferred structure:** an explanation of relationships, distinguished from the calculation. **Proposed mechanism:** a candidate physical process requiring explicit inputs. **Reference theory:** standard mathematical/coordinate definitions used for comparison. **Unresolved information:** missing inputs, residuals, ambiguities, gaps or unverified source bodies retained explicitly. A source-reported proof status is not a fresh compiler run.
