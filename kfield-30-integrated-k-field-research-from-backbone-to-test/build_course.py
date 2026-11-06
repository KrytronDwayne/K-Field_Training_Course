"""Authoring/recovery utility. Inputs remain in place; no source snapshots."""
from pathlib import Path
import json, hashlib
P=Path(__file__).resolve().parent
D=json.loads((P/'input-contract.json').read_text(encoding='utf-8-sig'))
def write(name,text): (P/name).write_text(text.strip()+'\n',encoding='utf-8')
def js(name,obj): write(name,json.dumps(obj,indent=2,ensure_ascii=False))
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
S=json.loads(Path(D['sources'][1]['path']).read_text(encoding='utf-8-sig'))
lessons={}
lessons[1]=r'''
# Lesson 1 — Rebuilding the complete dependency chain

Essential question: What must be supplied before a geometric construction can support an instrument prediction?

Goals: Draw a directed dependency map; classify premises and outputs; perform a finite coordinate construction; carry source boundaries into a downstream claim.

Prerequisite bridge: A coordinate triple is an ordered list of three numbers. Multiplying a column by a number scales all its entries; adding columns adds matching entries. An arrow A → B means that B uses A. These operations bridge the earlier courses on geometry, evidence, instruments, and closure; this course supplies the small examples needed for its assessments. No calculus or advanced algebra is required.

## C30.01-E1 — A chain has inputs as well as arrows

A dependency map is a recipe with return addresses. A **premise** is accepted at the start of a particular argument. A **derived object** is constructed using those premises. A **domain hypothesis** says where an operation is allowed: division requires a nonzero divisor. A **state coordinate** selects a particular state inside a permitted family. Proving that a family has six coordinates does not choose their six values.

The mature source S02 names M20 the closure theorem. Its `/backbone_sequence/19/requires` lists M01 through M18. Read the full module table in [sources.md](sources.md), which preserves every source-local `requires` entry, including the two non-module premises of M13. The five groups of work are geometry (M01–M03), retained calculus and shape/graphs (M04–M08), internal carriers (M09–M11), interactions/history/action/families (M12–M16), and decoding/continuum (M17–M18). Grouping helps reading but does not replace the individual edges.

S02 `/constitutive_principles` supplies six EG principles: retain the complete state (A1); require a decoder for a lossless transform (A2); define a finite change by subtraction (A3); retain the joint product of finite changes (A4); retain residuals as next-channel information (A5); keep units, scale, and approximation as typed views of a preserved source (A6). They are constitutive premises in this reading. A decoder reverses an encoding: if T encodes and D decodes, D(T(state))=state.

M20 also carries four state-coordinate entries: scale before the locked area anchor, time/action normalization, vacuum magnitude with admitted operator coefficients, and an occupied six-coordinate mass/coupling state. An anchor fixes a scale; a normalization fixes a convention for numerical values. These inputs must travel with any resulting prediction. History operators, finite gauge hypotheses, spin/coframe data, phase metrics and replay matrices need their declared domains and bodies too (S03 AUD-011).

M19 contains separately retained branches, including a gravity scalar lift, reciprocal-plane inversion and exceptional carrier constructions. Equal dimensions do not construct an action relating two objects: an explicit structure-preserving map would be needed. The corrected core chain therefore has no M19 → M20 arrow. S03 AUD-001 corrects the serialized edge ledger; it does not erase M19.

## C30.01-W1 — Read and use the chain

There are 18 core requirements in the M20 list: counting inclusively from 1 to 18 gives 18. The decoder M17 uses M05 and M11; the continuum renderer M18 uses M03 and M04. Both then feed M20. Write `M05,M11 → M17 → M20` and `M03,M04 → M18 → M20`. The complete table in sources.md lets you expand those inputs recursively rather than guessing from module numbers. The internal `requires` graph has 52 edges; its 18 incoming M20 edges are included in that count.

Here is one actual operation from the geometric side of that chain. The source uses x = O_K + Bq. Here x and O_K are physical position and origin, q is a dimensionless address, and B has three length-valued columns a,b,c in the ICRS celestial frame. For synthetic q=(1/2,0,0), x−O_K is half column a. The input column is a=(0.3275012420558906, −0.0548970078840064, −0.0374875028947299) nm, from S02 `/mature_locked_cell3/B_nm/0/0`, `/mature_locked_cell3/B_nm/1/0` and `/mature_locked_cell3/B_nm/2/0`. Divide each entry by 2. With this stored mature column, the result is (0.1637506210279453, −0.0274485039420032, −0.01874375144736495) nm. This is a calculation on stored decimals, not a new spatial measurement.

Cell ownership uses z=floor(q+1/2), applied separately to each component. Floor means the greatest integer no larger than its input. Thus z=(1,0,0) and u=q−z=(−1/2,0,0). Reconstruction gives z+u=q. The half-open interval [−1/2,1/2) includes its left endpoint and excludes its right endpoint. This assigns a shared boundary to exactly one cell. It is distinct from a rounding rule for residual integerization.

## C30.01-P1 — Practice, then check

Draw the M17, M18 and M19 branches, classify EG-A2 and the occupied vector c, and assign q=(−1/2,0,0) to a cell.

Answer: M17 and M18 have the inputs above and feed M20. M19 uses M07,M08,M10,M13,M18 and remains separate. EG-A2 is a constitutive premise; c supplies a state rather than being selected by a dimension count. For q=(−1/2,0,0), z=(0,0,0), u=(−1/2,0,0), and reconstruction is exact.

> Claim scope: The module roles and theorem are source-attributed. Reading their dependencies is not fresh verification of every proof body. The coordinate arithmetic is freshly checkable. The mature B has an intentional negative determinant; no axis is flipped to make it positive. Reciprocal identities use x−O_K, not an unshifted position. Source gaps and historical numerical branches remain in sources.md.

## C30.01-D1 — Diagnostics and worked answers

1. A diagram contains M19 → M20 but omits M01 → M20. What changes? **Answer:** Remove the former from the core graph and restore all M01–M18 incoming edges, following source `requires` and AUD-001.
2. Does knowing six coefficient slots determine six masses? **Answer:** No. The occupied coefficient values are supplied state coordinates; a renderer evaluates them after selection.
3. Why does q=+1/2 move to the next cell? **Answer:** floor(1)=1 and the retained local coordinate is −1/2; the current cell excludes +1/2.
4. What is lost by saying “Cell3 alone proves M20”? **Answer:** The six constitutive premises, domain hypotheses and supplied states disappear. Restore the complete contract before using the closure statement.

Next dependency: [Lesson 2](lesson-02.md) assigns each arrow's evidence a precise scope.
'''
lessons[2]=r'''
# Lesson 2 — Formal witnesses and empirical witnesses

Essential question: What exactly does a witness allow us to say?

Goals: Classify five witness types; reconstruct a finite mean/detail pair; distinguish compiler and backbone namespaces; attach a return address and assumptions to a claim.

Prerequisite bridge: Lesson 1 distinguished a supplied premise from a derived result. We now ask how another person can inspect that distinction. A **witness** is the actual object supporting a statement, such as a derivation, checker receipt, calibration record or acquisition record. A label describing a witness is not its body.

## C30.02-E1 — Five different questions

A proof answers “does this conclusion follow on this domain from these premises?” A replay answers “does this program with these inputs produce this output?” Calibration answers “how does this instrument respond to a known reference under declared conditions?” Measurement answers “what did this identified acquisition record?” A prospective protocol answers “what will be done and how will every possible outcome be handled?” Each can be useful without answering the other four questions.

A SHA-256 hash is a 64-character fingerprint of file bytes. It helps detect changed content; it does not certify the truth of the content. A JSON pointer such as `/backbone_sequence/19` is a return address: slashes descend into fields, and 19 selects the twentieth list item because numbering starts at zero. Record the path, hash, pointer, evidence type, premises, date and current execution status together.

For a simple proof, let two dimensionless readings be a and b. Define their mean m=(a+b)/2 and signed detail h=(a−b)/2. Then m+h=(a+b+a−b)/2=a and m−h=b. Every pair is reconstructed if both m and h are retained. For (2,6), m=4,h=−2, so 4+(−2)=2 and 4−(−2)=6. Keeping only 4 loses which channel was larger and by how much. A fresh arithmetic replay can check this case; the symbolic cancellation covers every real a,b.

Formal languages such as Safe Agda can check a precisely stated proof under a recorded module closure. A hostile mutant is an intentionally damaged version used to test whether a checker rejects that particular defect. Rejection gives evidence about that check. Neither the name of a language nor a green status automatically supplies apparatus calibration. Here we read source reports of these checks; we do not claim to have run Agda.

## C30.02-W1 — Two uses of M03

I02 `/direct_authority_modules` lists compiler M03, M07 and M08. S02 `/backbone_sequence/2` names backbone M03 “Lucas sheets and two non-aliased recursion systems.” The safe identifier is the pair (namespace,module label). Thus `(compiler,M03)` and `(backbone,M03)` are separate until an explicit mapping with its own scope is supplied. Number equality is not that mapping.

I01 `/results/9` reports dispositions for twenty compiler modules; `/results/10` reports six minimal two-question experiment portfolios. The source calls these designs and retains performing the experiments as an open obligation. Its formal transport statements and exact subclaims must remain separate from the source-attributed backbone M20 closure theorem. The supplied teaching contract names compiler M20 `compositeNonterminal`; that disposition is not a new name for the backbone theorem.

I01 `/hazards/3` and `/open_obligations/1` preserve global forms Z1,Z2,Z3,Z6 as an unresolved family for the integration. These are source labels for alternatives, not four numbers to average. A source-local determinant lock selecting a Z6 form under its own assumptions cannot silently remove the other integration alternatives. The course asks you to preserve that logical distinction, not to compute group theory.

## C30.02-P1 — Practice with witness cards

Classify: A, the mean/detail cancellation above; B, a checker log with exact input/output hashes; C, a known reference producing a recorded response interval; D, an instrument record with UTC time and channel; E, a future blinded detector plan. Add a return address and one limitation to each.

Answer: A is finite algebra at this section, assuming both components are retained. B is replay evidence at its log pointer, conditional on the identified program and inputs. C is calibration at its reference record, limited to its stated conditions and interval. D is an observation at its acquisition pointer; transfer interpretation still requires C. E is a protocol at its versioned plan; its outcome field remains unexecuted. These cards are teaching descriptions, not invented real logs or acquisitions. In a real report unresolved file/hash fields stay explicitly missing.

> Claim scope: I01 and I02 are freshly retrieved source reports, not fresh typechecking receipts. The synthetic mean/detail example verifies reconstruction only. Detection, extraction and induction each require their own empirical witness contract; T30 supplies those distinctions.

## C30.02-D1 — Diagnostics and worked answers

1. Recompute mean/detail for (3,7). **Answer:** m=5,h=−2; 5−2=3 and 5+2=7.
2. A file hash matches. Has its theorem been proved? **Answer:** The bytes match the pinned file. The proof body and its premises still determine theorem scope.
3. Does a minimal portfolio imply a favorable experiment occurred? **Answer:** No. Minimality concerns a design under its rules; the execution and outcome require separate records.
4. Can compiler M07's authority be attached to backbone M07? **Answer:** Only through an explicit scoped witness connecting them. A shared numeral alone does not identify objects.

Next dependency: [Lesson 3](lesson-03.md) asks what an instrument can distinguish even when its algebra is exact.
'''
lessons[3]=r'''
# Lesson 3 — Interferometers and identifiable coupling

Essential question: Which hidden quantities can a measured response recover?

Goals: Multiply a small measurement table by a parameter pair; exhibit an invisible change; recover parameters from sum and difference; explain why a physical transfer calibration is necessary.

Prerequisite bridge: You can solve two linear equations and reconstruct a mean/detail pair. An **inverse problem** starts from outputs and asks which inputs produced them. **Identifiable** means unique within the declared candidate domain and measurement model. We first use dimensionless synthetic channels so that instrument units cannot be hidden inside convenient arithmetic.

## C30.03-E1 — Reading a matrix as instructions

Write theta=(theta1,theta2) for two unknown response contributions. A matrix is a rectangular table. In y=H theta, each row of H gives multipliers: multiply each row entry by the corresponding theta entry, then add. For H=[[1,1],[2,2]], the outputs are y1=theta1+theta2 and y2=2theta1+2theta2. The second channel is twice the first, so it provides a repeat of the same combination rather than a new equation.

**Rank** counts independent combinations measured. Here rank is 1 because the second row is a multiple of the first. A **null direction** is a parameter change giving zero output change. Adding t to theta1 and subtracting t from theta2 changes neither sum. The direction (1,−1) is invisible for every real t. A set of inputs sharing one output is an equal-output family. Recognizing such a family tells you which measurement to add.

An interferometer compares wave paths through their relative phase. Phase labels position within a repeating cycle; a detector converts the comparison into recorded values through a transfer relation. A beat frequency describes cycles per second, not joules per second. This course uses a linear sum/difference response as a proposed local instrument model, not as a universal law for every interferometer. Before applying it to real channels, the apparatus must demonstrably implement the row coefficients, signs, units and operating range.

## C30.03-W1 — Same outputs, different states

For thetaA=(2,1), H thetaA=(2+1,4+2)=(3,6). For thetaB=(1,2), H thetaB=(1+2,2+4)=(3,6). Their difference is (1,−1), the invisible direction. One cannot choose between them from these two channels.

Add a third row (1,−1). It predicts +1 for A and −1 for B. Let s=theta1+theta2 and d=theta1−theta2. Adding the equations gives s+d=2theta1; subtracting gives s−d=2theta2. Therefore theta=((s+d)/2,(s−d)/2). The two rows (1,1) and (1,−1) are independent: no single multiplier turns the first into the second. Their rank is 2.

The physical-closure source T50 describes a related transfer obstruction: a scalar response can retain distinct gain/responsivity factorizations. In a dimensionless toy transfer with product gR=6, (g,R)=(2,3) and (1,6) give the same product. Exact wavelength geometry does not by itself choose either factor. A known reference that measures g separately can resolve this ambiguity within that product model.

## C30.03-P1 — Practice, then substitution

Recover theta for s=5,d=−1. Check all three original/added row outputs. Then describe what is missing when only gR=6 is recorded.

Answer: theta1=(5−1)/2=2 and theta2=(5+1)/2=3. The original channels are 5 and 10, and the new difference is −1. Product 6 alone cannot select a factorization; obtain a separate calibrated reference or retain the entire equal-product family. Do not discard the doubled channel: its disagreement with twice the first may reveal an unmodeled response.

> Claim scope: All numbers in the inverse examples are synthetic. T30 says detection needs a real blinded registered endpoint; extraction needs net-power accounting for a defined control volume; induction needs controlled reversing force/impulse evidence. Here an endpoint is a predeclared reported response, and a control volume is the bounded region whose energy flows are accounted for. Our rank calculation establishes none of those empirical outcomes.

## C30.03-D1 — Diagnostics and worked answers

1. Find another state giving (3,6). **Answer:** (0,3), because its sum is 3; there are infinitely many real examples.
2. Would row (3,3) resolve the ambiguity? **Answer:** No; it is three times (1,1), still blind to (1,−1).
3. For s=4,d=2, recover and check theta. **Answer:** (3,1), whose sum is 4 and difference is 2.
4. Why is adding row (1,−1) on paper insufficient for a detector claim? **Answer:** The apparatus must measure that combination with known transfer, orientation and calibration; an algebraic row does not construct an instrument.

Next dependency: [Lesson 4](lesson-04.md) chooses new measurements by their distinct predicted outputs.
'''
lessons[4]=r'''
# Lesson 4 — Choosing discriminating experiments

Essential question: Which next observation most directly separates the remaining candidate explanations?

Goals: Compare candidates on shared inputs; count distinguishable outcomes in a finite design; freeze a sign prediction; state the limits of a minimality argument.

Prerequisite bridge: Lesson 3 exhibited different states with the same sum and a row that separates them. A **candidate mechanism** explains how a state produces a response. Its parameters are the adjustable quantities in that explanation. To compare mechanisms fairly, specify the same input, units and measurement procedure before comparing their predictions.

## C30.04-E1 — A prediction must survive the observation

An experiment is informative when candidates predict different observable outcomes under a common contract. Repeating a sum channel can reveal temporal changes or transfer problems, but it cannot distinguish two fixed candidates whose sums are identical. A difference channel can separate them if its sign convention and calibration are independently known.

Explanatory compression means accounting for several observations with fewer independent choices. It is useful when accompanied by accurate predictions and retained residuals. It is not permission to delete inconvenient channels. Compare which observations each candidate explains, which parameters it fixes in advance, which it leaves free, and what would count as a mismatch. A candidate that chooses a new parameter after every result needs a new version; the original prediction remains in the ledger.

Cross-domain recurrence is a target for explanation. A common structure across geometry and instruments may motivate a shared mechanism. First keep the domains typed: a nanometre Cell3 basis and a unit-sphere galaxy coordinate system have different units and metrics. Connecting them requires an explicit transformation and new predictions, not merging their labels.

## C30.04-W1 — Two questions for four synthetic states

Consider states 00,01,10,11, each an ordered pair of bits. A bit is a value 0 or 1. Ask Q1, “is the first bit 1?”, and Q2, “is the second bit 1?” The answer pairs are respectively no/no, no/yes, yes/no, yes/yes. Thus these two questions distinguish all four states. One binary question has only two possible answers. Four states assigned to two answers must share an answer somewhere, so one question cannot distinguish all four. This proves minimality for this declared finite example.

I01 `/results/10` reports six goal-specific two-question portfolios with their own formal minimality witnesses. Our four-state count explains a design principle; it does not replace those witnesses or identify their actual questions. I01 explicitly leaves experimental execution open. Keep its six portfolios as designs, without fabricating favorable outcomes.

## C30.04-P1 — A mechanism comparison table

Use thetaA=(2,1) and thetaB=(1,2), fixed before any test, with all coordinates dimensionless. Complete the table and choose a discriminator.

| Proposed response state | sum | difference | newly fitted parameters allowed during check |
|---|---:|---:|---:|
| A | 3 | +1 | 0 |
| B | 3 | −1 | 0 |

Answer: The sum cannot choose. A calibrated difference sign can distinguish these fixed states. Record both predictions and preserve an “unresolved” outcome if calibration or the measured interval does not distinguish the signs. Neither table row alone is a detailed physical mechanism: a fuller candidate must explain why its state and transfer arise. State that remaining mechanism gap explicitly.

As a synthetic planning rule only, suppose a calibrated difference has a declared bounded error of 1/4. A predicts [3/4,5/4], B predicts [−5/4,−3/4]. These intervals do not overlap. A value 0 lies in neither, so retain a mismatch with both candidates. Do not force it into the nearer label or erase the value. A real interval must come from its actual calibration and uncertainty contract, not from this teaching choice.

> Claim scope: Binary counting and the table are exact finite deductions on synthetic inputs. The mechanism candidates and error bound are authored examples. Source portfolio minimality remains source-reported, and actual detection remains a prospective task.

## C30.04-D1 — Diagnostics and worked answers

1. Can one yes/no question distinguish four unrestricted states? **Answer:** No; at most two answer classes are available.
2. If both models predict sum 3, what does sum 3 choose? **Answer:** Neither model uniquely; preserve both.
3. If the difference is 0 under the toy interval rule, which candidate wins? **Answer:** Neither; the value is outside both intervals and remains a mismatch requiring explanation.
4. A researcher changes thetaA after reading the result. What record is needed? **Answer:** Preserve the original prediction/residual, declare the revised candidate and its extra choice, and reserve new independent data for its check.

Next dependency: [Lesson 5](lesson-05.md) freezes this comparison into a complete protocol.
'''
lessons[5]=r'''
# Lesson 5 — Preregistering a complete protocol

Essential question: What must be fixed before an experiment so that every outcome remains interpretable?

Goals: Write a prospective protocol with named fields; preserve all result branches; distinguish missing metadata from zero readings; define a reversible transform and stopping rule.

Prerequisite bridge: Lesson 4 froze competing predictions. A **protocol** is an executable instruction set for collecting and interpreting outputs. **Preregistration** means fixing a version before seeing the check outcomes. It prevents the original question from vanishing when an unexpected result motivates a new one.

## C30.05-E1 — Freeze the whole path

A usable protocol records the question, candidates and parameter values; source paths/hashes and domains; geometry/frame, site and orientation; device/channel identities; timing and exposure; calibration reference, version, units and uncertainty; training versus independent check roles; transformations and reconstructions; comparison branches; raw-data destination and metadata; stopping/interruption rules; and responsible operator and reviewer.

UTC is a common time standard. A midpoint timestamp identifies the middle of an exposure, not necessarily its start. Exposure duration states the interval over which the instrument collects a value. A blinded operator label conceals the candidate interpretation while preserving a separate recoverable label mapping. Training data may set parameters; check data evaluates the frozen version. A new version needs a new check allocation.

Non-destructive transformation means retaining enough to reconstruct the input. If a known offset b is subtracted, y_corrected=y_raw−b, retain b so y_raw=y_corrected+b. If invalid acquisition is independently identified, retain the affected raw row and its fault reason in parallel. A missing value cannot be converted to the numeric value zero.

## C30.05-W1 — Fully specified synthetic rehearsal v1

This is an arithmetic rehearsal, not an instrument run. The model fixes thetaA=(2,1), and two ordered operators: sum then difference. Prediction p=(3,1). Input rows are labeled S,D; all values are dimensionless. Transformation is identity; residual is r=y−p; reconstruction is y=p+r. Stop after both rows are supplied, or record interruption with whichever rows are present. Never impute an unprovided row. Candidate B stays (1,2), prediction (3,−1). Compare exact synthetic equality to each vector, retaining mismatch-to-both and absent/invalid cases.

The authored rehearsal inputs, revealed for the next lesson, are (3,0). This makes the exercise repeatable while preserving the original frozen prediction. A genuine future run must first replace every missing apparatus field below with verified information and freeze the new version. No device readings have been supplied here.

## C30.05-P1 — Draft a planned real protocol

Copy and complete this table. Its answer illustrates honest completion of a plan when instrument access is unavailable; a missing field is a gate on execution, not a fabricated value.

| Field | Planned value or unresolved entry | Owner / return address |
|---|---|---|
| Question and model | A versus B from Lesson 4; sum/difference predictions frozen | analyst / this lesson W1 |
| Source version | S02 mature geometry; S03 corrections; T30 capability boundary | analyst / sources.md |
| Raw destination | remain in instrument's original acquisition store; actual absolute location missing | operator / protocol field `raw_destination` |
| Instrument and channel IDs | missing; must demonstrate physical sum and difference response | operator / `device_channels` |
| Geometry/site/orientation | frozen convention needed; ICRS columns [a b c], intentional handedness; actual site/orientation missing | operator / `geometry_site_orientation` |
| Time and exposure | UTC midpoint convention selected; actual epoch and duration missing | operator / `timing` |
| Transfer/calibration | reference identity, version, operating range and units missing | calibration lead / `calibration` |
| Uncertainty | instrument-specific bounds and dependencies missing; toy 1/4 bound not adopted | calibration lead / `uncertainty` |
| Blinding | labels S,D hidden by custodian's retained mapping; real mapping not yet assigned | custodian / `label_map` |
| Training/check allocation | calibration/training records separate; future acquisition is check only | analyst / `roles` |
| Transform and outputs | preserve raw row, any offset/gain, transformed value, prediction, signed residual, reconstruction | analyst / `transform_v1` |
| Stop and exceptions | stop after two valid planned operator records, or log interruption; retain all attempted/faulted rows | operator / `stop_rule` |
| Comparison | A-compatible, B-compatible, unresolved overlap, mismatch to both, invalid/incomplete; retain raw values in every branch | analyst / `comparison` |
| Independent review | reviewer identity missing; must independently replay versioned analysis | research lead / `reviewer` |
| Execution state | planned; not ready for acquisition until required metadata and transfer are pinned | research lead / `execution` |

Answer: The table is a complete field inventory and an explicitly gated draft. It is not an executed experiment or a ready-to-run instrument contract. Recording the actual raw destination in place means pointing to the acquisition store rather than copying source data into this course. A calibration change creates a new version and retains the previous one.

> Claim scope: This course can finish the research portfolio while the empirical protocol remains planned. Detection, extraction and induction branches require different evidence (T30). Signed source events are kept by immutable reference, not reinterpreted as fourteen independent plane costs: the supplied bundle has three distinct plane-family cost levels.

## C30.05-D1 — Diagnostics and worked answers

1. A difference row never arrives. Is its residual −1? **Answer:** No; its value and residual are undefined/missing. −1 would follow from an actual numeric zero reading, a different case.
2. Subtract offset 2 from raw value 7. What is retained? **Answer:** Corrected value 5, offset 2, row identity and raw pointer; 5+2 reconstructs 7.
3. Can the toy uncertainty bound become an instrument bound? **Answer:** Only with a relevant calibration witness; an authored teaching number supplies none.
4. What happens after calibration changes mid-run? **Answer:** Record timing, old/new versions and all rows; mark the departure, preserve the frozen comparison, and define a new protocol/check scope.

Next dependency: [Lesson 6](lesson-06.md) interprets completed, discrepant and interrupted outcomes without erasure.
'''
lessons[6]=r'''
# Lesson 6 — Independent replication and negative outcomes

Essential question: How can an unexpected outcome identify the next useful measurement?

Goals: Compute and reconstruct signed residuals; distinguish replay from replication; preserve negative and invalid outcomes; propose a measurement separating model change from transfer change.

Prerequisite bridge: The protocol fixes prediction p and comparison rules before check data. A residual r is the componentwise difference y−p. Componentwise means subtract matching channels in their original order. It remains a primary coordinate of the result, not a reason to remove the row.

## C30.06-E1 — Keep both the model and the discrepancy

Replay uses the same inputs to check a computation. Independent replication obtains a new acquisition under a documented protocol with independently inspectable calibration and analysis. A second computer reading the same file is useful replay, but not a new physical observation. Independence is described by records: which apparatus, reference, operator, timing and processing are shared, and which are independently established? It is not asserted merely by changing a filename.

A zero response is a number. A negative response is a signed number. A failed acquisition is a record with a fault state. An interruption is an incomplete execution record. Preserve each according to its type. Compare residual patterns across channel, time, orientation and calibration state as possible missing coordinates. A new explanatory model can decode part of r, but the original p and r must still reconstruct the original y.

## C30.06-W1 — Rehearsal outcome

The authored, dimensionless rehearsal values from Lesson 5 are y=(3,0), with frozen A prediction p=(3,1). Thus r=(3−3,0−1)=(0,−1). Reconstruction gives p+r=(3+0,1−1)=(3,0), exactly the original pair. The sum agrees with A while the difference does not. For B, pB=(3,−1), so rB=(0,+1). Retain both signed residual vectors; neither candidate exactly matches the synthetic pair.

This pattern suggests at least two next branches. The underlying contributions might now be equal, giving a zero difference, or the difference-channel transfer might be failing or differently scaled. A known nonzero difference reference would test that transfer separately. Merely reusing the sum cannot separate those explanations. The instrument-specific known reference and its uncertainty remain to be specified before an empirical test.

## C30.06-P1 — Conditional future replication

If a future independent reading were (4,1), what residual would the frozen A prediction give? State what is retained and propose a separate calibration check.

Answer: r=(4−3,1−1)=(1,0). Reconstruction gives (3,1)+(1,0)=(4,1). This is a conditional example, not an observation. The sum changed while the difference did not. A separate known sum reference could test whether sum-channel gain changed; an independently calibrated contribution measurement could instead test a changed parameter sum. Keep both branches, the original prediction, the future acquisition identity, and the complete residual. For B the conditional residual is (1,2), also retained.

One informative next measurement has an input known independently of the unknown mechanism. In the toy product gR=6, if a known reference established g=2, then R=6/2=3 within that product model. The reference does the identifying work; the old product reading alone does not. In reality reference bounds and transfer conditions propagate into R's admissible range.

> Claim scope: This lesson performs synthetic arithmetic only. Agreement, disagreement and recurrence are all retained information. An unexplained residual motivates a mechanism test; it does not specify a unique mechanism without the additional distinguishing measurements.

## C30.06-D1 — Diagnostics and worked answers

1. For p=(3,1),y=(2,−1), find r and reconstruct. **Answer:** r=(−1,−2); (3−1,1−2)=(2,−1).
2. Is rerunning the same file on another computer independent physical replication? **Answer:** It is independent computational replay; a new acquisition is needed for physical replication.
3. May a negative result be removed from a summary table? **Answer:** Preserve its signed values and metadata; summaries may index it but cannot replace its residual record.
4. If a sensor saturates, why not set its reading to zero? **Answer:** Saturation is a fault/limit state, not a zero value. Retain the original recorded value, flag, range and reason, and keep any corrected view separately.

Next dependency: [Lesson 7](lesson-07.md) packages these records so another researcher can recover every distinction.
'''
lessons[7]=r'''
# Lesson 7 — Professional scientific communication

Essential question: Can another reader recover what was known, computed, proposed and still missing?

Goals: Write a source-addressed claim ledger; preserve raw field kinds; report a complete residual vector; propagate inherited boundaries into a conclusion.

Prerequisite bridge: A source pointer identifies a location, a hash identifies bytes, and an evidence class identifies what kind of support is present. A reproducible report joins these with equations, domain, units and retained results. A polished narrative without those joins cannot be independently checked.

## C30.07-E1 — Separate the layers in connected prose

Start with the question and the actual inputs. Report source observations or facts, then the transformations you performed, then inferred relationships, proposed mechanisms and unresolved branches. If reference theory is used, identify which assumption or prediction came from it. An archived theorem report, a new exact arithmetic check and a future measurement plan receive different execution statuses even if they appear in the same paragraph.

Give each equation its domain and units. State a model as “for these dimensionless synthetic channels, y=H theta,” not “the detector obeys H” when transfer has not been established. Retain source version mismatches as distinct branches. A return address allows a reader to inspect a disagreement rather than accepting an author's compressed conclusion.

JSON is a structured text format. A field can be present with the explicit value null; absent altogether; present with the string “unknown”; or present with the string “reported.” Those cases cannot be normalized to one blank without losing meaning. Keep presence, raw kind, raw value and pointer separately. An explicitly null boundary field is not a proof that there are no restrictions. S03 AUD-010 requires inherited constituent boundaries to travel to the endpoint.

## C30.07-W1 — A compact research ledger

| Report item | Result and support | Retained limitation |
|---|---|---|
| Source closure | S02 `/backbone_sequence/19`, 18 core modules plus explicit premises and states; S03 AUD-001/AUD-011 corrections | source-attributed theorem; unloaded bodies remain unloaded |
| Fresh finite check | Lesson 3 H rows (1,1),(2,2) measure one combination; A and B both give (3,6) | synthetic dimensionless model; no calibrated detector asserted |
| Rehearsal | p=(3,1), y=(3,0), r=(0,−1), y=p+r | authored data, not acquired observations |
| Prospective test | calibrated difference and separate reference under Lesson 5 protocol | planned; device/reference/timing fields missing |
| Open return paths | T20 named route certificate; S03 AUD-008 precision linkage; source spectral revision discrepancy | numerical replay of those source claims remains gated |

A report sentence can now be precise: “The supplied backbone reports conditional closure; our synthetic inverse calculation identifies only the sum from the original two channels. A proposed calibrated difference channel separates the frozen alternatives. The rehearsal retained a −1 difference residual; no real acquisition was performed.” Each clause has a different evidence role and an inspectable address.

## C30.07-P1 — Preserve four raw statuses

Use the synthetic object `{"a":null,"c":"unknown","d":"reported"}`. Make a row for each requested pointer /a,/b,/c,/d.

| Pointer | Present? | Raw kind | Raw value |
|---|---|---|---|
| /a | yes | null | null |
| /b | no | absent | no value exists |
| /c | yes | string | unknown |
| /d | yes | string | reported |

Answer: Reconstruct the object by emitting only present fields, with their original kinds. This returns exactly a=null,c="unknown",d="reported", and no b key. Retain the object's source/version address as well. A statement “b is null” would be false because b was absent. These four rows are not observations about the archival sources; they are a synthetic data-handling exercise.

> Claim scope: S03's reported nonzero reconstruction residual `4.58938078934712923077736690075e-12` at AUD-008 remains a source-reported closure coordinate with missing full precision linkage, not literal exact zero. The named route certificate and some proof bodies remain retrieval gaps. No short summary, null endpoint, or toy calculation supplies those missing witnesses.

## C30.07-D1 — Diagnostics and worked answers

1. What is wrong with replacing (0,−1) by “small error”? **Answer:** Sign, channel and reconstruction information vanish. Keep the vector and use any summary only as an index.
2. If /a is null and /b absent, can a decoder emit both keys with null? **Answer:** No; it changes presence. Emit a only and retain b's absence.
3. A constituent excludes force inference but its endpoint boundary is null. What belongs in the report? **Answer:** The force boundary and the raw null occurrence, with return addresses; null does not remove inherited restrictions.
4. Which dates are needed? **Answer:** Source/version dates, actual fresh computation date, and planned versus actual acquisition dates separately. An unexecuted plan has no invented execution date.

Next dependency: [Lesson 8](lesson-08.md) joins the ledger and calculations into a defensible continuous research chain.
'''
lessons[8]=r'''
# Lesson 8 — The integrated research defense

Essential question: Can every step from geometry to the next instrument test be defended without losing a premise or residual?

Goals: Reconstruct all decoder channels; retain six phase factors; state an explicit geometric-to-instrument interface; defend a prospective discriminator with its remaining gaps.

Prerequisite bridge: Lessons 1–7 taught coordinates, witness scope, matrix rows, inverse recovery, frozen comparisons and residual reporting. Here we add a small decoder calculation and teach its operations before the capstone. The advanced source names are reading labels; the finite calculations below require only multiplication, addition and simultaneous equations.

## C30.08-E1 — Connect the interfaces

A continuous chain has five interfaces: geometry defines addresses and lengths; a supplied trajectory/ruler turns displacement into phase coordinates; a proposed transfer maps these to instrument channels; a decoder separates a modeled component and retained residual; and an independent test compares frozen candidates. Every interface must name its inputs and output units. A missing physical transfer is an explicit proposed link rather than an invisible implication.

For a synthetic extension of Lesson 1, let q0=(0,0,0),q1=(1/2,0,0). The displacement is a/2 in nm, using the pinned mature column. Choose a synthetic dimensionless phase coordinate phi=2(q1_1−q0_1)=1. Here subscript 1 means first component and factor 2 is a supplied ruler convention, not a measured coupling. A proposed normalized transfer produces y_S=theta1+theta2 and y_D=phi(theta1−theta2). At phi=1 it is exactly Lesson 3's sum/difference model. Calibration must show how actual readings become these dimensionless channels; a prediction of phase alone cannot establish force or energy extraction. For A=(2,1), prediction is (3,1); for B=(1,2), it is (3,−1). This connects an exact address construction to a falsifiable proposed transfer without inventing the missing apparatus witness.

### A three-channel decoder bridge

Use the synthetic matrix A=[[1,0],[0,1],[1,1]] and y=(2,3,6), all dimensionless. A coefficient pair c=(c1,c2) predicts Ac=(c1,c2,c1+c2). Set r=y−Ac and retain all three entries. To choose a reproducible decomposition, require r1+r3=0 and r2+r3=0. These equations make the residual's dot product with each column of A zero; a dot product multiplies matching entries and adds them. This is a coordinate convention for decomposition, not a reason to erase r.

Substitute r=(2−c1,3−c2,6−c1−c2). The conditions give 2c1+c2=8 and c1+2c2=9. Doubling the first and subtracting the second gives 3c1=7, so c1=7/3. Then c2=8−14/3=10/3. Thus Ac=(7/3,10/3,17/3), r=(−1/3,−1/3,1/3). Adding produces (6/3,9/3,18/3)=(2,3,6). Both dot products are zero. Two coefficient coordinates plus one independent residual coordinate retain the three original channels. This is an analogue of S02 M17's six active plus seven syndrome coordinates in a 13-channel source system; it is not the source's 13-by-6 matrix.

## C30.08-W1 — All six determinant-line factors

S02 M15 names UV, light, regulator, heavy, cap and induced contributions and a trivialization, a chosen way to represent the combined line in ordinary complex numbers. It also retains topology and admitted sectors, meaning the permitted classes of states on which closure is claimed. A scalar toy can demonstrate why no factor may be dropped, without proving the global construction.

Teach the needed arithmetic: i is a symbol with i²=−1. Ordinary distributive multiplication then gives i(−i)=1. In a chosen synthetic scalar representation let (UV,light,reg,heavy,cap,induced)=(i,i,−1,−i,i,1). Multiplication in order gives i·i=−1, then (−1)(−1)=1, then −i, then (−i)i=1, then 1. Removing heavy instead gives i·i·(−1)·i·1=i. Thus the complete product is 1 but the shortened one is i. This proves only the displayed arithmetic. It does not prove existence of a global trivialization or closure in every admitted sector.

## C30.08-P1 — Prepare the defense

Reconstruct y=(2,3,6) from the decoder pair above and every residual entry. Then attach the geometric phi construction, proposed sum/difference transfer, calibration gate, frozen A/B predictions and all outcome branches to a single ledger.

Answer: Reconstruction is (7/3−1/3,10/3−1/3,17/3+1/3)=(2,3,6). Keep this decoder demonstration separate from the two-channel A/B experiment: c is not theta and the 3-channel y is not the prospective detector pair. The common connection is the information-retaining method. Geometry supplies q and a/2, the synthetic ruler supplies phi=1, and the proposed transfer supplies the sum/difference rows. Test A/B only after calibration establishes those rows. Retain A-compatible, B-compatible, unresolved/overlapping, mismatch-to-both and invalid/incomplete branches. M19 remains outside core M20, compiler labels keep their own namespace, and unprovided certificates remain gaps.

> Claim scope: The integrated defense is a complete research argument with a next test. Source-reported closure, exact synthetic calculations, proposed mechanisms and planned measurements have distinct roles. The decoder is not a fresh physical occupation-selection proof, and its coefficient c must not be confused with Cell3 column c.

## C30.08-D1 — Diagnostics and worked answers

1. What is the third reconstructed decoder channel? **Answer:** 17/3+1/3=6; omitting its residual would give 17/3 instead.
2. What happens if the heavy scalar factor is deleted? **Answer:** Product i replaces 1; the original six-factor record must remain intact.
3. Does phi=1 measure a force? **Answer:** It is a synthetic dimensionless phase coordinate under a chosen ruler. Force requires a separate calibrated force/impulse witness.
4. What must a defense say about an unavailable route certificate? **Answer:** Give its known source return address, mark the body missing, and state which source replay is gated; do not fill it using the toy calculation.

Next dependency: [Capstone](capstone.md), eight previously practiced operations assembled into a 32-point research portfolio.
'''
for n,t in lessons.items(): write(f'lesson-{n:02}.md',t)

