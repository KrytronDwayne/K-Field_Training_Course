# Lesson 04 — History projectors

**Essential question:** When does selecting parts of a history produce a complete, nonoverlapping ledger?

**Goals:** Construct four finite q_n maps; verify self-adjointness, idempotence and orthogonality; reconstruct a vector with its zero coordinates retained.

**Bridge:** TT† in Lesson 03 selected the reachable coordinates. We now select one chain position at a time, using the same three-state S from Lesson 02. No new physical data enter.

**Pacing:** 55 minutes: retrieval 5, teaching/example 20, practice 15, diagnostics/repair 15.

## C18.04-E1 — Selection that stabilizes

A projector satisfies P²=P: selecting twice does the same as selecting once. This is idempotence. An orthogonal projector also satisfies P†=P, called self-adjointness. These two conditions must both be checked; idempotence alone does not guarantee orthogonal selection. Two orthogonal projectors are mutually orthogonal if their product is zero: the selected subspaces do not overlap. For self-adjoint projectors, checking one order suffices, since taking the adjoint gives the other order.

Let P_0=diag(1,0,0) select the root. Define q_n=S^n P_0(S†)^n for n=0,1,2,… . A power means repeated composition, and the zero power is I. Read right to left: move back n steps, keep the root, move forward n steps. The rank of a projector counts available selected directions, not the number of nonzero entries in one particular output.

## C18.04-W1 — Walk the selection along the chain

For v=(x,y,z), q_0v=(x,0,0). For q_1, first S†v=(y,z,0); P_0 keeps (y,0,0); S moves this to (0,y,0). For q_2, (S†)²v=(z,0,0); P_0 keeps it; S² gives (0,0,z). Three backward steps give zero, so q_3=0.

Thus q_0=diag(1,0,0), q_1=diag(0,1,0), q_2=diag(0,0,1), q_3=diag(0,0,0). Their ranks are 1,1,1,0. Transpose leaves each diagonal unchanged. Squaring a 0 or 1 leaves it unchanged, so q_n²=q_n. Multiplying different diagonals gives zero in each position, so q_nq_m=0 for n≠m. The first three sum to I_3.

For (1,2,3), the outputs are (1,0,0),(0,2,0),(0,0,3), and the zero vector. Adding them returns (1,2,3). Their squared norms are 1,4,9,0, which sum to 14, the original squared norm. This arithmetic checks completeness as well as disjointness.

## C18.04-P1 — Keep a zero output

Compute all q_n outputs through n=3 for (−1,4,0). State their ranks, verify q_1²=q_1 and q_1q_2=0, and reconstruct the vector.

**Worked answer:** The four outputs are (−1,0,0),(0,4,0),(0,0,0),(0,0,0). The projector ranks remain 1,1,1,0: q_2 can select a nonzero terminal input even though this particular input has terminal coefficient zero. Diagonal multiplication gives q_1²=diag(0,1,0), and q_1q_2=diag(0,0,0). Adding all four stored outputs gives (−1,4,0). Keep labels q_2 and q_3 to distinguish a zero coefficient from a zero operator.

> **Claim scope:** S02#/backbone_sequence/13 states q_n=W^n P_Π(W†)^n and imposes that P_Π lies in the root defect space for the orthogonality assertion. For an isometry W the root defect is the missing output subspace, ker W†. Our P_0 is in the corresponding root direction of the finite toy. A generic P is not interchangeable with P_0. For example P=I_3 gives q_0=I_3 and q_1=SS†=diag(0,1,1); q_0q_1 is nonzero. Finite verification cannot remove the source hypothesis.

## Diagnostic checks

1. **C18.04-D1:** What source condition prevents arbitrary replacement of P_Π? Give the toy counterexample above in your own words.
2. Compute q_2² and q_0q_2.
3. Is rank q_2 zero when q_2(−1,4,0)=0?
4. If only q_0v and q_1v are saved for v=(2,−1,7), what must be retained to reconstruct v?

**Worked answers:** (1) The selected subspace must lie in the root defect for the stated wandering construction. P=I makes selections overlap. (2) q_2²=diag(0,0,1)=q_2; q_0q_2=0. (3) No, rank is 1; the single input happens to have coefficient zero there. (4) Retain q_2v=(0,0,7), and preserve q_3's zero label. Then (2,0,0)+(0,−1,0)+(0,0,7)=(2,−1,7).

**Next dependency:** [Lesson 05](lesson-05.md) adds an orientation ledger so signs and order survive geometric changes as well as coordinate selections.
