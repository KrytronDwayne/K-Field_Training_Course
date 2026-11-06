# Lesson 2: What uniform scaling leaves unchanged

Essential question: Why can changing every length leave the area ray unchanged?

Goals

- Derive the square law for uniform length scaling.
- Prove cancellation in both independent ratios.
- Distinguish uniform scaling from changing a single supplied area.

Pacing: 55 minutes — retrieval 5; explanation and worked example 20; guided practice 15; diagnostics and repair 15.

Prerequisite bridge

Lesson 1 taught the ordered triple and retained divisor. Recall that multiplying a fraction numerator and denominator by the same nonzero number preserves its value. Check 8/12=32/48=2/3. We now explain where the common factor comes from.

## C08.02-E1 — One scale, two length factors

Let s be a positive dimensionless length multiplier: every length becomes s times its old value while angles remain fixed. A face has two length factors. In a rectangle, (s×length)(s×width)=s²×area. A parallelogram obeys the same rule: its base and perpendicular height both scale by s. Here s² means s×s. Thus all three areas are multiplied by s². This uniform transformation is sometimes written B→sB, where B is the ordered list of the three basis vectors; no matrix calculation is needed here.

Write A'_ac=s²A_ac and A'_bc=s²A_bc, where the prime marks the scaled value. Because s>0 and A_bc>0, the denominator is nonzero. Cancel the common factor to obtain A'_ac/A'_bc=(s²A_ac)/(s²A_bc)=A_ac/A_bc. Separately, A'_ab/A'_bc=(s²A_ab)/(s²A_bc)=A_ab/A_bc. These two calculations prove invariance of both independent components, rather than relying on one numerical coincidence. The first ray component remains 1.

To reverse the scaling, divide all scaled areas by s² if s is retained. Alternatively retain the original A_bc as a dimensional anchor along with r. A ray by itself cannot tell us which s was used.

## C08.02-W1 — Doubling lengths

Starting with (12,8,6) U², choose s=2. Then s²=4 and the new areas are (48,32,24) U². Dividing by 48 gives (1,32/48,24/48)=(1,2/3,1/2). Divide the new areas by 4 to recover (12,8,6). The areas changed, although the ray did not.

> Claim scope: The proof applies to a positive uniform rescaling with angles and face labels fixed. It does not assert that any arbitrary change in three supplied areas is uniform scaling. It reproduces the common-scale argument in S01 and S02, M05; it establishes algebraic invariance, not a physical mechanism.

Guided practice — C08.02-P1

Use s=1/2 on W1’s original input. Compute the areas, normalize, and reverse. Then prove both ratio cancellations for an arbitrary positive s and positive starting areas. **Answer:** s²=1/4, so the areas are (3,2,3/2) U². Their ray is (1,2/3,1/2). Dividing by 1/4, equivalently multiplying by 4, restores (12,8,6) U². For arbitrary s>0, the two ratios are (s²A_ac)/(s²A_bc)=A_ac/A_bc and (s²A_ab)/(s²A_bc)=A_ab/A_bc. Each cancellation is valid because s² is nonzero and A_bc>0. Thus both independent components remain unchanged for every permitted s, not only the numerical case.

Diagnostic checks

1. **C08.02-D1** Change only A_ac from 8 to 9 U². Does the ray remain fixed?

2. **C08.02-D2** Starting with (15,10,5), test s=2 and s=1/2.

3. **C08.02-D3** Why is s=0 excluded from the proof?

4. **C08.02-D4** If areas all double, did lengths necessarily double under uniform scaling?

Worked diagnostic answers

1. No. The new ray is (1,9/12,6/12)=(1,3/4,1/2). Only one supplied area changed.

2. The triples are (60,40,20) and (15/4,5/2,5/4). Divide by 60 or 15/4 respectively to get (1,2/3,1/3) in both cases.

3. All areas would become zero, so the normalized fractions would be 0/0 and undefined.

4. No. Doubling lengths multiplies areas by 4. An area factor of 2 requires a positive length multiplier whose square equals 2; no square-root computation is required.

Next dependency: [lesson-03](lesson-03.md). Carry the labeled input triple, divisor, source role, and retained differences forward.
