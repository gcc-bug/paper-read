# 0918 calibration：讲解与背景笔记

2026-10-12 — 依据读者认可的 slide-writing skill 重写 slides。Slides 保留主线、图与关键诊断；本笔记保存讲解、背景、模型条件和出处。内容为 **Codex interpretation**；不代表读者确认了全部解释。没有新增 acquisition、完整 nonlinear audit 或文献全文阅读。

[完整 PDF](0918-calibration-zh.pdf) · [47 个案例的详细笔记](case-notes.md) · [案例索引](coverage.md) · [构建与 provenance](README.md) · [原讨论](../note.md) · [来源注释](../references.md)

正文面向具有 Quantum Information / Computer Science 基础的听众，沿用中文叙述与 English technical terms。“0918”只作为本地 filing / provenance label，不出现在 slides 的标题、正文或页脚。封面保留读者设置的 `\today`，表示编译日期，不是 acquisition date。报告人保留待填写字段。

## 1 — 从硬件到校准判断

这份报告沿着 hardware → control/readout → measurement records → diagnostic interpretation 讲解。核心问题是：一个 calibration number 怎样从实际 pulse sequence 与 measured response 得到，又是否被数据约束？正文展示八个代表案例；完整版本保留所有 47 个复查目标。数量不是 acquisition 的 error rate，也不是所有可能问题的穷举。

## 2 — 报告目录

目录来自 Beamer 的四个正文 sections：超导量子硬件概览、校准流程与记录、从数据判断可信度、References 与来源。页眉采用 Berlin 同款的原生 `miniframes` 导航：章节名称与可点击圆点，实心圆点表示当前 frame。同一 frame 的 overlays 共用一个圆点；后续圆点表示后续 frames，不估计剩余报告分钟数。页脚保留公司、报告短标题和页码。

正文四节分别占 6、6、10、2 页。完整版本的附录是独立 Beamer part，含 42 页；不计入正文四节的进度，目录也只列正文。当前仅交付一份 68 页完整 PDF，其中前 26 页为正文。

## 3 — 校准连接控制、器件与测量记录

**Codex interpretation**：区分 device、state、signal 和 record。Transmon、resonator、coupler 是器件；$|0\rangle,|1\rangle$ 与 superposition 是 state；drive、probe、flux 是控制或探测信号；数字化 response 与 assigned population 是 records。它们的 amplitude 不是同一物理量。

理想 $X_\pi:|0\rangle\mapsto|1\rangle$ 需要实际 pulse 实现。Measurement 则通过电路 response 推断 state。0918 是六类 measurements 的集合，不是存储 qubit wavefunction 的 tensor。Slide 的箭头是概念关系，不是恢复的具体 wiring。

来源：Krantz control/readout 相关章节；既有 [calibration concepts](../../../concepts/superconducting-qubit-calibration.md)。

## 4 — Transmon 的非等间隔能级允许选择性驱动

来源模型：$H_q=4E_C\hat n^2-E_J\cos\hat\varphi$，这里省略 offset charge；$E_C=e^2/(2C_\Sigma)$，$E_J$ 是 Josephson energy，$\hat n$ 是 Cooper-pair number operator，$\hat\varphi$ 是 junction phase operator。能级差 $E_1-E_0=hf_{10}$，$h$ 为 Planck constant。

**Codex interpretation**：Josephson junction 的 nonlinear response 使 transition spacing 不同，$f_{10}\ne f_{21}$。通常用最低两个 energy eigenstates 编码 qubit；higher levels 仍存在，误占据这些 levels 称为 leakage。选择性并非自动保证：实际 pulse 的频谱、强度与持续时间仍有影响。两幅图均为非按比例的概念示意。电路使用 Circuitikz 的 capacitor 与 cross/barrier symbols；标有 $E_J$ 的 cross 表示 Josephson junction，连线和符号由该 package 生成。

来源：Krantz 本地 arXiv v5，Fig. 1、Eq. (16)，PDF pp. 4–5。

## 5 — Resonator 与 coupler 的功能不同

Readout resonator 把 qubit state 编码到 microwave response；coupler / bus resonator 参与 qubit 间 interaction。多个 readout probe frequencies 可以共享 feedline。Drive 控制单 qubit transition；flux 可用于调节 tunable qubit frequency 或 coupling。Fixed-frequency 与 tunable transmon 的线路配置可能不同。

