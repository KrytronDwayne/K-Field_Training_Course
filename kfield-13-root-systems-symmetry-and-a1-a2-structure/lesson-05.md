# Lesson 05 — Primitive lifts and role separation

**Essential question:** When do identical-looking triples describe different things?

**Goals:** Decode and reconstruct a compatible address lift; distinguish 27 lift choices from three primitive channels; keep family, ray, and parity fields independently typed.

**Bridge and pacing:** Lesson 04 showed that a quotient label loses a displacement unless both are retained. Address reduction has the same bookkeeping need, but its carrier is different. One 55-minute period: 5 retrieval, 20 explanation/example, 15 practice, 15 diagnostics.

## C13.05-E1 — A record must say what its fields mean

The source keeps three ordered primitive-lift channels. For our finite model, represent channel identity by the formal basis e₁,e₂,e₃. “Formal” means that these symbols designate slots; they are not measured spatial directions. Each has sum 1; differences have sum zero. Centering gives u₁,u₂,u₃ from Lesson 04. The source's assertion about its full compiler is a source-reported contract; we use its finite channel model without running that compiler.

An address residue is another kind of triple. Modulo 3, we choose each component's representative from {0,1,2}. A compatible next-level lift of the residue ρ has the form ℓ=ρ+3v, where the balanced lift digit v has three entries in {-1,0,1}. Reduction of ℓ modulo 3 returns ρ because each added entry is divisible by 3. Given the representative ρ and ℓ, recover v=(ℓ-ρ)/3 componentwise. The source's general formula uses 3ⁿ; here we explicitly teach the n=1 instance. These choices represent next-level addresses modulo 9. There are 3×3×3=27 choices because each of three digit positions has three independent choices. Distinct digits give distinct lifts modulo 9: a digit difference in {-2,-1,0,1,2} cannot be a nonzero multiple of 3.

These 27 choices are not 27 primitive channel types. A particular digit need not sum to zero: v=(1,1,1) is allowed. Thus not every address-lift displacement is a root-lattice vector. The examples with zero-sum digits simply make comparison with Lesson 03 easy.

| Field | Meaning | What must remain separate |
|---|---|---|
| e_i; centered u_i | Formal channel; its centered weight | Address digit and spatial direction |
| ρ,v,ℓ | Residue, retained digit, reconstructed address | Three primitive channel types |
| F2 | An arbitrary family tag in our synthetic record | A number inferred from a quotient |
| [r_a:r_b:r_c] | Ratios representing a projective ray | Primitive channel basis |
| detector parity p | Sign under a specified antipodal detector operation | A1 integer remainder and family tag |

A projective ray records ratios: [1:2:3] and [2:4:6] label the same ray under positive rescaling. We use the source's positive-scale, oriented-ray convention here: negative multiples are not silently identified. In ordinary unoriented projective coordinates any nonzero common rescaling is identified, so its sign convention must be declared separately. If you replace an actual triple by a ratio view, also retain the removed scale to reconstruct it. Here the ray entries are supplied independently; no physical ray constants are being calculated. Detector parity +1 means a specified signal is unchanged under the detector's antipodal map; -1 means it changes sign. For example, a synthetic scalar function f(t)=t under t→-t has odd parity -1, whereas g(t)=t² has even parity +1. Arbitrary signals need not have a single definite parity. A parity tag does not recover a signal's values.

## C13.05-W1 — A lift and a channel difference

e₁-e₂=(1,-1,0)=α₁, and e₁-h=u₁, e₂-h=u₂. Separately take address residue ρ=(1,0,0) and digit v=(0,1,-1). Then ℓ=(1,0,0)+3(0,1,-1)=(1,3,-3). The last entry -3 has residue 0 because -3=0+3(-1). Reduction returns (1,0,0); decoding the digit gives ((1,3,-3)-(1,0,0))/3=(0,1,-1). This does not generate a new face-area ratio.

> **Source scope:** S02 /backbone_sequence/8/type_guards and /proof_nodes/58/formula (KFM-X014) distinguish primitive channels, compatible address lifts, and projective coordinates. Family tag F2, illustrative rays, and detector functions here are synthetic independent fields, not empirical assignments. Projective signs, chirality, and dyadic recursion receive no identification from this arithmetic.

## C13.05-P1 — Retain the entire record

Use ρ=(1,0,0), v=(-1,0,1), family tag F2, ray [1:2:3] with scale 2, and an independently supplied odd detector channel f(t)=t. Compute and reduce ℓ. State which data reconstruct the address, scaled ray, and detector values.

**Worked practice answer:** ℓ=(-2,0,3). Since -2=1+3(-1), its residue is (1,0,0). Store both ρ and v; their sum ρ+3v reconstructs ℓ. The scaled ray is (2,4,6), reconstructed from scale 2 and representative (1,2,3). The detector parity is -1 since f(-t)=-f(t); retaining f and t is still needed for values. Neither the family tag F2 nor this parity follows from a carry remainder or weight label. Do not overwrite any of these fields with another.

## Diagnostic checks

1. **C13.05-D1:** Why do 27 compatible address lifts not imply 27 primitive channels? Are primitive channels the projective ray coordinates?
2. **C13.05-D2:** For ρ=(1,0,0), v=(1,1,1), compute ℓ and its sum. Must every lift stay in a sum-one plane?
3. **C13.05-D3:** Recover v from ℓ=(1,-3,3),ρ=(1,0,0). Does keeping ρ alone suffice?
4. **C13.05-D4:** A record has carry A=2 and family F2. Can you infer odd or even detector parity? Give a finite reason.

**Worked answers:** 1. They count digit choices versus basis-channel slots, respectively; equal tuple lengths do not equate their roles. 2. ℓ=(4,3,3), sum 10; no, the digit has sum 3, not zero. 3. v=(0,-1,1); ρ alone leaves 27 choices at this level. 4. No. The independent synthetic detector functions f(t)=t and g(t)=t² have opposite parities while the supplied carry and family fields can remain identical.

**Next dependency:** [Lesson 06](lesson-06.md) asks for an explicit map before relating different carriers.
