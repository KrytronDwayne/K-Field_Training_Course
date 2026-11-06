# Lesson 5 — Events and interpolation

**Essential question:** What does a pair of signed samples actually tell us about the events between them?

**Goals:** Locate a zero on a linear segment; distinguish transverse passage, contact and discontinuity; preserve brackets, multiple roots and gaps.

**Time:** Three 55-minute periods, each retrieval 5, teaching/example 20, practice 15, checks/repair 15. Period 1: linear interpolation and P1a. Period 2: multiple roots and contacts, P1b and P2. Period 3: discontinuities, gaps, uncertainty, P1c and diagnostics.

**Prerequisite bridge:** From Lesson 1, an event on sheet k satisfies s_k=0. We now call the selected sheet's signed distance s(t) to keep notation short. A **root** is a time where that value equals zero. A **bracket** [a,b] records both endpoint times, values and the rule trusted between them.

## C25.05-E1 — Continuity is part of the input

A continuous path changes without a jump. If s(a)<0 and s(b)>0, continuity guarantees at least one root between a and b: the value cannot get from negative to positive while skipping zero. This statement guarantees existence, not uniqueness. It needs continuity on the whole interval. A straight line with nonzero slope is a special case that crosses zero exactly once.

For a declared linear segment, change per second is (s_b−s_a)/(b−a). At time t the distance is s_a+(s_b−s_a)(t−a)/(b−a). Set that expression to zero and solve:

`t*=a − s_a(b−a)/(s_b−s_a)`.

The numerator has units m·s and denominator m, giving seconds. If endpoint values are equal, this division fails: equal nonzero values define a constant nonzero linear segment with no root; two zero values define continuous occupancy under the linear rule. Neither case is an isolated crossing.

## C25.05-W1 — Worked brackets and hidden roots

Let a=0 s, b=2 s, s_a=−2/5 m, s_b=6/5 m, and explicitly assume a linear segment. Difference is 8/5 m. Thus t*=0−(−2/5)(2)/(8/5)=1/2 s. Recheck using slope (8/5)/2=4/5 m/s: −2/5+(4/5)(1/2)=0 m. Save the original [0,2] s bracket and both endpoints alongside the exact model root.

Now use a different path s(t)=(1 m)(τ−1)(τ−2), where τ=t/(1 s) is numerical time in seconds. Multiplication gives zero whenever either factor is zero, so roots are 1 and 2 s. At 0 and 3 s, s=2 m in both cases. Equal endpoint signs did not imply absence. At 1/2 s s=3/4 m; at 3/2 s s=−1/4 m; at 5/2 s s=3/4 m. Hence the first passage is positive-to-negative and the second negative-to-positive.

## C25.05-P1 — Three practice cases

**a.** A linear path has s(1 s)=−1 m and s(3 s)=3 m. Locate the root and verify it.

**b.** For s(t)=(1 m)(τ−1)², classify the zero at 1 s using nearby values.

**c.** Let s=−1 m for t<1 s and +1 m for t≥1 s. Do opposite signs at 0 and 2 s guarantee a zero?

**Worked answers:** (a) t*=1−(−1)(2)/4=3/2 s. Slope is 2 m/s; s(3/2)=−1+2(1/2)=0 m. (b) Squaring gives nonnegative values, with s=0 only at 1 s. Both 1/2 and 3/2 s give 1/4 m. This is a tangent contact: it touches and returns to the same side. Its instantaneous rate is zero; no calculus is needed to classify the equal-side pattern. (c) No: the path jumps and never takes the value zero. Save a discontinuity row, not an interpolated passage.

## Refinement, uncertainty and unresolved intervals

When a continuous path is known but not linear, halve a sign-changing bracket and evaluate the midpoint. Keep a smaller sign-changing bracket while preserving all earlier evaluations. This procedure is called bisection. A midpoint zero is an exact evaluated root; otherwise a finite bracket locates a root without pretending to know the exact time. It does not prove no other roots exist.

**C25.05-P2:** Let s(t)=(1 m)(τ²−2). Starting with [1,2] s, evaluate 1.5 s, then 1.25 s. **Answer:** Endpoint values are −1 and +2 m. At 1.5 s the value is +0.25 m, giving [1,1.5] s. At 1.25 s it is −0.4375 m, giving [1.25,1.5] s. All five values remain available. This is localization, not a claim of a measured timing uncertainty. A continuous increasing positive-time square has just one root here, but the generic sign-change rule alone does not give uniqueness.

If values inside (1,2) s are unavailable, retain a gap row with all known endpoints and any independent continuity information. Without a path model, do not draw a line through the missing interval and report its root as exact. If continuity is independently assured and opposite endpoints are known, existence is justified but root count and times remain unresolved. If continuity is unknown, even existence is unresolved. A failed midpoint evaluation leaves the previous bracket valid under its previous assumptions; store the failed attempt.

For measurement uncertainty, retain original values and their supplied bounds separately. A bound spanning zero cannot certify the sample's sign. For example a reported −0.02 m with bound ±0.05 m permits [−0.07,0.03] m. Do not choose the preferred sign. If no bounds were supplied, write “not supplied”; synthetic exact arithmetic is not evidence of zero instrument uncertainty.

> **Claim scope:** Existence follows mathematically from continuity and signs. Linear interpolation is exact within a stated linear model; for samples of an unspecified curve it is only a model estimate. Contacts, failed refinements, endpoint roots, jumps and gaps are information, not disposable exceptions.

## Diagnostics

1. **C25.05-D1:** Known endpoint values straddle an unknown gap. What must the ledger retain?
2. **C25.05-D2:** Does a continuous sign change prove exactly one root?
3. **C25.05-D3:** A root lies at a shared endpoint of two adjacent brackets. Count it once or twice?
4. **C25.05-D4:** Is a tangent contact a negative-to-positive passage?
5. **C25.05-D5:** What is lost by replacing the original bracket with only its refined midpoint?

**Worked answers:** (1) Both values/times, gap, geometry, continuity status and unresolved timing/count; existence only if continuity is known. (2) No; there may be multiple roots. (3) One event ID for that same family/sheet/time, retaining both supporting brackets. Different families retain distinct rows even at the same time. (4) No; the square example is positive on both sides, with zero at contact. (5) Original sample evidence, sign checks and localization bounds. Retain every refinement and failure with provenance.

**Next dependency:** [Lesson 6](lesson-06.md) applies event equations to angles and separates celestial meridians from spatial sheets.
