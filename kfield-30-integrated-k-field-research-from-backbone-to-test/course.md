# Integrated K-Field Research: From Backbone to Test

<!-- BEGIN: lesson-01 -->
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
<!-- END: lesson-01 -->

<!-- BEGIN: lesson-02 -->
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
<!-- END: lesson-02 -->

<!-- BEGIN: lesson-03 -->
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
<!-- END: lesson-03 -->

<!-- BEGIN: lesson-04 -->
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
<!-- END: lesson-04 -->

<!-- BEGIN: lesson-05 -->
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
<!-- END: lesson-05 -->

<!-- BEGIN: lesson-06 -->
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
<!-- END: lesson-06 -->

<!-- BEGIN: lesson-07 -->
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
<!-- END: lesson-07 -->

<!-- BEGIN: lesson-08 -->
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
<!-- END: lesson-08 -->
