# Lesson 01 — Changes across a finite edge

Essential question: What must we retain to recover a sequence from its changes?

Goals: calculate a signed finite difference; distinguish change from rate; reconstruct ordered values using an anchor; identify source premises as premises.

Prerequisite bridge: You can subtract signed numbers and solve an equation such as 5=2+u. Check 4−9=−5 and 2+3=5 before continuing. No limiting process or previous calculus is assumed. A function here is simply a table assigning one value to each sample ID. A list in parentheses gives the entries in their recorded order. All numerical samples in this course are synthetic teaching data, not measurements.

## C07.01-E1 — A directed transition

Let s name a starting sample and t an ending sample. An oriented edge s→t tells us which comes first in a subtraction. Write f_s for the value at s and f_t for the value at t. The finite difference on that edge is df=f_t−f_s. The letter d names a change, not division. Thus f_t=f_s+df gives the decoder: add the change back to the start. Reversing an edge reverses its sign, because f_s−f_t=−(f_t−f_s).

If f is recorded in signal-units (abbreviated SU), df is also in SU. When the elapsed time Δτ is nonzero, a rate is df/Δτ, in SU/s if time is in seconds. A difference does not require equal time spacing; a rate does require the actual elapsed time. Sample ID and time are different fields, even when both happen to run 0,1,2,3.

For several edges, keep the first value, called an anchor, and add consecutive differences. Differences alone cannot give an absolute level: adding the same constant to every sample changes no differences. Retaining the anchor supplies the missing coordinate. Keep sample order, time, unit, channel, and edge orientation alongside the numbers.

## C07.01-W1 — Worked reconstruction

Use f=(2,5,4,9) SU at IDs (0,1,2,3), with times (0,1,2,3) s. Forward differences are 5−2=3, 4−5=−1, and 9−4=5 SU. Store anchor f_0=2 SU. Decode successively: 2; 2+3=5; 5−1=4; 4+5=9. Each recovered entry matches its original ID. On the first edge a second channel g changes from 4 to 6 SU, so dg=2 SU. Channels are kept distinct even if their units agree.

## C07.01-W2 — Six source-premise cards

S02#/constitutive_principles/0 through /5 assigns every following card the exact logical_role `premise_not_derived_theorem`. The names and IDs are source names; the explanations below are teaching paraphrases. A constitutive premise specifies how a framework treats a state. Later algebraic equalities follow from stated definitions; a calculation with a geometric basis B does not derive these physical commitments.

| ID and source name | Finite classroom meaning | Where it is used |
|---|---|---|
| EG-A1 complete-state principle | Keep all fields that can change a later result: values, addresses, branches, orientation, scale, residuals and history. Our ledger keeps IDs, times, units and anchors. | This worked sequence |
| EG-A2 decoder principle | A lossless transform has a decoder D with D(T(S))=S: transform a state S with T, then recover it with D. | Lesson 03 pair decoder |
| EG-A3 finite-transition principle | Use endpoint minus start as the primary transition on an edge. | This lesson's df |
| EG-A4 finite-product principle | Retain the interaction df·dg when both factors change. | Lesson 02 |
| EG-A5 residual-information principle | Preserve unresolved components as the next channel for analysis. | Lesson 05 |
| EG-A6 typed-renderer principle | A reduced or displayed view retains its units, scale, projection rule and source state. | Lesson 07 ledger |

Worked reading: a difference list without an anchor is not a complete encoding of f. EG-A1 tells us to retain the later-relevant anchor; EG-A3 declares the chosen transition. The arithmetic above demonstrates recovery for this encoding. It does not establish the source's entire physical ontology. Terms such as lift, gauge transport, infinite resolution and phase are recognition-only here, not additional calculations.

> Claim scope: S02#/backbone_sequence/3 reports mathematical module M04 and its finite difference. The six cards are source-stated premises. Our table is synthetic; its decoder is a freshly checked algebraic consequence. No physical mechanism is inferred from it.

## C07.01-P1 — Practice, then check

For h=(3,7,6,10) SU at the same IDs and times, find forward differences, retain the anchor and reconstruct all samples. Also reverse edge 0→1. Work before reading the answer.

Answer: differences=(4,−1,4) SU and anchor=3 SU. Reconstruction is 3, 3+4=7, 7−1=6, 6+4=10. The reverse edge change is 3−7=−4 SU, a change rather than a sample value. This uses EG-A1 and EG-A3.

## Diagnostics

1. **C07.01-D1:** A signal changes from 5 to 9 SU between 1 and 3 s. Give its difference and rate. Would its difference determine its starting value?
2. **C07.01-D2:** Decode anchor −2 SU with changes (3,0,−1) SU. What does the zero change mean?
3. **C07.01-D3:** Which premise names the decoder requirement? Does a verified basis determinant prove that premise?

Worked answers: D1: df=9−5=4 SU; elapsed time=2 s, so rate=2 SU/s. The difference alone allows starts such as 5 or 15 with corresponding endpoints 9 or 19. D2: (−2,1,1,0) SU; the middle two samples agree but both sample records remain. D3: EG-A2; no, it is source-stated as a premise, not a determinant theorem.

Next dependency: [Lesson 02](lesson-02.md) uses two changes on the same edge to derive the finite product rule.
