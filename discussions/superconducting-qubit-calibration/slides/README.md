# 0918 calibration：中文 Beamer slides

2026-10-12 — 按读者认可的 [slide-writing skill](../../../skills/write-slides/SKILL.md) 重写。使用弧光量子 company theme 与较粗的字体；slides 保留主线、图与必要限制，讲解和 possible causes 移至配套笔记。解释为 Codex interpretation；数据来自既有实验及 recorded audit，不表示读者认可所有解释。

- [正文 PDF](0918-calibration-main-zh.pdf)：26 页，适合主报告。
- [完整 PDF](0918-calibration-zh.pdf)：68 页，包含全部 47 个待复查案例。
- [Beamer 源码](slides.tex)：中文叙述，保留 English technical terms；完整 definitions 在配套笔记。
- [讲解与背景笔记](notes.md)：按正文页组织的解释、模型条件、definitions 与来源。
- [详细案例笔记](case-notes.md)：47 个 targets 的完整诊断、观察、未验证原因与验证方向。
- [全部案例索引](coverage.md)：每个 target、reference 及所在部分。
- [返回讨论](../note.md)；[论文与来源注释](../references.md)。

## 组织与讲述

正文第 1 页为封面，第 2 页为目录。第 3–8 页介绍硬件与信号；第 9–14 页说明校准流程、六类 records 与模型；第 15–24 页区分 observation / diagnostic / cause 并展示八个代表案例与判断方法；第 25–26 页为 references 和 provenance。页脚使用原生 Beamer section navigation，当前章节红色突出；fraction 与细条表示本节当前页 / 总页，不是剩余讲述时间。

完整版本第 27–28 页为可点击案例导航，第 29 页说明附录约定，第 30–68 页覆盖其余 39 个案例。正文可按约 30–40 分钟准备；这只是讲述建议，不是实测报告时长。

每个案例页只讨论一个 experiment family：短标题、较大的 paired plot、关键 diagnostic 与必要限制。完整 observation、possible causes 和验证方向在 [case-notes.md](case-notes.md)；候选原因明确标为未验证 hypotheses。Reference 不等于通过 calibration certification；不同 case 通常不是 matched controlled experiment。Ramsey reference 本身也有 residual flags，案例页保留说明。

47 个案例包括既有 audit 的全部 46 个 flagged cases，以及另列的 Resonator Spectroscopy/006。并不声称这是 acquisition 所有可能问题的穷举。按 family 为 T1 3、Ramsey 8、Rabi 15、Qubit Spectroscopy 15、GMM 5、Resonator 1。

## 编译与修改

需要 XeLaTeX、latexmk、ctexbeamer、TikZ、Circuitikz 与 PGFPlots。主题、vector logo 和字体通过 repository-relative paths 复用 [company Beamer template](../../../skills/write-slides/assets/company-beamer/README.md)。中文使用 bundled Noto Sans SC Medium/Bold，英文使用 Open Sans Semibold/Bold；无需另装 system fonts。搬迁时保留仓库内 `skills/write-slides/assets/company-beamer/` 的相对位置；单独复制 slides 目录不足以编译。

在本目录运行：

```bash
bash build.sh
```

两份输出 PDF 会更新；辅助文件和 logs 位于忽略的 `build/`。`main.tex` 定义 `MainOnly` 后加载同一份 `slides.tex`，因此正文不需要维护两份。

普通排版编辑只需重编译。若修改案例解释、reference selection 或绘图，需要 Python 3、NumPy、Matplotlib，然后运行：

```bash
python3 generate_assets.py
bash build.sh
```

默认使用本目录的 `evidence.json` 和 64 份 `data/*.csv`，不要求原始 checkout 或网络。脚本逐份核对 SHA-256 后重绘 47 份 `figures/*.pdf`，生成简洁的 `generated/*.tex`、coverage JSON / Markdown 和全部 `case-notes.md`。`notes.md` 为手写的正文讲解笔记；内容或页码改变后需同步修改。案例页请修改 `generate_assets.py` 后再生成；直接编辑 `generated/` 会在下次生成时被覆盖。电路使用 Circuitikz 的 capacitor / cross symbols；概念 diagrams 使用 TikZ；示意 pulse envelope 使用 PGFPlots。案例图通过 Beamer `figure` 环境导入既有 Matplotlib vector PDFs。

需要从 canonical checkout 刷新快照时：

```bash
python3 generate_assets.py --source /home/gaodc/my_work/agent_control
```

