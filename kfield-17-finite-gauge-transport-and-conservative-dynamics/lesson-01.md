# Lesson 01 — Link transport between local frames

Essential question: How can we compare states described in different local coordinate frames?

Goals: apply a complex link in its declared direction; recover a state using the inverse link; check its squared norm.

Prerequisite bridge: courses 07 and 14 motivate coordinates and finite maps. Here we rebuild the specific operations needed: signed multiplication, ordered pairs, and undoing a map. No prior matrix or complex-number course is assumed. Pacing: one 55-minute period, with 5 minutes retrieval, 20 teaching, 15 practice, and 15 diagnostics and repair.

## C17.01-E1 — States and maps

A frame is a convention for recording components. Two people can describe the same arrow using different coordinate axes. A state at a site is a list of numbers in that site's frame. The site labels x and y identify places in our model; they are not numerical coordinates to multiply. A link U_xy maps a state FROM y TO x. Read the second subscript as the input and the first as the output. Transport first makes two states comparable in one frame.

We use complex numbers to give a small, exact model of a rotating component. Define i by i²=−1. Write a+bi as the pair (a,b), with a the real part and b the imaginary part. Distribute multiplication exactly as for brackets: (a+bi)(c+di)=(ac−bd)+(ad+bc)i. Thus i(a+bi)=−b+ai, a quarter-turn of the pair. The conjugate of a+bi is a−bi; its squared modulus is (a−bi)(a+bi)=a²+b². Squared modulus measures size while retaining phase separately in the original number.

A column state ψ=(z₁,z₂) has squared norm ‖ψ‖²=|z₁|²+|z₂|². All state components and links in our teaching examples are dimensionless. A matrix is a rectangular table defining a map. For a 2 by 2 matrix [[a,b],[c,d]], its action on (u,v) is (au+bv,cu+dv): multiply each row by the column and add. The diagonal map diag(a,d) is [[a,0],[0,d]] and acts separately on the two components. I=diag(1,1) leaves a state unchanged.

Transpose means exchange rows and columns. The adjoint U† means transpose AND conjugate every entry. An inverse U⁻¹ undoes the map: U⁻¹U=UU⁻¹=I. A map is unitary when U†U=UU†=I; for these maps U⁻¹=U†. In the one-number case the adjoint is just complex conjugation. The link in the reverse direction is U_yx=U_xy† when the link is unitary. A frame change re-expresses a state; it is not automatically an evolution of that state in time.

## C17.01-W1 — Worked transport and recovery

Let U_xy=i and ψ_y=2. Multiplication gives the transported state 2i in x. Its squared modulus is 0²+2²=4, the same as 2². To return, multiply by −i: (−i)(2i)=−2i²=2. The inverse has the opposite direction.

Now let U_xy=diag(i,−i) and ψ_y=(1,2). Row multiplication gives (i,−2i). The input squared norm is 1+4=5; the output gives |i|²+|−2i|²=1+4=5. The adjoint is diag(−i,i), and it returns ((−i)i,i(−2i))=(1,2). Keep both complex components; recording only 5 would lose the state.

## C17.01-P1 — Practice, then compare

1. Transport ψ_y=1+i with U_xy=−i. Find the inverse and check size and recovery.
2. Apply diag(−1,i) to (2,1). Check the squared norm and recover the input.

Worked answers: −i(1+i)=−i−i²=1−i. The inverse is i, and i(1−i)=1+i. Both squared moduli are 2. For the matrix, the output is (−2,i), with squared norm 4+1=5. The inverse diag(−1,−i) gives (2,1).

> Claim scope: These are explicitly synthetic finite states, not measured fields. Unitarity and recovery are directly checked algebraic properties. Source M13 uses site-indexed group links; our scalar and two-component cases teach the operations without claiming to reproduce its full carrier. The source carrier uses color-first C₃ direct-sum W₂; a different order needs an explicit permutation.

## Diagnostic checks

1. **C17.01-D1:** May U_xy and U_yx be exchanged without changing a calculation? Explain with i.
2. Compute (1+i)(1−i), and explain why the answer is real.
3. Is multiplication by 2 unitary? Is it invertible?
4. What information is lost if (i,−2i) is replaced by its squared norm alone?

Answers: (1) No. U_xy=i maps y to x; U_yx=−i maps x to y and has the opposite quarter-turn. (2) 1−i²=2; conjugate cross terms cancel. (3) It is invertible with inverse 1/2, but |2z|²=4|z|², so it is not unitary. (4) Component identities, signs and phases are lost; many different states have squared norm 5. Keep the state alongside the summary.

Next dependency: [lesson 02](lesson-02.md) uses link direction and inverses to form a difference in one frame.
