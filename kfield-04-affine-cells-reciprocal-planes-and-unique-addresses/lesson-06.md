# Lesson 6 — Reconstruction and boundary checks

**Essential question:** What must an atlas retain so that its labels and rounded displays can always be checked against the original point?

**Goals:** Build a typed reconstruction ledger; verify both affine and owner/local reconstruction; restore exact addresses from displays and retained residuals before testing boundaries.

**Bridge:** Lessons 1–5 supply q=B^-1(x-O), z=floor(q+1/2), u=q-z, and the affine plane and metric checks. We now put these together. A ledger is a table of related values with declared meanings and units. It is useful only if readers can reconstruct rather than guess the input.

## C04.06-E1 — Keep the information needed to reverse each step

For each synthetic point retain the input address q or exact physical point x, the common B and O, owner z and local coordinate u. If a shortened display q_disp is shown, also retain **r=q-q_disp**, called the display residual. It is a signed triple, not merely a size or a score. Reconstruct with **q=q_disp+r**, then x=O+Bq. Retain all three entries even when one is zero.

| Field | Meaning | Units | Reconstruction role |
|---|---|---|---|
| B,O | Ordered step matrix and origin | LU, LU | Define the affine map |
| q | Full address | dimensionless | x=O+Bq |
| z | Integer cell owner | dimensionless | q=z+u |
| u | Local address in [-1/2,1/2)^3 | dimensionless | Retains position inside cell |
| q_disp,r | Display and signed display residual | dimensionless | q=q_disp+r |
| x | Physical point | LU | q=B^-1(x-O) |

For exact fractions, compare boundaries without rounding. For example 499/1000<1/2 because multiplying both sides by positive 2000 gives 998<1000. Multiplying by a positive denominator preserves the inequality. If an input interval rather than an exact point crosses a boundary, record the possible owners and retain that interval; do not pretend the display determines a unique true owner. Our assessed examples supply exact fractions so the rule is unambiguous.

Source values and display values are separate fields. Keep the locked decimal lexeme on a source card even if a shorter number is shown beside it. A source-version replacement is recorded in the provenance ledger, not relabeled as this pointwise display residual. These distinctions keep mathematical reconstruction and historical source comparison separate.

## C04.06-W1 — A complete boundary row

Start with q=(1/2,-1/2,3/2). The affine map gives x1=2+1/2-1/2=2, x2=-1+2(-1/2)=-2, and x3=4-3(3/2)=-1/2. Thus **x=(2,-2,-1/2) LU**. Lesson 2's rule gives z=(1,0,2), u=(-1/2,-1/2,-1/2).

Reconstruct using the two retained parts: z+u=(1/2,-1/2,3/2), B(z+u)=(0,-1,-9/2) LU, and O+B(z+u)=(2,-2,-1/2) LU. The physical reconstruction difference is exactly (0,0,0) LU. Recovering the address from x-O also gives q1=0-(-1)/2=1/2, q2=-1/2, q3=-(-9/2)/3=3/2. Every direction agrees.

## C04.06-P1 — Fractions on opposite sides of a boundary

Use q=(-3/2,49/100,51/100). Compute x and reconstruct it using z and u from lesson 2. Keep all fractions.

**Worked answer:** x1=2-3/2+49/100=99/100; x2=-1+98/100=-1/50; x3=4-153/100=247/100, in LU. With z=(-1,0,1) and u=(-1/2,49/100,-49/100), their sum is the exact original q; substitution gives the same x. Independently, d=x-O=(-101/100,49/50,-153/100) LU. Then q2=49/100, q3=51/100, q1=-101/100-49/100=-3/2.

**Additional display practice, C04.06-P2:** Display q=(499/1000,0,0) as q_disp=(1/2,0,0). Find r and the corrected physical point before assigning the owner.

**Worked answer:** r=(-1/1000,0,0). The displayed point is (5/2,-1,4) LU; its correction Br=(-1/1000,0,0) LU gives x=(2499/1000,-1,4) LU. Restore q_disp+r first: its owner is (0,0,0), and its local coordinate is q itself.

> **Claim scope:** Every example here is synthetic and exact. A zero reconstruction difference checks the stated operations; it is not experimental evidence for a mechanism. A nonzero difference would be retained with its components and investigated. A shortened display is useful only with the removed information and a reconstruction rule. Local coordinate u and display residual r have different roles and must both be named.

## Diagnostic checks

1. **C04.06-D1:** For the display-practice point, what wrong owner would assignment from q_disp alone give, and how does r repair it?
2. A ledger retains z but deletes u after calling it “small.” Which reconstruction fails?
3. Restore q from q_disp=(-3/2,1/2,1/2) and r=(0,-1/100,1/100), then assign z.
4. Can you replace r=(-1/1000,0,0) with its positive magnitude and still reconstruct uniquely?

**Worked answers:** (1) Display-only ownership is (1,0,0), but q_disp+r=(499/1000,0,0) gives (0,0,0). (2) q=z+u and therefore x=O+B(z+u) cannot be reconstructed; z specifies a cell, not its point. (3) q=(-3/2,49/100,51/100), so z=(-1,0,1). (4) No: a magnitude loses the sign and which coordinate changed. Many residual triples have that magnitude.

**Pacing:** 20 minutes explanation/worked example, 15 reconstruction/display practice, 15 diagnostics and feedback, 5 transition.

**Next dependency:** The [capstone](capstone.md) builds a three-point cell-address atlas using only the operations introduced and practiced in these six lessons.
