# Capstone — Audit and decode a graph state

Allow two 55-minute periods. Period A: 5 minutes conventions, 35 minutes steps 1–4, 15 minutes checking. Period B: 5 minutes retrieval, 30 minutes steps 5–6, 20 minutes reconstruction checks and explanation. Use the lessons and glossary; no programming or advanced theorem is required. All supplied numerical states are synthetic and dimensionless.

Use square vertices 0 bottom left, 1 bottom right, 2 top right, 3 top left, with edges 01,12,23,30 in that order. Its tree is 01,12,23. Use the Lucas order, root and first-nonzero parent rule from Lesson 04, and the wrap order and cycle basis from Lesson 05. Keep every sign and remainder.

## Student tasks

1. **C11-CAP-01 — Build and count (12 points).** Draw the open 3×2 rectangle. List the two types of edge and count its vertices and edges. Use the same direction-count argument to audit 27 vertices and 54 edges for open Lucas. Explain why 0→2 is not an open edge. Output: drawing, edge description and justified counts.
2. **C11-CAP-02 — Encode incidence (18 points).** Build the ordered square incidence matrix. Compute the divergence of f=(2,3,4,5). Show the fourth column depends on the first three and prove those three independent by row equations. Output: table, divergence and rank proof.
3. **C11-CAP-03 — Verify a cycle (16 points).** Identify the square chord and construct its fundamental cycle with +1 on that chord. Verify balance. For φ=(0,1,3,2), compute the gradient and its dot product with the cycle. Decode 3c and explain the change if the cycle orientation is reversed. Output: signed cycle, gradient, check and decoder.
4. **C11-CAP-04 — Audit Lucas dimensions (18 points).** Specify the reproducible Lucas tree and give parent(1,2,1). Explain connected rank 26 and cycle dimension 28 using leaf elimination and chords. Explain independence and generation of the 28 cycle columns. Output: construction and proof, not just two numbers.
5. **C11-CAP-05 — Preserve wrap information (24 points).** Add periodic wraps to Lucas and audit 81 edges and 55 cycle coordinates. Use axis-0 wrap list (0,0,0,0,0,0,0,0,9), with the other axes and all open coefficients zero. Compute W, the mean, eight free details, and the ninth dependent detail. Recover all 55 cycle coefficients and state the resulting circulation as a basis sum. Identify its nonzero edges using the declared tree. Explain what 52+3 means and what it does not establish. Output: counts, reversible coordinate record and reconstructed state.
6. **C11-CAP-06 — Retain a complete flow (12 points).** For the square, reconstruct a general flow from q=5 and r=(−3,−2,−1,0). Check its divergence and compare it with the divergence of r. State what metadata the decoder needs and why 28, 52 or 55 does not specify a physical memory lifetime. Output: reconstructed flow and a scoped explanation.

## Full worked answer key and point rubric

**1.** The diagram in Lesson 01 has vertices (x,y), x=0,1,2 and y=0,1: six in all. Horizontal edges join (0,y) to (1,y) and (1,y) to (2,y), two per row and four total. Vertical edges join (x,0) to (x,1), three total. Thus E=7. Award 4 points for a correctly labeled drawing and 3 for the edge count with factors. Lucas has 3³=27 vertices; each of three axes contributes 2×3×3=18 edges, so E=54 (4 points). A 0→2 jump skips an allowed step (1 point).

**2.** With rows 0,1,2,3 and columns 01,12,23,30:

```text
-1  0  0  1
 1 -1  0  0
 0  1 -1  0
 0  0  1 -1
```

Award 6 points for signs and ordering. Df=(−2+5,2−3,3−4,4−5)=(3,−1,−1,−1), total zero (4 points). The fourth column is minus the sum of the first three (3 points). If sa+tb+uc=0, rows 0,1,2 give −s=0, s−t=0, t−u=0, hence s=t=u=0. First three independent; rank=3 (5 points).

