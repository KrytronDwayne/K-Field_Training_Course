# Lucas Geometry: 27 Nodes, Polarity, and Sheets

A complete short course for high-school seniors: six 55-minute core lessons and two capstone periods. Read lessons in order. Numerical work uses a declared classroom analogue; source definitions and freshly derived finite results are distinguished throughout.

[Course map](course-map.md) · [Terminology](terminology.md) · [Capstone and full answer key](capstone.md) · [Teacher guide](teacher-guide.md) · [Source notes](sources.md) · [Complete worked registry](registry.md)

The following six lessons are assembled verbatim from their separately audited files.

<!-- BEGIN: lesson-01 -->
# Lesson 1 — Enumerating the balanced node window

**Essential question:** How can we list every node exactly once?

**Goals:** Enumerate all 27 addresses in a reproducible order; justify the count by independent choices; classify nodes by their number of nonzero coordinates.

**Prerequisite bridge:** Course 04 supplies coordinate language. Here we need only signed arithmetic and the idea that an ordered triple gives three coordinates. A subscript is a position label: L₁ means the first coordinate, not L multiplied by 1. We rebuild the counting method before using it. Budget: explanation/work 20 minutes, practice 15, checks/feedback 15, transition 5.

## C05.01-E1 — Three choices, three times

An address L=(L₁,L₂,L₃) is an ordered list. Each entry can be −1, 0, or 1. The order matters: (1,0,0) differs from (0,1,0). The notation {−1,0,1}³ means all triples formed by choosing each entry from that three-element set. This is a Cartesian product: combine every first choice with every second choice and every third choice.

For each fixed first entry there are three second entries. Each of those has three third entries, giving 3×3=9 rows. There are three first entries, so there are 3×9=27 rows. Adding 3+3+3 counts entries available in three menus; it does not count complete combinations from those menus.

Use a nested listing: hold the first entry fixed; hold the second fixed; run the third through −1,0,1. Then change the second and repeat. Change the first only when all nine rows in its block are finished. A duplicate would have the same three entries, and therefore the same place in this listing. A missing row would require omitting one of the three choices in some block.

## C05.01-W1 — A complete worked enumeration

Each table cell below is one address. Read across each row, then down each block.

| Fixed L₁ | L₂ | L₃=−1 | L₃=0 | L₃=1 |
|---|---|---|---|---|
|−1|−1|(−1,−1,−1)|(−1,−1,0)|(−1,−1,1)|
|−1|0|(−1,0,−1)|(−1,0,0)|(−1,0,1)|
|−1|1|(−1,1,−1)|(−1,1,0)|(−1,1,1)|
|0|−1|(0,−1,−1)|(0,−1,0)|(0,−1,1)|
|0|0|(0,0,−1)|(0,0,0)|(0,0,1)|
|0|1|(0,1,−1)|(0,1,0)|(0,1,1)|
|1|−1|(1,−1,−1)|(1,−1,0)|(1,−1,1)|
|1|0|(1,0,−1)|(1,0,0)|(1,0,1)|
|1|1|(1,1,−1)|(1,1,0)|(1,1,1)|

The centered window includes its boundary. With zero nonzero coordinates, only (0,0,0) occurs: the center. With one nonzero coordinate choose its position in 3 ways and its sign in 2 ways: 6 face centers. With two nonzero coordinates choose the zero position in 3 ways and the other two signs in 2×2 ways: 12 edge centers. With all three coordinates nonzero choose three signs: 2³=8 vertices. These names describe a cube in address space and its image under an invertible basis map; a skew physical cell need not be a cube.

The count 1+6+12+8=27 agrees with the independent product count. Every row falls into exactly one of these four groups.

## C05.01-P1 — Guided practice, with answer

