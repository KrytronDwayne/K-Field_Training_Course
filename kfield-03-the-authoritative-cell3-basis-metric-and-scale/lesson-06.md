# Lesson 6 — A reproducible Cell3 specification

**Essential question:** What must accompany a decimal matrix so another reader can reproduce its meaning and checks?

**Goals.** Read exact source-decimal strings with labels and units; distinguish a mathematical identity from a stored-precision witness; calculate and preserve a signed residual; assemble a provenance-complete geometry card.

## Bridge

You can read columns, compute a metric, check faces and volume, invert the small analogue, and fix scale from an anchor. The remaining task is to keep a numerical record reproducible. A long decimal is not self-explanatory: a row/column convention, unit, source version, and arithmetic rule can change its meaning.

## Source identity and evidence layers

A **lexeme** is the written number string, including its digits. Preserve it before numerical conversion. A **JSON pointer** gives a location within a structured source: `/mature_locked_cell3/B_nm/0/1` means first row, second entry; indices start at zero. A **SHA-256** digest is a 64-character file fingerprint used here to check file identity. It does not prove the mathematics inside the file. [sources.md](sources.md) supplies exact source paths, digests, and pointers; [geometry-card.md](geometry-card.md) supplies the compact numeric fields.

S02 is the mature lock. S03 confirms canonical values and corrects specific stale witness uses. S01 is a historical corrected-source occurrence, not the active numerical branch. Never blend a historical spacing with a mature normal because their digits look close. Preserve a displaced value under its historical provenance. That historical comparison is different from a closure residual computed from one active numerical branch.

Keep the evidence layers explicit. A source fact says what the archived record contains. A mathematical derivation follows from stated assumptions. A numerical witness checks chosen decimals with specified arithmetic. A proposed mechanism explains why a physical structure might arise. This course performs the first three; it introduces no new observed dataset or mechanism. Standard Euclidean vector geometry supplies the reference mathematics.

## Worked example — a precision check you can do by hand

This is a **synthetic rounding example**, not a Cell3 measurement. An exact multiplier is 1/3. Suppose a display stores 0.333. A closure check gives 3·0.333−1=−0.001. Keep the sign and value r=−0.001. The computed product is reconstructed as 1+r=0.999. Do not replace the stored 0.333 by a different constant merely to make the check return zero.

For a matrix check define E=M_stored R_stored−I entry by entry. For a basis/metric comparison define F=B_stored^T B_stored−M_stored. The reference identities are exact when R is the exact inverse and M is the exact Gram matrix. Independently rounded stored arrays need not satisfy them digit for digit. Record **all nine entries** of E and F with their units, not just the largest absolute entry. Reconstruction is M_stored R_stored=I+E and B_stored^T B_stored=M_stored+F. Retaining the source path/hash and arithmetic recipe makes the inputs replayable without copying an archive.

For this course, the attached verification script reads number strings directly, uses Python Decimal with 60 significant digits and ROUND_HALF_EVEN, and preserves complete residual matrices in [verification.json](verification.json). Decimal rounding at a half-tie chooses the even final retained digit: to one decimal place, 1.25 becomes 1.2 and 1.35 becomes 1.4. This is an arithmetic precision rule; it is separate from the half-open spatial cell ownership in Lesson 1. No nearest-integer spatial rounding is used here. No residual is removed because it is small.

## Reading the checked card

The card labels the actual B in nm and M_cell in nm²; R_cell has nm^−2. It quotes source decimals without symmetrizing them. For example, stored R_12 is 0.0015348024281924184 while R_21 is 0.0015348024281924234. Their difference is −0.0000000000000000050 nm^−2, or −5.0×10^−18 nm^−2. The exact inverse metric is symmetric, but these two stored approximations differ. Both strings remain on the card; the difference remains in the verification record.

The source-reported `direct_reciprocal_closure_max_abs` is 2.8939781400741195e−16. The notation e−16 means multiply by 10^−16. This scalar is not our newly recomputed matrix residual, and its label does not specify enough arithmetic to reproduce that source calculation exactly. We retain it as source-reported. Our verification script separately declares its inputs, operations, and precision. A hash match confirms that we checked the intended file, not that its reported witness has been freshly reproduced.

For a short reading exercise, `/mature_locked_cell3/B_nm/0/1` gives 0.0353307758438284 nm, the x component of **b**. `/mature_locked_cell3/face_areas_nm2/ab` gives 0.19486916546048413 nm². A normalized area ray lists bc/ac/ab and begins with 1.0; the face-area table lists ab/ac/bc. Write these labels before doing arithmetic.

> **Claim scope.** The card is a source-grounded specification plus declared numerical verification. It neither replaces canonical source decimals with higher-precision recomputations nor interprets closure differences as measured physical changes. Unresolved arithmetic provenance of a source-reported scalar stays explicitly unresolved.

## Guided practice and diagnostic checks

1. Read B's third column from the card. Give units and axis convention.
2. A student replaces both unequal reciprocal-metric entries by their average. What information has changed?
3. In the synthetic rounding example, store 0.3333 instead. Find the signed residual and reconstruct the product.
4. Name the minimum records needed to distinguish a source-reported closure scalar from a new verification.

## Worked answers

1. c=(−0.0101293176267288,−0.3897877023662599,−0.6897344083672676) nm in the fixed ICRS axes.
2. Both source lexemes have changed and their antisymmetric difference has been lost unless separately retained. The locked card must preserve the originals.
3. 3·0.3333−1=−0.0001; 1+(−0.0001)=0.9999. Smaller magnitude does not authorize deleting the residual.
4. Source ID, full-file hash, exact pointer, original scalar string and reported status; for the new check, input fields, formula, units, arithmetic precision, rounding mode, and every signed residual component.

**Next dependency:** [Capstone](capstone.md) combines your classroom calculation sheet with a separately labeled locked Cell3 geometry card.
