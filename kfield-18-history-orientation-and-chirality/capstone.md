# Capstone — A recoverable history and orientation model

Build one report with ten labeled sections. All supplied values are synthetic, dimensionless teaching inputs. Keep original inputs, transformed parts, zero slots, complements and orientation operations. Use the source cards in Lesson 07 and the provenance in sources.md; no external lookup or missing certificate replay is needed.

Allow three 55-minute periods: period A, tasks 01–04 and 08; period B, 05–07 and 09; period C, 10, reconstruction checks and explanation revision. A calculator is optional. Show enough intermediate arithmetic that a partner can reproduce each answer. The answer key below is for checking after an independent attempt.

## Student tasks

### C18-CAP-01 — Word ledger

Input: alphabet {a,b}, maximum length 2. Generate all labels, including the root. Use order Ω,a,b,aa,ab,ba,bb and attach coefficients (2,−1,0,3,0,−2,4). Show prefix a on b and conditional removal a on ab and ba. Output: a labeled tree or table, amplitude ledger and explicit finite-cutoff rule.

### C18-CAP-02 — Square shift and reconstruction

Input: the Lesson 02 square S, f=(1,−2,5). Calculate Sf and S†Sf. Output: both vectors, terminal complement and exact reconstruction equation. Check squared-norm accounting with the retained terminal part.

### C18-CAP-03 — Rectangular map

Input: T:R²→R³, T(a,b)=(0,a,b), and output-space v=(5,2,3). Calculate T†v, TT†v and the complement. Output: a reconstruction equation, proof of norm preservation for general input (a,b), and a witness that T is not onto R³.

### C18-CAP-04 — Projector ledger

Input: S, P_0=diag(1,0,0), q_n=S^nP_0(S†)^n, and h=(−1,4,0). Calculate q_0 through q_3 and their ranks. Output: all selected vectors, checks of self-adjointness, idempotence and pairwise orthogonality, and reconstruction including zero slots.

### C18-CAP-05 — Orientation ledger

Input: B=diag(2,1,−4), ordered columns as written, forward time reader τ, four-coframe order (τ,θ¹,θ²,θ³). First rescale all spatial columns by positive 2; then reflect only the third column. Output: B, determinant and spatial/time/four-orientation signs at each stage. State how to recover the original basis and whether this transformed basis can silently replace locked Cell3.

### C18-CAP-06 — Correlation without identification

Input: paired order (L,even),(L,odd),(R,even),(R,odd), factor selectors from Lesson 06 and r=(2,−1,0,3). Construct Π=P_L⊗P_even+P_R⊗P_odd. Output: Π, Πr, (I−Π)r and reconstruction; verify Π²=Π and explain why its labels remain distinct.

### C18-CAP-07 — Source premise ledger

Input: Lesson 07 cards H,Q,O,C,F,R,A. Output: a table classifying the finite square index, the source radial index, the oriented coframe, γ_5/projector relations and Π_phys. Give the source pointers, the assumptions each needs and the missing replay objects. Explain the roles of source backbone M03 and M11 at recognition level. Do not attempt to reconstruct their proofs.

### C18-CAP-08 — Endpoint and domain comparison

Input: square S from task 02, rectangular T from task 03, and the explicitly defined infinite U from Lesson 02. Output: a table of input defect, output defect, kernel/cokernel dimensions and index. Explain why S is not an isometry, T is an isometry not onto, and U's infinite statement cannot be transferred to the three-state truncation or used as the missing definition of source T_0.

### C18-CAP-09 — Angular and spin counts

Input: the supplied dimension rules of Lesson 06, cutoff m=3. Output: angular total, spin-paired total, C₂ at ell=3, split dimensions at ell=2 and the ell=0 exception. State what the counts leave unspecified about physical energy and occupation.

### C18-CAP-10 — A commutator and a separate determinant witness

Input: A=diag(1,−1), B=[[0,1+i],[1−i,0]]. Compute AB, BA and [A,B]. Contrast the commuting pointwise real pair diag(1,2), diag(3,4). Then use A_0=diag(4,1,1/4), S=diag(2,1,1/2), D=diag(1,ω,ω²), ω³=1 with ω=−1/2+i√3/2, Y_u=S, Y_d=DS^−1D. Here S is the square-root matrix, not the history shift. Output: S², S^−1, Y_d, Y_uY_d, determinant and commutativity check. Classify what this proves and what it does not predict.