Cover the table and list the nine rows with L₁=0. Then sort them by number of nonzero entries. Answer: the nine rows are (0,−1,−1),(0,−1,0),(0,−1,1),(0,0,−1),(0,0,0),(0,0,1),(0,1,−1),(0,1,0),(0,1,1). There is one center, four one-nonzero rows and four two-nonzero rows in this slice. For the whole window the counts are 1,6,12,8; restricting a coordinate changes the counts, so a slice is not the full registry.

> **Claim scope:** S02 /backbone_sequence/2/definitions and /typed_finite_objects specify this finite window and its geometric classification. The list and counts above are directly derived from those definitions. These are node addresses, not measured events or 27 complete cell volumes. The source's Lucas Group is a different object: 27 complete cells.

## Diagnostic checks

1. **C05.01-D1:** Why is 3+3+3 wrong, and how does 1+6+12+8 check the correct total?
2. **C05.01-D3:** A list has 27 rows but repeats (0,0,0) and omits (1,0,0). Is the row count enough?
3. **C05.01-D4:** Classify (−1,1,0), (0,0,1), and (1,−1,1).
4. **C05.01-D5:** How many rows have L₁=1 and L₂=−1? Write them.

**Worked answers:** 1. Three independent choices multiply to 27; the mutually exclusive geometric groups sum to 27. 2. No: count distinct triples as well as rows; this list has only 26 distinct triples. 3. Two nonzero entries give an edge center; one gives a face center; three give a vertex. 4. Only L₃ is free: (1,−1,−1),(1,−1,0),(1,−1,1).

**Next dependency:** [Lesson 2](lesson-02.md) turns each address into a position while retaining the address.
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
# Lesson 2 — Node addresses versus physical positions

**Essential question:** How can the same address name a position without being that position?

**Goals:** Evaluate the half-basis map with a declared origin; reverse the classroom map; assign a boundary node to its half-open cell while retaining its centered-window membership.

**Prerequisite bridge:** Lesson 1 supplied L. Fractions let us halve each entry to form q=L/2. We now teach how a basis combines three directed steps. Budget: explanation/work 20 minutes, practice 15, checks/feedback 15, transition 5.

## C05.02-E1 — Address, displacement, position

A vector is an ordered triple used to describe a directed displacement. Add vectors entry by entry; multiply a vector by a number by multiplying each entry. A basis gives three independent step vectors a,b,c. Write B=[a b c] with those vectors as **columns**. The compact expression Bq means q₁a+q₂b+q₃c. It does not require a new kind of arithmetic. Independence here means that a position has one address; the explicit inverse below will check that property for our example.

The source's rule is p(L)=O_K+B L/2. O_K is the declared origin point, q=L/2 is the dimensionless half-address, Bq is displacement from that origin, and p is position. Adding the origin changes position, not displacement. When subtracting a point from another point, the result is a displacement.

All numerical work in this course uses a **classroom analogue, not Cell3 and not measured data**. Let U denote an arbitrary length unit. Take O=(2,−1,4) U and the following table of basis components:

|Component|a|b|c|
|---|---|---|---|
|x|1|1|0|
|y|0|2|0|
|z|0|0|−3|

The entries have unit U; thus a=(1,0,0) U, b=(1,2,0) U, c=(0,0,−3) U. This gives the directly usable rules

pₓ=2+q₁+q₂, pᵧ=−1+2q₂, p_z=4−3q₃,

where position components are numerical values in U. To reverse them, first subtract O and call the components dₓ,dᵧ,d_z. Solve the last two equations first: q₂=dᵧ/2, q₃=−d_z/3. Then q₁=dₓ−dᵧ/2. Finally L=2q. This teaches the inverse operation by ordinary linear equations, rather than assuming matrix inversion.

## C05.02-W1 — Worked map and reverse map

For L=(1,−1,1), q=(1/2,−1/2,1/2). The displacement is (1/2−1/2,2(−1/2),−3(1/2))=(0,−1,−3/2) U. Add O to obtain p=(2,−2,5/2) U. To reverse: d=(0,−1,−3/2), so q₂=−1/2, q₃=1/2, q₁=0−(−1)/2=1/2. Doubling recovers the original L. The forward and reverse answers agree exactly; no rounding is needed.

