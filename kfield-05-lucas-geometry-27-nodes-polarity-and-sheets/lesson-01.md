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
