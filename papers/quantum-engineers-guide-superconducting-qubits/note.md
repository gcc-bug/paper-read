---
type: paper
title: "A Quantum Engineer's Guide to Superconducting Qubits"
authors: [Philip Krantz, Morten Kjaergaard, Fei Yan, Terry P. Orlando, Simon Gustavsson, William D. Oliver]
year: 2019
status: reading
source: "source.pdf"
original_filename: "1904.06560.pdf"
provenance: "https://arxiv.org/pdf/1904.06560; retrieved 2026-09-29; downloaded PDF identifies arXiv:1904.06560v5"
reading_dates: [2026-09-29]
---

# A Quantum Engineer's Guide to Superconducting Qubits

## Source and reading coverage

[Local PDF](source.pdf) · [arXiv v5](https://arxiv.org/abs/1904.06560v5) · [DOI](https://doi.org/10.1063/1.5089550).

Published in *Applied Physics Reviews* **6**, 021318 (2019). The downloaded source is the later arXiv v5, posted July 2021; do not describe it as the 2019 publisher PDF. Title, authors, version, DOI, and journal reference were checked against the arXiv record and PDF on 2026-09-29.

Targeted partial reading for the 0918 discussion: selected passages in Sec. III.B.2–3 around PDF/printed pp. 13–16, Figs. 4–5; Sec. IV.D.1, especially Eqs. (92)–(94), p. 29; selected readout passages in Sec. V.A–C, pp. 41–48, especially Fig. 22/caption on p. 45 and projection/separation discussion on pp. 47–48. Text was extracted locally. Page 47 was also rendered and visually checked. The complete review, bibliography, device taxonomy, and gate implementations were not read in full. Page numbers here refer to this local arXiv version; these printed labels agree with PDF indices at the cited locations.

Source SHA-256: `7925f8e9ee45eac83142ec8862d12e2728e6913ac26b2f912f72ecdadca2f10d`.

## Source claims

### Purpose and mechanism

This review introduces qubit design, noise, control, and readout to quantum engineers. For this discussion, its useful causal chain is drive pulse → state rotation → relaxation/coherence evolution → state-dependent microwave response → demodulated IQ observations.

- **Relaxation versus coherence:** Eqs. (41)–(42), p. 14, distinguish longitudinal relaxation from transverse relaxation and state the exponential-decay assumptions for adding rates. Fig. 5, p. 15, shows T1, Ramsey, and echo sequences. The discussion on p. 16 explicitly explains that nonexponential dephasing can invalidate a simple sum-of-rates description.
- **π pulses:** Sec. IV.D.1, Eqs. (92)–(94), p. 29, relates drive phase to rotation axis and drive-envelope integral to rotation angle. The rotation angle is distinct from the measured microwave response phase.
- **IQ acquisition:** Sec. V.B and Fig. 22, p. 45, describe downconversion, sampling, and digital processing into IQ points; repeated records produce state-dependent distributions.
- **Distribution separation:** Sec. V.C, pp. 47–48, projects IQ data onto a discrimination axis and discusses Gaussian overlap error. The text explicitly adds that relaxation/excitation during readout creates additional wrong-side outcomes; overlap alone does not determine full fidelity.

These are reviewed mechanisms and illustrative examples, not fresh experimental results from the 0918 corpus. No numerical performance claim from this review is being transferred to that corpus.

## Codex interpretation

This is the first reading recommendation because it connects the reader's questions about π pulses, T1, Ramsey, and IQ without requiring the full circuit-QED formalism. Read Fig. 5 before fitting a decay, and Fig. 22 before interpreting the axes of a readout plot.

Use care with SNR conventions. Page 47 gives a particular width/separation definition and Gaussian overlap treatment. It cannot identify the formula behind the local `SNR=19.00`. The qualitative phrase “fully separated” in an illustrative Gaussian plot does not imply mathematically zero Gaussian tails. For numerical use, start from a stated probability distribution, variance convention, and threshold rather than matching metric names.

## Connections

- [Calibration quantities](../../concepts/superconducting-qubit-calibration.md): basis for excitation/coherence and control-pulse explanations.
- [IQ readout](../../concepts/iq-readout-and-assignment.md): general explanation of clouds, projections, and overlap limits.
- [Blais review](../circuit-quantum-electrodynamics/note.md): more detailed dispersive response and explicit fidelity normalization.

## Open questions

Codex: which original estimator defines the local figure's SNR and component errors? This source does not answer that; see [the provenance question](../../questions/0918-readout-estimator-provenance.md).
