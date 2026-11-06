# Lesson 7 — A signed crossing ledger

**Essential question:** What must an event record retain so another person can reproduce it without guessing?

**Goals:** Assemble multiple-family event rows; distinguish orientation, direction and polarity; reconstruct endpoint distances while preserving residuals and unresolved intervals.

**Time:** Two 55-minute periods, each retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15. Period 1 builds W1 and the reversed-family practice. Period 2 reconstructs brackets and adds contact, gap and residual rows.

**Prerequisite bridge:** Lessons 1–3 connect a full path to q, signed rate and period. Lesson 4 keeps ruler roles distinct. Lessons 5–6 distinguish event types and their existence conditions. A **ledger** is a collection of records that preserve these inputs with each derived event.

## C25.07-E1 — A record, not just a time

Use an immutable input card to avoid repeating a long path in every row. A card ID refers to the exact path, geometry, clock and evidence class. Changing any input creates a new card. Every event row needs:

| Field | What it retains |
|---|---|
| Event ID and type | Stable identity; sheet passage, contact, angular event, occupancy, gap or failure |
| Family, sheet k and input-card ID | Normal, origin, positive spacing, full path and units by reference |
| Time and epoch/clock | Numerical time plus the named start or absolute time convention |
| Bracket and signed endpoint values | Support before refinement; both adjacent brackets if applicable |
| Continuity/model rule | Linear, specified nonlinear, discontinuous or unknown |
| Direction | + for increasing q through the sheet, − for decreasing; contact/unknown separately |
| Orientation and polarity | Actual oriented normal and a separately declared polarity convention |
| Uncertainty and gaps | Model localization interval, supplied measurement bounds, unresolved inputs |
| Provenance and residual information | Source/card pointer, retained components and reconstruction rule |

For this course only, each family is assigned a **polarity label** p of +1 or −1 independently of its travel direction. It is a declared tag, not detector parity, chirality or an inferred physical charge. Never infer it from time order. If the normal reverses while origin and spacing remain fixed, q and k must both change sign to describe the same physical sheet; its direction reverses in the new coordinate convention. Retain both orientations, not an unsigned normal alone.

## C25.07-W1 — Worked two-family ledger

**Input card SYN-FWD:** Fixed perpendicular Cartesian axes; synthetic elapsed seconds from epoch E0 (not an actual UTC date); x(t)=((2 m/s)t,0,0), defined linearly beyond both ends of reporting interval [0,3/2] s. Family A has n=(3/5,4/5,0), o=0 m, d=3/5 m, p=+1. Family B has n=(1,0,0), o=0 m, d=2 m, p=−1. The family name B here is a label, not the Cell3 basis matrix B. Both paths are exact synthetic models; measurement bounds are not applicable, not measured zero.

Projection gives q_A=2t and q_B=t for numerical seconds. Retain both families at coincident times. All rows below have direction + and transverse passage under the declared extension. The bracket column uses evaluated model points, not fabricated observations. Distances refer to that row's sheet.

| ID | Family:k | Time s | Bracket s | Endpoint s_k values m | p |
|---|---|---:|---|---|---:|
| F-A0 | A:0 | 0 | [0,1/2] | [0,3/5] | +1 |
| F-A1 | A:1 | 1/2 | [0,1] | [−3/5,3/5] | +1 |
| F-A2 | A:2 | 1 | [1/2,3/2] | [−3/5,3/5] | +1 |
| F-A3 | A:3 | 3/2 | [1,3/2] | [−3/5,0] | +1 |
| F-B0 | B:0 | 0 | [0,1] | [0,2] | −1 |
| F-B1 | B:1 | 1 | [1/2,3/2] | [−1,1] | −1 |

Time roots are exact within SYN-FWD, so localization intervals are singleton sets {t}; retain the broader supporting brackets anyway. Boundary rows explicitly rely on the model extension for two-sided passage. Without that extension label them endpoint occupancy with only one-sided evidence. F-A2 and F-B1 both occur at 1 s, but belong to different sheet families. They are neither duplicate entries nor two independent observations: they are derived events on one synthetic trajectory.

