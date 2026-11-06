# Capstone — A typed interaction ledger

Prepare a ledger another learner can replay. All numerical data below are synthetic. Use the color-first basis (c1,c2,c3,w1,w2), its top form Ω, the sector table, and four source interface orders taught in lessons 1–2. Work three 55-minute periods: period 1 structural ledger and contractions; period 2 vacuum, mass, and matrix computations; period 3 energy accounting, contract, and explanation. Units μ and ε are the arbitrary mass and energy units taught in the lessons. They have no supplied conversion to each other. Do not import measured constants.

## Student tasks

1. **C16-CAP-01 (14 points).** Write all four interaction formulas. For each, list input types and q values, calculate the total charge, and track bidegrees through the actual operation. Explain why barH cannot simply be replaced by H.
2. **C16-CAP-02 (24 points).** Use up inputs u^c=c1c2,Q=c3w1,H=w2; neutrino inputs ν^c=1,L=c1c2c3w1,H=w2; down inputs d^c=c1c2w1w2,Q=c3w1,barH=w1*; electron inputs e^c=w1w2,L=c1c2c3w1,barH=w1*. Calculate all four top coefficients with signs. Replace H by w1 in the neutrino case and explain the result. Apply U=diag(1,1,1,i,−i) to every vector and dual input and show each scalar is unchanged. State the covariance argument and diagnose the error if barH wrongly gains i. These are separate test inputs for each interface; they need not be one simultaneously occupied Higgs state.
3. **C16-CAP-03 (10 points).** Using T3=diag(1/2,−1/2) and Y_h=I/2, calculate component electric charges. At v=4 μ compute the neutral vacuum, its squared length, and Q_electric H_vac. Test the alternative (1,0) μ.
4. **C16-CAP-04 (14 points).** In a separate mass example use g2=4,gY=3,v=2 μ. Compute squared masses, positive masses, c²_theta and rho. State the nonzero-domain requirements and what changes when v=0. Do not combine the separate v=4 vacuum exercise with these inputs.
5. **C16-CAP-05 (14 points).** Use Y_Yuk=[[2,0],[1,1]], f=(1,2), P=[[0,1],[1,0]]. Compute Y_Yuk f, Y′=P Y_Yuk P^T, f′, and Y′f′. Show the inverse coordinate change. Separate matrix shape, numerical entries, basis choice and mass normalization M=(v/√2)Y_Yuk at v=2 μ.
6. **C16-CAP-06 (12 points).** For labeled components A,B,C, before=(3,1,2) ε, after=(2,1,1) ε and prediction p=−1.5 ε, record signed changes, totals, residual and reconstruction. State whether external transfer, an elapsed time, or a transition rule was provided, and explain why no rate follows. Retain the original endpoints.
7. **C16-CAP-07 (12 points).** Assemble a contract using steps 1,2,4,5,6; keep step 3 as a separately labeled vacuum-direction test. List the five M12 occupied-state inputs, additional ledger metadata, and unfilled values. Suggest observations that could constrain two parameter categories, stating required modeling context. Separate source reports, fresh derivations, synthetic choices, proposed observations, and unresolved inputs. Include the accepted-integration scope in one sentence.

## Full answer key and rubric

### C16-CAP-01

I_u=Ω⁻¹(u^c∧Q∧H), q=−4+1+3=0, degrees (2,0)+(1,1)+(0,1)=(3,2).

I_ν=ν^cΩ⁻¹(L∧H), q=0−3+3=0, degrees (0,0)+(3,1)+(0,1)=(3,2).

I_d=Ω⁻¹(Q∧ι_barH d^c), q=1−3+2=0. barH is a weak covector; d^c degree (2,2) contracts to (2,1), then Q adds (1,1), yielding (3,2).

I_e=Ω⁻¹(L∧ι_barH e^c), q=−3−3+6=0. Contract e^c from (0,2) to (0,1), then add L's (3,1) to obtain (3,2). Replacing barH by H changes the type and charge; for down the charge becomes 6 and a full wedge would repeat weak slots.

Award 4 points for the ordered formulas, 4 for input charges and zero sums, 4 for types and degree routes, 2 for diagnosing the replacement. Accept equivalent source order-preserving notation.

### C16-CAP-02

Up yields c1c2c3w1w2=+Ω, so +1. Neutrino yields 1×Ω, so +1. Down contracts the third position of d^c with sign (+), giving c1c2w2; Q first gives c3w1c1c2w2, four neighboring swaps to Ω, so +1. Electron contracts position 1 of w1w2 to w2; L∧w2=Ω, so +1. Replacing neutrino H by w1 repeats w1 and gives 0.

For the weak phase action, up and neutrino each gain i(−i)=1. Down's d^c and electron's e^c gain i(−i)=1; Q or L gains i; barH gains inverse i, namely −i. Both complete products again gain 1. A covector ℓ transforms to ℓU⁻¹, so evaluation on Uv stays ℓv; the contraction sum therefore transforms consistently. U acts on every exterior slot, and det U=1 preserves Ω, so top coefficient extraction is unchanged. Giving barH factor i instead produces i²=−1, a retained failed test of the wrong dual rule.

