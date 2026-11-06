# Lesson 7 — Phase cost and physical coupling

**Essential question:** What extra information connects a modeled cost to measured response?

**Goals:** Demonstrate equal-output ambiguity; use an independent calibration without silently refitting; propose an observation that distinguishes candidate mechanisms while preserving residuals.

**Bridge:** A route optimum follows from an objective and constraints. An apparatus response requires another relation. We can study that logical gap with multiplication, without assuming a particular physical mechanism.

One 55-minute session: 5 retrieval, 20 teaching/example, 15 practice and 15 diagnostics/repair.

## C27.07-E1 — A model needs a typed transfer

Use y for a detector reading in detector units D. Suppose a proposed transfer model is y=k r, with a dimensionless response-driving input r and sensitivity k in D. This is a declared synthetic model, not a measured law. Knowing a separate cost label q does not establish r=q. That bridge would require a definition or an independently supported coupling model with compatible units.

**Nonidentifiability** means different allowed parameter choices produce the same observations. If only a product is observed, its factors may be nonidentifiable. To distinguish candidates, observe a factor independently, or change a controlled input and compare each candidate's stated prediction. Record timestamps, orientation, exposure, source state and detector calibration alongside the result; otherwise changes in these coordinates could be confused with changes in coupling.

Separate the evidence layers. An instrument reading is an observation. Computing a predicted response and its difference from that reading is a derived transform. Inferring a shared response law across conditions is an interpretation. Proposing a transfer mechanism is a mechanism hypothesis. Algebra and dimensional bookkeeping are mathematical reference tools, not observations of the mechanism. Missing inputs and residual structure are unresolved information to investigate next.

## C27.07-W1 — Same output, different factors

For the synthetic observation y=6D, (k,r)=(2D,3) predicts 2D·3=6D, while (1D,6) predicts 1D·6=6D. Both satisfy the one equation. If only y and a cost label q are supplied, neither factorization has been selected. Preserve both candidates. A measurement of r by an independent calibrated procedure could distinguish them; simply choosing r to make the model match would not do so.

T35 makes an analogous source distinction: an input-referred equivalent LED-energy interval is a model input, not measured transferred energy or a detected photon count. The overview describes fourteen rows sharing only three distinct plane-family cost levels. Distinct values do not establish statistical independence. Preserve the signed rows and their family identities by immutable reference; do not count fourteen distinct cost settings or discard negative events. The two works' PDF, JSON and abstract representations are two evidence bundles, not six independent studies. Their observations retain the source status reported_exploratory_to_be_verified [sources.md, T35].

## C27.07-P1 — Practice and worked answers

An independent calibration now supplies r=3, and the first reading remains y=6D. Determine k under the proposed model. Freeze that k. A second reading is 7D with the same declared r. Find prediction, residual and reconstruction, then propose one additional check.

**Answer:** k=y/r=6D/3=2D. The frozen model predicts 6D again. Retain residual e=y−prediction=7D−6D=+1D, so 7D=6D+1D. Save both readings in time order, r, k and the positive sign. Check the independently measured r, orientation and exposure on the second acquisition; alternatively, hold them fixed and collect a new response under a predeclared changed input. If r is confirmed unchanged, the residual identifies unresolved response structure or a limitation of the fixed transfer. Silently changing k to 7D/3 for that row would conceal what the fixed model failed to represent.

> **Claim scope:** The numbers 6 and 7 are synthetic teaching observations. This course identifies a class of sufficient additional evidence, not a completed physical coupling. Modeled path cost, route optimum, scalar phase and transferred energy remain distinct. The source's missing radiometric calibration and exposure-transfer witness must be supplied to connect its equivalent input to apparatus energy.

## C27.07-D1 — Diagnostic checks

1. Does y=6D alone select k=2D?
2. What signed residual is produced by a new reading 5D under the same frozen prediction 6D?
3. Which records would help evaluate a proposed coupling?
4. Can an exact synthetic route certificate fill in a missing apparatus transfer law?

**Answers:** (1) No; r=3 must be independently fixed or otherwise constrained. (2) −1D, with 5D=6D+(−1D); keep it. (3) Raw responses with signs and times, source state, orientation, exposure, calibration, a declared transfer equation and its units, matched controls/reference ledger and retained per-reading residuals. A predeclared replay can test predictions across conditions. (4) No; it proves a minimum under a mathematical specification and provides no such transfer observation.

**Next dependency:** [Capstone](capstone.md) combines the finite route proof, source-certificate audit and retained coupling residual.
