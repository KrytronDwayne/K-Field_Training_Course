# 7. Uncertainty as a structured record

Essential question: How can uncertainty retain its causes and dependencies?

Goals:

- Propagate positive interval bounds
- Track shared timing and exposure separately
- List unresolved calibration and channel contributors

## Prerequisite bridge

Use [Scale and channel comparisons](lesson-06.md): its retained records and operations are the inputs to this lesson.

Pacing: 2 period(s) of 55 minutes. Named uncertainty contributors and interval products / Shared timing offsets and exposure support.

## C28.07-E1 — first principles

An uncertainty record names what remains unresolved about the measurement and its interpretation. Different contributors have different structures: a shared clock offset moves all channel times together; an exposure covers an interval; a calibration factor may have a stated range; a gap is missing acquisition support; an unresolved wavelength dependence is a channel pattern. One number cannot describe all of these operations.

For a finite bound exercise, suppose factor k is in [1.9,2.1] units/count and input x in [0.9,1.1] counts. “Units” is a deliberately unspecified output unit, not a claim of watts or joules. Assume every combination inside this rectangular box is permitted. Both factors are positive, so the smallest product uses both lower endpoints: 1.9*0.9=1.71 units. The largest uses both upper endpoints: 2.1*1.1=2.31 units. The nominal product 2*1=2 lies inside. If factors can be negative, compute all four endpoint products before selecting bounds. If their dependence forbids some combinations, this box may be conservative; do not silently claim independent repeated observations from it.

Now suppose all midpoint times have one common unknown clock offset delta_t in [-0.1,0.1] seconds. Nominal event midpoint 2 maps to [1.9,2.1]. Exposure duration 0.2 has half-width 0.1, so possible exposure support runs from 1.9-0.1=1.8 to 2.1+0.1=2.2 seconds. This is a union of possible supports, not a claim that each exposure lasts 0.4 seconds. The common offset cancels in time differences between simultaneous channels.

Record orientation and angular resolution as unresolved if they are not supplied; do not invent bounds. Calibration missing, zero Clear, suspected saturation and absent sequence 5 are separate ledger fields. The zero count is still known even when its ratio cannot be formed.

Source card T35 keeps radiometric calibration (a link to optical quantities), exposure transfer (how time integration affects a signal), raw bytes, blank/reference measurements, angular uncertainty and an independent replay as open obligations. Its reported photon-equivalent model input is not an apparatus measurement of transferred energy. T50 additionally describes equal outputs from distinct gain/responsivity factorizations: if output is a product, the same product alone need not identify each factor. This is an identifiability problem. For a small illustration, 2*6=3*4=12; output 12 cannot select which pair produced it. These boundaries identify the measurements a prospective experiment needs.

> Claim scope: Bounds are synthetic assumptions. T35/T50 are source-reported boundaries, not new calibration measurements or fresh formal replay.

## C28.07-W1 — worked example

Synthetic factor k in [1.9,2.1] units/count and x in [0.9,1.1] counts give product in [1.71,2.31] units under the stated box of allowed combinations and positive factors. This exercise is not an instrument calibration. With timing offset in [-0.1,0.1] s, an event at 2 s maps to [1.9,2.1] s before exposure support is considered.

## C28.07-P1 — guided practice

**Student task.** First compute both product bounds for positive box inputs k in [1.9,2.1] units/count and x in [0.9,1.1] counts, stating the box assumption. Then an exposure lasts 0.2 s and its midpoint may lie anywhere in [1.9,2.1] s. Compute the union of possible exposure supports and explain why each exposure does not last 0.4 s. If all channels share the same clock offset, state whether their offsets should be treated as independent. List the zero-Clear, saturation and absent-sample records separately.

### Worked answer

A duration 0.2 s centered at an uncertain midpoint in [1.9,2.1] s has possible support [1.8,2.2] s. Keep the common clock offset as shared across channels rather than claiming five independent timing errors. Record zero-Clear, saturation and absent-sample branches separately.

The positive product bounds are [1.9*0.9,2.1*1.1]=[1.71,2.31] output units, assuming every combination in the declared box is allowed. Earliest support is 1.9-0.1=1.8 s; latest is 2.1+0.1=2.2 s. Each individual exposure has length 0.2 s; the union is wider because its midpoint can move. Row 1 has supplied synthetic C=0, row 3 has a stipulated flag, and expected row 5 is absent: these are three different records.

## C28.07-D1 — diagnostic checks

1. Multiply the positive lower endpoints.
2. Does possible support [1.8,2.2] imply exposure duration 0.4?
3. Do two simultaneous channels have independent clock offsets here?
4. What lets counts become measured transferred energy?

## Worked answers

1. 1.9*0.9=1.71 output units; upper endpoints give 2.31.
2. No. Each exposure lasts 0.2; midpoint uncertainty shifts its location.
3. No. Both share delta_t, which cancels in their time difference.
4. An appropriate calibrated apparatus and exposure-transfer account with required inputs; a photon-equivalent model value alone does not supply this.

Next dependency: [lesson-08](lesson-08.md) uses these operations. Reconstruct the worked input and explain the diagnostic answers before proceeding. Source boundaries: [sources](sources.md).
