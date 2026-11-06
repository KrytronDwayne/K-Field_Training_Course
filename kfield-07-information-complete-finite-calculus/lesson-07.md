# Lesson 07 — A complete transformation ledger

Essential question: Can someone else undo every stage of an analysis using only its records?

Goals: compose three taught transforms; reverse them in the opposite order; document every retained and removed component; link all six constitutive premises to concrete ledger operations.

Prerequisite bridge: Lesson 01 needs an anchor to invert differences; Lesson 03 needs signed detail to invert means; Lesson 05 needs model and residual layers; Lesson 06 needs free input coordinates and output compatibility information for a singular map. No new transform is required. Check that means (3,6) can be encoded by first mean 3 and difference 3, then recovered as (3,3+3).

## C07.07-E1 — Record enough to reverse the chain

A transformation ledger describes the input, output, rule, retained side information and decoder at each stage. A typed view says what its numbers mean: unit, sample or block IDs, ordering, and operation. A shorter display is allowed if its source and omitted components remain recoverable. The last operation must be undone first, because the earlier decoder expects the output of its own stage.

Our three stages are: subtract a fixed model; replace each residual pair by its mean and signed half-difference; replace the mean list by its anchor and difference. Each stage changes representation, not the available information. In a real archive, retain a source reference and a replayable recipe rather than copying raw data into every report. In these tiny synthetic exercises, showing the layers explicitly makes the decoder checkable.

## C07.07-W1 — Worked three-stage ledger

Source record: synthetic channel f, original IDs (0,1,2,3), times (0,1,2,3) s, values x=(2,5,4,9) SU. Blocks are {0,1} and {2,3}, in that order. The model rule is the constant 1 SU at every original ID.

| Stage | Input → output | Retained side information | Decoder |
|---|---|---|---|
| 1: subtract model | x → r_0=(1,4,3,8) SU | M_0=(1,1,1,1) SU; original record and rule | x=M_0+r_0 |
| 2: pair split | r_0 → m=(5/2,11/2), d=(3/2,5/2) SU | Signed d; block support; M_1=(5/2,5/2,11/2,11/2); r_1=(−3/2,3/2,−5/2,5/2) | r_0=(m_1−d_1,m_1+d_1,m_2−d_2,m_2+d_2) |
| 3: mean differences | m → anchor A=5/2, difference δ=3 SU | Anchor, mean order and units | m=(A,A+δ) |

At stage 2, compact m has block indices 1,2, whereas x has sample IDs 0,1,2,3. The support map connects them. At stage 3 δ=11/2−5/2=3. Decode in reverse: m=(5/2,5/2+3)=(5/2,11/2); r_0=(1,4,3,8); add M_0 to recover x=(2,5,4,9). Reconstructed minus original is (0,0,0,0) SU at IDs 0–3. Both r_0 and r_1 remain named layers. There are no unrecorded removed components.

## C07.07-E2 — Premises and ledger fields

EG-A1 governs the complete record, including sample addresses, signs and anchors. EG-A2 asks for the reverse decoder and entrywise equality check. EG-A3 names the endpoint-minus-start operation used on the mean list. EG-A4 governs the product-change side calculation from Lesson 02, in which the signed interaction is retained; the three-stage ledger itself does not multiply signals. EG-A5 names the residual recursion, preserving r_0 and r_1. EG-A6 governs how the compact displayed coordinates remain typed views of the source. A ledger may record an operation as not used in its main chain while retaining the linked side calculation; it must not claim that every premise was numerically exercised by every stage.

> Claim scope: All six EG IDs retain S02's logical_role `premise_not_derived_theorem`. Our decoder equalities are proved for the declared finite definitions. Neither EG-A6 nor the other constitutive commitments follow from a determinant of the geometric basis B. B and its physical geometry are not inputs to this synthetic decoder. The general archival E gap remains scoped in Lesson 04.

## C07.07-P1 — Practice, full reverse replay

Use x=(3,7,6,10) SU with IDs/times as in W1, fixed M_0=(2,2,2,2) SU and the same blocks. Build the three-stage ledger, show both residual layers and reverse every stage. State every reconstruction error entry.

Answer: stage 1 gives r_0=(1,5,4,8). Stage 2 gives means (3,6), signed details (2,2), M_1=(3,3,6,6) and r_1=(−2,2,−2,2). Stage 3 gives A=3, δ=3 SU. Decode m=(3,3+3)=(3,6); r_0=(3−2,3+2,6−2,6+2)=(1,5,4,8); x=M_0+r_0=(3,7,6,10). Error=(0,0,0,0) SU. All fields retain their stage and support labels.

## C07.07-P2 — Practice matching the six cards

Match each EG-A1–EG-A6 ID to a record or side calculation in P1, using the product example in Lesson 02 P1. Correct the sentence “EG-A6 follows from the determinant of B.”

Answer: EG-A1→source order, units and anchors; EG-A2→reverse replay; EG-A3→δ=6−3; EG-A4→Lesson 02's retained interaction (−2)·3=−6 SU²; EG-A5→r_0 and r_1 as distinct layers; EG-A6→typed compact view plus decoder and source record. All six are source-stated constitutive premises. The corrected sentence is: “EG-A6 is a constitutive premise; our specified decoder is an algebraic construction, not a derivation of that premise from B.”

## Diagnostics

1. **C07.07-D1:** Name the minimum ledger fields. Explain what fails if the mean anchor, detail sign or singular free parameter is omitted.
2. **C07.07-D2:** Match all six EG IDs to P1 and its product side calculation. Does any follow from a basis determinant?
3. **C07.07-D3:** Decode A=4, δ=−1, d=(1,−2) SU, model M_0=(2,2,2,2) SU and the standard blocks. Retain r_0 and r_1.

Worked answers: D1: original IDs/order/times/channel/units, source scope, model rule, block support, signed details, anchors, outputs, omitted components and inverse operations; singular views also keep t and c or rho. Missing A leaves an arbitrary common level; missing signs leaves ambiguity within pairs; missing t leaves a family of inputs. D2: use the six explicit mappings in P2; none is derived from B alone. D3: means=(4,3), r_0=(4−1,4+1,3−(−2),3+(−2))=(3,5,5,1); M_1=(4,4,3,3); r_1=(−1,1,2,−2); x=(5,7,7,3) SU.

Next dependency: [Capstone](capstone.md) combines the taught transforms, product checks, operator hypotheses and singular branches into one audited submission.
