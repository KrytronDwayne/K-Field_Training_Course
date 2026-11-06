# Lesson 05 — Parent maps and compatible histories

**Essential question:** When do records at different resolutions describe one compatible address history?

**Goals:** Apply the modular parent map; test compatibility using differences; identify which digit reduction removes.

**Bridge:** Lesson 04 taught low-to-high signed digits and congruent representatives. Lesson 01's binary parent uses a different operation. **Pacing:** explanation/examples 20, practice 15, diagnostics/feedback 15, transition 5 minutes.

## C06.05-E1 — A history is more than a list

A finite history stores one address at each declared depth. It is compatible when every child returns to the recorded parent under the rule for that type. For ternary addresses, the parent from depth d3+1 to d3 is reduction modulo 3^d3, coordinate by coordinate. This is called the bonding map in S02. A standard representative a and proposed parent b pass the test exactly when a−b is divisible by the parent's modulus. Balanced representatives obey the same test, even when their signs differ.

In a low-to-high digit word, every place above depth d3 has a factor of 3^d3. Such terms have remainder zero modulo 3^d3. Therefore reduction retains the low digits and removes the highest digit. It does not remove the low digit and shift the others. That latter operation divides a suitably adjusted integer by three and answers another question.

## C06.05-W1 — History of 8

| Depth d3 | Modulus | Standard class representative | Balanced word | Balanced integer |
|---|---|---|---|---|
| 3 | 27 | 8 | (−1,0,1) | 8 |
| 2 | 9 | 8 | (−1,0) | −1 |
| 1 | 3 | 2 | (−1) | −1 |

For depth 3 to 2, balanced difference 8−(−1)=9 is divisible by 9. For depth 2 to 1, −1−(−1)=0 is divisible by 3. Using standard representatives instead gives differences 8−8=0 and 8−2=6, also divisible by the required moduli. The two renderings describe the same compatible history. Zero differences are valid information, not missing tests.

Compare binary index 5 at depth 3: its parent is floor(5/2)=2, then 1. A binary child records which half of its parent it occupies. A ternary residue child records additional high-place modular information. The shared word 'parent' does not license swapping their formulas.

> **Scope:** S02 /backbone_sequence/2/recursions/ternary_address/bonding_map is the source rule. These finite histories are classroom arithmetic. Compatibility proves consistency under that rule; it does not select a unique higher-depth continuation from a coarse record.

## Guided practice

**C06.05-P1:** Build the depth 3,2,1 history of integer 5 in standard and balanced representatives. Check both transitions.

**Worked answer:** Standard classes are 5 mod 27, 5 mod 9, 2 mod 3. Balanced words are (−1,−1,1), (−1,−1), (−1), with integers 5,−4,−1. Differences are 5−(−4)=9 and −4−(−1)=−3, divisible by 9 and 3. Standard differences 0 and 3 pass too.

**Additional practice:** Is depth-3 class 8 with depth-2 class 7 compatible? Repair the parent. **Answer:** 8−7=1 is not divisible by 9; the parent must be class 8 mod 9, balanced representative −1.

## Diagnostic checks

1. **C06.05-D1:** Drop epsilon0 from (−1,0,1), then shift the remaining places. What integer results, and is it the parent?
2. Does depth-2 class 5 have depth-1 parent 2? Show the test.
3. What are the three depth-2 children of depth-1 class 2 in standard representatives?
4. A proposed history uses balanced integers 5,−4,+1 at depths 3,2,1. Where does it fail?

**Worked answers:** (1) (0,1) gives 3; that is class 3 mod 9, not class 8. Remove the high digit instead. (2) Yes: 5−2=3 is divisible by 3. (3) 2,5,8. (4) First difference 9 passes; second −4−1=−5 is not divisible by 3. Replace +1 with −1.

**Next:** [Lesson 06](lesson-06.md) retains the detail needed to invert these parent maps.
