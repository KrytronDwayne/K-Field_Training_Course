# Lesson 01 — Symmetry as an operation with a rule

**Essential question:** What must an operation preserve before we call it a symmetry?

**Goals:** Apply and compose tuple rules; identify identity and inverse operations; test closure and two declared invariants.

**Bridge and pacing:** You can substitute numbers into formulas and square signed numbers. An ordered tuple is a list whose positions have names: (2,5) differs from (5,2). No abstract algebra is assumed. One 55-minute period: retrieval 5, explanation/example 20, practice 15, diagnostics/repair 15 minutes.

## C13.01-E1 — Rules before names

A carrier is the collection of objects on which a rule acts. For example, the carrier of ordered real pairs contains (2,5), (-1,0), and pairs with fractions. A transformation assigns one output pair to each input pair. The swap rule R(x,y)=(y,x) uses the same input values in reversed positions. The identity I(x,y)=(x,y) leaves every pair unchanged.

Composition means applying one rule and then another. In FG, apply G first and F second. The result must again be a rule on the same carrier. An inverse undoes a rule on every input. Swapping twice restores the original pair, so R is its own inverse. Closure means that every composition of listed operations is still on the list. Checking one numerical input is useful, but a rule about all pairs needs symbolic substitution: R(R(x,y))=R(y,x)=(x,y).

An invariant is a specified quantity unchanged by the operation. Here the sum x+y and squared norm x²+y² are invariant under swapping. The squared norm is found by squaring each component and adding; it is the square of Euclidean length. These coordinates are dimensionless. Symmetry is always relative to a carrier and structure being preserved; a word or a matching shape alone is insufficient.

A closed set with identity, inverses, and associative composition is called a group. Function composition is associative because either grouping performs the same sequence of rules. We will only need small operation tables, not a general group theory course.

## C13.01-W1 — A fully worked two-operation table

For the pair (2,5), R gives (5,2). Both have sum 7 and squared norm 4+25=29. Compose symbolically to get II=I, IR=R, RI=R, RR=I. The entire table is therefore:

| Left operation after top operation | I | R |
|---|---|---|
| I | I | R |
| R | R | I |

Every entry is I or R, proving closure. I has inverse I; R has inverse R. Preserve the input and rule name if you want to reconstruct the input from a transformed record.

> **Scope:** This is an exact finite mathematical example, not a detector observation. The source's root structure is introduced later; no physical mechanism has been assigned here.

## C13.01-P1 — Try a cycle, then check

On real triples define T(x,y,z)=(z,x,y). Apply T repeatedly to (1,2,3). Complete the composition table for I,T,T² and check the sum and squared norm at each stage. T² means T applied twice, not componentwise squaring.

**Worked practice answer:** The sequence is (1,2,3) → (3,1,2) → (2,3,1) → (1,2,3). For arbitrary symbols the third application also restores (x,y,z), so T³=I. Exponents add under composition. Remove complete groups of three applications: T⁴=T. This is addition modulo 3, meaning equal remainders after division by 3.

| After | I | T | T² |
|---|---|---|---|
| I | I | T | T² |
| T | T | T² | I |
| T² | T² | I | T |

All entries belong to the list. The inverse of T is T², and the inverse of T² is T. Each triple has sum 6 and squared norm 1+4+9=14. More generally, moving the terms of a sum does not change either invariant.

## Diagnostic checks

1. **C13.01-D1:** Is {I,T} closed? Give a counterexample and state the missing information in a claim that merely says “this is a symmetry.”
2. **C13.01-D2:** Apply R twice to (-2,4). Check its sum and squared norm.
3. **C13.01-D3:** What is T⁵? What is its inverse within the three-operation set?
4. **C13.01-D4:** Does the rule H(x,y)=(x+1,y-1) preserve the sum and squared norm on (2,5)? Is preserving one quantity enough to claim all quantities are preserved?

**Worked answers:** 1. TT=T² is missing. State a carrier, rule, composition, and intended invariant. 2. (-2,4) → (4,-2) → (-2,4); sum 2, squared norm 4+16=20. 3. Remove three applications: T⁵=T²; its inverse is T. 4. H(2,5)=(3,4); sum remains 7, but squared norm changes from 29 to 25. A symmetry of the sum need not preserve Euclidean length. This distinction prepares the side transfer.

**Next dependency:** [Lesson 02](lesson-02.md) uses a sum-preserving transfer whose difference changes.
