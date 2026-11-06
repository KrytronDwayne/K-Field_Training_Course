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
