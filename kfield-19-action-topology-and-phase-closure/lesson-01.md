# Lesson 01 — An action as a complete mathematical specification

**Essential question:** What must be supplied before an action can be evaluated?

**Goals:** Identify variables and coefficients; specify domains and boundaries; check the units of a finite action.

**Prerequisite bridge.** You can subtract numbers, square them, and substitute into a formula. Courses 16–18 prepare carrier and transport language; this lesson supplies the finite bridge needed here. A state is a list of values describing a system at a chosen time. A path is an ordered list of states. Changing their order changes the increments, even when the same numbers appear.

## C19.01-E1 — A formula plus its contract

An action assigns one number to an entire path. It needs more than an expression: we must know the state, times, coefficient values and units, allowed inputs (the domain), boundary values, and the evaluation convention. A coefficient is a supplied multiplier. A constitutive rule is a chosen rule connecting quantities in a model. We will evaluate such a rule, not derive its physical selection.

Our **synthetic** state q is dimensionless. Write q_0, q_1, q_2 for three ordered samples. Subscripts name positions in the list, not powers. There are two intervals, indexed j=0 and j=1. Let Δt be their common positive duration. Define v_j=(q_(j+1)−q_j)/Δt. This is a finite rate of change, measured in inverse time units. AU means an abstract action unit; TU means an abstract time unit. Neither is an experimentally calibrated unit here.

The toy rule is

S = Σ_(j=0 to 1) Δt [ (k/2)v_j² − (vpot/2)q_j² ].

Σ means add one copy for each listed j. The potential uses the **left endpoint** q_j; the final q_2 is used in the final rate but not as a left endpoint. We allow real q values, Δt>0, k>0 and vpot>0. Endpoints q_0 and q_2 are fixed when comparing paths in the same boundary problem. The middle value is an interior state coordinate.

## C19.01-W1 — Unit and input ledger

Take Δt=1 TU, k=2 AU·TU, vpot=2 AU/TU, and path (0,1,3), with q_0=0 and q_2=3 fixed. A rate has units 1/TU, so k v_j² has units AU/TU. The potential vpot q_j² also has units AU/TU. Multiplying each by Δt gives AU; subtraction and addition are therefore permitted. The state ledger has three values, the time ledger t=(0,1,2) TU, and the interval ledger has two entries. Lesson 02 evaluates them. Specifying only the three q values would leave the action undetermined.

## Source-reading card: four terms, not the toy rule

S02, `/backbone_sequence/14/action`, records

`S_K[q]=int d tau sum_L {mu_L/2 dot(q_L)^T M dot(q_L)-kappa_K/2 tr(M Q_L R Q_L^T)-epsilon_K U_K(Cq_L)+s_L^Tq_L}`.

Read the braces as four contributions: a rate-quadratic term, a trace contraction, a potential term, and a linear source term. A vector is an ordered list; transpose T turns a column into a row; a matrix is a rectangular table acting on a vector. A contraction combines matching slots until no free slot remains. A trace adds the diagonal entries of a square table. These are recognition operations here: no matrix calculation is assigned. `int d tau` denotes accumulation over a continuous parameter, while `sum_L` accumulates over labeled carriers. The dot marks a rate with respect to that parameter. Calculus is not required in this course.

The source uses q_L as state and μ_L, κ_K, ε_K as coefficients. M and R are metric/operator symbols whose source-local definitions and units must be resolved; do not equate every M with every metric. Q_L, C, U_K and s_L require typed definitions before replay. U_K is the named potential function, C acts on q_L, and s_L supplies the linear contraction. L labels carriers. These syntactic roles do not supply missing numerical values or full domains. Every brace term must share action-per-parameter units, but the excerpt does not supply a complete calibrated unit assignment. The integral parameter `tau` is distinct from the determinant-line map τ in Lesson 05. Source M15 explicitly retains operator coefficients, boundary-sector values, and time/action normalization as state inputs.

> **Claim scope.** The displayed source expression is an archival fact. Its assertion of typed terms is source-reported. The toy action is a declared teaching model, not that expression with missing parts filled in. S03 `/findings/8` identifies M15 replay gaps, including topology carriers and determinant-line factors. No measured coefficients or physical mechanism are inferred here.

## C19.01-P1 — Guided practice, then compare

For (1,2,2), with the same Δt, k and vpot, list state values, intervals, endpoints and potential convention. Explain what changes if Δt changes.

**Worked answer:** There are three states q_0=1,q_1=2,q_2=2, two intervals, and fixed endpoints 1 and 2 for this boundary problem. The potential reads q_0 and q_1. A changed Δt changes both rates and interval weights, so retaining the old rate values would be incorrect. Changing vpot changes the model coefficient. This path has different boundaries from W1 and is not a competing path with W1's fixed endpoints.

**Source-reading practice:** Using the source card, name all four brace contributions and one input needed before numerical replay. **Answer:** They are the rate-quadratic term μ_L dot(q_L)ᵀM dot(q_L)/2, the negative trace term −κ_K tr(M Q_L R Q_Lᵀ)/2, the negative potential term −ε_K U_K(Cq_L), and the positive linear source term s_Lᵀq_L. A complete typed coefficient/operator definition with its units is one needed input; boundary-sector values and time/action normalization are others. Naming terms does not provide their missing values.

## Diagnostics

1. **C19.01-D1:** Can the source action be evaluated from its printed formula alone? Name two missing input classes.
2. What are the units of v_j² and k v_j²?
3. Does a list of four samples have four intervals?
4. Why must a right-endpoint potential be declared rather than silently substituted?

**Worked answers:** (1) No: typed operator/coefficient definitions and boundary-sector values are needed, alongside time/action normalization. (2) 1/TU² and AU/TU. (3) No, three adjacent intervals connect four samples. (4) It changes which q value enters each term and generally changes S; the convention is part of the specification.

**Next dependency:** [Lesson 02](lesson-02.md) evaluates and preserves every signed contribution.
