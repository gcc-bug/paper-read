---
type: paper
title: "Vibe Calibration: Autonomous Bring-up of a 112-Qubit Superconducting Quantum Processor by a Skill-Orchestrating Language Agent"
authors: [Huikai Xu, Jiaxiu Han, Shigang Ou, Cheng Ye, Zisong Shen, Jing Gao, Yijia Wang, Tianrui Che, Yu Song, Weiyang Liu, Lei Wang, Lin-Feng Zhang, Pan Zhang, Hai-Feng Yu]
year: 2026
status: reading
tags: []
source: "source.pdf"
original_filename: "2606.22376.pdf"
provenance: "https://arxiv.org/abs/2606.22376 (arXiv v1 PDF, downloaded 2026-09-23)"
reading_dates: [2026-09-23]
---

# Vibe Calibration

## Source and reading coverage

[Original PDF](source.pdf), arXiv:2606.22376v1. On 2026-09-23, read the main text through the conclusion (PDF pages 1-8, printed pages 1-8) and selected supplemental sections II-VI (PDF pages 12-21, supplement printed pages 2-11). The references, full supplemental deployment details and NVIDIA comparison, and remaining supplemental material were not reviewed closely. Text was extracted locally; the workflow figures and numerical tables were checked against their extracted captions and surrounding text, but not visually audited.

Discussion completed and consolidated on 2026-09-23 at the reader's request. Follow-up reading checked supplemental section VII B and the summary (PDF pp. 22-23, supplement printed pp. 12-13), and the opening of Appendix A (PDF p. 24, supplement printed p. 14). The full execution transcript was not audited. Status remains `reading` to reflect this partial coverage. The discussion focused on what Skills contain, their design and evaluation, model dependence, physical limits to automation, comparison with rule-based control, and appropriate escalation to a human.

## Source claims

### Problem and motivation

The authors argue that bringing up a large superconducting processor requires interdependent measurements and judgments that fixed scripts handle poorly when signals are anomalous or parameters drift. Human experts can resolve these cases but become a bottleneck as device size grows (Introduction, PDF pp. 1-3).

### Main idea and mechanism

The system packages expert procedures as reusable, parameterized Skills with a decision tree, numerical acceptance gates, rollback paths, and audit records. Development has three stages: human-guided distillation on a single fixed-frequency qubit, supervised exception handling on a 16-qubit tunable device, and deployment on a 112-qubit device (Fig. 1; "Vibe Calibration," PDF pp. 2-4). Its qubit-characterization path runs readout S21, spectroscopy (with flux mapping for tunable devices), Rabi checks, readout optimization, T1, and Ramsey; failed gates retry, roll back, skip a qubit, or flag review (Fig. 2; Table I; supplement section IV, PDF pp. 3-5, 15-18).

The measurement routines are existing control scripts exposed as commands; the agent chooses and sequences them, while a configuration adapter handles device-specific state. The authors report write-back gates including R-squared > 0.9, at least 10 samples per Rabi/Ramsey period, and fit SNR >= 10 dB; they say the thresholds bound parameter error below 5% under an additive-Gaussian-noise model with 1024 shots ("Agent Skill Architecture," PDF pp. 4-5; supplement section IV, PDF pp. 15-18). Hardware-safe parallel groups come from backend topology, with each qubit's upstream calibration validity checked before later stages; the supplement says four groups of 28 on the 112-qubit sample (supplement section IV, PDF p. 16).

The deployed agent uses a Qwen3.6-35B-A3B model fine-tuned on 120 operator-validated action examples. A separate knowledge dataset has 8,796 short examples. Both derive from human-supervised trajectories; the datasets were used to train separate checkpoints, not combined in the reported deployment checkpoint ("Fine-Tuned Large Language Models," PDF p. 5; supplement sections II-III, PDF pp. 12-15).

Here, a Skill follows the familiar filesystem package of instructions, scripts, and resources loaded on demand. Its calibration content comprises the workflow, parameterized measurement commands, device configuration adapter, acceptance and recovery rules, and audit records. Supplemental Table IV specifies these five components; Table V lists accepted outputs and fallback actions (PDF p. 15, supplement printed p. 5). For example, an inconsistent time-Rabi check sends the workflow back to spectroscopy to reconsider the candidate transition.

### Reported results and evidence

