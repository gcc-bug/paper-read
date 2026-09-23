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

## Source claims

### Problem and motivation

The authors argue that bringing up a large superconducting processor requires interdependent measurements and judgments that fixed scripts handle poorly when signals are anomalous or parameters drift. Human experts can resolve these cases but become a bottleneck as device size grows (Introduction, PDF pp. 1-3).

### Main idea and mechanism

The system packages expert procedures as reusable, parameterized Skills with a decision tree, numerical acceptance gates, rollback paths, and audit records. Development has three stages: human-guided distillation on a single fixed-frequency qubit, supervised exception handling on a 16-qubit tunable device, and deployment on a 112-qubit device (Fig. 1; "Vibe Calibration," PDF pp. 2-4). Its qubit-characterization path runs readout S21, spectroscopy (with flux mapping for tunable devices), Rabi checks, readout optimization, T1, and Ramsey; failed gates retry, roll back, skip a qubit, or flag review (Fig. 2; Table I; supplement section IV, PDF pp. 3-5, 15-18).

The measurement routines are existing control scripts exposed as commands; the agent chooses and sequences them, while a configuration adapter handles device-specific state. The authors report write-back gates including R-squared > 0.9, at least 10 samples per Rabi/Ramsey period, and fit SNR >= 10 dB; they say the thresholds bound parameter error below 5% under an additive-Gaussian-noise model with 1024 shots ("Agent Skill Architecture," PDF pp. 4-5; supplement section IV, PDF pp. 15-18). Hardware-safe parallel groups come from backend topology, with each qubit's upstream calibration validity checked before later stages; the supplement says four groups of 28 on the 112-qubit sample (supplement section IV, PDF p. 16).

The deployed agent uses a Qwen3.6-35B-A3B model fine-tuned on 120 operator-validated action examples. A separate knowledge dataset has 8,796 short examples. Both derive from human-supervised trajectories; the datasets were used to train separate checkpoints, not combined in the reported deployment checkpoint ("Fine-Tuned Large Language Models," PDF p. 5; supplement sections II-III, PDF pp. 12-15).

### Reported results and evidence

- On the 112-qubit tunable-transmon device, the authors report a 4.7-hour agent run: 1.2 hours for transmission-line characterization and wiring verification, including manual cable reconnection; 3.1 hours for per-qubit work; 0.4 hours for coherence measurement and reporting. The 18-24 hour full-chip manual duration is an expert estimate, yielding the reported 4-5x speedup rather than a measured full-chip head-to-head timing comparison ("Experimental Results," PDF p. 7).
- Figure 3 reports valid T1 fits for 108/112 agent qubits versus 112/112 manual qubits, and valid Ramsey T2R fits for 102/112 versus 110/112. Median T1 is 96.2 versus 95.7 microseconds (agent versus manual); median T2R is 7.9 versus 14.4 microseconds. The authors attribute the lower agent T2R to measurement near, rather than precisely at, each flux sweet spot (Fig. 3 and discussion, PDF pp. 6-7).
- In a randomly selected 16-qubit subset, agent and expert results agreed within measurement uncertainty on 14/16 qubits; the two differences were readout amplitudes. The agent took 0.6 hours and the expert 3.8 hours, a measured 6.3x time ratio on this subset. The reported paired tests found no significant difference in T1 or T2R (PDF p. 7).
- Three runs on an eight-qubit subset, with power cycling between runs, had a reported mean parameter coefficient of variation of 1.8%. The transfer test on a different 16-qubit chip measured adherence to a new Skill: the 35B action-trained checkpoint had 5 fully adherent and 1 partially adherent sessions; other checkpoints did worse, including 0 fully adherent sessions for the 35B knowledge-trained model and both 4B models (PDF pp. 7-8; supplement section V, Table VII, PDF pp. 18-20).

### Scope and limitations

The demonstrated pipeline is primarily initial single-qubit characterization, readout, and coherence measurement. The authors name crosstalk compensation, refined one- and two-qubit gate calibration, spectator mitigation, and continuous drift tracking as future extensions (Discussion, PDF p. 8). The 112-qubit run involved manual cable reconnection, and some qubits failed upstream gates. The reported transfer test measures Skill adherence on one new 16-qubit chip, not comparable physical calibration quality across a broad set of devices (PDF pp. 7-8; supplement section V, PDF pp. 18-20).

## Codex interpretation

The useful abstraction is an auditable experimental state machine: measurements propose parameter updates, numerical gates decide whether those updates are trusted, and rollback paths encode expert recovery. The language model's role is to navigate that structure and handle exceptions across a long run. This makes the paper's strongest evidence operational: a real 112-qubit characterization campaign completed in hours, with explicit per-qubit failure counts and a measured timing comparison on a 16-qubit subset.

The word "calibration" spans several depths. The results support autonomous execution of this initial characterization chain; they do not establish end-to-end, high-fidelity gate calibration or fault-tolerant operation. The full-chip speed comparison also has weaker evidence than the subset comparison because its manual baseline is estimated. I would treat the fit thresholds' claimed <5% parameter-error bound as model-dependent until checking the derivation and whether the noise assumptions hold for each measurement.

## Open questions

- Codex, 2026-09-23: Which failure modes caused the four missing agent T1 fits and ten missing agent T2R fits, and how many required later human repair? The reported counts and audit records could answer this if per-qubit outcomes are available (Fig. 3; supplement section IV).
- Codex, 2026-09-23: How much of the 16-qubit timing gain comes from batching and continuous operation versus agent decisions? A comparison with an equally parallel scripted baseline would help separate these effects ("Experimental Results," PDF p. 7).
- Codex, 2026-09-23: Would a matched sweet-spot policy close the T2R gap without materially increasing runtime? A same-operating-point comparison would test it (Fig. 3, PDF pp. 6-7).

## Important locations

- PDF pp. 2-5: three-stage development, workflow tree, acceptance gates, and model training summary.
- PDF pp. 6-8: 112-qubit results, 16-qubit comparison, transfer test, and future scope.
- PDF pp. 12-15 (supplement printed pp. 2-5): dataset sizes and fine-tuning configuration.
- PDF pp. 15-20 (supplement printed pp. 5-10): Skill implementation, flux ridge algorithm, and transfer-session counts.
