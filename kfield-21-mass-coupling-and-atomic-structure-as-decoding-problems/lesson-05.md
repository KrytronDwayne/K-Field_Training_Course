# lesson-05: Atomic and isotope inventories

3 sessions of 55 minutes.

**Essential question:** Which atomic labels must be fixed before two masses can be compared?

**Goals**

- Compute a nominal composition label and verify allowed endpoint counts.
- Test dependent and independent composition-preserving moves.
- Balance synthetic constituent and charge ledgers before applying a mass-energy conversion.

## Prerequisite bridge

Lessons 1–4 taught linear maps and reconstruction. Composition counting is another linear map, but its inputs have different meanings: atom counts rather than decoder coefficients. Do not identify the two spaces merely because both use tuples.

<a id="C21.05-E1"></a>
## Explanation — C21.05-E1

An element identifies a nucleus by its proton count. Isotopes of the same element have different neutron counts. A neutral atom has equal numbers of electrons and protons; removing an electron makes its charge one elementary charge more positive. A molecular formula counts constituent atoms. An isomer has the same formula but a different arrangement. These labels answer different questions, so a report keeps them in separate fields.

Declare the order (C,H,N,O), where each letter is the count of carbon, hydrogen, nitrogen or oxygen atoms. S05 R008 defines nominal V=12C+H+14N+16O. For (4,4,0,1), V=12 times 4+4+14 times 0+16=68. The source calls the label nominal Da; here we say nominal units to distinguish the arithmetic from exact isotope masses. It is not a physical geometric volume despite the symbol V. Negative counts cannot describe an endpoint formula, though signed differences between valid formulas can be useful.

A fiber is the set of inputs sharing one output value. Different compositions can lie in the same V-fiber. A move U is an integer difference tuple; V stays fixed precisely when its weighted sum is zero. For U1=(-1,-2,1,0), the weighted sum is -12-2+14=0. For U2=(1,4,0,-1), it is 12+4-16=0. For U3=(0,2,1,-1), it is 2+14-16=0. But U1+U2=U3 entry by entry, so these are only two independent directions. U1 and U2 are independent because the N entry forces the coefficient of U1 to vanish in a zero combination, after which U2’s O entry forces its coefficient to vanish.

The move K=(-4,0,0,3) also preserves V because -48+48=0. It cannot equal aU1+bU2: its N entry would force a=0, its H entry then forces 4b=0, leaving no C change. K adds a third direction. One constraint on four real coordinates leaves three independent directions; integer-lattice basis questions still require more than a rank count. These moves establish independent directions, not automatically a full integer basis.

Starting from (4,4,0,1), U1 gives (3,2,1,1), whose label is 36+2+14+16=68. U2 gives (5,8,0,0), whose label is 60+8=68. K sends (4,0,0,0) to (0,0,0,3); both labels are 48. Attempting K from (1,0,0,0) would give (-3,0,0,3), an invalid endpoint. A nominal count move is not automatically a physically balanced reaction: carbon and oxygen nuclei are different constituent types.

### Before subtracting endpoint masses

For a synthetic assembly A+B → AB, declare conserved labels A and B. Initial inventory is one A label and one B label; final AB contains exactly those same labels. Declare all three objects neutral and in the specified reference state, so total charge is zero on both sides. Declare each listed mass to include the entire object and its electrons and binding state. Isotopic identities are stipulated unchanged constituents, not inferred from nominal integer weights. There is no emitted unlisted object in this classroom ledger.

Use the reference relation Q_release=(m_initial-m_final)c_light². The symbol c_light is the speed entering mass-energy conversion, not the coefficient vector c. Positive Q_release means energy available by this endpoint difference; negative Q_release means required energy input under the convention. For classroom arithmetic stipulate a synthetic conversion of 1 u times c_light²=10 E_unit. This is not the physical numerical conversion for an atomic mass unit; u here is a declared mass unit in the synthetic problem.

With complete-object masses A=2u, B=3u, AB=4.9u, initial mass is 5u. Subtract final mass to retain delta m=0.1u. Multiply by 10 E_unit/u to get Q_release=1 E_unit. Setting AB=5.05u changes delta m to -0.05u and Q_release to -0.5 E_unit. The latter requires input of 0.5 E_unit; do not erase the sign or normalize it away.