Award 8 points for four scalar results with intermediate operations, 4 for down's four-swap sign explanation, 2 for the repeated-slot zero, 4 for the four phase-factor checks, 4 for the covariance/determinant argument, 2 for the wrong-dual diagnosis. Partial credit follows the demonstrated operation, not the bare final value.

### C16-CAP-03

Q_electric=diag(1,0); charges are +1 and 0. H_vac=(0,4/√2) μ=(0,2√2) μ. Squared length is 8 μ². The charge output is (0,0). The alternative (1,0) μ maps to itself, so it fails the annihilation test. Neutrality does not choose v.

Award 2 points for charges, 2 for vacuum, 2 for squared length, 2 for zero output, 2 for the alternative and interpretation.

### C16-CAP-04

m_W²=4²×2²/4=16 μ²; m_Z²=(16+9)×4/4=25 μ². Positive masses are 4 and 5 μ. c²_theta=16/25, denominator m_Z² c²_theta=16 μ²; rho=1. The cosine ratio needs g2²+gY²>0, and rho additionally needs g2≠0 and v≠0. At v=0 both squared masses are 0 and rho is undefined as 0/0. These are outputs of supplied formulas, not measured masses or a fresh kinetic-term derivation.

Award 4 points for squared masses, 2 for masses/units, 2 for c²_theta, 2 for rho calculation, 4 for domain and boundary interpretation.

### C16-CAP-05

Y_Yuk f=(2×1+0×2,1×1+1×2)=(2,3). Swapping rows then columns gives Y′=[[1,1],[0,2]]. f′=(2,1), so Y′f′=(3,2)=P(2,3). The inverse is f=Pf′ and Y_Yuk=P Y′ P, since P²=I. Matrix shape permits two inputs/two outputs, numerical entries specify the map, and P records a coordinate relabeling. At v=2 μ, M=√2 μ Y_Yuk, so Mf=(2√2,3√2) μ. These entries/output components are not automatically physical mass eigenvalues.

Award 2 points for original action, 4 for Y′ and f′, 2 for transformed output, 2 for inverse, 2 for structure/coefficient distinction, 2 for normalization and units.

### C16-CAP-06

Keep A:3→2, B:1→1, C:2→1 ε. Changes are (−1,0,−1) ε, totals 6→4 ε, net −2 ε. r=−2−(−1.5)=−0.5 ε and p+r=−2 ε. No external transfer, elapsed time, or transition dynamics is supplied. The open accounting does not assert an isolated-system energy violation. Energy difference has no time unit and cannot specify a rate. The component endpoints, prediction, residual, units, and labels are all retained.

Award 3 points for component differences, 2 for totals/net, 3 for residual/reconstruction, 2 for endpoint preservation, 2 for open transfer/rate explanation.

### C16-CAP-07

A complete record repeats the structural order/rules from step 1 and finite tests from step 2; records g2=4,gY=3,v=2 μ and outputs from step 4; retains Y_Yuk, f, P, Y′, f′, units and normalization from step 5; and includes all energy records from step 6. It labels step 3's v=4 μ as a separate test, not the contract vacuum magnitude.

The M12 list is vacuum magnitude, Higgs-potential coefficients, Yukawa coefficient matrices, mixing coordinates, and matching scale. Here v and a synthetic matrix are supplied. Potential coefficients, physical mixing values, and physical matching scale remain unspecified. P is a supplied basis swap, not measured physical mixing. Ordered bases, dual rule, Ω, couplings, normalization, units, initial/boundary conditions, external transfers, and any rate dynamics are additional ledger requirements. Synthetic f is specified; physical preparation and boundary conditions are not.

Possible masses could constrain coupling/v combinations with the applicable mass model and scale convention; time-resolved transition observations could constrain rates or mixing-dependent combinations with a supplied evolution/observation model, preparation and exposure. Neither is an acquired dataset. Source formulas are source statements; substitutions are derived implications; numbers are synthetic choices; mechanisms beyond the supplied architecture remain proposals requiring specification; missing inputs remain unresolved. Integration direct authority is limited to compiler M03/M07/M08 in a separate namespace, while its global-form family Z1,Z2,Z3,Z6 remains admitted without selection of a unique physical member.

Award 3 points for a replayable assembled contract, 3 for the five source inputs and blanks, 2 for additional metadata, 2 for proposed observations with context, 2 for evidence/integration separation.

## Backward teaching map

Each task uses named inputs and returns the output described above. For step n, prior explanation is C16.0n-E1, worked example C16.0n-W1, independently answered practice C16.0n-P1, and diagnostic C16.0n-D1 in lesson-0n. Step 2 also uses C16.02-E2/W2/P2/D2 for phase action. This maps every capstone operation to teaching and prior practice; no general Lie theory, variational derivation, diagonalization, or compiler execution is required.

Mastery guidance: 80/100 with successful type routes, dual transformation, rho-domain handling, and retained energy residual indicates readiness for the next course. A high score never cancels a misconception in one of those four essential operations; repair and reassess that operation. Preserve initial answers alongside repairs.
