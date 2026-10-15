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


<a id="calibration-software-sources"></a>

## 自动校准软件研究的既有来源与确认记录

2026-10-15 — 从 slides/notes.md 迁入，保留 2026-10-14 的来源咨询范围和读者确认记录；本次迁移未增加文献阅读或软件运行。以下叙述中的“此次”“本轮”指原记录的修订。

2026-10-14 — 根据读者审阅，替代前版五阶段、细架构的讲述。研究计划移入正文，在案例总结之后、参考文献之前。读者明确认可软件工程与 harness 视角，以及不同模型和智能体协作、平衡价格与效果的长期目标。以下是据此起草的解释；具体机制与收益属于拟研究内容。

### 已有工作与支持范围

[Vibe Calibration 阅读记录](../../papers/vibe-calibration-112-qubit-processor/note.md) 提供专家流程 Skills 化、智能体调用现有实验工具开展多步表征与校准的实例。此处复用已有阅读记录，不增加全文阅读或性能比较。

[NVIDIA Quantum Calibration Agent Blueprint](https://github.com/NVIDIA/Quantum-Calibration-Agent-Blueprint/) 是参考软件蓝图。此次选读其官方 README（2026-10-14）：项目介绍实验发现与调用、图与数据分析、多步工作流、JSON 工作流状态跟踪、结果存储与会话恢复。它支持“模型需要与工具和流程组成软件系统”的讲述。多个模型供应商接口不等于已经实现异构模型协同或自适应成本优化；README 不提供这里拟研究机制的效果结论。未运行该项目或进行设备实验。

**补充依据（2026-10-14 的此前讨论中选读，非全文阅读）**：

- [QUAlibrate 官方文档](https://qualibrate-docs.quantum-machines.co/)：overview 介绍可复用的 `QualibrationNode`、校准库、`QualibrationGraph` 与 QUAM 设备表示。它提供常规校准软件的组织基础；属于具体软件平台文档，不是本研究设想的性能验证。未运行该平台。
- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793)，2024：选读 arXiv v3 abstract 与[官方 README](https://github.com/SWE-agent/SWE-agent/)。论文研究模型操作代码仓库、编辑代码和执行测试的接口设计，支持“软件环境与模型接口值得研究”的视角。该证据来自软件工程任务，不能直接推出物理校准中的收益，也不意味着环境越复杂越好。

### 研究视角的确认记录

Harness 在此指连接模型、实验工具、工作流程与结果的软件环境。读者希望从软件工程角度研究：怎样复用校准经验，并适应不同设备、工具和模型。此次将问题进一步表述为“哪些能力应该由模型判断，哪些应该沉淀为可复用的软件流程？”这是研究问题，不是已经证明的设计结论。前面的案例分析为理解任务和判断环节提供背景，不被写成完整系统设计或已实现能力。

建议转场：“已有工作展示了模型参与校准的可能性。我希望进一步研究，怎样把这些能力组织为能够复用和扩展的软件系统。”

### 路线与模型路由的支持范围

依次研究单模型与现有工具的配合、可复用 harness、不同模型与智能体的协作。低成本模型承担分类与常规处理，较强或专长模型参与复杂分析、代码和文献，是拟研究的分工示例，不是固定角色架构或已测得的成本收益。阶段用于组织研究设想，没有承诺原型、时间表或实验结果。

[RouteLLM: Learning to Route LLMs with Preference Data](https://arxiv.org/abs/2406.18665)，2024：此前讨论选读 arXiv v4 abstract，介绍用偏好数据学习强弱模型间的路由，以平衡成本与回答质量。这是文本任务中的模型选择依据；它不证明校准任务中的收益，也不等于已经实现多智能体协作。报告把模型路由作为长期分工的支持，把如何评价整个校准流程的效果与成本保留为开放问题。

[原 proposal](proposal.md) 保留前期更详细的讨论与相关工作；报告采用本轮确认的简洁主线，其中此前以证据路由与状态契约为中心的表述不再代表本次汇报重点。


### 笔记来源范围的迁移说明

2026-10-14 — 为补充基础解释，本轮在本地提取 Krantz PDF pp. 4–5、18–19，以及 Blais pp. 25–26 的文字并核对所引内容；其余控制、读出和相干模型沿用已经记录的选择性阅读。新增选读 OpenStax §9.8 的超导性质和 BCS 入门段落。公式中的低温二能级例子、短窗口展开和案例教学解释是 Codex 的计算或推理，不是这些来源报告的本设备结果。详细新增注释见[本文件](references.md)。

两篇综述均未全文重读；软件研究参考沿用此前记录的咨询范围。尚待解决的内容包括原始读出估计器、部分采集时序和设备细节、异常的物理原因，以及研究设想的实际收益。


2026-10-15 — 为 IQ 与参数变化的补充解释，选读 Krantz PDF pp. 5–6、18–19、29、45，以及 Blais PDF p. 27；详细范围与解释边界见[本文件](references.md)。本轮没有新增本设备的测量或恢复原始解调实现。

以下保留此前记录的选择性阅读位置；本轮补读范围见本文件相应日期的咨询记录，没有全文重读：

- P. Krantz et al., *A Quantum Engineer's Guide to Superconducting Qubits*, Applied Physics Reviews 6, 021318 (2019)，[DOI](https://doi.org/10.1063/1.5089550)。[本地 PDF](references/krantz-quantum-engineers-guide-superconducting-qubits.pdf) 是 arXiv:1904.06560v5，2021 revision。使用 Fig. 1 / Eq. (16), pp. 4–5；Fig. 5, p. 15；Eqs. (92)–(94), p. 29；Fig. 22, p. 45。
- A. Blais et al., *Circuit Quantum Electrodynamics*, Reviews of Modern Physics 93, 025005 (2021)，[DOI](https://doi.org/10.1103/RevModPhys.93.025005)。[本地 PDF](references/blais-circuit-quantum-electrodynamics.pdf) 是 arXiv:2005.12667v1，2020 version。使用 Figs. 14/16, pp. 25/27；Eq. (107), p. 29；Fig. 19, p. 31。

这些位置按本地 PDF 页码；版本不同可能变化。旧制作记录另说明曾重新提取两篇 p. 29 核对 control/dispersive models。本轮继续沿用已记录的控制与读出解释，新增咨询范围见本文件相应日期的咨询记录；论文不能恢复 0918 未发布 plotting code 的 estimator。

<a id="fan-surface-trap-poster"></a>

## Fan et al.: 3D-printed surface-trap poster

- **Title:** *3D Printed Surface Trap designed for QCCD-based large-scale quantum computation using 174Yb+ and 138Ba+*.
- **Authors:** Xuan Fan, Pengfei Wang, Yuan Chai, Zexin Wu, Wenhan Hua, Dingchao Gao, Honghua Fang, Hongbo Sun, Kihwan Kim. Dingchao Gao's listed affiliation is Beijing Zhongke Arclight Quantum Software Technology Co., Ltd.
- **Year/event:** not verified. Original filename contains `v1.0`; PDF metadata is not used to infer an event or publication date.
- **Local source:** [preserved poster PDF](references/fan-3d-printed-surface-trap-qccd-poster.pdf).
- **Original filename and provenance:** `3_合肥海报-范宣v1.0.pdf`, supplied by the reader from `/Users/coldcat/Downloads/` on 2026-10-15. Copied byte-for-byte; original retained. SHA-256: `bb432e5de5593b8a427132b0d587be4815259712fcb802df0ab53ab1aaac6cd1`.
- **Role:** supporting reference for the early quantum-control software presentation, not a standalone paper-reading intake. Reader states the poster work was supported by sion; the poster itself does not name sion / sion-exper or specify individual software responsibilities.

**Consultation, 2026-10-15:** locally extracted and visually inspected the complete one-page poster, including title/authors, abstract, Figs. 1–8 and their captions, and bibliography. Closely checked Figs. 2, 7 and 8 for electrode counts, simulation/experiment categories, and image interpretation. The cited bibliography was not followed or independently read. Extraction repeats the title block; isotope notation and captions were checked visually. Embedded plot labels have the poster's finite image resolution; no numerical digitization or raw data recovery was attempted.

**Source claims used:** Fig. 2 describes a nine-wire surface trap with 22 pairs of segmented DC electrodes. Fig. 7 is theoretical ion-transport simulation using shortcuts to adiabaticity (STA); plot title “Optimized Voltages V1–V22 over Time,” time in μs and voltage in V. Fig. 8 reports one 138Ba+ ion transported across one electrode in 100 discrete steps. Its time-lapsed CCD image shows that same ion at two stationary endpoints, held for millisecond durations to enhance visibility. The abstract describes fundamental shuttling as a demonstrated step toward a future hundred-qubit system, not an achieved hundred-qubit processor.

**Limits and Codex interpretation:** Fig. 7's claimed average error below 10^-16 is not sufficiently defined on this poster to support a hardware-accuracy or fidelity statement. Fig. 8 does not demonstrate two simultaneous ions, two wells moving toward one another, or well merging. The poster does not establish that the displayed simulation curves were the exact experimental waveforms. The 22 electrode pairs, 22 plotted voltage labels, independent DAC channels and electrodes active in a given operation must not be equated without a mapping. Fig. 6's heating discussion and contamination attribution are outside the claims used in the slides; no independent diagnosis was made. Authorship does not establish who performed physical experiments.

**Reader clarification history:** before providing the poster, the reader confirmed “15 electrodes total; two wells move toward the middle.” Asked how that relates to the poster's 22 pairs, the reader replied “maybe i make mistake.” Accordingly the slides withdraw the 15 count and use generic electrode blocks; the original statement and subsequent uncertainty remain in the [companion notes](slides/early-control-work-notes.md). The actual driven subset and relation between the two descriptions remain unresolved.

**Slide assets:** [voltage plot crop](slides/figures/poster-transport-voltages.png) and [transport image crop](slides/figures/poster-transport-endpoints.png), reproduced by [crop script](slides/crop_transport_poster.py). Both use unchanged regions of the original page render, omit the original captions in favor of attributed Chinese slide captions, and do not include personal contact details. The complete original source is preserved for checking.
