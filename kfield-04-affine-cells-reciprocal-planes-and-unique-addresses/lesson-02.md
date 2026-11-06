# Lesson 2 — Why half-open cells have one owner

**Essential question:** How can every boundary point belong to exactly one cell?

**Goals:** Read half-open intervals; assign integer owners using floor, including negative addresses; reconstruct an address from its owner and local coordinate.

**Bridge:** Lesson 1 assigns exactly one dimensionless address q to each physical point. We now organize addresses into cells. Keep B and O unchanged; this lesson changes the description of q, not the point.

## C04.02-E1 — A number-line rule with no gaps

An interval is a range of numbers. A square bracket includes its endpoint; a round bracket excludes it. Thus [-1/2,1/2) includes -1/2 and all numbers up to, but not including, 1/2. The cell centered at integer k uses [k-1/2,k+1/2). The right endpoint of one interval is the included left endpoint of the next:

| Owner k | Included range |
|---|---|
| -1 | [-3/2,-1/2) |
| 0 | [-1/2,1/2) |
| 1 | [1/2,3/2) |

The **floor** of a real number t, written floor(t), is the greatest integer less than or equal to t. It is a move toward the left on the number line, not a deletion of decimal digits: floor(-1.2)=-2, while floor(1.2)=1.

For one address entry define z=floor(q+1/2). The defining floor inequality says z≤q+1/2<z+1. Subtract z+1/2 from every part to obtain -1/2≤q-z<1/2. Set u=q-z. We have **q=z+u**, with integer owner z and retained local coordinate u in [-1/2,1/2).

Why is z unique? The intervals above touch only at an endpoint, and only the interval on its right includes that point. Every number lies in one interval, never two. In three dimensions do this independently in each entry. The notation [-1/2,1/2)^3 means all triples whose three entries lie in that interval. It is a product of three ranges, not the cube of a number.

The physical cell owned by integer triple z consists of points O+B(z+u) with u in that product. Since B has a unique inverse, different address descriptions cannot secretly represent one physical point. Therefore the address partition gives unique physical ownership too.

## C04.02-W1 — Three exact boundaries

For q=(1/2,-1/2,3/2), first add 1/2 to each entry: (1,0,2). Applying floor gives **z=(1,0,2)**. Subtract componentwise: **u=(-1/2,-1/2,-1/2)**. Every local entry is allowed because the lower endpoint is included. Adding z+u returns the original q exactly.

A local +1/2 would be excluded. It must instead be represented as -1/2 in the next positive-index cell. This is true even when the global address is negative.

## C04.02-P1 — Negative and near-boundary addresses

Find z and u for q=(-3/2,49/100,51/100). Check the range of all three local entries, then add them back.

**Worked answer:** q+(1/2,1/2,1/2)=(-1,99/100,101/100), whose floors are (-1,0,1). Subtracting gives u=(-1/2,49/100,-49/100). The second entry stays just below the upper boundary; the third moves into the neighboring cell. The sum (-1,0,1)+(-1/2,49/100,-49/100) recovers all entries of q.

> **Claim scope:** This is an exact mathematical partition convention, adopted for Cell3 in S02 `/backbone_sequence/1`. It is not a claim that a measured point has infinite precision. It is also separate from a generic nearest-integer rounding rule. If nearest-integer rounding is needed elsewhere, its half-tie rule must be declared. Here floor(q+1/2) assigns half ties toward the larger integer and gives the local interval [-1/2,1/2). A library's ties-to-even rounding may disagree and cannot replace the ownership operation.

## Diagnostic checks

1. **C04.02-D1:** Compare owners of 499/1000 and 1/2. Why must you not round the first before assignment?
2. Find floor(-7/5), then the owner and local coordinate of q=-7/5.
3. Is z=0,u=1/2 a valid representation of q=1/2 under this rule? Repair it.
4. Does retaining only z allow reconstruction? Give two different addresses with owner zero.

**Worked answers:** (1) floor(999/1000)=0, but floor(1)=1. Rounding erases which side of the boundary the input occupies. (2) floor(-1.4)=-2; ownership uses floor(-1.4+0.5)=floor(-0.9)=-1. Thus u=-7/5+1=-2/5. (3) No: the local upper endpoint is excluded. Use z=1,u=-1/2. (4) No. q=0 and q=1/4 both have owner zero but different u. Retaining u is essential information.

**Pacing:** 20 minutes explanation/worked example, 15 practice, 15 diagnostics and feedback, 5 transition.

**Next dependency:** [Lesson 3](lesson-03.md) constructs physical vectors that read address entries and label parallel planes.
