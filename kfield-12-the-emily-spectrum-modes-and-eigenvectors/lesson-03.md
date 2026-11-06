# Lesson 03 · The three-node path spectrum

**Essential question:** Can we derive and compare all the modes of the open three-node path?

**Goals:** Derive all three eigenvalues using component equations; verify three eigenpairs; normalize modes and check their pairwise dot products.

**Prerequisite bridge.** Use A(a,b,c)=(b,a+c,b) and Av=λv from Lessons 01–02. Recall that √2 is positive and squares to 2. This lesson takes two periods: first derive and verify, then learn length and orthogonality.

## C12.03-E1 · Solve the component equations

An eigenpair must satisfy b=λa, a+c=λb, and b=λc. If λ=0, the first equation gives b=0 and the second gives c=−a. A nonzero input requires a≠0, giving multiples of (1,0,−1).

If λ≠0, the first and third equations imply a=c: divide λa=λc by the nonzero λ. Then the middle equation becomes 2a=λb=λ²a. Here a cannot be zero, since a=0 would force b=c=0. Dividing by a gives λ²=2, so λ=√2 or −√2. Taking a=1 produces (1,√2,1) or (1,−√2,1). These cases cover all possibilities, so no other eigenvalue exists. The list of eigenvalues, including how many independent modes share each value, is the **spectrum**.

To compare sizes, define the dot product x·y as the sum of matching-entry products. Thus (a,b,c)·(d,e,f)=ad+be+cf. The squared length of x is x·x; its length or norm is √(x·x). It is positive for a nonzero vector. Dividing every entry by that length produces a **normalized** vector of length 1. Two vectors are **orthogonal** when their dot product is zero. Here orthogonality is a precise algebraic test, so no spatial drawing is required. A list of mutually orthogonal unit vectors is **orthonormal**.

## C12.03-W1 / C12-EIG-EX1 · Verify every row and length

Let r=√2 for this calculation, so r²=2.

| Mode | Row outputs Av | λv | Squared length |
|---|---|---|---|
| v+=(1,r,1) | (r,1+1,r)=(r,2,r) | r(1,r,1)=(r,2,r) | 1+2+1=4 |
| v0=(1,0,−1) | (0,1−1,0)=(0,0,0) | 0(1,0,−1)=(0,0,0) | 1+0+1=2 |
| v−=(1,−r,1) | (−r,1+1,−r)=(−r,2,−r) | −r(1,−r,1)=(−r,2,−r) | 1+2+1=4 |

The lengths are 2,r,2. Our fixed mode order is (+,0,−), and the normalized modes are

u+=(1/2,r/2,1/2), u0=(1/r,0,−1/r), u−=(1/2,−r/2,1/2).

All have squared length 1. Their mutual dot products are u+·u−=(1−2+1)/4=0, u+·u0=(1−1)/(2r)=0, and u0·u−=(1−1)/(2r)=0. Scaling preserved the eigenvalues, so Au+=r u+, Au0=0, Au−=−r u−.

## C12.03-P1 / C12-EIG-P1 · Guided practice and answers

Verify A(2,0,−2)=0 and explain why the input remains an eigenvector. Its row outputs are (0,2−2,0)=0, and it is twice v0 with nonzero scale 2. Normalize (2,2r,2): its squared length is 4+8+4=16, length 4, and division by 4 gives u+. Check Au− directly: the outputs are (−r/2,1,−r/2)=−r(1/2,−r/2,1/2). Finally compute u+·u−=0 and u0·u−=0 using the fractions above.

Practice the derivation without looking: separate λ=0 from λ≠0, then explain why dividing by a in the second case is legal. Answer: a=0 would make all entries zero, violating the eigenvector condition. This is why the two-case argument does not miss a solution.

> **Claim scope.** This direct derivation supplies the finite path proof used in S02 /backbone_sequence/7/proof/2. No general spectral theorem is assumed or assessed. The symbols + and − label our chosen modes; they do not yet describe inversion parity, which is a different operation.

## C12.03-D1 / C12-EIG-D1 · Diagnostic checks

1. Reject (1,1,1) as an eigenvector using its three outputs.
2. Derive λ²=2 in the nonzero-λ case; state why the division is allowed.
3. Find the norm of (1,−√2,1), normalize it, and verify its middle output.
4. Calculate all three mutual dot products of u+,u0,u−. What does orthonormal mean?

**Worked answers.** 1. A(1,1,1)=(1,2,1), requiring conflicting multipliers 1 and 2. 2. Endpoints agree, b=λa, so 2a=λ²a; a≠0 as shown above. 3. Norm √4=2; u−=(1/2,−√2/2,1/2), whose middle output is 1=−√2·(−√2/2). 4. The products are (1−2+1)/4=0 and (1−1)/(2√2)=0 twice. Orthonormal means mutual zero dot products and each length 1.

**Next dependency:** [Lesson 04](lesson-04.md) combines these three one-dimensional choices into patterns on 27 nodes.
