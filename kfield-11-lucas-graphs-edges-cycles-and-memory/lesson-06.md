# Lesson 06 — Memory needs a specified state

**Essential question:** What must be retained to recover a flow exactly?

**Goals:** Decode a specified cycle state; separate a general flow into cycle coefficients and a retained tree remainder; explain why coordinate counts do not determine dynamics.

**Bridge and time:** Lessons 03–05 gave cycle bases and their decoders. We now apply subtraction without discarding the information it removes. One 55-minute period: 5 retrieval, 20 teaching/example, 15 practice and 15 diagnostics/repair minutes.

## C11.06-E1 — A reversible representation

In this course **memory** means a specified retained state together with a decoder that recovers it. This is an operational information definition. To specify a cycle state, retain the graph, edge order, orientations, tree, cycle basis and coefficients. The basis tells you how each coefficient affects the edges. A verified circulation needs only those cycle coefficients once the conventions are fixed.

A general edge flow f may not satisfy Df=0. Read each chord value q_i and form the circulation s=Σ_i q_i c_i. Define the **tree remainder** r=f−s. On every chord, subtraction removes the same q_i, so r is supported on tree edges. Keep r as a primary coordinate, rather than calling it error and erasing it. The inverse is f=s+r. Moreover Dr=Df−Ds=Df because Ds=0. Thus r retains the complete divergence information. If f was a circulation, Dr=0 and tree elimination forces r=0. Otherwise the remainder may be nonzero and is essential.

This particular decomposition is determined by chord readings. It is not in general an orthogonal split into a gradient and a cycle. A tree-supported remainder need not be a gradient on the full graph. Do not confuse the 26-dimensional cut space with every possible 26-coordinate complement to cycles. Our tree remainder is selected because its inverse is easy to teach and audit.

For the periodic graph, retain 28 open-cycle coefficients, 24 independent wrap details, 3 windings, and, for a general flow, the 26 tree-remainder values. The decoder reconstructs the 27 wrap coefficients, forms the 55-cycle sum, then adds the remainder. There are 55+26=81 independent real coordinates, matching the 81 edge values. Zero entries remain entries; signs and ordering remain part of the state.

A **dynamics** or update rule says how a state changes with time. A graph and its dimension do not select that rule. For example, a synthetic device could use q(t+1)=q(t), preserving a coordinate, or q(t+1)=2q(t), doubling it each step. Both rules use the same one-dimensional state. They predict different histories. To claim a physical memory lifetime we would need a specified physical state, update or retention mechanism, and observations over time. Those are unresolved by the dimension count itself.

## C11.06-W1 — Triangle reconstruction

Use the triangle tree 01,12 and chord 20 with c=(1,1,1). For f=(2,3,4), the chord value is q=4. Its cycle contribution is 4c=(4,4,4). Subtract entry by entry: r=(2−4,3−4,4−4)=(−2,−1,0). Then 4c+r=(2,3,4), exactly. The remainder's divergence is (2,−1,−1), the same as Df. If we retained only q=4, we would decode (4,4,4) and lose the two nonzero tree values and their imbalance. The remainder is information about this chosen flow, not a disposable defect.

> **Claim scope:** The examples are exact synthetic states, not measurements of a memory device. Source M08 names memory spaces, while the finite mathematics establishes coordinate capacity and decoding. Memory duration, forces and exceptional-group actions require further defined structure. The source-reported serialization gap AUD-002 remains separate from these finite checks.

## C11.06-P1 — Square reconstruction and scope

For the square ordered 01,12,23,30, use tree 01,12,23 and c=(1,1,1,1). Starting with f=(2,3,4,5), find q and r, reconstruct f and compare Dr with Df. Repeat for f=3c. State the metadata needed to interpret q. Finally compare q(t+1)=q(t) with q(t+1)=2q(t), starting at q(0)=3 for two updates.

**Worked answer:** q=5, 5c=(5,5,5,5), r=(−3,−2,−1,0). Adding gives (2,3,4,5). Dr=(3,−1,−1,−1)=Df. For 3c, q=3 and r=0, so q alone with the conventions recovers the flow. Required metadata include graph, edge order, orientations, tree and cycle basis. The first update rule gives 3,3,3 at times 0,1,2; the second gives 3,6,12. Identical dimension does not determine change through time.

## Diagnostics

1. **C11.06-D1:** What does a dimension count say about memory duration? Name what would be needed to say more.
2. Two square flows are (2,3,4,5) and (5,5,5,5). They share q=5. How can the stored representation distinguish them?
3. In the periodic graph, what data recover a general edge field?
4. When may the tree remainder be omitted from a circulation encoding without losing a value?

**Worked answers:** 1. It supplies no duration. Need a physical state, an update/retention mechanism and time observations. 2. Retain r=(−3,−2,−1,0) for the first and r=0 for the second. 3. Keep basis metadata, 28 open coefficients, 24 wrap details, 3 windings and 26 tree values; reconstruct wrap values, sum cycles, and add r. 4. After verifying Df=0 and applying the declared chord/tree decomposition, the tree remainder is provably zero. Recording that verification justifies its implicit zero value.

**Next dependency:** The [capstone](capstone.md) uses this entire chain to audit counts and reconstruct supplied states without dropping any coordinates.
