# Lesson 8 — The integrated research defense

Essential question: Can every step from geometry to the next instrument test be defended without losing a premise or residual?

Goals: Reconstruct all decoder channels; retain six phase factors; state an explicit geometric-to-instrument interface; defend a prospective discriminator with its remaining gaps.

Prerequisite bridge: Lessons 1–7 taught coordinates, witness scope, matrix rows, inverse recovery, frozen comparisons and residual reporting. Here we add a small decoder calculation and teach its operations before the capstone. The advanced source names are reading labels; the finite calculations below require only multiplication, addition and simultaneous equations.

## C30.08-E1 — Connect the interfaces

A continuous chain has five interfaces: geometry defines addresses and lengths; a supplied trajectory/ruler turns displacement into phase coordinates; a proposed transfer maps these to instrument channels; a decoder separates a modeled component and retained residual; and an independent test compares frozen candidates. Every interface must name its inputs and output units. A missing physical transfer is an explicit proposed link rather than an invisible implication.

For a synthetic extension of Lesson 1, let q0=(0,0,0),q1=(1/2,0,0). The displacement is a/2 in nm, using the pinned mature column. Choose a synthetic dimensionless phase coordinate phi=2(q1_1−q0_1)=1. Here subscript 1 means first component and factor 2 is a supplied ruler convention, not a measured coupling. A proposed normalized transfer produces y_S=theta1+theta2 and y_D=phi(theta1−theta2). At phi=1 it is exactly Lesson 3's sum/difference model. Calibration must show how actual readings become these dimensionless channels; a prediction of phase alone cannot establish force or energy extraction. For A=(2,1), prediction is (3,1); for B=(1,2), it is (3,−1). This connects an exact address construction to a falsifiable proposed transfer without inventing the missing apparatus witness.

### A three-channel decoder bridge

Use the synthetic matrix A=[[1,0],[0,1],[1,1]] and y=(2,3,6), all dimensionless. A coefficient pair c=(c1,c2) predicts Ac=(c1,c2,c1+c2). Set r=y−Ac and retain all three entries. To choose a reproducible decomposition, require r1+r3=0 and r2+r3=0. These equations make the residual's dot product with each column of A zero; a dot product multiplies matching entries and adds them. This is a coordinate convention for decomposition, not a reason to erase r.

Substitute r=(2−c1,3−c2,6−c1−c2). The conditions give 2c1+c2=8 and c1+2c2=9. Doubling the first and subtracting the second gives 3c1=7, so c1=7/3. Then c2=8−14/3=10/3. Thus Ac=(7/3,10/3,17/3), r=(−1/3,−1/3,1/3). Adding produces (6/3,9/3,18/3)=(2,3,6). Both dot products are zero. Two coefficient coordinates plus one independent residual coordinate retain the three original channels. This is an analogue of S02 M17's six active plus seven syndrome coordinates in a 13-channel source system; it is not the source's 13-by-6 matrix.

## C30.08-W1 — All six determinant-line factors

S02 M15 names UV, light, regulator, heavy, cap and induced contributions and a trivialization, a chosen way to represent the combined line in ordinary complex numbers. It also retains topology and admitted sectors, meaning the permitted classes of states on which closure is claimed. A scalar toy can demonstrate why no factor may be dropped, without proving the global construction.

Teach the needed arithmetic: i is a symbol with i²=−1. Ordinary distributive multiplication then gives i(−i)=1. In a chosen synthetic scalar representation let (UV,light,reg,heavy,cap,induced)=(i,i,−1,−i,i,1). Multiplication in order gives i·i=−1, then (−1)(−1)=1, then −i, then (−i)i=1, then 1. Removing heavy instead gives i·i·(−1)·i·1=i. Thus the complete product is 1 but the shortened one is i. This proves only the displayed arithmetic. It does not prove existence of a global trivialization or closure in every admitted sector.

## C30.08-P1 — Prepare the defense

Reconstruct y=(2,3,6) from the decoder pair above and every residual entry. Then attach the geometric phi construction, proposed sum/difference transfer, calibration gate, frozen A/B predictions and all outcome branches to a single ledger.

Answer: Reconstruction is (7/3−1/3,10/3−1/3,17/3+1/3)=(2,3,6). Keep this decoder demonstration separate from the two-channel A/B experiment: c is not theta and the 3-channel y is not the prospective detector pair. The common connection is the information-retaining method. Geometry supplies q and a/2, the synthetic ruler supplies phi=1, and the proposed transfer supplies the sum/difference rows. Test A/B only after calibration establishes those rows. Retain A-compatible, B-compatible, unresolved/overlapping, mismatch-to-both and invalid/incomplete branches. M19 remains outside core M20, compiler labels keep their own namespace, and unprovided certificates remain gaps.

> Claim scope: The integrated defense is a complete research argument with a next test. Source-reported closure, exact synthetic calculations, proposed mechanisms and planned measurements have distinct roles. The decoder is not a fresh physical occupation-selection proof, and its coefficient c must not be confused with Cell3 column c.

## C30.08-D1 — Diagnostics and worked answers

1. What is the third reconstructed decoder channel? **Answer:** 17/3+1/3=6; omitting its residual would give 17/3 instead.
2. What happens if the heavy scalar factor is deleted? **Answer:** Product i replaces 1; the original six-factor record must remain intact.
3. Does phi=1 measure a force? **Answer:** It is a synthetic dimensionless phase coordinate under a chosen ruler. Force requires a separate calibrated force/impulse witness.
4. What must a defense say about an unavailable route certificate? **Answer:** Give its known source return address, mark the body missing, and state which source replay is gated; do not fill it using the toy calculation.

Next dependency: [Capstone](capstone.md), eight previously practiced operations assembled into a 32-point research portfolio.
