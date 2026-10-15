# 0918 calibration：中文 Beamer slides

2026-10-12 — 按读者认可的 [slide-writing skill](../../../skills/write-slides/SKILL.md) 重写。使用弧光量子 company theme 与较粗的字体；slides 保留主线、图与必要限制，讲解和 possible causes 移至配套笔记。解释为 Codex interpretation；数据来自既有实验及 recorded audit，不表示读者认可所有解释。

- [完整 PDF](0918-calibration-zh.pdf)：78 页：正文 34 页、附录 44 页（含各章节目录页）。包含全部 47 个复查案例；三页研究计划位于正文总结之后。
- [Beamer 源码](slides.tex)：中文叙述，保留 English technical terms；完整 definitions 在配套笔记。
- [讲解与背景笔记](notes.md)：按学习问题组织的解释、模型条件、definitions 与来源。
- [详细案例笔记](case-notes.md)：47 个 targets 的完整诊断、观察、未验证原因与验证方向。
- [全部案例索引](coverage.md)：每个 target、reference 及所在部分。
- [返回讨论](../note.md)；[论文与来源注释](../references.md)。

## 组织与讲述

### 配套早期工作报告 — 2026-10-13

另有 [量子控制软件的早期工作 PDF](early-control-work-zh.pdf)（正文 8 页、模型附录 1 页），使用同一 company Beamer theme、字体与 native dot navigation。介绍 QuantaCS 的波形预失真编译集成，以及 sion / sion-exper 的电极电压序列计算和 ARTIQ 输出控制；最后接续本目录的校准数据报告。第 5、6 页用完整流程图标出个人软件贡献；第 7 页展示读者提供海报中的理论电压序列与单离子输运实验图像，第 8 页接续校准报告，第 9 页为模型附录。读者随后表示先前的 15 电极数量可能记错，当前图示已去掉该计数；海报的 22 对 DC 电极设计与操作启用数量不作等同。

[可编辑源码](early-control-work.tex) · [配套解释与职责依据](early-control-work-notes.md)。运行 `bash compile.sh` 同时编译两份报告。封面沿用读者填写的报告人和编译日期；离子项目的算法与接口细节尚待代码核对，当前只介绍本人确认的软件职责。示意阶跃图为模型说明，不是实验性能结果。

### 校准报告

当前页码按 2026-10-15 的编译结果，包含各章节目录页：

| PDF 页码 | 内容 |
| --- | --- |
| 1–2 | 封面与总目录 |
| 3、12、18、29、33 | 正文章节目录 |
| 4–11 | 电路能级、器件、控制、色散读出与 I/Q 接收 |
| 13 | 器件差异、参数漂移与工作条件 |
| 14–17 | 校准实验、状态保持与读出判别 |
| 19–28 | 判断方法、八个代表案例与总结 |
| 30–32 | 已有工作、harness 视角与三阶段研究路线 |
| 34 | 理论文献 |
| 35–39 | 附录目录、两页案例导航、解释条件与数据来源 |
| 40–78 | 其余 39 个案例 |

正文八个案例可从 PDF 导航跳转；配套解释如下：

