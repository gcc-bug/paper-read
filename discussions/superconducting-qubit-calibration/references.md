# Supporting references for the calibration discussion

[Discussion](note.md) · [Reading map](../../maps/superconducting-qubit-calibration.md).

These sources were consulted by Codex for the 0918 calibration discussion and its hardware/readout continuation. The annotations record the passages used, source claims, and Codex explanations; they are not standalone paper-reading results or reader-confirmed understanding.

2026-10-14 — Companion-note expansion added an introductory superconductivity reference and revisited selected local circuit/noise/measurement-chain passages. Exact additional coverage is recorded below. These additions support general explanations, not causal diagnoses of the local cases.

2026-10-08 — Filing correction: consolidated the former two paper notes here as discussion reference annotations. Existing coverage, provenance, source caveats, and explanations are retained. No additional source reading was performed for this correction.

## A Quantum Engineer's Guide to Superconducting Qubits

Authors: Philip Krantz, Morten Kjaergaard, Fei Yan, Terry P. Orlando, Simon Gustavsson, William D. Oliver. Publication year: 2019.

Original filename: `1904.06560.pdf`.

Provenance: https://arxiv.org/pdf/1904.06560; retrieved 2026-09-29; downloaded PDF identifies arXiv:1904.06560v5.

Consultation dates recorded in the former note: 2026-09-29, 2026-10-08.

### Source and reading coverage

