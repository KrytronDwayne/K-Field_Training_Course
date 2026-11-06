# Recursive K-Field Geometry and Address Histories

Six lessons, seven core periods, two capstone periods.

Use [course map](course-map.md), [terminology](terminology.md), [teacher guide](teacher-guide.md), [capstone with answers](capstone.md), and [sources](sources.md).

<!-- BEGIN: lesson-01 -->
# Lesson 01 — One subdivision at a time

**Essential question:** How can a rule name every piece without confusing pieces with boundaries?

**Goals:** Generate a binary tree; find parents; distinguish nodes, boundary vertices, and volumes.

**Bridge:** You can compare fractions and plot coordinates. Course 05 introduced cells and Lucas windows; the needed definitions are restated here. **Pacing:** explanation/examples 20, practice 15, checks/feedback 15, transition 5 minutes.

## C06.01-E1 — A repeated rule

A recursion repeats an operation on its output. The starting object is the root at depth zero. A child results from one application; its parent produced it. Depth counts applications. Start with the synthetic interval [0,1). A square bracket includes an endpoint; a round bracket excludes it. Splitting at the midpoint gives [0,1/2) and [1/2,1). Only the right child owns 1/2. Endpoint 1 remains a geometric boundary vertex even though no interval owns it.

At dyadic depth n2, each interval has width 1/2^n2. Index intervals left to right by j=0 through 2^n2−1. Interval j is [j/2^n2,(j+1)/2^n2). Parent k produces children 2k and 2k+1. Conversely parent(j)=floor(j/2), where floor means greatest integer at or below the number. Thus floor(5/2)=2. Here indices are nonnegative.

## C06.01-W1 — Worked tree

| Depth n2 | Indices and intervals | Parent indices |
|---|---|---|
| 0 | 0: [0,1) | none |
| 1 | 0: [0,1/2); 1: [1/2,1) | 0,0 |
| 2 | 0: [0,1/4); 1: [1/4,1/2); 2: [1/2,3/4); 3: [3/4,1) | 0,0,1,1 |

Index 3 is child 2(1)+1 of parent 1. Four widths of 1/4 total 1. Their distinct boundary vertices are 0,1/4,1/2,3/4,1: five, not eight. Eight counts cell–endpoint incidences (pairings), counting shared ends twice.

## C06.01-E2 and C06.01-W2 — Count the object you named

A basis B specifies three independent edge directions and lengths. Outer basis 3B triples each edge. A node is a sampled point; a complete cell volume is a region. In the source Lucas window, each axis has half-step positions −1/2,0,1/2. Independently choosing three coordinates gives 3×3×3=27 nodes. A Lucas Group instead contains three complete Cell3 cells per axis, hence 27 volumes and outer basis 3B.

Draw a row as `|---o---|---o---|---o---|`: three cell centers o, four boundary corners |. The drawing is schematic. A 9B Supergroup has nine complete cells per axis: 9×9×9=729 volumes. Equivalently it has 3×3×3=27 Groups, each with 27 cells. Counts are dimensionless; a measured volume would carry cubic length units.

> **Scope:** S02 /backbone_sequence/2/typed_finite_objects defines the three objects. The interval is synthetic. Finite counting derives totals, not a new physical mechanism. Sampling a boundary point and assigning region ownership are separate operations.

## Guided practice

**C06.01-P1:** Extend the tree to depth 3. List child indices and parents, then trace j=5.

**Answer:** Children 0,1,2,3,4,5,6,7 have parents 0,0,1,1,2,2,3,3. Index 5 is [5/8,6/8); its parents are 2 at depth 2, 1 at depth 1, and 0 at depth 0.

**C06.01-P2:** Count 9B Supergroup volumes by axes and by Groups.

**Answer:** 9^3=729 cells; 3^3 Groups times 27 cells per Group also gives 729.

## Diagnostic checks