典型 chip 位于 dilution refrigerator，原讲解给出的典型温度约 10–20 mK。这个数值是背景描述，不是 0918 的测得温度。Slide 是 generic architecture，不能据此推断原设备 wiring、coupler 类型或器件数量。

来源：Krantz Sec. II；Blais review。更完整解释见 [hardware and signals](../../../concepts/superconducting-qubit-hardware-and-signals.md)。

## 6 — 弱微波响应经过测量链变成 IQ

输入链通过 attenuation / filtering 控制到达 cold chip 的信号与热噪声；衰减通常分布在多个温度层。输出链利用 isolation 与 cold/warm amplification 保护和放大 response。Mixer 与 reference local oscillator 做 downconversion，数字化后进行 demodulation / integration，得到 in-phase 与 quadrature components，即 IQ。

Slide 为减少标签，将 mixer、digitization 与 processing 合为一组；这些仍是不同电子学步骤。AWG = Arbitrary Waveform Generator；DAC = Digital-to-Analog Converter；ADC = Analog-to-Digital Converter；FPGA = Field-Programmable Gate Array。AWG / DAC 合成 envelope；ADC / FPGA 用于采样与处理。

$I,Q$ 常用 arbitrary units，因为未恢复 absolute gain calibration。它们是测量信号的两个正交分量，不是 qubit wavefunction 的 coefficients。

来源：Blais Figs. 14、16，PDF pp. 25、27；Krantz Fig. 22，PDF p. 45。

## 7 — 四个控制量共同决定一次驱动

$V_d(t)=A(t)\cos(2\pi f_dt+\phi_d)$，$\omega=2\pi f$。Frequency $f_d$ 接近目标 $f_{10}$ 才能有效驱动目标 transition；在线性 drive regime 中，envelope strength 改变 Rabi rotation speed。Duration 决定 drive 作用多久；strength 与 duration 共同决定 rotation angle。Carrier phase $\phi_d$ 决定 transverse rotation axis。

**Codex interpretation**：强度不是 energy-level spacing。Drive frequency、readout probe frequency、混频 local oscillator 和 parametric amplifier pump 各有不同作用；不能把所有 microwave signals 都解释成用于 flip qubit 的信号。

来源：Krantz Sec. IV.D.1、Eqs. (92)–(94)，PDF p. 29；Blais Sec. V.A。

## 8 — Dispersive readout 把 state 映射到不同响应

来源模型：$H_{\mathrm{disp}}/\hbar=(\omega_r+\chi\sigma_z)a^\dagger a+(\omega_q/2)\sigma_z$。其中 $\omega_r,\omega_q$ 是 angular frequency；$a^\dagger a$ 是 photon number；$\chi$ 是 dispersive shift；$\hbar=h/(2\pi)$。采用 $\sigma_z|0\rangle=-|0\rangle$、$\sigma_z|1\rangle=+|1\rangle$ 的约定，得到 slide 上的 $\omega_r\mp\chi$。

Probe 得到 state-dependent complex response $z=I+iQ$。若选择 linear scalar response $y$，理想 two-state reference 下有 $y=y_0+(y_1-y_0)P_1$。$y_0,y_1$ 为两 state 的 reference response。$y_1>y_0$ 时 excitation 可形成 peak；相反约定可形成 dip。Magnitude / phase 一般不保持这个简单线性关系。

Resonance 是 circuit response 的性质；transmission interference 也可形成 dip。Polarity 本身不能确定 transition 方向。Dispersive approximation 有适用范围，过强 probe 可使近似失效。

来源：Blais Eq. (107)、Fig. 19，PDF pp. 29–31。通用模型不能识别 0918 unpublished plotting code 的 estimator。

## 9 — 校准通过反馈反复修正控制与读出

Resonator spectroscopy 定位 probe response；qubit spectroscopy 定位 candidate $f_{10}$；Rabi 用于估计 $\pi,\pi/2$ pulses；readout calibration 检查 preparation distributions；T1 / Ramsey 做 characterization；随后 refine / repeat 以跟踪 drift。

**Codex interpretation**：初始 spectroscopy / Rabi 可使用 averaged IQ，不要求最终 single-shot classifier。Readout calibration 依赖 approximate $\pi$ preparation；pulse calibration 又依赖 usable readout，因此需要反馈。Slide 是依赖关系图，不是恢复的 0918 acquisition 顺序。