## Full worked key and 100-point rubric

Each task is worth 10 points. Award method credit for correct operations with one propagated arithmetic slip; do not count that slip repeatedly. A materially wrong domain or evidence claim loses the designated scope points even if its arithmetic is correct. A completed report should correct all reconstruction failures before delivery; the score is feedback, not permission to erase residual information.

### Answer 01 — 10 points

Levels are Ω; a,b; aa,ab,ba,bb, totaling 1+2+4=7. Attach the supplied coefficients in exactly that order, including zeros on b and ab. Prefix a sends b→ab. Removal sends e_ab→e_b and e_ba→0, not e_Ω. One valid rule is: truncate prefix outputs beyond length 2 to zero and retain the affected terminal coefficients separately; alternatively enlarge the display and explicitly say so. An unqualified drawing cutoff is insufficient. **Points:** labels/root 3; complete ordered coefficient ledger 3; prefix/removal 2; explicit cutoff handling 2.

### Answer 02 — 10 points

Sf=(0,1,−2), S†Sf=(1,−2,0). Terminal complement is (I−S†S)f=(0,0,5). Reconstruction: (1,−2,0)+(0,0,5)=(1,−2,5). Squared norms are 30 for f, 5 for Sf and 25 for the retained component, so 30=5+25. **Points:** shift and reverse 4; complement 2; reconstruction 2; norm ledger 2.

### Answer 03 — 10 points

T†v=(2,3), TT†v=(0,2,3), complement=(5,0,0); sum=(5,2,3). For every (a,b), squared norm of T(a,b) is 0+a²+b², equal to that of the input. No input reaches (1,0,0), so T is not onto its stated codomain. Its inverse works on {(0,a,b)} only. The original output-space squared norm is 38=13+25. **Points:** maps/complement 4; reconstruction 2; general norm identity 2; missing output and inverse scope 2.

### Answer 04 — 10 points

q_0=diag(1,0,0), q_1=diag(0,1,0), q_2=diag(0,0,1), q_3=0. Ranks 1,1,1,0. On h their outputs are (−1,0,0),(0,4,0),(0,0,0),(0,0,0). Transpose leaves each unchanged; diagonal squaring fixes each 0/1; distinct selections have no shared 1, so their products vanish. Sum q_0+q_1+q_2=I_3, giving h exactly. q_2's zero output does not change its rank. **Points:** maps/ranks 4; algebra checks 3; labeled outputs/reconstruction 3.

### Answer 05 — 10 points

| Stage | Basis | det B | Spatial sign | Time sign | Four sign |
|---|---|---:|---:|---:|---:|
| Start | diag(2,1,−4) | −8 | − | + | − |
| Positive scale 2 | diag(4,2,−8) | −64 | − | + | − |
| Third-axis reflection | diag(4,2,8) | +64 | + | + | + |

Reflect the third column again, then divide all spatial columns by 2 to recover the original. The temporal direction is unchanged. These are synthetic bases; a reflection cannot silently replace the authoritative ordered, negative-determinant Cell3 basis. **Points:** bases/determinants 4; separate signs 3; inverse operations 1; source distinction 2.

### Answer 06 — 10 points

Π=diag(1,0,0,1). Πr=(2,0,0,3), complement=(0,−1,0,0); their sum is r. Squaring diagonal 0/1 entries gives Π²=Π. First-factor and second-factor selections commute because they act on independent labels. L and even are not synonyms: the four-pair carrier also contains (L,odd). The complement keeps information outside the correlation. **Points:** projector 2; both outputs 3; reconstruction/idempotence 3; factor distinction 2.

### Answer 07 — 10 points

