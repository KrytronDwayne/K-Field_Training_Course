# Capstone: a reconstructable decoding report

Three 55-minute sessions, 44 points. Session 1: input ledger, decoder tasks 1–4. Session 2: composition, sources and energy tasks 5–6 and 10–11. Session 3: solver, report and compatibility tasks 7–9; partner reconstruction and repair. Use the printed lessons and source cards. No external measurements, constants or missing source matrices are required. All numerical channel and reaction inputs are synthetic.

## Student tasks

### C21-CAP-01 — 4 points

Use A_small and synthetic y=(1,2,3). Write all three channel equations, solve the normal equations, and save the full residual.

Preparation: [lesson-01](lesson-01.md), C21.01-E1; answered practice C21.01-P1.

### C21-CAP-02 — 4 points

Use A_small and y=(1,1,3). Separate c and t, reconstruct every channel, and prove integer image/kernel equality for A0=(1,0)^T, L0=(0,1). Contrast the even-column counterexample.

Preparation: [lesson-02](lesson-02.md), C21.02-E1; answered practice C21.02-P1.

### C21-CAP-03 — 4 points

Using the source A printed in lesson-03, form y from c0=(1,-1,2,0,1,0) and s=(-2,-2,1,1,0,0,0,0,0,0,0,0,0). Verify perpendicularity and explain the six-plus-seven count and missing-source boundary.

Preparation: [lesson-03](lesson-03.md), C21.03-E1; answered practice C21.03-P1.

### C21-CAP-04 — 4 points

Use the lesson-04 toy b=(1,1/10,1/100,1/1000,1/5,2), c=(0,2,0,0,1,0), m_ref=2 mass units and s=0. Render mass and reconstruct the source-A channel packet. State the boundary for source b.

Preparation: [lesson-04](lesson-04.md), C21.04-E1; answered practice C21.04-P1.

### C21-CAP-05 — 4 points

For complete neutral synthetic objects A=2u, B=3u, AB=5.05u, keep conserved constituent labels A and B and unchanged isotope convention. Use 1u c_light²=10 E_unit. Compute signed Q and separately V for (4,4,0,1). Identify an electron-convention error that would block this subtraction.

Preparation: [lesson-05](lesson-05.md), C21.05-E1; answered practice C21.05-P1.

### C21-CAP-06 — 4 points

Complete an R029/R030/R031/R032 source row for (4,4,0,1), then repeat the neutral synthetic reaction with AB=4.8u. Identify supplied values, proposed mechanisms and unresolved information.

Preparation: [lesson-06](lesson-06.md), C21.06-E1; answered practice C21.06-P1.

### C21-CAP-07 — 4 points

For A_small and y=(2,3,6), start c0=0 and take t=1 in c_next=c+t A_small^T(y-A_small c). Save two updates, each full residual and normal residual. Explain the failure and reconstruct y at the second step.

Preparation: [lesson-07](lesson-07.md), C21.07-E1; answered practice C21.07-P1.

### C21-CAP-08 — 4 points

Assemble the y=(1,2,3) decoder report, the negative-Q endpoint ledger and source row from tasks 5–6. Separately classify 7/3 displayed as 2.33 and retain its closure.

Preparation: [lesson-08](lesson-08.md), C21.08-E1; answered practice C21.08-P1.

### C21-CAP-09 — 4 points

Use the explicit four-character W in lesson-03 on v=(2,0,0,2). Compute a=W^T v/4 and reconstruct. Verify the swap intertwiner for rho=diag(1,-1), sigma=diag(-1,1), and explain nonuniqueness and the source boundary.

Preparation: [lesson-03](lesson-03.md), C21.S01-E1; answered practice C21.S01-P1.

### C21-CAP-10 — 4 points

Apply U2=(1,4,0,-1) to (4,4,0,1) and K=(-4,0,0,3) to (4,0,0,0). Verify nominal invariance and nonnegative endpoints, U3=U1+U2, and independence of K. State the R023 and R032 boundaries.

Preparation: [lesson-05](lesson-05.md), C21.S02-E1; answered practice C21.S02-P1.

### C21-CAP-11 — 4 points

Repeat the same neutral reaction with AB=5.05u. In a separate positive release example, 2 E_unit is delivered over 4 time units with recovered fraction 1/2. Compute signed Q and recovered mean power, and state which premises are extra.

Preparation: [lesson-06](lesson-06.md), C21.S03-E1; answered practice C21.S03-P1.

## Full answer key

### C21-CAP-01

A_small=[[1,0],[0,1],[1,1]]; c1=1,c2=2,c1+c2=3. Normal equations 2c1+c2=4, c1+2c2=5 give c=(1,2). Ac=(1,2,3), r=(0,0,0), y=Ac+r. All inputs are dimensionless synthetic values.

### C21-CAP-02

c=(4/3,4/3), t=1/3, r=(-1/3,-1/3,1/3), Ac=(4/3,4/3,8/3). Adding gives (1,1,3); A_small^T r=(0,0). Every integer kernel point of L0 is (n,0)=A0 n. Replacing A0 by (2,0)^T misses (1,0), despite the same real rank.

