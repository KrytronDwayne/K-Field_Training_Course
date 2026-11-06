# Terminology and notation

|Term or symbol|Meaning, type and units|Introduced|
|---|---|---|
|L=(L₁,L₂,L₃)|Dimensionless signed address, entries −1,0,1; subscript indicates entry|Lesson 1|
|Cartesian product|All ordered combinations from coordinate menus|Lesson 1|
|Window|27 half-step nodes; distinct from 27 complete cell volumes|Lessons 1–2|
|Vertex / edge center / face center / center|Three / two / one / zero nonzero entries in L|Lesson 1|
|Vector|Ordered components describing displacement; entrywise addition and scaling|Lesson 2|
|B=[a b c]|Ordered basis columns, units of length; classroom rows are printed explicitly|Lesson 2|
|O_K; classroom O|Declared origin position; O abbreviates O_K only in the analogue|Lesson 2|
|q=L/2|Dimensionless half-address|Lesson 2|
|p|Position O+Bq, unit U in the analogue|Lesson 2|
|d=p−O|Displacement from origin, unit U|Lesson 2|
|U|Arbitrary classroom length unit; never nm or a Cell3 numerical constant|Lesson 2|
|z|Dimensionless integer cell-owner triple, floor(q+1/2)|Lesson 2|
|floor(t)|Greatest integer ≤t; evaluated entrywise for triples|Lesson 2|
|u=q−z|Dimensionless retained within-cell coordinate in [−1/2,1/2)³|Lesson 2|
|Half-open|Left boundary included, right boundary excluded|Lesson 2|
|λ|Integer sheet label L₁+L₂+L₃, from −3 through 3|Lesson 3|
|Permutation|Rearrangement; identical entries do not create different rows|Lesson 3|
|Dot product g·d|Sum of three corresponding component products|Lesson 3|
|g_λ|Reciprocal sheet vector whose dot product with each basis column is 1; unit inverse length|Lesson 3|
|B⁻ᵀ|Recognition notation for inverse-transpose; not a required computation|Lesson 3|
|χ|Node polarity (−1)^λ: +1 even, −1 odd; dimensionless|Lesson 4|
|r₃|λ mod 3: unique remainder 0,1,2 in λ=3k+r₃; dimensionless|Lesson 4|
|k|An integer used locally to express parity or division remainder; not a node address|Lesson 4|
|Antipodal|L and −L, with physical points reflected about O|Lesson 5|
|Equivalence class / quotient|Grouped members / collection of groups under a declared relation|Lesson 5|
|v|Canonical pair representative, first nonzero entry positive; center v=0|Lesson 5|
|s|Member orientation ±1 with L=s v for noncentral rows; N/A at center|Lesson 5|
|Even / odd function under negation|Value preserved / sign reversed by L→−L|Lesson 5|
|Singleton|One-member center class|Lesson 5|
|Registry|All typed per-node records plus checks; not just aggregates|Lesson 6|
|R_L|L_recovered−L, dimensionless inverse closure discrepancy; retained per row|Lesson 6|

Reserved source notation stays outside the core calculations: M_cell=BᵀB is the Cell3 Gram metric, R_cell its inverse; G_phase is a distinct phase metric. None is being replaced by the classroom B or by a reciprocal normal. Detector parity, A1 carry parity, chirality and family labels are not alternate names for χ. Source compiler M03 and mathematical backbone M03 are different naming systems. The present source references mean the mathematical backbone module.