If the initial masses include electrons but the final mass describes a bare positive ion, this ledger is incomplete. Specify the removed electron and consistent binding/ionization states before subtracting; a missing mass cannot be guessed. Even equal formulas can represent different binding states or isomers.

> Source scope: S05 /records/7 is archive_stated nominal composition arithmetic. /records/21 reports dependence of three tested moves; /records/22 reports the independent 4C↔3O direction and a mass-step claim of 15.25614129 mDa (one mDa is one thousandth of a dalton). That decimal and its source claim of exactness are attributed synthesis, not a fresh isotope-mass replay: the required isotope constants and full endpoints have not been loaded. We freshly verify nominal invariance and independence only. R032’s three rank-three structures do not supply a canonical connecting map.

<a id="C21.05-W1"></a>
## Worked example — C21.05-W1

C21-RXN-EX1: synthetic A+B -> AB conserves stipulated A and B constituent counts and charge. All are complete objects in one reference convention. Masses 2u+3u ->4.9u with synthetic 1u c^2=10 E_unit give delta m=0.1u and Q=1 E_unit. The mass difference is retained; this is not a measured reaction.

<a id="C21.05-P1"></a>
## Guided practice — C21.05-P1

Try the operation before reading the solution. C21-RXN-P1: keep every endpoint label but set final mass 5.05u. Delta m=-0.05u and Q=-0.5 E_unit, requiring input 0.5 E_unit. Separately calculate V for (C,H,N,O)=(4,4,0,1): V=68 nominal units. Neither calculation identifies an isomer.

<a id="C21.S02-E1"></a>
## Supplemental explanation — C21.S02-E1

Declare tuple order (C,H,N,O) and weights (12,1,14,16). Use U1=(-1,-2,1,0), U2=(1,4,0,-1), U3=(0,2,1,-1), K=(-4,0,0,3). Check nonnegative endpoints separately. The weights are nominal composition arithmetic, not exact isotope masses.

<a id="C21.S02-W1"></a>
### Worked example — C21.S02-W1

All four weighted moves are zero and U3=U1+U2. Starting (4,4,0,1), U1 gives (3,2,1,1), both V=68. The first three moves have rank two. If K=aU1+bU2, the N row forces a=0 and the H row b=0, a contradiction; K adds a third direction.

<a id="C21.S02-P1"></a>
### Practice with answer — C21.S02-P1

From (4,4,0,1), U2 gives (5,8,0,0), both V=68. From (4,0,0,0), K gives (0,0,0,3), both V=48. Explain why these are valid count endpoints but not an asserted physical carbon-to-oxygen reaction. S05 R023 reports a 15.25614129 mDa step as source synthesis; no missing isotope constants are invented to replay it.

<a id="C21.S02-D1"></a>
### Diagnostic boundary — C21.S02-D1

Negative atom counts invalidate an endpoint. Same V does not mean same formula, isotope mass, isomer or charge state. The three rank-three fibers in R032 recur structurally, but their canonical connecting map is unresolved.

<a id="C21.05-D1"></a>
## Diagnostic checks — C21.05-D1

1. Calculate V for (3,2,1,1), and compare it with (4,4,0,1).
2. Show U3=U1+U2 and explain why K supplies another direction.
3. Apply K to (1,0,0,0). Is this a valid composition endpoint?
4. For the neutral synthetic A+B → AB, calculate Q if final mass is 5.05u.
5. What must be repaired if a final positive ion is compared with initial neutral masses?

## Worked answers

1. 36+2+14+16=68, equal to 48+4+16=68. The formulas differ despite their common label.
2. The sum is (0,2,1,-1). If K=aU1+bU2, N forces a=0 and H forces b=0, contradicting K≠0.
3. The result (-3,0,0,3) has a negative C count and is invalid, though K remains a formal kernel direction.
4. 5-5.05=-0.05u; multiplying by the declared 10 E_unit/u gives -0.5 E_unit. Input 0.5 E_unit is needed.
5. Include removed electrons and consistent charge, isotope and binding/reference states for all whole objects; until supplied, mark the endpoint incomplete rather than compute an unsupported difference.

**Boundary to carry forward:** C21-RXN-D1: initial neutral-object masses and final bare-ion masses cannot be subtracted under an unstated electron convention. Supply all electrons and ionization/binding states first, or mark the endpoint incomplete. A nominally invariant composition move is not by itself a balanced physical reaction.

**Next dependency:** [lesson-06](lesson-06.md). Use this lesson’s reconstruction and scope checks there.
