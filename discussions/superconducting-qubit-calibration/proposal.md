# Adaptive multi-agent software for physical-device calibration

**Status:** research proposal under discussion. **Developed:** 2026-10-13. No implementation or device operation is requested at this stage.

## Reader-confirmed direction

The reader identified the [0918 analysis](slides/README.md) as preparation for a future project using LLMs to control and automatically calibrate physical devices, related to [Vibe Calibration](../../papers/vibe-calibration-112-qubit-processor/note.md). The reader's long-term vision is cooperation among agents backed by models with different costs and capabilities, balancing price and effectiveness. Proposed responsibilities include routine task classification, coding, and paper reading. The reader requested a formal proposal, research stages, support from prior work, and a software-engineering perspective.

The formulation and stages below are **Codex-proposed development of that direction**, not established results or confirmed personal claims. Superconducting-qubit calibration supplies the initial motivating setting; broader device coverage remains a future question.

## Proposal statement

Physical-device calibration combines repeatable measurement procedures with decisions about incomplete, noisy, and sometimes ambiguous evidence. Executing a procedure successfully does not establish that its returned parameter is valid. A system must track which observations support an update, which upstream settings remain valid, and whether the next step requires another measurement, more capable reasoning, or human expertise. Using a powerful model for every task can increase inference expenditure; indiscriminately replacing it with cheaper models can introduce incorrect decisions and additional experimental work.

We propose to investigate an adaptive multi-agent software architecture that coordinates measurement tools, models of different capabilities, and human expertise. Agents specialize in routine execution, diagnosis, literature interpretation, and procedure development, while an authoritative runtime maintains experimental state and controls parameter updates. A scheduling policy selects the agent, model, and next action using task context, evidence quality, action consequences, and remaining budget. The research goal is to characterize when this architecture can reduce total calibration cost while preserving independently assessed calibration quality, and which software contracts make the cooperation reliable and maintainable.

The intended contribution has two coupled parts: **adaptive allocation of heterogeneous agents** and **software architecture for consistent, traceable calibration decisions**. Improvements remain hypotheses to test. Multi-agent cooperation is the destination; a single-agent system is a comparison point and a way to isolate architectural effects.

## Research questions

1. **Evidence and actions:** What representation lets agents distinguish a completed measurement, a fitted parameter, an accepted calibration update, and an unresolved hypothesis? How does that distinction determine the next permissible action?
2. **Cost and effectiveness:** Which decisions can use inexpensive models or deterministic tools, and when should the system invoke a more capable model, collect another observation, or request an expert?
3. **Cooperation:** When does specialization, selective parallel work, or an additional review agent improve decisions enough to justify communication and repeated reasoning?
4. **Software evolution:** How can measurement tools, estimator versions, procedures, models, and devices change without silently changing the meaning or validity of accepted results?

These questions concern the complete calibration workflow, not just the quality of individual generated answers.

## Why 0918 is relevant

The existing corpus exposes distinctions that an agent must preserve:

| Local observation | Software/decision requirement | Evidence boundary |
| --- | --- | --- |
| [Rabi/007](slides/case-notes.md#case-rabi-007) has recorded R² = 0.959 but about 0.22 cycles of coverage | Represent parameter identifiability and acquisition coverage separately from fit score | Does not establish the correct replacement sweep or its outcome |
| [T1/004](slides/case-notes.md#case-t1-004) is almost flat and reaches the imposed fit bound | Distinguish an optimizer's returned number from a lifetime constrained by the observations | Does not identify the physical cause of the flat trace |
| [Spectroscopy/005](slides/case-notes.md#case-spectroscopy-005) has scan steps too coarse to resolve the candidate linewidth | Consider whether more informative measurements are needed | Existing records do not show the result of a finer scan |
| The [original readout estimator](../../questions/0918-readout-estimator-provenance.md) is unresolved | Retain estimator definitions, versions, labels, and preprocessing with reported metrics | A new classifier cannot recover the original metric's semantics |

The corpus motivates evidence requirements and retrospective decision tasks. Review flags are not verified labels of hardware faults, and suggested causes are not ground truth. Interactive recovery and calibration effectiveness would require additional evidence beyond these stored records.

## Proposed mechanism

### Separate roles from model assignments

An agent role specifies its responsibility, available tools, expected outputs, and authority. A model assignment specifies which model currently performs its reasoning. The same role may use different models as its task changes; several roles may share a model. More agents do not necessarily require more model families.

| Role | Responsibility | Proposed cost/capability policy |
| --- | --- | --- |
| Coordinator | Decompose goals, track progress, select workers and resolve dependencies | Simple scheduling where possible; stronger reasoning for substantial replanning |
| Routine worker | Check records, invoke established procedures, summarize structured results | Deterministic tools or an inexpensive model for well-defined cases |
| Diagnostic specialist | Compare plausible explanations and propose discriminating measurements | Stronger model when evidence is ambiguous or consequences are substantial |
| Literature specialist | Interpret a procedure or physical model from attributed sources | Invoked when a concrete knowledge gap affects a decision |
| Procedure developer | Adapt interfaces or create measurement/analysis code | Coding-capable model; proposed changes must enter the checked tool library |
| Validation role | Check whether a proposed update meets the applicable evidence and state requirements | Numerical/software checks first; selective model-assisted review for unresolved interpretation |
| Human expert | Supply missing expertise, observations, or physical intervention | Escalation accompanied by evidence, attempted actions, and the missing capability |

These are logical responsibilities, not a mandatory seven-agent team. Workers are activated as needed. A second model's agreement is not independent physical validation, especially when agents share inputs, assumptions, or model errors.

### Route actions using the experimental state

The scheduler should consider the current data, unresolved questions, calibration dependencies, available tools, model capabilities, and the consequences of an incorrect action. It chooses among ordinary execution, stronger reasoning, further measurement, selective collaboration, or expert intervention. Self-reported LLM confidence alone is insufficient to authorize an update.

For example, a routine worker may detect insufficient Rabi coverage. A known sweep-adjustment procedure may suffice. If the procedure is ambiguous, a diagnostic specialist can assess alternatives. If the alternatives predict indistinguishable existing observations, another measurement is needed. If no available measurement can resolve them, the system should state the missing capability and request an expert. This is a proposed decision structure, not a verified recovery for the recorded case.

The long-term research question is whether the scheduler can select the least costly adequate combination of these actions. A cheap router must retain an uncertainty/escalation path so an early classification cannot permanently hide difficult cases.

### Define cost and effectiveness at workflow level

A candidate objective is to minimize expected total operating cost subject to task-specific calibration-quality and invalid-update constraints. An accounting expression is:

\[
C_{\mathrm{total}}=C_{\mathrm{models}}+C_{\mathrm{measurement}}+C_{\mathrm{coordination}}+C_{\mathrm{expert}}+C_{\mathrm{rework}}.
\]

The categories must be disjoint in any actual accounting: coordination includes message handling and scheduling overhead not already charged as model calls; rework includes additional costs not already counted as measurements or expert time. Monetary cost, elapsed time, and expert effort should also be reported separately. Hardware time can dominate inference expenditure, so token savings need not imply cheaper calibration.

Effectiveness means independently assessed validity or performance of the intended calibration, appropriate recovery/escalation, and the ability to maintain valid state. Fit R², instruction adherence, and model agreement are intermediate diagnostics. Requirements and trade-off weights must follow the particular calibration goal rather than universal thresholds.

> [!hypothesis]
> Suggested by Codex; not yet verified. Heterogeneous agents may reduce total cost if inexpensive workers handle repeatable decisions and escalation concentrates capable reasoning on consequential ambiguities. Communication overhead, correlated errors, misrouting, and repeated measurements may erase that advantage. The useful result is the condition under which the trade-off holds, not a presumption that more agents are better.

## Software-engineering contribution

The software perspective is central because calibration results depend on stateful interactions and changing procedures. Proposed contracts include:

| Contract | What it records or enforces | Research significance |
| --- | --- | --- |
| Measurement/analysis interface | Typed arguments, units, preconditions, acquisition context, result IDs, estimator identity, diagnostics and side effects | Supports interchangeable tools without silently changing result meaning |
| Authoritative calibration state | Proposed/accepted/stale/failed status, operating point, parameter version and dependencies | Prevents a worker from treating an outdated upstream calibration as valid |
| Update protocol | Workers propose changes; one runtime checks versions and validation evidence before committing them | Makes conflicting concurrent proposals detectable; checks alone do not guarantee physical validity |
| Resource scheduling | Instrument ownership, compatible measurement groups, shared channels and reservations | Distinguishes parallel reasoning from physically compatible parallel measurements |
| Recovery semantics | Retry identity, bounded retries, configuration restore, downstream invalidation and expert handoff | Avoids interpreting a retry as a duplicate-free measurement or a software rollback as reversal of physical history |
| Trace and replay | Raw records, code/configuration versions, model and prompt identity, decisions, sources and update history | Supports diagnosis and regression checks; replaying recorded outputs does not reproduce unobserved hardware responses |
| Procedure evolution | Versioned skills and generated code, tests, review and release criteria | Allows capability expansion while preserving the meaning of existing workflows |

A concrete dependency example: after changing the spectroscopy-derived drive frequency, a Rabi result obtained at the previous frequency may need invalidation. A downstream agent must observe that state transition before using the old amplitude. The required invalidation depends on the device and procedure and must be specified, not assumed for every parameter change.

Existing calibration graphs and agent frameworks provide many of these ingredients. Potential software-engineering research lies in specifying their interaction, examining failure propagation and change impact, and identifying which contracts improve consistency and reduce expert maintenance effort. Creating a framework or adding a log is not itself a novelty claim.

## Research stages

The stages below organize a proposal. They are not requests to build a prototype now, promised results, or calendar commitments.

| Stage | Research focus | Intended intellectual output | What it enables |
| --- | --- | --- | --- |
| 1. Calibration semantics and task boundaries | Define evidence, accepted updates, dependencies, uncertainty and the intended quality criteria; use 0918 to illustrate the distinctions | Problem formulation and software contracts | Gives every later agent a common interpretation of its task |
| 2. An auditable agent workflow | Study a single capable agent and established automation using the same tool contracts and calibration goals | Reference architecture and account of decisions that benefit from language reasoning | Separates tool quality and workflow structure from multi-agent effects |
| 3. Heterogeneous agent cooperation | Decompose responsibilities and assign inexpensive/capable models; specify shared state and handoffs | Collaboration architecture and analysis of its useful and harmful interactions | Establishes the reader's intended multi-agent setting |
| 4. Adaptive allocation | Select models, collaborations, additional measurements and expert intervention according to evidence and action consequences | Scheduling formulation and policy; cost/effectiveness characterization | Moves from fixed role assignments to adaptive cooperation |
| 5. Long-term evolution | Consider procedure/model changes, device adaptation, drift, regressions and expert maintenance | Evidence about maintainability, transfer and continued calibration validity | Connects one calibration campaign to sustained device operation |

Stage 1 and Stage 2 can remain preparatory work rather than separate publication claims. The strongest candidate paper contribution is the connection between Stages 3–4 and the state/validation contracts. Stage 5 is a longer-term extension, not a requirement for the first proposal. These stages may overlap as the research develops.

## Prior work: support and boundaries

Consulted on **2026-10-13**. This is a targeted positioning lookup, not an exhaustive novelty review. Source-supported mechanisms below are separated from their proposed transfer to calibration.

| Source and inspected coverage | What supports the proposal | What it does not establish |
| --- | --- | --- |
| **Vibe Calibration** (2026), [arXiv:2606.22376v1](https://arxiv.org/abs/2606.22376), [existing local note/PDF](../../papers/vibe-calibration-112-qubit-processor/note.md). Rechecked PDF pp. 3–5, 8, 15–16 and opening of p. 24 | Agent orchestration of real qubit characterization; reusable procedures, acceptance gates, rollback and device adapters. Establishes close overlap with the application | The inspected passages do not establish an adaptive cost/quality policy for a heterogeneous agent team. The transcript opening also records unresolved hardware-related failures |
| **FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance** (2023 preprint), [arXiv:2305.05176v1 HTML](https://arxiv.org/html/2305.05176v1), Sections 2–4 | A response scorer and cascade choose when to use another model under a budget. Supports model allocation as an optimization problem | Query-answer quality is not physical calibration validity; reported savings cannot be transferred to device operation |
| **RouteLLM: Learning to Route LLMs with Preference Data** (2024 preprint), [arXiv:2406.18665v1](https://arxiv.org/html/2406.18665v1), Sections 2–3; earlier lookup in this discussion | Learned routing between stronger and weaker models. Supports task-dependent model selection | Preference-based response selection does not by itself handle sequential experiment dependencies or the cost of incorrect physical actions |
| **AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation** (2023, inspected arXiv v2), [arXiv:2308.08155v2](https://arxiv.org/html/2308.08155v2), Sections 2 and 4 | Customizable agents combining models, tools and humans; programmable collaboration patterns. Supports role/interface separation | A generic conversation framework does not establish calibration correctness or economic benefits from a particular team |
| **Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks** (2024 preprint), [arXiv:2411.04468v1](https://arxiv.org/html/2411.04468v1), Sections 4–5.1 | An orchestrator tracks task/progress ledgers and directs specialized workers. One configuration uses o1-preview for the outer orchestration loop and coding while other agents use GPT-4o | Different models for different roles already exist. Its digital task setting does not establish the proposed experimental allocation policy |
| **Autonomous chemical research with large language models / Coscientist** (Nature 624, 570–578, 2023), [DOI:10.1038/s41586-023-06792-0](https://www.nature.com/articles/s41586-023-06792-0), abstract, system description and cross-coupling execution passage | A planner integrates literature/documentation lookup, calculations and experimental APIs. Supports separation of knowledge acquisition, coding/calculation and execution | Chemical experimentation is a different task, and the inspected setup includes manual plate movement. It does not establish universal autonomous device repair |
| **AutoLabs: cognitive multi-agent systems with self-correction for autonomous chemical experimentation** (Scientific Reports 16, article 19554, 2026), [DOI:10.1038/s41598-026-45593-z](https://www.nature.com/articles/s41598-026-45593-z), abstract, model/architecture description, “The accuracy-cost relationship,” and execution-validation passage | Close support and overlap: specialized laboratory agents, model/reasoning configurations, self-correction and cost/correctness analysis. The source reports five procedures checked in simulation mode and physical execution of experiments 1–2 | Its procedure-generation/correctness findings do not directly establish sequential qubit-calibration quality or adaptive allocation from calibration evidence |
| **QUAlibrate**, [official documentation](https://qualibrate-docs.quantum-machines.co/), Overview: Key Features and Core Components; live documentation consulted on the date above | Reusable calibration nodes, adaptive graphs, looping/failure handling, nested workflows and a device representation. Provides a strong conventional software reference | Adaptive graphs and device state are existing capabilities. Documentation alone supplies no matched comparison against the proposed agents |

The public HTML/pages were selectively inspected; no new full-paper reading record was created. The existing Vibe Calibration source is reused. QUAlibrate is a software/documentation source rather than a research-result comparison. No publication venue is inferred for sources listed as preprints.

## Candidate contribution and evidence direction

The candidate central claim is:

> Evidence and dependency information can guide heterogeneous agent cooperation so that the system spends model effort and measurement effort where they affect valid calibration outcomes, while explicit software contracts preserve consistent state across those decisions.

> [!hypothesis]
> Suggested by Codex; not yet verified. Coupling allocation to calibration state and action consequences may outperform a fixed cheap/strong role assignment at a matched calibration-quality requirement. The novelty and benefit of that coupling remain to be established against calibration automation, laboratory agents, model routers and sequential decision methods.

Future evidence should distinguish this mechanism from equally equipped conventional calibration automation, one capable agent, a fixed heterogeneous team, and a generic task router. Tools, available observations, recovery knowledge and device-resource constraints must be matched. Compare total cost, valid calibration outcomes, invalid accepted updates, unnecessary/missed escalation, and maintenance effort; do not substitute token savings or task-completion counts for physical effectiveness. This is an evidence direction, not an experimental protocol or reported result.

A software-focused fallback is to study calibration-state consistency and workflow evolution across models and procedures, even if adaptive allocation gives little savings. A finding that a simpler controller or single agent is preferable under specified conditions would remain informative.

## Open proposal decisions

- Which calibration goal defines effectiveness: initial characterization, readout calibration, gate calibration, or sustained drift management?
- Is the first central contribution adaptive allocation, or the software contracts that make changing agent teams and procedures reliable? Both can belong in one architecture, but one should lead the research claim.
- Which costs matter to the intended laboratory, and over what operating horizon are development and maintenance effort accounted for?
- What evidence identifies an adequate cheap-model decision without relying on the same model's self-assessment?
- Which recent laboratory-agent and sequential-routing methods already implement parts of the proposed coupling? The lookup above identifies substantial ingredients and overlap; it does not establish a complete novelty boundary.

## Dated development

2026-10-13 — Formalized the reader's proposal direction and multi-agent cost/effectiveness vision. Added proposed research stages, software contracts, and selective prior-work positioning. No control code, slides, measurements, calibration parameters or original source files were changed as part of this proposal task.
