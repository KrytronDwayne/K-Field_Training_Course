# Lesson 6 — A complete finite registry

**Essential question:** What makes a 27-row registry complete and recoverable?

**Goals:** Construct every field of a node record; apply independent count and reconstruction checks; preserve discrepancies as explicit coordinates.

**Prerequisite bridge:** Lessons 1–5 supplied every arithmetic operation. We now combine them in an ordered workflow and check by a different route. Budget: explanation/work 20 minutes, practice 15, checks/feedback 15, transition 5. The full 27-row construction is completed in the two-period capstone; here students build and check representative rows.

## C05.06-E1 — A row is a record, not a total

Use the classroom O=(2,−1,4) U and basis columns a=(1,0,0), b=(1,2,0), c=(0,0,−3) U. Declare this geometry once for the registry. Keep a row ID and the following fields for each node:

|Field|Meaning and construction|
|---|---|
|L|Original signed triple; unique row identity|
|q|Dimensionless L/2|
|p|O+Bq, in U|
|λ|Integer sum of L entries|
|χ|+1 for even λ; −1 for odd λ|
|r₃|Remainder 0,1,2 in λ=3k+r₃|
|v,s|Canonical representative and member orientation; center has s=N/A|
|z,u|Cell owner and owned-cell residual q−z; both dimensionless|
|R_L|Reconstructed address minus stored L, three dimensionless components|

The residual u is not an error. It is the position within the owned cell and is essential to reconstruct q=z+u. R_L is a separate closure discrepancy: a difference produced by checking the map. Never merge these two meanings of residual. In an exact correct registry R_L=(0,0,0); keep that result per row. If a row fails, keep its original fields, record the discrepancy, and make a separately documented correction. Do not delete it to improve a summary.

Build in this order: enumerate L; halve it; calculate position; compute sum and class labels; assign representative and orientation; assign owner and within-cell residual; finally recompute L from position. A total of 27 does not establish that the 27 intended rows are present. Compare the set of distinct triples with the full nested enumeration.

## C05.06-E2 — Independent checks

Reverse the position with d=p−O, q₁=dₓ−dᵧ/2, q₂=dᵧ/2, q₃=−d_z/3, then double q to obtain L_recovered. Subtract the stored L entry by entry to get R_L. Also compare q with z+u. For a noncentral row compare L with s v. These checks attack different ways a row could be wrong.

Count the seven λ labels, the two χ labels and the three r₃ labels independently. Confirm 26 noncentral rows, each of 13 representatives occurring twice with signs −1,+1, plus exactly one center. For each pair check the sum of positions equals 2O. Counts alone can conceal a wrong position; inverse mapping can pass on a duplicated row. Both kinds of check are necessary.

## C05.06-W1 — Worked complete row

For L=(1,−1,1), q=(1/2,−1/2,1/2), p=(2,−2,5/2) U, λ=1, χ=−1, r₃=1. Its first nonzero entry is positive, so v=(1,−1,1), s=+1. The owner z=(1,0,1), and u=(−1/2,−1/2,−1/2). Adding z+u recovers q. Reverse p: d=(0,−1,−3/2) gives q=(1/2,−1/2,1/2), so L_recovered=(1,−1,1) and R_L=(0,0,0).

## C05.06-P1 — Guided practice, with answer

Complete the row for (−1,1,−1) and compare it with W1. Answer: q=(−1/2,1/2,−1/2), p=(2,0,11/2) U; λ=−1, χ=−1, r₃=2. The representative is again (1,−1,1), but s=−1. Owner z=(0,1,0), residual u=(−1/2,−1/2,−1/2). Inverting p gives q₁=0−1/2=−1/2, q₂=1/2, q₃=−(3/2)/3=−1/2. Thus R_L=0. The two p values sum to (4,−2,8) U. The equal u values do not make these the same node because their z values differ.

## C05.06-P2 — Finding a retained discrepancy

Suppose the W1 row keeps L=(1,−1,1) but stores p=(2,−2,3) U. Compute R_L before correcting it. Answer: d=(0,−1,−1) gives q=(1/2,−1/2,1/3); L_recovered=(1,−1,2/3). Therefore R_L=(0,0,−1/3). Retain that discrepancy and original stored p in a correction note; the forward rule gives corrected p_z=5/2. A record of this repair preserves what changed and why.

> **Claim scope:** This registry is a synthetic exact-arithmetic demonstration of source-defined finite operations. It is not a measurement dataset. Source definitions, derived counts, storage conventions, and synthetic discrepancies have separate roles. Nothing is averaged away or excluded.

## Diagnostic checks

1. **C05.06-D1:** State the distinct-address, sheet, pair and inverse checks required for completion.
2. **C05.06-D3:** Why do correct sheet counts not guarantee correct physical positions?
3. **C05.06-D4:** A registry stores v and χ but omits s. Can it reconstruct all L?
4. **C05.06-D5:** Distinguish u from R_L. Which can legitimately be nonzero in a correct registry?

**Worked answers:** 1. Exactly the 27 allowed distinct triples; sheets 1,3,6,7,6,3,1; 13 two-member noncentral pairs and one center; inverse map returns every L with R_L=0. Also reconcile χ counts 13,14 and r₃ counts 9,9,9. 2. λ uses L only; changing p leaves λ counts unchanged but fails the inverse check. 3. No: antipodes have equal χ; s must select the member. 4. u records within-cell position and is often nonzero; R_L records inverse closure and is zero for this exact example. Both are retained.

**Next dependency:** [Capstone](capstone.md) constructs the complete registry. [The full worked registry](registry.md) is the answer reference, to be opened after attempting the construction.
