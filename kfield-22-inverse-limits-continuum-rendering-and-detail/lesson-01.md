# Lesson 01 — Finite prefixes and compatible sequences

Essential question: How can several short addresses describe the beginning of one history?

Goals: Compute a residue from signed digits; test every adjacent reduction; preserve an incompatible proposal with its failure record.

Bridge and pacing: You need signed arithmetic, powers and division with remainder. Courses 06, 07 and 18 provide the wider series context; all address operations needed here are rebuilt below. One 55-minute period: retrieval 5, explanation/example 20, practice 15, diagnostics/repair 15 minutes.

## C22.01-E1 — A remainder is an address

For a positive integer m, two integers represent the same residue modulo m when their difference is a multiple of m. We store the representative between 0 and m−1. Thus −2 and 7 represent the same residue modulo 9: adding one copy of 9 to −2 gives 7. The expression “a mod m” means this stored remainder, not an approximate decimal.

At depth d we use m=3^d. Increasing d adds one base-three digit. Our balanced digits are −1, 0, 1 and are stored **least significant first**: u₁ contributes units, u₂ contributes threes, u₃ contributes nines. To convert a prefix, form t_d=u₁+3u₂+…+3^(d−1)u_d and then a_d=t_d mod 3^d. The signed t_d and the nonnegative a_d are two representations, not two different histories. Preserve both when calculating.

The reduction map π_d takes a depth-(d+1) residue and reduces it modulo 3^d. A sequence is compatible when π_d(a_(d+1))=a_d at every step. Why does adding a digit work? Its contribution is a multiple of 3^d, so it changes nothing modulo 3^d. Compatibility checks consistency across resolution levels; it does not require the displayed integers to increase.

The source uses three coordinates. A_d=(Z/3^d Z)^3 means ordered triples of residues; Z here denotes integers, and the exponent 3 means three entries. Reduce each coordinate separately. An example using one coordinate can be embedded as (a_d,0,0); the two zeros remain part of the record. Addresses and digits are dimensionless.

## C22.01-W1 — Worked history

Use digits (1,−1,0,1,−1). Read each row as one more digit, not as a reversal of the previous row.

|d|3^d|signed sum t_d|stored a_d|
|---|---|---|---|
|1|3|1|1|
|2|9|1−3=−2|7|
|3|27|−2+0=−2|25|
|4|81|−2+27=25|25|
|5|243|25−81=−56|187|

Now reduce: 7 mod3=1; 25 mod9=7; 25 mod27=25; 187 mod81=25. Every adjacent test passes. The triple history is (1,0,0), (7,0,0), (25,0,0), (25,0,0), (187,0,0). The unchanged integer 25 at two depths carries different depth labels.

> Claim scope: S02, /backbone_sequence/17/definitions and /backbone_sequence/2/recursions/ternary_address supply the residue system. This small digit example is synthetic, verified arithmetic. It is not a measured trajectory. Five rows leave all later digits unresolved.

## C22.01-P1 — Practice, then check

Convert digits (0,1,−1,0,1) at depths 1–5. Test every reduction. Separately test the proposed depth-1/depth-2 list (1,8).

Answer: signed sums are 0,3,−6,−6,75; residues are 0,3,21,75,75. Reductions give 3 mod3=0, 21 mod9=3, 75 mod27=21, 75 mod81=75. The proposal (1,8) fails because 8 mod3=2, not 1. Save the original proposal and failed equation; do not silently replace 8.

## Diagnostics — C22.01-D1

1. Are −2 and 7 different depth-2 addresses?
2. Must a compatible residue list increase as ordinary integers?
3. Does a five-digit prefix specify the sixth digit?
4. Is the triple transition (1,0,2) → (7,3,5), at moduli 3 and 9, compatible?

Worked answers: (1) No: their difference is 9. (2) No: (2,2) is compatible, and (2,2,2,2,2) can continue; increase is not the test. (3) No: each of −1,0,1 remains possible. (4) Yes: reducing 7,3,5 modulo3 gives 1,0,2, respectively. No coordinate may be skipped.

Next dependency: [Lesson 02](lesson-02.md) uses shared reductions to define address closeness.