### C21-CAP-03

Ac0=(2,-1,1,1,1,4,2,0,3,1,0,3,1); y=(0,-3,2,2,1,4,2,0,3,1,0,3,1). The first coefficient-column dot s is 0; the second is -2+1+1=0; the third is -2+1+1=0; columns 4 and 5 give 0; column 6 gives 1-1=0. Hence the Euclidean decoder returns c0 and this full s. Six represented directions leave seven independent syndrome directions stored in thirteen constrained entries. L_int is not the missing source L or W7.

### C21-CAP-04

Ratio=2/10+1/5=2/5; m=(2)(2/5)=4/5 mass units. Ac=(0,2,2,2,0,1,-1,2,3,1,2,3,1); s=(0,0,0,0,0,0,0,0,0,0,0,0,0). This is synthetic; source b still requires its own occupied-state inputs and reference mass. A scalar mass does not preserve arbitrary s.

### C21-CAP-05

Initial and final inventories are one A label and one B label; charges are 0+0=0. Complete-object masses include electrons and the declared binding/reference states. Delta m=5-5.05=-0.05u, Q=-0.5 E_unit, requiring input 0.5 E_unit. V=48+4+16=68 nominal units. Comparing a bare final ion with neutral initial masses without accounting for the removed electron makes the endpoint incomplete.

### C21-CAP-06

Counts and derived V=68 are supplied; address, scale/face, lambda, chosen composition coordinates, isotope mass, graph identity/spectrum, charge/parity, binding residual, phase tensor and selected physical c are not. R029 is coordinate synthesis; R030 is typed-edge mechanism synthesis; R031 is archive_stated unresolved isomer information; R032 leaves a canonical map among three rank-three structures unresolved. Delta m=0.2u, Q=2 E_unit with the declared conversion. Neither the source synthesis nor this arithmetic supplies a physical coefficient-selection rule.

### C21-CAP-07

At n=0, r=(2,3,6), g=(8,9). At n=1, c=(8,9), r=(-6,-6,-11), g=(-17,-17). At n=2, c=(-9,-8), r=(11,11,23), g=(34,34). Reconstruction is (-9,-8,-17)+(11,11,23)=(2,3,6). The nonzero sum-error component has multiplier -2, so it alternates and grows. Retain this failed parameter branch; the exact target still has nonzero channel residual.

### C21-CAP-08

Record synthetic input y, A_small, channel order, R field, Euclidean metric, dimensionless units, exact c=(1,2), Ac=y, full r=(0,0,0), and normal check (0,0). Attach all endpoint inputs from task 5 and source pointers/statuses from task 6. In a separate approximation illustration, 7/3-233/100=1/300. Source alpha is a witness, 7/3 a derived coefficient, 2.33 an approximant, and a rendered toy mass a model output; no new measured value is present.

### C21-CAP-09

W^T v=(4,0,0,4), a=(1,0,0,1), Wa=(2,0,0,2). T=[[0,1],[1,0]] gives T rho=sigma T=[[0,-1],[1,0]], determinant -1; it is invertible. 2T also intertwines, so compatibility does not select a unique T. The toy W does not load source W7, L or their action/order conventions.

### C21-CAP-10

The first endpoint is (5,8,0,0), V=60+8=68, matching 48+4+16. The second is (0,0,0,3), V=48, matching 12 times 4. All counts are nonnegative. U1=(-1,-2,1,0) plus U2 gives (0,2,1,-1)=U3. In K=aU1+bU2, N forces a=0 and H forces b=0, contradiction. R023’s 15.25614129 mDa is attributed synthesis with isotope replay inputs missing. R032 has no canonical map. These count moves are not asserted physical carbon-to-oxygen reactions.

### C21-CAP-11

For the negative branch delta m=-0.05u and Q=-0.5 E_unit, requiring input. Separately, recovered energy=(1/2)2=1 E_unit and mean recovered power=1/4 E_unit per time unit. Duration and recovery fraction are extra premises; endpoint mass difference alone supplies neither rate nor recoverable power.

## Rubric

Each task earns four independent points: one for declared inputs and scope, one for the correct operation, one for complete reconstruction or accurate source classification, and one for retained information and the boundary. Award demonstrated points even when another part is wrong; use the full key above for task-specific evidence. Total: 11 times 4=44.

For tasks 1–4 and 7, the reconstruction point requires every requested component, not a residual score. For tasks 5, 6 and 11, an inconsistent electron/reference convention loses the input point and must be repaired before the energy result is accepted as that endpoint’s answer. For tasks 6 and 10, a source-reported status presented as fresh physical verification loses the classification point. For task 9, equal dimension without the actual product check does not earn the operation point. For task 8, mixing rounding closure with channel residual loses the retained-information point.

Before advancing, repair any missing full residual, invented source coefficient selection, absent endpoint convention or unexplained source promotion, regardless of total score. A student can earn arithmetic credit and still need conceptual repair. Corrections retain the original attempted calculation and identify what changed.