[Local PDF](references/krantz-quantum-engineers-guide-superconducting-qubits.pdf) · [arXiv v5](https://arxiv.org/abs/1904.06560v5) · [DOI](https://doi.org/10.1063/1.5089550).

Published in *Applied Physics Reviews* **6**, 021318 (2019). The downloaded source is the later arXiv v5, posted July 2021; do not describe it as the 2019 publisher PDF. Title, authors, version, DOI, and journal reference were checked against the arXiv record and PDF on 2026-09-29.

Targeted partial reading for the 0918 discussion: selected passages in Sec. III.B.2–3 around PDF/printed pp. 13–16, Figs. 4–5; Sec. IV.D.1, especially Eqs. (92)–(94), p. 29; selected readout passages in Sec. V.A–C, pp. 41–48, especially Fig. 22/caption on p. 45 and projection/separation discussion on pp. 47–48. Text was extracted locally. Page 47 was also rendered and visually checked. The complete review, bibliography, device taxonomy, and gate implementations were not read in full. Page numbers here refer to this local arXiv version; these printed labels agree with PDF indices at the cited locations.

Source SHA-256: `7925f8e9ee45eac83142ec8862d12e2728e6913ac26b2f912f72ecdadca2f10d`.

### Source claims

#### Purpose and mechanism

This review introduces qubit design, noise, control, and readout to quantum engineers. For this discussion, its useful causal chain is drive pulse → state rotation → relaxation/coherence evolution → state-dependent microwave response → demodulated IQ observations.

- **Relaxation versus coherence:** Eqs. (41)–(42), p. 14, distinguish longitudinal relaxation from transverse relaxation and state the exponential-decay assumptions for adding rates. Fig. 5, p. 15, shows T1, Ramsey, and echo sequences. The discussion on p. 16 explicitly explains that nonexponential dephasing can invalidate a simple sum-of-rates description.
- **π pulses:** Sec. IV.D.1, Eqs. (92)–(94), p. 29, relates drive phase to rotation axis and drive-envelope integral to rotation angle. The rotation angle is distinct from the measured microwave response phase.
- **IQ acquisition:** Sec. V.B and Fig. 22, p. 45, describe downconversion, sampling, and digital processing into IQ points; repeated records produce state-dependent distributions.
- **Distribution separation:** Sec. V.C, pp. 47–48, projects IQ data onto a discrimination axis and discusses Gaussian overlap error. The text explicitly adds that relaxation/excitation during readout creates additional wrong-side outcomes; overlap alone does not determine full fidelity.

These are reviewed mechanisms and illustrative examples, not fresh experimental results from the 0918 corpus. No numerical performance claim from this review is being transferred to that corpus.

### Codex interpretation

This is the first reading recommendation because it connects the reader's questions about π pulses, T1, Ramsey, and IQ without requiring the full circuit-QED formalism. Read Fig. 5 before fitting a decay, and Fig. 22 before interpreting the axes of a readout plot.

Use care with SNR conventions. Page 47 gives a particular width/separation definition and Gaussian overlap treatment. It cannot identify the formula behind the local `SNR=19.00`. The qualitative phrase “fully separated” in an illustrative Gaussian plot does not imply mathematically zero Gaussian tails. For numerical use, start from a stated probability distribution, variance convention, and threshold rather than matching metric names.

### Connections

- [Calibration quantities](../../concepts/superconducting-qubit-calibration.md): basis for excitation/coherence and control-pulse explanations.
- [IQ readout](../../concepts/iq-readout-and-assignment.md): general explanation of clouds, projections, and overlap limits.
- [Blais review](references.md#circuit-quantum-electrodynamics): more detailed dispersive response and explicit fidelity normalization.

### 2026-10-08 targeted continuation: hardware and signal controls

Additional reading covered Sec. II.A, pp. 4–5, particularly Fig. 1 and Eqs. (13)–(16); revisited Sec. IV.D.1, p. 29, Eqs. (92)–(94), and the acquisition discussion/Fig. 22, p. 45. Extraction was local; p. 5 was rendered and visually checked. The complete paper remains only partially read. Source bytes and bibliographic metadata were preserved.

Source claims: Fig. 1 contrasts an LC oscillator's equally spaced levels with a Josephson oscillator's unequal spacing, permitting selection of the lowest two levels. Eq. (16) gives the simplified transmon Hamiltonian. Eqs. (92)–(94) connect drive phase and envelope to rotation axis and angle; adjacent discussion describes combining frequencies to address multiple qubits or resonators. Fig. 22 traces heterodyne detection through ADC sampling to IQ processing.

Codex interpretation: these passages explain why carrier frequency, amplitude, duration, and phase are separate controls, and why recorded IQ is a microwave response rather than the qubit wavefunction. The new [hardware and signals note](../../concepts/superconducting-qubit-hardware-and-signals.md) combines them into a generic setup and iterative calibration sequence. That sequence is explanatory synthesis, not an experimentally recovered ordering of 0918 cases.

### Open questions

Codex: which original estimator defines the local figure's SNR and component errors? This source does not answer that; see [the provenance question](../../questions/0918-readout-estimator-provenance.md).

### 2026-10-14 targeted continuation: circuit foundations and noise

Locally extracted and consulted PDF pp. 4–5, Sec. II.A, including Fig. 1 and Eqs. (13)–(16), and pp. 18–19, Sec. III.C.1–4. Text extraction used `pypdf`; no visual audit or full-paper rereading was performed. Original PDF bytes were unchanged.

Source claims: the LC model has equally spaced levels; the Josephson relations and cosine potential provide anharmonicity. A large shunt capacitance reduces charging energy and charge sensitivity in the transmon regime. The noise discussion covers interface/dielectric charge fluctuations, flux noise, residual resonator photon fluctuations, and quasiparticles, with relaxation or dephasing depending on the coupling and device. It also describes observed nonequilibrium quasiparticles at low refrigerator temperatures.

Codex interpretation: these passages support the expanded [personal preparation notes](slides/notes.md), especially why an engineered circuit can encode a qubit, why superconductivity does not imply unlimited coherence, and how environment changes affect control or measurement. The 5 GHz / 20 mK two-level equilibrium example is a Codex calculation, not a reported temperature or population of the local device. No source mechanism is assigned as the established cause of a local anomaly.

### 2026-10-15 targeted continuation: IQ and parameter variation

Locally extracted and consulted PDF pp. 5–6 (Secs. II.A–B.1 circuit model and frequency tuning), pp. 18–19 (Sec. III.C charge/flux noise, resonator photons and quasiparticles), p. 29 (Sec. IV.D.1 drive model), and p. 45 (Fig. 22 and heterodyne detection). This is selective text consultation, not a full rereading or new experimental evidence; original source bytes were preserved.

Source claims: circuit energies and drive coupling enter the qubit frequency and rotation; sensitivity to flux depends on device and bias point. Low-frequency fluctuations, residual photons and quasiparticles can affect coherence or population. Fig. 22 follows one received microwave signal through quadrature mixing, ADC sampling and processing to an IQ point.

Codex interpretation: the updated [companion notes](slides/notes.md) separate variation between devices, changes over time and changes with operating conditions. Changes in a control or readout transfer function can change the implemented rotation or recorded IQ without establishing intrinsic qubit drift. The ideal demodulation derivation, illustrative IQ values, and calibration-starting-point explanation are teaching synthesis; no local drift rate, cause or original demodulation convention was recovered.

## Circuit Quantum Electrodynamics

Authors: Alexandre Blais, Arne L. Grimsmo, S. M. Girvin, Andreas Wallraff. Publication year: 2021.

Original filename: `2005.12667.pdf`.

Provenance: https://arxiv.org/pdf/2005.12667; retrieved 2026-09-29; downloaded PDF identifies arXiv:2005.12667v1.

Consultation dates recorded in the former note: 2026-09-29, 2026-10-08.

### Source and reading coverage

[Local PDF](references/blais-circuit-quantum-electrodynamics.pdf) · [arXiv v1](https://arxiv.org/abs/2005.12667v1) · [DOI](https://doi.org/10.1103/RevModPhys.93.025005).

Published in *Reviews of Modern Physics* **93**, 025005 (2021). The local source is arXiv v1 from May 2020, not the final publisher PDF. Title, authors, DOI, journal reference, and source version were checked against the arXiv record/PDF on 2026-09-29.

Targeted partial reading: selected passages of Sec. V.C.1–2, PDF/printed pp. 29–32, including the state-dependent cavity response, Fig. 19, Eq. (115) for SNR, Eq. (116) for measurement fidelity, and footnote 7. Text extraction was local; page 32 was rendered and visually inspected to check an apparent sign error. The rest of this long review was not read for this task. Cited printed labels agree with PDF page indices in this local version.

Source SHA-256: `abb05ed2a9b721fd62273833d2a7bea638ddfbbbced78c082455c5263ddb6f95`.

### Source claims

- **Readout mechanism:** Sec. V.C.1 describes a dispersive interaction in which the resonator frequency/response depends on qubit state. The emitted field carries information about that state. Fig. 19, p. 31, shows corresponding state-dependent transmission and phase responses. These are resonator responses, not two peaks required in a qubit drive-frequency scan.
- **Signal processing:** Eq. (114), p. 31, describes weighted integration of measured quadratures, with discussion of how weighting can emphasize useful state information and reduce late-time relaxation effects.
- **SNR:** Eq. (115), p. 31, defines a specific ratio involving mean integrated-signal separation and noise variances. It is a convention, not a definition automatically shared by every experimental codebase.
- **Fidelity:** Eq. (116), p. 32, uses $F_m=1-[P(e\mid g)+P(g\mid e)]$. In terms of the two directional error probabilities ε₀ and ε₁, this is $1-(\epsilon_0+\epsilon_1)$, a contrast convention.
- **Model limits:** the discussion on p. 32 says the stated fidelity–SNR relation assumes Gaussian marginals; relaxation and higher-order effects can distort those distributions. Readout should also be fast compared with T1, and increasing readout drive is constrained by dispersive/QND limitations.

No source performance number is used as a benchmark or a calibration threshold for the 0918 data.

### Codex interpretation

This reference explains why a microwave response can distinguish a qubit state without directly plotting P1, and why readout duration, separation, and state transitions jointly matter. Its explicit fidelity convention is especially useful for avoiding comparisons between unlike percentages.

For two error probabilities, define balanced assignment fidelity explicitly:

$$
F_{\mathrm{assign}}=\frac{(1-\epsilon_0)+(1-\epsilon_1)}2,
\qquad F_m=2F_{\mathrm{assign}}-1.
$$

This algebra explains how a contrast near 0.88 can coexist with balanced assignment fidelity near 0.94. The local case-001 numbers agree with that relation, but agreement does not reconstruct the original plotting code.

#### Source-version caution

In the local arXiv v1, footnote 7 on p. 32 prints a **minus** between the two directional errors in its alternative assignment-fidelity expression. This is visible in the rendered PDF, not merely a text-extraction artifact. That expression does not yield the balanced correctness probability; for example, it would give 1 when equal nonzero errors should reduce accuracy. Treat it as an apparent source typo, not a definition to copy. The correct balanced expression above is derived directly from the stated conditional probabilities. Whether the final publisher version corrects the footnote was not checked.

### Connections

- [Four-panel readout explanation](../../concepts/iq-readout-and-assignment.md): definitions, CDF threshold derivation, and limits of local metric interpretation.
- [Krantz review](references.md#a-quantum-engineers-guide-to-superconducting-qubits): more introductory controls, coherence, and electronics background.
- [Reading map](../../maps/superconducting-qubit-calibration.md): official practical references and suggested order.

### 2026-10-08 targeted continuation: measurement chain and dispersive model

Additional selective reading covered Sec. V.A, pp. 25–27, especially Figs. 14 and 16 and their surrounding explanations; revisited Sec. V.C.1, pp. 29–31, Eq. (107), the steady-state response Eq. (110), and Fig. 19. Text extraction was local; p. 29 was rendered and visually checked to verify the dispersive Hamiltonian and state/sign convention. The full paper remains only partially read. Source bytes and bibliographic metadata were preserved.

Source claims: Fig. 14 traces the probe through thermal attenuation, a resonator, amplification, mixing, digitization, and FPGA processing; Sec. V.A explains incoming thermal noise and protection from amplifier noise. Fig. 16 describes mixing with reference signals offset by π/2 to measure quadratures. Eq. (107) yields resonator frequencies $\omega_r-\chi$ for the ground state and $\omega_r+\chi$ for the excited state under its stated approximations. Eq. (110) and Fig. 19 connect these shifts to complex resonator responses.

Codex interpretation: the response convention and chosen observable determine whether a state change looks like a peak or a dip. The [hardware and signals note](../../concepts/superconducting-qubit-hardware-and-signals.md) derives an illustrative linear-readout example and distinguishes it from a resonator transmission notch. This does not identify the topology or estimator behind any particular 0918 trace.

### Open questions

Codex: do the local fidelity and visibility use a shared threshold and the same input samples? The paper cannot answer this corpus-specific question. Recover the [original analysis provenance](../../questions/0918-readout-estimator-provenance.md).

### 2026-10-14 targeted continuation: thermal protection and amplification

Locally extracted and consulted PDF pp. 25–26, Sec. V opening and Sec. V.A, including Fig. 14 and surrounding explanations. Text extraction used `pypdf`; no new visual audit or full-paper rereading. Existing annotations on p. 27 and pp. 29–32 remain the basis for quadrature and dispersive-readout explanations.

Source claims: distributed, thermally anchored attenuators absorb incoming room-temperature noise; circulators limit amplifier noise reaching the sample. The output is amplified, mixed, digitized, and processed. The measurement chain has finite bandwidth and added amplifier noise; qubit readout involves backaction even when energy exchange is inhibited in the dispersive regime.

Codex interpretation: this supports explaining why low refrigerator temperature alone does not establish a cold, noise-free device or perfect readout. The simplified chain in the notes is generic, not a reconstruction of 0918 wiring or gain calibration.

### 2026-10-15 targeted continuation: two quadratures of one received signal

Locally extracted and consulted PDF p. 27, especially Fig. 16 and the IQ mixer description. The figure splits one received RF signal into two branches and mixes them against LO references shifted by pi/2; this supports explaining that I and Q are two components of the same received signal. The companion notes provide a classical voltage derivation with an explicit Q-sign convention. That derivation and its illustrative numbers do not identify the local acquisition hardware, gains, offsets or integration weights. No full-paper rereading or new measurement was performed; original source bytes were preserved.

<a id="openstax-superconductivity"></a>

## OpenStax: introductory superconductivity

Source: *University Physics Volume 3*, §9.8, “Superconductivity,” [official online chapter](https://openstax.org/books/university-physics-volume-3/pages/9-8-superconductivity). Online consultation on 2026-10-14; the page text was retrieved and inspected locally. The temporary HTML/text extraction stays outside the repository; no local PDF or standalone paper-reading record was created. An edition or revision date was not verified.

Coverage: the opening “Properties of Superconductors” discussion of zero resistance, the Meissner effect, critical temperature, and magnetic-field limits; selected “Theory of Superconductors” paragraphs introducing BCS theory and Cooper pairs. Exercises, numerical examples, applications, and the complete textbook were not studied for this task.

Source claims: zero resistance and the Meissner response are distinct properties; superconductivity is subject to material-dependent critical conditions. The BCS introduction describes electron pairing through an effective attraction in a lattice and Cooper pairs.

Codex interpretation: the textbook supplies elementary background before the Josephson-circuit explanation. The notes scope the pairing picture to conventional superconductors and avoid equating zero DC resistance with absence of microwave/device loss. The collective-phase variables and Josephson equations are grounded in the Krantz circuit passages rather than attributed to this introductory chapter. The notes do not use superconductivity to infer a temperature, material, or measured coherence of the local device.
