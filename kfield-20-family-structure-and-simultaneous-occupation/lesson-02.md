# Lesson 2 — Uniform and zero-sum sectors

Essential question: How can a class average simplify a list without losing any entry?

Goals: Normalize a class indicator; split a list into mean and detail and reconstruct it; count independent uniform and detail coordinates.

Prerequisite bridge: Lesson 1 supplied nine ordered nodes in each Cᵣ. Now place a number at every node. A vector is this ordered list of numbers. Adding vectors means adding corresponding entries; multiplying by a number scales every entry. These are dimensionless teaching amplitudes, not measured masses or densities. Use two periods: decomposition first, normalization and coordinate counts second.

## C20.02-E1 — Values, length and reversible decomposition

Write δₓ for the list with a 1 at node x and 0 at every other node. It acts like an address marker. Any list f can be written as the sum of its values times their markers. For real lists, the inner product f·g is the sum of entrywise products. The squared norm ||f||² is f·f; the norm is its nonnegative square root. Distinct address markers have inner product 0 and are called orthogonal. Each marker has norm 1.

The class indicator is 1 on its nine nodes and 0 elsewhere. Its squared norm is nine. Multiplying it by 1/3 gives the source's normalized indicator Φᵣ=(1/3)Σₓ∈Cᵣδₓ. Here Σ means “add all the indicated terms.” Its squared norm is 9×(1/3)²=1. Different Φᵣ are orthogonal because their nonzero entries never overlap.

For values f₁,…,f₉ in a class, define the mean m=(f₁+…+f₉)/9. Define details dⱼ=fⱼ−m. Their sum is Σfⱼ−9m=0. The reconstruction rule is fⱼ=m+dⱼ for every j. The mean and the full ordered detail list are both primary coordinates of the representation; keeping only one loses information.

The constant list m on a class equals (3m)Φᵣ, because Φᵣ has entries 1/3. Its coefficient in the normalized basis is therefore 3m, not m. The inner product gives the same result: Φᵣ·f=(Σfⱼ)/3=3m. A zero-sum detail has inner product (Σdⱼ)/3=0 with Φᵣ.

The source calls the class-constant space U_λ: choose three constants, one for each class. It calls the zero-sum space on Cᵣ Wᵣ. A space is a collection of lists closed under adding and scaling. Its dimension counts independent coordinates: choices that can be varied freely. Eight detail entries can be chosen freely; the ninth is forced to be the negative sum of the first eight. Hence dim Wᵣ=8. Across X we have 3+8+8+8=27 independent coordinates. The phrase direct sum means each f has one unique decomposition into these four parts. It does not mean deleting any of them.

## C20.02-W1 — Worked decomposition

Take the synthetic list (1,2,3,4,5,6,7,8,9) on C₀ in lesson 1's order. Its sum is 45, so m=45/9=5. Subtract 5 entry by entry to obtain d=(−4,−3,−2,−1,0,1,2,3,4). Pairing opposite entries verifies Σd=0. The normalized-indicator coefficient is 3×5=15. Thus f=15Φ₀+d on C₀, with zeros outside it.

Reconstruction at the first, middle and last entries gives 5−4=1, 5+0=5 and 5+4=9; the same addition restores all nine. Independently, ||f||²=285; the uniform part contributes 9×25=225, and the detail contributes 16+9+4+1+0+1+4+9+16=60. Because the parts are orthogonal, their squared norms add: 225+60=285.

## C20.02-P1 — Guided practice, with answers

Decompose (9,0,0,0,0,0,0,0,0), retaining order and all entries. Find the coefficient of Φᵣ and reconstruct.

Answer: m=9/9=1; d=(8,−1,−1,−1,−1,−1,−1,−1,−1), whose sum is 8−8=0. The coefficient is 3. At the first node 1+8=9 and at each other node 1−1=0. The norm check is 81=9+72. If a second class is all 2 and a third all −1, their coefficients are 6 and −3, with zero detail in each; keep those zero detail lists too.

> Claim scope: S02#/backbone_sequence/15/definitions supplies Φᵣ, U_λ and Wᵣ. These examples are synthetic finite data. Their residual details are preserved information. No observation is rejected because its deviation from the mean is large. W₀,W₁,W₂ here are class-detail spaces, not the weak gauge carrier W₂ from other courses.

## Diagnostic checks

1. **C20.02-D1:** Is an indicator with amplitude 1/9 normalized?
2. A class mean is −2. What coefficient multiplies Φᵣ?
3. Eight detail entries sum to 7. What is the ninth?
4. If only the details are saved, can you recover the original list uniquely?

Worked answers: (1) No: squared norm 9/81=1/9 and norm 1/3. (2) −6, because −6/3=−2 at each node. (3) −7 to make the sum zero. (4) No: adding any common constant leaves details unchanged. Save the mean or its equivalent coefficient as well.

Next dependency: [Lesson 3](lesson-03.md) uses norms and orthogonal coordinates to check lifted and Fourier representations.