- On the 112-qubit tunable-transmon device, the authors report a 4.7-hour agent run: 1.2 hours for transmission-line characterization and wiring verification, including manual cable reconnection; 3.1 hours for per-qubit work; 0.4 hours for coherence measurement and reporting. The 18-24 hour full-chip manual duration is an expert estimate, yielding the reported 4-5x speedup rather than a measured full-chip head-to-head timing comparison ("Experimental Results," PDF p. 7).
- Figure 3 reports valid T1 fits for 108/112 agent qubits versus 112/112 manual qubits, and valid Ramsey T2R fits for 102/112 versus 110/112. Median T1 is 96.2 versus 95.7 microseconds (agent versus manual); median T2R is 7.9 versus 14.4 microseconds. The authors attribute the lower agent T2R to measurement near, rather than precisely at, each flux sweet spot (Fig. 3 and discussion, PDF pp. 6-7).
- In a randomly selected 16-qubit subset, agent and expert results agreed within measurement uncertainty on 14/16 qubits; the two differences were readout amplitudes. The agent took 0.6 hours and the expert 3.8 hours, a measured 6.3x time ratio on this subset. The reported paired tests found no significant difference in T1 or T2R (PDF p. 7).
- Three runs on an eight-qubit subset, with power cycling between runs, had a reported mean parameter coefficient of variation of 1.8%. The transfer test on a different 16-qubit chip measured adherence to a new Skill: the 35B action-trained checkpoint had 5 fully adherent and 1 partially adherent sessions; other checkpoints did worse, including 0 fully adherent sessions for the 35B knowledge-trained model and both 4B models (PDF pp. 7-8; supplement section V, Table VII, PDF pp. 18-20).

### Scope and limitations

The demonstrated pipeline is primarily initial single-qubit characterization, readout, and coherence measurement. The authors name crosstalk compensation, refined one- and two-qubit gate calibration, spectator mitigation, and continuous drift tracking as future extensions (Discussion, PDF p. 8). The 112-qubit run involved manual cable reconnection, and some qubits failed upstream gates. The reported transfer test measures Skill adherence on one new 16-qubit chip, not comparable physical calibration quality across a broad set of devices (PDF pp. 7-8; supplement section V, PDF pp. 18-20).

Follow-up evidence, 2026-09-23: Appendix A says its transcript starts after flux arrangement was completed by automated scripts. It reports unresolved final Ramsey failures for Group 0 associated with readout/hardware conditions. Follow-up attempts exceeded the available Skill and the model's operational knowledge; the authors explicitly identify such cases as still requiring human diagnosis (PDF p. 24, supplement printed p. 14). This passage establishes a concrete limit to recovery, but does not by itself reconcile the transcript's group failures with every aggregate success count in Fig. 3.

Human escalation is part of the proposed workflow: Phase 2 requests expert help for previously unseen errors, and Skill construction specifies when execution must stop for human inspection (PDF p. 4; supplement section IV, PDF p. 15). Including an escalation path does not, by itself, measure how reliably the system recognizes unfamiliar situations that exceed its capabilities.

## My understanding

2026-09-23 — reader's words, retained verbatim:

> i basically aggree with the background.

> in usuallly, I think the agent skill is some reusable scripts and some md as promopt, also some config yaml

## My thoughts

2026-09-23 — reader's words, retained verbatim:

> in the real experiment, I think the bottle neck is the leak of auto tools. Or I think the problem is that it heavily rely on experts to redesgin something. Like find if any room hot or miscrowave leakage. Those process can't be auto at current stage. And heavily rely on the scope beyond the computation. Or I should say those hard to be auto run, auto fix.

Later in the same discussion, the reader suggested that the tool could say:

> ohm current stitution have beyond my ability, call the human

## Codex interpretation

The useful abstraction is an auditable experimental state machine: measurements propose parameter updates, numerical gates decide whether those updates are trusted, and rollback paths encode expert recovery. The language model's role is to navigate that structure and handle exceptions across a long run. This makes the paper's strongest evidence operational: a real 112-qubit characterization campaign completed in hours, with explicit per-qubit failure counts and a measured timing comparison on a 16-qubit subset.

The word "calibration" spans several depths. The results support autonomous execution of this initial characterization chain; they do not establish end-to-end, high-fidelity gate calibration or fault-tolerant operation. The full-chip speed comparison also has weaker evidence than the subset comparison because its manual baseline is estimated. I would treat the fit thresholds' claimed <5% parameter-error bound as model-dependent until checking the derivation and whether the noise assumptions hold for each measurement.

### Discussion synthesis — 2026-09-23

**Skill design.** The difficult work is specifying what evidence justifies each action: which causes can explain an anomaly, which available measurement distinguishes them, what makes an update trustworthy, and which downstream settings must be invalidated after an upstream change. A numerically good fit can still reflect the wrong physical interpretation. The file format itself does not solve these problems. The paper evaluates the assembled system; it does not establish a general metric of Skill quality.

**Model dependence and training.** Supplemental Table VII reports full/partial/non-adherence counts of 5/1/0 for the 35B action-trained model, 0/3/2 for the 35B knowledge-trained model, 0/0/1 for the 4B action-trained model, and 0/0/2 for the 4B knowledge-trained model. These are small tests of following a new Skill, not direct calibration-fidelity comparisons. Model architecture, capacity, training data, and training settings complicate causal attribution. Some trained models reverted to old procedures despite receiving new instructions. The comparisons examined do not establish that fine-tuning is necessary, or that a new base-model architecture is needed; an untuned version of the same model with identical tools and Skills would be a useful control.

