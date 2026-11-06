# Lesson 02 — Discrete action accounting

**Essential question:** How can one total retain the information in its signed parts?

**Goals:** Evaluate both interval contributions; reconstruct a total from a model and residual; distinguish action evaluation from a dynamical prediction.

**Prerequisite bridge.** Lesson 01 fixed the state, units, coefficients and left-endpoint convention. We now substitute values. Keep a row per interval: a total alone cannot tell you which interval contributed which sign.

## C19.02-E1 — Compute before compressing

Define K_j=Δt(k/2)v_j² and V_j=Δt(vpot/2)q_j², both in AU. The signed contribution is a_j=K_j−V_j. K and V are names for two model terms; their difference is not a measured transferred energy. For Δt=1 TU and numerical coefficients k=2 and vpot=2 in their declared units, the numerical shortcut is a_j=(q_(j+1)−q_j)²−q_j². This shortcut depends on those inputs and cannot be reused after changing Δt.

A residual records the difference from a declared model: r=S−S_model, so S=S_model+r. A single total residual preserves the total, but cannot recover the interval series. To preserve a path-level decomposition, retain each a_j, each model component m_j, and each r_j=a_j−m_j, so a_j=m_j+r_j. Zero and negative entries remain in the ledger.

## C19.02-W1 — Worked path (0,1,3)

The increments are 1−0=1 and 3−1=2. With Δt=1, the rates have numerical values 1 and 2 per TU. Squaring gives 1 and 4.

| j | q_j → q_(j+1) | K_j (AU) | V_j (AU) | a_j (AU) |
|---|---|---:|---:|---:|
| 0 | 0 → 1 | 1 | 0 | 1 |
| 1 | 1 → 3 | 4 | 1 | 3 |

Therefore S=1+3=4 AU. Independently group the totals: ΣK=5 AU and ΣV=1 AU; 5−1=4 AU. This second route checks the bookkeeping without dropping the row values.

If Δt becomes 2 TU with the same three states and the same physical coefficients, rates become 1/2 and 1 per TU. K becomes (1/2,2) AU and V becomes (0,2) AU. The signed terms are (1/2,0) AU, total 1/2 AU. Slower traversal changed both kinetic accumulation and potential accumulation. Merely doubling 4 would be wrong.

> **Claim scope.** These are exact finite consequences of the synthetic rule. No data were fitted. Evaluating a path is not minimizing over paths, solving an equation of motion, assigning a transition probability, or finding a transition rate. Each of those operations needs its own rule and normalization.

## C19.02-P1 — Guided practice and reconstruction

Evaluate (1,2,2) using the original Δt=1. Retain the two signed contributions. A declared component model is m=(1,−4) AU; calculate the residual vector and reconstruct the total.

**Worked answer:** Increments (1,0) give K=(1,0) AU; left endpoints (1,2) give V=(1,4) AU. Thus a=(0,−4) AU and S=−4 AU. The model total is 1−4=−3 AU. Residuals r=(0−1,−4−(−4))=(−1,0) AU have total −1 AU. Reconstruct row by row: (1,−4)+(−1,0)=(0,−4), and reconstruct the total: −3+(−1)=−4 AU. The zero first contribution does not authorize erasing its kinetic and potential parts, which are both 1 AU.

## Diagnostics

1. **C19.02-D1:** Does S=−4 AU make the calculation invalid or imply negative measured energy?
2. For path (0,1,1), find K,V,a and S with original parameters.
3. If only S=−4 and S_model=−3 survive, can you recover the two residual entries?
4. Can S=4 and S=−4 determine which path is more probable?

**Worked answers:** (1) No. S is a signed action sum in this toy model; it is not a measured energy. (2) K=(1,0), V=(0,1), a=(1,−1) AU, giving S=0 AU. (3) No: their sum is −1, but many pairs share it; preserve the component ledger. (4) No probability rule or scale converting action to a probability has been supplied, and W1/P1 also have different endpoints.

**Next dependency:** [Lesson 03](lesson-03.md) preserves link information while testing a whole loop.
