# Superconducting-qubit calibration: reading map

Notes consolidated on 2026-09-29 from the reader's 0918-data discussion. Explanations are Codex interpretations; they are not assertions that the reader has adopted them. The experiment corpus remains in the sibling `agent_control` checkout. No new experiment or calibration acceptance is claimed.

## Start here

1. [Calibration quantities and physical meaning](../concepts/superconducting-qubit-calibration.md): six experiments, raw columns, excitation, π pulses, peaks versus valleys, T1 versus Ramsey, and numerical rules.
2. [IQ readout and the four-panel figure](../concepts/iq-readout-and-assignment.md): every axis and reported metric in case 001, preparation versus assignment, histogram counts, threshold selection, and fidelity conventions.
3. [Unresolved readout provenance](../questions/0918-readout-estimator-provenance.md): what the original plotting/analysis code must establish.
4. [Hardware, microwave signals, and calibration progression](../concepts/superconducting-qubit-hardware-and-signals.md): device roles, energy levels, drive controls, dispersive readout, anticipating peak/dip polarity, and the iterative sequence.

## Reading order and references

| Priority | Reference | Read for this discussion |
| --- | --- | --- |
| First | P. Krantz et al., *A Quantum Engineer's Guide to Superconducting Qubits*, Applied Physics Reviews **6**, 021318 (2019), [DOI](https://doi.org/10.1063/1.5089550), [local note and PDF](../papers/quantum-engineers-guide-superconducting-qubits/note.md) | Figs. 4–5 for relaxation/coherence; Sec. IV.D.1 for rotations; Sec. V.B–C and Figs. 22–23 for IQ and distribution separation. Local source is arXiv v5 (2021 revision), not the publisher PDF. |
| Then | A. Blais et al., *Circuit Quantum Electrodynamics*, Reviews of Modern Physics **93**, 025005 (2021), [DOI](https://doi.org/10.1103/RevModPhys.93.025005), [local note and PDF](../papers/circuit-quantum-electrodynamics/note.md) | Sec. V.C.1–2, Fig. 19, Eqs. (115)–(116): state-dependent resonator response, SNR, and fidelity conventions. Local source is arXiv v1 (2020), not the publisher PDF. |
| Practical | Qiskit Experiments, [T1 Characterization](https://qiskit-community.github.io/qiskit-experiments/manuals/characterization/t1.html) | Background: repeat prepare–wait–measure and fit $A e^{-t/T_1}+B$. |
| Practical | Qiskit Experiments, [T2* Ramsey Characterization](https://qiskit-community.github.io/qiskit-experiments/manuals/characterization/t2ramsey.html) | Circuit sequence, damped oscillation, intentional oscillation frequency versus detuning. |
| Practical | Qiskit Experiments, [Readout Mitigation](https://qiskit-community.github.io/qiskit-experiments/manuals/measurement/readout_mitigation.html) | Opening definition of the assignment matrix and “Standard mitigation experiment.” |

The three documentation pages were inspected on 2026-09-29 and displayed Qiskit Experiments 0.14.2. They are live references, not locally executed examples. The Ramsey introduction has a misleading sentence referring to initialization in |1⟩; the listed SX–delay–RZ–SX circuit and Krantz Fig. 5 establish superposition preparation during the free-evolution interval. Use the circuit, not that isolated sentence.

The two papers received targeted partial reading, not full reviews. Their notes record exact coverage and source-version limitations. These sources establish general physics; none defines the unpublished 0918 plotting code's `stateErr`, `sepErr`, or SNR convention.

## Hardware and signal reading added 2026-10-08

Read Krantz Fig. 1, pp. 4–5, alongside the energy-level explanation; Eqs. (92)–(94), p. 29, alongside frequency/amplitude/time/phase controls; and Fig. 22, p. 45, alongside IQ acquisition. Read Blais Fig. 14, p. 25, for the measurement hardware; Fig. 16, p. 27, for the mixer/reference oscillator; and Eq. (107), p. 29, through Fig. 19, p. 31, for the state-dependent resonator response. These existing PDFs supply the references for the new hardware note; no full-paper reading or recovery of the 0918 wiring is claimed.

## Related reading already in this repository

[Vibe Calibration](../papers/vibe-calibration-112-qubit-processor/note.md) discusses an agent executing a similar characterization workflow. The connection is operational: interpreting quantities is a prerequisite for judging calibration actions. Its reported fit thresholds belong to its stated setup; they are not universal physics rules or automatically applicable to the 0918 corpus. Existing reader-authored remarks in that note have been preserved.

## Source boundaries

- Original measurements: [0918 corpus](../../agent_control/data/0918/), a sibling-checkout link that works locally when both repositories are adjacent; it is not portable to GitHub by itself.
- Local analysis implementation: [raw-data audit](../../agent_control/scripts/audit_raw_physics.py) and [review pipeline documentation](../../agent_control/docs/data_review_pipeline.md).
- The four-panel figure is copied into these notes for standalone reading; its provenance and checksum are recorded in the [readout note](../concepts/iq-readout-and-assignment.md#local-evidence-and-provenance).
- Corpus values and code policy were checked on 2026-09-29. Existing automated-fit reports were not regenerated for this note-taking task.