## C05.02-E2 — A centered window and a cell owner answer different questions

The centered window contains q entries −1/2,0,+1/2. Cell ownership uses half-open intervals: [−1/2,1/2) includes its left endpoint and excludes its right endpoint. A cell indexed by the integer triple z owns q when u=q−z has each component in that interval. For this finite window, −1/2 and 0 have owner component 0; +1/2 has owner component 1. For general q the same rule is z=floor(q+1/2), entry by entry. The floor of a number is the greatest integer no larger than it, so floor(−0.2)=−1.

For q=(1/2,−1/2,1/2), z=(1,0,1), u=(−1/2,−1/2,−1/2). Retain both z and u: q=z+u reconstructs the half-address. This is an ownership operation, not an unspecified nearest-integer rounding convention. No nearest-integer operation is needed in this course.

## C05.02-P1 — Guided practice, with answer

Map L=(0,1,−1) and the center. Reverse the first map and assign its owner. Answer: q=(0,1/2,−1/2); p=(2+1/2,−1+1,4+3/2)=(5/2,0,11/2) U. Subtracting O gives (1/2,1,3/2), so q=(1/2−1/2,1/2,−1/2), as required. Its owner is z=(0,1,0) and u=(0,−1/2,−1/2). At L=0, q=0 and p=O, with z=u=0.

> **Claim scope:** S02 /backbone_sequence/2/definitions gives the node map; /backbone_sequence/1/definitions and /boundary_rule give cell ownership. O abbreviates O_K only in the classroom analogue. Its basis never replaces the source-locked Cell3 basis. The source uses ICRS columns and an intentional negative determinant; our component arithmetic is a separate finite teaching example.

## Diagnostic checks

1. **C05.02-D1:** Map L=(1,0,0); give its cell owner. Does that change its membership in the centered window?
2. **C05.02-D3:** Recover L from p=(2,0,11/2) U.
3. **C05.02-D4:** Why is p=B L incorrect for this node rule?
4. **C05.02-D5:** Compare owners of q=(−1/2,0,0) and (+1/2,0,0), and reconstruct both using z+u.

**Worked answers:** 1. q=(1/2,0,0), p=(5/2,−1,4) U, z=(1,0,0). It remains a window node; it belongs to the positive neighbor cell. 2. d=(0,1,3/2), q=(−1/2,1/2,−1/2), so L=(−1,1,−1). 3. It omits the factor 1/2 and the origin; even the center would be misplaced. 4. Owners are (0,0,0) and (1,0,0), respectively. Both have u=(−1/2,0,0); keeping the owner distinguishes them and reconstructs both.

**Next dependency:** [Lesson 3](lesson-03.md) groups these physical points into sheets using their original integer addresses.
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
# Lesson 3 — Lambda sheets and population counts

**Essential question:** Why do 27 nodes occupy seven sheet levels?

**Goals:** Compute an integer sheet label; enumerate and reconcile seven populations; verify the affine sheet identity with its origin subtraction.

**Prerequisite bridge:** Lesson 2 taught p−O and the half-address q. We only need signed addition to label sheets; we introduce a dot product before using it to check a physical plane. Budget: explanation/work 20 minutes, practice 15, checks/feedback 15, transition 5.

## C05.03-E1 — Equal sums define a sheet

Define λ(L)=L₁+L₂+L₃, pronounced lambda. Each entry lies between −1 and 1, so λ is an integer between −3 and 3. A sheet groups all window nodes having the same λ. The full plane containing that group extends beyond the finite nodes; its population here counts only nodes in the window.

To count carefully, list the ways to achieve each sum. A permutation is a rearrangement of entries. Repeated entries give fewer different rearrangements: (1,1,0) has only three, since swapping the two 1s changes nothing. Negation changes every sign. It carries a node with sum λ to a node with sum −λ and has an inverse, namely negation again. Thus opposite sheet populations must match.

