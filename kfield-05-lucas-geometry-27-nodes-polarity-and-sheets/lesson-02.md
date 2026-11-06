# Lesson 2 — Node addresses versus physical positions

**Essential question:** How can the same address name a position without being that position?

**Goals:** Evaluate the half-basis map with a declared origin; reverse the classroom map; assign a boundary node to its half-open cell while retaining its centered-window membership.

**Prerequisite bridge:** Lesson 1 supplied L. Fractions let us halve each entry to form q=L/2. We now teach how a basis combines three directed steps. Budget: explanation/work 20 minutes, practice 15, checks/feedback 15, transition 5.

## C05.02-E1 — Address, displacement, position

A vector is an ordered triple used to describe a directed displacement. Add vectors entry by entry; multiply a vector by a number by multiplying each entry. A basis gives three independent step vectors a,b,c. Write B=[a b c] with those vectors as **columns**. The compact expression Bq means q₁a+q₂b+q₃c. It does not require a new kind of arithmetic. Independence here means that a position has one address; the explicit inverse below will check that property for our example.

The source's rule is p(L)=O_K+B L/2. O_K is the declared origin point, q=L/2 is the dimensionless half-address, Bq is displacement from that origin, and p is position. Adding the origin changes position, not displacement. When subtracting a point from another point, the result is a displacement.

All numerical work in this course uses a **classroom analogue, not Cell3 and not measured data**. Let U denote an arbitrary length unit. Take O=(2,−1,4) U and the following table of basis components:

|Component|a|b|c|
|---|---|---|---|
|x|1|1|0|
|y|0|2|0|
|z|0|0|−3|

The entries have unit U; thus a=(1,0,0) U, b=(1,2,0) U, c=(0,0,−3) U. This gives the directly usable rules

pₓ=2+q₁+q₂, pᵧ=−1+2q₂, p_z=4−3q₃,

where position components are numerical values in U. To reverse them, first subtract O and call the components dₓ,dᵧ,d_z. Solve the last two equations first: q₂=dᵧ/2, q₃=−d_z/3. Then q₁=dₓ−dᵧ/2. Finally L=2q. This teaches the inverse operation by ordinary linear equations, rather than assuming matrix inversion.

## C05.02-W1 — Worked map and reverse map

For L=(1,−1,1), q=(1/2,−1/2,1/2). The displacement is (1/2−1/2,2(−1/2),−3(1/2))=(0,−1,−3/2) U. Add O to obtain p=(2,−2,5/2) U. To reverse: d=(0,−1,−3/2), so q₂=−1/2, q₃=1/2, q₁=0−(−1)/2=1/2. Doubling recovers the original L. The forward and reverse answers agree exactly; no rounding is needed.

## C05.02-E2 — A centered window and a cell owner answer different questions

The centered window contains q entries −1/2,0,+1/2. Cell ownership uses half-open intervals: [−1/2,1/2) includes its left endpoint and excludes its right endpoint. A cell indexed by the integer triple z owns q when u=q−z has each component in that interval. For this finite window, −1/2 and 0 have owner component 0; +1/2 has owner component 1. For general q the same rule is z=floor(q+1/2), entry by entry. The floor of a number is the greatest integer no larger than it, so floor(−0.2)=−1.

For q=(1/2,−1/2,1/2), z=(1,0,1), u=(−1/2,−1/2,−1/2). Retain both z and u: q=z+u reconstructs the half-address. This is an ownership operation, not an unspecified nearest-integer rounding convention. No nearest-integer operation is needed in this course.

## C05.02-P1 — Guided practice, with answer

Map L=(0,1,−1) and the center. Reverse the first map and assign its owner. Answer: q=(0,1/2,−1/2); p=(2+1/2,−1+1,4+3/2)=(5/2,0,11/2) U. Subtracting O gives (1/2,1,3/2), so q=(1/2−1/2,1/2,−1/2), as required. Its owner is z=(0,1,0) and u=(0,−1/2,−1/2). At L=0, q=0 and p=O, with z=u=0.

> **Claim scope:** S02 /backbone_sequence/2/definitions gives the node map; /backbone_sequence/1/definitions and /boundary_rule give cell ownership. O abbreviates O_K only in the classroom analogue. Its basis never replaces the source-locked Cell3 basis. The source uses ICRS columns and an intentional negative determinant; our component arithmetic is a separate finite teaching example.

## Diagnostic checks

1. **C05.02-D1:** Map L=(1,0,0); give its cell owner. Does that change its membership in the centered window?
2. **C05.02-D3:** Recover L from p=(2,0,11/2) U.
3. **C05.02-D4:** Why is p=B L incorrect for this node rule?
4. **C05.02-D5:** Compare owners of q=(−1/2,0,0) and (+1/2,0,0), and reconstruct both using z+u.

**Worked answers:** 1. q=(1/2,0,0), p=(5/2,−1,4) U, z=(1,0,0). It remains a window node; it belongs to the positive neighbor cell. 2. d=(0,1,3/2), q=(−1/2,1/2,−1/2), so L=(−1,1,−1). 3. It omits the factor 1/2 and the origin; even the center would be misplaced. 4. Owners are (0,0,0) and (1,0,0), respectively. Both have u=(−1/2,0,0); keeping the owner distinguishes them and reconstructs both.

**Next dependency:** [Lesson 3](lesson-03.md) groups these physical points into sheets using their original integer addresses.
