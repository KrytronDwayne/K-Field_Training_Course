# Capstone — Audit an action and phase-closure packet

Allow three 55-minute periods: specification/action; loops/phases/lines; sectors/premise audit and repair. All numbers below are synthetic. The task is to audit this supplied finite packet, not infer a source coefficient or prove a continuum/global theorem. Use Lessons 01–07; no new operation is introduced here.

## Supplied packet

The dimensionless path is q=(1,2,2) at t=(0,1,2) TU. Use Δt=1 TU, k=2 AU·TU and vpot=2 AU/TU, all positive. Endpoints q_0=1,q_2=2 are fixed. Use the left-endpoint action S=Σ_(j=0,1) Δt[(k/2)((q_(j+1)−q_j)/Δt)²−(vpot/2)q_j²]. The component model is m=(1,−4) AU. Keep each contribution and residual.

The separate scalar triangle has links (i,−i,1) in ab,bc,ca order and frames (−1,i,1). Use U'_xy=g_x U_xy g_y^−1. This triangle is not asserted to generate the six determinant-line factors.

The six-factor line packet, in UV,light,reg,heavy,cap,induced order, is (−1,i,i,1,−i,i). Its chosen combined basis is E and τ(E)=1. Rebase cap only: e'_cap=−e_cap. All phases are dimensionless.

For the topology arithmetic set A_3=0,A_2=1,C=4 and d=(0,1,54), with the Lesson 06 integer/dual contract. The admitted sector list is **assumed** to be {a,b}. In the original bases let τ(E_a)=τ(E_b)=1. Sector a has phases (−1,i,i,1,−i,i); sector b has phases (−1,i,i,1,−i,−i). These are complete rows. The rebasing operation above concerns row a; row b stays in its declared original basis unless you explicitly transform it.

A damaged copy deletes induced, τ, Δt and the admitted-sector list. Do not fill absent entries from a desired outcome. Compare with the complete supplied packet to repair this toy copy; keep source gaps separate.

## Student tasks

1. **C19-CAP-01 — Specify.** Given q, times and coefficients, produce a ledger with states, intervals, units, domain, boundaries and evaluation convention. Identify all four source action contributions on the Lesson 01 source card and explain which full-source inputs remain unspecified. [Taught/practiced: C19.01-E1/P1.]
2. **C19-CAP-02 — Account.** Produce K,V,a,S; compute the residual vector against m and reconstruct each row and total. Explain the status of a negative contribution. [C19.02-E1/P1.]
3. **C19-CAP-03 — Transform.** Produce the new triangle links, old and new loop products, and inverse reconstruction formula. Explain why this local change cannot repair a nonclosing scalar loop. [C19.03-E1/P1.]
4. **C19-CAP-04 — Retain factors.** Produce a six-row running-product ledger. Omit cap as a recorded mutation and compute its product and closure residual. Discuss heavy=1. [C19.04-E1/P1.]
5. **C19-CAP-05 — Rebase.** Produce the new cap coefficient, total coefficient Z', τ(E') and scalar reading for sector a. Reconstruct the original cap coefficient. [C19.05-E1/P1.]
6. **C19-CAP-06 — Test domain.** Compute n, test d's dual contract and pair d with n by both methods. Test candidate (1,1,0). Produce a two-sector phase/residual ledger and state precisely whether closure holds on the assumed admitted list. [C19.06-E1/P1.]
7. **C19-CAP-07 — Audit premises.** Classify locked M_cell, trace conjugation, the toy action, positivity and sector membership, and boundary values into the five roles. Inventory the damaged copy's missing inputs, restore only the declared toy values, and list unresolved full-source replay objects with provenance. [C19.07-E1/P1.]

## Full answer key

**01 (12 points).** Three ordered state values, two intervals, fixed endpoints 1 and 2; q dimensionless, Δt=1 TU, k=2 AU·TU, vpot=2 AU/TU. Allowed q values are real, all three scalar parameters positive. Rates have units TU^−1; both bracket terms have AU/TU and interval actions have AU. Potential reads q_0,q_1. The source has rate-quadratic, trace, potential and linear-source terms; the toy is separately declared. Full-source typed operator coefficients, topology carriers, boundary-sector values and time/action normalization remain required, not supplied by this toy.

