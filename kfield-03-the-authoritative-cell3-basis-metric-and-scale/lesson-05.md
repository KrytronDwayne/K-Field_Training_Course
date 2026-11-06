# Lesson 5 — Scale classes and the area anchor

**Essential question:** Why can ratios determine shape while leaving one size still free?

**Goals.** Derive how lengths, areas, volume, and metrics scale; explain the positive ray of possible lengths; determine a scale from a positive area anchor; distinguish supplied ratios from a physical interpretation.

## Bridge

You have calculated edge lengths, face areas, and signed volume. Multiplying every edge by the same positive number s produces a larger or smaller version with the same angles. A positive s preserves handedness. Negative scaling would reverse orientation and is not part of the positive scale class used here.

Because a dot product multiplies two edge components, M becomes s²M. Each cross product also multiplies two components, so every face area becomes s² times its previous value. A triple product multiplies three components, so signed volume becomes s³det(B). Inverting s²M gives s^−2R: multiplying these two matrices still yields I. Edge lengths scale by s, while ratios of any two lengths or any two areas remain unchanged. A normalized direction stays the same because both vector and its magnitude gain s.

## Worked example — Classroom analogue, not Cell3

The original ab area is 2L². Choose a new supplied anchor A_ab=8L². Since 2s²L²=8L², s²=4 and the allowed positive scale is s=2. The new numerical basis is [[2,2,0],[0,4,0],[0,0,−6]]L.

Its ab/ac/bc areas are 8L²,12L²,12sqrt(5)L², its determinant is −48L³, its Gram matrix is 4M_ex, and its inverse metric is R_ex/4. The ratio A_ac/A_ab is 12/8=3/2, the same as 3/2 before scaling. Its normalized area list in bc/ac/ab order is (1,1/sqrt(5),2/(3sqrt(5))), both before and after. “Normalized” here means dividing the whole area list by A_bc; to reconstruct actual areas retain A_bc as well as the list. If we retained only ratios, absolute scale would be missing.

## The source's conditional uniqueness argument

S02 `/scale_uniqueness_theorem` supplies a fixed labeled angular frame and positive constants eta and alpha. They are inputs in this course, not quantities we derive from masses or other experiments. Their interpretation belongs to course-08. Write l_a,l_b,l_c for the three positive edge lengths, and theta_ab,theta_ac,theta_bc for the included angles. The source specifies

l_c/l_a=(eta/1000) sin(theta_ab)/sin(theta_bc)=k_c,

l_b/l_a=(alpha^−1/100) sin(theta_ac)/sin(theta_bc)=k_b.

Here alpha^−1 means 1/alpha; k_b and k_c name the resulting positive dimensionless ratios. Sines are the height factors taught in Lesson 3. Nondegenerate fixed angles and positive inputs are essential: a zero denominator is not permitted. The source angular frame must also be a realizable independent three-dimensional frame, as the locked basis supplies.

Set l_a=t. Then l_b=t k_b and l_c=t k_c, so

(l_a,l_b,l_c)=t(1,k_b,k_c), t>0.

This is a **positive ray**: one fixed ratio triple multiplied by any positive size t. Two ratios fix relative lengths, not orientation by themselves. The fixed labeled frame provides directions. With this frame and these ratios already supplied, only one continuous scale remains.

The area equation A_ab=l_a l_b sin(theta_ab) becomes A_ab=t² k_b sin(theta_ab). Supply a positive area anchor A_* for this face. Dividing and taking the positive square root gives

t=sqrt(A_*/[k_b sin(theta_ab)]).

The denominator is positive and dimensionless, so t is a length and is unique among positive choices. Other nonzero labeled face anchors work in the same way with their own factors. We can use the supplied locked A_ab=0.19486916546048413 nm² as the numerical anchor for the Cell3 card; that choice does not establish why nature would select it.

A hand-checkable ray example has k_b=2, k_c=3 and all three angles 90 degrees. With A_*=8L², t=sqrt(8/2)L=2L and lengths are (2,4,6)L. This **separate synthetic ray example** illustrates the algebra; its right angles differ from our sheared classroom analogue. It is not a replacement basis for that analogue or for Cell3.

> **Claim scope.** The scale-uniqueness argument is conditional algebra from supplied angular and ratio inputs. It does not derive the angular frame, eta, alpha, the area anchor, or their physical origin. The source's bc/ac/ab ray is a list of area ratios, not the edge-length ray (1,k_b,k_c).

## Guided practice and diagnostic checks

1. Scale the classroom analogue by s=3. Give ab area, determinant, and inverse metric factor.
2. An analogue anchor asks for A_ab=18L². Find s and the ac area.
3. Can the two supplied length ratios alone distinguish t=1L from t=10L? Explain.
4. In the right-angle ray example k_b=2,k_c=3, replace the anchor by 2L². Find lengths. Why is a zero anchor excluded?

## Worked answers

1. A_ab=9·2=18L²; det=27(−6)=−162L³; inverse metric R_ex/9.
2. 2s²=18 gives s=3, so A_ac=9·3=27L².
3. No. t cancels in both ratios. A dimensional anchor is needed.
4. t=sqrt(2/2)L=1L, so lengths (1,2,3)L. A zero anchor would force t=0 in this nondegenerate frame, collapsing the cell and violating t>0.

**Next dependency:** [Lesson 6](lesson-06.md) turns the source lock, units, and numerical checks into a reproducible geometry card.
