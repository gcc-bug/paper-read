---
type: paper
title: "Circuit Quantum Electrodynamics"
authors: [Alexandre Blais, Arne L. Grimsmo, S. M. Girvin, Andreas Wallraff]
year: 2021
status: reading
source: "source.pdf"
original_filename: "2005.12667.pdf"
provenance: "https://arxiv.org/pdf/2005.12667; retrieved 2026-09-29; downloaded PDF identifies arXiv:2005.12667v1"
reading_dates: [2026-09-29]
---

# Circuit Quantum Electrodynamics

## Source and reading coverage

[Local PDF](source.pdf) · [arXiv v1](https://arxiv.org/abs/2005.12667v1) · [DOI](https://doi.org/10.1103/RevModPhys.93.025005).

Published in *Reviews of Modern Physics* **93**, 025005 (2021). The local source is arXiv v1 from May 2020, not the final publisher PDF. Title, authors, DOI, journal reference, and source version were checked against the arXiv record/PDF on 2026-09-29.

Targeted partial reading: selected passages of Sec. V.C.1–2, PDF/printed pp. 29–32, including the state-dependent cavity response, Fig. 19, Eq. (115) for SNR, Eq. (116) for measurement fidelity, and footnote 7. Text extraction was local; page 32 was rendered and visually inspected to check an apparent sign error. The rest of this long review was not read for this task. Cited printed labels agree with PDF page indices in this local version.

Source SHA-256: `abb05ed2a9b721fd62273833d2a7bea638ddfbbbced78c082455c5263ddb6f95`.

## Source claims

- **Readout mechanism:** Sec. V.C.1 describes a dispersive interaction in which the resonator frequency/response depends on qubit state. The emitted field carries information about that state. Fig. 19, p. 31, shows corresponding state-dependent transmission and phase responses. These are resonator responses, not two peaks required in a qubit drive-frequency scan.
- **Signal processing:** Eq. (114), p. 31, describes weighted integration of measured quadratures, with discussion of how weighting can emphasize useful state information and reduce late-time relaxation effects.
- **SNR:** Eq. (115), p. 31, defines a specific ratio involving mean integrated-signal separation and noise variances. It is a convention, not a definition automatically shared by every experimental codebase.
- **Fidelity:** Eq. (116), p. 32, uses $F_m=1-[P(e\mid g)+P(g\mid e)]$. In terms of the two directional error probabilities ε₀ and ε₁, this is $1-(\epsilon_0+\epsilon_1)$, a contrast convention.
- **Model limits:** the discussion on p. 32 says the stated fidelity–SNR relation assumes Gaussian marginals; relaxation and higher-order effects can distort those distributions. Readout should also be fast compared with T1, and increasing readout drive is constrained by dispersive/QND limitations.

No source performance number is used as a benchmark or a calibration threshold for the 0918 data.

## Codex interpretation

This reference explains why a microwave response can distinguish a qubit state without directly plotting P1, and why readout duration, separation, and state transitions jointly matter. Its explicit fidelity convention is especially useful for avoiding comparisons between unlike percentages.

For two error probabilities, define balanced assignment fidelity explicitly:

$$
F_{\mathrm{assign}}=\frac{(1-\epsilon_0)+(1-\epsilon_1)}2,
\qquad F_m=2F_{\mathrm{assign}}-1.
$$

This algebra explains how a contrast near 0.88 can coexist with balanced assignment fidelity near 0.94. The local case-001 numbers agree with that relation, but agreement does not reconstruct the original plotting code.

### Source-version caution

In the local arXiv v1, footnote 7 on p. 32 prints a **minus** between the two directional errors in its alternative assignment-fidelity expression. This is visible in the rendered PDF, not merely a text-extraction artifact. That expression does not yield the balanced correctness probability; for example, it would give 1 when equal nonzero errors should reduce accuracy. Treat it as an apparent source typo, not a definition to copy. The correct balanced expression above is derived directly from the stated conditional probabilities. Whether the final publisher version corrects the footnote was not checked.

## Connections

- [Four-panel readout explanation](../../concepts/iq-readout-and-assignment.md): definitions, CDF threshold derivation, and limits of local metric interpretation.
- [Krantz review](../quantum-engineers-guide-superconducting-qubits/note.md): more introductory controls, coherence, and electronics background.
- [Reading map](../../maps/superconducting-qubit-calibration.md): official practical references and suggested order.

## Open questions

Codex: do the local fidelity and visibility use a shared threshold and the same input samples? The paper cannot answer this corpus-specific question. Recover the [original analysis provenance](../../questions/0918-readout-estimator-provenance.md).
