# lesson-06: Binding and periodic organization

2 sessions of 55 minutes.

**Essential question:** How can an atomic application be source-traced while its missing coordinates remain explicit?

**Goals**

- Classify each source card as synthesis, mechanism or unresolved record.
- Build a periodic-coordinate ledger without inventing values.
- Compute an energy difference and distinguish it from a rate or power.

## Prerequisite bridge

Lesson 5 separated formula, isotope, charge, arrangement and binding state. Lesson 3 showed why equal dimensions do not specify an action-preserving map. We now use both ideas to read an archival application without filling its gaps by analogy.

<a id="C21.06-E1"></a>
## Explanation — C21.06-E1

A source-traced report records what a document actually supplies and which operation was freshly checked. The source cards below are bounded readings of S05. The exact file path and digest appear in sources.md; record numbers use one-based labels but JSON pointers use zero-based array positions.

| Card | Pointer | Stored class | What the course can carry forward |
| --- | --- | --- | --- |
| R029 | /records/28 | synthesis | A proposed periodic coordinate package: base Cell3 address plus nested coordinate fibers. |
| R030 | /records/29 | synthesis; type mechanism | Nuclear, chemical and orientational relations as distinct types of edges. |
| R031 | /records/30 | archive_stated; type unresolved | Formula and nominal label leave isomers unresolved; preserve graph and binding information. |
| R032 | /records/31 | synthesis; type architecture | Three rank-three structures recur, while a canonical connecting map remains absent. |

A graph is a collection of vertices and edges: objects and their declared connections. An adjacency table records which vertex pairs connect; graph identity includes the labeled vertices and full edge list. A Laplacian is the degree table minus the adjacency table (degree counts the incident edges). Its spectrum is a list of eigenvalues, using the scaling-direction idea from lesson 3. These terms are recognition-only here: no unprovided molecular graph is assigned. A spectrum compresses a graph and need not uniquely identify it, so preserve graph identity alongside any spectral summary. An edge labeled chemical rearrangement is not the same operation as a nuclear change or an orientational coupling.

For a source-traced worked row, start with the synthetic composition (4,4,0,1). We know the counts and derived nominal V=68. R029 requests many more coordinates. A correct report looks like this:

| Field requested by R029 | Present value/status in this classroom packet |
| --- | --- |
| Composition counts, nominal label | (4,4,0,1), V=68; synthetic and freshly computed |
| Base Cell3 address | Not supplied |
| Scale/face sector and isospin lambda | Not supplied; source-local labels |
| Three composition-null coordinates | No basis and origin for this point supplied; invariant moves checked separately |
| Exact isotope mass | Not supplied; nominal weights do not replace it |
| Graph identity and spectrum | Not supplied; formula alone is insufficient |
| Charge/parity | Not supplied for this composition row; do not borrow synthetic A/B charge |
| Binding residual | Not supplied; retain as a required coordinate |
| QPC phase tensor | Not supplied; source-local phase-cost object, recognition only |
| Occupied coefficient selection | Not supplied; R030 edge classes do not select c |

The repeated rank three in R032 is an explanatory target: composition-null directions, a geometric isofacial tangent fiber and the EG three-channel phase transform. We have constructed only the composition arithmetic. A meaningful map would need typed domains, units, bases, actions and a rule taking one object to the other. The rank count alone is insufficient. No Cell3 metric, physical coordinate or phase tensor is introduced numerically in this course; their source-local meanings are not merged with our decoder Gram matrix.

### Energy, rate and power have different input requirements

Retain the complete neutral-object convention of lesson 5 and its synthetic conversion. For AB=4.8u, delta m=2+3-4.8=0.2u, and Q_release=2 E_unit. This is an endpoint difference. It supplies no duration, transition frequency or usable-energy fraction. A rate counts events per time; average power is energy delivered divided by duration. If a separate premise says this 2 E_unit release is delivered over 4 time units and half is recovered, recovered energy is 1 E_unit and mean recovered power is 1/4 E_unit per time unit. The duration and fraction must remain in the ledger.