**3.** Chord 30 closes the path 0→1→2→3, so c=(1,1,1,1) in declared edge order (4 points). Every row of Dc is zero (3 points). Dᵀφ=(1,2,−1,−2) and c·Dᵀφ=1+2−1−2=0 (5 points). The chord entry decodes coefficient 3, giving 3c=(3,3,3,3). In basis −c the coefficient is −3; the state is unchanged (4 points).

**4.** Order vertices lexicographically, edges by axis then tail, with increasing-coordinate arrows. Root is (0,0,0). Parent decrements the first nonzero coordinate, so parent(1,2,1)=(0,2,1). The coordinate sum decreases until zero, proving every vertex reaches the root; 26 distinct parent edges form the tree (5 points). Tree incidence columns are independent by leaf elimination, while all divergence lists sum to zero and hence have at most 26 free entries: rank=26 (5 points). There are 54−26=28 chords. Each has a fundamental cycle with own-chord entry +1 and no other chord. Inspecting chord entries proves independence. Subtracting those coefficients from any circulation leaves a tree circulation, zero by leaf elimination, proving generation and dimension 28 (8 points).

**5.** There are nine wraps per axis and 27 total: 54+27=81 edges. Vertex count and connected rank remain 27 and 26, so 81−26=55 cycles (6 points). For the supplied list W=9, μ=1, d1,…,d8=−1 and d9=8 (6 points). The inverse W/9+d_j recovers eight zeros and 9, with all other-axis coefficients and all 28 open coefficients zero. Thus among the 55 coefficients only w_(0,9)=9 is nonzero, giving f=9h_(0,9) (6 points). This cycle has wrap (2,2,2)→(0,2,2), then tree edges (0,2,2)→(1,2,2) and (1,2,2)→(2,2,2). Those entries are 9, all others zero (3 points). The equality 52+3 means 28 open-cycle coordinates plus 24 independent wrap details, together with 3 winding sums. It supplies no exceptional-group action or dynamics (3 points). Full credit requires keeping the details, even though all nine wrap values can be written compactly here.

**6.** q c=(5,5,5,5); adding r gives f=(2,3,4,5) (4 points). Df=Dr=(3,−1,−1,−1), computed row by row; Dc=0 explains the equality (4 points). The decoder needs the graph, ordered oriented edges, tree, cycle basis, coefficient and remainder. A count says how many scalar values are available, while lifetime requires a physical retained state and evolution/retention evidence (4 points).

Total: 100 points. Do not award reconstruction points when a nonzero remainder is silently dropped. A consistent alternative orientation is mathematically valid if the student explicitly transforms the requested convention and shows the inverse. Require repair of wrong graph adjacency, wrong matrix signs, discarded details/remainder, or an unsupported dynamics claim regardless of total score. Other partial credit follows the subdivisions above; assess reasoning as well as final numbers.

## Backward teaching map

| Step | Earlier explanation and example | Independently answered prior practice | Earlier diagnostic |
|---|---|---|---|
| C11-CAP-01 | C11.01-E1, C11.01-W1 | C11.01-P1: draw/count rectangle, square and cube | C11.01-D1 |
| C11-CAP-02 | C11.02-E1, C11.02-W1 | C11.02-P1: square D, product and elimination | C11.02-D1 |
| C11-CAP-03 | C11.03-E1, C11.03-W1 | C11.03-P1: square cycle, gradient and decoder | C11.03-D1 |
| C11-CAP-04 | C11.04-E1, C11.04-W1 | C11.04-P1: tree construction, rank, independence/generation | C11.04-D1 |
| C11-CAP-05 | C11.05-E1, C11.05-W1 | C11.05-P1: periodic counts, eight details and full inverse | C11.05-D1 |
| C11-CAP-06 | C11.06-E1, C11.06-W1 | C11.06-P1: square remainder, reconstruction and update comparison | C11.06-D1 |

**Evidence scope:** Core graph formulas: S02#/backbone_sequence/7. Count versus exceptional-action boundary: S02#/backbone_sequence/18/branches/exceptional_cycle_bridge. Serialization limitation: S03#/findings/1. Numerical flow lists are synthetic classroom inputs. The assessment proves finite calculations and decoder properties; it does not adjudicate the full source formula DAG or physical memory mechanism.
