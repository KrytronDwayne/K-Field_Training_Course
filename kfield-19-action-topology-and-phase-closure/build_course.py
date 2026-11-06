"""Authoring and recovery utility; all output remains beside this script."""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parent
packet=json.loads((ROOT/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(name,text):
    (ROOT/name).write_text(text.strip()+'\n',encoding='utf-8')
def dump(name,obj):
    write(name,json.dumps(obj,indent=2,ensure_ascii=False))
def sha(name): return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
LESSONS={}
LESSONS[1]=r'''
# Lesson 01 — An action as a complete mathematical specification

**Essential question:** What must be supplied before an action can be evaluated?

**Goals:** Identify variables and coefficients; specify domains and boundaries; check the units of a finite action.

**Prerequisite bridge.** You can subtract numbers, square them, and substitute into a formula. Courses 16–18 prepare carrier and transport language; this lesson supplies the finite bridge needed here. A state is a list of values describing a system at a chosen time. A path is an ordered list of states. Changing their order changes the increments, even when the same numbers appear.

## C19.01-E1 — A formula plus its contract

An action assigns one number to an entire path. It needs more than an expression: we must know the state, times, coefficient values and units, allowed inputs (the domain), boundary values, and the evaluation convention. A coefficient is a supplied multiplier. A constitutive rule is a chosen rule connecting quantities in a model. We will evaluate such a rule, not derive its physical selection.

Our **synthetic** state q is dimensionless. Write q_0, q_1, q_2 for three ordered samples. Subscripts name positions in the list, not powers. There are two intervals, indexed j=0 and j=1. Let Δt be their common positive duration. Define v_j=(q_(j+1)−q_j)/Δt. This is a finite rate of change, measured in inverse time units. AU means an abstract action unit; TU means an abstract time unit. Neither is an experimentally calibrated unit here.

The toy rule is

S = Σ_(j=0 to 1) Δt [ (k/2)v_j² − (vpot/2)q_j² ].

Σ means add one copy for each listed j. The potential uses the **left endpoint** q_j; the final q_2 is used in the final rate but not as a left endpoint. We allow real q values, Δt>0, k>0 and vpot>0. Endpoints q_0 and q_2 are fixed when comparing paths in the same boundary problem. The middle value is an interior state coordinate.

## C19.01-W1 — Unit and input ledger

Take Δt=1 TU, k=2 AU·TU, vpot=2 AU/TU, and path (0,1,3), with q_0=0 and q_2=3 fixed. A rate has units 1/TU, so k v_j² has units AU/TU. The potential vpot q_j² also has units AU/TU. Multiplying each by Δt gives AU; subtraction and addition are therefore permitted. The state ledger has three values, the time ledger t=(0,1,2) TU, and the interval ledger has two entries. Lesson 02 evaluates them. Specifying only the three q values would leave the action undetermined.

## Source-reading card: four terms, not the toy rule

S02, `/backbone_sequence/14/action`, records

`S_K[q]=int d tau sum_L {mu_L/2 dot(q_L)^T M dot(q_L)-kappa_K/2 tr(M Q_L R Q_L^T)-epsilon_K U_K(Cq_L)+s_L^Tq_L}`.

Read the braces as four contributions: a rate-quadratic term, a trace contraction, a potential term, and a linear source term. A vector is an ordered list; transpose T turns a column into a row; a matrix is a rectangular table acting on a vector. A contraction combines matching slots until no free slot remains. A trace adds the diagonal entries of a square table. These are recognition operations here: no matrix calculation is assigned. `int d tau` denotes accumulation over a continuous parameter, while `sum_L` accumulates over labeled carriers. The dot marks a rate with respect to that parameter. Calculus is not required in this course.

The source uses q_L as state and μ_L, κ_K, ε_K as coefficients. M and R are metric/operator symbols whose source-local definitions and units must be resolved; do not equate every M with every metric. Q_L, C, U_K and s_L require typed definitions before replay. U_K is the named potential function, C acts on q_L, and s_L supplies the linear contraction. L labels carriers. These syntactic roles do not supply missing numerical values or full domains. Every brace term must share action-per-parameter units, but the excerpt does not supply a complete calibrated unit assignment. The integral parameter `tau` is distinct from the determinant-line map τ in Lesson 05. Source M15 explicitly retains operator coefficients, boundary-sector values, and time/action normalization as state inputs.

> **Claim scope.** The displayed source expression is an archival fact. Its assertion of typed terms is source-reported. The toy action is a declared teaching model, not that expression with missing parts filled in. S03 `/findings/8` identifies M15 replay gaps, including topology carriers and determinant-line factors. No measured coefficients or physical mechanism are inferred here.

## C19.01-P1 — Guided practice, then compare

For (1,2,2), with the same Δt, k and vpot, list state values, intervals, endpoints and potential convention. Explain what changes if Δt changes.

**Worked answer:** There are three states q_0=1,q_1=2,q_2=2, two intervals, and fixed endpoints 1 and 2 for this boundary problem. The potential reads q_0 and q_1. A changed Δt changes both rates and interval weights, so retaining the old rate values would be incorrect. Changing vpot changes the model coefficient. This path has different boundaries from W1 and is not a competing path with W1's fixed endpoints.

**Source-reading practice:** Using the source card, name all four brace contributions and one input needed before numerical replay. **Answer:** They are the rate-quadratic term μ_L dot(q_L)ᵀM dot(q_L)/2, the negative trace term −κ_K tr(M Q_L R Q_Lᵀ)/2, the negative potential term −ε_K U_K(Cq_L), and the positive linear source term s_Lᵀq_L. A complete typed coefficient/operator definition with its units is one needed input; boundary-sector values and time/action normalization are others. Naming terms does not provide their missing values.

## Diagnostics

1. **C19.01-D1:** Can the source action be evaluated from its printed formula alone? Name two missing input classes.
2. What are the units of v_j² and k v_j²?
3. Does a list of four samples have four intervals?
4. Why must a right-endpoint potential be declared rather than silently substituted?

**Worked answers:** (1) No: typed operator/coefficient definitions and boundary-sector values are needed, alongside time/action normalization. (2) 1/TU² and AU/TU. (3) No, three adjacent intervals connect four samples. (4) It changes which q value enters each term and generally changes S; the convention is part of the specification.

**Next dependency:** [Lesson 02](lesson-02.md) evaluates and preserves every signed contribution.
'''
LESSONS[2]=r'''
# Lesson 02 — Discrete action accounting

**Essential question:** How can one total retain the information in its signed parts?

**Goals:** Evaluate both interval contributions; reconstruct a total from a model and residual; distinguish action evaluation from a dynamical prediction.

**Prerequisite bridge.** Lesson 01 fixed the state, units, coefficients and left-endpoint convention. We now substitute values. Keep a row per interval: a total alone cannot tell you which interval contributed which sign.

## C19.02-E1 — Compute before compressing

Define K_j=Δt(k/2)v_j² and V_j=Δt(vpot/2)q_j², both in AU. The signed contribution is a_j=K_j−V_j. K and V are names for two model terms; their difference is not a measured transferred energy. For Δt=1 TU and numerical coefficients k=2 and vpot=2 in their declared units, the numerical shortcut is a_j=(q_(j+1)−q_j)²−q_j². This shortcut depends on those inputs and cannot be reused after changing Δt.

A residual records the difference from a declared model: r=S−S_model, so S=S_model+r. A single total residual preserves the total, but cannot recover the interval series. To preserve a path-level decomposition, retain each a_j, each model component m_j, and each r_j=a_j−m_j, so a_j=m_j+r_j. Zero and negative entries remain in the ledger.

## C19.02-W1 — Worked path (0,1,3)

The increments are 1−0=1 and 3−1=2. With Δt=1, the rates have numerical values 1 and 2 per TU. Squaring gives 1 and 4.

| j | q_j → q_(j+1) | K_j (AU) | V_j (AU) | a_j (AU) |
|---|---|---:|---:|---:|
| 0 | 0 → 1 | 1 | 0 | 1 |
| 1 | 1 → 3 | 4 | 1 | 3 |

Therefore S=1+3=4 AU. Independently group the totals: ΣK=5 AU and ΣV=1 AU; 5−1=4 AU. This second route checks the bookkeeping without dropping the row values.

If Δt becomes 2 TU with the same three states and the same physical coefficients, rates become 1/2 and 1 per TU. K becomes (1/2,2) AU and V becomes (0,2) AU. The signed terms are (1/2,0) AU, total 1/2 AU. Slower traversal changed both kinetic accumulation and potential accumulation. Merely doubling 4 would be wrong.

> **Claim scope.** These are exact finite consequences of the synthetic rule. No data were fitted. Evaluating a path is not minimizing over paths, solving an equation of motion, assigning a transition probability, or finding a transition rate. Each of those operations needs its own rule and normalization.

## C19.02-P1 — Guided practice and reconstruction

Evaluate (1,2,2) using the original Δt=1. Retain the two signed contributions. A declared component model is m=(1,−4) AU; calculate the residual vector and reconstruct the total.

**Worked answer:** Increments (1,0) give K=(1,0) AU; left endpoints (1,2) give V=(1,4) AU. Thus a=(0,−4) AU and S=−4 AU. The model total is 1−4=−3 AU. Residuals r=(0−1,−4−(−4))=(−1,0) AU have total −1 AU. Reconstruct row by row: (1,−4)+(−1,0)=(0,−4), and reconstruct the total: −3+(−1)=−4 AU. The zero first contribution does not authorize erasing its kinetic and potential parts, which are both 1 AU.

## Diagnostics

1. **C19.02-D1:** Does S=−4 AU make the calculation invalid or imply negative measured energy?
2. For path (0,1,1), find K,V,a and S with original parameters.
3. If only S=−4 and S_model=−3 survive, can you recover the two residual entries?
4. Can S=4 and S=−4 determine which path is more probable?

**Worked answers:** (1) No. S is a signed action sum in this toy model; it is not a measured energy. (2) K=(1,0), V=(0,1), a=(1,−1) AU, giving S=0 AU. (3) No: their sum is −1, but many pairs share it; preserve the component ledger. (4) No probability rule or scale converting action to a probability has been supplied, and W1/P1 also have different endpoints.

**Next dependency:** [Lesson 03](lesson-03.md) preserves link information while testing a whole loop.
'''
LESSONS[3]=r'''
# Lesson 03 — Topology through loops and boundary data

**Essential question:** Can a change in local coordinates repair a nonclosing loop?

**Goals:** Multiply quarter-turn phases; transform each link under a declared frame convention; distinguish a local frame from a global loop test.

**Prerequisite bridge.** Lesson 02 kept ordered interval contributions. Here we keep ordered links around a triangle. Addition is replaced by multiplication, but the same discipline applies: retain the inputs as well as the total. We teach the small phase arithmetic explicitly even if Course 17 already introduced it.

## C19.03-E1 — Quarter turns and frames

A phase represents a turn. Use 1 for no turn, i for one quarter-turn, −1 for a half-turn, and −i for three quarter-turns. Multiplication combines turns. Four quarter-turns return to 1, so i²=−1, i³=−i and i⁴=1. These are complex numbers; i is defined by i²=−1. For this course the four-element multiplication cycle suffices. In particular i(−i)=1 and (−i)²=−1. An inverse undoes a turn: i^−1=−i, (−i)^−1=i, and (−1)^−1=−1.

Let vertices be a,b,c. U_ab,U_bc,U_ca are scalar links carrying phase data. Our convention is U'_xy=g_x U_xy g_y^−1, where nonzero frame phases g_x specify local coordinates. Declare this convention before calculating; reversing it changes individual transformed links. The closed product is P=U_ab U_bc U_ca. Substitution gives

P'=g_a U_ab (g_b^−1 g_b) U_bc (g_c^−1 g_c) U_ca g_a^−1=g_a P g_a^−1=P.

Adjacent inverse pairs cancel to 1. The last equality uses commuting scalar phases. For source matrix links, the product is conjugated instead; Lesson 07 explains the trace identity used to obtain a scalar invariant. The entire loop must be retained to see cancellation. An open chain retains different endpoint frames.

Topology concerns global connection and loop/boundary structure. This finite triangle teaches a limited global-versus-local distinction; it is not a classification of every possible space. A boundary condition specifies what must agree or what data are fixed at a boundary. A closure test asks whether the complete loop product equals 1 under the declared contract.

## C19.03-W1 — A loop that stays nonclosing

Take links (i,1,i) in ab,bc,ca order. P=i·1·i=−1. Apply frames (g_a,g_b,g_c)=(−1,i,1). Then U'_ab=(−1)i(−i)=−1; U'_bc=i·1·1=i; U'_ca=1·i·(−1)=−i. Their product is (−1)i(−i)=−1. Local coordinates changed each link but did not make the loop close. The closure residual P−1 is −2 both before and after, dimensionless. Keep the original and transformed links, frames and residual; the residual alone does not reconstruct the links.

## C19.03-P1 — Guided practice

Use links (i,−i,1) and the same frames (−1,i,1). Compute each new link and both loop products.

**Worked answer:** Original P=i(−i)1=1. U'_ab=(−1)i(−i)=−1; U'_bc=i(−i)1=1; U'_ca=1·1·(−1)=−1. Thus the new list is (−1,1,−1), whose product is 1. Record the three frames, their inverses and both link lists. Inverting the transformation, U_xy=g_x^−1 U'_xy g_y, reconstructs the original links.

> **Claim scope.** These synthetic scalar examples prove their own finite identities. S02 M13 reports conjugation of closed source transport, and M15 states a phase condition for every admitted sector. Neither one triangle nor a convenient local frame supplies M15's topology carriers, determinant-line data or admitted-sector list. Those requirements remain explicit. Lesson 06 will teach the stated rational charge contract.

## Diagnostics

1. **C19.03-D1:** Does one closed triangle establish M15 closure in every admitted sector?
2. Find (−i)² and i^−1 using turns.
3. Why does U_ab U_bc not have the same endpoint cancellation as the triangle?
4. If a nonclosing loop becomes 1 in someone's calculation after changing frames, what should you check first?

**Worked answers:** (1) No; the full sector domain and determinant-line inputs have not been checked. (2) Two three-quarter turns total six quarters, equivalent to two quarters, giving −1; the inverse of i is −i. (3) The a and c endpoints remain different: U'_ab U'_bc=g_a(U_ab U_bc)g_c^−1. (4) Check the declared link convention, all inverse phases and all three transformed links. P'=P for these scalar loops, so changing P signals a changed input or arithmetic/convention error.

**Next dependency:** [Lesson 04](lesson-04.md) expands the ledger from three links to six named phase contributions.
'''

LESSONS[4]=r'''
# Lesson 04 — Phase factors and their product

**Essential question:** What can disappear from a product without disappearing from the specification?

**Goals:** Compute a six-factor phase product; test factor omission; retain unit-valued contributions and their provenance.

**Prerequisite bridge.** Lesson 03 taught the cycle 1,i,−1,−i and inverse phases. We now use the same multiplication for six contributions. The labels are part of the input: a correct total with a missing label is an incomplete record.

## C19.04-E1 — Six contributions with a declared reading rule

S02 M15 names six determinant-line contributions in this order: **UV, light, reg, heavy, cap, induced**. Here these are source-local labels, not permission to invent numerical physical values. For this finite analogy we choose a basis for each line and a common scalar reading rule called a trivialization, τ. Specifically, τ sends the combined chosen basis to the number 1. Lesson 05 teaches what this means and how it changes under rebasing. This declaration is why, for the present examples, multiplying the six coefficients gives the scalar phase directly.

Write Φ=z_UV z_light z_reg z_heavy z_cap z_induced. Each z is dimensionless, with values drawn from our four quarter-turn phases. Closure for this one specified packet means Φ=1. Multiplying by 1 does not change a number, but a factor whose value is 1 still records that a contribution was supplied and checked. Missing is different from known-to-be-1.

## C19.04-W1 — Multiply without losing the ledger

Our synthetic ordered coefficients are (i,i,−1,−i,i,1). With τ(basis)=1, calculate:

| Contribution | Value | Running product |
|---|---|---|
| UV | i | i |
| light | i | −1 |
| reg | −1 | 1 |
| heavy | −i | −i |
| cap | i | 1 |
| induced | 1 | 1 |

Thus Φ=1. To test deletion of heavy, multiply the remaining five values: i·i·(−1)·i·1=i. Independently divide the complete product by the omitted nonzero factor: 1/(−i)=i. The two routes agree. The omission changed the packet and its closure value. Retain the original factor list and the omission label; a bare result i does not identify which contribution was removed.

The closure residual is ρ=Φ−1. For the complete packet ρ=0; with heavy deleted it is i−1. This is an exact complex difference, not a reason to discard the nonclosing result. Complex differences are written a+bi: i−1=−1+i. We need not convert it to a size score.

## C19.04-P1 — Guided practice

Use (−1,i,i,1,−i,i) in the same label order and the same τ. Find every running product, then delete cap and compare. Explain why heavy stays in the record.

**Worked answer:** Running products are −1,−i,1,1,−i,1. Thus Φ=1. Without cap=−i the product is i, also 1/(−i)=i, with residual i−1. Heavy has value 1, but keeping it records a supplied contribution rather than an absent one. Both the complete and mutated factor lists remain available.

> **Claim scope.** Source M15 describes a tensor product of sections, not six unqualified scalar numbers. Our scalar calculation is valid after the stated basis and τ choice and for this synthetic packet only. A product of 1 neither supplies a global trivialization nor establishes every admitted sector. No physical phase value has been measured here.

## Diagnostics

1. **C19.04-D1:** What does Φ=1 establish for the worked packet, and what remains outside that result?
2. What happens numerically if induced=1 is omitted from W1? Is the record complete?
3. If a missing factor z must satisfy i z=1, find z. May you record it as a recovered source value?
4. What must accompany the residual i−1 for reconstruction of the omitted-factor test?

**Worked answers:** (1) The declared finite scalar product closes; other sectors and global line constructions remain unchecked. (2) The value stays 1, but the record is incomplete. (3) z=−i solves the equation, but this is a conditional algebraic requirement, not evidence of the source factor's value. (4) Keep the original factors, mutation label, basis/trivialization and computed product. Adding 1 to the residual recovers the product, not the individual factors.

**Next dependency:** [Lesson 05](lesson-05.md) explains why the chosen bases and τ cannot be omitted.
'''
LESSONS[5]=r'''
# Lesson 05 — Determinant-line bookkeeping

**Essential question:** How can a coefficient change while the represented object and its scalar reading stay the same?

**Goals:** Distinguish a line element from its coefficient; apply a one-factor basis change; recover the same scalar using the retained trivialization.

**Prerequisite bridge.** Lesson 04 declared six bases and τ. A familiar number-and-unit expression such as “2 units” separates the amount from the chosen unit. We now use a similar separation for a one-dimensional complex line. This is two periods: first learn one line and the tensor basis, then practice rebasing and scope checks.

## C19.05-E1 — From one line to a tensor product

A complex line is a space in which each element can be written z e, where e is a chosen nonzero basis element and z is a complex coefficient. “One-dimensional” means one such basis element suffices; it does not mean only real coefficients are allowed. Let s=z e. Choose another basis e'=a e, with a≠0. To keep s unchanged, its new coefficient must be z'=z/a, since (z/a)(a e)=z e. This is a change of description, not a change of s.

To combine six lines we use a tensor product, written ⊗. At the level needed here, take the ordered composite basis

E=e_UV⊗e_light⊗e_reg⊗e_heavy⊗e_cap⊗e_induced.

Its rule is that coefficients multiply: (z_1 e_1)⊗...⊗(z_6 e_6)=(z_1...z_6)E. Thus S_total=Z E, where Z is the product of six coefficients. S_total here denotes a combined line element, not the action S from Lessons 01–02. In the source the objects s_label are sections: assignments of line elements over their domain. Our calculation concerns a single specified point/packet, not a whole varying family.

A trivialization τ turns a line element into an ordinary complex number consistently and linearly. Linearity means that τ preserves addition and scalar multiplication: τ(s+t)=τ(s)+τ(t) and τ(zE)=z τ(E). The second rule is the one used in our rebasing calculations. Declare τ(E)=1 initially. The scalar reading is Φ=τ(S_total)=Z τ(E). After rebasing, **the same map τ** may give a different number on the new basis. Forgetting this is the error we will test.

The source calls these determinant lines. Recognition only: for a finite square transformation, its determinant records its signed volume scaling; a determinant line packages the associated top-degree volume coordinate into a one-dimensional space. This motivates line bookkeeping but does not construct the source's determinant lines or their global sections. No determinant computation or exterior-algebra proof is required here.

## C19.05-W1 — Change the UV basis

Start with W1 of Lesson 04: coefficients (i,i,−1,−i,i,1), Z=1, τ(E)=1, Φ=1. Set e'_UV=i e_UV and leave other bases unchanged. The UV coefficient becomes i/i=1, and E'=iE. The new coefficient list is (1,i,−1,−i,i,1), whose product is Z'=−i. Directly, Z'=Z/i=−i. Meanwhile τ(E')=τ(iE)=iτ(E)=i. Therefore Φ'=Z'τ(E')=(−i)i=1. Also S_total=Z'E'=(−i)(iE)=E, so the element itself is unchanged.

This calculation retains three layers: six local coefficients, the combined tensor-basis coefficient, and the scalar reading under τ. Reporting only Z'=−i would falsely suggest that the physical scalar in the toy had changed.

## C19.05-P1 — Guided practice

Use Lesson 04's practice list (−1,i,i,1,−i,i). Rebase e'_cap=−e_cap. Compute the cap coefficient, combined coefficient, τ(E'), scalar and inverse reconstruction.

**Worked answer:** The cap coefficient becomes (−i)/(−1)=i. Thus the new list is (−1,i,i,1,i,i), with product −1. E'=−E and τ(E')=−1. The scalar is (−1)(−1)=1. To reconstruct the old cap coefficient multiply i by −1, obtaining −i; the old basis is −e'_cap. Keep both lists, the multiplier −1 and τ values, so the change is reversible.

> **Claim scope.** S02 `/backbone_sequence/14/determinant_line` supplies the six-factor architecture and the need for τ. Our finite line rules are declared and checked directly. The source's global existence question cannot be settled by choosing a basis in one example. The source's time parameter τ in its action is a different object; here τ is a map, never a duration.

## Diagnostics

1. **C19.05-D1:** Why is multiplying six coefficients alone insufficient after changing bases?
2. If s=2e and e'=−e, what is the new coefficient? Reconstruct s.
3. In W1, what wrong answer results from keeping τ(E')=1?
4. Does a local basis change require changing the represented section value?
5. Which record would permit an auditor to reverse P1?

**Worked answers:** (1) The scalar is Z'τ(E'), so the basis reading must be retained. (2) −2, because (−2)(−e)=2e. (3) −i, whereas the correct invariant scalar is 1. (4) No, coefficients compensate for the basis change; a genuine change in the section would be additional input. (5) Original and new coefficient lists, cap's basis multiplier −1, the ordered tensor basis and τ(E)=1, τ(E')=−1. A final scalar 1 alone loses this information.

**Next dependency:** [Lesson 06](lesson-06.md) applies complete phase ledgers to specified sectors.
'''
LESSONS[6]=r'''
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
'''
LESSONS[7]=r'''
# Lesson 07 — A complete premise ledger

**Essential question:** Which parts of a result were supplied, chosen, or proved?

**Goals:** Classify five premise roles; build a complete action/phase ledger; identify missing replay inputs without inventing them.

**Prerequisite bridge.** The earlier lessons supplied all finite operations: action substitution, residual reconstruction, frame changes, phase products, tensor-basis reading and charge pairing. This lesson organizes those dependencies so that a numerical result cannot conceal a missing premise.

## C19.07-E1 — Five roles and an evidence column

A **locked root** is an input held fixed by the chosen source/version, such as the locked Cell3 geometry. A **theorem** is an implication derived from stated premises, such as integral pairing under Lesson 06's contract. A **constitutive rule** specifies how a model combines quantities, such as our chosen finite action. A **domain condition** restricts allowed cases, such as Δt>0 or a declared admitted-sector set. A **state coordinate** gives a value within that domain, such as q_1 or a boundary value. Roles concern use in an argument; they are not measures of truth. The same numerical coefficient can be a supplied state/model parameter while its positivity is a domain condition.

Keep evidence status separately: source fact, freshly checked finite implication, declared teaching assumption, interpretation, proposed mechanism, reference-theory comparison or unresolved input. Calling a sentence a theorem in an archive does not show that its proof has been loaded and replayed. A ledger row should include object, role, value or restriction, units/type, source pointer or example ID, and verification status.

The named trace-conjugation identity provides a small bridge from Lesson 03. For a square table A, Tr(A) is the sum of diagonal entries. Matrix multiplication uses (AB)_ij=Σ_k A_ik B_kj. Thus Tr(AB)=Σ_iΣ_k A_ik B_ki=Σ_kΣ_i B_ki A_ik=Tr(BA), because finite scalar sums may be reordered. If G has an inverse, Tr(GPG^−1)=Tr(PG^−1G)=Tr(P). This is a finite derived identity with a stated invertibility condition. It does not certify an unavailable source operator. No numerical matrix problem is assigned.

## C19.07-W1 — Classify a packet

| Object | Role in this argument | Scope and retained record |
|---|---|---|
| Source M_cell=BᵀB | Locked geometric input | Locked basis/version; not a numerical toy coefficient |
| Trace conjugation | Derived finite theorem | Finite square matrices and invertible G; derivation above |
| Toy action S=Σ(K−V) | Constitutive rule | Synthetic, left-endpoint convention |
| k>0,vpot>0,Δt>0 | Domain conditions | Restrict toy input values |
| k=2 AU·TU,vpot=2 AU/TU,Δt=1 TU | Supplied model/state inputs | Values retained independently of their positivity |
| q=(1,2,2) | State coordinates | Ordered values; endpoints fixed at 1 and 2 |
| a=(0,−4),m=(1,−4),r=(−1,0) AU | Derived finite records | a=m+r; retain each vector |
| Six labeled phases from P1 | State inputs in declared bases | UV,light,reg,heavy,cap,induced all retained |
| τ(E)=1 | Declared reading rule | Combined line basis and τ are part of specification |
| Admitted set {a,b} | Domain condition | Synthetic membership assumption |
| Boundary-sector values | State coordinates | Values within the declared domain, not its membership rule |

Locked geometry notation remains typed: M_cell is the Cell3 Gram metric and R_cell its inverse; G_phase and G_eff are distinct phase/effective metrics. B is the ordered source-locked basis; any row/column representation must be stated. This course performs no geometry substitution. If such a substitution is later added, preserve the ICRS columns [a b c], negative determinant, half-open cells and affine origin; an action symbol M alone does not authorize silently replacing it by a convenient metric.

## C19.07-P1 — Guided missing-input audit

A packet supplies q, k, vpot and five phase values, but omits induced, Δt, τ and the admitted-sector list. Can you finish it by assuming 1 for each absent item? Restore a complete **toy** record from earlier practice, and identify what still cannot be restored for the full source.

**Worked answer:** No. Missing is not a unit factor or a known duration. For the declared toy recover Δt=1 TU; q=(1,2,2); k=2 AU·TU; vpot=2 AU/TU; left endpoint convention; a=(0,−4) AU; m=(1,−4) AU; r=(−1,0) AU. Restore (−1,i,i,1,−i,i) in the six-label order and τ(E)=1. Restore the explicitly assumed admitted set {a,b}, with the complete phase rows of Lesson 06 when auditing that sector example. Do not attach one row to a different sector without a declaration. The full source still requires operator coefficients, typed topology carriers, actual boundary-sector values and time/action normalization; toy values do not supply them. Record S02 M15 and S03 AUD-009 pointers and the unresolved replay status.

**Role-classification practice:** Classify the locked M_cell, trace-conjugation identity, chosen toy action, condition Δt>0, assumed membership set {a,b}, and endpoint q_0=1. **Answer:** M_cell is a locked root in this ledger; trace conjugation is a derived theorem under its finite-square/invertible hypotheses; the toy action is a constitutive rule; Δt>0 and the membership set are domain conditions; q_0=1 is a state coordinate. The value Δt=1 TU is an input distinct from the condition Δt>0. These roles do not themselves establish evidence status.

> **Claim scope.** Source-reported architecture, finite proved identities and declared toy inputs occupy separate evidence columns. No measurement or physical mechanism is introduced by this bookkeeping. Source missing bodies retain the source's `VERIFIED_NOT_LOADED` gate label; that label is not a fresh verification by this course. Do not merge a mathematical-backbone module with a compiler label or promote dimension matching to an intertwiner proof.

## Diagnostics

1. **C19.07-D1:** What should a ledger do with a missing proof body or determinant factor?
2. Classify q_0=1, the condition Δt>0, and the identity a=m+r.
3. Why is “coefficient positive” different from “coefficient equals 2”?
4. Can an audit remove sector b because its closure residual is −2?

**Worked answers:** (1) Mark the object and retrieval gap explicitly; do not fabricate a replacement or claim replay. (2) State coordinate, domain condition, and derived identity under r=a−m. (3) Positivity restricts admissible values but does not supply one; the numerical value is a separate input with units. (4) No: b remains in the supplied domain. Preserve the residual and identify which conditions fail.

**Next dependency:** [Capstone](capstone.md) audits a complete finite packet and a deliberately incomplete one.
'''

CAPSTONE=r'''
# Capstone — Audit an action and phase-closure packet

Allow three 55-minute periods: specification/action; loops/phases/lines; sectors/premise audit and repair. All numbers below are synthetic. The task is to audit this supplied finite packet, not infer a source coefficient or prove a continuum/global theorem. Use Lessons 01–07; no new operation is introduced here.

## Supplied packet

The dimensionless path is q=(1,2,2) at t=(0,1,2) TU. Use Δt=1 TU, k=2 AU·TU and vpot=2 AU/TU, all positive. Endpoints q_0=1,q_2=2 are fixed. Use the left-endpoint action S=Σ_(j=0,1) Δt[(k/2)((q_(j+1)−q_j)/Δt)²−(vpot/2)q_j²]. The component model is m=(1,−4) AU. Keep each contribution and residual.

The separate scalar triangle has links (i,−i,1) in ab,bc,ca order and frames (−1,i,1). Use U'_xy=g_x U_xy g_y^−1. This triangle is not asserted to generate the six determinant-line factors.

The six-factor line packet, in UV,light,reg,heavy,cap,induced order, is (−1,i,i,1,−i,i). Its chosen combined basis is E and τ(E)=1. Rebase cap only: e'_cap=−e_cap. All phases are dimensionless.

For the topology arithmetic set A_3=0,A_2=1,C=4 and d=(0,1,54), with the Lesson 06 integer/dual contract. The admitted sector list is **assumed** to be {a,b}. In the original bases let τ(E_a)=τ(E_b)=1. Sector a has phases (−1,i,i,1,−i,i); sector b has phases (−1,i,i,1,−i,−i). These are complete rows. The rebasing operation above concerns row a; row b stays in its declared original basis unless you explicitly transform it.

A damaged copy deletes induced, τ, Δt and the admitted-sector list. Do not fill absent entries from a desired outcome. Compare with the complete supplied packet to repair this toy copy; keep source gaps separate.

## Student tasks

1. **C19-CAP-01 — Specify.** Given q, times and coefficients, produce a ledger with states, intervals, units, domain, boundaries and evaluation convention. Identify all four source action contributions on the Lesson 01 source card and explain which full-source inputs remain unspecified. [Taught/practiced: C19.01-E1/P1.]
2. **C19-CAP-02 — Account.** Produce K,V,a,S; compute the residual vector against m and reconstruct each row and total. Explain the status of a negative contribution. [C19.02-E1/P1.]
3. **C19-CAP-03 — Transform.** Produce the new triangle links, old and new loop products, and inverse reconstruction formula. Explain why this local change cannot repair a nonclosing scalar loop. [C19.03-E1/P1.]
4. **C19-CAP-04 — Retain factors.** Produce a six-row running-product ledger. Omit cap as a recorded mutation and compute its product and closure residual. Discuss heavy=1. [C19.04-E1/P1.]
5. **C19-CAP-05 — Rebase.** Produce the new cap coefficient, total coefficient Z', τ(E') and scalar reading for sector a. Reconstruct the original cap coefficient. [C19.05-E1/P1.]
6. **C19-CAP-06 — Test domain.** Compute n, test d's dual contract and pair d with n by both methods. Test candidate (1,1,0). Produce a two-sector phase/residual ledger and state precisely whether closure holds on the assumed admitted list. [C19.06-E1/P1.]
7. **C19-CAP-07 — Audit premises.** Classify locked M_cell, trace conjugation, the toy action, positivity and sector membership, and boundary values into the five roles. Inventory the damaged copy's missing inputs, restore only the declared toy values, and list unresolved full-source replay objects with provenance. [C19.07-E1/P1.]

## Full answer key

**01 (12 points).** Three ordered state values, two intervals, fixed endpoints 1 and 2; q dimensionless, Δt=1 TU, k=2 AU·TU, vpot=2 AU/TU. Allowed q values are real, all three scalar parameters positive. Rates have units TU^−1; both bracket terms have AU/TU and interval actions have AU. Potential reads q_0,q_1. The source has rate-quadratic, trace, potential and linear-source terms; the toy is separately declared. Full-source typed operator coefficients, topology carriers, boundary-sector values and time/action normalization remain required, not supplied by this toy.

**02 (15 points).** Increments (1,0); K=(1,0) AU; V=(1,4) AU; a=(0,−4) AU; S=−4 AU. Residual r=a−m=(−1,0) AU. Row reconstruction (1,−4)+(−1,0)=(0,−4); total reconstruction −3+(−1)=−4 AU. Negative action is permitted by the signed rule and is not negative measured transferred energy. Preserve K,V as well as a; cancellation does not erase components.

**03 (12 points).** Frame inverses are (−1,−i,1). New links are ((−1)i(−i),i(−i)1,1·1·(−1))=(−1,1,−1). Both products equal 1. U_xy=g_x^−1 U'_xy g_y reconstructs each old link. On a closed scalar loop endpoint factors cancel to g_aPg_a^−1=P. Thus local frame choices cannot change a nonclosing scalar P into 1.

**04 (12 points).** Running products in label order are −1,−i,1,1,−i,1. Φ=1, residual 0. Without cap, the list (−1,i,i,1,i) multiplies to i, with residual i−1. Equivalently 1/(−i)=i. Heavy=1 stays as a known contribution with a label and provenance; omission would leave the numerical product unchanged but the packet incomplete.

**05 (14 points).** e'_cap=−e_cap gives z'_cap=(−i)/(−1)=i. New six coefficients (−1,i,i,1,i,i) have Z'=−1. E'=−E so τ(E')=−1. Φ'=Z'τ(E')=1. The old cap coefficient is i(−1)=−i. This preserves a fixed τ and a fixed line element. Forgetting τ(E') would give the wrong scalar −1. It does not establish a global source trivialization.

**06 (20 points).** n=(4/3,2,1/18). For d=(0,1,54), d_3,d_2 are integers and h=0+1/4+54/72=1. Direct pairing 0+2+54/18=5; expanded pairing 0·0+1·1+4·1=5. Candidate (1,1,0) fails because h=7/12. Sector a has Φ=1 and ρ=0. Sector b's running products are −1,−i,1,1,−i,−1, giving Φ=−1 and ρ=−2. Closure fails on b, so it fails on the assumed list {a,b}. Membership is not inferred from closure success; keep b and its residual. Passing dual arithmetic does not determine physical admission.

**07 (15 points).** M_cell is a locked geometric root for this ledger; trace conjugation is a finite derived theorem with square/invertible hypotheses; the chosen finite action is a constitutive rule; positivity and the assumed set {a,b} are domain conditions; boundary values are state coordinates. τ is a declared reading map, its basis value an input to the toy. The damaged copy lacks induced, τ, Δt and sector membership; mark all four before repairing. Restore Δt=1 TU, τ(E)=1 in each original basis, induced=i for a and −i for b, and the assumed set {a,b}. Retain the ordered six-factor rows, all K,V,a,m,r entries and the rebasing data. The full-source operator coefficients, topology carriers/factors, boundary-sector values and time/action normalization are not recovered. Cite S02 `/backbone_sequence/14` and S03 `/findings/8`; retain the latter's missing-body gate as source-reported, not freshly replayed.

## Scoring rubric — 100 points

| Task | Points and partial-credit basis |
|---|---|
| 01 | 4 state/time/boundaries; 4 dimensions and convention; 4 source terms/gaps |
| 02 | 6 K,V,a; 3 total; 4 residual/reconstruction; 2 sign scope |
| 03 | 6 links; 2 products; 4 inverse and invariance explanation |
| 04 | 5 six-row product; 4 omission/residual; 3 unit-factor provenance |
| 05 | 4 coefficient/basis; 4 τ; 4 scalar/reconstruction; 2 global scope |
| 06 | 4 n; 4 dual contract; 4 pairing both ways; 3 failing candidate; 5 sector ledger/scope |
| 07 | 5 role classification; 4 missing-input inventory; 3 toy restoration; 3 source gap/provenance |

Award method credit for consistent arithmetic after one slip; do not award a closure conclusion that drops a factor or an admitted sector. For instructional mastery, repair any missing-factor, missing-trivialization, unit or scope error even if the numerical score is high. An answer may use equivalent notation if meanings and reconstruction remain explicit.
'''

TEACHER=r'''
# Teacher guide — Action, Topology, and Phase Closure

This course contains seven lessons over nine core 55-minute periods, followed by three capstone periods. It teaches an audit of a finite packet, grounded in the exact M15 source architecture. It does not assign calculus, abstract algebra, a continuum proof, a global line construction or a physical sector-selection proof. All classroom numbers are explicitly synthetic. The source audit is a reading task with meaningful missing-input answers.

## Entry check and recovery

Ask students to compute (2−1)², 1/3+1/4, and solve 2x=6. Expected answers are 1,7/12,3. Repair signed arithmetic and common denominators before Lesson 01. Courses 16–18 are the series prerequisites, but the local bridges reteach the finite operations used here: state lists, quarter-turn phases, frames, line bases and dual-charge pairing. Do not assume a student understands a matrix because they recognize its letter. Lesson 01's matrix syntax is recognition-only; Lesson 07 gives the trace identity's finite derivation.

## Pacing and observable checks

Every period allocates 5 minutes to retrieval, 20 to explanation/worked example, 15 to guided practice, and 15 to independent diagnostics plus repair. For two-period lessons, divide the existing content as below; do not compress it to one period.

| Lesson | Periods | Focus and readiness check |
|---|---:|---|
| 01 | 1 | Build input/unit ledger; student explains why source syntax alone is insufficient |
| 02 | 1 | Retain signed rows; student reconstructs both rows from model and residual |
| 03 | 1 | Teach phase cycle then frames; student cancels the entire loop's frames |
| 04 | 1 | Six-factor product and omission; student retains known unit factors |
| 05 | 2 | First: one line, basis and tensor coefficient. Second: fixed τ under rebasing and inverse reconstruction |
| 06 | 2 | First: rational contract and two pairing routes. Second: admitted list, complete phase rows and residuals |
| 07 | 1 | Five premise roles and damaged packet; student separates domain conditions from values |

For Lesson 05 period 1, have students rehearse s=2e, e'=−e before six lines. In period 2 use W1 and P1 and all five diagnostics. For Lesson 06 period 1, derive the expanded pairing before computing its fractions. In period 2 use the supplied two-sector rows; students must explain why sector b cannot be deleted. The full capstone fits three periods by grouping tasks 01–02, 03–05, then 06–07 with repairs.

## Teaching interventions

If students think a zero action row is empty, ask them to recover K_0=V_0=1 from the retained row. If they confuse missing and one, hide a label while leaving the product visible and ask whether provenance survives. If they treat Z' as the scalar after rebasing, require the two-column record Z',τ(E') before multiplication. If they infer physical sector membership from integral pairing, have them state the exact conditional implication proved in Lesson 06. If they use one path to compare probabilities, ask for the absent probability rule and boundary compatibility.

Keep a repair sheet with item ID, original answer, corrected answer and reason; retain original work. A residual is primary information. A closure residual of −2 describes a case that failed the declared test; it does not justify excluding that case. No outlier or significance gate belongs in these finite examples.

## Source and evidence teaching

Use sources.md alongside the exact source card. S02 M15 requires M10,M13,M14. These mathematical-backbone labels are not compiler-module labels. Source assertions and accepted integration dispositions remain separate. M15's reported typed architecture is useful content; missing replay objects remain visibly missing. The archival correction AUD-009 supplies the `VERIFIED_NOT_LOADED` label, which students should not treat as this course's own proof verification. The scalar models were chosen to make multiplication hand-checkable and are not measurements.

The source's action `tau` is a time/parameter symbol; the line map τ is a different object. The integer C of the charge contract is different from the action's operator C. Keep local labels on the board. No fixed Cell3 numerical constants are used in these lessons, so do not import historical metric values to make an example appear physical.

## Assessment and audit use

All diagnostic answers are in the lessons for self-correction. For an independent check, cover the answers first, then require a reconstruction rather than a bare total. The capstone answer key gives a 100-point rubric, but closure and missing-input mistakes require targeted repair regardless of the score. Coverage-map rows link each capstone operation to an earlier explanation and answered practice. The deterministic validator checks files, hashes, dependencies, audit records and verbatim assembly; it does not replace the human content audit.
'''

def supporting():
    write('capstone.md',CAPSTONE)
    write('teacher-guide.md',TEACHER)
    terms=[
      ('Action S','Number assigned to a path by a declared rule; units AU in toy','01'),
      ('q_j, Δt, v_j','Dimensionless state, positive interval TU, finite rate TU^−1','01'),
      ('k, vpot','Toy coefficients: AU·TU and AU/TU','01'),
      ('K_j,V_j,a_j','Two nonnegative toy terms and signed difference K_j−V_j, AU','02'),
      ('m_j,r_j','Declared model and residual a_j−m_j; a_j=m_j+r_j','02'),
      ('i','Quarter-turn phase; i²=−1, i⁴=1','03'),
      ('U_xy,g_x,P','Link, local frame, ordered closed product; dimensionless','03'),
      ('UV,light,reg,heavy,cap,induced','Six source-local determinant-line labels; none omitted','04'),
      ('Φ,ρ','Scalar phase and closure residual Φ−1, dimensionless','04'),
      ('e,z,s','Chosen line basis, complex coefficient, element s=ze','05'),
      ('⊗,E,Z,S_total','Tensor product, combined basis, coefficient, line element S_total=ZE; not action S','05'),
      ('τ','Line trivialization map; distinct from action integration parameter tau','05'),
      ('Section','Assignment of line elements over a domain; toy uses one specified packet','05'),
      ('A_3,A_2,C','Integers defining charge lattice; C not the action operator','06'),
      ('n,d,h','Charge triple, dual charge, fractional combination tested for integrality','06'),
      ('〈d,n〉','Pairing d_3 n_3+d_2 n_2+d_1 n_1','06'),
      ('Sector/admitted list','Labeled case / explicitly declared allowed domain','06'),
      ('ell,E_3,E_2,c_1','Source lock, topology carriers, first topological class; recognition only','06'),
      ('Locked root','Version-fixed premise; evidence status recorded separately','07'),
      ('Theorem','Derived implication with hypotheses; archival label alone is not replay','07'),
      ('Constitutive rule','Declared relation specifying a model','07'),
      ('Domain condition','Restriction on permitted inputs/cases','07'),
      ('State coordinate','Value supplied within a declared domain','07'),
      ('Tr,T,G^−1','Trace, transpose, inverse; finite trace identity taught in Lesson 07','07'),
      ('M_cell,R_cell,G_phase,G_eff,B,O_K','Cell3 Gram metric, its inverse, distinct phase/effective metrics, ordered basis, physical origin; no numerical substitution here','07'),
      ('VERIFIED_NOT_LOADED','S03 missing-body gate label, not a fresh course verification','07')]
    write('terminology.md','# Terminology and notation\n\nLocal symbols are explicitly scoped. AU and TU are abstract teaching units. ℂ denotes complex numbers; it is not integer C or the action operator C.\n\n| Term | Meaning | First lesson |\n|---|---|---|\n'+'\n'.join(f'| {a} | {b} | {c} |' for a,b,c in terms))
    rows=[]
    for j,l in enumerate(packet['course_map'],1):
        c=f'C19.{j:02}'
        rows.append(f"| {c} | {l['title']} | lesson-{j:02}: {c}-E1 | {c}-W1 | {c}-P1 (answered) | {c}-D1 | "+(f'lesson-{j+1:02}' if j<7 else 'capstone')+f' | C19-CAP-{j:02} |')
    write('course-map.md', '''# Course map — Action, Topology, and Phase Closure

Seven lessons, nine core periods plus three capstone periods, all 55 minutes. Audience: high-school seniors with signed arithmetic, fractions, ratios, powers, linear equations and coordinate graphs, plus series courses 16–18. Local bridges teach every finite operation needed here. No calculus or university algebra is assumed. Units 1–2 (lessons 01–02), 3–5 and 6–7 are cumulative audit boundaries.

Dependency chain: lesson-01 → lesson-02 → lesson-03 → lesson-04 → lesson-05 → lesson-06 → lesson-07 → capstone. The source mathematical dependency is M15 requires M10,M13,M14; the finite course bridges are pedagogical, not substitute proofs of those modules.

| Concept | Outcome | Introduction | Worked example | Practice | Assessment | Later use | Capstone |
|---|---|---|---|---|---|---|---|
'''+ '\n'.join(rows)+'''

## Concrete capstone backward map

| Step | Named input → assessed output | Earlier explanation and independently answered practice |
|---|---|---|
| 01 | q,t,k,vpot,rule → typed state/domain/boundary ledger | C19.01-E1/P1 |
| 02 | ordered q and model m → K,V,a,S,r and reconstruction | C19.02-E1/P1 |
| 03 | links and frames → transformed links, invariant loop, inverse map | C19.03-E1/P1 |
| 04 | six labeled coefficients and τ(E)=1 → product, omission product/residual | C19.04-E1/P1 |
| 05 | cap basis multiplier and coefficients → Z',τ(E'),invariant scalar | C19.05-E1/P1 |
| 06 | A_3,A_2,C,d,admitted rows → n,pairing,dual test,sector ledger | C19.06-E1/P1 |
| 07 | complete/damaged packets and source cards → classified premises and missing-input audit | C19.07-E1/P1 |

Each C19.xx-P1 has a worked answer distinct from its worked-example prompt. Lessons 05 and 06 retain the approved two-period allocation to avoid hidden algebra/topology load. Per period: retrieval 5, teaching/worked example 20, practice 15, diagnostics/repair 15 minutes. This expands neither the required computation scope nor the seven concept IDs.

Evidence boundary: actual source text is cited as source fact; its proof/status claims remain archival unless explicitly derived here. Toy arithmetic is fresh finite verification, not empirical evidence. No mechanism or physical sector selection is inferred. Recognition-only source operations are not capstone computations.
''')
    source_rows=[]
    for s in packet['sources']:
        actual=hashlib.sha256(Path(s['path']).read_bytes()).hexdigest()
        assert actual==s['sha256'],s['id']
        source_rows.append(f"| {s['id']} | `{s['path']}` | `{actual}` |")
    write('sources.md','''# Source notes and scope

All five supplied archival files were read-only hash-checked against input-contract.json. No source snapshots were saved. Exact teaching content was read from S02 M15 and dependency entries M10/M13/M14, and S03 AUD-009. The other supplied files are provenance context, not independent supporting evidence for the finite examples.

| ID | Absolute source path | Verified SHA-256 |
|---|---|---|
'''+ '\n'.join(source_rows)+'''

## Claim-to-source pointers

| Claim/card | Exact pointer | Evidence class/use |
|---|---|---|
| Four action terms; retained state inputs | S02 `/backbone_sequence/14/action`, `/state_coordinates` | Source fact about expression and stated inputs; full numerical replay unavailable |
| M15 prerequisites M10,M13,M14 | S02 `/backbone_sequence/14/requires` | Exact module dependency, not compiler IDs |
| Determinant lock and rational charge contract | S02 `/backbone_sequence/14/topology/0` through `/3` | Source architecture; integer-sector assumption explicit for classroom arithmetic |
| Six sections and τ; every admitted sector | S02 `/backbone_sequence/14/determinant_line/0` through `/2` | Source architecture/condition; no global replay claimed |
| Source transport conjugation | S02 `/backbone_sequence/12/proof/0` | Source claim; scalar finite version freshly derived in lesson 03 |
| Weak-first source ordering and quotient claim | S02 `/backbone_sequence/9` | Historical/source-local ordering; no carrier tuple computation assigned; any color-first conversion needs explicit permutation |
| Chirality/history dependency | S02 `/backbone_sequence/13` | Recognition of required module, not source proof replay |
| Missing M15 topology carriers and determinant-line factors | S03 `/findings/8/evidence/missing_or_undefined/8` | Exact correction finding AUD-009; retain source-reported VERIFIED_NOT_LOADED gate |

Krytronx capabilities was queried read-only. RAG query `M15 determinant_line s_induced phase closure`, hybrid mode, rerank=false, returned corpus generation and manifest `sha256:5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7`, matching the packet. Search results were used for scope checking only, not promoted into a mathematical-backbone proof. Returned integration report `kfield_standard_model/evidence/p12_standard_model_compiler_adjudication_report.json`, lines 1–101, SHA-256 `a3dfca0e55e525c6522c3088b95e5bcc048c141fce340bfe980fcfc14123220a`, lists compiler direct-authority modules M03,M07,M08. That namespace is distinct from backbone M15. Returned hostile-audit report `kfield_standard_model/evidence/kfield_standard_model_corpus_integration_hostile_audit_2026-09-02.md`, lines 1–46, SHA-256 `58f1e3514944e3e21495ee6106168d69b187421b5b20266c3b8ed6e636b213ec`, preserves global forms n=1,2,3,6 without forcing n=6. These are source-reported dispositions; no compiler was run by this course.

## Unresolved information and invariant boundaries

The selected source excerpt does not supply a replayable full action evaluation or global determinant-line construction. Full topology carriers, individual source determinant factors, typed source operator/coefficient values, boundary sectors and time/action normalization remain unresolved inputs. This is an explicit boundary of the core task, not a missing assigned exercise. The course's finite numbers, units and sectors are declared synthetic and never substitute for these objects.

No geometry, velocity, experimental energy or molecular quantities are computed. All packet invariants remain in input-contract.json: Cell3 uses the mature locked geometry, intentional negative determinant, ICRS column order, half-open ownership and x−O_K affine identities; distinct metrics, parities, recursion branches and physical/phase vectors stay distinct. No historical/corrected constants are mixed. The detail-product theorem is not invoked. M19 is not used as a premise of M20. No source-data copies, deleted residuals, outlier gates or fabricated certificates are introduced.
''')

if __name__=='__main__':
    for n,body in LESSONS.items(): write(f'lesson-{n:02}.md',body)
    supporting()