## C05.03-W1 — Worked seven-sheet count

|λ|How the rows are obtained|Population|
|---|---|---|
|−3|(−1,−1,−1)|1|
|−2|three rearrangements of (−1,−1,0)|3|
|−1|three of (−1,0,0), three of (−1,−1,1)|6|
|0|center and six rearrangements of (1,0,−1)|7|
|1|three of (1,0,0), three of (1,1,−1)|6|
|2|three rearrangements of (1,1,0)|3|
|3|(1,1,1)|1|

For λ=0 the complete list is (0,0,0),(1,0,−1),(1,−1,0),(0,1,−1),(0,−1,1),(−1,1,0),(−1,0,1). The six noncentral rows have three distinct entries, so choose the 1's position in 3 ways and the −1's position in 2 remaining ways: 3×2=6. The sum 1+3+6+7+6+3+1=27 accounts for every row.

## C05.03-E2 — Checking the physical sheet

The dot product g·d multiplies corresponding components and adds: gₓdₓ+gᵧdᵧ+g_zd_z. If g has unit 1/U and d has unit U, the result is dimensionless. For the classroom basis choose g_λ=(1,0,−1/3)/U. Its dot product with each basis column is 1: with a it is 1; with b it is 1+0=1; with c it is (−1/3)(−3)=1. Consequently, for d=q₁a+q₂b+q₃c,

g_λ·(p−O)=q₁+q₂+q₃=λ/2.

The same linear expression having a fixed value describes a plane: changing a point while keeping that expression fixed keeps it in the same plane. In source notation g_λ=B⁻ᵀ(1,1,1)ᵀ is the vector whose dot product with each basis column is 1. The superscript is recognition-only here; students can verify the three dot products without calculating an inverse transpose.

For W1's physical check use L=(1,−1,1), p−O=(0,−1,−3/2) U. Then g_λ·(p−O)=0+0+(−1/3)(−3/2)=1/2=λ/2. Using p itself would give 2−(5/2)/3=7/6, which is not 1/2. The omitted origin term is g_λ·O=2−4/3=2/3; indeed 7/6−2/3=1/2.

## C05.03-P1 — Guided practice, with answer

List λ=2 and λ=1, then verify the physical identity for (0,1,−1). Answer: λ=2 consists of (1,1,0),(1,0,1),(0,1,1). λ=1 consists of (1,0,0),(0,1,0),(0,0,1),(1,1,−1),(1,−1,1),(−1,1,1). For (0,1,−1), p−O=(1/2,1,3/2) U, so g_λ·(p−O)=1/2−1/2=0=λ/2. Two different points can therefore share one sheet label.

> **Claim scope:** S02 /backbone_sequence/2/sheet_populations reports the seven populations; explicit enumeration independently verifies them. Its /proof/0 prints an identity without origin subtraction. Approved amendment SA-05 restores the affine expression g_λ·(p−O_K)=λ/2, consistent with the source node definition. This course uses that correction throughout. No sheet count is being interpreted as an observed particle population or mechanism.

## Diagnostic checks

1. **C05.03-D1:** Verify total 27, explain mirrored populations, and check g_λ·(p−O)=λ/2 for L=(1,−1,1).
2. **C05.03-D3:** Can λ=4 occur? Can two different addresses have λ=0?
3. **C05.03-D4:** A student says λ=0 has six nodes. What was omitted?
4. **C05.03-D5:** Check λ and the physical identity for L=(1,1,0).

**Worked answers:** 1. The table sums to 27; negation is a reversible pairing of opposite sheets; the dot product is 1/2 as worked above. 2. No, three entries at most 1 sum to at most 3. Yes: the center and (1,0,−1) both have sum zero. 3. The center, which adds one to the six rearrangements. 4. λ=2; q=(1/2,1/2,0), p−O=(1,1,0) U, and the dot product is 1=2/2.

