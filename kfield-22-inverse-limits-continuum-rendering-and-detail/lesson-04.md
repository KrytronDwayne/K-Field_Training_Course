# Lesson 04 — A convergent real-space renderer

Essential question: How can a finite image have a certified error bound without erasing its infinite history?

Goals: Derive a geometric sum and tail; choose depth by testing powers; convert coordinate bounds to length bounds; preserve distinct histories with a shared image.

Bridge and pacing: Lesson 03 supplied a full digit rule; a real sum now uses decreasing weights instead of the increasing weights of address residues. Three 55-minute periods, each with retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15. Periods cover geometric sums, vector bounds, then endpoint histories. All vector and matrix operations required here are defined below.

## C22.04-E1 — From finite sum to controlled tail

Write S_N=r+r²+…+r^N. Multiplying by r shifts the terms: rS_N=r²+…+r^(N+1). Subtracting cancels the middle terms, so (1−r)S_N=r−r^(N+1). If r≠1, division gives S_N=r(1−r^N)/(1−r). This is a finite identity. To pass to an infinite sum we additionally need |r|<1, so r^N tends to zero. For q=|r|<1, the sum of absolute weights after N is q^(N+1)/(1−q). Absolute values matter because cancellation of signed terms can hide a large tail of separate contributions.

The normalized M18 renderer is z_N=(1/2)Σ_(j=1)^N 3^(−j)u_j, with u_j an ordered triple of balanced digits. Σ means add the indicated terms. Calculate each coordinate separately. Each digit has absolute value at most 1, so each coordinate of z−z_N has absolute value at most (1/2)Σ_(j>N)3^(−j)=1/(4·3^N). This proves convergence: two sufficiently deep partial sums differ by at most the same shrinking tail bound. The complete real-number system supplies their limit z. Keep the full digit rule or the unresolved continuation as well as N and z_N; a bound describes the missing contribution but is not a replacement for it.

For a vector w=(w₁,w₂,w₃), define ||w||∞=max(|w₁|,|w₂|,|w₃|). A matrix B acts by row sums: (Bz)_i=B_i1 z₁+B_i2 z₂+B_i3 z₃. Define ||B||∞ as the largest sum of absolute entries in a row. The triangle inequality |a+b|≤|a|+|b| gives ||Bw||∞≤||B||∞||w||∞. Thus r_N=Bz_N has tail at most ||B||∞/(4·3^N). Here r_N denotes a physical displacement, whereas the scalar r earlier in the geometric formula was a ratio. Absolute positions would be x_N=O_K+r_N with declared origin O_K; differences use x−O_K. If B entries have length units, r and its bound do too.

## C22.04-W1 — Worked bounds (alias C22-TAIL-EX1)

First use d_j=2^(−j). The sum is S_N=1−2^(−N); the remaining positive tail is exactly 2^(−N). For tolerance 0.01, check successive powers: 1/64=0.015625>0.01 and 1/128=0.0078125≤0.01. The smallest acceptable depth is 7. This check uses no logarithms.

For the M18 normalized coordinate bound and tolerance 1/1000, depth 5 gives 1/(4·243)=1/972>1/1000; depth 6 gives 1/2916<1/1000. Hence N=6 is the smallest depth guaranteed for every allowed digit history. A specific history can have a smaller actual tail.

Use the **synthetic** length-valued matrix B=diag(2,3,4) LU, meaning rows (2,0,0), (0,3,0), (0,0,4) in an illustrative length unit LU. It is not the source-locked Cell3 basis. Its maximum absolute row sum is 4 LU, so the physical tail is at most 1/3^N LU. For the all-positive first-coordinate rule and zero other coordinates, z_N=((1−3^(−N))/4,0,0). At N=2, z₂=(2/9,0,0), r₂=(4/9,0,0) LU; the limit r=(1/2,0,0) LU. The actual remaining displacement is (1/18,0,0) LU, below the general bound 1/9 LU. Store that signed remainder, not merely its norm.

> Claim scope: S02 /backbone_sequence/17/definitions/3 and /backbone_sequence/17/proof/1 and /backbone_sequence/17/proof/2 supply the renderer and normalized bound. These calculations derive their finite consequences. The diagonal B and LU are teaching choices with no asserted Cell3 handedness or numerical calibration. No observation or mechanism claim is added.

## C22.04-P1 — Practice, then check (alias C22-TAIL-P1)

(a) Choose the smallest N for the binary-weight tail tolerance 1/32. (b) For the synthetic B above, certify a physical infinity-norm tolerance 1/1000 LU. (c) Render first-coordinate histories h=(1,−1,−1,…) and k=(0,1,1,…), each with the indicated constant tail and zero other coordinates. Compute their depth-2 images and their infinite images; retain both histories.

Answer: (a) N=5 since 2^(−5)=1/32 and depth 4 gives 1/16. (b) N=7 since 1/729>1/1000 but 1/2187≤1/1000. (c) Σ_(j≥2)3^(−j)=1/6. Thus z(h)=(1/2)(1/3−1/6)=1/12 and z(k)=(1/2)(1/6)=1/12 in the first coordinate. At depth 2, z₂(h)=1/9 and z₂(k)=1/18. Their signed tails are −1/36 and +1/36, respectively, each attaining the normalized depth-2 bound. Their first residues differ, so the complete histories remain distinct. For this synthetic B their common physical first coordinate is 1/6 LU. The mature object is the ordered pair (exact history, image); saving the image alone would lose which history occurred.

## Diagnostics — C22.04-D1 (alias C22-TAIL-D1)

1. Does the infinite-tail argument apply when scalar ratio r=1?
2. Do opposite signed contributions permit deleting both terms?
3. Is 1/(4·3^N) automatically a length bound for every B?
4. At depth 3 compute the normalized all-positive scalar image and its exact tail.

Worked answers: (1) No. The finite sum is N, division by 1−r fails, and partial sums grow. (2) No. Their sum may vanish but the individual contributions and their rule remain information. (3) No: it is dimensionless; multiply by the declared matrix norm for a physical bound. (4) z₃=(1−1/27)/4=13/54; limit 1/4; tail 1/108. The tail is positive for this rule, while the absolute bound permits either sign for other rules.

Next dependency: [Lesson 05](lesson-05.md) asks what a finite-prefix observation can distinguish even when finer history is retained.
