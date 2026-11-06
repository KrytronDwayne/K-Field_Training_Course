# Lesson 06 — Closure and admitted sectors

**Essential question:** What does checking every sector mean when the domain itself is an input?

**Goals:** Evaluate the rational charge formulas; test the dual-charge contract; audit closure over an explicit sector list.

**Prerequisite bridge.** Lessons 04–05 define complete phase packets and a scalar reading. We now attach those packets to sectors, meaning distinct labeled cases allowed by a declared domain. Fractions are sufficient for the charge arithmetic. Period 1 covers the charge contract; period 2 covers sector ledgers and missing-input tests.

## C19.06-E1 — A domain and a pairing

The source's determinant lock is written `ell:det E_3 tensor det E_2 -> 1` and `c=c_1(E_2)=-c_1(E_3)`. Recognition card: E_3 and E_2 name source carriers, det names their determinant lines, ell names the lock, and c_1 names the first topological class; the final 1 denotes the trivial target line. This states a relation between the two classes. It is not the same as assigning six scalar phases. We read the architecture but do not construct these topology carriers from a scalar triangle.

For the finite arithmetic contract take integers A_3,A_2,C and define

n_3=A_3+C/3,  n_2=A_2+C/4,  n_1=C/72.

These n values are dimensionless charge coordinates, not lengths. Here C is an integer coordinate; it is not the operator C in the action or the complex numbers, denoted ℂ. Integers are whole numbers including negatives and zero. The allowed n triples form a lattice in the sense used here: integer combinations of fixed generating triples. Expand n=A_3(1,0,0)+A_2(0,1,0)+C(1/3,1/4,1/72).

A dual charge d=(d_3,d_2,d_1) is tested by the contract: d_3,d_2 are integers and h=d_3/3+d_2/4+d_1/72 is an integer. “Dual” here means it pairs integrally with every n under this contract. Define the pairing by multiply-and-add:

〈d,n〉=d_3 n_3+d_2 n_2+d_1 n_1=A_3 d_3+A_2 d_2+C h.

The right side is an integer if the contract holds, because sums and products of integers remain integers. This derivation proves the finite arithmetic implication, not the physical admissibility of all these coordinates. A proposed d can fail the contract even if it pairs integrally with one chosen n.

## C19.06-W1 — Two routes to one pairing

For d=(1,0,48), h=1/3+48/72=1. For d=(0,1,54), h=1/4+54/72=1. For d=(1,1,30), h=(24+18+30)/72=1. For d=(1,1,−42), h=(24+18−42)/72=0. All have integer d_3,d_2 and pass.

Take A_3=1,A_2=0,C=3. Then n=(1+1,0+3/4,3/72)=(2,3/4,1/24). With d=(1,1,30), direct pairing gives 2+3/4+30/24=2+3/4+5/4=4. The expanded route gives A_3 d_3+A_2 d_2+C h=1+0+3=4. Agreement checks the arithmetic independently.

For the closure audit, suppose the admitted list is explicitly {a,b}; this is a **synthetic assumption**, not a source classification. Set τ(E_a)=τ(E_b)=1. Assign sector a the six phases (i,i,−1,−i,i,1), and sector b (i,i,−1,−i,i,−1). Their scalar products are 1 and −1. Closure over {a,b} fails at b. Retain residuals Φ−1 equal to 0 and −2 respectively. If b's final factor were unavailable, its result would be undetermined, not automatically 1 or −1.

## C19.06-P1 — Guided practice

Let A_3=0,A_2=1,C=4. Find n and its pairing with d=(0,1,54). Test candidate d=(1,1,0). Then audit an admitted list {a,b} using the two complete six-factor rows just above; explain the status if only a was checked.

**Worked answer:** n=(4/3,2,1/18). Pairing is 0·4/3+1·2+54/18=5; the expanded route gives 0+1+4·1=5. Candidate (1,1,0) has h=1/3+1/4=7/12, not an integer, and fails. For the sector ledger, a closes and b does not; both remain admitted by the supplied assumption. Checking only a leaves b unchecked and cannot establish “every admitted sector.” Failure does not authorize deleting b from the domain.

> **Claim scope.** S02 M15 states the determinant-lock/topology formulas and closure in every admitted sector. S03 flags missing replay objects. The integer assumptions are explicit here, and the two-sector list is synthetic. The source's quotient discussion is not a proof that the accepted integration uniquely forces a particular global form: the admitted global-form family Z1,Z2,Z3,Z6 remains separate. Compiler module numbers are not mathematical-backbone module numbers.

## Diagnostics

1. **C19.06-D1:** Does passing the dual contract establish physical admissibility?
2. Why does h=7/12 fail even though it is a well-defined fraction?
3. With C=0,A_3=1,A_2=0, candidate d=(1,1,0) pairs to 1. Has it now passed the dual contract?
4. What must be recorded if a sector's cap factor is missing?

**Worked answers:** (1) No. It establishes arithmetic membership under a declared contract; physical sector selection requires its own input. (2) The condition is integrality, not just existence. (3) No: one n gives an integer but the all-n condition still fails at h=7/12. (4) Mark cap unavailable, retain known factors, τ and sector definition, and leave closure undetermined. Do not infer cap from a desired closure value.

**Next dependency:** [Lesson 07](lesson-07.md) classifies every premise and locates incomplete inputs.