来源：既有解释与 Krantz Figs. 5、22。

## 10 — Frequency 与 amplitude scans 定位控制参数

0918 的 Resonator Spectroscopy 有 6 cases，扫 probe frequency；Qubit Spectroscopy 有 18 cases，扫 drive frequency；Rabi Oscillation 有 16 cases，扫 drive-amplitude setting。它们保留 frequency/amplitude setting、phase、magnitude、scaled magnitude、I、Q。

CSV 无 header；列号从 0 开始。Spectroscopy 的 0 列是 frequency (GHz)；Rabi 的 0 列是 drive-amplitude setting。两类的 1–5 列依次是 phase、magnitude、scaled magnitude、I、Q。Spectroscopy 图使用 column 3 / 1000；该除法只改善显示，仍为 a.u.，不能据此比较 absolute gain。

Rabi 图使用去均值 IQ 的第一 principal direction，除以该 record 的 standard deviation。其 sign / scale 在每份 record 中独立选择，不是 population。Figure 的 sinusoid 使用 recorded candidate frequency，只通过 linear least squares 重建 offset/cosine/sine coefficients；没有新增 nonlinear frequency fit。

## 11 — Delay 与 preparation records 检查状态保持和区分

T1 Visibility 有 6 cases；column 0 为 delay (μs)，1–2 为第一路 P0/P1，3–4 为第二路 P0/P1。图画 columns 2、4；将两路解释为 nominal with/no-pi **来自推断**。T2 Ramsey 有 8 cases；columns 0–2 为 delay、P0、P1；图画 P1 与 recorded-fit upper/lower envelope。

GMM Readout Clusters 有 10 cases；columns 0–4 为 record index、without-pi I/Q、with-pi I/Q。GMM = Gaussian Mixture Model；这里的组顺序由 configuration labels 支持。CSV = Comma-Separated Values。

六类共 64 cases、57,993 numeric rows。行的物理意义随 family 改变，不能把总行数当作 shots。文件标签“0918”不能单独确认 acquisition date。Source bytes、column mappings 与 recorded metrics 见 [evidence.json](evidence.json) 和 [README](README.md)。

## 12 — Rabi calibration 用 pulse area 控制旋转角

Ideal initial $|0\rangle$、resonant drive、固定 rotation axis 与 two-level dynamics 下，$\theta=\int\Omega(t)dt$，$P_1=\sin^2(\theta/2)$。Rectangular pulse 时 $\theta=\Omega T$，$\Omega$ 是 angular Rabi frequency。Slide 的矩形 envelope 使用 PGFPlots 的 axis 与坐标曲线绘制，仍是示意；0918 的真实 envelope 未恢复。

Amplitude Rabi 固定 duration、改变 strength；Time Rabi 固定 strength、改变 duration。$\pi$ pulse 对应 $180^\circ$ state rotation；$\pi/2$ pulse 可产生等 population superposition。稳定 two-state readout 下，averaged IQ 可近似沿 reference endpoints 连线，但 magnitude / phase 一般不再是简单 sinusoid。

来源：Krantz Eqs. (92)–(94)，PDF p. 29；0918 Rabi CSV。

## 13 — T1 测衰减；Ramsey 测相位保持

T1：$|0\rangle\xrightarrow{\pi}|1\rangle\xrightarrow{t}\mathrm{readout}$，模型 $P_1(t)=B+A e^{-t/T_1}$。$A$ 是 initial contrast，$B$ 是 long-delay baseline。$t=T_1$ 时，是相对 baseline 的 excess 变为原来的 $1/e$；不是全部 P1 必然降到 $1/e$。实际 audit 拟合两路 preparation-channel contrast，不能把图上的每一路 P1 都当作该 fit 的对象。

Ramsey：$\pi/2\to t\to\pi/2\to\mathrm{readout}$。第二个 pulse 将 relative phase 转成 population contrast。单一 exponential / frequency 模型为 $P_1(t)=B+A e^{-t/T_2^*}\cos(2\pi f_Rt+\phi)$；$f_R$ 是 fringe frequency，不是 microwave carrier frequency。对照页只画 recorded-fit envelope，不是完整 oscillatory prediction。

