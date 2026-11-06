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
