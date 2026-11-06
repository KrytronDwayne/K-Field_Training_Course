# Lesson 3 — Reciprocal vectors as plane counters

**Essential question:** What physical calculation reads an address coordinate without confusing it with a physical axis?

**Goals:** Verify three direct-reciprocal pairings; calculate affine plane levels; select matching canonical source fields while rejecting a superseded branch.

**Bridge:** Lessons 1–2 gave q=B^-1(x-O), with q=z+u. We keep the same synthetic B and O. A **dot product** multiplies corresponding components and adds: (r1,r2,r3) dot (s1,s2,s3)=r1s1+r2s2+r3s3. For example (1,2,0) dot (3,-1,4)=3-2+0=1. It produces a scalar, one number rather than a triple.

## C04.03-E1 — Design a vector by what it reads

We want a vector that reads q1 from the physical displacement d=q1a+q2b+q3c. It must have dot product 1 with a and 0 with b and c. Distributing the dot product then gives q1×1+q2×0+q3×0=q1. This reader is the first **reciprocal vector**. The second reads q2 with pairings (0,1,0); the third reads q3 with pairings (0,0,1). The reciprocal is not the direct vector normalized to length one.

Let h=(h1,h2,h3) be an integer triple specifying which combination h1q1+h2q2+h3q3 to read. We require g_h dot a=h1, g_h dot b=h2 and g_h dot c=h3. For our synthetic columns these conditions become:

```text
g1 = h1,      g1+2g2 = h2,      -3g3 = h3.
Therefore g_h = (h1,(h2-h1)/2,-h3/3) LU^-1.
```

Here g1,g2,g3 are components of the vector g_h, not separate plane labels. Taking a dot product with d now gives **g_h dot (x-O)=h dot q**. Both sides are dimensionless. A plane family consists of points where this level is an integer m: **g_h dot (x-O)=m**. A general point can have a noninteger level; it then lies between the integer-level planes. h must be nonzero for a plane normal and finite spacing.

The compact formula is g_h=B^-T h. The symbol T means transpose, swapping rows with columns; B^-T means transpose the inverse B^-1. Each row of B^-1 already reads one address entry. Turning these rows into columns and weighting them by h makes the required physical reader. This derives the notation from the three pairings; you do not need a general matrix-inversion algorithm.

## C04.03-W1 — Check every pairing

For h=(1,0,0), g=(1,-1/2,0) LU^-1. Pair with a=(1,0,0): 1. Pair with b=(1,2,0): 1-1=0. Pair with c=(0,0,-3): 0. At the lesson-1 point x=(2,-2,1) LU, x-O=(0,-1,-3) LU, so g dot (x-O)=0+1/2+0=1/2, correctly reading q1.

## C04.03-P1 — A second reader

Use h=(0,1,0). Find g, verify its three pairings, and evaluate the level at q=(1/2,-1/2,1).

**Worked answer:** g=(0,1/2,0) LU^-1. Its dot products with a,b,c are 0,1,0. At x-O=(0,-1,-3), the level is -1/2, equal to q2.

## C04.03-E2 and C04.03-W2 — Read a source card without changing its branch

A source pointer names a location inside a JSON document. The slash path `/backbone_sequence/1/result` selects the second sequence entry (indexing starts at zero), then its result field. S02's M02 result lists unit normals and spacings in u,v,w order. These source axis names are separate from our local-coordinate vector u; in the table they label the three reciprocal families. A unit normal specifies direction; a spacing specifies the perpendicular separation, taught computationally in lesson 4. A nanometre, nm, is 10^-9 metre.

Read the canonical table in [canonical-card.md](canonical-card.md), reproduced from S02 `/backbone_sequence/1/result`. For u, the full source spacing is **0.32954652969544673 nm** and its matching normal is **(0.9959651903089612, -0.08360216250737743, 0.03261929056440005)**. Copy the full lexemes (the exact written decimal strings), axis order, units and pointer onto your card. This is source-reading, not hand computation of those decimals.

## C04.03-P2 — Compare provenance before arithmetic

Compare canonical u spacing with S02 `/backbone_sequence/1/reciprocal_witness/u/spacing_nm`, which reads **0.3295465297092934 nm**. Use S03 `/findings/4` to decide which is active. Then identify canonical v and w spacings from the card.

**Worked answer:** AUD-005 in S03 marks `M02.reciprocal_witness` SUPERSEDED_NUMERIC_WITNESS. The canonical active u spacing is 0.32954652969544673 nm; the other is retained solely as superseded provenance. Canonical v is 0.4515973797212846 nm and w is 0.6050977415185554 nm. The discrepancy between branches is not measured residual information and should not be renamed as such.

> **Claim scope:** The table reports archival source values at stored precision; the small synthetic pairing examples are freshly checkable mathematical derivations. The source's printed unshifted plane expression must be read with its origin convention; our affine equations always retain x-O (x-O_K for Cell3). No closure theorem or physical mechanism is inferred from reading this card. Never mix a canonical normal with a stale spacing.

## Diagnostic checks

1. **C04.03-D1:** For h=(1,1,0), find g and evaluate g dot (x-O) and g dot x at the worked point. Which equals h dot q?
2. **C04.03-D2:** A card uses the canonical u normal but spacing 0.3295465297092934 nm. Accept or reject? Name the field that repairs it.
3. Find g for h=(0,0,1), and verify its pairing with c.
4. For h=0, can the formula provide a direction for a plane normal?

**Worked answers:** (1) g=(1,0,0) LU^-1; shifted level is 0 and unshifted is 2. h dot q=1/2-1/2=0, so only the shifted expression works. (2) Reject the mixed branch. Use S02 `/backbone_sequence/1/result/reciprocal_spacings_u_v_w_nm/0` with the matching normal at `/backbone_sequence/1/result/reciprocal_normals_u_v_w/0`. (3) g=(0,0,-1/3); g dot c=1. (4) No: g=0 has no direction. The equation is all space if m=0 and no points if m≠0, not a plane family.

**Pacing:** 20 minutes dot-product bridge and worked pairing, 10 pairing practice, 10 source-card worked/practice activity, 10 diagnostics and feedback, 5 transition. The source card is supplied; students do not browse or invert locked decimal matrices.

**Next dependency:** [Lesson 4](lesson-04.md) turns these nonzero plane counters into unit normals and physical spacings.
