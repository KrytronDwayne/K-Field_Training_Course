# Lesson 05 — Spatial handedness and a time direction

**Essential question:** Which changes preserve orientation, and which must appear as sign changes in our ledger?

**Goals:** Calculate determinants for diagonal toy bases; track swaps, positive rescaling and reflections; distinguish a spatial orientation choice from a time direction.

**Bridge:** Earlier lessons required an ordered list of coordinates. A spatial basis also has an order. Changing that order can change orientation even when no vector length changes. This lesson teaches only diagonal determinants and elementary sign rules; no general determinant expansion is needed.

**Pacing:** 55 minutes: retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15.

## C18.05-E1 — Keep an orientation ledger

A three-dimensional basis is an ordered set of three independent arrows. Put those arrows in the columns of B. A vector with coordinates u is represented by Bu. For B=diag(p,q,r), the arrows run along the three reference axes and their signed scale factors are p,q,r. The determinant is pqr. Its magnitude measures the volume scale of the coordinate box; its sign records handedness relative to the fixed reference orientation. Positive and negative determinants describe opposite handedness. Zero means a collapsed box, not a basis.

Multiplying one column by −1 reverses one arrow: it is a reflection and reverses the determinant sign. Swapping any two columns also reverses the sign; the order of the basis is part of its definition. Multiplying all three columns by a positive factor λ multiplies the determinant by λ³, preserving its sign. A positive rescale cannot repair or change handedness.

A coframe is the corresponding ordered set of coordinate readers, also called covectors. For the diagonal basis above the readers are x/p,y/q,z/r: each returns 1 on its matching basis arrow and 0 on the other two. The coframe determinant is 1/(pqr), so it has the same sign as the basis determinant. We need only this sign relationship here.

Time requires an additional reader τ and a declared positive or forward direction. In the ordered four-dimensional coframe (τ,θ¹,θ²,θ³), reversing τ reverses the four-dimensional orientation while leaving the spatial basis untouched. In this product convention the orientation sign is the time sign times the spatial coframe sign. Changing either once flips the product; changing both leaves the product unchanged but still changes two ledger entries. This is orientation bookkeeping, not a derivation of a physical arrow of time.

## C18.05-W1 — A swap and a time reversal

Take synthetic dimensionless B=diag(1,2,−3). Its determinant is 1·2·(−3)=−6. Its spatial coframe has determinant −1/6. With τ declared forward, the four-dimensional orientation sign is (+)(−)=−.

| Operation | Ordered spatial columns | det B | Time sign | Four-orientation sign |
|---|---|---:|---:|---:|
| Start | first, second, third | −6 | + | − |
| Swap columns 1 and 2 | second, first, third | +6 | + | + |
| Then reverse τ | second, first, third | +6 | − | − |

The final product sign matches the starting product, but neither the basis order nor time direction is the same. Keeping only the final sign would lose the history of changes.

## C18.05-P1 — Rescale, then reflect

Start with B=diag(2,1,−4), columns ordered as displayed and forward τ. Multiply all spatial lengths by 2. Then reverse only the third axis. Record the basis, determinant and four-orientation sign at every step.

**Worked answer:** Initially det B=2·1·(−4)=−8, sign −. Rescaling gives diag(4,2,−8) and determinant 4·2·(−8)=−64=8(−8), sign −. Reflecting the third axis gives diag(4,2,8), determinant +64 and sign +. Time stayed forward throughout. The reflected basis is a changed orientation, not the original source basis under another silent convention. The inverse operations are reflection again, then division of every spatial column by 2, which recovers the starting basis.

> **Claim scope:** S02 M14 uses the left-handed Cell3 spatial coframe together with the forward history covector. The course's locked convention is ICRS columns [a b c] with intentional negative determinant. Our integer diagonal B is a synthetic sign example, not numerical Cell3 geometry. No source constants, metric values or spatial units are inferred from it. Temporal direction, spatial handedness, internal exterior parity and detector parity are separate ledger fields. They do not become equal merely because each sometimes uses a plus/minus sign.

## Diagnostic checks

1. **C18.05-D1:** Can the magnitude 8 of a spatial determinant determine a forward time choice? Explain.
2. What happens to det diag(1,2,−3) if all columns are multiplied by positive 3?
3. What happens to the determinant sign after two successive column swaps?
4. A colleague reflects Cell3's third column “to fix the negative determinant.” What information must the record state?

**Worked answers:** (1) No. Magnitude is a volume scale; the time covector and its direction are additional premises. (2) It becomes 27(−6)=−162, still negative. (3) Two sign flips restore the sign, but the final column order must still be recorded; two different swaps can produce a different order. (4) State the reflected column and changed orientation; this is not the locked basis. Retain the original ordered columns and inverse transformation.

**Next dependency:** [Lesson 06](lesson-06.md) introduces graded labels without identifying them with spatial handedness.
