# Lesson 06 — What a finite resolution retains

**Essential question:** What must a coarse record preserve to recover its original fine address?

**Goals:** Construct coarse-plus-detail records; reconstruct binary indices and ternary words; explain exactly what information omission loses.

**Bridge:** Lesson 05 checked parent maps. A parent map can send several children to one parent, so reversing it needs additional coordinates. **Pacing:** explanation/examples 20, practice 15, diagnostics/feedback 15, transition 5 minutes.

## C06.06-E1 — Keep the removed coordinate

A map is invertible on a set of records when each output determines its original input. The binary parent k=floor(j/2) alone is not invertible: both 2k and 2k+1 have parent k. Retain the child bit b=j−2k, either 0 or 1. Then j=2k+b reconstructs the index. The bit is residual information relative to the coarse parent description. Zero is as necessary a recorded value as one.

For a ternary balanced word with d3 digits, write r for the integer represented by the low d3−1 digits and e for the removed high digit. Then t=r+3^(d3−1)e reconstructs the balanced integer and appending e reconstructs the exact word. Here e is −1,0,+1, not a binary bit. Specify that r is balanced: mixing a standard remainder with a balanced high digit would use the wrong reconstruction convention.

A complete record includes rule type, original depth, coordinate order, coarse value or word, removed detail, and reconstruction rule. For a coordinate triple, apply the relevant operation to each coordinate and retain all three details. Repeating a coarse operation requires retaining the details at every step. These are exact finite addresses; no infinite tail is inferred.

## C06.06-W1 — Two reconstructions

For binary depth-3 index j=5, k=floor(5/2)=2 and b=5−4=1. Store (type=binary interval, child depth=3, parent index=2, bit=1). Decode j=2×2+1=5; its interval is [5/8,6/8). If reducing again, parent 2 has parent 1 and bit 0; parent 1 has parent 0 and bit 1. Retaining bits from root outward as (1,0,1) reconstructs 0→1→2→5. This root-outward bit order differs from our low-to-high ternary digit order and must be named.

For ternary depth-3 word (−1,0,1), retain low-depth word (−1,0), integer r=−1, and high digit e=+1. Restore 8=−1+9×1 and append the high digit to recover (−1,0,1). Reduce r once more: low digit −1 and removed digit 0. Retaining the zero yields r=−1+3×0. The complete detail record recovers every digit, not merely a scalar score.

> **Scope:** This is finite arithmetic built on S02's separate recursion rules and the course's explicit encoding convention. It demonstrates lossless records, not a proposed force or an empirical measurement. Removed detail remains a primary coordinate; no residual is discarded because its value is small or zero.

## Guided practice

**C06.06-P1:** Make and invert a record for binary j=6 at depth 3 and ternary integer 5 with three balanced digits. Then reduce each one more step, preserving detail.

**Worked answer:** Binary k=3,b=0 gives 6=2×3+0. Next k=3 has parent 1 and bit 1; from 1 recover 3 then 6 using bits 1,0. Ternary word (−1,−1,1) has r=−4,e=1, so 5=−4+9. The low word reduces to −1 with removed digit −1, so −4=−1+3(−1). Both high details are needed for the full three-digit word.

**Additional practice:** Show two different children of the same coarse record. **Answer:** Binary parent 2 has children 4 and 5. Ternary balanced parent −1 at depth 2 has depth-3 children −10,−1,8, corresponding to high digits −1,0,+1. All reduce to class 8 modulo 9.

## Diagnostic checks

1. **C06.06-D1:** Is storing only the parent enough? List required metadata and detail.
2. A binary record has k=3,b=0 at child depth 3. Recover index and interval.
3. A ternary record has balanced r=−4,e=0 at child depth 3. Recover integer and word.
4. What goes wrong if the record for 8 uses standard remainder r=8 and the same e=1 in t=r+9e?

**Worked answers:** (1) No: keep rule type, original depth, coordinate/digit order, coarse fields, all bits/digits including zeros, and reconstruction rule. (2) j=6, interval [6/8,7/8). (3) t=−4; word (−1,−1,0), with three retained digits. (4) It incorrectly gives 17. The formula used r=−1 as the balanced low representative; changing representation requires changing the associated detail convention.

**Next:** [Capstone](capstone.md) combines both trees, counts and complete recovery records.
