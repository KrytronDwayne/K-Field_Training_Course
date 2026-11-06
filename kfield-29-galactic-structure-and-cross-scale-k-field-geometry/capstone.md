# Capstone: a source-traced cross-scale comparison

Create one comparison portfolio with eight numbered responses. Use the locally supplied cards below and the linked lessons. All finite input numbers in the tasks are synthetic unless explicitly labeled as source-reported. Preserve signed coordinates, zero counts, domain failures and source roles. Calculators are optional. No new operation is required.

Allow three 55-minute periods: (1) source ledger and tasks 01–03; (2) calculations and tasks 04–06; (3) frozen prediction, tasks 07–08, and repair using the rubric. A successful portfolio explains its operations, not just its answers.

## Tasks

### C29-CAP-01 — Directions and axes

Compute the unit direction for RA=90°, Dec=0°, and its directed and axial angles to e_x=(1,0,0). Then give the two angles for e_x and -e_x. State which direction data must survive an antipodal discovery transform and whether a radial distance or intrinsic galaxy axis follows from sky position alone. Use G04 pp1,3 as the source role.

### C29-CAP-02 — Two maps and their domains

Use the response card in lesson 02: u=n·N, kappa=nu π/(hu), q_resp=kappa n; F=sqrt(3+2cos psi_ab+2cos psi_ac+2cos psi_bc)/3 and G_star=D/F. In case A take n=e_x,N=e_z,h=1L,nu=1. In case B take the separately stipulated closure-consistent phases (2π/3,4π/3,2π/3), all weights 1 U_D, and D=sum w(1-cos psi). In case C take D=2 U_D,F=1/2. Classify each result and specify retained flags. Separately use reciprocal row (1,0)/L, point (5/4,0)L and phi=1/4 to find a plane index. Explain why these operations do not supply a calibrated galaxy force law.

### C29-CAP-03 — Typed center reconstruction

Take A=diag(2,3)L, phi=(1/4,1/2), k=(1,-1). Find c_k=A(k+phi), A phi, A⁻¹ and M⁻¹ for M=AᵀA. Recover k. Explain why phi is not a physical center. Compare the source determinant signs of the galaxy cell (G01) and mature Cell3 (S02), keeping their units distinct.

### C29-CAP-04 — Common grammar, distinct cells

For A'=diag(2,1,4)L calculate s_ab,s_bc,s_ac and verify closure. Compare M' with M=diag(1,4,9)L² from the earlier basis diag(1,2,3)L. Explain why the common closure does not identify the physical normals. Identify the missing input in a proposed physical ratio of galaxy reconstruction length to Cell3 nm. Cite G02 p4 and the source comparison card.

### C29-CAP-05 — Metric and nearest-center boundary

For M=[[2,1],[1,2]]L² and q=(1,1), compute squared distance and distance; verify positivity using the taught square decomposition or minor test. Explain why diag(1,-1)L² fails. For a=(1,0)L,b=(0.9,0.1)L,phi=0,q=(0.49,0.49), reconstruct x and compare squared distances to centers 0 and b. State precisely what this comparison proves. Keep both signed residual vectors.

### C29-CAP-06 — Full occupancy and residual ledger

Enumerate sheet populations for half-step labels in {-1,0,1}³ and distinguish availability from observed counts. Toy discovery memberships are P-left={a}, P-middle={b,c}, P-right={d}; holdout memberships are {},{e,f,g},{h}. Report both vectors and their signed difference. Split P-middle into {b} and {c} and show parent reconstruction. For x=(1,0,0),c=(4/5,0,0), calculate vector residual, length, angular miss and radial mismatch ||c||-1. Then describe the c=0 angular case.

### C29-CAP-07 — Frozen comparison

Read the seven-row source-comparison.md ledger. Report the signs of all seven holdout-minus-discovery differences in sheet order -3 through 3, and state whether the reported 27-state correlation has been freshly replayed here. Confirm the source population sum 57,076+57,305. In the toy A=I₂ L example, retain the original assignment for x=(3/10,1/2)L at phi=(1/4,1/2), then a proposed phi'=(1/3,1/2): give both centers, residuals and phase shift. Explain why the second branch is exploratory and list the source control families.

### C29-CAP-08 — Explicit transformation and independent prediction

For A=diag(1,2,3)L compare A with 2A: calculate V, M, root scaling and M/V^(2/3). Then design a future test of the G02 p19 hard-mode depletion proposal. Name what is frozen and what observation contradicts the prediction. As a finite example use the lesson-08 equal-exposure four-state rule: H1,H2 versus C1,C2, contrast=mean hard fraction minus mean comparison fraction. Evaluate toy counts (1,1,3,3) and (3,3,1,1). State how a real 27-state test retains all residuals and missing selection/distance fields.

## Full answer key

01. The vector is e_y=(0,1,0). Dot(e_x,e_y)=0, so both angles are 90°. For e_x,-e_x the directed angle is 180° and axial angle 0°. Preserve original directions and identifiers or a reversible sign/representative record. Sky position supplies neither intrinsic orientation nor physical distance. G04's actual fitting used directed positions; projective discovery did not redefine the observations.