The reference relation delta E=delta m c_light² concerns differences of rest energies of specified complete objects. It does not turn phase into force or a model energy into measured transferred energy. Our numerical conversion is stipulated, so every constant needed for the calculation is supplied locally; no external mass table is required.

> Claim scope: R029 and R030 are archival synthesis and proposed mechanism. The ledger’s missing fields are unresolved inputs, not zero values. The energy arithmetic is a synthetic application of a declared reference relation. No physical periodic address, nuclear reaction rate, binding force or occupied-state selection is claimed by these exercises.

<a id="C21.06-W1"></a>
## Worked example — C21.06-W1

Build a source-traced row: S05#/records/28 (R029) requests address, scale/face sector, lambda, composition-null coordinates, isotope mass, graph spectrum, charge/parity, binding residual and QPC phase tensor. For the synthetic composition from lesson05, only counts and nominal V are supplied; mark all other values not supplied. R030 describes edge classes rather than choosing coefficients.

<a id="C21.06-P1"></a>
## Guided practice — C21.06-P1

Try the operation before reading the solution. S05#/records/30 (R031) says formula/nominal volume leave isomers unresolved; retain adjacency or Laplacian data and binding residual. S05#/records/31 (R032) compares three rank-three fibers but supplies no canonical isomorphism. Complete a row with those exact source statuses. Repeat A+B -> AB with final 4.8u: Q=2 E_unit.

<a id="C21.S03-E1"></a>
## Supplemental explanation — C21.S03-E1

Repeat the declared Q_release=(m_initial-m_final)c^2 relation with balanced constituents/charge, complete-object masses, reference state and conversion. Binding differences remain coordinates. Energy difference, transition rate and recoverable power require different inputs.

<a id="C21.S03-W1"></a>
### Worked example — C21.S03-W1

Use synthetic neutral complete objects A=2u, B=3u, AB=4.8u with conserved A/B labels and 1u c^2=10 E_unit. Delta m=0.2u and Q=2 E_unit. No duration or efficiency was supplied, so power is not determined.

<a id="C21.S03-P1"></a>
### Practice with answer — C21.S03-P1

Repeat final AB=5.05u under the same balanced convention: Q=-0.5 E_unit. If, in a separate stipulated release example, 2 E_unit is delivered over 4 time units with efficiency 1/2, recovered mean power is (1/2)*2/4=1/4 E_unit per time unit. Those extra premises must be recorded.

<a id="C21.S03-D1"></a>
### Diagnostic boundary — C21.S03-D1

A positive Q does not supply a rate. An ion endpoint missing the removed electron fails bookkeeping. Preserve mass difference and supplied binding state rather than normalizing the discrepancy away.

<a id="C21.06-D1"></a>
## Diagnostic checks — C21.06-D1

1. Which R029 fields are actually known for the composition (4,4,0,1)?
2. What are the different roles of R030 and R031?
3. Why does R032 not furnish a canonical map?
4. Compute Q for AB=4.8u, then compute recovered mean power with fraction 1/2 and duration 4.
5. Does positive Q alone determine a transition rate?

## Worked answers

1. Only the supplied counts and V=68; none of the other required coordinate values follows just from those counts.
2. R030 proposes typed binding/transition edges; R031 records unresolved isomer distinction and calls for graph and binding coordinates.
3. Three spaces of equal rank can have different bases, units and actions. The source explicitly does not supply a canonical connecting map.
4. Delta m=0.2u, Q=2 E_unit; recovered energy=(1/2)2=1 E_unit; divide by 4 time units for 1/4 E_unit per time unit.
5. No. A rate requires an additional time-dependent process or supplied event count and duration.

**Boundary to carry forward:** A shared rank of three does not furnish a canonical map. A graph spectrum may also be shared by distinct graphs, so retain graph identity as well. Source mechanism synthesis, supplied coordinates and freshly checked arithmetic must occupy separate fields.

**Next dependency:** [lesson-07](lesson-07.md). Use this lesson’s reconstruction and scope checks there.
