# Capstone — A retained finite transport dossier

Build a small linked-state model, check its loop action and time update, and explain which objects correspond to S02 M13. All numerical model inputs below are synthetic. The archival bounds in step 07 are source statements. Do not claim to replay an unavailable certificate.

Use three 55-minute periods: steps 01–04 in period A; steps 05–06 in period B; steps 07–08 and checking the dossier in period C. Use exact fractions. Include all input states, link directions, ordered products, coefficients, transformed states and remainders. A list of invariant scalar answers alone is incomplete. The last section is a teacher answer key; attempt the tasks before reading it.

## Tasks

### C17-CAP-01 — Transport and reverse (8 points)

At sites x and y, U_xy=−i and ψ_y=1+i. State its direction, calculate the transported state, recover ψ_y, and compare squared moduli. As a two-component check apply diag(−1,i) to (2,1) and invert it. Output: both complete transport/recovery records.

### C17-CAP-02 — Compare in one frame (12 points)

Set ψ_x=2 with the scalar inputs from step 01. Let G_x=−1 and G_y=i. Find d_x, U′_xy, both transformed states, d′_x and G_xd_x. Recover ψ_x using the retained difference. Output: old and new descriptions and a covariance equality.

### C17-CAP-03 — An ordered loop (10 points)

At three sites use U01=Z=diag(1,−1), U12=X=[[0,1],[1,0]], U20=I. Specify the basepoint and travel path for U01 U12 U20. Multiply the links, apply the result to (1,0), and compare with exchanged assignments U01=X, U12=Z. Conjugate the original loop by G0=Z. Output: complete matrices and the order comparison.

### C17-CAP-04 — An invariant action (10 points)

With β=2 AU, find F=I−U_loop and S=β ReTr(F) for step 03 before and after conjugation by Z. Also verify the scalar loop with links (i,1,i) and frame changes (−1,i,1), using the same β. Output: transformed scalar links, both loop types, F and action values. Explain why matching actions do not identify the configurations.

### C17-CAP-05 — A conservative step (15 points)

Take Lhat=diag(0,2) TU⁻¹, τ_C=1/2 TU and ψ=(1+i,2). Form C=(I−iτ_C Lhat)(I+iτ_C Lhat)⁻¹. Check self-adjointness, real time, dimensionless product and denominator invertibility. Compute C, C†, Cψ, C†C and recovery. Output: hypothesis checks and full state record, including norm before and after.

### C17-CAP-06 — Metric weights (20 points)

Begin with squared length of (1,2) under the 2D metric diag(4,1) LU². Then use synthetic M=diag(4,1,16) LU². Calculate R, δ, wedge²R in order (12,13,23), H_E=δ^(1/3)R and H_B=δ^(2/3)wedge²R. Using J=[[0,0,1],[0,−1,0],[1,0,0]], verify determinants and J H_B Jᵀ=H_E⁻¹. State units, show the effect of M→4M, and calculate the historical-exponent determinants at numerical δ=64. Output: typed matrices and a clearly separated historical comparison. Do not identify M or J with an unloaded archival numerical object.

### C17-CAP-07 — A bounded source claim (15 points)

Using lesson 07 and sources.md, transcribe the four S02 bounds exactly. Identify the domain hypotheses, energy scale, known displayed precision and missing replay fields. Give the source ID, pointer and SHA-256. Then independently compute min(d_root,2c_*)E0 for synthetic d_root=3/10, c_*=1/20, E0=H_N/τ_R. Output: a source card with unavailable fields labeled and a separate toy computation. No numerical replay of the archival certificate is assigned.

### C17-CAP-08 — What is conserved? (10 points)

For step 05 compute N, Q_L and Q_L/N at time zero, after one step and after two. Recover the original state. Retain the one-step remainder relative to the original state. Explain the difference among this finite theorem, the source certificate report and a continuum comparison. Map your dossier's links, loop, action, Cayley update and metric blocks to S02 M13 without asserting identical carriers or coefficients. Output: conservation table, remainder/reconstruction and scoped interpretation.

## Backward map: every operation is taught and answered earlier

| Step | Explanation | Worked example | Independently attempted practice with answer | Diagnostic |
|---|---|---|---|---|
| C17-CAP-01 | C17.01-E1, lesson-01 | C17.01-W1 | C17.01-P1 | C17.01-D1 |
| C17-CAP-02 | C17.02-E1, lesson-02 | C17.02-W1 | C17.02-P1 | C17.02-D1 |
| C17-CAP-03 | C17.03-E1, lesson-03 | C17.03-W1 | C17.03-P1 | C17.03-D1 |
| C17-CAP-04 | C17.04-E1, lesson-04 | C17.04-W1 | C17.04-P1 | C17.04-D1 |
| C17-CAP-05 | C17.05-E1, lesson-05 | C17.05-W1 | C17.05-P1 | C17.05-D1 |
| C17-CAP-06 | C17.06-E1, lesson-06 | C17.06-W1 | C17.06-P1 | C17.06-D1 |
| C17-CAP-07 | C17.07-E1, lesson-07 | C17.07-W1 | C17.07-P1 | C17.07-D1 |
| C17-CAP-08 | C17.08-E1, lesson-08 | C17.08-W1 | C17.08-P1 | C17.08-D1 |