等 population superposition $(|0\rangle+e^{i\phi}|1\rangle)/\sqrt2$ 的 amplitudes 大小是 $1/\sqrt2$，probabilities 是 $1/2$。Stationary exponential relaxation / dephasing 下，$1/T_2=1/(2T_1)+1/T_\phi$；不能将无关 runs 的 T1 与 T2* 任意代入，非 exponential dephasing 也可能破坏这个简单 rate picture。

来源：Krantz Fig. 5、Sec. III.B.2–3，PDF pp. 13–16。

## 14 — Preparation label 与真实 state、assignment 不同

Without $\pi$ 名义上 prepare $|0\rangle$；with $\pi$ 名义上 prepare $|1\rangle$。Labels 记录执行的操作，不保证每个 shot 的真实 state。Classifier 根据 measured IQ 输出 assignment 0 或 1；GMM clustering 本身不能赋予 cluster 物理 state label，需要 preparation reference。

本报告复用 recorded audit 的 held-out linear classifier：用一半 records 训练、另一半评估，再交换。$F_0=P(\mathrm{assign}\ 0\mid\mathrm{nominal\ prepare}\ 0)$，$F_1=P(\mathrm{assign}\ 1\mid\mathrm{nominal\ prepare}\ 1)$，balanced accuracy 为 $(F_0+F_1)/2$。

该 accuracy 包含 preparation、relaxation 与 measurement 的影响；不是原始 GMM fidelity estimator 的复现，也不是 isolated measurement error。Source data 没有逐 shot 的真实 state labels。

来源：recorded `audit_raw_physics.py` 的 readout diagnostic；Krantz Sec. V.C、Blais Sec. V.C.2。原图 estimator 的未解决问题保留在 [provenance question](../../../questions/0918-readout-estimator-provenance.md)。

## 15 — 先观察，再检查模型，最后提出原因

Observation 是可见的 curve、overlap、edge、scatter 等；model diagnostic 是在明确 model / preprocessing 下的 fit score、coverage、resolution 和 residual；possible cause 需要重复或干预区分。

$R^2=1-\sum_i(y_i-\hat y_i)^2/\sum_i(y_i-\bar y)^2$，即 coefficient of determination。$y_i$ 是观察、$\hat y_i$ 是 prediction、$\bar y$ 是 mean。Residual $r_i=y_i-\hat y_i$ 的相邻 correlation 表明 model 仍留下有序结构，但不能唯一识别其原因。FWHM = Full Width at Half Maximum；a.u. = arbitrary units。

本地 $R^2<0.8$ 等 thresholds 是 exploratory screening policy；不是 universal physics laws、formal significance tests 或 acceptance criteria。46 个 recorded flagged cases 加一个 Resonator/006 descriptive review，共 47 个 targets。Reference 是相对清晰的对照，不等于 calibration certification；不同 cases 通常不是 matched controlled experiments。

## 16–23 — 八个正文案例

正文按下列顺序展示。图、完整诊断、观察、未验证原因和验证方向均在详细笔记中：

