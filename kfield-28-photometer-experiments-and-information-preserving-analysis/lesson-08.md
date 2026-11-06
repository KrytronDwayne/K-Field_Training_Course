# 8. A prospective measurement protocol

Essential question: What makes a future test reproducible?

Goals:

- Write an executable prospective protocol
- Rehearse and classify every outcome
- Version changes without overwriting earlier tests

## Prerequisite bridge

Use [Uncertainty as a structured record](lesson-07.md): its retained records and operations are the inputs to this lesson.

Pacing: 2 period(s) of 55 minutes. Complete evidence ledger / Source gaps and prospective protocol.

## C28.08-E1 — first principles

A prospective protocol is a dated, versioned instruction set fixed before new outcomes are examined. It specifies what will be measured, how rows will be identified, what event geometry will be used, which transformations will be applied, and what ends the run. A synthetic rehearsal tests whether those instructions are executable. It does not carry out the future physical experiment.

Build the protocol in order. First state a target: record channel-resolved responses around independently specified crossings, retaining both polarity comparisons and all residual fields. Then freeze instrument response identities, orientation, gain, exposure, calibration references and time conventions. Next declare raw keys, fault statuses and missing-sample rules. Freeze the geometry version and event mapping before accessing check-run values. If an earlier interval trained amplitudes or widths, name that interval and freeze the resulting parameters; do not tune them on the later check interval.

Protocol Toy-v1 rehearses the five-row acquisition. It uses q=t/(2 seconds), exact offsets (-1,0,1) seconds and no interpolation. It retains all three event windows, both defects where defined, raw and ratio masks, mean/detail pairs and the independent four-point parity exercise. It records zero Clear and the stipulated saturation flag separately. The parity exercise is a separate periodic synthetic input, not four samples silently taken from the five-row acquisition. Every output is labeled synthetic.

For a future 10-second rehearsal, specify midpoint interval [0,10) seconds with 1-second cadence: exactly ten expected midpoints 0 through 9. Exposure is 0.2 seconds, so the first exposure begins at -0.1 seconds relative to the first midpoint. Start acquisition early enough to cover it, or retain the missing support if it cannot be covered. Stop after the tenth scheduled midpoint, or record an interruption and every acquired row. Endpoints are part of a protocol, not a formatting detail.

A real forward version remains planned until its physical site, UTC epoch, ephemeris, crossing contract and calibration are supplied. Keep a blank/reference control with the same declared settings and label any difference in apparatus configuration. Retain opposite-sign responses, no apparent match, instrument failures and interruptions along with matches. Report observed records, derived arithmetic, inferred relationships, proposed mechanisms and unresolved contributors in separate fields. Reference theory can guide a comparison without replacing these records. If revision is needed after inspection, preserve v1 and call v2 exploratory until tested on a new later run.

> Claim scope: A complete protocol is planned work; a synthetic rehearsal is synthetic execution. Neither alone is a performed physical replication.

## C28.08-W1 — worked example

Rehearse the fixed q=t/2 rule on the toy five-row packet and publish all three windows, missing supports, zero-Clear status, reflection defects, even/odd components and mean/detail reconstruction. Mark execution as synthetic only. A future device run remains planned, with calibration and site/ephemeris inputs still required.

## C28.08-P1 — guided practice

**Student task.** Write a versioned prospective rehearsal plan for midpoint interval [0,10) s, 1 s cadence and 0.2 s exposure, using all declared channels. Specify expected rows, first exposure support, toy event rule, transforms, masks, controls, train/check roles, stopping rule and every retained outcome. Name what must replace the toy geometry before a real test.

### Worked answer

Freeze future duration 10 s, 1 s midpoint cadence, exposure 0.2 s, all declared channels, q=t/2 only for the toy rehearsal, both parity tests and all outcome fields. For a real forward test replace that toy geometry with a pinned physical event contract before acquisition. Store completion status, interruptions and every result; a mismatch stays in the comparison.

A complete answer names Forward-Toy-v1, expected midpoints 0..9, first exposure [-0.1,0.1] s and all channel/setting IDs. No training parameters are fitted in the toy. Freeze the check rule without future values, retain the exact window and ratio masks, both parity operators and mean/detail fields, and identify a separate same-setting blank/reference control. Stop after the tenth scheduled midpoint or log interruption. Physical v1 requires site, UTC time convention, ephemeris, physical crossing and calibration/transfer inputs. Keep mismatches and revisions with their version IDs.

## C28.08-D1 — diagnostic checks

1. How many midpoint samples belong to [0,10) at 1-second cadence?
2. What is the status of the five-row rehearsal?
3. What happens if v1 mismatches a channel?
4. Which outcomes enter the final ledger?

## Worked answers

1. Ten: 0 through 9. Endpoint 10 is excluded.
2. Executed synthetic arithmetic; no performed physical measurement is claimed.
3. Keep the mismatch and its residuals; retain v1. Any tuned v2 is separately labeled exploratory.
4. Every match, opposite sign, weak response, mismatch, invalid transform, gap, fault and interruption, with input identities.

Next dependency: [capstone](capstone.md) uses these operations. Reconstruct the worked input and explain the diagnostic answers before proceeding. Source boundaries: [sources](sources.md).
