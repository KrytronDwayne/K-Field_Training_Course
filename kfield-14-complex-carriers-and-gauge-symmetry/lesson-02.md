# Lesson 2 — Inner products and unitary changes

Essential question: How do we verify a reversible transformation that mixes complex coordinates?

Goals: Form a conjugate transpose; multiply a 2×2 matrix by a vector and matrix; test unitarity and recover an input.

Prerequisite bridge: Lesson 1 supplies conjugation and bracket expansion. Stack two numbers into a column v=(v₁,v₂)ᵀ. T means transpose: interchange rows and columns. Use two periods, first for matrix operations and then for mixing.

## C14.02-E1 — Rules for combining coordinates

A matrix is a rectangular array. In A=[[a,b],[c,d]], each row supplies one output coordinate: Av=(av₁+bv₂,cv₁+dv₂)ᵀ. Matrix multiplication AB applies B first, then A. Each entry is a row-column sum; for example (AB)₁₂=aB₁₂+bB₂₂. Thus [[1,2],[0,1]][[1,0],[3,1]]=[[7,2],[3,1]]. Identity I₂=[[1,0],[0,1]] leaves inputs unchanged. In diag(a,d), off-diagonal entries are zero.

The dagger † means conjugate transpose: [[a,b],[c,d]]†=[[ā,c̄],[b̄,d̄]]. The complex inner product is ⟨v,w⟩=v†w=v̄₁w₁+v̄₂w₂. In particular ||v||²=⟨v,v⟩=|v₁|²+|v₂|² is squared norm. It is real and nonnegative, although a general inner product may be complex. We conjugate the first argument.

A square matrix U is unitary when U†U=I. This tests every possible input. Indeed ||Uv||²=(Uv)†Uv=v†U†Uv=v†v. The identity (Uv)†=v†U† follows by conjugating the products and interchanging rows and columns. A unitary square matrix has inverse U†, giving v=U†(Uv). Our examples also multiply in both orders to check the inverse. General matrix multiplication is order-sensitive.

## C14.02-W1 — Worked example

For U=diag(i,−i), U†=diag(−i,i). Hence U†U=diag((−i)i,i(−i))=I₂; UU† is also I₂. On (1+i,2−i), output is (−1+i,−1−2i). Squared norm before and after is 2+5=7. Applying U† gives (−i)(−1+i)=1+i and i(−1−2i)=2−i. All components return.

## C14.02-P1 — Answered practice with mixing

Let V=(1/√2)[[1,i],[i,1]]. The scalar outside multiplies every entry. Its dagger is (1/√2)[[1,−i],[−i,1]]. Multiply, retaining the scalar factor 1/2:

V†V=(1/2)[[1+(−i)i,i−i],[−i+i,(−i)i+1]]=(1/2)[[2,0],[0,2]]=I₂.

The same calculation gives VV†=I₂. On v=(1,i), output is ((1+i²)/√2,(i+i)/√2)=(0,√2 i). Squared norm is 2 before and after. Recovery gives ((−i)(√2 i)/√2,(√2 i)/√2)=(1,i). On (2,0), output is (√2,√2 i), squared norm 2+2=4. Applying V† yields ((√2+(−i)(√2 i))/√2,((−i)√2+√2 i)/√2)=(2,0). Cancellation in an output slot has not destroyed the input information.

> Claim scope: These are synthetic, dimensionless vectors. A single preserved vector length is insufficient to prove unitarity. U†U=I supplies the general check; retain the transformation to reverse it.

## Diagnostics — C14.02-D1

1. Find [[1,i],[2,−i]]†.
2. Compute ⟨(1,i),(i,1)⟩ and ||(1,i)||².
3. Why does VᵀV fail as the unitarity test? Multiply it.
4. Is diag(1,2) unitary? Give matrix and vector checks.

Worked answers: (1) [[1,2],[−i,i]]. (2) i+(−i)·1=0; the squared norm is 1+(−i)i=2. (3) Vᵀ=V, so VᵀV=(1/2)[[0,2i],[2i,0]]=[[0,i],[i,0]], not I₂. Conjugation matters. (4) Its dagger-product is diag(1,4); it changes (0,1) to (0,2), changing squared norm from 1 to 4. Invertibility alone is insufficient.

Next dependency: [Lesson 3](lesson-03.md) uses an explicitly ordered five-coordinate carrier.
