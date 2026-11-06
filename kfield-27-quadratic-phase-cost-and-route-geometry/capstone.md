# Capstone — Two routes, one declared cost, and an honest certificate audit

Allow three 55-minute periods: (1) typed inputs, ellipse and pullback; (2) ledgers, route comparison and proof; (3) source/precision audit, coupling, reconstruction and corrections. All numerical inputs are synthetic except the explicitly identified source cards. No internet, calculus or missing source matrix is needed to complete this assessment.

## Input packet

Use length unit L, time unit τ, detector unit D, a fixed origin (0,0)L and fixed orthogonal axes. For Tasks 1, 3–5 use G=[[2,1],[1,2]]L⁻². B=diag(2,1)L maps dimensionless u to displacement z=Bu/2. J=ΣΔt vᵀGv. Start (0,0)L, end (2,0)L and total duration 2τ. Admissible core paths have any finite number of positive-duration constant-velocity segments, with no obstacles or speed cap. Path A has velocities (1,0),(1,0)L/τ; path B has (1,1),(1,−1)L/τ; each listed segment lasts τ.

Task 2 is a **separate ruler contract**, not a substitution into that G: n₁=(1,0),d₁=L,n₂=(0,1),d₂=2L,o=(0,0)L,H=I. Use v=(−1,2)L/τ for two τ-long segments.

Source cards, available in full teaching context in Lesson 6 and provenance in sources.md: T20 names a least-cost certificate but supplies no numeric path, bounds or gap. S02 /branch_proofs/12 reports exact QPC linear-algebra closure. S03 AUD-008 names missing G_phase, C and complete W_qpc and stores **4.58938078934712923077736690075e-12** without the needed precision/interval bridge. AUD-009 provides missing-body status VERIFIED_NOT_LOADED. A separate spectral G_phase has been retrieved, but its equivalence to the locked route inputs is not supplied. Do not invent those inputs.

## Student tasks

### C27-CAP-01 — Evaluate and visualize

Compute q for velocities (1,2) and (1,−1)L/τ, then reverse each and retain all signed vectors. For displacement inputs, draw the q=1 ellipse with the exact diagonal and axis-crossing anchors from Lesson 1; label principal semiaxes. Show why diag(1,−1)L⁻² is not a positive form.

### C27-CAP-02 — Derive from rulers

Under Task 2's separate rulers, derive signed plane rates from Δp/Δt, compute the physical ruler matrix and give cumulative count and cost after each segment. Explain why the result cannot be claimed as a source route value without source ruler and time conventions.

### C27-CAP-03 — Check the complete congruence

Compute all four entries of W=BᵀGB/4. Use u-dot=(2,−2)/τ to calculate v and both costs. Recover u-dot from v and check T_BᵀWT_B=G. Explain the factor 1/4 and why this identity alone adds no dynamics.

### C27-CAP-04 — Keep the path ledger

For A and B, provide duration, signed velocity, endpoint, rate, segment cost and cumulative cost. Reverse B's segment order and report the changed history. Split A into four half-τ segments and provide the map back to its two original segments.

### C27-CAP-05 — Certify within a fixed domain

Use v-bar=D/T and retained deviations δ_i to prove the finite-route lower bound for the input packet. Give an attaining path, upper bound and gap. Reconstruct B's excess from its deviations. Explain the changed outcome if T becomes 4τ and what remains valid if an obstacle excludes the straight path.

### C27-CAP-06 — Audit precision and provenance

Audit the supplied T20/S02/S03 cards: separate the attributed source claim from what can be replayed here, list the missing certificate fields and preserve the full nonzero closure string. Independently compute 1/3−0.3333 under four-decimal positive truncation, provide its interval and reconstruction. Calculate the gap between bounds 3.9/τ and 4.1/τ. Explain why neither toy rule certifies the source closure.

### C27-CAP-07 — Propose a discriminating observation

Under synthetic y=kr with dimensionless r, give two factor pairs for y=6D. An independent calibration supplies r=3; determine and freeze k. For a second reading 7D with the same r, record prediction, signed residual and reconstruction. Name the observations and transfer specification needed to distinguish coupling candidates. Separate your route proof from any claim of measured energy transfer.

## Full worked key and 28-point rubric

Award four points per task, one for each specified component below. Award a calculation point for correct carried-forward work after a separately penalized arithmetic error; do not penalize the same error twice. Source fabrication or deleting residuals loses the relevant scope/retention point and requires correction before reporting mastery.

