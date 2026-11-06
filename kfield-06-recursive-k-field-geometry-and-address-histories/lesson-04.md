# Lesson 04 — Balanced ternary as an address language

**Essential question:** How can negative digits encode an address exactly?

**Goals:** Decode signed digits; encode finite integers; distinguish an integer representative from its residue class.

**Bridge:** Lesson 02 introduced powers-of-three moduli and congruence. Lesson 03 showed why a label needs its grid and depth. **Pacing:** explanation/examples 20, practice 15, checks/feedback 15, transition 5 minutes.

## C06.04-E1 — Place values with signs

In decimal notation, each digit multiplies a place value. Balanced ternary uses place values 1,3,9,27,... and digits −1,0,+1. We always store digits **least significant first**: (epsilon0,epsilon1,epsilon2) means epsilon0×1+epsilon1×3+epsilon2×9. Epsilon is simply the name of a signed digit, not a measured error. Store the depth d3 as the number of retained digits; a zero high digit is still a retained coordinate.

To encode an integer t, choose its low digit by the remainder modulo 3: remainder 0 gives digit 0; remainder 1 gives +1; remainder 2 gives −1 because −1 is congruent to 2. Subtract that digit and divide by 3. The result is an integer, to be encoded at the next place. Repeat until the requested depth. A nonzero leftover after that depth means the exact integer needs more digits; do not silently discard it.

Three digits cover integers from −13 to 13: the largest is 1+3+9=13 and the smallest its negative. At depth 2 the balanced range is −4 through 4. Balanced representatives can therefore be negative even when the standard remainder is nonnegative.

## C06.04-W1 — Integer 8

8 has remainder 2, so choose epsilon0=−1. Then (8−(−1))/3=3. The next remainder is 0, so epsilon1=0 and the next quotient is 1. Choose epsilon2=1 and obtain final quotient 0. The depth-3 word (−1,0,1) decodes to −1+0+9=8.

As a class modulo 27 it is class 8. Reduce to depth 2, modulo 9: it is still standard class 8. But the low two signed digits (−1,0) decode to −1. These representatives are congruent because 8−(−1)=9. Removing the highest digit changed the integer by 9 while preserving its class modulo 9. It did not turn 8 into −1 as an equality of integers.

> **Scope:** S02 /backbone_sequence/2/recursions/ternary_address defines finite residue classes and reduction. Balanced signed-digit words are the course's explicit finite representation of those classes. Encoding examples are exact classroom arithmetic, not experimental evidence. No infinite address is reconstructed from a finite word.

## Guided practice

**C06.04-P1:** Encode integer 5 with three digits. Show the two-digit balanced representative and the one-digit class.

**Worked answer:** Remainder 2 gives −1; (5+1)/3=2. Again remainder 2 gives −1; (2+1)/3=1. The final digit is +1 and quotient 0. Thus (−1,−1,1) gives −1−3+9=5. Two low digits give −4, congruent to 5 modulo 9 because their difference is 9. One low digit gives −1, congruent to standard remainder 2 modulo 3. Depth and order are part of the answer.

**Additional practice:** Encode −2 in two digits. **Answer:** Low digit +1 because −2=3(−1)+1; remaining quotient −1 gives high digit −1. Word (1,−1) gives 1−3=−2.

## Diagnostic checks

1. **C06.04-D1:** Why does depth-2 class 8 not determine the original integer 8 at depth 3?
2. Decode (1,0,−1), least significant first, at depth 3.
3. Are (1) at depth 1 and (1,0) at depth 2 identical records?
4. Can integer 14 be stored exactly in three balanced digits with zero leftover?

**Worked answers:** (1) Integers −1,8 and −10 all reduce to standard class 8 modulo 9. High detail was lost. (2) 1+0−9=−8. (3) Both decode to 1 but have different moduli/depths; the zero is retained. (4) No: largest three-digit sum is 13. The algorithm leaves a nonzero quotient, requiring another digit.

**Next:** [Lesson 05](lesson-05.md) checks whether records at successive depths form a compatible history.