# Compact authored source ledger; source JSON files are never copied.
lines=['# Sources and exact dependency return addresses','',
'Retrieval date: 2026-11-05. Source files were read in place, and all five supplied archival SHA-256 hashes matched. These are source-reported mathematical/research records, not fresh formal verification. Only small selected numerical teaching inputs and authored provenance are retained here.','',
'## Archival registry','', '| ID | Absolute path | SHA-256 | Read scope / role |','|---|---|---|---|']
for x in D['sources']:
 if 'path' in x:
  assert digest(Path(x['path']))==x['sha256']
  scope={'S01':'Historical corrected branch; hash and structure inspected, not active constants','S02':'/proof_contract, /mature_locked_cell3, /constitutive_principles, /backbone_sequence','S03':'/findings/0 through /findings/12; correction authority','S04':'Audit context; hash and structure inspected, not fresh audit execution','S05':'Historical cross-domain context; hash and structure inspected, not new empirical evidence'}[x['id']]
  lines.append(f"| {x['id']} | `{x['path']}` | `{x['sha256']}` | {scope} |")
lines+=['','## Live source-module table','',
'Generated by reading S02 `/backbone_sequence` in place. Each list below is the actual source-local `requires`, not the defective serialized edge list. Non-module requirements are preserved verbatim. Titles serve as recognition labels; advanced source constructions are not untaught capstone calculations.','',
'| Module / pointer | Source title | Requires |','|---|---|---|']
for i,m in enumerate(S['backbone_sequence']): lines.append(f"| {m['id']} /backbone_sequence/{i} | {m['title']} | {', '.join(m['requires']) or 'none (root contract still applies)'} |")
lines+=['','M20 receives 18 core edges. M19 is separate. Full internal graph: 52 requires-derived edges. EG-A1 through EG-A6, supplied coordinates and domain hypotheses remain part of the contract. S03 AUD-001 corrects the edge ledger; AUD-011 corrects compressed premise wording.','',
'## Pinned testbench and integration sources','',
'The read-only capabilities call succeeded. Its response did not include a corpus generation; subsequent RAG and graph traversal returned generation and manifest digest `5bdbf0c70fed3830b8239d3107bc47cd950a7e6d6f7813edfc4dd605e39990c7`, matching the packet. Traversal of application:kfield-lucas-lab at depth one was truncated; it is discovery, not complete proof coverage. RAG used rerank:false.','',
'| ID | Exact logical path | SHA-256 | Fresh read / locator |','|---|---|---|---|',
'| T50 | applications/kfield_lucas_lab/rag_corpus/50_physical_closure.md | c2a25a583af904601968adc1d3efde825f76218c92a2f52d829afc093f52c02a | bounded bytes 0–1761; item 4 optical-transfer obstruction |',
'| T20 | applications/kfield_lucas_lab/rag_corpus/20_phase_route.md | c9335e2df74344bff5665df5a5e0b9094fef22147c76458f1a54efe49cefce62 | bounded bytes 0–470; route paragraph |',
'| T30 | applications/kfield_lucas_lab/rag_corpus/30_interferometer_capabilities.md | e9c6d0346e7f4fa120e9836df9d4a45b7e2c587bc046874d91cb38a0c68c16bc | bounded bytes 0–687; capability paragraph |',
'| I01 | applications/kfield_standard_model/collaborator_record/project_record.json | 3800c854da827a64e72507722904bcafab07a31e88f2bc73920a8e7f62f62c1c | bounded bytes 0–13847; /results/9, /results/10, /hazards, /open_obligations |',
'| I02 | applications/kfield_standard_model/collaborator_record/evidence/p12_standard_model_compiler_adjudication_report.json | a3dfca0e55e525c6522c3088b95e5bcc048c141fce340bfe980fcfc14123220a | bounded bytes 0–3173; /direct_authority_modules, /semantic_fence, /known_science_replay |',
'','Ranges are start-inclusive/end-exclusive; returned complete-range digests matched the object IDs. No Agda compiler was executed. I02 reports compiler M03,M07,M08 direct authority and a non-promotion fence. The compiler M20 compositeNonterminal label is preserved from the input teaching contract; its declaration body was not freshly retrieved here. I01 retains Z1,Z2,Z3,Z6 and six unperformed portfolio designs.','',
'## Boundaries carried forward','',
'1. S02 M02 proof prose omits the affine origin in a reciprocal-plane identity; use g_h dot (x−O_K)=m, with g_h=B^(−T)h. Stored reciprocal witnesses disagree across branches; canonical mature spacings are 0.32954652969544673, 0.4515973797212846, 0.6050977415185554 nm (S03 AUD-005). Historical values remain at their original addresses, never mixed into active examples.',
'2. M_cell=B^T B is the direct metric in nm², R_cell=M_cell^−1 the reciprocal metric in nm^−2. They are not G_phase or G_eff. Q as a detail operator, Q_g as an integerized ray, Q_nu as a frequency-related cost and Q as a distance symbol are source-local meanings, not interchangeable quantities. The course does not numerically replay missing phase matrices.',
'3. Source carrier tuples are color-first C_3 direct-sum W_2; a weak-first view needs an explicit permutation (AUD-004). Detector parity, carry parity, projective sign, chirality, family labels, primitive lifts and dyadic/ternary recursions remain distinct. These are recognition boundaries, not new computations required in this course.',
'4. For integerization residual epsilon=nint(x)−x in [−1/2,1/2), choose half-ties toward the lower integer: nint(x)=ceil(x−1/2). This is separate from cell ownership floor(q+1/2), whose local residual is q−z. AUD-013 requires an explicit convention; finite decimals are stored-precision witnesses, not infinite-precision identities.',
'5. The detail-product identity needs E idempotent and appropriate conditional-expectation/bimodule properties, beyond Q=I−E (AUD-006). Our mean/detail exercise proves reconstruction directly and does not invoke that stronger identity. The finite difference product retains (df)(dg).',
'6. AUD-007/009 retain source-reported mature gates while missing bodies remain VERIFIED_NOT_LOADED. This includes occupation-selection and other replay objects; rank arithmetic cannot replace their physical-state selection argument.',
'7. AUD-008 records residual 4.58938078934712923077736690075e-12 with missing complete G_phase,C,W_qpc precision linkage. No equality-to-zero promotion is made. AUD-010 propagates all constituent boundaries despite null endpoints.',
'8. T20 describes the named least-cost route certificate, but its full body and numerical bounds were not retrieved. T50 names contracts/kfield_physical_closure_v1.json and agda/PhysicalClosure.agda; discovery returned source prose rather than those full bodies. We teach its reported equal-output obstruction and independently verify a synthetic analogue; no source numerical contract is claimed replayed.',
'9. Packet spectral references retain all fourteen signed event rows by immutable reference, with only three distinct plane-family cost levels. Bundle SHA 04044230f3b2536d22654b294760106eca301f212e4eb4157989b330ff611f17; spectral-work SHA d4105a6d6802e6bb2a2ba8e76a1d23a27973fca3d3335fd8335690a41ab72dfa; energy-work SHA 9120f80210b235b8612d6479fe25272eb3824f31c5a1394e7e9d12718e57e70f. Three distinct levels alone do not establish statistical independence. These are packet provenance, not freshly read acquisition data. Cross-document revision discrepancies remain unresolved source branches; no numeric spectral assessment relies on them.',
'10. Packet physical CMB speed is 369812.50200040644 m/s, distinct from phase-transformed vectors. The Galactic Center is a visual gauge; no Solar/Galactic short-window dynamics are added. Galaxy unit-sphere and Cell3 length geometry are separately typed. Model photon-equivalent energy is not measured energy transfer.',
'','The remaining source gaps limit source replay, not the solvability of the declared finite teaching tasks. All actual lesson and capstone numerical data are completely supplied and labeled synthetic or stored-source decimal arithmetic.']
write('sources.md','\n'.join(lines))

