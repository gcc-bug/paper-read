# Superconducting-qubit calibration: discussion

Notes consolidated on 2026-09-29 from the reader's 0918-data discussion. Explanations are Codex interpretations; they are not assertions that the reader has adopted them. The experiment corpus remains in the sibling `agent_control` checkout. No new experiment or calibration acceptance is claimed.

## Start here

1. [Calibration quantities and physical meaning](../../concepts/superconducting-qubit-calibration.md): six experiments, raw columns, excitation, π pulses, peaks versus valleys, T1 versus Ramsey, and numerical rules.
2. [IQ readout and the four-panel figure](../../concepts/iq-readout-and-assignment.md): every axis and reported metric in case 001, preparation versus assignment, histogram counts, threshold selection, and fidelity conventions.
3. [Unresolved readout provenance](../../questions/0918-readout-estimator-provenance.md): what the original plotting/analysis code must establish.
4. [Hardware, microwave signals, and calibration progression](../../concepts/superconducting-qubit-hardware-and-signals.md): device roles, energy levels, drive controls, dispersive readout, anticipating peak/dip polarity, and the iterative sequence.

## Reading order and references

[Consolidated source annotations and PDFs](references.md).

| Priority | Reference | Read for this discussion |
| --- | --- | --- |
| First | P. Krantz et al., *A Quantum Engineer's Guide to Superconducting Qubits*, Applied Physics Reviews **6**, 021318 (2019), [DOI](https://doi.org/10.1063/1.5089550), [source annotations and PDF](references.md#a-quantum-engineers-guide-to-superconducting-qubits) | Figs. 4–5 for relaxation/coherence; Sec. IV.D.1 for rotations; Sec. V.B–C and Figs. 22–23 for IQ and distribution separation. Local source is arXiv v5 (2021 revision), not the publisher PDF. |
| Then | A. Blais et al., *Circuit Quantum Electrodynamics*, Reviews of Modern Physics **93**, 025005 (2021), [DOI](https://doi.org/10.1103/RevModPhys.93.025005), [source annotations and PDF](references.md#circuit-quantum-electrodynamics) | Sec. V.C.1–2, Fig. 19, Eqs. (115)–(116): state-dependent resonator response, SNR, and fidelity conventions. Local source is arXiv v1 (2020), not the publisher PDF. |
| Practical | Qiskit Experiments, [T1 Characterization](https://qiskit-community.github.io/qiskit-experiments/manuals/characterization/t1.html) | Background: repeat prepare–wait–measure and fit $A e^{-t/T_1}+B$. |
| Practical | Qiskit Experiments, [T2* Ramsey Characterization](https://qiskit-community.github.io/qiskit-experiments/manuals/characterization/t2ramsey.html) | Circuit sequence, damped oscillation, intentional oscillation frequency versus detuning. |
| Practical | Qiskit Experiments, [Readout Mitigation](https://qiskit-community.github.io/qiskit-experiments/manuals/measurement/readout_mitigation.html) | Opening definition of the assignment matrix and “Standard mitigation experiment.” |

The three documentation pages were inspected on 2026-09-29 and displayed Qiskit Experiments 0.14.2. They are live references, not locally executed examples. The Ramsey introduction has a misleading sentence referring to initialization in |1⟩; the listed SX–delay–RZ–SX circuit and Krantz Fig. 5 establish superposition preparation during the free-evolution interval. Use the circuit, not that isolated sentence.

The two papers were consulted selectively as supporting references. Their annotations record exact consultation coverage and source-version limitations. These sources establish general physics; none defines the unpublished 0918 plotting code's `stateErr`, `sepErr`, or SNR convention.

## Hardware and signal reading added 2026-10-08

Read Krantz Fig. 1, pp. 4–5, alongside the energy-level explanation; Eqs. (92)–(94), p. 29, alongside frequency/amplitude/time/phase controls; and Fig. 22, p. 45, alongside IQ acquisition. Read Blais Fig. 14, p. 25, for the measurement hardware; Fig. 16, p. 27, for the mixer/reference oscillator; and Eq. (107), p. 29, through Fig. 19, p. 31, for the state-dependent resonator response. These existing PDFs supply the references for the new hardware note; no full-paper reading or recovery of the 0918 wiring is claimed.

## Related reading already in this repository

[Vibe Calibration](../../papers/vibe-calibration-112-qubit-processor/note.md) discusses an agent executing a similar characterization workflow. The connection is operational: interpreting quantities is a prerequisite for judging calibration actions. Its reported fit thresholds belong to its stated setup; they are not universal physics rules or automatically applicable to the 0918 corpus. Existing reader-authored remarks in that note have been preserved.

## Source boundaries

- Original measurements: [0918 corpus](../../../agent_control/data/0918), a sibling-checkout link that works locally when both repositories are adjacent; it is not portable to GitHub by itself.
- Local analysis implementation: [raw-data audit](../../../agent_control/scripts/audit_raw_physics.py) and [review pipeline documentation](../../../agent_control/docs/data_review_pipeline.md).
- The four-panel figure is copied into these notes for standalone reading; its provenance and checksum are recorded in the [readout note](../../concepts/iq-readout-and-assignment.md#local-evidence-and-provenance).
- Corpus values and code policy were checked on 2026-09-29. Existing automated-fit reports were not regenerated for this note-taking task.

## Organization correction

2026-10-08 — The reader clarified that the two supporting papers belong to this discussion rather than standalone paper readings. Their PDFs and source annotations now live here. The reusable calibration, IQ-readout, and hardware explanations remain in the linked concept notes. This correction changes filing and navigation, with no new paper reading or experiment.

## Chinese Beamer presentation added 2026-10-10

The reader approved a presentation covering hardware, the calibration pipeline, and paired clearer/needs-review data. [Slides and build instructions](slides/README.md): 24-page main talk, [65-page full version](slides/0918-calibration-zh.pdf), and [all 47 review cases](slides/coverage.md). English technical terms are retained and abbreviations are expanded on first use. The appendix includes all 46 recorded audit flags plus Resonator/006; these are review targets, not established acquisition errors. Figures replot byte-preserved numeric snapshots and reuse recorded diagnostics. No new acquisition or full nonlinear audit rerun was performed.

The explanations and possible causes are Codex interpretations. Supporting sources are the existing Krantz/Blais PDFs; the previously consulted passages are reused, with p. 29 of each PDF selectively re-extracted and checked for the pulse-control/dispersive models. This does not constitute a full rereading. Source versions, column mappings, estimator differences, reproducibility instructions, and limitations are recorded in the slides README.

## Presentation rewrite added 2026-10-12

The reader requested shorter slides, moved explanations into companion notes, and approved the company Beamer layout and stronger typography for less clear screens. The deck is now a 25-page main talk and a [67-page full version](slides/0918-calibration-zh.pdf), with [background and slide explanations](slides/notes.md) and [detailed notes for all 47 cases](slides/case-notes.md). Slides retain the figures, key diagnostics, and essential interpretation limits; candidate causes in the case notes are labeled as unverified hypotheses.

The original evidence snapshot, all 64 CSVs, both supporting PDFs, reference selections, and full case explanations are preserved. This revision changes presentation and navigation; it adds no acquisition or full nonlinear audit. All 67 pages were rendered and inspected, including representative low-resolution previews. [Build instructions and validation scope](slides/README.md) record the current organization. The 2026-10-10 description above records the earlier delivery.

## Presentation navigation and figure tools added 2026-10-12

The reader clarified that “0918” is a private label and requested an agenda,
section progress, and established figure tools. At this revision, the main talk
is 26 pages and the [full version](slides/0918-calibration-zh.pdf) is 68 pages.
The agenda and section footer use native Beamer navigation data; appendix pages
are kept separate from main-section progress. Circuitikz supplies electrical
symbols, PGFPlots draws the illustrative pulse, and case plots use Beamer figure
environments with their existing Matplotlib PDFs. The internal label remains
in filenames and provenance notes, outside displayed slide content. The reader's
existing title/date edits are preserved. Evidence and diagnostics are unchanged;
[companion notes](slides/notes.md) have updated page references.

## Native dot navigation and single PDF — 2026-10-12

The reader chose Berlin-style native frame dots, consistent Beamer `figure`
environments for both drawn and imported visuals, and one full PDF. The earlier
main-only deliveries described above are superseded; PDF links point to the
current [68-page full deck](slides/0918-calibration-zh.pdf), with the main talk
followed by the appendix. The shared company theme now uses the native
`miniframes` headline instead of a custom progress bar/fraction. All nine
hardware/workflow visuals in the deck source use `figure`, including those
inside columns. Existing reader title, date, and hardware-section edits are
preserved. Companion links and the reusable slide-writing skill follow the
single-PDF preference. No scientific evidence or case interpretation changed.

## Future calibration-agent proposal — 2026-10-13

The reader clarified that the 0918 analysis motivates a future project using LLMs to control and automatically calibrate physical devices. The long-term vision is cooperation among agents using models of different costs and capabilities to balance price and effectiveness, with a software-engineering perspective. The current request is proposal development, not implementation.

[Research proposal: adaptive multi-agent software for physical-device calibration](proposal.md) records the reader-confirmed direction separately from Codex's proposed formulation, research stages, software contracts and hypotheses. It connects the stored cases to evidence-aware decisions and annotates selected prior work on laboratory agents, heterogeneous models, routing and calibration software. This targeted comparison does not establish novelty or demonstrate improved calibration outcomes.

## Personal preparation notes expanded — 2026-10-14

At the reader's request, [the companion notes](slides/notes.md) now follow an explanatory learning sequence: superconductivity and circuit energy levels, control and environmental effects, calibration versus characterization, IQ and populations, experiment mechanisms, fit identifiability, eight case walkthroughs, and the software/harness research view. They include foundational definitions, worked reasoning, and likely audience questions beyond what the slides show. [Early-control-work notes](slides/early-control-work-notes.md) also explain transfer functions, predistortion boundaries, and general ion-transport software roles while preserving confirmed contribution ownership.

Codex explanations remain separate from reader-confirmed views and unverified research hypotheses. Additional supporting coverage is recorded in [references.md](references.md): selected local Krantz/Blais passages and OpenStax's introductory superconductivity discussion. The deck, figures, measurements, recorded diagnostics, and generated case notes were not changed or regenerated. Original estimator provenance, case causes, and proposed system benefits remain unresolved.

Link check on 2026-10-14: the three historical sibling-checkout links under “Source boundaries” are unavailable in this workspace. They remain as provenance locations; the [packaged data and evidence](slides/README.md) are available within this repository. New local links were checked, and all 64 packaged CSV hashes match the stored evidence snapshot.