Reconstruct F-A2 at its endpoints: s_2=(3/5)(2t−2). At 1/2 s this is −3/5 m; at 3/2 s it is +3/5 m. Reconstruct F-B1 using s_1=2(t−1), obtaining −1 and +1 m. Replaying q does not recover movement parallel to sheets; SYN-FWD preserves all original path components.

## C25.07-P1 — Practice and worked answer

Create SYN-REV by replacing x with ((−2 m/s)t,0,0), preserving geometry, polarity and extension. Report every A event on [0,3/2] s and all B events. Add separate input cards for Lesson 5's tangent s=(1 m)(t/(1 s)−1)² and a gap with known s(1 s)=−1 m, s(2 s)=+1 m, no values inside and unknown continuity. Use n=(1,0,0), o=0, d=1 m, k=0 and x=(s,0,0) for both separate cases; declare p=+1. The tangent is defined on [0,2] s. The gap card supplies no interpolating path.

**Worked answer:** q_A=−2t, q_B=−t. A indices are 0,−1,−2,−3 at 0,1/2,1,3/2 s, all direction −. B indices 0,−1 occur at 0,1 s, also direction −. Their polarities remain A:+1, B:−1. Use the same brackets as W1; the endpoint-distance pairs are the negatives of W1's corresponding pairs, because both q and k negate. For example A:−2 gives s_(−2)=(3/5)(−2t+2), hence +3/5 and −3/5 m on [1/2,3/2]. B:−1 gives s=2(−t+1), hence +1 and −1 m there.

Add T-0: tangent contact at 1 s, bracket [0,2] s with distances [1,1] m, direction “contact; no sign reversal,” localization {1 s}, exact quadratic model, p=+1. Add G-0: unresolved interval (1,2) s with endpoints [−1,+1] m, unknown continuity, time/count/direction unknown, p=+1. The gap is a row, not evidence of absence or a fabricated t=1.5 s passage.

## Residual reconstruction and uncertainty

If an observed signed coordinate y and model m are available, define residual e=y−m and preserve y=m+e. For a small synthetic illustration at times [0,1,2] s, let y=[0,11/10,19/10] m and m=[0,1,2] m. Then e=[0,1/10,−1/10] m. Addition reconstructs every y, including the negative residual. Averaging e to zero would lose its ordered structure. These are illustrative sample values, not source data or instrument evidence.

**C25.07-P2:** Reconstruct y at 2 s; then suppose its supplied bound is ±1/20 m. What is retained? **Answer:** 2+(−1/10)=19/10 m. Keep y, m, e, timestamp and bound; the allowed y interval is [37/20,39/20] m. The residual describes a difference; the bound describes supplied uncertainty. Neither substitutes for the other. For a real archive, reference original records in place rather than duplicating raw data.

> **Claim scope:** A signed ledger preserves derived structure and its provenance. It supplies no force or measured energy claim. Mechanisms remain separate hypotheses. Source-reported empirical rows must keep their own identifiers, uncertainties and dependencies; a new teaching ledger is not a replacement for them.

## Diagnostics

1. **C25.07-D1:** Can polarity be recovered by sorting event times?
2. **C25.07-D2:** Should F-A2 and F-B1 be merged because their times match?
3. **C25.07-D3:** What does an unknown gap permit you to say about its event time?
4. **C25.07-D4:** For y=9/10 m and model m=1 m, give the residual and reconstruction.
5. **C25.07-D5:** What changes when the normal is reversed but the same physical sheet is described?

**Worked answers:** (1) No: p is a separately declared convention. (2) No: retain both family IDs and shared-trajectory dependence. (3) Timing and count remain unresolved without sufficient path/continuity information. (4) e=−1/10 m and 1−1/10=9/10 m. (5) n,q,k and coordinate direction negate; d stays positive. Keep the orientation revision and separately specified polarity; do not silently identify the two signed ledgers.

**Next dependency:** [Capstone](capstone.md) assembles and audits a complete synthetic ledger using these same operations.