| Entry | Classification and source | Required structure or gap |
|---|---|---|
| Square index 0 | Fresh synthetic finite check, Lesson 02; capstone task 08 | Three-state S with both defects |
| Radial index −1 | Source report, S02#/backbone_sequence/13/index | Source radial T_0 domain and replay definition; not supplied by finite S |
| K4 orientation | Declared premises, S02#/backbone_sequence/13/proof | Left-handed spatial coframe, forward covector and explicit order |
| γ_5 and P_L/P_R | Conditional source construction, same module definitions/proof | Compatible metric signature, Clifford matrices and adjoint convention |
| Π_phys | Source correlation, same module correlated_projector | Spacetime and exterior-parity factors separately defined |

S03#/findings/8 names B_8 and T_0 among missing replay objects and assigns the missing-body gate VERIFIED_NOT_LOADED. Backbone M03 supplies the Lucas/address and distinct recursion context; M11 supplies exterior matter/parity carrier context. They are recognition-level dependencies, not completed proofs in this course. Matching compiler numbers or dimensions supplies no intertwiner. **Points:** five classifications with assumptions 5; exact module/audit pointers 2; explicit gaps 2; dependency distinction 1.

### Answer 08 — 10 points

| Map/domain | Input defect | Output defect | dim kernel | dim cokernel | Index |
|---|---|---|---:|---:|---:|
| S:R³→R³ | diag(0,0,1) | diag(1,0,0) | 1 | 1 | 0 |
| T:R²→R³ | zero on R² | diag(1,0,0) | 0 | 1 | −1 |
| U:l²(N_0)→l²(N_0) | zero | root projector | 0 | 1 | −1 |

S loses e_2's norm. T preserves every input norm but misses e_0. U has no terminal slot, so it has no terminal defect. U is explicitly defined separately from the source radial T_0. Equal index alone does not identify their operators or carriers. **Points:** defect entries 4; dimensions/indices 3; scope explanation 3.

### Answer 09 — 10 points

Angular total is 1+3+5+7=16=(3+1)². Spin pairing doubles it to 32. C₂ at ell=3 is 3·4=12. At ell=2 the j=5/2 and j=3/2 blocks have dimensions 6 and 4, summing to 10=2·5. At ell=0 retain only j=1/2 of dimension 2. These are supplied representation rules, not a physical Cell3 energy operator, energy spacing or occupation prediction. **Points:** totals 3; C₂ 1; split and exception 4; physical boundary 2.

### Answer 10 — 10 points

AB=[[0,1+i],[−1+i,0]], BA=[[0,−1−i],[1−i,0]], so [A,B]=[[0,2+2i],[−2+2i,0]]. The pointwise pair both multiply to diag(3,8), so their commutator is zero. This restriction does not apply to all real matrices.

For the separate witness, S²=diag(4,1,1/4)=A_0 and S^−1=diag(1/2,1,2). Multiplying diagonal entries gives Y_d=diag(1/2,ω²,2ω⁴)=diag(1/2,ω²,2ω). Thus Y_uY_d=diag(1,ω²,ω) and determinant ω³=1. Both Y matrices are diagonal, so they commute. The supplied A_0 and phase label establish a finite determinant identity. This does not establish nonzero CP merely from determinant 1 or predict physical CKM/PMNS values. **Points:** commutator products 3; commuting contrast 1; witness matrices/determinant 4; scope 2.

## Prior-learning map

Every step uses an earlier explanation, worked example, answered practice and diagnostic. In the table, a stem denotes the four concrete IDs with suffixes -E1, -W1, -P1 and -D1, each printed in its lesson. No capstone operation requires recognition-only extension proofs.

| Step | Earlier lesson | Required ID stem |
|---|---|---|
| C18-CAP-01 | lesson-01 | C18.01 |
| C18-CAP-02 | lesson-02 | C18.02 |
| C18-CAP-03 | lesson-03 | C18.03 |
| C18-CAP-04 | lesson-04 | C18.04 |
| C18-CAP-05 | lesson-05 | C18.05 |
| C18-CAP-06 | lesson-06 | C18.06 |
| C18-CAP-07 | lesson-07 | C18.07 |
| C18-CAP-08 | lesson-02 | C18.S01 |
| C18-CAP-09 | lesson-06 | C18.S02 |
| C18-CAP-10 | lesson-07 | C18.S03 |
