# Terminology and notation

| Term / symbol | Meaning and domain | First teaching |
|---|---|---|
| premise / domain hypothesis | supplied assumption / condition restricting an operation | 1 |
| state coordinate | a value selecting a state within an allowed family | 1 |
| dependency A → B | B uses A, not automatically the converse | 1 |
| namespace | named identifier system; compiler and backbone M labels remain separate | 2 |
| B=[a b c] | mature ICRS column basis, entries in nm, negative determinant intentional | 1 |
| x, O_K, q | position and origin in nm; dimensionless address in x=O_K+Bq | 1 |
| z, u | integer cell address and local coordinate, q=z+u | 1 |
| floor / half-open | greatest integer no larger than input / include left but exclude right endpoint | 1 |
| m,h | local mean and signed half-difference, not mass or Planck constant | 2 |
| witness / hash / pointer | supporting object / byte fingerprint / location within structured source | 2 |
| proof / replay | implication under premises / execution on specified inputs | 2 |
| calibration / observation | reference-to-response relation / acquisition record | 2 |
| protocol / preregistration | executable plan / version frozen before check outcomes | 2,5 |
| theta=(theta1,theta2) | synthetic response contributions, dimensionless | 3 |
| H, y=H theta | measurement row table and its output; synthetic dimensionless examples | 3 |
| s,d | sum and difference channels, dimensionless; d is not a distance here | 3 |
| rank / null direction | independent measured combinations / parameter change with zero output change | 3 |
| identifiable / equal-output family | unique under model and domain / inputs sharing an output | 3 |
| g,R | toy gain and responsivity, dimensionless product example; R is not R_cell | 3 |
| phase / beat frequency | cycle position / cycles per second; neither implies force or power | 3 |
| candidate mechanism | proposed causal account with parameters and predicted observables | 4 |
| bit | binary value, 0 or 1 | 4 |
| uncertainty interval | declared admissible range from a specified contract, not erasure rule | 4 |
| p,r | frozen prediction and retained residual r=y−p | 5,6 |
| UTC midpoint / exposure | common time convention at collection midpoint / duration of collection | 5 |
| replication | new acquisition with independently inspectable protocol and calibration | 6 |
| null / absent / string | distinct raw data kinds and presence states | 7 |
| A,c in decoder | 3-by-2 synthetic design and two coefficients; not candidate A or basis column c | 8 |
| dot product | multiply matching entries and add; used for residual convention | 8 |
| phi | synthetic dimensionless phase 2 times first-address displacement | 8 |
| i | complex unit with i²=−1 | 8 |
| trivialization / sector | representation of combined line by scalars / admitted class of states | 8 |
| syndrome | retained residual coordinates; small analogue has one, source M17 reports seven | 8 |

Source-only notation is separately scoped in sources.md: M_cell, R_cell, G_phase, G_eff and the several Q symbols are not silently merged. EG principles and M modules are source reading labels. UV/light/reg/heavy/cap/induced are the six M15 factor labels; the displayed scalar example teaches multiplication without requiring determinant-line theory. “Source-reported” is an evidence attribution, never a numeric value or an automatically verified status.
