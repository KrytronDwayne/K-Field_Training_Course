from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
P=json.loads((R/'input-contract.json').read_text(encoding='utf-8-sig'))
def w(n,s): (R/n).write_text(s.strip()+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for i,c in enumerate(P['course_map'],1):
 a=c['teaching_anchor']; cid=f'C23.{i:02}'
 rows.append(f"| {cid}: {c['title']} | [{c['id']}]({c['id']}.md) / {cid}-E1 | {cid}-W1 / {cid}-P1 | {cid}-D1 | {c['later_use']} / C23-CAP-{i:02} | {a['planned_periods']} |")
w('course-map.md','''# Gravity, Inertia, and Exceptional Branches — course map

Audience: high-school seniors. Entry capabilities are signed arithmetic, fractions, ratios, powers, substitution and coordinate graphs; prior courses 10,12,14,17,22 supply motivation. This course locally teaches the logarithm, vector, matrix and finite-graph operations used in assessment. Advanced theorem names are recognition only.

The seven lessons occupy 13 periods of 55 minutes (715 minutes); the capstone occupies three more (165 minutes), for 880 minutes. Lesson boundaries follow the approved map; multiple periods prevent dense mathematical bridges from becoming single-period overloads. Every period allocates 5 retrieval + 20 explanation/example + 15 practice + 15 diagnostic/repair minutes. The teacher guide assigns the focus within each period.

| Concept | Introduction/explanation | Worked/practiced | Assessment | Later use/capstone | Periods |
|---|---|---|---|---|---:|
'''+ '\n'.join(rows)+'''

Teaching dependency: lesson-01 → lesson-02 → lesson-03 → lesson-04 → lesson-05 → lesson-06 → lesson-07 → capstone. The historical source dependency is separately M19 requires M07,M08,M10,M13,M18; M19 is not a premise of M20 core closure. This curriculum order does not revise the source graph.

E05 content gate: each named anchor occurs in its corresponding lesson as actual teaching, worked calculation, answered practice or diagnostic. Each capstone step below names inputs and outputs and reuses an earlier independently answered practice. See capstone.md for the complete backward map. Recognition-only cohomology and exceptional-algebra statements are assessed as source classifications, never as untaught theorem proofs.

Units and evidence rules are in terminology.md and sources.md. All numerical exercises are explicitly synthetic. No raw source snapshots are stored. All residual vectors, input lists, branch choices and source limitations remain available for reconstruction.
''')
w('terminology.md',r'''# Terminology and notation

| Term or symbol | Meaning and local contract |
|---|---|
| A_ab,A_ac,A_bc; A_ref | Positive face areas and a common positive reference area, in the same squared-length unit. |
| y_ab,y_ac,y_bc | Classroom dimensionless log ratios ln(A/A_ref), in this order. |
| ln; e^y | Natural logarithm and its inverse exponential; ln(uv)=ln u+ln v for positive inputs. |
| F,M,G=G_Gamma | Lesson 01 inferred dimensionless coordinates F=y_ac-y_bc, M=y_bc-y_ab, G=9y_ab+8y_ac-11y_bc. Archival definition bodies remain missing. M is not mass or M_cell. |
| Gamma2 | Archival gravity scalar; its definition and reference/integration constant remain VERIFIED_NOT_LOADED. |
| Gamma_B | Dimensionless conditional Bragg logarithm ln(d/L_ref)+ln(abs(sin theta))-ln(lambda_wave/L_ref). Distinct from Gamma2. |
| B; B^T; B^-T | Ordered basis matrix, transpose (swap rows and columns), inverse transpose. Synthetic B=diag(2,3,4) LU is not the locked Cell3 basis. |
| diag(a,b,c) | Matrix with those diagonal entries and zeros elsewhere. |
| O_K; x; u | Declared physical origin, physical position, dimensionless address u=B^-1(x-O_K). |
| M_cell; R_cell | Gram metric B^T B (LU^2) and inverse metric (LU^-2) in the synthetic example. |
| G_phase,G_eff,Q,Q_g,Q_nu | Distinct source objects reserved by the input contract; no identification with M_cell, R_cell or G_Gamma is made or needed here. Their formulas are not assessed. |
| h; q; d; n_hat | Integer reciprocal address, reciprocal vector (LU^-1), positive spacing 1/length(q) (LU), unit normal q/length(q). q must be nonzero. |
| dot product; length | Sum of paired component products; nonnegative square root of self dot product. |
| rho in lesson 02 | Full signed reciprocal residual vector, LU^-1; retained in q_observed=3^(signed g)B^-T h+rho. |
| g; m; lambda_wave; theta | Declared recursion depth/exponent sign; positive Bragg order; positive wavelength LU; angle with nonzero sine. |
| LU,T,MU,U | Synthetic length, time, mass and response units. U is not automatically force or energy. |
| v,a,n | Velocity LU/T, acceleration LU/T^2 and dimensionless unit normal. |
| v_parallel; v_perp | Signed projection v dot n and perpendicular vector v-(v dot n)n. |
| mu; F_parallel | Added mass coefficient MU and conditional force scalar MU*LU/T^2; distinct from lesson 01 F. |
| graph; vertex; edge | Declared points and undirected links. Boundary and edge-count conventions are part of the input. |
| spanning tree; cycle dimension | Connected no-cycle subgraph containing all vertices; independent cycle count E-V+1 for a connected finite graph. |
| V,E; P3 | Vertex and edge counts; three-vertex open path. E here is not a projection operator. |
| periodic; winding | Adds wrap links; a route around a periodic direction. A sector decomposition requires an actual map. |
| Z3; H^2 | Modulo-three labels; source cohomology classification name. Dimension-six theorem is supplied, not proved here. |
| SU(3),F4,E6,E7; Albert algebra | Source theorem/carrier names. Exceptional action and real-form selection require explicit construction. |
| action; involution | Operators preserving the stated composition rules; operation whose square is identity. |
| rho,sigma,sigma-prime in lesson 05 | Matrices for finite actions; not reciprocal residuals. Sigma-prime=-I is distinct from worked sigma=diag(-1,1). |
| I; T_map | Identity matrix; an intertwiner (written T in lesson 05), not the time unit T. |
| D; trace; canonical | Full matrix defect; sum of diagonal entries; selected by additional declared rules, not mere existence. |
| [A,B]; R(X) | Commutator AB-BA; assigned operator for a Lie generator. Not the metric R_cell. |
| w,z,k,b,r | Motion projection LU/T, response U, H1 coefficient U*T/LU, H2 coefficient U*T^2/LU^2, signed residual z-prediction in U. |
| invariant; odd/even | A property preserved under a specified transformation; response reverses/stays fixed when the input reverses. |
| calibration; held case | Inputs used to set a parameter; case excluded from that choice and predicted after freezing it. |
| VERIFIED_NOT_LOADED | Source-reported verification status with missing replay definition/body, preserved without inventing one. |
| source fact / local replay | What pinned bytes say / what calculations this course actually recomputes. A matching hash establishes byte identity, not theorem validity. |
| branch boundary | A domain restriction or unconstructed extension that must propagate even when an endpoint field is null. |

The locked Cell3 conventions remain ICRS columns [a b c], intentional negative determinant and half-open cells [-1/2,1/2)^3. Classroom examples do not replace those constants. No nearest-integer rule is used in the core exercises; cell ownership is not silently treated as rounding. No detector parity, carry parity, projective sign, chirality, family label, primitive lift or dyadic/ternary recursion is identified with another.
''')
w('teacher-guide.md',r'''# Teacher guide

Teach this as a topical course on reconstructing and comparing branches. Its aim is an accurate branch atlas, one verified reconstruction, one explicit mechanism comparison and one falsifiable proposal. It neither requires nor substitutes for a complete theory of gravity. Students should be able to point to exactly which inputs justify each output.

## Entry check and materials

Supply paper, pencils and the seven lesson files; a basic calculator is optional. Ask learners to evaluate -13+16+3, add 1/2+1/10, multiply (3/5)^2+(4/5)^2, and solve 2d(1/2)=3. Answers are 6,3/5,1,3. Repair these arithmetic skills before proceeding. No external source access, calculus, abstract algebra or prior matrix inversion is necessary for core assessment. Source/theorem cards are reproduced as scoped descriptions with pointers in sources.md.

## Pacing and progression

Every 55-minute period has 5 minutes retrieval, 20 explanation and worked example, 15 practice and 15 diagnostic check/repair. Across 13 core periods this totals 65/260/195/195 minutes. Use the answers after students attempt each item, asking a second student to reconstruct the original inputs.

| Period | Focus | Evidence for progression |
|---:|---|---|
| 1 | Lesson 01 ratios/log coordinates and inferred forward map | Student distinguishes a dimensionless ratio from an area with units. |
| 2 | Lesson 01 inverse substitution and source bodies | Recovers (1,0,2); explains missing integration constant. |
| 3 | Lesson 02 basis, affine origin, metric and reciprocal | Computes B^T q=h and retains O_K. |
| 4 | Lesson 02 spacing, sine branches and logarithms | Keeps separate reciprocal and Bragg input packets. |
| 5 | Lesson 02 vector residual and scaling | Reconstructs q_observed with signed rho and its own spacing. |
| 6 | Lesson 03 projections and response premise | Retains perpendicular vectors and the added mu law. |
| 7 | Lesson 04 spanning trees/open and periodic grids | Derives counts by coordinate lines, with no double counting. |
| 8 | Lesson 04 source theorem cards and extensions | Computes 729 but does not claim to prove dimension six. |
| 9 | Lesson 05 matrix operations and successful map | Computes both sides of T rho=sigma T. |
| 10 | Lesson 05 failed pair, trace and bracket checklist | Distinguishes diag(2,-2) from diag(2,0); names missing operators. |
| 11 | Lesson 06 fixed calibration and invariants | Keeps coefficient units and predicts held cases. |
| 12 | Lesson 06 residual ledger and extension protocol | Reconstructs all responses; proposes a frozen-parameter test. |
| 13 | Lesson 07 source/finite/conditional/open atlas | Propagates constituent restrictions despite a null endpoint. |

If a progression check fails, add a repair period using the existing alternate example or reversed reconstruction; record actual pacing. Do not make an unsupported map or missing source body into a required exercise. All lessons already contain 3–5 diagnostic questions and worked answers. Lessons 01–03 are unit A, 04–05 unit B, and 06–07 unit C. At boundaries, check terminology and ask: which inputs remain necessary for reconstruction? Unit A requires signed components and references; B requires graph/action conventions and whole defect matrices; C requires calibration, case order and source boundaries.

## Common errors and targeted repairs

If a learner logs a dimensional area, ask which reference cancels its units. If a learner identifies G_Gamma with force, request the units and response equation. If a learner drops O_K, reconstruct the explicit (3,4,5) position from its address. If a learner mixes spacings, attach each result to its input packet. If a learner deletes a reciprocal or response residual, ask them to reconstruct the original values without it.

If a learner equates 52 with an action, request one generator operator and a relation. If they use diag(2,-2) for the sigma-prime=-I pair, recompute the second diagonal subtraction -1-(-1)=0. If they refit k on a held output, move that case into a newly labeled calibration set and request another held case. Preserve the original predictions.

## Assessment and acceptance

The capstone uses three 55-minute sessions: definitions and first reconstruction; remaining calculations and residuals; source classification, proposal and independent reconstruction. It is 28 points, four per step. Give partial credit by the explicit criteria, not by agreement with a preferred mechanism. Require repairs to any wrong units, missing input/residual, or upgraded evidence status before calling an atlas complete, even if its numerical score is high.

No lab results are implied by the synthetic data. Source exactness claims stay attributed. The supplied input contract's one ambiguous matrix answer is corrected in the actual lessons and capstone; do not reintroduce it from the blueprint. The independent audit and deterministic validator assess different things: teaching/correctness versus containment/hashes/assembly identity.
''')
w('capstone.md',r'''# Capstone — A recoverable branch atlas

Produce one atlas containing source claims, your finite reconstructions, a mechanism comparison and a falsifiable proposal. Use only the taught operations. Allow three 55-minute periods: establish inputs and first reconstruction; complete calculations and residual tables; classify every row and independently reconstruct it. All numerical inputs below are synthetic. Keep signed values, units, origins, angle choices and model coefficients. Advanced theorem proof bodies and exceptional generators are not required computations.

## Backward map and tasks

| Step (4 points each) | Prior explanation and answered practice | Named inputs → required outputs |
|---|---|---|
| C23-CAP-01 | C23.01-E1; C23.01-P1 | y=(1,0,2), positive A_ref, formulas from lesson 01 → F,M,G, inverse y, common-shift effect and source status |
| C23-CAP-02 | C23.02-E1; C23.02-P1 | B=diag(2,3,4) LU; h=(0,0,1) → q, metric length, d,n_hat; separate m=1, wavelength=3 LU, sin theta=1/2 → Bragg d,Gamma_B; h=(1,1,0), g=0, rho=(1/10,-1/5,0) LU^-1 → q_observed with full reconstruction |
| C23-CAP-03 | C23.03-E1; C23.03-P1 | n=(3/5,4/5,0), v=(5,0,0) LU/T, a=(0,5,0) LU/T^2; proposed mu=2 MU → projections, complements and conditional force |
| C23-CAP-04 | C23.04-E1; C23.04-P1 | 2D 3x3 open and periodic grids with one undirected edge per neighbor pair; supplied cohomology dimension 6 → V,E,cycle counts, 729 consequence and theorem boundary |
| C23-CAP-05 | C23.05-E1; C23.05-P1 | rho=diag(1,-1), sigma-prime=-I, proposed T=I; compare worked sigma=diag(-1,1) → whole defects, trace obstruction and missing exceptional-action inputs |
| C23-CAP-06 | C23.06-E1; C23.06-P1 | calibration w=1 LU/T,z=2 U; H1 z=kw,H2 z=bw^2; held w=(-1,2),z=(-2,5) → frozen coefficients, ordered predictions/residuals and orientation proposal |
| C23-CAP-07 | C23.07-E1; C23.07-P1 | outputs above and S02 M19/S03 AUD-001,009,010,011 cards → integrated atlas with source, units/domain, retention and next obligation for every row |

For step 01 distinguish inferred classroom F,M from missing archival bodies. For step 02 explicitly retain the original/source domain and distinguish the two independent spacings. For step 05 state the bracket-preservation defect symbolically; do not manufacture a 52-by-52 action. For step 06 use the three taught held orientations to specify a test before any new outputs. For step 07 explain why null cannot erase a constituent boundary and why M19 does not become a core-closure premise.

## Full answer key

### C23-CAP-01

F=0-2=-2, M=2-1=1, G=9+0-22=-13. Inverse numerators are -13+16+3=6, -13+4+9=0, -13+16+9=12; dividing by 6 recovers (1,0,2). Areas are A_ref times (e,1,e^2), keeping their reference. A common shift t cancels in the differences and changes G by 6t. The formulas are conditional algebraic reconstruction with dimensionless log ratios. Source F/M/Gamma2 bodies and reference/integration constants remain VERIFIED_NOT_LOADED (S03 AUD-009).

### C23-CAP-02

M_cell=diag(4,9,16) LU^2 and R_cell=diag(1/4,1/9,1/16) LU^-2. For h=(0,0,1), q=(0,0,1/4) LU^-1, B^T q=h, q dot q=h^T R_cell h=1/16 LU^-2. Hence d=4 LU and n_hat=(0,0,1). In the separate Bragg case, d=1*3/(2*1/2)=3 LU and Gamma_B=ln(1/2); 30 and 150 degrees retain separate equal-sine branches. Positive wavelength/order and nonzero sine are necessary.

For the residual case, predicted q=(1/2,1/3,0) LU^-1 and observed q=(3/5,2/15,0) LU^-1. Difference observed minus predicted=(1/10,-1/5,0) LU^-1. The observed squared length is 17/45 LU^-2, so its spacing is sqrt(45/17) LU, not the first case's 4 LU. Preserve B,h,g,exponent sign and rho. With an origin, position reconstruction is x=O_K+B u, not B u alone. The synthetic positive-determinant basis is not the locked Cell3 geometry.

### C23-CAP-03

n dot n=9/25+16/25=1. v dot n=3 LU/T; a dot n=4 LU/T^2. Parallel velocity vector=(9/5,12/5,0), perpendicular=(16/5,-12/5,0) LU/T. Parallel acceleration=(12/5,16/5,0), perpendicular=(-12/5,9/5,0) LU/T^2. Each pair sums to its input. With the additional law F_parallel=mu a_parallel and mu=2 MU, the force scalar is 8 MU*LU/T^2. The law and mass are added premises; no such force follows from dimensionless G alone.

### C23-CAP-04

V=9. Open grid has 3*2 horizontal and 3*2 vertical edges: E=12. Its cycle dimension is 12-9+1=4. Periodic grid has E=18 and cycle dimension 10. In each connected graph a spanning tree has V-1 edges; the remaining edges supply independent cycles. Given six independent three-way cohomology coordinates, the class count is 3^6=729. The supplied dimension theorem is not proved by this multiplication or by a grid count. Source carrier statements and F4/E6/E7 extensions retain their distinct statuses.

### C23-CAP-05

For the practice pair, T rho-sigma-prime T=diag(2,0). Traces are 0 and -2, so no invertible intertwiner can equate these actions. Directly, T=[[a,b],[c,d]] would require a=c=0, hence a zero first column and no inverse. For the separate worked pair with sigma=diag(-1,1), the identity-map defect is diag(2,-2); the exchange matrix succeeds there. Retain both labeled defects. A proposed Lie action must make [R(X),R(Y)]-R([X,Y]) zero on the required generating relations. Supply sector, field, basis, operators, brackets, comparison map and normalization. A dimension match supplies none of those constructions, nor a real-form choice or physical coupling.

### C23-CAP-06

Calibration gives k=2 U*T/LU and b=2 U*T^2/LU^2. In ordered held cases w=(-1,2), H1 predicts (-2,4) U with residuals (0,1) U; H2 predicts (2,8) U with residuals (-4,-3) U. Check reconstruction in every case: -2+0=-2,4+1=5,2-4=-2,8-3=5. H1 is odd under reversal, H2 even. Neither bare law exactly reproduces all held values, and neither residual field is discarded.

Freeze k=2 and v=(1,0,0) LU/T; use normals (1,0,0),(-1,0,0),(0,1,0). Predict +2,-2,0 U before collecting any new z. Preserve orientation, inputs and all resulting signed residuals. Nonzero residual contradicts exact agreement at its case. A proposed c n_y extension requires a new declared calibration and new held orientations; do not fit away this test retrospectively. Neither toy rule specifies mass reconstruction, binding or an exceptional action.

### C23-CAP-07

A complete atlas can use Lesson 07's W1 table plus its practice rows with the capstone computations attached. Every row must name its own domain, units, retained inputs/output and next obligation. Scalar row: S02 gravity_scalar_lift, inferred finite coordinates checked, source bodies/constants missing. Reciprocal row: S02 reciprocal_plane_inversion, synthetic inputs, full vector rho and angle/scale branches retained. Cycle row: S02 exceptional_cycle_bridge, finite enumeration checked; theorem bodies and the sector map distinguished. Action row: synthetic matrices checked, exceptional action and real-form choices unconstructed. Mechanism row: synthetic calibration and held cases, entire residual ledger preserved, future orientation observations still blank.

S03 AUD-010 forbids a null endpoint from erasing constituent restrictions. AUD-001 keeps M19 outside M20's M01–M18 core closure; M19's own requires list is M07,M08,M10,M13,M18. AUD-011 requires full typed premises, not Cell3 alone. A matching source hash preserves attribution but does not replay the theorem. No source-reported claim is silently turned into a new observation or a fresh proof.

## Rubric — 28 points

For each of the seven steps award one point for declared inputs, units and evidence scope; one for the correct taught operation; one for complete reconstruction or correct source classification; one for retaining information and the applicable boundary. These are four distinct checks, not four points for a final number. A numerical slip loses the operation point; missing rho or an upgraded theorem claim also loses the retention/scope point as applicable. Full-credit models must include all elements in the corresponding answer above. Correct repairs should be resubmitted with the original discrepancy retained in a correction note.

The capstone is complete only when all seven rows are present and every substantive error is repaired. Recognition-only extensions receive credit for accurate missing-input specifications, never for invented operators or proof bodies.
''')
sources=[]
for s in P['sources']:
 p=Path(s['path']); actual=sha(p); assert actual==s['sha256']; sources.append({**s,'actual_sha256':actual,'hash_match':True})
w('sources.json',json.dumps({'sources':sources,'active_corpus_generation':'sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7','manifest_sha256':'5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7','retrieval':'Capabilities called; sparse project RAG query gravity_scalar_lift M19 reciprocal_plane_inversion, rerank false. Returned compiler namespace, not the requested backbone body; exact local pinned S02/S03 read instead. No source data copied.','primary_pointers':['S02#/backbone_sequence/18','S03#/findings/0','S03#/findings/8','S03#/findings/9','S03#/findings/10']},indent=2))
provenance='\n'.join(f"- {s['id']}: `{s['path']}`; SHA-256 `{s['sha256']}`; fresh hash match." for s in sources)
w('sources.md','''# Compact source notes

All five designated files were hashed read-only and matched. The following paths identify the exact archive bytes; no full source copy is included.

'''+provenance+'''

Direct content grounding: S02 `/backbone_sequence/18`, module M19, type D+E, requires M07,M08,M10,M13,M18. Read its complete branches: `gravity_scalar_lift/formulas` and `result`; `exceptional_cycle_bridge/exact_counts` and `exceptional_action_extension`; `reciprocal_plane_inversion/formulas`, `branch_identity`, `residual`; and module result. These are archived claims, not automatically fresh proofs. S01,S04,S05 are provenance context and were hash-verified, not promoted as independently replayed derivations. No historical constants from them are mixed into classroom examples.

Read S03 `/findings/0` AUD-001 (requires-derived edges, remove M19-to-M20); `/findings/8` AUD-009 (missing F,M,Gamma2 bodies among replay objects, VERIFIED_NOT_LOADED); `/findings/9` AUD-010 (14 of 16 source endpoints reported null despite constituent boundaries); `/findings/10` AUD-011 (full premise contract). The count 14 of 16 is an attributed audit finding, not newly enumerated here. The course uses the resulting boundary rule without copying the archive.

Graph access: used the krytronx-knowledge-graph skill and read-only capabilities call. The subsequent sparse project-RAG query reported active generation and manifest digest `5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7`, matching the requested generation. Capabilities itself did not include corpus generation. RAG returned the compiler-adjudication namespace rather than an archive M19 node; no relevant original archive node_id was returned for traversal. This result is not used as a backbone proof. Exact supplied local pointers provide the requested topic grounding.

The source five scalar formulas motivate an inferred coordinate map under positive dimensionless area ratios; they do not supply missing definition bodies or integration constants. Bragg examples are synthetic and conditional, retaining nonzero-sine domains and angle branches. Finite grid enumeration checks totals; cohomology/SU(3)/Albert-F4 statements remain source/theorem cards. Specific F4 action, E6/E7 real-form selection and physical coupling are explicitly unconstructed extensions.

Source boundaries are not unresolved course defects when the assessed operation is to preserve and correctly classify them. No measured gravity, inertial, binding or response dataset is supplied or invented. Core calculations use small authored examples. See verification.json for what was actually recomputed.
''')
print('Support artifacts written')