1. **C06.01-D1:** At depth 2, are there four cells and eight distinct vertices? What about endpoint 1?
2. **C06.01-D2:** Classify 27 window nodes, 27 Group volumes, and 729 Supergroup volumes. Do the two 27s identify objects?
3. Which depth-2 interval owns 1/2? Which owns 1?
4. Give the parent of depth-3 index 6 and its sibling (the other child).

**Worked answers:** (1) Four cells and five distinct vertices; eight counts incidences. Vertex 1 is an excluded ownership endpoint. (2) Points, complete cells, complete cells. Equal cardinality means equal number only. (3) Index 2 owns 1/2; none owns 1. (4) Parent floor(6/2)=3; sibling 7.

**Next:** [Lesson 02](lesson-02.md) compares this halving rule with ternary addresses.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 02 — Dyadic geometry and triadic addresses

**Essential question:** How can two recursions have matching counts but different rules?

**Goals:** Reduce integers modulo a positive integer; build a residue tree; distinguish depths and solve the source rung equation.

**Bridge:** Lesson 01 taught roots, children and cell counts. This lesson groups integers by remainders. **Pacing:** explanation/examples 20, practice 15, diagnostics/feedback 15, transition 5 minutes.

## C06.02-E1 — Remainders as addresses

For positive integer m, write a=mq+r with integer q and 0≤r<m. The remainder r is the standard representative modulo m. Integers are congruent modulo m when their difference is divisible by m. Thus 7=3×2+1 and −2=3×(−1)+1 both have remainder 1. This does not make −2 and 1 equal integers.

A residue class groups integers with the same remainder. At ternary depth d3=1, modulus 3 gives classes 0,1,2. At depth 2, modulus 9 gives classes 0 through 8. Reducing modulo 3 returns each depth-2 class to its parent:

| Depth 0 (mod 1) | Depth 1 (mod 3) | Depth 2 children (mod 9) |
|---|---|---|
| 0 | 0 | 0,3,6 |
| 0 | 1 | 1,4,7 |
| 0 | 2 | 2,5,8 |

A three-coordinate address independently chooses one class on each axis, so it has (3^d3)^3=27^d3 possibilities. The source notation A_d=(Z/3^d Z)^3 means this set of triples; Z denotes integers and the slash denotes residue classes, not ordinary division. We call its depth d3 to distinguish dyadic depth n2.

## C06.02-W1 — Two counters

Fix an outer geometric Group 3B. At n2=0 there are 3 cells and 4 boundary corners per axis: 27 cells and 64 distinct vertices. At n2=1 there are 6 cells and 7 corners per axis: 216 cells and 343 vertices. Lesson 03 derives the general formula. Separately A_1 has 3^3=27 classes and A_2 has 9^3=729. Increasing n2 halves geometric edges; increasing d3 triples the residue modulus. Equal counts do not equate regions and classes.

## C06.02-E2 and C06.02-W2 — A finite rung equation

The source equation is 3^g_rung×2^n_rung+1=10, with both exponents nonnegative integers. These local rung variables are not automatically n2 or d3. Subtract 1 to obtain a product of 9. If n_rung≥1 the product is even, whereas 9 is odd. Therefore n_rung=0. Then 3^g_rung=9, giving g_rung=2. Powers of 3 strictly increase, so there is only one solution in this domain. This use of odd/even arithmetic is separate from detector parity or carry-sign conventions.

For an exhaustive finite check, g_rung≤2 because 3^3>9; n_rung≤3 because 2^4>9. All 12 products before adding 1 are:

| g_rung / n_rung | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| 0 | 1 | 2 | 4 | 8 |
| 1 | 3 | 6 | 12 | 24 |
| 2 | 9 | 18 | 36 | 72 |

Only (2,0) gives the required 9. The source's outer 9B Supergroup has 729 complete volumes. A_2 also has 729 elements, but those are modular triples.