**Next dependency:** [Lesson 4](lesson-04.md) derives two different class labels from λ without replacing λ.
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
# Lesson 4 — Parity and directed signs

**Essential question:** Which information survives when a sheet number becomes a class label?

**Goals:** Compute node polarity for positive and negative sheet numbers; compute remainder classes modulo 3; distinguish both labels from directed orientation and reconcile their populations.

**Prerequisite bridge:** Lesson 3 supplied the integer λ and its seven populations. We now group those integers in two ways. Budget: explanation/work 20 minutes (10 parity, 10 remainder), practice 15 (7 parity, 8 remainder), checks/feedback 15, transition 5.

## C05.04-E1 — Even and odd include negative integers

An integer is even when it equals 2k for some integer k. It is odd when it equals 2k+1. Thus −2=2(−1) is even and −3=2(−2)+1 is odd. Define the node polarity χ(L)=(-1)^λ, pronounced chi. Operationally χ is +1 for even λ and −1 for odd λ. For nonnegative powers, pairs of factors (−1)(−1) multiply to +1. Negative powers are reciprocals: (−1)⁻³=1/(−1)³=−1, giving the same even/odd rule. Zero is even and (−1)⁰=1.

Negating L changes λ to −λ. If λ=2k, then −λ=2(−k) remains even. If λ is odd, its negative remains odd. Therefore χ(−L)=χ(L), even though p(−L)−O=−(p(L)−O). A number giving even/odd class cannot tell us which direction a displacement points.

## C05.04-W1 — Worked polarity

For L=(1,−1,1), λ=1−1+1=1, odd, so χ=−1. For L=(1,1,0), λ=2, even, so χ=+1. Their negatives have sums −1 and −2 and retain those respective χ values. A negative λ does not automatically mean negative χ.

## C05.04-P1 — Guided polarity practice, with answer

Find χ for (−1,−1,−1) and the center, then count both polarities from the seven sheets. Answer: sums −3 and 0 give −1 and +1. Even sheets −2,0,2 contain 3+7+3=13 nodes. Odd sheets −3,−1,1,3 contain 1+6+6+1=14. Keep all 27 rows; these totals are an additional summary.

## C05.04-E2 — Remainders modulo 3

The notation r₃=λ mod 3 means the unique remainder in {0,1,2} when λ=3k+r₃ with integer k. For negative λ, choose k so the remainder is nonnegative and less than 3. This groups integers three steps apart; parity instead groups integers two steps apart. Do not give these fields the same column name.

## C05.04-W2 — Worked distinction

At λ=−2, write −2=3(−1)+1, so r₃=1 and χ=+1. At λ=1, write 1=3(0)+1, so r₃=1 but χ=−1. The shared remainder has not preserved parity. Conversely λ=0 and λ=2 both have χ=+1 but have remainders 0 and 2, so polarity does not preserve remainder either.

## C05.04-P2 — Guided remainder practice, with answer

Find r₃ and χ at −1 and 2. Then group the seven populations by r₃. Answer: −1=3(−1)+2, giving r₃=2, χ=−1; 2=3(0)+2 gives r₃=2, χ=+1. The full accounting is:

|r₃|Sheets contributing|Population|
|---|---|---|
|0|−3,0,3|1+7+1=9|
|1|−2,1|3+6=9|
|2|−1,2|6+3=9|

These equal populations describe the same 27 nodes whose seven-sheet populations are unequal and whose polarity populations are 13 and 14. A different grouping answers a different question.

> **Claim scope:** χ is the node-polarity definition in S02 /backbone_sequence/2/definitions/2. The remainder counts are our finite derivation. χ, r₃, directed vector signs, and the orientation sign introduced next are separate fields. Detector parity, A1 carry parity, chirality, family labels, and primitive lifts are other source concepts, not synonyms for χ. Their calculations are outside this course. No complex phase formula is required; any such extension would also require the same affine origin convention.

