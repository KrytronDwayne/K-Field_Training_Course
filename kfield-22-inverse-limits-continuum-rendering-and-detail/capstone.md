# Capstone — A history-preserving continuum report

Deliver a single report containing the seven numbered tasks below, your input ledger, calculations, source card and retained-information ledger. Use fractions and distinguish dimensionless coordinates from LU displacements. The mathematical examples are synthetic; source definitions are identified in sources.md. You may consult lessons and glossary. Three 55-minute sessions are allocated in the teacher guide. No external data or software is required.

Each task has four points: one for declared inputs and scope; one for correct operation; one for reconstruction or source classification; one for retained information and boundaries. The task-specific key below explains what earns each point. Total:28 points. An arithmetic correction must leave a labeled record of the original input or failed proposal.

## C22-CAP-01

From balanced digits (0,1,−1,0,1), produce signed sums and residues at moduli 3,9,27,81,243; test all reductions. Also test the proposal (1,8) at moduli3,9. Embed the valid history as triples with two zero coordinates. State the continuation status.

Prerequisite trail: [lesson-01](lesson-01.md), C22.01-E1 → C22.01-W1 → answered C22.01-P1; check C22.01-D1. Output: the named calculations and retained-information statement for this operation.

## C22-CAP-02

Find real and address distances between 4 and13. Find triple address distance between (1,4,0) and (28,13,0). Name what each distance measures.

Prerequisite trail: [lesson-02](lesson-02.md), C22.02-E1 → C22.02-W1 → answered C22.02-P1; check C22.02-D1. Output: the named calculations and retained-information statement for this operation.

## C22-CAP-03

Specify an exact infinite triple by using all −1 digits in its first coordinate and all0 digits in the other two. Produce its first four levels, verify compatibility generally, and count next triples for a prefix with no fixed continuation.

Prerequisite trail: [lesson-03](lesson-03.md), C22.03-E1 → C22.03-W1 → answered C22.03-P1; check C22.03-D1. Output: the named calculations and retained-information statement for this operation.

## C22-CAP-04

For the exact triple rule in task03, compute z₂ and r₂ using B=diag(2,3,4) LU. Give its signed limiting remainder and certify a uniform physical tail≤1/1000 LU by the smallest guaranteed depth. Separately choose depth for Σ2^(−j) tail≤1/32. Compare full normalized images of h=(1,−1,−1,…) and k=(0,1,1,…) in the first coordinate, zeros elsewhere; preserve both histories.

Prerequisite trail: [lesson-04](lesson-04.md), C22.04-E1 → C22.04-W1 → answered C22.04-P1; check C22.04-D1. Output: the named calculations and retained-information statement for this operation.

## C22-CAP-05

Evaluate g₂(a)=a mod9 for depth3 addresses 7,16,25. Supply their balanced third digits and explain what remains invisible. Apply this first-coordinate observation to (a,0,0) while retaining every coordinate.

Prerequisite trail: [lesson-05](lesson-05.md), C22.05-E1 → C22.05-W1 → answered C22.05-P1; check C22.05-D1. Output: the named calculations and retained-information statement for this operation.

## C22-CAP-06

For v=(2,0,6,4), compute P₀v,Q₀v,Q₁v, reconstruct P₁v then v, and state which infinite-reconstruction assumptions this calculation does not supply.

Prerequisite trail: [lesson-06](lesson-06.md), C22.06-E1 → C22.06-W1 → answered C22.06-P1; check C22.06-D1. Output: the named calculations and retained-information statement for this operation.

## C22-CAP-07

For the explicitly defined D on real ℓ², test y_n=1/n² and compute Dy. Use the Lesson07 source card to report what is and is not supplied for a proposed archival operator H. Classify the source renderer, the synthetic D calculation, and any proposed physical mechanism separately.

Prerequisite trail: [lesson-07](lesson-07.md), C22.07-E1 → C22.07-W1 → answered C22.07-P1; check C22.07-D1. Output: the named calculations and retained-information statement for this operation.

## Full answer key and marking rubric

Use after independent work. Award a point when its corresponding operation is correct or is corrected with a reproducible explanation; unsupported numerical answers do not earn the scope/retention points.

### C22-CAP-01 answer

Signed sums 0,3,−6,−6,75; residues 0,3,21,75,75. The reductions are 0,3,21,75 respectively. The triple rows are (0,0,0),(3,0,0),(21,0,0),(75,0,0),(75,0,0). The proposal fails: 8 mod3=2≠1; keep its input and failed equation. No continuation was specified.

