# Lesson 03 — Scaling length, area, and node counts

**Essential question:** Which quantity changes when a fixed region is subdivided?

**Goals:** Derive length/area/volume scale factors; count distinct corners; count half-step samples and reachable sheets.

**Bridge:** Lessons 01–02 distinguished regions, vertices and residue classes. Multiplication counts independent coordinate choices. **Pacing:** two 55-minute periods. Period A covers E1/W1/P1/D1,D3; period B covers E2/W2/P2/D2,D4. In each use 20 minutes explanation/examples, 15 practice, 15 checks/feedback, 5 transition. The extra period prevents the sampling-grid argument being rushed.

## C06.03-E1 — Hold the outer boundary fixed

Take a fixed outer Group with basis 3B. At depth n2 each original cell edge has been halved n2 times, giving subcell basis 2^(−n2)B. A negative exponent means reciprocal: 2^(−2)=1/4. There are m=3×2^n2 subcells along each outer edge. Thus m^3=27×8^n2 cells fill the Group. A row of m adjoining cells has m+1 distinct boundary corners. Choosing a corner on each axis yields (m+1)^3=(3×2^n2+1)^3 distinct vertices, including the geometric outer boundary.

To scale every edge by factor s, a line length is multiplied by s. An area is multiplied by s×s=s^2 because both spanning lengths change while their angle stays fixed. A volume is multiplied by s^3 because all three spanning lengths change. This remains true for a slanted parallelepiped: scaling does not change its angles. Therefore one halving divides length by 2, area by 4 and volume by 8. Eight children exactly replace a parent's volume.

## C06.03-W1 — A fixed Group through depth 2

| n2 | Cells per axis | Complete subcells | Distinct corner vertices | Subcell edge factor |
|---|---|---|---|---|
| 0 | 3 | 27 | 64 | 1 |
| 1 | 6 | 216 | 343 | 1/2 |
| 2 | 12 | 1728 | 2197 | 1/4 |

At n2=2, 27×8×8=1728; 13×13×13=2197. Multiplying 216 cells by 8 corners at depth 1 gives 1728 incidences, not 343 distinct vertices. Shared vertices belong geometrically to multiple cell closures, so counting once per incident cell repeats them.

For numerical volume practice use a **classroom analogue, not Cell3 or measured data**. Its edge columns are a=(1,0,0), b=(1,2,0), c=(0,0,−3) arbitrary length units. In the first two coordinates a and b span base area 1×2=2 square units; c has perpendicular height 3. Its positive volume is 6 cubic units (its signed determinant is −6). The fixed Group occupies 27×6=162 cubic units. We do not replace the locked physical Cell3 basis with these toy values.

The source family B_(p,n)=3^p×2^(−n)B describes a scaled basis: p,n are its scale labels. Holding p fixed and varying n changes that basis. It does not say the fixed outer 3B boundary shrinks in our cell-count experiment; distinguish the basis of the object you are naming from its containing region.

## C06.03-E2 and C06.03-W2 — Half-step samples and sheets

Now change the sampling grid, not the outer region. A centered 9B span extends from −9/2 to 9/2 along each basis coordinate. Half-step sampling labels coordinates i/2, with integer i=−9 through 9. An inclusive integer list from −m to m has 2m+1 entries: m negatives, zero, m positives. Thus 19 choices per axis yield 19^3=6859 sample points.

Define lambda=i+j+k for the three integer half-step labels. A sheet is the set of grid points sharing one lambda value. Minimum lambda is −27, maximum 27. All 55 integer values are attained: for target t from 0 to 9 use (t,0,0); for 10 through 18 use (9,t−9,0); for 19 through 27 use (9,9,t−18). Negate coordinates for negative targets. This proves no intermediate sheet is missing. It does not claim equal populations on all sheets.

An ordinary cell-corner grid on the same 9B span has ten corners per axis, hence 1000 corners. The half-step grid includes those boundary corners plus additional samples. Keep four separate counts: 729 volumes, 1000 ordinary corners, 6859 half-step points, 55 sheets.

> **Scope:** S02 /backbone_sequence/2/typed_finite_objects and /recursions supply the grid and source counts. These derivations are finite geometry. Sampling includes boundary points even where half-open ownership assigns them to a neighbor. Lambda here uses half-step integer labels; no force or measured signal is inferred.

## Guided practice

**C06.03-P1:** Derive the cell and distinct corner counts at depth 2 from cells per axis. Then from depth 1 to 2, give subcell length/area/volume factors and verify total volume for the toy Group.

**Answer:** Depth 2 has 3×4=12 cells per axis, so 12^3=1728 cells and 13^3=2197 distinct corners. Factors are 1/2,1/4,1/8. Depth 1: each volume 6/8=3/4, so 216×3/4=162. Depth 2: each volume 6/64=3/32, so 1728×3/32=162. No volume disappeared.

**C06.03-P2:** For a centered 3B span count half-step points, sheet values, volumes and ordinary corners. Produce lambda=8 and −8.

**Answer:** Labels −3 through 3 give 7^3=343 samples; sums −9 through 9 give 19 sheets. There are 3^3=27 volumes and 4^3=64 corners. (3,3,2) and (−3,−3,−2) realize ±8. The same filling argument as W2 realizes every intermediate sum.

## Diagnostic checks

1. **C06.03-D1:** Why is 216×8 not the distinct vertex count at n2=1? Is outer 3B shrinking?
2. **C06.03-D2:** Label 729,1000,6859,55 for the 9B span, including sampling grids.
3. **C06.03-D3:** Relative to depth zero, what are the depth-2 length, area and volume factors?
4. **C06.03-D4:** Exhibit a half-step index triple with lambda=23 and explain why endpoints alone do not prove all sheets exist.

**Worked answers:** (1) It counts incidences with shared corners repeated; outer 3B stays fixed. (2) Complete volumes, ordinary corners, half-step samples, lambda sheets respectively. (3) 1/4,1/16,1/64. (4) (9,9,5); a range could contain gaps, so the constructive filling rule is needed.

**Next:** [Lesson 04](lesson-04.md) encodes signed addresses with powers of three.