rows=['# Course map','',D['topic'],'',
'Audience: high-school seniors. Entry capabilities: signed arithmetic, fractions, ratios, powers, linear equations and coordinate graphs, plus the prior series capabilities from courses 19–23 and 27–29. Local bridges teach matrix-row multiplication, finite rank, coordinate ownership, raw JSON kinds, complex scalar multiplication and retained decoding before assessment. Advanced module names are recognition-only.','',
'Eight lessons, 16 core periods of 55 minutes, plus three capstone periods: 1045 minutes total. Multi-period lessons are intentionally retained to allow source-map rehearsal and defense. Each period allocates 5 minutes retrieval, 20 instruction/worked example, 15 guided practice, and 15 diagnostics/repair.','',
'| Lesson | Periods / minutes | Explanation | Worked example | Answered practice | Diagnostic | Later use / capstone |','|---|---|---|---|---|---|---|']
periods=[3,2,2,2,2,1,1,3]
for i,m in enumerate(D['course_map'],1):
 c=f'C30.{i:02}'
 rows.append(f"| [lesson-{i:02}](lesson-{i:02}.md): {m['title']} | {periods[i-1]} / {55*periods[i-1]} | {c}-E1 | {c}-W1 | {c}-P1 | {c}-D1 | {m['later_use']} / C30-CAP-{i:02} |")