- 1 point: Declare digit order, moduli and dimensionless triples.
- 1 point: Compute both signed sums and residues.
- 1 point: Show all reductions and identify failed8 mod3.
- 1 point: Keep failed proposal, zeros and unresolved continuation.

### C22-CAP-02 answer

Difference 9=3² gives real distance9 and address distance1/9. Triple coordinate address distances are 1/27,1/9,0, maximum1/9. Real distance uses number-line separation; address distance uses shared low-order residues. All are dimensionless in this exercise.

- 1 point: Name the two distance conventions.
- 1 point: Compute9 and1/9.
- 1 point: Compute triple maximum1/9.
- 1 point: Retain identical third coordinate and distinguish shared prefix from real separation.

### C22-CAP-03 answer

First signed coordinates −1,−4,−13,−40 give residue triples (2,0,0),(5,0,0),(14,0,0),(41,0,0). At general depth t_d=−(3^d−1)/2; t_(d+1)−t_d=−3^d, so every reduction holds. A prefix without the prescribed continuation has 3³=27 next triples. The all-negative rule selects one of them at each level.

- 1 point: Specify full rules for all three coordinates.
- 1 point: Produce four signed/residue levels.
- 1 point: Give general difference −3^d and27 extension count.
- 1 point: Distinguish selected exact rule from unresolved-prefix alternatives.

### C22-CAP-04 answer

z₂=(−2/9,0,0), r₂=(−4/9,0,0) LU. The all-negative limit is z=(−1/4,0,0), r=(−1/2,0,0) LU; signed remaining displacement is (−1/18,0,0) LU. The general norm bound is ||B||∞/(4·3^N)=1/3^N LU, so N=7 since 1/729>1/1000≥1/2187. Binary tail≤1/32 first at N=5. The endpoint sum from j=2 onward is1/6, giving z(h)=z(k)=(1/12,0,0). They differ at their first residue and remain different histories paired with the same image. Store exact rule, depth, partial values, bounds and signed known remainder.

- 1 point: Declare synthetic B, LU, rule and tolerance.
- 1 point: Compute partial image and choose depths7 and5.
- 1 point: Derive endpoint equality and signed remainder.
- 1 point: Retain both histories, depth ledger and uniform-bound scope.

### C22-CAP-05 answer

Outputs 7,7,7. Full three-digit prefixes are (1,−1,1),(1,−1,−1),(1,−1,0); third digits1,−1,0. The observation reads depth2 and hides the third and later digits. Keep three separate input triples (7,0,0),(16,0,0),(25,0,0), outputs and unresolved continuations.

- 1 point: Declare g₂ and depth3 input triples.
- 1 point: Compute outputs7.
- 1 point: Recover three distinct third digits.
- 1 point: Retain all input rows and unresolved finer continuations.

### C22-CAP-06 answer

P₀v=(3,3,3,3), Q₀v=(−2,−2,2,2), Q₁v=(1,−1,1,−1). The first two sum to(1,1,5,5)=P₁v; all three sum to v. Entries are dimensionless and signed. An infinite version still needs an ambient space, limiting subspace and convergence mode; retain every sector and any complementary component.

- 1 point: Declare vector and finite equal-weight operations.
- 1 point: Compute all three sectors.
- 1 point: Reconstruct P₁v and v.
- 1 point: Retain signed entries and name infinite-scope obligations.

### C22-CAP-07 answer

The input-square sum Σ1/n⁴≤Σ1/n²<∞. The weighted sum Σn²/n⁴=Σ1/n²<∞ by the taught dyadic-block bound, so y∈Dom(D), Dy=(1/n)∈ℓ². The M18 card supplies an address object and renderer; it does not supply a particular H carrier/domain/action/inner product/convergence mode. Mark these not supplied for H. Renderer definitions are source facts, its bound is derived mathematics, D is a synthetic mathematical example, and no empirical or physical mechanism is established or required by these calculations.

- 1 point: Declare ℓ², D action and domain.
- 1 point: Bound input and weighted square sums.
- 1 point: Compute Dy and classify H missing contracts.
- 1 point: Keep source/derived/synthetic/mechanism categories separate.

## Backward audit and final report check

No new technique appears in this assessment. Task04 applies Lesson04's all-positive computation to an all-negative rule using signed arithmetic already practiced in Lesson03. The other calculations use the answered practice packets directly; integration and information accounting supply the synthesis. Before submission check the residue ladder, reproduce the geometric bound by subtraction, sum the three detail sectors entrywise and review H against all five contract fields. The source card's omissions stay omissions; filling them with the example D would change the subject.