| Task | Point 1: typed inputs/domain | Point 2: operation | Point 3: reconstruction/classification | Point 4: retained information/boundary |
|---|---|---|---|---|
| 01 | G in L⁻²; rates τ⁻² and displacement cost dimensionless | 2+4+8=14 and 2−2+2=2; reversals same | Ellipse long semiaxis L on n₋, short L/√3 on n₊; correct anchors | Signed vectors retained; counterexample (0,1)L gives −1 for alternative matrix |
| 02 | Declare the separate spacings and H=I | a=(−1,1)/τ; G_ruler=diag(1,1/4)L⁻²; rate 2/τ² | Cumulative counts (−1,1),(−2,2); cumulative cost 2/τ,4/τ | Preserve signs, origin, two durations; source normalization still required |
| 03 | B's column map and u-dot units declared | GB=[[4,1],[2,2]]L⁻¹, BᵀGB=[[8,2],[2,2]], W=[[2,1/2],[1/2,1/2]] | v=(2,−1)L/τ; both costs 8−4+2=6/τ²; T_B=diag(1,2)L⁻¹ recovers (2,−2)/τ and T_BᵀWT_B=G | Two factors 1/2 give 1/4; identity is coordinate substitution, not new dynamics |
| 04 | Common start/end, time, G and segment interpolation | A contributions 2,2 per τ; B contributions 6,2 per τ | A endpoints (1,0),(2,0); B (1,1),(2,0); cumulative A 2,4; B 6,8 per τ | Reversed B endpoints (1,−1),(2,0), cumulative 2,8; split A contributes four 1/τ values; pair 1–2→A1 and 3–4→A2 |
| 05 | Finite positive-duration segments, fixed T, G positive, no obstacle | ΣΔt δ=0; mixed terms cancel; J=T v-barᵀGv-bar+ΣΔt δᵀGδ | v-bar=(1,0)L/τ; lower=upper=4/τ, zero gap; B deviations (0,±1)L/τ add excess 4/τ | At 4τ minimum is 2/τ for a different problem; obstacle preserves bound but removes straight attainment claim |
| 06 | Same units for bounds; source provenance distinguished | Residual 1/30000; interval [0.3333,0.3334); gap 0.2/τ | 3333/10000+1/30000=1/3; S02 exact claim preserved as attributed, no source replay claimed | Exact AUD-008 string retained; list full source matrices, order/units, precision, objective, domain, time/endpoints, path/bounds/gap and replay; no imported toy tolerance |
| 07 | y in D, r dimensionless, k in D | Pairs (2D,3),(1D,6); with r=3, k=2D | Frozen prediction 6D; e=+1D; 7D=6D+1D | Keep candidates and rows; independent calibration plus source state, timing/orientation/exposure and transfer law; no energy-transfer promotion |

For Task 1's drawing, the short-axis endpoints are ±(1/√6,1/√6)L; long-axis endpoints ±(1/√2,−1/√2)L; horizontal/vertical crossings are ±L/√2 on each axis. All satisfy q=1. The diagonal decomposition 3(s/L)²+(t/L)²=1 explains the smooth ellipse.

For Task 4, subdivision endpoints are (1/2,0),(1,0),(3/2,0),(2,0)L, cumulative costs 1,2,3,4 per τ. Dividing segment contributions by their durations recovers the constant rate; retaining the signed velocities additionally reconstructs positions. Costs alone cannot reconstruct direction.

For Task 6, an acceptable source audit explicitly says that the spectral-instance decimal matrix does not supply the locked C, complete W or certificate bridge. A source's exact claim and an auditor's missing-object report are separate records. VERIFIED_NOT_LOADED is a retrieval state, not a freshly checked theorem or a claim that the source is false.

For Task 7, acceptable discrimination includes independently measuring r under fixed orientation/exposure or testing two predeclared transfer laws under a controlled changed input that makes their predictions differ. Merely refitting k to each output does not distinguish them. The additional residual remains an observation channel for later decoding.

## Backward map: actual operations before assessment

| Capstone step and input→output | Explanation | Answered practice | Local diagnostic |
|---|---|---|---|
| 01: G,v→q; q=1→ellipse anchors | C27.01-E1/W1 | C27.01-P1, including plot | C27.01-D1 |
| 02: n,d,H,v,Δt→ruler matrix, signed rates/counts/cost | C27.02-E1/W1 | C27.02-P1a and remaining P1 | C27.02-D1 |
| 03: B,G,u-dot→W,v,cost and inverse | C27.03-E1/W1 | C27.03-P1a and remaining P1 | C27.03-D1 |
| 04: ordered velocities/durations→ledger and subdivision map | C27.04-E1/W1 | C27.04-P1 | C27.04-D1 |
| 05: fixed contract and δ→lower/upper bound proof and constraint comparison | C27.05-E1/W1 | C27.05-P1a and remaining P1 | C27.05-D1 |
| 06: cards/decimals→source missing-field audit and retained residual | C27.06-E1/W1 | C27.06-P1 | C27.06-D1 |
| 07: response/calibration→candidate factors, fixed prediction/residual and proposed observation | C27.07-E1/W1 | C27.07-P1 | C27.07-D1 |

No generalized eigenproblem, real laboratory motion calculation or continuum proof is assessed.