rows+=['','## Unit checkpoints','',
'After lesson 2: reconstruct M20 inputs and classify witnesses without namespace promotion. After lesson 4: recover theta and choose a genuine discriminator. After lesson 6: execute the synthetic protocol and reconstruct every provided row, preserving absent/invalid cases. After lesson 8: defend the geometric ruler/transfer interface, three-channel decoder and six-factor boundary before the capstone.','',
'The approved anchors are expanded rather than replaced. The finite M17 decoder and complex multiplication are taught explicitly in lesson 8 before use. The synthetic geometric phase/transfer bridge also appears there to make the portfolio continuous; it is labeled a proposed interface, not an archived physical coupling. No substantive teaching is added during assembly.','',
'## Observable capstone coverage','']
for x in D['capstone_specification']['backward_map']:
 rows.append(f"- {x['step_id']}: {x['operation']}. Introduction {x['explanation_id']}; model {x['worked_example_id']}; independently answered practice {x['prior_practice_id']}; check {x['diagnostic_id']}. See the matching concrete input/output and rubric in capstone.md.")
write('course-map.md','\n'.join(rows))

write('terminology.md',r'''
# Terminology and notation

| Term / symbol | Meaning and domain | First teaching |
|---|---|---|
| premise / domain hypothesis | supplied assumption / condition restricting an operation | 1 |
| state coordinate | a value selecting a state within an allowed family | 1 |
| dependency A → B | B uses A, not automatically the converse | 1 |
| namespace | named identifier system; compiler and backbone M labels remain separate | 2 |
| B=[a b c] | mature ICRS column basis, entries in nm, negative determinant intentional | 1 |
| x, O_K, q | position and origin in nm; dimensionless address in x=O_K+Bq | 1 |
| z, u | integer cell address and local coordinate, q=z+u | 1 |
| floor / half-open | greatest integer no larger than input / include left but exclude right endpoint | 1 |
| m,h | local mean and signed half-difference, not mass or Planck constant | 2 |
| witness / hash / pointer | supporting object / byte fingerprint / location within structured source | 2 |
| proof / replay | implication under premises / execution on specified inputs | 2 |
| calibration / observation | reference-to-response relation / acquisition record | 2 |
| protocol / preregistration | executable plan / version frozen before check outcomes | 2,5 |
| theta=(theta1,theta2) | synthetic response contributions, dimensionless | 3 |
| H, y=H theta | measurement row table and its output; synthetic dimensionless examples | 3 |
| s,d | sum and difference channels, dimensionless; d is not a distance here | 3 |
| rank / null direction | independent measured combinations / parameter change with zero output change | 3 |
| identifiable / equal-output family | unique under model and domain / inputs sharing an output | 3 |
| g,R | toy gain and responsivity, dimensionless product example; R is not R_cell | 3 |
| phase / beat frequency | cycle position / cycles per second; neither implies force or power | 3 |
| candidate mechanism | proposed causal account with parameters and predicted observables | 4 |
| bit | binary value, 0 or 1 | 4 |
| uncertainty interval | declared admissible range from a specified contract, not erasure rule | 4 |
| p,r | frozen prediction and retained residual r=y−p | 5,6 |
| UTC midpoint / exposure | common time convention at collection midpoint / duration of collection | 5 |
| replication | new acquisition with independently inspectable protocol and calibration | 6 |
| null / absent / string | distinct raw data kinds and presence states | 7 |
| A,c in decoder | 3-by-2 synthetic design and two coefficients; not candidate A or basis column c | 8 |
| dot product | multiply matching entries and add; used for residual convention | 8 |
| phi | synthetic dimensionless phase 2 times first-address displacement | 8 |
| i | complex unit with i²=−1 | 8 |
| trivialization / sector | representation of combined line by scalars / admitted class of states | 8 |
| syndrome | retained residual coordinates; small analogue has one, source M17 reports seven | 8 |

Source-only notation is separately scoped in sources.md: M_cell, R_cell, G_phase, G_eff and the several Q symbols are not silently merged. EG principles and M modules are source reading labels. UV/light/reg/heavy/cap/induced are the six M15 factor labels; the displayed scalar example teaches multiplication without requiring determinant-line theory. “Source-reported” is an evidence attribution, never a numeric value or an automatically verified status.
''')

