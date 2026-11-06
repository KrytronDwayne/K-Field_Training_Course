# Lesson 08 — Conservation and continuum scope

Essential question: Exactly what is conserved by our finite evolution, and what remains a separate question?

Goals: compute norm and Lhat quadratic value before and after evolution; recover full states and retain comparison remainders; distinguish finite identities, source bounds and infinite comparison claims.

Prerequisite bridge: lesson 05 proved a finite Cayley step unitary; lesson 07 separated a source bound from its missing replay inputs. We now identify the quantities we can check completely. Pacing: 5 retrieval, 20 teaching, 15 practice, 15 diagnostic/repair minutes, total 55. The infinite-series paragraph is recognition-only.

## C17.08-E1 — Conservation needs a specified quantity

To say a quantity is conserved means it has the same value before and after the stated update. Unitarity conserves N=ψ†ψ. It does not require each complex component to stay fixed. For a self-adjoint Lhat also define Q_L=ψ†Lhatψ, with units TU⁻¹ for our dimensionless states. For diagonal Lhat with entries λ₁,λ₂, multiply the column by Lhat and then by ψ†: Q_L=λ₁|z₁|²+λ₂|z₂|². We call this the unnormalized Lhat quadratic value. The normalized expectation is Q_L/N when N>0. These must not be confused: for a state of squared norm 5, the number 9 is a numerator, not the normalized expectation 9/5.

The Cayley C commutes with Lhat because I±iτ_C Lhat do, and their invertible factors retain that commutation. To see the last step, if ALhat=Lhat A, multiply by A⁻¹ on both sides to obtain Lhat A⁻¹=A⁻¹Lhat. Therefore

    (Cψ)†Lhat(Cψ) = ψ† C† Lhat C ψ
                  = ψ† C† C Lhat ψ = ψ† Lhat ψ.

This is a conservation law for this update and this matrix. For another observable represented by a matrix A_obs, unitarity alone only gives ψ†C†A_obs Cψ; it equals the old value if the needed commutation holds. The proof does not claim conservation of every possible measurement.

Every finite number of steps remains reversible with the corresponding inverse steps. A continuum limit is a different assertion: it compares a sequence of finer models or smaller time steps with a specified limiting object. Such a claim requires a comparison rule, a domain where the limiting operation is defined, and control of the entire limiting process. Exact finite conservation is useful evidence about a construction, but does not supply these missing definitions by itself.

## C17.08-W1 — Check two quantities

Return to Lhat=diag(1,2) TU⁻¹, τ_C=1 TU and ψ=(1,2). The step gives ψ_new=(−i,−6/5−8i/5). Its squared component sizes are 1 and (36+64)/25=4. Consequently N=5 both before and after, and Q_L=1·1+2·4=9 TU⁻¹ both before and after. The normalized expectation is 9/5 TU⁻¹ in both states. The component phases changed and are retained in ψ_new.

If we compare the new state with the deliberately simple reference ψ_ref=ψ, the full remainder is r=ψ_new−ψ=(−1−i,−16/5−8i/5). It is nonzero even though the two conserved scalars agree. Retain ψ_ref and r, giving ψ_new=ψ_ref+r. Do not replace r by a score or call it a violated conservation law.

## C17.08-P1 — Two steps and two recoveries

Use the practice Lhat=diag(0,2) TU⁻¹, τ_C=1/2 TU and ψ=(1+i,2). Find N and Q_L initially, after one step and after two. Compute the normalized expectation and explain how to recover the original state.

Worked answer: C=diag(1,−i) gives (1+i,−2i), then (1+i,−2). In all three states component squared sizes are 2 and 4, so N=6 and Q_L=0·2+2·4=8 TU⁻¹. The normalized expectation is 8/6=4/3 TU⁻¹. Applying C†=diag(1,i) twice reverses the second component −2→−2i→2. The one-step remainder against the initial reference is (0,−2−2i), retained with that reference. These finite computations supply no unprovided continuum operator.

> Claim scope: The exact finite conservation statements follow from our hypotheses and calculations. S02 M13 separately reports finite compiler bounds and a thermal-detail convergence statement. Its optional infinite-depth domain comparison and continuum Yang–Mills comparison remain separate source categories. No empirical measurements or proposed physical mechanism are established by the teaching numbers.

Recognition-only extension: S02 writes a thermal-detail series with terms 8^n exp(−β_T c_*2^n), n=0,1,2,…, with positive coefficients. Here β_T is a thermal parameter, distinct from lesson 04's action coefficient, and β_T c_* must be dimensionless in this normalized expression. The exponential exp and natural logarithm ln are inverse functions; the only fact used here is exp(ln16)=16. If the synthetic product β_T c_*=ln16, each term is 8^n/16^(2^n). At n=0,1,2 the terms are 1/16, 8/256=1/32, and 64/65536=1/1024. The three-term sum is 97/1024. A partial sum retains an uncomputed tail T: full sum =97/1024+T, if the series converges. We do not treat T as zero or assign an infinite operator proof from three terms. No calculus, logarithm computation or convergence proof is assessed.

## Diagnostic checks

1. **C17.08-D1:** Do those three thermal terms certify the source's infinite comparison? Separate the three evidence layers.
2. Is Q_L=9 TU⁻¹ the normalized expectation for the worked state?
3. Could a nonzero state remainder coexist with exactly conserved norm?
4. Does C†C=I alone prove conservation of ψ†A_obsψ for every A_obs?

Answers: (1) No. Our finite identities are derived; the archival certificate and convergence claims are source-reported; optional infinite-domain/continuum comparisons require their own supplied objects and proofs. (2) No: divide by N=5 to get 9/5 TU⁻¹. (3) Yes, the worked remainder explicitly does. (4) No; one must check C†A_obs C=A_obs (commutation with a unitary C is sufficient). A norm check cannot replace an observable-specific check.

Next dependency: [capstone](capstone.md) joins the finite operations and exact source reading into one retained model dossier.
