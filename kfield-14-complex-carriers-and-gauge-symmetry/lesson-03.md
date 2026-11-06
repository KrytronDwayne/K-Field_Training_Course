# Lesson 3 — The ordered three-plus-two carrier

Essential question: What must accompany a tuple so its meaning survives a change of order?

Goals: Write the color-first carrier; split and reconstruct it with projectors; permute coordinates and operators consistently.

Prerequisite bridge: Lesson 2 taught columns, matrices, and inverse changes. Five slots use the same multiplication rule. This lesson takes one period.

## C14.03-E1 — Slots have types

A carrier is a space on which transformations act. Here H=C₃⊕W₂: C₃ is a three-dimensional complex color block and W₂ a two-dimensional complex weak block. Names identify source roles, not visible paint colors or measurements. The direct sum ⊕ keeps both blocks separately identifiable. Store h=(c₁,c₂,c₃,w₁,w₂)ᵀ. Example entries are dimensionless.

P_c=diag(1,1,1,0,0) projects onto the color block in its original slots. P_w=I₅−P_c=diag(0,0,0,1,1) selects the weak block. Diagonal multiplication gives P_cP_w=0, P_c²=P_c and P_w²=P_w. Each projection loses the other block; together they reconstruct h=P_ch+P_wh. The 0 in the matrix equation means the zero matrix.

M10 displays a weak-first tuple although the governing convention and correction require color-first. Reconcile it with the actual permutation P below, whose rows select old coordinates:

```text
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
1 0 0 0 0
0 1 0 0 0
```

P(w₁,w₂,c₁,c₂,c₃)ᵀ=(c₁,c₂,c₃,w₁,w₂)ᵀ. Its inverse is Pᵀ: each slot returns, so PᵀP=PPᵀ=I₅. The zero-based output indices are [2,3,4,0,1]; counting slots from one gives [3,4,5,1,2].

Operators must move too. If old output is A_old h_old, new output is P A_old Pᵀ h_new. The rightmost factor first restores the old input order. Thus A_new=P A_old Pᵀ. The integer phase weights diag(3,3,−2,−2,−2) become Q_charge=diag(−2,−2,−2,3,3). This local symbol denotes a charge operator, not a distance metric Q. A phase z acts as diag(z⁻²,z⁻²,z⁻²,z³,z³); Lesson 4 explains the weights.

## C14.03-W1 — Worked example

The weak-first tuple (1,2,3,4,5) becomes h=(3,4,5,1,2). Its projections are (3,4,5,0,0) and (0,0,0,1,2), whose sum is h. Pᵀ restores (1,2,3,4,5). Nothing changed except each entry's slot. The charge list becomes (−2,−2,−2,3,3).

## C14.03-P1 — Answered practice

Convert (i,−1,2,0,1+i) from weak-first to color-first and retain both projections. Answer: h=(2,0,1+i,i,−1); P_ch=(2,0,1+i,0,0); P_wh=(0,0,0,i,−1). Their sum reconstructs h. Verify the charge change by applying Pᵀ to an arbitrary h, multiplying old first-two slots by 3 and old last-three by −2, then applying P. Output is (−2c₁,−2c₂,−2c₃,3w₁,3w₂), proving P A_old Pᵀ=Q_charge on every input.

> Claim scope: S02 /typed_conventions/carrier_order and /backbone_sequence/9 give the source convention and displayed M10; S03 /findings/3 (AUD-004) gives the correction. Tuple calculations are fresh finite verification. Role labels alone supply no physical interaction law.

## Diagnostics — C14.03-D1

1. Why is merely relabeling (w₁,w₂,c₁,c₂,c₃) as color-first wrong?
2. Find both projections of (1,i,−1,2,0) and reconstruct it.
3. Can P_ch alone reconstruct arbitrary h? Identify what is missing.
4. Give the formula for changing A_old to the new order. Explain the rightmost factor.

Worked answers: (1) The first two values still belong to W₂; the action and labels would disagree. (2) (1,i,−1,0,0)+(0,0,0,2,0)=h. (3) No; w₁,w₂ remain unresolved unless retained. (4) P A_old Pᵀ, where Pᵀ restores the order expected by A_old.

Next dependency: [Lesson 4](lesson-04.md) uses the block sizes three and two to calculate a determinant constraint.