write('teacher-guide.md',r'''
# Teacher guide

Teach this as an integrated senior research course with eight lessons across 16 core 55-minute periods, then three capstone periods. Students produce a complete portfolio even though the real protocol remains explicitly planned. Do not arrange an unprovided experiment or substitute classroom arithmetic for an empirical witness.

Each period: 5 minutes retrieval from prior work; 20 minutes explanation and the worked operation; 15 minutes guided practice with an individual written response before revealing answers; 15 minutes independent diagnostic checks and correction. Preserve corrected drafts so students can identify which premise or operation changed. If a student cannot reconstruct the inputs or distinguish a source claim from a measured result, add a recovery period before dependent work; log that pacing change.

| Lesson | Sessions and classroom product | Check before advancing |
|---|---|---|
| 1 (3 periods) | module-role cards; premises/state ledger; corrected dependency map and boundary coordinate | all 18 incoming core requirements, M19 separate, q=z+u |
| 2 (2) | witness classification; namespace and return-address exercise | exact mean/detail reconstruction; no proof-to-measurement promotion |
| 3 (2) | row arithmetic and invisible direction; inversion and calibration ambiguity | substitute recovered theta into all rows |
| 4 (2) | finite two-bit discriminator; candidate comparison and bounded-error branches | frozen predictions, overlap/mismatch branches retained |
| 5 (2) | synthetic rehearsal protocol; gated real protocol field ledger | missing is not zero; raw and transform parameters reconstruct |
| 6 (1) | all residual channels and replication design | both synthetic residuals and conditional status correct |
| 7 (1) | claim ledger and four raw-status rows | reverse-readback preserves absent key and explicit null |
| 8 (3) | phase factors; decoder and transfer chain; oral defense | full reconstruction, all six factors, no hidden physical transfer |

At the four unit boundaries in course-map.md, ask students to exchange work and try to find a missing prerequisite, an unscoped symbol, a changed source branch or an erased outcome. Require a specific file/section and corrected calculation, not a general complaint. The teacher answer keys are in each lesson and capstone.md. The executable verification script provides a second check, but students should show hand calculations before seeing its output.

Common teaching repairs: if matrix notation is unfamiliar, replace each row with its expanded linear equation; if fractions obstruct the decoder, multiply all channels by 3 and reconstruct (6,9,18) before dividing; if i is unfamiliar, use only i²=−1 and multiply left to right. For source maps, teach arrows as recipes rather than requiring students to derive the advanced modules. The assessment requires reading their roles and boundaries, not university-level proof reconstruction.

Keep the distinction between two separate synthetic systems visible on the board: theta is the two-channel candidate experiment, while c is the three-channel decoder analogue. They share a retention method but are not the same data. Neither is an empirical Cell3 coupling. The exact source coordinate operation uses stored mature B decimals and synthetic q. The phase ruler and detector transfer are proposed teaching interfaces with explicit calibration gates.

Capstone session 1: prepare source/premise ledger and dependency map, classify witnesses, solve the inverse problem. Session 2: compare candidate predictions, freeze protocol, compute conditional replication residuals. Session 3: finish raw-kind ledger and integrated defense, then apply the 32-point rubric and repair. Students may consult all course artifacts; there is no need to retrieve missing source data to solve an assessed question.

For oral defense, ask: “Which arrow requires a calibration?”, “What would a zero, missing or saturated channel mean?”, “What survives if the favored mechanism fails?”, and “Can I reconstruct every supplied value from your report?” Accept alternate prospective designs when they preserve all inputs, candidate-specific predictions, identifiable transfer requirements and outcome branches. Do not reward an unsupported empirical claim for sounding decisive.

Source gaps are legitimate reported boundaries: full route certificate, phase precision linkage and some formal/occupation bodies are not newly supplied. The course does not repair the archival corpus. The author's local calculations and deterministic packaging checks are distinct from the archived proof or empirical statuses.
''')

