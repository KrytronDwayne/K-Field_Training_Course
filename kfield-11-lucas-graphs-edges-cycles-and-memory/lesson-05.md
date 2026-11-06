# Lesson 05 — Adding periodic wrap edges

**Essential question:** How can 27 new cycle values be preserved as 24 details and three winding sums?

**Goals:** Count periodic edges and cycles; separate wrap sums from details; invert the coordinate change exactly; reconstruct a circulation in the declared basis.

**Bridge and time:** Lesson 04 supplied the open tree, ordered chords and the basis decoder. Keep that tree throughout this lesson. Two 55-minute periods with 5 retrieval, 20 teaching/example, 15 practice and 15 diagnostics/repair minutes each. Period A adds wraps and counts; period B decodes details and reconstructs.

## C11.05-E1 — Add edges without losing coordinates

For each axis line, add one **wrap edge** from coordinate 2 to coordinate 0, keeping its other coordinates fixed. It closes that three-node line into a ring. These edges connect existing vertices; they do not add vertices. There are 3×3=9 lines per axis and three axes, so 27 new edges. Retain the open tree from Lesson 04. All new edges are chords relative to that tree, and each gets a fundamental cycle using the same head-to-tail tree path rule.

Order all open edges as before, then wrap edges by axis and lexicographic tail. For axis 0 their tails are (2,0,0),(2,0,1),(2,0,2),(2,1,0),(2,1,1),(2,1,2),(2,2,0),(2,2,1),(2,2,2). The analogous rule orders axes 1 and 2. Let c_i, i=1,…,28, name the open fundamental cycles. Let h_(a,j), a=0,1,2 and j=1,…,9, name the wrap fundamental cycles. Subscripts are labels, not multiplication. Each h has +1 on its own wrap edge and only tree edges elsewhere.

A periodic circulation is reconstructed by multiplying and adding:

f = Σ_i q_i c_i + Σ_a Σ_j w_(a,j) h_(a,j).

The symbol Σ means “sum over the listed index values.” The 28 numbers q_i are read at open chords, and the 27 numbers w_(a,j) at wrap chords. We retain all of them. The open cycles are local in the sense of having no seam crossing; they need not each be a single small face.

For one axis suppress the axis label and write w=(w1,…,w9). Define its **winding coordinate** W=w1+…+w9, its mean μ=W/9, and details d_j=w_j−μ. The details sum to W−9μ=0. Hence only the first eight details are free; d9=−(d1+…+d8). The inverse rule is w_j=W/9+d_j for every j. The sum and the mean differ by a factor of nine.

Why call W a winding? With the chosen seam, it is the net signed wrap crossing on that axis. For a closed route on the periodic graph, this counts net passages through the seam; a sum of weighted cycles gives the corresponding weighted coordinate. Zero-sum changes among the nine seam entries can rearrange crossings without changing W. Such changes are retained in the eight details. Winding alone therefore cannot recover the distribution among lines.

## C11.05-W1 — Count, transform, reconstruct

The periodic graph has 54+27=81 edges and the same 27 vertices. It remains connected. Rank is still 26, so cycle dimension is 81−26=55. Each axis contributes eight free details and one winding, so

55 = 28 + 3×8 + 3 = 28 + 24 + 3 = 52 + 3.

For axis 0 choose synthetic coefficients w=(1,2,3,4,5,6,7,8,9). Their sum is 45, mean 5, and details are (−4,−3,−2,−1,0,1,2,3,4). The first eight sum to −4, so the ninth is +4. Add 5 to each detail to recover the original list. With all open coefficients and other-axis wrap coefficients zero, the entire circulation is h_(0,1)+2h_(0,2)+…+9h_(0,9). This specifies all 81 edge entries by the declared signed paths, including tree entries; it is not just a list of seam values.

> **Claim scope:** S02#/backbone_sequence/7/periodic_augmentation reports 28+24+3; the coordinate construction here makes that split explicit. S02#/backbone_sequence/18/branches/exceptional_cycle_bridge separately lists exceptional-action extensions. The equality 52=28+24 does not construct an F4 action, a force or a dynamical law. The present change of coordinates is over real or rational numbers. For integer w, details can be fractional; their allowed values must satisfy W/9+d_j being an integer, including the dependent ninth value. No free integer product decomposition is asserted.

## C11.05-P1 — A concentrated seam state

Use w=(0,0,0,0,0,0,0,0,9) on axis 0, zeros on other axes and all 28 open coefficients zero. Find W, the mean, eight independent details, the ninth detail, and all reconstructed coefficients. Write the resulting circulation in the basis. Then repeat the periodic edge/rank/cycle count. As an integer check, transform w=(1,0,0,0,0,0,0,0,0).

**Worked answer:** W=9, μ=1, d1,…,d8=−1; d9=−(−8)=8. Reconstructing gives eight zeros and 1+8=9. Other coefficients remain zero, so f=9h_(0,9). Its wrap edge runs (2,2,2)→(0,2,2); its tree return path is (0,2,2)→(1,2,2)→(2,2,2), both increasing axis 0. Thus these three edge entries are 9 and all others zero. Counts are 81 edges, rank 26, cycles 55. For the integer check W=1, μ=1/9; d1=8/9 and d2,…,d9=−1/9. Every μ+d_j is integral even though each detail is fractional. Retaining W and eight details recovers the ninth and the entire original list.

## Diagnostics

1. **C11.05-D1:** If W=9, is the mean 9? Explain the integer compatibility issue as well.
2. Why are there only eight free details per axis?
3. What is lost by keeping only the three winding sums? How do we avoid losing it?
4. If all W values are zero, must the circulation be zero?

**Worked answers:** 1. The mean is 9/9=1. With integer source coefficients each reconstructed W/9+d_j must be integral; arbitrary integer choices of W and details need not satisfy this. 2. The zero-sum equation fixes the ninth as minus the first eight. 3. The 24 wrap-distribution details and 28 open-cycle coordinates are not specified by W; retain them and the basis. 4. No. An open fundamental cycle has zero winding, and nonzero opposite wrap details can also sum to zero.

**Next dependency:** [Lesson 06](lesson-06.md) asks exactly which state these coordinates preserve, especially when the original edge field does not balance.