## Diagnostic checks

1. **C05.04-D1:** Compare λ, χ and displacement for L=(1,−1,1) and −L. Can χ recover orientation?
2. **C05.04-D2:** Reconcile populations 9,9,9 with 13,14. Does either label determine L?
3. **C05.04-D3:** A learner reports −2 mod 3=−2. Repair the result and show λ=3k+r₃.
4. **C05.04-D4:** Compute λ,r₃,χ for (0,−1,0) and (1,1,1).

**Worked answers:** 1. λ changes from 1 to −1; χ stays −1; displacement reverses from (0,−1,−3/2) to (0,1,3/2) U. χ cannot choose a direction. 2. Remainders partition by steps of three, polarity by steps of two; both totals are 27. Neither label identifies a triple: (1,0,0) and (0,1,0) share both labels. 3. −2=3(−1)+1, so the allowed remainder is 1. 4. The first has λ=−1,r₃=2,χ=−1; the second λ=3,r₃=0,χ=−1.

**Next dependency:** [Lesson 5](lesson-05.md) explicitly stores the direction that polarity cannot recover.
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
# Lesson 5 — Antipodal pairs and observation rules

**Essential question:** How can we group opposite nodes without losing their directions?

**Goals:** Construct 13 noncentral antipodal pairs; choose a unique representative and store its orientation sign; reconstruct addresses and positions and distinguish even from direction-sensitive observations.

**Prerequisite bridge:** Lessons 2 and 4 established that negating L reverses displacement but preserves χ. We now turn that relation into a reversible registry representation. Budget: explanation/work 20 minutes, practice 15, checks/feedback 15, transition 5.

## C05.05-E1 — Pairing and choosing a representative

Two nonzero addresses are in the same antipodal pair when one equals the other or its negative. This grouping is an equivalence relation: every address is related to itself; if L is related to M, M is related to L; and following two sign changes still gives either L or −L. An equivalence class is the set grouped together; here it is {L,−L}. Calling the collection a quotient means treating each pair as one object for a chosen purpose.

A nonzero triple cannot equal its negative: L=−L would give 2L=0 entry by entry and hence L=0. Thus the 26 noncentral nodes divide into 26/2=13 two-member classes. The center is one separate singleton. If we include it, the quotient has 14 classes, not 13.

Choose the canonical representative v as the member whose **first nonzero entry is positive**, reading coordinates left to right. Store orientation s=+1 when L=v and s=−1 when L=−v. Then L=s v. At the center store v=(0,0,0), s=not applicable; do not manufacture two central orientations. A single deterministic representative rule makes independent registries comparable.

## C05.05-W1 — Worked quotient and reconstruction

For L=(−1,0,1), the first nonzero entry is negative. Negate all entries to obtain v=(1,0,−1); s=−1. Multiplication s v=(−1,0,1) reconstructs L. The classroom point is q=(−1/2,0,1/2), p=(3/2,−1,5/2) U. Its opposite has p=(5/2,−1,11/2) U. The sum is (4,−2,8) U=2O, so the midpoint is O. Opposite means opposite about the declared origin, not necessarily about coordinate zero.

For any noncentral pair, p(sv)=O+s Bv/2. Summing the + and − versions cancels the displacements. Retaining v and s therefore retains every address and position once O and B are declared.

## C05.05-E2 — What an observation can retain

An antipodally even function is one whose value is unchanged under L→−L. For example χ and λ² are even: (−λ)²=λ². A directed sheet reading λ is odd: its sign reverses. A pair-only record can carry an even value without ambiguity. For a directed reading it must retain the member sign or both signed readings. Even a zero sheet label does not mean the point is the center: (1,0,−1) is noncentral with λ=0.

These are rules for representing information. If a measurement procedure is direction-sensitive, grouping alone cannot justify discarding its signed observations. Retain the original observations alongside any paired summary and any unresolved difference.