| 正文页 | 案例与解释 | 核心问题 |
| --- | --- | --- |
| 16 | [T1/004](case-notes.md#case-t1-004) | Flat trace 与 fit bound |
| 17 | [GMM/008](case-notes.md#case-readout-008) | Preparation groups overlap |
| 18 | [Rabi/003](case-notes.md#case-rabi-003) | Noise-like trace 与高频 candidate |
| 19 | [Rabi/007](case-notes.md#case-rabi-007) | High fit score 与有限 cycle coverage |
| 20 | [Spectroscopy/008](case-notes.md#case-spectroscopy-008) | Scan boundary |
| 21 | [Spectroscopy/005](case-notes.md#case-spectroscopy-005) | Step 大于 candidate linewidth |
| 22 | [Ramsey/008](case-notes.md#case-ramsey-008) | Envelope / residual structure |
| 23 | [Resonator/006](case-notes.md#case-resonator-006) | First-point spike |

这些页展示 measured records 与 reused diagnostics；possible causes 移到详细笔记并标为 hypotheses。把解释移出 slide 不意味着这些解释已经被确认。

## 24 — 校准参数需要六类检查共同支持

依次确认 observable、coverage、resolution、model adequacy、preparation/readout 与 reproducibility。Rabi magnitude 不直接等于 P1；Rabi/007 没有完整 cycle；T1/004 没有 resolved decay；Spectroscopy/008 的 feature 在 boundary；Spectroscopy/005 的 step 不能分辨 candidate linewidth；Ramsey/008 留下结构；GMM/008 的 nominal groups overlap；Resonator/006 需要重测首点或改变 sweep direction。

Fit 返回数字是分析的起点。Parameter 是否被数据约束、能否用于目标 operation，应结合这些检查判断。

## 25 — 理论依据：hardware、control 与 readout

沿用既有 selective consultation，没有本次 full-paper rereading：

- P. Krantz et al., *A Quantum Engineer's Guide to Superconducting Qubits*, Applied Physics Reviews 6, 021318 (2019)，[DOI](https://doi.org/10.1063/1.5089550)。[本地 PDF](../references/krantz-quantum-engineers-guide-superconducting-qubits.pdf) 是 arXiv:1904.06560v5，2021 revision。使用 Fig. 1 / Eq. (16), pp. 4–5；Fig. 5, p. 15；Eqs. (92)–(94), p. 29；Fig. 22, p. 45。
- A. Blais et al., *Circuit Quantum Electrodynamics*, Reviews of Modern Physics 93, 025005 (2021)，[DOI](https://doi.org/10.1103/RevModPhys.93.025005)。[本地 PDF](../references/blais-circuit-quantum-electrodynamics.pdf) 是 arXiv:2005.12667v1，2020 version。使用 Figs. 14/16, pp. 25/27；Eq. (107), p. 29；Fig. 19, p. 31。

这些位置按本地 PDF 页码；版本不同可能变化。旧制作记录另说明曾重新提取两篇 p. 29 核对 control/dispersive models。本次重写复用这些已记录的解释和出处；论文不能恢复 0918 未发布 plotting code 的 estimator。

## 26 — 记录、diagnostic 与因果解释分开判断

Measurements 来自 64 份原 bytes 保留的 numeric snapshots；diagnostics 来自已完成的 recorded audit；解释是 Codex interpretation。制作时原记录已经核对 input、report、audit script 的 SHA-256 (Secure Hash Algorithm 256-bit)。本次再次核对 packaged CSV 的 hashes，而没有执行完整 nonlinear audit。Rabi 仅在固定 recorded frequency 下重建 linear coefficients，并检查 R² 与记录值一致。

T1 metrics fit contrast；Rabi metrics fit projected IQ；spectroscopy R² / FWHM 来自 single-Lorentzian IQ diagnostic。低 whole-window R² 不排除存在真实 narrow feature；高 R² 也不能补足 resolution。Resonator/006 仅有 descriptive review，没有 validated transfer-function fit。Shot counts、noise covariance、absolute gain 与原始 estimator provenance 未完全恢复。

Hash 一致支持输入与 recorded snapshot 的对应关系，不保证原 acquisition、model 或 causal interpretation 正确。说明文件、source annotations 与 byte-preserved data 仍是解释的一部分。

## 27–29 — 附录导航与对照条件

完整版本增加两页可点击导航与一页使用约定，其后覆盖其余 39 个 cases。全部 47 个案例的数值、reference selection 与详细解释见 [case-notes.md](case-notes.md)。Case IDs 在每个 family 内独立编号。

Ramsey 全部 cases 均有 flag，因此 reference 使用相对清晰的 002 或 006。GMM/002–005 用同为 q10 的 009；GMM/008 用同为 q12 的 007；相同 qubit 不保证所有 settings 相同。Spectroscopy 图是 magnitude，指标是 IQ diagnostic。Rabi standardized projection 不可跨 case 比较 sign / scale，也不是 population。Flag 数量不应解释为 error / failure rate。

## Implementation revision — 2026-10-12

读者指出缺少目录 / section progress、内部 label 不应出现在 slide content，并希望 figure 使用已有专业工具。本次修订采用原生 Beamer `\tableofcontents`、section navigation / page ranges；使用 Circuitikz 重画电路符号、PGFPlots 绘制示意 pulse envelope；案例图放入 Beamer `figure` 环境，继续导入既有 Matplotlib vector PDFs。数据、预处理与 recorded diagnostics 均未改变。全文的页码已按新增目录更新。

## Native dot navigation and single PDF — 2026-10-12

读者选择 Berlin 同款原生圆点导航、一份含附录的完整 PDF，以及所有 diagrams / plots 使用 `figure`。此次取代先前的 bar / fraction 与双 PDF 交付；历史修订说明保留。正文仍为第 1–26 页，附录为第 27–68 页；案例解释与 scientific caveats 不变。
