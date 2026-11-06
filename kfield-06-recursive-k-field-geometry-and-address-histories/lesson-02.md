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
