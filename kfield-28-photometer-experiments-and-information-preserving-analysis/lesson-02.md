# 2. Acquisition identity and raw-value preservation

Essential question: How can every later result be traced back to the acquisition?

Goals:

- Construct reversible acquisition keys
- Distinguish zero, null and absent support
- Retain faults beside raw values

## Prerequisite bridge

Use [From light to channel readings](lesson-01.md): its retained records and operations are the inputs to this lesson.

Pacing: 1 period(s) of 55 minutes. Raw retention, order and invalid branches.

## C28.02-E1 — first principles

A raw ledger is the record of what was supplied before an analysis changes its representation. A row key tells us which acquisition a value belongs to. Use device, session, sequence number and channel together; a timestamp alone may repeat. A sequence number records acquisition order even if a later display is sorted by time.

Separate three situations. A recorded zero is a value. A null is an explicit entry saying no usable numeric value was supplied. An absent expected sample has no acquired row; its gap belongs in a parallel expectation ledger. None may be replaced by the others. A gap is meaningful only relative to a declared expected schedule.

A fault flag states a diagnostic condition and its origin. It does not change the stored value. For practice, independently attach suspected saturation to row 3 with reason “synthetic instrument-status exercise.” Saturation means an instrument may have reached a response limit; the small count 1 does not itself establish saturation. We are practicing a flagged branch, not diagnosing this count from its size. Retain the reason and the fact that the flag was stipulated.

A mask is a parallel list of inclusion or validity labels for a particular view. Its purpose must be named: a ratio-validity mask is not a raw-acquisition validity mask. A corrected view, if independently justified, gets a new field and transformation record. Keeping the original key lets us join every result back to its input.

To make sorting reversible, record the original sequence beside each displayed row. For example, if rows appear in order 2,0,1, their original sequence labels restore 0,1,2. Duplicate timestamps remain separate keys. No large source copy is needed: for real archives preserve an immutable source path and hash, then store only authored derived records and their keys.

> Claim scope: The saturation flag is stipulated for a synthetic exercise. It is not inferred from the value 1. No source observation is deleted.

## C28.02-W1 — worked example

Retain all five toy rows including row 1 A=5, Clear=0. Mark its ratio transform invalid later, while its raw count remains valid as an authored input. If row 3 is independently marked suspected saturation, keep A=1 plus the flag and reason; do not silently replace its raw value.

## C28.02-P1 — guided practice

**Student task.** Create distinct device/session/sequence/channel keys for A and Clear at t=2. Write a separate gap record for expected sequence 5 at t=5 s. A display lists sequence 2,0,1: describe how to restore acquisition order. State what happens to the stipulated row-3 fault and its raw count.

### Worked answer

Two rows may share a timestamp but differ by sequence or channel. Keep both IDs. If sequence 5 is absent, add a gap record with expected time 5 s and no invented count. A display sorted by time also stores original sequence so the acquisition order can be recovered.

At t=2 use T/A/2/A and T/A/2/Clear. In the expectation ledger write T/A/5, expected midpoint 5 s, status absent, value not supplied. Sorting retained sequence labels restores 0,1,2. Row 3 keeps A=1 and C=10 with the stipulated saturation reason; no correction value is invented.

## C28.02-D1 — diagnostic checks

1. How does a recorded zero differ from a gap?
2. Can two channels at one timestamp share one row key?
3. What stays beside suspected saturation at row 3?
4. How do you restore a display ordered 2,0,1?

## Worked answers

1. Zero is an acquired numeric value; a gap records an expected but absent acquisition.
2. They need distinct channel identities within their keys; keep both.
3. Raw A=1, Clear=10, sequence/time and the stipulated diagnostic reason remain.
4. Use retained sequence labels to order 0,1,2; never infer sequence only from timestamp.

Next dependency: [lesson-03](lesson-03.md) uses these operations. Reconstruct the worked input and explain the diagnostic answers before proceeding. Source boundaries: [sources](sources.md).
