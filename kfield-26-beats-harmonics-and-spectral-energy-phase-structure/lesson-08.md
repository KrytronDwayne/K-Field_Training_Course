# Residual spectra as the next measurement

**Essential question:** How can an incomplete model be useful without erasing what it fails to represent?

**Goals:** Reconstruct a signal from a represented component and residual; transform both with the same convention; design a next comparison that retains domain failures and odd information.

**Prerequisite bridge.** Lesson 5 split a sequence into even and odd components; Lesson 4 reconstructed a DFT. A model need not describe everything. Define residual r=x−m for any declared represented component m. This is a coordinate equality, x=m+r, not a judgment that r is disposable.

## C26.08-E1 — Keep a complete decomposition

Subtract entry by entry at matching times and channels. Keep m, r, their units, their sample order, and the exact rule that constructed m. The DFT is linear: each output is a sum of fixed multipliers times samples. Distributing those multipliers over m+r proves DFT(x)=DFT(m)+DFT(r). Apply the same inverse to both spectra and add to recover x.

An average magnitude or scalar score can summarize a residual but cannot replace it. For example (1,−1) and (−1,1) have equal squared totals yet different timing. A useful next comparison can inspect residual phase, wavelength, orientation, parity or event neighborhood. It must use common coordinates and keep the component removed at each stage. In a second stage write r=m₁+r₁; then x=m+m₁+r₁. Save all three.

An undefined ratio has a different status from a numerical residual. Keep its original row and reason, plus every defined intermediate. Never fill it with zero to make a plot convenient. If a display hides such a point, the report must still contain its row and status.

## C26.08-W1 — Worked exact reconstruction

Use x=(1,2,3,4) counts with Δt=1/4 s and the DFT convention of Lesson 4. Choose m=E x=(2,3,2,3). The residual r=O x=(−1,−1,1,1). Calculate spectra directly:

DFT(m)=(2+3+2+3, 2−3i−2+3i, 2−3+2−3, 2+3i−2−3i)=(10,0,−2,0).

DFT(r)=(−1−1+1+1, −1+i−1+i, −1+1+1−1, −1−i−1−i)=(0,−2+2i,0,−2−2i).

Adding gives (10,−2+2i,−2,−2−2i), the full spectrum. Inverse m has numerators (8,12,8,12); inverse r has (−4,−4,4,4). Dividing by 4 gives the two retained components, whose entrywise sum is (1,2,3,4).

An even-only comparison has no access to the odd residual. That blindness explains a missing comparison response without implying that the measured odd information is zero.

## C26.08-P1 — Practice and worked answer

For x=(3,1,−1,1), form m=E x and r=O x. **Answer:** Hx=(−1,1,3,1), hence m=(1,1,1,1) and r=(2,0,−2,0). Their spectra are (4,0,0,0) and (0,4,0,4). The inverse of the first is all ones; the second gives (8,0,−8,0)/4=(2,0,−2,0). Add to reconstruct x exactly.

For a next comparison, retain the residual coefficients at bins 1 and 3 and compare them with a second channel sampled at the same Δt and origin. If that reference coefficient is zero, record an undefined ratio and both coefficients instead of replacing the ratio by zero. Keep m alongside that comparison.

Append the three failure rows from Lesson 5: A counts (2,0,4,0), Q=0 with defined M=3,D₀=−1,D₉₀=0, contrast=3,ρ=1/2; B counts (8,4,6,2), g=4/3 but ρ=0; C the same counts and g but sin θ=0, so ρ is undefined. In B and C M=7,Q=3,D₀=D₉₀=1. None permits a defined P. Their different reasons remain distinguishable.

## Plan a replayable comparison

Your output packet should contain: the input reference or full small synthetic sequence; timestamps and units; reference-channel definition; model rule and component; full signed residual and its spectrum; inverse convention; reconstruction residual; defined/undefined statuses; and the evidence class. For archive work, retain the immutable references and all source diagnostic masks, rather than making another raw data copy. For a tiny classroom example, save the complete synthetic coordinates.

Compare candidate mechanisms by what retained structures they can jointly explain and what new predictions they make. A proposal that only fits the even component leaves an explicit task: explain or predict the odd component. No scalar fit summary closes that task. The 25/27-to-2 source pathway remains a proposed branch; our four-sample transform aliases high indices and cannot independently test that native pathway.

## C26.08-D1 — Diagnostic checks and answers

1. Why does DFT(m+r)=DFT(m)+DFT(r)? **Answer:** Each row is a fixed weighted sum, and multiplication distributes over addition.
2. A residual score is zero after rounding. Can r be erased? **Answer:** No. Save its actual signed coordinates and precision; a rounded summary is not the residual.
3. How do you reconstruct after modeling r again? **Answer:** If r=m₁+r₁, sum m+m₁+r₁ with the same coordinates.
4. Does the even comparator's nullspace explain away odd observations? **Answer:** It identifies a comparator limitation. Keep the odd observations and test them with a comparison that has odd support.

> **Claim scope:** Exact closure in these finite synthetic examples demonstrates bookkeeping and algebra. Source binary64 closure, physical calibration, and mechanism identification are different checks. Residual information remains a primary measurement coordinate at each step.

**Next dependency:** [Capstone](capstone.md) combines all nine operations in a complete retained-information packet.
