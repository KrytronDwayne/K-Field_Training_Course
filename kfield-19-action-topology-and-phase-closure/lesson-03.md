# Lesson 03 — Topology through loops and boundary data

**Essential question:** Can a change in local coordinates repair a nonclosing loop?

**Goals:** Multiply quarter-turn phases; transform each link under a declared frame convention; distinguish a local frame from a global loop test.

**Prerequisite bridge.** Lesson 02 kept ordered interval contributions. Here we keep ordered links around a triangle. Addition is replaced by multiplication, but the same discipline applies: retain the inputs as well as the total. We teach the small phase arithmetic explicitly even if Course 17 already introduced it.

## C19.03-E1 — Quarter turns and frames

A phase represents a turn. Use 1 for no turn, i for one quarter-turn, −1 for a half-turn, and −i for three quarter-turns. Multiplication combines turns. Four quarter-turns return to 1, so i²=−1, i³=−i and i⁴=1. These are complex numbers; i is defined by i²=−1. For this course the four-element multiplication cycle suffices. In particular i(−i)=1 and (−i)²=−1. An inverse undoes a turn: i^−1=−i, (−i)^−1=i, and (−1)^−1=−1.

Let vertices be a,b,c. U_ab,U_bc,U_ca are scalar links carrying phase data. Our convention is U'_xy=g_x U_xy g_y^−1, where nonzero frame phases g_x specify local coordinates. Declare this convention before calculating; reversing it changes individual transformed links. The closed product is P=U_ab U_bc U_ca. Substitution gives

P'=g_a U_ab (g_b^−1 g_b) U_bc (g_c^−1 g_c) U_ca g_a^−1=g_a P g_a^−1=P.

Adjacent inverse pairs cancel to 1. The last equality uses commuting scalar phases. For source matrix links, the product is conjugated instead; Lesson 07 explains the trace identity used to obtain a scalar invariant. The entire loop must be retained to see cancellation. An open chain retains different endpoint frames.

Topology concerns global connection and loop/boundary structure. This finite triangle teaches a limited global-versus-local distinction; it is not a classification of every possible space. A boundary condition specifies what must agree or what data are fixed at a boundary. A closure test asks whether the complete loop product equals 1 under the declared contract.

## C19.03-W1 — A loop that stays nonclosing

Take links (i,1,i) in ab,bc,ca order. P=i·1·i=−1. Apply frames (g_a,g_b,g_c)=(−1,i,1). Then U'_ab=(−1)i(−i)=−1; U'_bc=i·1·1=i; U'_ca=1·i·(−1)=−i. Their product is (−1)i(−i)=−1. Local coordinates changed each link but did not make the loop close. The closure residual P−1 is −2 both before and after, dimensionless. Keep the original and transformed links, frames and residual; the residual alone does not reconstruct the links.

## C19.03-P1 — Guided practice

Use links (i,−i,1) and the same frames (−1,i,1). Compute each new link and both loop products.

**Worked answer:** Original P=i(−i)1=1. U'_ab=(−1)i(−i)=−1; U'_bc=i(−i)1=1; U'_ca=1·1·(−1)=−1. Thus the new list is (−1,1,−1), whose product is 1. Record the three frames, their inverses and both link lists. Inverting the transformation, U_xy=g_x^−1 U'_xy g_y, reconstructs the original links.

> **Claim scope.** These synthetic scalar examples prove their own finite identities. S02 M13 reports conjugation of closed source transport, and M15 states a phase condition for every admitted sector. Neither one triangle nor a convenient local frame supplies M15's topology carriers, determinant-line data or admitted-sector list. Those requirements remain explicit. Lesson 06 will teach the stated rational charge contract.

## Diagnostics

1. **C19.03-D1:** Does one closed triangle establish M15 closure in every admitted sector?
2. Find (−i)² and i^−1 using turns.
3. Why does U_ab U_bc not have the same endpoint cancellation as the triangle?
4. If a nonclosing loop becomes 1 in someone's calculation after changing frames, what should you check first?

**Worked answers:** (1) No; the full sector domain and determinant-line inputs have not been checked. (2) Two three-quarter turns total six quarters, equivalent to two quarters, giving −1; the inverse of i is −i. (3) The a and c endpoints remain different: U'_ab U'_bc=g_a(U_ab U_bc)g_c^−1. (4) Check the declared link convention, all inverse phases and all three transformed links. P'=P for these scalar loops, so changing P signals a changed input or arithmetic/convention error.

**Next dependency:** [Lesson 04](lesson-04.md) expands the ledger from three links to six named phase contributions.