## C05.05-P1 — Guided practice, with answer

Represent L=(0,−1,−1), reconstruct it and its partner, and check their physical midpoint. Answer: v=(0,1,1), s=−1. The two labels are −v=(0,−1,−1) and +v=(0,1,1). Their half-addresses give p(−v)=(3/2,−2,11/2) U and p(v)=(5/2,0,5/2) U. Their sum is (4,−2,8) U, so their midpoint is (2,−1,4) U. Both have χ=+1 because λ=−2 and 2 are even, but their s values differ.

## C05.05-P2 — Pair inventory practice, with answer

List representatives by the position of their first nonzero entry. Answer: nine have first entry 1 and any two entries after it; three have first entry 0, second 1, and any last entry; one is (0,0,1). The list is (1,−1,−1),(1,−1,0),(1,−1,1),(1,0,−1),(1,0,0),(1,0,1),(1,1,−1),(1,1,0),(1,1,1),(0,1,−1),(0,1,0),(0,1,1),(0,0,1). The count 9+3+1=13 independently checks 26/2.

> **Claim scope:** The finite pairing result follows from the source-defined window. The canonical representative convention is an authored storage convention. It is not a claim about physical detector response. Source-reported projective signs and node polarity remain separately typed.

## Diagnostic checks

1. **C05.05-D1:** Why can a pair label alone not recover directed L, and how is the center handled?
2. **C05.05-D3:** Find v and s for (0,0,−1), then reconstruct it.
3. **C05.05-D4:** Which can be stored as one unambiguous pair value: χ, λ, λ²? Explain.
4. **C05.05-D5:** Does λ=0 identify the singleton? How many pair classes including the singleton exist?

**Worked answers:** 1. Both members have the same pair label; retaining s selects one. The center is stored once with no orientation sign. 2. v=(0,0,1), s=−1, so sv=(0,0,−1). 3. χ and λ² are even. λ generally differs between members and needs orientation; the special λ=0 pairs do not fix that general loss. 4. No: six noncentral λ=0 nodes form three pairs. There are 13 noncentral classes plus one singleton, or 14 classes.

**Next dependency:** [Lesson 6](lesson-06.md) combines these fields into a complete, checkable registry.
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
# Lesson 6 — A complete finite registry

**Essential question:** What makes a 27-row registry complete and recoverable?

**Goals:** Construct every field of a node record; apply independent count and reconstruction checks; preserve discrepancies as explicit coordinates.

**Prerequisite bridge:** Lessons 1–5 supplied every arithmetic operation. We now combine them in an ordered workflow and check by a different route. Budget: explanation/work 20 minutes, practice 15, checks/feedback 15, transition 5. The full 27-row construction is completed in the two-period capstone; here students build and check representative rows.

## C05.06-E1 — A row is a record, not a total

Use the classroom O=(2,−1,4) U and basis columns a=(1,0,0), b=(1,2,0), c=(0,0,−3) U. Declare this geometry once for the registry. Keep a row ID and the following fields for each node:

|Field|Meaning and construction|
|---|---|
|L|Original signed triple; unique row identity|
|q|Dimensionless L/2|
|p|O+Bq, in U|
|λ|Integer sum of L entries|
|χ|+1 for even λ; −1 for odd λ|
|r₃|Remainder 0,1,2 in λ=3k+r₃|
|v,s|Canonical representative and member orientation; center has s=N/A|
|z,u|Cell owner and owned-cell residual q−z; both dimensionless|
|R_L|Reconstructed address minus stored L, three dimensionless components|

The residual u is not an error. It is the position within the owned cell and is essential to reconstruct q=z+u. R_L is a separate closure discrepancy: a difference produced by checking the map. Never merge these two meanings of residual. In an exact correct registry R_L=(0,0,0); keep that result per row. If a row fails, keep its original fields, record the discrepancy, and make a separately documented correction. Do not delete it to improve a summary.

