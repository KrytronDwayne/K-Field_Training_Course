# Lesson 7 — Family labels and numerical properties

Essential question: Which numerical information is still needed after the family carrier is specified?

Goals: Distinguish a family-label construction from supplied numerical coefficients; solve and reconstruct a two-block scalar system; preserve singular branches and all eliminated coordinates.

Prerequisite bridge: Lessons 3–6 taught coordinates, matrix operations, rank and source status. Here we use ordinary substitution to learn the source's Schur interface. Use three periods: numerical-input scope; elimination and reconstruction; singular cases and synthesis.

## C20.07-E1 — Labels are addresses, not numerical properties

The label r=0,1,2 tells us where a family coordinate belongs. It does not give that family's mass, a matrix entry coupling it to another family, or an experimentally determined mixing value. Mixing here means that a chosen coordinate state can have components along more than one family address. A matrix describes such relations once its entries and interpretation are supplied. A Yukawa matrix is a matrix of coupling coefficients used in the reference particle-theory language; no numerical physical Yukawa matrix is derived by our finite basis calculation.

The source's Weyl formula represents a given 3-by-3 Y by nine coefficients. For example both Y=I and Y=2I have the same three row labels and the same Weyl basis, but their y₀₀ values differ. Thus carrier labels and a basis cannot by themselves select numerical coefficients. Physical masses require additional physical relations and inputs beyond merely writing Y. This course assigns no mass unit to its dimensionless synthetic entries.

| Quantity | What is supplied here | What remains outside this check |
|---|---|---|
| Family addresses | Three λ classes, dimension 3 | Physical-carrier selection proof body |
| Projector count | Conditional rank 48 and source occupation record | New measured population or density |
| Weyl coordinates | All nine coefficients for explicitly supplied synthetic Y | Selected physical Y and its numerical coefficients |
| Masses and mixing values | No numerical physical values in the M16 material used here | Numerical physical inputs or derivation tying them to states |
| Block-system solution | Exact values for supplied synthetic K and s | Identification of that K,s as a physical experiment |

This is a scope statement about the retrieved M16 material, not a claim that no other archive document contains numerical properties.

## C20.S02-E1 — Schur elimination from substitution

Write two coupled equations Au+Bw=s_U and Cu+Ew=s_W. In the core examples A,B,C,E are ordinary numbers, u,w are unknown numbers and s_U,s_W are supplied numbers. The matrix K=[[A,B],[C,E]] records the two equations. These block letters are local to this lesson: B is not Cell3's basis or a Weyl B_ab, E is not the class-mean map, and C is not a lambda class. All values in the examples are dimensionless.

If E≠0, solve the second equation for w=(s_W−Cu)/E. Substitute into the first:

Au+B(s_W−Cu)/E=s_U,

so (A−BC/E)u=s_U−Bs_W/E. Name the reduced coefficient S=A−BC/E the Schur complement and the reduced source r=s_U−Bs_W/E. If S≠0 as well, u=r/S, then reconstruct w from the saved formula. Each inverse has its own condition: E≠0 permits elimination; S≠0 permits unique solution of the reduced equation.

For a 2-by-2 matrix, define its determinant det K=AE−BC. It is nonzero exactly when the two equations have a unique solution for every supplied right-hand side. When E≠0, ES=E(A−BC/E)=AE−BC, giving the source identity det K=(det E)(det S) in this scalar example. For larger blocks the inverses are matrix inverses, and factor order must be retained: S=A−BE⁻¹C and r=s_U−BE⁻¹s_W. That larger-block notation is recognition-only; the core tasks need only the substitution just taught.

## C20.07-W1 / C20.S02-W1 — Worked reconstruction

Use K=[[2,1],[1,3]] and s=(5,7). The equations are 2u+w=5 and u+3w=7. E=3 is nonzero, so w=(7−u)/3. Substitution gives 2u+(7−u)/3=5. Multiply by 3: 6u+7−u=15, hence 5u=8 and u=8/5.

In Schur notation S=2−1/3=5/3 and r=5−7/3=8/3. Then r/S=(8/3)/(5/3)=8/5, agreeing with direct substitution. Reconstruct w=(7−8/5)/3=(27/5)/3=9/5. Check BOTH original equations: 16/5+9/5=5 and 8/5+27/5=7. The determinant check is 2×3−1×1=5=3×(5/3). Saving only u would discard w; retain K, s, u and w, and the two residuals Au+Bw−s_U and Cu+Ew−s_W, both zero here.

## C20.07-P1 / C20.S02-P1 — Guided practice and worked answers

Use K=[[3,1],[2,2]], s=(7,8). Then solve the separate E=0 example K=[[1,1],[1,0]], s=(3,1) directly from its original equations.

First answer: E=2; S=3−(1×2)/2=2; r=7−8/2=3. Thus u=3/2 and w=(8−2×3/2)/2=5/2. Original equations give 3×3/2+5/2=14/2=7 and 2×3/2+2×5/2=3+5=8. The determinant is 6−2=4=2×2. Both equation residuals are zero and both unknowns are retained.

Second answer: the equations are u+w=3 and u=1. Thus u=1,w=2. E=0 makes the E-inverse formula unavailable, but det K=−1≠0. Therefore the full system is uniquely solvable. A singular chosen block is not automatically a singular full matrix.

## Keeping every singular branch

If E≠0 but S=0, the reduced equation is 0u=r. If r≠0 it is inconsistent; retain that incompatibility rather than produce a number. If r=0, u remains free, and each allowed u has w=(s_W−Cu)/E. For example K=[[1,1],[1,1]], s=(2,2) gives E=1, S=0, r=0. Every pair (t,2−t) solves both equations. Changing s to (2,3) gives r=−1 and incompatible equations u+w=2 and u+w=3. A zero inverse must never be inserted to “solve” either branch. With E=0, return to the original equations as in the practice example; they may have one solution, many, or none.

> Claim scope: S02#/backbone_sequence/15/schur_interface supplies the block formulas, and /weyl_basis supplies coordinate extraction. Our scalar examples are synthetic and freshly checked. The source occupation claim and AUD-007 conflict remain as in lesson 6. Neither choosing a basis nor eliminating a variable selects physical masses, mixing coordinates or the occupied carrier. Reconstructing w and retaining compatibility conditions preserves information through the calculation.

## Diagnostic checks

1. **C20.07-D1:** Which physical masses or mixing numbers were supplied by the three-label count?
2. **C20.S02-D1:** May you use E⁻¹ when E=0? Does E≠0 guarantee S⁻¹ exists?
3. What is lost if only u is retained after solving the worked example?
4. For K=[[1,1],[1,1]], compare right-hand sides (2,2) and (2,3).

Worked answers: (1) None; three labels and a coordinate basis do not choose numerical physical inputs. (2) No and no. E and S each require their own nonzero test in scalar examples. (3) The second state coordinate w=9/5 and the immediate ability to check the full state; save the reconstruction inputs and w explicitly. (4) The first gives all (t,2−t), with t retained as free information. The second is incompatible because one sum cannot equal both 2 and 3. Keep that incompatible branch as a reported result.

Next dependency: [Capstone](capstone.md) combines class counts, retained detail, finite lifts, trace coordinates, typed projector accounting and source-status tracing.
