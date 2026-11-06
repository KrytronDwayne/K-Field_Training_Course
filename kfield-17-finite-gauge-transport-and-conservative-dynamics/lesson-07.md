# Lesson 07 — Reading a fixed-rung certificate

Essential question: What must accompany a numerical bound before we can replay its calculation?

Goals: transcribe bounds with their inequality signs and units; identify supplied and missing certificate inputs; evaluate a separately declared synthetic bound without merging evidence classes.

Prerequisite bridge: lesson 06 showed that numbers depend on conventions and normalization. A certificate similarly depends on its finite model, coefficients and method. Two 55-minute periods: A source card and units, B missing-input analysis and synthetic arithmetic. Each period uses 5 retrieval, 20 teaching, 15 practice and 15 diagnostic/repair minutes.

## C17.07-E1 — The scope of a certificate

A finite compiler here means an explicit procedure assembling the finite model's matrices and coefficients. A rung is a fixed level of its hierarchy. A certificate is a calculation record supporting a stated result for specified inputs. The result and its scope belong together: changing coefficients or rung means a different calculation. A hash is a file fingerprint used to check which exact bytes were read; it does not prove the file's claims.

An interval bound encloses a quantity instead of replacing it by a rounded guess. The statement ε<0.007744166 is an upper bound with a strict inequality, not an equality or a measured uncertainty distribution. A non-strict ≤ allows equality. A gap is a separation between spectral levels of the specified model; this is a recognition definition, not an assignment to compute an untaught spectrum. A contraction factor α bounds a shrinkage in the certificate's specified comparison; its reported value does not supply the missing comparison norm or matrices.

S02 M13 names site-indexed compact-group links and positive native plaquette/detail coefficients as domain hypotheses. For our reading purposes a compact group is a bounded, closed collection of allowed invertible frame maps with composition and inverses; the scalar unit-modulus phases are a familiar example. The exact source group's carrier and compiler still must be specified to replay its certificate. Positive coefficients mean strictly greater than zero. Its detail coefficient lower bound c_*>0 must also be retained. A theorem for one pinned finite compiler does not automatically range over every model bearing the same module label.

Use this certificate card: exact source path/hash and pointer; rung and compiler identifier; spaces and basis conventions; complete matrix inputs; positive coefficients and their units; enclosure method and precision; bound with inequality; replay command and object availability. If a field is missing, say unavailable. Do not fill it with our teaching matrix.

## C17.07-W1 — Read the archived card

At S02 /backbone_sequence/12/proof, the source reports:

| Quantity | Source-reported bound | Reading |
|---|---|---|
| ε_E | <0.007744166 | strict dimensionless enclosure bound |
| ε_B | <0.015868134 | strict dimensionless enclosure bound |
| α | ≤0.5244 | non-strict contraction bound |
| Δ | >0.10185916 H_N/τ_R | strict finite-rung energy-gap bound |

H_N denotes an action scale and τ_R a positive time scale in this reading, so E0=H_N/τ_R has energy units. Action is energy multiplied by time; division by time recovers energy. The coefficient 0.10185916 is dimensionless. Retain all displayed digits as reported bounds, not a claim that the underlying method used exactly that many digits of working precision.

What can we verify now? We can verify the source bytes, pointer, inequality transcription and units. The full fixed-rung matrices, native coefficient list, interval method, numerical precision settings and executable certificate reference are not supplied in this read packet. S03 /findings/8, AUD-009, explicitly lists fixed-rung interval certificate inputs among missing replay objects. Thus this is a source-scoped reading, not a fresh replay. Its source-local VERIFIED_NOT_LOADED handling preserves the claim and the retrieval gap together.

## C17.07-P1 — Separate reading from a toy calculation

First, classify a packet containing only the four bounds above. Name at least four missing fields. Then evaluate this independent, synthetic rule: d_root=3/10 and c_*=1/20 are dimensionless positive inputs; define b=min(d_root,2c_*). The symbol min selects the smaller of its two arguments. Report bE0. For an optional unit check take H_N=2 AU and τ_R=4 TU, with EU=AU/TU.

Worked answer: the packet is a source summary; the exact compiler/rung, full matrices, positive coefficient list, interval method/working precision, and pinned replay object/command are absent. Replay is unavailable. In the synthetic rule, 2c_*=2/20=1/10, which is less than 3/10, so b=1/10 and bE0=E0/10. For the optional units, E0=(2/4) EU=1/2 EU, so bE0=1/20 EU. This arithmetic does not reproduce the archived 0.10185916 bound. Here d_root is explicitly normalized; if a root gap is instead given in energy units, divide it by E0 before placing it in this dimensionless minimum.

> Claim scope: The four archival numbers are source-reported facts about what S02 states. Hash checking does not verify their proof. Our min calculation is a fresh synthetic finite calculation. Neither one supplies an infinite-depth operator-domain theorem or a conventional continuum comparison. M13 here is the mathematical-backbone module; an integration compiler's similarly numbered M13 is not interchangeable with it.

## Diagnostic checks

1. **C17.07-D1:** What does VERIFIED_NOT_LOADED permit us to report? What positivity condition remains essential?
2. Is α=0.5244 an exact transcription of the source claim?
3. Would changing c_* to zero preserve a strictly positive synthetic lower bound?
4. Can the four displayed bounds determine the original compiler matrices or working precision?

Answers: (1) A source-reported status and unresolved retrieval requirement, not a fresh verification or an automatic refutation. Retain positive native coefficients and c_*>0. (2) No: use α≤0.5244. (3) No: min(3/10,0)=0, and the stipulated positivity hypothesis fails. (4) No. The full replay inputs and numerical method are separate records; displayed decimal places are not sufficient.

Next dependency: [lesson 08](lesson-08.md) separates what finite conservation proves from what an infinite limit would require.
