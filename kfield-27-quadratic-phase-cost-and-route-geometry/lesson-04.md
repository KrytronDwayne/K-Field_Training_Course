# Lesson 4 — Integrating cost along a path

**Essential question:** What information is needed to turn instantaneous cost into a path total?

**Goals:** Construct a signed segment ledger; compute cumulative cost and endpoint; verify subdivision without losing the original path.

**Bridge:** We can evaluate a quadratic rate in either coordinate system. Now multiply each rate by the time for which it acts. “Integrating” here means adding those contributions; our piecewise-constant velocities make the calculation exact using multiplication and addition alone. Piecewise means that each declared segment follows its own rule.

Two 55-minute sessions: the first builds the ledger, the second checks subdivision and reconstruction. Each uses 5 retrieval, 20 teaching/example, 15 practice and 15 diagnostics/repair minutes.

## C27.04-E1 — A path is more than its endpoints

Specify a fixed coordinate frame and origin, start position, strictly positive durations Δt_i, and velocities v_i. Index i labels time-ordered segments. During a segment the velocity is constant, so Δx_i=v_iΔt_i. Add displacements successively to recover positions. Reject missing durations, decreasing times and incompatible coordinate units; do not silently reorder them.

With one constant positive metric G, define

J = Σ_i Δt_i v_iᵀGv_i.

The symbol Σ means “add the following expression for every listed index.” Under G's L⁻² classroom typing, each rate has units τ⁻² and J has units τ⁻¹. The cumulative cost after segment k is the sum only through k. Keep the segment values, signs, durations and ordering even when two paths have the same final J.

This is exact for the declared piecewise-constant path. If a real instrument only samples velocities at endpoints, a constant segment between samples is a modeling choice. A linear interpolation would mean velocity changes evenly between endpoints and generally gives a different quadratic integral. For example, velocities (0,0) then (2,0)L/τ over τ have constant-mean-velocity cost 2/τ under our G; a genuinely linearly increasing velocity has cost 8/(3τ). The latter is a recognition-only extension, not a required calculus exercise. State interpolation and retain unresolved between-sample structure; cadence alone is not an accuracy guarantee. Our core problems supply the entire segment rule, so this ambiguity is absent.

## C27.04-W1 — Straight path and dogleg

Use G=[[2,1],[1,2]]L⁻², start (0,0)L, two segments of duration τ, and no obstacles. Let path A have velocities (1,0),(1,0)L/τ. Path B has velocities (1,1),(1,−1)L/τ. Evaluate the cross term with its sign on each segment.

| Path/segment | Δt/τ | v in L/τ | End position in L | Rate in τ⁻² | Segment J in τ⁻¹ | Cumulative J in τ⁻¹ |
|---|---:|---|---|---:|---:|---:|
| A1 | 1 | (1,0) | (1,0) | 2 | 2 | 2 |
| A2 | 1 | (1,0) | (2,0) | 2 | 2 | 4 |
| B1 | 1 | (1,1) | (1,1) | 2+2+2=6 | 6 | 6 |
| B2 | 1 | (1,−1) | (2,0) | 2−2+2=2 | 2 | 8 |

Draw A through (0,0),(1,0),(2,0). Draw B through (0,0),(1,1),(2,0). Both end at (2,0)L after 2τ. The dogleg costs 8/τ versus 4/τ for A. The scalar total does not show that B's expensive segment came first; the ledger does.

## C27.04-P1 — Practice and worked answers

Reverse B's segment order. Then split each A segment into two equal half-τ segments without changing velocity. Show endpoint and cumulative cost in each case, keeping a map to the old segments.

**Answer:** Reversed B has endpoint sequence (1,−1),(2,0)L, rates 2,6 per τ², contributions 2,6 per τ and cumulative costs 2,8 per τ. Total and endpoint match B, but intermediate position differs. For A, four half-τ segments each have rate 2/τ² and cost 1/τ. Cumulative costs are 1,2,3,4 per τ and positions (1/2,0),(1,0),(3/2,0),(2,0)L. New segments 1–2 reconstruct old A1 and 3–4 reconstruct A2 by adding their durations and increments. No original velocity is discarded.

> **Claim scope:** These are explicitly synthetic complete paths. They are not a numerical replay of the named source route certificate. A coordinate cost gives a model total, not a detector energy measurement. No mean or scalar replaces the signed segment ledger.

## C27.04-D1 — Diagnostic checks

1. What is wrong with adding rates while omitting durations?
2. If each dogleg duration doubles with the same velocities, what endpoint and cost result?
3. Does the reversed dogleg have the same cumulative history?
4. Which conditions are needed before treating sampled data as our exact segment model?

**Answers:** (1) The result retains τ⁻² units and changes under arbitrary resampling; it is not J. (2) Endpoint (4,0)L and J=16/τ after 4τ, a different path specification. (3) No; first cumulative values are 2/τ versus 6/τ, though both finish at 8/τ. (4) Explicit durations, frame, metric and interpolation, plus the assumption of constant velocity within each segment. Physical variation not supplied by the samples remains unresolved, not deleted.

**Next dependency:** [Lesson 5](lesson-05.md) asks whether the straight route minimizes cost among all allowed paths.
