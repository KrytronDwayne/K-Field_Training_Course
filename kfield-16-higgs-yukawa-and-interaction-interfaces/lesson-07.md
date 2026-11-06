# Lesson 7 — What a complete interaction specification needs

Essential question: How can a precise interaction contract show both what is determined and what remains open?

Goals: assemble a typed interaction record; distinguish source-defined inputs from outputs; identify possible constraining observations and their limits.

Bridge: lessons 1–6 supplied type checks, contractions, vacuum and mass calculations, coefficient maps, and reversible ledgers. One 55-minute period: 5 retrieval, 20 teaching/example, 15 practice, 15 diagnostics/repair.

## C16.07-E1 — Structure and occupied-state coordinates

A contract states enough about inputs and operations that another person can reproduce the same result. It also names blanks. “Unspecified” is more informative than a guessed value: it tells us which future input could change an output. A structural contract can be fully described even when the numerical physical state remains undetermined.

S02 M12 lists five occupied-state inputs: vacuum magnitude, Higgs-potential coefficients, Yukawa coefficient matrices, mixing coordinates, and matching scale. “Occupied-state” means values specifying the chosen state within the supplied architecture. The matching scale records the scale at which model parameter conventions are compared or matched; a value and unit must be declared when making a numerical physical comparison. We do not evolve coefficients between scales in this course.

Our computational ledger also needs g2 and gY, ordered bases, units and normalization, initial/boundary states, dual/conjugation rules, Ω, and any dynamical rule used for rates. A boundary state specifies conditions at the edge of the modeled region or process; an initial state specifies where evolution starts. These are needed even if the list of allowed interactions is already known.

| Contract layer | What to record | What it supports |
|---|---|---|
| Structure | C₃ ⊕ W₂ order; sector table; four source interface orders; dual rule; Ω | type, charge, and contraction tests |
| Numerical state | v, potential coefficients, Y_Yuk, mixing coordinates, couplings | declared numerical outputs where formulas are supplied |
| Conventions | mass/energy units, normalization, bases, matching scale | reproducible comparison |
| Evolution/accounting | initial/boundary conditions, time rule, transfers, component labels | evolution or balance only to supplied scope |
| Evidence | source pointers, synthetic labels, actual observations if supplied, residuals | separation of source statements and fresh checks |

Possible observations are proposals, not data. With an applicable model and conventions, masses may constrain combinations of v and couplings; the formulas alone leave tradeoffs (rescale v and inversely rescale both couplings, and the two masses stay fixed). Relative transition observations may constrain mixing and coefficient combinations when the interaction-to-observation rule is supplied. Potential-sensitive measurements may constrain potential coefficients under a specified potential model. Time-resolved event counts with preparation/exposure information can constrain rates when an evolution model is available. Matching scale and basis choices are recorded comparison metadata; an isolated mass value does not determine every input. Keep every observation and its residual against the chosen prediction.

## C16.07-W1 — A worked contract with honest blanks

Take the worked mass example g2=3, gY=4, v=2 μ, and the worked coefficient matrix [[1,2],[0,3]] with f=(2,−1). Record the color-first basis and Ω from lesson 1 and the four basis contraction tests from lesson 2. Derived mass outputs are (3,5) μ and rho=1. The dimensionless matrix output is (0,−3). At this contract's v=2 μ, M=√2 μ Y_Yuk and Mf=(0,−3√2) μ; the separate lesson-5 normalization example used v=√2 μ and must not silently replace this value.

Attach the energy endpoints (5,2,1)→(4,4,1) ε, p=0.8 ε, r=0.2 ε. Potential coefficients, physical matching scale, empirical mixing values, external transfer, elapsed time, and a dynamical rate rule are unspecified. The chosen basis is specified, but no physical mixing inference has been made. The source reports a typed architecture; our recomputation verifies this finite synthetic record. No empirical observation has been acquired.

## C16.07-P1 — Build the practice contract

Use g2=4, gY=3, v=2 μ; Y_Yuk=[[2,0],[1,1]], f=(1,2); swap P from lesson 5; and the practice energy ledger from lesson 6. Identify all recorded outputs and open inputs. Propose two measurement categories without pretending that either was performed. Read the source-scope card below, then write one sentence distinguishing its compiler authority and global-form status from our M12 finite replay.

Worked answer: retain the ordered basis, four interfaces, covector action, Ω, and charges. Record masses 4 and 5 μ, c²_theta=16/25 and rho=1; Y_Yuk f=(2,3); P=[[0,1],[1,0]], Y′=[[1,1],[0,2]], f′=(2,1), output′=(3,2). With v=2 μ, M=√2 μ Y_Yuk. Energy endpoints are (3,1,2)→(2,1,1) ε, changes (−1,0,−1) ε, totals 6→4 ε, prediction −1.5 ε, residual −0.5 ε. Potential coefficients, physical mixing coordinates, matching scale, physical preparation/boundary states and rate model remain unfilled. Possible mass and time-resolved transition measurements could constrain parameter combinations and rates under an explicit model; neither is present as data here.

> Claim scope: S02 /backbone_sequence/11 and /branch_proofs/7 report the architecture and its state-coordinate boundary. The integration's compiler labels M03/M07/M08 have direct-authority status in that separate namespace; that status does not attach automatically to mathematical-backbone M12. The integration admits global-form alternatives Z1,Z2,Z3,Z6 rather than a uniquely selected physical member. These are source-reading boundaries, not extra capstone calculations. We have not freshly typechecked a compiler certificate.

Source-scope practice answer: integration direct authority covers compiler M03/M07/M08 in a separate namespace, not automatically backbone M12, and its admitted global-form family Z1,Z2,Z3,Z6 does not select a unique physical member; our calculations freshly replay finite examples without executing that compiler.

## Diagnostics and worked answers

1. **C16.07-D1:** Is a precise structural contract a table of unique physical masses and rates? Answer: no; it names operations and open numerical inputs. Unfilled entries must remain visible.
2. **C16.07-D2:** Which five input categories come directly from M12? Answer: vacuum magnitude, Higgs-potential coefficients, Yukawa coefficient matrices, mixing coordinates, and matching scale.
3. **C16.07-D3:** Distinguish “rho=1 was recomputed” from “a rate was measured.” Answer: the former is a finite algebraic result from supplied formulas and nonzero inputs; the latter would require actual time-based observations, which this course does not supply.
4. **C16.07-D4:** Can two measured masses alone choose all five M12 inputs? Answer: no; even v and two couplings can trade off while maintaining these masses, and potential, Yukawa, and mixing information remains additional.

Next dependency: [Capstone](capstone.md) assembles and defends a complete synthetic interaction ledger using only these taught operations.