> **Scope:** S02 /backbone_sequence/2/recursions and /supergroup_uniqueness specify these systems and the rung domain. The finite calculations are verified here. Infinite inverse limits are recognition-only: histories may extend to further depths; no infinite calculation is assessed.

## Guided practice

**C06.02-P1:** Reduce 7 and −2 modulo 3, then reduce (7,5,0) from depth 2 to depth 1. Rebuild the one-coordinate tree and state the three-coordinate counts at depths 0,1,2.

**Answer:** Both first remainders are 1; the triple becomes (1,2,0). The children of r are r,r+3,r+6 for r=0,1,2, exhausting 0 through 8. The three-coordinate counts are 1^3=1,3^3=27,9^3=729 at depths 0,1,2.

**C06.02-P2:** Reproduce the exponent bounds and table. Why is no outside pair needed?

**Answer:** Each factor is at least 1. Exponents g≥3 or n≥4 therefore exceed product 9. In the table only (2,0) works.

## Diagnostic checks

1. **C06.02-D1:** Are 27 Group volumes and 27 ternary classes the same typed object?
2. **C06.02-D2:** State the rung domain and the two meanings of 729.
3. Compute −4 modulo 3 using a division equality.
4. Is the parent of depth-2 residue 7 floor(7/2)?

**Worked answers:** (1) No: regions versus classes. (2) Nonnegative integer exponents; 729 volumes in a Supergroup versus 729 triples in A_2. (3) −4=3(−2)+2, so remainder 2. (4) No: 7 mod 3=1. The floor rule belongs to binary interval indices.

**Next:** [Lesson 03](lesson-03.md) derives scaling and shared-boundary counts.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
# Lesson 03 — Scaling length, area, and node counts

**Essential question:** Which quantity changes when a fixed region is subdivided?

**Goals:** Derive length/area/volume scale factors; count distinct corners; count half-step samples and reachable sheets.

**Bridge:** Lessons 01–02 distinguished regions, vertices and residue classes. Multiplication counts independent coordinate choices. **Pacing:** two 55-minute periods. Period A covers E1/W1/P1/D1,D3; period B covers E2/W2/P2/D2,D4. In each use 20 minutes explanation/examples, 15 practice, 15 checks/feedback, 5 transition. The extra period prevents the sampling-grid argument being rushed.

## C06.03-E1 — Hold the outer boundary fixed

Take a fixed outer Group with basis 3B. At depth n2 each original cell edge has been halved n2 times, giving subcell basis 2^(−n2)B. A negative exponent means reciprocal: 2^(−2)=1/4. There are m=3×2^n2 subcells along each outer edge. Thus m^3=27×8^n2 cells fill the Group. A row of m adjoining cells has m+1 distinct boundary corners. Choosing a corner on each axis yields (m+1)^3=(3×2^n2+1)^3 distinct vertices, including the geometric outer boundary.

To scale every edge by factor s, a line length is multiplied by s. An area is multiplied by s×s=s^2 because both spanning lengths change while their angle stays fixed. A volume is multiplied by s^3 because all three spanning lengths change. This remains true for a slanted parallelepiped: scaling does not change its angles. Therefore one halving divides length by 2, area by 4 and volume by 8. Eight children exactly replace a parent's volume.

## C06.03-W1 — A fixed Group through depth 2

| n2 | Cells per axis | Complete subcells | Distinct corner vertices | Subcell edge factor |
|---|---|---|---|---|
| 0 | 3 | 27 | 64 | 1 |
| 1 | 6 | 216 | 343 | 1/2 |
| 2 | 12 | 1728 | 2197 | 1/4 |

At n2=2, 27×8×8=1728; 13×13×13=2197. Multiplying 216 cells by 8 corners at depth 1 gives 1728 incidences, not 343 distinct vertices. Shared vertices belong geometrically to multiple cell closures, so counting once per incident cell repeats them.

