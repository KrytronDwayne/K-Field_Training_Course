# 3. Normalization with an inverse account

Essential question: What must a normalization retain to be reversible?

Goals:

- Compute valid Clear ratios and flag failures
- Reconstruct inputs including rounding closure
- State the transformation domain

## Prerequisite bridge

Use [Acquisition identity and raw-value preservation](lesson-02.md): its retained records and operations are the inputs to this lesson.

Pacing: 2 period(s) of 55 minutes. Clear ratio and zero denominator / Exact reconstruction and decimal residual.

## C28.03-E1 — first principles

A ratio answers “how much A per unit of Clear in this paired reading?” It does not answer how much absolute light arrived. Let C mean the Clear count in the same acquisition row, and define r=A/C when both inputs are present and finite and C is nonzero. This is the mathematical domain. A stricter instrument implementation may require positive C; record that policy separately. The installed Clear-Normalize tool uses the stricter nonpositive-C invalid branch. Our toy valid denominators are all positive, so the policies agree here.

The units count/count cancel, so r is dimensionless. Do not divide times, sequence numbers or orientations by C. Where C is valid, Clear/C=1. Do not clip a ratio greater than 1: A=12,C=10 gives 1.2 and remains a ratio. A negative spectral input stays signed with its instrument status. Undefined is a status, not a large number or zero.

An inverse account explains how to recover inputs. If r is exact, A=rC. The pair (r,C) preserves amplitude; r alone does not, because (2,10) and (4,20) both give 1/5. For an invalid ratio retain the raw A and C directly. They are still available for other analyses.

Displayed decimals may be rounded. Ten significant digits count from the first nonzero digit. Keep exact fractions when possible. If r_display is rounded, define the signed ratio closure delta=r_exact-r_display. Then A=(r_display+delta)C. For 1/3, 0.3333333333 equals 3333333333/10000000000. Subtracting from 1/3 gives (10000000000-9999999999)/30000000000=1/30000000000. Multiplying the display alone by 3 gives 0.9999999999; adding the retained closure recovers 1 exactly.

For the common acquisition, row 0 gives 2/10=1/5 and returns (1/5)10=2; row 2 gives 8/20=2/5 and returns 8; row 3 gives 1/10 and returns 1; row 4 gives 3/10 and returns 3. Row 1 has A=5,C=0, so no division is performed. Keep its pair (5,0), the undefined-ratio flag and all original metadata.

> Claim scope: Ratios and inverse identities are derived arithmetic. They do not calibrate optical response. Missing and zero denominators remain distinct statuses.

## C28.03-W1 — worked example

For the five-row toy, ratios are (1/5,undefined,2/5,1/10,3/10). Reconstruct defined rows by multiplication and row 1 from retained raw A=5. The zero-Clear branch is a preserved row, not r=0 or infinity.

## C28.03-P1 — guided practice

**Student task.** For the separate pair A=1,C=3, compute the exact ratio, its ten-significant-digit display 0.3333333333, the signed closure exact minus display, and reconstructed A. Then classify A=0,C=5 and A=0,C=0. List the inputs and rules that must survive.

### Worked answer

For raw A=1, Clear=3, exact r=1/3. A 10-significant-digit display 0.3333333333 differs by 1/(3*10^10); retain that ratio closure and the original integers. For A=0, Clear=5 the ratio is valid 0, contrasting with invalid 0/0.

Here delta=1/30000000000 and (0.3333333333+delta)*3=1 exactly. Retain A=1,C=3, exact r, displayed r, delta and the ten-significant-digit rounding rule. For 0/0 record undefined rather than valid zero.

## C28.03-D1 — diagnostic checks

1. Compute A=0,C=5 and A=0,C=0.
2. Can r=1/5 alone recover A?
3. What is the missing numerator when r=2/5,C=20?
4. How is 1/3 reconstructed from its ten-digit display?

## Worked answers

1. First ratio is valid 0; second is undefined and retains both raw zeros.
2. No: A=2,C=10 and A=4,C=20 both work. Retain C.
3. A=(2/5)*20=8 counts.
4. Add delta=1/30000000000 to 0.3333333333, then multiply by C=3 to return 1.

Next dependency: [lesson-04](lesson-04.md) uses these operations. Reconstruct the worked input and explain the diagnostic answers before proceeding. Source boundaries: [sources](sources.md).
