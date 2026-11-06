# Lesson 1: From faces to dimensionless ratios

Essential question: What information does a face-area ratio keep, and what must we retain to recover size?

Goals

- Compute a ray in bc/ac/ab order.
- Reconstruct all three areas from the ray and its labeled divisor.
- Explain why an area ray does not specify a unique spatial cell.

Pacing: 55 minutes — retrieval 5; explanation and worked example 20; guided practice 15; diagnostics and repair 15.

Prerequisite bridge

Courses 03 and 07 supply labeled geometry and arithmetic. Here the needed entry skills are multiplying two lengths to find a rectangular area and simplifying a fraction. Check: 3 times 4 is 12; 8/12 reduces to 2/3 by dividing numerator and denominator by 4. If either operation is uncertain, repeat with 6/9 before proceeding.

## C08.01-E1 — Labels before division

Imagine a classroom box with three perpendicular edges named a, b, and c. The face meeting b and c is called bc; the other two face types are ac and ab. Write their areas as A_bc, A_ac, and A_ab. A is a name for area, and its subscript identifies the face. If a length unit is U, area uses U²: a square U by U. Cell3 faces need not be rectangles. In this course their areas are supplied, so no angle formula or vector operation is needed.

An ordered triple is a list whose positions have declared meanings. We always use (A_bc,A_ac,A_ab). A positive area ray is the collection of all positive common multiples of one such triple. For example, (12,8,6) and (18,12,9) belong to one ray because the second is 3/2 times the first. The order still matters.

To normalize, divide each entry by the positive first area. This produces r=(1,A_ac/A_bc,A_ab/A_bc). The symbol r names the normalized area ray. Each quotient has units U²/U²=1, so it is dimensionless. The first entry is always 1; only the other two entries can vary independently. This determines the area triple up to one common multiplier. It does not determine all angles, edge directions, or a unique basis in space. In the source's phrase “projective shape,” the scope here is the projective **area** triple; a spatial reconstruction needs additional geometric assumptions.

Normalizing without retaining A_bc loses the absolute size. We therefore keep the pair (A_bc,r), including the unit and labels. The reconstruction rule is (A_bc,A_ac,A_ab)=A_bc times r, meaning multiply every component by the retained area.

## C08.01-W1 — A fully labeled synthetic box

Take a=2 U, b=3 U, c=4 U, mutually perpendicular. Its areas are bc=3×4=12 U², ac=2×4=8 U², ab=2×3=6 U². Normalize: 12/12=1, 8/12=2/3, 6/12=1/2. Thus r=(1,2/3,1/2), with divisor 12 U². Reconstruction gives 12×1=12, 12×2/3=8, and 12×1/2=6 U². Every original component is recovered.

> Claim scope: This is a synthetic orthogonal box, not Cell3 or a measurement. The ray definition is S02#/backbone_sequence/4/definitions. Source paths and verified hashes are in sources.md. Source Cell3 uses an ordered basis with a negative determinant; positive face-area magnitudes do not encode that orientation.

Guided practice — C08.01-P1

Normalize (18,12,9) U², keep the divisor, and reconstruct. Work before reading the answer. **Answer:** dividing by 18 U² gives (1,2/3,1/2). Multiplying that ray by 18 U² gives (18,12,9) U². The normalized shape matches W1, while each area is 3/2 as large. The divisor distinguishes them.

Diagnostic checks

1. **C08.01-D1** Swap ac and ab in W1 while retaining the declared order. What ray results?

2. **C08.01-D2** Normalize (15,10,5) U² and reconstruct it.

3. **C08.01-D3** Can (1,2/3,1/2) alone tell you A_bc or the cell angles?

4. **C08.01-D4** Why must A_bc be positive in this course?

Worked diagnostic answers

1. The input becomes (12,6,8), so r=(1,1/2,2/3); this differs from W1.

2. Dividing by 15 gives (1,2/3,1/3). Retain 15 U²; multiplying returns (15,10,5) U².

3. No. Any positive divisor supplies a possible size, and the ray contains no complete angle specification.

4. Zero would make division undefined; negative values would not be positive face-area magnitudes. The positivity contract also makes every later reciprocal defined.

Next dependency: [lesson-02](lesson-02.md). Carry the labeled input triple, divisor, source role, and retained differences forward.