Build in this order: enumerate L; halve it; calculate position; compute sum and class labels; assign representative and orientation; assign owner and within-cell residual; finally recompute L from position. A total of 27 does not establish that the 27 intended rows are present. Compare the set of distinct triples with the full nested enumeration.

## C05.06-E2 — Independent checks

Reverse the position with d=p−O, q₁=dₓ−dᵧ/2, q₂=dᵧ/2, q₃=−d_z/3, then double q to obtain L_recovered. Subtract the stored L entry by entry to get R_L. Also compare q with z+u. For a noncentral row compare L with s v. These checks attack different ways a row could be wrong.

Count the seven λ labels, the two χ labels and the three r₃ labels independently. Confirm 26 noncentral rows, each of 13 representatives occurring twice with signs −1,+1, plus exactly one center. For each pair check the sum of positions equals 2O. Counts alone can conceal a wrong position; inverse mapping can pass on a duplicated row. Both kinds of check are necessary.

## C05.06-W1 — Worked complete row

For L=(1,−1,1), q=(1/2,−1/2,1/2), p=(2,−2,5/2) U, λ=1, χ=−1, r₃=1. Its first nonzero entry is positive, so v=(1,−1,1), s=+1. The owner z=(1,0,1), and u=(−1/2,−1/2,−1/2). Adding z+u recovers q. Reverse p: d=(0,−1,−3/2) gives q=(1/2,−1/2,1/2), so L_recovered=(1,−1,1) and R_L=(0,0,0).

## C05.06-P1 — Guided practice, with answer

Complete the row for (−1,1,−1) and compare it with W1. Answer: q=(−1/2,1/2,−1/2), p=(2,0,11/2) U; λ=−1, χ=−1, r₃=2. The representative is again (1,−1,1), but s=−1. Owner z=(0,1,0), residual u=(−1/2,−1/2,−1/2). Inverting p gives q₁=0−1/2=−1/2, q₂=1/2, q₃=−(3/2)/3=−1/2. Thus R_L=0. The two p values sum to (4,−2,8) U. The equal u values do not make these the same node because their z values differ.

## C05.06-P2 — Finding a retained discrepancy

Suppose the W1 row keeps L=(1,−1,1) but stores p=(2,−2,3) U. Compute R_L before correcting it. Answer: d=(0,−1,−1) gives q=(1/2,−1/2,1/3); L_recovered=(1,−1,2/3). Therefore R_L=(0,0,−1/3). Retain that discrepancy and original stored p in a correction note; the forward rule gives corrected p_z=5/2. A record of this repair preserves what changed and why.

> **Claim scope:** This registry is a synthetic exact-arithmetic demonstration of source-defined finite operations. It is not a measurement dataset. Source definitions, derived counts, storage conventions, and synthetic discrepancies have separate roles. Nothing is averaged away or excluded.

## Diagnostic checks

1. **C05.06-D1:** State the distinct-address, sheet, pair and inverse checks required for completion.
2. **C05.06-D3:** Why do correct sheet counts not guarantee correct physical positions?
3. **C05.06-D4:** A registry stores v and χ but omits s. Can it reconstruct all L?
4. **C05.06-D5:** Distinguish u from R_L. Which can legitimately be nonzero in a correct registry?

**Worked answers:** 1. Exactly the 27 allowed distinct triples; sheets 1,3,6,7,6,3,1; 13 two-member noncentral pairs and one center; inverse map returns every L with R_L=0. Also reconcile χ counts 13,14 and r₃ counts 9,9,9. 2. λ uses L only; changing p leaves λ counts unchanged but fails the inverse check. 3. No: antipodes have equal χ; s must select the member. 4. u records within-cell position and is often nonzero; R_L records inverse closure and is zero for this exact example. Both are retained.

**Next dependency:** [Capstone](capstone.md) constructs the complete registry. [The full worked registry](registry.md) is the answer reference, to be opened after attempting the construction.
<!-- END: lesson-06 -->
