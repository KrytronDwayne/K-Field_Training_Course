# Lesson 7 — Professional scientific communication

Essential question: Can another reader recover what was known, computed, proposed and still missing?

Goals: Write a source-addressed claim ledger; preserve raw field kinds; report a complete residual vector; propagate inherited boundaries into a conclusion.

Prerequisite bridge: A source pointer identifies a location, a hash identifies bytes, and an evidence class identifies what kind of support is present. A reproducible report joins these with equations, domain, units and retained results. A polished narrative without those joins cannot be independently checked.

## C30.07-E1 — Separate the layers in connected prose

Start with the question and the actual inputs. Report source observations or facts, then the transformations you performed, then inferred relationships, proposed mechanisms and unresolved branches. If reference theory is used, identify which assumption or prediction came from it. An archived theorem report, a new exact arithmetic check and a future measurement plan receive different execution statuses even if they appear in the same paragraph.

Give each equation its domain and units. State a model as “for these dimensionless synthetic channels, y=H theta,” not “the detector obeys H” when transfer has not been established. Retain source version mismatches as distinct branches. A return address allows a reader to inspect a disagreement rather than accepting an author's compressed conclusion.

JSON is a structured text format. A field can be present with the explicit value null; absent altogether; present with the string “unknown”; or present with the string “reported.” Those cases cannot be normalized to one blank without losing meaning. Keep presence, raw kind, raw value and pointer separately. An explicitly null boundary field is not a proof that there are no restrictions. S03 AUD-010 requires inherited constituent boundaries to travel to the endpoint.

## C30.07-W1 — A compact research ledger

| Report item | Result and support | Retained limitation |
|---|---|---|
| Source closure | S02 `/backbone_sequence/19`, 18 core modules plus explicit premises and states; S03 AUD-001/AUD-011 corrections | source-attributed theorem; unloaded bodies remain unloaded |
| Fresh finite check | Lesson 3 H rows (1,1),(2,2) measure one combination; A and B both give (3,6) | synthetic dimensionless model; no calibrated detector asserted |
| Rehearsal | p=(3,1), y=(3,0), r=(0,−1), y=p+r | authored data, not acquired observations |
| Prospective test | calibrated difference and separate reference under Lesson 5 protocol | planned; device/reference/timing fields missing |
| Open return paths | T20 named route certificate; S03 AUD-008 precision linkage; source spectral revision discrepancy | numerical replay of those source claims remains gated |

A report sentence can now be precise: “The supplied backbone reports conditional closure; our synthetic inverse calculation identifies only the sum from the original two channels. A proposed calibrated difference channel separates the frozen alternatives. The rehearsal retained a −1 difference residual; no real acquisition was performed.” Each clause has a different evidence role and an inspectable address.

## C30.07-P1 — Preserve four raw statuses

Use the synthetic object `{"a":null,"c":"unknown","d":"reported"}`. Make a row for each requested pointer /a,/b,/c,/d.

| Pointer | Present? | Raw kind | Raw value |
|---|---|---|---|
| /a | yes | null | null |
| /b | no | absent | no value exists |
| /c | yes | string | unknown |
| /d | yes | string | reported |

Answer: Reconstruct the object by emitting only present fields, with their original kinds. This returns exactly a=null,c="unknown",d="reported", and no b key. Retain the object's source/version address as well. A statement “b is null” would be false because b was absent. These four rows are not observations about the archival sources; they are a synthetic data-handling exercise.

> Claim scope: S03's reported nonzero reconstruction residual `4.58938078934712923077736690075e-12` at AUD-008 remains a source-reported closure coordinate with missing full precision linkage, not literal exact zero. The named route certificate and some proof bodies remain retrieval gaps. No short summary, null endpoint, or toy calculation supplies those missing witnesses.

## C30.07-D1 — Diagnostics and worked answers

1. What is wrong with replacing (0,−1) by “small error”? **Answer:** Sign, channel and reconstruction information vanish. Keep the vector and use any summary only as an index.
2. If /a is null and /b absent, can a decoder emit both keys with null? **Answer:** No; it changes presence. Emit a only and retain b's absence.
3. A constituent excludes force inference but its endpoint boundary is null. What belongs in the report? **Answer:** The force boundary and the raw null occurrence, with return addresses; null does not remove inherited restrictions.
4. Which dates are needed? **Answer:** Source/version dates, actual fresh computation date, and planned versus actual acquisition dates separately. An unexecuted plan has no invented execution date.

Next dependency: [Lesson 8](lesson-08.md) joins the ledger and calculations into a defensible continuous research chain.