write('capstone.md',r'''
# Capstone — A reproducible geometric-to-instrument research portfolio

Work in three 55-minute sessions. Use lessons and sources.md; no outside calculation, experiment or university mathematics is required. All supplied numerical data below are synthetic except the explicitly identified stored mature column in lesson 1. Produce eight labeled sections C30-CAP-01 through C30-CAP-08. Keep source readings, finite calculations, proposed transfer and future measurements distinct.

## Student task packet

1. **C30-CAP-01 — Dependency ledger.** Using the exact source-module table, show all 18 core inputs of M20 and trace M17, M18 and separate M19. Classify EG-A2 and the occupied coefficient c. State all six constitutive principles and four state-coordinate entries. Output a source-addressed map with inherited boundaries. Practiced in C30.01-P1.
2. **C30-CAP-02 — Witness cards.** Classify the five cards in lesson 2's P1; give each a return address, assumptions and execution status. Explain the distinction between compiler and backbone M20 and preserve the integration's global-form alternatives and portfolio status. Output a five-row evidence table. Practiced in C30.02-P1.
3. **C30-CAP-03 — Inverse problem.** H has rows (1,1),(2,2); the sum is s=5, and an added difference row (1,−1) gives d=−1. Recover theta and check all rows. Explain why a detector product gR=6 alone cannot select factors. Output the solved parameters, checks and calibration gap. Practiced in C30.03-P1.
4. **C30-CAP-04 — Discriminator.** For a separate frozen candidate test use thetaA=(2,1),thetaB=(1,2). Compute sum and difference predictions, explain which distinguishes them, and use lesson 4's synthetic 1/4 bound to include mismatch/overlap logic. State why the four-state, two-bit example and six source portfolios are designs with separate scopes. Output a comparison table and next question. Practiced in C30.04-P1.
5. **C30-CAP-05 — Protocol.** Draft the planned real protocol using every field in lesson 5's P1. Freeze the two operator predictions; specify raw retention, UTC midpoint, exposure, orientation, calibration, units, blinding, independent roles, stop, exception and comparison branches. Mark unavailable fields with owner and return address. Output a versioned, gated plan, not fabricated readings. Practiced in C30.05-P1.
6. **C30-CAP-06 — Residual and replication.** For pA=(3,1), first reconstruct the authored rehearsal y=(3,0). Then consider the conditional independent future reading (4,1): compute residuals for both A and B and identify a separate calibration measurement. Output both complete residual ledgers and the replay/replication distinction. Practiced in C30.06-P1.
7. **C30-CAP-07 — Report fidelity.** For {"a":null,"c":"unknown","d":"reported"}, preserve /a,/b,/c,/d as four raw-status rows and reconstruct the object. Add a paragraph with separate source, calculation, mechanism and unresolved layers, including route/precision gaps and inherited boundaries. Output a readback table and report paragraph. Practiced in C30.07-P1.
8. **C30-CAP-08 — Integrated defense.** Follow the lesson 8 geometric chain q0=(0,0,0) to q1=(1/2,0,0), stored a/2 displacement and proposed phi=1 ruler/transfer. Separately reconstruct the three-channel decoder with A=[[1,0],[0,1],[1,1]],y=(2,3,6),c=(7/3,10/3),r=(−1/3,−1/3,1/3). Multiply all six toy phase factors and compare deleting heavy. State the next calibrated discriminator and all failure branches. Output a continuous chain with separate data-system labels and remaining source gates. Practiced in C30.08-P1 and W1.

## Full answer key and 32-point rubric

Award four points per section, one for each criterion stated below. Arithmetic slips earn only the criteria still satisfied; no point may be earned by fabricating an observation. Every criterion corresponds to previously taught work.

### C30-CAP-01 (4)

M20 requires M01–M18 (18 modules). M17 inputs M05,M11; M18 inputs M03,M04; each feeds M20. M19 inputs M07,M08,M10,M13,M18 and remains a separate mixed extension. EG-A2 is the constitutive decoder premise; occupied c is a supplied state. EG-A1–A6 mean complete state, decoder, finite transition, finite product with joint term, residual retention, typed renderer. Four state entries are pre-anchor scale, time/action normalization, vacuum magnitude/admitted coefficients, occupied six-coordinate state. Cite S02 /backbone_sequence/19 and /constitutive_principles plus S03 /findings/0 and /findings/10. Points: 1 source/premise typing; 1 correct core and branch map; 1 supplied-state distinction; 1 full premises and retained M19 boundary.

### C30-CAP-02 (4)

A is algebra with mean/detail reconstruction; B is a replay receipt on exact inputs; C is calibration against a known reference and conditions; D is an acquisition observation with identity/time; E is an unexecuted protocol. Missing real addresses remain missing in the synthetic cards. A report should cite lesson-02 C30.02-P1 for the teaching cards, I01 /results/9,/results/10 and I02 /direct_authority_modules for integration facts. Compiler M20 compositeNonterminal and backbone M20 closure have distinct namespaces. Retain Z1,Z2,Z3,Z6; six portfolios are planned designs. Points: 1 typed cards/addresses; 1 five classifications; 1 namespace/evidence distinction; 1 alternatives and unperformed boundary.

### C30-CAP-03 (4)

theta=((5−1)/2,(5+1)/2)=(2,3). Checks: 2+3=5; 2·2+2·3=10; 2−3=−1. The original two rows have rank 1 and invisible direction (1,−1); the added difference raises recoverable combinations to 2 if physically implemented. Product 6 admits (2,3) and (1,6); a separate reference is required to identify a factor. Points: 1 dimensionless inputs and transfer domain; 1 correct inversion; 1 all row checks; 1 retained ambiguity/calibration gate.

### C30-CAP-04 (4)

A predicts (3,+1), B predicts (3,−1). The sum is shared; difference separates the fixed candidates. With the synthetic 1/4 bound, intervals [3/4,5/4] and [−5/4,−3/4] are disjoint; zero matches neither. Actual uncertainty overlap would leave ambiguity. Four synthetic states 00,01,10,11 require at least two yes/no answers because one yields only two classes. That count is not the witness for the six source-specific portfolios. Points: 1 shared model/parameter contract; 1 predictions; 1 discriminator/count reasoning; 1 mismatch/uncertainty and source-design boundary.

### C30-CAP-05 (4)

The completed answer is the field table in lesson-05 P1, adapted as protocol version 1 with planned execution state. Preserve A/B predictions, identity/order of sum and difference, r=y−p, reconstruction, all attempted rows, original acquisition store pointer, explicit missing actual epoch/duration/device/reference/units and reviewer, and required metadata gates. An operator/custodian retains the blinded label map. Stop after the planned pair or document interruption; do not fabricate a missing row. Calibration changes are versioned. Points: 1 all physical/timing/source fields with missing status and owners; 1 frozen operations and comparisons; 1 reversible/raw record design; 1 exceptions, independent roles and unexecuted status.

### C30-CAP-06 (4)

Rehearsal rA=(0,−1),rB=(0,+1); pA+rA=pB+rB=(3,0). Conditional future rA=(1,0),rB=(1,2); both reconstruct (4,1). A separate known sum reference can test a gain change; an independently calibrated state measurement can test changed sum. Neither has occurred here. Replay recomputes existing values, while replication needs a new acquisition identity and inspectable calibration/protocol. Points: 1 authored versus conditional labels; 1 all four residual pairs; 1 both reconstructions; 1 distinguishing next reference and retained branches.

### C30-CAP-07 (4)

/a: present/null/null; /b: absent/no raw value; /c: present/string/unknown; /d: present/string/reported. Emit a,c,d with their original kinds and no b key. A suitable paragraph says: “S02 reports closure under explicit premises; the finite sum/difference calculation distinguishes fixed synthetic states. A calibrated physical difference response is proposed. The rehearsal retains (0,−1); the named route certificate and phase precision linkage remain unavailable, and constituent boundaries survive null endpoints.” Include dates/source hashes from sources.md and label no real execution. Points: 1 raw presence/kinds; 1 exact readback; 1 layered report with return addresses; 1 residual and inherited-gap retention.

### C30-CAP-08 (4)

q displacement is (1/2,0,0), physical displacement is (0.1637506210279453,−0.0274485039420032,−0.01874375144736495) nm using stored source decimals. phi=2·1/2=1 is a supplied synthetic ruler, followed by proposed normalized sum/difference transfer; it requires actual calibration. Decoder Ac=(7/3,10/3,17/3); adding r yields (2,3,6), with r1+r3=r2+r3=0. This decoder c is separate from theta and from basis column c. Six phase factors multiply to 1; deleting heavy gives i. A scalar calculation does not prove global trivialization or every admitted sector. Next test: independent calibrated difference under the frozen A/B protocol, plus reference testing where transfer remains ambiguous. Preserve A-compatible, B-compatible, unresolved overlap, mismatch-to-both and invalid/incomplete outcomes, every residual, M19/namespace distinctions and source replay gates. Points: 1 typed geometric/ruler/transfer chain; 1 decoder reconstruction; 1 six-factor arithmetic and scope; 1 frozen next test and all retained branches.

Total: 32 points. Repair any wrong reconstruction, invented empirical claim, erased outcome or missing calibration gate before accepting the portfolio, regardless of total. These are correctness conditions, not optional presentation preferences.
''')

