# Lesson 6 — Local symmetry and physical role

Essential question: What must be supplied before an abstract symmetry becomes a rule acting on specified objects?

Goals: Name a group, carrier, and action separately; apply and invert two local phases; distinguish an invariant from an evolution rule.

Prerequisite bridge: Lesson 5 defined groups and maps, while Lesson 2 taught matrix actions and inverses. Now we distinguish the labels being composed from the objects they transform. One period is allocated.

## C14.06-E1 — A group needs an action

An abstract group specifies elements and composition. An action additionally tells how each element transforms each carrier element. Write ρ(g)v for this rule. It must satisfy ρ(identity)v=v and ρ(gh)v=ρ(g)(ρ(h)v). These equations say the action respects composition. The same group may have different actions. For U(1) on a single complex coordinate, ρ₁(z)v=zv and ρ₂(z)v=z²v both satisfy these equations. But i sends 1 to i in the first and to −1 in the second. In the second action −1 acts as identity, while in the first it does not. A group name alone therefore does not determine the action or its invisible elements.

A global phase on two nodes uses the same phase at both positions: (v₁,v₂)↦(zv₁,zv₂). A local choice allows independent phases z₁,z₂, so (v₁,v₂)↦(z₁v₁,z₂v₂). Here a node is just a labeled position in a toy model, not a detector observation. The local group is U(1)×U(1), with carrier ℂ² and action ρ(z₁,z₂)=diag(z₁,z₂). Composing two choices multiplies phases node by node. The inverse conjugates each phase. Squared norm |v₁|²+|v₂|² is preserved, as is each individual squared modulus.

“Local” tells where a transformation may vary. It does not say how values evolve with time or how nodes interact. An evolution rule would tell how a state changes between times; a coupling rule would relate different nodes. Neither follows from the norm calculation alone. A physical-role record must say what the coordinates represent, how the action is used, and what observational or dynamical rule connects them to a system. In a gauge interpretation, transformations may relate descriptions of one physical state; that interpretation is an additional contract, not a conclusion from matrix size.

## C14.06-W1 — Worked example

Choose carrier (v₁,v₂)=(1,1) and local phases (i,−i). The matrix diag(i,−i) gives (i,−i), squared norm 1+1=2. The inverse diag(−i,i) gives ((−i)i,i(−i))=(1,1). Choosing the global phase i instead gives (i,i). Both preserve norm but are different transformations of this input. The record must retain the two node labels and their two phase choices.

## C14.06-P1 — Answered practice

On (2,i), apply phases (−1,i). Output is (−2,−1), with squared norm 4+1=5 matching the input. Inverse phases (−1,−i) return (2,i). Record: group U(1)×U(1); carrier ℂ² with node order 1,2; action diag(z₁,z₂); invariant squared norm; inverse diag(z̄₁,z̄₂). The amplitudes and phase parameters suffice to replay either direction. For the single-node actions above, z=−1 sends v=2 to −2 under ρ₁ and to 2 under ρ₂, an explicit distinction even though the abstract group is the same.

> Claim scope: These node calculations are synthetic mathematical models. The source's typed-role rule (S02 /typed_conventions/logic) forbids identifying physical roles merely from an abstract group isomorphism. We assert no measured field, force, coupling, or time-evolution law from these examples.

## Diagnostics — C14.06-D1

1. Apply local phases (i,1) to (1,2) and invert.
2. Are ρ₁ and ρ₂ above the same action? Demonstrate with z=i,v=1.
3. Does preserved norm tell us how one node affects another? What extra rule is needed?
4. If only total norm 5 is saved from the practice example, can the amplitudes and phases be recovered?

Worked answers: (1) Output (i,2); inverse phases (−i,1) restore (1,2); norm stays 5. (2) No: outputs i and −1 differ. (3) No; a coupling or evolution rule must specify the relationship. (4) No: (√5,0), (2,i), and many other states share that norm. Retain the complex amplitudes, node ordering, and phase choices instead of replacing them by the scalar norm.

Next dependency: [Lesson 7](lesson-07.md) applies the same distinction between a mathematical construction and a wider physical-role claim when reading sources.