02. A has u=0, so kappa and q_resp are undefined and downstream response fields are null with u_zero. B has cosines -1/2, so F²=(3-3)/9=0. The closure relation holds because 2π/3+2π/3=4π/3. D=3·(3/2)=9/2 U_D, while G_star is null with transfer_zero; even 0/0 would be undefined. These are symbolic domain cards, not asserted replayed source directions. C gives 4 U_D. The independent reciprocal row yields 5/4-1/4=1, an integer plane label. G03 is historical Cell3 relative response with no absolute gravity calibration, while G04 defines galaxy plane addresses. Preserve inputs, weights, phases and flags.

03. k+phi=(5/4,-1/2), c_k=(5/2,-3/2)L and A phi=(1/2,3/2)L. A⁻¹=diag(1/2,1/3)L⁻¹, M=diag(4,9)L² and M⁻¹=diag(1/4,1/9)L⁻². Apply A⁻¹ to c_k to recover (5/4,-1/2), then subtract phi to get (1,-1). Phi is dimensionless, A phi has L units. G01's determinant is positive in reconstruction units cubed; S02's is negative in nm³. Preserve intentional ordering and physical origin O_K in Cell3 affine coordinates.

04. s_ab=(1,-1/2,0)L, s_bc=(0,1/2,-2)L, s_ac=(1,0,-2)L. Addition gives s_ac exactly. M'=diag(4,1,16)L² differs from diag(1,4,9)L². The perpendicular vectors (1/2,1,1/4)/L and (1,1/2,1/3)/L are not parallel; common cancellation does not fix metric or normal. A physical galaxy radial calibration and declared cross-domain mapping are missing for the proposed physical scale quotient.

05. Mq=(3,3)L² and qᵀMq=6L², distance=sqrt(6)L. Positivity follows from (x+y)²+x²+y²>0 for nonzero q; equivalently leading entry 2 and determinant 3 are positive. The indefinite diagonal matrix gives -1L² for (0,1). In the skew example x=(0.931,0.049)L; r₀=x and r_b=(0.031,-0.051)L. Squared distances are 0.869162L² and 0.003562L². Thus coordinate rounding fails as a universal closest-center rule; testing one better candidate does not certify a global optimum.

06. Sheet populations are (1,3,6,7,6,3,1), totaling 27 available labels, not empirical occupancies. Toy vectors are (1,2,1) and (0,3,1); difference=(-1,1,0). Preserve memberships and zero bins. Middle reconstructs as 1+1=2 and parent as 1+2+1=4. Vector residual=(1/5,0,0), length=1/5, angular miss=0°, radial mismatch=-1/5. Reconstruct x=c+r. At c=0 the angle is null with zero_center_direction, while r=x and radial mismatch=-1 remain defined.

07. Signs are (+,+,+,-,+,-,-); retain the numerical ledger too. The full 27-state correlation is source-reported and not replayed from full catalog arrays here. Population sum is 114,381. Original center=(1/4,1/2)L and residual=(1/20,0)L; changed center=(1/3,1/2)L and residual=(-1/30,0)L; phase shift=(1/12,0). Both have k=0 and reconstruct the same x. Changing after seeing holdout defines an exploratory branch. G02 p8 source controls are orientation rotations, common phase translations, and RA/Dec coordinate permutations. Keep all original frozen results and phase changes.

08. Original V=6L³ and M=diag(1,4,9)L². New V=48L³, M'=diag(4,16,36)L²; roots double. Since 48^(2/3)=4·6^(2/3), normalized M is invariant. Retain V and the basis/orientation to undo normalization. A valid plan freezes basis, phase, root-tensor eigenframe, aligned-state set, assignment, inclusion rules, exposures/selection transform and contrast before an independent catalog. The toy contrasts are -1/4 and +1/4, respectively. The second contradicts strict predicted depletion under equal exposure; zero would also fail it. In real work retain all 27 counts/fractions, signed contrasts, control results, vector/angular/radial residuals, and missing-distance/selection flags. A new eigenframe is another exploratory branch. The source proposal is a hypothesis, not an already completed independent confirmation.

## Rubric and backward map

Award four points for each task, 32 total. Give one point per criterion below; partial points may be used only with an explicit correction note. No score overrides a substantive error: repair missing source distinctions or lost residuals before calling the portfolio complete.

| Task | 1: typed inputs/domain | 2: operation | 3: reconstruction/source class | 4: retained information/boundary |
|---|---|---|---|---|
| 01 | directed vs axial | vectors and angles | position vs intrinsic axis | original directions and missing radius |
| 02 | u/F domains, units | all card calculations and address | G03 vs G04 roles | inputs/null flags, no force promotion |
| 03 | phi, L and reciprocal units | centers and inverses | recover k, determinant roles | origins and handedness |
| 04 | ordered bases and units | roots and metrics | closure vs normals | absent physical calibration |
| 05 | positive metric domain | distances | exact scope of counterexample | both signed residuals |
| 06 | half-step/state labels | counts and differences | parent and x reconstruction | zeros, IDs and undefined angle |
| 07 | frozen contract | seven signs and phase/residuals | source-only correlation | old/new branches and controls |
| 08 | normalization/test contract | scaling and contrasts | hypothesis vs independent result | full states and missing fields |

Each task NN is introduced at C29.NN-E1, modeled at C29.NN-W1, practiced at C29.NN-P1 and diagnosed at C29.NN-D1 in lesson-NN. Task 05 combines both exercises already practiced under C29.05-P1. Task 07 uses the source ledger already read in C29.07-W1; task 08 uses the prediction exercise already taught in C29.08-P1. No operation first appears in this assessment.