For numerical volume practice use a **classroom analogue, not Cell3 or measured data**. Its edge columns are a=(1,0,0), b=(1,2,0), c=(0,0,−3) arbitrary length units. In the first two coordinates a and b span base area 1×2=2 square units; c has perpendicular height 3. Its positive volume is 6 cubic units (its signed determinant is −6). The fixed Group occupies 27×6=162 cubic units. We do not replace the locked physical Cell3 basis with these toy values.

The source family B_(p,n)=3^p×2^(−n)B describes a scaled basis: p,n are its scale labels. Holding p fixed and varying n changes that basis. It does not say the fixed outer 3B boundary shrinks in our cell-count experiment; distinguish the basis of the object you are naming from its containing region.

## C06.03-E2 and C06.03-W2 — Half-step samples and sheets

Now change the sampling grid, not the outer region. A centered 9B span extends from −9/2 to 9/2 along each basis coordinate. Half-step sampling labels coordinates i/2, with integer i=−9 through 9. An inclusive integer list from −m to m has 2m+1 entries: m negatives, zero, m positives. Thus 19 choices per axis yield 19^3=6859 sample points.

Define lambda=i+j+k for the three integer half-step labels. A sheet is the set of grid points sharing one lambda value. Minimum lambda is −27, maximum 27. All 55 integer values are attained: for target t from 0 to 9 use (t,0,0); for 10 through 18 use (9,t−9,0); for 19 through 27 use (9,9,t−18). Negate coordinates for negative targets. This proves no intermediate sheet is missing. It does not claim equal populations on all sheets.

An ordinary cell-corner grid on the same 9B span has ten corners per axis, hence 1000 corners. The half-step grid includes those boundary corners plus additional samples. Keep four separate counts: 729 volumes, 1000 ordinary corners, 6859 half-step points, 55 sheets.

> **Scope:** S02 /backbone_sequence/2/typed_finite_objects and /recursions supply the grid and source counts. These derivations are finite geometry. Sampling includes boundary points even where half-open ownership assigns them to a neighbor. Lambda here uses half-step integer labels; no force or measured signal is inferred.

## Guided practice

**C06.03-P1:** Derive the cell and distinct corner counts at depth 2 from cells per axis. Then from depth 1 to 2, give subcell length/area/volume factors and verify total volume for the toy Group.

**Answer:** Depth 2 has 3×4=12 cells per axis, so 12^3=1728 cells and 13^3=2197 distinct corners. Factors are 1/2,1/4,1/8. Depth 1: each volume 6/8=3/4, so 216×3/4=162. Depth 2: each volume 6/64=3/32, so 1728×3/32=162. No volume disappeared.

**C06.03-P2:** For a centered 3B span count half-step points, sheet values, volumes and ordinary corners. Produce lambda=8 and −8.

**Answer:** Labels −3 through 3 give 7^3=343 samples; sums −9 through 9 give 19 sheets. There are 3^3=27 volumes and 4^3=64 corners. (3,3,2) and (−3,−3,−2) realize ±8. The same filling argument as W2 realizes every intermediate sum.

## Diagnostic checks

1. **C06.03-D1:** Why is 216×8 not the distinct vertex count at n2=1? Is outer 3B shrinking?
2. **C06.03-D2:** Label 729,1000,6859,55 for the 9B span, including sampling grids.
3. **C06.03-D3:** Relative to depth zero, what are the depth-2 length, area and volume factors?
4. **C06.03-D4:** Exhibit a half-step index triple with lambda=23 and explain why endpoints alone do not prove all sheets exist.

**Worked answers:** (1) It counts incidences with shared corners repeated; outer 3B stays fixed. (2) Complete volumes, ordinary corners, half-step samples, lambda sheets respectively. (3) 1/4,1/16,1/64. (4) (9,9,5); a range could contain gaps, so the constructive filling rule is needed.

**Next:** [Lesson 04](lesson-04.md) encodes signed addresses with powers of three.
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
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
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
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
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
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
<!-- END: lesson-06 -->

