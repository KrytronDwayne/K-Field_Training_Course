# Terminology and notation

| Term/symbol | Meaning and contract | First taught |
|---|---|---|
| Integer | Whole number, positive, zero, or negative | 01 |
| ceil(t), floor(t) | Least integer ≥t; greatest integer ≤t | 01 E1 |
| nint(t) | ceil(t−1/2); lower neighbor at either signed half-tie | 01 E1 |
| Half-tie | Input halfway between adjacent integers | 01 E1 |
| [−1/2,1/2) | Includes −1/2, excludes +1/2 | 01 E1 |
| Integer translation | nint(t+m)=nint(t)+m for integer m | 01 P1 |
| Cell owner | floor(q+1/2), centers q−owner in the half-open cell | 01 E2 |
| Projective ray, r | Here a class of positive triples under positive common scaling, represented by first coordinate 1 | 02 E1 |
| Normalization magnitude | Original first coordinate; must be retained separately if original triple is needed | 02 E1 |
| a,b,c | Ordered coordinate slots; not lengths or basis columns in this course | 02 E1 |
| g | Nonnegative integer generation, not another course's address depth | 02 E1 |
| K_g | Scale 27^g | 02 E1 |
| Q_g | Componentwise nint(K_g r), an integer-count triple; not a metric or detail operator | 02 E1 |
| epsilon_g | Signed count-coordinate residual Q_g−K_g r; each entry in [−1/2,1/2) | 03 E1 |
| epsilon_g/K_g | Ratio-coordinate difference Q_g/K_g−r | 03 E1 |
| Decoder | r=(Q_g−epsilon_g)/K_g; reconstructs the supplied normalized ray | 03 E1 |
| C_g | Carry Q_g−27Q_(g−1), g≥1; C_0 is undefined here | 04 E1 |
| S,A | C_b+C_c and C_b−C_c at one generation; retain C_a separately | 04 E2 |
| Same parity | Both even or both odd; S congruent A modulo 2 | 04 E2 |
| Side-mode lattice | Integer pairs (S,A) with same parity; only this membership condition is used | 04 E2 |
| delta, prime mark | Signed difference between two input coordinates; prime marks the second input | 05 E1 |
| R,R',T,T' | Names of synthetic rays/comparisons, not metrics | 05 W1/P1 |
| Terminal residual | Residual at the final retained generation, required for exact finite decoding | 06 E1 |
| sum_(j=1..g) | Add terms with integer index j from 1 through g | 06 E1 |
| Finite compiler | Deterministic, reversible ledger transformation under its metadata contract | 06 E1 |
| Branch | Named source or synthetic input identity, never inferred from matching integer rows | 03 D4; 05 E2 |

All ray ratios and scales are dimensionless. “Count coordinate” distinguishes the scaled integer/residual representation from its ratio-coordinate decoder; neither denotes a measured length or energy. Source input precision is part of the branch metadata.

Reserved series notation M_cell, R_cell, G_phase, O_K, and B is not needed for these finite operations and is not reassigned. Likewise projective signs, detector parity, chirality, and family labels remain separate notions, not synonyms for the even/odd side-mode condition.
