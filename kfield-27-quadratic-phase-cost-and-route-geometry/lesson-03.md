# Lesson 3 — Pullbacks and coordinate changes

**Essential question:** How do two coordinate descriptions give the same scalar cost?

**Goals:** Multiply and transpose small matrices; calculate all four entries of a pullback; reconstruct velocities and state the source replay boundary.

**Bridge:** Lesson 2 substituted a ruler map into a quadratic form. Now the map converts dimensionless coordinates u to a displacement z=x−O_K. Keep O_K fixed. Synthetic B maps dimensionless columns to lengths, and z=Bu/2. B is invertible, meaning each z has exactly one u. This classroom B is not a replacement for the locked, left-handed, three-dimensional Cell3 basis.

Two 55-minute sessions: first matrix multiplication and substitution, then inverse reconstruction and source reading. Per session: 5 retrieval, 20 teaching/example, 15 practice, 15 diagnostics/repair.

## C27.03-E1 — Multiplication order carries meaning

To find entry (i,j) of a matrix product PQ, multiply row i of P against column j of Q and add. For example, [[2,1],[1,2]] [[2,0],[0,1]] has top-right entry 2·0+1·1=1 and bottom-left entry 1·2+2·0=2. These entries differ: you cannot generally swap matrix order. Transposition exchanges rows and columns. The transpose of a product reverses order, (PQ)ᵀ=QᵀPᵀ, as you can check by writing matching entries.

With a fixed B and origin, velocity v=B u-dot/2. Here u-dot is coordinate change per unit time. Substitution gives

vᵀG_phase v = (u-dot)ᵀ [BᵀG_phase B/4] u-dot.

Both copies of v contribute a factor 1/2, producing 1/4. The bracketed matrix is called a **pullback**: it expresses the same cost using input coordinates u. Write W_qpc=BᵀG_phase B/4. This specific identity is source-grounded in S02's typed conventions and KFM-X044. Our numerical demonstration uses synthetic G in place of the unprovided locked source matrix.

Under our classroom typing B has units L, G has units L⁻², and W is dimensionless. Coordinate rates have units τ⁻¹, so either calculation has units τ⁻². The geometric Gram matrix M_cell=BᵀB instead measures length products and has units L² under this typing. Its inverse R_cell has units L⁻². Similar shape or units do not make R_cell and G_phase identical. G_eff and distance forms Q, Q_g, Q_nu are also separately defined source objects; none is an alias supplied for G_phase in this course.

## C27.03-W1 — Check every entry

Use B=[[2,0],[0,1]]L and G=[[2,1],[1,2]]L⁻². First

GB = [[4,1],[2,2]]L⁻¹.

Then Bᵀ(GB)=[[8,2],[2,2]], so W=[[2,1/2],[1/2,1/2]]. The top-right and bottom-left entries are both 1/2; omitting them would destroy equality. For u-dot=(1,2)/τ, v=(1,1)L/τ. The physical calculation is 2+2+2=6/τ². The coordinate calculation is 2·1²+2·(1/2)·1·2+(1/2)·2²=2+2+2=6/τ².

For this diagonal B, undoing B means dividing the first component by 2L and the second by L. Thus B⁻¹=diag(1/2,1)L⁻¹, and u-dot=2B⁻¹v. Define T_B=2B⁻¹=diag(1,2)L⁻¹. The reverse congruence can also be checked entry by entry:

W T_B = [[2,1],[1/2,1]]L⁻¹;

T_Bᵀ W T_B = [[2,1],[1,2]]L⁻² = G.

This is a reversible change of description, not a newly discovered force law.

## C27.03-P1 — Practice and worked answers

**P1a — Forward congruence from blank paper.** With the supplied B and G, independently compute GB and all four entries of Bᵀ(GB)/4. **Answer:** GB entries are 2·2+1·0=4, 2·0+1·1=1, 1·2+2·0=2, 1·0+2·1=2, in L⁻¹. Left multiplication by Bᵀ gives entries 2·4+0·2=8, 2·1+0·2=2, 0·4+1·2=2, 0·1+1·2=2. Divide all four by 4 to obtain W=[[2,1/2],[1/2,1/2]], dimensionless. The two off-diagonal terms must both survive.

Use u-dot=(2,−2)/τ. Compute v and both scalar costs, reconstruct u-dot, and state what happens if the factor 1/4 is omitted. Separately multiply T_BᵀWT_B yourself.

**Answer:** v=(2,−1)L/τ. Physical cost=2·4+2·2·(−1)+2·1=8−4+2=6/τ². Coordinate cost=2·4+1·2·(−2)+(1/2)·4=8−4+2=6/τ². Recovery gives (v_x/L,2v_y/L)=(2,−2)/τ. Without 1/4, the coordinate matrix is four times W and predicts 24/τ² for the unchanged u-dot. Reverse congruence gives G as shown above. Save both signed vectors and their explicit map; the scalar alone cannot reconstruct them.

> **Source scope card:** S02 /branch_proofs/12 reports “closed_exact_QPC_linear_algebra.” Its formula KFM-F039 states W_qpc=CᵀC as well as the pullback. C here is a source factor matrix, not the time-integrated cost J. S03 /findings/7 says the locked G_phase, C and complete W_qpc are missing replay objects and stores a nonzero reconstruction coordinate. A spectral-analysis decimal G_phase is not automatically the locked route G_phase. Before source replay, pin these matrices, their ordered basis, units, precision and bridge to the route certificate. The synthetic matrices above provide none of those missing source values. Retain the exact source claim as attributed and its unavailable body as VERIFIED_NOT_LOADED, rather than asserting a new numerical replay [sources.md].

## C27.03-D1 — Diagnostic checks

1. Why is there a 1/4 rather than a 1/2?
2. What would dropping W's cross term do to the worked cost?
3. Does BᵀGB/4 equal BGBᵀ/4 for every B?
4. Why does verifying this congruence not establish new dynamics?

**Answers:** (1) The two velocity factors each contribute 1/2. (2) It would give 4/τ² instead of 6/τ² for u-dot=(1,2)/τ. (3) No; order follows the coordinate map. The diagonal example happens to have B=Bᵀ, which is not a general rule. (4) Equality follows from substitution; it says two descriptions agree, not how an apparatus exchanges energy or accelerates.

**Next dependency:** [Lesson 4](lesson-04.md) accumulates the scalar rate while retaining the full path ledger.