## Full worked answer key and point rubric

**01 — 8 points:** U_xy maps y→x (1). −i(1+i)=1−i; inverse i restores i(1−i)=1+i (2). Both squared moduli are 2 (1). The matrix output is (−2,i) (1); inverse diag(−1,−i) returns (2,1) (2); both norms squared are 5 (1).

**02 — 12 points:** Uψ_y=1−i and d_x=1+i (2). G_y⁻¹=−i and U′=(−1)(−i)(−i)=1 (2). ψ′_x=−2, ψ′_y=i(1+i)=−1+i (2). d′=−2−(−1+i)=−1−i=G_xd_x (3). Reconstruction d_x+Uψ_y=(1+i)+(1−i)=2, with both descriptions retained (3).

**03 — 10 points:** Basepoint 0, path 0→2→1→0 (2). U_loop=ZX=[[0,1],[−1,0]] and it sends (1,0) to (0,−1) (3). Exchanged assignments yield XZ=[[0,−1],[1,0]]=−ZX, sending (1,0) to (0,1) (3). Z(ZX)Z=XZ verifies conjugation (2). This exchange comparison is not a general formula for reversing a path.

**04 — 10 points:** F=[[1,−1],[1,1]], Tr(F)=2, S=4 AU (3). After conjugation F′=[[1,1],[−1,1]], still trace 2 and S′=4 AU (2). Scalar links become (−1,i,−i), product −1, scalar F=2 and S=4 AU (3). Keeping different matrices, dimensions and links explains why equal action is insufficient to identify a configuration (2).

**05 — 15 points:** Lhat†=Lhat, τ_C real, τ_C Lhat=diag(0,1) dimensionless; A=diag(1,1+i) has determinant 1+i≠0 (4). C=diag(1,(1−i)/(1+i))=diag(1,−i) (3); C†=diag(1,i), C†C=I (2). The output is (1+i,−2i) (2). Squared norm is 2+4=6 initially and finally (2). The adjoint returns (1+i,2), preserving the full components (2).

**06 — 20 points:** The warm-up is 4·1²+1·2²=8 LU² (2). R=diag(1/4,1,1/16) LU⁻², δ=64 LU⁶; wedge²R=diag(1/4,1/64,1/16) LU⁻⁴ (4). H_E=diag(1,4,1/4), H_B=diag(4,1/4,1), both dimensionless (4). Their determinants equal 1 and J H_B Jᵀ=diag(1,1/4,4)=H_E⁻¹ (3). Scaling M by 4 multiplies δ by 64, divides R by 4 and area factors by 16, leaving normalized blocks unchanged; retain M's scale separately (3). Historical a=2/3,b=4/3 give determinant powers δ and δ², so numerical 64 and 4096, not mature normalization. Historical block units are LU² and LU⁴ (3). Explicitly label the matrix and J synthetic (1).

**07 — 15 points:** Correct transcription ε_E<0.007744166, ε_B<0.015868134, α≤0.5244, Δ>0.10185916 H_N/τ_R (4). State fixed native finite compiler, site-indexed compact-group links, positive native plaquette/detail coefficients and c_*>0; E0 is energy because action/time is energy (3). Missing exact compiler/rung identifier, matrices, coefficient list, interval algorithm/working precision and replay object/command; displayed digits do not define working precision (3). Source S02 /backbone_sequence/12/proof, SHA-256 6f3e555ed161ef3311b31dcf64c003f4f8ec493f56d22356cf8d162467c1a2f3; S03 /findings/8 identifies replay gaps (2). Independently min(3/10,2/20)=1/10 gives E0/10; label this synthetic and not a replay (3).

**08 — 10 points:** States (1+i,2), (1+i,−2i), (1+i,−2) all have N=6, Q_L=8 TU⁻¹ and normalized expectation 4/3 TU⁻¹ (3). Two C† steps recover the initial state (1). Retained remainder (0,−2−2i) added to initial reference gives the one-step state (2). Finite identities are proved under finite hypotheses; archived bounds remain source-reported without their replay object; a continuum comparison requires its own domain, limiting object and control (2). Dossier objects match the operation types in M13—ordered links/loops, trace action, Cayley rational map, normalized metric blocks—without identifying the synthetic coefficients, state spaces or J with unavailable source objects (2).

Total: 100 points. Award arithmetic partial credit for a correct method with a local slip; do not double-penalize its consistent propagation. Essential repairs regardless of score: reversing a link silently, discarding full states, mixing historical/mature exponents, conflating Q_L with Q_L/N, or claiming fresh certificate/continuum proof. Reattempt the corresponding lesson practice before final acceptance. No convergence proof or unavailable certificate calculation earns required points.