# Initial draft recovery: checks are not marked passed until review and verification.
ordered=['course-map.md','sources.md','terminology.md']+[f'lesson-{i:02}.md' for i in range(1,9)]+['teacher-guide.md','capstone.md','course.md','audit_report.json','verification.json','verify_examples.py','build_course.py','completion_report.json']
write('course.md','# '+D['topic']+'\n\n'+ '\n\n'.join(f'<!-- BEGIN: lesson-{i:02} -->\n'+(P/f'lesson-{i:02}.md').read_text(encoding='utf-8').rstrip() +f'\n<!-- END: lesson-{i:02} -->' for i in range(1,9)))
checks=[]
for f in ordered:
 if f=='completion_report.json': continue
 cid=Path(f).stem
 kind='lesson' if cid.startswith('lesson-') else {'course-map':'course-map','terminology':'terminology','teacher-guide':'teacher-guide','capstone':'capstone','course':'assembly','audit_report':'audit'}.get(cid,'supplement')
 deps=[]
 if kind=='lesson': deps=['course-map','sources']+([f'lesson-{int(cid[-2:])-1:02}'] if cid!='lesson-01' else [])
 if cid in ['teacher-guide','capstone','course']: deps=[f'lesson-{i:02}' for i in range(1,9)]
 checks.append({'id':cid,'kind':kind,'path':f,'dependencies':deps,'status':'drafted' if (P/f).exists() else 'pending','summary':f'Authored {cid}; pending completed review','sha256':digest(P/f) if (P/f).exists() else None})
js('manifest.json',{'schema_version':'1.0','topic':D['topic'],'audience':D['audience'],'assumptions':D['assumptions'],'ordered_deliverables':ordered,'checkpoints':checks,'dependencies':{c['id']:c['dependencies'] for c in checks},'course_order':[f'lesson-{i:02}' for i in range(1,9)],'assembly':{'path':'course.md','section_ids':[f'lesson-{i:02}' for i in range(1,9)]},'audit_counts':{'critical':0,'major':0,'minor':0},'blockers':[],'next_action':'Run independent review, numerical verification and deterministic validator'})
print('Eight lessons and supporting artifacts drafted; status remains incomplete pending audit.')