**Physical limits.** The reader's examples motivate separating observation, diagnosis, and intervention. Temperature sensors or additional microwave measurements may be necessary to identify the cause; repairs may require physical access. Reasoning cannot supply missing observations or actuators. The unresolved hardware-related failure in Appendix A supports a limited claim of autonomy within the available procedures and tools.

**Comparison with rule-based automation.** Correction to the initial framing: a capable conventional controller can already implement branching, retries, fit thresholds, dependencies, and logs. Comparing the agent to a simple fixed sequence understates that baseline. The reported human timing comparison does not isolate the LLM's incremental benefit over equally equipped conventional automation.

> [!hypothesis]
> Suggested by Codex; not yet verified. Interpreting and combining procedures expressed in language may reduce the expert effort needed to introduce or maintain calibration workflows. The rationale is that an agent might execute some procedural changes without bespoke orchestration code. Test this against a conventional controller with the same measurement tools, physical checks, parallelism, and recovery knowledge, counting both initial development and later maintenance effort. The paper's runtime results alone do not establish this advantage.

**Human handoff as a useful outcome.** The reader's later comment changed the emphasis of Codex's assessment: inability to repair every physical failure does not eliminate the value of automation. A timely, informative request for human help can be a successful outcome. A useful handoff would state what was observed, what was tried, what remains uncertain, and which further diagnostic action is unavailable. This is a proposed evaluation target, not a demonstrated general ability of the paper's agent. An encoded stop rule offers protection; reliable recognition of unfamiliar limits needs separate evidence.

### Evaluation and possible future work suggested by Codex

The following are proposals arising from discussion, not established results or reader-endorsed conclusions:

| Evaluation target | Proposed measurement or comparison |
| --- | --- |
| Physical correctness | Independent validation of accepted calibration parameters and resulting performance |
| Recovery within the tool set | Correct diagnosis and resolution rates for specified faults |
| Recognition of limits | Unnecessary escalations, missed necessary escalations, and time spent on ineffective retries |
| Useful human handoff | Expert diagnosis time with and without the agent's evidence and attempted-action record |
| Total expert effort | Time to build, adapt, maintain, and operate the workflow, including difficult failures |
| Model contribution | Same model before and after fine-tuning, with identical Skills, tools, and tasks |
| Agent versus conventional automation | Matched tools, checks, batching, and recovery knowledge; compare outcomes and expert effort |

A proposed test would include both recoverable measurement problems and faults requiring an unavailable sensor or physical intervention. The desired outcome would depend on the case: valid recovery when possible, or appropriate escalation when necessary. This would test the boundary of autonomy more directly than successful execution under normal conditions alone.

## Open questions

- Codex, 2026-09-23: Which failure modes caused the four missing agent T1 fits and ten missing agent T2R fits, and how many required later human repair? The reported counts and audit records could answer this if per-qubit outcomes are available (Fig. 3; supplement section IV).
- Development, 2026-09-23: The opening of Appendix A identifies unresolved Group 0 Ramsey failures associated with readout/hardware conditions. This partially addresses the preceding question; the full mapping to Fig. 3 and subsequent human repair remains unverified.
- Codex, 2026-09-23: How much of the 16-qubit timing gain comes from batching and continuous operation versus agent decisions? A comparison with an equally parallel scripted baseline would help separate these effects ("Experimental Results," PDF p. 7).
- Codex, 2026-09-23: Would a matched sweet-spot policy close the T2R gap without materially increasing runtime? A same-operating-point comparison would test it (Fig. 3, PDF pp. 6-7).
- Reader questions, summarized by Codex on 2026-09-23: What makes a Skill good, how much does the base model affect it, and is retraining necessary? The package definition is clarified by supplemental section IV. General design metrics and the necessity of retraining remain open; the controls proposed above would help answer them.
- Reader question, summarized by Codex on 2026-09-23: What is the benefit over prior rule-based calibration? The incremental benefit remains unresolved without a matched automation baseline and accounting for expert development effort.
- Codex follow-up to the reader's handoff suggestion, 2026-09-23: Can the system reliably recognize when to call a human, and does its handoff reduce diagnosis time? Evaluate unfamiliar faults with expert judgments of when intervention is needed, including both excessive and missed escalation.

## Important locations

- PDF pp. 2-5: three-stage development, workflow tree, acceptance gates, and model training summary.
- PDF pp. 6-8: 112-qubit results, 16-qubit comparison, transfer test, and future scope.
- PDF pp. 12-15 (supplement printed pp. 2-5): dataset sizes and fine-tuning configuration.
- PDF pp. 15-20 (supplement printed pp. 5-10): Skill implementation, flux ridge algorithm, and transfer-session counts.
- PDF p. 24 (supplement printed p. 14), opening of Appendix A: transcript scope and unresolved readout/hardware-related Ramsey failure.
