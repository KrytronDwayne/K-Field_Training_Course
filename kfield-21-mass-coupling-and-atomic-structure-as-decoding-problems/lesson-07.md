# lesson-07: Solver convergence and unresolved information

2 sessions of 55 minutes.

**Essential question:** What can a failed numerical iteration teach us without losing its input?

**Goals**

- Perform two explicit solver updates and retain the full history.
- Explain convergence or divergence using two taught error directions.
- Distinguish numerical convergence, channel closure and physical identification.

## Prerequisite bridge

Use A_small and synthetic y=(2,3,6) from lesson 1. The exact solution c_star=(7/3,10/3) is already known. A sequence is an ordered list indexed n=0,1,2,...; c_n is simply the coefficient pair after n updates.

<a id="C21.07-E1"></a>
## Explanation — C21.07-E1

A solver is a rule for producing successive candidates. Declare c_0=(0,0) and a step parameter t. At every stage compute r_n=y-A_small c_n, then the two normal residual sums g_n=A_small^T r_n, then c_(n+1)=c_n+t g_n. Save n, t, c_n, r_n and g_n together. These are different fields: the normal residual is two sums; the channel residual is three entries.

For t=1/4, the initial normal residual is (8,9). Multiply by 1/4 to get c_1=(2,9/4). Its represented channels are (2,9/4,17/4), so r_1=(0,3/4,7/4). Adding first-plus-third and second-plus-third gives g_1=(7/4,5/2). Multiply that by 1/4 and add to c_1: c_2=(2+7/16,9/4+5/8)=(39/16,23/8). Subtract its channels from y to get (-7/16,1/8,11/16).

Step t=1/4

| n | c_n | r_n | A_small^T r_n |
| --- | --- | --- | --- |
| 0 | (0, 0) | (2, 3, 6) | (8, 9) |
| 1 | (2, 9/4) | (0, 3/4, 7/4) | (7/4, 5/2) |
| 2 | (39/16, 23/8) | (-7/16, 1/8, 11/16) | (1/4, 13/16) |

Step t=1

| n | c_n | r_n | A_small^T r_n |
| --- | --- | --- | --- |
| 0 | (0, 0) | (2, 3, 6) | (8, 9) |
| 1 | (8, 9) | (-6, -6, -11) | (-17, -17) |
| 2 | (-9, -8) | (11, 11, 23) | (34, 34) |

The t=1 branch is a useful comparison, not a discarded run. It first gives c_1=(8,9), so r_1=(2-8,3-9,6-17)=(-6,-6,-11). Thus g_1=(-17,-17), and c_2=(-9,-8). Reconstruction still works: (-9,-8,-17)+(11,11,23)=(2,3,6). The solver has moved away from its target while the retained packet remains exact.

To explain these branches without calculus, define coefficient error e_n=c_n-c_star. Since the exact solution obeys A_small^T y=G c_star with G=[[2,1],[1,2]], subtraction gives e_(n+1)=(I-tG)e_n. The sum direction (1,1) is multiplied by G by 3; the difference direction (1,-1) by 1. Every error (a,b) equals ((a+b)/2)(1,1)+((a-b)/2)(1,-1). Each update multiplies these two parts by 1-3t and 1-t respectively.

If a multiplier has absolute value less than one, repeated multiplication shrinks that component toward zero. For t=1/4, the multipliers are 1/4 and 3/4, so both shrink. For t=1, they are -2 and 0; the nonzero sum component flips sign and doubles each step. In general both shrink when 0<t<2/3. At the boundary t=2/3, the sum component flips without shrinking; at t=0 it does not move. These conclusions are about this explicit solver and matrix, not about all solvers.

Even as c_n approaches c_star, the channel residual approaches (-1/3,-1/3,1/3), not zero. Numerical convergence is reaching the decoder’s coefficients. Channel closure is whether r itself vanishes. Physical identification is whether the model coordinates and source selection rule describe the measured system. They are three distinct claims.

If columns are dependent, the normal matrix may be singular, meaning it has no unique inverse. For example two identical columns produce the same channels for coefficients (1,0) and (0,1). A solver must preserve the free-coordinate ambiguity, use additional declared constraints if supplied, and check compatibility; it must not invent uniqueness.

> Scope: These finite iteration histories are synthetic computations. Divergence exposes parameter dependence; it is not a reason to delete inputs, negative residuals or the failed branch. A scalar norm may index a history but cannot replace any saved coordinate.

<a id="C21.07-W1"></a>
## Worked example — C21.07-W1

For t=1/4, c0=(0,0), r0=(2,3,6); c1=(2,9/4), r1=(0,3/4,7/4); c2=(39/16,23/8), r2=(-7/16,1/8,11/16). Error multipliers 3/4 and 1/4 imply convergence to the previously solved c, whose full r remains nonzero.

<a id="C21.07-P1"></a>
## Guided practice — C21.07-P1

Try the operation before reading the solution. For t=1, c1=(8,9), r1=(-6,-6,-11), c2=(-9,-8), r2=(11,11,23). Error multiplier -2 exposes a divergent branch for these inputs. Preserve this branch and all signed entries. Compare against the exact trace instead of deleting the failed result.

<a id="C21.07-D1"></a>
## Diagnostic checks — C21.07-D1

1. Recompute c_2 and r_2 for t=1/4.
2. Recompute the t=1 branch through its second update.
3. At t=2/3, what happens to the sum-direction error?
4. If g_n=0, must r_n=0 or c_n represent a physical occupied state?

## Worked answers

1. c_2=(39/16,46/16); its third channel is 85/16. Subtract from (32/16,48/16,96/16) to get (-7/16,2/16,11/16).
2. c_1=(8,9), r_1=(-6,-6,-11), g_1=(-17,-17), c_2=(-9,-8), r_2=(11,11,23).
3. The multiplier 1-3(2/3)=-1 flips the sign without shrinking a nonzero component.
4. No. At c_star the two normal sums are zero while r_star=(-1/3,-1/3,1/3). Physical occupied-state selection is a separate, here missing, input.

**Boundary to carry forward:** Convergence of a numerical update is different from channel closure or physical identification. A singular normal matrix requires compatibility/free-coordinate handling; an unstable t does not erase the measurements.

**Next dependency:** [lesson-08](lesson-08.md). Use this lesson’s reconstruction and scope checks there.