| PDF 页码 | 案例与判断重点 |
| --- | --- |
| 20 | [Resonator/006](case-notes.md#case-resonator-006)：首点与扫描窗口 |
| 21 | [Spectroscopy/008](case-notes.md#case-spectroscopy-008)：边缘特征与背景 |
| 22 | [Spectroscopy/005](case-notes.md#case-spectroscopy-005)：步长与线宽 |
| 23 | [Rabi/003](case-notes.md#case-rabi-003)：数值周期与可见振荡 |
| 24 | [Rabi/007](case-notes.md#case-rabi-007)：局部弧段与周期约束 |
| 25 | [T1/004](case-notes.md#case-t1-004)：短窗口与拟合上界 |
| 26 | [Ramsey/008](case-notes.md#case-ramsey-008)：振荡结构与包络 |
| 27 | [GMM/008](case-notes.md#case-readout-008)：名义准备与真实状态 |

研究计划强调软件工程与长期多智能体协作目标。已有工作页连接 Vibe Calibration / NVIDIA 的校准工具与流程、QUAlibrate 的模块化软件基础、SWE-agent 的模型接口研究；RouteLLM 为成本与质量路由提供参考。这些支持不等于本设想已实现或在校准任务中得到验证。

页眉使用原生 `miniframes` 圆点导航；保留各章节开始时的目录页。附录为独立 part，不增加正文导航进度。

每个案例页只讨论一个 experiment family：短标题、paired plot、任务相关的左右标注、正式图注中的 diagnostic 与必要限制，以及正文的校准判断。完整 observation、possible causes 和验证方向在 [case-notes.md](case-notes.md)；候选原因明确标为未验证 hypotheses。Reference 不等于通过 calibration certification；不同 case 通常不是 matched controlled experiment。Ramsey reference 本身也有 residual flags，案例页保留说明。

47 个案例包括既有 audit 的全部 46 个 flagged cases，以及另列的 Resonator Spectroscopy/006。并不声称这是 acquisition 所有可能问题的穷举。按 family 为 T1 3、Ramsey 8、Rabi 15、Qubit Spectroscopy 15、GMM 5、Resonator 1。

## 编译与修改

需要 XeLaTeX、latexmk、ctexbeamer、TikZ、Circuitikz 与 PGFPlots。主题、vector logo 和字体通过 repository-relative paths 复用 [company Beamer template](../../../skills/write-slides/assets/company-beamer/README.md)。中文使用 bundled Noto Sans SC Medium/Bold，英文使用 Open Sans Semibold/Bold；无需另装 system fonts。搬迁时保留仓库内 `skills/write-slides/assets/company-beamer/` 的相对位置；单独复制 slides 目录不足以编译。

在本目录运行：

```bash
bash compile.sh
```

一个命令编译两份源码：`slides.tex` 输出 `0918-calibration-zh.pdf`，`early-control-work.tex` 输出 `early-control-work-zh.pdf`。两份 PDF 均包含各自的正文与附录；辅助文件和 logs 位于忽略的 `build/`，早期工作报告使用其 `early-control-work/` 子目录。

普通排版编辑只需重编译。若修改案例解释、reference selection 或绘图，需要 Python 3、NumPy、Matplotlib，然后运行：

```bash
python3 generate_assets.py
bash compile.sh
```

默认使用本目录的 `evidence.json` 和 64 份 `data/*.csv`，不要求原始 checkout 或网络。脚本逐份核对 SHA-256 后重绘 47 份 `figures/*.pdf`，生成简洁的 `generated/*.tex`、coverage JSON / Markdown 和全部 `case-notes.md`。`notes.md` 按学习问题组织；当前页码集中维护在本 README，避免重复导航随修改失效。案例页请修改 `generate_assets.py` 后再生成；直接编辑 `generated/` 会在下次生成时被覆盖。电路使用 Circuitikz 的 capacitor / cross symbols；概念 diagrams 使用 TikZ；示意 pulse envelope 使用 PGFPlots。所有 slide visuals 都置于 Beamer `figure` 环境，包括直接绘制的 diagrams 和 columns 内的 visuals；案例图继续导入既有 Matplotlib vector PDFs。

需要从 canonical checkout 刷新快照时：

```bash
python3 generate_assets.py --source /home/gaodc/my_work/agent_control
```

刷新前检查 recorded review 的 complete status、manifest/summary hashes、全部 manifest input hashes、CSV hashes 和 audit script hash。导入器使用 recorded manifest 中的原始路径，因此搬迁 canonical checkout 后需先处理该路径依赖；便携的默认重绘不受影响。不要将刷新操作误解为重新执行物理 audit。

<a id="data-conventions"></a>

## Records 与图轴

打包保留全部 64 份 numeric CSV 的原始 bytes，包括换行形式。CSV 无 header；列号从 0 开始。`evidence.json` 记录原始相对路径、packaged path、SHA-256、metrics 和 review flags。`.gitattributes` 关闭这些 CSV 的自动换行转换。

| Family | Columns | Slides 使用方式 |
| --- | --- | --- |
| Resonator / Qubit Spectroscopy | 0 frequency (GHz), 1 phase, 2 magnitude, 3 scaled magnitude, 4 I, 5 Q | 画 column 3 / 1000；该除法只改善显示，仍为 a.u. |
| Rabi Oscillation | 0 drive-amplitude setting, 1 phase, 2 magnitude, 3 scaled magnitude, 4 I, 5 Q | 对 columns 4–5 去均值，取第一 principal direction，再除以该 projection 的 standard deviation |
| GMM Readout Clusters | 0 record index, 1–2 without-pi I/Q, 3–4 with-pi I/Q | 两组 scatter；记录顺序由 configuration labels 支持 |
| T1 Visibility | 0 delay (μs), 1–2 first P0/P1, 3–4 second P0/P1 | 画 columns 2、4；将 first/second 解释为 nominal with/no-pi **来自推断** |
| T2 Ramsey | 0 delay (μs), 1 P0, 2 P1 | 画 P1 与 recorded-fit upper/lower envelope |

### 频率与幅度扫描

0918 的 Resonator Spectroscopy 有 6 cases，扫 probe frequency；Qubit Spectroscopy 有 18 cases，扫 drive frequency；Rabi Oscillation 有 16 cases，扫 drive-amplitude setting。它们保留 frequency/amplitude setting、phase、magnitude、scaled magnitude、I、Q。

CSV 无 header；列号从 0 开始。Spectroscopy 的 0 列是 frequency (GHz)；Rabi 的 0 列是 drive-amplitude setting。两类的 1–5 列依次是 phase、magnitude、scaled magnitude、I、Q。Spectroscopy 图使用 column 3 / 1000；该除法只改善显示，仍为 a.u.，不能据此比较 absolute gain。

Rabi 图使用去均值 IQ 的第一 principal direction，除以该 record 的 standard deviation。其 sign / scale 在每份 record 中独立选择，不是 population。Figure 的 sinusoid 使用 recorded candidate frequency，只通过 linear least squares 重建 offset/cosine/sine coefficients；此前绘图时核对重建 R² 与记录值相差小于 10⁻⁶。没有新增 nonlinear frequency fit。

### 延迟与准备记录

T1 Visibility 有 6 cases；column 0 为 delay (μs)，1–2 为第一路 P0/P1，3–4 为第二路 P0/P1。图画 columns 2、4；将两路解释为 nominal with/no-pi **来自推断**。T2 Ramsey 有 8 cases；columns 0–2 为 delay、P0、P1；图画 P1 与 recorded-fit upper/lower envelope。

GMM Readout Clusters 有 10 cases；columns 0–4 为 record index、without-pi I/Q、with-pi I/Q。GMM = Gaussian Mixture Model；这里的组顺序由 configuration labels 支持。CSV = Comma-Separated Values。

六类共 64 cases、57,993 numeric rows。行的物理意义随 family 改变，不能把总行数当作 shots。文件标签“0918”不能单独确认 acquisition date。Source bytes、column mappings 与 recorded metrics 见 [evidence.json](evidence.json) 和 [README](README.md)。

### 诊断、证据与对照条件

Measurements 来自 64 份原 bytes 保留的 numeric snapshots；diagnostics 来自已完成的 recorded audit；解释是 Codex interpretation。此前制作时原记录已经核对 input、report、audit script 的 SHA-256 (Secure Hash Algorithm 256-bit)，并在固定 recorded frequency 下重建 Rabi linear coefficients、检查 R² 与记录值一致。此前扩充笔记时再次核对了 64 份 packaged CSV 的 hashes，没有重新生成曲线或执行完整 nonlinear audit。

T1 metrics fit contrast；Rabi metrics fit projected IQ；spectroscopy R² / FWHM 来自 single-Lorentzian IQ diagnostic。低 whole-window R² 不排除存在真实 narrow feature；高 R² 也不能补足 resolution。Resonator/006 仅有 descriptive review，没有 validated transfer-function fit。Shot counts、noise covariance、absolute gain 与原始 estimator provenance 未完全恢复。

Hash 一致支持输入与 recorded snapshot 的对应关系，不保证原 acquisition、model 或 causal interpretation 正确。说明文件、source annotations 与 byte-preserved data 仍是解释的一部分。

附录包含案例导航、解释条件与数据来源，其后覆盖其余 39 个 cases。全部 47 个案例的数值、reference selection 与详细解释见 [case-notes.md](case-notes.md)。Case IDs 在每个 family 内独立编号。

Ramsey 全部 cases 均有 flag，因此 reference 使用相对清晰的 002 或 006。GMM/002–005 用同为 q10 的 009；GMM/008 用同为 q12 的 007；相同 qubit 不保证所有 settings 相同。Spectroscopy 图是 magnitude，指标是 IQ diagnostic。Rabi standardized projection 不可跨 case 比较 sign / scale，也不是 population。Flag 数量不应解释为 error / failure rate。

### 示意图的解释条件

Transmon 的电路与能级图不是按比例绘制，标有 $E_J$ 的交叉符号表示约瑟夫森结。通用架构图不能用来推断原设备的线路数量、耦合器类型或实际温度；10–20 mK 是典型低温背景，并非 0918 温度测量。

两条状态依赖响应示意使用 $[1+((f-f_{r,s})/w)^2]^{-1/2}$，其中 $f_{r,s}$ 是假定的状态相关中心，$w$ 是示意宽度参数。它们只展示相同形状移频后在某个探测频率产生不同响应，不是本设备传输函数拟合，所画探测点也不表示最优读出点。实际区分度依赖复响应、噪声、时间和探测强度。

Rabi 的矩形包络同样是示意，原实验的真实包络尚未恢复。案例图复用真实记录与已有诊断，其物理含义需结合前述列定义；不能把示意图当成补充实验数据。封面的 `\today` 是编译日期，内部标签“0918”也不能单独确认采集日期。

### 指标与限制

- GMM comparison 的 balanced accuracy 来自 audit 的 held-out linear classifier，不是原始 GMM fidelity estimator。Preparation error 和 relaxation 可影响结果；没有逐 shot 的真实 state labels。
- T1 audit fit 的对象是 preparation-channel contrast；图上则显示两路 recorded P1。T1/004 接近 imposed fit upper bound，表示 lifetime 在此 window 未被确定，不能当作精确 10000 μs 的测量。
- Rabi cycle coverage、sampling、orthogonal IQ variance 和 correlated residual 是模型诊断；不能单独证明 leakage 或硬件故障。
- Single-Lorentzian 不足以描述所有 spectroscopy background/multiple features。低 whole-window R² 不排除存在真实 narrow feature；高 R² 也不能补足 frequency resolution。
- Resonator/006 只是 descriptive review，没有 validated circuit transfer-function fit。首点 spike 的 transient 与 out-of-window resonance 等解释仍需实验区分。
- Thresholds 是既有 exploratory screening policy，不是 universal physics laws、formal significance tests 或 calibration acceptance criteria。不同 runs 的 T1/T2* 不能直接用于检验 T2 ≤ 2T1。

`evidence.json` 记录 import date、review generation time、source hashes 和 policy；canonical report 为 `agent_control/output/review_0918/raw_physics/results.json`，code 为 `scripts/audit_raw_physics.py`。制作时核对既有证据，没有重新采集或执行完整 nonlinear audit。标签 `0918` 本身不能确认 acquisition date。输入/脚本 hash 一致证明该 recorded snapshot 对应关系，不保证原始 acquisition 或模型正确。

## 必要 references

复用上一级 `references/` 的两个 supporting PDFs，未重复复制：

1. P. Krantz et al., *A Quantum Engineer's Guide to Superconducting Qubits*, Applied Physics Reviews 6, 021318 (2019), [DOI](https://doi.org/10.1063/1.5089550)。本地 arXiv:1904.06560v5（2021 revision）；Fig. 1 / Eq. (16), pp. 4–5；Fig. 5, p. 15；Eqs. (92)–(94), p. 29；Fig. 22, p. 45。
2. A. Blais et al., *Circuit Quantum Electrodynamics*, Reviews of Modern Physics 93, 025005 (2021), [DOI](https://doi.org/10.1103/RevModPhys.93.025005)。本地 arXiv:2005.12667v1（2020）；Figs. 14/16, pp. 25/27；Eq. (107), p. 29；Fig. 19, p. 31。

位置按本地 PDF 页码，版本不同可能变化。沿用既有 selective consultation；2026-10-10 制作时另外重新提取并核对两篇 PDF 的 p. 29，以确认 control/dispersive models；2026-10-12 重写复用已记录的解释与出处。未作 full-paper rereading；这些论文也不定义 0918 unpublished plotting code 的 estimator。Hardware 图是 generic conceptual setup，不是恢复的 0918 wiring。

## 首次交付检查 — 2026-10-12（历史记录）

完整 PDF 已用 XeLaTeX 编译，共 68 页（正文 26 页、附录 42 页）。最终 `slides.log` 无 overflow、missing-character 或 undefined-reference warnings；通过 repository-relative theme lookup 加载时的 package-name warning 不影响输出。所有 68 页已渲染检查，并在 854 × 480 的代表页与较高分辨率 render 上检查图轴、标题、关键 diagnostic 和导航。低分辨率预览是模拟，不是实际房间 / 屏幕测量。

已验证全部 47 个唯一案例 labels、47 份 paired figures、64 份 CSV hashes、57,993 行总数、notes 中的 local links / case anchors，以及 reference selections 和完整 explanation 与旧版一致。`evidence.json`、64 份 CSV 和两篇原始 supporting PDFs 的 SHA-256 均保持不变。Rabi 固定频率重建仍通过 R² consistency assertion。上述为交付与证据对应检查，不是新增 acquisition validation。

## Navigation and figure-tools revision — 2026-10-12

“0918”是读者的内部 filing label；输出文件名、原始来源与 provenance 保留该 label，slides 的标题、正文、页脚与显示的 PDF metadata 已移除。保留读者已有的封面标题 / subtitle 与 `\today` 日期设置。正文目录与 section footer 由 shared company theme 提供；附录独立，不增加正文 section 的进度。图的数据 / 拟合未改变；仅电路符号与示意 pulse 使用对应专业 packages，导入图采用 Beamer figure 环境。配套笔记的正文页码已同步更新。

## Native dot navigation and single PDF — 2026-10-12

按读者最新选择，改用 Berlin 同款原生 `miniframes` 圆点页眉，删除自定义 bar / fraction。所有直接绘制的 visuals 与导入图均采用 `figure`，columns 内的图也一致。仅交付含附录的完整 PDF；旧 main-only PDF 和入口已移除，当前笔记链接同步更新。保留读者的 title / subtitle、`\today` 和 hardware section 名称。正文与附录页码不变；数据和案例解释未改变。

本轮重新编译并检查完整 68 页与六页 shared preview，均无 overflow / missing-character / undefined-reference warnings；核对各节首尾的原生圆点链接，以及 259 个 local note links / anchors。116 份保护文件 bytes 不变；案例笔记仅删除旧正文 PDF 链接，47 个 generated case frames 与 generator 一致。

## Native figure captions — 2026-10-13

按读者反馈修正图注：所有 figure 的描述、必要解释条件与相关出处改用环境内的 `\caption{...}`，由 shared theme 提供编号和统一格式；不再用脱离 figure 的 `\src` 小字段落代替图注。正文结论仍放在 slide body，较长讲解保留在笔记。同步修改 skill、company template 与 case generator，避免重新生成后恢复旧格式。

两份 PDF 重新编译，分别保持 68 页和 14 页；全部页面及六页 shared preview 已渲染检查，无裁切、重叠或 overfull/underfull、missing-character、undefined-reference warnings。原案例指标、解释限制与配对不变；64 份 CSV、47 份原始 plot PDFs、两篇 supporting PDFs 和 evidence JSON 的 bytes 均保持不变。校准报告保留读者已填写的报告人；早期工作报告的封面字段仍待填写。

## Calibration-agent proposal slides — 2026-10-13（历史记录；现已改写并移入正文）

按读者要求，在全部案例之后追加第 69–71 页：成本与校准质量的研究目标、多智能体的软件架构、五阶段研究路线。内容来自 [proposal](../proposal.md)，是研究计划而非已实现功能或已测得收益。保持原第 1–68 页的内容与编号；新 section 位于附录 part 内，正文目录不变。

新增 [proposal-slides.tex](proposal-slides.tex) 由主源码导入；配套解释、相关工作与讲述转场见 [notes](notes.md#calibration-agent-proposal)。只编译校准报告即可更新这三页；`bash compile.sh` 仍同时编译两份报告。

完整报告重新编译为 71 页；三页新增 slides 已渲染检查，最终 log 无 overfull/underfull、missing-character 或 undefined-reference warnings。核对原 68 页正文文字和页码（附录新增 section navigation 除外）、六个 prior-work hyperlinks、数据/图/evidence hashes 与早期工作 PDF 均保持不变。

## 叙述与研究计划改写 — 2026-10-14

根据读者认可的 plain-text 稿件压缩两份报告，并保留读者已改动的封面与研究计划位置。早期工作只讲个人职责与控制目标；调研依据留在笔记。校准正文合并重复背景，案例按频率、脉冲、状态保持、读出的顺序呈现。研究计划以 Vibe Calibration 和 NVIDIA Blueprint 为基础，突出可复用 harness 的软件工程问题，按单模型、harness、异构协作三个阶段展开。该部分是拟研究方向。

同步案例 generator、生成文本与笔记页码；统一两份报告的编译入口为 `bash compile.sh`。图注继续使用 figure 环境内的正式 caption。历史交付记录中的页码对应当时版本。

两份 PDF 重新编译为 67 页和 8 页；全部 75 页、修正后的表格与相关工作页，以及共享主题六页预览已渲染检查。最终日志无 overfull/underfull、missing-character 或 undefined-reference warnings。验证 47 个案例跳转、205 个配套本地链接和生成文本一致性；64 份 CSV、47 份底层图、两篇参考 PDF 与 evidence JSON 共 114 份保护文件与提交前基线一致。slide-writing skill validator 通过。


## IQ 与参数变化说明 — 2026-10-15（此前修订的历史记录）

正文第 8 页明确 I/Q 来自同一路输出微波的正交解调，两个分量均为实数；第 9 页新增器件间差异、随时间变化与工作条件变化的对照，解释共享校准起点与逐器件确认的关系。配套笔记补充解调推导、复数表示、实际 CSV 列的含义和漂移机制的适用范围，来源选读范围记录在上一级 `references.md`。

验证：校准 PDF 共 70 页；第 8–10 页已渲染并逐页检查，最终编译日志无 overfull/underfull、缺字或未定义引用。新增页之后的 61 页与原版文字一致（页码顺延除外）；数据、底层图、evidence、两篇参考 PDF 与早期工作 PDF 共 115 份保护文件字节保持不变。


## 学习结构与解释图更新 — 2026-10-15

将 [notes.md](notes.md) 重组为六章：电路与人造原子、控制与参数变化、微波响应与测量、校准实验、结果判断、软件研究。重复追问融入对应概念，文末保留问题导航。数据约定和制作历史集中到本 README；既有软件来源及咨询范围移至 [references.md](../references.md#calibration-software-sources)，保留日期、读者确认记录和研究假设。

幻灯片第 5 页对比 LC 与非线性电路的能级，第 6 页说明编码与低温，第 10–11 页区分接收记录、正交本振参考和复坐标，第 17 页连接积分点、重复点云与判别标签。第 13 页保留参数差异与漂移解释。保留任务开始前已加入的各章节目录页；实际基线为 76 页，本次新增两页后为 78 页，先前记录的 70 页属于更早版本。

验证：仅重编译校准报告；渲染全部 78 页检查整体布局，并以较高分辨率检查第 5、6、10、11、13、17 页。最终编译日志无 overfull/underfull、缺字或未定义引用；47 个案例目标及案例导航链接有效，Markdown 文件与锚点链接检查通过。121 个保护文件的 SHA-256 保持一致，覆盖 CSV、底层图、生成案例、参考 PDF、evidence、生成器、案例笔记、覆盖索引及早期工作 PDF。未新增实验、重跑完整数据审计或扩大文献阅读范围。

<a id="notes-production-history"></a>

## 从学习笔记迁入的制作历史

2026-10-15 — 以下保留原 notes.md 的历史记录。页数、章节号与“本轮”均指各条记录当时的版本，不作为当前导航。当前页码见本文上方报告导航。

### Implementation revision — 2026-10-12

读者指出缺少目录 / section progress、内部 label 不应出现在 slide content，并希望 figure 使用已有专业工具。本次修订采用原生 Beamer `\tableofcontents`、section navigation / page ranges；使用 Circuitikz 重画电路符号、PGFPlots 绘制示意 pulse envelope；案例图放入 Beamer `figure` 环境，继续导入既有 Matplotlib vector PDFs。数据、预处理与 recorded diagnostics 均未改变。全文的页码已按新增目录更新。

### Native dot navigation and single PDF — 2026-10-12

读者选择 Berlin 同款原生圆点导航、一份含附录的完整 PDF，以及所有 diagrams / plots 使用 `figure`。此次取代先前的 bar / fraction 与双 PDF 交付；历史修订说明保留。正文仍为第 1–26 页，附录为第 27–68 页；案例解释与 scientific caveats 不变。

### Native figure captions — 2026-10-13

读者指出图下说明应归入 figure caption。现将九个背景 figures 与全部 47 个案例对照图的描述、相关出处、指标和必要解释条件放入原生 `\caption{...}`，统一编号；正文结论和扩展讲解分别保留在 slide body 与笔记。同步修改 case generator。保留读者已填写的报告人；页码、案例配对、所有原指标及 caveats 不变。

重新编译并渲染检查全部 68 页，无裁切或重叠，最终 log 无 overfull/underfull、missing-character 或 undefined-reference warnings。CSV、原始 plot PDFs、supporting PDFs 与 evidence JSON 经 SHA-256 核对保持不变；此次仅为排版修正，没有新增数据或物理验证。


### 硬件、案例与研究依据修订 — 2026-10-14

按照读者确认的讨论扩充硬件概览为六页：恢复 Transmon 电路与能级示意，分别介绍状态依赖的谐振响应及测量链。三页研究计划增加 QUAlibrate、SWE-agent、RouteLLM 的支持，并保留 harness 与异构模型协作的研究设想。八个正文案例及 39 个附录案例补充任务相关的左右说明与校准判断；全部说明仍为 Codex interpretation，不把缺陷归因于未经验证的物理机制。保留读者对器件图 caption 与实验概览来源行的修改。

此修订仅改变叙述、示意图与版面；原数据、既有 plot PDFs、evidence JSON 与指标不变。页码以上方当前目录为准；前面的历史制作记录保留当时页码。

验证：重新编译两份报告，校准 PDF 共 69 页；渲染检查整份报告与新增页面，编译 log 无溢出、缺字或未定义引用。64 份 CSV 的 SHA-256、47 份原图及 evidence JSON 与原记录一致；47 个案例跳转与配套笔记链接检查通过。

### 理解笔记扩充 — 2026-10-14

按读者确认的讨论，改用个人学习主线组织解释，补充超导与低温、约瑟夫森非线性、控制与环境影响、校准与表征、IQ 与布居、实验原理、参数可辨识性、八个案例的判断原因、harness 与模型分工，以及备讲追问。将列定义、来源和制作记录集中到文末，保留原始诊断与历史依据。该更新不构成新实验、完整数据审计或研究设想验证。


### IQ 与参数差异、漂移解释 — 2026-10-15

根据读者追问，扩充第 5.2 节，说明同一路输出信号的正交解调、两个实数与复数表示、CSV 列的物理含义及原始处理约定的限制；第 3.4 节区分器件间差异、随时间变化与工作条件变化。正文第 8 页补充 I/Q 与虚数记号解释，第 9 页新增参数差异与漂移表格；后续正文与附录页码顺延一页。更新来源咨询记录与当前导航；既有个人文字和历史修订记录保留。

验证：校准 PDF 共 70 页；第 8–10 页已渲染并逐页检查，最终编译日志无 overfull/underfull、缺字或未定义引用。新增页之后的 61 页与原版文字一致（页码顺延除外）；数据、底层图、evidence、两篇参考 PDF 与早期工作 PDF 共 115 份保护文件字节保持不变。


## 离子输运海报补充 — 2026-10-15

按读者提供的 [Fan 等海报](../references/fan-3d-printed-surface-trap-qccd-poster.pdf)，新增早期工作报告第 7 页，对照图 7 的理论电压序列与图 8 的单离子实验图像。图注明确：100 个离散步跨越一个电极，两个亮点是同一个离子的两个轨迹端点。物理实验归团队，个人工作仍为电压序列计算与输出控制软件。读者对原先 15 电极数量表示可能记错；第 6 页改用无计数的分段电极和单次移动示意，旧描述及更正保存在配套笔记。海报单页阅读范围、元数据与数量边界见[来源注释](../references.md#fan-surface-trap-poster)。

两份 PNG 是原海报的裁剪，未重画数值曲线。使用 bundled Python 运行 `crop_transport_poster.py` 可重建，依赖 Pillow 与 Poppler。只重编译早期工作报告，校准报告保持原文件。

验证：早期工作 PDF 共 9 页，全部页面已渲染检查，第 6、7 页单独检查。最终日志无 overfull/underfull、缺字或未定义引用；任务涉及的本地文件链接有效，海报副本与原件 SHA-256 一致，193 个非任务保护文件的字节保持不变。任务开始前源码与 PDF 已有未提交且重叠的修改，故本轮保留全部工作、不自动混合提交。
