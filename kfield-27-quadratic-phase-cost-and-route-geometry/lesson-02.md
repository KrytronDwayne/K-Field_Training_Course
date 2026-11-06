# Lesson 2 — From plane counts to phase cost

**Essential question:** What definitions turn motion across planes into a cost?

**Goals:** Calculate signed plane coordinates and rates; derive a rate cost from declared rulers; distinguish accumulated cost from net count.

**Bridge:** Lesson 1 taught matching-product sums and quadratic forms. We now attach those operations to a ruler. A plane is a flat surface; a unit normal is a length-one vector perpendicular to it. The dot product n·z is the sum of matching components and gives the signed distance along a unit normal. For example, (0,1)·(3,4)L=4L.

Two 55-minute sessions, each 5 retrieval + 20 instruction/example + 15 practice + 15 diagnostic/repair minutes. Session 1 derives the rate formula; session 2 tests signs and normalization.

## C27.02-E1 — Declare the ruler before calculating

Choose an origin o, fixed unit normals n_j and positive plane spacings d_j. The index j simply labels a plane family. Define its continuous plane coordinate

p_j = n_j·(x−o)/d_j.

The numerator is a signed length; division by spacing makes p_j dimensionless. A value 1.5 means one and a half spacings from the origin along that normal. It is not an integer counter of completed crossings. Actual crossing events require an additional boundary rule; we do not round these coordinates or assign cell ownership here. Using x−o prevents an arbitrary shift of the physical origin from changing the ruler interpretation.

For a constant velocity v during a duration Δt, displacement is Δx=vΔt. Divide the change in p_j by Δt to obtain the signed rate a_j=n_j·v/d_j. The notation p-dot sometimes denotes this rate; no derivative calculation is needed for our constant segments. Assemble the rates in a column a. Declare a dimensionless positive matrix H on these plane coordinates. Then aᵀHa is a rate cost with units τ⁻². Its time accumulation on one constant segment is Δt aᵀHa, with units τ⁻¹.

Equivalently, construct a matrix A whose jth row is n_jᵀ/d_j. Then a=Av and the physical-coordinate form is G_ruler=AᵀHA. Its entries have units L⁻². You can derive this by substituting Av into (Av)ᵀH(Av). Lesson 3 explains the order of this multiplication in detail.

The exact ruler and time convention matter. If all spacings double, rates halve and quadratic rate costs become one quarter. The installed quadratic-phase-cost application instead declares a dimensionless ICRS G_phase and J=∫vᵀG_phase v dt, yielding m²/s. The integral sign means accumulation over time. That application convention is not our inverse-length-squared classroom typing and is not an archived physical conversion law. Neither convention has an implicit factor 1/2. Declare any normalization before comparing numbers [sources.md, QPC skill].

## C27.02-W1 — Two independent rulers

Use synthetic n₁=(1,0), d₁=L; n₂=(0,1), d₂=2L; o=(0,0)L; and H=I, where I=[[1,0],[0,1]] leaves a vector unchanged. Then a=(v_x/L,v_y/(2L)), so rate cost is (v_x/L)²+(v_y/(2L))². The physical matrix is diag(1,1/4)L⁻², different from Lesson 1's G.

For v=(1,2)L/τ, a=(1,1)/τ, cost rate=2/τ². Over 3τ, the displacement is (3,6)L, plane-coordinate change is (3,3), and accumulated cost is 3τ·2/τ²=6/τ. Net-count squared is 3²+3²=18, dimensionless. It is a different operation with different units.

## C27.02-P1 — Practice and worked answers

**P1a — Construct the ruler matrix independently.** From n₁,d₁,n₂,d₂ and H above, write each row of A, then multiply AᵀHA. Attempt this before consulting the answer. **Answer:** A=diag(1,1/2)L⁻¹ because the second normal is divided by 2L. H=I leaves A unchanged. The four entries of AᵀA are 1·1+0·0=1, 1·0+0·(1/2)=0, 0·1+(1/2)·0=0, and 0·0+(1/2)·(1/2)=1/4, all with units L⁻². Hence G_ruler=diag(1,1/4)L⁻². This independent construction explains both the scalar coefficients and their units.

Use the same rulers for v=(−1,2)L/τ, for two consecutive τ-long segments. Find signed rates, cumulative counts and cumulative cost. Then reverse the entire velocity for a third τ-long segment.

**Answer:** a=(−1,1)/τ, rate cost 1+1=2/τ². Starting at p=(0,0), cumulative counts after the first two segments are (−1,1),(−2,2); costs are 2/τ,4/τ. On the third segment a=(1,−1)/τ; cumulative count returns to (−1,1), but cost increases to 6/τ. Keeping just that final count would conceal the reversals. The ledger of durations and signed rates reconstructs every count increment by Δp=aΔt.

> **Claim scope:** T20 describes a positive cost on plane-passing coordinates. It does not provide these synthetic spacings, a time normalization, or numeric route bounds. Our derivation is conditional on the stated rulers. It cannot supply absent source values. Plane counts, scalar phase, modeled cost and transferred energy remain different quantities.

## C27.02-D1 — Diagnostic checks

1. What happens to rate cost if d₂ doubles while only v_y is nonzero?
2. Opposite rates +1/τ and −1/τ each last τ. Find net count and accumulated squared-rate cost.
3. Why subtract o before evaluating a position's plane coordinate?
4. May you compare a value in τ⁻¹ with a value in m²/s as if they were the same number?

**Answers:** (1) The second rate halves; its cost becomes one quarter. (2) Net count is zero, cost is 2/τ. (3) The ruler is referenced to its declared origin, not to an unstated coordinate zero. (4) No; identify the metric and normalization that relate them, if any. Matching the label “phase cost” does not establish a unit conversion.

**Next dependency:** [Lesson 3](lesson-03.md) verifies the full coordinate pullback without silently replacing a source metric.
