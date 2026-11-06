# Lesson 02 — Covariant finite differences

Essential question: How does a meaningful difference change when the local coordinate conventions change?

Goals: compute a transported difference; transform a link and both endpoint states; verify the covariance rule with full components.

Prerequisite bridge: lesson 01 taught how U_xy moves a state from y into x and how inverses undo a map. We now subtract only after both terms are expressed in x. Pacing: 5 minutes retrieval, 20 teaching, 15 practice, 15 diagnostics, total 55.

## C17.02-E1 — Compare after transport

Define d_x=ψ_x−U_xyψ_y. This is a finite difference: it compares two states without taking any infinitesimal limit. If a length-divided derivative were wanted, a spacing and its units would need to be supplied; we do not insert one. Our d_x has the same dimensionless units as ψ.

Suppose G_x and G_y are invertible changes of frame at the two sites. A prime marks the new description, not a time derivative. Set ψ′_x=G_xψ_x and ψ′_y=G_yψ_y. The new link must undo the new y convention, apply the old link, and then use the new x convention. Since the rightmost map acts first, this is U′_xy=G_x U_xy G_y⁻¹. Remember the order even when working with numbers that happen to commute.

Substitute these rules into the new difference:

    d′_x = G_x ψ_x − (G_x U_xy G_y⁻¹)(G_y ψ_y)
         = G_x ψ_x − G_x U_xy ψ_y
         = G_x(ψ_x − U_xy ψ_y) = G_x d_x.

The adjacent G_y⁻¹G_y cancels. We regroup products but do not exchange their order. A quantity is covariant when it follows the declared frame-change rule; its components need not stay identical. If G_x is unitary, the squared norm of d_x stays the same even though d_x changes components. That squared norm is an invariant under these frame changes.

The difference is also a reconstruction coordinate. If ψ_y, U_xy, and d_x are retained, then ψ_x=d_x+U_xyψ_y. Thus a nonzero difference carries information about the mismatch. It is not a disposable error term.

## C17.02-W1 — Worked cancellation

Take ψ_x=1, ψ_y=2, U_xy=i. Transport gives 2i, so d_x=1−2i. Change frames with G_x=i and G_y=−1, whose inverse is −1. The new link is i·i·(−1)=1. The states are ψ′_x=i and ψ′_y=−2. Therefore d′_x=i−1(−2)=2+i. Independently, G_x d_x=i(1−2i)=i+2. Both routes agree component by component, and both differences have squared modulus 5.

Reconstruction in the original frame is (1−2i)+i·2=1. In the new frame it is (2+i)+1·(−2)=i. Neither description has been discarded.

## C17.02-P1 — A different frame choice

Use ψ_x=2, ψ_y=1+i, U_xy=−i, G_x=−1 and G_y=i. Compute d_x, U′_xy, the two new states, d′_x, and G_xd_x. Check reconstruction.

Worked answer: U_xyψ_y=1−i, so d_x=2−(1−i)=1+i. Since G_y⁻¹=−i, U′_xy=(−1)(−i)(−i)=1. The transformed states are −2 and i(1+i)=−1+i. Hence d′_x=−2−(−1+i)=−1−i, which equals (−1)(1+i). Reconstruction gives (1+i)+(1−i)=2 and (−1−i)+(−1+i)=−2. The squared modulus of each difference is 2.

> Claim scope: We derived finite covariance from definitions and invertibility. The examples are synthetic. A covariant difference can be nonzero without contradicting covariance. No force law, measured interaction, or continuum equation has been inferred from this identity. Source connection: S02, /backbone_sequence/12, gauge transformation proof; see sources.md.

## Diagnostic checks

1. **C17.02-D1:** Why is ψ_x−ψ_y not our declared comparison? Must d′_x=d_x?
2. In the worked example, what goes wrong if the states change but the old link i is kept?
3. What data are sufficient to reconstruct ψ_x from its difference?
4. Does covariance alone require G_x to preserve norms?

Answers: (1) The terms belong to different frames until y is transported; covariance requires d′_x=G_xd_x, not identical components. (2) The incorrectly computed difference is i−i(−2)=3i, not 2+i. (3) Keep d_x, ψ_y, and U_xy, then add d_x+U_xyψ_y. (4) No. Invertibility suffices for the algebra; unitarity is the additional condition used for norm preservation.

Next dependency: [lesson 03](lesson-03.md) repeats this cancellation along a closed chain of links.
