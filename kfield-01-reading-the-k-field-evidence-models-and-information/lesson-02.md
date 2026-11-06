# Lesson 2 — Following a claim to its source

**Essential question:** What must travel with a claim so another reader can find and assess the same statement?

**Goals:** Build a file–locator–version–evidence address; distinguish a reported measurement from a finite replay; preserve the scope of a source status.

**Prerequisite bridge:** Lesson 1 classified claim roles. Now add access: a geometric derivation in its source remains source-reported to a reader who has not checked the proof.

## Build a complete source address

A filename finds a container, not a passage. A locator selects a passage inside it. A version identifies which contents were read. SHA-256 is a content fingerprint written as 64 hexadecimal characters. It checks byte identity against a pinned version, not whether the contents are correct.

JSON is structured text with named fields and ordered lists. A JSON pointer follows slash-separated field names. List positions start at zero. Thus `/backbone_sequence/0/invariants` selects the invariants field of the first item in the backbone sequence. Markdown can instead use a heading and numbered item. Full paths and fingerprints are in [sources.md](sources.md); S02 and S06 below are short labels for those records.

An evidence address contains the source ID and exact path, version fingerprint, locator, claim, evidence class, and access limits. Keep a source's status wording separate from your verification. Reading a “closed” label is different from freshly checking every proof.

## Worked example A: a geometric identity

S02 is the mature archival JSON. At `/backbone_sequence/0/invariants`, it lists `B R B^T=I`. This is a source-stated geometric identity. Read it here as “the declared combination of coordinate rules returns the input.” A transformation is a rule taking coordinates in and giving coordinates out. Lesson 5 teaches a finite arithmetic version. Deriving the full matrix identity is outside the core assessment.

At `/proof_contract`, S02 gives authority as “mature locked values at their stored precision.” Its orientation contract uses ICRS columns [a b c] and an intentional left-handed determinant. ICRS names the spatial reference frame; [a b c] fixes three basis directions in order. Do not swap that order or borrow constants from another branch. Source-local G is called M_cell in this course; source-local R is R_cell. This explicit naming translation does not change the metric.

These source labels are recognition vocabulary here. A basis provides the ordered directions used to assign coordinates. A determinant is a signed volume factor; its sign records orientation. A metric is a rule for computing geometric lengths and angles from coordinates. You need not calculate any of these for this address card. Lesson 5 introduces a small coordinate example before asking you to calculate a return identity.

At `/mature_locked_cell3/direct_reciprocal_closure_max_abs`, S02 reports `2.8939781400741195e-16`. The notation e-16 means multiply by 10 to the power −16. This is a reported numerical closure discrepancy, not an instrument residual or exact zero. The course checked source bytes and the locator; it has not rerun the full locked-matrix calculation.

## Worked example B: measurement and replay

S06, numbered item 2, **Reported angular response**, reports 180,000 samples, 2,000 rotations, ten channels, and a recovered clock of 15.0407096514 degrees/hour. A degree measures angle; degrees/hour measures angular change per hour. These are metadata describing a record, not every reading. The acquisition schema is needed to know whether a “sample” counts a multichannel acquisition or an individual channel value.

The same item says `SiderealReplay` realizes 97 finite states. A state is a model configuration; finite means the model has a specified finite collection of configurations. Those 97 states are not 97 newly measured rotations. The source gives a supplied spectral-response-law scope and separately excludes physical K-field co-rotation from that conclusion. Item 3 makes Earth coupling conditional on `EarthOnlyAttribution`, an explicit additional attribution premise. This course does not silently supply it.

Here a spectral response law describes how a response is organized by repeating components. Co-rotation means rotating together physically. A replay can reproduce a specified response rule without by itself establishing that physical motion. “Conditional” means the conclusion requires an additional stated premise. These interpretations let you preserve the source's scope without performing spectral analysis or a formal proof.

> **Claim scope:** S06 is a retrieved source narrative. Its reported formal replay and reported measured response have different authority. No compiler was run and no raw instrument series was analyzed here. The raw measurement residual remains a retrieval gap.

## Guided practice

Make two address cards for S06 item 2: A for 180,000 samples, B for 97 replay states. Give the full path and hash using sources.md, then distinguish claim roles and access limits. Explain why dividing 180,000 by ten does not establish the acquisition count per channel without its schema.

## Diagnostic checks

1. What does zero in `/backbone_sequence/0/invariants` select?
2. Does matching SHA-256 establish a theorem? What does it establish?
3. A student writes “97 measured states establish physical co-rotation.” Identify both scope changes.
4. Make an address card for the closure discrepancy, including what has and has not been verified.

## Worked answers

Guided cards: A uses the exact S06 path and hash, item 2, reported acquisition metadata, raw samples unavailable here. B uses the same address but identifies reported finite replay states, with no fresh formal execution. The sampling distribution requires an acquisition convention; division alone cannot supply it.

1. The first list item; indexing starts at zero.
2. It checks byte identity with the pinned version. Theorem correctness needs the relevant mathematical checks.
3. Replay states were promoted to measured states, and a supplied response law was promoted to physical co-rotation beyond its stated scope.
4. S02, complete path and hash from sources.md; `/mature_locked_cell3/direct_reciprocal_closure_max_abs`; reported 2.8939781400741195 × 10^−16; archival computational witness. Byte identity and field presence were checked, but the locked calculation was not reproduced. Retain the discrepancy as reported information.

**Next dependency:** [Lesson 3](lesson-03.md) examines what reconstruction requires beyond metadata.