刷新前检查 recorded review 的 complete status、manifest/summary hashes、全部 manifest input hashes、CSV hashes 和 audit script hash。导入器使用 recorded manifest 中的原始路径，因此搬迁 canonical checkout 后需先处理该路径依赖；便携的默认重绘不受影响。不要将刷新操作误解为重新执行物理 audit。

## Records 与图轴

打包保留全部 64 份 numeric CSV 的原始 bytes，包括其换行形式，只将文件名简化为 family/case。无 header；以下列号从 **0** 开始。`evidence.json` 提供每份原始相对路径、packaged path、SHA-256、metrics 和 review flags。

`.gitattributes` 对这些 CSV 关闭自动换行转换，并允许源文件原有的行尾 CR；内容完整性以逐份 SHA-256 检查为准。

| Family | Columns | Slides 使用方式 |
| --- | --- | --- |
| Resonator / Qubit Spectroscopy | 0 frequency (GHz), 1 phase, 2 magnitude, 3 scaled magnitude, 4 I, 5 Q | 画 column 3 / 1000；该除法只改善显示，仍为 a.u. |
| Rabi Oscillation | 0 drive-amplitude setting, 1 phase, 2 magnitude, 3 scaled magnitude, 4 I, 5 Q | 对 columns 4–5 去均值，取第一 principal direction，再除以该 projection 的 standard deviation |
| GMM Readout Clusters | 0 record index, 1–2 without-pi I/Q, 3–4 with-pi I/Q | 两组 scatter；记录顺序由 configuration labels 支持 |
| T1 Visibility | 0 delay (μs), 1–2 first P0/P1, 3–4 second P0/P1 | 画 columns 2、4；将 first/second 解释为 nominal with/no-pi **来自推断** |
| T2 Ramsey | 0 delay (μs), 1 P0, 2 P1 | 画 P1 与 recorded-fit upper/lower envelope |

共 57,993 numeric rows；每行的物理意义随 family 改变，不能把总行数当作 shots。Magnitude/phase 的原始 convention 和 absolute gain calibration 未完整恢复；这些数字不是 wavefunction amplitudes。

Rabi projection 的 sign 与 scale 在每份 record 中独立选择，不能跨 case 比较其正负或大小。图中 sinusoid 使用 audit 已记录的 candidate frequency；绘图时只通过 linear least squares 重建 offset/cosine/sine coefficients，并核对重建 R² 与记录值相差小于 10⁻⁶。**没有重新做 nonlinear frequency fit，也没有获得新 calibration。**

Spectroscopy 图展示 magnitude；页内 R²/FWHM 来自 audit 的 **IQ-projection single-Lorentzian diagnostic**，不是图上 magnitude 的 fit score。Case 005 右图为局部 zoom，其完整数组仍在 data/。Ramsey 只画 recorded-fit envelope，没有把 dashed lines 当作完整 oscillatory prediction。

## 指标与限制

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

## 本次交付检查

两份 PDF 已用 XeLaTeX 编译，正文 26 页、完整版本 68 页。最终 `main.log` / `slides.log` 无 overflow、missing-character 或 undefined-reference warnings；通过 repository-relative theme lookup 加载时的 package-name warning 不影响输出。所有 68 页已渲染检查，并在 854 × 480 的代表页与较高分辨率 render 上检查图轴、标题、关键 diagnostic 和导航。低分辨率预览是模拟，不是实际房间 / 屏幕测量。

已验证全部 47 个唯一案例 labels、47 份 paired figures、64 份 CSV hashes、57,993 行总数、notes 中的 local links / case anchors，以及 reference selections 和完整 explanation 与旧版一致。`evidence.json`、64 份 CSV 和两篇原始 supporting PDFs 的 SHA-256 均保持不变。Rabi 固定频率重建仍通过 R² consistency assertion。上述为交付与证据对应检查，不是新增 acquisition validation。

## Navigation and figure-tools revision — 2026-10-12

“0918”是读者的内部 filing label；输出文件名、原始来源与 provenance 保留该 label，slides 的标题、正文、页脚与显示的 PDF metadata 已移除。保留读者已有的封面标题 / subtitle 与 `\today` 日期设置。正文目录与 section footer 由 shared company theme 提供；附录独立，不增加正文 section 的进度。图的数据 / 拟合未改变；仅电路符号与示意 pulse 使用对应专业 packages，导入图采用 Beamer figure 环境。配套笔记的正文页码已同步更新。