**02 (15 points).** Increments (1,0); K=(1,0) AU; V=(1,4) AU; a=(0,−4) AU; S=−4 AU. Residual r=a−m=(−1,0) AU. Row reconstruction (1,−4)+(−1,0)=(0,−4); total reconstruction −3+(−1)=−4 AU. Negative action is permitted by the signed rule and is not negative measured transferred energy. Preserve K,V as well as a; cancellation does not erase components.

**03 (12 points).** Frame inverses are (−1,−i,1). New links are ((−1)i(−i),i(−i)1,1·1·(−1))=(−1,1,−1). Both products equal 1. U_xy=g_x^−1 U'_xy g_y reconstructs each old link. On a closed scalar loop endpoint factors cancel to g_aPg_a^−1=P. Thus local frame choices cannot change a nonclosing scalar P into 1.

**04 (12 points).** Running products in label order are −1,−i,1,1,−i,1. Φ=1, residual 0. Without cap, the list (−1,i,i,1,i) multiplies to i, with residual i−1. Equivalently 1/(−i)=i. Heavy=1 stays as a known contribution with a label and provenance; omission would leave the numerical product unchanged but the packet incomplete.

**05 (14 points).** e'_cap=−e_cap gives z'_cap=(−i)/(−1)=i. New six coefficients (−1,i,i,1,i,i) have Z'=−1. E'=−E so τ(E')=−1. Φ'=Z'τ(E')=1. The old cap coefficient is i(−1)=−i. This preserves a fixed τ and a fixed line element. Forgetting τ(E') would give the wrong scalar −1. It does not establish a global source trivialization.

**06 (20 points).** n=(4/3,2,1/18). For d=(0,1,54), d_3,d_2 are integers and h=0+1/4+54/72=1. Direct pairing 0+2+54/18=5; expanded pairing 0·0+1·1+4·1=5. Candidate (1,1,0) fails because h=7/12. Sector a has Φ=1 and ρ=0. Sector b's running products are −1,−i,1,1,−i,−1, giving Φ=−1 and ρ=−2. Closure fails on b, so it fails on the assumed list {a,b}. Membership is not inferred from closure success; keep b and its residual. Passing dual arithmetic does not determine physical admission.

**07 (15 points).** M_cell is a locked geometric root for this ledger; trace conjugation is a finite derived theorem with square/invertible hypotheses; the chosen finite action is a constitutive rule; positivity and the assumed set {a,b} are domain conditions; boundary values are state coordinates. τ is a declared reading map, its basis value an input to the toy. The damaged copy lacks induced, τ, Δt and sector membership; mark all four before repairing. Restore Δt=1 TU, τ(E)=1 in each original basis, induced=i for a and −i for b, and the assumed set {a,b}. Retain the ordered six-factor rows, all K,V,a,m,r entries and the rebasing data. The full-source operator coefficients, topology carriers/factors, boundary-sector values and time/action normalization are not recovered. Cite S02 `/backbone_sequence/14` and S03 `/findings/8`; retain the latter's missing-body gate as source-reported, not freshly replayed.

## Scoring rubric — 100 points

| Task | Points and partial-credit basis |
|---|---|
| 01 | 4 state/time/boundaries; 4 dimensions and convention; 4 source terms/gaps |
| 02 | 6 K,V,a; 3 total; 4 residual/reconstruction; 2 sign scope |
| 03 | 6 links; 2 products; 4 inverse and invariance explanation |
| 04 | 5 six-row product; 4 omission/residual; 3 unit-factor provenance |
| 05 | 4 coefficient/basis; 4 τ; 4 scalar/reconstruction; 2 global scope |
| 06 | 4 n; 4 dual contract; 4 pairing both ways; 3 failing candidate; 5 sector ledger/scope |
| 07 | 5 role classification; 4 missing-input inventory; 3 toy restoration; 3 source gap/provenance |

Award method credit for consistent arithmetic after one slip; do not award a closure conclusion that drops a factor or an admitted sector. For instructional mastery, repair any missing-factor, missing-trivialization, unit or scope error even if the numerical score is high. An answer may use equivalent notation if meanings and reconstruction remain explicit.
