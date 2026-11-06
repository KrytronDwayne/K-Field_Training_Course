# Lesson 5 — Route comparison and constraints

**Essential question:** When can we prove that a route is least costly?

**Goals:** State a fixed optimization specification; derive a finite-route lower bound; distinguish a feasible example, an attained minimum and a changed problem.

**Bridge:** Lesson 4 compared two paths. Beating one competitor does not eliminate every other possible path. We now use positivity to bound all finite piecewise-constant paths with the same endpoints, time and metric.

Two 55-minute sessions: finite minimum proof, then changed constraints. Each: 5 retrieval, 20 explanation/example, 15 practice, 15 diagnostics/repair.

## C27.05-E1 — Separate average motion from deviations

An **admissible** path is one allowed by the problem's rules. Fix start, end, total duration T>0 and a constant positive symmetric G. For the core proof, allow any finite number of constant-velocity segments of positive duration adding to T, with no speed limit or obstacle. Let D=end−start. Define average velocity v-bar=D/T, and on each segment define δ_i=v_i−v-bar. Delta, δ, labels a signed deviation vector, not a deleted error.

Because Σ_i Δt_i v_i=D and Σ_i Δt_i=T,

Σ_i Δt_i δ_i = D−T v-bar = 0.

Expand the quadratic on each segment just as you expand (a+b)²:

(v-bar+δ_i)ᵀG(v-bar+δ_i)
= v-barᵀGv-bar + 2 v-barᵀGδ_i + δ_iᵀGδ_i.

Symmetry of G makes the two mixed scalar terms equal. Multiply by Δt_i and add. The mixed terms cancel because the duration-weighted deviations sum to zero. This gives the exact decomposition

J = T v-barᵀGv-bar + Σ_i Δt_i δ_iᵀGδ_i.

Each term in the final sum is nonnegative. Thus L_b=T v-barᵀGv-bar is a **lower bound**, meaning no admissible finite path can cost less. Constant velocity v-bar has every δ_i=0, so it reaches the bound when it is admissible. Its cost is an **upper bound** U_b on the minimum because we have an actual allowed route at that cost. When U_b=L_b, the gap U_b−L_b is zero and the minimum is certified for this specification. L_b denotes a bound, not the length unit L.

The deviations remain useful: reconstruct v_i=v-bar+δ_i using the original durations. Keeping only the nonnegative excess cost would lose this signed information.

**Recognition-only continuum extension.** The same decomposition applies to absolutely continuous paths with square-integrable velocity: paths obtained by accumulating a velocity over time, with finite integral of squared speed. For them, integrals replace sums, ∫δ dt=0 and J=T v-barᵀGv-bar+∫δᵀGδ dt. The nonnegative integral gives the same lower bound. This statement assumes the defined integrals exist and the path is recovered from its velocity; it is not inferred solely from checking a finite grid. No continuum calculation is required in the capstone. Constant velocity belongs to both classes.

## C27.05-W1 — An exact synthetic certificate

Use Lesson 4's specification: D=(2,0)L, T=2τ, G=[[2,1],[1,2]]L⁻², no obstacles. Then v-bar=(1,0)L/τ, rate=2/τ² and L_b=4/τ. The straight route attains 4/τ, so U_b=4/τ and gap=0/τ.

For the dogleg, δ₁=(0,1)L/τ and δ₂=(0,−1)L/τ. Each has δᵀGδ=2/τ². The excess is τ·2/τ²+τ·2/τ²=4/τ. Thus J=4/τ+4/τ=8/τ, agreeing with direct calculation. For two equal-duration segments v-bar+δ and v-bar−δ, excess is 2τ δᵀGδ; including the duration is essential for units.

## C27.05-P1 — Practice and worked answers

**P1a — Independent finite bound proof.** Given any finite list of positive durations totaling T and velocities whose displacements total D, prove ΣΔt_iδ_i=0 for δ_i=v_i−D/T. Expand the quadratic, show why its mixed sum vanishes, and state when the bound is attained. **Answer:** ΣΔt_iδ_i=ΣΔt_iv_i−(D/T)ΣΔt_i=D−(D/T)T=0. Substitution v_i=v-bar+δ_i gives the constant term T v-barᵀGv-bar, mixed sum 2v-barᵀG(ΣΔt_iδ_i)=0, and deviation sum ΣΔt_iδ_iᵀGδ_i≥0. Therefore J≥T v-barᵀGv-bar. Constant velocity v-bar makes every δ_i zero and attains equality if admissible. This proof requires the fixed symmetric positive G, endpoints and T; it is not a conclusion from a two-route sample.

Recompute the dogleg excess from δ=(0,1)L/τ. Next allow the same displacement but T=4τ. Finally place an obstacle on the straight route while keeping T=2τ. What survives of the proof?

**Answer:** Excess=2τ·2/τ²=4/τ. For T=4τ, v-bar=(1/2,0)L/τ, rate=1/(2τ²), and the straight cost is 4τ/(2τ²)=2/τ. Lower cost here does not beat the old fixed-time problem: the time rule changed. With an obstacle, the algebraic bound 4/τ still applies to every remaining admissible path, but the previous upper bound is no longer supplied by the forbidden straight path. A feasible replacement path is needed for an upper bound; attainment of 4/τ is not established. Do not invent an obstacle geometry or a new optimum.

> **Claim scope:** This is an exact synthetic finite-route proof, with a separately stated continuum extension. T20 is an overview of a different named certificate. Neither these bounds nor a historical maximum-residual objective may be substituted for that source's missing least-cost contract.

## C27.05-D1 — Diagnostic checks

1. Why must the duration-weighted deviations sum to zero?
2. Why does comparing just A and B not prove the minimum?
3. What breaks if G is not positive?
4. What changes when an obstacle excludes the attaining path?

**Answers:** (1) They are defined relative to displacement divided by total time, so D−Tv-bar=0. (2) Other admissible paths have not been compared; the decomposition covers them. (3) The excess need not be nonnegative, so the asserted lower bound can fail. (4) The lower-bound argument survives; the old attaining path does not furnish an admissible upper bound.

**Next dependency:** [Lesson 6](lesson-06.md) distinguishes this exact certificate from incomplete source records and finite-precision closure.
