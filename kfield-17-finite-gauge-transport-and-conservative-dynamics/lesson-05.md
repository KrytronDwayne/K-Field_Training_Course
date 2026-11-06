# Lesson 05 — Norm-preserving time steps

Essential question: Can a finite time update change all the components while preserving their total squared size?

Goals: evaluate a diagonal Cayley step with complex division; verify its hypotheses and adjoint inverse; prove norm conservation in the finite model.

Prerequisite bridge: lessons 01–04 taught adjoints, inverses, ordered multiplication and the difference between a frame change and time evolution. Here ψ_new=Cψ_old describes a specified evolution. Two 55-minute periods: A covers complex division and the worked step; B covers cancellation, practice and failure cases. Each period has 5 retrieval, 20 teaching, 15 practice, 15 diagnostic/repair minutes.

## C17.05-E1 — A rational update

To divide by a nonzero complex number c+di, multiply numerator and denominator by its conjugate c−di. The denominator becomes c²+d², a positive real number. For example (1−2i)/(1+2i)=(1−2i)²/5=(−3−4i)/5. A diagonal matrix is inverted by inverting each diagonal entry, provided no entry is zero. Its determinant, a scalar indicating invertibility here, is the product of those entries. For a general 2 by 2 matrix [[a,b],[c,d]], the determinant is ad−bc; a nonzero determinant permits an inverse.

Let Lhat be a finite square matrix with units TU⁻¹, where TU is our chosen time unit. Let τ_C be real with units TU. Require Lhat†=Lhat (self-adjoint), and require I+iτ_C Lhat to be invertible. The product τ_C Lhat is dimensionless, so adding it to I makes sense. Define

    C = (I−iτ_C Lhat)(I+iτ_C Lhat)⁻¹.

This is a rational or Cayley update. A self-adjoint diagonal matrix has real diagonal entries. Self-adjointness is not the same as unitarity: diag(1,2) is self-adjoint but does not preserve norms when applied directly. It is the Cayley construction from Lhat that will preserve them.

Here is why. Write A=I+iτ_C Lhat and B=I−iτ_C Lhat. For real τ_C and self-adjoint Lhat, A†=B and B†=A. Multiplying their brackets shows AB=BA=I+τ_C² Lhat². The adjoint of a product reverses its order, (PQ)†=Q†P†: transposing interchanges input and output, and conjugation acts on each number. Likewise (A⁻¹)†=(A†)⁻¹, obtained by taking adjoints of AA⁻¹=I. Thus C†=B⁻¹A. The commutation just checked gives

    C†C = B⁻¹ A B A⁻¹ = B⁻¹ B A A⁻¹ = I.

The same calculation gives CC†=I. In finite dimensions, A invertible also makes its adjoint B invertible. Consequently C† is the reverse step, and ‖Cψ‖²=ψ†C†Cψ=ψ†ψ. The expression ψ†ψ means the conjugate row times the original column, exactly the sum of squared moduli from lesson 01. These cancellations supply a proof for the stated finite domain, not just a numerical pattern.

## C17.05-W1 — Two unequal phase changes

Choose Lhat=diag(1,2) TU⁻¹ and τ_C=1 TU. Its diagonal entries are real, hence self-adjoint. A=diag(1+i,1+2i) has nonzero determinant (1+i)(1+2i)=−1+3i. The Cayley factors are (1−i)/(1+i)=−i and (1−2i)/(1+2i)=−3/5−4i/5. Both have squared modulus 1.

Apply C to ψ=(1,2). The result is (−i,−6/5−8i/5). The new squared norm is 1+36/25+64/25=5, equal to 1²+2². The adjoint C†=diag(i,−3/5+4i/5) recovers the input: its first product is 1; its second is (18+32)/25=2 with imaginary cross terms cancelling. Record C and the full output, not only 5.

## C17.05-P1 — A stationary component

Use Lhat=diag(0,2) TU⁻¹, τ_C=1/2 TU and ψ=(1+i,2). Check all hypotheses, calculate Cψ, its squared norm, and its recovery.

Worked answer: Lhat is real diagonal; τ_C is real; A=diag(1,1+i) has determinant 1+i≠0. The dimensionless factors τ_C Lhat are 0 and 1. Thus C=diag(1,−i). The output is (1+i,−2i), with norm squared 1²+1²+4=6. C†=diag(1,i) recovers (1+i,2). The two factor moduli are 1. The zero entry in Lhat causes no singularity in A because A's corresponding entry is 1.

> Claim scope: The Cayley form and self-adjoint condition are reported in S02 M13; the finite cancellation and these synthetic numbers are checked here. τ_C is a time parameter. It is not the Hodge length symbol called tau in the source, nor the archival τ_R time without a supplied conversion. We do not infer an experimental time calibration.

## Diagnostic checks

1. **C17.05-D1:** If scalar Lhat=i/2 TU⁻¹ and τ_C=1 TU, find C. Which hypothesis fails?
2. Why is the denominator nonzero for a real scalar value λ of Lhat and real τ_C?
3. In the practice example, compute C†C and C applied twice.
4. Would replacing the output by its norm permit recovery with C†?

Answers: (1) iτ_C Lhat=−1/2, so C=(3/2)/(1/2)=3; squared norm scales by 9. Lhat†=−i/2≠Lhat. (2) |1+iτ_Cλ|²=1+(τ_Cλ)²>0. (3) C†C=diag(1,i(−i))=I; C²=diag(1,−1). (4) No: the norm discards phases and component amplitudes. The inverse acts on the complete output column.

Next dependency: [lesson 06](lesson-06.md) separates a Euclidean norm from a metric-weighted comparison.
