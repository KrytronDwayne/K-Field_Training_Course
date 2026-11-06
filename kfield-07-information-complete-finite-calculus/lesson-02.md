# Lesson 02 — The finite product rule

Essential question: How does a product change when both factors change by a finite amount?

Goals: derive the full product difference by expansion; calculate its three signed terms; check an equivalent endpoint formula and product units.

Prerequisite bridge: Lesson 01 taught f_t=f_s+df. Recall distributivity: (a+b)c=ac+bc. To multiply two sums, distribute each term of the first across the second. For example (2+3)(4+2)=8+4+12+6. Products here multiply scalar entries at the same edge endpoint; they are not matrix multiplication.

## C07.02-E1 — Derive before shortening

Use starting values f_s,g_s and ending values f_t,g_t on one common edge. Substitute f_t=f_s+df and g_t=g_s+dg:

    d(fg) = f_t g_t − f_s g_s
          = (f_s+df)(g_s+dg) − f_s g_s
          = f_s g_s + f_s dg + g_s df + df dg − f_s g_s
          = f_s dg + g_s df + df dg.

The first term changes g while holding f at its starting value; the second changes f while holding g at its starting value. The third is the joint finite interaction. It can be positive, negative or zero. Nothing in this exact expansion permits us to erase it because a term is inconvenient or small. If either change is zero, the joint term is exactly zero for that edge.

An equivalent grouping is d(fg)=f_s dg+df g_t. This uses the ending g_t, so df g_t already contains g_s df+df dg. Confusing g_t with g_s loses the interaction. If f has unit U and g has unit V, every term has unit UV. In our examples both signals use SU, so products and product changes use SU². A product change is not a time rate.

## C07.02-W1 — Worked two-channel edge

Let f:2→5 SU and g:4→6 SU. Then df=3 SU and dg=2 SU. The direct product change is 5·6−2·4=30−8=22 SU². Separately, f_s dg=2·2=4, g_s df=4·3=12, df dg=3·2=6, all in SU². Their sum is 22. Omitting the interaction gives 16 and fails the endpoint check. The endpoint grouping gives 2·2+3·6=4+18=22 SU².

> Claim scope: S02#/constitutive_principles/3 names EG-A4 as a constitutive premise about retaining finite interaction. S02#/backbone_sequence/3 gives this scalar expansion. Under our definitions, the equality follows from distributivity; the physical commitment is not derived from B alone. The numbers are synthetic.

## C07.02-P1 — Practice with opposing changes

Let f:3→1 SU and g:2→5 SU. Compute the direct product difference, the three-term rule and the endpoint grouping. Label the interaction's sign and connect it to EG-A4.

Answer: df=−2, dg=3 SU. Directly, 1·5−3·2=−1 SU². The terms are 3·3=9, 2·(−2)=−4 and (−2)·3=−6 SU²; total −1. Endpoint form is 3·3+(−2)·5=9−10=−1. The negative interaction is retained under EG-A4; the expansion is exact algebra.

## Diagnostics

1. **C07.02-D1:** For f:1→1 SU and g:2→4 SU, find all three terms. Why is the interaction zero, and what is EG-A4's logical role?
2. **C07.02-D2:** For f:−1→2 SU and g:3→2 SU, check both sides of the rule.
3. **C07.02-D3:** A student writes f_s dg+df g_s and calls it the endpoint formula. Locate and repair the error. State its units.

Worked answers: D1: df=0,dg=2; terms (2,0,0) SU², product change 2. The zero factor df makes the interaction zero. EG-A4 remains a source constitutive premise. D2: df=3,dg=−1; terms 1,9,−3 sum 7 SU², matching 2·2−(−1)·3=7. D3: replace the final g_s by g_t, or add df dg to the written expression; all product terms have SU².

Next dependency: [Lesson 03](lesson-03.md) separates a signal into two retained parts; Lesson 04 will expand their product in the same way.
