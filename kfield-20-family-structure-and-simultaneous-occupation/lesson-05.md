# Lesson 5 — The rank-48 projector

Essential question: What precisely is counted by the source's number 48?

Goals: Derive rank 48 from an independent image basis; describe the equal restriction to each family; test zero and higher-rank history alternatives.

Prerequisite bridge: Lesson 4 distinguished carrier dimension and image rank and proved finite rank multiplication for product maps. We now apply that proof to source-typed factors, not to a numerical coincidence. Use two periods: factor accounting and history alternatives.

## C20.05-E1 — The declared factors

S02#/backbone_sequence/15/family_projector states Qₙ=I₁₆⊗I₃⊗qₙ. Read the factors in order: internal carrier, family-label carrier, history carrier. The identity I₁₆ preserves 16 independent internal coordinates; I₃ preserves all three family coordinates. The history projector qₙ selects one independent history direction. The subscript n labels which history projection is used; it is not a family label.

For the rank calculation assume qₙ is nonzero, self-adjoint (qₙ†=qₙ), idempotent (qₙ²=qₙ), and rank one. Choose a normalized history vector hₙ spanning its image. Then qₙhₙ=hₙ. No total history dimension has been supplied in this calculation. If that dimension is a finite H, the full carrier dimension is 16×3×H; its selected image still has rank 48. If the history space is infinite, the image count below remains finite under the rank-one assumption. No infinite-dimensional calculation is required of students.

| Factor | Type and basis addresses | Ambient dimension | Image rank |
|---|---|---:|---:|
| I₁₆ | internal eᵢ, i=1,…,16 | 16 | 16 |
| I₃ | family fᵣ, r=0,1,2 | 3 | 3 |
| qₙ | history, image spanned by hₙ | H if finite; not fixed here | 1, assumed nonzero |
| Qₙ | ordered product (i,r,history) | 48H if finite | 48 |

These are dimensionless counts, not masses or physical volumes. S02#/proof_nodes/81 names the internal identity I_(Lambda_even). This course takes its declared dimension 16 as a source premise; it does not silently infer that dimension from the 27 lambda nodes. The internal carrier and the lambda function are separately typed objects.

## C20.05-W1 — The image basis and uniform restriction

Every image output is a sum of vectors eᵢ⊗fᵣ⊗hₙ. There are 16×3×1=48. They are independent: projecting onto any internal-family address reads exactly its coefficient of hₙ, so a zero sum forces each coefficient to vanish. This proves rank 48 under the declared assumptions. Qₙ²=I₁₆²⊗I₃²⊗qₙ²=Qₙ and Qₙ†=Qₙ follow factor by factor.

Fix a family r. The restriction still permits 16 internal choices and one history direction. Its rank is 16, while its history occupancy count is one. Across families those history counts form (1,1,1). It would be incorrect to call each entire family restriction rank one, or to call (1,1,1) a measured density. The same history projector acts for every r because the middle factor is I₃.

The source also states QₙQₘ=0 for n≠m and common history transport. Orthogonality between different n additionally requires qₙqₘ=0; rank one alone does not imply it. For example two identical rank-one q factors would have nonzero product. We preserve the source's assertion and its necessary condition without claiming a fresh replay of the transported history construction.

## C20.05-P1 — Practice and worked answers

For an explicitly finite teaching history carrier with addresses h₀,h₁,h₂, set q₀=diag(1,0,0), q₁=diag(0,1,0), q₂=diag(0,0,1). For this teaching example only, set q₃=0: there is no fourth history address. Find the rank of I₂⊗I₃⊗q₁, then I₂⊗I₃⊗q₃. What would a rank-two history projector do in the source-sized product?

Answers: The first has dimension 2×3×3=18 and rank 2×3×1=6. Its image basis is (i,r,h₁), so each family has two internal image states and one history direction. The second is the zero map with rank 0; it does not satisfy the nonzero rank-one premise. A rank-two history factor yields 16×3×2=96, provided the history space has at least two independent directions. These alternatives show why the assumptions are essential. They do not modify the source's qₙ definition.

> Claim scope: The factorization and occupation wording come from S02#/backbone_sequence/15, S02#/proof_nodes/78 (F038), and S02#/proof_nodes/81 (X033). Conditional rank arithmetic is freshly derived here. F038 reports exact simultaneous occupation for a common history projector; its D10 shared guard says “No physical occupation conclusion.” S03#/findings/6 (AUD-007) directs recovery of the selection proof and conditional removal of the obsolete guard. Keep all these records together. The mathematical image construction and its identification as the physical occupied carrier have distinct premises; lesson 6 addresses the latter.

## Diagnostic checks

1. **C20.05-D1:** Which factor gives uniform treatment of the family labels, and what further identification is needed for a physical occupation conclusion?
2. Does “rank one” by itself imply orthogonality of qₙ and qₘ?
3. If H=4, what are the source-sized product's ambient dimension and selected rank?
4. What data must be retained when applying Qₙ to an arbitrary finite input x?

Worked answers: (1) I₃; one must connect the actual physical-state carrier to the declared image with the required selection premises. (2) No: equal rank-one projectors are a counterexample; qₙqₘ=0 must be supplied or proved. (3) Ambient dimension 192; rank 48. (4) Keep Qₙx and (I−Qₙ)x, with their address convention and reconstruction x=Qₙx+(I−Qₙ)x. Uniform rank is not permission to discard the complement.

Next dependency: [Lesson 6](lesson-06.md) traces the source's occupation conclusion and its correction record.
